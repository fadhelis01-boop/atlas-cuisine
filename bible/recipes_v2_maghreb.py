# -*- coding: utf-8 -*-
"""Vague 2 · Afrique du Nord : Maroc, Algérie, Tunisie, Égypte, Libye."""
from recipes_v2_base import *

M = "Afrique du Nord"

K("tajine_poulet_citron", "Tajine de poulet au citron confit et aux olives", "Djej mqualli", f"{M} › Maroc", "P", 1, 6, 25, 60, "€€", "Tajine ou cocotte.",
  "Poulet fondant au gingembre et safran, sauce onctueuse aux oignons, citron confit et olives violettes.",
  [f"1,5 kg|de cuisses de poulet|{CUISSE}|3", "2|citrons confits|Citron confit|3", "150 g|d'olives violettes|Olives (violettes, cassées)|2", f"3|oignons râpés|{OIG}|3", f"3 gousses|d'ail|{AIL}|1",
   "1 c. à c.|de gingembre en poudre|Gingembre (poudre)|1", f"½ c. à c.|de curcuma|{CURC}|1", "1 pincée|de safran|Safran (pistils)|1", f"1 bouquet|de coriandre et persil|{CORI}|1", f"4 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Mariner.** Poulet, ail, épices, huile, sel, herbes ; 1 h.", "**Cuire.** Avec les oignons râpés et un verre d'eau, à couvert, 45 min à feu doux.",
   "**Finir.** Écorce de citron confit en lanières et olives 15 min ; réduis la sauce à découvert jusqu'à onctueuse."],
  age=1, cats=["enfants"], profil=["acide"], fetes=["Ramadan / Aïd", "Repas de famille"], sa=["Thé à la menthe"])

K("tajine_kefta_oeufs", "Tajine de kefta aux œufs", "Tajine kefta", f"{M} › Maroc", "P", 1, 4, 20, 25, "€", "Tajine ou sauteuse avec couvercle.",
  "Boulettes épicées qui mijotent dans une sauce tomate au cumin, avec des œufs pochés dedans à la fin.",
  [f"500 g|de bœuf ou d'agneau haché|{HACHE}|3", f"6|tomates râpées|{TOM}|3", f"4|œufs|{OEUF}|2", f"1|oignon|{OIG}|1", f"2 c. à c.|de cumin|{CUMIN}|2", f"1 c. à c.|de paprika|{PAPRIKA}|1", f"1 bouquet|de persil et coriandre|{CORI}|1", f"3 gousses|d'ail|{AIL}|1", f"3 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Kefta.** Viande, oignon râpé, la moitié des herbes et des épices, sel : petites boulettes.", "**Sauce.** Tomates, ail, reste des épices, huile, 15 min.", "**Mijoter.** Boulettes 10 min ; casse les œufs, couvre 5 min. Herbes, pain."],
  age=1, cats=["enfants"], profil=["viande_rouge", "epice"])

K("harira", "Harira", "Harira", f"{M} › Maroc", "So", 2, 8, 30, 90, "€", "Grand faitout.",
  "La soupe de rupture du jeûne : tomate, lentilles, pois chiches, herbes, épices et un peu de viande, liée à la farine.",
  ["300 g|d'agneau ou de bœuf en petits dés|Épaule d'agneau|2", "150 g|de lentilles vertes|Lentilles vertes / brunes|2", f"150 g|de pois chiches trempés|{POIS}|2", f"6|tomates mixées|{TOM}|3", f"2 c. à s.|de concentré|{CONC}|1",
   f"1|oignon|{OIG}|1", "2|branches de céleri|Céleri-branche|1", f"1 bouquet|de coriandre + 1 de persil|{CORI}|2", "1 c. à c.|de gingembre, ½ de cannelle, ½ de curcuma|Gingembre (poudre)|1", f"40 g|de farine|{F55}|1", f"50 g|de vermicelles|{PATES}|1", f"1|citron|{CIT}|1"],
  ["**Base.** Viande, oignon, céleri, herbes hachées, épices, huile ; 10 min. Pois chiches, 2 L d'eau ; 45 min.", "**Ajouter.** Lentilles, tomates, concentré ; 30 min.",
   "**Lier.** Farine délayée dans 25 cl d'eau, versée en remuant ; vermicelles 8 min : la soupe devient veloutée. Citron et dattes au service."],
  age=1, cats=["enfants"], fetes=["Ramadan / Aïd"], profil=["epice"])

K("rfissa", "Rfissa express (poulet, lentilles, msemen)", "Rfissa", f"{M} › Maroc", "P", 2, 6, 30, 75, "€€", "Cocotte, poêle.",
  "Poulet aux lentilles et au fenugrec sur des crêpes feuilletées déchirées qui boivent la sauce : le plat des grandes occasions.",
  [f"1,5 kg|de poulet en morceaux|{CUISSE}|3", "150 g|de lentilles vertes|Lentilles vertes / brunes|2", f"3|oignons|{OIG}|2", "1 c. à s.|de graines de fenugrec trempées|Fenugrec|2", "1 c. à c.|de ras el-hanout|Ras el-hanout|2",
   "1 pincée|de safran|Safran (pistils)|1", "8|msemen ou crêpes feuilletées|Farine de blé T55|3", f"4 c. à s.|d'huile|{HO}|1"],
  ["**Poulet.** Avec oignons, épices, fenugrec, huile, sel ; 1 L d'eau ; 45 min.", "**Lentilles.** 30 min dans la sauce.", "**Servir.** Msemen réchauffés et déchirés en lanières dans un grand plat, sauce dessus, poulet et lentilles."],
  age=1, fetes=["Repas de famille"], profil=["epice"])

K("zaalouk", "Zaalouk (caviar d'aubergine marocain)", "Zaalouk", f"{M} › Maroc", "E", 1, 6, 15, 30, "€", "Sauteuse.",
  "Aubergine et tomate écrasées au cumin, à l'ail et au paprika, servies tièdes avec du pain.",
  ["2|aubergines|Aubergine|3", f"4|tomates|{TOM}|2", f"3 gousses|d'ail|{AIL}|1", f"1 c. à c.|de cumin + 1 de paprika|{CUMIN}|2", f"5 c. à s.|d'huile d'olive|{HO}|2", f"1 bouquet|de coriandre|{CORI}|1", f"½|citron|{CIT}|1"],
  ["**Cuire.** Aubergines en cubes (ou cuites à la vapeur) et tomates pelées, ail, épices, huile ; 25 min en écrasant.", "**Finir.** Jusqu'à ce que l'huile ressorte ; coriandre, citron."],
  keep="4 jours au frigo.", age=1, cats=["enfants"], profil=["leger", "epice"], fetes=["Ramadan / Aïd"])

K("briouates_kefta", "Briouates à la viande hachée", "Briwat", f"{M} › Maroc", "E", 2, 24, 40, 15, "€", "Poêle, pinceau, plaque.",
  "Petits triangles croustillants de brick farcis de viande épicée : au four, plus légers qu'en friture.",
  [f"400 g|de bœuf haché|{HACHE}|3", "12|feuilles de brick|Pâte filo / feuilles de brick|3", f"1|oignon|{OIG}|1", f"1 c. à c.|de cumin, paprika, cannelle|{CUMIN}|2", f"1 bouquet|de persil et coriandre|{CORI}|1", f"1|œuf|{OEUF}|1", f"50 g|de beurre fondu|{BEURRE}|1"],
  ["**Farce.** Oignon, viande, épices 10 min ; hors du feu, herbes et œuf.", "**Plier.** Bandes de brick beurrées, une cuillère de farce, plie en triangles.", "**Cuire.** 15 min à 200 °C, dorés."],
  age=3, cats=["enfants"], fetes=["Ramadan / Aïd", "Apéritif dînatoire"], profil=["gras"])

K("cornes_gazelle", "Cornes de gazelle", "Kaab el ghzal", f"{M} › Maroc", "G", 3, 30, 75, 15, "€€", "Rouleau, plaque.",
  "Une pâte fine qui enferme une pâte d'amande parfumée à la fleur d'oranger : délicat et peu sucré.",
  ["300 g|de poudre d'amande|Farine d'amande / poudre d'amande|3", "150 g|de sucre glace|Sucre glace|2", f"30 g|de beurre fondu|{BEURRE}|1", "3 c. à s.|d'eau de fleur d'oranger|Eau de fleur d'oranger|2", f"200 g|de farine|{F55}|2", f"1|œuf|{OEUF}|1", f"1 pincée|de cannelle|{CANN}|0"],
  ["**Farce.** Amande, sucre, beurre, fleur d'oranger, cannelle : boudins de 6 cm.", "**Pâte.** Farine, œuf, 30 g de beurre, fleur d'oranger, eau : très souple, 30 min de repos ; étale très fin.", "**Façonner.** Enroule chaque boudin, courbe en croissant, pique.", "**Cuire.** 15 min à 180 °C : à peine blonds."],
  keep="2 semaines en boîte.", age=1, fetes=["Ramadan / Aïd"], profil=["sucre"])

K("lablabi", "Lablabi (soupe de pois chiches)", "Lablabi", f"{M} › Tunisie", "So", 1, 4, 15, 60, "€", "Faitout.",
  "Pois chiches au bouillon d'ail et de cumin, sur du pain rassis, avec harissa, huile d'olive, câpres et un œuf : le petit-déjeuner des ouvriers tunisois.",
  [f"400 g|de pois chiches trempés|{POIS}|3", f"6 gousses|d'ail|{AIL}|2", f"2 c. à c.|de cumin|{CUMIN}|2", "1 c. à s.|de harissa|Harissa (tube/pâte)|1", "200 g|de pain rassis|Pain rassis (réservé)|2", f"4|œufs (mollets ou crus pochés)|{OEUF}|1", f"6 c. à s.|d'huile d'olive|{HO}|1", "1 c. à s.|de câpres|Câpres|1", f"1|citron|{CIT}|1"],
  ["**Cuire.** Pois chiches 1 h avec ail ; sel, cumin.", "**Bol.** Pain déchiré, louche de pois chiches et bouillon, harissa, cumin, huile, câpres, œuf mollet, citron."],
  age=1, cats=["zero_dechet"], profil=["epice"])

K("brik_oeuf", "Brick à l'œuf", "Brik", f"{M} › Tunisie", "E", 2, 4, 15, 5, "€", "Poêle, huile.",
  "Une feuille de brick pliée sur un œuf, thon, câpres et persil, frite : croustillant et jaune coulant.",
  ["4|feuilles de brick|Pâte filo / feuilles de brick|3", f"4|œufs|{OEUF}|3", "100 g|de thon|Thon en conserve|2", "1 c. à s.|de câpres|Câpres|1", f"1 bouquet|de persil|{PERSIL}|1", "1 c. à s.|de parmesan ou fromage râpé|Parmesan / Parmigiano|1?", "30 cl|d'huile|Huile de tournesol / colza|1", f"1|citron|{CIT}|1"],
  ["**Garnir.** Sur la feuille dans une assiette : thon, câpres, persil au centre, puis l'œuf.", "**Frire.** Plie en demi-lune, glisse dans l'huile chaude, 1 min par face.", "**Servir.** Égoutte, citron."],
  age=None, kids="✓ dès 3 ans avec l'œuf bien cuit.", profil=["poisson", "gras"], fetes=["Ramadan / Aïd"])

K("couscous_poisson", "Couscous au poisson (Sfax)", "Couscous au poisson", f"{M} › Tunisie › Sfax", "P", 2, 6, 40, 60, "€€", "Couscoussier.",
  "Darnes de mérou ou de dorade sur une semoule parfumée et un bouillon rouge aux légumes : le couscous du littoral.",
  ["1 kg|de darnes de poisson ferme (dorade, mérou, lotte)|Dorade|3", "500 g|de semoule moyenne|Semoule de couscous|3", f"2 c. à s.|de concentré de tomate|{CONC}|2", "1 c. à s.|de harissa|Harissa (tube/pâte)|1", f"2|pommes de terre|{PDT}|1",
   "2|courgettes|Courgette|1", f"2|carottes|{CAROTTE}|1", f"1|oignon|{OIG}|1", f"1 c. à c.|de cumin, carvi, paprika|{CUMIN}|1", f"5 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Bouillon.** Oignon, concentré, harissa, épices dans l'huile ; 2 L d'eau, légumes, 30 min.", "**Semoule.** Mouillée, huilée, cuite 2 fois 15 min à la vapeur du bouillon.", "**Poisson.** Les 12 dernières minutes dans le bouillon. Sers la semoule arrosée."],
  age=3, profil=["poisson", "epice"])

K("makroud", "Makrouds au four", "Makroud", f"{M} › Tunisie › Kairouan", "G", 2, 30, 45, 25, "€", "Plaque, casserole.",
  "Losanges de semoule fourrés de pâte de dattes, trempés dans un sirop au miel : version au four, moins grasse.",
  ["500 g|de semoule moyenne|Semoule de blé (fine/moyenne)|3", "300 g|de pâte de dattes|Pâte de dattes|3", f"150 g|de beurre fondu|{BEURRE}|2", "15 cl|d'eau tiède|-|0", f"150 g|de miel|{MIEL}|2", "2 c. à s.|d'eau de fleur d'oranger|Eau de fleur d'oranger|1", f"1 c. à c.|de cannelle|{CANN}|1"],
  ["**Pâte.** Semoule + beurre, 30 min ; eau, pâte souple.", "**Fourrer.** Boudin de pâte, rainure, pâte de dattes cannelle, referme ; aplatis, losanges.", "**Cuire et tremper.** 25 min à 180 °C ; plonge-les chauds dans le miel tiède à la fleur d'oranger."],
  keep="2 semaines en boîte.", age=1, fetes=["Ramadan / Aïd"], profil=["sucre"])

K("bourek_algerien", "Bourek à la viande et pommes de terre", "Bourek", f"{M} › Algérie", "E", 1, 12, 30, 15, "€", "Poêle, plaque.",
  "Cigares croustillants de brick à la viande hachée, pomme de terre écrasée, œuf et persil.",
  [f"300 g|de bœuf haché|{HACHE}|3", f"2|pommes de terre cuites|{PDT}|2", "12|feuilles de brick|Pâte filo / feuilles de brick|3", f"1|oignon|{OIG}|1", f"2|œufs|{OEUF}|1", f"1 bouquet|de persil|{PERSIL}|1", "60 g|de fromage râpé|Gruyère / comté / emmental / beaufort|1?", f"1 c. à c.|de cannelle|{CANN}|0"],
  ["**Farce.** Viande et oignon dorés, cannelle ; pommes de terre écrasées, persil, œufs, fromage.", "**Rouler.** En cigares, bords collés à l'eau.", "**Cuire.** Au four 15 min à 200 °C, huilés (ou poêlés)."],
  age=3, cats=["enfants"], fetes=["Ramadan / Aïd"], profil=["gras"])

K("loubia", "Loubia (haricots blancs à la tomate)", "Loubia", f"{M} › Algérie", "P", 1, 6, 15, 90, "€", "Cocotte.",
  "Des haricots blancs mijotés à l'ail, au cumin et à la tomate : un plat de tous les jours, nourrissant et économique.",
  ["500 g|de haricots blancs trempés|Haricots blancs / lingots|3", f"3|tomates|{TOM}|2", f"1 c. à s.|de concentré|{CONC}|1", f"5 gousses|d'ail|{AIL}|2", f"2 c. à c.|de cumin + 1 de paprika|{CUMIN}|2", f"1|oignon|{OIG}|1", f"4 c. à s.|d'huile d'olive|{HO}|1", f"1 bouquet|de coriandre|{CORI}|1"],
  ["**Cuire.** Haricots 1 h dans l'eau non salée.", "**Sauce.** Oignon, ail, épices, tomates, concentré ; haricots et un peu d'eau ; 30 min. Sel à la fin, coriandre."],
  age=1, cats=["enfants"], profil=["epice"])

K("chtitha_poulet", "Chtitha djej (poulet sauce rouge)", "Chtitha djej", f"{M} › Algérie", "P", 1, 6, 20, 50, "€", "Cocotte.",
  "Poulet en sauce rouge à l'ail, au paprika et au carvi, avec pois chiches : relevé et réconfortant.",
  [f"1,2 kg|de cuisses de poulet|{CUISSE}|3", f"200 g|de pois chiches cuits|{POIS}|2", f"6 gousses|d'ail|{AIL}|2", f"2 c. à c.|de paprika|{PAPRIKA}|2", "1 c. à c.|de carvi|Carvi / fenouil / anis vert (graines)|1", f"1 pincée|de piment|{CAYENNE}|1", f"2 c. à s.|de concentré|{CONC}|1", f"4 c. à s.|d'huile|{HO}|1"],
  ["**Dorer.** Poulet dans l'huile.", "**Sauce.** Ail pilé, épices, concentré, 50 cl d'eau ; 35 min.", "**Finir.** Pois chiches 10 min, sauce nappante. Avec pain ou frites."],
  age=3, profil=["epice"])

K("mhadjeb", "Mhadjeb (crêpes farcies à la tomate)", "Mhajeb", f"{M} › Algérie", "Pa", 2, 10, 50, 30, "€", "Poêle, plan huilé.",
  "Crêpes de semoule étirées très fin, farcies d'une chakchouka oignon-tomate, pliées et dorées : la street-food d'Alger.",
  ["500 g|de semoule fine|Semoule de blé (fine/moyenne)|3", "30 cl|d'eau tiède|-|0", f"1 c. à c.|de sel|{SEL}|0", f"4|oignons|{OIG}|2", f"6|tomates|{TOM}|3", f"1|poivron|{POIVRON}|1", f"1 c. à c.|de paprika|{PAPRIKA}|1", f"10 cl|d'huile|{HN}|1"],
  ["**Farce.** Oignons, poivron, tomates, paprika fondus 30 min jusqu'à épais. Refroidis.", "**Pâte.** Semoule, sel, eau, pétris 15 min : très élastique. Boules huilées, 30 min.",
   "**Étirer.** À la main huilée, jusqu'à transparent ; farce au centre, plie en carré.", "**Cuire.** 3 min par face."],
  age=1, cats=["pains"], profil=["leger"], fetes=["Ramadan / Aïd"])

K("kalb_el_louz", "Kalb el louz (gâteau de semoule aux amandes)", "Qalb el louz", f"{M} › Algérie", "G", 2, 20, 25, 720, "€", "Plat à four carré, casserole.",
  "Un gâteau de semoule fourré aux amandes, imbibé de sirop à la fleur d'oranger : fondant, se prépare la veille.",
  ["500 g|de semoule moyenne|Semoule de blé (fine/moyenne)|3", f"150 g|de sucre|{SUCRE}|2", f"125 g|de beurre fondu|{BEURRE}|2", "25 cl|d'eau de fleur d'oranger + eau|Eau de fleur d'oranger|2", "200 g|d'amandes en poudre|Farine d'amande / poudre d'amande|2", f"60 cl|de sirop (500 g sucre + 50 cl eau + citron)|{SUCRE}|2"],
  ["**Repos.** Semoule, sucre, beurre ; mouille à l'eau de fleur d'oranger, sable mouillé. 8 h.", "**Monter.** Moitié tassée, amandes sucrées-cannelle, l'autre moitié ; losanges, amande.", "**Cuire et sirop.** 50 min à 180 °C, sirop tiède sur gâteau chaud, il boit tout."],
  age=1, fetes=["Ramadan / Aïd"], profil=["sucre"])

K("ful_medames", "Ful medames", "Fūl medammes", f"{M} › Égypte", "P", 1, 4, 10, 15, "€", "Casserole.",
  "Fèves mijotées écrasées avec ail, cumin, citron et beaucoup d'huile d'olive : le petit-déjeuner égyptien.",
  ["800 g|de fèves cuites (bocal)|Ful medames (fèves)|3", f"3 gousses|d'ail|{AIL}|2", f"1 c. à c.|de cumin|{CUMIN}|2", f"1|citron|{CIT}|2", f"6 c. à s.|d'huile d'olive|{HO}|2", f"2|tomates|{TOM}|1", f"1 bouquet|de persil|{PERSIL}|1", f"2|œufs durs|{OEUF}|1"],
  ["**Chauffer.** Fèves avec leur jus 10 min.", "**Écraser.** Grossièrement avec ail, cumin, citron, sel.", "**Servir.** Huile, tomate, persil, œuf dur, pain pita."],
  age=1, cats=["enfants"], profil=["leger"], fetes=["Ramadan / Aïd"])

K("koshari", "Koshari", "Koshary", f"{M} › Égypte › Le Caire", "P", 2, 6, 40, 40, "€", "3 casseroles, poêle.",
  "Riz, lentilles, pâtes, sauce tomate vinaigrée et oignons frits croustillants : le plat national, végétarien et généreux.",
  [f"250 g|de riz|{RIZ}|2", "200 g|de lentilles brunes|Lentilles vertes / brunes|2", f"200 g|de petites pâtes|{PATES}|2", f"200 g|de pois chiches cuits|{POIS}|1", f"4|oignons|{OIG}|3",
   f"500 g|de passata|{PELEES}|2", f"4 gousses|d'ail|{AIL}|1", "3 c. à s.|de vinaigre|Vinaigre blanc|1", f"1 c. à c.|de cumin|{CUMIN}|1", f"1 pincée|de piment|{CAYENNE}|1", "15 cl|d'huile|Huile de tournesol / colza|1"],
  ["**Oignons.** Fines lamelles frites jusqu'à brun-croustillant ; garde l'huile.", "**Lentilles et riz.** Lentilles 15 min, puis riz avec, dans l'huile des oignons ; 15 min.", "**Sauce.** Ail, cumin, piment, passata, vinaigre ; 15 min.", "**Servir.** Riz-lentilles, pâtes, pois chiches, sauce, oignons frits."],
  age=1, cats=["enfants"], profil=["acide", "epice"])

K("om_ali", "Om Ali (pudding feuilleté)", "Om Ali", f"{M} › Égypte", "D", 1, 6, 15, 20, "€", "Plat à four.",
  "Feuilletage en morceaux, lait sucré, raisins, noix et coco, gratiné : le pain perdu égyptien.",
  ["1|pâte feuilletée cuite et cassée (ou croissants rassis)|Pâte feuilletée (prête)|3", f"75 cl|de lait|{LAIT}|3", f"20 cl|de crème|{CL}|1", f"80 g|de sucre|{SUCRE}|2", "50 g|de raisins secs|Raisins secs|1", "60 g|de pistaches, amandes|Pistache|1", "30 g|de noix de coco râpée|Noix de coco râpée|1"],
  ["**Monter.** Feuilleté cassé, fruits secs, coco dans le plat.", "**Lait.** Chaud, sucré, versé dessus ; crème en surface.", "**Gratiner.** 20 min à 200 °C."],
  age=1, cats=["enfants", "zero_dechet"], fetes=["Ramadan / Aïd"], profil=["sucre"])

K("basboussa", "Basboussa (gâteau de semoule au sirop)", "Basbousa", f"{M} › Égypte", "G", 1, 16, 15, 35, "€", "Plat à four, casserole.",
  "Gâteau de semoule au yaourt et à la noix de coco, imbibé de sirop citronné : fondant et parfumé.",
  ["300 g|de semoule fine|Semoule de blé (fine/moyenne)|3", f"200 g|de yaourt|{YAO}|2", f"150 g|de sucre|{SUCRE}|2", f"100 g|de beurre fondu|{BEURRE}|2", "50 g|de noix de coco râpée|Noix de coco râpée|1", f"1 c. à c.|de levure chimique|{LEVC}|0", "16|amandes|Amande (entière, effilée, poudre)|1", f"40 cl|de sirop (300 g sucre + eau + citron)|{SUCRE}|2"],
  ["**Pâte.** Tout mélanger, étaler, prédécouper en losanges, une amande sur chacun.", "**Cuire.** 30 min à 180 °C, doré.", "**Sirop.** Froid sur le gâteau chaud. Attends 1 h."],
  age=1, cats=["enfants"], fetes=["Ramadan / Aïd"], profil=["sucre"])
