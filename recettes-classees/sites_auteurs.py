# -*- coding: utf-8 -*-
"""Recettes des sites web des créateurs suivis sur TikTok (22/10/2026). Pour chaque site : robots.txt respecté, plan du site
(sitemap) lu pour trouver les pages de recettes, puis les données structurées schema.org « Recipe » de chaque page
(nom, ingrédients, temps, portions, note moyenne et nombre d'avis). Une requête toutes les 3 s, plafond de pages par site.
Seuls les faits sont gardés pour la sélection (pas les textes de l'auteur) ; sortie dans prive/ (non publié).
Usage : python sites_auteurs.py https://site1.fr https://site2.com …"""
import gzip, json, os, re, sys, time, urllib.parse, urllib.request, urllib.robotparser

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "prive", "recettes_sites.json")
UA = "ATLAS-recettes/1.0 (projet personnel ; lecture polie des données schema.org)"
MAX_PAGES = int(os.environ.get("ATLAS_MAX_PAGES", "250"))

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.5"})
    b = urllib.request.urlopen(req, timeout=25).read()
    if url.endswith(".gz") or b[:2] == b"\x1f\x8b": b = gzip.decompress(b)
    return b.decode("utf-8", "ignore")

def sitemap_urls(base, rp):
    found, queue, seen = [], [], set()
    try:
        robots = get(urllib.parse.urljoin(base, "/robots.txt"))
        queue += re.findall(r"(?im)^sitemap:\s*(\S+)", robots)
    except Exception: pass
    queue += [urllib.parse.urljoin(base, p) for p in ("/sitemap_index.xml", "/sitemap.xml", "/wp-sitemap.xml")]
    while queue and len(seen) < 40:
        sm = queue.pop(0)
        if sm in seen: continue
        seen.add(sm)
        try: x = get(sm); time.sleep(1.5)
        except Exception: continue
        locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", x)
        for l in locs:
            if l.endswith((".xml", ".xml.gz")):
                if re.search(r"post|recette|recipe|page-sitemap|wp-sitemap-posts", l, re.I) or "sitemap_index" in sm or "wp-sitemap.xml" in sm: queue.append(l)
            elif rp.can_fetch(UA, l): found.append(l)
    # pages probablement de recettes d'abord
    found = list(dict.fromkeys(found))
    found.sort(key=lambda u: 0 if re.search(r"recette|recipe|/\d{4}/", u, re.I) else 1)
    return found

def recipes_in(html):
    out = []
    for blob in re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', html, re.S | re.I):
        try: data = json.loads(blob.strip())
        except Exception: continue
        stack = data if isinstance(data, list) else [data]
        while stack:
            n = stack.pop()
            if isinstance(n, dict):
                t = n.get("@type"); t = t if isinstance(t, list) else [t]
                if "Recipe" in t: out.append(n)
                for k in ("@graph", "mainEntity", "itemListElement"):
                    if isinstance(n.get(k), list): stack += n[k]
                    elif isinstance(n.get(k), dict): stack.append(n[k])
            elif isinstance(n, list): stack += n
    return out

def facts(r, url, site):
    ar = r.get("aggregateRating") or {}
    def num(x):
        try: return float(str(x).replace(",", "."))
        except Exception: return None
    return {"site": site, "url": url, "name": r.get("name"), "ingredients": r.get("recipeIngredient") or [], "yield": r.get("recipeYield"),
            "prep": r.get("prepTime"), "cook": r.get("cookTime"), "total": r.get("totalTime"), "category": r.get("recipeCategory"),
            "cuisine": r.get("recipeCuisine"), "keywords": r.get("keywords"), "rating": num(ar.get("ratingValue")),
            "votes": int(num(ar.get("ratingCount") or ar.get("reviewCount")) or 0), "steps_count": len(r.get("recipeInstructions") or [])}

def main(sites):
    db = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for base in sites:
        site = urllib.parse.urlparse(base).netloc
        rp = urllib.robotparser.RobotFileParser(); rp.set_url(urllib.parse.urljoin(base, "/robots.txt"))
        try: rp.read()
        except Exception: pass
        pages = [u for u in sitemap_urls(base, rp) if u not in db][:MAX_PAGES]
        print(f"{site} : {len(pages)} pages à lire", flush=True)
        got = 0
        for i, u in enumerate(pages, 1):
            if not rp.can_fetch(UA, u): continue
            try: h = get(u)
            except Exception as e: db[u] = {"site": site, "error": str(e)[:80]}; continue
            rs = recipes_in(h)
            db[u] = facts(rs[0], u, site) if rs else {"site": site, "none": True}
            got += bool(rs)
            if i % 20 == 0: json.dump(db, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1); print(f"  [{i}/{len(pages)}] {got} recettes", flush=True)
            time.sleep(3)
        json.dump(db, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"{site} : {got} recettes lues", flush=True)

if __name__ == "__main__":
    main(sys.argv[1:])
