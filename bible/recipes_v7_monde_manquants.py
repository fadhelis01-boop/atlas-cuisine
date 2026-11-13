# -*- coding: utf-8 -*-
"""Audit des manques TikTok (13/11/2026, AUDIT_MANQUES_TIKTOK_2026-11-13.md §5, priorités 2, 3 et 5) : Philippines
(pays à 4 fiches malgré un poids TikTok énorme), classiques mondiaux « étonnamment absents » vérifiés un par un, et
compléments Colombie/Chili. Recherche TikTok bloquée (erreur serveur sur /search/video) pendant cette vague : aucune
fiche créditée ici, à faire dans une passe ultérieure. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

PH = "Asie du Sud-Est › Philippines"; IN = "Asie du Sud › Inde"; CN = "Asie de l'Est › Chine"
AR = "Amérique latine & Caraïbes › Argentine"; GB = "Europe du Nord › Royaume-Uni"; ECO = "Europe du Nord › Royaume-Uni › Écosse"
CO = "Amérique latine & Caraïbes › Colombie"; CL = "Amérique latine & Caraïbes › Chili"
PORC_PO = "Poitrine de porc (fraîche)"; QF = "Queso fresco / cotija"; HBN = "Haricots rouges / noirs"
PATE_ARACHIDE = "Pâte d'arachide"; QBOEUF = "Queue de bœuf"; GEL = "Gélatine de bœuf / poisson, agar-agar, pectine"
FRISE = "Farine de riz / riz gluant"; SEMFINE = "Semoule de blé (fine/moyenne)"; PLANTAIN = "Plantain (banane à cuire)"
DULCE = "Dulce de leche"; CHORIZOBF = "Chorizo de bœuf ou de volaille"; FOIE_V = "Foie de veau"
SAUCISSE_VOL = "Saucisse de bœuf / de veau / de volaille"

# ---------- Philippines ----------
K("sisig", "Sisig (poitrine de porc grillée et hachée, citron vert, piment, œuf)", "Sisig", PH, "P", 2, 4, 25, 15, "€€",
  "Poêle, plancha ou poêle en fonte très chaude, hachoir ou deux couteaux.",
  "Le plat de bar le plus commandé des Philippines, servi grésillant dans son plat en fonte : de la poitrine de porc "
  "grillée puis hachée grossièrement au couteau, relevée de citron vert, d'oignon et de piment, finie d'un œuf cru "
  "qu'on mélange à table pour le lier à la chaleur du plat.",
  [f"700 g|de poitrine de porc (ou de travers), avec un peu de couenne|{PORC_PO}|3", "2|citrons verts|Citron vert|1",
   f"1|oignon rouge, haché fin|{OIG}|1", "2|piments oiseau (plus ou moins selon le goût)|Piment frais (divers)|1",
   f"3 c. à s.|de mayonnaise|Mayonnaise industrielle|1?", f"2 c. à s.|de sauce soja|{SOJA}|1",
   f"1|œuf (cru, posé dessus)|{OEUF}|1", f"2 c. à s.|d'huile|{HN}|1", f"-|poivre|{POIVRE}|1"],
  ["**Griller.** Poitrine de porc bouillie 20 min dans l'eau salée (pour l'attendrir), égouttée, puis grillée au four "
   "ou à la poêle très chaude 10 à 15 min par face : bien dorée et croustillante en surface.",
   "**Hacher.** Encore chaude, hachée grossièrement au couteau (ou au hachoir par à-coups) : des morceaux de 5 mm, "
   "pas une purée. C'est ce geste qui donne au sisig sa texture caractéristique.",
   "**Sauter.** À la poêle très chaude avec l'huile, 3 à 4 min, le porc haché, l'oignon et le piment : bien grésillant.",
   "**Assaisonner.** Hors du feu, soja, jus d'un citron vert, mayonnaise ; mélangé.",
   "**Servir.** Dans un plat brûlant (fonte si possible, encore sur le feu une minute), œuf cru cassé dessus au "
   "dernier moment, quartiers du second citron vert ; chacun mélange l'œuf à table avec la fourchette, la chaleur le "
   "cuit presque instantanément."],
  tips=["Pas de plat en fonte : un plat très chaud sorti du four 2 min avant fait aussi grésiller.",
        "L'œuf cru cuit à la chaleur du porc et du plat : s'il reste cru au centre, mélange un peu plus avant de servir."],
  var=[("Sans porc", ["pork"], {PORC_PO: [("Cuisse / pilon de poulet", 1.0)], "Foies / gésiers de volaille": [("Foies / gésiers de volaille", 1.0)]},
        "Porc → **sisig de poulet** : cuisses de poulet grillées puis hachées, mêmes proportions et même geste. **À tester**.")],
  keep="Le jour même, œuf compris ; sans l'œuf, 2 jours au frigo.", age=4, kids="Peu adapté : piment et plat brûlant ; une version douce sans piment dès 4 ans.",
  cats=["express"], profil=["epice", "gras", "acide"])
K("lechon_kawali", "Lechon kawali (poitrine de porc bouillie puis frite, très croustillante)", "Lechon kawali", PH, "P", 2, 6, 20, 90, "€€",
  "Grande casserole, friteuse ou poêle profonde.",
  "Le lechon du quotidien, sans passer par le cochon entier à la broche : une poitrine de porc longuement bouillie "
  "avec des aromates jusqu'à très tendre, séchée, puis frite juste avant de servir pour une peau qui craque sous la "
  "dent. Trempé dans une sauce au vinaigre et à l'ail.",
  [f"1,2 kg|de poitrine de porc avec sa couenne|{PORC_PO}|3", f"4 gousses|d'ail écrasées|{AIL}|1", f"2|feuilles de laurier|{LAURIER}|1",
   f"1 c. à s.|de grains de poivre|{POIVRE}|1", f"-|sel|{SEL}|1", f"1 l|d'huile de friture|{HN}|2",
   f"4 c. à s.|de vinaigre (pour la sauce)|{CIDRE}|1", f"1 gousse|d'ail (pour la sauce), écrasée|{AIL}|1", "1|piment oiseau (pour la sauce, facultatif)|Piment frais (divers)|1?"],
  ["**Bouillir.** Poitrine couverte d'eau avec ail, laurier, poivre et sel ; 1 h à 1 h 15 à petits bouillons, "
   "couvercle entrouvert : la viande se perce facilement à la fourchette, encore entière.",
   "**Sécher.** Égouttée, épongée, posée sur une grille au frigo 2 h minimum (ou toute une nuit) : la peau sèche "
   "bien, c'est ce qui la rendra croustillante et évite les projections à la friture.",
   "**Frire.** Huile à 175 °C ; poitrine entière plongée avec précaution (couvercle ou grille de protection, l'eau "
   "résiduelle peut gicler), 10 à 12 min en la retournant, jusqu'à bien dorée et la peau soufflée et craquante partout.",
   "**Reposer et trancher.** 5 min sur une grille (jamais dans du papier absorbant à plat, sinon la peau ramollit "
   "en dessous) ; tranché en morceaux de 3 cm au couperet, en travaillant les zones les plus croustillantes.",
   "**Servir.** Avec la sauce vinaigre-ail (vinaigre, ail écrasé, piment, pincée de sel, mélangés), et du riz blanc."],
  tips=["La poitrine doit être bien sèche avant de frire : c'est l'humidité résiduelle qui fait gicler l'huile et "
        "empêche la peau de craquer.", "La version volaille traditionnelle des Philippines est le lechon manok "
        "(poulet entier rôti à la citronnelle) : à faire, recette distincte, pas juste une substitution dans celle-ci."],
  keep="2 jours au frigo ; se réchauffe mal (perd son croustillant) : à frire à nouveau 2 min si besoin.", age=4,
  kids="Peu adapté avant 4 ans (morceaux croustillants) ; viande tendre sans la peau dès 2 ans.", cats=[],
  fetes=["Repas de famille"], profil=["gras"])
K("kare_kare", "Kare-kare (ragoût de queue de bœuf à la sauce cacahuète, légumes)", "Kare-kare", PH, "P", 2, 6, 30, 180, "€€",
  "Grande cocotte, poêle.",
  "Le ragoût de fête des Philippines, couleur ocre et fondant : de la queue de bœuf mijotée des heures jusqu'à "
  "tendre, liée d'une sauce épaisse à la pâte de cacahuète et au riz grillé moulu, avec aubergines et haricots longs. "
  "Servi avec une pâte de crevettes fermentée à part, à doser soi-même.",
  [f"1,5 kg|de queue de bœuf en tronçons|{QBOEUF}|3", f"2|oignons|{OIG}|1", f"4 gousses|d'ail|{AIL}|1",
   f"4 c. à s.|de pâte d'arachide (ou de beurre de cacahuète)|{PATE_ARACHIDE}|2", f"3 c. à s.|de riz cru, torréfié à sec et moulu|{RIZ}|1",
   f"1|aubergine, en tranches|Aubergine|2", "200 g|de haricots verts ou de haricots longs, en tronçons|Haricots verts|2",
   f"2 c. à s.|d'huile|{HN}|1", f"1 c. à c.|de curcuma (pour la couleur)|{CURC}|1?", f"-|sel|{SEL}|1",
   f"3 c. à s.|de pâte de crevettes (bagoong, à part pour chacun)|Pâte de crevettes|1?",
   f"3 c. à s.|de vinaigre (sawsawan, pour tremper, avec un piment écrasé)|{CIDRE}|1?"],
  ["**Mijoter la queue de bœuf.** Dorée à l'huile dans la cocotte avec oignon et ail ; couverte d'eau à hauteur, "
   "sel, 2 h 30 à 3 h à petits bouillons couverts : la viande se détache de l'os à la fourchette. Bouillon réservé "
   "(3 verres pour la sauce).",
   "**Sauce.** Riz torréfié moulu (ou de la farine de riz torréfiée à sec 2 min à la poêle) délayé dans le bouillon "
   "chaud avec la pâte d'arachide et le curcuma : sauce lisse et épaisse qui nappe la cuillère.",
   "**Réunir.** Queue de bœuf remise dans la sauce, 10 min à feu doux pour qu'elle s'imprègne.",
   "**Légumes.** Aubergine et haricots ajoutés en dernier, 8 à 10 min à couvert : juste tendres, encore un peu "
   "croquants pour les haricots.",
   "**Servir.** Avec du riz blanc, la pâte de crevettes à part (chacun en ajoute une pointe selon son goût, elle "
   "est très salée et puissante) et le sawsawan : vinaigre et piment écrasé dans une petite coupelle, pour "
   "tremper chaque bouchée et réveiller le plat."],
  tips=["Le riz torréfié moulu (sans robot : au pilon ou au rouleau dans un torchon) épaissit et parfume la sauce "
        "bien mieux qu'une simple fécule.", "La pâte de crevettes à part permet aux enfants de manger le plat sans "
        "elle, qui est très forte en goût."],
  keep="3 jours au frigo ; se congèle sans les légumes (ajoutés frais à la décongélation).", age=4,
  kids="✓ dès 4 ans, sans la pâte de crevettes.", cats=[], fetes=["Repas de famille"], profil=["gras"])

# ---------- Classiques « étonnamment absents » ----------
K("dosa_instantane", "Dosa instantanée (crêpe croustillante de riz et semoule, sambar ou chutney)", "Dosa", IN, "P", 2, 8, 20, 15, "€",
  "Mixeur, poêle plate ou crêpière antiadhésive, louche.",
  "La crêpe fine et dentelée du Sud de l'Inde, en version instantanée sans fermentation de 24 h : une pâte de "
  "semoule, de riz et de yaourt qui repose 20 minutes, versée en fine couche et étalée en spirale, dorée et "
  "croustillante sur les bords. Avec un chutney à la noix de coco ou un sambar de lentilles.",
  [f"150 g|de semoule fine|{SEMFINE}|3", f"100 g|de farine de riz|{FRISE}|2", f"200 g|de yaourt nature|{YAO}|2",
   f"30 cl|d'eau (à ajuster)|{EAU}|2", f"1/2 c. à c.|de bicarbonate de soude|Bicarbonate de soude|1",
   f"1 pincée|de sel|{SEL}|1", f"3 c. à s.|d'huile (pour la cuisson)|{HN}|1"],
  ["**Pâte.** Semoule, farine de riz, yaourt, eau et sel fouettés en pâte fluide, un peu plus liquide qu'une pâte "
   "à crêpes classique ; 20 min de repos couverte : la semoule gonfle.",
   "**Ajuster.** Bicarbonate incorporé juste avant de cuire (il pétille et allège la pâte) ; eau rajoutée si elle a "
   "trop épaissi, elle doit couler facilement de la louche.",
   "**Étaler.** Poêle très chaude, à peine huilée au papier absorbant ; une louche versée au centre et étalée en "
   "spirale du centre vers les bords avec le dos de la louche, en couche très fine.",
   "**Cuire.** Un filet d'huile sur les bords ; 2 à 3 min à feu moyen-vif sans la retourner, jusqu'à ce que les "
   "bords se décollent et dorent franchement et que le centre ne soit plus brillant : elle se cuit d'un seul côté.",
   "**Servir.** Roulée ou pliée en deux, aussitôt, avec un chutney coco ou un sambar de lentilles bien chaud."],
  tips=["Trop épaisse, la dosa reste molle : la pâte doit couler toute seule quand on incline la louche.",
        "La poêle doit être très chaude avant la première dosa, puis juste chaude pour les suivantes : trop chaude, "
        "la pâte n'a pas le temps de s'étaler."],
  keep="La pâte se garde 1 jour au frigo ; les dosa cuites ne se gardent pas, à manger aussitôt.", age=2,
  kids="✓ dès 2 ans.", cats=["enfants", "vegetarien", "express"], profil=["leger"])
K("xiaolongbao", "Xiaolongbao (raviolis chinois à la soupe, porc et bouillon gélifié)", "小笼包", CN, "P", 3, 24, 60, 15, "€€",
  "Panier vapeur en bambou (ou passoire + couvercle), rouleau à pâtisserie, petite cuillère.",
  "Le ravioli le plus spectaculaire de la cuisine chinoise : une farce de porc enveloppe un bouillon gélifié qui "
  "fond à la vapeur et redevient liquide, caché à l'intérieur d'une fine pâte plissée en vingt replis. On le mange "
  "en le perçant d'abord d'un petit trou pour aspirer le bouillon, puis en croquant le reste.",
  [f"400 g|d'échine de porc hachée|Échine / palette de porc|3",
   f"25 cl|de bouillon de volaille froid et bien parfumé|{BOUILLON}|2", f"8 g|de gélatine (ou agar-agar, voir astuce)|{GEL}|1",
   f"2 c. à s.|de sauce soja|{SOJA}|1", f"1 c. à c.|d'huile de sésame|Huile de sésame (grillée)|1", f"2 cm|de gingembre frais, râpé|{GING}|1",
   f"2|cébettes, ciselées|Oignon nouveau / cébette|1", f"300 g|de farine|{F55}|2", f"15 cl|d'eau chaude|{EAU}|1",
   f"4 c. à s.|de vinaigre noir chinois (pour servir)|Vinaigre noir chinois (Chinkiang)|1?"],
  ["**Bouillon gélifié (la veille ou 3 h avant).** Gélatine ramollie dans un peu de bouillon froid, puis dissoute "
   "dans le reste du bouillon tiédi avec soja, huile de sésame et gingembre ; versé dans un plat sur 1 cm, pris au "
   "frigo au moins 3 h : il doit être ferme et se couper en petits dés.",
   "**Farce.** Porc haché mélangé aux dés de bouillon gélifié coupés très fin et aux cébettes : la farce doit "
   "rester froide pour que les dés ne fondent pas avant la cuisson.",
   "**Pâte.** Farine et eau chaude pétries en pâte souple et lisse ; 20 min de repos sous un torchon.",
   "**Façonner.** Pâte étirée en boudin, coupée en 24 tronçons, chacun étalé en disque fin de 8 cm, plus fin sur "
   "les bords qu'au centre ; une cuillerée de farce au centre, bords remontés et plissés tout autour (16 à 20 "
   "plis), pincés et tordus pour sceller en haut.",
   "**Cuire à la vapeur.** Posés sur un carré de papier cuisson percé (ou une feuille de chou), espacés dans le "
   "panier vapeur ; 8 à 10 min à la vapeur bouillante : la pâte est translucide et tendue, gonflée par le bouillon "
   "qui a refondu à l'intérieur.",
   "**Servir.** Aussitôt, très chauds, avec le vinaigre noir et des lamelles de gingembre : on les prend à la "
   "cuillère chinoise, on perce un petit trou pour aspirer le bouillon avant de croquer le reste."],
  tips=["Sans gélatine de bœuf : l'agar-agar marche aussi (porté à ébullition 1 min dans le bouillon puis pris au "
        "frigo), avec une texture un peu plus ferme.", "Les plis se ratent les premières fois : même mal pliés, "
        "ils gardent le bouillon tant que la pâte n'est pas percée — c'est l'étanchéité qui compte, pas la "
        "symétrie."],
  var=[("Sans porc", ["pork"], {"Échine / palette de porc": [("Cuisse / pilon de poulet", 1.0)]},
        "Porc → **poulet haché avec un peu de peau** (le gras garde la farce juteuse) et bouillon de volaille. **À tester**.")],
  keep="Farcis crus, 1 jour au frigo ou 1 mois au congélateur (cuits directement à la vapeur, sans décongeler, "
       "2 min de plus) ; cuits, à manger aussitôt.", age=4, kids="Attention à la chaleur du bouillon intérieur : "
       "dès 4 ans, en soufflant bien avant de croquer.", cats=[], profil=["gras"])
K("asado_argentin", "Asado argentin (bœuf grillé à la braise, chorizo criollo, chimichurri)", "Asado", AR, "P", 2, 8, 20, 90, "€€€",
  "Barbecue à braise (ou four + plancha), pince longue, planche à découper large.",
  "Le rituel du dimanche en Argentine, plus une méthode qu'une recette : une braise de bois ou de charbon réduite "
  "en chaleur douce et constante, de longues cuissons de pièces entières (vacío, côtes) et des chorizos, le tout "
  "tranché à table et servi avec le chimichurri. On ne retourne la viande qu'une fois, et on ne la presse jamais.",
  ["1,5 kg|de bavette ou de flanchet (vacío) en un seul morceau|Bavette|3", "1,2 kg|de côtes de bœuf (asado de tira), en travers de l'os|Côte de bœuf|3",
   f"4|chorizos criollos (chorizo frais à griller)|{SAUCISSE_VOL}|2", f"-|gros sel|{SEL}|2",
   "1 pot|de chimichurri (recette liée)|SUB:chimichurri|2"],
  ["**Préparer la braise.** Bois ou charbon brûlé à feu vif puis tiré en braise ardente mais sans flamme, étalée "
   "en couche égale ; la grille posée haut (la main y résiste 4 à 5 secondes) : l'asado est une cuisson lente et "
   "douce, jamais une cuisson vive.",
   "**Saler.** Gros sel sur les deux faces des pièces de bœuf, 10 min avant la grille : il forme une légère croûte "
   "sans assécher.",
   "**Griller les pièces longues d'abord.** Côtes et vacío posés côté os ou côté gras en premier, 25 à 35 min sans "
   "les toucher ni les piquer (la pointe du couteau laisse fuir le jus) ; retournés une seule fois, encore 20 à "
   "25 min : une croûte brun doré, le centre qui résiste encore un peu sous le doigt pour une cuisson à point.",
   "**Chorizos.** Posés sur la grille 20 min avant la fin, retournés plusieurs fois : dorés et fermes, le jus ne "
   "doit plus être rosé en les piquant légèrement.",
   "**Reposer et trancher.** Pièces de bœuf posées 10 min sur la planche avant de trancher, perpendiculairement "
   "aux fibres, en tranches de 1,5 cm.",
   "**Servir.** À table, avec le chimichurri à disposition et du pain ; on commence toujours par les chorizos "
   "pendant que le bœuf repose."],
  tips=["Une braise trop vive brûle l'extérieur avant que l'intérieur ne cuise : si ça flambe encore, attends.",
        "Sans barbecue : au four à 160 °C (chaleur douce, 1 h pour le vacío) puis 3 min de plancha très chaude de "
        "chaque côté pour la croûte."],
  var=[("Sans porc", ["pork"], {SAUCISSE_VOL: [(SAUCISSE_VOL, 1.0)]}, "Les chorizos criollos sont déjà de bœuf/veau par défaut ici ; vérifier l'étiquette si achetés tout prêts, certains sont au porc.")],
  keep="Bœuf tranché, 2 jours au frigo ; sandwich le lendemain (choripán).", age=4, kids="✓ dès 4 ans, viande coupée fin.",
  cats=[], fetes=["Repas de famille"], profil=["gras"])
K("bangers_mash", "Bangers and mash (saucisses rôties, purée crémeuse, sauce aux oignons)", "Bangers and mash", GB, "P", 1, 4, 20, 30, "€",
  "Poêle, casserole, presse-purée.",
  "Le plat de pub britannique par excellence : des saucisses bien dorées au four, une purée de pommes de terre "
  "généreusement beurrée, et une sauce brune aux oignons longuement caramélisés qui noie le tout.",
  [f"8|saucisses de porc (ou de bœuf/volaille)|{SAUCISSE_VOL}|3", f"1 kg|de pommes de terre à purée|{PDT}|3",
   f"80 g|de beurre|{BEURRE}|2", f"15 cl|de lait chaud|{LAIT}|2", f"2|gros oignons, émincés finement|{OIG}|2",
   f"2 c. à s.|de farine|{F55}|1", f"40 cl|de bouillon de bœuf|{BOUILLON}|2", f"1 c. à c.|de sauce anglaise (Worcestershire)|Sauce Worcestershire|1?",
   f"2 c. à s.|d'huile|{HN}|1", f"-|sel, poivre|{SEL}|1"],
  ["**Saucisses.** Four à 200 °C ; saucisses piquées une fois chacune (elles n'éclatent pas), rôties 20 à 25 min "
   "en les retournant à mi-cuisson : bien dorées sur toutes les faces.",
   "**Oignons.** À la poêle avec l'huile, feu doux, 20 à 25 min en remuant souvent : ils fondent et caramélisent "
   "jusqu'à une couleur brun doré, sans brûler. C'est le temps qui fait le goût, pas le feu fort.",
   "**Sauce.** Farine saupoudrée sur les oignons, 1 min ; bouillon versé en filet en remuant, sauce Worcestershire ; "
   "8 à 10 min à feu doux : elle nappe la cuillère.",
   "**Purée.** Pommes de terre cuites à l'eau salée 20 min, égouttées, écrasées encore chaudes ; beurre et lait "
   "chaud incorporés : lisse et bien crémeuse, salée et poivrée.",
   "**Servir.** Purée en dôme, saucisses posées dessus, sauce aux oignons versée généreusement."],
  tips=["La sauce aux oignons se prépare pendant que les saucisses rôtissent : rien n'attend personne.",
        "Des petits pois à l'anglaise en accompagnement sont un classique du pub."],
  var=[("Sans porc", ["pork"], {SAUCISSE_VOL: [(SAUCISSE_VOL, 1.0)]}, "Déjà proposé en bœuf/volaille par défaut ; vérifier l'étiquette des saucisses achetées toutes prêtes, souvent au porc.")],
  keep="2 jours au frigo, purée et saucisses séparées.", age=1, kids="✓ dès 1 an.", cats=["enfants"], profil=["gras"])
K("haggis_facon_maison", "Haggis façon maison (agneau haché, foie, avoine, épices, cuit en terrine)", "Haggis", ECO, "P", 2, 6, 30, 90, "€€",
  "Cocotte ou terrine, poêle.",
  "Le plat national écossais, ici dans sa version simplifiée et déjà très répandue dans les foyers écossais eux-mêmes : "
  "agneau haché et foie, avoine, oignon et un mélange d'épices chaudes, cuits lentement dans une terrine plutôt que "
  "dans la panse traditionnelle. Servi avec une purée de pommes de terre et de rutabaga (« tatties and swede »).",
  [f"500 g|d'agneau haché|Agneau haché|3", f"250 g|de foie d'agneau ou de foie de veau, haché fin|{FOIE_V}|2",
   f"150 g|de flocons d'avoine|Avoine (flocons)|2", f"1|gros oignon, haché fin|{OIG}|2",
   f"100 g|de beurre fondu (à défaut de graisse de rognon)|{BEURRE}|1", f"1 c. à c.|de muscade|{MUSC}|1",
   f"1 c. à c.|de poivre noir moulu|{POIVRE}|1", f"1/2 c. à c.|de piment de la Jamaïque (ou quatre-épices)|Quatre-épices|1",
   f"20 cl|de bouillon de volaille ou d'agneau|{BOUILLON}|2", f"-|sel|{SEL}|1",
   f"2 c. à s.|de moutarde anglaise (ou de Dijon, à défaut)|{DIJON}|1?"],
  ["**Torréfier l'avoine.** À sec dans une poêle, 3 à 4 min en remuant : légèrement dorée, odeur de noisette.",
   "**Mélanger.** Agneau haché, foie haché, oignon, avoine torréfiée, beurre fondu, épices et bouillon mélangés à "
   "la main dans un grand saladier, jusqu'à homogène ; salé.",
   "**Cuire.** Four à 160 °C. Versé dans une terrine ou un plat à gratin, tassé, couvert de papier aluminium ; "
   "1 h 15 à 1 h 30 : ferme et doré sur les bords découverts, le jus clair quand on pique au centre.",
   "**Reposer.** 10 min avant de servir : elle se tranche plus net.",
   "**Servir.** En tranches épaisses, avec une purée de pommes de terre et de rutabaga à parts égales, beurrée, "
   "et un peu de moutarde anglaise à côté — c'est la façon dont les Écossais le mangent eux-mêmes."],
  tips=["Le foie peut être remplacé par des foies de volaille pour une version plus douce : le goût est moins "
        "typé mais reste bon.", "Cette version en terrine évite la panse d'estomac traditionnelle (nettoyage et "
        "cuisson longues, réservées à qui veut vraiment l'authenticité) : décision du propriétaire si une version "
        "100 % traditionnelle doit être ajoutée un jour."],
  keep="3 jours au frigo ; se congèle en tranches.", age=4, kids="✓ dès 4 ans (goût prononcé, abats).", cats=[],
  profil=["gras"])

# ---------- Colombie et Chili ----------
K("bandeja_paisa", "Bandeja paisa (plateau colombien : riz, haricots rouges, viande, chicharrón, œuf, plantain, avocat)", "Bandeja paisa", CO, "P", 3, 4, 40, 90, "€€€",
  "Grande cocotte, poêle, assiettes larges.",
  "Le plateau généreux de la région d'Antioquia, un repas à lui seul : riz, haricots rouges mijotés, viande hachée "
  "grillée, chicharrón croustillant, œuf au plat, plantain mûr frit, avocat et une arepa, le tout dressé côte à côte "
  "sur une grande assiette.",
  [f"300 g|de riz long|{RIZ}|2", f"400 g|de haricots rouges secs, trempés une nuit|{HBN}|3", f"300 g|de bœuf haché|{HACHE}|3",
   f"300 g|de poitrine de porc, en lanières (chicharrón)|{PORC_PO}|2", f"4|œufs|{OEUF}|2",
   f"2|plantains mûrs, en tranches épaisses|{PLANTAIN}|2", f"1|avocat, en tranches, citron vert pressé dessus|Avocat|1",
   f"1|citron vert|Citron vert|1",
   f"4|arepas (recette liée)|-|1?", f"1|oignon|{OIG}|1", f"2 gousses|d'ail|{AIL}|1",
   f"4 c. à s.|d'huile|{HN}|1", f"-|sel, cumin|{CUMIN}|1"],
  ["**Haricots.** Haricots trempés égouttés, cuits 1 h 30 à 2 h à l'eau avec la moitié de l'oignon et de l'ail, "
   "jusqu'à bien tendres ; sel en fin de cuisson (pas avant, sinon ils durcissent).",
   "**Chicharrón.** Poitrine de porc en lanières, frite ou rôtie au four à 200 °C 25 min jusqu'à bien croustillante.",
   "**Viande hachée.** Bœuf haché doré à la poêle avec oignon, ail, cumin et sel, 10 min, émietté à la fourchette : "
   "sec et bien doré, pas en sauce.",
   "**Riz.** Cuit à l'absorption, classique.",
   "**Plantain et œuf.** Plantain frit 3 min par face à l'huile chaude jusqu'à doré ; œufs au plat cuits juste "
   "avant de dresser, jaune encore coulant.",
   "**Dresser.** Sur une grande assiette, chaque élément dans sa zone : riz, haricots, viande hachée, chicharrón, "
   "œuf au plat, plantain, avocat, et l'arepa à côté."],
  tips=["Tout se prépare en avance sauf l'œuf au plat et le réchauffage final : c'est un plat d'assemblage, pas une "
        "cuisson de dernière minute.", "Moins généreux pour les enfants : une petite portion de chaque élément, "
        "sans le chicharrón si trop gras pour eux."],
  var=[("Sans porc", ["pork"], {PORC_PO: [("Cuisse / pilon de poulet", 1.0)]}, "Porc (chicharrón) → **peau de poulet grillée très croustillante** à la place. **À tester**.")],
  side="arepas", keep="Chaque élément séparément, 2 jours au frigo ; à réassembler et réchauffer au moment.", age=3,
  kids="✓ dès 3 ans, en petites portions de chaque élément.", cats=[], fetes=["Repas de famille"], profil=["gras"])
K("patacones", "Patacones (tostones, plantain vert aplati et refrit, sel et ail)", "Patacones / tostones", CO, "A", 1, 4, 15, 15, "€",
  "Poêle ou friteuse, objet plat pour aplatir (fond de verre, presse-purée, planche).",
  "L'accompagnement incontournable de la Colombie et de toute la Caraïbe : des rondelles de plantain vert frites "
  "une première fois, aplaties, puis refrites jusqu'à bien dorées et croustillantes, salées à l'ail dès la sortie "
  "de la friture.",
  [f"3|plantains verts (peau encore bien verte, fermes)|{PLANTAIN}|3", f"50 cl|d'huile de friture (ou 4 c. à s. pour une cuisson à la poêle)|{HN}|2",
   f"2 gousses|d'ail, écrasées|{AIL}|1", f"-|sel|{SEL}|1"],
  ["**Préparer.** Plantains épluchés (la peau verte résiste : fendre sur la longueur au couteau puis décoller), "
   "coupés en tronçons de 4 cm.",
   "**Première friture.** Huile à 160 °C ; tronçons frits 3 à 4 min, encore pâles mais tendres à la pointe du "
   "couteau.",
   "**Aplatir.** Égouttés, aplatis aussitôt (encore chauds, sinon ils se fendent) au fond d'un verre ou à la presse-"
   "purée, jusqu'à 1 cm d'épaisseur.",
   "**Deuxième friture.** Huile remontée à 175 °C ; patacones replongés 3 à 4 min, retournés une fois : dorés et "
   "croustillants sur les deux faces.",
   "**Finir.** Égouttés, salés et frottés d'un peu d'ail écrasé dès la sortie de l'huile, aussitôt."],
  tips=["Trop mûr (peau qui jaunit), le plantain devient sucré et ne tient pas à la double friture : il faut la "
        "variété bien verte et ferme.", "Les enfants aplatissent très bien les tronçons tièdes."],
  keep="Le jour même, recroustillés 5 min au four si besoin.", age=2, kids="✓ dès 2 ans. Les enfants aplatissent.",
  cats=["enfants", "vegetarien", "express"], profil=["leger"])
K("bunuelos_colombianos", "Buñuelos colombiens (beignets de fromage frais, boules dorées de Noël)", "Buñuelos", CO, "G", 1, 16, 20, 15, "€",
  "Friteuse ou casserole profonde, écumoire.",
  "Les boules dorées qu'on fait frire par dizaines pour les fêtes de fin d'année en Colombie : une pâte à la "
  "fécule de manioc et au fromage frais salé, qui gonfle en boules craquantes et filantes dedans.",
  [f"200 g|de fécule de manioc (tapioca, à défaut maïzena)|Fécule de maïs (maïzena)|3", f"150 g|de queso fresco ou de feta émiettée|{QF}|3",
   f"2|œufs|{OEUF}|2", f"2 c. à s.|de sucre|{SUCRE}|1", f"1 c. à c.|de levure chimique|{LEVC}|1",
   f"1 pincée|de sel|{SEL}|1", f"1 l|d'huile de friture|{HN}|2"],
  ["**Pâte.** Fécule de manioc, fromage émietté, œufs, sucre, levure et sel mélangés à la main (ou au robot) "
   "jusqu'à pâte souple, un peu collante, qui se tient en boule.",
   "**Façonner.** Boules de 4 cm roulées entre les paumes légèrement huilées (la pâte colle).",
   "**Frire.** Huile à 160 °C (plus douce que pour des beignets classiques, sinon l'extérieur brûle avant que "
   "l'intérieur ne gonfle) ; boules frites par petites fournées 6 à 8 min en les retournant souvent, jusqu'à bien "
   "dorées partout et gonflées : elles doublent de volume et flottent en tournant toutes seules.",
   "**Servir.** Égouttées sur grille, tièdes : craquantes dehors, filantes et moelleuses dedans grâce au fromage."],
  tips=["Une huile trop chaude fait brunir l'extérieur avant que le centre ne cuise, et elles retombent en "
        "refroidissant : mieux vaut une friture douce et un peu plus longue.", "Les enfants roulent très bien les "
        "boules."],
  keep="Le jour même, meilleurs chauds ou tièdes ; se ramollissent en refroidissant.", age=2,
  kids="✓ dès 2 ans. Les enfants façonnent les boules.", cats=["enfants", "vegetarien", "fetes"],
  fetes=["Noël et Nouvel An"], profil=["gras"])
K("obleas_dulce_de_leche", "Obleas (gaufrettes fines au dulce de leche, fromage et fruits)", "Obleas", CO, "D", 1, 4, 10, 0, "€",
  "Aucun matériel particulier (gaufrettes du commerce).",
  "Le dessert de rue le plus simple de Colombie, qu'on monte à la demande sur un chariot : deux fines gaufrettes "
  "rondes et craquantes, généreusement tartinées de dulce de leche, parfois de fromage frais émietté et de confiture "
  "de fruits, empilées comme un sandwich sucré.",
  [f"8|gaufrettes rondes fines (obleas, ou gaufrettes à hostie)|{SEMFINE}|2", f"200 g|de dulce de leche|{DULCE}|3",
   f"4 c. à s.|de fromage frais émietté (queso fresco, facultatif)|{QF}|1?", "4 c. à s.|de confiture de fruits (mûre, framboise, facultatif)|Confiture / gelée|1?"],
  ["**Tartiner.** Une gaufrette posée à plat, dulce de leche étalé généreusement jusqu'aux bords à la cuillère.",
   "**Garnir.** Fromage frais émietté et/ou une cuillerée de confiture par-dessus, selon l'envie.",
   "**Fermer.** Une seconde gaufrette posée dessus, légèrement pressée pour que ça tienne sans casser.",
   "**Servir.** Aussitôt : les gaufrettes ramollissent si elles attendent trop longtemps."],
  tips=["Ne se prépare qu'à la demande, juste avant de manger : les gaufrettes perdent leur croquant en 10 à "
        "15 minutes.", "Sans obleas spécifiques, de fines gaufrettes à glace rondes font une bonne alternative."],
  keep="À monter et manger dans les minutes qui suivent.", age=2, kids="✓ dès 2 ans. Les enfants tartinent et "
       "montent eux-mêmes.", cats=["enfants", "vegetarien", "express"], profil=["sucre"])
K("completo_italiano", "Completo italiano (hot-dog chilien à l'avocat, tomate et mayonnaise)", "Completo italiano", CL, "P", 1, 4, 15, 10, "€",
  "Poêle, grille-pain ou four.",
  "Le hot-dog national du Chili, surnommé « italien » pour ses couleurs du drapeau : une saucisse dans un pain "
  "moelleux, couverte d'une épaisse couche d'avocat écrasé, de dés de tomate et d'un trait généreux de mayonnaise, "
  "qu'on mange à pleines mains.",
  [f"4|saucisses de bœuf ou de volaille type knacki|{SAUCISSE_VOL}|3", "4|pains à hot-dog moelleux|Brioche|2",
   f"2|avocats bien mûrs, écrasés à la fourchette|Avocat|2", f"2|tomates, en petits dés, égouttées|{TOM}|2",
   f"8 c. à s.|de mayonnaise|Mayonnaise industrielle|2", f"-|sel|{SEL}|1"],
  ["**Saucisses.** Pochées 5 min à l'eau frémissante ou dorées 5 min à la poêle, selon le type ; égouttées.",
   "**Avocat.** Écrasé à la fourchette avec une pincée de sel, pas en purée lisse : il doit garder un peu de "
   "texture.",
   "**Tomate.** Dés égouttés quelques minutes dans une passoire pour qu'ils ne détrempent pas le pain.",
   "**Pain.** Légèrement grillé au four ou au grille-pain, ouvert en deux sans le séparer complètement.",
   "**Monter.** Saucisse dans le pain, avocat écrasé généreusement sur toute la longueur, dés de tomate par-dessus, "
   "mayonnaise en lignes croisées sur le dessus. On le mange tout de suite, avant que l'avocat ne s'oxyde."],
  tips=["L'avocat noircit vite une fois écrasé : prépare-le en dernier, juste avant de monter les sandwichs.",
        "Pour les enfants, moins de mayonnaise et des dés de tomate plus petits tiennent mieux dans le pain."],
  var=[("Sans porc", ["pork"], {SAUCISSE_VOL: [(SAUCISSE_VOL, 1.0)]}, "Déjà bœuf/volaille par défaut ; vérifier l'étiquette des saucisses prêtes à l'emploi.")],
  keep="À monter et manger aussitôt (l'avocat noircit).", age=2, kids="✓ dès 2 ans, moins de mayonnaise.",
  cats=["enfants", "express"], profil=["gras"])
