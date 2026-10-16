# -*- coding: utf-8 -*-
"""Vague 3 · Plats végétariens complets du monde (audit UX du 16/10/2026 : « ≈ 27 % de plats sans viande ni poisson »).
Chaque plat associe une légumineuse, un œuf, un fromage ou du tofu à des légumes et un féculent. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

QF = "France › Cuisine du quotidien"; IT = "Europe du Sud › Italie"; IN = "Asie du Sud › Inde"; TH = "Asie du Sud-Est › Thaïlande"
VG = ["vegetarien"]

K("curry_legumes_coco", "Curry de légumes au lait de coco", "Vegetable curry", f"{IN} › Kerala", "P", 1, 4, 20, 25, "€", "Cocotte, casserole (riz).",
  "Pommes de terre, chou-fleur, carottes, petits pois et pois chiches dans une sauce coco aux épices douces : le curry de légumes complet.",
  [f"2|pommes de terre|{PDT}|2", "½|chou-fleur|Chou-fleur|2", f"2|carottes|{CAROTTE}|2", "100 g|de petits pois|Petits pois / pois gourmands|1", f"1 boîte|de pois chiches|{POIS}|2", "40 cl|de lait de coco|Lait de coco / crème de coco|3", f"1|oignon|{OIG}|1", f"2 gousses|d'ail|{AIL}|1", "1 morceau (3 cm)|de gingembre|Gingembre frais|1", f"2 c. à s.|de curry|{CUR}|2", f"½ bouquet|de coriandre|{CORI}|1?"],
  ["**Base.** Oignon 5 min ; ail, gingembre, curry 1 min : ça embaume.", "**Mijoter.** Légumes en morceaux, lait de coco, 20 cl d'eau, sel ; 20 min couvert : la lame entre dans la pomme de terre.",
   "**Finir.** Pois chiches et petits pois 5 min ; coriandre ; avec du riz basmati ou du naan."],
  age=3, cats=VG + ["enfants"], profil=["epice"], tech=["torréfier les épices"])

K("lasagnes_legumes_ricotta", "Lasagnes aux légumes et à la ricotta", "Lasagne alle verdure", IT, "P", 2, 6, 40, 40, "€€", "Plat à gratin, four.",
  "Courgettes, aubergines et épinards, sauce tomate, ricotta et mozzarella entre les feuilles : généreuses et végétariennes.",
  ["250 g|de feuilles de lasagne|Lasagnes|3", "2|courgettes|Courgette|2", "1|aubergine|Aubergine|2", "200 g|d'épinards|Épinard|2", "250 g|de ricotta|Ricotta|2", "1 boule|de mozzarella|Mozzarella / burrata|2", f"700 g|de sauce tomate|{PELEES}|2", f"50 g|de parmesan|{PARM}|1", f"2 gousses|d'ail|{AIL}|1"],
  ["**Légumes.** En dés, rôtis 20 min à 200 °C avec huile et sel ; épinards tombés à la poêle avec l'ail.", "**Monter.** Sauce, feuilles, légumes, ricotta ; trois fois ; finir par sauce, mozzarella, parmesan.",
   "**Cuire.** 180 °C, 40 min : doré et bouillonnant ; 10 min de repos avant de couper."], age=1, cats=VG + ["enfants"], fetes=["Repas de famille"])

K("risotto_courge_sauge", "Risotto à la courge et à la sauge", "Risotto alla zucca", f"{IT} › Lombardie", "P", 2, 4, 35, 0, "€", "Sauteuse.",
  "Courge fondue dans un risotto crémeux, sauge croustillante et parmesan : l'automne italien.",
  ["300 g|de riz à risotto|Riz à risotto (arborio, carnaroli)|3", "500 g|de courge (butternut, potimarron)|Butternut / courge musquée|3", f"1|oignon|{OIG}|1", "1 l|de bouillon de légumes chaud|Bouillon cube légumes|2", f"60 g|de parmesan|{PARM}|2", f"30 g|de beurre|{BEURRE}|2", "8 feuilles|de sauge|Sauge|1"],
  ["**Nacrer.** Oignon 3 min au beurre ; riz 2 min : il devient translucide sur les bords.", "**Cuire.** Courge en petits dés ; bouillon louche par louche en remuant, 18 min : le riz est crémeux mais encore un peu ferme.",
   "**Lier.** Hors du feu, beurre et parmesan, 2 min couvert ; sauge frite 30 s dans le beurre."], age=1, cats=VG, tech=["nacrer"])

K("hachis_lentilles_patate_douce", "Hachis de lentilles à la purée de patate douce", "Lentil shepherd's pie", "Europe du Nord › Royaume-Uni", "P", 1, 6, 30, 30, "€", "Cocotte, plat à gratin.",
  "Lentilles mijotées aux légumes et à la tomate sous une purée de patate douce gratinée : le shepherd's pie végétarien.",
  ["250 g|de lentilles vertes|Lentilles vertes / brunes|3", "1 kg|de patates douces|Patate douce|3", f"2|carottes|{CAROTTE}|1", f"1|oignon|{OIG}|1", f"2 c. à s.|de concentré de tomate|{CONC}|1", "1 c. à s.|de sauce Worcestershire (ou soja)|Sauce Worcestershire|1?", f"60 g|de fromage râpé|{GRUY}|1", f"20 g|de beurre|{BEURRE}|1", f"1 c. à c.|de thym|{THYM}|1"],
  ["**Lentilles.** Oignon et carottes 5 min, concentré, lentilles, thym, 60 cl d'eau ; 25 min : épaisses ; sel, sauce.", "**Purée.** Patates douces cuites 15 min, écrasées au beurre.",
   "**Gratiner.** Lentilles dans le plat, purée, fromage ; 200 °C, 20 min : doré."], age=1, cats=VG + ["enfants"])

K("tajine_legumes_pois_chiches", "Tajine de légumes aux pois chiches et abricots", "Tajine khodra", "Afrique du Nord › Maroc", "P", 1, 4, 20, 40, "€", "Tajine ou cocotte.",
  "Carottes, courgettes, navets, pois chiches et abricots secs, épices douces et citron confit : sucré-salé, végétarien.",
  [f"3|carottes|{CAROTTE}|2", "2|courgettes|Courgette|2", "2|navets|Navet / navet boule d'or|1", f"1 boîte|de pois chiches|{POIS}|3", "80 g|d'abricots secs|Abricots secs|1", f"1|oignon|{OIG}|1", "2 c. à c.|de ras el-hanout|Ras el-hanout|2", "½|citron confit|Citron confit|1?", f"½ bouquet|de coriandre|{CORI}|1"],
  ["**Base.** Oignon 5 min, épices 1 min.", "**Mijoter.** Légumes en gros morceaux, abricots, 30 cl d'eau, sel ; couvert 35 min à feu doux.", "**Finir.** Pois chiches et citron confit 5 min ; coriandre ; semoule."],
  age=1, cats=VG + ["enfants"], profil=["sucre", "epice"])

K("curry_vert_tofu_legumes", "Curry vert au tofu et aux légumes", "Kaeng khiao wan phak", TH, "P", 1, 4, 20, 15, "€€", "Wok ou sauteuse.",
  "Pâte de curry vert, lait de coco, tofu, aubergine, haricots verts et basilic thaï : vif, parfumé, sans viande.",
  ["400 g|de tofu ferme|Tofu (ferme / soyeux)|3", "40 cl|de lait de coco|Lait de coco / crème de coco|3", "2 c. à s.|de pâte de curry vert|Pâte de curry thaï (rouge, verte)|2", "1|aubergine|Aubergine|2", "150 g|de haricots verts|Haricots verts|1", "1 poignée|de basilic thaï|Basilic thaï|1", f"1 c. à s.|de sauce soja|{SOJA}|1", f"1 c. à c.|de sucre|{SUCRE}|1"],
  ["**Pâte.** Curry vert frit 1 min dans 4 c. à s. de crème de coco : l'huile se sépare et ça sent fort.", "**Mijoter.** Lait de coco, aubergine en dés, haricots, 10 min.",
   "**Finir.** Tofu en cubes 3 min, soja, sucre, basilic ; riz jasmin."], age=6, cats=VG, profil=["epice"])

K("aubergines_parmigiana", "Aubergines à la parmesane", "Parmigiana di melanzane", f"{IT} › Campanie", "P", 2, 6, 40, 40, "€€", "Four, plat à gratin.",
  "Tranches d'aubergine rôties, sauce tomate au basilic, mozzarella et parmesan en couches : fondant, gratiné, végétarien.",
  ["3|aubergines|Aubergine|3", f"700 g|de sauce tomate|{PELEES}|3", "2 boules|de mozzarella|Mozzarella / burrata|2", f"80 g|de parmesan|{PARM}|2", "1 bouquet|de basilic|Basilic|1", f"6 c. à s.|d'huile d'olive|{HO}|2", f"2 gousses|d'ail|{AIL}|1"],
  ["**Rôtir.** Aubergines en tranches de 1 cm, huilées, salées ; 220 °C, 20 min : dorées et souples (plus léger que frites).", "**Sauce.** Ail, tomates, basilic, 15 min.",
   "**Monter et cuire.** Sauce, aubergines, mozzarella, parmesan, trois fois ; 180 °C, 35 min ; repos 15 min."], age=3, cats=VG, fetes=["Repas de famille"])

K("poivrons_farcis_riz", "Poivrons et tomates farcis au riz et aux herbes", "Gemistá", "Europe du Sud › Grèce", "P", 1, 6, 30, 60, "€", "Plat à four.",
  "Légumes farcis de riz parfumé à la menthe, à l'aneth et au persil, cuits au four avec des pommes de terre : le plat d'été grec.",
  [f"4|tomates|{TOM}|2", f"4|poivrons|{POIVRON}|2", f"200 g|de riz rond|Riz rond / sushi|3", f"1|oignon|{OIG}|1", "½ bouquet|de menthe|Menthe|1", "½ bouquet|d'aneth|Aneth|1", f"½ bouquet|de persil|{PERSIL}|1", f"3|pommes de terre|{PDT}|2", f"10 c. à s.|d'huile d'olive|{HO}|2"],
  ["**Vider.** Chapeaux coupés ; pulpe des tomates mixée.", "**Farce.** Riz cru, pulpe, oignon râpé, herbes, sel, 4 c. à s. d'huile ; légumes remplis aux trois quarts (le riz gonfle).",
   "**Cuire.** Pommes de terre en quartiers autour, huile, 1 verre d'eau ; 180 °C, 1 h : légumes fripés, riz tendre."], age=3, cats=VG, fetes=["Barbecue d'été"])

K("boulettes_lentilles_tomate", "Boulettes de lentilles en sauce tomate", "Polpette di lenticchie", IT, "P", 1, 4, 30, 20, "€", "Four, sauteuse.",
  "Boulettes de lentilles, chapelure et parmesan, cuites au four puis mijotées dans la sauce tomate : avec des spaghetti, comme des polpette.",
  ["250 g|de lentilles cuites|Lentilles vertes / brunes|3", "50 g|de chapelure|Chapelure|2", f"40 g|de parmesan|{PARM}|1", f"1|œuf|{OEUF}|2", f"1 gousse|d'ail|{AIL}|1", f"½ bouquet|de persil|{PERSIL}|1", f"500 g|de sauce tomate|{PELEES}|2", f"300 g|de spaghetti|{PATES}|2"],
  ["**Mélanger.** Lentilles écrasées, chapelure, parmesan, œuf, ail, persil, sel : se tient en boule (sinon un peu de chapelure).", "**Cuire.** Boulettes huilées, 200 °C, 15 min : fermes et dorées.",
   "**Mijoter.** 5 min dans la sauce tomate ; sur les spaghetti."], age=1, cats=VG + ["enfants"])

K("quiche_epinards_feta", "Quiche épinards et feta", "Quiche épinards-feta", QF, "P", 1, 6, 20, 35, "€", "Moule à tarte, four.",
  "Pâte brisée, épinards, feta, œufs et crème, une pointe de muscade : la quiche sans lardons que tout le monde redemande.",
  ["1|pâte brisée|Pâte brisée / sablée (prête)|3", "300 g|d'épinards|Épinard|2", "150 g|de feta|Feta|2", f"3|œufs|{OEUF}|2", f"20 cl|de crème|{CF}|2", f"1 pincée|de muscade|{MUSC}|0"],
  ["**Épinards.** Tombés à la poêle, bien pressés : sinon la quiche sera détrempée.", "**Appareil.** Œufs, crème, muscade, poivre (peu de sel : la feta est salée).",
   "**Cuire.** Pâte, épinards, feta, appareil ; 180 °C, 35 min : prise et dorée."], age=1, cats=VG + ["enfants"], tech=["foncer une pâte"])

K("enchiladas_haricots", "Enchiladas aux haricots noirs et patate douce", "Enchiladas de frijoles", "Amérique latine › Mexique", "P", 1, 4, 30, 25, "€", "Plat à four.",
  "Tortillas roulées sur haricots noirs et patate douce, nappées de sauce tomate pimentée et gratinées : végétariennes et fondantes.",
  ["8|tortillas|Tortillas de blé|3", "400 g|de haricots noirs|Haricots rouges / noirs|3", "1|patate douce|Patate douce|2", f"500 g|de tomates pelées|{PELEES}|2", f"1 c. à c.|de cumin|{CUMIN}|1", f"1 c. à c.|de paprika fumé|{PFUME}|1", "150 g|de cheddar|Cheddar|2", f"½ bouquet|de coriandre|{CORI}|1"],
  ["**Garniture.** Patate douce en dés rôtie 20 min ; mélangée aux haricots, cumin, sel.", "**Sauce.** Tomates, paprika, sel, 10 min.",
   "**Monter.** Tortillas garnies roulées, serrées dans le plat, sauce, fromage ; 200 °C, 20 min."], age=3, cats=VG, profil=["epice"])

K("biryani_legumes", "Biryani aux légumes", "Sabzi biryani", f"{IN} › Hyderabad", "P", 2, 6, 40, 30, "€€", "Cocotte avec couvercle.",
  "Riz basmati parfumé en couches avec des légumes épicés au yaourt, oignons frits, safran et herbes : festif et végétarien.",
  [f"400 g|de riz basmati|{RIZ}|3", "½|chou-fleur|Chou-fleur|2", f"2|carottes|{CAROTTE}|2", "150 g|de petits pois|Petits pois / pois gourmands|1", f"150 g|de yaourt|{YAO}|2", f"3|oignons|{OIG}|2", "2 c. à s.|de garam masala|Garam masala|2", "1 pincée|de safran|Safran (pistils)|1?", "½ bouquet|de menthe|Menthe|1", f"½ bouquet|de coriandre|{CORI}|1"],
  ["**Oignons.** Émincés, frits doucement 15 min : bruns et croustillants.", "**Légumes.** En morceaux, yaourt, garam masala, la moitié des oignons, 10 min. Riz cuit 6 min seulement (aux deux tiers).",
   "**Étager.** Légumes, riz, safran infusé, herbes, oignons ; couvercle serré, feu très doux 25 min."], age=3, cats=VG, fetes=["Ramadan / Aïd", "Diwali"], profil=["epice"])

K("cannellonis_epinards_ricotta", "Cannellonis épinards-ricotta", "Cannelloni ricotta e spinaci", IT, "P", 2, 4, 35, 30, "€€", "Plat à gratin, poche ou cuillère.",
  "Tubes de pâte farcis d'épinards et de ricotta, sous béchamel et sauce tomate : un classique italien du dimanche.",
  ["12|cannellonis (ou feuilles de lasagne roulées)|Lasagnes|3", "400 g|d'épinards|Épinard|2", "250 g|de ricotta|Ricotta|3", f"50 g|de parmesan|{PARM}|1", f"400 g|de sauce tomate|{PELEES}|2", f"40 cl|de béchamel|SUB:bechamel|2", f"1 pincée|de muscade|{MUSC}|0"],
  ["**Farce.** Épinards tombés, pressés, hachés ; ricotta, parmesan, muscade, sel.", "**Garnir.** Cannellonis remplis à la poche (ou un sac coupé).",
   "**Cuire.** Sauce tomate au fond, cannellonis, béchamel, parmesan ; 180 °C, 30 min."], age=1, cats=VG + ["enfants"], tech=["faire un roux"])

K("polenta_champignons_creme", "Polenta crémeuse aux champignons", "Polenta ai funghi", f"{IT} › Vénétie", "P", 1, 4, 15, 15, "€", "Casserole, poêle.",
  "Polenta souple au parmesan, champignons poêlés à l'ail et au thym : réconfortant et prêt en 30 minutes.",
  ["200 g|de polenta (cuisson rapide)|Polenta / semoule de maïs|3", "500 g|de champignons variés|Champignon de Paris|3", f"60 g|de parmesan|{PARM}|2", f"30 g|de beurre|{BEURRE}|1", f"2 gousses|d'ail|{AIL}|1", f"1 c. à c.|de thym|{THYM}|1", "1 l|d'eau ou de bouillon|Bouillon cube légumes|1"],
  ["**Polenta.** En pluie dans le bouillon frémissant en fouettant, 5-8 min : épaisse ; beurre, parmesan.", "**Champignons.** Poêle très chaude, sans les remuer d'abord : ils dorent ; ail, thym, sel.", "**Servir.** Polenta dans l'assiette creuse, champignons dessus."],
  age=1, cats=VG)

K("burger_vegetarien_haricots", "Burger végétarien aux haricots rouges", "Bean burger", "Amérique du Nord › États-Unis", "P", 1, 4, 25, 12, "€", "Poêle.",
  "Galettes de haricots rouges, flocons d'avoine et paprika fumé, dorées à la poêle, dans un pain brioché avec cheddar et oignons.",
  ["400 g|de haricots rouges|Haricots rouges / noirs|3", "50 g|de flocons d'avoine|Flocons d'avoine (porridge)|2", f"1|œuf|{OEUF}|1", f"1 c. à c.|de paprika fumé|{PFUME}|1", f"1 c. à c.|de cumin|{CUMIN}|1", "4|pains burger|Brioche|2", "4 tranches|de cheddar|Cheddar|1", "1|oignon rouge|Oignon rouge|1", "4 feuilles|de salade|Salade (laitue, batavia)|1"],
  ["**Galettes.** Haricots égouttés et séchés, écrasés ; avoine, œuf, épices, sel ; 4 galettes, 15 min au frais.", "**Cuire.** Poêle huilée, 4-5 min par face : croûte dorée ; cheddar sur le dessus, couvert 1 min.",
   "**Monter.** Pain grillé, sauce, salade, galette, oignon."], age=3, cats=VG + ["enfants"])

K("dhal_epinards_coco", "Dal aux épinards et au lait de coco", "Palak dal", IN, "P", 1, 4, 15, 25, "€", "Casserole.",
  "Lentilles corail fondues au lait de coco, épinards et tadka (épices grésillantes) : doux, complet, très économique.",
  ["250 g|de lentilles corail|Lentilles corail|3", "200 g|d'épinards|Épinard|2", "20 cl|de lait de coco|Lait de coco / crème de coco|2", f"1|oignon|{OIG}|1", f"2 gousses|d'ail|{AIL}|1", f"1 c. à c.|de curcuma|{CURC}|1", f"1 c. à c.|de cumin en graines|{CUMIN}|1", "1 c. à c.|de graines de moutarde|Graines de moutarde|1?"],
  ["**Cuire.** Lentilles rincées, 70 cl d'eau, curcuma, 20 min : elles se défont ; lait de coco, épinards, sel.", "**Tadka.** Huile chaude, cumin, moutarde : ça crépite ; oignon et ail 5 min : dorés.", "**Verser.** Le tadka sur le dal ; riz ou naan."],
  age=1, cats=VG + ["enfants"], tech=["torréfier les épices"])

K("shakshuka_haricots_blancs", "Œufs pochés aux haricots blancs et poivrons", "Shakshuka aux haricots", "Afrique du Nord › Tunisie", "P", 1, 4, 10, 25, "€", "Sauteuse avec couvercle.",
  "Sauce tomate-poivron au cumin enrichie de haricots blancs, œufs pochés dedans : complet en protéines, une seule poêle.",
  [f"6|œufs|{OEUF}|3", "400 g|de haricots blancs|Haricots blancs / lingots|2", f"2|poivrons|{POIVRON}|2", f"400 g|de tomates pelées|{PELEES}|2", f"1|oignon|{OIG}|1", f"1 c. à c.|de cumin|{CUMIN}|1", "1 c. à c.|de harissa|Harissa (tube/pâte)|1?", f"½ bouquet|de coriandre|{CORI}|1"],
  ["**Sauce.** Oignon et poivrons 8 min ; cumin, harissa, tomates, haricots ; 10 min.", "**Pocher.** Six creux, un œuf dans chacun ; couvert 6-8 min : blancs pris, jaunes coulants.", "**Servir.** Coriandre, pain."],
  age=3, cats=VG, profil=["epice"])

K("tarte_tatin_legumes", "Tatin de tomates cerises et oignons rouges", "Tatin salée", QF, "P", 2, 6, 20, 30, "€", "Moule à manqué, four.",
  "Tomates cerises et oignons caramélisés au balsamique sous une pâte feuilletée, retournée : chic et facile.",
  ["1|pâte feuilletée|Pâte feuilletée (prête)|3", "400 g|de tomates cerises|Tomate cerise|3", "2|oignons rouges|Oignon rouge|2", "2 c. à s.|de vinaigre balsamique|Vinaigre balsamique|1", f"1 c. à s.|de sucre|{SUCRE}|1", f"1 c. à c.|de thym|{THYM}|1", "100 g|de chèvre frais|Chèvre (frais, bûche)|1?"],
  ["**Caraméliser.** Oignons en quartiers 10 min à l'huile ; sucre, balsamique : sirupeux.", "**Monter.** Dans le moule : oignons, tomates serrées, thym ; pâte par-dessus, bords rentrés.",
   "**Cuire et retourner.** 200 °C, 30 min : pâte gonflée et dorée ; 5 min de repos, retourne ; chèvre émietté."], age=3, cats=VG, fetes=["Apéritif dînatoire"])

K("pad_thai_tofu", "Pad thaï au tofu", "Phat thai taohu", TH, "P", 2, 2, 25, 10, "€", "Wok.",
  "Nouilles de riz sautées au tamarin, tofu doré, œuf, germes de soja et cacahuètes : la version végétarienne du plat national thaï.",
  ["200 g|de nouilles de riz plates|Nouilles de riz / vermicelles|3", "200 g|de tofu ferme|Tofu (ferme / soyeux)|3", f"2|œufs|{OEUF}|2", "100 g|de germes de soja|Germes de soja|1", "2 c. à s.|de pâte de tamarin|Pâte de tamarin|2", f"2 c. à s.|de sauce soja|{SOJA}|2", f"1 c. à s.|de sucre|{SUCRE}|1", "40 g|de cacahuètes|Cacahuète / arachide|1", f"1|citron vert|{CITV}|1", f"3|cébettes|Oignon nouveau / cébette|1"],
  ["**Tremper.** Nouilles 10 min à l'eau tiède : souples mais pas cuites.", "**Sauter.** Tofu en dés doré ; œufs brouillés ; nouilles et sauce (tamarin, soja, sucre, 3 c. à s. d'eau), 3 min : elles absorbent.",
   "**Finir.** Germes, cébette 30 s ; cacahuètes concassées, citron vert."], age=3, cats=VG, tech=["wok"])

K("gratin_chou_fleur_lentilles", "Gratin de chou-fleur et lentilles corail au curry", "Gratin curry", QF, "P", 1, 4, 20, 25, "€", "Plat à gratin.",
  "Chou-fleur rôti, lentilles corail au curry doux et fromage gratiné : un gratin complet, sans béchamel.",
  ["1|chou-fleur|Chou-fleur|3", "150 g|de lentilles corail|Lentilles corail|3", "20 cl|de lait de coco|Lait de coco / crème de coco|2", f"1 c. à s.|de curry doux|{CUR}|1", f"80 g|de fromage râpé|{GRUY}|2", f"1|oignon|{OIG}|1"],
  ["**Lentilles.** Oignon 5 min, curry, lentilles, lait de coco, 30 cl d'eau, 15 min : crémeuses.", "**Chou-fleur.** En bouquets, 6 min à l'eau salée.", "**Gratiner.** Le tout dans le plat, fromage, 200 °C, 20 min : doré."],
  age=1, cats=VG + ["enfants"])

K("galettes_sarrasin_champignons", "Galettes de sarrasin aux champignons, œuf et emmental", "Galette forestière", "France › Bretagne", "P", 1, 4, 20, 10, "€", "Poêle ou crêpière.",
  "Galette de sarrasin, champignons poêlés, œuf et emmental : la complète bretonne en version végétarienne.",
  ["8|galettes de sarrasin (ou pâte maison)|Farine de sarrasin|3", "300 g|de champignons|Champignon de Paris|2", f"4|œufs|{OEUF}|2", f"120 g|d'emmental râpé|{GRUY}|2", f"30 g|de beurre salé|{BEURRE}|1", f"1 c. à s.|de persil|{PERSIL}|0"],
  ["**Champignons.** Poêlés au beurre, persil, sel.", "**Garnir.** Galette dans la poêle beurrée ; fromage, œuf au centre (blanc étalé à la spatule), champignons ; 3 min : le blanc prend.",
   "**Plier.** Les bords en carré, le jaune visible au centre."], age=3, cats=VG)
