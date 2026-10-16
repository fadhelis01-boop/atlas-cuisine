# -*- coding: utf-8 -*-
"""Vague 4 · Audit du chef (16/10/2026) : Asie de l'Est, du Sud et du Sud-Est, les classiques du catalogue (Tome 4) encore sans fiche.
Mirin et saké : variantes sans alcool « à tester » (D21). NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

JP = "Asie de l'Est › Japon"; KR = "Asie de l'Est › Corée"; CN = "Asie de l'Est › Chine"; IN = "Asie du Sud › Inde"
TH = "Asie du Sud-Est › Thaïlande"
VSAKE = ("Sans alcool", ["alcohol"], {"Mirin": [("Vinaigre de riz", 0.5), ("Sucre blanc / roux / cassonade / vergeoise", 0.3)],
                                       "Saké / saké de cuisine": [("Bouillon cube volaille", 1.0)]},
         "Mirin → **vinaigre de riz + sucre** ; saké → **bouillon**. **À tester**.")

# ——— Japon ———
K("gyudon", "Gyudon (bol de riz au bœuf et oignon)", "Gyūdon", f"{JP} › Tokyo", "P", 1, 4, 15, 15, "€€", "Sauteuse, cuiseur ou casserole à riz.",
  "Fines lamelles de bœuf et oignon mijotées quelques minutes dans un bouillon sucré-salé, sur un bol de riz : le repas rapide des Japonais.",
  [f"400 g|de bœuf en tranches très fines (rumsteck, paleron)|Rumsteck|3", f"2|oignons|{OIG}|2", f"320 g|de riz rond|Riz rond / sushi|3", f"4 c. à s.|de sauce soja|{SOJA}|2", "3 c. à s.|de mirin|Mirin|2", "2 c. à s.|de saké|Saké / saké de cuisine|1?", "20 cl|de dashi (ou bouillon léger)|Dashi (instantané)|1", "1 c. à c.|de gingembre mariné|Gingembre mariné (gari)|1?"],
  ["**Riz.** Rincé jusqu'à eau claire, cuit (1,2 fois son volume d'eau, 12 min couvert, 10 min de repos).", "**Mijoter.** Dashi, soja, mirin, saké, sucre (1 c. à s.) frémissants ; oignon en lamelles, 5 min : translucide.",
   "**Bœuf.** Tranches posées dans le bouillon, 2 min, en écumant : à peine cuit. Sur le riz, avec un peu de jus et le gingembre."],
  tips=["Le bœuf se tranche finement s'il passe 30 min au congélateur."], age=1, cats=["enfants"], var=[VSAKE])

K("yakitori", "Yakitori (brochettes de poulet laquées)", "Yakitori", JP, "P", 1, 4, 25, 15, "€€", "Brochettes en bois trempées, grill du four ou plancha.",
  "Morceaux de cuisse de poulet et de cébette en brochettes, grillés et laqués de sauce tare au soja et au mirin : le classique des comptoirs japonais.",
  [f"600 g|de cuisses de poulet désossées|{CUISSE}|3", "1 botte|de cébettes|Oignon nouveau / cébette|2", f"6 c. à s.|de sauce soja|{SOJA}|2", "4 c. à s.|de mirin|Mirin|2", f"2 c. à s.|de sucre|{SUCRE}|1", "1 pincée|de shichimi togarashi|Shichimi togarashi|1?"],
  ["**Tare.** Soja, mirin, sucre, 5 min à frémissement : sirupeux.", "**Brochettes.** Poulet en cubes de 3 cm alternés avec des tronçons de cébette.",
   "**Griller.** 10-12 min en tournant ; badigeonnés de tare les 3 dernières minutes, 2-3 fois : laqués, légèrement grillés."], age=1, cats=["enfants"], fetes=["Barbecue d'été"], var=[VSAKE])

K("tempura_legumes_crevettes", "Tempura de légumes et crevettes", "Tempura", JP, "P", 3, 4, 30, 15, "€€", "Casserole profonde, thermomètre, baguettes.",
  "Une pâte à peine mélangée et glacée, des légumes et des crevettes plongés dans l'huile : une dentelle croustillante et légère. Le secret : tout très froid et des grumeaux.",
  ["12|crevettes crues décortiquées (queue gardée)|Crevettes (cuites/crues)|3", "1|patate douce|Patate douce|2", "1|courgette|Courgette|1", "8|champignons shiitake ou de Paris|Shiitake|1", f"120 g|de farine (ou moitié fécule)|{F55}|3", f"1|jaune d'œuf|Jaune d'œuf|1", "20 cl|d'eau gazeuse glacée|-|2", "1,5 l|d'huile de friture|Huile d'arachide|2", f"4 c. à s.|de sauce soja (pour tremper)|{SOJA}|1"],
  ["**Préparer.** Légumes en tranches de 5 mm ; crevettes incisées sous le ventre (elles restent droites), séchées.", "**Pâte minute.** Jaune + eau glacée, farine versée d'un coup, 10 coups de baguettes : il reste des grumeaux (c'est voulu).",
   "**Frire.** 175 °C ; tremper puis frire par petites quantités, 2 min (crevettes) à 3 min (légumes) : pâle et craquant ; égoutter sur grille. Soja coupé de dashi et un peu de radis râpé."],
  age=3, tech=["frire en sécurité"], profil=["poisson"])

K("kake_udon", "Kake udon (bouillon dashi et nouilles épaisses)", "Kake udon", f"{JP} › Kagawa", "So", 1, 2, 10, 10, "€", "Casserole.",
  "Grosses nouilles udon dans un bouillon dashi au soja, cébette et parfois un œuf : la soupe simple et réconfortante des gares japonaises.",
  ["2 portions|de nouilles udon|Nouilles udon|3", "70 cl|de dashi|Dashi (instantané)|3", f"3 c. à s.|de sauce soja|{SOJA}|2", "2 c. à s.|de mirin|Mirin|1", "2|cébettes|Oignon nouveau / cébette|1", f"2|œufs (facultatif)|{OEUF}|1?", "1 pincée|de shichimi togarashi|Shichimi togarashi|1?"],
  ["**Bouillon.** Dashi, soja, mirin frémissants ; goûte : salé doux.", "**Nouilles.** Réchauffées 2 min à l'eau bouillante, égouttées dans les bols.", "**Servir.** Bouillon brûlant, cébette ; œuf poché 3 min dans le bouillon si tu veux, shichimi."],
  age=1, cats=["enfants"], var=[VSAKE])

K("chawanmushi", "Chawanmushi (flan salé japonais à la vapeur)", "Chawanmushi", JP, "E", 2, 4, 15, 15, "€€", "Ramequins ou tasses, panier vapeur ou casserole couverte.",
  "Un flan d'œuf au dashi, si tremblotant qu'il se mange à la cuillère, avec crevette, champignon et poulet cachés au fond.",
  [f"3|œufs|{OEUF}|3", "36 cl|de dashi froid|Dashi (instantané)|3", f"1 c. à s.|de sauce soja claire|Sauce soja claire|1", "1 c. à s.|de mirin|Mirin|1?", "4|crevettes|Crevettes (cuites/crues)|1", f"80 g|de blanc de poulet|{BLANC_P}|1", "4|shiitake|Shiitake|1"],
  ["**Appareil.** Œufs battus sans mousser, dashi, soja, mirin ; passé au tamis : lisse.", "**Remplir.** Garniture en dés au fond, appareil versé, bulles crevées ; couvert d'aluminium.",
   "**Vapeur douce.** Frémissement très faible, 12-15 min : tremblant, et un jus clair sort si on pique (vapeur trop forte = trous)."],
  age=1, cats=["enfants"], var=[VSAKE])

K("maki_maison", "Makis maison (concombre, thon, saumon cuit)", "Hosomaki", JP, "E", 2, 4, 45, 30, "€€", "Natte en bambou (ou torchon + film), couteau bien aiguisé.",
  "Riz vinaigré roulé dans la feuille de nori autour d'un seul ingrédient : un atelier convivial. Par défaut sans poisson cru (saumon cuit ou thon en boîte).",
  ["300 g|de riz rond pour sushi|Riz rond / sushi|3", "4 c. à s.|de vinaigre de riz|Vinaigre de riz|2", f"1 c. à s.|de sucre|{SUCRE}|1", "4|feuilles de nori|Algue nori|3", "1|concombre|Concombre|1", "150 g|de thon en conserve ou de saumon cuit|Thon en conserve|2", f"1 c. à s.|de sauce soja|{SOJA}|1", "1 c. à c.|de wasabi|Wasabi (pâte)|1?"],
  ["**Riz.** Rincé, cuit (33 cl d'eau, 12 min, 10 min de repos) ; vinaigre + sucre + 1 c. à c. de sel mélangés en coupant, éventé : brillant, tiède.",
   "**Rouler.** Demi-feuille de nori brillante dessous, riz en couche fine (mains mouillées) en laissant 1 cm en haut ; un bâtonnet de garniture ; roulé serré avec la natte.",
   "**Couper.** Couteau mouillé, 6 tronçons. Soja, gingembre, wasabi."],
  tips=["**Poisson cru** : seulement très frais « qualité sashimi » et congelé 7 jours à −20 °C avant (anisakis) ; jamais pour femmes enceintes ni jeunes enfants."],
  keep="Le jour même (le riz durcit au froid).", age=3, cats=["enfants"], fetes=["Apéritif dînatoire"])

# ——— Corée ———
K("japchae", "Japchae (vermicelles de patate douce sautés)", "Japchae", KR, "P", 2, 4, 35, 10, "€€", "Grande poêle ou wok.",
  "Vermicelles transparents et élastiques sautés avec bœuf, épinards, carotte, champignons et huile de sésame : le plat des fêtes coréennes.",
  ["200 g|de vermicelles de patate douce (ou de haricot mungo)|Vermicelles de haricots mungo|3", f"200 g|de bœuf en lanières|Rumsteck|2", "150 g|d'épinards|Épinard|2", f"1|carotte|{CAROTTE}|1", "6|shiitake|Shiitake|1", f"4 c. à s.|de sauce soja|{SOJA}|2", "2 c. à s.|d'huile de sésame|Huile de sésame (grillée)|2", f"1 c. à s.|de sucre|{SUCRE}|1", "1 c. à s.|de sésame|Sésame (blanc/noir)|1"],
  ["**Vermicelles.** Cuits 6 min, rincés, coupés aux ciseaux, assaisonnés de 1 c. à s. de soja et d'huile de sésame.", "**Sauter séparément.** Carotte en julienne, champignons, bœuf mariné (soja, sucre, ail), chacun 2-3 min ; épinards blanchis et pressés.",
   "**Assembler.** Tout dans la poêle avec le reste de soja, sucre, sésame, 2 min : brillant. Chaud ou tiède."], age=1, cats=["enfants"], fetes=["Repas de famille"])

K("kimchi_jjigae_tofu", "Kimchi jjigae au tofu", "Kimchi jjigae", KR, "So", 1, 4, 15, 20, "€", "Cocotte ou faitout.",
  "Le ragoût-soupe le plus courant des maisons coréennes : kimchi bien fermenté, tofu, oignon et gochujang. Plus le kimchi est vieux, meilleur c'est. Version sans porc (tofu, ou thon en boîte).",
  ["300 g|de kimchi bien mûr + son jus|SUB:kimchi_maison|3", "300 g|de tofu ferme|Tofu (ferme / soyeux)|3", f"1|oignon|{OIG}|1", "1 c. à s.|de gochujang|Gochujang|2", "1 c. à c.|de gochugaru (ou paprika + piment)|Gochugaru|1?", "1 c. à s.|d'huile de sésame|Huile de sésame (grillée)|1", "2|cébettes|Oignon nouveau / cébette|1", "50 cl|d'eau ou de dashi|Dashi (instantané)|1"],
  ["**Faire revenir.** Kimchi et oignon dans l'huile de sésame, 5 min : il fond et sent fort.", "**Mijoter.** Gochujang, gochugaru, eau et jus de kimchi, 15 min.", "**Tofu.** En tranches épaisses, 5 min ; cébette. Riz blanc à côté."],
  age=6, cats=["vegetarien"], profil=["epice"])

K("kimbap", "Kimbap (rouleaux coréens au riz)", "Gimbap", KR, "E", 2, 4, 50, 20, "€", "Natte en bambou.",
  "Gros rouleaux de riz à l'huile de sésame et nori, garnis d'omelette, carotte, épinards, concombre et thon-mayonnaise : le pique-nique coréen.",
  ["400 g|de riz rond|Riz rond / sushi|3", "4|feuilles de nori|Algue nori|3", f"3|œufs|{OEUF}|2", f"1|carotte|{CAROTTE}|1", "150 g|d'épinards|Épinard|1", "1|concombre|Concombre|1", "140 g|de thon en conserve|Thon en conserve|2", "2 c. à s.|de mayonnaise|SUB:mayonnaise|1", "2 c. à s.|d'huile de sésame|Huile de sésame (grillée)|2"],
  ["**Riz.** Cuit, assaisonné d'huile de sésame et de sel (pas de vinaigre).", "**Garnitures.** Omelette fine en bandes, carotte sautée en julienne, épinards blanchis au sésame, concombre en bâtonnets, thon-mayonnaise.",
   "**Rouler.** Nori entière, riz fin sur les ¾, garnitures alignées, roulé serré ; huile de sésame sur le dessus, tranché au couteau mouillé."],
  keep="Le jour même, à température fraîche.", age=3, cats=["enfants"], fetes=["Pique-nique"])

# ——— Chine ———
K("soupe_wonton_poulet", "Soupe de wontons au poulet et crevettes", "Húntún tāng", f"{CN} › Canton", "So", 2, 4, 45, 10, "€€", "Faitout.",
  "Petits raviolis fins farcis poulet-crevette, flottant dans un bouillon clair au gingembre et pak-choï : la soupe des échoppes de Hong Kong.",
  ["24|feuilles de pâte à wonton|Pâte à gyoza / wonton|3", "250 g|de poulet haché (ou blanc mixé)|Blanc de poulet|3", "150 g|de crevettes crues|Crevettes (cuites/crues)|2", "1 c. à s.|de gingembre râpé|Gingembre frais|1", f"2 c. à s.|de sauce soja|{SOJA}|1", "1 c. à c.|d'huile de sésame|Huile de sésame (grillée)|1", "1 l|de bouillon de volaille|Bouillon cube volaille|2", "2|pak-choï|Chou chinois / pak-choï|1", "2|cébettes|Oignon nouveau / cébette|1"],
  ["**Farce.** Poulet, crevettes hachées, gingembre, soja, sésame, cébette ; mélangée énergiquement : collante.", "**Former.** 1 c. à c. au centre, bords mouillés, plié en triangle puis pointes rejointes.",
   "**Cuire.** Bouillon frémissant au gingembre ; wontons 4 min après qu'ils remontent ; pak-choï 2 min."], age=1, cats=["enfants"],
  keep="Wontons crus congelés à plat : 2 mois.")

K("poulet_aigre_doux", "Poulet aigre-doux à l'ananas", "Tángcù jī", f"{CN} › Canton", "P", 1, 4, 25, 15, "€€", "Wok ou grande poêle.",
  "Poulet en morceaux enrobés de fécule et poêlés, poivrons, ananas et une sauce aigre-douce brillante : le classique des restaurants chinois, fait maison.",
  [f"600 g|de blancs de poulet|{BLANC_P}|3", "4 c. à s.|de fécule de maïs|Fécule de maïs (maïzena)|2", f"1|œuf|{OEUF}|1", f"1|poivron rouge|{POIVRON}|1", "200 g|d'ananas|Ananas|2", f"1|oignon|{OIG}|1", "3 c. à s.|de ketchup|Ketchup|2", "3 c. à s.|de vinaigre de riz|Vinaigre de riz|2", f"2 c. à s.|de sucre|{SUCRE}|1", f"1 c. à s.|de sauce soja|{SOJA}|1"],
  ["**Enrober.** Poulet en cubes, œuf, 3 c. à s. de fécule, sel ; poêlé dans 1 cm d'huile, 6 min : doré ; égoutté.", "**Légumes.** Oignon et poivron en morceaux, 3 min vifs ; ananas 1 min.",
   "**Sauce.** Ketchup, vinaigre, sucre, soja, 1 c. à s. de fécule + 10 cl d'eau ; versée, 1 min : brillante ; poulet remis, enrobé. Riz blanc."], age=1, cats=["enfants"])

K("oeufs_tomates_chinois", "Œufs brouillés aux tomates (Chine)", "Xīhóngshì chǎo jīdàn", CN, "P", 1, 2, 10, 5, "€", "Wok ou poêle.",
  "Le plat que tous les Chinois savent cuisiner : œufs à peine pris et tomates fondues en sauce sucrée-salée. 10 minutes, un bol de riz, c'est un repas.",
  [f"4|œufs|{OEUF}|3", f"3|tomates mûres|{TOM}|3", "1|cébette|Oignon nouveau / cébette|1", f"1 c. à c.|de sucre|{SUCRE}|1", f"1 c. à s.|de sauce soja|{SOJA}|1", f"2 c. à s.|d'huile|{HN}|1"],
  ["**Œufs.** Battus salés, versés dans l'huile chaude, remués 30 s : gros caillots encore baveux ; réservés.", "**Tomates.** En quartiers, 3 min : elles rendent leur jus ; sucre, soja.", "**Réunir.** Œufs remis, 30 s ; cébette. Riz."],
  age=1, cats=["enfants", "vegetarien", "express"])

K("zha_jiang_mian", "Zha jiang mian (nouilles sauce soja-bœuf haché)", "Zhájiàngmiàn", f"{CN} › Pékin", "P", 1, 4, 20, 15, "€", "Wok, casserole.",
  "Nouilles épaisses couvertes d'une sauce de viande hachée à la pâte de soja fermentée, concombre croquant par-dessus : le plat populaire de Pékin. Bœuf par défaut (D21).",
  ["400 g|de nouilles aux œufs ou udon|Nouilles chinoises aux œufs|3", "400 g|de bœuf haché|Bœuf haché|3", "3 c. à s.|de pâte de haricots (doubanjiang ou miso brun)|Pâte de haricots jaunes/noirs|2", "1 c. à s.|de sauce hoisin (ou soja + miel)|Sauce d'huître|1?", "1|concombre|Concombre|1", f"2 gousses|d'ail|{AIL}|1", "2|cébettes|Oignon nouveau / cébette|1"],
  ["**Sauce.** Viande émiettée 6 min ; ail, pâte de haricots, hoisin, 15 cl d'eau, 8 min : épais et brillant.", "**Nouilles.** Cuites, rincées si servies tièdes.", "**Servir.** Nouilles, sauce, concombre en julienne, cébette ; on mélange à table."],
  age=1, cats=["enfants"])

# ——— Inde & Sri Lanka ———
K("paratha", "Paratha (pain feuilleté indien)", "Paratha", f"{IN} › Pendjab", "Pa", 2, 6, 30, 30, "€", "Poêle épaisse ou tava, rouleau.",
  "Pâte de farine complète roulée avec du ghee, pliée et cuite à la poêle : un pain feuilleté et beurré qui accompagne dals et currys.",
  ["300 g|de farine atta (ou ½ complète ½ T55)|Farine de blé T80 (semi-complète)|3", "4 c. à s.|de ghee ou beurre fondu|Ghee|2", f"1 pincée|de sel|{SEL}|1", "18 cl|d'eau tiède|-|1"],
  ["**Pâte.** Farine, sel, 1 c. à s. de ghee, eau ; pétrie 5 min : souple ; 30 min sous un torchon.", "**Feuilleter.** 6 boules ; abaissées fines, ghee étalé, pliées en éventail puis roulées en escargot ; abaissées à nouveau (18 cm).",
   "**Cuire.** Poêle chaude à sec, 1 min ; retourné, ghee, pressé à la spatule ; 1 min par face : taches dorées, couches visibles. Froissé dans les mains pour ouvrir les feuilles."],
  age=1, cats=["enfants", "vegetarien"])

K("sambar", "Sambar (dal aux légumes et tamarin)", "Sambar", f"{IN} › Tamil Nadu", "So", 2, 6, 25, 40, "€", "Faitout, petite poêle.",
  "Le dal du Sud de l'Inde : lentilles jaunes et légumes dans un bouillon acidulé au tamarin, relevé d'épices torréfiées et de feuilles de curry. Avec riz, idli ou dosa.",
  ["200 g|de lentilles corail (ou toor dal)|Lentilles corail (masoor)|3", "300 g|de légumes (aubergine, carotte, courge, gombo)|Aubergine|2", "1 c. à s.|de pâte de tamarin|Pâte de tamarin|2", f"2|tomates|{TOM}|1", "2 c. à s.|de sambar masala (ou curry)|Curry (mélange)|2", "1 c. à c.|de graines de moutarde|Graines de moutarde|1?", "10|feuilles de curry|Feuille de curry|1?", f"½ c. à c.|de curcuma|{CURC}|1", "2 c. à s.|de ghee ou huile|Ghee|1"],
  ["**Dal.** Lentilles, curcuma, 1 l d'eau, 20 min : fondues, fouettées.", "**Légumes.** En morceaux, tomates, tamarin, masala, sel, dans le dal, 15 min : tendres.",
   "**Tempérer.** Ghee chaud, moutarde (elle saute), feuilles de curry 10 s ; versé sur le sambar."], age=1, cats=["vegetarien"], profil=["epice"])

K("rajma", "Rajma (haricots rouges à la tomate, Pendjab)", "Rajma chawal", f"{IN} › Pendjab", "P", 1, 4, 20, 30, "€", "Cocotte.",
  "Haricots rouges fondants dans une sauce épaisse oignon-tomate-gingembre et garam masala : le plat du dimanche des familles du Nord de l'Inde, avec du riz.",
  ["500 g|de haricots rouges cuits|Haricots rouges / noirs|3", f"2|oignons|{OIG}|2", f"400 g|de tomates concassées|{PELEES}|2", f"3 gousses|d'ail|{AIL}|1", "1 c. à s.|de gingembre râpé|Gingembre frais|1", f"1 c. à c.|de cumin|{CUMIN}|1", "2 c. à c.|de garam masala|Garam masala|2", f"½ c. à c.|de piment|{CAYENNE}|1", f"1 bouquet|de coriandre|{CORI}|1"],
  ["**Masala.** Cumin dans l'huile 30 s, oignons 10 min : bien dorés ; ail, gingembre, épices 1 min ; tomates 10 min : l'huile perle.", "**Mijoter.** Haricots, 30 cl d'eau, 20 min ; écrase une louche contre la paroi : sauce épaisse.", "**Servir.** Coriandre ; riz basmati."],
  age=1, cats=["vegetarien", "enfants"], profil=["epice"])

K("korma_legumes", "Korma de légumes (sauce douce cajou-yaourt)", "Navratan korma", f"{IN} › Moghol", "P", 1, 4, 25, 25, "€€", "Cocotte, mixeur.",
  "Légumes dans une sauce crémeuse et douce à la noix de cajou, au yaourt et à la cardamome : le curry le moins piquant, parfait pour découvrir.",
  ["600 g|de légumes (chou-fleur, carotte, petits pois, pommes de terre)|Chou-fleur|3", "60 g|de noix de cajou|Noix de cajou|2", f"15 cl|de yaourt|{YAO}|2", f"1|oignon|{OIG}|1", "1 c. à s.|de gingembre râpé|Gingembre frais|1", "4|gousses de cardamome|Cardamome|1", "2 c. à c.|de garam masala|Garam masala|1", f"10 cl|de crème|{CF}|1?", "2 c. à s.|de ghee|Ghee|1"],
  ["**Base.** Cajou trempés 15 min dans l'eau chaude ; oignon fondu au ghee 8 min, gingembre, cardamome écrasée, garam masala.", "**Sauce.** Oignon + cajou + 15 cl d'eau mixés lisses ; remis, légumes en morceaux, 20 min couvert.",
   "**Finir.** Hors du feu, yaourt (il ne tranche pas hors ébullition), crème ; sel. Riz ou naan."], age=1, cats=["vegetarien", "enfants"])

K("chutney_menthe", "Chutney menthe-coriandre", "Pudina chutney", IN, "S", 1, 6, 10, 0, "€", "Mixeur.",
  "Sauce verte vive à la menthe, coriandre, piment vert, citron et un peu de yaourt : avec samoussas, tandoori, pakoras.",
  ["1 bouquet|de menthe|Menthe|3", f"1 bouquet|de coriandre|{CORI}|3", f"1|piment vert|{PIMENT}|1", f"1|citron vert|{CITV}|2", f"3 c. à s.|de yaourt|{YAO}|1?", "1 c. à c.|de gingembre|Gingembre frais|1", f"1 pincée|de sel|{SEL}|1"],
  ["**Mixer.** Herbes avec tiges tendres, piment, gingembre, citron, sel, 2 c. à s. d'eau glacée : vert vif.", "**Option crémeuse.** Yaourt ajouté (raita vert).", "**Garder.** 2 jours au frais, au contact d'un film (il noircit à l'air)."],
  keep="2 jours au frigo, film au contact.", age=3, cats=["vegetarien"])

K("gulab_jamun", "Gulab jamun (beignets au sirop de rose)", "Gulab jamun", IN, "D", 2, 20, 30, 120, "€", "Casserole profonde, thermomètre.",
  "Petites boules de pâte au lait frites doucement puis plongées dans un sirop à la cardamome et à l'eau de rose : le dessert des fêtes indiennes (Diwali).",
  ["100 g|de lait en poudre|Lait en poudre|3", f"30 g|de farine|{F55}|2", "½ c. à c.|de bicarbonate|Bicarbonate de soude|1", f"5 cl|de lait|{LAIT}|1", "1 c. à s.|de ghee|Ghee|1", f"300 g|de sucre|{SUCRE}|2", "4|gousses de cardamome|Cardamome|1", "1 c. à s.|d'eau de rose|Eau de rose|1", "1 l|d'huile de friture|Huile d'arachide|1"],
  ["**Sirop.** Sucre, 30 cl d'eau, cardamome, 5 min ; eau de rose ; tiède.", "**Pâte.** Lait en poudre, farine, bicarbonate, ghee, lait : pâte souple sans pétrir ; 20 boules lisses sans fissure.",
   "**Frire doucement.** 140 °C (pas plus : sinon cru dedans), 7-8 min en remuant l'huile : brun foncé régulier ; directement dans le sirop tiède, 2 h : ils gonflent et s'imbibent."],
  age=3, fetes=["Diwali"], profil=["sucre"], tech=["frire en sécurité"])

K("poulet_kadai", "Poulet kadai (aux poivrons et coriandre torréfiée)", "Kadai murgh", f"{IN} › Pendjab", "P", 1, 4, 25, 25, "€€", "Wok ou sauteuse, mortier.",
  "Poulet sauté dans le kadai (wok indien) avec poivrons, tomates et un mélange frais de coriandre et piment torréfiés et concassés : relevé et parfumé.",
  [f"700 g|de cuisses désossées|{CUISSE}|3", f"2|poivrons|{POIVRON}|2", f"2|oignons|{OIG}|2", f"3|tomates|{TOM}|2", "2 c. à s.|de graines de coriandre|Coriandre (graines)|2", f"2|piments séchés|{PIMENT}|1", "1 c. à s.|d'ail-gingembre|Gingembre frais|1", "1 c. à c.|de garam masala|Garam masala|1", f"1 bouquet|de coriandre|{CORI}|1"],
  ["**Kadai masala.** Coriandre et piments torréfiés 1 min à sec, concassés au mortier.", "**Sauce.** Oignon 8 min, ail-gingembre, tomates 8 min ; poulet en morceaux, ½ du masala, 15 min.",
   "**Finir.** Poivrons en carrés et oignon en pétales, 5 min (croquants) ; reste du masala, garam masala, coriandre."], age=6, profil=["epice"])

K("malai_kofta", "Malai kofta (boulettes paneer-pomme de terre, sauce crème)", "Malai kofta", f"{IN} › Moghol", "P", 3, 4, 50, 30, "€€", "Casserole de friture, mixeur.",
  "Boulettes de paneer et pomme de terre frites, servies dans une sauce douce tomate-cajou-crème : le plat végétarien de fête des restaurants indiens.",
  ["200 g|de paneer (ou ricotta égouttée)|Paneer|3", f"2|pommes de terre cuites|{PDT}|2", f"2 c. à s.|de fécule|Fécule de maïs (maïzena)|1", "40 g|de noix de cajou|Noix de cajou|2", f"400 g|de tomates concassées|{PELEES}|2", f"1|oignon|{OIG}|1", "2 c. à c.|de garam masala|Garam masala|1", f"15 cl|de crème|{CF}|2", "1 l|d'huile de friture|Huile d'arachide|1"],
  ["**Koftas.** Paneer émietté, pommes de terre écrasées, fécule, sel, garam masala ; 12 boules (un raisin ou un cajou au centre) ; frites 170 °C, 3 min : dorées.",
   "**Sauce.** Oignon fondu, tomates, cajou, 15 min ; mixée lisse, crème, garam masala.", "**Servir.** Koftas posées dans la sauce au dernier moment (elles se défont si elles y mijotent)."],
  age=1, cats=["vegetarien"], fetes=["Diwali"], tech=["frire en sécurité"])

K("kottu_roti", "Kottu roti (pain haché sauté, Sri Lanka)", "Kottu roti", "Asie du Sud › Sri Lanka", "P", 1, 4, 20, 10, "€", "Grande poêle ou plancha, 2 spatules.",
  "Pains plats coupés en lanières, sautés avec œuf, légumes, curry et poulet, hachés à la spatule dans un bruit de percussion : le street-food de Colombo, parfait pour les restes.",
  ["4|parathas ou pains plats|SUB:paratha|3", f"300 g|de poulet cuit ou restes de curry|{BLANC_P}|2", f"3|œufs|{OEUF}|2", f"1|carotte|{CAROTTE}|1", "¼|chou|Chou blanc / rouge|1", f"1|oignon|{OIG}|1", "2 c. à c.|de curry|Curry (mélange)|1", f"1|piment vert|{PIMENT}|1?"],
  ["**Couper.** Pains en lanières de 1 cm ; légumes en julienne.", "**Sauter.** Oignon, piment, légumes 4 min ; curry ; œufs brouillés dans un coin.",
   "**Hacher.** Pain et poulet, un peu de sauce de curry ou d'eau ; hache et mélange à la spatule 3 min : moelleux et doré."],
  age=3, zw=["pain d'hier", "restes de curry"], profil=["epice"])

# ——— Asie du Sud-Est ———
K("curry_rouge_boeuf", "Curry rouge thaï au bœuf et bambou", "Kaeng phet nuea", TH, "P", 1, 4, 20, 20, "€€", "Wok ou sauteuse.",
  "Pâte de curry rouge frite dans la crème de coco, bœuf émincé, pousses de bambou ou haricots, basilic thaï : plus corsé que le vert.",
  [f"500 g|de bœuf (rumsteck)|Rumsteck|3", "3 c. à s.|de pâte de curry rouge|Pâte de curry rouge/verte/jaune|3", "40 cl|de lait de coco|Lait de coco / crème de coco|3", "200 g|de haricots verts ou pousses de bambou|Haricots verts|2", "2 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|2", f"1 c. à s.|de sucre (de palme)|{SUCRE}|1", "1 bouquet|de basilic thaï|Basilic thaï|1?", "3|feuilles de combava|Feuille de combava (kaffir)|1?"],
  ["**Frire la pâte.** La crème du dessus de la boîte de coco, 3 min : l'huile se sépare ; pâte de curry 2 min : très parfumée.", "**Mijoter.** Bœuf en fines lamelles 2 min, reste du lait, haricots, combava, 8 min.",
   "**Assaisonner.** Sauce de poisson, sucre : salé, sucré, piquant. Basilic. Riz jasmin."], age=6, profil=["epice"])

K("massaman_poulet", "Curry massaman au poulet", "Kaeng matsaman", TH, "P", 1, 4, 20, 40, "€€", "Cocotte.",
  "Le curry thaï d'influence persane : doux, épicé à la cannelle et à la cardamome, avec pommes de terre, oignons et cacahuètes. Élu souvent « meilleur plat du monde ».",
  [f"700 g|de cuisses de poulet désossées|{CUISSE}|3", "3 c. à s.|de pâte de curry massaman (ou rouge + ½ c. à c. de cannelle)|Pâte de curry rouge/verte/jaune|3", "40 cl|de lait de coco|Lait de coco / crème de coco|3", f"3|pommes de terre|{PDT}|2", f"1|oignon|{OIG}|1", "50 g|de cacahuètes grillées|Cacahuète / arachide|2", "1 c. à s.|de pâte de tamarin|Pâte de tamarin|1?", "2 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|1", f"1|bâton de cannelle|{CANN}|1"],
  ["**Frire la pâte.** Crème de coco 3 min, pâte 2 min.", "**Mijoter.** Poulet en morceaux, pommes de terre en cubes, oignon en quartiers, cannelle, reste du lait + 20 cl d'eau, 30 min : tendre.",
   "**Équilibrer.** Tamarin, sauce de poisson, 1 c. à s. de sucre ; cacahuètes. Riz."], age=3, cats=["enfants"], profil=["epice"])

K("tom_yum_crevettes", "Tom yum aux crevettes", "Tom yum goong", TH, "So", 1, 4, 15, 15, "€€", "Casserole.",
  "La soupe thaïe aigre et piquante : bouillon infusé à la citronnelle, galanga et combava, crevettes, champignons, citron vert et piment.",
  ["300 g|de crevettes crues|Crevettes (cuites/crues)|3", "2|tiges de citronnelle|Citronnelle|3", "4 tranches|de galanga (ou gingembre)|Galanga|2", "4|feuilles de combava|Feuille de combava (kaffir)|2", "200 g|de champignons|Champignon de Paris|1", f"2|citrons verts|{CITV}|2", "3 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|2", f"2|piments oiseaux|{PIMENT}|1", f"1 bouquet|de coriandre|{CORI}|1"],
  ["**Infuser.** 1 l d'eau ou de bouillon, citronnelle écrasée en tronçons, galanga, combava déchiré, piments, 10 min.", "**Cuire.** Champignons 3 min, crevettes 2 min : roses.",
   "**Assaisonner hors du feu.** Sauce de poisson, jus de citron vert (jamais bouilli, il devient amer) : aigre, salé, piquant. Coriandre. (La citronnelle et le galanga ne se mangent pas.)"],
  age=6, profil=["epice", "poisson"])

K("riz_saute_ananas", "Riz sauté à l'ananas (khao pad sapparot)", "Khao pad sapparot", TH, "P", 1, 4, 20, 10, "€€", "Wok.",
  "Riz de la veille sauté avec ananas, crevettes ou poulet, cajou, raisins et curry doux, servi dans l'ananas évidé pour les grandes occasions.",
  [f"600 g|de riz cuit froid|{RIZ}|3", "250 g|d'ananas|Ananas|3", "200 g|de crevettes ou poulet|Crevettes (cuites/crues)|2", f"2|œufs|{OEUF}|1", "40 g|de noix de cajou|Noix de cajou|1", "30 g|de raisins secs|Raisins secs|1?", "1 c. à c.|de curry|Curry (mélange)|1", "2 c. à s.|de sauce de poisson (ou soja)|Sauce de poisson (nuoc-mâm, nam pla)|1", "2|cébettes|Oignon nouveau / cébette|1"],
  ["**Sauter.** Crevettes ou poulet 2 min ; œufs brouillés ; réservé.", "**Riz.** Wok fumant, riz froid égrené 3 min ; curry, sauce de poisson.", "**Finir.** Ananas en dés, cajou, raisins, crevettes, œuf, 1 min ; cébette."],
  age=3, cats=["enfants"], zw=["riz d'hier"], fetes=["Repas de famille"])

K("soto_ayam", "Soto ayam (bouillon de poulet au curcuma)", "Soto ayam", "Asie du Sud-Est › Indonésie › Java", "So", 2, 4, 30, 45, "€€", "Faitout, mixeur.",
  "Bouillon de poulet jaune au curcuma, citronnelle et gingembre, servi avec vermicelles, œuf, chou et pousses de soja : la soupe de rue de Java.",
  [f"4|cuisses de poulet|{CUISSE}|3", "100 g|de vermicelles de riz|Nouilles de riz / vermicelles|2", f"1 c. à c.|de curcuma|{CURC}|2", "2|tiges de citronnelle|Citronnelle|2", "1 c. à s.|de gingembre|Gingembre frais|1", f"3|échalotes|{ECH}|1", f"2 gousses|d'ail|{AIL}|1", f"2|œufs durs|{OEUF}|1", "100 g|de pousses de soja|Germes de soja|1?", f"1|citron vert|{CITV}|1"],
  ["**Pâte.** Échalotes, ail, gingembre, curcuma mixés ; frits 3 min : parfumés.", "**Bouillon.** Poulet, pâte, citronnelle, 1,5 l d'eau salée, 40 min ; effiloché.",
   "**Servir.** Vermicelles trempés, poulet, demi-œuf, pousses, chou émincé ; bouillon brûlant ; citron vert, sambal."], age=1, cats=["enfants"])

K("riz_poulet_hainan", "Riz au poulet de Hainan", "Hainanese chicken rice", "Asie du Sud-Est › Singapour", "P", 2, 4, 30, 60, "€€", "Grand faitout, casserole.",
  "Poulet poché tout doucement (chair soyeuse), riz cuit dans son bouillon à l'ail et au gingembre, trois sauces : le plat national de Singapour.",
  ["1|poulet de 1,5 kg|Poulet entier|3", f"350 g|de riz jasmin|{RIZ}|3", "1 morceau|de gingembre (5 cm)|Gingembre frais|2", f"4 gousses|d'ail|{AIL}|2", "4|cébettes|Oignon nouveau / cébette|1", f"3 c. à s.|de sauce soja|{SOJA}|1", "1 c. à s.|de sriracha ou sauce piment|Sriracha|1?", "1|concombre|Concombre|1"],
  ["**Pocher.** Poulet couvert d'eau salée avec gingembre et cébettes ; frémissement à peine, 35 min, puis 20 min hors du feu couvert : 74 °C ; plongé dans l'eau glacée (peau ferme).",
   "**Riz.** Ail haché et riz revenus dans un peu de gras du poulet, cuit dans 1,2 fois son volume de bouillon.",
   "**Sauces.** Gingembre-cébette râpés arrosés d'huile chaude ; soja ; piment-citron vert. Poulet découpé, concombre, bol de bouillon."],
  age=1, cats=["enfants"], tech=["pocher une volaille"])

K("lok_lak", "Lok lak (bœuf sauté sauce poivre-citron, Cambodge)", "Lok lak", "Asie du Sud-Est › Cambodge", "P", 1, 4, 20, 10, "€€", "Wok.",
  "Dés de bœuf marinés et saisis, sur salade, tomate et oignon, avec une sauce citron vert-poivre de Kampot ; souvent un œuf au plat. Simple et très vif.",
  [f"500 g|de rumsteck|Rumsteck|3", "3 c. à s.|de sauce d'huître|Sauce d'huître|2", f"1 c. à s.|de sauce soja|{SOJA}|1", f"1 c. à s.|de ketchup ou sucre|Ketchup|1", f"2|citrons verts|{CITV}|2", f"1 c. à c.|de poivre noir concassé|{POIVRE}|2", "1|salade|Salade (laitue, batavia)|1", f"2|tomates|{TOM}|1", "1|oignon rouge|Oignon rouge|1"],
  ["**Mariner.** Bœuf en cubes, sauce d'huître, soja, ketchup, ail, 20 min.", "**Saisir.** Wok fumant, 2-3 min : bruni dehors, rosé dedans.", "**Servir.** Sur salade, tomate, oignon ; sauce : jus de citron vert, poivre, sel. Riz, œuf au plat."],
  age=3, fetes=["Repas de famille"])
