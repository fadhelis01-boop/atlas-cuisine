# -*- coding: utf-8 -*-
"""Collecte des légendes complètes et des statistiques des vidéos TikTok enregistrées (favoris + comptes suivis), pour
transformer les favoris en fiches ATLAS (22/10/2026). Pages publiques uniquement, une à la fois, 3 à 4 s d'intervalle ;
arrêt net si TikTok cesse de répondre normalement (aucun contournement de sa protection). Sortie dans prive/ (non publié) :
les légendes sont le texte de leurs auteurs, elles servent à l'analyse, jamais recopiées dans l'appli.
Usage : python collecte_legendes.py   (reprend là où il s'est arrêté)"""
import json, os, random, re, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "prive", "legendes_tiktok.json")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"

def urls():
    seen, out = set(), []
    md = open(os.path.join(HERE, "tiktok_favoris_classes.md"), encoding="utf-8").read()
    section = ""
    for line in md.splitlines():
        if line.startswith("## "): section = line[3:].strip()
        m = re.search(r"\((https://www\.tiktok\.com/@[^)]+/(?:video|photo)/\d+)\)", line)
        if m and m.group(1) not in seen and not section.startswith(("Lire", "Synthèse")):
            seen.add(m.group(1)); out.append({"url": m.group(1), "from": "favoris", "section": section})
    # relevé du 22/10/2026 (compte connecté) : les favoris ajoutés depuis le 14/10, et ceux qui manquaient
    # relevés datés (compte connecté) : prive/favoris_AAAA-MM-JJ.txt, et les vidéos choisies sur les profils des créateurs
    # prive/createurs_AAAA-MM-JJ.txt (22/10/2026, 29/10/2026…)
    import glob
    for kind, frm in (("favoris", "favoris"), ("createurs", "createurs")):
        for f in sorted(glob.glob(os.path.join(HERE, "prive", f"{kind}_*.txt"))):
            day = os.path.basename(f)[len(kind) + 1:-4]
            label = f"relevé {day[8:10]}/{day[5:7]}" if kind == "favoris" else f"profil créateur {day[8:10]}/{day[5:7]}"
            for p in open(f, encoding="utf-8").read().split():
                u = "https://www.tiktok.com/" + p
                if u not in seen: seen.add(u); out.append({"url": u, "from": frm, "section": label})
    brut = json.load(open(os.path.join(HERE, "createurs_tiktok_brut.json"), encoding="utf-8"))
    for _, vids in brut.items():
        for v in vids:
            if v["url"] not in seen: seen.add(v["url"]); out.append({"url": v["url"], "from": "createurs", "section": ""})
    return out

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "fr-FR,fr;q=0.9"})
    h = urllib.request.urlopen(req, timeout=25).read().decode("utf-8", "ignore")
    m = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__"[^>]*>(.*?)</script>', h, re.S)
    if not m: return None
    d = json.loads(m.group(1))["__DEFAULT_SCOPE__"]
    it = d.get("webapp.video-detail", {}).get("itemInfo", {}).get("itemStruct", {})
    if not it: return None
    a = it.get("author", {})
    return {"desc": it.get("desc", ""), "stats": it.get("stats", {}), "author": a.get("uniqueId"), "nickname": a.get("nickname"),
            "bio": a.get("signature", ""), "bioLink": (a.get("bioLink") or {}).get("link"), "created": it.get("createTime"),
            "isPhoto": bool(it.get("imagePost"))}

def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    db = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    todo = [u for u in urls() if u["url"] not in db]
    print(len(todo), "pages à lire", flush=True)
    fails = 0
    for n, u in enumerate(todo, 1):
        try:
            r = fetch(u["url"])
        except Exception as e:
            r = None; print("erreur", u["url"], str(e)[:80], flush=True)
        if r is None:
            fails += 1
            db[u["url"]] = {"missing": True, **u}
            if fails >= 6:  # TikTok ne répond plus normalement : on s'arrête, on ne force pas
                print("arrêt : 6 pages sans données d'affilée (protection de TikTok probable)", flush=True); break
        else:
            fails = 0; db[u["url"]] = {**u, **r}
        if n % 10 == 0:
            json.dump(db, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print(f"[{n}/{len(todo)}]", flush=True)
        time.sleep(3 + random.random())
    json.dump(db, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    ok = sum(1 for v in db.values() if not v.get("missing"))
    print(f"fini : {ok} légendes lues sur {len(db)}", flush=True)

if __name__ == "__main__":
    main()
