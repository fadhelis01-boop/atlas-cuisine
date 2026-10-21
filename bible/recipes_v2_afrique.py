# -*- coding: utf-8 -*-
"""Vague 2 · Afrique subsaharienne : Sénégal, Côte d'Ivoire, Mali, Cameroun, Nigeria, Ghana, Éthiopie, Afrique du Sud, Madagascar, Congo."""
from recipes_v2_base import *

M = "Afrique subsaharienne"

K("thieboudienne", "Thiéboudienne (riz au poisson)", "Ceebu jën", f"{M} › Sénégal › Saint-Louis", "P", 2, 6, 50, 75, "€€", "Grand faitout.",
  "Le plat national sénégalais : poisson farci au nokoss, légumes fondants et riz cuit dans la sauce tomate, avec son gratin croustillant au fond (le xooñ).",
  ["1,2 kg|de poisson ferme (thiof, mérou, dorade) en darnes|Dorade|3", "1|recette de nokoss (liée)|SUB:nokoss|2", f"500 g|de riz brisé ou long|{RIZ}|3", f"70 g|de concentré de tomate|{CONC}|2", "1|chou en quartiers|Chou blanc / rouge|1",
   f"2|carottes|{CAROTTE}|1", "1|aubergine|Aubergine|1", "1|morceau de manioc|Manioc / yuca|1", "200 g|de potiron|Potiron / citrouille|1", "6|gombos|Gombo (okra)|1", "1 morceau|de poisson séché (guedj, facultatif)|Poisson fumé / séché|1?", f"15 cl|d'huile|{HN}|2", f"2|oignons|{OIG}|1", "1|piment antillais entier|Piment antillais / scotch bonnet|1"],
  ["**Farcir.** Entaille le poisson et remplis de nokoss ; dore-le dans l'huile, réserve.", "**Sauce.** Oignons, concentré dilué, 10 min ; 2 L d'eau, poisson séché, piment entier ; légumes durs d'abord (manioc, carottes, chou), puis les tendres. Remets le poisson 15 min.",
   "**Riz.** Retire poisson et légumes au chaud ; riz lavé dans le bouillon (il doit juste le couvrir), couvert, feu doux, 25 min : le fond accroche et dore.", "**Servir.** Riz rouge, légumes et poisson dessus, xooñ à part, citron vert."],
  age=3, profil=["poisson", "epice"], fetes=["Repas de famille"], sa=["Bissap", "Jus de gingembre"])

K("thiebou_yapp", "Thiébou yapp (riz à la viande)", "Ceebu yapp", f"{M} › Sénégal", "P", 1, 6, 30, 70, "€€", "Faitout.",
  "Riz cuit dans un jus d'oignons caramélisés et de viande d'agneau, moutarde et ail : le riz de fête à la viande.",
  ["1 kg|d'agneau en morceaux|Épaule d'agneau|3", f"500 g|de riz|{RIZ}|3", f"4|oignons|{OIG}|3", f"6 gousses|d'ail|{AIL}|2", f"2 c. à s.|de moutarde|{DIJON}|1", f"1 c. à c.|de poivre|{POIVRE}|1", f"8 cl|d'huile|{HN}|1", f"1|citron vert|{CITV}|1"],
  ["**Viande.** Dorée, puis oignons jusqu'à bien caramélisés, ail, moutarde, poivre ; eau à hauteur, 45 min.", "**Riz.** Retire la viande ; riz dans le jus (complète en eau), 20 min couvert.", "**Servir.** Viande dessus, oignons, citron vert."],
  age=1, profil=["viande_rouge"], fetes=["Ramadan / Aïd"])

K("dibi", "Dibi (agneau grillé aux oignons)", "Dibi", f"{M} › Sénégal › Dakar", "P", 1, 4, 20, 20, "€€", "Gril ou barbecue.",
  "Côtelettes d'agneau grillées, oignons crus moutardés, piment : l'agneau de rue de Dakar.",
  ["1 kg|de côtelettes ou d'épaule d'agneau|Côtelettes d'agneau|3", f"3|oignons|{OIG}|2", f"3 c. à s.|de moutarde|{DIJON}|2", f"1 c. à c.|de poivre|{POIVRE}|1", "1 c. à c.|de pâte de bouillon maison|SUB:bouillon_cube_maison|1", f"1|citron vert|{CITV}|1", f"1 pincée|de piment|{CAYENNE}|1"],
  ["**Assaisonner.** Viande frottée de bouillon, poivre, huile.", "**Griller.** Feu vif, 8-12 min.", "**Oignons.** Émincés, moutarde, citron vert, piment, sel. Avec la viande et du pain."],
  age=3, profil=["viande_rouge"], fetes=["Barbecue d'été", "Ramadan / Aïd"])

K("fataya", "Fatayas (chaussons frits au poisson)", "Fataya", f"{M} › Sénégal", "E", 2, 20, 50, 15, "€", "Rouleau, emporte-pièce, friteuse.",
  "Chaussons croustillants farcis de poisson (ou de viande) épicé, avec une sauce tomate-oignon : le snack sénégalais.",
  [f"500 g|de farine|{F55}|3", f"1 c. à c.|de levure|{LEV}|1", f"60 g|de beurre|{BEURRE}|1", "400 g|de thon en conserve ou de poisson cuit|Thon en conserve|3", f"2|oignons|{OIG}|2", "1 c. à s.|de nokoss|SUB:nokoss|2", f"2 c. à s.|de concentré|{CONC}|1", "1 L|d'huile de friture|Huile d'arachide|1"],
  ["**Pâte.** Farine, levure, beurre, sel, eau tiède : souple, 1 h.", "**Farce.** Oignons, nokoss, concentré, poisson émietté, 10 min.", "**Façonner.** Disques de 10 cm, farce, plie, ferme à la fourchette.", "**Frire.** 3 min par face à 170 °C."],
  age=3, cats=["enfants"], fetes=["Apéritif dînatoire", "Ramadan / Aïd"], profil=["poisson"])

K("thiakry", "Thiakry (couscous de mil au lait caillé)", "Thiakry", f"{M} › Sénégal", "D", 1, 6, 15, 30, "€", "Saladier.",
  "Graines de mil (ou semoule) mélangées à du lait caillé sucré, vanille et muscade : frais et doux.",
  ["250 g|de couscous de mil (ou semoule moyenne)|Millet / sorgho|3", f"500 g|de yaourt nature|{YAO}|3", f"200 g|de fromage blanc|Fromage blanc / faisselle|2", "100 g|de lait concentré sucré|Lait concentré sucré / non sucré|2", f"1 pincée|de muscade et vanille|{MUSC}|1", "50 g|de raisins secs|Raisins secs|1"],
  ["**Graines.** Cuites à la vapeur 20 min (ou semoule hydratée), égrenées, refroidies.", "**Mélanger.** Yaourt, fromage blanc, lait concentré, épices, graines, raisins. Très frais."],
  age=1, cats=["enfants"], fetes=["Ramadan / Aïd"], profil=["sucre"])

K("attieke_poisson", "Attiéké poisson braisé", "Garba / attiéké poisson", f"{M} › Côte d'Ivoire › Abidjan", "P", 1, 4, 25, 25, "€€", "Gril ou four, cuit-vapeur.",
  "Semoule de manioc fermentée acidulée, poisson grillé mariné, tomates, oignons et piment : le plat des maquis.",
  ["2|poissons (tilapia, dorade, maquereau)|Dorade|3", "500 g|d'attiéké|Manioc / attiéké / garri|3", f"3|tomates|{TOM}|2", f"2|oignons|{OIG}|2", f"4 gousses|d'ail|{AIL}|1", f"1 morceau|de gingembre|{GING}|1", "1|piment antillais|Piment antillais / scotch bonnet|1", f"2|citrons verts|{CITV}|1", f"4 c. à s.|d'huile|{HN}|1"],
  ["**Mariner.** Poissons entaillés : ail, gingembre, piment, huile, sel, 30 min.", "**Griller.** 10 min par face (ou four 220 °C 25 min).", "**Attiéké.** Vapeur 10 min, égrené à la fourchette.", "**Crudités.** Tomates et oignons en dés, citron vert, sel. Tout sur l'assiette."],
  age=3, profil=["poisson", "acide"])

K("alloco", "Alloco (bananes plantains frites)", "Alloco", f"{M} › Côte d'Ivoire", "A", 1, 4, 10, 10, "€", "Poêle profonde.",
  "Plantain bien mûr (peau noire) frit en rondelles, caramélisé : avec poisson, œufs ou sauce piment.",
  ["3|bananes plantains bien mûres|Plantain (banane à cuire)|3", "50 cl|d'huile|Huile d'arachide|2", f"1 pincée|de sel|{SEL}|0"],
  ["**Couper.** En biais, 1,5 cm.", "**Frire.** 3-4 min à 170 °C, dorées et caramélisées. Sel."],
  age=1, cats=["enfants"], profil=["sucre", "gras"])

K("kedjenou", "Kedjenou de poulet", "Kedjenou", f"{M} › Côte d'Ivoire", "P", 1, 4, 20, 60, "€", "Cocotte bien fermée.",
  "Poulet et légumes cuits à l'étouffée dans leur propre jus, sans eau, en secouant la cocotte : tendre et concentré.",
  [f"1,2 kg|de poulet en morceaux|{CUISSE}|3", f"3|tomates|{TOM}|2", f"2|oignons|{OIG}|2", "1|aubergine|Aubergine|1", f"1 morceau|de gingembre|{GING}|1", f"3 gousses|d'ail|{AIL}|1", "1|piment|Piment antillais / scotch bonnet|1", "2|feuilles de laurier + thym|Laurier|1"],
  ["**Monter.** Tout cru dans la cocotte, sel.", "**Étouffée.** Couvercle fermé (papier aluminium dessous), feu doux 1 h ; secoue la cocotte toutes les 10 min sans ouvrir. Avec attiéké ou riz."],
  age=3, profil=["leger"])

K("mafe_boeuf", "Mafé de bœuf (sauce arachide)", "Maafe", f"{M} › Mali", "P", 1, 6, 25, 90, "€€", "Cocotte.",
  "Bœuf mijoté dans une sauce tomate à la pâte d'arachide, patates douces et carottes : onctueux et nourrissant.",
  ["1 kg|de paleron en cubes|Paleron|3", "200 g|de pâte d'arachide (100 % cacahuète)|Pâte d'arachide|3", f"2 c. à s.|de concentré|{CONC}|1", f"2|oignons|{OIG}|1", "2|patates douces|Patate douce|2", f"2|carottes|{CAROTTE}|1", f"4 gousses|d'ail|{AIL}|1", "1|piment entier|Piment antillais / scotch bonnet|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Saisir.** Bœuf, oignons, ail, concentré.", "**Mijoter.** Eau à hauteur, 1 h.", "**Arachide.** Pâte délayée dans le bouillon, légumes, piment ; 30 min en remuant (elle attache). Riz blanc."],
  age=1, profil=["viande_rouge", "gras"], tips=["⚠️ Arachide : allergène majeur."])

K("ndole", "Ndolé (épinards-arachides, crevettes)", "Ndolè", f"{M} › Cameroun › Douala", "P", 2, 6, 40, 60, "€€", "Faitout, mixeur.",
  "Le plat national camerounais : feuilles amères (ici épinards et un peu de roquette), purée d'arachides fraîches, crevettes et bœuf.",
  ["1 kg|d'épinards (ou ndolé surgelé)|Épinard|3", "100 g|de roquette (amertume)|Roquette / mâche|1", "300 g|de cacahuètes crues décortiquées|Cacahuète / arachide|3", "300 g|de crevettes|Crevettes (cuites/crues)|2", "500 g|de bœuf en cubes|Paleron|2",
   f"2|oignons|{OIG}|1", f"4 gousses|d'ail|{AIL}|1", f"1 morceau|de gingembre|{GING}|1", f"10 cl|d'huile|{HN}|1"],
  ["**Bœuf.** Cuit 45 min dans l'eau avec ail, gingembre, oignon.", "**Arachides.** Bouillies 15 min, mixées en purée avec du bouillon ; cuites 20 min en remuant.", "**Feuilles.** Blanchies, pressées, ajoutées avec le bœuf, 15 min.", "**Finir.** Crevettes et oignons frits dans l'huile, versés dessus. Avec plantain."],
  age=1, profil=["gras"], tips=["⚠️ Arachide : allergène majeur."], fetes=["Repas de famille"])

K("poulet_dg", "Poulet DG", "Poulet directeur général", f"{M} › Cameroun", "P", 1, 6, 30, 45, "€€", "Cocotte, poêle.",
  "Poulet, plantains frits et légumes mijotés : le plat des grandes occasions au Cameroun, riche en couleurs.",
  [f"1,2 kg|de poulet en morceaux|{CUISSE}|3", "3|plantains mûrs|Plantain (banane à cuire)|3", f"2|carottes|{CAROTTE}|1", "200 g|de haricots verts|Haricots verts|1", f"1|poivron|{POIVRON}|1", f"3|tomates|{TOM}|2", f"2|oignons|{OIG}|1", f"1 morceau|de gingembre + 3 gousses d'ail|{GING}|1", f"30 cl|d'huile|{HN}|1"],
  ["**Poulet.** Mariné ail-gingembre, doré.", "**Plantains.** En rondelles frites, réservées.", "**Légumes.** Oignons, tomates, carottes, haricots, poivron ; poulet ; 25 min.", "**Finir.** Plantains 5 min. Persil."],
  age=1, cats=["enfants"], fetes=["Repas de famille"], profil=["gras"])

K("jollof_rice", "Riz jollof", "Jollof rice", f"{M} › Nigeria", "P", 1, 6, 25, 40, "€", "Cocotte à fond épais.",
  "Riz cuit dans une sauce tomate-poivron-piment mixée, avec thym et curry : fumé au fond, objet d'une rivalité joyeuse entre Nigeria et Ghana.",
  [f"500 g|de riz long étuvé|{RIZ}|3", f"4|tomates|{TOM}|2", f"2|poivrons rouges|{POIVRON}|2", "1|piment scotch bonnet|Piment antillais / scotch bonnet|1", f"2|oignons|{OIG}|2", f"3 c. à s.|de concentré|{CONC}|2", f"1 c. à c.|de curry|{CUR}|1", f"1 c. à c.|de thym|{THYM}|1", f"50 cl|de bouillon|{BOUILLON}|2", f"8 cl|d'huile|{HN}|1", "2|feuilles de laurier|Laurier|0"],
  ["**Base.** Mixe tomates, poivrons, 1 oignon, piment ; frits avec l'autre oignon et le concentré 20 min jusqu'à ce que l'huile remonte.", "**Riz.** Lavé, ajouté avec bouillon, épices, laurier ; couvert d'aluminium et du couvercle, feu très doux 30 min.", "**Finir.** Mélange ; laisse 5 min accrocher pour le goût fumé."],
  age=1, cats=["enfants"], fetes=["Anniversaire", "Repas de famille"], profil=["epice"], kids="✓ dès 1 an, piment entier retiré.")

K("suya", "Brochettes suya", "Suya", f"{M} › Nigeria", "P", 1, 4, 20, 15, "€€", "Brochettes, gril.",
  "Bœuf émincé enrobé d'un mélange cacahuète-épices (yaji), grillé : la street-food du soir au Nigeria.",
  ["600 g|de bœuf (rumsteck) en fines tranches|Rumsteck|3", "60 g|de cacahuètes grillées mixées|Cacahuète / arachide|3", f"1 c. à c.|de gingembre, paprika, piment|{PAPRIKA}|2", "1 c. à c.|de poudre d'oignon et d'ail|Poudre d'ail / d'oignon|1", f"2 c. à s.|d'huile|{HN}|1", "1|oignon rouge|Oignon rouge|1", f"2|tomates|{TOM}|1"],
  ["**Yaji.** Cacahuètes mixées + épices + sel.", "**Enrober.** Viande huilée puis roulée dans le yaji, en brochettes ; 1 h.", "**Griller.** 3-4 min par face. Oignon rouge, tomate, yaji en plus."],
  age=3, fetes=["Barbecue d'été"], profil=["viande_rouge", "epice"], tips=["⚠️ Arachide : allergène majeur."])

K("puff_puff", "Puff-puff (beignets)", "Puff-puff / bofrot", f"{M} › Nigeria", "G", 1, 30, 15, 60, "€", "Friteuse ou casserole profonde.",
  "Beignets ronds, légers et sucrés, levés à la levure : on les sert en montagne aux fêtes.",
  [f"300 g|de farine|{F55}|3", f"60 g|de sucre|{SUCRE}|2", f"7 g|de levure|{LEV}|1", "25 cl|d'eau tiède|-|0", f"1 pincée|de muscade|{MUSC}|0", "1 L|d'huile|Huile d'arachide|1"],
  ["**Pâte.** Tout mélanger : pâte collante. Pousse 1 h.", "**Frire.** Petites boules à la main mouillée, 3-4 min à 170 °C en les retournant."],
  age=1, cats=["enfants"], fetes=["Anniversaire"], profil=["sucre", "gras"])

K("kelewele", "Kelewele (plantain épicé)", "Kelewele", f"{M} › Ghana", "A", 1, 4, 15, 10, "€", "Poêle profonde.",
  "Dés de plantain marinés au gingembre et piment, frits : sucrés, piquants, irrésistibles.",
  ["3|plantains mûrs|Plantain (banane à cuire)|3", f"1 morceau|de gingembre|{GING}|2", f"½|oignon|{OIG}|1", f"1 pincée|de piment|{CAYENNE}|1", f"½ c. à c.|de muscade|{MUSC}|1", "50 cl|d'huile|Huile d'arachide|1"],
  ["**Mariner.** Plantain en dés avec gingembre et oignon râpés, épices, sel, 15 min.", "**Frire.** Dorés et caramélisés. Avec des cacahuètes grillées."],
  age=3, profil=["epice", "sucre"])

K("doro_wat", "Doro wat (poulet au berbéré)", "Doro wat", f"{M} › Éthiopie", "P", 2, 6, 30, 90, "€€", "Cocotte.",
  "Le plat de fête éthiopien : poulet mijoté dans des oignons confits et le berbéré, avec des œufs durs.",
  [f"1,2 kg|de cuisses de poulet sans peau|{CUISSE}|3", f"1 kg|d'oignons|{OIG}|3", "3 c. à s.|de berbéré|SUB:berbere_maison|3", "80 g|de beurre clarifié épicé|Ghee|2", f"4 gousses|d'ail + gingembre|{AIL}|1", f"6|œufs durs|{OEUF}|2", f"1|citron|{CIT}|1"],
  ["**Oignons.** Hachés très fin, à sec 30 min à feu doux, puis le beurre, encore 15 min.", "**Épices.** Berbéré, ail, gingembre ; un peu d'eau.", "**Poulet.** Frotté au citron, mijoté 45 min ; œufs durs entaillés 10 min."],
  age=3, fetes=["Repas de famille"], profil=["epice"])

K("bobotie", "Bobotie", "Bobotie", f"{M} › Afrique du Sud › Le Cap", "P", 1, 6, 25, 45, "€€", "Plat à four.",
  "Viande hachée au curry doux, raisins secs et chutney, sous une crème aux œufs : le gratin du Cap, sucré-épicé.",
  [f"800 g|de bœuf ou agneau haché|{HACHE}|3", f"2|oignons|{OIG}|1", f"1 c. à s.|de curry|{CUR}|2", "2 c. à s.|de chutney de mangue|SUB:chutney_mangue|2", "50 g|de raisins secs|Raisins secs|1", "1 tranche|de pain trempé dans le lait|Pain rassis (réservé)|1", f"2|œufs|{OEUF}|2", f"25 cl|de lait|{LAIT}|1", "3|feuilles de laurier|Laurier|0"],
  ["**Viande.** Oignons, curry, viande, pain pressé, chutney, raisins, sel ; 10 min.", "**Crème.** Œufs + lait du pain, versés dessus, laurier planté.", "**Cuire.** 35 min à 180 °C. Avec riz jaune."],
  age=1, profil=["viande_rouge", "sucre"])

K("chakalaka", "Chakalaka", "Chakalaka", f"{M} › Afrique du Sud", "A", 1, 6, 15, 25, "€", "Sauteuse.",
  "Une poêlée épicée de carottes, poivrons, haricots et tomates : l'accompagnement des braai (barbecues).",
  [f"3|carottes râpées|{CAROTTE}|2", f"2|poivrons|{POIVRON}|2", "400 g|de haricots blancs à la tomate ou nature|Haricots blancs / lingots|2", f"3|tomates|{TOM}|2", f"1|oignon|{OIG}|1", f"1 c. à s.|de curry|{CUR}|2", f"1|piment|{PIMENT}|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Cuire.** Oignon, curry, piment, poivrons, carottes 10 min ; tomates et haricots 15 min."],
  age=3, fetes=["Barbecue d'été"], profil=["epice"])

K("romazava", "Romazava (bouillon de bœuf aux brèdes)", "Romazava", f"{M} › Madagascar", "P", 1, 6, 20, 90, "€", "Faitout.",
  "Bœuf mijoté avec des brèdes (feuilles vertes) et du gingembre : le plat national malgache, avec du riz.",
  ["1 kg|de bœuf (jarret, paleron)|Jarret de bœuf|3", "500 g|de brèdes (épinards, cresson, feuilles de moutarde)|Cresson|3", f"3|tomates|{TOM}|2", f"1|oignon|{OIG}|1", f"1 morceau|de gingembre|{GING}|2", f"3 gousses|d'ail|{AIL}|1"],
  ["**Mijoter.** Bœuf doré, oignon, tomates, ail, gingembre ; eau à hauteur, 1 h 15.", "**Brèdes.** 10 min. Avec riz blanc."], age=1, profil=["leger"])

K("moambe", "Poulet moambé", "Moambe", f"{M} › Congo (RDC)", "P", 1, 6, 20, 60, "€€", "Cocotte.",
  "Poulet mijoté dans une sauce de noix de palme (ou de beurre de cacahuète pour la version de diaspora), avec épinards.",
  [f"1,2 kg|de poulet en morceaux|{CUISSE}|3", "400 g|de crème de noix de palme (ou 150 g de beurre de cacahuète)|Huile de palme rouge|3", f"2|oignons|{OIG}|1", f"3|tomates|{TOM}|1", "300 g|d'épinards|Épinard|1", f"3 gousses|d'ail|{AIL}|1", "1|piment|Piment antillais / scotch bonnet|1"],
  ["**Dorer.** Poulet, oignons, ail.", "**Sauce.** Tomates, crème de palme, eau ; 45 min.", "**Finir.** Épinards 5 min. Riz ou fufu."],
  age=1, profil=["gras"])

K("maharagwe", "Maharagwe (haricots rouges au coco)", "Maharagwe", f"{M} › Kenya", "P", 1, 4, 15, 30, "€", "Sauteuse.",
  "Haricots rouges mijotés dans le lait de coco avec curry et tomate : réconfortant, avec chapati ou riz.",
  ["500 g|de haricots rouges cuits|Haricots rouges / noirs|3", f"40 cl|de lait de coco|{COCO}|3", f"2|tomates|{TOM}|1", f"1|oignon|{OIG}|1", f"1 c. à c.|de curry|{CUR}|1", f"½ c. à c.|de curcuma|{CURC}|1", f"2 gousses|d'ail|{AIL}|1", f"1 bouquet|de coriandre|{CORI}|1"],
  ["**Base.** Oignon, ail, épices, tomates 10 min.", "**Mijoter.** Haricots et coco, 20 min. Coriandre."], age=1, cats=["enfants"], profil=["leger"])

K("bissap_sirop", "Sirop de bissap maison", "Bissap", f"{M} › Sénégal", "B", 1, 15, 15, 60, "€", "Casserole, filtre, bouteille.",
  "Fleurs d'hibiscus infusées, sucre, menthe et fleur d'oranger : un sirop à allonger d'eau ou d'eau pétillante.",
  ["60 g|d'hibiscus séché|Hibiscus séché (bissap)|3", f"400 g|de sucre|{SUCRE}|2", "1 L|d'eau|-|0", "10|feuilles de menthe|Menthe|1", "1 c. à s.|d'eau de fleur d'oranger|Eau de fleur d'oranger|1"],
  ["**Infuser.** Hibiscus dans l'eau bouillante, 15 min hors du feu ; filtre.", "**Sirop.** Avec le sucre, 10 min ; menthe et fleur d'oranger. Bouteille."],
  keep="1 mois au frigo.", age=1, cats=["boissons", "enfants"], fetes=["Ramadan / Aïd"], profil=["sucre", "acide"], tips=["Les fleurs infusées : 2e infusion plus légère, ou confites dans le sucre."])
