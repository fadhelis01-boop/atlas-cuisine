# -*- coding: utf-8 -*-
"""Vague 2 (Tome 13) : format de saisie compact, converti au format des fiches du Tome 11 (recipes_data.R).
K(id, titre, origine, région « Macro › Pays/Région », type, niveau, portions, min actives, min repos/cuisson, coût,
  équipement, intro, ingrédients, étapes, ...)
  type : E entrée · P plat · D dessert · G goûter · B boisson · S sauce · A accompagnement · Pa pain · Ba base · So soupe
  ingrédient : "quantité|libellé|réf. Tome 3|poids" ; poids suivi de « ? » = facultatif ; réf. « - » = eau / hors référentiel ;
               réf. « SUB:id » = sous-recette ATLAS.
  var : [(nom, ["pork"|"alcohol"], {réf: [(réf, ratio), …]}, note)]
Critère éditorial de la vague 2 (cahier du critique gastronomique) : goût franc et généreux, 10 ingrédients au plus en
général, gestes simples, matériel d'une cuisine française, repères sensoriels dans chaque étape. NON TESTÉES (Tome 7 §2)."""
from recipes_data import R

KIND = {"E": "Entrée", "So": "Entrée", "P": "Plat", "D": "Dessert", "G": "Goûter / dessert", "B": "Boisson", "S": "Sauce",
        "A": "Accompagnement", "Pa": "Pain", "Ba": "Base"}
V2 = []

def K(id, title, origin, region, kind, niveau, portions, actif, repos, cost, equip, intro, ing, steps,
      tips=(), keep="3 jours au frigo, dans une boîte fermée.", age=None, cats=(), fetes=(), profil=(), tech=(),
      sa=(), a=(), var=(), kids=None, zw=(), side=None):
    lines = []
    for s in ing:
        q, label, ref, w = (s.split("|") + ["", "", "", "1"])[:4]
        opt = w.endswith("?")
        lines.append((q.strip(), label.strip(), None if ref.strip() in ("-", "") else ref.strip(), int(w.rstrip("?") or 1), opt))
    variantes = [dict(name=n, constraints=set(c), tested=False, replace={k: list(v) for k, v in rep.items()}, note=note) for n, c, rep, note in var]
    if kids is None:
        kids = f"✓ dès {age} an{'s' if (age or 0) > 1 else ''}." if age is not None else "Pour les adultes et les grands enfants."
    R(id=id, title=title, origin=origin, region=region, kind=KIND[kind], niveau=niveau, portions=portions, actif=actif, repos=repos,
      cost=cost, equip=equip, intro=intro, ing=lines, steps=list(steps), astuces=list(tips), variantes=variantes, conservation=keep,
      zero_dechet=[f"**{z[0]}** {z[1]}" if isinstance(z, tuple) else z for z in zw], accords_sa=list(sa), accords_a=list(a), techniques=list(tech), enfants=kids, age=age,
      cats=list(cats), fetes=list(fetes), profil=list(profil), side=side, tests="Quantités, temps et rendu à confirmer au Test 1 et au Test 2 (Tome 7 §2).", vague=2)
    V2.append(id)

# Raccourcis d'ingrédients courants (réf. exactes du Tome 3)
SEL = "Sel fin / gros sel / fleur de sel"; POIVRE = "Poivre noir / blanc / vert"; HO = "Huile d'olive vierge extra"
HN = "Huile de tournesol / colza"; BEURRE = "Beurre doux / demi-sel"; OIG = "Oignon jaune"; AIL = "Ail"; ECH = "Échalote"
PERSIL = "Persil plat / frisé"; CORI = "Coriandre fraîche"; THYM = "Thym / romarin"; LAURIER = "Laurier"; F55 = "Farine de blé T55"
F45 = "Farine de blé T45"; OEUF = "Œuf entier (frais)"; LAIT = "Lait entier / demi-écrémé / écrémé"; CF = "Crème fraîche"
CL = "Crème fleurette (liquide)"; SUCRE = "Sucre blanc / roux / cassonade / vergeoise"; PDT = "Pomme de terre"; TOM = "Tomate"
PELEES = "Coulis / passata / tomates pelées"; CONC = "Concentré de tomate"; GRUY = "Gruyère / comté / emmental / beaufort"
PARM = "Parmesan / Parmigiano"; CIT = "Citron"; CITV = "Citron vert"; CUMIN = "Cumin (graines / moulu)"; PAPRIKA = "Paprika doux"
PFUME = "Paprika fumé (pimentón)"; CANN = "Cannelle (bâton / poudre)"; GING = "Gingembre frais"; CURC = "Curcuma (poudre)"
RIZ = "Riz long / basmati / thaï"; PATES = "Pâtes sèches (spaghetti, penne…)"; POIS = "Pois chiches (secs / bocal)"
CUISSE = "Cuisse / pilon de poulet"; BLANC_P = "Blanc de poulet"; HACHE = "Bœuf haché"; SOJA = "Sauce soja claire"
CIDRE = "Vinaigre de cidre"; DIJON = "Moutarde de Dijon"; YAO = "Yaourt nature"; GREC = "Yaourt grec"; LEV = "Levure boulangère sèche"
LEVC = "Levure chimique"; CHOCO = "Chocolat noir"; BOUILLON = "Bouillon d'os maison (bœuf/volaille)"; PIMENT = "Piment frais (divers)"
CAYENNE = "Cayenne / piment en poudre"; MUSC = "Noix de muscade"; POIVRON = "Poivron (rouge/jaune/vert)"; CAROTTE = "Carotte"
CUR = "Curry (mélange)"; COCO = "Lait de coco / crème de coco"; MIEL = "Miel"; VAN = "Poudre de vanille"; EAU = "-"
