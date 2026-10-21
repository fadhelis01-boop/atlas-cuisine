# -*- coding: utf-8 -*-
"""Vague 3 · Plats express (20 min au plus, du placard au plat) : réponse à l'audit UX du 16/10/2026
(« 2 plats en 15 min, 40 en 30 min »). Ingrédients de supermarché, une poêle ou une casserole. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

QF = "France › Cuisine du quotidien"; IT = "Europe du Sud › Italie"; CN = "Asie de l'Est › Chine"; JP = "Asie de l'Est › Japon"
MX = "Amérique latine › Mexique"; TH = "Asie du Sud-Est › Thaïlande"; VN = "Asie du Sud-Est › Vietnam"; GR = "Europe du Sud › Grèce"
IN = "Asie du Sud › Inde"; LB = "Moyen-Orient › Liban"; MA = "Afrique du Nord › Maroc"; US = "Amérique du Nord › États-Unis"; PT = "Europe du Sud › Portugal"
EX = ["express"]

K("pates_citron_parmesan", "Pâtes au citron et parmesan", "Pasta al limone", IT, "P", 1, 4, 5, 10, "€", "Casserole, râpe.",
  "Zeste et jus de citron, beurre, parmesan et l'eau de cuisson qui fait la sauce : 15 minutes, et c'est d'une fraîcheur étonnante.",
  [f"400 g|de spaghetti|{PATES}|3", f"2|citrons non traités|{CIT}|3", f"40 g|de beurre|{BEURRE}|2", f"80 g|de parmesan râpé|{PARM}|2", f"1 pincée|de poivre|{POIVRE}|0", f"1 c. à s.|de persil (facultatif)|{PERSIL}|1?"],
  ["**Cuire.** Pâtes dans une grande casserole d'eau salée (10 g de sel par litre), 1 min de moins que le paquet ; garde un verre d'eau de cuisson.",
   "**Sauce.** Dans la casserole égouttée, hors du feu : beurre, zeste et jus des citrons, parmesan, 1/2 verre d'eau de cuisson ; remue vivement : la sauce devient crémeuse et nappe les pâtes.",
   "**Servir.** Poivre, persil ; ajoute un peu d'eau de cuisson si ça sèche."],
  age=1, cats=EX + ["enfants"], profil=["acide"], tech=["cuire les pâtes"], tips=["Le secret : l'amidon de l'eau de cuisson lie le beurre et le fromage, comme une crème sans crème."])

K("pates_thon_tomate", "Pâtes au thon, tomate et câpres", "Pâtes au thon", QF, "P", 1, 4, 5, 12, "€", "Casserole, poêle.",
  "Le grand classique du placard : sauce tomate express au thon, ail et câpres. Tout s'achète en conserve.",
  [f"400 g|de pâtes courtes|{PATES}|3", f"2 boîtes (280 g)|de thon au naturel|Thon en conserve|3", f"400 g|de tomates pelées|{PELEES}|3", f"2 gousses|d'ail|{AIL}|1", "1 c. à s.|de câpres|Câpres|1?", f"2 c. à s.|d'huile d'olive|{HO}|1", f"1 pincée|d'origan|Origan frais / sec|0"],
  ["**Cuire.** Pâtes à l'eau bouillante salée.", "**Sauce.** Ail émincé 1 min dans l'huile (il blondit à peine), tomates écrasées, origan ; 8 min à frémissement.",
   "**Finir.** Thon émietté et câpres, 1 min ; mélange avec les pâtes égouttées."],
  age=1, cats=EX + ["enfants"], tech=["cuire les pâtes"])

K("orecchiette_brocoli_ail", "Pâtes au brocoli, ail et piment", "Orecchiette con cime di rapa", f"{IT} › Pouilles", "P", 1, 4, 5, 12, "€", "Grande casserole, poêle.",
  "Le brocoli cuit avec les pâtes dans la même eau, puis sauté à l'ail et au piment : un plat des Pouilles, végétarien et vert.",
  [f"400 g|de pâtes (orecchiette, penne)|{PATES}|3", "1|gros brocoli|Brocoli|3", f"3 gousses|d'ail|{AIL}|2", f"1 pincée|de piment|Flocons de piment|1", f"4 c. à s.|d'huile d'olive|{HO}|2", f"40 g|de parmesan|{PARM}|1?"],
  ["**Cuire ensemble.** Brocoli en petits bouquets dans l'eau salée des pâtes, 5 min avant la fin de leur cuisson.",
   "**Sauter.** Ail émincé et piment dans l'huile, 1 min ; ajoute pâtes et brocoli égouttés, une louche d'eau de cuisson ; écrase un peu le brocoli : il fait la sauce.",
   "**Servir.** Parmesan ou chapelure dorée."], age=3, cats=EX, profil=["epice", "leger"])

K("nouilles_sautees_legumes_oeuf", "Nouilles sautées aux légumes et à l'œuf", "Chǎo miàn", CN, "P", 1, 2, 10, 8, "€", "Wok ou grande poêle.",
  "Nouilles, chou, carotte, œuf brouillé et sauce soja : le plat sauté du soir, prêt avant que l'eau du thé ne bouille.",
  ["200 g|de nouilles aux œufs|Nouilles chinoises aux œufs|3", f"2|œufs|{OEUF}|2", f"1|carotte|{CAROTTE}|1", "¼|chou chinois|Chou chinois / pak-choï|2", f"2|cébettes|Oignon nouveau / cébette|1", f"3 c. à s.|de sauce soja|{SOJA}|2", "1 c. à c.|d'huile de sésame|Huile de sésame (grillée)|1?", f"1 c. à s.|d'huile neutre|{HN}|1"],
  ["**Préparer.** Nouilles cuites 3 min, rincées à l'eau froide ; légumes en fines lanières.",
   "**Sauter.** Wok très chaud : œufs brouillés 30 s, réservés ; légumes 2 min, ils restent croquants.",
   "**Finir.** Nouilles, sauce soja, œufs, 1 min en remuant ; huile de sésame, cébette."], age=3, cats=EX, tech=["wok"])

K("riz_saute_oeuf_express", "Riz sauté à l'œuf et aux petits pois", "Dàn chǎofàn", CN, "P", 1, 2, 5, 8, "€", "Wok ou poêle.",
  "Le meilleur usage du riz de la veille : œuf, petits pois, cébette, sauce soja. Le riz froid se sépare et grille sans coller.",
  [f"400 g|de riz cuit froid|{RIZ}|3", f"3|œufs|{OEUF}|3", "100 g|de petits pois surgelés|Petits pois / pois gourmands|2", f"2|cébettes|Oignon nouveau / cébette|1", f"2 c. à s.|de sauce soja|{SOJA}|2", f"1 c. à s.|d'huile neutre|{HN}|1"],
  ["**Œufs.** Battus, versés dans l'huile très chaude, brouillés grossièrement 30 s.",
   "**Riz.** Ajoute riz et petits pois ; écrase les mottes, saute 4 min : les grains se séparent et grésillent.",
   "**Assaisonner.** Sauce soja en filet sur le bord du wok, cébette ; goûte."], age=1, cats=EX + ["enfants", "zero_dechet"], tech=["wok"],
  tips=["Riz cuit et refroidi au frigo (24 h au plus) : jamais laissé à température ambiante."])

K("omelette_legumes_feta", "Omelette courgette, menthe et feta", "Omeléta", GR, "P", 1, 2, 8, 6, "€", "Poêle 24 cm.",
  "Courgette râpée revenue, œufs battus, feta et menthe : grecque, légère et prête en 12 minutes.",
  [f"5|œufs|{OEUF}|3", "1|courgette|Courgette|2", "80 g|de feta|Feta|2", "4 feuilles|de menthe|Menthe|1", f"1 c. à s.|d'huile d'olive|{HO}|1", f"1 pincée|de poivre|{POIVRE}|0"],
  ["**Courgette.** Râpée, pressée dans les mains, revenue 3 min : elle ne rend plus d'eau.",
   "**Cuire.** Œufs battus sur la courgette, feu moyen ; ramène les bords vers le centre 2 min ; feta émiettée.",
   "**Plier.** Quand le dessus est encore baveux, plie et glisse sur l'assiette ; menthe."], age=1, cats=EX, profil=["leger"], tech=["omelette baveuse"])

K("oeufs_brouilles_saumon_toast", "Toasts aux œufs brouillés et saumon fumé", "Scrambled eggs & smoked salmon", QF, "P", 1, 2, 10, 0, "€€", "Casserole, grille-pain.",
  "Œufs brouillés crémeux sur pain grillé, saumon fumé et ciboulette : un dîner chic en 10 minutes.",
  [f"4|œufs|{OEUF}|3", "100 g|de saumon fumé|Saumon fumé|2", "2 tranches|de pain de campagne|Pain de campagne / complet|2", f"15 g|de beurre|{BEURRE}|1", "1 c. à s.|de ciboulette|Ciboulette|1", f"1 c. à s.|de crème fraîche|{CF}|1?"],
  ["**Brouiller.** Œufs battus, beurre, feu doux ; remue sans arrêt à la spatule 4-5 min : de petits grumeaux crémeux se forment.",
   "**Arrêter.** Retire du feu quand c'est encore brillant ; crème : la chaleur finit la cuisson.",
   "**Dresser.** Sur le pain grillé, saumon, ciboulette, poivre."], age=3, cats=EX, tech=["œufs brouillés"])

K("quesadillas_haricots_fromage", "Quesadillas haricots noirs et cheddar", "Quesadillas de frijoles", MX, "P", 1, 4, 10, 8, "€", "Poêle.",
  "Tortillas pliées sur des haricots écrasés au cumin et du fromage fondant, dorées à la poêle : croustillantes dehors, filantes dedans.",
  ["8|tortillas de blé|Tortillas de blé|3", "400 g|de haricots noirs (boîte)|Haricots rouges / noirs|3", "150 g|de cheddar râpé|Cheddar|2", f"1 c. à c.|de cumin|{CUMIN}|1", "½|oignon rouge|Oignon rouge|1", f"1 c. à s.|de coriandre|{CORI}|1?", "4 c. à s.|de salsa|Salsa du commerce|1?"],
  ["**Garniture.** Haricots rincés, écrasés à la fourchette avec cumin, sel, oignon haché.",
   "**Garnir.** Sur une moitié de tortilla : haricots, fromage ; plie.",
   "**Dorer.** Poêle sèche, feu moyen, 2 min par face : dorée, le fromage fond."], age=3, cats=EX + ["enfants"], tech=[])

K("wrap_poulet_croquant", "Wraps au poulet, crudités et sauce yaourt", "Chicken wrap", US, "P", 1, 4, 15, 6, "€", "Poêle.",
  "Lanières de poulet saisies au paprika, salade, tomate, carotte et sauce yaourt-citron, roulées dans une tortilla : le déjeuner à emporter.",
  ["4|tortillas de blé|Tortillas de blé|3", f"2|blancs de poulet|{BLANC_P}|3", f"1 c. à c.|de paprika|{PAPRIKA}|1", "4 feuilles|de salade|Salade (laitue, batavia)|1", f"1|tomate|{TOM}|1", f"1|carotte râpée|{CAROTTE}|1", f"4 c. à s.|de yaourt grec|{GREC}|2", f"½|citron|{CIT}|1"],
  ["**Saisir.** Poulet en lanières, paprika, sel ; poêle chaude 5-6 min : doré, jus clair quand on le coupe.",
   "**Sauce.** Yaourt, jus de citron, sel, poivre.", "**Rouler.** Tortilla tiédie 10 s, sauce, salade, crudités, poulet ; replie les côtés puis roule serré."],
  age=3, cats=EX + ["enfants"])

K("wrap_houmous_legumes", "Wraps houmous, légumes croquants et feta", "Wrap végétarien", LB, "P", 1, 2, 10, 0, "€", "Planche.",
  "Houmous, concombre, carotte, poivron, feta et menthe dans un pain plat : végétarien, sans cuisson, en 10 minutes.",
  ["2|tortillas ou pains plats|Tortillas de blé|3", "4 c. à s.|d'houmous|Houmous|3", "½|concombre|Concombre|1", f"1|carotte|{CAROTTE}|1", f"½|poivron|{POIVRON}|1", "60 g|de feta|Feta|1", "4 feuilles|de menthe|Menthe|1?"],
  ["**Tailler.** Légumes en bâtonnets fins.", "**Garnir.** Houmous étalé, légumes, feta émiettée, menthe ; sel, poivre.", "**Rouler.** Serré, coupé en deux en biais."],
  age=3, cats=EX, profil=["leger"])

K("tartines_avocat_oeuf", "Tartines avocat, œuf mollet et piment", "Avocado toast", QF, "P", 1, 2, 5, 6, "€€", "Casserole, grille-pain.",
  "Pain grillé, avocat écrasé au citron vert, œuf mollet qui coule et une pincée de piment : un repas complet en 11 minutes.",
  ["2 tranches|de pain de campagne|Pain de campagne / complet|2", "1|avocat mûr|Avocat|3", f"2|œufs|{OEUF}|3", f"½|citron vert|{CITV}|1", f"1 pincée|de piment|Flocons de piment|1?", "1 c. à c.|de graines de sésame|Sésame (blanc/noir)|0"],
  ["**Œufs.** 6 min dans l'eau bouillante, puis 1 min à l'eau froide ; écale doucement.", "**Avocat.** Écrasé avec citron vert, sel.",
   "**Dresser.** Pain grillé, avocat, œuf ouvert en deux (le jaune coule), piment, sésame."], age=3, cats=EX, profil=["gras"], tech=["œuf mollet"])

K("saumon_poele_haricots_citron", "Pavé de saumon poêlé, haricots verts au citron", "Saumon poêlé", QF, "P", 1, 2, 8, 10, "€€", "Poêle, casserole.",
  "Saumon cuit côté peau jusqu'à ce qu'elle croustille, haricots verts au beurre citronné : le dîner équilibré qui fait plaisir.",
  [f"2|pavés de saumon avec peau|Saumon (frais, pavé)|3", "300 g|de haricots verts (surgelés extra-fins)|Haricots verts|3", f"20 g|de beurre|{BEURRE}|1", f"1|citron|{CIT}|2", f"1 c. à s.|d'huile|{HN}|1", "1 c. à s.|d'aneth (facultatif)|Aneth|1?"],
  ["**Haricots.** 6-7 min à l'eau bouillante salée : ils restent légèrement croquants ; égouttés, beurre, zeste de citron.",
   "**Saumon.** Côté peau dans la poêle chaude huilée, 5 min sans y toucher : la chair devient opaque aux deux tiers ; retourne 1 min.",
   "**Servir.** Jus de citron, fleur de sel, aneth."], age=1, cats=EX, profil=["poisson", "leger"], tech=["cuire côté peau"])

K("crevettes_coco_citron_vert", "Crevettes sautées coco-citron vert", "Kung phat kati", TH, "P", 1, 2, 10, 8, "€€", "Poêle ou wok, casserole (riz).",
  "Crevettes saisies, lait de coco, citron vert, ail et coriandre : une sauce parfumée à servir sur du riz, en 18 minutes avec la cuisson du riz.",
  ["300 g|de crevettes crues décortiquées|Crevettes (cuites/crues)|3", "20 cl|de lait de coco|Lait de coco / crème de coco|3", f"1|citron vert|{CITV}|2", f"2 gousses|d'ail|{AIL}|1", f"1 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|1", f"½ bouquet|de coriandre|{CORI}|1", f"150 g|de riz|{RIZ}|2"],
  ["**Riz.** Cuit à l'avance ou en même temps (12 min).", "**Crevettes.** Saisies 1 min par face dans l'huile chaude avec l'ail : elles deviennent roses et se recourbent ; réservées.",
   "**Sauce.** Lait de coco, sauce de poisson, 3 min à frémissement ; crevettes, zeste et jus de citron vert, coriandre."],
  age=3, cats=EX, profil=["poisson"], sa=["Eau pétillante au citron vert"])

K("poulet_minute_moutarde", "Émincé de poulet à la moutarde", "Poulet à la moutarde", QF, "P", 1, 4, 8, 12, "€", "Sauteuse.",
  "Lanières de poulet dorées, crème et moutarde à l'ancienne : la sauce du dimanche en 20 minutes, avec des pâtes ou du riz.",
  [f"4|blancs de poulet|{BLANC_P}|3", f"20 cl|de crème|{CF}|2", "2 c. à s.|de moutarde à l'ancienne|Moutarde à l'ancienne|2", f"1|échalote|{ECH}|1", f"10 g|de beurre|{BEURRE}|1", f"1 c. à s.|de persil|{PERSIL}|0"],
  ["**Dorer.** Poulet en lanières, sel, poivre ; sauteuse chaude, beurre ; 5 min : doré sur toutes les faces.",
   "**Sauce.** Échalote hachée 1 min ; crème et moutarde ; 4 min à frémissement : la sauce nappe la cuillère.",
   "**Goûter.** Sel, poivre ; persil."], age=1, cats=EX + ["enfants"], tech=["saisir", "réduire"])

K("escalopes_dinde_champignons", "Escalopes de dinde à la crème et aux champignons", "Escalope à la crème", QF, "P", 1, 4, 8, 12, "€", "Poêle.",
  "Escalopes dorées, champignons poêlés, crème : simple, tendre et très familial.",
  ["4|escalopes de dinde|Dinde (escalope, cuisse, filet)|3", "250 g|de champignons de Paris|Champignon de Paris|2", f"20 cl|de crème|{CF}|2", f"1|échalote|{ECH}|1", f"15 g|de beurre|{BEURRE}|1", f"1 c. à s.|de farine|{F55}|1"],
  ["**Saisir.** Escalopes farinées légèrement, 3 min par face au beurre : dorées ; réservées au chaud.",
   "**Champignons.** Émincés, échalote, 5 min : ils rendent leur eau puis dorent.",
   "**Sauce.** Crème, 2 min ; remets les escalopes 1 min ; goûte."], age=1, cats=EX + ["enfants"], tech=["saisir"])

K("curry_pois_chiches_express", "Curry de pois chiches express", "Chana masala rapide", IN, "P", 1, 4, 10, 10, "€", "Sauteuse, casserole (riz).",
  "Oignon, ail, gingembre, épices, tomates et pois chiches en boîte : un curry végétarien plein de goût en 20 minutes.",
  [f"2 boîtes (530 g égouttés)|de pois chiches|{POIS}|3", f"400 g|de tomates pelées|{PELEES}|2", f"1|oignon|{OIG}|2", f"2 gousses|d'ail|{AIL}|1", "1 morceau (2 cm)|de gingembre|Gingembre frais|1", "2 c. à c.|de garam masala|Garam masala|2", f"1 c. à c.|de cumin|{CUMIN}|1", "10 cl|de lait de coco|Lait de coco / crème de coco|1?", f"½ bouquet|de coriandre|{CORI}|1?"],
  ["**Base.** Oignon haché 5 min à l'huile : il blondit ; ail, gingembre râpé, épices 1 min : ça sent très bon.",
   "**Mijoter.** Tomates, pois chiches rincés, 10 min à frémissement ; écrase quelques pois chiches pour épaissir.",
   "**Finir.** Lait de coco, sel, coriandre ; avec du riz ou du pain naan."], age=3, cats=EX, profil=["epice"], tech=["torréfier les épices"])

K("udon_sautees_legumes", "Udon sautées aux légumes et sauce soja-miel", "Yaki udon végétarien", JP, "P", 1, 2, 10, 8, "€", "Wok ou poêle.",
  "Nouilles épaisses et moelleuses, champignons, chou, carotte, sauce soja-miel : végétarien, réconfortant, très rapide.",
  ["400 g|de nouilles udon (précuites)|Nouilles udon|3", "150 g|de champignons|Champignon de Paris|2", "¼|chou chinois|Chou chinois / pak-choï|2", f"1|carotte|{CAROTTE}|1", f"3 c. à s.|de sauce soja|{SOJA}|2", f"1 c. à c.|de miel|{MIEL}|1", f"1 c. à s.|d'huile neutre|{HN}|1", "1 c. à c.|de sésame|Sésame (blanc/noir)|0"],
  ["**Légumes.** En lanières, sautés 3 min à feu vif.", "**Nouilles.** Passées 1 min sous l'eau chaude, ajoutées avec soja et miel ; 2 min en remuant : la sauce les enrobe et brille.",
   "**Servir.** Sésame."], age=3, cats=EX, tech=["wok"])

K("gnocchi_poeles_tomates_cerises", "Gnocchi poêlés, tomates cerises et basilic", "Gnocchi in padella", IT, "P", 1, 2, 5, 12, "€", "Poêle.",
  "Gnocchi dorés directement à la poêle, sans les bouillir, avec tomates cerises éclatées et mozzarella : croustillants et fondants.",
  ["500 g|de gnocchi|Gnocchi|3", "250 g|de tomates cerises|Tomate cerise|2", "1 boule|de mozzarella|Mozzarella / burrata|2", f"2 c. à s.|d'huile d'olive|{HO}|1", f"1 gousse|d'ail|{AIL}|1", "6 feuilles|de basilic|Basilic|1"],
  ["**Dorer.** Gnocchi dans l'huile chaude, 6-7 min en remuant de temps en temps : dorés et croustillants.",
   "**Tomates.** Ail, tomates cerises, 4 min : elles éclatent et font une petite sauce.",
   "**Finir.** Mozzarella en morceaux, basilic, poivre ; sers tout de suite."], age=1, cats=EX + ["enfants"])

K("pates_epinards_chevre", "Pâtes crémeuses aux épinards et au chèvre", "Pâtes épinards-chèvre", QF, "P", 1, 4, 5, 12, "€", "Casserole.",
  "Épinards qui tombent dans les pâtes chaudes, chèvre frais fondu et noix : végétarien, doux et prêt en un quart d'heure.",
  [f"400 g|de pâtes|{PATES}|3", "200 g|de jeunes pousses d'épinard|Épinard|2", "150 g|de chèvre frais|Chèvre (frais, bûche)|2", "40 g|de noix|Noix|1?", f"1 gousse|d'ail|{AIL}|1", f"1 pincée|de muscade|{MUSC}|0"],
  ["**Cuire.** Pâtes à l'eau salée ; garde un verre d'eau de cuisson.", "**Épinards.** Dans la casserole égouttée, avec l'ail râpé : ils tombent en 1 min.",
   "**Lier.** Pâtes, chèvre, eau de cuisson, muscade ; remue : crémeux ; noix concassées."], age=1, cats=EX)

K("soupe_tomate_express", "Soupe de tomate rôtie express", "Soupe de tomate", QF, "So", 1, 4, 5, 15, "€", "Casserole, mixeur.",
  "Tomates pelées, oignon, ail, un peu de sucre et de crème : une soupe veloutée en 20 minutes, avec des tartines au fromage.",
  [f"800 g|de tomates pelées|{PELEES}|3", f"1|oignon|{OIG}|2", f"2 gousses|d'ail|{AIL}|1", f"50 cl|d'eau ou de bouillon|Bouillon cube légumes|1", f"1 c. à c.|de sucre|{SUCRE}|1", f"4 c. à s.|de crème|{CF}|1?", "6 feuilles|de basilic|Basilic|1?"],
  ["**Suer.** Oignon et ail 5 min à l'huile : translucides.", "**Cuire.** Tomates, bouillon, sucre, 10 min à frémissement.", "**Mixer.** Lisse ; crème, basilic ; goûte le sel."],
  age=1, cats=EX + ["enfants"], profil=["acide", "leger"])

K("veloute_petits_pois_menthe", "Velouté de petits pois à la menthe", "Pea soup", QF, "So", 1, 4, 5, 12, "€", "Casserole, mixeur.",
  "Petits pois surgelés, oignon et menthe : vert éclatant, doux, prêt en 17 minutes ; chaud l'hiver, froid l'été.",
  ["500 g|de petits pois surgelés|Petits pois / pois gourmands|3", f"1|oignon|{OIG}|2", "60 cl|de bouillon de légumes|Bouillon cube légumes|2", "8 feuilles|de menthe|Menthe|2", f"3 c. à s.|de crème|{CF}|1?"],
  ["**Suer.** Oignon 4 min au beurre.", "**Cuire.** Petits pois et bouillon, 6 min seulement : ils restent bien verts.", "**Mixer.** Avec la menthe ; crème ; goûte."],
  age=1, cats=EX + ["enfants"], profil=["leger"])

K("bowl_riz_thon_avocat", "Bol de riz au thon, avocat et sésame", "Tuna rice bowl", JP, "P", 1, 2, 10, 0, "€€", "Bols.",
  "Riz tiède, thon assaisonné soja-citron, avocat, concombre et sésame : l'esprit poke, avec des ingrédients de supermarché.",
  [f"300 g|de riz cuit|{RIZ}|3", "1 boîte (140 g)|de thon|Thon en conserve|3", "1|avocat|Avocat|2", "½|concombre|Concombre|1", f"2 c. à s.|de sauce soja|{SOJA}|1", f"½|citron vert|{CITV}|1", "1 c. à s.|de graines de sésame|Sésame (blanc/noir)|1", "1 c. à s.|de mayonnaise (facultatif)|SUB:mayonnaise|1?"],
  ["**Assaisonner.** Thon émietté, soja, citron vert.", "**Tailler.** Avocat et concombre en dés.", "**Dresser.** Riz, garnitures en rangs, sésame, un trait de mayonnaise."],
  age=3, cats=EX, profil=["poisson", "leger"])

K("bowl_tofu_croustillant", "Bol de tofu croustillant, brocoli et sauce cacahuète", "Crispy tofu bowl", "Asie du Sud-Est › Food fusion", "P", 1, 2, 12, 8, "€", "Poêle, casserole.",
  "Cubes de tofu dorés et croustillants, brocoli, riz et sauce au beurre de cacahuète : végétarien et très gourmand.",
  ["200 g|de tofu ferme|Tofu (ferme / soyeux)|3", f"1 c. à s.|de fécule de maïs|Fécule de maïs (maïzena)|1", "1|brocoli|Brocoli|2", f"300 g|de riz cuit|{RIZ}|2", "2 c. à s.|de beurre de cacahuète|Beurre de cacahuète|2", f"2 c. à s.|de sauce soja|{SOJA}|1", f"½|citron vert|{CITV}|1", f"2 c. à s.|d'huile|{HN}|1"],
  ["**Tofu.** Épongé, en cubes, roulé dans la fécule ; poêle chaude huilée 6-8 min en le retournant : doré sur toutes les faces.",
   "**Brocoli.** 4 min à l'eau bouillante salée.", "**Sauce.** Beurre de cacahuète, soja, citron vert, 3 c. à s. d'eau chaude : lisse. Dresse et nappe."],
  age=3, cats=EX + ["fusion"], profil=["gras"])

K("pad_kra_pao_poulet", "Poulet sauté au basilic thaï (pad kra pao)", "Phat kaphrao", TH, "P", 1, 2, 10, 6, "€", "Wok, casserole (riz).",
  "Le plat de rue le plus populaire de Thaïlande : poulet haché sauté à l'ail, au piment et au basilic, servi sur riz avec un œuf frit.",
  [f"300 g|de poulet haché (ou blanc haché au couteau)|{BLANC_P}|3", f"3 gousses|d'ail|{AIL}|2", f"1-2|piments|{PIMENT}|1", "1 poignée|de basilic thaï (ou basilic)|Basilic thaï|2", "1 c. à s.|de sauce d'huître|Sauce d'huître|2", f"1 c. à s.|de sauce soja|{SOJA}|1", f"2|œufs|{OEUF}|2", f"300 g|de riz cuit|{RIZ}|2"],
  ["**Sauter.** Ail et piment pilés 20 s dans l'huile chaude ; poulet, 4 min en l'émiettant : il n'est plus rose.",
   "**Assaisonner.** Sauce d'huître, soja, une pincée de sucre, basilic : il tombe en 10 s.",
   "**Œuf.** Frit dans beaucoup d'huile chaude : bords croustillants, jaune coulant. Sur le riz, avec le poulet."],
  age=6, cats=EX, profil=["epice"], tech=["wok"])

K("tacos_poisson_express", "Tacos de poisson, chou croquant et sauce citron vert", "Tacos de pescado", f"{MX} › Basse-Californie", "P", 1, 4, 12, 8, "€€", "Poêle.",
  "Poisson blanc saisi au cumin et paprika, chou finement émincé, sauce crème-citron vert : les tacos de Basse-Californie.",
  ["400 g|de poisson blanc (cabillaud, lieu)|Colin, lieu noir, merlu|3", "8|tortillas de maïs ou de blé|Tortillas de maïs|3", "¼|chou blanc|Chou blanc / rouge|2", f"1 c. à c.|de cumin|{CUMIN}|1", f"1 c. à c.|de paprika|{PAPRIKA}|1", f"4 c. à s.|de crème|{CF}|1", f"1|citron vert|{CITV}|2", f"½ bouquet|de coriandre|{CORI}|1"],
  ["**Sauce.** Crème, jus de citron vert, sel ; chou émincé très fin, salé.", "**Poisson.** En gros morceaux, épices, sel ; 2-3 min par face : il s'effeuille.",
   "**Garnir.** Tortillas chaudes, chou, poisson, sauce, coriandre."], age=3, cats=EX, profil=["poisson"])

K("pitas_poulet_yaourt", "Pitas au poulet mariné, tzatziki et tomates", "Pita kotópoulo", GR, "P", 1, 4, 12, 8, "€", "Poêle ou gril.",
  "Poulet citron-origan saisi, tzatziki, tomates et oignon rouge dans un pain pita chaud : le souvlaki de la maison.",
  [f"3|blancs de poulet|{BLANC_P}|3", "4|pains pita|Pain pita / libanais|3", f"1|citron|{CIT}|1", f"1 c. à c.|d'origan|Origan frais / sec|1", f"2|tomates|{TOM}|1", "½|oignon rouge|Oignon rouge|1", "200 g|de tzatziki|Tzatziki|2"],
  ["**Mariner.** Poulet en lanières, citron, origan, huile, sel, 5 min.", "**Saisir.** Poêle très chaude 6 min : doré, jus clair.", "**Garnir.** Pitas chauffées, tzatziki, poulet, tomates, oignon."],
  age=3, cats=EX + ["enfants"])

K("quinoa_saute_legumes", "Quinoa sauté aux légumes et à l'œuf", "Quinoa sauté", "Amérique latine › Pérou", "P", 1, 2, 8, 12, "€", "Casserole, poêle.",
  "Le quinoa remplace le riz dans un sauté : poivron, courgette, maïs, œuf et sauce soja. Complet, végétarien, sans gluten.",
  ["150 g|de quinoa|Quinoa|3", f"1|poivron|{POIVRON}|2", "1|courgette|Courgette|2", "100 g|de maïs|Maïs doux|1", f"2|œufs|{OEUF}|2", f"2 c. à s.|de sauce soja|{SOJA}|1"],
  ["**Cuire.** Quinoa rincé, 12 min à l'eau bouillante salée ; égoutté.", "**Sauter.** Légumes en dés 5 min ; œufs brouillés à côté.", "**Mélanger.** Quinoa, soja, 2 min ; goûte."],
  age=1, cats=EX, profil=["leger"])

K("couscous_express_legumes", "Couscous express aux légumes et pois chiches", "Couscous rapide", MA, "P", 1, 4, 10, 10, "€", "Sauteuse, saladier.",
  "Semoule gonflée en 5 minutes, légumes sautés au ras el-hanout, pois chiches et raisins : le goût du couscous un soir de semaine.",
  ["250 g|de semoule moyenne|Semoule de couscous|3", "2|courgettes|Courgette|2", f"2|carottes|{CAROTTE}|2", f"1 boîte|de pois chiches|{POIS}|2", "2 c. à c.|de ras el-hanout|Ras el-hanout|2", "40 g|de raisins secs|Raisins secs|1?", f"20 g|de beurre|{BEURRE}|1", "25 cl|de bouillon de légumes|Bouillon cube légumes|1"],
  ["**Semoule.** Arrosée de 25 cl de bouillon bouillant, couverte 5 min ; égrenée à la fourchette avec le beurre.",
   "**Légumes.** En dés, sautés 8 min avec les épices ; pois chiches et raisins 2 min.", "**Servir.** La semoule, les légumes par-dessus ; harissa à part."],
  age=1, cats=EX + ["enfants"], profil=["epice"])

K("spaghetti_pomodoro_express", "Spaghetti à la tomate fraîche et au basilic", "Spaghetti al pomodoro", IT, "P", 1, 4, 5, 12, "€", "Casserole, poêle.",
  "Tomates cerises éclatées dans l'huile d'olive et l'ail, basilic : la sauce la plus simple d'Italie, prête pendant que l'eau bout.",
  [f"400 g|de spaghetti|{PATES}|3", "500 g|de tomates cerises|Tomate cerise|3", f"2 gousses|d'ail|{AIL}|1", f"4 c. à s.|d'huile d'olive|{HO}|2", "1 bouquet|de basilic|Basilic|2", f"40 g|de parmesan|{PARM}|1?"],
  ["**Sauce.** Ail écrasé dans l'huile 1 min, tomates coupées en deux, 8 min : elles éclatent ; écrase-les un peu.", "**Lier.** Spaghetti cuits, 1 louche d'eau de cuisson, 1 min dans la sauce.", "**Servir.** Basilic déchiré, parmesan."],
  age=1, cats=EX + ["enfants"], profil=["leger"], tech=["cuire les pâtes"])

K("toasts_champignons_oeuf", "Tartines de champignons à l'ail, œuf au plat", "Mushrooms on toast", QF, "P", 1, 2, 8, 8, "€", "Poêle.",
  "Champignons dorés au beurre, ail et persil sur pain grillé, couronnés d'un œuf au plat : rustique et rassasiant.",
  ["250 g|de champignons|Champignon de Paris|3", "2 tranches|de pain de campagne|Pain de campagne / complet|2", f"2|œufs|{OEUF}|2", f"20 g|de beurre|{BEURRE}|1", f"1 gousse|d'ail|{AIL}|1", f"1 c. à s.|de persil|{PERSIL}|1"],
  ["**Champignons.** Poêle chaude, beurre, champignons en lamelles sans les remuer 3 min : ils dorent ; ail, persil, sel.",
   "**Œufs.** Au plat à côté, 3 min : blanc pris, jaune coulant.", "**Dresser.** Pain grillé, champignons, œuf, poivre."], age=3, cats=EX)

K("frittata_courgettes", "Frittata aux courgettes et parmesan", "Frittata di zucchine", IT, "P", 1, 4, 8, 12, "€", "Poêle allant au four (ou couvercle).",
  "Omelette épaisse aux courgettes et au parmesan, finie sous le gril : se mange chaude, tiède ou froide en pique-nique.",
  [f"6|œufs|{OEUF}|3", "2|courgettes|Courgette|2", f"40 g|de parmesan|{PARM}|2", f"1|oignon|{OIG}|1", f"2 c. à s.|d'huile d'olive|{HO}|1", "6 feuilles|de basilic|Basilic|1?"],
  ["**Légumes.** Oignon et courgettes en fines rondelles, 6 min : tendres et un peu dorés.", "**Œufs.** Battus avec parmesan, sel ; versés, feu doux 6 min sans remuer : les bords prennent.",
   "**Finir.** 2-3 min sous le gril du four (ou couvert) : le dessus est pris et gonflé."], age=1, cats=EX + ["enfants"], fetes=["Barbecue d'été"])

K("burrito_bowl_haricots", "Burrito bowl végétarien", "Burrito bowl", "Amérique du Nord › États-Unis › Tex-Mex", "P", 1, 4, 15, 0, "€", "Casserole, saladier.",
  "Riz, haricots noirs au cumin, maïs, tomate, avocat, cheddar et salsa : tout ce qu'il y a dans un burrito, sans la tortilla.",
  [f"400 g|de riz cuit|{RIZ}|3", "400 g|de haricots noirs|Haricots rouges / noirs|3", "150 g|de maïs|Maïs doux|2", "1|avocat|Avocat|2", f"2|tomates|{TOM}|1", "80 g|de cheddar|Cheddar|1", f"1|citron vert|{CITV}|1", f"1 c. à c.|de cumin|{CUMIN}|1"],
  ["**Haricots.** Chauffés 3 min avec cumin, sel et un peu d'eau.", "**Préparer.** Tomates et avocat en dés, citron vert.", "**Dresser.** Riz, rangs de haricots, maïs, tomate, avocat, fromage, salsa."],
  age=3, cats=EX, profil=["leger"])

K("cabillaud_vapeur_gingembre", "Cabillaud vapeur, gingembre et cébette", "Qīngzhēng yú", CN, "P", 1, 2, 8, 10, "€€", "Panier vapeur ou assiette sur casserole.",
  "Poisson cuit à la vapeur, arrosé d'huile chaude sur gingembre et cébette, sauce soja : délicat, très léger, cantonais.",
  ["2|dos de cabillaud|Cabillaud / morue fraîche|3", "1 morceau (4 cm)|de gingembre|Gingembre frais|2", f"3|cébettes|Oignon nouveau / cébette|2", f"2 c. à s.|de sauce soja|{SOJA}|2", f"2 c. à s.|d'huile neutre|{HN}|1", f"½ bouquet|de coriandre|{CORI}|1?"],
  ["**Vapeur.** Poisson sur une assiette, au-dessus de l'eau frémissante, couvert, 8-10 min : la chair devient nacrée et s'effeuille.",
   "**Garnir.** Gingembre et cébette en fins bâtonnets sur le poisson ; soja.", "**Grésiller.** Huile très chaude versée dessus : ça crépite et parfume. Avec du riz."],
  age=1, cats=EX, profil=["poisson", "leger"], tech=["cuire à la vapeur"])

K("poulet_citronnelle_express", "Poulet sauté à la citronnelle", "Gà xào sả ớt", VN, "P", 1, 4, 12, 8, "€", "Wok, casserole (riz).",
  "Poulet sauté à la citronnelle, à l'ail et au piment, un peu caramélisé à la sauce de poisson : parfumé et rapide.",
  [f"4|cuisses de poulet désossées (ou blancs)|{CUISSE}|3", "2 tiges|de citronnelle|Citronnelle|2", f"2 gousses|d'ail|{AIL}|1", f"1|piment|{PIMENT}|1?", "2 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|2", f"1 c. à s.|de sucre|{SUCRE}|1", f"1|oignon|{OIG}|1"],
  ["**Préparer.** Citronnelle (partie tendre) hachée très fin, ail, piment ; poulet en morceaux.", "**Sauter.** Poulet 5 min à feu vif : doré ; oignon, citronnelle, ail 2 min.",
   "**Caraméliser.** Sucre et sauce de poisson, 1 min : ça brille et colle légèrement. Avec du riz."], age=3, cats=EX, profil=["epice"])

K("tartines_sardines_citron", "Tartines de sardines, citron et persil", "Tostas de sardinha", PT, "P", 1, 2, 10, 0, "€", "Grille-pain.",
  "Sardines à l'huile écrasées avec citron, persil et oignon rouge sur pain grillé frotté à l'ail : un dîner portugais en 10 minutes.",
  [f"2 boîtes|de sardines à l'huile|Sardine (fraîche / conserve)|3", "4 tranches|de pain de campagne|Pain de campagne / complet|2", f"½|citron|{CIT}|1", f"1 c. à s.|de persil|{PERSIL}|1", "¼|oignon rouge|Oignon rouge|1", f"1 gousse|d'ail|{AIL}|1"],
  ["**Griller.** Pain grillé, frotté à l'ail.", "**Écraser.** Sardines (arêtes comprises : elles sont tendres et riches en calcium), citron, persil, oignon.", "**Tartiner.** Poivre ; une salade verte à côté."],
  age=3, cats=EX + ["zero_dechet"], profil=["poisson"])

K("pates_courgettes_feta_citron", "Pâtes aux courgettes, feta et citron", "Pâtes d'été", "Europe du Sud › Grèce", "P", 1, 4, 5, 12, "€", "Casserole, poêle.",
  "Courgettes poêlées à l'ail, feta, zeste de citron et menthe : des pâtes d'été légères et fraîches.",
  [f"400 g|de pâtes|{PATES}|3", "3|courgettes|Courgette|3", "150 g|de feta|Feta|2", f"1|citron|{CIT}|1", f"2 gousses|d'ail|{AIL}|1", "6 feuilles|de menthe|Menthe|1", f"3 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Courgettes.** En demi-rondelles, poêle chaude 6 min : dorées sur les bords ; ail 1 min.", "**Lier.** Pâtes, un peu d'eau de cuisson, zeste et jus de citron.", "**Finir.** Feta émiettée, menthe, poivre."],
  age=1, cats=EX, profil=["leger"])

K("pizza_tortilla", "Pizzas express sur tortilla", "Pizza tortilla", QF, "P", 1, 4, 8, 8, "€", "Four, plaque.",
  "Une tortilla comme pâte fine et croustillante : tomate, mozzarella, garniture au choix, 8 minutes au four. Les enfants garnissent eux-mêmes.",
  ["4|tortillas de blé|Tortillas de blé|3", "8 c. à s.|de sauce tomate|Sauce tomate (bocal)|2", "1 boule|de mozzarella|Mozzarella / burrata|2", "100 g|de champignons|Champignon de Paris|1?", f"1|poivron|{POIVRON}|1?", f"1 pincée|d'origan|Origan frais / sec|0"],
  ["**Préchauffer.** Four à 220 °C.", "**Garnir.** Sauce en couche fine, mozzarella, légumes en fines tranches, origan.", "**Cuire.** 7-8 min : le bord est doré et croustillant, le fromage bulle."],
  age=1, cats=EX + ["enfants"], tech=[])

K("steak_hache_oignons_express", "Steak haché maison aux oignons, purée minute", "Steak haché", QF, "P", 1, 4, 10, 10, "€", "Poêle.",
  "Steaks hachés saisis, oignons fondus au beurre et déglacés : le classique du soir, bien fait.",
  ["4|steaks hachés (5 %)|Bœuf haché|3", f"2|oignons|{OIG}|2", f"15 g|de beurre|{BEURRE}|1", f"1 c. à c.|de moutarde|{DIJON}|1", "1 c. à c.|de vinaigre|Vinaigre de vin rouge / blanc|1?"],
  ["**Oignons.** Émincés, beurre, feu moyen 8 min : fondants et dorés ; un trait de vinaigre, réservés.",
   "**Saisir.** Steaks dans la poêle très chaude, 2-3 min par face (cuits à cœur pour les enfants : 70 °C, plus de rose).", "**Servir.** Oignons dessus, moutarde ; purée ou salade."],
  age=3, cats=EX + ["enfants"], tech=["saisir"], tips=["Viande hachée : toujours cuite à cœur pour les enfants, les femmes enceintes et les personnes fragiles."])

K("nouilles_beurre_cacahuete", "Nouilles froides au beurre de cacahuète", "Peanut noodles", "Asie de l'Est › Food fusion", "P", 1, 2, 10, 5, "€", "Casserole, saladier.",
  "Nouilles enrobées d'une sauce beurre de cacahuète, soja, citron vert et sésame, concombre croquant : tiède ou froid, végétarien.",
  ["200 g|de nouilles (blé ou riz)|Nouilles chinoises aux œufs|3", "3 c. à s.|de beurre de cacahuète|Beurre de cacahuète|3", f"2 c. à s.|de sauce soja|{SOJA}|2", f"1|citron vert|{CITV}|1", f"1 c. à c.|de miel|{MIEL}|1", "½|concombre|Concombre|1", "1 c. à s.|de cacahuètes|Cacahuète / arachide|1?", f"2|cébettes|Oignon nouveau / cébette|1"],
  ["**Cuire.** Nouilles selon le paquet, rincées à l'eau froide.", "**Sauce.** Beurre de cacahuète, soja, citron vert, miel, 4 c. à s. d'eau chaude : lisse et nappante.", "**Mélanger.** Nouilles, sauce, concombre en bâtonnets, cébette, cacahuètes."],
  age=3, cats=EX + ["fusion"], profil=["gras"])

K("tagliatelles_saumon_citron", "Tagliatelles au saumon fumé et citron", "Pâtes au saumon", QF, "P", 1, 4, 5, 10, "€€", "Casserole.",
  "Crème citronnée, saumon fumé en lanières, aneth : les pâtes du dimanche soir, en 15 minutes.",
  ["400 g|de tagliatelles|Pâtes fraîches aux œufs|3", "250 g|de saumon fumé|Saumon fumé|3", f"20 cl|de crème|{CF}|2", f"1|citron|{CIT}|1", "1 c. à s.|d'aneth|Aneth|1?"],
  ["**Cuire.** Tagliatelles.", "**Sauce.** Crème, zeste de citron, poivre, chauffée 2 min (pas de sel : le saumon est salé).", "**Mélanger.** Pâtes, sauce, saumon en lanières hors du feu, aneth."],
  age=3, cats=EX, profil=["poisson"])

K("croque_poulet_pesto", "Croque au poulet, pesto et mozzarella", "Croque pesto", QF, "P", 1, 2, 8, 6, "€", "Poêle ou appareil à croque.",
  "Pain de mie, pesto, poulet cuit, mozzarella et tomate, doré à la poêle : un croque sans jambon, très gourmand.",
  ["4 tranches|de pain de mie|Pain de mie|3", "150 g|de poulet cuit (reste de rôti)|Poulet entier|2", "2 c. à s.|de pesto|Pesto (bocal)|2", "½ boule|de mozzarella|Mozzarella / burrata|2", f"1|tomate|{TOM}|1", f"10 g|de beurre|{BEURRE}|1"],
  ["**Monter.** Pesto, poulet, tomate, mozzarella entre deux tranches.", "**Dorer.** Beurré dehors, poêle moyenne couverte 3 min par face : doré, le fromage fond.", "**Couper.** En triangles ; salade."],
  age=3, cats=EX + ["enfants", "zero_dechet"])

K("galettes_courgettes_feta", "Galettes de courgette à la feta", "Kolokithokeftedes", GR, "P", 1, 4, 12, 8, "€", "Poêle.",
  "Courgette râpée, feta, menthe, œuf et farine, en petites galettes dorées : végétarien, avec une sauce yaourt.",
  ["2|courgettes|Courgette|3", "120 g|de feta|Feta|2", f"1|œuf|{OEUF}|2", f"4 c. à s.|de farine|{F55}|2", "6 feuilles|de menthe|Menthe|1", f"4 c. à s.|d'huile|{HN}|1", f"4 c. à s.|de yaourt grec|{GREC}|1?"],
  ["**Presser.** Courgettes râpées, salées, pressées fort dans un torchon : il faut enlever l'eau.", "**Mélanger.** Feta, œuf, farine, menthe, poivre.",
   "**Cuire.** Cuillerées aplaties dans l'huile chaude, 3 min par face : dorées. Avec le yaourt."], age=1, cats=EX + ["enfants"], fetes=["Apéritif dînatoire"])

K("riz_cantonais_vegetarien", "Riz sauté végétarien aux légumes croquants", "Riz sauté aux légumes", CN, "P", 1, 4, 10, 8, "€", "Wok.",
  "Riz de la veille sauté avec carotte, poivron, petits pois, maïs, œuf et sauce soja : vide-frigo coloré.",
  [f"600 g|de riz cuit froid|{RIZ}|3", f"1|carotte|{CAROTTE}|2", f"1|poivron|{POIVRON}|2", "100 g|de petits pois|Petits pois / pois gourmands|1", "100 g|de maïs|Maïs doux|1", f"2|œufs|{OEUF}|2", f"3 c. à s.|de sauce soja|{SOJA}|2"],
  ["**Légumes.** En petits dés, 3 min à feu vif.", "**Œufs.** Poussés sur le côté, brouillés.", "**Riz.** Ajouté, émietté, 4 min : il grésille ; soja ; goûte."],
  age=1, cats=EX + ["enfants", "zero_dechet"], tech=["wok"])

K("soupe_nouilles_miso_express", "Soupe de nouilles au miso, tofu et épinards", "Miso rāmen végétarien", JP, "So", 1, 2, 8, 8, "€", "Casserole.",
  "Bouillon au miso, nouilles, tofu, épinards et cébette : un bol chaud et complet en un quart d'heure.",
  ["150 g|de nouilles (ramen ou soba)|Nouilles ramen|3", "2 c. à s.|de miso|Miso|3", "150 g|de tofu|Tofu (ferme / soyeux)|2", "100 g|d'épinards|Épinard|1", f"2|cébettes|Oignon nouveau / cébette|1", "1 c. à c.|de sésame|Sésame (blanc/noir)|0"],
  ["**Bouillon.** 80 cl d'eau frémissante ; miso délayé dans une louche puis ajouté (il ne doit pas bouillir).", "**Cuire.** Nouilles à part ; tofu en dés et épinards 1 min dans le bouillon.", "**Servir.** Nouilles dans les bols, bouillon, cébette, sésame."],
  age=3, cats=EX, profil=["leger"])
