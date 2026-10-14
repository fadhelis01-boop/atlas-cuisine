# -*- coding: utf-8 -*-
import sys, re
from collections import OrderedDict
from load_ref import parse_tome3
from atlas_engine import *
from atlas_engine import _walk
from recipes_data import RECIPES

REF = parse_tome3()
ALLER = {"GL":"gluten","CR":"crustacés","OE":"œufs","PO":"poissons","AR":"arachide","SO":"soja","LA":"lait","FC":"fruits à coque",
         "CE":"céleri","MO":"moutarde","SE":"sésame","SU":"sulfites","LU":"lupin","MM":"mollusques"}
DISPO = {"🟢":"supermarché","🟡":"rayon monde / bio","🟠":"épicerie spécialisée","🔴":"difficile"}

# 1) référentiel -> objets Ingredient (tout est « C » : référentiel non vérifié)
ING = {}
for n, r in REF.items():
    ING[n] = Ingredient(n, {k: v for k, v in r["derivs"].items() if k in ("pork", "alcohol")}, set(r["allergens"]), "C")

def check_ref(name, rid):
    if name not in REF:
        close = [k for k in REF if name.split()[0].lower() in k.lower()][:5]
        raise SystemExit(f"[{rid}] référence introuvable : {name!r} ; proches : {close}")

# 2) recettes -> objets Recipe
RS = OrderedDict(); GAPS = []; HARD = OrderedDict()
for d in RECIPES:
    lines = []
    for qty, label, ref, w, opt in d["ing"]:
        if ref is None:
            GAPS.append((d["id"], label)); continue
        if ref.startswith("SUB:"):
            lines.append(Line(sub=ref[4:], weight=w)); continue
        check_ref(ref, d["id"])
        lines.append(Line(ing=ref, qty=0, weight=w, optional=opt))
        if REF[ref]["dispo"] in "🟠🔴": HARD.setdefault(ref, []).append(d["title"])
    RS[d["id"]] = Recipe(d["id"], lines)

# 3) règles issues des variantes (statut « validated » = SIMULATION pour afficher ce que serait le badge)
RULES = []
for d in RECIPES:
    for v in d["variantes"]:
        for orig, items in v["replace"].items():
            check_ref(orig, d["id"])
            for it, _ in items: check_ref(it, d["id"])
            if v["constraints"]:
                RULES.append(Rule(f'{d["id"]}:{orig}', orig, [(a, b) for a, b in items], set(v["constraints"]), "validated"))

def direct_rewrite(rec, replace):
    nl = []
    for ln in rec.lines:
        if ln.ing in replace:
            for it, ratio in replace[ln.ing]: nl.append(Line(ing=it, qty=0, weight=ln.weight, optional=ln.optional))
        else: nl.append(ln)
    return Recipe(rec.id + "#v", nl)

def lab(st): return {"ok": "✅", "ok_warning": "🟡", "adaptable": "🔄", "hidden": "⛔"}[st]
def fmt_allergens(res, maybe):
    s = ", ".join(ALLER[a] for a in sorted(res["allergens"])) or "aucun déclaré"
    m = ", ".join(ALLER[a] for a in sorted(maybe - res["allergens"]))
    return s + (f" ; **possibles selon marque** : {m}" if m else "")
def maybe_of(rec):
    m = set()
    for ln in _walk(rec, RS): m |= REF[ln.ing]["maybe"]
    return m
def pork_badge(st, off):
    return {"ok": "✅ Sans porc (calculé)", "uncertain": "🟡 Porc possible, à vérifier : " + ", ".join(off),
            "violates": "🐖 **Contient du porc** : " + ", ".join(off), "trace": "🟡"}[st]
def alc_badge(st, off):
    return {"ok": "✅ Sans alcool (calculé)", "trace": "🟡 **Traces d'alcool possibles** (fermentation/support) : " + ", ".join(off),
            "uncertain": "🟡 Alcool possible : " + ", ".join(off), "violates": "🍷 **Contient de l'alcool** : " + ", ".join(off)}[st]
def hm(m): return f"{m//60} h {m%60:02d}" if m >= 60 else f"{m} min"

ev = {rid: evaluate(r, ING, RS) for rid, r in RS.items()}

# 4) vérification croisée : variante calculée en direct == variante issue du moteur (apply_substitutions)
cross = []
for d in RECIPES:
    for v in d["variantes"]:
        direct = evaluate(direct_rewrite(RS[d["id"]], v["replace"]), ING, RS)
        if v["constraints"]:
            out = apply_substitutions(RS[d["id"]], RULES, ING, RS, set(v["constraints"]), True)
            eng = evaluate(out["recipe"], ING, RS) if out["adapted"] else None
            same = eng is not None and all(eng[k] == direct[k] for k in ("pork", "alcohol")) and eng["allergens"] == direct["allergens"]
            cross.append((d["id"], v["name"], out["adapted"], same))

# 5) démonstration de suggestion sur ces 10 recettes
PANTRY = {"Sel fin / gros sel / fleur de sel", "Poivre noir / blanc / vert", "Huile d'olive vierge extra", "Huile de tournesol / colza",
          "Sucre blanc / roux / cassonade / vergeoise", "Farine de blé T55", "Farine de blé T45", "Moutarde de Dijon", "Vinaigre de cidre"}
def sugg(have, expiring=()):
    flat = []
    for rid, r in RS.items():
        ls = [Line(ing=l.ing, weight=l.weight, optional=l.optional) for l in _walk(r, RS)]
        flat.append(Recipe(rid, ls))
    return suggest(flat, set(have), set(expiring), subs={}, staples=PANTRY)
S1 = sugg({"Cuisse / pilon de poulet", "Oignon jaune", "Citron", "Ail", "Riz long / basmati / thaï", "Olives (vertes / noires)",
           "Coriandre fraîche", "Persil plat / frisé", "Gingembre (poudre)", "Curcuma (poudre)"}, expiring={"Citron"})
S2 = sugg({"Lentilles corail", "Oignon jaune", "Ail", "Gingembre frais", "Tomate", "Cumin (graines / moulu)", "Curcuma (poudre)", "Citron", "Coriandre fraîche"})
S3 = sugg({"Œuf entier (frais)", "Lait entier / demi-écrémé / écrémé", "Farine de blé T45", "Beurre doux / demi-sel", "Huile de tournesol / colza"})
TITLE = {d["id"]: d["title"] for d in RECIPES}

# ----------------------------------------------------------------- rendu
o = []
P = o.append
P("# 📗 BIBLE ATLAS : TOME 11 (vague 0) : 11 fiches étalons\n")
P("> Première livraison du catalogue : **11 fiches étalons** (9 plats ou pains et 2 sauces, dont une hérite de l'autre) rédigées selon le Tome 6 (style), reliées au référentiel du Tome 3, avec **badges calculés par le moteur du Tome 8**.\n>")
P("> **Statut : « Brouillon rédactionnel prêt pour le Test 1 »**. Aucune de ces recettes n'a été **testée en cuisine** : les quantités et les temps sont ceux des pratiques usuelles et **doivent passer** le protocole du Tome 7 §2 (Test 1 chef·fe, Test 2 domestique) avant publication.\n>")
P("> **Lecture des badges** : ils sont **calculés** à partir du référentiel (niveau de confiance **C : non vérifié**, Tome 3 §1.5). Les **variantes** (sans porc, sans alcool, sans œuf) sont **à tester** : le calcul montre ce que serait le badge **si** la règle était validée ; elles ne peuvent **pas** être présentées comme « goût préservé » (Tome 7 §3.6).\n")
P("---\n")
P("## 1. Tableau récapitulatif (calculé)\n")
P("| # | Recette | Allergènes (sûrs) | Porc | Alcool | Sans porc Std / Strict | Sans alcool Std / Strict | Variantes |")
P("|---|---|---|---|---|---|---|---|")
for i, d in enumerate(RECIPES, 1):
    r = RS[d["id"]]; e = ev[d["id"]]
    al = ", ".join(sorted(e["allergens"])) or "–"
    pk = {"ok": "✅", "uncertain": "🟡", "violates": "🐖", "trace": "🟡"}[e["pork"]]
    ac = {"ok": "✅", "uncertain": "🟡", "violates": "🍷", "trace": "🟡 traces"}[e["alcohol"]]
    ps, pt = lab(availability(e, {"pork"}, False, RULES)), lab(availability(e, {"pork"}, True, RULES))
    as_, at = lab(availability(e, {"alcohol"}, False, RULES)), lab(availability(e, {"alcohol"}, True, RULES))
    P(f"| {i} | {d['title']} | {al} | {pk} | {ac} | {ps} / {pt} | {as_} / {at} | {len(d['variantes'])} |")
P("\n**Légende** : ✅ visible sans réserve · 🟡 visible avec avertissement · 🔄 visible avec version adaptée (règle à valider) · ⛔ masquée pour ce profil. **Std** = Standard, **Strict** = traces et incertitudes exclues (Tome 8 §1.2, ADR-007).\n")
P("> Lecture : la **mayonnaise**, la **sauce algérienne** (qui en hérite) et le **poulet yassa** ressortent ✅ en profil sans alcool **Standard** (traces tolérées, signalées) mais 🔄 en **Strict** : la **moutarde de Dijon** peut contenir du vin (`ALC~`). Les **crêpes** sont 🔄 dans les deux profils tant que le **rhum facultatif** figure dans la recette : un ingrédient facultatif **compte** (invariant I2). C'est le comportement voulu.\n")
P("---\n")
for i, d in enumerate(RECIPES, 1):
    r = RS[d["id"]]; e = ev[d["id"]]; mb = maybe_of(r)
    P(f"## {i+1}. {d['title']}\n")
    P(f"*{d['origin']} · {d['region']} · {d['kind']}*\n")
    P("| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |\n|---|---|---|---|---|---|")
    P(f"| {'⭐'*d['niveau']} ({['','Facile','Intermédiaire','Avancé'][d['niveau']]}) | {d['portions']} | {hm(d['actif'])} | {hm(d['repos'])} | **{hm(d['actif']+d['repos'])}** | {d['cost']} |\n")
    P("**Badges (calculés)**\n")
    P(f"- {pork_badge(e['pork'], e['offenders']['pork'])}")
    P(f"- {alc_badge(e['alcohol'], e['offenders']['alcohol'])}")
    P(f"- ⚠️ **Allergènes** : {fmt_allergens(e, mb)}")
    P(f"- ⚪ **Confiance C** : référentiel non vérifié (à relire avant publication)")
    P(f"- 👶 **Enfants** : {d['enfants']}\n")
    P(f"**Équipement** : {d['equip']}\n")
    P(f"{d['intro']}\n")
    P("### Ingrédients\n")
    P("| Quantité | Ingrédient | Réf. référentiel (Tome 3) | Disponibilité |\n|---|---|---|---|")
    for qty, label, ref, w, opt in d["ing"]:
        if ref is None: rr = "*implicite (hors référentiel)*"; dd = "🟢"
        elif ref.startswith("SUB:"): rr = f"*sous-recette : {TITLE[ref[4:]]}*"; dd = "–"
        else: rr = ref; dd = REF[ref]["dispo"]
        P(f"| {qty} | {label} | {rr} | {dd} |")
    P("\n### Étapes\n")
    for n, s in enumerate(d["steps"], 1): P(f"{n}. {s}")
    P("\n### Astuces et dépannage\n")
    for a in d["astuces"]: P(f"- {a}")
    if d["variantes"] or d["id"] == "mayonnaise":
        P("\n### Variantes et substitutions (à tester)\n")
        for v in d["variantes"]:
            direct = evaluate(direct_rewrite(r, v["replace"]), ING, RS)
            new_al = direct["allergens"] - e["allergens"]; lost = e["allergens"] - direct["allergens"]
            res = f"porc : **{direct['pork']}** · alcool : **{direct['alcohol']}**"
            if new_al: res += " · allergènes **introduits** : " + ", ".join(ALLER[a] for a in sorted(new_al))
            if lost: res += " · allergènes **retirés** : " + ", ".join(ALLER[a] for a in sorted(lost))
            P(f"**{v['name']}**\n\n{v['note']}\n\n*Calcul du moteur si la règle était validée* : {res}.\n")
    P(f"\n**Conservation** : {d['conservation']}\n")
    P("**Zéro déchet : que faire des restes**\n")
    for z in d["zero_dechet"]: P(f"- {z}")
    if d["accords_sa"] or d["accords_a"]:
        P("\n**Accords boissons**\n")
        if d["accords_sa"]: P("- *Sans alcool* : " + " ; ".join(d["accords_sa"]))
        if d["accords_a"]: P("- *Avec alcool (18 ans et plus, avec modération)* : " + " ; ".join(d["accords_a"]))
    P(f"\n**Techniques liées** : {', '.join(d['techniques'])}\n")
    P(f"**À valider au test** (Tome 7 §2) : {d['tests']}\n")
    P("---\n")

P("## 13. Démonstration du moteur de suggestion sur ces 11 fiches (calculée)\n")
P("*Placard supposé : sel, poivre, huiles, sucre, farine, moutarde de Dijon, vinaigre de cidre. Aucune substitution déclarée. Résultat réel du moteur du Tome 8 sur ces 11 fiches (paramètres non calibrés).*\n")
def tbl(S, title):
    P(f"**{title}**\n"); P("| Recette | Score | Section | Manque |\n|---|---|---|---|")
    for x in S: P(f"| {TITLE[x['id']]} | {x['score']} | {x['bucket']} | {', '.join(x['missing']) or '–'} |")
    P("")
tbl(S1, "Cas A : poulet, oignons, citron (à consommer vite), ail, riz, olives, coriandre, persil, gingembre et curcuma")
tbl(S2, "Cas B : lentilles corail, oignon, ail, gingembre frais, tomate, cumin, curcuma, citron, coriandre")
tbl(S3, "Cas C : œufs, lait, farine T45, beurre, huile")
P("> **Lecture du cas C** : la *mayonnaise* n'apparaît pas alors que l'on a des œufs et de l'huile : la fiche demande un **jaune d'œuf** (ingrédient structurant, distinct de l'**œuf entier** dans le référentiel) et du **citron**, absent de la liste ; le manque du jaune seul coûte déjà 15 points. Le moteur ne sait pas encore qu'*un œuf contient un jaune*. **Écart à combler** : relation « parent → partie » (œuf → jaune / blanc ; poulet → cuisse / blanc) dans le référentiel (Tome 3 §17.4, anatomie des ingrédients) et dans le moteur (Tome 8, annexe C).\n")

P("## 14. Rapport d'écarts avec le référentiel (Tome 3)\n")
P("Lignes **non couvertes** ou **sensibles** détectées en reliant les recettes au référentiel : à traiter avant de passer en niveau B/A.\n")
P("**Ingrédients absents du référentiel (marqués « implicites » ici)**\n")
if GAPS: P("- *Eau* : utilisée dans %d fiches ; à ajouter au Tome 3 (§1.2) avec attributs vides pour que le moteur ne la traite pas comme **inconnue** (elle est ignorée ici)." % len({g[0] for g in GAPS}))
P("\n**Ingrédients de disponibilité 🟠 / 🔴 utilisés (substitut exigé ou information « où trouver »)**\n")
for k, v in HARD.items(): P(f"- **{k}** ({REF[k]['dispo']}) : {', '.join(v)}")
P("\n**Cas révélés par le calcul**\n")
P("- **Moutarde de Dijon** : `ALC~?` (vin blanc/verjus) → en profil **sans alcool Strict**, *poulet yassa*, *mayonnaise* et *sauce algérienne* passent en 🔄 (version sans vin **à tester**) ; sans cette variante elles seraient ⛔ masquées. En profil Standard elles restent ✅ (traces signalées). Prévoir une **moutarde sans vin** au référentiel (graines de moutarde + vinaigre de cidre) et une recette de moutarde maison.")
P("- **Lardons** (bourguignon) : porc certain ; la règle « lardons de dinde + paprika fumé » est **à tester** (Tome 3 §16).")
P("- **Vin rouge** (bourguignon) : alcool certain ; la règle « jus de raisin + vinaigre de cidre » est **à tester**.")
P("- **Rhum** (crêpes) : facultatif, mais **compte** pour le régime (invariant I2) : la recette sort ✅ seulement sans rhum.")
P("- **Bouillon d'os maison** (`CE?`) : allergène possible (céleri) à vérifier selon la recette de bouillon.")
P("- **Guanciale** : porc certain → la carbonara est 🔄 (variante magret fumé, **à tester**), jamais ✅.")
P("\n**Contrôles de cohérence du moteur** (variante calculée directement vs variante issue de `apply_substitutions`)\n")
for rid, name, adapted, same in cross:
    P(f"- {TITLE[rid]} → *{name}* : adaptation acceptée = **{adapted}**, résultats identiques = **{same}**")
P("\n---\n")
P("## 15. Prochaines étapes pour ces 11 fiches\n")
P("| Étape | Qui | Critère |\n|---|---|---|\n| Test 1 (chef·fe, cuisine témoin) | Chef·fe exécutif·ve | Quantités et temps confirmés ; corrections reportées dans les données |\n| Test 2 (cuisine domestique, **2 testeur·se·s** pour niveau 2) | Panel Tome 7 §2.5 | Critères Tome 7 §2.4 |\n| Relecture diététique et référentiel | Diététicien·ne | Passage C → B → A |\n| Relecture culturelle | Consultant·e par région (Tome 6 §6) | Noms, contexte, fidélité |\n| Tests de goût des variantes | Panel ≥ 36 (Tome 7 §3) | Statut `validated` |\n| Photo + vidéo + audio | Équipe tournage (Tome 6 §9-16) | Checklist Tome 6 §16.4 |")
P("\n> **Rappel** : ces fiches sont des **briefs complets**, pas des recettes publiées. La publication exige les tests ci-dessus.")
open('/mnt/user-data/outputs/BIBLE_TOME11_VAGUE0_RECETTES_ETALONS.md','w',encoding='utf-8').write("\n".join(o))

# --------- résumé console pour contrôle
print("recettes:", len(RS), "| lignes:", len(o))
for d in RECIPES:
    e = ev[d["id"]]
    print(f"{d['id']:22s} porc={e['pork']:9s} alcool={e['alcohol']:9s} all={sorted(e['allergens'])} off_p={e['offenders']['pork']} off_a={e['offenders']['alcohol']}")
print("écarts (eau, etc.):", sorted(set(g[1] for g in GAPS)))
print("difficiles:", {k: v for k, v in HARD.items()})
print("cross:", cross)
print("S1:", [(x['id'], x['score'], x['bucket'], x['missing']) for x in S1])
print("S2:", [(x['id'], x['score'], x['bucket'], x['missing']) for x in S2])
print("S3:", [(x['id'], x['score'], x['bucket'], x['missing']) for x in S3])
