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
import recipes_v2_all  # noqa: F401 (vague 2, Tome 13)
from recipes_data import RECIPES
from complements_ingredients import ADD as _ADD_ING  # audit gourmet : ingrédients oubliés dans la liste
for _d in RECIPES:
    for _s in _ADD_ING.get(_d["id"], []):
        _q, _l, _r, _w = (_s.split("|") + ["", "", "", "1"])[:4]
        if not any((x[2] or "") == _r and x[1] == _l for x in _d["ing"]):
            _d["ing"] = list(_d["ing"]) + [(_q, _l, _r, int(_w.rstrip("?") or 1), _w.endswith("?"))]
assert set(_ADD_ING) <= {d["id"] for d in RECIPES}, set(_ADD_ING) - {d["id"] for d in RECIPES}
# audit gourmet §4.2 : l'acidité que chaque cuisine donne au plat (dans la recette ou à table), ou la raison de s'en passer
from complements_gout import ACIDE as _ACIDE, EXTRA as _EXTRA_G, SALADE as _SALADE, SANS_ACIDE as _SANS_ACIDE
_BYB = {d["id"]: d for d in RECIPES}
assert not (set(_ACIDE) | set(_SANS_ACIDE) | set(_EXTRA_G)) - set(_BYB), (set(_ACIDE) | set(_SANS_ACIDE)) - set(_BYB)
assert not set(_ACIDE) & set(_SANS_ACIDE)
def _addline(d, s):
    _q, _l, _r, _w = (s.split("|") + ["", "", "", "1"])[:4]
    if not any((x[2] or "") == _r and x[1] == _l for x in d["ing"]):
        d["ing"] = list(d["ing"]) + [(_q, _l, _r, int(_w.rstrip("?") or 1), _w.endswith("?"))]
for _id, (_line, _phrase) in _ACIDE.items():
    _d = _BYB[_id]; _addline(_d, _line)
    _d["acide_ref"] = _line.split("|")[2]
    for _s in _EXTRA_G.get(_id, []): _addline(_d, _s)
    if _phrase and _phrase not in _d["steps"][-1]: _d["steps"] = list(_d["steps"][:-1]) + [_d["steps"][-1].rstrip() + " " + _phrase]
for _id in _SALADE:
    if not _BYB[_id].get("side"): _BYB[_id]["side"] = "achat:Salade (laitue, batavia)"
for _id, _why in _SANS_ACIDE.items(): _BYB[_id]["sans_acide"] = _why

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
import collections as _c
_dup = [k for k, n in _c.Counter(d["id"] for d in RECIPES).items() if n > 1]
assert not _dup, f"identifiants de recettes en double : {_dup}"
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
        "fetes": d.get("fetes", []), "profile": d.get("profil", []), "tests": d.get("tests", ""), "side": d.get("side"), "sansAcide": d.get("sans_acide"), "acideAjoute": d.get("acide_ref"),
        "source": "Tome 11 (vague 0)" if d["id"] in EXTRA else ("Tome 13 (vague 2)" if d.get("vague") == 2 else "Tome 12 (vague 1)"), "verified": "C",
        # fiche écrite par ATLAS d'après une vidéo (favoris TikTok du 22/10/2026) : crédit + lien, jamais le texte de l'auteur
        **({"credit": d["credit"]} if d.get("credit") else {}),
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
sys.path.insert(0, IMP)
from hors_cuisine import is_hors_cuisine as _hors_cuisine  # liste privée (recettes-classees/prive), vide si absente
for fname, source in (("tiktok_favoris_classes.md", "TikTok"), ("createurs_tiktok_classes.md", "TikTok"), ("favoris_createurs_2026-10-22_classes.md", "TikTok"), ("favoris_createurs_2026-10-29_classes.md", "TikTok"), ("cookingwithmorgane_classees.md", "Cooking with Morgane"), ("createurs_youtube_classes.md", "YouTube"), ("ajouts_classes.md", "Ajouts")):
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
        if _hors_cuisine(m.group(2)): continue  # favori hors cuisine (liste privée) : jamais publié
        rest = m.group(3)
        if "rangée aussi" in rest: continue
        author = (re.search(r"@([\w.]+)", rest) or [None, ""])[1] if source == "TikTok" else                  ((re.search(r"▶ ([^·]+)", rest) or [None, ""])[1].strip() if source in ("YouTube", "Ajouts") else "Cooking with Morgane")
        title = m.group(1).strip()
        if re.match(r"(?i)voir la recette", title):  # texte de lien générique sur l'index du site : titre tiré de l'adresse
            from urllib.parse import unquote
            slug = unquote(m.group(2).rsplit("/", 1)[-1].rsplit(".", 1)[0]).replace("-", " ").strip()
            title = slug[:1].upper() + slug[1:]
        if source == "Cooking with Morgane":  # titre et sous-titre du site collés : « Mafé de pouletLe plat star… » → « Mafé de poulet : le plat star… »
            title = re.sub(r"(?<=[a-zà-ÿ0-9)\]])(?=[A-ZÀ-Ý][a-zà-ÿ])", " : ", title, count=1)
        imports.append({"title": title, "url": m.group(2), "source": source, "author": author, "cat": sec, "sub": subsec,
                        "pork": "🐖" in rest, "alcohol": "🍷" in rest, "fete": "🎉" in rest, "photo": "carrousel" in rest,
                        **({"lang": l} if (l := next((c for f, c in (("🇬🇧", "en"), ("🇩🇪", "de"), ("🇳🇱", "nl")) if f in rest), "")) else {})})

imports = list({it["url"]: it for it in reversed(imports)}.values())[::-1]  # une vidéo relevée deux fois (favori + profil) : la première rubrique gagne
# ---------------------------------------------------------------- vidéos : lecture dans l'application
# TikTok : intégration officielle (tiktok.com/embed/v2/<id>) pour les vidéos ; les carrousels photo s'ouvrent dans TikTok.
# Cooking with Morgane : la vidéo YouTube de chaque recette (relevée sur sa page le 14/10/2026).
YT = {}
ytp = os.path.join(IMP, "cookingwithmorgane_videos.json")
if os.path.exists(ytp): YT = json.load(open(ytp, encoding="utf-8"))
for it in imports:
    m = re.search(r"tiktok\.com/@[^/]+/video/(\d+)", it["url"])
    ys = re.search(r"youtube\.com/shorts/([\w-]{11})", it["url"]); yw = re.search(r"youtube\.com/watch\?v=([\w-]{11})", it["url"])
    it["embed"] = f"tt:{m.group(1)}" if m else f"ys:{ys.group(1)}" if ys else f"yt:{yw.group(1)}" if yw else (f"yt:{YT[it['url']]}" if it["url"] in YT else "")

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
# vague 2 : quelques plats au nom court ou multiple, relus à la main
VIDEO_KEYS.update({"pho_boeuf": (r"\bpho\b", r"bun bo|ga\b"), "bo_bun": (r"\bbo bun\b|\bbun bo nam bo\b", None), "ramen_shoyu": (r"\bramen\b", r"burger|tsukemen"),
                   "nems_poulet": (r"\bnems?\b", None), "bibimbap": (r"\bbibimbap\b", None), "tom_kha_kai": (r"\btom kha\b", None), "laksa": (r"\blaksa\b", None),
                   "falafels": (r"\bfalafels?\b", None), "butter_chicken": (r"butter chicken|poulet au beurre|murgh makhani", None), "biryani_poulet": (r"\bbiryani\b", None),
                   "mafe_boeuf": (r"\bmafe\b", None), "ndole": (r"\bndole\b", None), "kimchi_maison": (r"\bkimchi\b", r"riz|fried rice|ramen|jjigae|nouilles"),
                   "okonomiyaki": (r"\bokonomiyaki\b", None), "katsu_poulet": (r"\bkatsu\b", r"sando|don\b"), "char_siu_poulet": (r"char siu", None)})
# vague 2 : pas de mots-clés relus un à un ; on cherche le nom exact du plat (avant la parenthèse) dans le titre de la vidéo
for r in recipes:
    if r["id"] not in VIDEO_KEYS:
        words = nrm(re.split(r" \(| :| ,", r["title"])[0]).replace("'", " ").split()
        stop = {"a", "au", "aux", "de", "du", "des", "la", "le", "les", "en", "et", "l", "d"}
        core = words[:2]
        while len(core) < len(words) and core[-1] in stop: core = words[:len(core) + 1]  # « soupe a l oignon »
        name = " ".join(core)
        alts = [name] if len(name) >= 5 else []
        on = nrm(re.split(r" \(|,", r["origin"])[0]).replace("'", " ").strip()  # nom d'origine (« ceebu jen », « tartiflette »)
        if on and on != name and 4 <= len(on) <= 40 and len(on.split()) <= 4: alts.append(on)
        if alts: VIDEO_KEYS[r["id"]] = ("|".join(r"\b" + re.escape(a).replace(r"\ ", r"\W+") + r"\b" for a in alts), None)
        # repli : le premier mot seul quand il désigne un plat précis (tajine, gyoza, bibimbap…), jamais un mot générique
        GENERIC = {"soupe", "salade", "poulet", "tarte", "gateau", "gateaux", "sauce", "riz", "pain", "pains", "pates", "creme", "mousse", "gratin", "boeuf", "agneau",
                   "poisson", "crevettes", "nouilles", "curry", "brochettes", "beignets", "galette", "galettes", "crepes", "cookies", "muffins", "glace", "jus", "the",
                   "cafe", "chocolat", "pommes", "legumes", "oeufs", "oeuf", "filet", "cote", "pave", "roti", "bouillon", "marinade", "petits", "petites", "mini", "pate",
                   "lait", "sirop", "fondant", "biscuits", "veloute", "chips", "compote", "puree", "quiche", "tartines", "sandwich", "boulettes", "saucisses", "cake",
                   "bowl", "porc", "canard", "lapin", "dinde", "saumon", "thon", "cabillaud", "moules", "huile", "vinaigrette", "smoothie", "limonade", "punch", "bonbons",
                   "truffes", "tablette", "sucettes", "fruits", "salade", "carottes", "ragout", "spaghetti", "fondue", "pickles", "macarons", "risotto", "lasagnes", "tagliatelles", "biscuit", "flan", "beignet", "pancakes", "omelette", "frites", "wraps", "tacos", "haricots", "lentilles", "pois", "chou", "champignons", "aubergines", "courgettes"}
        first = words[0] if words else ""
        if len(first) >= 4 and first not in GENERIC: VIDEO_KEYS[r["id"] + "#large"] = (r"\b" + re.escape(first) + r"s?\b", None)
VIDEOS = {}
for r in recipes:
    inc, exc = VIDEO_KEYS.get(r["id"], (None, None))
    if not inc: continue
    def find(rx): return [it for it in imports if it.get("embed") is not None and it["cat"] != "a_verifier" and re.search(rx, nrm(it["title"]))
                          and not (exc and re.search(exc, nrm(it["title"])))]
    hits = find(inc)
    if not hits and (r["id"] + "#large") in VIDEO_KEYS: hits = find(VIDEO_KEYS[r["id"] + "#large"][0])
    hits = list({it["url"]: it for it in hits}.values())
    hits.sort(key=lambda it: (it["source"] != "Cooking with Morgane", not it.get("embed"), it["pork"] or it["alcohol"]))
    if hits: VIDEOS[r["id"]] = [{"url": it["url"], "title": it["title"], "source": it["source"], "author": it["author"], "embed": it.get("embed", ""),
                                 "pork": it["pork"], "alcohol": it["alcohol"]} for it in hits[:8]]
# Favoris TikTok du 22/10/2026 : la vidéo d'origine d'une fiche créditée passe en tête, puis les vidéos d'un même plat
# relevées à la main (videos_favoris.py), puis celles trouvées par mots-clés. Huit au plus.
from videos_favoris import EN_PLUS as _EN_PLUS
_IMP_BY_URL = {it["url"]: it for it in imports}
assert not set(_EN_PLUS) - {r["id"] for r in recipes}, set(_EN_PLUS) - {r["id"] for r in recipes}
def _vid(url, author=None, credited=False):
    it = _IMP_BY_URL.get(url)
    m = re.search(r"tiktok\.com/@([\w.]+)/video/(\d+)", url)
    return {"url": url, "title": it["title"] if it else "Vidéo d'origine", "source": "TikTok", "author": (author or (it or {}).get("author") or m.group(1)).lstrip("@"),
            "embed": (it or {}).get("embed") or f"tt:{m.group(2)}", "pork": False if credited else bool(it and it["pork"]), "alcohol": False if credited else bool(it and it["alcohol"])}
for r in recipes:
    first = [_vid(c["url"], c["author"], True) for c in r.get("credit") or []] + [_vid(u) for u in _EN_PLUS.get(r["id"], [])]
    if first:
        seen = {v["url"] for v in first}
        VIDEOS[r["id"]] = (first + [x for x in VIDEOS.get(r["id"], []) if x["url"] not in seen])[:8]
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
# ---------------------------------------------------------------- dictionnaire illustré + saisons (Tome 13 §8-9)
import sys as _sys
_sys.path.insert(0, os.path.join(HERE, "..", "illustrations"))
from dictionnaire_data import DICO, ALIAS
from dico_subjects import slug as _slug
def months(spec):
    if not spec: return []
    a, b = (int(x) for x in spec.split("-"))
    return [((a - 1 + i) % 12) + 1 for i in range(((b - a) % 12) + 1)]
dico = {}
for n in ingredients:
    tgt = ALIAS.get(n, n)
    q, what, use, season = DICO[tgt]
    ingredients[n]["slug"] = _slug(tgt)
    ingredients[n]["season"] = months(season)
    if n == tgt:
        dico[_slug(n)] = {"name": n, "section": ingredients[n]["section"], "what": what, "use": use, "season": months(season),
                          "aliases": sorted(a for a, b in ALIAS.items() if b == n)}
used = {}
for r in recipes:
    for ln in r["ingredients"]:
        if ln["ref"] and not ln["ref"].startswith("SUB:"):
            used.setdefault(ingredients[ln["ref"]]["slug"], set()).add(r["id"])
for k, v in dico.items(): v["recipes"] = sorted(used.get(k, []))
print(f"dictionnaire : {len(dico)} fiches, {sum(1 for v in dico.values() if v['season'])} avec saison, {sum(1 for v in dico.values() if v['recipes'])} utilisées dans les recettes")
dump("dico.json", dico)
# chargés à la demande par l'application (fiche recette) : les restes zéro déchet ; le texte « tests » est le même partout
LEFT = {r["id"]: r.pop("leftovers") for r in recipes}
for r in recipes: r.pop("tests", None)
dump("leftovers.json", LEFT)
# ---------------------------------------------------------------- âge des enfants ↔ piment (audit famille 2026-10-16)
# Une fiche épicée marquée « dès 1 à 5 ans » doit dire comment l'adoucir. Quand le piment est dans la base (pâte, marinade,
# condiment fermenté), il ne se retire pas : l'âge passe à 6 ans. Sinon, on précise de le servir à part.
_ADOUCI = re.compile(r"sans (le )?piment|piment a part|a part pour les adultes|version douce|doux pour les enfants|sans epices fortes|sans garam")
_BASE_PIQUANTE = re.compile(r"harissa|berbere|gochujang|gochugaru|pate de curry|sambal|marinade_jerk|poivre du sichuan|huile pimentee|piments ancho|scotch bonnet|piment antillais|sriracha|pate de piment|nokoss|tandoori")
def _n(t): return _ud.normalize("NFD", t.lower()).encode("ascii", "ignore").decode()
_ages = [0, 0]
for r in recipes:
    if "epice" not in r.get("profile", []) or r.get("age") is None or r["age"] > 5 or _ADOUCI.search(_n(r.get("kids") or "")):
        continue
    refs = _n(" ".join(l.get("ref") or "" for l in r["ingredients"] if not l.get("optional")))
    if _BASE_PIQUANTE.search(refs):
        r["age"] = 6; _ages[0] += 1
        r["kids"] = "✓ dès 6 ans : le piment est dans la base (pâte, marinade ou condiment), il ne se retire pas. Pour les plus petits, choisis un plat doux."
    else:
        _ages[1] += 1
        r["kids"] = (r.get("kids") or "").rstrip(" .") + ". Pour les plus petits : piment à part, ajouté seulement dans les assiettes des grands."
print(f"âges ↔ piment : {_ages[0]} fiches passées à 6 ans, {_ages[1]} avec le piment à part")

# ---------------------------------------------------------------- accompagnements (audit gourmet 2026-10-21, recommandation 4)
# Chaque plat qui se sert « avec du riz, de la polenta, du pain… » reçoit un accompagnement relié (une fiche, ou un produit à
# acheter), ajouté aux courses. Champ explicite `side` d'abord ; sinon déduit de la fin des étapes, si l'ingrédient manque.
_SIDES = [(r"\bpolenta\b", "polenta_cremeuse", "Polenta"), (r"\bpuree\b", "puree_maison", "Pomme de terre"), (r"\bfrites\b", "frites_maison", "Pomme de terre"),
          (r"\bsemoule\b|\bcouscous\b", "semoule_nature", "Semoule de couscous"), (r"\briz\b", "riz_nature", "Riz"),
          (r"\bnaan\b", "naan", "Farine"), (r"\bpates\b|tagliatelle|macaroni", "pates_nature", "Pâtes"),
          (r"\bpommes? vapeur\b", "pommes_vapeur", "Pomme de terre"), (r"\bpain\b|baguette", "achat:Baguette tradition", "Pain"), (r"\btortillas?\b", "achat:Tortillas de blé", "Tortillas")]
_ids = {r["id"] for r in recipes}
_side_n = [0, 0]
for r in recipes:
    if r["role"] != "plat": r["side"] = None; continue
    if r.get("side"): _side_n[0] += 1; continue
    tail = _n(" ".join(r["steps"][-2:]))
    have = _n(" ".join((l.get("ref") or "") + " " + l.get("label", "") for l in r["ingredients"]))
    for rx, sid, key in _SIDES:
        if re.search(rx, tail) and _n(key).split()[0] not in have and (sid.startswith("achat:") or sid in _ids) and sid != r["id"]:
            r["side"] = sid; _side_n[1] += 1; break
    else:
        r["side"] = None
for r in recipes:
    s_ = r.get("side")
    assert not s_ or s_.startswith("achat:") or s_ in _ids, f"accompagnement inconnu : {r['id']} → {s_}"
    if s_ and s_.startswith("achat:"): assert s_[6:] in REF, f"produit d'accompagnement hors Tome 3 : {s_}"
print(f"accompagnements : {_side_n[0]} indiqués, {_side_n[1]} déduits des étapes")
# protéines par part (estimation, accompagnement compris) : repère d'équilibre de la fiche
from proteines import per_portion as _prot
_BYA = {r["id"]: r for r in recipes}
for r in recipes:
    # à la pièce (empanadas, tamales, mini-pizzas : plus de 8 « parts »), une valeur par part tromperait
    if r["role"] == "plat": r["prot"] = round(_prot(r, _BYA, lambda ref: ingredients.get(ref, {}).get("section", ""))) if r["portions"] <= 8 else None
_pl = [r["prot"] for r in recipes if r["role"] == "plat" and r["prot"] is not None]
print(f"protéines par part : médiane {sorted(_pl)[len(_pl) // 2]} g · moins de 15 g : {sum(p < 15 for p in _pl)} plats sur {len(_pl)}")

# ---------------------------------------------------------------- vidéos : la liste complète à la demande (audit famille, poids au démarrage)
# recipes.json garde une seule vidéo (bouton « Voir la vidéo », filtre « avec vidéo ») et le nombre total.
VIDS = {}
for r in recipes:
    full = r.get("videos") or []
    if full:
        VIDS[r["id"]] = full
        first = next((v for v in full if v.get("embed")), full[0])
        r["videos"] = [first]
    r["videoCount"] = len(full)
dump("recipe_videos.json", VIDS)
# Démarrage léger (audit dév/UX 2026-10-21 §2.1) : l'index garde ce qu'il faut aux cartes, à la recherche, au moteur et au
# planificateur ; le détail d'une fiche (étapes, introduction, vidéos, conseils, matériel, conservation) part dans un second
# fichier, lu juste après le premier affichage (et tout de suite par les écrans qui en ont besoin).
DETAIL = ("steps", "intro", "videos", "tips", "equipment", "storage", "credit")
detail = {r["id"]: {k: r[k] for k in DETAIL if k in r} for r in recipes}
index = [{k: v for k, v in r.items() if k not in DETAIL} for r in recipes]
# Ingrédients de l'index en tableaux [quantité, libellé, réf., poids(, 1 si facultatif)] : 13 Ko compressés de moins au
# démarrage (place pour les fiches TikTok du 22/10/2026) ; data.ts les remet en objets à la lecture.
for x in index:
    x["ingredients"] = [[l["qty"], l["label"], l["ref"], l["weight"]] + ([1] if l["optional"] else []) for l in x["ingredients"]]
from renommages import RENAMES
_ids_all = {r["id"] for r in recipes}
assert all(n in _ids_all and o not in _ids_all for o, n in RENAMES.items()), "renommage : l'ancien nom existe encore ou le nouveau manque"
dump("ingredients.json", ingredients); dump("recipes.json", index); dump("recipes_detail.json", detail); dump("rules.json", RULES); dump("renames.json", RENAMES)
print(f"recettes : index {len(json.dumps(index, ensure_ascii=False)) // 1024} Ko, détail {len(json.dumps(detail, ensure_ascii=False)) // 1024} Ko")
dump("catalogue.json", catalogue); dump("imports.json", imports)
print(f"zéro déchet : {ZW_COUNT} ingrédients entamés repérés dans {sum(1 for v in LEFT.values() if v)} fiches")
print(f"vidéos liées : {sum(len(v) for v in VIDEOS.values())} sur {len(VIDEOS)} fiches ; imports lisibles dans l'app : {sum(1 for i in imports if i.get('embed'))}")
print(f"ingrédients {len(ingredients)} · recettes {len(recipes)} · règles {len(RULES)} · catalogue {len(catalogue)} · imports {len(imports)}")
print(f"écarts (ingrédients hors référentiel, ref=None) : {len(gaps)}")
for g in sorted(set(x.split(' : ', 1)[1] for x in gaps)): print("  -", g)
