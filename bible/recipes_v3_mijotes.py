# -*- coding: utf-8 -*-
"""Vague 4 · Audit du chef, suite (16/10/2026) : les grands mijotés longs. D'abord les trois plats que le Tome 4 avait mis de côté
à cause du porc ou de l'alcool (fabada, tripes, choucroute garnie), en « version » selon D21. Ensuite les mijotés du monde qui
méritent leur place à table, et des mijotés végétariens pour garder la part de plats sans chair (contrôle 63).
Chaque fiche donne la cuisson à l'autocuiseur (Cocotte-Minute), l'appareil le plus courant des cuisines françaises. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

KEEP = "4 jours au frigo, meilleur réchauffé le lendemain ; 3 mois au congélateur."
FROID = "Un grand mijoté se refroidit vite : réparti dans des boîtes peu profondes, au frigo dans les 2 heures (jamais toute une nuit sur le feu éteint)."
VR = ("Sans alcool", ["alcohol"], {"Vin rouge": [("Bouillon cube bœuf", 0.8), ("Jus de pomme / raisin / orange (pur jus)", 0.2)]},
      "Vin rouge → **bouillon + un peu de jus de raisin** et 1 c. à s. de vinaigre de vin. **À tester**.")
VB = ("Sans alcool", ["alcohol"], {"Vin blanc": [("Bouillon cube volaille", 0.8), ("Citron", 0.1)]}, "Vin blanc → **bouillon + un trait de citron**. **À tester**.")

# ——— Les trois plats du Tome 4 mis de côté, en « version » (D21) ———
K("fabada_version", "Fabada asturiana (version bœuf et volaille)", "Fabada asturiana", "Europe du Sud › Espagne › Asturies", "P", 2, 6, 25, 180, "€€", "Grande cocotte en fonte.",
  "Le grand plat des Asturies : de gros haricots blancs fondants mijotés avec chorizo, boudin et lard. Ici en version sans porc (D21) : chorizo de bœuf, jarret et bœuf fumé, paprika fumé et safran. Le goût fumé et la sauce épaisse restent ; ce n'est pas l'original et la fiche le dit.",
  ["500 g|de gros haricots blancs secs (fabes, ou lingots)|Haricots blancs / lingots|3", "250 g|de chorizo de bœuf ou de volaille|Chorizo de bœuf ou de volaille|3", "400 g|de jarret de bœuf|Jarret de bœuf|2", "100 g|de bœuf fumé (pastrami) en morceau|Pastrami / bœuf fumé|2", f"1|oignon|{OIG}|1", f"4 gousses|d'ail|{AIL}|1", f"1 c. à c.|de paprika fumé|{PFUME}|2", "1 pincée|de safran|Safran (pistils)|1?", f"2|feuilles de laurier|{LAURIER}|1"],
  ["**La veille.** Haricots dans trois fois leur volume d'eau froide, 12 h.", "**Départ à froid.** Haricots égouttés, viandes entières, oignon et ail entiers, laurier, eau à 2 cm au-dessus ; porter doucement à frémissement en écumant.",
   "**Mijoter sans remuer.** 2 h 30 à 3 h à feu très doux, à peine un frémissement ; on « effraie » les haricots 3 fois avec un verre d'eau froide et on secoue la cocotte au lieu de remuer (ils restent entiers). Paprika et safran à mi-cuisson.",
   "**Finir.** Haricots fondants, sauce épaissie et orangée ; viandes coupées et remises ; sel à la fin seulement. Repos 20 min hors du feu."],
  tips=["**Autocuiseur** : 35 min après la mise en rotation de la soupape, puis 15 min à découvert pour épaissir.", "Les haricots durcissent si on sale trop tôt : sel en fin de cuisson.", FROID],
  keep=KEEP, age=3, fetes=["Repas de famille"])

K("tripes_caen_version", "Tripes à la mode de Caen (version sans alcool)", "Tripes à la mode de Caen", "France › Normandie › Caen", "P", 2, 8, 30, 480, "€€", "Grande cocotte en fonte avec couvercle (ou tripière), four.",
  "Le plat de la confrérie de Caen : gras-double de bœuf et pied de bœuf cuits huit heures au four avec carottes, oignons et poireau, jusqu'à devenir fondants dans une gelée parfumée. L'original se mouille au cidre et se relève au calvados ; cette version sans alcool remplace le cidre par du jus de pomme brut et un trait de vinaigre de cidre.",
  ["1,5 kg|de tripes de bœuf blanchies (gras-double, panse, feuillet)|Tripes / gras-double de bœuf|3", "1|pied de veau ou de bœuf fendu|Pied de veau / de bœuf|3", f"4|carottes|{CAROTTE}|2", f"3|oignons piqués de clous de girofle|{OIG}|2", "1|poireau|Poireau|1", "50 cl|de jus de pomme brut (non sucré)|Jus de pomme / raisin / orange (pur jus)|2", "2 c. à s.|de vinaigre de cidre|Vinaigre de cidre|1", f"1|bouquet garni (thym, laurier, persil)|{THYM}|1", "1 l|de bouillon de bœuf maison (ou d'eau)|Bouillon d'os maison (bœuf/volaille)|2"],
  ["**Préparer.** Tripes rincées et coupées en carrés de 5 cm ; pied blanchi 10 min, rincé.", "**Monter.** Dans la cocotte : pied au fond, carottes en tronçons, oignons, poireau, tripes, bouquet garni, sel, poivre ; jus de pomme, vinaigre, bouillon à hauteur.",
   "**Luter et cuire.** Couvercle fermé (un boudin de farine et d'eau autour l'étanchéifie) ; four 140 °C, 8 h sans ouvrir.",
   "**Servir.** C'est cuit quand un morceau de tripe se coupe à la cuillère. Os du pied retirés, gras dégraissé en surface ; brûlant, dans des assiettes chaudes, avec des pommes de terre vapeur."],
  tips=["**Autocuiseur** : 1 h 30 après la rotation de la soupape ; le goût est un peu moins fondu qu'au four.", "Chez le boucher, demande des tripes « blanchies » : le nettoyage, long, est déjà fait.", FROID],
  keep="3 jours au frigo ; la gelée qui prend au froid est normale (elle refond en chauffant). Se congèle 3 mois.", age=None, fetes=["Repas de famille"])

K("choucroute_garnie_version", "Choucroute garnie (version bœuf et volaille)", "Choucroute garnie", "France › Grand Est › Alsace", "P", 1, 6, 30, 120, "€€", "Grande cocotte.",
  "Le plat d'hiver de l'Alsace : choucroute crue braisée au riesling et au genièvre, garnie de saucisses, de viandes fumées et de pommes de terre. Ici sans porc (D21) : saucisses de Strasbourg de volaille, bœuf fumé, poitrine de dinde fumée.",
  ["1,5 kg|de choucroute crue|Chou blanc / rouge|3", "6|saucisses de Strasbourg de volaille ou de bœuf|Saucisse de bœuf / de veau / de volaille|3", "300 g|de poitrine de dinde fumée|Bacon de dinde / de bœuf|2", "400 g|de bœuf fumé en morceau|Pastrami / bœuf fumé|2", f"25 cl|de riesling|Vin blanc|2", f"1|oignon|{OIG}|1", "10|baies de genièvre|Baies de genièvre|2", f"6|pommes de terre|{PDT}|2", f"40 g|de graisse de canard ou beurre|Graisse de canard|1"],
  ["**Choucroute.** Rincée à l'eau froide si elle est très acide, pressée.", "**Braiser.** Oignon fondu dans la graisse, choucroute, genièvre, laurier ; riesling et 25 cl d'eau ; bœuf fumé et dinde fumée enfouis ; couvert, 1 h 30 à feu doux.",
   "**Garnir.** Pommes de terre épluchées posées dessus, 30 min ; saucisses 10 min à la fin (elles éclatent si elles bouillent).", "**Servir.** Choucroute en dôme, viandes tranchées autour, moutarde et raifort."],
  tips=["**Autocuiseur** : 25 min pour la choucroute et les viandes, puis pommes de terre 8 min.", FROID],
  keep=KEEP, age=3, fetes=["Repas de famille"], var=[VB])

# ——— Mijotés du monde ———
K("carbonnade_flamande", "Carbonnade flamande", "Stoofvlees / carbonade flamande", "Europe du Nord › Belgique", "P", 1, 6, 25, 180, "€€", "Cocotte en fonte.",
  "Bœuf mijoté longuement dans la bière brune avec des oignons fondus, une tranche de pain d'épices tartinée de moutarde qui lie la sauce et un peu de cassonade : sucré, amer et profond. Avec des frites, en Belgique.",
  ["1,5 kg|de paleron ou joue de bœuf en gros cubes|Paleron|3", "50 cl|de bière brune|Bière (blonde, brune, blanche)|3", f"4|oignons|{OIG}|2", "2 tranches|de pain d'épices (ou 6 spéculoos)|Biscuits (spéculoos, sablés)|2", f"2 c. à s.|de moutarde|{DIJON}|1", "1 c. à s.|de cassonade|Sucre blanc / roux / cassonade / vergeoise|1", f"1 c. à s.|de vinaigre de cidre|{CIDRE}|1", f"1|bouquet thym-laurier|{THYM}|1", f"30 g|de beurre|{BEURRE}|1"],
  ["**Saisir.** Bœuf séché, coloré en 3 fois dans le beurre très chaud : croûte brune ; réservé.", "**Oignons.** Émincés, 15 min dans la même cocotte : blonds ; cassonade, vinaigre, 2 min.",
   "**Mijoter.** Viande, bière, bouquet ; pain d'épices tartiné de moutarde posé dessus (il fond et lie) ; couvert, 3 h à feu très doux ou four 150 °C.", "**Finir.** Sauce nappante et brillante ; trop amère : un peu de cassonade. Frites ou purée."],
  tips=["**Autocuiseur** : 50 min, puis 10 min à découvert.", FROID], keep=KEEP, age=3, fetes=["Repas de famille"],
  var=[("Sans alcool", ["alcohol"], {"Bière (blonde, brune, blanche)": [("Bière 0,0 % / vin désalcoolisé", 1.0)]}, "Bière brune → **bière brune 0,0 %** (ou bouillon + 1 c. à s. de café fort). **À tester**.")])

K("cocido_madrileno_version", "Cocido madrileño (version sans porc)", "Cocido madrileño", "Europe du Sud › Espagne › Madrid", "P", 2, 6, 30, 180, "€€", "Très grand faitout.",
  "Le pot-au-feu de Madrid, servi en trois temps (« vuelcos ») : d'abord le bouillon avec des vermicelles, puis pois chiches et légumes, enfin les viandes. Version sans porc (D21) : bœuf, poule, chorizo de bœuf.",
  [f"400 g|de pois chiches secs|{POIS}|3", "600 g|de jarret ou macreuse de bœuf|Jarret de bœuf|3", f"4|cuisses de poulet|{CUISSE}|2", "200 g|de chorizo de bœuf|Chorizo de bœuf ou de volaille|2", "½|chou vert|Chou vert / frisé / kale|1", f"4|carottes|{CAROTTE}|1", f"6|pommes de terre|{PDT}|1", "100 g|de vermicelles|Pâtes sèches (spaghetti, penne…)|1", f"4 gousses|d'ail|{AIL}|1"],
  ["**La veille.** Pois chiches trempés 12 h dans l'eau tiède salée.", "**Bouillon.** Bœuf dans 4 l d'eau froide, écumé ; pois chiches dans un filet, poulet, 2 h 30 à frémissement.",
   "**Légumes.** Carottes et pommes de terre 30 min ; chou cuit à part avec le chorizo (il rougirait le bouillon), sauté à l'ail.", "**Trois services.** Bouillon filtré + vermicelles 4 min ; puis pois chiches et légumes ; enfin viandes tranchées. Restes : ropa vieja ou croquetas."],
  tips=["**Autocuiseur** : pois chiches et bœuf 45 min, poulet et légumes 10 min de plus.", FROID],
  keep=KEEP, age=1, cats=["enfants"], fetes=["Repas de famille"], zw=["restes de viande → croquettes"])

K("dafina", "Dafina (skhina, mijoté du shabbat marocain)", "Dafina / skhina", "Maghreb › Maroc", "P", 2, 8, 40, 720, "€€", "Grande cocotte en fonte qui va au four, sachet de cuisson ou mousseline.",
  "Le plat que les familles juives du Maroc mettent au four le vendredi soir pour le déjeuner du samedi : bœuf, pois chiches, pommes de terre, patates douces, blé et œufs entiers qui deviennent bruns et fondants après une nuit à four très doux.",
  ["1 kg|de paleron ou jarret de bœuf|Paleron|3", f"250 g|de pois chiches trempés|{POIS}|2", "200 g|de blé dur ou boulgour gros|Boulgour|2", f"6|pommes de terre|{PDT}|2", "2|patates douces|Patate douce|2", f"6|œufs entiers dans leur coquille, lavés|{OEUF}|2", "6|dattes|Datte (medjool, deglet)|1", f"1 c. à c.|de curcuma|{CURC}|1", f"1 c. à c.|de paprika|{PAPRIKA}|1", f"½ c. à c.|de cannelle|{CANN}|1"],
  ["**Fond.** Viande dorée, pois chiches, dattes et épices au fond de la cocotte.", "**Le blé.** Mélangé à 2 c. à s. d'huile, sel, paprika, posé dans un sachet de cuisson noué lâche (il gonfle) au centre.",
   "**Couches.** Pommes de terre et patates douces entières autour, œufs entiers lavés posés dans les creux ; eau à hauteur, sel.",
   "**Nuit au four.** Porter à frémissement, couvercle fermé, four 100 °C toute la nuit (10 à 12 h). Servir en plats séparés : viande, blé, légumes, œufs écalés bruns."],
  tips=["Les œufs cuits 12 h sont crémeux et brun clair : c'est voulu (« huevos haminados »).", "Sans four allumé la nuit : mijoteuse électrique, position basse, 10 h.", FROID],
  keep=KEEP, age=1, cats=["enfants"], fetes=["Repas de famille", "Shabbat"])

K("haleem", "Haleem (blé, lentilles et bœuf fondus)", "Haleem", "Asie du Sud › Pakistan › Hyderabad", "P", 2, 8, 40, 240, "€€", "Grande cocotte, mixeur plongeant ou presse-purée.",
  "Blé, lentilles et viande mijotés des heures puis battus jusqu'à devenir une crème épaisse et filante, garnie d'oignons frits, gingembre, citron et coriandre : le plat de rupture du jeûne pendant le Ramadan, de Hyderabad à Karachi.",
  ["700 g|de bœuf (paleron) ou d'agneau|Paleron|3", "200 g|de blé concassé ou boulgour|Boulgour|3", "150 g|de lentilles corail et pois cassés mélangés|Lentilles corail|2", f"3|oignons émincés et frits|{OIG}|2", "1 c. à s.|de gingembre-ail|Gingembre frais|1", "2 c. à c.|de garam masala|Garam masala|2", f"½ c. à c.|de curcuma|{CURC}|1", "4 c. à s.|de ghee|Ghee|2", f"2|citrons verts|{CITV}|1", f"1 bouquet|de coriandre et menthe|{CORI}|1"],
  ["**La veille.** Blé trempé dans l'eau.", "**Viande.** Gingembre-ail, épices dans le ghee ; viande, eau à hauteur, 2 h à couvert : elle s'effiloche.",
   "**Céréales.** Blé et lentilles cuits à part dans 1,5 l d'eau, 1 h 30 : défaits.", "**Battre.** Tout réuni, 30 min à feu doux en battant à la cuillère (ou quelques impulsions de mixeur) : texture de porridge filant. Oignons frits, gingembre en julienne, citron, herbes, garam masala."],
  tips=["**Autocuiseur** : viande 40 min, céréales 30 min.", FROID], keep=KEEP, age=1, fetes=["Ramadan", "Aïd"], profil=["epice"])

K("nihari", "Nihari (jarret de bœuf mijoté toute la nuit)", "Nihari", "Asie du Sud › Pakistan › Lahore", "P", 2, 6, 30, 360, "€€", "Cocotte en fonte.",
  "« Nihar » veut dire le matin : le jarret de bœuf mijote toute la nuit dans une sauce épicée au fenouil et au gingembre, liée à la farine complète, et se mange au petit matin avec du naan, gingembre, piment vert et citron. Le plat du vendredi de Lahore et Karachi.",
  ["1,5 kg|de jarret de bœuf avec os|Jarret de bœuf|3", "3 c. à s.|de farine complète|Farine de blé T80 (semi-complète)|2", f"2|oignons|{OIG}|2", "1 c. à s.|de gingembre-ail|Gingembre frais|1", "2 c. à c.|de garam masala|Garam masala|2", "1 c. à c.|de graines de fenouil|Carvi / fenouil / anis vert (graines)|1", f"1 c. à c.|de piment|{CAYENNE}|1", "5 c. à s.|de ghee|Ghee|2", f"2|citrons verts|{CITV}|1", "1 morceau|de gingembre (julienne)|Gingembre frais|1"],
  ["**Saisir.** Oignons dorés dans le ghee (moitié réservée pour la fin) ; viande, gingembre-ail, épices et fenouil moulus, 5 min.", "**Nuit.** Eau à 3 cm au-dessus, couvercle, feu le plus doux (ou four 120 °C), 6 à 8 h : la viande se détache de l'os.",
   "**Lier.** Farine délayée dans 20 cl d'eau froide, versée en remuant, 20 min : sauce veloutée et brillante, une couche de ghee rouge en surface.", "**Servir.** Oignons frits, gingembre en julienne, piment vert, citron, coriandre ; naan."],
  tips=["**Autocuiseur** : 1 h 15, puis liaison à découvert.", FROID], keep=KEEP, age=6, profil=["epice"], fetes=["Aïd"])

K("birria_res", "Birria de bœuf et son consommé (Jalisco)", "Birria de res", "Amérique latine › Mexique › Jalisco", "P", 2, 8, 40, 240, "€€", "Grande cocotte, mixeur.",
  "Bœuf mariné dans une sauce de piments séchés, vinaigre et épices, mijoté jusqu'à s'effilocher. On le mange en tacos trempés dans le bouillon rouge (« quesabirria ») ou en bol de consommé avec oignon, coriandre et citron vert.",
  ["1,5 kg|de paleron et jarret de bœuf|Paleron|3", "5|piments séchés (guajillo, ancho)|Piments ancho / chipotle / guajillo / pasilla|3", f"3|tomates|{TOM}|1", f"4 c. à s.|de vinaigre de cidre|{CIDRE}|1", f"1 c. à c.|de cumin|{CUMIN}|1", f"1 c. à c.|d'origan|Origan frais / sec|1", f"1|bâton de cannelle|{CANN}|1", f"1|oignon|{OIG}|1", "16|tortillas de maïs|Tortillas de maïs|2", f"2|citrons verts|{CITV}|1"],
  ["**Sauce.** Piments épépinés grillés 30 s, trempés 20 min ; mixés avec tomates, ail, vinaigre, épices : rouge sombre.", "**Mariner.** Viande en gros morceaux enrobée de sauce, 4 h ou une nuit.",
   "**Mijoter.** Viande, sauce, oignon, laurier, eau à hauteur ; couvert 3 h 30 à feu doux : effilochable. Gras rouge de surface réservé.", "**Tacos.** Tortillas trempées dans le gras rouge, dorées à la poêle avec la viande (et du fromage) ; bol de consommé à côté pour tremper ; oignon, coriandre, citron vert."],
  tips=["**Autocuiseur** : 1 h 10.", FROID], keep=KEEP, age=6, fetes=["Repas de famille"], profil=["epice"])

K("pollo_pibil", "Pollo pibil (la cochinita pibil, version poulet)", "Pollo pibil", "Amérique latine › Mexique › Yucatán", "P", 1, 6, 25, 150, "€€", "Plat à four avec couvercle, aluminium.",
  "Au Yucatán, la cochinita pibil (porc) et le pollo pibil sont deux classiques : la viande est marinée au rocou et au jus d'orange amère, enveloppée de feuilles de bananier et cuite lentement. Servie effilochée avec des oignons rouges marinés et des tortillas.",
  [f"8|hauts de cuisse de poulet|{CUISSE}|3", "2 c. à s.|de pâte de rocou (achiote)|Achiote / rocou|3", "2|oranges|Orange|2", f"2|citrons verts|{CITV}|2", f"4 gousses|d'ail|{AIL}|1", f"1 c. à c.|de cumin|{CUMIN}|1", f"1 c. à c.|d'origan|Origan frais / sec|1", "4|feuilles de bananier (ou papier sulfurisé)|Feuille de bananier|2", "2|oignons rouges|Oignon rouge|1", "12|tortillas de maïs|Tortillas de maïs|1"],
  ["**Marinade.** Rocou délayé dans le jus des oranges et d'un citron vert, ail, cumin, origan, sel ; poulet enrobé, 4 h à une nuit.", "**Envelopper.** Feuilles de bananier passées à la flamme (souples) dans le plat, poulet et marinade, feuilles repliées, couvercle.",
   "**Cuire lentement.** Four 160 °C, 2 h 30 : la chair se détache ; effilochée dans son jus.", "**Oignons marinés.** Oignons rouges émincés, jus de citron vert, sel, 30 min : roses. Tacos, oignons, piment."],
  tips=[FROID], keep=KEEP, age=3, cats=["enfants"], fetes=["Repas de famille"])

K("langue_boeuf_piquante", "Langue de bœuf sauce piquante", "Langue de bœuf sauce piquante", "France › Bourgogne-Franche-Comté", "P", 2, 6, 30, 180, "€€", "Faitout, casserole.",
  "Le plat de bistrot et de grand-mère : langue pochée longuement comme un pot-au-feu, pelée, tranchée et nappée d'une sauce brune au vinaigre, cornichons et câpres. Tendre, fondante et franchement relevée.",
  ["1|langue de bœuf (1,2 kg)|Langue de bœuf|3", f"2|carottes|{CAROTTE}|1", f"1|oignon piqué de clous de girofle|{OIG}|1", f"1|bouquet garni|{THYM}|1", f"3|échalotes|{ECH}|1", f"5 cl|de vinaigre de vin|Vinaigre de vin rouge / blanc|2", f"2 c. à s.|de concentré de tomate|{CONC}|1", f"30 g|de farine|{F55}|1", "8|cornichons|Cornichon|2", "1 c. à s.|de câpres|Câpres|1"],
  ["**Dégorger et pocher.** Langue 2 h dans l'eau froide ; blanchie 10 min, rincée ; puis eau froide, carottes, oignon, bouquet, gros sel ; frémissement 3 h.", "**Peler.** Tiède, la peau blanche s'enlève en un seul geste (une incision dessous) ; parures retirées ; tranches de 1 cm gardées dans un peu de bouillon.",
   "**Sauce.** Échalotes et vinaigre réduits à sec ; roux blond (30 g de beurre + farine), concentré, 50 cl de bouillon de cuisson, 15 min ; cornichons en rondelles, câpres, persil.", "**Servir.** Tranches nappées, pommes de terre vapeur."],
  tips=["**Autocuiseur** : 1 h 10 pour pocher la langue.", "Les restes froids, en fines tranches avec une sauce gribiche, sont un classique.", FROID],
  keep=KEEP, age=3, zw=["bouillon de cuisson → soupe"])

K("oxtail_jamaicain", "Queue de bœuf mijotée à la jamaïcaine (oxtail)", "Jamaican oxtail stew", "Amérique latine › Jamaïque", "P", 2, 6, 30, 210, "€€", "Cocotte en fonte.",
  "La queue de bœuf brunie, mijotée des heures avec thym, cébette, piment antillais et piment de la Jamaïque, puis des haricots blancs moelleux à la fin : une sauce collante et brillante, le plat du dimanche de Kingston, avec riz et pois.",
  ["1,8 kg|de queue de bœuf en tronçons|Queue de bœuf|3", "400 g|de gros haricots blancs cuits (butter beans)|Haricots blancs / lingots|2", f"1|oignon|{OIG}|1", "4|cébettes|Oignon nouveau / cébette|1", f"6 brins|de thym|{THYM}|1", "1|piment antillais entier (non percé)|Piment antillais / scotch bonnet|1", "1 c. à c.|de piment de la Jamaïque (ou quatre-épices)|Quatre-épices|1", "1 c. à s.|de cassonade|Sucre blanc / roux / cassonade / vergeoise|1", f"2 c. à s.|de sauce soja|{SOJA}|1", f"1 c. à s.|de concentré de tomate|{CONC}|1"],
  ["**Mariner.** Tronçons frottés de soja, ail, thym, épices, une nuit.", "**Brunir.** Cassonade dans un peu d'huile jusqu'à brun foncé ; viande saisie dedans en 2 fois : laquée.",
   "**Mijoter.** Oignon, cébette, thym, concentré, piment entier, eau à hauteur ; couvert 3 h : la viande se détache de l'os. Piment retiré (s'il éclate, le plat devient brûlant).", "**Finir.** Haricots 15 min ; sauce réduite, collante. Riz et pois, bananes plantains."],
  tips=["**Autocuiseur** : 1 h, puis réduction à découvert.", FROID], keep=KEEP, age=6, profil=["epice"], fetes=["Repas de famille"])

K("galbi_jjim", "Galbi-jjim (côtes de bœuf braisées coréennes)", "Galbi-jjim", "Asie de l'Est › Corée", "P", 2, 6, 40, 150, "€€€", "Cocotte.",
  "Le plat des fêtes coréennes (Chuseok, Nouvel An) : plat de côtes de bœuf braisé dans une sauce soja sucrée à la poire, avec radis, carottes, châtaignes et champignons qui s'imprègnent. Laqué et tendre.",
  ["1,5 kg|de plat de côtes de bœuf (ou paleron)|Paleron|3", f"8 c. à s.|de sauce soja|{SOJA}|2", "1|poire mûre râpée|Poire|2", "300 g|de radis daikon|Radis noir / daikon|2", f"2|carottes|{CAROTTE}|1", "12|châtaignes cuites|Châtaigne (fraîche, crème, purée)|1?", "8|shiitake|Shiitake|1", f"6 gousses|d'ail|{AIL}|1", f"2 c. à s.|de sucre|{SUCRE}|1", "1 c. à s.|d'huile de sésame|Huile de sésame (grillée)|1"],
  ["**Dégorger et blanchir.** Côtes 1 h dans l'eau froide, puis 10 min dans l'eau bouillante ; rincées (sauce claire, sans écume).", "**Sauce.** Soja, poire râpée, ail, sucre, sésame, gingembre, 50 cl d'eau.",
   "**Braiser.** Côtes et sauce, couvert, 1 h 30 à feu doux ; légumes en gros morceaux aux angles arrondis (ils ne se défont pas), châtaignes, champignons, 40 min.", "**Laquer.** À découvert, 10 min en arrosant : brillant. Sésame, cébette ; riz."],
  tips=["**Autocuiseur** : 35 min pour la viande, légumes 5 min de plus.", FROID], keep=KEEP, age=3, cats=["enfants"], fetes=["Nouvel An chinois", "Repas de famille"])

K("niu_rou_mian", "Niu rou mian (soupe de nouilles au bœuf braisé de Taïwan)", "Hóngshāo niúròu miàn", "Asie de l'Est › Taïwan", "So", 2, 6, 30, 150, "€€", "Faitout.",
  "Jarret de bœuf « braisé rouge » à la sauce soja, pâte de fèves pimentée, anis étoilé et tomate, servi dans son bouillon sur des nouilles épaisses avec pak-choï et pickles de moutarde : la soupe nationale de Taïwan.",
  ["1 kg|de jarret de bœuf|Jarret de bœuf|3", "500 g|de nouilles de blé épaisses|Nouilles chinoises aux œufs|3", f"6 c. à s.|de sauce soja|{SOJA}|2", "2 c. à s.|de pâte de fèves pimentée (doubanjiang)|Pâte de haricots jaunes/noirs|2", "3|anis étoilés|Anis étoilé (badiane)|1", f"2|tomates|{TOM}|1", "1 morceau|de gingembre|Gingembre frais|1", "4|cébettes|Oignon nouveau / cébette|1", "4|pak-choï|Chou chinois / pak-choï|1", f"1 c. à s.|de sucre|{SUCRE}|1"],
  ["**Blanchir.** Jarret en gros cubes, 5 min dans l'eau bouillante, rincé.", "**Braiser rouge.** Gingembre, cébette, doubanjiang 1 min dans l'huile ; viande, soja, sucre, anis, tomates, 2 l d'eau ; 2 h à petit frémissement.",
   "**Servir.** Nouilles et pak-choï cuits à part dans les bols, viande et bouillon brûlant ; cébette, piment, pickles."],
  tips=["**Autocuiseur** : 45 min.", FROID], keep=KEEP, age=6, profil=["epice"])

K("sancocho", "Sancocho de poulet (Colombie)", "Sancocho de gallina", "Amérique latine › Colombie", "So", 1, 8, 30, 90, "€€", "Très grand faitout.",
  "La grande soupe-plat du dimanche en Colombie et dans les Caraïbes : poulet, plantain vert, manioc, pommes de terre et épis de maïs cuits ensemble jusqu'à ce que le manioc lie le bouillon ; coriandre, riz et avocat à côté.",
  [f"1|poulet en morceaux (ou 6 cuisses)|{CUISSE}|3", "2|plantains verts|Plantain (banane à cuire)|2", "500 g|de manioc (frais ou surgelé)|Manioc / yuca|2", f"4|pommes de terre|{PDT}|2", "3|épis de maïs en tronçons|Maïs doux|2", f"1|oignon|{OIG}|1", f"3 gousses|d'ail|{AIL}|1", f"1 c. à c.|de cumin|{CUMIN}|1", f"1 bouquet|de coriandre|{CORI}|2", f"2|citrons verts|{CITV}|1"],
  ["**Bouillon.** Poulet, oignon, ail, cumin, tiges de coriandre, 3 l d'eau salée, 40 min en écumant.", "**Légumes durs.** Plantain en tronçons (coupé à la main : il lie mieux), manioc, maïs, 25 min.",
   "**Finir.** Pommes de terre 20 min : le manioc s'effrite et épaissit. Coriandre hachée. Riz blanc, avocat, citron vert à table."],
  tips=["Manioc frais : retirer la fibre centrale. Le surgelé, déjà pelé, est plus simple.", FROID], keep=KEEP, age=1, cats=["enfants"], fetes=["Repas de famille"])

# ——— Mijotés végétariens (part des plats sans chair ≥ 33 %) ———
K("kuru_fasulye", "Kuru fasulye (haricots blancs mijotés à la turque)", "Kuru fasulye", "Moyen-Orient › Turquie", "P", 1, 6, 15, 120, "€", "Cocotte.",
  "Haricots blancs mijotés doucement dans une sauce tomate au poivron et au piment doux, servis avec du riz pilaf et des pickles : le plat national de tous les jours en Turquie, ici dans sa version végétarienne courante.",
  ["500 g|de haricots blancs secs|Haricots blancs / lingots|3", f"2|oignons|{OIG}|2", f"1|poivron|{POIVRON}|1", f"3 c. à s.|de concentré de tomate|{CONC}|2", "1 c. à s.|de pâte de piment doux (ou paprika)|Piment doux (poudre de poivron)|1", "1 c. à c.|de flocons de piment|Flocons de piment|1?", f"6 c. à s.|d'huile d'olive|{HO}|2", f"30 g|de beurre|{BEURRE}|1"],
  ["**La veille.** Haricots trempés 12 h ; précuits 30 min dans l'eau, égouttés.", "**Base.** Oignons et poivron 10 min dans l'huile et le beurre ; concentré et piment 2 min : rouge sombre.",
   "**Mijoter.** Haricots, eau chaude à 2 cm au-dessus, 1 h 30 à couvert à feu doux : fondants, sauce épaisse. Sel à la fin. Riz pilaf, pickles, oignon cru."],
  tips=["**Autocuiseur** : 25 min (haricots trempés).", FROID], keep=KEEP, age=1, cats=["vegetarien", "enfants"])

K("gigantes_plaki", "Gigantes plaki (haricots géants au four, Grèce)", "Gigantes plaki", "Europe du Sud › Grèce", "P", 1, 6, 20, 150, "€", "Plat à four.",
  "Très gros haricots blancs cuits au four dans une sauce tomate à l'huile d'olive, aneth et persil, jusqu'à ce que le dessus caramélise : un des grands plats végétariens grecs, servi tiède avec de la feta et du pain.",
  ["500 g|de gros haricots blancs secs (gigantes, ou lingots)|Haricots blancs / lingots|3", f"800 g|de tomates concassées|{PELEES}|2", f"2|oignons|{OIG}|1", f"2|carottes|{CAROTTE}|1", f"3 gousses|d'ail|{AIL}|1", "1 bouquet|d'aneth|Aneth|1", f"1 bouquet|de persil|{PERSIL}|1", f"10 cl|d'huile d'olive|{HO}|2", "150 g|de feta|Feta|1?"],
  ["**Haricots.** Trempés une nuit, cuits 45 min à l'eau : tendres mais entiers.", "**Sauce.** Oignons, carottes râpées, ail dans la moitié de l'huile, 10 min ; tomates, 15 min ; herbes, sel, sucre si acide.",
   "**Four.** Haricots et sauce dans le plat, 15 cl de leur eau, reste d'huile ; 180 °C, 1 h 15 : dessus caramélisé, sauce confite. Tiède, feta."],
  tips=["**Autocuiseur** pour les haricots : 20 min.", FROID], keep=KEEP, age=1, cats=["vegetarien", "enfants"])

K("bourguignon_champignons", "Bourguignon de champignons", "Bourguignon de champignons", "France › Bourgogne-Franche-Comté", "P", 1, 4, 25, 60, "€€", "Cocotte.",
  "La sauce du bœuf bourguignon (vin rouge, carottes, petits oignons, thym) sur des champignons saisis en gros morceaux : la version végétale du grand plat bourguignon, prête en une heure et demie. Purée ou pâtes fraîches.",
  ["800 g|de champignons variés en gros morceaux|Champignon de Paris|3", "50 cl|de vin rouge de Bourgogne|Vin rouge|3", f"3|carottes|{CAROTTE}|2", f"12|petits oignons (ou 2 oignons)|{OIG}|1", f"2 gousses|d'ail|{AIL}|1", f"2 c. à s.|de concentré de tomate|{CONC}|1", f"2 c. à s.|de farine|{F55}|1", f"1 c. à s.|de sauce soja|{SOJA}|1", f"1|bouquet thym-laurier|{THYM}|1", f"30 g|de beurre|{BEURRE}|1"],
  ["**Saisir.** Champignons en 2 fois dans une cocotte très chaude, sans remuer 3 min : bien dorés ; réservés.", "**Base.** Carottes et oignons au beurre 8 min ; ail, concentré, farine 1 min ; vin, soja, 25 cl d'eau, bouquet.",
   "**Mijoter.** 40 min à couvert ; champignons remis 15 min : sauce nappante et brillante, d'un brun violacé."],
  tips=[FROID], keep=KEEP, age=3, cats=["vegetarien"], var=[VR])

K("garbanzos_espinacas", "Pois chiches aux épinards (Séville)", "Espinacas con garbanzos", "Europe du Sud › Espagne › Andalousie", "P", 1, 4, 15, 30, "€", "Sauteuse, mortier ou mixeur.",
  "Un plat de tapas sévillan d'origine mauresque : pois chiches et épinards liés par une pâte de pain frit, ail, cumin, paprika fumé et vinaigre de xérès. Simple, profond, végétalien.",
  [f"500 g|de pois chiches cuits|{POIS}|3", "400 g|d'épinards|Épinard|3", "2 tranches|de pain rassis|Pain rassis (réservé)|2", f"4 gousses|d'ail|{AIL}|1", f"1 c. à c.|de cumin|{CUMIN}|1", f"1 c. à c.|de paprika fumé|{PFUME}|1", f"2 c. à s.|de vinaigre de xérès|Vinaigre de xérès|1", f"6 c. à s.|d'huile d'olive|{HO}|2"],
  ["**Picada.** Pain et ail dorés dans l'huile ; pilés avec cumin, paprika, vinaigre et un peu d'eau : pâte épaisse.", "**Épinards.** Fondus 3 min dans la même poêle.",
   "**Mijoter.** Pois chiches, picada, 20 cl d'eau ou de bouillon, 15 min : sauce liée. Pain grillé."], age=1, cats=["vegetarien"], zw=["pain d'hier"])

K("fasolakia_ladera", "Fasolakia (haricots verts mijotés à l'huile d'olive)", "Fasolakia lathera", "Europe du Sud › Grèce", "P", 1, 4, 15, 50, "€", "Cocotte.",
  "Un « ladera », plat mijoté à l'huile d'olive : haricots verts, pommes de terre et tomate cuits lentement jusqu'à être fondants, servis tièdes avec de la feta et du pain. L'été grec, sans viande.",
  ["800 g|de haricots verts plats ou fins|Haricots verts|3", f"3|pommes de terre|{PDT}|2", f"400 g|de tomates concassées|{PELEES}|2", f"2|oignons|{OIG}|1", f"2 gousses|d'ail|{AIL}|1", f"1 bouquet|de persil ou aneth|{PERSIL}|1", f"10 cl|d'huile d'olive|{HO}|3", "100 g|de feta|Feta|1?"],
  ["**Base.** Oignons et ail fondus 10 min dans la moitié de l'huile.", "**Mijoter.** Haricots, pommes de terre en quartiers, tomates, 15 cl d'eau, sel ; couvert, 45 min à feu doux : très tendres, sauce réduite.",
   "**Finir.** Reste d'huile crue, herbes. Tiède, feta, pain."], age=1, cats=["vegetarien", "enfants"])

K("briam", "Briam (légumes confits au four, Grèce)", "Briam", "Europe du Sud › Grèce", "P", 1, 6, 25, 90, "€", "Grand plat à four.",
  "Courgettes, aubergines, pommes de terre, poivrons et tomates rôtis lentement à l'huile d'olive et à l'origan jusqu'à confire : le cousin grec de la ratatouille, encore meilleur le lendemain.",
  ["3|courgettes|Courgette|3", "2|aubergines|Aubergine|2", f"4|pommes de terre|{PDT}|2", f"2|poivrons|{POIVRON}|1", f"4|tomates|{TOM}|2", f"2|oignons rouges|Oignon rouge|1", f"1 c. à s.|d'origan|Origan frais / sec|1", f"12 cl|d'huile d'olive|{HO}|2", "150 g|de feta|Feta|1?"],
  ["**Couper.** Légumes en morceaux de taille égale ; tomates râpées.", "**Assaisonner.** Tout mélangé avec l'huile, l'origan, l'ail, sel, poivre ; 10 cl d'eau.",
   "**Confire.** 190 °C, 1 h 30, remué 2 fois, couvert la première heure : légumes fondants, bords caramélisés. Feta, pain."], age=1, cats=["vegetarien", "enfants"])

K("baked_beans_maison", "Baked beans maison (haricots au four, Boston)", "Boston baked beans", "Amérique du Nord › États-Unis › Boston", "P", 1, 6, 15, 240, "€", "Cocotte en fonte qui va au four.",
  "Les vrais haricots à la tomate, cuits des heures au four avec mélasse, moutarde et oignon : rien à voir avec la boîte. L'original contient du lard ; ici en version végétarienne fumée au paprika. Sur du pain grillé ou avec des œufs.",
  ["500 g|de petits haricots blancs secs (lingots ou cocos)|Haricots blancs / lingots|3", "4 c. à s.|de mélasse (ou miel)|Mélasse / sirop de canne|2", f"3 c. à s.|de concentré de tomate|{CONC}|2", f"1 c. à s.|de moutarde|{DIJON}|1", f"1|oignon|{OIG}|1", f"1 c. à c.|de paprika fumé|{PFUME}|1", "2 c. à s.|de cassonade|Sucre blanc / roux / cassonade / vergeoise|1", f"2 c. à s.|de vinaigre de cidre|{CIDRE}|1"],
  ["**Haricots.** Trempés une nuit, précuits 40 min : la peau se fend quand on souffle dessus.", "**Monter.** Oignon coupé en deux au fond, haricots, tous les autres ingrédients délayés dans 50 cl de leur eau.",
   "**Four lent.** Couvert, 150 °C, 3 h ; découvert la dernière heure ; rajoute de l'eau si ça sèche : sauce épaisse et brillante."],
  tips=["**Autocuiseur** pour précuire : 15 min.", FROID], keep=KEEP, age=1, cats=["vegetarien", "enfants", "brunch"])

K("mafe_vegetarien", "Mafé végétarien (patate douce et pois chiches)", "Mafé", "Afrique subsaharienne › Sénégal", "P", 1, 6, 20, 50, "€", "Cocotte.",
  "La sauce d'arachide du mafé, onctueuse et relevée, avec patate douce, chou, carottes et pois chiches à la place de la viande : un plat complet et bon marché, avec du riz blanc.",
  ["150 g|de pâte d'arachide (sans sucre)|Pâte d'arachide|3", "2|patates douces|Patate douce|3", f"300 g|de pois chiches cuits|{POIS}|2", "¼|chou vert|Chou vert / frisé / kale|1", f"2|carottes|{CAROTTE}|1", f"2 c. à s.|de concentré de tomate|{CONC}|1", f"1|oignon|{OIG}|1", f"1|piment|{PIMENT}|1?", "1|cube de bouillon de légumes|Bouillon cube légumes|1"],
  ["**Base.** Oignon 8 min, concentré 2 min ; pâte d'arachide délayée dans 1 l d'eau chaude avec le cube, versée en remuant.", "**Mijoter.** Carottes, chou, piment entier, 20 min ; patates douces en gros cubes et pois chiches, 25 min en remuant de temps en temps (ça accroche).",
   "**Finir.** Une huile rouge remonte en surface : c'est prêt. Riz blanc."], tips=[FROID], keep=KEEP, age=3, cats=["vegetarien", "enfants"])
