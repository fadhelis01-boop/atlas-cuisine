# -*- coding: utf-8 -*-
"""Audit gourmet (21/10/2026) §4.2 : estimation des protéines par part d'un plat, toutes sources comprises (viande, poisson,
œufs, fromage, tofu, légumineuses, céréales), avec son accompagnement relié. Densités : repères CIQUAL arrondis (g pour
100 g cru, conserve égouttée). Les quantités non chiffrées (« 1 bouquet ») sont ignorées : c'est un ordre de grandeur, pas
une analyse nutritionnelle. Affiché sur la fiche (« ≈ 25 g de protéines par part ») et dans le repère d'équilibre."""
import re, unicodedata
def norm(s):
    s = s.replace("œ", "oe").replace("Œ", "oe").replace("æ", "ae")
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")
# g de protéines pour 100 g (repères CIQUAL arrondis), cherchés dans « réf + libellé », du plus précis au plus large
DENS = [
 (r"viande sechee|grisons|bresaola|jambon cru|serrano|coppa", 30), (r"jambon|blanc de dinde|bacon de dinde|jambon de dinde", 18), (r"guanciale|lardon|poitrine|pancetta|chorizo|saucisse|merguez|chipolata|boudin|bacon", 14),
 (r"saumon fume|truite fumee", 22), (r"thon", 25), (r"sardines? (a l.huile|en boite)|maquereaux? (en boite|fume)", 22), (r"moule|coque|palourde|vongole", 12), (r"crevette|gambas|langoust|saint.jacques|calamar|seiche|poulpe|crabe", 18),
 (r"anchois", 25), (r"morue|cabillaud|lieu|merlu|colin|saumon|truite|bar\b|dorade|sole|maquereau|sardine|poisson|haddock|tilapia|espadon|lotte|rouget|eglefin|merlan", 19),
 (r"poulet|volaille|dinde|canard|pintade|caille|lapin|boeuf|veau|agneau|mouton|porc|viande|steak|gigot|epaule|jarret|joue|paleron|bavette|entrecote|filet mignon|escalope|cote|foie|rognon|langue|tripe|chevreau|chevre fraiche viande|haché|hache", 20),
 (r"jaunes? d.oeufs?", 16), (r"blanc d.oeuf|blancs d.oeufs", 11), (r"(?<!b)oeufs?", 13),
 (r"parmesan|pecorino|grana|comte|gruyere|emmental|beaufort|cantal|mimolette|manchego|gouda|cheddar|abondance|tomme", 27),
 (r"raclette|reblochon|camembert|brie|munster|morbier|mozzarella|scamorza|halloumi|paneer|fromage|chevre|roquefort|bleu|gorgonzola|burrata", 20), (r"feta", 15), (r"ricotta|mascarpone", 9),
 (r"yaourt grec|skyr|fromage blanc|faisselle", 9), (r"yaourt|kefir", 4), (r"lait de coco|creme de coco", 2), (r"creme|beurre|ghee|huile", 0), (r"lait", 3.3),
 (r"tofu soyeux", 5), (r"tofu|tempeh", 13), (r"seitan", 25), (r"edamame", 11),
 (r"(haricots?|pois chiches?|lentilles?|feves?|flageolets?|pois casses?|azukis?|mungo|cocos?).*(boite|bocal|cuit|conserve)|(boite|bocal|conserve).*(haricots?|pois chiches?|lentilles?)", 7),
 (r"lentille|pois chiche|haricots? (blanc|rouge|noir|sec|coco|tarbais|pinto|borlotti|lingot|azuki|mungo)|flageolet|pois casse|feves? seches|soja jaune|dal|urad|toor|chana|garrofo", 22),
 (r"cacahuete|arachide|amande|noix|noisette|cajou|pistache|pignon|sesame|tahini|graine", 20),
 (r"vermicelles? de (patate|haricot)|nouilles? de riz|vermicelles? de riz|fecule|maizena|tapioca", 0.5),
 (r"pate|spaghetti|tagliatelle|lasagne|penne|bucatini|linguine|fusilli|macaroni|orecchiette|gnocchi|nouille|udon|soba|ramen|couscous|semoule|boulgour|ble|epeautre|orge|freekeh|sarrasin|farine|quinoa|avoine", 11),
 (r"pain|naan|tortilla|pita|paratha|chapati|muffin anglais|brioche|baguette|bun|wrap|pate (a pizza|brisee|feuilletee|sablee)|focaccia|galette de ble|crepe|blini|biscotte|chapelure", 8),
 (r"riz", 7), (r"pomme de terre|patate|polenta|mais|manioc|igname|plantain", 2),
]
PIECE = [(r"poulet (entier|fermier|en \d+ morceaux)|^1 poulet|un poulet", 1500), (r"jaunes? d.oeufs?", 18), (r"blanc d.oeuf|blancs d.oeufs", 33), (r"(?<!b)oeufs?", 55), (r"tranches? de (jambon|dinde|bacon)", 40), (r"tranche.*(saumon|truite)", 25), (r"tranches? de pain de mie", 25), (r"tranche", 40),
 (r"boites? de (thon|sardines|maquereau)|boite.*thon", 112), (r"(boite|bocal|conserve)", 240), (r"reblochon", 450), (r"camembert|brie", 250), (r"mozzarella|burrata", 125), (r"feta", 200), (r"chevre", 180),
 (r"naan|pita|paratha|pain plat|muffin", 80), (r"tortilla|crepe|galette", 45), (r"pate (a pizza|brisee|feuilletee|sablee)|pates? feuilletees?|pates? brisees?|pate maison", 230), (r"petits? pains?|bun|pain rond", 80),
 (r"portions? de nouilles", 200), (r"bloc de tofu", 400), (r"paves?|filets?|dos|escalopes?|steaks?|blancs? de (poulet|dinde)|supremes?", 140), (r"magrets?", 350), (r"souris", 350), (r"morceaux de poulet|hauts? de cuisse|pilons?", 150), (r"baguettes?", 250), (r"plaques? de ravioles", 60), (r"cannellonis?", 12), (r"feuilles? de filo", 0), (r"croustades?", 0), (r"cuisse", 250), (r"lapin", 1400),
 (r"merguez|chipolata", 70), (r"saucisse", 100), (r"crevettes?|gambas", 18), (r"noix de saint", 30), (r"jarret", 300), (r"sardines?", 50), (r"maquereaux?", 250), (r"soles?", 300), (r"dorades?|bar\b", 400)]
UNIT = [(r"^([\d.]+)\s*(?:a\s*[\d.]+\s*)?kg\b", 1000), (r"^([\d.]+)\s*(?:a\s*[\d.]+\s*)?g\b", 1), (r"^([\d.]+)\s*(?:a\s*[\d.]+\s*)?l\b", 1000), (r"^([\d.]+)\s*(?:a\s*[\d.]+\s*)?cl\b", 10),
 (r"^([\d.]+)\s*(?:a\s*[\d.]+\s*)?ml\b", 1), (r"^([\d.]+)\s*c\. a s\.", 15), (r"^([\d.]+)\s*c\. a c\.", 5), (r"^([\d.]+)\s*(poignee|bol)", 60)]
def num(s):
    s = s.replace("½", ".5").replace("¼", ".25").replace("¾", ".75")
    try: return float(s if not s.startswith(".") else "0" + s)
    except: return None
def grams(q, label):
    n = norm((q + " " + label).strip()).replace(",", ".")
    for rx, f in UNIT:
        m = re.match(rx, n)
        if m: return num(m.group(1)) * f
    m = re.search(r"\(\s*(?:≈\s*)?([\d.]+)\s*(kg|g)\b|\bde ([\d.]+)\s*(?:a\s*[\d.]+\s*)?(kg|g)\b", n)
    c = re.match(r"([\d.½¼¾]+)", n); k = num(c.group(1)) if c else None
    if m:
        v, u = (m.group(1), m.group(2)) if m.group(1) else (m.group(3), m.group(4))
        g = float(v) * (1000 if u == "kg" else 1)
        return g if (k and k > 1 and "(" in n) else g * (k or 1)
    if k is None: return None
    for rx, g in PIECE:
        if re.search(rx, n): return k * g
    return None
BONE = r"poulet (entier|fermier|en \d+ morceaux)|^1 poulet|\bcoq\b|avec os|cuisses?|pilons?|gigot|epaule.*\bos\b|jarret|souris|plat de cotes|cote de boeuf|carcasse|lapin|canard entier|dinde de|osso|queue de boeuf"
LEG = r"lentille|pois chiche|haricot|flageolet|pois casse|feve|dal\b|cocos?\b|azuki|mungo|garrofo|lingot"
def dens(text):
    for rx, d in DENS:
        if re.search(rx, text): return d
    return None
def protein(r, BY, SECTION, d=0, unknown=None):
    tot = 0
    for l in r["ingredients"]:
        if l["optional"]: continue
        ref = l.get("ref") or ""
        if ref.startswith("SUB:") and ref[4:] in BY and d < 2:
            sub = BY[ref[4:]]; m = re.match(r"([\d.½¼]+)", norm(l["qty"]).replace(",", "."))
            share = 1.0
            if "½" in l["qty"] or "1/2" in l["qty"]: share = 0.5
            tot += protein(sub, BY, SECTION, d + 1, unknown) * share; continue
        if not ref or ref.startswith("achat:"): continue  # eau, glace… : sans référence, sans protéine
        sec = SECTION(ref)
        if sec.startswith(("Herbes", "Épices", "Condiments", "Alcools", "Légumes", "Fruits")) and not re.search(r"edamame|soja|petits pois", norm(ref + l["label"])): continue
        t = norm(ref + " " + l["label"]); lab = norm(l["label"]); dd = dens(t)
        g = grams(l["qty"], l["label"])
        if sec.startswith("Légumineuses") and re.search(LEG, t):
            # le libellé de la fiche décide (le nom de référence dit souvent « secs / en boîte ») ; sans précision, 400 g et plus = conserve
            canned = re.search(r"boite|bocal|cuit|conserve|egoutt", lab) or re.match(r"[\d.,½]+\s*(boite|bocal)", norm(l["qty"]))
            dry = re.search(r"\bsec|trempe", lab)
            dd = 7 if canned or (not dry and g is not None and g >= 400) else 22
        if not dd:
            dd = 20 if sec.startswith("Viandes") else 19 if sec.startswith("Poissons") else 15 if sec.startswith("Porc") else None
        if not dd: continue
        if g is not None and re.search(BONE, t): g *= 0.65  # os et carcasse : environ un tiers du poids
        if g is None:
            if unknown is not None and dd >= 7: unknown.append(l["qty"] + " " + l["label"])
            continue
        tot += g * dd / 100
    return tot

ACHAT = {"Baguette tradition": 6.5, "Tortillas de blé": 7.0, "Salade (laitue, batavia)": 1.0}
def per_portion(r, BY, SECTION):
    """Protéines par part (g), accompagnement relié compris."""
    p = protein(r, BY, SECTION) / max(1, r["portions"])
    side = r.get("side")
    if side and side.startswith("achat:"): p += ACHAT.get(side[6:], 0)
    elif side and side in BY: p += protein(BY[side], BY, SECTION) / max(1, BY[side]["portions"])
    return p
