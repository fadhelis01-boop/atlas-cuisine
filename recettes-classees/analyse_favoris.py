# -*- coding: utf-8 -*-
"""Analyse des favoris TikTok pour en faire des fiches ATLAS (22/10/2026) : nom du plat, doublons avec le catalogue et entre
favoris, adaptation (porc structurant, alcool), popularité (enregistrements et « j'aime »), présence d'une liste
d'ingrédients dans la légende. Sortie : prive/candidats_fiches.json + un tableau lisible prive/candidats_fiches.md."""
import json, os, re, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(HERE, "..", "app", "src", "data")
DB = json.load(open(os.path.join(HERE, "prive", "legendes_tiktok.json"), encoding="utf-8"))
RECIPES = json.load(open(os.path.join(APP, "recipes.json"), encoding="utf-8"))

def norm(s):
    s = unicodedata.normalize("NFD", (s or "").lower().replace("œ", "oe"))
    return "".join(c for c in s if unicodedata.category(c) != "Mn")

STOP = set("""recette recettes facile rapide maison simple delicieux delicieuse tres super bon bonne meilleur meilleure le la les de du des un une et a au aux en pour avec sans
ma mon mes ta ton tes sa son ses ce cette ces qui que quoi ou est sont faire fait voici comment vous tu je il elle on nous petit petite grand grande vraie vrai top
express astuce astuces secret secrets ultime parfait parfaite moelleux moelleuse croustillant croustillante gourmand gourmande pourtoi viral fyp food cuisine
cooking recipe easy tiktok foryou abonne abonnez like partage commente commentaire video tuto plat plats dimanche soir midi famille enfants version""".split())

def dish(desc):
    t = re.sub(r"#\S+|@\S+", " ", desc or "")
    first = re.split(r"[\n.!?:]|ingr[ée]dients", t, flags=re.I)[0]
    words = [w for w in re.findall(r"[a-zà-ÿœ'-]+", norm(first)) if len(w) > 2 and w not in STOP]
    return " ".join(words[:6])

def tokens(s): return {w for w in re.findall(r"[a-z]+", norm(s)) if len(w) > 3 and w not in STOP}
CAT = [(r["id"], r["title"], tokens(f"{r['title']} {r.get('origin') or ''} {r['id'].replace('_', ' ')}"), r["role"]) for r in RECIPES]

PORK = re.compile(r"\b(porc|lardons?|jambon|bacon|chorizo|saucisson|pancetta|guanciale|rillettes|andouill|boudin|travers|echine|poitrine fumee|saindoux|pork|ham)\b")
ALCO = re.compile(r"\b(vin blanc|vin rouge|biere|rhum|cognac|whisky|vodka|calvados|amaretto|liqueur|champagne|porto|pastis|kirsch|alcool)\b")
HAS_ING = re.compile(r"ingr[ée]dients?|\b\d+\s?(g|gr|kg|ml|cl|l)\b|\bc\.? ?a\.? ?s\b|cuill|tasses?|\* ")

def best_match(name):
    tk = tokens(name)
    if not tk: return None, 0
    best, score = None, 0.0
    for rid, title, ctk, role in CAT:
        inter = len(tk & ctk)
        if not inter: continue
        s = inter / len(tk | ctk) + (0.25 if inter >= 2 else 0)
        if s > score: best, score = (rid, title, role), s
    return best, round(score, 2)

rows = []
for url, v in DB.items():
    if v.get("missing"): continue
    d = v.get("desc", ""); st = v.get("stats") or {}
    n = dish(d)
    m, sc = best_match(n)
    saves = int(st.get("collectCount") or 0); likes = int(st.get("diggCount") or 0); plays = int(st.get("playCount") or 0)
    rows.append({"url": url, "author": v.get("author"), "section": v.get("section", ""), "from": v.get("from"), "dish": n,
                 "match": m[0] if m else None, "match_title": m[1] if m else None, "match_score": sc,
                 "pork": bool(PORK.search(norm(d))), "alcohol": bool(ALCO.search(norm(d))), "ingredients_in_caption": bool(HAS_ING.search(norm(d))),
                 "saves": saves, "likes": likes, "plays": plays, "save_rate": round(saves / plays * 1000, 2) if plays else 0, "len": len(d)})
# doublons entre favoris : même nom de plat
by = {}
for r in rows: by.setdefault(r["dish"], []).append(r)
for k, g in by.items():
    g.sort(key=lambda r: -r["saves"])
    for i, r in enumerate(g): r["dup_rank"] = i  # 0 = la plus enregistrée des vidéos du même plat
json.dump(rows, open(os.path.join(HERE, "prive", "candidats_fiches.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
new = [r for r in rows if r["match_score"] < 0.5 and r["dup_rank"] == 0 and r["dish"]]
print(f"{len(rows)} légendes · {len([r for r in rows if r['ingredients_in_caption']])} avec ingrédients · {len(new)} plats apparemment absents d'ATLAS")
with open(os.path.join(HERE, "prive", "candidats_fiches.md"), "w", encoding="utf-8") as f:
    f.write("| plat (légende) | auteur | section | enregistrements | proche d'ATLAS | porc | alcool | ingrédients |\n|---|---|---|---|---|---|---|---|\n")
    for r in sorted(rows, key=lambda r: -r["saves"]):
        f.write(f"| {r['dish']} | @{r['author']} | {r['section'][:22]} | {r['saves']} | {r['match'] or ''} ({r['match_score']}) | {'oui' if r['pork'] else ''} | {'oui' if r['alcohol'] else ''} | {'oui' if r['ingredients_in_caption'] else ''} |\n")
