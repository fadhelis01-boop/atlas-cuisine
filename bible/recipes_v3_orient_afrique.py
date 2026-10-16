# -*- coding: utf-8 -*-
"""Vague 4 · Audit du chef (16/10/2026) : Maghreb, Moyen-Orient, Afrique, Océanie, plus un bloc de plats végétariens du monde
(l'ajout des grands classiques carnés faisait baisser la part végétarienne sous le seuil validé de 33 %). NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

MA = "Maghreb › Maroc"; DZ = "Maghreb › Algérie"; TN = "Maghreb › Tunisie"; EG = "Afrique du Nord › Égypte"
LB = "Moyen-Orient › Liban"; PS = "Moyen-Orient › Palestine"; JO = "Moyen-Orient › Jordanie"; TR = "Moyen-Orient › Turquie"; IR = "Moyen-Orient › Iran"
IN = "Asie du Sud › Inde"

# ——— Maghreb ———
K("couscous_royal", "Couscous royal (poulet, agneau, merguez)", "Couscous", f"{DZ} › Oran", "P", 2, 8, 50, 90, "€€€", "Couscoussier (ou faitout + passoire), grand plat.",
  "Le couscous des grandes tablées : bouillon aux sept légumes, pois chiches, poulet et agneau mijotés, merguez grillées à part, graine roulée et cuite à la vapeur trois fois.",
  ["1 kg|de semoule moyenne|Semoule de couscous|3", "800 g|d'épaule d'agneau en morceaux|Épaule d'agneau|3", f"4|cuisses de poulet|{CUISSE}|2", "8|merguez|Merguez (agneau/bœuf)|2", f"4|carottes|{CAROTTE}|2", "3|courgettes|Courgette|2", "2|navets|Navet / navet boule d'or|2", f"250 g|de pois chiches cuits|{POIS}|2", "2 c. à c.|de ras el-hanout|Ras el-hanout|2", f"80 g|de beurre|{BEURRE}|1"],
  ["**Bouillon.** Viandes dorées avec 2 oignons et les épices (1 c. à s. de concentré de tomate si tu aimes) ; 3 l d'eau, 45 min ; carottes et navets 20 min, courgettes et pois chiches 15 min.",
   "**Graine.** Semoule mouillée d'un verre d'eau salée, roulée entre les mains, 15 min ; 1ʳᵉ vapeur au-dessus du bouillon (20 min dès que la vapeur traverse) ; aérée, remouillée ; 2ᵉ vapeur ; beurrée.",
   "**Merguez et service.** Merguez grillées 8 min. Graine en dôme, viandes et légumes, bouillon en saucière, harissa diluée de bouillon."],
  tips=["Sans couscoussier : semoule « moyenne » 1 pour 1 d'eau bouillante salée + beurre, 5 min couverte, égrenée (version express)."], age=1, cats=["enfants"], fetes=["Repas de famille", "Aïd"])

K("tajine_agneau_pruneaux", "Tajine d'agneau aux pruneaux et amandes", "Tajine lham bel barkouk", f"{MA} › Fès", "P", 1, 6, 25, 120, "€€€", "Tajine ou cocotte en fonte.",
  "Agneau fondant au safran, gingembre et cannelle, pruneaux caramélisés au miel, amandes grillées et sésame : le tajine sucré-salé des fêtes marocaines.",
  ["1,2 kg|d'épaule d'agneau en morceaux|Épaule d'agneau|3", "250 g|de pruneaux|Pruneaux|3", "60 g|d'amandes|Amande (entière, effilée, poudre)|2", f"2|oignons|{OIG}|2", "1 pincée|de safran|Safran (pistils)|1", "1 c. à c.|de gingembre en poudre|Gingembre (poudre)|1", f"1|bâton de cannelle|{CANN}|1", f"2 c. à s.|de miel|{MIEL}|1", "1 c. à s.|de sésame grillé|Sésame (blanc/noir)|1"],
  ["**Mijoter.** Agneau, oignons râpés, épices, sel, 3 c. à s. d'huile, 50 cl d'eau ; couvert, 1 h 45 à feu doux : la viande se détache.", "**Pruneaux.** Pochés 10 min dans une louche de sauce avec le miel et la cannelle : brillants.",
   "**Servir.** Sauce réduite si besoin ; pruneaux dessus, amandes dorées, sésame. Pain ou semoule."], age=1, fetes=["Aïd", "Repas de famille"], profil=["sucre"])

K("pastilla_poulet", "Pastilla au poulet et amandes", "Bastila", f"{MA} › Fès", "P", 3, 8, 75, 75, "€€", "Moule à manqué 28 cm, pinceau.",
  "Feuilles de brick croustillantes, poulet effiloché au safran et aux oignons, œufs brouillés dans la sauce, amandes sucrées à la fleur d'oranger, cannelle et sucre glace : le chef-d'œuvre sucré-salé de Fès.",
  [f"6|cuisses de poulet|{CUISSE}|3", "10|feuilles de brick|Pâte de brick / ouarka|3", f"3|oignons|{OIG}|2", f"4|œufs|{OEUF}|2", "150 g|d'amandes|Amande (entière, effilée, poudre)|2", "1 pincée|de safran|Safran (pistils)|1", f"2 c. à c.|de cannelle|{CANN}|2", "2 c. à s.|de sucre glace|Sucre glace|1", "1 c. à s.|d'eau de fleur d'oranger|Eau de fleur d'oranger|1", f"80 g|de beurre fondu|{BEURRE}|2"],
  ["**Poulet.** Cuit 1 h avec oignons râpés, safran, gingembre, cannelle, persil, 40 cl d'eau ; effiloché ; sauce réduite, œufs battus ajoutés en remuant : brouillés crémeux.",
   "**Amandes.** Grillées, concassées avec 2 c. à s. de sucre glace, cannelle, fleur d'oranger.",
   "**Monter et cuire.** Briks beurrées en rosace débordant du moule ; amandes, poulet, œufs, briks ; rabats repliés, 2 briks dessus, beurre ; 180 °C, 30 min : doré. Sucre glace et cannelle en croisillons."],
  age=1, fetes=["Aïd", "Repas de famille"], profil=["sucre"])

K("rechta_poulet", "Rechta algéroise (nouilles fines, poulet, navets)", "Rechta", f"{DZ} › Alger", "P", 2, 6, 30, 60, "€€", "Faitout, couscoussier ou passoire.",
  "Nouilles plates très fines cuites à la vapeur, nappées d'une sauce blanche à la cannelle avec poulet, navets et pois chiches : le plat de l'Aïd à Alger.",
  ["500 g|de nouilles fines (rechta, ou linguine cassées)|Pâtes sèches (spaghetti, penne…)|3", f"6|cuisses de poulet|{CUISSE}|3", "4|navets|Navet / navet boule d'or|2", f"200 g|de pois chiches cuits|{POIS}|1", f"2|oignons|{OIG}|1", f"1 c. à c.|de cannelle|{CANN}|2", f"½ c. à c.|de poivre blanc|{POIVRE}|1", f"50 g|de beurre|{BEURRE}|1"],
  ["**Sauce blanche.** Poulet, oignon, cannelle, poivre, sel, beurre, 2 l d'eau, 40 min ; navets en quartiers et pois chiches 15 min.", "**Nouilles.** À la vapeur au-dessus de la sauce, 2 fois 10 min, huilées entre les deux (ou cuites à la casserole 2 min de moins que le paquet).",
   "**Servir.** Nouilles beurrées, arrosées de sauce, poulet, navets ; cannelle."], age=1, cats=["enfants"], fetes=["Aïd"])

K("ojja_merguez", "Ojja aux merguez (Tunisie)", "Ojja merguez", f"{TN} › Tunis", "P", 1, 4, 15, 20, "€", "Sauteuse.",
  "Sauce tomate-poivrons à la harissa et au carvi, merguez en rondelles et œufs pochés dedans : le plat express des cafés tunisiens, à saucer au pain.",
  ["6|merguez|Merguez (agneau/bœuf)|3", f"4|œufs|{OEUF}|3", f"2|poivrons|{POIVRON}|2", f"400 g|de tomates concassées|{PELEES}|2", "1 c. à s.|de harissa|Harissa (tube/pâte)|2", f"3 gousses|d'ail|{AIL}|1", "1 c. à c.|de carvi|Carvi / fenouil / anis vert (graines)|1"],
  ["**Merguez.** En rondelles, dorées 4 min ; gras retiré en partie.", "**Sauce.** Poivrons en lanières 5 min, ail, harissa, carvi, tomates, 10 min.", "**Œufs.** Cassés dans des creux, couvert 5 min : blancs pris, jaunes coulants. Pain."],
  age=6, profil=["epice"])

K("taktouka", "Taktouka (salade cuite poivrons-tomates)", "Taktouka", MA, "E", 1, 6, 15, 30, "€", "Four (gril), sauteuse.",
  "Poivrons grillés et tomates mijotés à l'huile d'olive, ail, paprika et cumin jusqu'à la confiture : une des salades cuites qui ouvrent le repas marocain.",
  [f"4|poivrons verts et rouges|{POIVRON}|3", f"4|tomates|{TOM}|3", f"3 gousses|d'ail|{AIL}|1", f"1 c. à c.|de paprika|{PAPRIKA}|1", f"1 c. à c.|de cumin|{CUMIN}|1", f"4 c. à s.|d'huile d'olive|{HO}|2", f"1 c. à s.|de persil|{PERSIL}|1"],
  ["**Griller.** Poivrons sous le gril 15 min en tournant : peau noircie ; en sac 10 min, pelés, en lanières.", "**Mijoter.** Tomates pelées concassées, ail, épices, huile, 10 min ; poivrons, 15 min : compoté, plus d'eau.", "**Servir.** Froid ou tiède, persil, pain."],
  age=1, cats=["vegetarien"], keep="4 jours au frigo.")

K("bissara", "Bissara (soupe de fèves sèches)", "Bissara", f"{MA} › Nord", "So", 1, 6, 10, 60, "€", "Faitout, mixeur.",
  "Purée-soupe de fèves sèches à l'ail, arrosée d'huile d'olive, cumin et paprika : le petit-déjeuner d'hiver des ouvriers de Fès et Tanger, pour presque rien.",
  ["400 g|de fèves sèches pelées|Fèves sèches|3", f"4 gousses|d'ail|{AIL}|1", f"1 c. à c.|de cumin|{CUMIN}|2", f"1 c. à c.|de paprika|{PAPRIKA}|1", f"6 c. à s.|d'huile d'olive|{HO}|2", f"1|citron|{CIT}|1?"],
  ["**Cuire.** Fèves trempées une nuit, ail, 1,5 l d'eau, 50 min : défaites.", "**Mixer.** Lisse, sel ; ajuste l'épaisseur (soupe ou purée).", "**Servir.** Filet d'huile d'olive généreux, cumin, paprika ; pain et olives."],
  age=1, cats=["vegetarien"], keep="4 jours au frigo (épaissit : rallonge d'eau).")

K("harcha", "Harcha (galettes de semoule au beurre)", "Harcha", MA, "Pa", 1, 10, 15, 20, "€", "Poêle épaisse.",
  "Petites galettes de semoule fine au beurre et au lait, cuites à la poêle : sablées dedans, dorées dehors. Avec miel et beurre ou fromage frais au thé.",
  ["300 g|de semoule fine|Semoule de blé (fine/moyenne)|3", f"80 g|de beurre fondu|{BEURRE}|2", f"15 cl|de lait|{LAIT}|2", f"1 c. à s.|de sucre|{SUCRE}|1", f"1 c. à c.|de levure chimique|{LEVC}|1", f"1 pincée|de sel|{SEL}|1"],
  ["**Sabler.** Semoule, sucre, sel, levure, beurre frottés entre les mains : sable humide.", "**Lier.** Lait petit à petit : pâte qui se tient sans coller ; 10 min de repos.",
   "**Cuire.** Galettes de 1 cm roulées dans la semoule, poêle sans matière grasse à feu doux, 6-8 min par face : dorées. Miel et beurre."],
  age=1, cats=["enfants", "vegetarien", "brunch"])

K("mechouia", "Salade méchouia (Tunisie)", "Slata mechouia", TN, "E", 1, 6, 15, 25, "€", "Gril du four ou barbecue.",
  "Poivrons, piments, tomates et oignon grillés jusqu'à noircir, pelés et hachés au couteau avec ail, carvi, huile d'olive ; thon et œuf dur dessus.",
  [f"4|poivrons|{POIVRON}|3", f"4|tomates|{TOM}|2", f"1|oignon|{OIG}|1", f"2 gousses|d'ail|{AIL}|1", "1 c. à c.|de carvi|Carvi / fenouil / anis vert (graines)|1", f"4 c. à s.|d'huile d'olive|{HO}|2", "140 g|de thon (facultatif)|Thon en conserve|1?", f"2|œufs durs|{OEUF}|1?", f"1|citron|{CIT}|1"],
  ["**Griller.** Légumes entiers sous le gril ou sur la braise, 20 min : peau noire.", "**Peler et hacher.** Pelés, épépinés, hachés au couteau avec ail, carvi, sel.", "**Servir.** Huile d'olive, citron ; thon, œuf, olives."],
  age=3, cats=["vegetarien"], fetes=["Ramadan", "Barbecue d'été"])

K("tameya", "Tameya (falafels égyptiens aux fèves)", "Ta'ameya", f"{EG} › Le Caire", "E", 2, 6, 25, 15, "€", "Mixeur, casserole profonde.",
  "Les falafels du Caire, à la fève et non au pois chiche, mixés avec beaucoup d'herbes : verts à l'intérieur, croustillants dehors. Dans le pain baladi avec tahini.",
  ["300 g|de fèves sèches pelées (crues, trempées)|Fèves sèches|3", f"1 bouquet|de persil|{PERSIL}|2", f"1 bouquet|de coriandre|{CORI}|2", f"1|oignon|{OIG}|1", f"4 gousses|d'ail|{AIL}|1", f"1 c. à c.|de cumin|{CUMIN}|1", "½ c. à c.|de bicarbonate|Bicarbonate de soude|1", "2 c. à s.|de sésame|Sésame (blanc/noir)|1", "1 l|d'huile de friture|Huile d'arachide|1"],
  ["**Mixer.** Fèves trempées 24 h (crues, jamais cuites : sinon elles se défont), herbes, oignon, ail, cumin, sel : pâte fine et verte ; bicarbonate juste avant de frire.",
   "**Former.** Petits palets humides, sésame d'un côté.", "**Frire.** 175 °C, 3-4 min : bruns dehors, verts dedans. Sauce tahini, pain, tomates."],
  age=3, cats=["vegetarien"], tech=["frire en sécurité"])

# ——— Moyen-Orient ———
K("mansaf_simple", "Mansaf simplifié (agneau au yaourt, Jordanie)", "Mansaf", JO, "P", 2, 6, 30, 120, "€€€", "Cocotte, grand plat.",
  "Le plat national jordanien : agneau mijoté dans une sauce de yaourt fermenté (jameed), sur riz au curcuma et pain fin, amandes et pignons grillés. Ici avec du yaourt grec stabilisé.",
  ["1,2 kg|d'épaule d'agneau en morceaux|Épaule d'agneau|3", "500 g|de yaourt grec|Yaourt grec|3", f"1 c. à s.|de fécule|Fécule de maïs (maïzena)|1", f"400 g|de riz long|{RIZ}|2", f"½ c. à c.|de curcuma|{CURC}|1", "50 g|d'amandes et pignons|Pignons de pin|1", "1|pain fin (marqouq ou lavash)|Lavash / pain azyme|1", "2|gousses de cardamome|Cardamome|1"],
  ["**Agneau.** Blanchi 5 min, rincé ; mijoté 1 h 30 avec oignon, cardamome, laurier, 1,5 l d'eau.", "**Sauce yaourt.** Yaourt + fécule fouettés, délayés de bouillon chaud, chauffés en remuant toujours dans le même sens (il ne tranche pas) ; agneau dedans, 20 min.",
   "**Monter.** Pain au fond du plat, riz au curcuma, agneau, sauce, amandes et pignons dorés."], age=1, fetes=["Aïd", "Repas de famille"])

K("maqluba_legumes", "Maqluba aux aubergines et chou-fleur (végétarienne)", "Maqluba", PS, "P", 2, 6, 40, 50, "€€", "Grande cocotte à fond épais, grand plat.",
  "« À l'envers » : couches d'aubergines et de chou-fleur dorés, de tomates et de riz épicé cuits ensemble, puis démoulés d'un coup de cocotte sur le plat. Spectaculaire, ici sans viande.",
  ["2|aubergines|Aubergine|3", "1|chou-fleur|Chou-fleur|3", f"400 g|de riz long|{RIZ}|3", f"2|tomates|{TOM}|1", "2 c. à c.|de baharat (ou cumin + cannelle + poivre)|Baharat / tabil|2", f"½ c. à c.|de curcuma|{CURC}|1", "80 cl|de bouillon de légumes|Bouillon cube légumes|2", "50 g|de pignons ou amandes|Pignons de pin|1", f"15 cl|de yaourt (pour servir)|{YAO}|1?"],
  ["**Dorer.** Aubergines en tranches et chou-fleur en bouquets, au four 220 °C huilés, 25 min : dorés.", "**Étager.** Tomates en rondelles au fond, aubergines, chou-fleur, riz rincé mélangé aux épices ; bouillon à 1 cm au-dessus.",
   "**Cuire et retourner.** Couvert 30 min à feu doux, 10 min de repos ; plat posé dessus, retourné d'un geste ; on tapote, on soulève. Pignons, yaourt."],
  age=1, cats=["vegetarien"], fetes=["Repas de famille"])

K("musakhan", "Musakhan (poulet au sumac et oignons sur pain)", "Musakhan", PS, "P", 1, 4, 25, 50, "€€", "Plat à four.",
  "Poulet rôti au sumac, posé sur un pain plat imbibé d'huile d'olive et couvert d'oignons fondus au sumac, pignons grillés : le plat palestinien de la récolte des olives.",
  [f"4|cuisses de poulet|{CUISSE}|3", f"4|oignons|{OIG}|3", "3 c. à s.|de sumac|Sumac|3", f"8 c. à s.|d'huile d'olive|{HO}|2", "4|pains plats (taboun, pita, lavash)|Pain pita / libanais|2", "40 g|de pignons|Pignons de pin|1", f"1 c. à c.|de cumin|{CUMIN}|1"],
  ["**Poulet.** Frotté de sumac, cumin, sel, huile ; 200 °C, 40 min.", "**Oignons.** Émincés, 20 min à feu doux dans l'huile : fondants ; sumac.",
   "**Monter.** Pains badigeonnés du jus, oignons, poulet ; 5 min au four : bords croustillants. Pignons dorés."], age=1, fetes=["Repas de famille"])

K("fatayer_epinards", "Fatayer aux épinards (chaussons libanais)", "Fatayer bi sabanekh", LB, "E", 2, 20, 50, 70, "€", "Rouleau, emporte-pièce, four.",
  "Petits chaussons triangulaires farcis d'épinards au sumac, oignon et citron : les incontournables du mezzé, qui se congèlent très bien.",
  [f"400 g|de farine|{F55}|3", f"7 g|de levure sèche|{LEV}|1", f"6 c. à s.|d'huile d'olive|{HO}|2", "600 g|d'épinards|Épinard|3", f"1|oignon|{OIG}|1", "2 c. à s.|de sumac|Sumac|2", f"1|citron|{CIT}|2", "40 g|de pignons|Pignons de pin|1?"],
  ["**Pâte.** Farine, levure, sel, 3 c. à s. d'huile, 22 cl d'eau tiède ; 1 h : doublée.", "**Farce.** Épinards crus hachés, salés, pressés fort (sinon les chaussons s'ouvrent) ; oignon, sumac, citron, huile, pignons.",
   "**Former et cuire.** Disques de 9 cm, une cuillerée, trois bords relevés et pincés en triangle ; 200 °C, 15 min : dorés."],
  age=1, cats=["vegetarien"], fetes=["Apéritif dînatoire", "Ramadan"], keep="3 jours au frigo ; 3 mois au congélateur.")

K("muhammara", "Muhammara (poivrons grillés, noix, mélasse de grenade)", "Muhammara", "Moyen-Orient › Syrie › Alep", "S", 1, 6, 15, 20, "€", "Mixeur.",
  "Tartinade d'Alep : poivrons grillés, noix, chapelure, mélasse de grenade et piment : douce, fumée, acidulée. Avec du pain ou des légumes.",
  [f"3|poivrons rouges|{POIVRON}|3", "100 g|de noix|Noix|3", "40 g|de chapelure|Chapelure|1", "2 c. à s.|de mélasse de grenade|Mélasse de grenade|2", f"1 c. à c.|de cumin|{CUMIN}|1", "1 c. à c.|de flocons de piment|Flocons de piment|1", f"4 c. à s.|d'huile d'olive|{HO}|2", f"½|citron|{CIT}|1"],
  ["**Poivrons.** Grillés 20 min, pelés, épépinés.", "**Mixer.** Avec noix grillées, chapelure, mélasse, cumin, piment, citron, sel : texture un peu granuleuse.", "**Servir.** Filet d'huile, quelques noix."],
  age=3, cats=["vegetarien"], fetes=["Apéritif dînatoire"])

K("dolma_riz", "Dolmas (feuilles de vigne farcies au riz)", "Yalancı dolma", TR, "E", 2, 30, 60, 60, "€", "Cocotte large.",
  "Feuilles de vigne roulées serré autour d'un riz aux oignons, herbes, raisins secs et pignons, cuites à l'huile d'olive et au citron : servies froides.",
  ["40|feuilles de vigne en bocal|Feuilles de vigne (bocal)|3", f"200 g|de riz rond|Riz rond / sushi|3", f"3|oignons|{OIG}|2", "30 g|de pignons|Pignons de pin|1", "30 g|de raisins secs|Raisins secs|1", "1 bouquet|de menthe et d'aneth|Menthe|2", f"10 cl|d'huile d'olive|{HO}|2", f"2|citrons|{CIT}|2", f"½ c. à c.|de cannelle|{CANN}|1?"],
  ["**Farce.** Oignons fondus 10 min dans l'huile, pignons, riz rincé 3 min, raisins, épices, 15 cl d'eau, 8 min : riz à moitié cuit ; herbes.", "**Rouler.** Feuilles rincées, nervures en haut ; 1 c. à c. de farce, côtés repliés, roulé serré.",
   "**Cuire.** Serrés en cocotte, citron en rondelles, eau à hauteur, assiette dessus ; 45 min à petit feu. Refroidis dans la cocotte."],
  age=3, cats=["vegetarien"], fetes=["Apéritif dînatoire", "Ramadan"], keep="5 jours au frigo.")

K("borek_fromage", "Börek au fromage et persil (rouleaux)", "Sigara böreği", TR, "E", 1, 20, 30, 15, "€", "Poêle ou four.",
  "Feuilles de pâte roulées comme des cigarettes autour de feta et persil, dorées : l'en-cas turc qu'on fait avec les enfants.",
  ["10|feuilles de brick ou de yufka|Pâte filo / feuilles de brick|3", "250 g|de feta|Feta|3", f"1 bouquet|de persil|{PERSIL}|2", f"1|œuf|{OEUF}|1", f"4 c. à s.|d'huile|{HN}|1"],
  ["**Farce.** Feta émiettée, persil haché, œuf.", "**Rouler.** Feuilles coupées en deux ; une ligne de farce, côtés repliés, roulé serré ; bord collé à l'eau.", "**Cuire.** Poêle 1 cm d'huile, 2 min en tournant ; ou four 200 °C, badigeonnés, 15 min."],
  age=1, cats=["vegetarien", "enfants"], fetes=["Apéritif dînatoire", "Ramadan"])

K("kofte_turques", "Köfte turques (boulettes grillées)", "Izgara köfte", TR, "P", 1, 4, 20, 10, "€€", "Poêle-gril ou barbecue.",
  "Petites galettes de bœuf et d'agneau au cumin, oignon râpé et persil, grillées : avec salade d'oignon au sumac, piments grillés et yaourt.",
  ["400 g|de bœuf haché|Bœuf haché|3", "200 g|d'agneau haché|Agneau haché|2", f"1|oignon râpé|{OIG}|1", "40 g|de chapelure|Chapelure|1", f"1 c. à c.|de cumin|{CUMIN}|1", f"1 bouquet|de persil|{PERSIL}|1", "1|oignon rouge|Oignon rouge|1", "1 c. à s.|de sumac|Sumac|1"],
  ["**Pétrir.** Viandes, oignon râpé pressé, chapelure, cumin, persil, sel ; pétris 3 min ; 30 min au frais.", "**Former.** Petits palets ovales de 1,5 cm.", "**Griller.** 3-4 min par face. Oignon rouge émincé au sumac et persil, yaourt, pain."],
  age=1, cats=["enfants"], fetes=["Barbecue d'été"])

K("adana_kebab", "Adana kebab (brochettes d'agneau pimentées)", "Adana kebabı", f"{TR} › Adana", "P", 2, 4, 30, 10, "€€", "Brochettes plates en métal, barbecue.",
  "Agneau haché au piment doux et au poivron, moulé à la main sur des brochettes plates et grillé sur la braise : servi sur pain lavash avec oignon au sumac et tomates grillées.",
  ["700 g|d'agneau haché assez gras|Agneau haché|3", f"1|poivron rouge|{POIVRON}|1", "2 c. à c.|de flocons de piment (pul biber)|Flocons de piment|2", f"1 c. à c.|de paprika|{PAPRIKA}|1", "4|pains lavash|Lavash / pain azyme|2", "1|oignon rouge|Oignon rouge|1", "1 c. à s.|de sumac|Sumac|1", f"4|tomates|{TOM}|1"],
  ["**Pétrir.** Agneau, poivron haché très fin et pressé, épices, sel ; pétris 5 min : collant ; 1 h au frais.", "**Mouler.** Mains mouillées, boudin long et plat pressé autour de la brochette, marques de doigts.",
   "**Griller.** Braise vive, 8 min en tournant ; posés sur le lavash pour qu'il prenne le jus. Oignon au sumac, tomates grillées."], age=6, fetes=["Barbecue d'été"], profil=["epice"])

K("simit", "Simit (anneaux au sésame d'Istanbul)", "Simit", f"{TR} › Istanbul", "Pa", 2, 8, 40, 90, "€", "Plaque, four.",
  "Anneaux de pâte torsadée trempés dans un sirop de mélasse puis roulés dans le sésame : croustillants et dorés, vendus à chaque coin de rue d'Istanbul.",
  [f"500 g|de farine|{F55}|3", f"7 g|de levure sèche|{LEV}|1", f"1 c. à c.|de sucre|{SUCRE}|1", "4 c. à s.|de mélasse (ou miel)|Mélasse / sirop de canne|2", "150 g|de sésame|Sésame (blanc/noir)|3", f"2 c. à s.|d'huile|{HN}|1"],
  ["**Pâte.** Farine, levure, sucre, sel, huile, 30 cl d'eau tiède ; pétrie 8 min ; 1 h.", "**Former.** 8 boudins de 60 cm pliés en deux et torsadés, fermés en anneau.",
   "**Tremper et cuire.** Dans mélasse + 15 cl d'eau, puis sésame grillé ; 20 min de repos ; 220 °C, 15-18 min : brun doré."], age=1, cats=["vegetarien", "brunch", "enfants"])

K("fesenjan", "Fesenjan (poulet aux noix et à la grenade)", "Khoresh fesenjan", f"{IR} › Gilan", "P", 2, 6, 20, 90, "€€", "Cocotte, mixeur.",
  "Ragoût persan de poulet dans une sauce épaisse de noix moulues et de mélasse de grenade, longuement mijotée jusqu'à brunir : aigre-doux, profond.",
  [f"6|cuisses de poulet|{CUISSE}|3", "250 g|de noix|Noix|3", "8 c. à s.|de mélasse de grenade|Mélasse de grenade|3", f"1|oignon|{OIG}|1", f"1 c. à s.|de sucre|{SUCRE}|1?", f"½ c. à c.|de cannelle|{CANN}|1", "1|grenade (graines, pour servir)|Grenade|1?"],
  ["**Noix.** Grillées à sec 5 min, moulues fin ; avec 70 cl d'eau, 30 min à feu doux en remuant : l'huile perle.", "**Poulet.** Doré avec l'oignon ; dans la sauce avec la mélasse, la cannelle, 50 min.",
   "**Équilibrer.** Trop acide : sucre ; trop doux : mélasse. Sauce brun foncé, nappante. Riz au safran, grains de grenade."], age=3, fetes=["Norouz"])

K("koobideh", "Kebab koobideh (brochettes persanes)", "Kabab koobideh", IR, "P", 2, 4, 25, 10, "€€", "Brochettes plates, barbecue.",
  "Bœuf et agneau hachés avec beaucoup d'oignon râpé et pressé, moulés sur des brochettes plates et grillés : avec riz au safran, tomates grillées et sumac.",
  ["400 g|de bœuf haché|Bœuf haché|3", "300 g|d'agneau haché|Agneau haché|2", f"2|oignons|{OIG}|2", "1 c. à c.|de sumac|Sumac|1", "1 pincée|de safran|Safran (pistils)|1?", f"350 g|de riz basmati|{RIZ}|2", f"4|tomates|{TOM}|1", f"30 g|de beurre|{BEURRE}|1"],
  ["**Pétrir.** Oignons râpés et pressés (le jus fait tomber la viande), viandes, sel, poivre ; pétris 5 min ; 1 h au frais.", "**Mouler.** Mains mouillées, boudin plat autour de la brochette, marques de doigts tous les 2 cm.",
   "**Griller.** Braise vive, 6-8 min en tournant sans cesse au début (sinon ça glisse). Riz au beurre et safran, tomates grillées, sumac."], age=1, fetes=["Barbecue d'été", "Norouz"])

K("mast_o_khiar", "Mast-o-khiar (yaourt concombre, menthe, raisins)", "Mast-o-khiar", IR, "S", 1, 6, 10, 30, "€", "Bol, râpe.",
  "Le yaourt persan au concombre, menthe séchée, noix, raisins secs et pétales de rose : plus riche que le tzatziki, à manger avec du pain ou les kebabs.",
  [f"500 g|de yaourt grec|{GREC}|3", "1|concombre|Concombre|3", "1 c. à s.|de menthe séchée|Menthe|2", "30 g|de noix|Noix|1", "30 g|de raisins secs|Raisins secs|1", f"1 pincée|de sel|{SEL}|1", "1 c. à c.|de pétales de rose séchés|Eau de rose|1?"],
  ["**Concombre.** En petits dés (ou râpé, pressé).", "**Mélanger.** Yaourt, concombre, menthe frottée entre les mains, noix concassées, raisins trempés, sel.", "**Servir.** Frais, 30 min ; pétales de rose."],
  age=1, cats=["vegetarien"], keep="2 jours au frigo.")

K("plov", "Plov ouzbek (riz à l'agneau et carottes)", "Osh / plov", "Asie du Sud › Ouzbékistan", "P", 2, 6, 30, 75, "€€", "Cocotte en fonte (kazan).",
  "Agneau saisi, montagne de carottes en bâtonnets, cumin, tête d'ail entière, puis le riz cuit par-dessus sans remuer : le plat des fêtes d'Asie centrale.",
  ["800 g|d'épaule d'agneau en cubes|Épaule d'agneau|3", f"500 g|de riz long|{RIZ}|3", f"6|carottes (bâtonnets)|{CAROTTE}|3", f"2|oignons|{OIG}|1", "1|tête d'ail entière|Ail|1", f"2 c. à c.|de cumin en graines|{CUMIN}|2", "1 c. à c.|de coriandre en graines|Coriandre (graines)|1", "50 g|de raisins secs ou pois chiches|Raisins secs|1?", f"10 cl|d'huile|{HN}|2"],
  ["**Zirvak.** Agneau saisi très chaud, oignons, carottes (sans remuer 3 min, puis 10 min), épices, 60 cl d'eau, tête d'ail ; 40 min.", "**Riz.** Rincé jusqu'à eau claire, étalé dessus sans mélanger ; eau à 1 cm ; feu vif jusqu'à absorption.",
   "**Étuver.** Quelques trous au manche de cuillère, couvert, 20 min à feu doux ; mélangé seulement au service."], age=1, fetes=["Repas de famille", "Aïd"])

# ——— Afrique ———
K("egusi_soup", "Soupe egusi (Nigeria) au bœuf et épinards", "Egusi soup", "Afrique subsaharienne › Nigeria", "P", 2, 6, 30, 60, "€€", "Cocotte, mixeur.",
  "Ragoût épais de graines de courge moulues, bœuf, épinards, piment et huile de palme : le plat du Sud nigérian, qu'on mange avec fufu, igname ou riz.",
  ["600 g|de bœuf à mijoter|Paleron|3", "200 g|de graines de courge décortiquées moulues|Graines de tournesol / courge|3", "400 g|d'épinards|Épinard|2", f"1|oignon|{OIG}|1", f"2|tomates|{TOM}|1", "1|piment scotch bonnet (ou piment oiseau)|Piment scotch bonnet|1?", "4 c. à s.|d'huile de palme rouge (ou huile + paprika)|Huile de palme rouge|1", "1|cube de bouillon|Bouillon cube bœuf|1", "100 g|de poisson fumé (facultatif)|Poisson fumé / séché|1?"],
  ["**Bœuf.** Mijoté 45 min avec oignon, cube, sel, 1 l d'eau.", "**Egusi.** Graines moulues délayées d'un peu d'eau en pâte ; huile chauffée, tomates et piment mixés 10 min ; pâte d'egusi en petits tas, 10 min sans remuer : grumeaux.",
   "**Finir.** Bœuf et bouillon, poisson fumé, 10 min ; épinards 5 min. Avec riz, igname ou fufu."], age=6, profil=["epice"])

K("bunny_chow_haricots", "Bunny chow aux haricots (Durban)", "Bunny chow", "Afrique subsaharienne › Afrique du Sud › Durban", "P", 1, 4, 20, 30, "€", "Cocotte, couteau à pain.",
  "Un quart de pain de mie évidé rempli de curry : le street-food de la communauté indienne de Durban. La version « beans bunny » est végétarienne et très bon marché.",
  ["1|pain de mie non tranché (ou 4 petits pains)|Pain de mie|3", "500 g|de haricots (rouges ou blancs) cuits|Haricots rouges / noirs|3", f"2|pommes de terre|{PDT}|2", f"1|oignon|{OIG}|1", f"2|tomates|{TOM}|1", "2 c. à s.|de curry|Curry (mélange)|2", "1 c. à s.|de gingembre|Gingembre frais|1", f"1 bouquet|de coriandre|{CORI}|1"],
  ["**Curry.** Oignon 8 min, gingembre, ail, curry 1 min ; tomates, pommes de terre en dés, haricots, 30 cl d'eau, 25 min : épais.", "**Pain.** Coupé en quarts, mie retirée (gardée comme « couvercle »).", "**Servir.** Curry dans le pain, couvercle de mie posé ; carottes râpées au piment à côté. On mange avec les doigts."],
  age=3, cats=["vegetarien"], profil=["epice"])

K("malva_pudding", "Malva pudding (Afrique du Sud)", "Malva pudding", "Afrique subsaharienne › Afrique du Sud", "D", 1, 8, 20, 45, "€", "Plat à four.",
  "Gâteau spongieux à la confiture d'abricot, arrosé à la sortie du four d'une sauce chaude beurre-crème-sucre qu'il boit entièrement : collant, caramélisé.",
  [f"150 g|de farine|{F55}|2", f"150 g|de sucre|{SUCRE}|2", f"1|œuf|{OEUF}|1", "2 c. à s.|de confiture d'abricot|Confiture / gelée|2", "1 c. à c.|de bicarbonate|Bicarbonate de soude|1", f"25 cl|de lait|{LAIT}|1", f"1 c. à s.|de vinaigre|{CIDRE}|1", f"80 g|de beurre|{BEURRE}|2", f"20 cl|de crème|{CL}|2"],
  ["**Pâte.** Œuf et 100 g de sucre fouettés, confiture, beurre fondu (30 g), vinaigre ; farine et bicarbonate en alternance avec le lait.", "**Cuire.** 180 °C, 40 min : brun foncé.",
   "**Sauce.** 50 g de beurre, crème, 50 g de sucre, 5 cl d'eau, chauffés ; versée sur le gâteau brûlant, piqué : il boit tout. Chaud, avec crème anglaise."],
  age=1, cats=["enfants"], fetes=["Noël"], profil=["sucre"])

K("red_red", "Red red (haricots à la tomate et plantains, Ghana)", "Red red", "Afrique subsaharienne › Ghana", "P", 1, 4, 15, 25, "€", "Cocotte, poêle.",
  "Haricots cornille mijotés dans une sauce tomate-oignon-gingembre à l'huile de palme rouge, avec des plantains frits : le plat populaire et végétarien du Ghana, rouge sur rouge.",
  ["500 g|de haricots (cornille ou blancs) cuits|Haricots blancs / lingots|3", "2|plantains mûrs|Plantain (banane à cuire)|3", f"1|oignon|{OIG}|1", f"400 g|de tomates concassées|{PELEES}|2", "1 c. à s.|de gingembre|Gingembre frais|1", "3 c. à s.|d'huile de palme rouge (ou huile + paprika)|Huile de palme rouge|1", f"1|piment|{PIMENT}|1?"],
  ["**Sauce.** Huile, oignon 6 min, gingembre, piment, tomates, 10 min.", "**Haricots.** Dans la sauce, 10 min ; sel.", "**Plantains.** En biais, poêlés 3 min par face : caramélisés. Ensemble, avec garri ou riz."],
  age=3, cats=["vegetarien"])

K("misir_wat", "Misir wat (lentilles corail au berbéré, Éthiopie)", "Misir wot", "Afrique subsaharienne › Éthiopie", "P", 1, 4, 15, 30, "€", "Cocotte.",
  "Lentilles corail fondues dans beaucoup d'oignon cuit à sec puis à l'huile, ail, gingembre et berbéré : le plat végétal des jours de jeûne éthiopiens, avec injera ou riz.",
  ["250 g|de lentilles corail|Lentilles corail|3", f"3|oignons|{OIG}|3", "2 c. à s.|de berbéré|Berbéré|3", f"3 gousses|d'ail|{AIL}|1", "1 c. à s.|de gingembre|Gingembre frais|1", f"2 c. à s.|de concentré de tomate|{CONC}|1", f"4 c. à s.|d'huile|{HN}|2"],
  ["**Oignons.** Hachés très fin, 10 min à sec en remuant (ils fondent), puis l'huile, 5 min.", "**Épices.** Berbéré, ail, gingembre, concentré, 2 min : rouge sombre.", "**Lentilles.** Rincées, 75 cl d'eau, 20 min en remuant : épais. Sel. Injera ou riz."],
  age=6, cats=["vegetarien"], profil=["epice"])

K("githeri", "Githeri (maïs et haricots mijotés, Kenya)", "Githeri", "Afrique subsaharienne › Kenya", "P", 1, 4, 15, 25, "€", "Cocotte.",
  "Maïs et haricots mijotés avec oignon, tomate, carotte et un peu de curry : le plat simple et complet des cantines kényanes.",
  ["400 g|de maïs (surgelé ou conserve)|Maïs doux|3", "400 g|de haricots rouges cuits|Haricots rouges / noirs|3", f"1|oignon|{OIG}|1", f"2|tomates|{TOM}|1", f"1|carotte|{CAROTTE}|1", f"2|pommes de terre|{PDT}|1?", "1 c. à c.|de curry|Curry (mélange)|1", f"1 bouquet|de coriandre|{CORI}|1"],
  ["**Base.** Oignon 6 min, curry, tomates 5 min.", "**Mijoter.** Carotte et pommes de terre en dés, 25 cl d'eau, 15 min ; maïs et haricots, 10 min.", "**Finir.** Sel, coriandre ; avec des épinards sautés (sukuma wiki)."],
  age=1, cats=["vegetarien", "enfants"])

# ——— Plats végétariens du monde (rééquilibrage) ———
K("kuku_sabzi", "Kuku sabzi (omelette persane aux herbes)", "Kuku sabzi", IR, "P", 1, 4, 25, 30, "€", "Poêle avec couvercle ou plat à four.",
  "Une omelette épaisse, presque toute en herbes (persil, coriandre, aneth, ciboulette), avec noix et épine-vinette : verte à la coupe, servie tiède ou froide. Le plat de Norouz.",
  [f"6|œufs|{OEUF}|3", f"2 bouquets|de persil|{PERSIL}|3", f"1 bouquet|de coriandre|{CORI}|2", "1 bouquet|d'aneth|Aneth|2", "1 bouquet|de ciboulette|Ciboulette|1", "40 g|de noix|Noix|1", "30 g|de raisins secs ou cranberries|Raisins secs|1?", f"½ c. à c.|de curcuma|{CURC}|1", f"4 c. à s.|d'huile|{HN}|1"],
  ["**Herbes.** Lavées, séchées (important), hachées fin.", "**Appareil.** Œufs, curcuma, sel, levure (½ c. à c.), herbes, noix, raisins : plus vert que jaune.",
   "**Cuire.** Poêle huilée, couvert, 20 min à feu doux ; retourné à l'aide d'une assiette, 5 min (ou four 180 °C, 25 min). Yaourt, pain."],
  age=1, cats=["vegetarien", "brunch"], fetes=["Norouz"])

K("mercimek_kofte", "Mercimek köftesi (boulettes lentilles-boulgour)", "Mercimek köftesi", TR, "P", 1, 6, 30, 30, "€", "Casserole, saladier.",
  "Lentilles corail cuites avec du boulgour fin qui gonfle hors du feu, oignon, concentré, cumin, herbes : modelées à la main, mangées froides dans une feuille de salade. Sans cuisson finale.",
  ["200 g|de lentilles corail|Lentilles corail|3", "150 g|de boulgour fin|Boulgour fin|3", f"1|oignon|{OIG}|1", f"2 c. à s.|de concentré de tomate|{CONC}|1", f"1 c. à c.|de cumin|{CUMIN}|1", "1 c. à c.|de flocons de piment|Flocons de piment|1", "3|cébettes|Oignon nouveau / cébette|1", f"1 bouquet|de persil|{PERSIL}|1", f"1|citron|{CIT}|1"],
  ["**Lentilles.** 50 cl d'eau, 15 min : fondues ; hors du feu, boulgour, couvert 20 min : il boit tout.", "**Oignon.** Fondu dans l'huile, concentré, épices ; mélangé à la pâte avec cébette, persil, citron, sel ; pétri.",
   "**Former.** Pressés dans la paume (marque des doigts). Feuilles de salade, citron, grenade."], age=1, cats=["vegetarien"], fetes=["Apéritif dînatoire"])

K("gemista", "Gemista (légumes farcis au riz, Grèce)", "Gemista", "Europe du Sud › Grèce", "P", 1, 6, 30, 70, "€", "Grand plat à four.",
  "Tomates et poivrons évidés, remplis de riz cru à leur propre pulpe, herbes et huile d'olive, cuits au four entre des quartiers de pommes de terre : l'été grec, sans viande.",
  [f"6|grosses tomates|{TOM}|3", f"4|poivrons|{POIVRON}|2", f"200 g|de riz rond|Riz rond / sushi|3", f"1|oignon|{OIG}|1", "1 bouquet|de menthe et persil|Menthe|2", f"10 cl|d'huile d'olive|{HO}|2", f"4|pommes de terre|{PDT}|1", "50 g|de feta (facultatif)|Feta|1?"],
  ["**Évider.** Chapeaux coupés, pulpe récupérée et mixée.", "**Farce.** Oignon fondu, riz cru, pulpe, herbes, sel, la moitié de l'huile ; remplis aux ¾ (le riz gonfle).",
   "**Cuire.** Chapeaux remis, pommes de terre en quartiers entre, reste d'huile, 15 cl d'eau ; 180 °C, 1 h 10, couvert la première demi-heure : riz tendre, légumes fripés."],
  age=1, cats=["vegetarien", "enfants"])

K("baingan_bharta", "Baingan bharta (caviar d'aubergine fumé à l'indienne)", "Baingan bharta", f"{IN} › Pendjab", "P", 1, 4, 20, 25, "€", "Feu de gaz ou gril, sauteuse.",
  "Aubergines noircies à la flamme (goût fumé), écrasées et sautées avec oignon, tomate, gingembre, piment et épices : avec chapati ou riz.",
  ["2|grosses aubergines|Aubergine|3", f"1|oignon|{OIG}|1", f"2|tomates|{TOM}|2", "1 c. à s.|de gingembre|Gingembre frais|1", f"1 c. à c.|de cumin|{CUMIN}|1", "1 c. à c.|de garam masala|Garam masala|1", f"1|piment vert|{PIMENT}|1?", f"1 bouquet|de coriandre|{CORI}|1"],
  ["**Fumer.** Aubergines piquées, directement sur la flamme du gaz ou sous le gril, 15-20 min en tournant : peau noire, chair effondrée ; pelées, écrasées.", "**Masala.** Cumin, oignon 8 min, gingembre, piment, tomates 6 min.",
   "**Mélanger.** Aubergine, garam masala, sel, 5 min ; coriandre."], age=3, cats=["vegetarien"], profil=["epice"])

K("matar_paneer", "Matar paneer (petits pois et paneer en sauce)", "Matar paneer", f"{IN} › Pendjab", "P", 1, 4, 20, 25, "€€", "Sauteuse, mixeur.",
  "Cubes de fromage paneer et petits pois dans une sauce tomate-oignon aux épices douces : le plat végétarien du quotidien en Inde du Nord, que les enfants aiment.",
  ["250 g|de paneer (ou halloumi)|Paneer|3", "250 g|de petits pois|Petits pois / pois gourmands|3", f"2|oignons|{OIG}|1", f"400 g|de tomates concassées|{PELEES}|2", "1 c. à s.|de gingembre-ail|Gingembre frais|1", "2 c. à c.|de garam masala|Garam masala|2", f"½ c. à c.|de curcuma|{CURC}|1", f"5 cl|de crème|{CF}|1?"],
  ["**Paneer.** En cubes, dorés 3 min ; dans de l'eau tiède (il reste tendre).", "**Sauce.** Oignons 10 min, gingembre-ail, épices, tomates 10 min ; mixée si tu la veux lisse.", "**Mijoter.** Petits pois 8 min, paneer 3 min, crème. Riz ou naan."],
  age=1, cats=["vegetarien", "enfants"])

K("kadhi_pakora", "Kadhi pakora (sauce yaourt-besan et beignets d'oignon)", "Kadhi pakora", f"{IN} › Pendjab", "P", 2, 4, 30, 30, "€", "Casserole, poêle profonde.",
  "Une sauce jaune acidulée de yaourt épaissi à la farine de pois chiche, avec de petits beignets d'oignon qui s'y imbibent : le plat de famille du Pendjab, avec du riz.",
  [f"40 cl|de yaourt nature|{YAO}|3", "100 g|de farine de pois chiche (besan)|Farine de pois chiche (besan)|3", f"2|oignons|{OIG}|2", f"½ c. à c.|de curcuma|{CURC}|1", f"1 c. à c.|de cumin|{CUMIN}|1", "½ c. à c.|de graines de moutarde|Graines de moutarde|1?", "½ c. à c.|de fenugrec|Fenugrec|1?", "50 cl|d'huile de friture|Huile d'arachide|1"],
  ["**Kadhi.** Yaourt, 40 g de besan, curcuma, 70 cl d'eau fouettés ; chauffé en remuant jusqu'à frémir, puis 20 min à feu doux : nappant.", "**Pakoras.** 60 g de besan, oignon émincé, sel, piment, un peu d'eau : pâte épaisse ; cuillerées frites 175 °C, 3 min.",
   "**Tempérer.** Ghee, cumin, moutarde, fenugrec 20 s, versé sur le kadhi ; pakoras dedans 5 min avant de servir. Riz."], age=3, cats=["vegetarien"], tech=["frire en sécurité"])

K("kitchari", "Kitchari (riz et lentilles au ghee)", "Khichdi", IN, "P", 1, 4, 10, 25, "€", "Cocotte.",
  "Riz et lentilles cuits ensemble jusqu'à devenir crémeux, au curcuma et au ghee : le plat doux et digeste qu'on donne en Inde aux enfants et aux convalescents.",
  [f"150 g|de riz basmati|{RIZ}|3", "150 g|de lentilles corail (ou moong dal)|Lentilles corail (masoor)|3", f"½ c. à c.|de curcuma|{CURC}|1", f"1 c. à c.|de cumin en graines|{CUMIN}|1", "1 c. à s.|de gingembre|Gingembre frais|1", "2 c. à s.|de ghee|Ghee|2", "150 g|de légumes (carotte, petits pois)|Petits pois / pois gourmands|1?"],
  ["**Rincer.** Riz et lentilles ensemble, à l'eau claire.", "**Cuire.** Ghee, cumin 30 s, gingembre ; riz-lentilles, curcuma, légumes, sel, 1,2 l d'eau ; 25 min en remuant de temps en temps : crémeux comme un porridge.", "**Servir.** Un peu de ghee, yaourt, pickles."],
  age=1, cats=["vegetarien", "enfants"])

K("lobio", "Lobio (haricots rouges aux noix et coriandre, Géorgie)", "Lobio", "Europe du Nord › Géorgie", "P", 1, 4, 15, 25, "€", "Cocotte.",
  "Haricots rouges en partie écrasés avec oignon, noix, ail, coriandre, fenugrec et un trait de vinaigre : le plat géorgien de tous les jours, servi en pot de terre avec pain et pickles.",
  ["600 g|de haricots rouges cuits|Haricots rouges / noirs|3", "60 g|de noix|Noix|2", f"2|oignons|{OIG}|1", f"3 gousses|d'ail|{AIL}|1", f"1 bouquet|de coriandre|{CORI}|2", "½ c. à c.|de fenugrec|Fenugrec|1?", f"1 c. à s.|de vinaigre de vin|Vinaigre de vin rouge / blanc|1", "1 c. à c.|de flocons de piment|Flocons de piment|1?"],
  ["**Oignons.** Fondus 10 min dans l'huile.", "**Mijoter.** Haricots + 20 cl de leur eau, 10 min ; la moitié écrasée.", "**Finir.** Noix pilées avec ail, sel, fenugrec ; coriandre, vinaigre, piment. Tiède, pain, cornichons."],
  age=1, cats=["vegetarien"])

K("gozleme_epinards_feta", "Gözleme épinards-feta", "Gözleme", TR, "P", 2, 4, 35, 30, "€", "Grande poêle, rouleau.",
  "Galettes de pâte très fine farcies d'épinards et feta, pliées et cuites à sec puis beurrées : le plat des marchés turcs, croustillant et fondant.",
  [f"300 g|de farine|{F55}|3", f"15 cl|de yaourt|{YAO}|1", "300 g|d'épinards|Épinard|3", "200 g|de feta|Feta|3", f"1|oignon|{OIG}|1", f"30 g|de beurre fondu|{BEURRE}|1", "1 c. à c.|de flocons de piment|Flocons de piment|1?"],
  ["**Pâte.** Farine, yaourt, sel, 10 cl d'eau : souple ; 30 min.", "**Farce.** Épinards crus hachés, salés, pressés ; oignon, feta, piment.",
   "**Cuire.** 4 boules abaissées très fines ; farce sur la moitié, pliée, bords pressés ; poêle à sec, 3 min par face, beurrée : taches dorées. Citron."],
  age=1, cats=["vegetarien", "enfants"])

K("yasai_kare", "Curry japonais aux légumes (yasai karē)", "Yasai karē raisu", "Asie de l'Est › Japon", "P", 1, 4, 20, 30, "€", "Cocotte.",
  "Le plat préféré des enfants japonais : sauce brune épaisse et douce au curry, roux maison, pommes de terre, carottes, oignons et une pomme râpée, sur du riz.",
  [f"2|oignons|{OIG}|2", f"2|carottes|{CAROTTE}|2", f"3|pommes de terre|{PDT}|2", "1|pomme râpée|Pomme|1", f"40 g|de beurre|{BEURRE}|2", f"40 g|de farine|{F55}|2", "2 c. à s.|de curry doux|Curry (mélange)|2", f"1 c. à s.|de sauce soja|{SOJA}|1", "1 c. à s.|de ketchup|Ketchup|1", f"320 g|de riz rond|Riz rond / sushi|2"],
  ["**Légumes.** Oignons 10 min (dorés), carottes et pommes de terre en gros morceaux, pomme râpée, 70 cl d'eau, 20 min.", "**Roux.** Beurre + farine 3 min (blond), curry 1 min ; délayé avec une louche de bouillon.",
   "**Lier.** Roux dans la cocotte, soja, ketchup, 5 min : sauce épaisse et brillante. Sur le riz."], age=1, cats=["vegetarien", "enfants"], tech=["faire un roux"])

K("dubu_jorim", "Dubu jorim (tofu braisé coréen)", "Dubu-jorim", "Asie de l'Est › Corée", "P", 1, 4, 10, 15, "€", "Poêle.",
  "Tranches de tofu dorées puis braisées dans une sauce soja, gochugaru, ail et cébette jusqu'à ce qu'elles soient laquées : un banchan devenu plat, avec du riz.",
  ["400 g|de tofu ferme|Tofu (ferme / soyeux)|3", f"4 c. à s.|de sauce soja|{SOJA}|2", "1 c. à s.|de gochugaru (ou paprika + piment)|Gochugaru|2", f"1 c. à c.|de sucre|{SUCRE}|1", f"2 gousses|d'ail|{AIL}|1", "2|cébettes|Oignon nouveau / cébette|1", "1 c. à s.|d'huile de sésame|Huile de sésame (grillée)|1", "1 c. à c.|de sésame|Sésame (blanc/noir)|1"],
  ["**Dorer.** Tofu épongé, tranches de 1 cm, poêlé 3 min par face : doré.", "**Sauce.** Soja, gochugaru, sucre, ail, cébette, sésame, 10 cl d'eau.", "**Braiser.** Versée sur le tofu, 6 min en arrosant : réduite, laquée. Riz."],
  age=3, cats=["vegetarien"], profil=["epice"])

K("berkoukes_legumes", "Berkoukes aux légumes (plombs, Algérie)", "Berkoukes", DZ, "P", 1, 6, 25, 40, "€", "Cocotte.",
  "Grosses perles de semoule (ou couscous perlé) cuites dans une sauce rouge aux légumes, pois chiches et herbes : le plat d'hiver des familles algériennes, ici sans viande.",
  ["400 g|de berkoukes ou couscous perlé|Couscous perlé (moghrabieh)|3", f"200 g|de pois chiches cuits|{POIS}|2", f"2|carottes|{CAROTTE}|2", "2|courgettes|Courgette|1", f"1|pomme de terre|{PDT}|1", f"2 c. à s.|de concentré de tomate|{CONC}|1", "1 c. à c.|de ras el-hanout|Ras el-hanout|1", f"1 bouquet|de coriandre|{CORI}|1", f"1|oignon|{OIG}|1"],
  ["**Sauce.** Oignon, concentré, épices, légumes en dés, 1,5 l d'eau, 20 min.", "**Berkoukes.** Revenus 3 min à l'huile ; dans la sauce avec les pois chiches, 15-20 min en remuant : tendres, sauce épaissie.", "**Servir.** Coriandre, citron, piment."],
  age=1, cats=["vegetarien", "enfants"])

K("pupusas_frijol_queso", "Pupusas haricots-fromage (Salvador)", "Pupusas de frijol con queso", "Amérique latine › Salvador", "P", 2, 4, 30, 15, "€", "Poêle épaisse.",
  "Galettes épaisses de farine de maïs farcies de purée de haricots et de fromage fondant, dorées à sec ; avec curtido (chou mariné) et sauce tomate.",
  ["300 g|de farine de maïs nixtamalisée (masa harina)|Farine de maïs|3", "250 g|de haricots rouges ou noirs cuits|Haricots rouges / noirs|2", "150 g|de mozzarella ou fromage à pâte fondante|Mozzarella / burrata|2", "¼|chou|Chou blanc / rouge|1", f"1|carotte|{CAROTTE}|1", f"5 cl|de vinaigre|{CIDRE}|1", f"200 g|de sauce tomate|Sauce tomate (bocal)|1"],
  ["**Curtido.** Chou et carotte râpés, vinaigre, origan, sel ; 1 h au frais.", "**Pâte.** Masa, sel, 35 cl d'eau tiède : souple comme pâte à modeler.",
   "**Farcir et cuire.** Boule creusée, cuillerée haricots écrasés + fromage, refermée, aplatie à 1 cm ; poêle à sec, 4 min par face : taches brunes. Curtido, sauce tomate."],
  age=1, cats=["vegetarien", "enfants"])

# ——— Océanie ———
K("agneau_roti_kumara", "Gigot d'agneau rôti et patates douces (Nouvelle-Zélande)", "Roast lamb & kumara", "Océanie › Nouvelle-Zélande", "P", 1, 8, 25, 110, "€€€", "Grand plat à rôtir, thermomètre.",
  "Le rôti du dimanche néo-zélandais : gigot piqué d'ail et de romarin, rôti sur des patates douces (kumara) qui caramélisent dans le jus, sauce à la menthe.",
  ["1|gigot d'agneau de 2 kg|Gigot d'agneau|3", "1 kg|de patates douces|Patate douce|3", f"6 gousses|d'ail|{AIL}|1", "4 brins|de romarin|Thym / romarin|1", f"4 c. à s.|d'huile d'olive|{HO}|1", "1 bouquet|de menthe|Menthe|1", f"2 c. à s.|de vinaigre|{CIDRE}|1", f"1 c. à s.|de sucre|{SUCRE}|1"],
  ["**Piquer.** Gigot sorti 1 h avant, piqué d'ail et de romarin, huilé, salé.", "**Rôtir.** Sur les patates douces en gros morceaux ; 180 °C, environ 1 h 30 (57 °C à cœur rosé, 65 °C à point) ; arrosé 2 fois.",
   "**Reposer.** 20 min sous aluminium. Sauce menthe : menthe hachée, vinaigre, sucre, 3 c. à s. d'eau chaude."],
  age=1, fetes=["Pâques", "Repas de famille"], tech=["rôtir", "températures à cœur"])

K("poulet_parmigiana_aus", "Chicken parmigiana (« parma » australien)", "Chicken parmigiana", "Océanie › Australie", "P", 1, 4, 25, 20, "€€", "Poêle, plat à four.",
  "Le plat des pubs australiens : escalope de poulet panée, sauce tomate et mozzarella gratinée, avec frites et salade. Version au jambon de dinde si on veut la garniture classique.",
  [f"4|blancs de poulet aplatis|{BLANC_P}|3", "100 g|de chapelure|Chapelure|2", f"2|œufs|{OEUF}|1", f"50 g|de farine|{F55}|1", f"300 g|de sauce tomate|Sauce tomate (bocal)|2", "200 g|de mozzarella|Mozzarella / burrata|2", f"40 g|de parmesan|{PARM}|1", "4 tranches|de jambon de dinde (facultatif)|Jambon de dinde / de poulet|1?"],
  ["**Paner.** Escalopes aplaties à 1 cm, farine, œuf, chapelure + parmesan.", "**Dorer.** Poêle 5 mm d'huile, 3 min par face : dorées.", "**Gratiner.** Sur plaque : jambon, sauce tomate, mozzarella ; gril 6-8 min : bouillonnant. Frites, salade."],
  age=1, cats=["enfants"], tech=["paner à l'anglaise"])
