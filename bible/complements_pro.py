# -*- coding: utf-8 -*-
"""Audit « chef professionnel senior » (12/11/2026, AUDIT_CHEF_PRO_2026-11-12.md). Appliqué par export_app_data.py
après les étapes réécrites :
- cuisson_a_coeur() : la volaille, la viande hachée, les saucisses et le porc cuits vite (poêle, gril, four, friture)
  reçoivent un repère de sécurité chiffré dans l'étape de cuisson quand la fiche n'en donnait aucun ;
- repos_viande() : les pièces de viande rouge saisies ou grillées reçoivent le temps de repos avant de trancher ;
- CORRECTIONS : températures de four et d'huile manquantes, allergène mal référencé, pesées en volume."""
import re, unicodedata

def _n(s):
    return unicodedata.normalize("NFD", s.replace("œ", "oe").replace("Œ", "Oe")).encode("ascii", "ignore").decode().lower()

POULTRY = re.compile(r"poulet|dinde|canard|pintade|caille|volaille")
MINCED = re.compile(r"hache|saucisse|merguez|chipolata|kefta|chair a saucisse|porc")
RED = re.compile(r"rumsteck|bavette|entrecote|cote de boeuf|steak|filet de boeuf|onglet|gigot|cotelettes d.agneau|agneau|chevre / cabri|rosbif")
CUE = re.compile(r"(6[3-9]|7\d|8[0-5]) ?.?c|jus (est )?clair|cuit[es]* a coeur|blancs? a coeur|chauds? a coeur|plus de rose|chair (est )?blanche|"
                 r"se detache|s.effiloch|se defait|tendre[s]? a la fourchette|s.ecrase|cuites? (a point|a coeur)")
COOK = re.compile(r"poel|grill|braise\b|plancha|saisi|rot[ie]|four|frit|frire|dore|dorer|cuire|cuis|cuit|mijot|poch|vapeur")
LONG = re.compile(r"mijot|brais|1 h|2 h|3 h|heure")

PROCESSED = re.compile(r"bouillon|fond |fumet|jambon|lardons|rillettes|terrine|pate de foie|bacon|fumee?|seche|confit|graisse|pastrami|knack|chorizo|magret|boudin|andouill")
COOKED_LABEL = re.compile(r"cuits?|cuites?|reste|roti|effiloche")

def _main_refs(d, rx):
    return [x for x in d["ing"] if x[2] and not x[2].startswith("SUB:") and x[3] >= 2 and rx.search(_n(x[2]))
            and not PROCESSED.search(_n(x[2])) and not COOKED_LABEL.search(_n(x[1] or ""))]

def _cook_step(steps, meat_rx, meat_rx2=None):
    """Index de la dernière étape de cuisson qui nomme la viande, sinon qui parle de viande, sinon la dernière cuisson."""
    serve = re.compile(r"^\*\*(servir|dresser|monter|garnir|finir|assembler|presenter|tacos|sandwich|accompagner)")
    cand = [i for i, s in enumerate(steps) if not serve.search(_n(s).strip())] or list(range(len(steps)))
    idx = [i for i in cand if COOK.search(_n(steps[i])) and meat_rx.search(_n(steps[i]))]
    if not idx and meat_rx2 is not None:
        idx = [i for i in cand if COOK.search(_n(steps[i])) and meat_rx2.search(_n(steps[i]))]
    if not idx:
        idx = [i for i in cand if COOK.search(_n(steps[i]))]
    return idx[-1] if idx else None

def cuisson_a_coeur(d):
    """Ajoute un repère de cuisson à cœur ; renvoie 'volaille' / 'hache' / None."""
    if d.get("kind") not in ("Plat", "Entrée") or d["region"].startswith("France › Sauces"):
        return None
    text = _n(" ".join(d["steps"]))
    if CUE.search(text):
        return None
    if _main_refs(d, POULTRY):
        kind, phrase = "volaille", "Volaille cuite à cœur : 74 °C au thermomètre, jus clair, chair sans trace rosée."
        rx = re.compile(r"poulet|volaille|dinde|canard|pintade|caille|escalope|blancs?|cuisses?|ailes?|pilons?|magret")
        rx2 = re.compile(r"viande|morceaux|lanieres")
    elif _main_refs(d, MINCED):
        sausage = any(re.search(r"saucisse|merguez|chipolata|porc|boudin|andouill", _n(x[2])) for x in _main_refs(d, MINCED))
        kind = "hache"
        phrase = ("Saucisses et porc cuits à cœur : 70 °C, plus de rose au centre." if sausage else
                  "Viande hachée : 70 °C à cœur, plus de rose, pour les enfants, les femmes enceintes et les personnes fragiles.")
        rx = re.compile(r"hache|boulette|saucisse|merguez|kefta|farce|porc|steak|galette|chipolata")
        rx2 = re.compile(r"viande|morceaux")
    else:
        return None
    # un long mijotage (plus de 40 min) cuit à cœur sans risque : pas de repère nécessaire
    if (d.get("repos") or 0) >= 40 and LONG.search(text):
        return None
    i = _cook_step(d["steps"], rx, rx2)
    if i is None:
        return None
    s = d["steps"][i].rstrip()
    d["steps"] = list(d["steps"][:i]) + [s + ("" if s.endswith((".", ":", ";")) else ".") + " " + phrase] + list(d["steps"][i + 1:])
    return kind

def repos_viande(d):
    """Repos des pièces de viande rouge saisies, grillées ou rôties ; renvoie True si ajouté."""
    if d.get("kind") != "Plat" or not _main_refs(d, RED):
        return False
    text = _n(" ".join(d["steps"]))
    if re.search(r"repos|reposer|repose", text) or re.search(r"mijot|brais|hach|emince|lanieres|wok|saute", text):
        return False
    i = None
    for k, s in enumerate(d["steps"]):
        if re.search(r"grill|saisi|rot[ie]|poel|braise\b|barbecue|plancha", _n(s)):
            i = k
    if i is None:
        return False
    s = d["steps"][i].rstrip()
    d["steps"] = list(d["steps"][:i]) + [s + ("" if s.endswith((".", ":", ";")) else ".") + " Repos 5 min sous aluminium avant de trancher : le jus se répartit."] + list(d["steps"][i + 1:])
    return True

# corrections ponctuelles : (id, ancien texte, nouveau texte) dans les étapes ; (id, libellé, nouvelle ligne) dans les ingrédients
STEP_FIX = [
 ("pizza_margherita", "Préchauffe au maximum (th. 9) avec la plaque dedans, 30 min.", "Préchauffe au maximum (250 à 280 °C, th. 9) avec la plaque dedans, 30 min."),
 ("flammekueche", "Au maximum avec la plaque dedans, 30 min.", "Au maximum (250 à 280 °C) avec la plaque dedans, 30 min."),
 ("kelewele", "**Frire.** Dorés et caramélisés.", "**Frire.** Huile à 170 °C, par petites quantités, 4 à 5 min : dorés et caramélisés ; égouttés sur papier."),
]
ING_FIX = {  # libellé exact → (quantité, libellé, référence)
 ("ha_kao", "d'amidon de blé"): ("100 g", "d'amidon de blé (contient du gluten)", "Farine de blé T45"),
 ("gateaux_de_lune_coco_matcha", "d'amidon de blé (ou fécule de maïs)"): ("30 g", "d'amidon de blé (ou fécule de maïs, sans gluten)", "Farine de blé T45"),
 ("ablo", "de riz cuit (bien tendre)"): ("200 g", "de riz cuit (bien tendre)", None),
 ("ablo", "de farine de maïs fine"): ("300 g", "de farine de maïs fine", None),
 ("ablo", "de fécule de maïs"): ("200 g", "de fécule de maïs", None),
 ("ablo", "de sucre"): ("100 g", "de sucre", None),
}

def apply(recipes):
    by = {d["id"]: d for d in recipes}
    for i, a, b in STEP_FIX:
        d = by[i]
        assert any(a in s for s in d["steps"]), (i, a)
        d["steps"] = [s.replace(a, b) for s in d["steps"]]
    for (i, label), (q, l2, ref) in ING_FIX.items():
        d = by[i]; hit = False; out = []
        for x in d["ing"]:
            if x[1] == label:
                hit = True
                x = (q, l2, ref if ref is not None else x[2]) + tuple(x[3:])
            out.append(x)
        assert hit, (i, label)
        d["ing"] = out
    stats = {"volaille": 0, "hache": 0, "repos": 0}
    for d in recipes:
        k = cuisson_a_coeur(d)
        if k: stats[k] += 1
        if repos_viande(d): stats["repos"] += 1
    return stats
