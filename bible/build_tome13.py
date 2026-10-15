# -*- coding: utf-8 -*-
"""Génère BIBLE_TOME13_VAGUE2.md : les fiches de la vague 2 (plus de 500 recettes), les techniques ajoutées
(pâtisserie, chocolat, boulangerie, poissons, viandes, cuissons, œufs, condiments) et les décisions associées.
À lancer après export_app_data.py (il relit les données de l'application pour les vérifications croisées)."""
import json, os, re
from collections import Counter, OrderedDict
from load_ref import parse_tome3
from atlas_engine import Ingredient, Line, Recipe, Rule, availability, evaluate, _walk
import export_app_data as X  # exécute l'export : vérifie toutes les références et charge toutes les fiches
from recipes_data import RECIPES
from recipes_v2_base import V2

HERE = os.path.dirname(os.path.abspath(__file__))
REF = parse_tome3(os.path.join(HERE, "BIBLE_TOME3_REFERENTIEL_INGREDIENTS.md"))
ALLER = {"GL": "gluten", "CR": "crustacés", "OE": "œufs", "PO": "poissons", "AR": "arachide", "SO": "soja", "LA": "lait", "FC": "fruits à coque",
         "CE": "céleri", "MO": "moutarde", "SE": "sésame", "SU": "sulfites", "LU": "lupin", "MM": "mollusques"}
ING = {n: Ingredient(n, {k: v for k, v in r["derivs"].items() if k in ("pork", "alcohol")}, set(r["allergens"]), "C") for n, r in REF.items()}
TITLE = {d["id"]: d["title"] for d in RECIPES}
WAVE2 = [d for d in RECIPES if d["id"] in set(V2)]

RS = OrderedDict()
for d in RECIPES:
    lines = []
    for qty, label, ref, w, opt in d["ing"]:
        if ref is None: continue
        lines.append(Line(sub=ref[4:], weight=w) if ref.startswith("SUB:") else Line(ing=ref, weight=w, optional=opt))
    RS[d["id"]] = Recipe(d["id"], lines)
RULES = []
for d in RECIPES:
    for v in d["variantes"]:
        for orig, items in v["replace"].items():
            if v["constraints"]: RULES.append(Rule(f'{d["id"]}:{orig}', orig, [(a, b) for a, b in items], set(v["constraints"]), "validated"))
for r in X.RULES:
    RULES.append(Rule("gen:" + r["replaces"], r["replaces"], [(a, b) for a, b in r["items"]], set(r["satisfies"]), "validated"))

def lab(st): return {"ok": "✅", "ok_warning": "🟡", "adaptable": "🔄", "hidden": "⛔"}[st]
def hm(m): return f"{m//60} h {m%60:02d}" if m >= 60 else f"{m} min"
def maybe_of(rec):
    m = set()
    for ln in _walk(rec, RS): m |= REF[ln.ing]["maybe"]
    return m
def fmt_allergens(e, mb):
    s = ", ".join(ALLER[a] for a in sorted(e["allergens"])) or "aucun déclaré"
    m = ", ".join(ALLER[a] for a in sorted(mb - e["allergens"]))
    return s + (f" ; **possibles selon marque** : {m}" if m else "")
def direct_rewrite(rec, replace):
    nl = []
    for ln in rec.lines:
        if ln.ing in replace: nl += [Line(ing=it, weight=ln.weight, optional=ln.optional) for it, _ in replace[ln.ing]]
        else: nl.append(ln)
    return Recipe(rec.id + "#v", nl)

ev = {d["id"]: evaluate(RS[d["id"]], ING, RS) for d in WAVE2}
APP = {r["id"]: r for r in json.load(open(os.path.join(HERE, "..", "app", "src", "data", "recipes.json"), encoding="utf-8"))}
assert all(d["id"] in APP for d in WAVE2), "fiche absente des données de l'application"

# Lots (un fichier recipes_v2_*.py = un lot éditorial)
LOTS = OrderedDict()
for f in sorted(os.listdir(HERE)):
    m = re.match(r"recipes_v2_(\w+)\.py$", f)
    if not m or m.group(1) in ("base", "all"): continue
    src = open(os.path.join(HERE, f), encoding="utf-8").read()
    doc = re.search(r'"""(.*?)"""', src, re.S).group(1).strip().splitlines()[0]
    ids = [i for i in re.findall(r'(?m)^(?:K|sauce_mayo|drink|fusion)\("([^"]+)"', src) if i in TITLE]
    LOTS[doc.replace("Vague 2 · ", "")] = ids

# Techniques ajoutées (lues dans l'application, source unique)
TS = open(os.path.join(HERE, "..", "app", "src", "lib", "techniques2.ts"), encoding="utf-8").read()
TECH = re.findall(r'\{ id: "([^"]+)", name: "([^"]+)", family: "([^"]+)", level: (\d)', TS)

o = []; P = o.append
P(f"# 📘 BIBLE ATLAS : TOME 13 : Vague 2 ({len(WAVE2)} fiches), techniques de chef, pâtissier, boulanger et chocolatier\n")
P("> Ce tome **intègre à la bible** la livraison du 15/10/2026 :")
P(f"> 1. **{len(WAVE2)} nouvelles fiches** au format du Tome 11 (France par région, Europe, Maghreb, Afrique, Moyen-Orient, Asie, Amériques, Océanie, food fusion, pâtisserie française, chocolats d'occasion, condiments et marinades maison, sauces à frites, boulangerie, cuisine des enfants, quotidien, anti-gaspi, boissons sans alcool, desserts simples, cahier du chef). Le catalogue rédigé compte désormais **{len(RECIPES)} recettes complètes** ;")
P(f"> 2. **{len(TECH)} nouvelles fiches techniques** dans l'application (pâtisserie, chocolat, boulangerie-viennoiserie, poissons et fruits de mer, viandes et volailles, maîtrise des cuissons, œufs, condiments et marinades), avec tableaux de températures et de proportions ;")
P("> 3. un **nouvel habillage graphique** de l'application (§6).\n>")
P("> **Statut des fiches : « Brouillon rédactionnel prêt pour le Test 1 »**, comme aux Tomes 11 et 12. **Aucune n'a été testée en cuisine.** Badges porc / alcool / allergènes **calculés** par le moteur de référence sur le référentiel du Tome 3 (confiance C). Variantes : **à tester**.\n")
P("---\n")

P("## 0. Cahier des charges éditorial de la vague 2 (le regard du critique gastronomique)\n")
P("- **Goût d'abord** : chaque fiche vise un résultat franc et généreux (assaisonnement, croûte, acidité finale, herbes fraîches), avec des **repères sensoriels** dans les étapes (« bec d'oiseau », « nappe la cuillère », « l'os se détache »).")
P("- **Peu de complexité** : 10 ingrédients au plus en général, matériel d'une cuisine française, gestes décrits pas à pas ; les recettes exigeantes (macarons, croissants, tempérage) le disent (niveau ⭐⭐⭐) et renvoient à la fiche technique.")
P("- **Respect des bibles** : chaque ingrédient est un nom exact du Tome 3 (vérifié à l'export) ; versions sans porc par défaut quand le porc n'est pas indissociable (cassoulet, tartiflette, choucroute : version inspirée, signalée) ; versions **sans alcool** rédigées pour les plats où le vin, la bière, le rhum ou une liqueur structurent le goût ; allergènes calculés ; sécurité des publics fragiles (œuf cru, poisson cru, miel avant 1 an, fruits à coque) rappelée dans la fiche.")
P("- **Zéro déchet** : chaque ingrédient entamé reçoit une solution (calcul automatique, Tome 12 §6) ; les condiments maison (bouillon cube, nokoss, pickles, chapelure) recyclent parures et restes.")
P("- **Sources** : savoir-faire culinaire courant ; la sélection « sauces pour accompagner les frites » de Femme Actuelle n'a servi que de liste de noms (aucun texte repris). Vidéos : intégrations officielles, liées automatiquement par mots-clés quand un import correspond.\n")
P("---\n")

P("## 1. Récapitulatif par lot (calculé)\n")
for name, ids in LOTS.items():
    P(f"### {name} ({len(ids)})\n")
    P("| Recette | Région | Allergènes (sûrs) | Porc | Alcool | Sans porc Strict | Sans alcool Strict | Enfants dès |")
    P("|---|---|---|---|---|---|---|---|")
    for rid in ids:
        d = next(x for x in WAVE2 if x["id"] == rid); e = ev[rid]
        pk = {"ok": "✅", "uncertain": "🟡", "violates": "🐖", "trace": "🟡"}[e["pork"]]
        ac = {"ok": "✅", "uncertain": "🟡", "violates": "🍷", "trace": "🟡 traces"}[e["alcohol"]]
        P(f"| {d['title']} | {d['region'].split(' › ')[-1]} | {', '.join(sorted(e['allergens'])) or '–'} | {pk} | {ac} | {lab(availability(e, {'pork'}, True, RULES))} | {lab(availability(e, {'alcohol'}, True, RULES))} | {d.get('age') if d.get('age') is not None else '–'} |")
    P("")
cnt = Counter(c for d in WAVE2 for c in d.get("cats", []))
P("**Rubriques couvertes par la vague 2** : " + " · ".join(f"{k} : {v}" for k, v in cnt.most_common()) + ".\n")
P("---\n")

P("## 2. Fiches de la vague 2\n")
n = 0
for name, ids in LOTS.items():
    P(f"## 2.{list(LOTS).index(name) + 1} {name}\n")
    for rid in ids:
        n += 1
        d = next(x for x in WAVE2 if x["id"] == rid); r = RS[rid]; e = ev[rid]; mb = maybe_of(r)
        P(f"### {d['title']}\n")
        P(f"*{d['origin']} · {d['region']} · {d['kind']}*" + (f" · Fêtes : {', '.join(d['fetes'])}" if d.get("fetes") else "") + "\n")
        P(f"Niveau {'⭐' * d['niveau']} · {d['portions']} portions · actif {hm(d['actif'])} · repos/cuisson {hm(d['repos'])} · coût {d['cost']}\n")
        pkb = {"ok": "✅ Sans porc (calculé)", "uncertain": "🟡 Porc possible", "violates": "🐖 **Contient du porc**", "trace": "🟡"}[e["pork"]]
        acb = {"ok": "✅ Sans alcool (calculé)", "trace": "🟡 **Traces d'alcool possibles**", "uncertain": "🟡 Alcool possible", "violates": "🍷 **Contient de l'alcool**"}[e["alcohol"]]
        P(f"- {pkb}" + (f" : {', '.join(e['offenders']['pork'])}" if e["offenders"]["pork"] else ""))
        P(f"- {acb}" + (f" : {', '.join(e['offenders']['alcohol'])}" if e["offenders"]["alcohol"] else ""))
        P(f"- ⚠️ **Allergènes** : {fmt_allergens(e, mb)}")
        P(f"- 👶 **Enfants** : {d['enfants']}\n")
        P(f"**Équipement** : {d['equip']}\n\n{d['intro']}\n")
        P("**Ingrédients** : " + " · ".join(f"{q} {l}{' *(facultatif)*' if opt else ''}" for q, l, ref, w, opt in d["ing"]) + "\n")
        for k, s in enumerate(d["steps"], 1): P(f"{k}. {s}")
        if d["astuces"]: P("\n" + "\n".join(f"- {a}" for a in d["astuces"]))
        for v in d["variantes"]:
            dr = evaluate(direct_rewrite(r, v["replace"]), ING, RS)
            P(f"\n- **Variante {v['name']}** : {v['note']} *Calcul* : porc **{dr['pork']}**, alcool **{dr['alcohol']}**.")
        P(f"\n**Conservation** : {d['conservation']}" + (f" · **Zéro déchet** : {' '.join(d['zero_dechet'])}" if d["zero_dechet"] else "") + "\n")
        if d["techniques"]: P(f"**Techniques** : {', '.join(d['techniques'])}\n")
        P("---\n")
assert n == len(WAVE2), (n, len(WAVE2))

P("## 3. Nouvelles fiches techniques (application, rubrique Techniques)\n")
fam = OrderedDict()
for tid, name, family, lvl in TECH: fam.setdefault(family, []).append(f"{name} (niv. {lvl})")
for f, items in fam.items(): P(f"- **{f}** : " + " · ".join(items))
P("\nChaque fiche donne : pourquoi, matériel, pas à pas, erreurs fréquentes, solution sans équipement et, quand c'est utile, un **tableau de repères** (températures à cœur des viandes et poissons, temps de cuisson des œufs, courbes de tempérage du chocolat, stades du sucre, proportions de ganache, dosages de crème pâtissière, dix marinades du monde). Les températures de sécurité suivent les recommandations courantes (volaille 74 °C, viande hachée 70 °C, poisson pour publics fragiles 63 °C).")
P("\n**Vidéos des gestes** : ATLAS n'a pas encore tourné ses démonstrations (Tome 6). Chaque fiche propose une recherche vidéo ciblée et les vidéos importées (TikTok, YouTube) qui traitent du sujet, lues dans l'application par les intégrations officielles.\n")
P("---\n")

P("## 4. Condiments et bases maison (sans additifs)\n")
P("Bouillon « cube » en pâte (légumes + 15 % de sel, 6 mois au frigo) et en poudre (légumes séchés), nokoss sénégalais, ras el-hanout, garam masala, curry doux, berbéré, dukkah, zaatar, pâte de curry vert, citrons confits, ghee, moutarde, ketchup de betterave, pickles, sauce chien, piri-piri, sweet chili, satay, nuoc cham, chutney de mangue, huile pimentée, beurres composés et dix marinades du monde. **Règle de sécurité** : toutes ces préparations se gardent **au frigo** (ou congelées) ; aucune conserve longue à température ambiante n'est proposée sans stérilisation maîtrisée (risque botulique).\n")
P("---\n")

LEFT = json.load(open(os.path.join(HERE, "..", "app", "src", "data", "leftovers.json"), encoding="utf-8"))
zw = sum(len(LEFT.get(d["id"], [])) for d in WAVE2)
P("## 5. Zéro déchet de la vague 2\n")
P(f"Le calcul du Tome 12 §6 s'applique aux nouvelles fiches : **{zw} ingrédients entamés** repérés dans la vague 2, chacun avec ses solutions (entrée, accompagnement, autre plat, conservation, usage hors cuisine).\n")
P("---\n")

P("## 6. Habillage graphique de l'application (direction artistique)\n")
P("- **Ambiance** : gourmande et chaleureuse, palette « marché » : tomate, safran, piment, pistache, aubergine, crème ; papier crème légèrement texturé en mode clair, « nuit d'épicerie » brun-prune en mode sombre.")
P("- **Accueil** : grand bandeau illustré (assiette, épices, herbes dessinés en SVG, sans image lourde), salutation selon l'heure, bandes de rubriques colorées, cartes de recettes à couverture photo ou **couverture illustrée générée** (dégradé et motif propres à chaque région et type de plat) pour les fiches sans photo.")
P("- **Accessibilité** : contrastes conformes au Tome 5 (texte ≥ 4,5:1), animations désactivées si « réduire les animations » est activé, aucune information portée par la seule couleur.\n")
P("---\n")

P("## 7. Décisions à valider (suite du Tome 12 §8)\n")
P("- **D21** : versions « inspirées » sans porc des plats où le porc est indissociable (cassoulet, tartiflette au choix, potjevleesch, rougail saucisses, char siu, feijoada) : garder le nom d'origine avec la mention « version », ou renommer ?")
P("- **D22** : glace vanille utilisée en ingrédient (profiteroles, milk-shake, poires Belle-Hélène) est rattachée provisoirement à « crème fleurette » faute d'entrée « glace » au Tome 3 : ajouter l'entrée ?")
P("- **D23** : matcha et café soluble n'ont pas d'entrée au Tome 3 (référence vide) : à ajouter avec la mention « théine / caféine » pour le filtre enfants ?")
P("- **D24** : fiches à poisson cru (gravlax, ceviche, poisson cru tahitien, kokoda, tataki, poke) : afficher un bandeau « publics fragiles » plus visible que l'astuce ?")
P("- **D25** : priorité des tests en cuisine de la vague 2 (proposition : pâtisserie et chocolat d'abord, les dosages y sont le moins tolérants).\n")

P("---\n")
from dictionnaire_data import DICO, ALIAS
P("## 8. Dictionnaire illustré des ingrédients\n")
P(f"**{len(DICO)} fiches** couvrent les {len(DICO) + len(ALIAS)} lignes du Tome 3 ({len(ALIAS)} doublons de la section « Produits du monde » renvoient à leur fiche). Chaque fiche : ce que c'est, comment l'utiliser, la saison en France métropolitaine, la disponibilité (Tome 3), les allergènes et dérivés porc/alcool calculés, l'astuce du référentiel (substitut, zéro déchet), les recettes ATLAS qui l'utilisent, et une photo sous licence libre quand une image juste a été trouvée (sinon pictogramme de la famille). Source unique : `bible/dico_1.py` à `dico_4.py`, exportée dans `app/src/data/dico.json` (chargée à la demande, disponible hors connexion). Chaque ingrédient d'une recette renvoie à sa fiche.\n")
P("Exemples de fiches pour des produits peu connus : **passata** (purée de tomates crues tamisée), **soumbala / netetou** (graines de néré fermentées d'Afrique de l'Ouest, le « bouillon cube » traditionnel), galanga, tahini, gochujang, ful medames, achiote, asafoetida, amchur, berbéré, niter kibbeh, katsuobushi, mahleb, farofa, colombo…\n")
P("---\n")
P("## 9. Saisonnalité selon le lieu d'utilisation\n")
P("- **Zone** : déduite du fuseau horaire de l'appareil (aucune géolocalisation, aucune donnée envoyée) et modifiable dans le profil : hémisphère nord tempéré, hémisphère sud tempéré (calendrier décalé de 6 mois), zone tropicale (pas d'hiver : produits tropicaux et plats frais privilégiés).")
P(f"- **Calendrier** : {sum(1 for v in DICO.values() if v[3])} produits frais datés (légumes, fruits, herbes, poissons, quelques fromages), mois de pleine récolte en France métropolitaine.")
P("- **Score de saison d'une recette** : + produits structurants de saison, − produits structurants hors saison, + plat réconfortant (mijotés, soupes, gratins) en hiver et à l'automne, + plat frais (salades, grillades, boissons fraîches) en été et sous les tropiques.")
P("- **Usages** : menu du jour (entrée, plat, dessert tirés du tiers le mieux accordé à la saison, stables sur la journée), « marché du mois », envie « De saison », pastille « de saison / hors saison » sur chaque fiche (avec le conseil : surgelés et conserves de qualité conviennent souvent).")
P("- **Limites** : le calendrier tropical est simplifié (pas de saisons des pluies) ; les zones méditerranéennes ou de montagne suivent le calendrier tempéré.\n")
P("- **D26** : faut-il un calendrier propre aux Antilles, à La Réunion et à l'Afrique de l'Ouest (saisons de la mangue, du letchi, de l'igname) ?\n")
P("---\n")
P("## 10. Chaînes YouTube de recettes (corpus vidéo)\n")
YTM = open(os.path.join(HERE, "..", "recettes-classees", "createurs_youtube_classes.md"), encoding="utf-8").read()
P("Relevé du 15/10/2026, à la demande : Le Riz Jaune, La cuisine de Marina, L'Ardoise Porto-Vecchio, Armand Hasanpapaj, AlexCook'in, Britney Breaks Bread, Tinas Kitchenworld, Shota Horii · Aisle to Tokyo, CookWithBash, ChesterFoodies, Dishcovery, Cook with Nabeela, Kookmutsjes (vidéos et Shorts les plus récents, 400 au plus par chaîne). Tri **automatique** d'après le titre (`recettes-classees/build_youtube.py`), avec la cuisine de la chaîne par défaut ; hors-recette écarté ; porc et alcool repérés dans le titre et signalés ; titres étrangers gardés dans leur langue et signalés. Lecture dans l'application par le lecteur officiel YouTube (youtube-nocookie ; Shorts en vertical). Les vidéos sont aussi liées automatiquement aux fiches ATLAS de même nom.\n")
P("\n".join(l for l in YTM.split("\n") if l.startswith("|")) + "\n")
P("- **Limites** : tri par mots-clés (quelques erreurs possibles, signalables) ; vidéos plus anciennes que les 400 dernières non relevées ; pas de traduction des titres anglais, allemands et néerlandais.\n")
open(os.path.join(HERE, "BIBLE_TOME13_VAGUE2.md"), "w", encoding="utf-8").write("\n".join(o))
print(f"Tome 13 : {len(WAVE2)} fiches, {len(LOTS)} lots, {len(TECH)} techniques, {len(o)} lignes")
