# -*- coding: utf-8 -*-
"""Vague 4 · Pique-nique (16/10/2026) : ce qui voyage bien, se mange froid ou tiède, souvent avec les doigts, sans mayonnaise
crue au soleil. Classiques, originaux, du monde, pour les enfants et pour les grands, avec les restes et sans emballage jetable.
Règle D21 pour le porc, variantes sans alcool « à tester ». NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

PN = ["pique_nique"]
FETE = ["Pique-nique"]
FROID = "Glacière avec pains de glace jusqu'au repas ; 2 h au plus hors du froid (1 h s'il fait plus de 32 °C), puis on ne rapporte pas les restes."
VSAKE = ("Sans alcool", ["alcohol"], {"Mirin": [("Vinaigre de riz", 0.5), ("Sucre blanc / roux / cassonade / vergeoise", 0.3)]}, "Mirin → **vinaigre de riz + sucre**. **À tester**.")

# ——— Les grands classiques à emporter ———
K("pain_surprise", "Pain surprise (le pain garni à partager)", "Pain surprise", "France", "E", 2, 10, 45, 120, "€€", "Couteau-scie, film ou torchon.",
  "Un gros pain de campagne évidé d'un bloc, la mie coupée en tranches et garnie en mini-sandwichs, puis remise dans la croûte : on ouvre le chapeau sur la nappe et chacun pioche.",
  ["1|gros pain de campagne rond (1 kg, de la veille)|Pain de campagne / complet|3", f"80 g|de beurre mou|{BEURRE}|2", "150 g|de saumon fumé|Saumon fumé|2", "4 tranches|de jambon de dinde|Jambon de dinde / de poulet|2", "150 g|de fromage frais aux herbes|Fromage à tartiner / fondu|2", "1|concombre|Concombre|1", "1 c. à s.|d'aneth ou ciboulette|Aneth|1"],
  ["**Évider.** Chapeau coupé ; couteau long glissé à 1 cm de la croûte tout autour, puis par une fente à la base : le cylindre de mie sort d'un bloc.",
   "**Trancher et garnir.** Mie en tranches horizontales de 1 cm ; tartinées de beurre ou de fromage frais, garnies (saumon-aneth, dinde-concombre), refermées deux à deux et coupées en parts.",
   "**Remonter.** Sandwichs remis en place dans la croûte, chapeau reposé ; filmé, 2 h au frais (il se tient)."],
  tips=["Le pain d'hier se tranche mieux que le pain frais.", FROID], keep="Le jour même, au frais.", age=3, cats=PN + ["enfants"], fetes=FETE + ["Anniversaire"])

K("terrine_legumes", "Terrine de légumes du soleil", "Terrine de légumes", "France › Provence-Alpes-Côte d'Azur", "E", 1, 8, 30, 60, "€", "Moule à cake, four.",
  "Courgettes, carottes et poivrons en couches dans un appareil œufs-fromage frais aux herbes, cuite au bain-marie : elle se tranche froide comme un pâté, sans viande.",
  ["2|courgettes|Courgette|3", f"3|carottes|{CAROTTE}|2", f"1|poivron rouge|{POIVRON}|2", f"5|œufs|{OEUF}|3", "150 g|de fromage frais|Fromage à tartiner / fondu|2", f"50 g|de parmesan|{PARM}|1", "1 bouquet|de basilic|Basilic|1"],
  ["**Légumes.** Courgettes et carottes en lanières à l'économe, poivron en bandes ; 5 min à la vapeur, bien égouttés (sinon la terrine rend de l'eau).", "**Appareil.** Œufs, fromage frais, parmesan, basilic, sel, poivre.",
   "**Cuire.** Moule chemisé : couches de légumes et d'appareil ; bain-marie 170 °C, 50 min : prise au centre. Refroidie, une nuit au frais avant de démouler et trancher."],
  tips=[FROID], keep="3 jours au frigo.", age=1, cats=PN + ["vegetarien", "enfants"], fetes=FETE)

K("tarte_courgette_chevre", "Tarte fine courgette-chèvre", "Tarte fine", "France", "E", 1, 6, 15, 30, "€", "Plaque, four.",
  "Une pâte feuilletée à plat, de fines rondelles de courgette en écailles, du chèvre et du miel : elle se coupe en carrés et se mange froide, à la main.",
  ["1|pâte feuilletée|Pâte feuilletée (prête)|3", "2|courgettes|Courgette|3", "150 g|de bûche de chèvre|Chèvre (frais, bûche)|2", f"1 c. à s.|de miel|{MIEL}|1", f"2 c. à s.|d'huile d'olive|{HO}|1", f"1 c. à c.|de thym|{THYM}|1"],
  ["**Base.** Pâte sur plaque, piquée à la fourchette en laissant 1 cm de bord.", "**Garnir.** Courgettes en rondelles de 2 mm en écailles, chèvre émietté, huile, thym, sel.", "**Cuire.** 200 °C, 25-30 min : bords gonflés et dorés ; miel en filet. En carrés, refroidie sur grille (le dessous reste croustillant)."],
  tips=[FROID], keep="2 jours au frigo ; 5 min au four pour recroustiller.", age=1, cats=PN + ["vegetarien", "enfants"], fetes=FETE)

K("salade_pates_grecque", "Salade de pâtes à la grecque", "Salade de pâtes", "Europe du Sud › Grèce", "P", 1, 4, 15, 10, "€", "Casserole, saladier.",
  "Pâtes courtes, concombre, tomates, olives, feta et origan dans une vinaigrette citronnée : sans mayonnaise, elle tient au soleil et se prépare la veille.",
  [f"300 g|de pâtes courtes|{PATES}|3", "1|concombre|Concombre|2", "250 g|de tomates cerises|Tomate cerise|2", "150 g|de feta|Feta|2", "60 g|d'olives noires|Olives (vertes / noires)|1", "1|oignon rouge|Oignon rouge|1", f"1 c. à c.|d'origan|Origan frais / sec|1", f"6 c. à s.|d'huile d'olive|{HO}|2", f"1|citron|{CIT}|1"],
  ["**Pâtes.** Cuites 1 min de moins que le paquet, rincées à l'eau froide, huilées.", "**Assembler.** Légumes en dés, olives, oignon émincé fin, feta en cubes.", "**Assaisonner.** Huile, citron, origan, sel, poivre ; au frais. On remue avant de servir (les pâtes boivent la sauce : garde un peu de vinaigrette à part)."],
  tips=[FROID], keep="2 jours au frigo.", age=1, cats=PN + ["vegetarien", "salade", "enfants"], fetes=FETE)

K("taboule_chou_fleur", "Taboulé de chou-fleur cru", "Taboulé de chou-fleur", "Moyen-Orient › Liban", "E", 1, 6, 20, 0, "€", "Râpe ou mixeur.",
  "Le chou-fleur cru râpé en semoule remplace le boulgour : beaucoup de persil et de menthe, tomate, citron, huile d'olive. Croquant, frais, sans gluten, et il ne ramollit pas pendant le trajet.",
  ["1|petit chou-fleur|Chou-fleur|3", f"2 bouquets|de persil plat|{PERSIL}|3", "1 bouquet|de menthe|Menthe|2", f"3|tomates|{TOM}|2", "4|cébettes|Oignon nouveau / cébette|1", f"2|citrons|{CIT}|2", f"8 c. à s.|d'huile d'olive|{HO}|2"],
  ["**Semoule de chou-fleur.** Bouquets râpés gros ou quelques impulsions de mixeur : grains de la taille du boulgour (pas de purée). La tige se râpe aussi.", "**Herbes.** Hachées au couteau (le mixeur les noircit) ; tomates en petits dés épépinés.", "**Assaisonner.** Citron, huile, sel ; 30 min au frais : le chou-fleur s'attendrit."],
  tips=["Les feuilles du chou-fleur : rôties 10 min au four avec un filet d'huile, comme des chips.", FROID], keep="2 jours au frigo.", age=3, cats=PN + ["vegetarien", "salade", "zero_dechet"], fetes=FETE)

K("courgettes_scapece", "Courgettes a scapece (marinées à la menthe)", "Zucchine alla scapece", "Europe du Sud › Italie › Campanie", "A", 1, 4, 20, 120, "€", "Poêle, boîte en verre.",
  "Rondelles de courgettes dorées à l'huile puis marinées dans le vinaigre, l'ail et la menthe : la recette napolitaine qui se garde plusieurs jours et devient meilleure en voyageant.",
  ["4|courgettes|Courgette|3", f"10 cl|d'huile d'olive|{HO}|2", "4 c. à s.|de vinaigre de vin|Vinaigre de vin rouge / blanc|2", f"2 gousses|d'ail|{AIL}|1", "1 bouquet|de menthe|Menthe|2", f"1 pincée|de sel|{SEL}|1"],
  ["**Dorer.** Rondelles de 5 mm, en une couche, 3 min par face : brunes par endroits ; sur papier absorbant, salées.", "**Mariner.** En couches dans la boîte avec ail en lamelles, menthe déchirée et vinaigre ; 2 h au moins.", "**Servir.** À température ambiante, avec du pain."],
  keep="5 jours au frigo dans leur marinade.", age=3, cats=PN + ["vegetarien"], fetes=FETE)

K("brochettes_caprese_melon", "Brochettes tomate-mozzarella-melon", "Spiedini caprese", "Europe du Sud › Italie", "E", 1, 6, 15, 0, "€", "Piques en bois, boîte.",
  "Tomates cerises, billes de mozzarella, melon et basilic sur des piques : l'entrée que les enfants assemblent eux-mêmes et qui se mange sans assiette.",
  ["250 g|de tomates cerises|Tomate cerise|3", "250 g|de billes de mozzarella|Mozzarella / burrata|3", "½|melon|Melon / pastèque|2", "1 bouquet|de basilic|Basilic|1", f"2 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Couper.** Melon en billes (cuillère parisienne) ou en cubes ; tomates entières.", "**Piquer.** Tomate, basilic, mozzarella, melon : les enfants enfilent.", "**Transport.** Dans une boîte au frais ; huile, sel, poivre au moment de manger."],
  tips=["Avant 4 ans : tomates cerises et billes coupées en deux dans la longueur (risque d'étouffement).", FROID], keep="Le jour même.", age=3, cats=PN + ["vegetarien", "enfants"], fetes=FETE)

# ——— Sandwichs et roulés du monde ———
K("club_sandwich_poulet", "Club sandwich au poulet", "Club sandwich", "Amérique du Nord › États-Unis", "P", 1, 4, 20, 0, "€€", "Grille-pain, piques.",
  "Trois étages de pain de mie grillé, poulet, bacon de dinde croustillant, tomate, salade et une sauce yaourt-moutarde : coupé en triangles tenus par une pique.",
  ["12 tranches|de pain de mie|Pain de mie|3", f"300 g|de blanc de poulet cuit|{BLANC_P}|3", "8 tranches|de bacon de dinde|Bacon de dinde / de bœuf|2", f"2|tomates|{TOM}|1", "1|salade|Salade (laitue, batavia)|1", f"8 c. à s.|de yaourt grec|{GREC}|1", f"1 c. à s.|de moutarde|{DIJON}|1"],
  ["**Préparer.** Bacon de dinde doré à sec 2 min ; poulet en tranches ; sauce : yaourt, moutarde, sel, poivre (plus sûre que la mayonnaise en plein air).", "**Monter.** Pain grillé tartiné de sauce, salade, poulet, pain, tomate, bacon, pain.",
   "**Couper.** Quatre piques, coupé en diagonale en 4 triangles ; filmé serré."], tips=[FROID], keep="Le jour même.", age=3, cats=PN + ["enfants"], fetes=FETE)

K("muffuletta_vege", "Muffuletta aux légumes grillés", "Muffuletta", "Amérique du Nord › États-Unis › La Nouvelle-Orléans", "P", 2, 6, 30, 240, "€€", "Poêle-gril, poids (casserole remplie).",
  "Le grand sandwich rond de La Nouvelle-Orléans, pressé plusieurs heures pour que la salade d'olives imbibe la mie. L'original est aux charcuteries ; ici légumes grillés, mozzarella et olivade.",
  ["1|grand pain rond|Pain de campagne / complet|3", "1|aubergine|Aubergine|2", "2|courgettes|Courgette|2", f"2|poivrons grillés|{POIVRON}|2", "250 g|de mozzarella|Mozzarella / burrata|2", "150 g|d'olives vertes et noires|Olives (vertes / noires)|2", "1 c. à s.|de câpres|Câpres|1", f"6 c. à s.|d'huile d'olive|{HO}|2", f"1 c. à c.|d'origan|Origan frais / sec|1"],
  ["**Olivade.** Olives, câpres, ail, origan hachés grossièrement avec l'huile et un trait de vinaigre.", "**Légumes.** Aubergine et courgettes en tranches, grillées 3 min par face.",
   "**Presser.** Pain coupé en deux, un peu évidé ; olivade sur les deux faces, légumes et mozzarella en couches ; refermé, filmé serré, sous un poids 4 h au frais. Coupé en parts comme un gâteau."],
  tips=[FROID], keep="24 h au frigo (il est encore meilleur).", age=3, cats=PN + ["vegetarien"], fetes=FETE)

K("bocadillo_tortilla", "Bocadillo de tortilla (Espagne)", "Bocadillo de tortilla", "Europe du Sud › Espagne", "P", 1, 4, 10, 0, "€", "Couteau.",
  "Le sandwich des pique-niques espagnols : une épaisse tranche de tortilla de pommes de terre froide dans une baguette frottée à la tomate et à l'huile d'olive.",
  ["1|tortilla espagnole cuite (la veille)|SUB:tortilla_espanola|3", "2|baguettes|Baguette tradition|3", f"2|tomates mûres|{TOM}|2", f"4 c. à s.|d'huile d'olive|{HO}|1", f"1 gousse|d'ail|{AIL}|1"],
  ["**Pain.** Baguettes coupées en deux puis ouvertes ; frottées d'ail et de tomate coupée en deux (pan con tomate), huile, sel.", "**Garnir.** Une tranche de tortilla froide de 2 cm.", "**Emballer.** Dans du papier ou un torchon à sandwich : la tomate imbibe la mie pendant le trajet."],
  tips=[FROID], keep="Le jour même.", age=1, cats=PN + ["vegetarien", "enfants"], fetes=FETE, zw=["tortilla de la veille"])

K("pinwheels_tortilla", "Roulés de tortilla (pinwheels)", "Pinwheels", "Amérique du Nord › États-Unis", "E", 1, 4, 15, 30, "€", "Film, couteau.",
  "Des tortillas tartinées de fromage frais, garnies d'épinards, de carotte râpée et de dinde, roulées serré puis coupées en spirales : les bouchées préférées des enfants.",
  ["4|grandes tortillas de blé|Tortillas de blé|3", "200 g|de fromage frais|Fromage à tartiner / fondu|3", "60 g|de jeunes pousses d'épinards|Épinard|1", f"2|carottes râpées|{CAROTTE}|1", "6 tranches|de jambon de dinde (ou rien)|Jambon de dinde / de poulet|1?"],
  ["**Tartiner.** Fromage frais jusqu'aux bords (c'est la colle).", "**Garnir et rouler.** Épinards, carotte, dinde ; roulé serré, filmé, 30 min au frais.", "**Couper.** Tranches de 2 cm au couteau-scie : spirales nettes."],
  tips=[FROID], keep="Le jour même.", age=1, cats=PN + ["enfants"], fetes=FETE + ["Anniversaire"])

K("pizza_scrolls", "Pizza scrolls (roulés à la pizza, Australie)", "Pizza scrolls", "Océanie › Australie", "G", 1, 12, 20, 20, "€", "Plaque, four.",
  "La pâte à pizza tartinée de sauce tomate et de fromage, roulée et coupée en escargots : les « scrolls » des boîtes à goûter australiennes, bons froids.",
  ["1|pâte à pizza|Pâte à pizza (prête)|3", f"150 g|de sauce tomate|Sauce tomate (bocal)|2", f"150 g|de fromage râpé|{GRUY}|2", "100 g|de légumes en petits dés (poivron, maïs, épinards)|Maïs doux|1?", f"1 c. à c.|d'origan|Origan frais / sec|1"],
  ["**Tartiner.** Pâte étalée en rectangle, sauce (pas trop : elle coule), fromage, légumes, origan.", "**Rouler et couper.** Roulé par le grand côté, tranches de 3 cm, posées à plat sur la plaque.", "**Cuire.** 200 °C, 18-20 min : dorés. Refroidis sur grille avant la boîte."],
  keep="2 jours au frigo ; se congèlent 2 mois.", age=1, cats=PN + ["enfants", "vegetarien"], fetes=FETE + ["Anniversaire"], zw=["fonds de légumes"])

K("onigirazu", "Onigirazu (sandwich de riz en nori)", "Onigirazu", "Asie de l'Est › Japon", "P", 2, 4, 25, 15, "€€", "Film, couteau mouillé.",
  "Le sandwich japonais sans pain : riz, garniture et riz, pliés dans une feuille de nori comme une enveloppe, puis coupés en deux pour montrer les couches. Thon, omelette, concombre.",
  ["300 g|de riz rond cuit|Riz rond / sushi|3", "4|feuilles de nori|Algue nori|3", "140 g|de thon en conserve|Thon en conserve|2", f"2|œufs (omelette fine)|{OEUF}|2", "½|concombre|Concombre|1", f"1 c. à s.|de sauce soja|{SOJA}|1", "1 c. à s.|de vinaigre de riz|Vinaigre de riz|1"],
  ["**Riz.** Assaisonné de vinaigre de riz et d'une pincée de sel ; tiède.", "**Monter.** Nori posée en losange sur un film ; un carré de riz au centre, thon au soja, omelette, concombre, un carré de riz.",
   "**Plier et couper.** Les quatre coins de la nori rabattus, film serré, 5 min de repos ; coupé en deux au couteau mouillé."],
  tips=[FROID], keep="Le jour même, au frais (le riz durcit au frigo : sors-le 20 min avant).", age=3, cats=PN + ["enfants"], fetes=FETE)

K("ajitama", "Œufs marinés au soja (ajitama)", "Ajitsuke tamago", "Asie de l'Est › Japon", "E", 1, 6, 15, 360, "€", "Casserole, sac congélation.",
  "Œufs mollets écalés puis marinés une nuit dans le soja et le mirin : blanc ambré, jaune fondant. L'œuf dur du pique-nique, en mieux.",
  [f"6|œufs|{OEUF}|3", f"6 c. à s.|de sauce soja|{SOJA}|2", "4 c. à s.|de mirin|Mirin|2", f"1 c. à s.|de sucre|{SUCRE}|1", "10 cl|d'eau|-|1"],
  ["**Cuire.** Œufs sortis du frigo, eau bouillante, 6 min 30 ; eau glacée 5 min ; écalés sous l'eau.", "**Mariner.** Soja, mirin, sucre, eau ; œufs dans un sac ou un bocal, 6 h à une nuit.", "**Servir.** Coupés en deux au fil ou au couteau mouillé."],
  tips=["Pour les jeunes enfants et les femmes enceintes : 9 min de cuisson (jaune pris).", FROID], keep="3 jours au frigo dans la marinade.", age=3, cats=PN, fetes=FETE, var=[VSAKE])

K("brochettes_poulet_tandoori_froid", "Brochettes de poulet tandoori (froides)", "Chicken tikka skewers", "Asie du Sud › Inde", "P", 1, 6, 20, 15, "€€", "Piques, four (gril).",
  "Poulet mariné au yaourt et aux épices, grillé la veille puis servi froid avec une raïta : il reste moelleux grâce au yaourt.",
  [f"800 g|de blancs ou hauts de cuisse|{CUISSE}|3", "6 c. à s.|de marinade tandoori|SUB:marinade_tandoori|3", f"1|citron vert|{CITV}|1", "1|pot de raïta (pour tremper)|SUB:raita|1?"],
  ["**Mariner.** Cubes de poulet dans la marinade, 4 h ou une nuit.", "**Griller.** Sur piques, sous le gril, 12 min en tournant : bords dorés, 74 °C à cœur.", "**Refroidir vite.** Au frigo dans l'heure ; citron vert au départ."],
  tips=[FROID], keep="2 jours au frigo.", age=3, cats=PN, fetes=FETE + ["Barbecue d'été"], profil=["epice"])

K("cornish_pasty", "Cornish pasty (chausson de Cornouailles)", "Cornish pasty", "Europe du Nord › Royaume-Uni › Cornouailles", "P", 2, 6, 40, 50, "€€", "Rouleau, plaque, four.",
  "Le chausson des mineurs de Cornouailles : bœuf, pomme de terre, rutabaga et oignon, crus, en dés, cuits dans une pâte épaisse fermée par une torsade. Un repas complet qui tient dans la main.",
  [f"500 g|de farine|{F55}|3", f"250 g|de beurre froid|{BEURRE}|2", "500 g|de bœuf (paleron ou rumsteck) en petits dés|Paleron|3", f"2|pommes de terre|{PDT}|2", "200 g|de rutabaga ou navet|Panais / rutabaga|1", f"1|oignon|{OIG}|1", f"1|œuf (dorure)|{OEUF}|1"],
  ["**Pâte.** Farine, beurre en dés sablés du bout des doigts, sel, 15 cl d'eau froide ; 30 min au frais.", "**Farce crue.** Légumes et bœuf en dés de 1 cm, sel, beaucoup de poivre.",
   "**Former.** 6 disques de 20 cm ; farce au centre, pâte relevée et pincée en torsade sur le dessus ; dorés, une petite entaille.", "**Cuire.** 200 °C 15 min puis 170 °C 35 min : la vapeur cuit la farce. Froids ou tièdes."],
  tips=[FROID], keep="2 jours au frigo ; se congèlent cuits 2 mois.", age=3, cats=PN + ["enfants"], fetes=FETE)

K("scotch_eggs_volaille", "Scotch eggs (version volaille)", "Scotch eggs", "Europe du Nord › Royaume-Uni", "E", 2, 6, 40, 15, "€€", "Casserole profonde, thermomètre (ou four).",
  "L'œuf mollet enrobé de chair à saucisse puis pané et frit, star des pique-niques anglais. Selon D21 : chair de saucisse de volaille aux herbes.",
  [f"7|œufs|{OEUF}|3", "450 g|de chair de saucisses de volaille|Saucisse de bœuf / de veau / de volaille|3", "1 c. à s.|de sauge ou thym|Sauge|1", f"50 g|de farine|{F55}|1", "100 g|de chapelure ou panko|Chapelure|2", "1 l|d'huile de friture (ou four)|Huile d'arachide|1"],
  ["**Œufs.** 6 œufs, 6 min 30 à l'eau bouillante, eau glacée, écalés.", "**Enrober.** Chair aux herbes en 6 galettes ; œuf fariné au centre, enveloppé sans trou ; farine, œuf battu, chapelure.",
   "**Cuire.** 165 °C, 7-8 min (viande cuite à cœur, jaune encore tendre), ou four 200 °C 25 min huilés. Refroidis sur grille, coupés en deux."],
  tips=["Avec de jeunes enfants : œufs 9 min (jaune pris).", FROID], keep="2 jours au frigo.", age=3, cats=PN, fetes=FETE, tech=["frire en sécurité"])

# ——— Douceurs qui voyagent (et anti-gaspi) ———
K("flapjacks", "Flapjacks (barres d'avoine au miel)", "Flapjacks", "Europe du Nord › Royaume-Uni", "G", 1, 16, 10, 25, "€", "Moule carré, casserole.",
  "Flocons d'avoine, beurre, sucre roux et miel cuits en plaque : des barres moelleuses et dorées qui ne craignent pas le transport.",
  ["250 g|de flocons d'avoine|Flocons d'avoine (porridge)|3", f"125 g|de beurre|{BEURRE}|2", "100 g|de sucre roux|Sucre blanc / roux / cassonade / vergeoise|2", f"4 c. à s.|de miel ou sirop d'érable|{MIEL}|2", "50 g|de raisins secs ou fruits secs|Raisins secs|1?"],
  ["**Fondre.** Beurre, sucre, miel, une pincée de sel, à feu doux.", "**Mélanger.** Avec l'avoine et les fruits secs ; tassé dans le moule chemisé.", "**Cuire.** 180 °C, 20-25 min : doré sur les bords, encore souple au centre ; découpé tiède, démoulé froid."],
  keep="1 semaine dans une boîte en métal.", age=1, cats=PN + ["enfants"], fetes=FETE, profil=["sucre"])

K("energy_balls_dattes", "Boules d'énergie dattes-avoine-cacao", "Energy balls", "Amérique du Nord › États-Unis", "G", 1, 20, 15, 30, "€", "Mixeur.",
  "Dattes, flocons d'avoine, cacao et une purée de noix mixés, roulés en boules : un goûter sans cuisson et sans sucre ajouté, à faire avec les enfants.",
  ["250 g|de dattes dénoyautées|Datte (medjool, deglet)|3", "100 g|de flocons d'avoine|Flocons d'avoine (porridge)|2", "2 c. à s.|de cacao|Cacao en poudre non sucré|2", "3 c. à s.|de beurre de cacahuète (ou purée d'amande)|Beurre de cacahuète|2", "3 c. à s.|de noix de coco râpée|Noix de coco râpée|1?"],
  ["**Mixer.** Dattes (trempées 10 min si elles sont sèches), avoine, cacao, beurre de cacahuète : pâte qui colle quand on la presse.", "**Rouler.** Boules de la taille d'une noix, roulées dans la coco.", "**Raffermir.** 30 min au frais."],
  tips=["Allergie à l'arachide : purée d'amande ou de graines de tournesol.", "Avant 4 ans : les servir aplaties en galettes plutôt qu'en boules."], keep="1 semaine au frigo.", age=3, cats=PN + ["enfants", "vegetarien"], fetes=FETE)

K("barres_cereales_maison", "Barres de céréales du fond du placard", "Barres de céréales", "France", "G", 1, 12, 15, 25, "€", "Moule carré.",
  "Les fonds de paquets (flocons, céréales, fruits secs, graines, chocolat) liés au miel et au beurre de cacahuète : des barres moins sucrées que celles du commerce, sans emballage individuel.",
  ["200 g|de flocons d'avoine et fonds de céréales|Flocons d'avoine (porridge)|3", "100 g|de fruits secs en morceaux|Abricots secs|2", "50 g|de graines (courge, tournesol)|Graines de tournesol / courge|1", f"5 c. à s.|de miel|{MIEL}|2", "3 c. à s.|de beurre de cacahuète|Beurre de cacahuète|2", "40 g|de chocolat noir|Chocolat noir|1?"],
  ["**Lier.** Miel et beurre de cacahuète chauffés ensemble, versés sur les secs.", "**Tasser.** Fort, dans le moule chemisé (c'est ce qui les fait tenir).", "**Cuire.** 170 °C, 20 min ; refroidies complètement avant de couper."],
  tips=["Allergie à l'arachide : purée d'amande ou de sésame."], keep="1 semaine dans une boîte.", age=3, cats=PN + ["enfants", "zero_dechet"], fetes=FETE, zw=["fonds de paquets de céréales"])

K("crackers_pain_rassis", "Crackers de pain rassis aux herbes", "Crackers maison", "France", "A", 1, 6, 10, 15, "€", "Plaque, four.",
  "Le pain dur coupé très fin, huilé, assaisonné et séché au four : des crackers pour les tartinades du pique-nique (houmous, tzatziki), sans rien jeter.",
  ["½|baguette ou pain rassis|Pain rassis (réservé)|3", f"4 c. à s.|d'huile d'olive|{HO}|2", "1 c. à c.|de zaatar ou herbes de Provence|Herbes de Provence|1", f"1 pincée|de sel|{SEL}|1"],
  ["**Trancher.** Le plus fin possible (pain dur : couteau-scie).", "**Assaisonner.** Huile au pinceau, herbes, sel.", "**Sécher.** 160 °C, 12-15 min : dorés et cassants ; refroidis dans le four entrouvert."],
  keep="2 semaines dans une boîte en métal.", age=1, cats=PN + ["zero_dechet", "enfants", "vegetarien"], fetes=FETE, zw=["pain rassis"])

K("eau_infusee_epluchures", "Eau infusée concombre, agrumes et menthe", "Eau aromatisée", "France", "B", 1, 6, 5, 120, "€", "Grande bouteille ou carafe.",
  "La boisson du pique-nique sans sucre ni bouteille jetable : de l'eau fraîche parfumée aux épluchures d'agrumes, aux fins de concombre et aux tiges de menthe qu'on allait jeter.",
  ["1,5 l|d'eau|-|3", "½|concombre (ou ses extrémités)|Concombre|2", f"1|citron (zestes et rondelles)|{CIT}|2", "1|orange (zestes)|Orange|1", "1 bouquet|de menthe (tiges comprises)|Menthe|1"],
  ["**Parfumer.** Concombre en rondelles, zestes d'agrumes bio prélevés en rubans, menthe froissée.", "**Infuser.** Eau froide par-dessus, 2 h au frais (pas plus de 12 h : l'amertume vient).", "**Emporter.** Dans une gourde ou une bouteille en verre, au frais."],
  keep="24 h au frigo.", age=1, cats=PN + ["boissons", "zero_dechet", "enfants"], fetes=FETE, zw=["épluchures d'agrumes", "tiges d'herbes"])
