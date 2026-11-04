# -*- coding: utf-8 -*-
"""Vague 9 · Favoris TikTok ajoutés entre le 29/10 et le 04/11/2026 (compte connecté par le propriétaire). Fiches
réécrites (repères et durées ATLAS) et créditées (`credit`) ; rien n'est recopié des légendes. Quand la légende ne donne
que le nom du plat (widjila, orzo cajun), la fiche suit la recette de référence et la vidéo est créditée comme source
d'idée. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *
from recipes_v6_tiktok_plats import C

PAINS_BURGER = "SUB:pains_burger"; CAFE = "-"

# ———————————————————————————————— plats
K("kebab_poulet_pain_maison", "Kebab de poulet maison (pain fait maison, poulet mariné au yaourt, sauce blanche)", "Kebab maison", "France › Food fusion", "P", 2, 6, 45, 90, "€", "Saladier, poêle en fonte ou plaque, rouleau.",
  "Le kebab des snacks, en entier à la maison : des pains moelleux cuits à la poêle, du blanc de poulet mariné au yaourt grec, au concentré de tomate et aux épices puis saisi et émincé, crudités et sauce blanche. Bien meilleur et moins gras.",
  [f"500 g|de farine|{F55}|3", f"8 g|de levure boulangère sèche (+ 1 c. à c. de sucre)|{LEV}|1", f"800 g|de blancs de poulet|{BLANC_P}|3", f"150 g|de yaourt grec|{GREC}|2", f"35 g|de concentré de tomate|{CONC}|1", f"1 c. à c.|de paprika, de cumin et d'origan|{PAPRIKA}|1", f"3|gousses d'ail|{AIL}|1", f"1/2|citron (jus)|{CIT}|2", f"4 c. à s.|d'huile d'olive|{HO}|1", "1|salade, tomates, oignon rouge|Salade (laitue, batavia)|2", "6 c. à s.|de sauce blanche|SUB:sauce_blanche|2"],
  ["**Pâte.** Farine, sel, levure, sucre ; 27,5 cl d'eau tiède, 2 c. à s. d'huile ; pétrie 8 min : souple et lisse ; 1 h à couvert : doublée.",
   "**Mariner.** Poulet en lanières épaisses, yaourt, concentré, épices, ail râpé, jus de citron, sel, poivre, 2 c. à s. d'huile : au moins 1 h au frais (une nuit, c'est mieux).",
   "**Pains.** 6 boules aplaties à 1 cm ; poêle sèche bien chaude, 2 à 3 min par face : ils gonflent et prennent des taches dorées ; sous un torchon.",
   "**Poulet.** Poêle fumante, en 2 fois, 4 min par face sans bouger : bords grillés, 74 °C à cœur ; 5 min de repos, émincé fin comme à la broche.",
   "**Monter.** Pain ouvert, sauce blanche, poulet, salade, tomate, oignon ; un trait de citron."],
  keep="Poulet cuit : 2 jours au frigo ; pains : se congèlent.", age=3, cats=["enfants"], profil=["acide", "epice"], tech=["Pétrir une pâte riche"],
  credit=C(("@lescasserolesdebineta", "https://www.tiktok.com/@lescasserolesdebineta/video/7689011214755630368")))
K("riz_saute_boeuf_asiatique", "Riz sauté au bœuf façon asiatique (sauce huître, poivrons, gingembre)", "Riz sauté au bœuf", "Asie de l'Est › Chine", "P", 1, 3, 20, 10, "€", "Wok ou grande poêle.",
  "Le riz sauté des traiteurs, au bœuf : des lamelles marinées à la fécule (elles restent tendres), saisies d'un coup, puis du riz froid sauté avec poivrons, oignon, ail et gingembre, et une sauce soja-huître. Un plat complet en 10 minutes de cuisson.",
  ["300 g|de bœuf tendre (rumsteck)|Rumsteck|3", f"350 g|de riz cuit la veille, froid|{RIZ}|3", f"1|oignon|{OIG}|1", f"1|poivron (½ rouge, ½ vert)|{POIVRON}|2", f"2|gousses d'ail|{AIL}|1", f"1 c. à c.|de gingembre râpé|{GING}|1", f"3 c. à s.|de sauce soja (dont 1 foncée)|{SOJA}|2", "2 c. à s.|de sauce d'huître|Sauce d'huître|2", "1 c. à c.|de fécule de maïs|Fécule de maïs (maïzena)|1", "1 c. à s.|d'huile de sésame|Huile de sésame (grillée)|1", f"1/2|citron vert|{CITV}|1"],
  ["**Mariner.** Bœuf en lamelles fines contre les fibres, 1 c. à s. de soja, fécule, poivre, quelques gouttes de sésame : 10 min.",
   "**Saisir.** Wok fumant, 1 c. à s. d'huile, bœuf étalé, 2 min sans remuer puis 30 s : doré dehors, encore rosé ; réservé.",
   "**Légumes.** Oignon et poivron en dés, ail, gingembre, 3 min à feu vif : croquants et parfumés.",
   "**Sauter.** Riz froid égrené, 3 min en faisant sauter : il grésille, les grains se détachent ; sauces, bœuf, 1 min : tout est enrobé et brillant ; sésame, citron vert à table."],
  tips=["Le riz doit être froid (cuit la veille) : chaud, il colle et fait de la purée."], keep="1 jour au frigo ; se réchauffe au wok.", age=3, cats=["express"], profil=["gras"], tech=["Sauter au wok"],
  credit=C(("@latelierdekhady", "https://www.tiktok.com/@latelierdekhady/video/7701362168532372768")))
K("orzo_poulet_cajun", "Orzo crémeux au poulet cajun, en une seule poêle", "Cajun chicken orzo", "Amérique du Nord › États-Unis", "P", 1, 4, 15, 25, "€", "Sauteuse avec couvercle.",
  "Le dîner en une poêle qui tourne partout aux États-Unis : du poulet frotté d'épices cajun et doré, puis des pâtes langues d'oiseau (orzo) cuites directement dans le bouillon avec la tomate, finies à la crème, au parmesan et aux épinards.",
  [f"3|blancs de poulet|{BLANC_P}|3", "2 c. à c.|d'épices cajun|Mélange cajun|2", f"250 g|d'orzo (langues d'oiseau)|{PATES}|3", f"60 cl|de bouillon de volaille|{BOUILLON}|2", f"200 g|de coulis de tomate|{PELEES}|1", f"10 cl|de crème|{CL}|2", f"40 g|de parmesan|{PARM}|1", "2|poignées d'épinards|Épinard|1", f"1|oignon et 2 gousses d'ail|{OIG}|1", f"1/2|citron|{CIT}|1"],
  ["**Poulet.** Coupé en deux dans l'épaisseur, frotté d'épices cajun et de sel ; 4 min par face à la poêle huilée : croûte foncée, presque cuit ; réservé.",
   "**Base.** Oignon et ail, 3 min ; orzo, 1 min : nacré ; bouillon et coulis, porté à frémir.",
   "**Cuire.** Couvert, 10 min à feu doux en remuant 2 fois : orzo tendre, liquide presque absorbé ; poulet posé dessus, 5 min : 74 °C à cœur.",
   "**Finir.** Poulet retiré et tranché ; crème, parmesan, épinards, 1 min : crémeux, épinards tombés ; jus de citron, poulet dessus."],
  keep="2 jours au frigo.", age=3, cats=["enfants", "express"], profil=["epice", "gras"],
  credit=C(("@simplylemmons", "https://www.tiktok.com/@simplylemmons/video/7688446831616970015")))
K("widjila", "Widjila (pains cuits à la vapeur, sauce d'agneau épicée, Tombouctou)", "Widjila / woudjila", "Afrique subsaharienne › Mali", "P", 2, 6, 40, 120, "€€", "Couscoussier, cocotte, saladier.",
  "Le plat songhaï de Tombouctou : de grosses boules de pâte levée cuites à la vapeur dans le couscoussier, au-dessus de la sauce, puis servies déchirées et arrosées d'une sauce d'agneau mijotée à la tomate et aux épices. Parfois avec des dattes.",
  [f"500 g|de farine|{F55}|3", f"7 g|de levure boulangère sèche|{LEV}|1", f"1|œuf|{OEUF}|1", "1 kg|d'épaule d'agneau en morceaux|Épaule d'agneau|3", f"3|oignons|{OIG}|2", f"3|tomates (+ 1 c. à s. de concentré)|{TOM}|2", f"3|gousses d'ail|{AIL}|1", f"1 c. à c.|de poivre et de piment doux|{POIVRE}|1", f"1|piment frais|{PIMENT}|1", "4|dattes (facultatif)|Datte (medjool, deglet)|1?", f"1|citron|{CIT}|1"],
  ["**Pâte.** Farine, levure, sel, œuf ; eau tiède peu à peu (30 cl environ), pétrie 10 min : pâte molle et élastique ; 1 h à couvert.",
   "**Sauce.** Agneau saisi dans la cocotte du couscoussier, 8 min : bien doré ; oignons, 5 min ; ail, tomates mixées, concentré, épices, piment entier, sel, 1 l d'eau ; à frémissement.",
   "**Vapeur.** Pâte en 6 boules ; dans le panier huilé, au-dessus de la sauce, couvercle ; 40 min sans ouvrir les 30 premières : gonflées, sèches au toucher. La sauce mijote dessous en même temps (1 h 30 en tout) : agneau fondant.",
   "**Servir.** Dattes dans la sauce les 15 dernières minutes ; boules déchirées dans les assiettes, sauce et viande par-dessus, citron à table."],
  keep="Sauce : 3 jours au frigo ; pains : le jour même.", age=3, cats=["fetes"], fetes=["Repas de famille"], profil=["epice", "acide"], tech=["Mijoter"],
  credit=C(("@ammey.food", "https://www.tiktok.com/@ammey.food/video/7703623087304002849")))
K("crispy_chicken_caesar_burger", "Burger de poulet croustillant, salade César et parmesan", "Crispy chicken Caesar burger", "Europe du Nord › Royaume-Uni", "P", 1, 4, 30, 20, "€€", "Casserole à friture, 3 assiettes creuses.",
  "La vidéo la plus enregistrée de la semaine : du poulet épicé pané au panko et frit, dans un pain burger avec une salade romaine enrobée de sauce César (mayonnaise, moutarde, ail, parmesan), et encore du parmesan râpé dessus.",
  [f"500 g|de blancs de poulet en 4 escalopes|{BLANC_P}|3", "4|pains burger|SUB:pains_burger|3", f"1 c. à c.|de paprika (+ ail et oignon en poudre)|{PAPRIKA}|1", f"60 g|de farine|{F55}|1", f"2|œufs|{OEUF}|1", "100 g|de panko|Chapelure|2", "6 c. à s.|de mayonnaise|SUB:mayonnaise|2", f"1 c. à s.|de moutarde|{DIJON}|1", f"60 g|de parmesan|{PARM}|2", "1|cœur de laitue romaine|Salade (laitue, batavia)|2", f"1/2|citron|{CIT}|1", f"50 cl|d'huile de friture|{HN}|1"],
  ["**Mariner.** Escalopes aplaties à 1,5 cm, paprika, ail et oignon en poudre, sel, poivre, 1 c. à s. d'huile : 30 min.",
   "**Paner.** Farine épicée, œufs battus, panko bien pressé.",
   "**Frire.** 7 à 8 min à 165 °C, retournés à mi-cuisson : dorés, 74 °C à cœur ; égouttés sur une grille.",
   "**Sauce.** Mayonnaise, moutarde, ail râpé, 3 c. à s. de parmesan, jus de citron, eau pour la détendre : nappante ; romaine émincée enrobée d'une partie.",
   "**Monter.** Pain toasté, sauce, poulet, salade César, parmesan râpé, encore un trait de sauce."],
  keep="Le jour même.", age=3, cats=["enfants"], profil=["gras", "acide"], tech=["Frire en sécurité"],
  credit=C(("@zoyacooks7", "https://www.tiktok.com/@zoyacooks7/video/7702890935159360790")))
K("ramen_miso_curry_coco_boeuf", "Ramen crémeux miso-curry au lait de coco et bœuf haché (version sans porc)", "Creamy miso curry ramen", "Asie de l'Est › Japon", "P", 2, 2, 20, 20, "€€", "Casserole, poêle, petite casserole pour les œufs.",
  "Un bol réconfortant : un bouillon soyeux au lait de coco, au miso et à la pâte de curry, parfumé à la citronnelle et au combava, des nouilles ramen, de la viande hachée caramélisée et salée-sucrée, et un œuf mollet. La recette d'origine est au porc ; ici au bœuf (ou au poulet) haché.",
  ["2|portions de nouilles ramen|Nouilles ramen|3", "250 g|de bœuf haché (ou poulet haché)|Bœuf haché|3", "2 c. à s.|de miso blanc|Miso|2", "1 c. à s.|de pâte de curry rouge|Pâte de curry rouge/verte/jaune|2", "20 cl|de lait de coco|Lait de coco / crème de coco|2", f"50 cl|de bouillon de volaille|{BOUILLON}|2", "1|tige de citronnelle et 2 feuilles de combava|Citronnelle|1", f"2|gousses d'ail et 2 cm de gingembre|{GING}|1", "1 c. à c.|de sauce de poisson (nuoc-mâm)|Sauce de poisson (nuoc-mâm, nam pla)|1", f"2|œufs|{OEUF}|2", f"1|citron vert|{CITV}|2"],
  ["**Œufs.** 6 min 30 dans l'eau bouillante, eau glacée : blanc pris, jaune coulant ; écalés.",
   "**Viande.** Poêle chaude, haché étalé, 5 min sans trop remuer : bien grillé ; 1 c. à s. de soja, 1 min : laqué et brillant.",
   "**Bouillon.** Ail et gingembre râpés, citronnelle écrasée, 1 min dans un peu d'huile ; pâte de curry, 1 min : elle sent fort ; bouillon, lait de coco, combava, 10 min à frémissement ; hors du feu, miso délayé dans une louche, sauce de poisson, jus de citron vert.",
   "**Servir.** Nouilles cuites à part (3 à 4 min), égouttées, dans les bols ; bouillon brûlant filtré, viande, œuf coupé en deux, quelques gouttes de citron vert."],
  tips=["Le miso ne doit pas bouillir : il perd son parfum.", "Version d'origine : porc haché."], keep="Bouillon : 2 jours au frigo, nouilles à cuire au moment.", age=6, cats=[], profil=["epice", "gras", "acide"],
  credit=C(("@dishcovery_", "https://www.tiktok.com/@dishcovery_/video/7683625349653024022")))
K("rougag_dajaj", "Rougag dajaj (poulet aux légumes sur feuilles de pâte fine, Algérie)", "Rougag / rougague dajaj", "Afrique du Nord › Algérie", "P", 2, 6, 50, 120, "€€", "Tajine ou cocotte, grande poêle, saladier.",
  "Le plat de fête de l'Oranie : du poulet mijoté avec carottes, navets, courgette et pois chiches dans une sauce rouge au ras el-hanout, servi sur de fines galettes de semoule et de farine qui boivent tout le jus.",
  [f"1,2 kg|de poulet en 6 morceaux|{CUISSE}|3", f"6|carottes|{CAROTTE}|2", "3|navets|Navet / navet boule d'or|2", "1|courgette|Courgette|1", f"200 g|de pois chiches cuits|{POIS}|2", f"1|oignon|{OIG}|1", f"1 c. à s.|de concentré de tomate|{CONC}|1", "1 c. à c.|de ras el-hanout (+ curcuma, paprika, ½ c. à c. de cannelle)|Ras el-hanout|2", "300 g|de semoule fine (+ 300 g de farine)|Semoule de blé (fine/moyenne)|3", f"2 c. à s.|d'huile d'olive|{HO}|1", f"1|citron|{CIT}|1"],
  ["**Saisir.** Huile, poulet, 6 min : doré ; oignon, épices, concentré, 2 min : ça sent les épices grillées.",
   "**Mijoter.** Carottes coupées en deux, navets en quartiers, 75 cl d'eau, sel ; couvert, 1 h 30 à feu doux : sauce rouge et parfumée ; courgette et pois chiches, 20 min : légumes fondants.",
   "**Pâte.** Semoule, farine, sel ; 38 cl d'eau tiède peu à peu, pétrie 15 min : souple, ne colle plus ; en boules de la taille d'une mandarine, 20 min sous un film huilé.",
   "**Cuire les feuilles.** Chaque boule étalée très fin à la main huilée (on voit à travers) ; poêle légèrement huilée, 1 min par face : souple, quelques taches dorées.",
   "**Servir.** Feuilles déchirées dans un grand plat, arrosées de sauce, poulet et légumes dessus ; citron à table."],
  keep="Sauce : 3 jours au frigo ; feuilles : le jour même.", age=3, cats=["fetes"], fetes=["Repas de famille", "Ramadan / Aïd"], profil=["epice"], tech=["Mijoter"],
  credit=C(("@mohamedcheikh_", "https://www.tiktok.com/@mohamedcheikh_/video/7695383185902882081")))
K("tartine_sardines_oeufs_mollets", "Tartine de sardines aux œufs mollets, câpres et herbes", "Sardine egg sandwich", "Amérique du Nord › États-Unis", "P", 1, 2, 15, 7, "€", "Poêle, petite casserole.",
  "Un déjeuner rapide avec une boîte de sardines : écrasées avec des œufs mollets, un peu de mayonnaise et de moutarde, relevées de câpres, d'oignon rouge, d'herbes et de citron, sur un pain au levain doré à l'huile d'olive.",
  ["1|boîte de sardines à l'huile d'olive|Sardine (fraîche / conserve)|3", f"2|œufs|{OEUF}|3", "1 c. à s.|de mayonnaise|SUB:mayonnaise|1", f"1 c. à c.|de moutarde|{DIJON}|1", "1 c. à s.|de câpres|Câpres|1", "1/4|oignon rouge|Oignon rouge|1", f"1 c. à s.|de persil et de ciboulette|{PERSIL}|1", f"1/2|citron (zeste et jus)|{CIT}|2", "2|grandes tranches de pain au levain|Pain de campagne / complet|3", f"2 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Œufs.** 7 min dans l'eau bouillante, eau glacée : jaune encore crémeux au centre ; écalés.",
   "**Écraser.** Sardines égouttées et œufs à la fourchette avec mayonnaise et moutarde : grossier, pas en purée.",
   "**Relever.** Câpres hachées, oignon rouge en lamelles fines, herbes, zeste et jus de citron, poivre.",
   "**Toaster.** Pain dans l'huile d'olive, 2 min par face à feu moyen : doré et croustillant ; garniture dessus, un filet d'huile pimentée si tu veux."],
  keep="Garniture : 1 jour au frigo.", age=3, cats=["express"], profil=["poisson", "acide"],
  credit=C(("@totamsachikaroberts", "https://www.tiktok.com/@totamsachikaroberts/video/7700108797313846558")))
K("poulet_croustillant_airfryer", "Hauts de cuisse croustillants à la friteuse sans huile, sauce mayo aigre-douce", "Poulet frit sans friture", "France › Food fusion", "P", 1, 4, 20, 20, "€", "Friteuse à air (ou four à chaleur tournante), 2 bols.",
  "Le poulet frit sans bain d'huile : des hauts de cuisse marinés au soja et aux cinq-épices, panés deux fois dans un mélange farine-fécule, cuits à la friteuse à air jusqu'à ce que la panure croustille. Une sauce mayonnaise aigre-douce à côté.",
  [f"5|hauts de cuisse de poulet|{CUISSE}|3", f"1 c. à s.|de sauce soja claire|{SOJA}|1", "1 c. à c.|de cinq-épices (+ cumin, paprika, ail en poudre)|Cinq-épices chinois|1", f"1/2 c. à c.|de gingembre en poudre|Gingembre (poudre)|1", f"40 g|de farine|{F55}|1", "40 g|de fécule de pomme de terre|Fécule de pomme de terre|2", f"2|œufs|{OEUF}|1", "2 c. à s.|de mayonnaise|SUB:mayonnaise|1", "1 c. à s.|de sauce aigre-douce (ou ketchup + vinaigre de riz)|Vinaigre de riz|1", f"1 c. à s.|d'huile en spray|{HN}|1"],
  ["**Mariner.** Poulet, soja, épices, gingembre : 30 min (ou une nuit).",
   "**Paner deux fois.** Farine et fécule mélangées ; œuf battu, panure, œuf, panure : couche épaisse et irrégulière (c'est elle qui croustille).",
   "**Cuire.** Côté peau en dessous, vaporisé d'huile, 10 min à 190 °C ; retourné, vaporisé, 10 min : doré, croustillant, 74 °C à cœur près de l'os. (Four : 35 min à 220 °C sur une grille.)",
   "**Sauce.** Mayonnaise, aigre-douce, 1 c. à s. d'eau, poivre : à côté, avec une salade de chou au vinaigre de riz."],
  keep="Le jour même.", age=3, cats=["enfants"], profil=["gras"],
  credit=C(("@sandencuisine", "https://www.tiktok.com/@sandencuisine/video/7702403203312127264")))

# ———————————————————————————————— pain
K("cheese_naan", "Cheese naan (naan fourré au fromage fondant, à la poêle)", "Cheese naan", "Asie du Sud › Inde", "Pa", 1, 6, 30, 70, "€", "Poêle en fonte avec couvercle, saladier.",
  "Le naan fourré qui a fait le tour des restaurants indiens de France : une pâte souple au yaourt refermée sur du fromage fondu, étalée et cuite à la poêle couverte. Il gonfle, le fromage file. Version gourmande de la même vidéaste : bœuf effiloché et raclette.",
  [f"400 g|de farine|{F55}|3", f"150 g|de yaourt nature|{YAO}|2", f"10 cl|de lait tiède|{LAIT}|1", f"5 g|de levure boulangère sèche (+ 1 c. à c. de sucre)|{LEV}|1", "6|portions de fromage fondu (ou 200 g de fromage à tartiner)|Fromage à tartiner / fondu|3", "100 g|de mozzarella râpée|Mozzarella / burrata|2", f"40 g|de beurre fondu (+ 1 gousse d'ail)|{BEURRE}|1", f"1 c. à s.|de coriandre ou de persil|{CORI}|1"],
  ["**Pâte.** Farine, sel, levure, sucre ; yaourt, lait, 1 c. à s. de beurre ; pétrie 5 min : souple, un peu collante ; 1 h à couvert : doublée.",
   "**Fourrer.** 6 boules ; chacune étalée en disque, fromage fondu et mozzarella au centre, bords ramenés et pincés ; soudure dessous, aplatie au rouleau à 5 mm sans percer.",
   "**Cuire.** Poêle très chaude, sans matière grasse, 2 min : grosses bulles ; retourné, couvert, 2 min : taches brunes, fromage fondu.",
   "**Finir.** Beurre fondu à l'ail et herbes au pinceau, servi aussitôt."],
  tips=["Version bœuf-raclette : 200 g de bœuf mijoté effiloché et une tranche de raclette dans chaque naan, avec le fromage fondu."],
  keep="Le jour même ; se réchauffe 1 min à la poêle couverte.", age=1, cats=["enfants", "vegetarien"], profil=["gras"],
  credit=C(("@ammey.food", "https://www.tiktok.com/@ammey.food/video/7702502995681873185"), ("@ammey.food", "https://www.tiktok.com/@ammey.food/video/7701757086782311713")))

# ———————————————————————————————— sauces et bases
K("mayonnaise_oeufs_durs", "Mayonnaise aux œufs durs, au mixeur (sans œuf cru)", "Mayonnaise aux œufs durs", "France › Cuisine du quotidien", "S", 1, 8, 10, 10, "€", "Casserole, mixeur ou blender.",
  "Une mayonnaise qui ne tranche jamais et sans œuf cru (pour les femmes enceintes, les petits, les pique-niques au frais) : des œufs durs mixés avec un peu d'eau, d'huile d'olive et de vinaigre. Plus légère, très crémeuse.",
  [f"4|œufs|{OEUF}|3", f"6 cl|d'huile d'olive (ou moitié tournesol)|{HO}|2", "1 c. à s.|de vinaigre de cidre|Vinaigre de cidre|2", f"1 c. à c.|de moutarde (facultatif)|{DIJON}|1", f"1/2 c. à c.|de sel|{SEL}|1", f"1 pincée|de poivre|{POIVRE}|1"],
  ["**Cuire.** Œufs 10 min dans l'eau bouillante ; eau glacée 5 min : jaune pris, sans cerne verte ; écalés.",
   "**Mixer.** Œufs coupés, 3 c. à s. d'eau, huile, vinaigre, moutarde, sel, poivre ; 40 à 60 s : lisse et crémeux.",
   "**Ajuster.** Trop épaisse : une cuillerée d'eau à la fois en mixant ; goûter, sel et vinaigre.",
   "**Reposer.** 15 min au frais : elle se raffermit."],
  keep="3 jours au frigo, bocal fermé.", age=1, cats=["enfants", "vegetarien"], profil=["acide"],
  credit=C(("@wellbraintips", "https://www.tiktok.com/@wellbraintips/video/7692062991558249759")))
K("sauce_verte_entrecote", "Sauce verte au beurre et aux herbes pour l'entrecôte (persil, estragon, anchois)", "Sauce verte de bistrot", "France › Cuisine du quotidien", "S", 2, 4, 15, 10, "€€", "Petite casserole, mixeur plongeant.",
  "La sauce des brasseries à entrecôte-frites, version chef : une réduction échalote-crème-moutarde avec anchois et câpres, mixée avec persil et estragon, puis montée au beurre froid pour la rendre brillante. Sur une viande saisie et des frites.",
  [f"150 g|de beurre doux froid en dés|{BEURRE}|3", f"1|échalote|{ECH}|1", f"10 cl|de crème liquide entière|{CL}|2", f"1 c. à s.|de moutarde de Dijon|{DIJON}|1", "3|filets d'anchois|Anchois (filets, conserve)|2", "1 c. à c.|de câpres|Câpres|1", f"1|petite gousse d'ail|{AIL}|1", f"1|grosse poignée de persil plat|{PERSIL}|2", "1|petite poignée d'estragon|Estragon|2", f"1 c. à c.|de jus de citron|{CIT}|1"],
  ["**Suer.** Échalote ciselée, une noix de beurre, 3 min à feu doux : translucide, sans couleur.",
   "**Réduire.** Crème, moutarde, anchois, câpres, ail, 4 min à frémissement : un peu épaissie, les anchois ont fondu.",
   "**Mixer.** Persil et estragon (feuilles), 30 s au mixeur plongeant : vert vif et lisse.",
   "**Monter.** Feu très doux, beurre froid ajouté morceau par morceau en fouettant : sauce brillante et nappante, jamais bouillante (elle tranche) ; citron, poivre (peu de sel : les anchois salent)."],
  keep="Le jour même ; se réchauffe au bain-marie en fouettant.", age=6, cats=[], profil=["gras", "acide"],
  credit=C(("@mohamedcheikh_", "https://www.tiktok.com/@mohamedcheikh_/video/7692391381850934561")))
K("piment_camerounais", "Piment camerounais (piments, djansang, « 4 côtés », à l'huile)", "Piment du Cameroun", "Afrique subsaharienne › Cameroun", "S", 1, 20, 20, 25, "€", "Mixeur, casserole, bocaux.",
  "La pâte de piment qui accompagne tout au Cameroun : piments rouges et jaunes mixés avec oignon, ail, poivron, épices locales (djansang, « 4 côtés ») et confits doucement dans l'huile. Très fort : une pointe de couteau suffit.",
  ["250 g|de piments (rouges et jaunes)|Piment antillais / scotch bonnet|3", f"2|poivrons rouges (la chair)|{POIVRON}|2", f"2|oignons|{OIG}|2", f"6|gousses d'ail|{AIL}|1", "2 c. à s.|de djansang moulu (épicerie africaine, facultatif)|-|1?", "1 c. à c.|de « 4 côtés » ou de poivre blanc|Poivre noir / blanc / vert|1", "1|cube de bouillon|Bouillon cube volaille|1", f"25 cl|d'huile de tournesol|{HN}|2", f"1|citron (jus)|{CIT}|2"],
  ["**Protéger.** Gants pour couper les piments, cuisine aérée ; on ne se touche pas les yeux.",
   "**Mixer.** Piments équeutés (garder quelques graines selon la force voulue), poivrons, oignons, ail, épices, cube écrasé, sel, un trait d'huile : purée grossière.",
   "**Confire.** Dans l'huile chaude, 20 à 25 min à feu doux en remuant : l'eau s'évapore, la pâte fonce et l'huile remonte, rouge, en surface ; jus de citron à la fin.",
   "**Conserver.** En bocaux ébouillantés, couvert d'huile ; une pointe de couteau par assiette."],
  keep="1 mois au frigo, toujours couvert d'huile, cuillère propre.", age=None, kids="Trop fort pour les enfants.", cats=[], profil=["epice", "acide"],
  credit=C(("@tiaghohilson", "https://www.tiktok.com/@tiaghohilson/video/7702078164255788320")))
K("rillettes_poulet_legeres", "Rillettes de poulet sans graisse ajoutée (au fromage frais et aux herbes)", "Rillettes de poulet légères", "France › Cuisine du quotidien", "E", 1, 6, 15, 25, "€", "Casserole, fourchette ou robot.",
  "Des rillettes à tartiner sans saindoux ni beurre : du blanc de poulet poché dans un bouillon parfumé, effiloché et lié au fromage frais, à la moutarde et aux herbes. Pour l'apéritif, les sandwichs, les tartines du soir.",
  [f"3|blancs de poulet|{BLANC_P}|3", f"150 g|de fromage frais (type carré frais ou faisselle)|Fromage blanc / faisselle|2", f"1 c. à c.|de moutarde à l'ancienne|{DIJON}|1", f"1|échalote|{ECH}|1", "1/2|botte de ciboulette|Ciboulette|1", f"1|citron (zeste et 1 c. à s. de jus)|{CIT}|2", "1|cube de bouillon et 1 feuille de laurier|Bouillon cube volaille|1", f"1 pincée|de piment d'Espelette|Piment d'Espelette|1"],
  ["**Pocher.** Bouillon (1 l d'eau, cube, laurier, poivre) à frémissement ; poulet, 15 min sans bouillir : blanc à cœur, 74 °C ; refroidi 10 min dans le bouillon (il reste juteux).",
   "**Effilocher.** À deux fourchettes, très fin ; 4 c. à s. de bouillon pour l'humidité.",
   "**Lier.** Fromage frais, moutarde, échalote ciselée très fin, ciboulette, zeste et jus de citron, Espelette, sel : texture de rillettes.",
   "**Reposer.** En pots, 2 h au frais : elles se raffermissent ; avec du pain grillé et des cornichons."],
  keep="3 jours au frigo.", age=1, cats=["enfants", "pique_nique"], profil=["leger", "acide"],
  credit=C(("@lacuisinedes.m.and.ms", "https://www.tiktok.com/@lacuisinedes.m.and.ms/video/7703869624021994784")))

# ———————————————————————————————— dessert et boisson
K("tiramisu_creme_brulee", "Tiramisu crème brûlée (fond biscuité, croûte de sucre caramélisé)", "Crème brûlée tiramisu", "France › Food fusion", "D", 2, 3, 30, 300, "€€", "3 cercles individuels de 8 cm, batteur, chalumeau (ou gril du four).",
  "Le dessert le plus enregistré de la semaine, par la vidéaste déjà la plus enregistrée des favoris : un fond de biscuits au beurre comme un cheesecake, des boudoirs au café entre deux couches de crème mascarpone, et une fine croûte de sucre caramélisée au chalumeau qui craque sous la cuillère.",
  ["150 g|de biscuits (petits-beurre ou spéculoos)|Biscuits (spéculoos, sablés)|2", f"50 g|de beurre fondu|{BEURRE}|1", "500 g|de mascarpone|Mascarpone|3", f"2|jaunes d'œufs très frais|{OEUF}|1", f"70 g|de sucre (40 g + 30 g pour la croûte)|{SUCRE}|2", f"20 cl|de crème liquide entière froide|{CL}|2", "9|boudoirs|Boudoirs / biscuits cuillère|2", "1|tasse de café fort refroidi|-|2", "1 c. à s.|de cacao (facultatif)|Cacao en poudre non sucré|1?"],
  ["**Fond.** Biscuits mixés, beurre fondu : sable humide ; tassé au fond des cercles ; 20 min au frais.",
   "**Crème.** Jaunes et 40 g de sucre fouettés 3 min : blanchis ; mascarpone, lissé ; crème montée en chantilly ferme, incorporée à la maryse : légère et tenue.",
   "**Monter.** Une couche de crème sur le fond ; boudoirs trempés 1 s dans le café ; reste de crème, lissée.",
   "**Reposer.** 4 à 6 h au frais : il se tient au démoulage.",
   "**Brûler.** Juste avant de servir : fine couche de sucre, chalumeau en mouvement 30 à 40 s : croûte ambrée et lisse ; 2 min pour qu'elle durcisse."],
  tips=["Jaunes crus : pour les femmes enceintes et les petits, les retirer (la chantilly suffit à tenir la crème)."],
  keep="2 jours au frigo, sans la croûte (elle fond).", age=6, cats=["fetes"], fetes=["Repas de famille", "Anniversaire"], profil=["sucre"],
  credit=C(("@on_est_gourmands", "https://www.tiktok.com/@on_est_gourmands/video/7698405334116732193")))
K("chocolat_chaud_italien", "Chocolat chaud à l'italienne (épais, à la petite cuillère)", "Cioccolata calda", "Europe du Sud › Italie", "B", 1, 3, 5, 8, "€", "Petite casserole, fouet.",
  "La cioccolata calda des cafés italiens : si épaisse qu'elle nappe la cuillère, presque un dessert. Du cacao, du chocolat noir fondu et une pointe de maïzena pour la texture. Avec de la chantilly pour les gourmands.",
  [f"50 cl|de lait entier|{LAIT}|3", f"60 g|de chocolat noir (50 à 60 %)|{CHOCO}|3", "4 c. à s.|de cacao non sucré|Cacao en poudre non sucré|2", f"2 c. à s.|de sucre|{SUCRE}|1", "5 à 10 g|de maïzena|Fécule de maïs (maïzena)|1", f"1 pincée|de cannelle (facultatif)|{CANN}|1?"],
  ["**Délayer.** Cacao, sucre, maïzena dans 10 cl de lait froid, au fouet : sans grumeau.",
   "**Chauffer.** Reste du lait à frémissement ; mélange versé en fouettant.",
   "**Épaissir.** Feu doux, 3 à 4 min en fouettant sans arrêt : ça nappe la cuillère ; hors du feu, chocolat haché, 1 min : fondu, brillant.",
   "**Servir.** Bien chaud, en petites tasses ; plus de maïzena pour une texture de crème."],
  keep="Le jour même ; se réchauffe en fouettant.", age=1, cats=["enfants"], profil=["sucre", "chocolat"],
  credit=C(("@gourmmy", "https://www.tiktok.com/@gourmmy/video/7704001125397122336")))
