# -*- coding: utf-8 -*-
"""Exporte la bible ATLAS vers les données JSON de l'application (../app/src/data).
- Référentiel d'ingrédients (Tome 3) ; recettes étalons (Tome 11) + vague 1 ; catalogue (Tome 4) ;
  règles de substitution génériques (Tome 1 §7.5, Tome 3 §3.2, §14, §16) ; imports classés.
- Vérifie chaque référence d'ingrédient comme build_tome11.py : une référence inconnue arrête l'export.
Usage : python export_app_data.py"""
import json, os, re, sys
from load_ref import parse_tome3
import recipes_data
import recipes_v1_pains, recipes_v1_sauces, recipes_v1_plats, recipes_v1_desserts  # noqa: F401 (enregistrent leurs recettes)
from recipes_data import RECIPES

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "app", "src", "data")
os.makedirs(OUT, exist_ok=True)
REF = parse_tome3(os.path.join(HERE, "BIBLE_TOME3_REFERENTIEL_INGREDIENTS.md"))

# ---------------------------------------------------------------- Tome 3 : colonne « notes / substitut »
NOTES = {}
for line in open(os.path.join(HERE, "BIBLE_TOME3_REFERENTIEL_INGREDIENTS.md"), encoding="utf-8"):
    if not line.startswith("|"): continue
    c = [x.strip() for x in line.strip().strip("|").split("|")]
    if len(c) >= 5:
        n = re.sub(r"\*\*|^✅\s*", "", c[0]).strip()
        if n in REF and c[4] and c[4] != "—": NOTES.setdefault(n, re.sub(r"\*\*", "", c[4]))

ingredients = {n: {"allergens": sorted(r["allergens"]), "maybe": sorted(r["maybe"]), "derivs": r["derivs"],
                   "dispo": r["dispo"], "section": re.sub(r"^## \d+\.\s*", "", r["section"]), "note": NOTES.get(n, "")}
               for n, r in REF.items()}

# ---------------------------------------------------------------- compléments des 11 fiches du Tome 11
EXTRA = {
 "tajine_poulet_olives": dict(cats=["fetes", "enfants"], age=4, fetes=["Ramadan / Aïd", "Repas de famille"], profil=["gras", "acide"]),
 "poulet_yassa": dict(cats=["fetes"], age=3, fetes=["Repas de famille"], profil=["acide", "epice"]),
 "dal_tadka": dict(cats=["enfants"], age=2, profil=["epice", "leger"]),
 "spaghetti_carbonara": dict(cats=["enfants"], age=3, profil=["gras"]),
 "boeuf_bourguignon": dict(cats=["fetes"], age=3, fetes=["Noël", "Repas de famille"], profil=["viande_rouge", "gras"]),
 "pad_thai": dict(cats=[], age=3, profil=["epice", "sucre"]),
 "ratatouille": dict(cats=["enfants", "zero_dechet"], age=1, profil=["leger"]),
 "baguette_24h": dict(cats=["pains"], age=4),
 "mayonnaise": dict(cats=["sauces"], age=None),
 "sauce_algerienne": dict(cats=["sauces"], age=None),
 "crepes_bretonnes": dict(cats=["pains", "enfants", "fetes"], age=3, fetes=["Chandeleur", "Anniversaire"], profil=["sucre"]),
}
for d in RECIPES:
    for k, v in EXTRA.get(d["id"], {}).items(): d.setdefault(k, v)
    if d["region"].startswith("Sauces"): d["region"] = "France › Sauces de snack (France, Belgique)"

# ---------------------------------------------------------------- vérification des références
ids = {d["id"] for d in RECIPES}
errors, gaps = [], []
def check(name, rid):
    if name is None: return
    if name.startswith("SUB:"):
        if name[4:] not in ids: errors.append(f"[{rid}] sous-recette inconnue : {name}")
        return
    if name not in REF:
        close = [k for k in REF if name.split()[0].lower() in k.lower()][:5]
        errors.append(f"[{rid}] ingrédient introuvable dans le Tome 3 : {name!r} ; proches : {close}")
for d in RECIPES:
    for qty, label, ref, w, opt in d["ing"]:
        check(ref, d["id"])
        if ref is None: gaps.append(f"{d['id']} : {label}")
    for v in d["variantes"]:
        for orig, items in v["replace"].items():
            check(orig, d["id"]); [check(i, d["id"]) for i, _ in items]
if errors:
    print("\n".join(errors)); sys.exit(1)

# ---------------------------------------------------------------- règles génériques (statut « draft » = à tester)
def rule(orig, items, sat, note):
    for i, _ in items: assert i in REF, i
    assert orig in REF, orig
    return {"replaces": orig, "items": items, "satisfies": sat, "status": "draft", "note": note}
P, A = ["pork"], ["alcohol"]
RULES = [
 rule("Lardons", [("Lardons de dinde / de volaille fumés", 1), ("Paprika fumé (pimentón)", .005)], P, "Lardons de dinde fumés + 1 pincée de paprika fumé et un trait d'huile."),
 rule("Poitrine fumée / lard fumé", [("Poitrine de dinde fumée", 1), ("Paprika fumé (pimentón)", .005)], P, "Poitrine de dinde fumée + paprika fumé."),
 rule("Bacon", [("Bacon de dinde / de bœuf", 1)], P, "Bacon de dinde ou de bœuf."),
 rule("Jambon blanc", [("Jambon de dinde / de poulet", 1)], P, "Jambon de dinde ou de poulet."),
 rule("Jambon cru (Bayonne, Parme, serrano)", [("Viande des Grisons / bresaola", 1)], P, "Viande des Grisons, bresaola ou magret séché, tranchés très finement."),
 rule("Guanciale", [("Magret de canard séché / fumé", 1), ("Huile d'olive vierge extra", .03)], P, "Magret fumé en dés + 1 c. à s. d'huile d'olive."),
 rule("Pancetta", [("Magret de canard séché / fumé", 1), ("Huile d'olive vierge extra", .03)], P, "Magret fumé ou bœuf fumé + un peu d'huile."),
 rule("Chorizo (sec/frais)", [("Chorizo de bœuf ou de volaille", 1)], P, "Chorizo de bœuf ou de volaille (paprika fumé + ail)."),
 rule("Saucisse de Toulouse", [("Saucisse de bœuf / de veau / de volaille", 1)], P, "Saucisse de bœuf, de veau ou de volaille."),
 rule("Chipolatas", [("Saucisse de bœuf / de veau / de volaille", 1)], P, "Saucisses de volaille."),
 rule("Saucisse de Strasbourg / Francfort", [("Saucisse de bœuf / de veau / de volaille", 1)], P, "Saucisses de volaille ou de bœuf."),
 rule("Knack / saucisse cocktail", [("Saucisse de bœuf / de veau / de volaille", 1)], P, "Saucisses de volaille."),
 rule("Rillettes de porc", [("Rillettes de poulet / thon / saumon", 1)], P, "Rillettes de poulet, de thon ou de saumon."),
 rule("Saindoux", [("Graisse de canard / beurre clarifié", 1)], P, "Graisse de canard ou beurre clarifié, même quantité."),
 rule("Gélatine alimentaire", [("Gélatine de bœuf / poisson, agar-agar, pectine", .33)], P, "Agar-agar : environ 1/3 de la dose, à faire bouillir 1-2 min (texture plus ferme)."),
 rule("Merguez (agneau/bœuf)", [("Saucisse de bœuf / de veau / de volaille", 1)], P, "Merguez à l'origine vérifiée (100 % bœuf/agneau, boyau de mouton) ou saucisse de bœuf."),
 rule("Bouillon cube volaille", [("Bouillon d'os maison (bœuf/volaille)", 1)], P, "Bouillon maison (recette liée) : sans graisse de porc ni exhausteur."),
 rule("Bouillon cube bœuf", [("Bouillon d'os maison (bœuf/volaille)", 1)], P, "Bouillon maison."),
 rule("Vin rouge", [("Jus de raisin / pomme (pur jus)", .67), ("Vinaigre de cidre", .06), ("Bouillon d'os maison (bœuf/volaille)", .33)], A, "Jus de raisin rouge pur jus + bouillon + vinaigre de cidre ; réduire en fin de cuisson."),
 rule("Vin blanc", [("Bouillon d'os maison (bœuf/volaille)", 1), ("Citron", .05)], A, "Bouillon + 1 c. à c. de jus de citron par 100 ml (ou verjus)."),
 rule("Bière (blonde, brune, blanche)", [("Bouillon d'os maison (bœuf/volaille)", 1), ("Vinaigre de cidre", .02)], A, "Mijotés : bouillon + trait de vinaigre ; pâte à beignets : eau gazeuse très froide."),
 rule("Cidre", [("Jus de raisin / pomme (pur jus)", 1), ("Vinaigre de cidre", .03)], A, "Jus de pomme + trait de vinaigre de cidre."),
 rule("Calvados", [("Jus de raisin / pomme (pur jus)", 2), ("Vinaigre de cidre", .05)], A, "Jus de pomme réduit de moitié + une goutte de vinaigre de cidre."),
 rule("Cognac / armagnac / brandy", [("Jus de raisin / pomme (pur jus)", 2), ("Poudre de vanille", .05)], A, "Jus de pomme ou de raisin réduit + vanille."),
 rule("Rhum ambré / blanc", [("Poudre de vanille", .1)], A, "Poudre de vanille (ou sirop + zeste d'orange)."),
 rule("Amaretto", [("Farine d'amande / poudre d'amande", .5)], A, "Poudre d'amande infusée dans le liquide chaud, puis filtrée."),
 rule("Mirin", [("Jus de raisin / pomme (pur jus)", 1), ("Vinaigre de cidre", .15), ("Sucre blanc / roux / cassonade / vergeoise", .2)], A, "Jus de raisin blanc + vinaigre de cidre + sucre (3:1:1)."),
 rule("Saké / saké de cuisine", [("Bouillon d'os maison (bœuf/volaille)", 1)], A, "Bouillon léger (ou dashi maison) + trait de vinaigre de cidre."),
 rule("Madère / marsala / xérès", [("Jus de raisin / pomme (pur jus)", 1.5)], A, "Jus de raisin réduit."),
 rule("Porto", [("Jus de raisin / pomme (pur jus)", 1.5)], A, "Jus de raisin réduit."),
 rule("Extrait de vanille liquide", [("Poudre de vanille", .1)], A, "Gousse, poudre ou pâte de vanille sans alcool."),
 rule("Kirsch / eaux-de-vie de fruits", [("Jus de raisin / pomme (pur jus)", 2)], A, "Jus de cerise réduit."),
 rule("Grand Marnier / Cointreau / triple sec", [("Orange", .5)], A, "Jus d'orange réduit + zestes."),
 rule("Eau de fleur d'oranger / de rose", [("Orange", .2)], A, "Zeste fin d'orange (ou eau florale certifiée sans alcool)."),
 rule("Sauce soja claire", [("Sauce d'huître", .7), ("Sel fin / gros sel / fleur de sel", .1)], A, "Profil Strict : sauce d'huître + pincée de sel (mollusques : allergène)."),
 rule("Moutarde de Dijon", [("Graines de moutarde", .3), ("Vinaigre de cidre", .3)], A, "Profil Strict : graines de moutarde écrasées + vinaigre de cidre."),
 rule("Moutarde à l'ancienne", [("Graines de moutarde", .5), ("Vinaigre de cidre", .3)], A, "Profil Strict : graines de moutarde + vinaigre de cidre."),
 rule("Vinaigre de vin rouge / blanc", [("Vinaigre de cidre", 1)], A, "Vinaigre de cidre."),
 rule("Vinaigre balsamique", [("Vinaigre de cidre", .7), ("Sucre blanc / roux / cassonade / vergeoise", .2)], A, "Vinaigre de cidre + un peu de sucre."),
 rule("Vinaigre de riz", [("Vinaigre de cidre", 1)], A, "Vinaigre de cidre."),
 rule("Cornichon", [("Concombre", 1), ("Vinaigre de cidre", .2)], A, "Concombre en dés + vinaigre de cidre."),
]

# ---------------------------------------------------------------- recettes -> JSON
# 12 macro-régions (Tome 1 §5.1) ; les libellés du Tome 1, du Tome 4 et des fiches sont ramenés à un identifiant
MACRO_KEYS = [("france", "France"), ("europe_sud", "Europe du Sud"), ("europe_nord", "Europe du Nord"), ("maghreb", "Maghreb"),
              ("maghreb", "Afrique du Nord"), ("afrique", "Afrique subsaharienne"), ("moyen_orient", "Moyen-Orient"),
              ("asie_sud_est", "Asie du Sud-Est"), ("asie_sud", "Asie du Sud"), ("asie_est", "Asie de l'Est"),
              ("amerique_nord", "Amérique du Nord"), ("amerique_latine", "Amérique latine"), ("oceanie", "Océanie")]
def macro_id(label):
    for k, prefix in MACRO_KEYS:
        if label.startswith(prefix): return k
    raise SystemExit(f"macro-région inconnue : {label!r}")
def strip_md(s): return re.sub(r"\*\*", "", s)
recipes = []
for d in RECIPES:
    path = [p.strip() for p in d["region"].split("›")]
    macro = macro_id(path[0])
    kind = d["kind"]
    role = ("boisson" if kind == "Boisson" else "dessert" if kind in ("Dessert", "Goûter / dessert") else "entree" if kind == "Entrée"
            else "plat" if kind == "Plat" else "autre")
    recipes.append({
        "id": d["id"], "title": d["title"], "origin": d.get("origin", ""), "regionPath": path, "macro": macro,
        "kind": kind, "role": role, "level": d["niveau"], "portions": d["portions"], "active": d["actif"], "rest": d["repos"],
        "cost": d["cost"], "equipment": d["equip"], "intro": d["intro"],
        "ingredients": [{"qty": q, "label": l, "ref": r, "weight": w, "optional": o} for q, l, r, w, o in d["ing"]],
        "steps": d["steps"], "tips": d["astuces"],
        "variants": [{"name": v["name"], "constraints": sorted(v["constraints"]), "tested": v["tested"], "note": v["note"],
                      "replace": {k: [[i, r] for i, r in it] for k, it in v["replace"].items()}} for v in d["variantes"]],
        "storage": d["conservation"], "zeroWaste": d["zero_dechet"], "drinksNoAlcohol": d["accords_sa"], "drinksAlcohol": d["accords_a"],
        "techniques": d["techniques"], "kids": d["enfants"], "age": d.get("age"), "cats": d.get("cats", []),
        "fetes": d.get("fetes", []), "profile": d.get("profil", []), "tests": d.get("tests", ""),
        "source": "Tome 11 (vague 0)" if d["id"] in EXTRA else "Tome 12 (vague 1)", "verified": "C",
    })

# ---------------------------------------------------------------- zéro déchet ingrédient par ingrédient (Tome 12 §6)
import unicodedata as _ud
from zero_dechet_data import LEFTOVERS
_rid = {r["id"] for r in recipes}
for ref, spec in LEFTOVERS.items():
    assert ref in REF, f"zéro déchet : ingrédient inconnu du Tome 3 : {ref}"
    for _, _, ideas in spec["left"]:
        for kind, _, rid in ideas:
            assert kind in ("repas", "plat", "conserver", "hors"), kind
            assert rid is None or rid in _rid, f"zéro déchet : recette inconnue {rid}"
def _n(t): return _ud.normalize("NFD", t.lower().replace("œ", "oe")).encode("ascii", "ignore").decode()
ZW_COUNT = 0
for r in recipes:
    out, seen = [], set()
    for ln in r["ingredients"]:
        ref = ln["ref"]
        if not ref or ref not in LEFTOVERS or ref in seen: continue
        spec = LEFTOVERS[ref]
        if spec["partial"] and not re.search(spec["partial"], _n(f"{ln['qty']} {ln['label']}")): continue
        seen.add(ref)
        out.append({"ref": ref, "line": f"{ln['qty']} {ln['label']}".strip(), "sold": spec["sold"],
                    "parts": [{"part": part, "keep": keep, "ideas": [{"kind": k, "text": t, "recipe": rid} for k, t, rid in ideas if rid != r["id"]]}
                              for part, keep, ideas in spec["left"]]})
    r["leftovers"] = out; ZW_COUNT += len(out)

# ---------------------------------------------------------------- Tome 4 : catalogue de titres
catalogue, macro, region = [], "", ""
T4 = os.path.join(HERE, "BIBLE_TOME4_CATALOGUE_EDITORIAL.md")
for line in open(T4, encoding="utf-8"):
    m = re.match(r"^## (\d+)\. (.+)", line)
    if m:
        n = int(m.group(1)); macro = re.sub(r"^[^\wÀ-ÿ]+", "", re.sub(r"\(.*?\)", "", m.group(2))).strip() if 3 <= n <= 14 else ""
        region = ""; continue
    m = re.match(r"^### [\d.]+ (.+)", line)
    if m: region = m.group(1).strip(); continue
    if macro and line.startswith("|"):
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 6 and c[0] not in ("Titre", "") and not set(c[0]) <= set("-: "):
            catalogue.append({"title": strip_md(c[0]), "macro": macro_id(macro), "region": region or macro, "type": c[1], "level": c[2],
                              "pork": c[3], "alcohol": c[4], "kids": c[5], "notes": strip_md(c[6]) if len(c) > 6 else ""})

# ---------------------------------------------------------------- imports classés (TikTok + sites)
IMP = os.path.join(HERE, "..", "recettes-classees")
CAT_OF = {"Repas de fêtes": "fetes", "Afrique de l'Ouest": "afrique", "Maghreb": "maghreb", "Moyen-Orient": "moyen_orient", "Asie": "asie",
          "Italie": "italie", "France": "france", "autres pays": "europe", "Amériques": "ameriques", "Street food": "street_food",
          "Pains, pâtes": "pains", "Sauces": "sauces", "Fait maison sans additifs": "fait_maison", "Desserts": "desserts", "Boissons": "boissons",
          "Techniques": "techniques", "Zéro déchet": "zero_dechet", "À vérifier": "a_verifier", "Hors cuisine": None, "Moyen-Orient": "moyen_orient"}
imports = []
for fname, source in (("tiktok_favoris_classes.md", "TikTok"), ("createurs_tiktok_classes.md", "TikTok"), ("cookingwithmorgane_classees.md", "Cooking with Morgane")):
    p = os.path.join(IMP, fname)
    if not os.path.exists(p): continue
    sec = None; subsec = ""
    for line in open(p, encoding="utf-8"):
        if line.startswith("## "):
            h = line[3:]
            sec = next((v for k, v in CAT_OF.items() if k in h), "autre") if not h.startswith(("Lire", "Synthèse")) else "skip"
            subsec = h.split(":", 1)[1].split("(")[0].strip() if source != "TikTok" and "Asie" in h and ":" in h else ""
            continue
        m = re.match(r"^- \[(.*)\]\((https://[^)]+)\)(.*)$", line.strip())
        if not m or sec in (None, "skip"): continue
        rest = m.group(3)
        if "rangée aussi" in rest: continue
        author = (re.search(r"@([\w.]+)", rest) or [None, ""])[1] if source == "TikTok" else "Cooking with Morgane"
        title = m.group(1).strip()
        if re.match(r"(?i)voir la recette", title):  # texte de lien générique sur l'index du site : titre tiré de l'adresse
            from urllib.parse import unquote
            slug = unquote(m.group(2).rsplit("/", 1)[-1].rsplit(".", 1)[0]).replace("-", " ").strip()
            title = slug[:1].upper() + slug[1:]
        if source != "TikTok":  # titre et sous-titre du site collés : « Mafé de pouletLe plat star… » → « Mafé de poulet : le plat star… »
            title = re.sub(r"(?<=[a-zà-ÿ0-9)\]])(?=[A-ZÀ-Ý][a-zà-ÿ])", " : ", title, count=1)
        imports.append({"title": title, "url": m.group(2), "source": source, "author": author, "cat": sec, "sub": subsec,
                        "pork": "🐖" in rest, "alcohol": "🍷" in rest, "fete": "🎉" in rest, "photo": "carrousel" in rest})

# ---------------------------------------------------------------- vidéos : lecture dans l'application
# TikTok : intégration officielle (tiktok.com/embed/v2/<id>) pour les vidéos ; les carrousels photo s'ouvrent dans TikTok.
# Cooking with Morgane : la vidéo YouTube de chaque recette (relevée sur sa page le 14/10/2026).
YT = {}
ytp = os.path.join(IMP, "cookingwithmorgane_videos.json")
if os.path.exists(ytp): YT = json.load(open(ytp, encoding="utf-8"))
for it in imports:
    m = re.search(r"tiktok\.com/@[^/]+/video/(\d+)", it["url"])
    it["embed"] = f"tt:{m.group(1)}" if m else (f"yt:{YT[it['url']]}" if it["url"] in YT else "")

import unicodedata
def nrm(t): return unicodedata.normalize("NFD", t.lower().replace("œ", "oe")).encode("ascii", "ignore").decode()
# Food fusion : recettes qui mélangent plusieurs traditions ou dont l'origine ne se rattache pas à un seul pays
# (catégorie demandée le 14/10/2026 ; complète la règle du Tome 1 §5.2). Motifs relus à la main sur les titres.
FUSION_IMPORTS = [
    r"feuilles? de riz", r"rice paper", r"pizza.*(tonkatsu|butter chicken|rendang|big ?mac)|(tonkatsu|butter chicken|rendang|big ?mac).*pizza",
    r"piadizza", r"couscous tiep", r"bao.*teriyaki|teriyaki.*bao", r"sans (utiliser )?(aucun )?ingredients? asiatiques?", r"los pollos", r"one piece",
    r"fusion", r"a ma facon", r"carbonara ramen|ramen carbonara|avocado carbonara", r"enroule dans de l.?aligot", r"kebab de poulet au bbq",
    r"sloppy joe hot pocket", r"flatbread with butter chicken", r"burger (en|dans).*(brioche|pate)", r"tamago sando.*(pizza|burger)",
]
FUSION_RECIPES = {"chili_con_carne": "Tex-Mex : cuisine texane née de traditions mexicaines",
                  "sauce_algerienne": "sauce de snack franco-belge aux saveurs maghrébines",
                  "sauce_samourai": "sauce de snack franco-belge (mayonnaise, ketchup, harissa)"}
for r in recipes:
    if r["id"] in FUSION_RECIPES and "fusion" not in r["cats"]:
        r["cats"].append("fusion"); r["fusionNote"] = FUSION_RECIPES[r["id"]]
for it in imports:
    if it["cat"] not in ("a_verifier",) and any(re.search(p, nrm(it["title"])) for p in FUSION_IMPORTS):
        it["from"] = it["cat"]; it["cat"] = "fusion"
print(f"food fusion : {sum(1 for i in imports if i['cat'] == 'fusion')} imports, {len(FUSION_RECIPES)} fiches")

# Vidéos existantes liées à chaque fiche : mots-clés relus à la main (titre de la vidéo, sans accents).
# « exclude » écarte les faux amis (ex. « pizza » ne doit pas ramener une pizza au porc pour la margherita).
VIDEO_KEYS = {
 "tajine_poulet_olives": (r"tajine|poulet aux olives", r"tangia|tanjia"), "poulet_yassa": (r"yassa", None), "dal_tadka": (r"\bdal\b|dhal|lentilles corail", None),
 "spaghetti_carbonara": (r"carbonara", r"ramen|asperge|avocado"), "boeuf_bourguignon": (r"bourguignon", None), "pad_thai": (r"pad tha", None),
 "ratatouille": (r"ratatouille", None), "baguette_24h": (r"baguette", r"pizza|garlic|ail"), "mayonnaise": (r"\bmayo", r"poulet mayo|algerienne|samourai|burger|salade|chou"),
 "sauce_algerienne": (r"algerienne", None), "crepes_bretonnes": (r"\bcrepes?\b", r"cake|chinois|vietnam|banh|feuillet|cheung"), "pain_cocotte": (r"no.knead|sans petriss|cocotte en fonte|pain en cocotte", r"ciabatta|focaccia"),
 "pate_pizza": (r"pate a pizza|masa de pizza|masa para|pizza sin amasar|pate magique", None), "pizza_margherita": (r"margherita|pizza napoletana", None),
 "naan": (r"\bnaans?\b", None), "pain_pita": (r"\bpita\b", r"chips|arayes"), "focaccia": (r"focaccia", r"sandwich"), "msemen": (r"msemen|msmen", None),
 "batbout": (r"batbout|chiyar", None), "galette_complete": (r"galette.*(sarrasin|complete)|sarrasin", None), "pancakes": (r"pancakes?", r"chicken"),
 "pain_de_mie": (r"pain de mie", r"tamago"), "brioche": (r"^brioche|brioche (ultra|maison|moelleuse|japonaise|facile)|brioches? soffici", r"burger|nutella|chocolat|custard|garlic|air fryer|bao|feuilles d ail|chinoise|char siu|poulet|porc"), "pate_brisee": (r"pate brisee", None),
 "chapati": (r"chapati", None), "tortillas_ble": (r"tortilla", None), "ketchup": (r"ketchup", None), "sauce_samourai": (r"samourai", None),
 "sauce_blanche": (r"sauce blanche", r"mtewem"), "sauce_burger": (r"sauce (big ?mac|burger|giant)", None), "sauce_barbecue": (r"sauce (bbq|barbecue)", None),
 "sauce_andalouse": (r"andalouse", None), "harissa": (r"harissa|puree de piment|meilleure sauce piquante", None), "pesto": (r"pesto", r"pates|spaghetti|pasta|rings"),
 "sauce_tomate": (r"sauce tomate|tomato sauce", None), "bechamel": (r"bechamel", None), "vinaigrette": (r"vinaigrette", None), "tzatziki": (r"tzatziki", None),
 "frites_maison": (r"\bfrites\b|fish ?& ?chips", r"nuggets|nouilles"), "bouillon_volaille": (r"bouillon maison|bouillon (de volaille|d os)|vs cube", None), "bouillon_legumes": (r"bouillon maison|bouillon de legumes|vs cube", None),
 "mafe_poulet": (r"\bmafe\b", None), "chorba": (r"chorba|horba", None), "salade_carottes_cumin": (r"carottes", None), "houmous": (r"houmous|hummus", None),
 "taboule_libanais": (r"taboul", None), "shakshuka": (r"chakchouka|shakshuka|ojja", None), "riz_cantonais": (r"riz cantonais|riz saute", r"pates? de riz|vermicelle"),
 "poulet_teriyaki": (r"poulet teriyaki", r"brioche|bao"), "chili_con_carne": (r"chili con carne", None), "guacamole": (r"guacamole", None),
 "accras_morue": (r"accras|akra", None), "quiche_lorraine": (r"quiche", None), "gratin_dauphinois": (r"gratin dauphinois|pommes boulangeres", None),
 "veloute_potiron": (r"potiron|potimarron|citrouille", None), "poulet_roti": (r"poulet roti", r"rillettes"), "mousse_chocolat": (r"mousse au chocolat", None),
 "meringues": (r"meringue", r"salee"), "pain_perdu": (r"pain perdu", None), "banana_bread": (r"banana bread", None), "tiramisu": (r"tiramisu", r"rochers"),
 "gateau_yaourt": (r"gateau au yaourt|gateau yaourt", None), "oranges_cannelle": (r"oranges? (a la )?cannelle", None), "riz_au_lait": (r"riz au lait", None),
 "galette_rois": (r"galette des rois", None), "bissap": (r"bissap", None), "citronnade_menthe": (r"citronnade|limonade", None), "lassi_mangue": (r"\blassi\b", None),
 "the_menthe": (r"the a la menthe|\batay\b", None), "jus_gingembre": (r"jus de gingembre|gnamakoudji|ginger (shot|juice)", None),
}
missing_keys = [r["id"] for r in recipes if r["id"] not in VIDEO_KEYS]
if missing_keys: print("⚠️ fiches sans mots-clés vidéo :", missing_keys)
VIDEOS = {}
for r in recipes:
    inc, exc = VIDEO_KEYS.get(r["id"], (None, None))
    if not inc: continue
    hits = [it for it in imports if it.get("embed") is not None and it["cat"] != "a_verifier" and re.search(inc, nrm(it["title"]))
            and not (exc and re.search(exc, nrm(it["title"])))]
    hits = list({it["url"]: it for it in hits}.values())
    hits.sort(key=lambda it: (it["source"] != "Cooking with Morgane", not it.get("embed"), it["pork"] or it["alcohol"]))
    if hits: VIDEOS[r["id"]] = [{"url": it["url"], "title": it["title"], "source": it["source"], "author": it["author"], "embed": it.get("embed", ""),
                                 "pork": it["pork"], "alcohol": it["alcohol"]} for it in hits[:8]]
for r in recipes: r["videos"] = VIDEOS.get(r["id"], [])

# une recette listée dans « fêtes » ET dans sa catégorie : on garde la catégorie et le drapeau fête
by_url = {}
for it in imports:
    if it["url"] in by_url:
        prev = by_url[it["url"]]; prev["fete"] = True
        if re.match(r"(?i)voir la recette", prev["title"]): prev["title"] = it["title"]
        if prev["cat"] == "fetes": prev.update(cat=it["cat"], sub=it["sub"])
    else:
        if it["cat"] == "fetes": it["fete"] = True
        by_url[it["url"]] = it
imports = list(by_url.values())

def dump(name, obj):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f: json.dump(obj, f, ensure_ascii=False, separators=(",", ":"))
dump("ingredients.json", ingredients); dump("recipes.json", recipes); dump("rules.json", RULES)
dump("catalogue.json", catalogue); dump("imports.json", imports)
print(f"zéro déchet : {ZW_COUNT} ingrédients entamés repérés dans {sum(1 for r in recipes if r['leftovers'])} fiches")
print(f"vidéos liées : {sum(len(v) for v in VIDEOS.values())} sur {len(VIDEOS)} fiches ; imports lisibles dans l'app : {sum(1 for i in imports if i.get('embed'))}")
print(f"ingrédients {len(ingredients)} · recettes {len(recipes)} · règles {len(RULES)} · catalogue {len(catalogue)} · imports {len(imports)}")
print(f"écarts (ingrédients hors référentiel, ref=None) : {len(gaps)}")
for g in sorted(set(x.split(' : ', 1)[1] for x in gaps)): print("  -", g)
