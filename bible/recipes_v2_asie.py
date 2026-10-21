# -*- coding: utf-8 -*-
"""Vague 2 · Asie de l'Est (Chine, Japon, Corée, Taïwan) et Asie du Sud-Est (Thaïlande, Vietnam, Indonésie, Malaisie, Philippines, Cambodge)."""
from recipes_v2_base import *

AE = "Asie de l'Est"; ASE = "Asie du Sud-Est"
SAKE_VAR = ("Sans alcool", ["alcohol"], {"Mirin": [("Jus de pomme / raisin / orange (pur jus)", 0.8), ("Vinaigre de riz", 0.1)]}, "Mirin → **jus de pomme + un trait de vinaigre de riz**. **À tester**.")

K("gyoza", "Gyoza poulet-chou", "Gyōza", f"{AE} › Japon", "E", 2, 30, 45, 10, "€", "Poêle avec couvercle.",
  "Raviolis grillés dessous et cuits à la vapeur dessus : croustillants et juteux, avec une sauce soja-vinaigre.",
  ["30|feuilles à gyoza|Pâte à gyoza / wonton|3", "300 g|de poulet haché (cuisse)|Cuisse / pilon de poulet|3", "200 g|de chou chinois haché salé et pressé|Chou chinois / pak-choï|2", f"2|oignons nouveaux|Oignon nouveau / cébette|1", f"1 morceau|de gingembre + 2 gousses d'ail|{GING}|1", f"2 c. à s.|de sauce soja|{SOJA}|2", "1 c. à s.|d'huile de sésame|Huile de sésame (grillée)|1", "2 c. à s.|de vinaigre de riz (sauce)|Vinaigre de riz|1"],
  ["**Farce.** Tout mélanger énergiquement jusqu'à ce que ce soit collant.", "**Plier.** Une cuillère, bord mouillé, plis d'un seul côté.", "**Cuire.** Poêle huilée, 2 min (dessous doré) ; 8 cl d'eau, couvercle, 6 min ; découvre, 1 min pour recroustiller.", "**Sauce.** Soja + vinaigre de riz + huile pimentée."],
  keep="Crus : 2 mois congelés à plat.", age=3, cats=["enfants"], fetes=["Nouvel An chinois"], profil=["gras"])

K("ramen_shoyu", "Ramen shoyu au poulet", "Shōyu rāmen", f"{AE} › Japon › Tokyo", "P", 2, 4, 40, 180, "€€", "Faitout, casserole.",
  "Un bouillon clair de poulet et dashi au soja, nouilles, œuf mollet mariné, poulet, oignons verts : le bol réconfort.",
  [f"1,5 L|de bouillon de volaille maison|{BOUILLON}|3", "1 sachet|de dashi (ou 10 g de kombu)|Dashi (instantané)|2", "4 portions|de nouilles ramen|Nouilles ramen|3", f"6 c. à s.|de sauce soja|{SOJA}|2", "2 c. à s.|de mirin|Mirin|1", f"4|œufs|{OEUF}|2", f"2|blancs de poulet|{BLANC_P}|2", "4|oignons nouveaux|Oignon nouveau / cébette|1", "4|feuilles de nori|Algue nori|1", "1 poignée|de pousses de soja|Germes de soja|1"],
  ["**Œufs.** 6 min 30, eau glacée, écalés ; marinés 4 h dans 4 c. à s. de soja + mirin + eau.", "**Bouillon.** Bouillon de volaille + dashi, 10 min ; tare = soja + mirin dans le fond des bols.", "**Poulet.** Poché 15 min dans le bouillon, tranché.", "**Bol.** Tare, bouillon brûlant, nouilles cuites, poulet, œuf coupé, oignons, nori, pousses."],
  var=[SAKE_VAR], age=3, cats=["enfants"], profil=["leger"])

K("onigiri", "Onigiri (boules de riz garnies)", "Onigiri", f"{AE} › Japon", "P", 1, 8, 25, 30, "€", "Bol d'eau salée.",
  "Triangles de riz japonais garnis de saumon, thon-mayonnaise ou prune salée, enveloppés de nori : le pique-nique japonais.",
  ["400 g|de riz rond japonais|Riz rond / sushi|3", "150 g|de saumon cuit émietté ou thon-mayo|Saumon (frais, pavé)|2", "4|feuilles de nori|Algue nori|2", "1 c. à s.|de sésame|Sésame (blanc/noir)|1", f"1 c. à c.|de sel|{SEL}|0"],
  ["**Riz.** Rincé jusqu'à eau claire, cuit (1,1 volume d'eau), reposé 10 min.", "**Former.** Mains mouillées et salées, une poignée de riz, creux, garniture, referme en triangle en pressant 3 fois.", "**Nori.** Bande de nori au moment de manger (croustillante)."],
  keep="Le jour même, à température ambiante couverts.", age=1, cats=["enfants"], profil=["leger"])

K("tonkatsu_poulet", "Katsu de poulet, sauce curry japonaise", "Chicken katsu curry", f"{AE} › Japon", "P", 2, 4, 30, 30, "€€", "Poêle profonde, casserole.",
  "Escalopes panées au panko, très croustillantes, nappées d'un curry japonais doux et sucré : le plat des cantines au Japon.",
  [f"4|blancs de poulet aplatis|{BLANC_P}|3", "100 g|de panko|Panko|3", f"2|œufs|{OEUF}|1", f"50 g|de farine|{F55}|1", f"2|carottes|{CAROTTE}|1", f"2|pommes de terre|{PDT}|1", f"1|oignon|{OIG}|1", f"2 c. à s.|de curry doux|{CUR}|2", "1|pomme râpée|Pomme|1", f"1 c. à s.|de sauce soja|{SOJA}|1", f"30 g|de beurre + 30 g de farine (roux)|{BEURRE}|1", "50 cl|d'huile de friture|Huile de tournesol / colza|1"],
  ["**Curry.** Oignon, carottes, pommes de terre, pomme, 50 cl d'eau, 20 min ; roux beurre-farine-curry délayé, soja : épais et brillant.", "**Paner.** Farine, œuf, panko.", "**Frire.** 4 min par face à 170 °C. Tranche, riz, sauce."],
  age=1, cats=["enfants"], profil=["gras"], tech=["Paner"])

K("saumon_teriyaki", "Saumon teriyaki, riz et brocoli", "Sake teriyaki", f"{AE} › Japon", "P", 1, 4, 15, 12, "€€", "Poêle.",
  "Pavés de saumon saisis côté peau puis laqués d'une sauce teriyaki maison : 15 minutes, brillant et fondant.",
  ["4|pavés de saumon avec peau|Saumon (frais, pavé)|3", "1|recette de sauce teriyaki|SUB:marinade_teriyaki_sauce|3", "1|brocoli|Brocoli|2", f"300 g|de riz rond|Riz rond / sushi|2", "1 c. à s.|de sésame|Sésame (blanc/noir)|1"],
  ["**Saumon.** Côté peau 5 min à feu moyen-vif, retourne 1 min.", "**Laquer.** Verse la sauce, arrose 1 min jusqu'à brillant.", "**Servir.** Riz, brocoli vapeur, sésame."],
  age=1, cats=["enfants"], profil=["poisson"], tech=["Cuisson du poisson", "Laquer"])

K("miso_soupe", "Soupe miso au tofu et wakame", "Misoshiru", f"{AE} › Japon", "So", 1, 4, 10, 10, "€", "Casserole.",
  "Dashi, miso, tofu soyeux, wakame et oignon vert : la soupe de chaque repas japonais, en 10 minutes.",
  ["1 L|de dashi|Dashi (instantané)|3", "4 c. à s.|de miso|Miso|3", "200 g|de tofu soyeux en dés|Tofu (ferme / soyeux)|2", "1 c. à s.|de wakame séché|Algue wakame / kombu|1", "2|oignons nouveaux|Oignon nouveau / cébette|1"],
  ["**Chauffer.** Dashi, wakame et tofu, 3 min.", "**Miso.** Hors du feu, dilué dans une louche de bouillon (ne fais jamais bouillir le miso). Oignons."],
  age=1, cats=["enfants"], profil=["leger"])

K("okonomiyaki", "Okonomiyaki (galette au chou)", "Okonomiyaki", f"{AE} › Japon › Osaka", "P", 1, 4, 20, 15, "€", "Poêle.",
  "Une galette épaisse de chou et d'œufs, dorée, avec sauce brune sucrée, mayonnaise et oignons verts : « ce que tu aimes, grillé ».",
  ["½|chou blanc finement émincé|Chou blanc / rouge|3", f"150 g|de farine|{F55}|2", f"3|œufs|{OEUF}|2", "15 cl|de dashi ou d'eau|Dashi (instantané)|1", "200 g|de crevettes ou de poulet émincé|Crevettes (cuites/crues)|2", "4|oignons nouveaux|Oignon nouveau / cébette|1", "3 c. à s.|de sauce Worcestershire + 1 de ketchup + 1 de miel (sauce)|Sauce Worcestershire|1", f"4 c. à s.|de mayonnaise|SUB:mayonnaise|1"],
  ["**Pâte.** Farine, dashi, œufs ; chou, oignons, crevettes.", "**Cuire.** Galettes épaisses, 5 min par face à feu moyen, couvert.", "**Garnir.** Sauce brune, filets de mayonnaise, oignons, nori."],
  age=3, profil=["gras"])

K("mochi_daifuku", "Daifuku (mochi à la pâte de haricot rouge)", "Daifuku mochi", f"{AE} › Japon", "G", 2, 12, 30, 10, "€", "Bol, micro-ondes, fécule.",
  "Pâte de riz gluant élastique qui enveloppe une pâte sucrée de haricots rouges (ou une fraise) : doux et moelleux.",
  ["150 g|de farine de riz gluant|Farine de riz / riz gluant|3", f"50 g|de sucre|{SUCRE}|1", "15 cl|d'eau|-|0", "250 g|de pâte de haricots rouges (azuki sucrés)|Haricots mungo / azuki|3", "2 c. à s.|de fécule pour fariner|Fécule de pomme de terre|1", "6|fraises (facultatif)|Fraise|1?"],
  ["**Mochi.** Farine + sucre + eau, 1 min au micro-ondes, remue, 1 min, remue, 30 s : pâte translucide élastique.", "**Former.** Sur la fécule, 12 boules aplaties, une boule de pâte d'azuki (et une fraise), referme en pinçant."],
  tips=["⚠️ Texture collante : à couper en petits morceaux pour les enfants et les personnes âgées (risque d'étouffement)."], keep="Le jour même.", age=None, kids="✓ dès 6 ans, coupé en petits morceaux.", profil=["sucre"])

K("bibimbap", "Bibimbap", "Bibimbap", f"{AE} › Corée", "P", 2, 4, 40, 20, "€€", "Poêle, casserole.",
  "Un bol de riz garni de légumes sautés séparément, bœuf mariné, œuf au plat et sauce gochujang : on mélange tout.",
  [f"300 g|de riz rond|Riz rond / sushi|3", "300 g|de bœuf émincé mariné bulgogi|SUB:marinade_bulgogi|3", f"2|carottes en julienne|{CAROTTE}|1", "200 g|d'épinards|Épinard|1", "200 g|de pousses de soja|Germes de soja|1", "1|courgette|Courgette|1", "150 g|de shiitakés|Shiitake|1", f"4|œufs|{OEUF}|2", "2 c. à s.|de gochujang + 1 de miel + 1 d'huile de sésame (sauce)|Gochujang|2", "1 c. à s.|de sésame|Sésame (blanc/noir)|1"],
  ["**Légumes.** Chacun sauté 2 min séparément avec un peu de sésame et sel (épinards et pousses blanchis).", "**Bœuf.** Saisi à feu vif.", "**Bol.** Riz, légumes en couronne, bœuf, œuf au plat, sauce, sésame."],
  age=3, profil=["epice"])

K("kimchi_maison", "Kimchi de chou chinois maison", "Baechu-kimchi", f"{AE} › Corée", "Ba", 2, 20, 60, 4320, "€", "Grand saladier, gants, bocal.",
  "Chou chinois salé puis enrobé d'une pâte piment-ail-gingembre et fermenté : acidulé, piquant, vivant.",
  ["1|gros chou chinois|Chou chinois / pak-choï|3", "80 g|de gros sel|Sel fin / gros sel / fleur de sel|2", "4 c. à s.|de gochugaru|Gochugaru|3", f"6 gousses|d'ail|{AIL}|2", f"1 morceau|de gingembre|{GING}|1", "2 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|2", f"1 c. à s.|de sucre|{SUCRE}|1", "1|radis daikon en julienne|Radis noir / daikon|1", "4|oignons nouveaux|Oignon nouveau / cébette|1", "1 c. à s.|de farine de riz cuite dans 10 cl d'eau|Farine de riz / riz gluant|1"],
  ["**Saler.** Chou en quartiers, sel entre les feuilles, 2 h en retournant ; rince 3 fois, égoutte.", "**Pâte.** Bouillie de farine de riz refroidie + gochugaru, ail, gingembre, sauce de poisson, sucre ; daikon et oignons.", "**Enrober.** Chaque feuille (gants !), tasse dans le bocal.", "**Fermenter.** 2-3 jours à température ambiante, puis au frigo."],
  keep="1 à 3 mois au frigo (il s'acidifie).", age=None, cats=["sauces"], profil=["epice", "acide"], tips=["Kimchi trop acide : parfait pour le riz sauté au kimchi ou la soupe."])

K("kimchi_bokkeumbap", "Riz sauté au kimchi", "Kimchi-bokkeumbap", f"{AE} › Corée", "P", 1, 2, 10, 10, "€", "Poêle.",
  "Le plat anti-gaspi coréen : riz de la veille, kimchi bien fermenté, un œuf au plat.",
  [f"300 g|de riz cuit froid|{RIZ}|3", "150 g|de kimchi haché|SUB:kimchi_maison|3", "1 c. à s.|de gochujang|Gochujang|1", f"2|œufs|{OEUF}|2", "1 c. à c.|d'huile de sésame|Huile de sésame (grillée)|1", "2|oignons nouveaux|Oignon nouveau / cébette|1"],
  ["**Sauter.** Kimchi 3 min, gochujang, riz, 4 min à feu vif.", "**Finir.** Huile de sésame, œuf au plat, oignons, nori."],
  age=None, cats=["zero_dechet"], profil=["epice"])

K("poulet_frit_coreen", "Poulet frit coréen (yangnyeom)", "Yangnyeom chikin", f"{AE} › Corée", "P", 2, 4, 30, 25, "€€", "Casserole profonde, thermomètre.",
  "Ailes ou hauts de cuisse frits deux fois, très croustillants, laqués d'une sauce sucrée-piquante au gochujang.",
  ["1 kg|d'ailes ou de hauts de cuisse|Ailes de poulet|3", "80 g|de fécule de pomme de terre|Fécule de pomme de terre|2", "3 c. à s.|de gochujang|Gochujang|3", f"3 c. à s.|de miel|{MIEL}|2", f"2 c. à s.|de sauce soja|{SOJA}|1", f"3 gousses|d'ail|{AIL}|1", "1 c. à s.|de sésame|Sésame (blanc/noir)|1", "1 L|d'huile|Huile de tournesol / colza|1"],
  ["**Enrober.** Poulet salé, fécule.", "**Frire deux fois.** 8 min à 160 °C, repos 5 min, puis 3 min à 180 °C : craquant.", "**Laquer.** Sauce chaude, mélange, sésame."],
  age=3, profil=["sucre", "epice"], tech=["Frire"])

K("mapo_tofu", "Mapo tofu", "Mápó dòufu", f"{AE} › Chine › Sichuan", "P", 2, 4, 15, 15, "€", "Wok ou poêle.",
  "Tofu soyeux dans une sauce rouge au doubanjiang, bœuf haché et poivre du Sichuan qui fourmille : intense, avec du riz.",
  ["400 g|de tofu soyeux|Tofu (ferme / soyeux)|3", f"150 g|de bœuf haché|{HACHE}|2", "2 c. à s.|de pâte de haricots fermentés pimentée|Pâte de haricots noirs fermentés|3", "1 c. à c.|de poivre du Sichuan moulu|Poivre du Sichuan|2", f"3 gousses|d'ail + gingembre|{AIL}|1", f"25 cl|de bouillon|{BOUILLON}|1", f"1 c. à s.|de maïzena|Fécule de maïs (maïzena)|1", "2|oignons nouveaux|Oignon nouveau / cébette|1", f"2 c. à s.|d'huile|{HN}|1"],
  ["**Tofu.** Cubes blanchis 2 min dans l'eau salée (ils se tiennent).", "**Sauce.** Bœuf croustillant, pâte pimentée, ail-gingembre ; bouillon.", "**Mijoter.** Tofu 5 min sans remuer (pousse avec le dos de la cuillère) ; maïzena délayée en 2 fois. Sichuan, oignons."],
  age=None, profil=["epice"])

K("poulet_kung_pao", "Poulet kung pao", "Gōngbǎo jīdīng", f"{AE} › Chine › Sichuan", "P", 1, 4, 20, 10, "€€", "Wok.",
  "Dés de poulet sautés aux cacahuètes, piments secs et sauce aigre-douce au vinaigre noir.",
  [f"600 g|de blanc ou haut de cuisse en dés|{BLANC_P}|3", "80 g|de cacahuètes grillées|Cacahuète / arachide|2", "8|piments secs|Piment frais (divers)|1", "1 c. à c.|de poivre du Sichuan|Poivre du Sichuan|1", f"3 c. à s.|de sauce soja|{SOJA}|2", "2 c. à s.|de vinaigre noir (ou balsamique)|Vinaigre noir chinois (Chinkiang)|2", f"1 c. à s.|de sucre|{SUCRE}|1", f"1 c. à s.|de maïzena|Fécule de maïs (maïzena)|1", "4|oignons nouveaux|Oignon nouveau / cébette|1", f"3 gousses|d'ail + gingembre|{AIL}|1"],
  ["**Mariner.** Poulet, 1 c. à s. de soja, maïzena, 15 min.", "**Sauce.** Soja, vinaigre, sucre, 3 c. à s. d'eau, 1 c. à c. de maïzena.", "**Sauter.** Piments et Sichuan 20 s, poulet 4 min, ail-gingembre-oignons, sauce, cacahuètes."],
  age=3, profil=["epice", "sucre"], tips=["⚠️ Arachide : allergène majeur."], tech=["Sauter au wok"])

K("char_siu_poulet", "Poulet laqué char siu", "Char siu", f"{AE} › Chine › Canton", "P", 1, 4, 15, 40, "€€", "Four, grille.",
  "La laque cantonaise (hoisin, miel, cinq-épices) sur des hauts de cuisse de poulet : brillant, sucré, légèrement grillé.",
  [f"1 kg|de hauts de cuisse désossés|{CUISSE}|3", "4 c. à s.|de sauce hoisin|Sauce hoisin|3", f"3 c. à s.|de miel|{MIEL}|2", f"2 c. à s.|de sauce soja|{SOJA}|1", "1 c. à c.|de cinq-épices|Cinq-épices chinois|2", f"3 gousses|d'ail|{AIL}|1"],
  ["**Mariner.** Tout (garde 3 c. à s. de marinade), 4 h.", "**Rôtir.** Sur grille, 30 min à 200 °C, puis badigeon miel-marinade, 10 min sous le gril : bords caramélisés."],
  age=3, cats=["enfants"], fetes=["Nouvel An chinois"], profil=["sucre"])

K("nouilles_sautees_boeuf", "Nouilles sautées au bœuf et brocoli", "Chow mein", f"{AE} › Chine › Canton", "P", 1, 4, 20, 10, "€€", "Wok.",
  "Nouilles aux œufs sautées, bœuf tendre, brocoli croquant, sauce d'huître : un plat complet en 15 minutes.",
  ["300 g|de nouilles chinoises aux œufs|Nouilles chinoises aux œufs|3", "400 g|de bœuf (rumsteck) émincé|Rumsteck|3", "1|brocoli|Brocoli|2", "2 c. à s.|de sauce d'huître|Sauce d'huître|2", f"2 c. à s.|de sauce soja|{SOJA}|2", f"1 c. à c.|de maïzena|Fécule de maïs (maïzena)|1", f"2 gousses|d'ail + gingembre|{AIL}|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Bœuf.** Mariné soja + maïzena, saisi 1 min, réservé.", "**Sauter.** Brocoli 3 min, ail-gingembre, nouilles cuites, sauces.", "**Finir.** Bœuf, 30 s."],
  age=1, cats=["enfants"], profil=["gras"], tech=["Sauter au wok"])

K("bao_poulet", "Bao (petits pains vapeur) au poulet", "Gua bao", f"{AE} › Taïwan", "P", 2, 10, 50, 90, "€€", "Panier vapeur, papier cuisson.",
  "Des pains vapeur moelleux, pliés en sandwich autour d'un poulet laqué, pickles et cacahuètes.",
  [f"300 g|de farine|{F45}|3", f"5 g|de levure|{LEV}|1", f"15 cl|de lait tiède|{LAIT}|2", f"20 g|de sucre|{SUCRE}|1", f"1 c. à c.|de levure chimique|{LEVC}|0", "1|recette de poulet char siu|SUB:char_siu_poulet|3", "1 bocal|de pickles d'oignons rouges|SUB:pickles_oignons_rouges|1", "1 poignée|de coriandre et cacahuètes|Coriandre fraîche|1"],
  ["**Pâte.** Pétris 10 min, pousse 1 h.", "**Former.** 10 ovales, huilés, pliés sur un carré de papier ; 30 min.", "**Vapeur.** 10 min, puis 3 min couvercle fermé feu éteint.", "**Garnir.** Poulet tranché, pickles, coriandre, cacahuètes."],
  age=3, cats=["enfants"], profil=["sucre"])

K("tom_kha_kai", "Tom kha kai (soupe coco-galanga)", "Tom kha kai", f"{ASE} › Thaïlande", "So", 1, 4, 15, 15, "€€", "Casserole.",
  "Poulet poché dans un bouillon de coco à la citronnelle, galanga et combava, relevé de citron vert et sauce de poisson.",
  [f"40 cl|de lait de coco|{COCO}|3", f"50 cl|de bouillon|{BOUILLON}|2", f"2|blancs de poulet émincés|{BLANC_P}|3", "2|bâtons de citronnelle|Citronnelle|2", "1 morceau|de galanga|Galanga|2", "4|feuilles de combava|Feuille de combava (kaffir)|2", "150 g|de champignons|Pleurote|1", f"2|citrons verts|{CITV}|2", "2 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|2", f"1 bouquet|de coriandre|{CORI}|1"],
  ["**Parfumer.** Bouillon + coco, citronnelle écrasée, galanga, combava, 10 min.", "**Cuire.** Poulet et champignons 5 min.", "**Assaisonner.** Hors du feu : citron vert, sauce de poisson, coriandre, piment."],
  age=3, profil=["acide"])

K("curry_vert_poulet", "Curry vert thaï au poulet", "Kaeng khiao wan kai", f"{ASE} › Thaïlande", "P", 1, 4, 15, 20, "€€", "Wok ou sauteuse.",
  "Pâte de curry vert frite dans la crème de coco, poulet, aubergines et basilic thaï : vif, parfumé, crémeux.",
  [f"600 g|de poulet émincé|{BLANC_P}|3", "3 c. à s.|de pâte de curry vert maison|SUB:pate_curry_vert|3", f"40 cl|de lait de coco|{COCO}|3", "1|aubergine|Aubergine|2", "1 poignée|de haricots verts|Haricots verts|1", "1 bouquet|de basilic thaï|Basilic thaï|2", "2 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|1", f"1 c. à c.|de sucre|{SUCRE}|0"],
  ["**Frire la pâte.** Crème du dessus du lait de coco + pâte, 3 min jusqu'à ce que l'huile perle.", "**Mijoter.** Poulet, reste de coco, légumes, 12 min.", "**Finir.** Sauce de poisson, sucre, basilic. Riz jasmin."],
  age=None, profil=["epice"])

K("som_tam", "Som tam (salade de papaye verte)", "Som tam", f"{ASE} › Thaïlande › Isan", "E", 1, 4, 20, 0, "€", "Mortier ou saladier, râpe.",
  "Papaye verte (ou chou-rave, carotte) pilée avec ail, piment, citron vert, sauce de poisson et cacahuètes : croquant, acide, piquant.",
  ["1|papaye verte (ou 2 carottes + ¼ chou blanc)|Papaye|3", f"2|tomates cerises × 6|{TOM}|1", "100 g|de haricots verts crus|Haricots verts|1", f"2 gousses|d'ail|{AIL}|1", f"2|piments|{PIMENT}|2", f"2|citrons verts|{CITV}|2", "2 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|2", "1 c. à s.|de sucre de palme ou cassonade|Sucre de coco|1", "40 g|de cacahuètes grillées|Cacahuète / arachide|1"],
  ["**Piler.** Ail, piment, sucre.", "**Assaisonner.** Citron vert, sauce de poisson.", "**Mélanger.** Papaye râpée, haricots, tomates, en pilant légèrement. Cacahuètes."],
  age=None, profil=["acide", "epice"])

K("mango_sticky_rice", "Riz gluant à la mangue", "Khao niao mamuang", f"{ASE} › Thaïlande", "D", 2, 4, 15, 300, "€", "Panier vapeur, casserole.",
  "Riz gluant cuit à la vapeur, imbibé de lait de coco sucré-salé, avec une mangue bien mûre.",
  ["250 g|de riz gluant trempé 4 h|Riz gluant|3", f"30 cl|de lait de coco|{COCO}|3", f"60 g|de sucre|{SUCRE}|2", f"1 pincée|de sel|{SEL}|1", "2|mangues mûres|Mangue|3", "1 c. à s.|de sésame grillé|Sésame (blanc/noir)|1"],
  ["**Vapeur.** Riz égoutté, 25 min.", "**Coco.** 20 cl de coco + sucre + sel chauffés, versés sur le riz chaud ; 20 min couvert.", "**Servir.** Mangue en tranches, reste de coco légèrement salé, sésame."],
  age=1, cats=["enfants"], profil=["sucre"])

K("bo_bun", "Bò bún", "Bún bò Nam Bộ", f"{ASE} › Vietnam", "P", 1, 4, 30, 10, "€€", "Wok, casserole.",
  "Vermicelles de riz froids, bœuf sauté à la citronnelle, crudités, herbes, cacahuètes, nems et nuoc cham : frais et complet.",
  ["250 g|de vermicelles de riz|Nouilles de riz / vermicelles|3", "400 g|de bœuf émincé|Rumsteck|3", "2|bâtons de citronnelle hachés|Citronnelle|2", "1|salade|Salade (laitue, batavia)|1", f"2|carottes|{CAROTTE}|1", "1|concombre|Concombre|1", "200 g|de pousses de soja|Germes de soja|1", "1 bouquet|de menthe et coriandre|Menthe|2", "50 g|de cacahuètes|Cacahuète / arachide|1", "1|recette de nuoc cham|SUB:nuoc_cham|3"],
  ["**Bœuf.** Mariné citronnelle, ail, sauce de poisson, sucre ; saisi 2 min à feu vif.", "**Vermicelles.** 3 min, rincés à l'eau froide.", "**Bol.** Salade, crudités, vermicelles, bœuf chaud, herbes, cacahuètes, nuoc cham."],
  age=3, profil=["leger", "acide"])

K("rouleaux_printemps", "Rouleaux de printemps aux crevettes", "Gỏi cuốn", f"{ASE} › Vietnam", "E", 1, 12, 35, 0, "€€", "Grande assiette d'eau tiède.",
  "Galettes de riz transparentes, crevettes, vermicelles, salade et herbes, avec une sauce hoisin-cacahuète.",
  ["12|galettes de riz|Galettes de riz (rice paper)|3", "24|crevettes cuites coupées en deux|Crevettes (cuites/crues)|3", "100 g|de vermicelles de riz|Nouilles de riz / vermicelles|2", "1|salade|Salade (laitue, batavia)|1", "1 bouquet|de menthe, coriandre, ciboulette|Menthe|2", "3 c. à s.|de sauce hoisin + 1 de beurre de cacahuète (sauce)|Sauce hoisin|1"],
  ["**Tremper.** Galette 3 s dans l'eau tiède (elle finit de ramollir sur le plan).", "**Rouler.** Crevettes en bas, salade, vermicelles, herbes ; un tour, rabats les côtés, roule serré.", "**Sauce.** Hoisin + cacahuète + eau chaude."],
  keep="Le jour même, sous un torchon humide.", age=3, cats=["enfants"], fetes=["Nouvel An chinois", "Apéritif dînatoire"], profil=["leger"])

K("nems_poulet", "Nems au poulet (au four ou frits)", "Chả giò", f"{ASE} › Vietnam", "E", 2, 20, 50, 20, "€", "Saladier, poêle ou plaque.",
  "Rouleaux croustillants farcis de poulet, vermicelles, champignons noirs et carotte : avec salade, menthe et nuoc cham.",
  ["20|galettes de riz|Galettes de riz (rice paper)|3", "400 g|de poulet haché|Cuisse / pilon de poulet|3", "50 g|de vermicelles de soja trempés|Vermicelles de haricots mungo|1", "15 g|de champignons noirs trempés|Champignon noir séché|1", f"1|carotte râpée|{CAROTTE}|1", f"1|oignon|{OIG}|1", f"1|œuf|{OEUF}|1", "1 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|1", "1 L|d'huile (friture) ou 3 c. à s. (four)|Huile de tournesol / colza|1"],
  ["**Farce.** Tout mélanger, poivre.", "**Rouler.** Galettes humidifiées, farce en boudin, rabats, roule serré.", "**Cuire.** Friture 8 min à 160 °C puis 2 min à 180 °C ; ou au four huilés, 25 min à 200 °C en retournant."],
  age=3, cats=["enfants"], fetes=["Nouvel An chinois"], profil=["gras"])

K("pho_boeuf", "Phở au bœuf", "Phở bò", f"{ASE} › Vietnam › Hanoï", "So", 2, 6, 40, 240, "€€", "Grand faitout, poêle.",
  "Un bouillon clair de bœuf parfumé à la badiane, cannelle et oignon grillé, nouilles de riz, bœuf cru tranché qui cuit dans le bol.",
  ["1,5 kg|d'os à moelle et jarret de bœuf|Jarret de bœuf|3", "300 g|de rumsteck très finement tranché|Rumsteck|2", "400 g|de nouilles de riz plates|Nouilles de riz / vermicelles|3", f"2|oignons + 1 morceau de gingembre grillés|{OIG}|2", "3|badianes + 1 bâton de cannelle + 4 clous de girofle|Anis étoilé (badiane)|2", "4 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|2", "1 bouquet|de basilic thaï, coriandre, menthe|Basilic thaï|2", "200 g|de pousses de soja|Germes de soja|1", f"2|citrons verts|{CITV}|1"],
  ["**Blanchir.** Os et jarret 5 min, rincés (bouillon clair).", "**Griller.** Oignons et gingembre noircis à sec, épices toastées.", "**Bouillon.** Tout dans 4 L d'eau, frémissement 3-4 h, écume ; sauce de poisson, sucre, sel.", "**Bol.** Nouilles, bœuf cru, bouillon bouillant ; herbes, pousses, citron à table."],
  age=None, kids="✓ dès 3 ans avec le bœuf bien cuit dans le bouillon.", profil=["leger"])

K("banh_mi", "Bánh mì au poulet citronnelle", "Bánh mì", f"{ASE} › Vietnam › Saïgon", "P", 1, 4, 30, 30, "€", "Poêle.",
  "Baguette croustillante, poulet mariné, pickles de carotte-daikon, concombre, coriandre, piment et mayonnaise : le sandwich franco-vietnamien.",
  ["2|baguettes|Baguette tradition|3", f"500 g|de hauts de cuisse émincés|{CUISSE}|3", "2|bâtons de citronnelle|Citronnelle|1", f"2|carottes|{CAROTTE}|1", "½|daikon|Radis noir / daikon|1", "5 cl|de vinaigre de riz|Vinaigre de riz|1", "1|concombre|Concombre|1", f"1 bouquet|de coriandre|{CORI}|1", f"4 c. à s.|de mayonnaise|SUB:mayonnaise|1", "1 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|1"],
  ["**Pickles.** Carotte et daikon en julienne, vinaigre + sucre + sel, 30 min.", "**Poulet.** Mariné citronnelle, ail, sauce de poisson, sucre ; poêlé 8 min.", "**Monter.** Pain réchauffé, mayonnaise, poulet, pickles, concombre, coriandre, piment."],
  age=3, cats=["enfants"], profil=["acide"])

K("nasi_goreng", "Nasi goreng", "Nasi goreng", f"{ASE} › Indonésie", "P", 1, 4, 15, 10, "€", "Wok.",
  "Riz sauté au kecap manis (soja sucré), ail, échalotes et piment, œuf au plat, crudités : le riz frit indonésien.",
  [f"600 g|de riz cuit froid|{RIZ}|3", "3 c. à s.|de kecap manis|Kecap manis|3", f"4|échalotes|{ECH}|2", f"3 gousses|d'ail|{AIL}|1", "1 c. à c.|de sambal|Sambal oelek|1", f"2|blancs de poulet en dés|{BLANC_P}|2", f"4|œufs|{OEUF}|2", "1|concombre et 2 tomates|Concombre|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Pâte.** Échalotes, ail, sambal pilés, frits 1 min.", "**Sauter.** Poulet 4 min, riz, kecap manis, 4 min à feu vif.", "**Servir.** Œuf au plat, crudités, cacahuètes ou oignons frits."],
  age=3, cats=["zero_dechet"], profil=["sucre", "epice"])

K("rendang", "Rendang de bœuf", "Rendang daging", f"{ASE} › Indonésie › Sumatra", "P", 2, 6, 30, 210, "€€", "Cocotte à fond épais.",
  "Bœuf cuit très longtemps dans le lait de coco et les épices jusqu'à ce que la sauce disparaisse et caramélise : intense et fondant.",
  ["1,2 kg|de paleron en gros cubes|Paleron|3", f"80 cl|de lait de coco|{COCO}|3", f"6|échalotes|{ECH}|2", f"6 gousses|d'ail|{AIL}|1", f"1 morceau|de gingembre + 1 de galanga|{GING}|2", "3|bâtons de citronnelle|Citronnelle|2", "6|feuilles de combava|Feuille de combava (kaffir)|1", f"4|piments|{PIMENT}|2", f"1 c. à c.|de curcuma|{CURC}|1", "60 g|de noix de coco râpée grillée|Noix de coco râpée|1", "1 c. à s.|de tamarin|Tamarin (pulpe)|1"],
  ["**Pâte.** Échalotes, ail, gingembre, galanga, piments, curcuma mixés.", "**Mijoter.** Pâte frite 5 min, bœuf, coco, citronnelle, combava, tamarin ; 2 h à découvert en remuant.", "**Caraméliser.** Coco grillée ; continue 30-60 min jusqu'à ce que la sauce soit absorbée et brune."],
  age=None, profil=["epice", "gras"], fetes=["Ramadan / Aïd"])

K("laksa", "Laksa au poulet et crevettes", "Curry laksa", f"{ASE} › Malaisie", "So", 2, 4, 30, 25, "€€", "Faitout.",
  "Une soupe de nouilles au curry coco, crevettes, poulet, œuf, pousses de soja et herbes : riche et parfumée.",
  ["2 c. à s.|de pâte de curry rouge|Pâte de curry rouge/verte/jaune|3", f"40 cl|de lait de coco|{COCO}|3", f"60 cl|de bouillon|{BOUILLON}|2", "250 g|de nouilles de riz|Nouilles de riz / vermicelles|3", "200 g|de crevettes|Crevettes (cuites/crues)|2", f"2|blancs de poulet|{BLANC_P}|2", f"2|œufs durs|{OEUF}|1", "150 g|de pousses de soja|Germes de soja|1", "1 bouquet|de menthe et coriandre|Menthe|1", f"1|citron vert|{CITV}|1"],
  ["**Base.** Pâte frite 2 min, coco, bouillon, 10 min.", "**Cuire.** Poulet émincé 6 min, crevettes 2 min.", "**Bol.** Nouilles, soupe, œuf, pousses, herbes, citron vert."],
  age=None, profil=["epice"])

K("amok_poisson", "Amok de poisson (Cambodge)", "Amok trey", f"{ASE} › Cambodge", "P", 2, 4, 30, 25, "€€", "Ramequins ou feuilles de bananier, cuit-vapeur.",
  "Poisson blanc cuit à la vapeur dans une crème de coco au kroeung (pâte de citronnelle) : un flan doux et parfumé.",
  ["500 g|de cabillaud ou lieu|Cabillaud / morue fraîche|3", f"30 cl|de lait de coco|{COCO}|3", f"1|œuf|{OEUF}|1", "2|bâtons de citronnelle|Citronnelle|2", "1 morceau|de galanga|Galanga|1", f"½ c. à c.|de curcuma|{CURC}|1", "4|feuilles de combava|Feuille de combava (kaffir)|1", f"3 gousses|d'ail + 2 échalotes|{AIL}|1", "1 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|1", "200 g|d'épinards ou chou|Épinard|1"],
  ["**Kroeung.** Citronnelle, galanga, curcuma, ail, échalotes, combava pilés.", "**Crème.** Coco + œuf + kroeung + sauce de poisson ; poisson en cubes.", "**Vapeur.** Épinards au fond des ramequins, appareil, 20 min. Filet de coco épais."],
  age=1, profil=["poisson"])

K("pancit_bihon", "Pancit (nouilles de riz sautées, Philippines)", "Pancit bihon", f"{ASE} › Philippines", "P", 1, 4, 20, 15, "€", "Wok.",
  "Vermicelles de riz sautés avec poulet, chou, carotte et sauce soja, citron vert : le plat des anniversaires philippins (longue vie).",
  ["250 g|de vermicelles de riz|Nouilles de riz / vermicelles|3", f"2|blancs de poulet|{BLANC_P}|2", "¼|chou|Chou blanc / rouge|2", f"2|carottes|{CAROTTE}|1", f"3 c. à s.|de sauce soja|{SOJA}|2", f"40 cl|de bouillon|{BOUILLON}|1", f"1|oignon + 3 gousses d'ail|{OIG}|1", f"1|citron vert|{CITV}|1"],
  ["**Sauter.** Oignon, ail, poulet, légumes.", "**Nouilles.** Trempées 5 min, ajoutées avec bouillon et soja : elles boivent tout.", "**Servir.** Citron vert."],
  age=1, cats=["enfants"], fetes=["Anniversaire"], profil=["leger"])
