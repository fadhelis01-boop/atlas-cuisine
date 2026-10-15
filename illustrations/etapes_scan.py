# -*- coding: utf-8 -*-
"""Photos d'étapes : qu'existe-t-il vraiment sous licence libre ?
1. Recettes : catégories Wikimedia Commons du type « Preparation of X », « Making X », « Cooking X » (une série cohérente
   d'un même cuisinier, seule façon d'avoir des étapes qui se suivent), avec leur nombre de fichiers.
2. Techniques : photos de gestes (pétrir, ciseler, monter des blancs…), candidates pour illustrer chaque fiche technique.
Sortie : etapes_scan.json. Une requête par seconde (fetch_candidates.get). Usage : .venv/Scripts/python.exe etapes_scan.py"""
import json, os, re, urllib.parse
from fetch_candidates import get, commons
from subjects import ALL

HERE = os.path.dirname(os.path.abspath(__file__))
API = "https://commons.wikimedia.org/w/api.php?action=query&format=json"
STEPWORDS = re.compile(r"\b(preparation|preparing|making|production|cooking of|cooking|process|step|steps|how to|recipe)\b", re.I)

# gestes des fiches techniques : requêtes en anglais (Commons est surtout indexé en anglais)
TECH = {
    "ciseler-oignon": ["dicing onion knife", "chopped onion cutting board"], "ciseler-herbes": ["chopping parsley knife"],
    "emincer": ["julienne carrots knife", "brunoise cut vegetables"], "tenir-couteau": ["claw grip knife cutting"],
    "saisir": ["searing meat pan", "browning beef pan"], "faire-revenir": ["sauteing onions pan", "sweating onions"],
    "deglacer": ["deglazing pan wine"], "mijoter": ["stew simmering pot", "braising meat dutch oven"],
    "rotir-volaille": ["roast chicken oven tray"], "cuire-pates": ["boiling pasta pot", "spaghetti cooking water"],
    "cuire-riz": ["cooking rice pot absorption"], "emulsionner": ["making mayonnaise whisk", "mayonnaise emulsion"],
    "roux-bechamel": ["roux flour butter pan", "bechamel sauce whisk"], "reduire": ["reducing sauce pan"],
    "bouillon": ["skimming stock pot", "chicken stock pot"], "oeufs-cuissons": ["poached egg", "soft boiled egg"],
    "separer-oeuf": ["separating egg yolk", "egg whites stiff peaks"], "incorporer": ["folding egg whites batter"],
    "bain-marie": ["melting chocolate double boiler"], "pate-brisee": ["rolling pie dough", "pie crust blind baking"],
    "pate-crepes": ["crepe batter pan", "cooking crepes"], "petrir": ["kneading dough hands", "kneading bread"],
    "pointage": ["bread dough rising bowl", "proofing dough"], "faconner": ["shaping baguette dough", "shaping bread loaf"],
    "vapeur-four": ["scoring bread dough lame"], "poele-tres-chaude": ["naan cooking pan", "chapati cooking tawa"],
    "frire": ["deep frying oil pot", "frying fries oil"], "torrefier": ["toasting spices pan", "grinding spices mortar"],
    "infuser": ["hibiscus tea infusion"], "wok": ["stir frying wok"], "laquer-cuisson-peau": ["crispy skin salmon pan"],
    "pate-sucree": ["sweet pastry dough tart"], "creme-patissiere": ["pastry cream whisk", "creme patissiere"],
    "pate-a-choux": ["choux pastry dough", "piping choux pastry"], "pate-feuilletee-rapide": ["puff pastry layers folding"],
    "meringues": ["meringue stiff peaks", "piping meringue"], "creme-anglaise": ["creme anglaise spoon"],
    "creme-chantilly-ganache-montee": ["whipped cream whisk"], "biscuits-base": ["genoise sponge batter", "swiss roll rolling"],
    "caramel-sucre": ["caramel sugar pan", "making caramel"], "macarons": ["macaron batter piping", "macaronage"],
    "temperer-chocolat": ["tempering chocolate marble", "chocolate tempering"], "ganache": ["ganache chocolate cream"],
    "mouler-chocolat": ["chocolate mold bonbons"], "praline-maison": ["praline hazelnut caramel"],
    "levain-maison": ["sourdough starter jar"], "autolyse-hydratation": ["bread dough stretch and fold"],
    "pate-levee-feuilletee": ["croissant dough lamination", "rolling croissants"], "brioche-technique": ["brioche dough braiding"],
    "lever-filets": ["filleting fish knife"], "poisson-plat": ["filleting sole flatfish"], "cuissons-poisson": ["pan fried fish fillet"],
    "moules-coquillages": ["cleaning mussels", "debearding mussels"], "crevettes-calamars": ["peeling shrimp", "cleaning squid"],
    "cuisson-viande-rouge": ["steak doneness", "resting steak"], "decouper-poulet": ["cutting whole chicken pieces", "chicken butchery"],
    "basse-temperature": ["sous vide cooking"], "attendrir-viande": ["marinating meat", "brining chicken"],
    "rotir-viande-four": ["roast leg of lamb", "meat thermometer roast"], "omelette-brouilles": ["making omelette pan", "scrambled eggs pan"],
    "oeufs-temperatures": ["slow cooked egg 64"], "vapeur-papillote": ["fish en papillote", "steaming bamboo steamer"],
    "griller-barbecue": ["grilling barbecue meat"], "confire": ["duck confit fat"], "frire-tempura": ["tempura batter frying", "breading station flour egg breadcrumbs"],
    "marinades-monde": ["marinade meat bowl"], "condiments-maison": ["homemade ketchup jar", "pickled red onions jar"],
    "fumet-fond": ["fish stock bones", "veal stock roasting bones"], "presenter-une-assiette": ["food plating chef", "plating dish tweezers"],
}

def categories(q):
    u = API + "&list=search&srnamespace=14&srlimit=8&srsearch=" + urllib.parse.quote(q)
    return [x["title"] for x in get(u).get("query", {}).get("search", [])]

def count(cat):
    u = API + "&prop=categoryinfo&titles=" + urllib.parse.quote(cat)
    p = next(iter(get(u).get("query", {}).get("pages", {}).values()), {})
    return p.get("categoryinfo", {}).get("files", 0)

def main():
    out_p = os.path.join(HERE, "etapes_scan.json")
    out = json.load(open(out_p, encoding="utf-8")) if os.path.exists(out_p) else {"recettes": {}, "techniques": {}}
    rec = [(k, v) for k, v in ALL.items() if k.startswith("recette/")]
    for i, (k, qs) in enumerate(rec):
        if k in out["recettes"]: continue
        en = qs[-1]
        head = [w for w in re.findall(r"[a-z]+", en.lower()) if len(w) > 3][:2]
        found = []
        for c in categories(f"{en} preparation") + categories(f"making {en}"):
            t = c.lower()
            if STEPWORDS.search(t) and any(w in t for w in head) and c not in [f[0] for f in found]:
                found.append([c, count(c)])
        out["recettes"][k] = [f for f in found if f[1] >= 3]
        print(f"[{i+1}/{len(rec)}] {k}: {out['recettes'][k]}", flush=True)
        if i % 20 == 0: json.dump(out, open(out_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for tid, qs in TECH.items():
        if tid in out["techniques"]: continue
        cands = []
        for q in qs:
            try: cands += commons(q, 12)
            except Exception as e: print("commons", q, e)
        seen = set(); uniq = [c for c in cands if not (c["page"] in seen or seen.add(c["page"]))]
        out["techniques"][tid] = uniq[:16]
        print(f"technique {tid}: {len(uniq)} candidates", flush=True)
        json.dump(out, open(out_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(out, open(out_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("recettes avec série d'étapes :", sum(1 for v in out["recettes"].values() if v))

if __name__ == "__main__":
    main()
