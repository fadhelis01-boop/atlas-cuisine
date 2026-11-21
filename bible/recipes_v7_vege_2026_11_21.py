# -*- coding: utf-8 -*-
"""Audit cuisinier amateur (21/11/2026) : corriger le filtre végétarien sur les abats et le gibier (tête de veau, foie
gras, ris et rognons de veau, pigeon, lièvre, faisan, grenouilles — ingrédient principal non référencé au Tome 3,
invisible au filtre) les a fait basculer à juste titre du côté « non végétarien », repassant la part de plats
végétariens sous le seuil de 33 % (test 63). 4 plats végétariens de plus pour compenser, dans des angles encore
peu couverts (légumes d'automne, tofu, légumineuses). NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

BLETTE = "Blette / bette"; PLEUROTE = "Pleurote"; CHATAIGNE = "Châtaigne (fraîche, crème, purée)"
CELERI_RAVE = "Céleri-rave"; TOFU = "Tofu (ferme / soyeux)"; ORANGE = "Orange"; LENTILLE_CORAIL = "Lentilles corail"
FR_BASE = "France › Cuisine de base"

K("gratin_blettes_bechamel_comte", "Gratin de blettes à la béchamel et au comté", "Gratin de blettes", FR_BASE, "P", 1, 4, 25, 30, "€",
  "Casserole, plat à gratin.",
  "Les côtes et les feuilles de blette ne finissent pas à la poubelle : cuites ensemble, nappées d'une béchamel "
  "simple et gratinées au comté, pour un accompagnement d'automne qui change du gratin de pommes de terre.",
  [f"1 kg|de blettes (côtes et feuilles)|{BLETTE}|3", f"40 g|de beurre|{BEURRE}|1", f"40 g|de farine|{F55}|1",
   f"50 cl|de lait|{LAIT}|2", f"80 g|de {GRUY}, râpé|{GRUY}|2", f"1 pincée|de {MUSC}|{MUSC}|0", f"1/2|citron (jus)|{CIT}|1",
   f"-|sel, poivre|{SEL}|1"],
  ["**Blettes.** Côtes et feuilles séparées, lavées ; côtes en tronçons cuites 10 min à l'eau bouillante salée avec "
   "un trait de jus de citron (elles restent plus claires), feuilles ajoutées 3 min ; égouttées en pressant.",
   "**Béchamel.** Beurre fondu, farine ajoutée hors du feu, remise sur feu doux 1 min en remuant (roux blond) ; "
   "lait versé peu à peu en fouettant, 5 min à frémissement jusqu'à napper la cuillère ; muscade, sel, poivre.",
   "**Assembler.** Blettes dans le plat, béchamel versée dessus, comté râpé par-dessus.",
   "**Gratiner.** Four à 200 °C, 15 à 20 min : dessus doré et bouillonnant."],
  tips=["Les côtes cuisent plus longtemps que les feuilles : toujours les séparer avant la cuisson à l'eau."],
  keep="2 jours au frigo ; se réchauffe au four.", age=2, kids="✓ dès 2 ans, mixé si besoin.", cats=["vegetarien"],
  profil=["gras"], side="riz_nature")
K("poelee_pleurotes_chataignes_puree_celeri", "Poêlée de pleurotes et châtaignes, purée de céleri-rave", "Pleurotes-châtaignes", FR_BASE, "P", 1, 4, 20, 30, "€",
  "Poêle, casserole, mixeur.",
  "Un plat d'automne tout en champignons et châtaignes, posé sur une purée de céleri-rave plus légère qu'une purée "
  "de pommes de terre classique, avec juste un peu de crème pour lier.",
  [f"1|céleri-rave (environ 800 g)|{CELERI_RAVE}|3", f"15 cl|de crème|{CL}|2", f"400 g|de pleurotes|{PLEUROTE}|3",
   "200 g|de châtaignes cuites (sous vide)|Châtaigne (fraîche, crème, purée)|2", f"2|échalotes|{ECH}|1",
   f"40 g|de beurre|{BEURRE}|1", f"1 c. à s.|de persil haché|{PERSIL}|1", "1 c. à s.|de vinaigre de vin|Vinaigre de vin rouge / blanc|1",
   f"-|sel, poivre|{SEL}|1"],
  ["**Purée.** Céleri-rave épluché, en cubes, cuit 20 min à l'eau salée : une lame entre sans résistance ; "
   "égoutté, mixé avec la crème, sel, poivre.",
   "**Pleurotes.** Déchirées en lanières, poêle très chaude sans matière grasse 3 min : elles rendent leur eau, "
   "puis beurre et échalotes, 5 min : dorées.",
   "**Châtaignes.** Ajoutées entières ou en morceaux, 3 min pour les réchauffer ; un trait de vinaigre hors du "
   "feu pour relever.",
   "**Servir.** Purée en fond d'assiette, poêlée dessus, persil."],
  tips=["Les pleurotes rendent beaucoup d'eau : les saisir d'abord sans matière grasse laisse cette eau s'évaporer, "
        "elles dorent ensuite bien mieux."],
  keep="2 jours au frigo, séparément.", age=3, kids="✓ dès 3 ans, châtaignes écrasées.", cats=["vegetarien"],
  profil=["gras"])
K("tofu_laque_orange_gingembre", "Tofu laqué à l'orange et au gingembre, riz vapeur", "Tofu laqué à l'orange", "Asie de l'Est › Chine", "P", 1, 3, 15, 15, "€",
  "Poêle, wok.",
  "Du tofu ferme doré à la poêle puis laqué dans une sauce à l'orange, au gingembre et à la sauce soja, qui "
  "réduit en quelques minutes jusqu'à devenir brillante et sirupeuse.",
  [f"400 g|de tofu ferme|{TOFU}|3", f"3 c. à s.|de fécule|Fécule de maïs (maïzena)|1", "Jus et zeste de 2|oranges|Orange|2",
   f"2 cm|de gingembre frais|{GING}|1", f"2 c. à s.|de sauce soja|{SOJA}|1", f"2 c. à s.|de miel|{MIEL}|1",
   f"2 gousses|d'ail|{AIL}|1", f"4 c. à s.|d'huile|{HN}|1", "1 c. à c.|de sésame|Sésame (blanc/noir)|1?"],
  ["**Tofu.** Pressé 15 min entre deux torchons, en cubes, roulé dans la fécule ; poêle huilée chaude, 8 min en "
   "retournant : doré sur toutes les faces ; réservé.",
   "**Sauce.** Jus et zeste d'orange, gingembre et ail râpés, soja, miel mélangés.",
   "**Laquer.** Sauce versée dans la poêle chaude, 2 à 3 min à feu vif jusqu'à épaissir et napper une cuillère.",
   "**Enrober.** Tofu remis dans la sauce, 1 min en l'enrobant ; sésame. Riz vapeur à part."],
  keep="1 jour au frigo (le tofu ramollit).", age=2, kids="✓ dès 2 ans.", cats=["vegetarien", "express"],
  profil=["sucre", "acide"], side="riz_nature")
K("galettes_lentilles_corail_carottes", "Galettes de lentilles corail et carottes, sauce yaourt-citron", "Galettes de lentilles", FR_BASE, "P", 1, 4, 25, 20, "€",
  "Casserole, poêle, mixeur ou fourchette.",
  "Des lentilles corail cuites puis écrasées avec de la carotte râpée et un œuf pour lier, façonnées en petites "
  "galettes dorées à la poêle, avec une sauce fraîche au yaourt et au citron.",
  [f"200 g|de lentilles corail|{LENTILLE_CORAIL}|3", f"2|carottes râpées|{CAROTTE}|2", f"1|oignon haché|{OIG}|1",
   f"1|œuf|{OEUF}|1", f"3 c. à s.|de farine|{F55}|1", f"1 c. à c.|de cumin|{CUMIN}|1",
   f"4 c. à s.|d'huile|{HN}|1", f"20 cl|de yaourt nature|{YAO}|1", f"1/2|citron (jus)|{CIT}|1"],
  ["**Lentilles.** Rincées, cuites 12 min à l'eau non salée : tendres et en purée grossière ; égouttées si besoin.",
   "**Mélanger.** Lentilles, carotte, oignon, œuf, farine, cumin, sel, poivre : pâte épaisse qui se tient.",
   "**Former.** 8 galettes aplaties à la main.",
   "**Cuire.** Poêle huilée chaude, 4 min par face : dorées et craquantes dessus.",
   "**Sauce.** Yaourt, jus de citron, sel mélangés ; servie à côté."],
  tips=["Si la pâte est trop molle pour tenir en galette, une cuillerée de farine de plus suffit : les lentilles "
        "corail rendent plus ou moins d'eau selon la marque."],
  keep="2 jours au frigo ; se congèlent crues.", age=2, kids="✓ dès 2 ans, les enfants façonnent les galettes.",
  cats=["vegetarien", "enfants"], profil=["acide"])
