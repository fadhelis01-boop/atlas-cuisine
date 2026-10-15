# -*- coding: utf-8 -*-
"""Vague 2 · Amérique du Nord, Amérique latine & Caraïbes, Océanie."""
from recipes_v2_base import *

AN = "Amérique du Nord"; AL = "Amérique latine & Caraïbes"; OC = "Océanie"

K("burger_maison", "Cheeseburger maison", "Cheeseburger", f"{AN} › États-Unis", "P", 1, 4, 25, 10, "€€", "Poêle en fonte ou plancha.",
  "Steak haché bien saisi (smash), cheddar fondu, pain brioché toasté, pickles et sauce burger : mieux qu'au fast-food.",
  [f"600 g|de bœuf haché à 15-20 % de gras|{HACHE}|3", "4|pains burger briochés|Brioche|2", "4 tranches|de cheddar|Cheddar|2", "1|oignon rouge|Oignon rouge|1", f"2|tomates|{TOM}|1", "4|feuilles de salade|Salade (laitue, batavia)|1", "4|cornichons|Cornichon|1", "4 c. à s.|de sauce burger maison|SUB:sauce_burger|2"],
  ["**Boules.** 4 boules de 150 g, pas trop tassées, salées au dernier moment.", "**Smash.** Poêle fumante, boule écrasée fort à la spatule, 2 min ; retourne, cheddar, 1 min, couvercle.", "**Pains.** Toastés face coupée.", "**Monter.** Sauce, salade, steak, tomate, oignon, cornichons."],
  tips=["⚠️ Steak haché : cuisson à cœur 70 °C pour les enfants."], age=3, cats=["enfants"], profil=["viande_rouge", "gras"], fetes=["Barbecue d'été", "Anniversaire"], tech=["Cuisson de la viande"])

K("mac_cheese", "Mac and cheese au four", "Macaroni and cheese", f"{AN} › États-Unis", "P", 1, 6, 20, 25, "€", "Casserole, plat à gratin.",
  "Macaronis nappés d'une sauce cheddar crémeuse, gratinés à la chapelure : le réconfort américain.",
  [f"400 g|de macaronis|{PATES}|3", "250 g|de cheddar râpé|Cheddar|3", f"50 cl|de lait|{LAIT}|2", f"40 g|de beurre + 40 g de farine|{BEURRE}|2", f"1 c. à c.|de moutarde|{DIJON}|1", "40 g|de chapelure|Chapelure|1", f"1 pincée|de paprika|{PAPRIKA}|0"],
  ["**Pâtes.** 2 min de moins que le paquet.", "**Sauce.** Roux, lait, 5 min ; hors du feu, 200 g de cheddar, moutarde.", "**Gratiner.** Pâtes + sauce, reste de cheddar, chapelure, 20 min à 200 °C."],
  age=1, cats=["enfants"], profil=["gras"])

K("pulled_chicken", "Effiloché de poulet barbecue", "Pulled chicken", f"{AN} › États-Unis › Caroline du Nord", "P", 1, 6, 15, 180, "€€", "Cocotte, four.",
  "Hauts de cuisse cuits longuement aux épices fumées puis effilochés dans la sauce barbecue : en burger avec coleslaw.",
  [f"1,2 kg|de hauts de cuisse désossés|{CUISSE}|3", "25 cl|de sauce barbecue maison|SUB:sauce_barbecue|3", f"1 c. à s.|de paprika fumé|{PFUME}|2", "1 c. à s.|de cassonade|Sucre blanc / roux / cassonade / vergeoise|1", "1 c. à c.|de poudre d'ail et d'oignon|Poudre d'ail / d'oignon|1", f"1|oignon|{OIG}|1", "6|pains burger|Brioche|2"],
  ["**Frotter.** Poulet avec épices, sucre, sel.", "**Cuire.** Sur l'oignon, couvert, 2 h 30 à 150 °C.", "**Effilocher.** À deux fourchettes, avec le jus et la sauce barbecue. En pains avec coleslaw."],
  age=1, cats=["enfants"], profil=["sucre"], fetes=["Barbecue d'été"])

K("coleslaw", "Coleslaw", "Coleslaw", f"{AN} › États-Unis", "A", 1, 6, 15, 30, "€", "Râpe, saladier.",
  "Chou et carotte râpés dans une sauce crémeuse acidulée : croquant, pour burgers et barbecue.",
  ["½|chou blanc|Chou blanc / rouge|3", f"2|carottes|{CAROTTE}|2", f"4 c. à s.|de mayonnaise|SUB:mayonnaise|2", f"2 c. à s.|de yaourt|{YAO}|1", "1 c. à s.|de vinaigre de cidre|Vinaigre de cidre|1", f"1 c. à c.|de sucre|{SUCRE}|0", f"1 c. à c.|de moutarde|{DIJON}|0"],
  ["**Râper.** Chou très fin, carottes.", "**Mélanger.** Sauce, 30 min au frais."], age=3, cats=["enfants"], fetes=["Barbecue d'été"], profil=["acide"])

K("pancakes_myrtilles", "Pancakes aux myrtilles", "Blueberry pancakes", f"{AN} › États-Unis", "G", 1, 4, 15, 15, "€", "Poêle.",
  "Épais et moelleux grâce au babeurre, avec des myrtilles qui éclatent et du sirop d'érable.",
  [f"200 g|de farine|{F55}|3", "25 cl|de babeurre (ou lait + citron)|Babeurre|2", f"1|œuf|{OEUF}|1", f"30 g|de beurre fondu|{BEURRE}|1", f"1 c. à s.|de sucre|{SUCRE}|1", f"1 c. à c.|de levure + ½ de bicarbonate|{LEVC}|1", "150 g|de myrtilles|Framboise / mûre / myrtille|2", "4 c. à s.|de sirop d'érable (service)|Sirop d'agave / d'érable|1"],
  ["**Pâte.** Secs et humides séparément, mélangés juste (grumeaux OK).", "**Cuire.** Petites louches, myrtilles dessus, bulles puis retourne."],
  age=1, cats=["enfants"], profil=["sucre"])

K("cheesecake_ny", "Cheesecake new-yorkais", "New York cheesecake", f"{AN} › États-Unis › New York", "D", 2, 10, 25, 600, "€€", "Moule à charnière 22 cm, bain-marie.",
  "Dense et crémeux sur un fond de biscuits au beurre, cuit doucement pour ne pas fendre.",
  ["200 g|de biscuits (spéculoos ou sablés)|Biscuits (spéculoos, sablés)|2", f"80 g|de beurre fondu|{BEURRE}|1", "750 g|de fromage frais type Philadelphia ou St Môret|Fromage à tartiner / fondu|3", f"180 g|de sucre|{SUCRE}|2", f"3|œufs|{OEUF}|2", f"20 cl|de crème aigre (ou crème fraîche)|{CF}|2", f"1|citron (zeste)|{CIT}|1", f"1 c. à s.|de maïzena|Fécule de maïs (maïzena)|1"],
  ["**Fond.** Biscuits mixés + beurre, tassés, 10 min à 180 °C.", "**Appareil.** Fromage + sucre + maïzena lisse, œufs un à un sans fouetter fort, crème, zeste.", "**Cuire.** Au bain-marie, 1 h à 150 °C ; éteins, 1 h four entrouvert.", "**Repos.** Une nuit au frigo. Coulis de fruits rouges."],
  age=1, fetes=["Anniversaire"], profil=["sucre", "gras"])

K("poutine", "Poutine", "Poutine", f"{AN} › Canada › Québec", "P", 2, 4, 30, 30, "€€", "Friteuse, casserole.",
  "Frites croustillantes, fromage en grains qui « couine » et sauce brune chaude : le plat-réconfort du Québec.",
  ["1|recette de frites maison|SUB:frites_maison|3", "300 g|de fromage en grains (ou mozzarella en cubes)|Mozzarella / burrata|3", f"50 cl|de bouillon de bœuf|{BOUILLON}|2", f"30 g|de beurre + 30 g de farine|{BEURRE}|1", "1 c. à s.|de sauce Worcestershire|Sauce Worcestershire|1", f"1 c. à c.|de concentré|{CONC}|1"],
  ["**Sauce.** Roux brun, bouillon, Worcestershire, concentré, 10 min : nappante.", "**Monter.** Frites brûlantes, fromage, sauce bouillante dessus (le fromage ramollit sans fondre)."],
  age=3, cats=["enfants"], profil=["gras"])

K("pouding_chomeur", "Pouding chômeur", "Pouding chômeur", f"{AN} › Canada › Québec", "D", 1, 8, 15, 35, "€", "Plat à four.",
  "Un gâteau simple qui cuit dans un sirop d'érable et de cassonade : le dessous devient un caramel fondant.",
  [f"200 g|de farine|{F55}|2", f"80 g|de beurre|{BEURRE}|2", f"100 g|de sucre|{SUCRE}|1", f"1|œuf|{OEUF}|1", f"15 cl|de lait|{LAIT}|1", f"2 c. à c.|de levure|{LEVC}|0", "25 cl|de sirop d'érable|Sirop d'agave / d'érable|3", "100 g|de cassonade|Sucre blanc / roux / cassonade / vergeoise|2", f"20 cl|de crème|{CL}|1"],
  ["**Sirop.** Érable + cassonade + crème + 10 cl d'eau, bouillants, versés dans le plat.", "**Pâte.** Beurre + sucre, œuf, farine + levure, lait ; à la cuillère sur le sirop.", "**Cuire.** 35 min à 180 °C."],
  age=1, cats=["enfants"], profil=["sucre"])

K("tacos_al_pastor", "Tacos de poulet à l'ananas (façon al pastor)", "Tacos al pastor", f"{AL} › Mexique › Mexico", "P", 1, 4, 25, 20, "€€", "Poêle, plancha.",
  "Poulet mariné au piment doux, achiote et ananas, saisi, dans des tortillas de maïs, oignon, coriandre, ananas grillé.",
  [f"800 g|de hauts de cuisse|{CUISSE}|3", "12|tortillas de maïs|Tortillas de maïs|3", "½|ananas|Ananas|2", "2|piments guajillo ou 2 c. à s. de piment doux|Piments ancho / chipotle / guajillo / pasilla|2", "1 c. à s.|d'achiote (ou paprika)|Achiote / rocou|1", f"1 c. à c.|de cumin + origan|{CUMIN}|1", "3 c. à s.|de vinaigre|Vinaigre de cidre|1", f"1|oignon blanc|{OIG}|1", f"1 bouquet|de coriandre|{CORI}|1", f"2|citrons verts|{CITV}|1"],
  ["**Marinade.** Piments réhydratés, achiote, épices, vinaigre, ail, 100 g d'ananas : mixés. Poulet 4 h.", "**Cuire.** Saisi en entier, émincé, recroustillé.", "**Tacos.** Tortillas chaudes, poulet, ananas grillé, oignon, coriandre, citron vert, salsa."],
  age=3, profil=["epice", "sucre"])

K("guacamole_tostadas", "Tostadas haricots noirs, avocat et feta", "Tostadas", f"{AL} › Mexique", "P", 1, 4, 20, 10, "€", "Four ou poêle.",
  "Tortillas croustillantes, purée de haricots noirs, avocat, salsa, fromage frais : rapide et végétarien.",
  ["8|tortillas de maïs|Tortillas de maïs|3", "400 g|de haricots noirs cuits|Haricots noirs|3", "2|avocats|Avocat|2", "1|recette de pico de gallo|SUB:pico_de_gallo|2", "100 g|de feta ou queso fresco|Feta|1", f"1 c. à c.|de cumin|{CUMIN}|1", f"1|citron vert|{CITV}|1"],
  ["**Tostadas.** Tortillas huilées, 8 min à 200 °C : croustillantes.", "**Haricots.** Écrasés chauds avec cumin, sel.", "**Monter.** Haricots, avocat, pico, fromage, citron vert."],
  age=3, cats=["enfants"], profil=["leger"])

K("enchiladas_poulet", "Enchiladas au poulet, sauce rouge", "Enchiladas rojas", f"{AL} › Mexique", "P", 2, 6, 35, 25, "€€", "Plat à four, mixeur.",
  "Tortillas roulées autour de poulet effiloché, nappées d'une sauce aux piments doux et gratinées.",
  ["12|tortillas de maïs ou blé|Tortillas de maïs|3", f"600 g|de poulet cuit effiloché|{BLANC_P}|3", "3|piments ancho réhydratés|Piments ancho / chipotle / guajillo / pasilla|2", f"400 g|de tomates pelées|{PELEES}|2", f"1|oignon|{OIG}|1", f"2 gousses|d'ail|{AIL}|1", f"1 c. à c.|de cumin|{CUMIN}|1", "200 g|de fromage râpé|Cheddar|2", f"10 cl|de crème|{CF}|1"],
  ["**Sauce.** Piments, tomates, oignon, ail, cumin mixés, cuits 10 min.", "**Rouler.** Tortillas trempées dans la sauce, poulet, roulées serrées.", "**Gratiner.** Sauce, fromage, 20 min à 200 °C. Crème, coriandre."],
  age=3, profil=["epice"])

K("chili_sin_carne", "Chili sin carne", "Chili sin carne", f"{AN} › États-Unis › Texas", "P", 1, 6, 20, 40, "€", "Cocotte.",
  "Haricots rouges et noirs, lentilles corail, poivrons et épices fumées : la texture et le goût du chili, sans viande.",
  ["400 g|de haricots rouges cuits|Haricots rouges / noirs|3", "400 g|de haricots noirs cuits|Haricots noirs|2", "100 g|de lentilles corail|Lentilles corail|2", f"2|poivrons|{POIVRON}|2", f"800 g|de tomates pelées|{PELEES}|2", f"1|oignon|{OIG}|1", "150 g|de maïs|Maïs doux|1", f"2 c. à c.|de cumin + 1 de paprika fumé|{CUMIN}|2", "1|piment chipotle (ou 1 pincée de piment)|Piments ancho / chipotle / guajillo / pasilla|1", "1 carré|de chocolat noir|Chocolat noir|0"],
  ["**Base.** Oignon, poivrons, épices.", "**Mijoter.** Tomates, lentilles, 25 cl d'eau, 20 min ; haricots, maïs, chocolat, 15 min."],
  age=1, cats=["enfants"], profil=["epice"])

K("feijoada_light", "Feijoada (version bœuf et volaille fumée)", "Feijoada", f"{AL} › Brésil", "P", 2, 8, 40, 180, "€€", "Grande cocotte.",
  "Haricots noirs mijotés avec des viandes, servis avec riz, chou sauté, orange et farofa. Version sans porc : bœuf séché, saucisses de volaille fumées.",
  ["600 g|de haricots noirs trempés|Haricots noirs|3", "500 g|de joue ou paleron de bœuf|Paleron|3", "4|saucisses de volaille fumées|Saucisse de bœuf / de veau / de volaille|2", "150 g|de bœuf séché ou bresaola|Viande des Grisons / bresaola|1", f"2|oignons|{OIG}|1", f"6 gousses|d'ail|{AIL}|1", "3|feuilles de laurier|Laurier|1", "2|oranges|Orange|1", "100 g|de farofa|Farofa / farine de manioc torréfiée|1", "1|chou kale|Chou vert / frisé / kale|1"],
  ["**Cuire.** Haricots, bœuf, laurier, 2 h.", "**Ajouter.** Oignons et ail revenus, saucisses en tronçons, bœuf séché, 45 min ; écrase une louche de haricots pour épaissir.", "**Accompagnements.** Riz blanc, kale sauté à l'ail, oranges en tranches, farofa."],
  age=1, fetes=["Repas de famille"], profil=["viande_rouge"])

K("pao_de_queijo", "Pão de queijo (petits pains au fromage)", "Pão de queijo", f"{AL} › Brésil › Minas Gerais", "Pa", 1, 25, 15, 25, "€", "Casserole, plaque.",
  "Boules de tapioca et fromage, creuses et élastiques : naturellement sans gluten.",
  ["250 g|de fécule de tapioca (ou de manioc)|Farine de manioc|3", f"12 cl|de lait|{LAIT}|2", f"6 cl|d'huile|{HN}|1", f"2|œufs|{OEUF}|2", f"120 g|de parmesan + gruyère râpés|{PARM}|3", f"1 c. à c.|de sel|{SEL}|0"],
  ["**Ébouillanter.** Lait, huile, sel bouillants sur le tapioca ; mélange.", "**Pâte.** Tiède : œufs, fromage, pâte collante.", "**Cuire.** Boules de 3 cm, 25 min à 190 °C."],
  age=1, cats=["enfants", "pains"], profil=["gras"], kids="✓ dès 1 an ; sans gluten.")

K("brigadeiros", "Brigadeiros", "Brigadeiro", f"{AL} › Brésil", "G", 1, 25, 20, 120, "€", "Casserole.",
  "Bouchées de lait concentré et cacao cuites jusqu'à fondant, roulées dans les vermicelles : les bonbons des anniversaires brésiliens.",
  ["1 boîte (397 g)|de lait concentré sucré|Lait concentré sucré / non sucré|3", "2 c. à s.|de cacao|Cacao en poudre non sucré|2", f"20 g|de beurre|{BEURRE}|1", "60 g|de vermicelles en chocolat|Pépites de chocolat|1"],
  ["**Cuire.** Tout à feu doux en remuant 10-12 min, jusqu'à ce que la masse se décolle du fond.", "**Rouler.** Froide, mains beurrées, boules, vermicelles."],
  age=3, cats=["enfants"], fetes=["Anniversaire"], profil=["sucre"])

K("ceviche", "Ceviche péruvien", "Cebiche", f"{AL} › Pérou › Lima", "E", 1, 4, 20, 5, "€€€", "Saladier froid.",
  "Poisson extra-frais « cuit » quelques minutes au citron vert avec piment, oignon rouge et coriandre, servi avec patate douce.",
  ["500 g|de bar ou dorade extra-frais|Bar / loup|3", f"8|citrons verts|{CITV}|3", "1|oignon rouge|Oignon rouge|2", "1|piment (aji amarillo ou autre)|Aji amarillo|2", f"1 bouquet|de coriandre|{CORI}|2", "1|patate douce cuite|Patate douce|1", "1|épi de maïs cuit|Maïs doux|1", f"1 c. à c.|de sel|{SEL}|0"],
  ["**Couper.** Poisson en cubes de 2 cm, salé.", "**Leche de tigre.** Jus de citron vert pressé à la main (sans amertume), piment, coriandre.", "**Mariner.** 3-5 min seulement, oignon rouge émincé. Patate douce et maïs à côté."],
  tips=["⚠️ Poisson cru : extra-frais ou congelé 7 jours à −20 °C ; déconseillé femmes enceintes et jeunes enfants."], keep="À manger tout de suite.", age=None, profil=["poisson", "acide"], fetes=["Barbecue d'été"])

K("lomo_saltado", "Lomo saltado", "Lomo saltado", f"{AL} › Pérou", "P", 1, 4, 20, 15, "€€", "Wok.",
  "Le plat chifa (sino-péruvien) : bœuf sauté au soja et vinaigre, tomates, oignon rouge, frites et riz.",
  ["600 g|de rumsteck en lanières|Rumsteck|3", "1|oignon rouge en quartiers|Oignon rouge|2", f"3|tomates en quartiers|{TOM}|2", f"3 c. à s.|de sauce soja|{SOJA}|2", "2 c. à s.|de vinaigre de vin|Vinaigre de vin rouge / blanc|1", "1|piment aji (ou piment doux)|Aji amarillo|1", f"1 bouquet|de coriandre|{CORI}|1", "1|recette de frites|SUB:frites_maison|2"],
  ["**Saisir.** Bœuf par petites quantités, wok fumant.", "**Sauter.** Oignon, piment 1 min, tomates 1 min ; bœuf, soja, vinaigre.", "**Servir.** Avec frites (dedans ou à côté) et riz, coriandre."],
  age=3, profil=["viande_rouge", "acide"], tech=["Sauter au wok"])

K("empanadas", "Empanadas au bœuf (au four)", "Empanadas criollas", f"{AL} › Argentine", "P", 2, 16, 50, 25, "€", "Rouleau, plaque.",
  "Chaussons dorés farcis de bœuf aux oignons, paprika, cumin, olives et œuf dur : le repas à la main argentin.",
  [f"500 g|de farine|{F55}|3", f"120 g|de beurre|{BEURRE}|2", f"500 g|de bœuf haché au couteau|{HACHE}|3", f"3|oignons|{OIG}|2", f"1 c. à c.|de paprika + 1 de cumin|{PAPRIKA}|1", f"2|œufs durs|{OEUF}|1", "12|olives vertes|Olives (vertes / noires)|1", f"1|œuf (dorure)|{OEUF}|1"],
  ["**Pâte.** Farine, beurre fondu, sel, 20 cl d'eau tiède : souple, 30 min.", "**Farce.** Oignons fondus, viande, épices, 10 min ; froide, œufs et olives hachés.", "**Façonner.** Disques de 12 cm, farce, ferme en torsade (repulgue).", "**Cuire.** Dorure, 20-25 min à 200 °C."],
  age=1, cats=["enfants"], fetes=["Apéritif dînatoire", "Repas de famille"], profil=["viande_rouge"])

K("alfajores", "Alfajores au dulce de leche", "Alfajores de maicena", f"{AL} › Argentine", "G", 2, 20, 30, 15, "€", "Plaque, emporte-pièce.",
  "Deux sablés fondants à la maïzena, collés au dulce de leche et roulés dans la noix de coco.",
  [f"200 g|de maïzena|Fécule de maïs (maïzena)|3", f"100 g|de farine|{F55}|2", f"150 g|de beurre mou|{BEURRE}|2", f"80 g|de sucre|{SUCRE}|1", "3|jaunes d'œufs|Jaune d'œuf|1", f"1 c. à c.|de levure|{LEVC}|0", "300 g|de dulce de leche|Dulce de leche|3", "40 g|de noix de coco râpée|Noix de coco râpée|1"],
  ["**Pâte.** Beurre + sucre, jaunes, maïzena + farine + levure. 30 min au frais.", "**Cuire.** Disques de 5 cm, 10 min à 170 °C : ils restent blancs.", "**Monter.** Dulce de leche entre deux, bord roulé dans la coco."],
  age=1, cats=["enfants"], profil=["sucre"])

K("arepas", "Arepas garnies", "Arepas", f"{AL} › Venezuela", "Pa", 1, 8, 20, 20, "€", "Poêle, four.",
  "Galettes de maïs précuit, croustillantes dehors, moelleuses dedans, fendues et garnies (poulet-avocat, haricots-fromage).",
  ["300 g|de farine de maïs précuite (masarepa)|Farine de maïs|3", "40 cl|d'eau tiède|-|0", f"1 c. à c.|de sel|{SEL}|0", f"300 g|de poulet effiloché|{BLANC_P}|2", "2|avocats|Avocat|2", f"2 c. à s.|de mayonnaise|SUB:mayonnaise|1", f"1|citron vert|{CITV}|1"],
  ["**Pâte.** Farine, eau, sel : 5 min de repos, pâte souple.", "**Cuire.** Galettes de 1,5 cm, 5 min par face à la poêle, puis 10 min au four à 200 °C.", "**Garnir.** Fendues, reina pepiada : poulet + avocat écrasé + mayonnaise + citron."],
  age=1, cats=["enfants", "pains"], profil=["leger"], kids="✓ dès 1 an ; sans gluten.")

K("pollo_guisado", "Poulet stewed à la caribéenne", "Brown stew chicken", f"{AL} › Jamaïque", "P", 1, 6, 20, 50, "€", "Cocotte.",
  "Poulet caramélisé dans le sucre brun puis mijoté avec thym, poivrons et piment : sauce sombre et parfumée.",
  [f"1,2 kg|de cuisses de poulet|{CUISSE}|3", "2 c. à s.|de cassonade|Sucre blanc / roux / cassonade / vergeoise|2", f"1|oignon|{OIG}|1", f"1|poivron|{POIVRON}|1", f"2|tomates|{TOM}|1", f"3 gousses|d'ail|{AIL}|1", f"4 branches|de thym|{THYM}|2", "1|piment scotch bonnet entier|Piment antillais / scotch bonnet|1", "1 c. à c.|de quatre-épices|Quatre-épices|1", f"2 c. à s.|de sauce soja|{SOJA}|1"],
  ["**Mariner.** Poulet, ail, thym, épices, soja, 1 h.", "**Caraméliser.** Sucre dans l'huile jusqu'à brun foncé ; poulet, dore.", "**Mijoter.** Légumes, piment entier, 25 cl d'eau, 40 min. Riz aux haricots rouges."],
  age=3, profil=["sucre"])

K("riz_haricots_rouges_coco", "Riz aux haricots rouges et coco (rice and peas)", "Rice and peas", f"{AL} › Jamaïque", "A", 1, 6, 10, 30, "€", "Cocotte.",
  "Riz cuit dans le lait de coco avec haricots rouges, thym et piment entier : l'accompagnement des Caraïbes.",
  [f"400 g|de riz|{RIZ}|3", "400 g|de haricots rouges cuits|Haricots rouges / noirs|3", f"40 cl|de lait de coco|{COCO}|2", "3|oignons nouveaux|Oignon nouveau / cébette|1", f"3 branches|de thym|{THYM}|1", "1|piment entier|Piment antillais / scotch bonnet|1", f"2 gousses|d'ail|{AIL}|1"],
  ["**Cuire.** Coco + 40 cl d'eau, haricots, aromates, piment entier, sel, à ébullition ; riz, couvert, 20 min feu doux."],
  age=1, cats=["enfants"], profil=["leger"])

K("pavlova", "Pavlova aux fruits rouges", "Pavlova", f"{OC} › Nouvelle-Zélande", "D", 2, 8, 25, 180, "€€", "Plaque, batteur.",
  "Une meringue croquante dehors et guimauve dedans, couverte de chantilly et de fruits frais.",
  ["4|blancs d'œufs|Blanc d'œuf|3", f"220 g|de sucre|{SUCRE}|3", f"1 c. à c.|de maïzena|Fécule de maïs (maïzena)|1", "1 c. à c.|de vinaigre blanc|Vinaigre blanc|1", f"30 cl|de crème|{CL}|2", "400 g|de fruits rouges, kiwi, fruit de la passion|Framboise / mûre / myrtille|2"],
  ["**Meringue.** Blancs montés, sucre en pluie jusqu'à très ferme et brillant ; maïzena et vinaigre.", "**Cuire.** Disque de 22 cm creusé au centre, 1 h 15 à 120 °C ; refroidit dans le four éteint.", "**Garnir.** Au dernier moment : chantilly, fruits."],
  age=1, cats=["enfants", "zero_dechet"], fetes=["Anniversaire", "Noël"], profil=["sucre"], tech=["Meringue"])

K("anzac_biscuits", "Biscuits Anzac", "Anzac biscuits", f"{OC} › Australie", "G", 1, 20, 10, 15, "€", "Plaque.",
  "Biscuits sans œuf à l'avoine, à la noix de coco et au sirop doré : croustillants et moelleux à la fois.",
  ["100 g|de flocons d'avoine|Avoine (flocons)|3", f"100 g|de farine|{F55}|2", "80 g|de noix de coco râpée|Noix de coco râpée|2", "100 g|de cassonade|Sucre blanc / roux / cassonade / vergeoise|2", f"100 g|de beurre|{BEURRE}|2", "2 c. à s.|de sirop de canne ou de miel|Mélasse / sirop de canne|1", "½ c. à c.|de bicarbonate|Bicarbonate de soude|1"],
  ["**Fondre.** Beurre + sirop ; bicarbonate dans 2 c. à s. d'eau bouillante, ajouté (ça mousse).", "**Mélanger.** Avec les secs.", "**Cuire.** Boules aplaties, 12-15 min à 170 °C."],
  age=1, cats=["enfants"], profil=["sucre"])

K("poisson_cru_fidji", "Kokoda (poisson mariné des Fidji)", "Kokoda", f"{OC} › Fidji", "E", 1, 4, 20, 15, "€€€", "Saladier.",
  "Poisson blanc mariné au citron vert puis baigné de lait de coco, piment, tomate et oignon : servi dans une demi-noix de coco.",
  ["500 g|de poisson blanc extra-frais (mahi-mahi, dorade)|Dorade|3", f"5|citrons verts|{CITV}|3", f"20 cl|de lait de coco|{COCO}|3", f"1|tomate|{TOM}|1", "1|oignon rouge|Oignon rouge|1", f"1|piment|{PIMENT}|1", f"1 bouquet|de coriandre|{CORI}|1"],
  ["**Mariner.** Cubes de poisson, citron vert, sel, 10 min.", "**Égoutter.** Retire le jus.", "**Finir.** Coco, légumes en dés, piment, coriandre."],
  tips=["⚠️ Poisson cru : extra-frais ou congelé ; déconseillé femmes enceintes et jeunes enfants."], keep="À manger tout de suite.", age=None, profil=["poisson", "acide"])
