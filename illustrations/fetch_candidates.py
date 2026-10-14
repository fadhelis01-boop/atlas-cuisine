# -*- coding: utf-8 -*-
"""Rassemble des photos candidates sous licence libre réutilisable pour chaque sujet, et fabrique des planches contact.
Sources : Wikimedia Commons (API MediaWiki) et Openverse (Flickr, Wikimedia…). Licences acceptées : CC0, domaine public,
CC BY, CC BY-SA (usage commercial et modification autorisés). Refusées : NC, ND, GFDL seule, « tous droits réservés ».
Usage : python fetch_candidates.py [filtre]   (python du venv A1111 : Pillow + WebP)"""
import json, os, re, ssl, sys, time, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageDraw, ImageFont
from subjects import ALL

HERE = os.path.dirname(os.path.abspath(__file__))
CAND = os.path.join(HERE, "candidats"); os.makedirs(CAND, exist_ok=True)
SHEETS = os.path.join(HERE, "planches"); os.makedirs(SHEETS, exist_ok=True)
CTX = ssl.create_default_context(cafile=r"C:\IA\tools\combined_cacert.pem")  # interception TLS d'Avast (voir mémoire A1111)
UA = {"User-Agent": "ATLAS-cuisine-illustrations/1.0 (personal project; openly licensed images with credit)"}  # ASCII seulement : sinon 403

def get(url, raw=False, tries=6):
    for k in range(tries):
        try:
            time.sleep(0.4)  # politesse envers les API publiques
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), context=CTX, timeout=40) as r:
                b = r.read()
                return b if raw else json.loads(b)
        except Exception as e:  # noqa: BLE001
            if k == tries - 1: raise
            wait = 30 * (k + 1) if "429" in str(e) else 2 + 3 * k  # 429 : on attend vraiment
            time.sleep(wait)

def strip_html(s): return re.sub(r"<[^>]+>", "", s or "").replace("&#160;", " ").replace("&amp;", "&").strip()
def ok_license(l):
    l = (l or "").lower()
    if any(x in l for x in ("nc", "nd", "all rights")): return False
    return any(x in l for x in ("cc0", "public domain", "pdm", "cc by", "by-sa", "by ", "cc-by")) or l in ("by", "by-sa", "cc0", "pdm")

def commons(q, n=12):
    u = ("https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6&gsrlimit=%d"
         "&gsrsearch=%s&prop=imageinfo&iiprop=url|size|extmetadata|mime&iiurlwidth=480") % (n, urllib.parse.quote(q + " filetype:bitmap"))
    out = []
    pages = sorted(get(u).get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 99))
    for p in pages:
        ii = p["imageinfo"][0]; m = ii.get("extmetadata", {})
        lic = m.get("LicenseShortName", {}).get("value", "")
        if not ok_license(lic) or ii.get("mime") not in ("image/jpeg", "image/png", "image/webp"): continue
        out.append({"src": "Wikimedia Commons", "title": p["title"].replace("File:", ""), "w": ii["width"], "h": ii["height"],
                    "thumb": ii.get("thumburl"), "full": ii["url"], "page": ii.get("descriptionurl"), "license": lic,
                    "license_url": m.get("LicenseUrl", {}).get("value", ""), "author": strip_html(m.get("Artist", {}).get("value", ""))[:120]})
    return out

def openverse(q, n=12):
    u = "https://api.openverse.org/v1/images/?q=%s&license=by,by-sa,cc0,pdm&page_size=%d&mature=false" % (urllib.parse.quote(q), n)
    out = []
    try: res = get(u).get("results", [])
    except Exception: return out  # quota anonyme atteint : Commons suffit
    for x in res:
        if x.get("source") == "wikimedia": continue  # déjà couvert par Commons
        out.append({"src": f"Openverse ({x.get('source')})", "title": x.get("title") or "", "w": x.get("width") or 0, "h": x.get("height") or 0,
                    "thumb": x.get("thumbnail"), "full": x.get("url"), "page": x.get("foreign_landing_url"), "license": f"CC {x.get('license','').upper()} {x.get('license_version','')}".replace("CC CC0", "CC0").replace("CC PDM", "Domaine public").strip(),
                    "license_url": x.get("license_url", ""), "author": (x.get("creator") or "")[:120]})
    return out

def candidates(key, queries):
    def keep(c):
        if not c["thumb"]: return False
        if c["w"] and (c["w"] < 900 or c["h"] < 600): return False
        return not (c["w"] and c["h"] and not 0.7 <= c["w"] / c["h"] <= 2.0)
    tries = []
    for q in queries:  # Wikimedia exige tous les mots : on raccourcit la requête si elle ne trouve rien
        w = q.split()
        tries += [" ".join(w[:n]) for n in range(len(w), 1 if len(w) > 1 else 0, -1)]
    com = []
    for q in tries:
        com += [c for c in commons(q) if keep(c)]
        if len(com) >= 8: break
    ov = [c for c in openverse(queries[-1]) + (openverse(queries[0]) if len(queries) > 1 else []) if keep(c)]
    seen, out = set(), []
    for c in com[:6] + ov[:4] + com[6:] + ov[4:]:  # variété : 6 de Commons, 4 d'Openverse (Flickr surtout)
        if c["full"] in seen: continue
        seen.add(c["full"]); out.append(c)
    return out[:10]

def fetch_thumb(path, url):
    if os.path.exists(path): return True
    try:
        b = get(url, raw=True)
        with open(path, "wb") as f: f.write(b)
        Image.open(path).verify(); return True
    except Exception:
        if os.path.exists(path): os.remove(path)
        return False

def run(filter_=""):
    db_path = os.path.join(HERE, "candidats.json")
    db = json.load(open(db_path, encoding="utf-8")) if os.path.exists(db_path) else {}
    keys = [k for k in ALL if filter_ in k]
    todo = [k for k in keys if not db.get(k)]
    def one(k):
        try: return k, candidates(k, ALL[k])
        except Exception as e: print("échec", k, e, flush=True); return k, []
    with ThreadPoolExecutor(2) as ex:  # 2 sujets en parallèle : au-delà, Wikimedia répond 429
        for k, c in ex.map(one, todo):
            db[k] = c; print(f"{k}: {len(c)} candidates", flush=True)
            json.dump(db, open(db_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    jobs = []
    for k in keys:
        for i, c in enumerate(db.get(k, [])):
            c["file"] = os.path.join(CAND, k.replace("/", "__") + f"__{i}.jpg"); jobs.append((c["file"], c["thumb"]))
    with ThreadPoolExecutor(3) as ex: list(ex.map(lambda j: fetch_thumb(*j), jobs))
    json.dump(db, open(db_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    sheets(db, keys)

def sheets(db, keys, per=4, tw=230, th=172):
    try: font = ImageFont.truetype("arial.ttf", 18); small = ImageFont.truetype("arial.ttf", 15)
    except Exception: font = small = ImageFont.load_default()
    for s in range(0, len(keys), per):
        group = keys[s:s + per]
        W = 10 * (tw + 6) + 10; H = len(group) * (th + 44) + 10
        sheet = Image.new("RGB", (W, H), (245, 240, 230)); d = ImageDraw.Draw(sheet)
        for r, k in enumerate(group):
            y = 10 + r * (th + 44)
            d.text((10, y), k, fill=(150, 50, 30), font=font)
            for i, c in enumerate(db.get(k, [])):
                x = 10 + i * (tw + 6)
                try:
                    im = Image.open(c["file"]).convert("RGB"); im.thumbnail((tw, th))
                    sheet.paste(im, (x + (tw - im.width) // 2, y + 24 + (th - im.height) // 2))
                except Exception: pass
                d.rectangle([x, y + 24, x + 26, y + 46], fill=(0, 0, 0)); d.text((x + 7, y + 25), str(i), fill=(255, 255, 255), font=small)
        sheet.save(os.path.join(SHEETS, f"planche_{s // per:03d}.jpg"), quality=82)
    print("planches :", len(range(0, len(keys), per)))

if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else "")
