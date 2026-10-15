# -*- coding: utf-8 -*-
"""Planches contact des photos de gestes (techniques) et des séries d'étapes (recettes) trouvées par etapes_scan.py.
- techniques : les candidates de etapes_scan.json["techniques"]
- recettes : les fichiers des catégories « Preparation of… » (16 au plus, dans l'ordre de la catégorie)
Les candidates sont ajoutées à candidats.json sous la clé « geste/<technique> » ou « etape/<recette> », pour que
process.py les traite comme les autres une fois choisies. Planches : planches_v2/geste_NNN.jpg et etape_NNN.jpg.
Usage : .venv/Scripts/python.exe etapes_sheets.py"""
import json, os, urllib.parse
from PIL import Image, ImageDraw, ImageFont
import fetch_candidates as F

HERE = os.path.dirname(os.path.abspath(__file__))
OUTD = os.path.join(HERE, "planches_v2"); os.makedirs(OUTD, exist_ok=True)
API = "https://commons.wikimedia.org/w/api.php?action=query&format=json"

def category_files(cat, n=16):
    u = (API + "&generator=categorymembers&gcmtype=file&gcmlimit=%d&gcmtitle=%s&prop=imageinfo&iiprop=url|size|extmetadata|mime&iiurlwidth=480"
         % (n, urllib.parse.quote(cat)))
    out = []
    for p in sorted(F.get(u).get("query", {}).get("pages", {}).values(), key=lambda p: p["title"]):
        ii = (p.get("imageinfo") or [{}])[0]; md = ii.get("extmetadata", {})
        lic = F.strip_html(md.get("LicenseShortName", {}).get("value", ""))
        if not ii.get("thumburl") or not F.ok_license(lic) or "svg" in ii.get("mime", ""): continue
        out.append({"src": "Wikimedia Commons", "title": p["title"].replace("File:", ""), "w": ii["width"], "h": ii["height"],
                    "thumb": ii["thumburl"], "full": ii["url"], "page": ii.get("descriptionurl", ""),
                    "author": F.strip_html(md.get("Artist", {}).get("value", ""))[:80], "license": lic,
                    "license_url": md.get("LicenseUrl", {}).get("value", "")})
    return out

def thumb_file(key, i): return os.path.join(F.CAND, key.replace("/", "__") + f"__{i}.jpg")

def fetch_thumbs(key, cands):
    for i, c in enumerate(cands):
        f = thumb_file(key, i)
        if not os.path.exists(f):
            try: open(f, "wb").write(F.get(c["thumb"], raw=True, tries=3))
            except Exception as e: print("vignette", key, i, str(e)[:60])

def sheets(subjects, tag, per=3, tw=180, th=135):
    font = ImageFont.truetype("arial.ttf", 17); small = ImageFont.truetype("arial.ttf", 14)
    index = {}
    for s in range(0, len(subjects), per):
        group = subjects[s:s + per]; name = f"{tag}_{s // per:03d}.jpg"
        rowh = 2 * (th + 4) + 26
        W = 8 * (tw + 4) + 8; H = len(group) * rowh + 6
        sheet = Image.new("RGB", (W, H), (245, 240, 230)); d = ImageDraw.Draw(sheet)
        for r, (key, label, cands) in enumerate(group):
            y = 4 + r * rowh; index[key] = name
            d.text((8, y), f"{r}. {key.split('/', 1)[1]}  —  {label}"[:150], fill=(150, 50, 30), font=font)
            for i in range(min(16, len(cands))):
                x = 6 + (i % 8) * (tw + 4); yy = y + 22 + (i // 8) * (th + 4)
                try:
                    im = Image.open(thumb_file(key, i)).convert("RGB"); im.thumbnail((tw, th))
                    sheet.paste(im, (x + (tw - im.width) // 2, yy + (th - im.height) // 2))
                except Exception: pass
                d.rectangle([x, yy, x + 24, yy + 20], fill=(0, 0, 0)); d.text((x + 4, yy + 2), str(i), fill=(255, 255, 255), font=small)
        sheet.save(os.path.join(OUTD, name), quality=80)
    json.dump(index, open(os.path.join(OUTD, f"{tag}_index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(tag, "planches :", (len(subjects) + per - 1) // per, flush=True)

def main():
    scan = json.load(open(os.path.join(HERE, "etapes_scan.json"), encoding="utf-8"))
    db_p = os.path.join(HERE, "candidats.json")
    db = json.load(open(db_p, encoding="utf-8"))
    gestes = []
    for tid, cands in scan.get("techniques", {}).items():
        key = f"geste/{tid}"; db[key] = cands[:16]; fetch_thumbs(key, db[key]); gestes.append((key, tid, db[key]))
    etapes = []
    for rid, cats in scan.get("recettes", {}).items():
        if not cats: continue
        key = "etape/" + rid.split("/", 1)[1]
        if key not in db:
            files = []
            for cat, _n in cats[:2]: files += category_files(cat)
            db[key] = files[:16]
        fetch_thumbs(key, db[key]); etapes.append((key, " | ".join(c for c, _ in cats), db[key]))
    json.dump(db, open(db_p, "w", encoding="utf-8"), ensure_ascii=False)
    if gestes: sheets(gestes, "geste")
    if etapes: sheets(etapes, "etape")

if __name__ == "__main__":
    main()
