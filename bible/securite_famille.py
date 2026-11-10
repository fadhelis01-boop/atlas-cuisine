# -*- coding: utf-8 -*-
"""Audit chef + famille du 10/11/2026 : règles calculées à l'export, pour qu'aucune fiche (ancienne ou future) n'y échappe.

1. Lignes composées (« 40 g de beurre + 40 g de farine ») séparées en vraies lignes quand chaque morceau est un ingrédient
   connu : la farine arrive dans la liste de courses et son gluten dans les allergènes.
2. Allergènes écrits dans le libellé mais absents de l'ingrédient de référence (« coriandre et cacahuètes ») : ajoutés à la
   ligne ; ceux d'une alternative (« ou de cacahuètes ») comptent comme « peut contenir ».
3. Conservation par famille d'aliment : poisson et fruits de mer, riz cuit, mayonnaise maison, œufs coulants.
4. « À lancer la veille » : trempage, marinade longue, décongélation, riz cuit la veille, dessalage, pâte qui lève longtemps.
"""
import re, unicodedata

def nrm(s):
    return unicodedata.normalize("NFD", (s or "").lower().replace("œ", "oe")).encode("ascii", "ignore").decode()

# ———————————————————————————————— 1. lignes composées
# morceau (normalisé, sans quantité) → ingrédient de référence ; l'ordre compte (le plus précis d'abord)
PARTS = [
    (r"^(de )?farine", "Farine de blé T55"), (r"branches? de celeri|^(de )?celeri$", "Céleri-branche"), (r"celeri-rave", "Céleri-rave"),
    (r"gousses? d.ail|^(d.)?ail$", "Ail"), (r"petits oignons", "Oignon jaune"), (r"^(d.)?oignons?\b", "Oignon jaune"), (r"carottes?", "Carotte"),
    (r"clous? de girofle", "Clou de girofle"), (r"bouquet garni|feuilles? de laurier", "Laurier"), (r"branches? de thym|^(de )?thym", "Thym / romarin"),
    (r"huile de sesame", "Huile de sésame (grillée)"), (r"^(d.)?huile", "Huile de tournesol / colza"), (r"^(de )?sucre", "Sucre blanc / roux / cassonade / vergeoise"),
    (r"persil", "Persil plat / frisé"), (r"jaunes?( d.oeufs?)?$", "Jaune d'œuf"), (r"cacahuetes?", "Cacahuète / arachide"), (r"sesame", "Sésame (blanc/noir)"),
    (r"^(de )?lait$", "Lait entier / demi-écrémé / écrémé"), (r"coriandre moulue", "Coriandre (graines)"), (r"quatre-epices", "Quatre-épices"),
    (r"paprika", "Paprika doux"), (r"fleur d.oranger", "Eau de fleur d'oranger"), (r"zeste de citron", "Citron"), (r"champignons", "Champignon de Paris"),
    (r"a l.ancienne", "Moutarde à l'ancienne"), (r"^(de )?sel$", "Sel fin / gros sel / fleur de sel"), (r"safran", "Safran (pistils)"),
    (r"gingembre", "Gingembre frais"), (r"^(de )?beurre$", "Beurre doux / demi-sel"),
]
QTY = r"(\d+(?:[,.]\d+)?(?:\s?[½¼¾])?|[½¼¾]|une?|quelques)"
UNIT = r"(?:\s?(?:g|kg|cl|ml|l|c\. à s\.|c\. à c\.|pincées?)(?![\wà-ÿ]))?"

def _part_ref(text, known):
    t = nrm(text).strip(" ,.")
    for rx, ref in PARTS:
        if re.search(rx, t) and ref in known: return ref
    return None

def split_line(ln, known):
    """Une ligne « A + qté B (+ qté C) » → plusieurs lignes, ou None si un morceau ne correspond à rien de connu."""
    label = ln["label"]
    if " + " not in label or re.search(r"\([^)]*\+[^)]*\)", label) or re.search(r"\bou\b", label): return None
    pieces = label.split(" + ")
    first, rest = pieces[0], pieces[1:]
    out = []
    for p in rest:
        m = re.match(rf"^{QTY}{UNIT}\s*(.*)$", p.strip())
        if not m: return None
        body = m.group(2) or ""
        qty = p.strip()[: len(p.strip()) - len(body)].strip()
        ref = _part_ref(body, known)
        if not ref or not body.strip(): return None
        out.append({"qty": qty, "label": body.strip(), "ref": ref, "weight": 1, "optional": ln["optional"]})
    # le premier morceau garde la ligne d'origine (sa référence ne change pas)
    head = dict(ln, label=first.strip())
    return [head] + out

def split_composites(recipes, known):
    n = 0
    for r in recipes:
        new = []
        for ln in r["ingredients"]:
            parts = split_line(ln, known) if ln.get("ref") and not str(ln["ref"]).startswith("SUB:") else None
            if parts:
                n += 1
                new.extend(parts)
            else:
                new.append(ln)
        r["ingredients"] = new
    return n

# ———————————————————————————————— 2. allergènes du libellé
ALLERGEN_WORDS = {
    "CE": r"celeri", "AR": r"cacahuetes?|arachide", "SE": r"sesame|tahini", "MO": r"moutarde",
    "FC": r"\bamandes?\b|\bnoix\b(?! de (coco|muscade|palme|beurre|veau|saint))|noisettes?\b(?! de beurre)|pistaches?|cajou|pecan|macadamia",
    "LA": r"(?<!de )\blait\b(?! de (coco|soja|riz|amande|avoine))|\bbeurre\b(?! de (cacahuete|karite)| d.amande)|\bcreme\b(?! de coco)|fromage|yaourt|parmesan|mozzarella|feta|cheddar",
    "GL": r"\bfarine\b(?! de (riz|mais|pois|manioc|sarrasin|coco|chataigne|teff))|\bpain\b|chapelure|panko",
    "OE": r"\boeufs?\b|jaunes? d.oeuf", "PO": r"gelatine de poisson|nuoc|sauce de poisson|anchois", "CR": r"crevettes?",
}
def label_allergens(label, ref_allergens):
    """(sûrs, possibles) : allergènes nommés dans le libellé et absents de l'ingrédient de référence."""
    t = nrm(label)
    alt = re.split(r"\bou\b", t, maxsplit=1)
    sure, maybe = set(), set()
    for code, rx in ALLERGEN_WORDS.items():
        if code in ref_allergens: continue
        if re.search(r"sans (" + rx + ")", t): continue
        if re.search(rx, alt[0]): sure.add(code)
        elif len(alt) > 1 and re.search(rx, alt[1]): maybe.add(code)
    # la noix de muscade, la noix de coco, le beurre de cacahuète (déjà AR) : réglés par les expressions ci-dessus
    return sorted(sure), sorted(maybe)

def raw_egg_text(r):
    """La fiche dit elle-même qu'elle contient de l'œuf cru (tiramisu, mousse, sabayon…)."""
    return bool(re.search(r"oeufs? crus?|jaunes? crus?|blancs? crus?", nrm(" ".join(r.get("tips") or []) + " " + (r.get("kids") or ""))))

# ———————————————————————————————— 3. conservation par famille d'aliment
DEFAULT_KEEP = "3 jours au frigo, dans une boîte fermée."
def keep_rule(r, sections, sub_keeps):
    """Durée de conservation au frigo (en jours, 0 = à manger tout de suite) imposée par les ingrédients, et la raison."""
    rules = []
    refs = [ln["ref"] or "" for ln in r["ingredients"]]
    labs = nrm(" ".join(ln["label"] for ln in r["ingredients"]))
    steps = nrm(" ".join(r["steps"]))
    if any("Poissons" in sections.get(x, "") for x in refs):
        shell = re.search(r"moules?|palourdes?|coques?|huitres?|crevettes?|crabe|homard|langoust|calamar|encornet|seiche|poulpe|saint-jacques", labs)
        rules.append((1, "fruits de mer : 24 h au plus") if shell else (2, "poisson cuit : 2 jours au plus"))
    if r["role"] in ("plat", "entree") and any(x.startswith("Riz") for x in refs) and not re.search(r"riz au lait|teurgoule", nrm(r["title"])):
        rules.append((1, "riz cuit : 24 h au plus, refroidi vite, à cause de la bactérie Bacillus cereus"))
    if "SUB:mayonnaise" in refs or r["id"] == "mayonnaise" or re.search(r"mayonnaise maison", labs) or raw_egg_text(r):
        rules.append((1, "œuf cru : 24 h au plus, au froid"))
    if re.search(r"oeufs? mollets?|oeufs? poches?|jaune coulant|oeufs? coulants?", steps + " " + labs) and r["role"] in ("plat", "entree"):
        rules.append((1, "œufs coulants : à manger tout de suite, le reste du plat 24 h"))
    for sid, (days, why) in sub_keeps:
        rules.append((days, why))
    return min(rules) if rules else None

def apply_keep(r, rule):
    """Remplace le texte par défaut, ou ramène une durée trop longue à la règle (la congélation éventuelle est gardée)."""
    if not rule: return False
    days, why = rule
    s = r["storage"] or DEFAULT_KEEP
    label = "24 h" if days == 1 else f"{days} jours"
    if s.startswith(DEFAULT_KEEP):
        r["storage"] = f"{label} au frigo au plus, dans une boîte fermée ({why})." + s[len(DEFAULT_KEEP):]
        return True
    m = re.search(r"(\d+) jours?", s)
    if m and int(m.group(1)) > days:
        r["storage"] = s[: m.start()] + label + s[m.end():] + f" ({why})"
        return True
    if re.search(r"(\d+) semaines?|1 semaine|1 mois", s):
        r["storage"] = re.sub(r"(\d+ semaines?|1 semaine|1 mois)", label, s, count=1) + f" ({why})"
        return True
    return False

# ———————————————————————————————— 4. à lancer la veille, ou à prévoir avant
VEILLE = [
    (r"trempee?s? (la veille|24 ?h|12 ?h|une nuit|toute la nuit|8 ?h)|a tremper la veille|secs? trempee?s?|\(crues?, trempee?s?\)", "faire tremper"),
    (r"cuite?s? la veille|cuite?s? \(la veille\)|\(de la veille\)|de la veille, froid", "cuire la veille (riz, pommes de terre, tortilla…)"),
    (r"\(la veille\)", "préparer une partie la veille"),
    (r"dessal", "dessaler"),
    (r"decongel|surgele[^.]*une nuit", "décongeler au frigo"),
    (r"(mariner|marinade|marine)\W{0,4}[^.]{0,60}?(?<!ou )(une nuit|toute la nuit|la veille|(?:[4-9]|1\d|2\d) ?h\b)", "lancer la marinade"),
    (r"(une nuit|la veille)[^.]{0,40}(au frais|au frigo|de repos)", "préparer la base la veille"),
]
def _clean(t):
    t = nrm(t).replace("**", " ")
    return re.sub(r"\((?:ou|jusqu.a)[^)]*\)", " ", t)  # « (ou une nuit) », « (jusqu'à une nuit) » : facultatif
def veille_of(r):
    """Ce qu'il faut lancer la veille pour que le plat soit prêt à l'heure : texte court, ou None."""
    raw = nrm(" ".join(f"{ln['qty']} {ln['label']}" for ln in r["ingredients"])) + " . " + nrm(" ".join(r["steps"])).replace("**", " ")
    txt = _clean(" ".join(f"{ln['qty']} {ln['label']}" for ln in r["ingredients"])) + " . " + _clean(" ".join(r["steps"]))
    out = []
    for rx, task in VEILLE:
        src = raw if task.startswith(("cuire la veille", "préparer une partie")) else txt
        if re.search(rx, src) and task not in out: out.append(task)
    return " ; ".join(out) or None

def _mins(n, u):
    return int(n) * 60 if u.startswith("h") else int(n)
def avance_of(r):
    """Minutes à prévoir avant de cuisiner (marinade, repos au frais, dégorger, pousse) quand le temps annoncé ne les compte pas."""
    txt = _clean(" ".join(r["steps"]))
    need = 0
    for m in re.finditer(r"(mariner|marinade|marine|au frais|au frigo|degorger|degorge|lever|pousse)\W{0,6}[^.]{0,60}?(\d+) ?(h|min)\b|(\d+) ?(h|min)\b[^.;]{0,15}(au frais|au frigo|de marinade)", txt):
        n, u = (m.group(2), m.group(3)) if m.group(2) else (m.group(4), m.group(5))
        need = max(need, _mins(n, u))
    return need if need >= 30 and need > r["rest"] else 0


# ———————————————————————————————— 5. congélation (cuisine en lot)
def freeze_note(r):
    """Les plats mijotés en sauce se congèlent : la mention manque sur la plupart des fiches (audit chef + famille)."""
    st = nrm(r["storage"] or "")
    if r["role"] not in ("plat", "entree") or re.search(r"congel", st) or r.get("rawEgg"): return None
    title, steps = nrm(r["title"]), nrm(" ".join(r["steps"]))
    labs = nrm(" ".join(ln["label"] for ln in r["ingredients"]))
    if not re.search(r"mijot|fremiss|brais|a couvert|couvercle|cocotte|feu doux|petit feu|compote|reduit|\d ?h\b", steps) or r["rest"] < 30: return None
    if re.search(r"salade|frit|friture|pane|croustillant|tempura|beignet|sushi|tartare|carpaccio|gratin|risotto|omelette|\boeufs?\b|souffle|quiche|tarte|roti|wellington|laque|farci", title): return None
    if re.search(r"\bfrire\b|friture|creme fouettee|mayonnaise", steps + " " + labs): return None
    if any((ln["ref"] or "").startswith(("Crevettes", "Moules", "Calamar", "Poulpe")) for ln in r["ingredients"]): return None
    side = " (sans les pommes de terre, les pâtes ni le riz, à cuire au moment)" if re.search(r"pomme de terre|pates|riz|nouilles|semoule", labs) else ""
    return f"Se congèle 3 mois{side} : à décongeler une nuit au frigo, à réchauffer à feu doux jusqu'à frémissement."


# ———————————————————————————————— 6. lait cru (grossesse), participation des enfants, desserts légers
RAW_MILK = {"Camembert / brie", "Roquefort / bleu", "Reblochon / raclette / mont-d'or"}
def raw_milk_tip(r):
    if not any(ln["ref"] in RAW_MILK for ln in r["ingredients"]): return None
    if any("enceinte" in nrm(t) for t in r["tips"]): return None
    cooked = re.search(r"four|gratin|fondu|fond|200 ?°c|180 ?°c|bouillant", nrm(" ".join(r["steps"])))
    return ("Femme enceinte : ces fromages sont souvent au lait cru ; le plat doit être brûlant à cœur (listeria), ou prends une version au lait pasteurisé."
            if cooked else "Femme enceinte : fromage souvent au lait cru, à remplacer par une version au lait pasteurisé (listeria).")

# ce qu'un enfant peut faire, avec l'âge (repères des ateliers cuisine pour enfants) ; jamais le feu, le four ni le couteau pointu
KID_TASKS = [
    (r"\blave|rince|egoutte les (salades|feuilles)", 3, "laver les légumes"), (r"effeuill|cisel\w* (le |les )?(persil|coriandre|basilic|menthe|ciboulette)", 3, "effeuiller les herbes"),
    (r"melang|remu\w+ (la pate|le tout)|fouett", 3, "mélanger, fouetter"), (r"casse[rz]? (les |\d+ )?oeufs|oeufs? battus?", 4, "casser les œufs"),
    (r"boulettes?|facon\w+|roule[rz]? (en|des) boules?|former? des boules", 4, "façonner les boulettes ou les boules"),
    (r"etale[rz]? la pate|abaiss|garni[rs]? (les|la) (pate|pizza|tarte)", 5, "étaler la pâte, garnir"), (r"pese[rz]?|mesure[rz]?", 6, "peser et mesurer"),
    (r"rape[rz]? (le |du )?(fromage|parmesan|carotte|courgette)", 7, "râper (râpe à main, doigts loin)"), (r"presse[rz]? (le |les )?(citron|agrume)", 4, "presser les citrons"),
]
def kid_help(r):
    if r["role"] in ("boisson",): return None
    t = nrm(" ".join(r["steps"]))
    tasks = [(a, x) for rx, a, x in KID_TASKS if re.search(rx, t)]
    if not tasks: return None
    tasks.sort()
    return "Les enfants peuvent aider : " + ", ".join(f"{x} (dès {a} ans)" for a, x in tasks[:4]) + "."

FRUIT_SECTIONS = ("Fruits",)
def light_dessert(r, sections):
    """Dessert du quotidien : fruit en vedette, peu de sucre, sans pâte ni crème riche."""
    # un dessert de fête marqué « léger » sortirait dans tous les menus de fête (test 79) : on ne touche qu'aux desserts du quotidien
    if r["role"] != "dessert" or "fetes" in r.get("cats", []): return False
    main = [ln for ln in r["ingredients"] if ln["weight"] >= 3]
    fruit = any(sections.get(ln["ref"] or "", "").startswith(FRUIT_SECTIONS) or re.search(r"yaourt|fromage blanc|compote", nrm(ln["label"])) for ln in main)
    heavy = any(re.search(r"^(Beurre|Crème|Mascarpone|Chocolat|Farine|Pâte|Lait concentré)", ln["ref"] or "") and ln["weight"] >= 2 for ln in r["ingredients"])
    return fruit and not heavy and r["actif"] + r["repos"] <= 45 if "actif" in r else fruit and not heavy and r["active"] + r["rest"] <= 45
