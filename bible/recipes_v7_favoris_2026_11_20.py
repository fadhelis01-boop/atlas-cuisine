# -*- coding: utf-8 -*-
"""Favoris TikTok du 20/11/2026 (favoris ajoutés depuis le 10-11/11, compte connecté par le propriétaire) et comblement
des angles morts du catalogue. 18 fiches nouvelles, créditées, sans doublon avec l'existant (vérifié un par un : riz au
gras et « gbonlant dessi » ont failli faire doublon avec gboma_dessi déjà présent — seul gbonlant était un doublon,
retiré). NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *
from recipes_v6_tiktok_plats import C

TT = "https://www.tiktok.com/"
def V(author, vid):
    return (f"@{author}", f"{TT}@{author}/video/{vid}")

TG = "Afrique subsaharienne › Togo"; CI = "Afrique subsaharienne › Côte d'Ivoire"; BJ = "Afrique subsaharienne › Bénin"
MG = "Afrique subsaharienne › Madagascar"; GB = "Europe du Nord › Royaume-Uni"; CH = "Europe du Nord › Suisse"
TR = "Moyen-Orient & Caucase › Turquie"; BA = "Europe du Sud › Bosnie-Herzégovine"; AF = "Asie du Sud › Afghanistan"
IT = "Europe du Sud › Italie"; US = "Amérique du Nord › États-Unis"; FR = "France › Cuisine du quotidien"
CREVSECHE = "Crevettes séchées"; SELNITRITE = "Sel nitrité (charcuterie maison)"; MOZZ = "Mozzarella / burrata"
BASIL = "Basilic"; BOUDOIRS = "Boudoirs / biscuits cuillère"; PISTA = "Pistache"; CORNICHON = "Cornichon"

K("agnamahogo", "Agnamahogo (feuilles de manioc au lait de coco et aux crevettes séchées)", "Agnamahogo", MG, "P", 2, 6, 25, 50, "€€",
  "Grande marmite, mixeur ou pilon.",
  "Le plat du dimanche des hauts plateaux malgaches : des feuilles de manioc pilées puis longuement mijotées dans le "
  "lait de coco, adoucies d'une pointe de sucre et relevées de crevettes séchées en fin de cuisson. Avec du riz blanc.",
  ["800 g|de feuilles de manioc pilées (surgelées, épicerie africaine ; à défaut épinards hachés menu)|Épinard|3",
   f"2 boîtes (400 ml)|de lait de coco|{COCO}|3", f"2|oignons, hachés|{OIG}|2", f"3 gousses|d'ail, hachées|{AIL}|1",
   f"3 c. à s.|de crevettes séchées|{CREVSECHE}|2", f"1 c. à c.|de sucre|{SUCRE}|1", f"1|citron vert (pour servir)|Citron vert|1?", f"-|sel|{SEL}|1"],
  ["**Base.** Feuilles de manioc (ou épinards) mijotés 15 min à feu doux avec l'oignon et l'ail dans un fond d'eau, "
   "jusqu'à bien tendres.",
   "**Lait de coco.** Ajouté en 2 à 3 fois au fil de la cuisson plutôt qu'en une fois, selon la consistance "
   "voulue : plus onctueux à chaque ajout. 20 min à petit frémissement, à découvert, en remuant de temps en temps.",
   "**Assaisonner.** Sucre et sel ajoutés : le sucre adoucit l'amertume naturelle de la feuille.",
   "**Finir.** Crevettes séchées incorporées dans les 5 dernières minutes (plus tôt, elles deviennent caoutchouteuses) ; "
   "goûté, rectifié.",
   "**Servir.** Chaud, avec du riz blanc et un quartier de citron vert pressé dessus au moment de manger."],
  tips=["Les feuilles de manioc surgelées (épicerie africaine) sont déjà pilées et prêtes à cuire : gain de temps "
        "énorme par rapport aux feuilles fraîches.", "Sans crevettes séchées (allergie, végétarien) : un peu de sel "
        "et de poivre suffisent, le plat reste bon."],
  keep="3 jours au frigo ; se congèle.", age=2, kids="✓ dès 2 ans.", cats=[], profil=["gras"],
  credit=C(V("tsara.cuisine", "7688672510279306518")))
K("galette_oignons_pdt_fromage", "Galette anglaise aux oignons caramélisés, pommes de terre et fromage", "Potato & onion galette", GB, "P", 2, 6, 30, 60, "€€",
  "Poêle large, plat à four ou moule à charlotte.",
  "Une galette réconfortante du nord de l'Angleterre : des couches de pommes de terre finement tranchées et "
  "d'oignons longuement caramélisés au thym, gratinées sous le fromage jusqu'à fondantes et dorées.",
  [f"1 kg|de pommes de terre, en tranches très fines (mandoline)|{PDT}|3", f"3|gros oignons, émincés|{OIG}|3",
   f"60 g|de beurre|{BEURRE}|2", f"4 brins|de thym|{THYM}|1", f"150 g|de gruyère ou de cheddar râpé|{GRUY}|2",
   f"20 cl|de crème fraîche|{CF}|2", f"-|sel, poivre|{SEL}|1"],
  ["**Caraméliser.** Oignons fondus dans le beurre, feu doux, 25 à 30 min en remuant souvent, thym effeuillé : "
   "couleur brun doré, bien fondants et tout doux.",
   "**Monter.** Four à 180 °C. Dans un moule beurré : une couche de pommes de terre salées, une couche d'oignons, "
   "un peu de crème et de fromage ; répété jusqu'en haut, fromage sur le dessus.",
   "**Cuire.** Couvert de papier aluminium 35 min, puis découvert 20 à 25 min de plus : pommes de terre fondantes "
   "à la pointe du couteau, dessus bien doré et gratiné.",
   "**Reposer.** 10 min avant de démouler ou de servir à la cuillère : elle se tient mieux tiède."],
  tips=["Des tranches toutes fines et régulières (mandoline) cuisent ensemble sans qu'aucune ne reste crue.",
        "Se prépare la veille, réchauffée 20 min au four."],
  keep="3 jours au frigo.", age=1, kids="✓ dès 1 an.", cats=["enfants", "vegetarien"], profil=["gras"],
  credit=C(V("cheftomwalton", "7361194054840896776")))
K("paleron_boeuf_confit_7h", "Paleron de bœuf confit 7 heures, moelleux à la fourchette", "Slow-cooked beef chuck", FR, "P", 2, 6, 25, 420, "€€",
  "Cocotte en fonte allant au four.",
  "Le paleron, morceau peu cher et plein de collagène, devient fondant et se mange à la cuillère après une très "
  "longue et très douce cuisson au four : à lancer le matin pour le soir, ou la veille pour le lendemain.",
  [f"1,5 kg|de paleron de bœuf, en un seul morceau|Paleron|3", f"3|carottes, en tronçons|{CAROTTE}|2",
   f"2|oignons, en quartiers|{OIG}|2", f"4 gousses|d'ail en chemise|{AIL}|1", f"3 brins|de thym|{THYM}|1",
   f"2|feuilles de laurier|{LAURIER}|1", f"50 cl|de bouillon de bœuf|{BOUILLON}|2", f"3 c. à s.|d'huile|{HN}|1",
   f"1|citron (zeste, pour la gremolata)|{CIT}|1?", f"1/2 bouquet|de persil (pour la gremolata)|{PERSIL}|1?",
   f"-|sel, poivre|{SEL}|1"],
  ["**Saisir.** Four à 110 °C. Paleron doré sur toutes les faces à l'huile dans la cocotte chaude, 8 à 10 min : "
   "croûte brune, surface qui ne colle plus.",
   "**Réunir.** Carottes, oignons, ail, thym, laurier autour de la viande ; bouillon versé à mi-hauteur ; sel, "
   "poivre.",
   "**Confire.** Couvercle fermé, 7 h au four à 110 °C, sans ouvrir : la viande se détache en filaments sous une "
   "simple pression de fourchette, le jus est devenu un fond sirupeux.",
   "**Servir.** Tranché ou effiloché à la fourchette, nappé de son jus, avec une purée et une gremolata (zeste "
   "de citron et persil hachés ensemble) parsemée dessus : sa fraîcheur acidulée réveille le plat très riche."],
  tips=["Une cuisson aussi longue et douce pardonne tout : 30 min de plus ou de moins ne changent rien.",
        "Encore meilleur réchauffé le lendemain : le jus a eu le temps de bien imprégner la viande."],
  keep="3 jours au frigo ; se congèle en portions avec son jus.", age=1, kids="✓ dès 1 an.", cats=["enfants"],
  fetes=["Repas de famille"], profil=["gras"], credit=C(V("bellymedia", "7581069041519856919")))
K("pain_a_kebab_turc", "Pain à kebab turc moelleux (pour döner et dürüm)", "Kebab ekmeği", TR, "Pa", 2, 8, 20, 90, "€",
  "Four, plaque de cuisson, rouleau à pâtisserie.",
  "Le pain plat et moelleux qui enveloppe le kebab turc à la maison : une pâte levée simple, étalée en ovale, "
  "cuite très chaud en quelques minutes pour qu'elle gonfle et reste souple, jamais sèche.",
  [f"500 g|de farine|{F55}|3", f"7 g|de levure boulangère sèche|{LEV}|2", f"1 c. à c.|de sel|{SEL}|1",
   f"1 c. à c.|de sucre|{SUCRE}|1", f"3 c. à s.|d'huile d'olive|{HO}|2", f"30 cl|d'eau tiède|{EAU}|2"],
  ["**Pâte.** Levure et sucre dissous dans l'eau tiède, 5 min ; farine, sel et huile ajoutés, pétris 8 à 10 min "
   "jusqu'à pâte souple et élastique ; 1 h de pousse couverte, à température ambiante : elle double de volume.",
   "**Façonner.** Dégazée, divisée en 6 à 8 pâtons, boulés ; 15 min de repos sous un torchon.",
   "**Étaler.** Chaque pâton étalé en ovale de 5 mm d'épaisseur.",
   "**Cuire.** Four à 250 °C (ou le plus chaud possible), plaque déjà chaude ; pains cuits 3 à 4 min par face : "
   "ils gonflent et se colorent de taches dorées, restent souples.",
   "**Garder souple.** Empilés sous un torchon propre dès la sortie du four : la vapeur les garde moelleux."],
  tips=["La plaque doit déjà être chaude au four avant d'y poser le pain : c'est le choc de chaleur qui le fait "
        "gonfler.", "Se congèlent cuits, réchauffés 2 min au four ou à la poêle avant de garnir."],
  keep="2 jours à température ambiante dans un sac ; se congèlent.", age=1, kids="✓ dès 1 an.",
  cats=["enfants", "vegetarien"], profil=["leger"], credit=C(V("ammey.food", "7705110493689662753")))
K("tchantchanga", "Tchantchanga (brochettes de bœuf épicées, street food béninoise)", "Tchantchanga", BJ, "P", 1, 6, 25, 15, "€€",
  "Brochettes en bois (trempées 30 min), barbecue ou gril de four.",
  "Les brochettes de rue les plus populaires du Bénin : des cubes de bœuf bien gras marinés aux épices sèches et "
  "au piment, grillés très vifs jusqu'à bien caramélisés dehors, servis avec un oignon cru et du piment en poudre "
  "à table.",
  [f"900 g|de bœuf à brochette, bien persillé, en cubes de 3 cm|{HACHE}|3", f"2 c. à s.|d'huile|{HN}|1",
   f"1 c. à s.|de paprika|{PAPRIKA}|1", f"1 c. à c.|de cumin|{CUMIN}|1", f"1 c. à c.|de gingembre en poudre|{GING}|1",
   f"1 c. à c.|de piment en poudre|{CAYENNE}|1", f"3 gousses|d'ail, écrasées|{AIL}|1", f"-|sel|{SEL}|1",
   f"1|oignon, en quartiers (pour servir)|{OIG}|1?", f"1|citron (pour servir)|{CIT}|1?"],
  ["**Mariner.** Cubes de bœuf enrobés d'huile, épices, ail et sel ; au moins 1 h au frigo (toute une nuit pour "
   "plus de goût).",
   "**Embrocher.** Cubes enfilés serrés sur les brochettes, sans trop les tasser (ils doivent dorer sur toutes "
   "les faces).",
   "**Griller.** Braise vive ou gril de four au maximum ; 3 à 4 min par face, retournées souvent : bien "
   "caramélisées et marquées dehors, encore juteuses dedans.",
   "**Servir.** Aussitôt, avec l'oignon cru en quartiers, un quartier de citron et du piment en poudre à part."],
  tips=["Un bœuf bien persillé (pas trop maigre) reste juteux à la cuisson très vive ; un morceau trop sec durcit.",
        "Brochettes en bois trempées 30 min dans l'eau froide avant : elles ne brûlent pas sur le gril."],
  keep="2 jours au frigo, marinées crues ou grillées.", age=4, kids="✓ dès 4 ans, moins pimenté.", cats=[],
  profil=["epice", "acide"], credit=C(V("suskaymanagement", "7709820269241617684")))
K("somun", "Somun (pain plat bosniaque, moelleux et gonflé)", "Somun", BA, "Pa", 2, 6, 20, 90, "€",
  "Four très chaud, plaque, torchon propre.",
  "Le pain traditionnel des Balkans qui accompagne le ćevapi : une pâte levée simple, façonnée en disques, cuite "
  "très chaud pour qu'elle gonfle en formant une grande poche d'air entre deux croûtes fines et moelleuses.",
  [f"500 g|de farine|{F55}|3", f"7 g|de levure boulangère sèche|{LEV}|2", f"1 c. à c.|de sucre|{SUCRE}|1",
   f"1 c. à c.|de sel|{SEL}|1", f"30 cl|d'eau tiède|{EAU}|2", f"2 c. à s.|d'huile|{HN}|1"],
  ["**Pâte.** Levure et sucre dissous dans l'eau tiède, 5 min ; farine, sel et huile incorporés, pétris 8 à "
   "10 min : pâte souple et lisse ; 1 h de pousse couverte, à température ambiante.",
   "**Façonner.** Dégazée, divisée en 4 à 6 pâtons, aplatis à la main en disques de 2 cm d'épaisseur ; 20 min de "
   "repos sous un torchon.",
   "**Cuire.** Four préchauffé le plus chaud possible (250 °C), plaque déjà très chaude ; pains cuits 8 à 10 min : "
   "ils gonflent nettement et forment une poche d'air, dessus doré.",
   "**Servir.** Tièdes, ouverts en portefeuille pour y glisser de la viande grillée, ou nature avec un peu "
   "d'huile d'olive."],
  tips=["La poche d'air se forme grâce à la vapeur et à la chaleur très vive : un four pas assez chaud donne un "
        "pain plat et dense.", "Se congèlent cuits ; réchauffés 3 min au four."],
  keep="2 jours à température ambiante ; se congèlent.", age=1, kids="✓ dès 1 an.", cats=["enfants", "vegetarien"],
  profil=["leger"], credit=C(V("midia.mhd", "7705819428763520289")))
K("pain_brochette_ivoirien", "Pain brochette ivoirien (sandwich de rue à Abidjan)", "Pain brochette", CI, "P", 1, 4, 20, 15, "€€",
  "Brochettes, gril ou barbecue.",
  "Le sandwich qu'on s'arrache dans les rues d'Abidjan : des brochettes de bœuf grillées au charbon, glissées "
  "toutes chaudes dans une demi-baguette avec oignon cru, tomate et une pointe de piment.",
  [f"600 g|de bœuf à brochette, en cubes|{HACHE}|3", f"2 c. à s.|d'huile|{HN}|1", f"1 c. à c.|de paprika|{PAPRIKA}|1",
   f"1 c. à c.|de cube de bouillon émietté|Bouillon cube bœuf|1?", f"2 gousses|d'ail, écrasées|{AIL}|1",
   f"2|baguettes, coupées en deux et creusées|Baguette tradition|2", f"1|oignon, émincé|{OIG}|1",
   f"2|tomates, en rondelles|{TOM}|1", f"1 c. à c.|de piment en poudre (à part)|{CAYENNE}|1?", f"-|sel|{SEL}|1"],
  ["**Mariner.** Cubes de bœuf enrobés d'huile, paprika, bouillon émietté, ail et sel ; 1 h au frigo au moins.",
   "**Embrocher et griller.** Enfilés sur les brochettes, grillés au charbon ou au gril très chaud, 6 à 8 min en "
   "les tournant : bien dorés et caramélisés dehors.",
   "**Monter.** Pain légèrement creusé et grillé quelques secondes côté charbon ; brochettes désembrochées "
   "directement dans le pain, oignon et tomate ajoutés, piment à volonté.",
   "**Servir.** Aussitôt, tant que la viande et le pain sont encore chauds."],
  tips=["Désembrocher directement dans le pain (et non dans une assiette) garde tout le jus de la viande pour le "
        "sandwich.", "Sans charbon : un gril en fonte très chaud sur le feu donne un résultat très proche."],
  keep="À manger aussitôt.", age=3, kids="✓ dès 3 ans, moins pimenté.", cats=["express"], profil=["gras"],
  credit=C(V("aidyskitchen", "7709245680509914400")))
K("limonade_suisse", "Limonade suisse crémeuse (citron, lait et sucre)", "Limmilemonade", CH, "B", 1, 6, 10, 0, "€",
  "Mixeur ou blender.",
  "La limonade d'été la plus bue en Suisse alémanique : du jus de citron, du lait et du sucre mixés ensemble, qui "
  "donnent une boisson trouble, crémeuse et rafraîchissante, à servir bien glacée.",
  [f"4|citrons (jus)|{CIT}|2", f"1 l|de lait entier bien froid|{LAIT}|3", f"120 g|de sucre|{SUCRE}|2",
   f"1 c. à c.|de vanille en poudre (facultatif)|{VAN}|1?", f"-|glaçons|-|1?"],
  ["**Presser.** Citrons pressés, pépins retirés.",
   "**Mixer.** Jus de citron, lait, sucre et vanille mixés ensemble 30 secondes : la boisson mousse légèrement et "
   "devient trouble et crémeuse (le lait caille très légèrement au contact du citron, c'est normal et voulu).",
   "**Filtrer.** Passée au tamis fin si on veut une boisson bien lisse (facultatif : la version non filtrée est "
   "la plus traditionnelle, avec ses petits grains de lait caillé).",
   "**Servir.** Aussitôt, sur glaçons, bien froide."],
  tips=["Elle se sépare un peu si elle attend : un coup de mixeur ou de fouet juste avant de servir la remet "
        "crémeuse.", "Le lait doit être bien froid : tiède, le mélange tourne de façon désagréable."],
  keep="Le jour même, mixée à nouveau avant de servir.", age=2, kids="✓ dès 2 ans.", cats=["enfants", "vegetarien", "boissons"],
  profil=["sucre", "acide"], credit=C(V("chef.paprika", "7700190623340547360")))
K("duchess_potatoes", "Duchess potatoes (pommes de terre duchesse, ail et herbes)", "Duchess potatoes", GB, "A", 2, 6, 25, 20, "€",
  "Presse-purée ou moulin à légumes, poche à douille cannelée, plaque de four.",
  "La purée de pommes de terre transformée en petites rosaces dorées au four : enrichie de jaunes d'œufs, de "
  "beurre et d'ail, elle gonfle et dore sans jamais s'affaisser, pour un accompagnement qui change de la purée "
  "simple.",
  [f"1 kg|de pommes de terre à purée|{PDT}|3", f"80 g|de beurre|{BEURRE}|2", f"3|jaunes d'œufs|{OEUF}|2",
   f"2 gousses|d'ail, écrasées|{AIL}|1", f"1 pincée|de muscade|{MUSC}|1", f"2 c. à s.|de persil ciselé|{PERSIL}|1?",
   f"1|œuf (pour dorer)|{OEUF}|1", f"-|sel, poivre|{SEL}|1"],
  ["**Cuire et sécher.** Pommes de terre cuites à l'eau salée 20 min, égouttées, repassées 1 min à feu doux dans "
   "la casserole vide pour qu'elles sèchent bien : purée sèche = rosaces qui tiennent.",
   "**Purée.** Écrasées au presse-purée (jamais au robot, qui les rend collantes) ; beurre, ail, muscade "
   "incorporés chauds ; jaunes d'œufs ajoutés hors du feu un par un, en fouettant.",
   "**Dresser.** Four à 200 °C. Purée encore tiède mise en poche à douille cannelée ; rosaces de 6 cm dressées sur "
   "une plaque chemisée, dorées à l'œuf battu au pinceau.",
   "**Cuire.** 18 à 20 min : bien dorées et légèrement craquantes sur les pointes, moelleuses dedans."],
  tips=["La purée doit être assez ferme pour tenir sa forme à la poche : si elle est trop molle, repasse-la 1 min "
        "à feu doux avant de dresser.", "Se dressent cru à l'avance, au frigo, et se cuisent au dernier moment."],
  keep="Crues dressées, 1 jour au frigo ; cuites, 2 jours (recroustillées au four).", age=2,
  kids="✓ dès 2 ans. Les enfants dressent les rosaces.", cats=["enfants", "vegetarien"], profil=["gras"],
  credit=C(V("chefalextrim", "7407095644277558559")))
K("cube_bouillon_maison", "Arôme « Maggi » maison (cube de bouillon concentré sans additif)", "Homemade stock cube", FR, "Ba", 1, 20, 30, 40, "€",
  "Mixeur, poêle, bacs à glaçons ou petit plat.",
  "L'arôme qui parfume tant de plats du quotidien, fait soi-même sans exhausteurs de goût ni huile de palme : des "
  "légumes, des herbes et du sel mixés puis légèrement déshydratés en pâte concentrée, à utiliser comme un cube "
  "du commerce.",
  [f"2|carottes|{CAROTTE}|2", f"2|oignons|{OIG}|2", f"2|branches de céleri|Céleri-branche|2",
   f"4 gousses|d'ail|{AIL}|1", f"1/2 bouquet|de persil|{PERSIL}|1", f"150 g|de gros sel|{SEL}|3",
   f"2 c. à s.|d'huile d'olive|{HO}|1", f"1 c. à c.|de poivre|{POIVRE}|1?"],
  ["**Mixer.** Légumes et herbes lavés, grossièrement coupés, mixés avec le sel, l'huile et le poivre jusqu'à une "
   "pâte fine et homogène : le sel sert à la fois d'assaisonnement et de conservateur.",
   "**Concentrer.** Étalée sur 1 cm dans un plat ou une poêle à feu très doux, 25 à 30 min en remuant souvent : "
   "l'eau des légumes s'évapore, la pâte devient plus foncée et brillante, sans brûler.",
   "**Conserver.** Versée encore chaude dans des petits pots ou des bacs à glaçons ; complètement refroidie avant "
   "de fermer.",
   "**Utiliser.** 1 à 2 c. à c. par litre de bouillon ou par plat, à la place d'un cube du commerce."],
  tips=["Le sel (environ 20 % du poids) est ce qui permet de la garder plusieurs semaines sans ferment ni "
        "conservateur ajouté : ne pas en réduire la quantité.", "Se congèle très bien en cubes individuels, "
        "pratique à doser."],
  keep="1 mois au frigo dans un bocal fermé ; plusieurs mois au congélateur en cubes.", age=None,
  kids="Pour les adultes (dosage de sel à l'aveugle) ; les enfants mixent les légumes.", cats=["vegetarien", "zero_dechet"],
  profil=["leger"], credit=C(V("les.atypiques.en.cuisine", "7694676381682240800")))
K("choukouya_poulet", "Choukouya de poulet (poulet braisé à l'ivoirienne, sauce pimentée)", "Choukouya", CI, "P", 1, 4, 25, 40, "€€",
  "Four ou barbecue, poêle.",
  "Le poulet grillé le plus demandé des maquis d'Abidjan : mariné au nokoss, braisé jusqu'à la peau bien colorée, "
  "puis nappé d'une sauce tomate-oignon relevée. Avec de l'attiéké ou de l'alloco.",
  [f"1,2 kg|de hauts de cuisse de poulet, avec la peau|{CUISSE}|3", "4 c. à s.|de nokoss (marinade liée)|SUB:nokoss|2",
   f"2|oignons, émincés|{OIG}|2", f"2|oignons rouges, émincés|{OIG}|1", f"3|tomates, en dés|{TOM}|2",
   f"1 c. à c.|de paprika|{PAPRIKA}|1", f"2 c. à s.|de mayonnaise|Mayonnaise industrielle|1",
   f"1 c. à c.|de moutarde|{DIJON}|1", f"1/2 bouquet|de persil|{PERSIL}|1?", f"3 c. à s.|d'huile|{HN}|1",
   f"-|sel, poivre|{SEL}|1"],
  ["**Mariner.** Poulet enrobé de nokoss, sel et poivre ; 1 h au frigo au moins.",
   "**Braiser.** Four à 200 °C ou barbecue, 30 à 35 min en retournant à mi-cuisson : peau bien colorée et "
   "croustillante, chair cuite à cœur (jus clair).",
   "**Sauce.** Oignons fondus à l'huile 8 min, tomates et paprika ajoutés, 10 min de plus jusqu'à épaissir ; "
   "mayonnaise et moutarde incorporées hors du feu.",
   "**Servir.** Poulet nappé de sauce, persil ciselé, avec de l'attiéké ou de l'alloco (banane plantain frite)."],
  tips=["Le nokoss (ail, piment, poivron, persil pilés) est ce qui fait tout le goût : sans lui, c'est juste un "
        "poulet grillé ordinaire.", "La mayonnaise dans la sauce chaude est une habitude locale, elle l'épaissit "
        "et l'adoucit : à ajouter hors du feu pour qu'elle ne tranche pas."],
  keep="2 jours au frigo.", age=3, kids="✓ dès 3 ans, sauce moins pimentée.", cats=[], profil=["epice", "gras"],
  credit=C(V("chef_thed", "7706578230274231584")))
K("riz_au_gras_togolais", "Riz au gras togolais (riz à la viande et à la tomate)", "Riz au gras", TG, "P", 1, 6, 20, 40, "€",
  "Grande cocotte.",
  "Le riz du quotidien le plus courant au Togo et en Afrique de l'Ouest : du riz cuit directement dans une sauce "
  "tomate-oignon avec de la viande, qui prend une belle couleur orangée et un goût concentré. Plus simple et "
  "moins épicé que le riz jollof des grandes occasions.",
  [f"400 g|de riz long|{RIZ}|3", f"500 g|de bœuf ou de poulet, en morceaux|{HACHE}|3", f"3|tomates, mixées|{TOM}|2",
   f"2 c. à s.|de concentré de tomate|{CONC}|1", f"2|oignons, hachés|{OIG}|2", f"3 gousses|d'ail, hachées|{AIL}|1",
   f"2 c. à s.|d'huile|{HN}|2", f"1|cube de bouillon|Bouillon cube bœuf|1?", f"1 c. à c.|de piment en poudre (facultatif)|{CAYENNE}|1?",
   f"-|sel|{SEL}|1"],
  ["**Dorer la viande.** Morceaux de viande dorés à l'huile dans la cocotte, 8 min ; oignon et ail ajoutés, 5 min "
   "de plus.",
   "**Sauce.** Tomates mixées, concentré, cube et piment ajoutés ; 10 min à feu moyen : la sauce épaissit et "
   "fonce.",
   "**Cuire le riz.** Riz rincé ajouté directement dans la sauce, eau à hauteur (environ 1,5 fois le volume de "
   "riz) ; porté à ébullition puis couvert, feu très doux, 20 à 25 min sans soulever le couvercle : le riz absorbe "
   "toute la sauce et prend une couleur orangée uniforme.",
   "**Reposer.** 5 min hors du feu, couvercle toujours fermé, puis égrainé à la fourchette."],
  tips=["Ne pas soulever le couvercle pendant la cuisson : la vapeur qui s'échappe est ce qui cuit le riz "
        "uniformément.", "Un reste de riz au gras se réchauffe très bien à la poêle avec un peu d'eau."],
  keep="3 jours au frigo ; se réchauffe à la poêle.", age=1, kids="✓ dès 1 an.", cats=["enfants"],
  profil=["acide"], credit=C(V("saf.kitchenn", "7707727165579676961")))
K("borani_banjan", "Borani banjan (aubergines frites, sauce tomate et yaourt à l'ail, Afghanistan)", "بورانی بادنجان", AF, "E", 1, 4, 20, 25, "€",
  "Poêle, passoire.",
  "Le classique afghan des grandes tables : des tranches d'aubergine frites jusqu'à fondantes, nappées d'une "
  "sauce tomate à l'ail et à la menthe, servies tièdes sur un lit de yaourt épais à l'ail. Avec du pain plat.",
  [f"2|aubergines, en tranches de 1 cm|Aubergine|3", f"-|sel (pour dégorger)|{SEL}|1",
   f"4 c. à s.|d'huile (friture ou poêle)|{HN}|2", f"3|tomates, en dés (ou 1 boîte de pelées)|{TOM}|2",
   f"4 gousses|d'ail, hachées|{AIL}|2", f"1 c. à c.|de menthe séchée|Menthe|1",
   f"1/2 c. à c.|de curcuma|{CURC}|1?", f"300 g|de yaourt grec épais|{GREC}|2", f"1 gousse|d'ail, écrasée (pour le yaourt)|{AIL}|1",
   f"-|poivre|{POIVRE}|1"],
  ["**Dégorger.** Tranches d'aubergine salées des deux côtés, 20 min sur une grille : elles rendent leur eau et "
   "absorbent moins d'huile à la cuisson ; épongées.",
   "**Frire.** À la poêle avec l'huile, 3 à 4 min par face à feu moyen-vif, par fournées : bien dorées et "
   "fondantes ; égouttées sur papier absorbant.",
   "**Sauce.** Ail fondu 1 min dans un fond d'huile, tomates et curcuma ajoutés, 12 à 15 min à feu moyen : "
   "épaisse ; menthe et poivre en fin de cuisson.",
   "**Monter.** Yaourt mélangé à l'ail écrasé et une pincée de sel, étalé dans le plat ; aubergines frites "
   "disposées dessus, sauce tomate versée par-dessus.",
   "**Servir.** Tiède, avec du pain plat pour saucer."],
  tips=["Dégorger les aubergines est l'étape qui évite qu'elles boivent toute l'huile : ne la saute pas, même "
        "pressé.", "Se prépare en deux temps à l'avance (aubergines frites, sauce) et se monte juste avant de "
        "servir."],
  keep="2 jours au frigo, les trois éléments séparés.", age=2, kids="✓ dès 2 ans.", cats=["enfants", "vegetarien"],
  profil=["acide", "gras"], credit=C(V("dr.vegans", "7438871052337433888")))
K("panuzzo", "Panuzzo (pain italien fourré et cuit au four, façon panino chaud)", "Panuzzo", IT, "P", 2, 4, 25, 20, "€€",
  "Four, plaque de cuisson.",
  "Le sandwich italien qui se cuit comme une pizza repliée : une pâte à pizza garnie de charcuterie, de "
  "mozzarella et de légumes, refermée en chausson et dorée au four jusqu'à ce que le fromage file à l'intérieur.",
  [f"500 g|de pâte à pizza (recette liée ou toute prête)|{F55}|3", "150 g|de jambon de dinde ou de poulet|Jambon de dinde / de poulet|2",
   f"200 g|de mozzarella, en tranches|{MOZZ}|3", f"2|tomates, en rondelles|{TOM}|2", f"1/2 bouquet|de basilic|{BASIL}|1",
   f"3 c. à s.|d'huile d'olive|{HO}|1", f"-|sel, origan|{SEL}|1"],
  ["**Étaler.** Four à 220 °C. Pâte étalée en grand disque fin sur un plan fariné.",
   "**Garnir.** Jambon, mozzarella, tomates et basilic disposés sur une moitié du disque, en laissant 2 cm de "
   "bord libre ; huile, sel, origan.",
   "**Refermer.** Pâte repliée en chausson, bords pincés fermement (comme un gros chausson aux pommes salé) pour "
   "que le fromage ne coule pas à la cuisson.",
   "**Cuire.** Sur une plaque chaude, 18 à 20 min : doré, gonflé, le fromage a fondu à l'intérieur (on l'entend "
   "presque grésiller).",
   "**Reposer.** 5 min avant de trancher : le fromage fondu se tient mieux."],
  tips=["Mal scellé, le panuzzo s'ouvre et le fromage coule à la cuisson : presse bien les bords, humidifiés si "
        "besoin.", "Se mange chaud ou tiède, jamais froid (le fromage fige et devient caoutchouteux)."],
  keep="Le jour même, réchauffé 5 min au four.", age=2, kids="✓ dès 2 ans.", cats=["enfants"], profil=["gras"],
  credit=C(V("casapori.france", "7706617791469669664")))
K("french_dip_sandwich", "French dip sandwich (rosbif tranché fin, jus à tremper)", "French dip", US, "P", 2, 4, 20, 180, "€€",
  "Cocotte, four, tranchoir ou couteau bien aiguisé.",
  "Le sandwich américain né à Los Angeles : un rosbif longuement rôti, tranché très fin, empilé dans un pain "
  "croustillant, qu'on trempe directement dans son jus de cuisson concentré avant chaque bouchée.",
  [f"1,2 kg|de rumsteck ou de rond de gîte, en un seul morceau|Rumsteck|3",
   f"2 c. à s.|d'huile|{HN}|1", f"1|oignon, émincé|{OIG}|1", f"3 gousses|d'ail, écrasées|{AIL}|1",
   f"75 cl|de bouillon de bœuf|{BOUILLON}|3", f"1 c. à s.|de sauce soja|{SOJA}|1",
   f"4|pains à sandwich croustillants (type sous-marin)|Baguette tradition|2",
   f"150 g|de provolone ou de gruyère, en tranches|{GRUY}|2", f"8|cornichons (pour servir)|{CORNICHON}|1?",
   f"-|sel, poivre|{SEL}|1"],
  ["**Saisir.** Four à 150 °C. Viande salée, poivrée, dorée sur toutes les faces à l'huile en cocotte, 8 à 10 min.",
   "**Rôtir.** Oignon et ail ajoutés autour, bouillon versé, soja ; couvert, 2 h 30 à 3 h au four à 150 °C : la "
   "viande est très tendre, se tranche sans effort.",
   "**Trancher.** Viande reposée 15 min, puis tranchée la plus fine possible, contre les fibres ; jus de cuisson "
   "filtré, dégraissé, réservé chaud dans de petits bols.",
   "**Monter.** Pain légèrement grillé, fromage fondu dessus sous le gril 2 min, tranches de viande empilées "
   "généreusement.",
   "**Servir.** Avec un bol de jus chaud à part et des cornichons : chaque bouchée se trempe avant de croquer."],
  tips=["Trancher la viande froide (ou juste tiède) donne des tranches bien plus fines et nettes qu'à chaud.",
        "Le jus se prépare très bien la veille, il ne fait que gagner en goût réchauffé."],
  keep="Viande et jus séparés, 3 jours au frigo.", age=2, kids="✓ dès 2 ans.", cats=["enfants"], profil=["gras"],
  credit=C(V("thesapor", "7706580740296756510")))
K("eclair_cake_sans_cuisson", "Éclair cake sans cuisson (biscuits, crème pâtissière, glaçage chocolat)", "No-bake eclair cake", US, "D", 1, 10, 25, 240, "€€",
  "Plat rectangulaire, fouet.",
  "Le dessert qui a tout du goût d'un éclair au café sans jamais allumer le four : des couches de biscuits à la "
  "cuillère imbibés, de crème pâtissière à la vanille et d'un glaçage au chocolat, à découper en parts bien "
  "nettes après une nuit au frigo.",
  [f"400 g|de boudoirs ou de biscuits à la cuillère|{BOUDOIRS}|3",
   f"1 l|de crème pâtissière froide (recette liée ou toute prête)|{LAIT}|3",
   f"150 g|de chocolat noir|{CHOCO}|2", f"10 cl|de crème fleurette|{CL}|1",
   f"2 c. à s.|de sucre glace|Sucre glace|1?"],
  ["**Première couche.** Biscuits disposés côte à côte au fond d'un plat rectangulaire, pour couvrir toute la "
   "surface.",
   "**Crème.** Moitié de la crème pâtissière étalée en couche égale sur les biscuits.",
   "**Répéter.** Une deuxième couche de biscuits, le reste de la crème, puis une troisième couche de biscuits "
   "tout en haut.",
   "**Glaçage.** Chocolat et crème fleurette fondus ensemble au bain-marie ou 1 min au micro-ondes, lissés ; "
   "versé sur le dessus et étalé jusqu'aux bords.",
   "**Reposer.** Au moins 4 h au frigo, idéalement toute une nuit : les biscuits s'imbibent et se détendent, le "
   "gâteau se tranche alors net comme un vrai gâteau."],
  tips=["Il faut vraiment attendre le lendemain pour le trancher net : la veille, les biscuits sont encore trop "
        "fermes et ça s'effondre.", "Une pointe de café fort dans la crème pâtissière rapproche encore plus du "
        "goût de l'éclair classique."],
  keep="4 jours au frigo, couvert.", age=2, kids="✓ dès 2 ans.", cats=["enfants", "vegetarien", "fetes"],
  profil=["sucre", "gras"], credit=C(V("amber_recipes", "7704786060269604110")))
K("gnocchi_pain_rassis", "Gnocchi de pain rassis (zéro déchet, parmesan et sauge)", "Canederli / gnocchi di pane", IT, "P", 1, 4, 20, 15, "€",
  "Grande casserole, écumoire.",
  "La façon la plus gourmande de ne rien jeter du pain de la veille : trempé dans le lait, mêlé à l'œuf, à la "
  "farine et au parmesan, façonné en petites boulettes pochées puis juste dorées au beurre et à la sauge.",
  [f"300 g|de pain rassis (baguette, pain de campagne), en dés|Pain rassis (réservé)|3", f"20 cl|de lait tiède|{LAIT}|2",
   f"2|œufs|{OEUF}|2", f"60 g|de parmesan râpé|{PARM}|2", f"80 g|de farine (et un peu pour fariner les mains)|{F55}|2",
   f"1/2 bouquet|de persil, haché|{PERSIL}|1?", f"50 g|de beurre|{BEURRE}|1", f"6 feuilles|de sauge|Sauge|1?",
   f"2 c. à c.|de vinaigre balsamique (pour servir)|Vinaigre balsamique|1?", f"-|sel, muscade|{SEL}|1"],
  ["**Tremper.** Dés de pain arrosés de lait tiède, 15 min, en pressant de temps en temps : ils doivent devenir "
   "une pâte humide mais pas détrempée (presser l'excès de lait si besoin).",
   "**Mélanger.** Œufs, parmesan, farine, persil, sel et muscade incorporés au pain ; pâte homogène qui se tient "
   "en boule sans trop coller (ajuster la farine si elle colle trop).",
   "**Façonner.** Boulettes de 3 cm roulées entre les paumes légèrement farinées.",
   "**Pocher.** Eau bouillante salée ; gnocchi plongés par fournées, 4 à 5 min : ils remontent à la surface une "
   "fois cuits à cœur ; égouttés.",
   "**Finir.** Beurre mousseux à la poêle avec la sauge, 2 min ; gnocchi pochés roulés dedans 1 à 2 min pour les "
   "dorer légèrement ; un filet de vinaigre balsamique à table, pour qui aime."],
  tips=["Le pain doit être vraiment rassis (dur), pas frais : un pain encore mou donne une pâte trop collante.",
        "Les enfants façonnent très bien les boulettes."],
  keep="Crus façonnés, 1 jour au frigo ; cuits, 2 jours, réchauffés à la poêle.", age=2,
  kids="✓ dès 2 ans. Les enfants roulent les boulettes.", cats=["enfants", "vegetarien", "zero_dechet", "express"],
  profil=["gras"], credit=C(V("quellemaison", "7704253585348971798")))
K("jambon_dinde_maison", "Jambon de dinde maison (cuit, sans conservateur inutile)", "Homemade cooked turkey ham", FR, "P", 2, 10, 30, 1440, "€€",
  "Grande cocotte ou four avec thermomètre à sonde, ficelle de cuisine.",
  "Le geste du charcutier simplifié, en version volaille : un blanc de dinde en saumure deux jours avec du sel "
  "nitrité (pour une couleur rose et une vraie sécurité alimentaire, pas pour le goût), puis poché longuement à "
  "basse température. Pas une recette à l'improvisation, mais un vrai jambon maison.",
  [f"1,5 kg|de blanc de dinde, en un seul morceau, roulé et ficelé|Blanc de poulet|3",
   f"2 l|d'eau (pour la saumure)|{EAU}|3", f"150 g|de sel nitrité, dosé selon l'indication du paquet (jamais à l'œil)|{SELNITRITE}|3",
   f"50 g|de sucre|{SUCRE}|1", f"2|feuilles de laurier|{LAURIER}|1", f"1 c. à c.|de grains de poivre|{POIVRE}|1",
   f"2|clous de girofle|Clou de girofle|1?", f"8|cornichons (pour servir)|{CORNICHON}|1?"],
  ["**Saumure.** Eau, sel nitrité (au poids exact indiqué sur le paquet : ni plus ni moins, c'est ce qui garantit "
   "la sécurité du jambon), sucre et aromates portés à ébullition 2 min, puis complètement refroidis au frigo.",
   "**Saler.** Blanc de dinde immergé entièrement dans la saumure froide, un poids dessus pour qu'il ne flotte "
   "pas ; 48 h au frigo.",
   "**Pocher.** Dinde rincée, séchée, pochée dans une eau fraîche à frémissement très doux (jamais un bouillon "
   "franc), thermomètre planté au centre : sortie du feu dès 65 °C à cœur, après environ 1 h 30 à 2 h selon la "
   "taille (la volaille demande un repère plus bas et un temps plus court que le porc).",
   "**Refroidir.** Dans son jus de cuisson jusqu'à tiède, puis au frigo, toujours ficelée : elle se tranche bien "
   "mieux froide.",
   "**Trancher.** Ficelle retirée, tranché fin. Servi avec des cornichons, comme chez le charcutier."],
  tips=["Le sel nitrité n'est pas optionnel ni une question de goût : c'est lui qui empêche le développement de "
        "bactéries dangereuses (dont le botulisme) sur une viande saumurée puis pochée à basse température. On "
        "respecte le dosage indiqué sur l'emballage, à la lettre.",
        "Un thermomètre à sonde est ici un vrai outil de sécurité, pas un détail : sans lui, impossible de savoir "
        "si le cœur a bien atteint une température sûre."],
  keep="5 jours au frigo, bien enveloppé ; se congèle en tranches.", age=1, kids="✓ dès 1 an.", cats=[],
  profil=["gras"], credit=C(V("nabil_zemmouri", "7578529561860656406")))
K("sauce_ranch_maison", "Sauce ranch maison (yaourt, herbes et ail, pour tremper ou assaisonner)", "Ranch dressing", US, "S", 1, 10, 10, 0, "€",
  "Bol, fouet.",
  "La sauce américaine qu'on trempe dans tout : un yaourt épais ou de la crème fraîche, de l'ail, des herbes "
  "fraîches et un peu de vinaigre, pour napper une salade, tremper des crudités ou des ailes de poulet.",
  [f"200 g|de yaourt grec ou de crème fraîche épaisse|{GREC}|3", f"3 c. à s.|de mayonnaise|Mayonnaise industrielle|1",
   f"1 gousse|d'ail, écrasée (ou 1/2 c. à c. de poudre d'ail)|{AIL}|1", f"1 c. à c.|de poudre d'ail / d'oignon|Poudre d'ail / d'oignon|1?",
   f"2 c. à s.|de ciboulette ciselée|{PERSIL}|1", f"1 c. à s.|d'aneth ciselé (frais ou séché)|Aneth|1?",
   f"1 c. à c.|de vinaigre de cidre|{CIDRE}|1", f"3 c. à s.|de lait (pour ajuster la texture)|{LAIT}|1?",
   f"-|sel, poivre|{SEL}|1"],
  ["**Mélanger.** Yaourt, mayonnaise, ail, herbes et vinaigre fouettés ensemble jusqu'à lisse.",
   "**Ajuster.** Lait ajouté cuillerée par cuillerée jusqu'à la texture voulue : plus épaisse pour tremper, plus "
   "fluide pour napper une salade.",
   "**Reposer.** Au moins 30 min au frigo avant de servir : les herbes parfument toute la sauce.",
   "**Servir.** Sur une salade, en trempette pour des crudités ou des ailes de poulet, ou sur un sandwich."],
  tips=["Elle épaissit encore un peu au frigo : prévois-la légèrement plus fluide que voulu au départ.",
        "Avec de l'aneth frais plutôt que séché, le goût est nettement plus proche de l'original américain."],
  keep="5 jours au frigo.", age=1, kids="✓ dès 1 an.", cats=["enfants", "vegetarien", "express"], profil=["acide"],
  credit=C(V("lardoise_porto_vecchio", "7708342943995743520")))
K("crepes_gari_coco", "Crêpes de gari (semoule de manioc, lait de coco et sucre)", "Crêpes de gari", TG, "G", 1, 8, 15, 20, "€",
  "Saladier, poêle.",
  "Après le smoothie de gari, ses crêpes : la semoule de manioc grillée réhydratée dans le lait de coco sucré, "
  "liée à l'œuf et à la farine, cuites en petites galettes épaisses et moelleuses, parfumées à la noix de coco.",
  [f"200 g|de gari (semoule de manioc)|Manioc / attiéké / garri|3", f"40 cl|de lait de coco|{COCO}|3",
   f"80 g|de sucre|{SUCRE}|2", f"2|œufs|{OEUF}|2", f"100 g|de farine|{F55}|2", f"1 c. à c.|de levure chimique|{LEVC}|1",
   f"1 pincée|de sel|{SEL}|1", f"2 c. à s.|d'huile (pour la cuisson)|{HN}|1"],
  ["**Réhydrater.** Gari versé dans le lait de coco tiède avec le sucre, 10 min de repos : il gonfle et "
   "ramollit, absorbant presque tout le liquide.",
   "**Pâte.** Œufs, farine, levure et sel incorporés au gari réhydraté : pâte épaisse qui tombe lourdement de la "
   "cuillère (plus dense qu'une pâte à crêpes classique).",
   "**Cuire.** Poêle chaude et légèrement huilée ; petites galettes de 2 c. à s. versées, aplaties légèrement, "
   "3 à 4 min par face à feu moyen : dorées et bien cuites à cœur (elles sont épaisses, ne pas presser la "
   "cuisson).",
   "**Servir.** Tièdes, telles quelles ou avec un filet de miel."],
  tips=["La pâte est volontairement épaisse et granuleuse (c'est le gari) : ne pas chercher à la fluidifier "
        "comme une pâte à crêpes classique.", "Se mangent aussi froides, en goûter à emporter."],
  keep="2 jours à température ambiante, dans une boîte ; 4 jours au frigo.", age=2,
  kids="✓ dès 2 ans. Les enfants versent et aplatissent les galettes.", cats=["enfants", "vegetarien"],
  profil=["sucre"], credit=C(V("bolimix_officiel", "7699811741445770516")))
K("chou_fleur_roti_feta_menthe", "Chou-fleur rôti entier, crème de feta à la menthe et grenade", "Whole roasted cauliflower, whipped feta", GB, "P", 1, 6, 15, 40, "€€",
  "Plaque de four, mixeur ou fourchette.",
  "Le chou-fleur traité comme une pièce de viande : de grosses tranches badigeonnées de miel et de paprika, "
  "rôties jusqu'à tendres et caramélisées, posées sur un lit de feta fouettée au yaourt et au citron, parsemées "
  "de menthe et de grains de grenade. De quoi convaincre que le chou-fleur peut être un plat principal.",
  [f"1|gros chou-fleur, en tranches épaisses de 2 cm|Chou-fleur|3", f"4 c. à s.|d'huile d'olive|{HO}|2",
   f"2 c. à s.|de paprika|{PAPRIKA}|1", f"2 c. à s.|de miel|{MIEL}|1", f"200 g|de feta|Feta|3",
   f"3 c. à s.|de yaourt grec|{GREC}|2", f"1/2|citron (jus)|{CIT}|1", f"1 bouquet|de menthe fraîche|Menthe|1",
   f"3 c. à s.|de graines de grenade|Grenade|1?", "1 c. à s.|de graines de sésame|Sésame (blanc/noir)|1?",
   f"-|sel|{SEL}|1"],
  ["**Préparer.** Four à 180 °C. Huile, paprika, 1 c. à s. de miel et une pincée de sel mélangés ; tranches de "
   "chou-fleur badigeonnées généreusement des deux côtés.",
   "**Rôtir.** Sur une plaque, en une couche, 35 à 40 min en retournant à mi-cuisson : tendres à cœur à la pointe "
   "du couteau, bien colorées et caramélisées sur les bords.",
   "**Crème de feta.** Feta, yaourt, jus de citron et le reste du miel mixés (ou écrasés à la fourchette pour "
   "une texture plus rustique) jusqu'à crémeux.",
   "**Monter.** Crème de feta étalée au fond d'un plat de service ; tranches de chou-fleur rôti disposées dessus.",
   "**Finir.** Menthe ciselée, graines de grenade et de sésame parsemées sur le dessus. Servi tiède, à partager."],
  tips=["Des tranches toutes de la même épaisseur cuisent uniformément : les plus fines brûlent avant que les "
        "épaisses ne soient tendres.", "La crème de feta se prépare pendant que le chou-fleur rôtit : rien "
        "n'attend."],
  keep="2 jours au frigo, les éléments séparés.", age=2, kids="✓ dès 2 ans, menthe en moins grande quantité.",
  cats=["enfants", "vegetarien"], profil=["acide", "sucre"], credit=C(V("acha_happybody", "7708111537545792800")))
K("tarte_poireaux_burrata_pistache", "Tarte rustique aux poireaux, burrata et pesto de pistache", "Leek tart, burrata, pistachio pesto", FR, "P", 1, 6, 20, 35, "€€",
  "Plaque de four, casserole.",
  "Une tarte toute simple qui devient spectaculaire à la sortie du four : des poireaux fondus enveloppés dans "
  "une pâte brisée repliée sur elle-même, garnie à chaud d'une burrata crémeuse qui fond doucement et d'un trait "
  "de pesto de pistache.",
  ["3|poireaux, émincés|Poireau|3", f"1|pâte brisée (prête ou maison)|Pâte brisée / sablée (prête)|3",
   f"2 c. à s.|de crème fraîche|{CF}|1", f"1 c. à c.|de moutarde|{DIJON}|1", f"2 c. à s.|d'huile d'olive|{HO}|1",
   f"3 brins|de thym|{THYM}|1", f"1|burrata|{MOZZ}|3", "3 c. à s.|de pesto (vert, ou de pistache)|Pesto (bocal)|1",
   f"2 c. à s.|de pistaches concassées|{PISTA}|1?", f"-|sel, poivre|{SEL}|1"],
  ["**Fondre les poireaux.** Émincés, cuits à la poêle avec l'huile et un fond d'eau, 12 à 15 min à couvert à feu "
   "doux : bien tendres, sans coloration ; sel, poivre.",
   "**Garnir.** Four à 180 °C. Pâte brisée déroulée sur une plaque ; crème et moutarde mélangées, étalées au "
   "centre en laissant 4 cm de bord libre ; thym effeuillé, poireaux fondus par-dessus.",
   "**Replier.** Bords de la pâte rabattus vers le centre, en chevauchant légèrement, pour une tarte rustique à "
   "ciel ouvert.",
   "**Cuire.** 30 à 35 min : la pâte est bien dorée et croustillante.",
   "**Finir.** À la sortie du four, encore chaude : burrata déchirée à la main posée au centre, pesto versé en "
   "filet, pistaches concassées par-dessus. Servie aussitôt, pendant que la burrata est encore fondante."],
  tips=["La burrata se pose à la toute fin, jamais au four : la chaleur résiduelle de la tarte suffit à "
        "l'attendrir sans la faire fondre en flaque.", "Sans pesto de pistache, un pesto au basilic classique "
        "convient très bien."],
  keep="2 jours au frigo (sans la burrata, ajoutée fraîche à chaque réchauffage).", age=2,
  kids="✓ dès 2 ans.", cats=["enfants", "vegetarien"], profil=["gras"],
  credit=C(V("acha_happybody", "7708111537545792800")))
