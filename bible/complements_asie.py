# -*- coding: utf-8 -*-
"""Audit « cuisinier senior, cuisines d'Asie » (12/11/2026, AUDIT_CUISINE_ASIATIQUE_2026-11-12.md). Appliqué par
export_app_data.py après l'audit fin gourmet et avant l'audit chef professionnel :
- region() : régions d'Asie rangées dans l'arborescence (« Chine (Sichuan) » → « Chine › Sichuan », plov en Asie centrale) ;
- FAUX_VEG : fiches étiquetées végétariennes qui portaient de la sauce de poisson ou du dashi à la bonite ;
- riz() : le rinçage (et le trempage du riz gluant) que chaque cuisine d'Asie fait avant de cuire le riz ;
- wok() : le repère du wok fumant et des petites fournées, sans lequel un sauté bout au lieu de sauter ;
- accords() : le thé ou la boisson de chaque pays, et un accord vin ou bière, pour les plats d'Asie qui n'en avaient pas."""
import re, unicodedata

def _n(s):
    return unicodedata.normalize("NFD", s.replace("œ", "oe")).encode("ascii", "ignore").decode().lower()

ASIE = ("Asie de l'Est", "Asie du Sud", "Asie du Sud-Est", "Asie centrale")

# ---------------------------------------------------------------- régions
_REGION_FIX = {"Asie du Sud › Ouzbékistan": "Asie centrale › Ouzbékistan", "Asie de l'Est": "Asie de l'Est › Cuisine de base"}

def region(d):
    r = d["region"]
    if r in _REGION_FIX:
        return _REGION_FIX[r]
    # « Asie du Sud › Inde (Goa) », « Europe du Sud › Italie (Sicile) » → « … › Inde › Goa », « … › Italie › Sicile » : toutes
    # les régions depuis le 12/11, la carte d'origine lit le pays et la région séparément ; pas les listes ni les sigles
    m = re.search(r" › ([^›(]+?) \(([^),]+)\)$", r)
    if m and m.group(2) != "RDC":
        r = r[:m.start()] + f" › {m.group(1)} › {m.group(2)}"
    return r

# ---------------------------------------------------------------- faux végétariens : (id, libellé) → (quantité, libellé, référence)
KOMBU = "Kombu / wakame"
FAUX_VEG = {
    ("kai_jeow", "de sauce de poisson (ou de soja)"): ("1 c. à s.", "de sauce soja claire (la sauce de poisson thaïe d'origine n'est pas végétarienne)", "Sauce soja claire"),
    ("kimchi_jjigae_tofu", None): ("50 cl", "d'eau et une feuille de kombu (le dashi à la bonite n'est pas végétarien)", KOMBU),
    ("tteokbokki", "de dashi ou d'eau"): ("50 cl", "d'eau et une feuille de kombu (le dashi à la bonite n'est pas végétarien)", KOMBU),
    ("curry_vert_tofu_legumes", "de pâte de curry vert"): ("2 c. à s.", "de pâte de curry vert sans crevettes (lis l'étiquette : beaucoup en contiennent)", None),
}
FAUX_VEG_STEP = {"tteokbokki": ("**Sauce.** Dashi,", "**Sauce.** Kombu 20 min dans l'eau froide, retiré au premier frémissement ; puis"),
                 "kai_jeow": ("Œufs, sauce de poisson,", "Œufs, sauce soja,")}
FAUX_VEG_INTRO = {"kai_jeow": ("battus à la sauce de poisson,", "battus à la sauce de poisson (ici au soja, pour rester végétarienne),")}

# ---------------------------------------------------------------- riz : (id) → (motif de l'étape, phrase ajoutée) ; None = remplace l'étape
_JP = "Riz rond rincé 3 ou 4 fois en frottant jusqu'à eau presque claire, égoutté 30 min, cuit avec 1,1 fois son volume d'eau : grains brillants, qui se tiennent sans coller."
_LONG = "Riz rincé à l'eau froide jusqu'à eau presque claire, cuit par absorption (voir « Cuire le riz ») : grains détachés."
RIZ = {
    "poulet_teriyaki": (r"riz", _JP), "saumon_teriyaki": (r"riz", _JP), "bibimbap": (r"riz", _JP), "yasai_kare": (r"riz", _JP),
    "oyakodon": (r"servir", _JP), "katsudon_poulet": (r"riz", _JP),
    "agedashi_tofu": (r"servir", "Avec un bol de riz : " + _JP[0].lower() + _JP[1:]), "doenjang_jjigae": (r"riz", _JP), "nasu_dengaku": (r"gratiner", "Avec un bol de riz : " + _JP[0].lower() + _JP[1:]),
    "kimbap": (r"^\*\*riz", "Avant : riz rond rincé jusqu'à eau presque claire, égoutté 30 min, cuit avec 1,1 fois son volume d'eau ; étalé tiède pour l'assaisonner."),
    "onigirazu": (r"^\*\*riz", "Avant : riz rond rincé jusqu'à eau presque claire, égoutté 30 min, cuit avec 1,1 fois son volume d'eau, assaisonné encore chaud."),
}
RIZ_REPLACE = {"mango_sticky_rice": ("**Vapeur.** Riz égoutté, 25 min.",
    "**Tremper puis vapeur.** Riz gluant rincé, trempé 4 h (ou une nuit) dans l'eau froide, égoutté ; 25 min à la vapeur dans un linge humide, retourné à mi-cuisson : grains translucides, tendres et collants. Sans trempage, il reste dur au cœur.")}

def riz(d):
    i = d["id"]
    if i in RIZ_REPLACE:
        a, b = RIZ_REPLACE[i]
        assert a in d["steps"], (i, a)
        d["steps"] = [b if s == a else s for s in d["steps"]]
        return True
    if i not in RIZ:
        return False
    rx, phrase = RIZ[i]
    idx = [k for k, s in enumerate(d["steps"]) if re.search(rx, _n(s))]
    assert idx, (i, rx)
    k = idx[0]
    s = d["steps"][k].rstrip()
    d["steps"] = list(d["steps"][:k]) + [s + ("" if s.endswith((".", ":", ";")) else ".") + " " + phrase] + list(d["steps"][k + 1:])
    return True

# ---------------------------------------------------------------- wok
WOK_CUE = re.compile(r"fum|feu vif|tres chaud|tres vif|fumant|feu maximal|feu fort")
WOK_PHRASE = "Wok fumant, feu vif : par petites fournées (300 g au plus à la fois), sinon tout rend son eau et bout au lieu de sauter."
WOK_SAUF = re.compile(r"curry|kai_jeow|kadai")  # currys mijotés au wok (ou au kadai) et omelette frite : pas de sauté
WOK_ETAPE = {"mapo_tofu": 1, "oeufs_tomates_chinois": 0, "zha_jiang_mian": 0}  # l'étape sautée ne dit pas « sauter »

def wok(d):
    if not d["region"].startswith(ASIE) or WOK_SAUF.search(d["id"]):
        return False
    text = _n(" ".join(d["steps"]))
    if "wok" not in _n(d.get("equip") or "") + text or WOK_CUE.search(text):
        return False
    bad = re.compile(r"a sec|blanchi|frire|friture|1[6-8]0 .?c|(^|\W)marin")
    steps = [_n(s) for s in d["steps"]]
    k = next((k for k, s in enumerate(steps) if re.search(r"(^|\W)saut|wok", s) and not bad.search(s)), None)
    if k is None:
        k = WOK_ETAPE.get(d["id"])
    if k is None:
        k = next((k for k, s in enumerate(steps) if re.search(r"saisi|revenir|poel|dore", s) and not bad.search(s)), None)
    if k is None:
        return False
    s = d["steps"][k].rstrip()
    d["steps"] = list(d["steps"][:k]) + [s + ("" if s.endswith((".", ":", ";")) else ".") + " " + WOK_PHRASE] + list(d["steps"][k + 1:])
    return True

# ---------------------------------------------------------------- accords : (pays, boisson sans alcool)
_THE = [("Chine", "thé oolong ou thé vert au jasmin, servi chaud"), ("Japon", "thé vert sencha ou genmaicha (thé au riz grillé)"),
        ("Corée", "thé d'orge grillée (boricha), chaud ou glacé"), ("Mongolie", "thé au lait légèrement salé (suutei tsai)"),
        ("Thaïlande", "thé glacé à la citronnelle ; eau de coco"), ("Vietnam", "thé vert glacé (trà đá) ; jus de canne au citron vert"),
        ("Birmanie", "thé noir au lait concentré"), ("Indonésie", "thé au jasmin sucré (teh manis)"), ("Malaisie", "teh tarik (thé au lait tiré)"),
        ("Singapour", "teh tarik (thé au lait tiré)"), ("Philippines", "calamansi juice (citron vert sucré)"),
        ("Népal", "thé masala au lait"), ("Bangladesh", "borhani (babeurre épicé à la menthe)"), ("Inde", "lassi nature ou chaas (babeurre au cumin)"),
        ("Pakistan", "lassi salé"), ("Sri Lanka", "thé de Ceylan"), ("Ouzbékistan", "thé vert (kok choy)"), ("Asie centrale", "thé vert (kok choy)")]

def accords(d):
    """(alcool, sans_alcool) pour un plat ou une entrée d'Asie qui n'en a pas ; None sinon."""
    reg = d["region"]
    if not reg.startswith(ASIE) or d.get("kind") not in ("Plat", "Entrée"):
        return None
    sa = next((t for p, t in _THE if p in reg), "thé vert ou thé au jasmin")
    prof = set(d.get("profil") or [])
    if "epice" in prof:
        vin = "un riesling ou un gewurztraminer à peine doux (le sucre calme le piment) ; ou une bière blonde légère"
    elif "poisson" in prof:
        vin = "un saké junmai servi frais, ou un riesling sec" if "Japon" in reg or "Corée" in reg else "un riesling sec ou un muscadet"
    elif "viande_rouge" in prof:
        vin = "un pinot noir léger, servi frais"
    else:
        vin = "une bière blonde légère ou un blanc sec et aromatique (pinot gris)"
    return [vin], [sa]

def apply(recipes):
    by = {d["id"]: d for d in recipes}
    for (i, label), (q, l2, ref) in FAUX_VEG.items():
        d = by[i]; hit = False; out = []
        for x in d["ing"]:
            if (label is not None and x[1] == label) or (label is None and (x[2] or "").startswith("Dashi")):
                hit = True
                x = (q, l2, ref if ref is not None else x[2]) + tuple(x[3:])
            out.append(x)
        assert hit, (i, label)
        d["ing"] = out
    for i, (a, b) in FAUX_VEG_STEP.items():
        assert any(a in s for s in by[i]["steps"]), (i, a)
        by[i]["steps"] = [s.replace(a, b) for s in by[i]["steps"]]
    for i, (a, b) in FAUX_VEG_INTRO.items():
        assert a in by[i]["intro"], (i, a)
        by[i]["intro"] = by[i]["intro"].replace(a, b)
    stats = {"regions": 0, "riz": 0, "wok": 0, "accords": 0}
    for d in recipes:
        r = region(d)
        if r != d["region"]:
            d["region"] = r; stats["regions"] += 1
        if riz(d): stats["riz"] += 1
        if wok(d): stats["wok"] += 1
        ac = accords(d) if not (d["accords_a"] and d["accords_sa"]) else None
        if ac:
            if not d["accords_a"]: d["accords_a"] = list(ac[0])
            if not d["accords_sa"]: d["accords_sa"] = list(ac[1])
            stats["accords"] += 1
    return stats
