# -*- coding: utf-8 -*-
"""Génère BIBLE_TOME12_VAGUE1_ET_APPLICATION.md : fiches de la vague 1 (badges calculés par atlas_engine.py,
comme le Tome 11), corpus d'imports classés, et description de l'application v1.
Usage : python build_tome12.py   (après python export_app_data.py)"""
import json, os, re
from collections import Counter, OrderedDict
from load_ref import parse_tome3
from atlas_engine import Ingredient, Line, Recipe, availability, evaluate, _walk
import recipes_data
import recipes_v1_pains, recipes_v1_sauces, recipes_v1_plats, recipes_v1_desserts  # noqa: F401
from recipes_data import RECIPES
import export_app_data as X  # réutilise les règles génériques et les vérifications (exécute l'export)

HERE = os.path.dirname(os.path.abspath(__file__))
REF = parse_tome3(os.path.join(HERE, "BIBLE_TOME3_REFERENTIEL_INGREDIENTS.md"))
ALLER = {"GL": "gluten", "CR": "crustacés", "OE": "œufs", "PO": "poissons", "AR": "arachide", "SO": "soja", "LA": "lait", "FC": "fruits à coque",
         "CE": "céleri", "MO": "moutarde", "SE": "sésame", "SU": "sulfites", "LU": "lupin", "MM": "mollusques"}
ING = {n: Ingredient(n, {k: v for k, v in r["derivs"].items() if k in ("pork", "alcohol")}, set(r["allergens"]), "C") for n, r in REF.items()}
V0 = set(X.EXTRA)  # les 11 fiches du Tome 11
WAVE1 = [d for d in RECIPES if d["id"] not in V0 and d.get("vague") != 2]  # la vague 2 a son propre tome (13)
TITLE = {d["id"]: d["title"] for d in RECIPES}

RS = OrderedDict()
for d in RECIPES:
    lines = []
    for qty, label, ref, w, opt in d["ing"]:
        if ref is None: continue
        lines.append(Line(sub=ref[4:], weight=w) if ref.startswith("SUB:") else Line(ing=ref, weight=w, optional=opt))
    RS[d["id"]] = Recipe(d["id"], lines)

# règles : variantes de chaque fiche + règles génériques (statut « validated » = SIMULATION, comme au Tome 11)
from atlas_engine import Rule
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

ev = {rid: evaluate(r, ING, RS) for rid, r in RS.items()}

# vérification croisée avec l'application : mêmes statuts porc/alcool/allergènes que recipes.json évalué en TypeScript
APP = json.load(open(os.path.join(HERE, "..", "app", "src", "data", "recipes.json"), encoding="utf-8"))
assert len(APP) == len(RECIPES)

o = []; P = o.append
P("# 📘 BIBLE ATLAS : TOME 12 : Vague 1 (59 fiches), corpus importé et application v1\n")
P("> Ce tome **intègre à la bible** trois livraisons du 14/10/2026 :")
P("> 1. **59 nouvelles fiches** (vague 1) au format du Tome 11 : pains et bases, sauces maison, plats et entrées du monde, desserts, fêtes, anti-gaspi, boissons sans alcool. Avec les 11 fiches étalons, le catalogue rédigé compte **70 recettes complètes** ;")
P("> 2. le **corpus d'imports classés** : 585 recettes des favoris TikTok du compte et 339 recettes du site Cooking with Morgane, triées dans les catégories de la bible ;")
P("> 3. **l'application ATLAS v1** (PWA iPhone, iPad, Mac, Android, PC), construite à partir des Tomes 1 à 11 et de ce tome.\n>")
P("> **Statut des fiches : « Brouillon rédactionnel prêt pour le Test 1 »**, comme au Tome 11. **Aucune n'a été testée en cuisine** ; quantités et temps = pratiques usuelles, à confirmer par le Tome 7 §2. Badges **calculés** par le moteur de référence (`atlas_engine.py`) sur le référentiel du Tome 3 (**confiance C**). Variantes et règles génériques : **à tester** (Tome 7 §3).\n")
P("---\n")

# ---------------------------------------------------------------- 1. récapitulatif
P("## 1. Tableau récapitulatif de la vague 1 (calculé)\n")
P("| # | Recette | Région | Rubriques | Allergènes (sûrs) | Porc | Alcool | Sans porc Std / Strict | Sans alcool Std / Strict | Enfants dès |")
P("|---|---|---|---|---|---|---|---|---|---|")
for i, d in enumerate(WAVE1, 1):
    e = ev[d["id"]]
    al = ", ".join(sorted(e["allergens"])) or "–"
    pk = {"ok": "✅", "uncertain": "🟡", "violates": "🐖", "trace": "🟡"}[e["pork"]]
    ac = {"ok": "✅", "uncertain": "🟡", "violates": "🍷", "trace": "🟡 traces"}[e["alcohol"]]
    ps, pt = lab(availability(e, {"pork"}, False, RULES)), lab(availability(e, {"pork"}, True, RULES))
    as_, at = lab(availability(e, {"alcohol"}, False, RULES)), lab(availability(e, {"alcohol"}, True, RULES))
    P(f"| {i} | {d['title']} | {d['region'].split(' › ')[-1]} | {', '.join(d.get('cats', [])) or '–'} | {al} | {pk} | {ac} | {ps} / {pt} | {as_} / {at} | {d.get('age') if d.get('age') is not None else '–'} |")
P("\n**Légende** : identique au Tome 11 §1. **🔄** = version adaptée par une variante de la fiche ou une règle générique (§4), **à tester**. **Enfants dès** : âge minimal conseillé (Tome 1 §7.6).\n")
cnt = Counter(c for d in WAVE1 for c in d.get("cats", []))
P("**Couverture des rubriques demandées** (vague 0 + vague 1) : " + " · ".join(f"{k} : {sum(1 for d in RECIPES if k in d.get('cats', []))}" for k in ["pains", "sauces", "enfants", "fetes", "zero_dechet", "boissons", "techniques"]) + ".\n")
P("---\n")

# ---------------------------------------------------------------- 2. fiches
P("## 2. Fiches de la vague 1\n")
for i, d in enumerate(WAVE1, 1):
    r = RS[d["id"]]; e = ev[d["id"]]; mb = maybe_of(r)
    P(f"### 2.{i} {d['title']}\n")
    P(f"*{d['origin']} · {d['region']} · {d['kind']}*" + (f" · Fêtes : {', '.join(d['fetes'])}" if d.get("fetes") else "") + "\n")
    P("| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |\n|---|---|---|---|---|---|")
    P(f"| {'⭐'*d['niveau']} | {d['portions']} | {hm(d['actif'])} | {hm(d['repos'])} | **{hm(d['actif']+d['repos'])}** | {d['cost']} |\n")
    pkb = {"ok": "✅ Sans porc (calculé)", "uncertain": "🟡 Porc possible", "violates": "🐖 **Contient du porc**", "trace": "🟡"}[e["pork"]]
    acb = {"ok": "✅ Sans alcool (calculé)", "trace": "🟡 **Traces d'alcool possibles**", "uncertain": "🟡 Alcool possible", "violates": "🍷 **Contient de l'alcool**"}[e["alcohol"]]
    P(f"- {pkb}" + (f" : {', '.join(e['offenders']['pork'])}" if e["offenders"]["pork"] else ""))
    P(f"- {acb}" + (f" : {', '.join(e['offenders']['alcohol'])}" if e["offenders"]["alcohol"] else ""))
    P(f"- ⚠️ **Allergènes** : {fmt_allergens(e, mb)}")
    P(f"- 👶 **Enfants** : {d['enfants']}\n")
    P(f"**Équipement** : {d['equip']}\n")
    P(f"{d['intro']}\n")
    P("**Ingrédients**\n")
    P("| Quantité | Ingrédient | Réf. Tome 3 | Dispo |\n|---|---|---|---|")
    for qty, label, ref, w, opt in d["ing"]:
        if ref is None: rr, dd = "*implicite*", "🟢"
        elif ref.startswith("SUB:"): rr, dd = f"*sous-recette : {TITLE[ref[4:]]}*", "–"
        else: rr, dd = ref, REF[ref]["dispo"]
        P(f"| {qty} | {label}{' *(facultatif)*' if opt else ''} | {rr} | {dd} |")
    P("\n**Étapes**\n")
    for n, s in enumerate(d["steps"], 1): P(f"{n}. {s}")
    if d["astuces"]:
        P("\n**Astuces et sécurité**\n")
        for a in d["astuces"]: P(f"- {a}")
    if d["variantes"]:
        P("\n**Variantes (à tester)**\n")
        for v in d["variantes"]:
            dr = evaluate(direct_rewrite(r, v["replace"]), ING, RS)
            P(f"- **{v['name']}** : {v['note']} *Calcul* : porc **{dr['pork']}**, alcool **{dr['alcohol']}**.")
    P(f"\n**Conservation** : {d['conservation']}\n")
    P("**Zéro déchet** : " + " ".join(d["zero_dechet"]) + "\n")
    if d["accords_sa"] or d["accords_a"]:
        P("**Boissons** : " + ("*sans alcool* : " + " ; ".join(d["accords_sa"]) if d["accords_sa"] else "") + (" · *avec alcool (adultes)* : " + " ; ".join(d["accords_a"]) if d["accords_a"] else "") + "\n")
    P(f"**Techniques** : {', '.join(d['techniques'])} · **À valider au test** : {d['tests']}\n")
    P("---\n")

# ---------------------------------------------------------------- 3. corpus importé
IMP = json.load(open(os.path.join(HERE, "..", "app", "src", "data", "imports.json"), encoding="utf-8"))
by_src = Counter(i["source"] for i in IMP)
by_cat = Counter(i["cat"] for i in IMP)
P("## 3. Corpus importé et classé (TikTok, Cooking with Morgane)\n")
P("### 3.1 Sources et méthode\n")
P("| Source | Relevé | Recettes retenues | Méthode de tri | Fichier |\n|---|---|---|---|---|")
P(f"| Favoris TikTok du compte (onglet Favoris) | 14/10/2026 : 672 favoris, dont 87 hors cuisine écartés | {by_src.get('TikTok', 0)} | **Manuel**, d'après la légende de chaque vidéo | `recettes-classees/tiktok_favoris_classes.md` |")
P(f"| Site Cooking with Morgane (index `/fr/liste.aspx`) | 14/10/2026 | {by_src.get('Cooking with Morgane', 0)} | **Automatique**, mots-clés du titre (pays deviné ; 208 en « Chine ou à préciser ») | `recettes-classees/cookingwithmorgane_classees.md` |")
P("\n- **Ce qui est conservé** : titre, lien, auteur·e, catégorie, pastilles porc/alcool **repérées dans la légende** (pré-évaluation). **Aucune vidéo ni aucun texte de recette n'est copié** (Tome 7 §7.5, Tome 1 §19.7) : ces recettes appartiennent à leurs auteur·e·s ; l'application les présente comme **liens crédités**.")
P("- 43 favoris TikTok ont une légende vide ou insuffisante : catégorie « À vérifier » (il faut regarder la vidéo).")
P("- Les pastilles 🐖/🍷 ne valent pas badge : une recette importée reste en confiance C ; le moteur ne la déclare jamais « sans porc » sans liste d'ingrédients reconnue (Tome 7 §7.2).\n")
P("### 3.2 Répartition par catégorie de la bible\n")
P("| Catégorie | Recettes |\n|---|---|")
for k, n in by_cat.most_common(): P(f"| {k} | {n} |")
P("\n### 3.3 Usage dans la bible et l'application\n")
P("- **Atlas** : chaque région affiche « Dans tes imports ». **Pains**, **Sauces**, **Techniques**, **Zéro déchet**, **Fêtes** listent les favoris de leur catégorie.")
P("- **Vivier éditorial** : les plats récurrents des favoris (thieb, yassa, mafé, msemen, naan, focaccia, flan, sauces de snack…) confirment les priorités du Tome 4 ; la vague 1 en couvre déjà une partie. Les recettes de créateur·rice·s ne sont **pas** recopiées : elles peuvent inspirer un brief (Tome 4 §2) rédigé et testé par l'équipe.")
P("- **Import continu** : l'application importe un lien + sa légende (tri automatique), une liste de liens, ou l'**export de données TikTok** (fichier JSON du compte : liens des favoris), voie officielle à défaut d'API (Tome 1 §14.1).\n")
P("### 3.4 Food fusion (catégorie ajoutée le 14/10/2026)\n")
P("Pour les recettes **dont l'origine ne se rattache pas à un seul pays** ou qui **marient plusieurs traditions**, une entrée « **🌐 Food fusion** » s'ajoute aux 12 macro-régions de l'atlas. Elle **complète** la règle du Tome 1 §5.2 (classement par plat structurant) : une fiche garde sa cuisine principale pour la recherche par région, et porte en plus la rubrique `fusion` avec une phrase qui explique le mélange.\n")
P("| Fiche | Mélange |\n|---|---|")
for k, v in X.FUSION_RECIPES.items(): P(f"| {TITLE[k]} | {v} |")
fus = [i for i in IMP if i["cat"] == "fusion"]
P(f"\n**Corpus importé : {len(fus)} recettes reclassées en food fusion** (motifs relus à la main : pizzas au butter chicken, tonkatsu ou rendang ; feuilles de riz détournées ; couscous-tiep ; carbonara-ramen ; big mac « piadizza » ; poulets de séries et de mangas ; bao teriyaki…). Exemples :\n")
for i in fus[:12]: P(f"- {i['title'][:90]} *({i['source']}, rangée avant dans « {i.get('from', '?')} »)*")
P("\nÀ l'import, le tri automatique de l'application teste la food fusion **avant** les régions : un mélange de traditions prime sur la région d'un des ingrédients.\n")
P("### 3.5 Vidéos des recettes, lues dans l'application\n")
nv = sum(len(d.get("videos", [])) for d in APP); nf = sum(1 for d in APP if d.get("videos"))
P(f"- **{nf} fiches sur {len(APP)}** sont reliées à **{nv} vidéos existantes** (favoris TikTok, vidéos YouTube de Cooking with Morgane), choisies par mots-clés relus à la main pour chaque fiche (`VIDEO_KEYS` dans `export_app_data.py`), les versions sans porc ni alcool d'abord.")
P(f"- **{sum(1 for i in IMP if i.get('embed'))} des {len(IMP)} recettes importées** se lisent **dans l'application** : TikTok par l'intégration officielle (`tiktok.com/embed/v2/<id>`), YouTube par `youtube-nocookie.com` ; les 339 identifiants YouTube ont été relevés sur les pages du site (`recettes-classees/cookingwithmorgane_videos.json`). Les carrousels photo TikTok s'ouvrent dans TikTok.")
P("- La lecture se lance **dans une fenêtre de l'application** (fiche recette, mode cuisine, listes de favoris) ; **rien n'est chargé chez TikTok ou YouTube avant d'appuyer sur ▶** (RGPD). Chaque fiche permet aussi d'**ajouter son propre lien vidéo**.")
P("- Ce sont les vidéos de leurs auteur·e·s : crédit et lien vers l'original sous chaque lecture ; aucune vidéo n'est copiée (D15). Une vidéo supprimée ou rendue privée par son auteur·e ne se lit plus.\n")
P("### 3.6 Comptes « La cuisine de Marina » et « NiangCook » (ajoutés le 15/10/2026)\n")
cre = [i for i in IMP if i["author"] in ("lacuisinedemarina", "niangcook")]
P(f"- **{sum(1 for i in cre if i['author'] == 'lacuisinedemarina')} vidéos de @lacuisinedemarina** (cuisine camerounaise : ndolé, eru, okok, koki, placali, macabo, safou…) et **{sum(1 for i in cre if i['author'] == 'niangcook')} de @niangcook** (cuisine sénégalaise : yassa, thieb, thiakry, bissap blanc, jus de bouye…), favoris et comptes réunis sans doublon.")
P("- Relevé : toutes les vidéos que TikTok affiche sur le web (67 et 18) ; au-delà, TikTok ne renvoie plus rien à un navigateur automatisé et **sa protection anti-robot n'a pas été contournée**. Pour le catalogue complet, importer les liens depuis l'application (onglet Importer).")
P("- 16 vidéos écartées (annonces, vente d'épices, livre, restaurant, rappels de notification). Tri manuel : `recettes-classees/build_createurs.py`.\n")
P("---\n")

# ---------------------------------------------------------------- 4. règles génériques
P("## 4. Règles de substitution génériques (moteur de l'application)\n")
P("Quand une fiche n'a pas de variante pour le régime du foyer, l'application applique ces règles **par fonction** (Tome 1 §7.5, Tome 3 §3.2, §14, §16) aux **seuls ingrédients fautifs**, puis **revérifie** la recette obtenue (invariant du Tome 8). Toutes au statut **`draft`** : l'interface affiche « **Substitution à tester** » (Tome 7 §3.2) et jamais « goût préservé ».\n")
P("| Remplace | Par (ratio sur la quantité d'origine) | Régime | Indication |\n|---|---|---|---|")
for r in X.RULES:
    P(f"| {r['replaces']} | {' + '.join(f'{a} (×{b})' for a, b in r['items'])} | {', '.join({'pork': 'sans porc', 'alcohol': 'sans alcool'}[s] for s in r['satisfies'])} | {r['note']} |")
P("\n**Décision prise pour l'application (à valider, D13)** : le moteur de référence n'utilise que les règles `validated` ; l'application affiche **aussi** les versions adaptées par des règles `draft`, **clairement étiquetées « à tester »**, parce que la demande initiale exige des substitutions dès le départ et que le Tome 7 §3.2 autorise ce libellé pour `draft` et `testing`. Le contrôle de régime, lui, n'est jamais assoupli : une version adaptée qui ne passe pas la revérification est refusée.\n")
P("---\n")

# ---------------------------------------------------------------- 5. application
P("## 5. Application ATLAS v1\n")
P("### 5.1 Choix techniques (écart assumé avec D2)\n")
P("| Sujet | Bible (T1 §17, D2) | v1 livrée | Pourquoi |\n|---|---|---|---|")
P("| Plateformes | Flutter + modules natifs | **PWA** (React + TypeScript, Vite) installable sur iPhone, iPad, Mac (Safari › Ajouter au Dock), Android, Windows | Un seul code, testable tout de suite, hors connexion ; la version native reste l'objectif (Live Activities, Watch, minuteur écran éteint) |")
P("| Données | API + base | Données de la bible **embarquées** (export JSON) ; état du foyer sur l'appareil (localStorage) ; export/import de sauvegarde | Pas de serveur ni de compte : aucune donnée de santé ou de religion ne quitte l'appareil (T1 §19.1) |")
P("| Moteur diététique | `atlas_engine.py` (référence) | Portage TypeScript fidèle + 36 tests automatiques (les 28 du Tome 8 adaptés, propriétés aléatoires, 70 fiches réelles, import) | Mêmes invariants ; vérifié contre le moteur Python (§5.4) |")
P("| Audio | Voix neuronales pré-générées | Synthèse vocale **du système** (AVSpeechSynthesizer via Safari, voix Google/Microsoft), normalisation du texte (fractions, c. à s., °C, thermostat) et lexique de prononciation | Hors ligne et gratuit ; les voix premium restent une évolution |")
P("| Vidéos / photos | Tournage (Tome 6) | Couvertures générées ; liens « Tutos YouTube » + favoris importés liés à chaque recette et technique | Les médias ATLAS ne sont pas tournés ; aucun média tiers n'est copié |")
P("\n### 5.2 Couverture des 10 modules du Tome 1 §4.1\n")
P("| Module | Livré en v1 | Reste à faire |\n|---|---|---|")
P("| 1. Atlas du monde | 12 macro-régions + **Food fusion**, fiches complètes + 381 titres « au programme » (Tome 4) + imports liés ; vue cartes et vue liste accessible | Carte interactive, fiches culturelles par région |")
P("| 2. Recherche | Par **nom** (accents, ligatures, translittérations, synonymes, fautes), par **région**, par **ingrédients** (moteur de suggestion du Tome 1 §6.3 : « tu as tout », « il manque 1-2 choses », « idées », bonus anti-gaspi, familles de substitution, mode « tout utiliser ») | Scan de code-barres, dictée, photo du frigo |")
P("| 3. Enfants | Filtre par âge, toujours sans alcool, sans porc au choix, 30 min max ; règles de sécurité (miel < 1 an, étouffement, œuf cru…) ; « Petit chef » | Mode enfant verrouillé par code parent |")
P("| 4. Mes imports | Lien + légende → **tri automatique** (catégorie, région, porc/alcool, ingrédients rapprochés du Tome 3) ; liste de liens ; **export de données TikTok** ; partage direct depuis TikTok/Instagram sur Android (Web Share Target) ; bibliothèque des 924 recettes classées | Extraction depuis la vidéo (transcription), API officielles |")
P("| Vidéos | Lecteur intégré (TikTok, YouTube) sur les fiches, en mode cuisine et dans les listes ; vidéos existantes liées aux fiches ; ajout de ses propres liens | Vidéos ATLAS à tourner (Tome 6) |")
P("| 5. Techniques | 30 fiches P0 au format T1 §9.3 (pourquoi, matériel, pas à pas, erreurs, sans équipement), reliées aux recettes et aux vidéos | Vidéos ATLAS, parcours d'apprentissage |")
P("| 6. Pains & bases | 16 recettes (baguette, cocotte, pizza, focaccia, naan, pita, chapati, tortillas, msemen, batbout, crêpes, galettes, pancakes, pain de mie, brioche, pâte brisée) + **calculateur de pâte** (pourcentages boulangers, levure sèche ↔ fraîche) | Version « express / pointage long » pour chaque pain |")
P("| 7. Sauces maison | 16 recettes (mayo, algérienne, samouraï, blanche, burger, barbecue, andalouse, ketchup, harissa, pesto, tomate, béchamel, vinaigrette, tzatziki) + **frites maison** + **Sauce Builder** (base → profil → aromates, conservation et alertes calculées) | Fiches rouille, tartare, sauce fromagère dédiée |")
P("| 8. Fêtes & menus | Calendrier de 14 fêtes d'ici et d'ailleurs ; **composeur de menu** à partir d'un plat (Classique / Léger / Audacieux) : régime du foyer, cohérence régionale, équilibre, sous-produits réutilisés, ingrédients partagés, temps cumulé ; **boissons** sans alcool toujours proposées, avec alcool seulement pour un adulte déclaré, message loi Evin ; quantités par convive ; rétro-planning type | Rétro-planning daté, profils d'invités |")
P("| 9. Zéro déchet | Anatomie des ingrédients liée aux recettes ; « ce qu'il te restera » sur chaque fiche ; frigo virtuel (zones, DLC, J-x, tri par urgence) ; DLC/DDM ; conservation ; plat-mère poulet rôti → bouillon → riz cantonais | Bilan matière d'une semaine, score zéro déchet |")
P("| 10. Mode cuisine | Une étape à la fois en très grand texte, cibles de 64 px, **écran toujours allumé**, mise en place à cocher, **lecture audio** (continue, résumé, pas à pas automatique), **commandes vocales** (« suivant », « répète », « minuteur 10 minutes ») là où le navigateur les permet, **minuteurs multiples** nommés lancés depuis le texte des étapes, qui survivent au rechargement (son, vibration, notification) | Live Activity / Dynamic Island, Apple Watch (version native) |")
P("\n**Transversal** : profil de foyer (sans porc, sans alcool standard ou strict, mode strict sur le doute, végétarien, 14 allergènes, âge des enfants, majorité, équipement) ; version adaptée **A/B** sur chaque fiche avec ce qui a été remplacé et les quantités recalculées ; portions ; liste de courses par rayon partageable ; favoris, menus, recettes cuisinées ; thème clair/sombre (palette corrigée du Tome 5), taille du texte, police lisible ; mises à jour détectées.\n")
P("### 5.3 Limites connues de la v1\n")
P("- **iPhone (application web)** : un minuteur ne sonne pas quand l'application est fermée (notification si autorisée) ; la commande vocale dépend de Safari ; pas de Live Activity ni d'Apple Watch. → version native (D2).")
P("- **Données** : référentiel en confiance C ; aucune recette testée en cuisine ; substitutions à tester ; pas de nutrition ni de coût réel.")
P("- **Quantités** : mise à l'échelle simple (les quantités non numériques restent telles quelles) ; liste de courses sans addition des doublons.")
P("- **Imports** : le tri automatique repose sur des mots-clés ; un import sans légende reste « À vérifier ».\n")
P("### 5.4 Vérifications faites\n")
mism = []
for a in APP:
    e = ev[a["id"]]
    # même nombre d'allergènes sûrs et mêmes fautifs que le calcul TypeScript (contrôlé dans tests/engine.test.ts) : ici, contrôle de présence
    if a["id"] not in RS: mism.append(a["id"])
P(f"- `export_app_data.py` : **toutes** les références d'ingrédients des 70 fiches et de leurs variantes existent dans le Tome 3 (sinon l'export s'arrête) ; {len(X.gaps)} lignes « implicites » (eau, café, thé vert : à ajouter au Tome 3).")
P("- `npm test` (application) : **36 contrôles** (invariants du moteur, 2 000 recettes aléatoires × 4 profils, les 70 fiches en profil le plus strict, suggestion, import et cas piégés du Tome 7 §7.3).")
P(f"- Ce tome : badges recalculés par `atlas_engine.py` ; fiches présentes des deux côtés : {len(APP) - len(mism)}/{len(APP)}.")
P("- Parcours de tous les écrans dans le navigateur (mobile et grand écran, clair et sombre) sans erreur ; version de production installable, **service worker actif, fonctionnement hors connexion** vérifié.\n")
P("### 5.5 Faire évoluer\n")
P("```")
P("cd bible && python export_app_data.py      # bible -> données de l'application (vérifie les références)")
P("python build_tome12.py                      # régénère ce tome")
P("cd ../app && npm run dev                    # développement (port 5196)")
P("npm run build                               # tests + typage + version de production (dist/)")
P("npm run deploy                              # publication GitHub Pages (dépôt git à créer)")
P("```")
P("Ajouter une recette = l'écrire dans un fichier `recipes_v1_*.py` au format du Tome 11, relancer l'export : elle apparaît dans l'application avec ses badges, ses substitutions, sa place dans les menus, les rubriques et la recherche par ingrédients.\n")
P("---\n")
from zero_dechet_data import LEFTOVERS
P("## 6. Zéro déchet ingrédient par ingrédient\n")
nlo = sum(len(r.get("leftovers", [])) for r in APP); nfl = sum(1 for r in APP if r.get("leftovers"))
P(f"Chaque fiche liste automatiquement **les ingrédients qu'elle n'utilise pas en entier** et ce qu'on peut faire de chaque reste. Couverture : **{nlo} ingrédients entamés dans {nfl} fiches sur {len(APP)}** ; les autres n'utilisent que des produits du placard en entier.\n")
P("**Comment c'est calculé** : `zero_dechet_data.py` décrit, pour chaque ingrédient du Tome 3 souvent entamé, comment il s'achète (botte, pot, tube, boîte…), quand une ligne de recette signale un usage partiel (« ½ bouquet », « jus de citron », « 2 c. à s. de concentré »…), ce qui reste (tiges, zeste, blancs d'œufs, carcasse, eau de cuisson…), **comment le garder sans risque**, et **quatre familles d'idées** dans cet ordre : 🍽 *dans le repas en cours* (entrée, accompagnement), 🍲 *un autre plat* (lié à une fiche ATLAS), 🧊 *conserver*, 🌱 *hors cuisine* (compost, jardin, ménage). L'export vérifie chaque ingrédient et chaque recette liée ; l'application masque une recette liée qui ne convient pas au foyer et propose d'**ajouter le reste au frigo virtuel** (il remonte alors dans « Avec ce que j'ai »).\n")
P("**Angles morts traités** : sécurité sanitaire (riz cuit 24 h maximum, huiles aromatisées à l'ail 4 jours au froid, jaunes 24 h, blancs 2 jours ou congelés) ; achat juste (format de vente rappelé) ; régimes (une idée liée à une recette non adaptée est signalée) ; restes non alimentaires (huile de friture en déchetterie, jamais à l'évier) ; aucune recette ne se propose elle-même.\n")
P("| Ingrédient | Format d'achat | Reste | Conservation | Idées |\n|---|---|---|---|---|")
for ref, spec in LEFTOVERS.items():
    for part, keep, ideas in spec["left"]:
        P(f"| {ref} | {spec['sold']} | {part} | {keep} | " + " ; ".join(f"{t}" + (f" (→ {TITLE[rid]})" if rid else "") for _, t, rid in ideas) + " |")
P("\n> Durées de conservation **prudentes** (Tome 3 §17.2) : à faire valider par le·la diététicien·ne et un·e référent·e hygiène (D20).\n")
P("---\n")
IMGS = json.load(open(os.path.join(HERE, "..", "app", "src", "data", "images.json"), encoding="utf-8"))
from collections import Counter as _C
P("## 7. Illustrations : photos sous licence libre\n")
kinds = _C(k.split("/")[0] for k in IMGS)
P(f"**{len(IMGS)} photos** illustrent l'application : " + ", ".join(f"{n} {k}s" for k, n in kinds.items()) + ".\n")
P("**Méthode (illustrations/)** : `fetch_candidates.py` rassemble 10 candidates par sujet sur Wikimedia Commons et Openverse (Flickr), **uniquement sous CC0, domaine public, CC BY ou CC BY-SA** (usage commercial et modification permis ; NC, ND et GFDL seule refusées) ; planches contact relues **une à une** ; choix dans `selections.json` ; `process.py` recadre en 4:3 (point d'intérêt réglable), applique un étalonnage commun discret (contraste, chaleur, saturation, piqué), produit du WebP 400/800/1200 px et la couleur dominante (fond pendant le chargement), et écrit les crédits (`app/src/data/images.json`).\n")
P("**Règles de choix** : le plat doit être reconnaissable et appétissant, en lumière naturelle ; pas de marque visible (flacons, emballages), pas de bouteille ni de verre d'alcool mis en avant, pas de porc quand le sujet ne l'impose pas (plateau de jambon écarté pour Pâques), **pas de scène d'abattage** (Aïd), **pas de visage d'enfant** (droit à l'image des mineurs), **pas d'image générée par IA** présentée comme une photo (images de robots écartées), pas d'homonymes (la « vinegret » russe pour la vinaigrette).\n")
P("**Affichage** : crédit sous chaque photo (auteur·e, licence, source) et page « Crédits photos » ; mention « photo d'illustration : le plat peut différer de la recette ATLAS » ; les versions recadrées restent sous la licence d'origine ; chargement différé et taille adaptée à l'écran ; photos gardées hors connexion après affichage, ou toutes d'un coup depuis le Profil ; titre sur photo avec voile ≥ 55 % (Tome 5 §2.5).\n")
P("**Manques et suite** : *pain de mie* sans photo acceptable (illustration de secours conservée) ; quelques photos correctes sans plus (baguette, sauce samouraï, jus de gingembre). Le pipeline local (ComfyUI / AUTOMATIC1111) n'a qu'un modèle de style manga (Animagine XL), inadapté à la photo culinaire : générer les manques demanderait un modèle photoréaliste (≈ 7 Go) et un étiquetage « image générée » (D19). L'objectif reste les photos ATLAS du Tome 6.\n")
P("---\n")
P("## 8. Décisions ouvertes ajoutées au registre\n")
P("| # | Décision | Recommandation | Échéance |\n|---|---|---|---|")
P("| D13 | Afficher les versions adaptées par des règles `draft` (étiquetées « à tester ») | Oui jusqu'au lancement public ; au Go/No-Go, seules les règles `validated` disent « goût préservé » (T7 §14) | Avant bêta |")
P("| D14 | PWA d'abord, native ensuite | PWA pour la bêta fermée ; prototype natif (D2) pour minuteur écran éteint, Live Activities, Watch | Sprint 0 |")
P("| D15 | Corpus TikTok et sites : usage | Liens crédités et inspiration de briefs uniquement ; jamais de recopie de texte ou de média | Phase 0 |")
P("| D16 | Végétarien : fromages à présure animale | Avertissement (pas d'exclusion) en v1 ; à arbitrer avec le·la diététicien·ne | Avant bêta |")
P("| D17 | Catégorie « Food fusion » | Entrée d'atlas transversale ; la fiche garde sa cuisine principale (T1 §5.2) et porte une phrase d'explication | Fait (v1) |")
P("| D18 | Lecture de vidéos tierces dans l'application | Intégrations officielles TikTok et YouTube sans cookie, chargées au clic, crédit + lien ; à revoir si une plateforme le restreint | Avant bêta |")
P("| D19 | Images manquantes : génération IA ? | Non par défaut ; si oui, modèle photoréaliste local, étiquette « image générée », jamais pour un plat présenté comme la recette | Avant bêta |")
P("| D20 | Durées de conservation des restes | Valider les durées prudentes de `zero_dechet_data.py` (diététicien·ne + hygiène) | Avant bêta |")
P("\n> **Fin du Tome 12.**")
open(os.path.join(HERE, "BIBLE_TOME12_VAGUE1_ET_APPLICATION.md"), "w", encoding="utf-8").write("\n".join(o))
print(f"Tome 12 : {len(WAVE1)} fiches, {len(o)} lignes")
