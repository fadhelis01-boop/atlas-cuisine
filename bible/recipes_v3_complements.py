# -*- coding: utf-8 -*-
"""Vague 4 · Audit du chef (16/10/2026) : derniers trous du catalogue du Tome 4 après les quatre lots régionaux.
Laissés de côté volontairement : fabada (❌ « porc structurant, non adaptable » au Tome 4) et tripes à la mode de Caen
(abat absent du Tome 3, 8 h de cuisson, deux alcools structurants). NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

K("quenelles_nantua_simple", "Quenelles sauce Nantua simplifiée", "Quenelles de brochet, sauce Nantua", "France › Auvergne-Rhône-Alpes › Lyon", "P", 3, 4, 45, 30, "€€", "Mixeur, casserole, plat à gratin.",
  "La panade lyonnaise mixée avec du poisson blanc, pochée en quenelles qui gonflent au four dans une sauce crémeuse aux crustacés. Ici cabillaud et sauce aux crevettes (l'écrevisse est rare).",
  [f"300 g|de cabillaud ou brochet|Cabillaud / morue fraîche|3", f"25 cl|de lait|{LAIT}|2", f"80 g|de farine|{F55}|2", f"80 g|de beurre|{BEURRE}|2", f"3|œufs|{OEUF}|2", "250 g|de crevettes avec carapaces|Crevettes (cuites/crues)|2", f"25 cl|de crème|{CF}|2", f"1 c. à s.|de concentré de tomate|{CONC}|1", f"1 pincée|de muscade|{MUSC}|0"],
  ["**Panade.** Lait + 50 g de beurre bouillants, farine d'un coup, dessécher 2 min ; refroidie ; mixée avec le poisson, les œufs un à un, sel, muscade ; 2 h au frais.",
   "**Pocher.** Quenelles moulées à deux cuillères, eau frémissante salée, 8 min : elles remontent ; égouttées.",
   "**Sauce et four.** Carapaces revenues au beurre, concentré, crème, 10 min, filtrée ; crevettes décortiquées dedans ; quenelles nappées ; 200 °C, 15 min : elles doublent de volume."],
  age=3, profil=["poisson"])

K("full_english_volaille", "Full English breakfast (version volaille)", "Full English breakfast", "Europe du Nord › Royaume-Uni", "G", 1, 2, 25, 0, "€€", "Grande poêle, casserole.",
  "L'assiette complète du matin anglais : œufs, saucisses, bacon, haricots à la tomate, champignons, tomate grillée et toast. Selon D21 : saucisses et bacon de volaille.",
  [f"4|œufs|{OEUF}|3", "4|saucisses de volaille|Saucisse de bœuf / de veau / de volaille|2", "4 tranches|de bacon de dinde|Bacon de dinde / de bœuf|2", "400 g|de haricots blancs à la tomate|Haricots blancs / lingots|2", "150 g|de champignons|Champignon de Paris|1", f"2|tomates|{TOM}|1", "4|tranches de pain de mie|Pain de mie|1", f"20 g|de beurre|{BEURRE}|1"],
  ["**Four doux (100 °C) pour tenir au chaud.** Saucisses 12 min à la poêle ; bacon 3 min ; au four.", "**Légumes.** Champignons et demi-tomates côté coupé dans le gras, 5 min ; haricots chauffés.", "**Œufs et toast.** Œufs au plat, toasts beurrés ; tout sur une grande assiette chaude."],
  age=1, cats=["brunch", "enfants"])

K("bigos_volaille", "Bigos (version volaille, sans alcool)", "Bigos", "Europe du Nord › Pologne", "P", 2, 8, 30, 150, "€€", "Grande cocotte.",
  "Le « ragoût du chasseur » polonais : choucroute et chou frais mijotés longuement avec viandes, saucisse fumée, champignons séchés et pruneaux. Meilleur réchauffé. Selon D21 : bœuf et saucisse de volaille, sans vin.",
  ["1 kg|de choucroute crue rincée|Chou blanc / rouge|3", "½|chou blanc émincé|Chou blanc / rouge|2", "500 g|de bœuf à mijoter|Paleron|3", "300 g|de saucisse fumée de volaille|Saucisse de bœuf / de veau / de volaille|2", "20 g|de champignons séchés|Champignon noir séché|1", "8|pruneaux|Pruneaux|1", f"1|oignon|{OIG}|1", f"2 c. à s.|de concentré de tomate|{CONC}|1", f"2|feuilles de laurier|{LAURIER}|1"],
  ["**Viande.** Bœuf en cubes doré avec l'oignon.", "**Mijoter.** Choucroute, chou frais, champignons trempés et leur eau filtrée, pruneaux, laurier, concentré, 50 cl d'eau ; couvert 2 h à feu doux.",
   "**Saucisse.** En rondelles, 20 min. Repos une nuit si possible ; réchauffé avec pain de seigle et pommes de terre."],
  keep="5 jours au frigo ; meilleur le lendemain. Se congèle.", age=3, fetes=["Noël", "Repas de famille"])

K("barszcz", "Barszcz (bouillon de betterave)", "Barszcz czerwony", "Europe du Nord › Pologne", "So", 1, 4, 20, 45, "€", "Faitout.",
  "Un bouillon rubis de betteraves, légumes et ail, aigrelet au citron : servi clair en tasse à Noël en Pologne, ou plus épais avec chou et pommes de terre en Ukraine (borchtch).",
  ["4|betteraves crues|Betterave (crue/cuite)|3", f"2|carottes|{CAROTTE}|1", "1|poireau|Poireau|1", f"1|oignon|{OIG}|1", f"2 gousses|d'ail|{AIL}|1", f"1|citron|{CIT}|2", "1 l|de bouillon de légumes|Bouillon cube légumes|2", "1 c. à s.|d'aneth|Aneth|1", f"10 cl|de crème|{CF}|1?"],
  ["**Bouillon.** Légumes et 3 betteraves en morceaux, 1,2 l d'eau ou bouillon, 40 min ; filtré.", "**Couleur.** 1 betterave crue râpée, 10 min sans bouillir, citron : rouge vif (le citron fixe la couleur).",
   "**Servir.** Ail, sel, sucre si besoin ; en tasse, ou avec crème et aneth."], age=1, cats=["vegetarien"], fetes=["Noël"])

K("chakhchoukha", "Chakhchoukha (galettes émiettées en sauce, Biskra)", "Chakhchoukha", "Maghreb › Algérie › Biskra", "P", 3, 6, 50, 60, "€€", "Poêle épaisse, cocotte, couscoussier.",
  "Fines galettes de semoule cuites à sec, déchirées en petits morceaux, cuites à la vapeur puis arrosées d'une sauce rouge à l'agneau et aux pois chiches : le plat des grandes occasions des Aurès.",
  ["500 g|de semoule fine|Semoule de blé (fine/moyenne)|3", "800 g|d'épaule d'agneau en morceaux|Épaule d'agneau|3", f"200 g|de pois chiches cuits|{POIS}|2", f"2|tomates|{TOM}|1", f"2 c. à s.|de concentré|{CONC}|1", f"1|oignon|{OIG}|1", "1 c. à c.|de ras el-hanout|Ras el-hanout|1", f"1 c. à c.|de paprika|{PAPRIKA}|1", f"60 g|de beurre|{BEURRE}|1"],
  ["**Galettes (rougag).** Semoule, sel, eau : pâte souple ; disques très fins cuits à sec 1 min par face ; déchirés en morceaux de 2 cm.",
   "**Sauce.** Agneau, oignon, épices, concentré, tomates, 1,5 l d'eau, 1 h ; pois chiches.", "**Vapeur et service.** Morceaux à la vapeur 10 min, beurrés, arrosés de sauce, viande dessus."],
  age=3, fetes=["Aïd", "Repas de famille"])

K("kunefe", "Künefe (kadaïf au fromage fondant et sirop)", "Künefe", "Moyen-Orient › Turquie › Hatay", "D", 3, 6, 25, 25, "€€", "Poêle ou petit moule, casserole.",
  "Cheveux d'ange (kadaïf) beurrés, croustillants, autour d'un fromage qui file, arrosés de sirop chaud et de pistaches : à manger tout de suite, brûlant.",
  ["250 g|de pâte kadaïf (épicerie orientale ; sinon filo coupée en fils)|Pâte filo / feuilles de brick|3", "200 g|de mozzarella (ou akawi dessalé)|Mozzarella / burrata|3", f"100 g|de beurre clarifié|Beurre clarifié / ghee|2", f"200 g|de sucre|{SUCRE}|2", f"½|citron|{CIT}|1", "30 g|de pistaches|Pistaches vertes|1", "1 c. à c.|d'eau de fleur d'oranger|Eau de fleur d'oranger|1?"],
  ["**Sirop.** Sucre, 15 cl d'eau, citron, 8 min ; fleur d'oranger ; refroidi.", "**Monter.** Kadaïf effiloché et beurré ; la moitié tassée dans le moule beurré, fromage en tranches égouttées, reste du kadaïf, tassé.",
   "**Cuire.** Poêle à feu moyen, 8 min par face (retourné sur une assiette) ou 200 °C 25 min : doré, fromage fondu. Sirop froid sur künefe brûlant, pistaches."],
  age=3, fetes=["Aïd", "Ramadan"], profil=["sucre"])

K("poulet_tikka_masala", "Poulet tikka masala", "Chicken tikka masala", "Asie du Sud › Inde", "P", 2, 4, 30, 30, "€€", "Four (gril), sauteuse, mixeur.",
  "Poulet mariné au yaourt et aux épices, grillé au four jusqu'à charbonner un peu, dans une sauce tomate-crème épicée : le curry le plus commandé du Royaume-Uni, sans tandoor.",
  [f"700 g|de cuisses désossées ou blancs|{CUISSE}|3", "4 c. à s.|de marinade tandoori|SUB:marinade_tandoori|2", f"400 g|de tomates concassées|{PELEES}|2", f"2|oignons|{OIG}|2", "1 c. à s.|de gingembre-ail|Gingembre frais|1", "2 c. à c.|de garam masala|Garam masala|2", f"1 c. à c.|de paprika|{PAPRIKA}|1", f"15 cl|de crème|{CF}|2", f"1 bouquet|de coriandre|{CORI}|1"],
  ["**Mariner et griller.** Poulet en gros cubes, marinade, 2 h minimum ; sous le gril, plaque haute, 10-12 min : bords noircis.", "**Masala.** Oignons 10 min, gingembre-ail, épices 1 min, tomates 10 min ; mixée lisse.",
   "**Réunir.** Poulet dans la sauce, crème, 8 min ; coriandre. Riz, naan."], age=3, profil=["epice"])

K("thali_vegetarien", "Thali végétarien familial (menu complet)", "Thali", "Asie du Sud › Inde", "P", 3, 6, 120, 0, "€", "Plusieurs casseroles ; plateaux ou grandes assiettes.",
  "Un repas indien complet sur un plateau : dal, légume sec, yaourt, chutney, pain et riz, chacun en petite portion. Un projet de week-end : voici l'ordre de travail pour tout servir chaud en même temps.",
  ["1 recette|de dal tadka|SUB:dal_tadka|3", "1 recette|d'aloo gobi|SUB:aloo_gobi|3", "1 recette|de raïta|SUB:raita|2", "1 recette|de chutney menthe-coriandre|SUB:chutney_menthe|2", "1 recette|de parathas|SUB:paratha|2", f"350 g|de riz basmati|{RIZ}|2", "1|concombre et oignon rouge (kachumber)|Concombre|1"],
  ["**J-1 ou le matin.** Dal cuit (il se réchauffe), pâte à paratha, chutney.", "**1 h avant.** Aloo gobi au four ; raïta et kachumber au frais ; riz lancé 25 min avant.",
   "**Au dernier moment.** Tadka du dal, parathas à la poêle ; petits bols sur chaque plateau, riz et pain au centre. On mélange un peu de chaque à chaque bouchée."],
  tips=["Pour 6 personnes, une portion de chaque recette suffit car tout se partage."], age=1, cats=["vegetarien"], fetes=["Diwali", "Repas de famille"])

K("tteokbokki", "Tteokbokki (gâteaux de riz sauce piquante)", "Tteokbokki", "Asie de l'Est › Corée", "P", 1, 3, 10, 15, "€", "Sauteuse.",
  "Bâtonnets de riz moelleux et élastiques mijotés dans une sauce rouge sucrée-piquante au gochujang, avec œufs durs et cébette : le snack des rues de Séoul. Piment à doser.",
  ["500 g|de gâteaux de riz tteok (rayon frais asiatique)|Farine de riz / riz gluant|3", "2 c. à s.|de gochujang|Gochujang|3", "1 c. à c.|de gochugaru|Gochugaru|1?", f"1 c. à s.|de sucre|{SUCRE}|1", f"1 c. à s.|de sauce soja|{SOJA}|1", "50 cl|de dashi ou d'eau|Dashi (instantané)|1", f"2|œufs durs|{OEUF}|1", "2|cébettes|Oignon nouveau / cébette|1"],
  ["**Tremper.** Tteok durs : 20 min dans l'eau tiède.", "**Sauce.** Dashi, gochujang, gochugaru, sucre, soja, frémissants.", "**Mijoter.** Tteok, 10-12 min en remuant : sauce épaisse et brillante, tteok moelleux ; œufs, cébette."],
  age=6, cats=["vegetarien"], profil=["epice"])

K("dan_dan_noodles", "Dan dan noodles (version bœuf)", "Dàndàn miàn", "Asie de l'Est › Chine › Sichuan", "P", 2, 4, 20, 10, "€", "Wok, casserole.",
  "Nouilles dans une sauce sésame-soja-huile pimentée, couvertes de bœuf haché croustillant et de poivre du Sichuan qui fourmille sur la langue. Bœuf à la place du porc (D21).",
  ["400 g|de nouilles de blé|Nouilles chinoises aux œufs|3", "250 g|de bœuf haché|Bœuf haché|3", "2 c. à s.|de tahini|Tahini (purée de sésame)|2", f"3 c. à s.|de sauce soja|{SOJA}|2", "2 c. à s.|d'huile pimentée|Huile pimentée chinoise|2", "1 c. à c.|de poivre du Sichuan moulu|Poivre du Sichuan|1", "1 c. à s.|de vinaigre noir|Vinaigre noir chinois (Chinkiang)|1", "2|pak-choï|Chou chinois / pak-choï|1?", "2|cébettes|Oignon nouveau / cébette|1"],
  ["**Bœuf.** Wok chaud, 6 min sans trop remuer : doré et croustillant ; 1 c. à s. de soja.", "**Sauce au fond des bols.** Tahini, soja, vinaigre, huile pimentée, poivre du Sichuan, 3 c. à s. d'eau des nouilles.",
   "**Servir.** Nouilles et pak-choï cuits, égouttés dans les bols, bœuf, cébette ; on mélange tout."], age=6, profil=["epice"])

K("canard_laque_four", "Canard laqué (version four)", "Běijīng kǎoyā", "Asie de l'Est › Chine › Pékin", "P", 3, 6, 40, 1560, "€€€", "Four, grille + lèchefrite, pinceau.",
  "Peau ébouillantée, laquée de miel et séchée une nuit au frigo, puis rôtie : brillante et craquante. Servie en crêpes fines avec concombre, cébette et sauce hoisin.",
  ["1|canard entier de 2 kg|Canard entier / carcasse|3", f"3 c. à s.|de miel|{MIEL}|2", "1 c. à c.|de cinq-épices|Cinq-épices chinois|2", f"3 c. à s.|de sauce soja|{SOJA}|1", "1 c. à s.|de vinaigre de riz|Vinaigre de riz|1", "1|concombre|Concombre|1", "4|cébettes|Oignon nouveau / cébette|1", "20|crêpes fines (mandarin) ou galettes de riz|Galettes de riz (rice paper)|2", "4 c. à s.|de sauce hoisin (ou soja + miel + sésame)|Sauce d'huître|1?"],
  ["**Ébouillanter et sécher.** Intérieur frotté de cinq-épices et soja ; peau arrosée d'eau bouillante (elle se tend), puis laquée miel + vinaigre ; une nuit au frigo à découvert sur grille.",
   "**Rôtir.** 160 °C 1 h 15 sur grille au-dessus d'une lèchefrite d'eau, puis 220 °C 15 min : peau acajou et craquante.",
   "**Servir.** Peau et chair tranchées fin ; crêpes, hoisin, concombre et cébette en bâtonnets."], age=3, fetes=["Nouvel An chinois"], tech=["rôtir une volaille"])

K("hot_pot_familial", "Hot pot familial (fondue chinoise)", "Huǒguō", "Asie de l'Est › Chine › Sichuan", "P", 2, 6, 40, 0, "€€€", "Réchaud et caquelon (ou appareil à fondue), petites épuisettes.",
  "Une marmite de bouillon frémissant au centre de la table, où chacun cuit lamelles de bœuf, crevettes, tofu, champignons et légumes, puis les trempe dans sa sauce. Bouillon doux pour les enfants, pimenté pour les autres.",
  ["2 l|de bouillon de volaille|Bouillon cube volaille|3", "600 g|de bœuf en lamelles très fines|Rumsteck|3", "300 g|de crevettes|Crevettes (cuites/crues)|2", "400 g|de tofu|Tofu (ferme / soyeux)|2", "300 g|de champignons (shiitake, enoki)|Shiitake|2", "1|chou chinois|Chou chinois / pak-choï|2", "200 g|de nouilles|Nouilles de riz / vermicelles|1", "1 morceau|de gingembre|Gingembre frais|1", "2 c. à s.|d'huile pimentée|Huile pimentée chinoise|1?"],
  ["**Bouillon.** Bouillon, gingembre, cébette ; une moitié corsée d'huile pimentée et de poivre du Sichuan si caquelon double.", "**Plateaux.** Viande étalée en rosace (mi-congelée pour la trancher fin), crevettes, tofu en cubes, légumes, nouilles.",
   "**Sauces.** Chacun compose : soja, sésame, ail, cébette, vinaigre noir, tahini. **À table :** viande 20-30 s, crevettes 2 min ; nouilles en dernier dans le bouillon devenu riche. Viande crue : baguettes séparées."],
  age=3, fetes=["Nouvel An chinois", "Repas de famille"])

K("roti_canai", "Roti canai (pain feuilleté malaisien)", "Roti canai", "Asie du Sud-Est › Malaisie", "Pa", 3, 8, 40, 600, "€", "Plan de travail huilé, poêle.",
  "Une pâte huilée qu'on étire jusqu'à la transparence, plie et cuit à la poêle : feuilletée, croustillante et moelleuse. Avec un dal ou un curry pour tremper.",
  [f"500 g|de farine|{F55}|3", f"1|œuf|{OEUF}|1", f"25 cl|de lait|{LAIT}|2", f"1 c. à s.|de sucre|{SUCRE}|1", "100 g|de ghee ou beurre fondu|Ghee|2", f"10 cl|d'huile neutre|{HN}|1"],
  ["**Pâte.** Farine, sel, sucre, œuf, lait, 5 cl d'eau ; pétrie 10 min : très souple ; 8 boules huilées, une nuit (ou 6 h) couvertes : c'est ce repos qui permet d'étirer.",
   "**Étirer.** Plan huilé ; boule aplatie puis étirée du bout des doigts vers l'extérieur jusqu'à voir le plan à travers ; ghee ; repliée en carré.",
   "**Cuire.** Poêle moyenne, 2 min par face : doré ; tapé entre les mains pour ouvrir les feuilles. Avec dal ou curry."], age=1, cats=["vegetarien"])

K("apple_pie", "Apple pie américaine", "Apple pie", "Amérique du Nord › États-Unis", "D", 2, 8, 40, 60, "€€", "Moule à tarte profond, rouleau.",
  "Une tourte à double pâte beurrée, garnie d'un kilo de pommes à la cannelle et au sucre roux : croûte feuilletée, fruits fondants qui tiennent. Avec une boule de glace vanille.",
  ["2|pâtes brisées (ou maison)|Pâte brisée / sablée (prête)|3", "1,2 kg|de pommes (mélange acidulées et sucrées)|Pomme|3", "100 g|de sucre roux|Sucre blanc / roux / cassonade / vergeoise|2", f"1 c. à c.|de cannelle|{CANN}|1", f"2 c. à s.|de fécule|Fécule de maïs (maïzena)|1", f"½|citron|{CIT}|1", f"20 g|de beurre|{BEURRE}|1", f"1|œuf (dorure)|{OEUF}|1"],
  ["**Garniture.** Pommes en tranches de 5 mm, sucre, cannelle, fécule, citron, 20 min : elles rendent du jus.", "**Monter.** Pâte au fond, pommes en dôme (sans le jus), noisettes de beurre, couvercle soudé, 4 entailles, dorure, sucre.",
   "**Cuire.** 220 °C 20 min puis 180 °C 40 min : jus qui bouillonne par les entailles. Refroidir 2 h (sinon le jus coule)."], age=1, cats=["enfants"], fetes=["Repas de famille"], profil=["sucre"])

K("ribs_boeuf_laques", "Ribs de bœuf laqués (plat de côtes)", "Beef short ribs", "Amérique du Nord › États-Unis", "P", 2, 4, 20, 210, "€€€", "Plat à four, aluminium.",
  "Le plat de côtes de bœuf cuit très lentement en papillote, puis laqué d'une sauce barbecue au four : la viande se détache de l'os. À la place des travers de porc.",
  ["1,6 kg|de plat de côtes de bœuf (short ribs)|Paleron|3", f"1 c. à s.|de paprika fumé|{PFUME}|2", f"1 c. à s.|de sucre roux|{SUCRE}|1", "1 c. à c.|de poudre d'ail|Poudre d'ail / d'oignon|1", "15 cl|de ketchup|Ketchup|2", f"3 c. à s.|de miel|{MIEL}|1", "2 c. à s.|de sauce Worcestershire|Sauce Worcestershire|1", f"2 c. à s.|de vinaigre de cidre|{CIDRE}|1"],
  ["**Frotter.** Paprika, sucre, ail, sel, poivre ; une nuit au frais si possible.", "**Confire.** Papillote serrée, 150 °C, 3 h : la viande cède sous la fourchette.",
   "**Laquer.** Sauce : ketchup, miel, Worcestershire, vinaigre réduits 5 min ; ribs badigeonnés, 220 °C, 15 min en badigeonnant 2 fois : collants et brillants."], age=1, cats=["enfants"], fetes=["Barbecue d'été"])

K("tamales_poulet", "Tamales au poulet en feuille de bananier", "Tamales oaxaqueños", "Amérique latine › Mexique › Oaxaca", "P", 3, 12, 75, 90, "€€", "Grand faitout avec panier vapeur.",
  "Pâte de maïs fouettée avec du bouillon et du beurre (à la place du saindoux), farcie de poulet en sauce rouge, enveloppée et cuite à la vapeur : les petits paquets de fête mexicains.",
  ["500 g|de farine de maïs nixtamalisée (masa harina)|Farine de maïs|3", f"150 g|de beurre mou (à la place du saindoux)|{BEURRE}|2", "50 cl|de bouillon de volaille|Bouillon cube volaille|2", f"1 c. à c.|de levure chimique|{LEVC}|1", f"400 g|de poulet cuit effiloché|{BLANC_P}|3", "3|piments séchés (ou paprika fumé)|Piments ancho / chipotle / guajillo / pasilla|2", f"2|tomates|{TOM}|1", "1 paquet|de feuilles de bananier (ou papier sulfurisé)|Feuille de bananier|2"],
  ["**Farce.** Piments trempés mixés avec tomates, ail, sel, 10 min de cuisson ; poulet dedans.", "**Masa.** Beurre fouetté 3 min, masa, levure, sel, bouillon tiède petit à petit, 5 min : légère (une boulette flotte dans l'eau).",
   "**Envelopper et cuire.** Rectangles de feuille passés à la flamme (souples), masa étalée, farce, pliés en paquet ; debout dans le panier, 1 h 30 de vapeur : la pâte se détache de la feuille."],
  keep="5 jours au frigo ; 3 mois au congélateur (vapeur 20 min).", age=3, fetes=["Noël", "Repas de famille"])

K("griot_poulet", "Griot (version poulet) et pikliz", "Griyo", "Amérique latine › Haïti", "P", 2, 4, 30, 90, "€€", "Cocotte, poêle.",
  "Le griot haïtien est du porc mariné aux agrumes et à l'épis, braisé puis frit. Selon D21 : version poulet, même méthode, avec le pikliz (chou mariné au vinaigre et au piment) et des bananes pesées.",
  [f"1 kg|de hauts de cuisse en morceaux|{CUISSE}|3", "2|oranges amères (ou 1 orange + 1 citron vert)|Orange|2", f"2|citrons verts|{CITV}|1", f"1 bouquet|de persil et thym|{PERSIL}|1", f"4 gousses|d'ail|{AIL}|1", "1|piment scotch bonnet (ou piment oiseau)|Piment scotch bonnet|1", "¼|chou|Chou blanc / rouge|1", f"25 cl|de vinaigre blanc|Vinaigre blanc|1", "2|plantains verts|Plantain (banane à cuire)|1?"],
  ["**Pikliz (la veille).** Chou, carotte, oignon émincés, piment, vinaigre, sel, en bocal.", "**Mariner et braiser.** Poulet frotté d'épis (persil, thym, ail, cébette, piment mixés), jus d'agrumes, 4 h ; braisé à couvert dans la marinade + 20 cl d'eau, 40 min, jusqu'à évaporation.",
   "**Frire.** Morceaux dorés dans 1 cm d'huile, 5 min : croustillants. Pikliz, bananes pesées, riz collé."], age=6, profil=["epice"])

K("couscous_sept_legumes", "Couscous aux sept légumes (végétarien)", "Seksu bi sebaa khodra", "Maghreb › Maroc", "P", 1, 6, 30, 60, "€", "Couscoussier ou faitout.",
  "Le couscous du vendredi marocain dans sa version végétale : sept légumes de saison, pois chiches, bouillon au safran et au ras el-hanout, tfaya (oignons-raisins confits) en option.",
  ["500 g|de semoule moyenne|Semoule de couscous|3", f"3|carottes|{CAROTTE}|2", "2|courgettes|Courgette|2", "2|navets|Navet / navet boule d'or|2", "300 g|de courge|Potiron / citrouille|2", f"2|tomates|{TOM}|1", f"200 g|de pois chiches cuits|{POIS}|2", "1 pincée|de safran|Safran (pistils)|1", "1 c. à c.|de ras el-hanout|Ras el-hanout|1", f"2|oignons (+ 40 g de raisins secs pour la tfaya)|{OIG}|1?"],
  ["**Bouillon.** Oignon, tomates, épices, 2 l d'eau, 15 min ; carottes et navets 20 min (un quart de chou si tu en as) ; courgettes, courge, pois chiches 15 min.", "**Graine.** Deux passages à la vapeur (ou express : 1 pour 1 d'eau bouillante salée + beurre, 5 min).",
   "**Tfaya.** Oignons émincés et raisins fondus 30 min avec cannelle et miel. Graine en dôme, légumes en pyramide, bouillon à part."], age=1, cats=["vegetarien", "enfants"], fetes=["Repas de famille"])

K("mechoui_four", "Méchoui d'épaule d'agneau au four", "Méchoui", "Maghreb › Maroc", "P", 1, 6, 15, 240, "€€€", "Plat à four avec couvercle ou aluminium.",
  "L'esprit du méchoui sans broche : épaule frottée de beurre, cumin et ail, cuite 4 heures à four doux jusqu'à s'effilocher, puis dorée. On la mange à la main avec du cumin et du sel.",
  ["1|épaule d'agneau de 2 kg avec os|Épaule d'agneau|3", f"80 g|de beurre mou (ou smen)|{BEURRE}|2", f"2 c. à s.|de cumin|{CUMIN}|2", f"6 gousses|d'ail|{AIL}|1", f"1 c. à c.|de paprika|{PAPRIKA}|1", f"1 c. à c.|de gros sel|{SEL}|1"],
  ["**Frotter.** Beurre écrasé avec ail, cumin, paprika, sel ; épaule entaillée, frottée partout, 2 h (ou une nuit).", "**Cuire lentement.** Couvert, 20 cl d'eau, 150 °C, 3 h 30 en arrosant toutes les heures.",
   "**Dorer.** Découvert, 220 °C, 20 min : croûte dorée. Cumin et sel en coupelles ; pain, salade méchouia."], age=1, fetes=["Aïd", "Repas de famille"], tech=["rôtir"])

K("baba_ghanoush", "Baba ghanoush (caviar d'aubergine fumé au tahini)", "Baba ghanoush", "Moyen-Orient › Liban", "E", 1, 6, 15, 30, "€", "Feu de gaz, gril ou barbecue.",
  "Aubergines brûlées à la flamme jusqu'à s'effondrer, écrasées avec tahini, citron et ail : fumé, crémeux, le compagnon du houmous.",
  ["3|aubergines|Aubergine|3", "3 c. à s.|de tahini|Tahini (purée de sésame)|2", f"1|citron|{CIT}|2", f"1 gousse|d'ail|{AIL}|1", f"3 c. à s.|d'huile d'olive|{HO}|1", f"1 c. à s.|de persil|{PERSIL}|1", "1|grenade (graines)|Grenade|1?"],
  ["**Brûler.** Aubergines entières sur la flamme ou sous le gril, 20-25 min en tournant : peau noire, chair effondrée ; égouttées 10 min dans une passoire.", "**Écraser.** Chair à la fourchette (pas au mixeur : texture), tahini, citron, ail râpé, sel.", "**Servir.** Huile d'olive, persil, grenade ; pain."],
  age=3, cats=["vegetarien"], fetes=["Apéritif dînatoire", "Ramadan"])

# ——— Plats végétariens de tous les jours (le seuil validé de 33 % de plats sans chair) ———
K("quiche_poireaux", "Quiche aux poireaux et comté", "Flamiche légère / quiche aux poireaux", "France › Hauts-de-France", "P", 1, 6, 20, 40, "€", "Moule à tarte, sauteuse.",
  "Poireaux fondus au beurre, crème, œufs et comté dans une pâte brisée : la quiche végétarienne qu'on fait toute l'année, avec une salade verte.",
  ["1|pâte brisée|Pâte brisée / sablée (prête)|3", "3|poireaux|Poireau|3", f"3|œufs|{OEUF}|2", f"20 cl|de crème|{CF}|2", f"10 cl|de lait|{LAIT}|1", f"100 g|de comté râpé|{GRUY}|2", f"20 g|de beurre|{BEURRE}|1", f"1 pincée|de muscade|{MUSC}|0"],
  ["**Fondre.** Poireaux émincés et lavés, beurre, 15 min à couvert : tendres, sans couleur.", "**Appareil.** Œufs, crème, lait, sel, poivre, muscade.",
   "**Cuire.** Pâte, poireaux, comté, appareil ; 180 °C, 35-40 min : prise et dorée."], age=1, cats=["vegetarien", "enfants"])

K("gratin_ravioles", "Gratin de ravioles du Dauphiné", "Gratin de ravioles", "France › Auvergne-Rhône-Alpes › Romans-sur-Isère", "P", 1, 4, 10, 20, "€€", "Plat à gratin.",
  "Les minuscules ravioles au comté et au persil (achetées en plaques) en couches avec de la crème et du fromage : gratinées en 20 minutes, un plat de fête express.",
  ["4 plaques|de ravioles du Dauphiné|Pâtes fraîches aux œufs|3", f"30 cl|de crème|{CF}|3", f"100 g|de comté râpé|{GRUY}|2", f"1 c. à s.|de persil|{PERSIL}|1", f"1 pincée|de muscade|{MUSC}|0"],
  ["**Monter.** Plat beurré, une plaque de ravioles, crème, fromage ; ainsi de suite.", "**Gratiner.** 200 °C, 15-20 min : bouillonnant et doré.", "**Servir.** Persil, salade verte aux noix."],
  age=1, cats=["vegetarien", "enfants", "express"])

K("gnocchi_gorgonzola_noix", "Gnocchi gorgonzola et noix", "Gnocchi al gorgonzola", "Europe du Sud › Italie › Lombardie", "P", 1, 4, 10, 10, "€€", "Casserole, sauteuse.",
  "Gnocchi enrobés d'une sauce fondante au gorgonzola et à la crème, noix grillées et poivre : prêt en 15 minutes.",
  ["800 g|de gnocchi|Gnocchi|3", "150 g|de gorgonzola|Roquefort / bleu|3", f"15 cl|de crème|{CF}|2", "40 g|de noix|Noix|1", f"20 g|de parmesan|{PARM}|1"],
  ["**Sauce.** Gorgonzola et crème fondus à feu doux, 3 min.", "**Gnocchi.** Eau bouillante salée, retirés dès qu'ils remontent.", "**Lier.** Dans la sauce avec une louche d'eau de cuisson ; noix grillées, parmesan, poivre."],
  age=3, cats=["vegetarien", "express"])

K("pasta_e_ceci", "Pasta e ceci (pâtes aux pois chiches, Rome)", "Pasta e ceci", "Europe du Sud › Italie › Latium", "P", 1, 4, 10, 25, "€", "Cocotte.",
  "Pois chiches en partie mixés, ail, romarin et tomate, petites pâtes cuites dedans : entre la soupe et le plat, le repas du vendredi romain. Placard uniquement.",
  [f"500 g|de pois chiches cuits|{POIS}|3", "200 g|de petites pâtes (ditalini)|Pâtes sèches (spaghetti, penne…)|3", f"2 gousses|d'ail|{AIL}|1", "1 brin|de romarin|Thym / romarin|1", f"2 c. à s.|de concentré de tomate|{CONC}|1", f"4 c. à s.|d'huile d'olive|{HO}|2", f"40 g|de parmesan|{PARM}|1?"],
  ["**Base.** Ail et romarin dans l'huile 1 min, concentré, pois chiches et 1 l d'eau, 10 min ; la moitié mixée.", "**Pâtes.** Cuites dedans, 10 min en remuant : crémeux (rallonge d'eau chaude si besoin).", "**Servir.** Huile d'olive crue, poivre, parmesan."],
  age=1, cats=["vegetarien", "enfants"])

K("stroganoff_champignons", "Stroganoff de champignons", "Mushroom stroganoff", "Europe du Nord › Russie", "P", 1, 4, 15, 15, "€", "Grande poêle.",
  "La sauce du bœuf Stroganov (crème, moutarde, paprika) sur des champignons bien saisis : végétarien, rapide, avec du riz ou des pâtes.",
  ["600 g|de champignons variés|Champignon de Paris|3", f"1|oignon|{OIG}|1", f"20 cl|de crème|{CF}|2", f"1 c. à s.|de moutarde|{DIJON}|1", f"1 c. à c.|de paprika|{PAPRIKA}|1", f"1 c. à s.|de sauce soja|{SOJA}|1", f"20 g|de beurre|{BEURRE}|1", f"1 c. à s.|de persil|{PERSIL}|1"],
  ["**Saisir.** Champignons en quartiers, poêle très chaude en 2 fois sans remuer 3 min : dorés (pas bouillis).", "**Sauce.** Oignon 5 min, paprika, soja, crème, moutarde, 2 min.", "**Réunir.** Champignons, persil. Riz, pâtes ou purée."],
  age=1, cats=["vegetarien", "express"])
