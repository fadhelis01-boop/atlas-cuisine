# -*- coding: utf-8 -*-
"""Vague 2 · France (3/3) : Sud-Ouest, Centre, bistrot parisien, Outre-mer."""
from recipes_v2_base import *

K("magret_cerises", "Magret de canard aux cerises", "Magret aux cerises", "France › Nouvelle-Aquitaine › Gascogne", "P", 2, 4, 20, 20, "€€€", "Poêle, casserole.",
  "Un magret rosé à la peau croustillante, une sauce aigre-douce aux cerises : chic et rapide.",
  ["2|magrets de canard|Canard : magret, cuisse|3", "300 g|de cerises dénoyautées (fraîches ou surgelées)|Cerise / griotte|3", f"2 c. à s.|de vinaigre balsamique|Vinaigre balsamique|1", f"1 c. à s.|de miel|{MIEL}|1", f"1 pincée|de fleur de sel, poivre|{SEL}|0"],
  ["**Peau.** Quadrille la peau sans toucher la chair. Poêle froide, côté peau, feu moyen, 10 min : la graisse fond. Vide-la (garde-la pour les pommes de terre).",
   "**Chair.** Retourne 4 min. Repose 8 min sous aluminium : il reste rosé.", "**Sauce.** Dans la poêle, cerises, miel et balsamique 5 min. Tranche le magret, nappe."],
  age=3, profil=["gras", "viande_rouge", "sucre"], fetes=["Saint-Valentin"], zw=[], a=["Madiran"], sa=["Jus de cerise"])

K("pommes_sarladaises", "Pommes de terre sarladaises", "Pommes sarladaises", "France › Nouvelle-Aquitaine › Périgord", "A", 1, 4, 15, 30, "€", "Grande poêle.",
  "Pommes de terre dorées dans la graisse de canard, ail et persil : la garniture du Périgord.",
  [f"1 kg|de pommes de terre fermes|{PDT}|3", f"3 c. à s.|de graisse de canard|Graisse de canard|2", f"3 gousses|d'ail|{AIL}|2", f"1 bouquet|de persil|{PERSIL}|1", f"1 pincée|de fleur de sel|{SEL}|0"],
  ["**Dorer.** Rondelles de 3 mm dans la graisse chaude, 25 min en retournant.", "**Finir.** Ail et persil hachés les 3 dernières minutes, fleur de sel."],
  age=1, cats=["enfants"], profil=["gras"])

K("garbure", "Garbure (soupe paysanne du Béarn)", "Garbure", "France › Nouvelle-Aquitaine › Béarn", "So", 1, 6, 30, 120, "€", "Grand faitout.",
  "Une soupe épaisse de chou, haricots et légumes, avec du confit de canard : la cuillère tient debout.",
  [f"½|chou vert|Chou vert / frisé / kale|3", "250 g|de haricots blancs secs trempés|Haricots blancs / lingots|2", f"4|pommes de terre|{PDT}|2", f"3|carottes|{CAROTTE}|1", "2|navets|Navet / navet boule d'or|1",
   f"1|poireau|Poireau|1", "2|cuisses de canard confites|Canard : magret, cuisse|3", f"3 gousses|d'ail|{AIL}|1", f"1|bouquet garni|{LAURIER}|1"],
  ["**Haricots.** 1 h dans 3 L d'eau avec le bouquet garni.", "**Légumes.** Ajoute tous les légumes en morceaux et l'ail, 45 min.", "**Confit.** Ajoute les cuisses 15 min. Sers sur une tranche de pain de campagne."],
  age=1, cats=["zero_dechet"], profil=["gras"], kids="✓ dès 1 an, mixée sans le confit.")

K("piperade", "Piperade basque", "Piperade", "France › Nouvelle-Aquitaine › Pays basque", "A", 1, 4, 20, 30, "€", "Sauteuse.",
  "Poivrons, tomates et oignons fondus au piment d'Espelette ; on y casse des œufs ou on la sert avec une volaille.",
  [f"3|poivrons (rouges et verts)|{POIVRON}|3", f"6|tomates|{TOM}|3", f"2|oignons|{OIG}|2", f"2 gousses|d'ail|{AIL}|1", f"1 c. à c.|de piment d'Espelette|Piment d'Espelette|2", f"3 c. à s.|d'huile d'olive|{HO}|1", f"4|œufs (facultatif)|{OEUF}|1?"],
  ["**Fondre.** Oignons et poivrons en lanières 15 min dans l'huile.", "**Tomates.** Ajoute tomates concassées, ail, Espelette, sel ; 15 min.",
   "**Œufs.** Casse-les dessus, couvre 4 min (ou brouille-les dedans)."],
  age=1, cats=["enfants"], profil=["leger"], kids="✓ dès 1 an, sans piment pour les petits.")

K("gateau_basque", "Gâteau basque à la crème", "Gâteau basque (etxeko biskotxa)", "France › Nouvelle-Aquitaine › Pays basque", "D", 2, 8, 40, 45, "€", "Moule à manqué 24 cm, casserole.",
  "Une pâte sablée beurrée qui renferme une crème pâtissière à la vanille (ou une confiture de cerises noires).",
  [f"300 g|de farine|{F55}|3", f"200 g|de beurre mou|{BEURRE}|3", f"200 g|de sucre|{SUCRE}|2", f"3|œufs (2 + 1 jaune pour dorer)|{OEUF}|2", f"1 c. à c.|de levure chimique|{LEVC}|0",
   f"50 cl|de lait|{LAIT}|2", "3|jaunes d'œufs (crème)|Jaune d'œuf|2", f"40 g|de maïzena|Fécule de maïs (maïzena)|1", "1|gousse de vanille|Vanille (gousse)|1"],
  ["**Crème.** Lait vanillé chaud sur jaunes, 60 g de sucre et maïzena ; épaissis 2 min en fouettant. Filme au contact, refroidis.",
   "**Pâte.** Beurre + reste de sucre, 2 œufs, farine et levure : pâte molle, 1 h au frais.", "**Monter.** Deux disques ; crème au milieu ; ferme, dore au jaune, raye à la fourchette.", "**Cuire.** 45 min à 170 °C (th. 5-6)."],
  age=1, cats=["enfants"], fetes=["Repas de famille"], profil=["sucre", "gras"])

K("canneles", "Cannelés bordelais", "Canelé", "France › Nouvelle-Aquitaine › Bordeaux", "G", 2, 12, 15, 1500, "€", "Moules à cannelés (silicone ou cuivre), four.",
  "Croûte caramélisée, cœur moelleux à la vanille : le secret est le repos de la pâte et un four très chaud.",
  [f"50 cl|de lait|{LAIT}|3", f"250 g|de sucre|{SUCRE}|2", f"100 g|de farine|{F45}|2", f"2|œufs + 2 jaunes|{OEUF}|2", f"50 g|de beurre|{BEURRE}|2", "1|gousse de vanille|Vanille (gousse)|2",
   "3 c. à s.|de rhum (facultatif)|Rhum ambré / blanc|1?"],
  ["**Pâte.** Fais bouillir lait, vanille et beurre. Mélange farine, sucre, œufs ; verse le lait chaud, mélange sans fouetter. Rhum.",
   "**Repos.** 24 h au frigo : c'est indispensable.", "**Cuire.** Moules beurrés ; 15 min à 250 °C puis 50 min à 180 °C : la croûte doit être brun foncé."],
  var=[("Sans alcool", ["alcohol"], {"Rhum ambré / blanc": [("Extrait de vanille liquide", 0.3), ("Mélasse / sirop de canne", 0.3)]},
        "Rhum → **1 c. à c. d'extrait de vanille + 1 c. à c. de sirop de canne** : on retrouve la note ambrée. **À tester**.")],
  age=3, fetes=["Anniversaire"], profil=["sucre"], sa=["Café", "Thé noir"])

K("tourin", "Tourin à l'ail", "Tourin", "France › Nouvelle-Aquitaine › Périgord", "So", 1, 4, 15, 25, "€", "Casserole.",
  "Une soupe d'ail doux et d'oignon liée à l'œuf, sur du pain : économique et réconfortante.",
  [f"1 tête|d'ail|{AIL}|3", f"1|oignon|{OIG}|2", f"2 c. à s.|de graisse de canard|Graisse de canard|2", f"1 c. à s.|de farine|{F55}|1", f"2|œufs (blancs et jaunes séparés)|{OEUF}|2", f"1 c. à s.|de vinaigre|{CIDRE}|1", "4 tranches|de pain rassis|Pain rassis (réservé)|2"],
  ["**Fondre.** Ail et oignon émincés 10 min dans la graisse, sans colorer. Farine, puis 1,2 L d'eau salée, 15 min.", "**Lier.** Verse les blancs en filet en remuant ; hors du feu, les jaunes battus avec le vinaigre.", "**Servir.** Sur le pain."],
  age=1, cats=["zero_dechet"], profil=["gras"])

K("brandade", "Brandade de morue gratinée", "Brandade", "France › Occitanie › Nîmes", "P", 2, 6, 30, 30, "€€", "Casserole, presse-purée, plat à gratin.",
  "Morue pochée, émiettée et montée avec pommes de terre, ail et huile d'olive, gratinée au four.",
  ["600 g|de morue salée dessalée 24 h|Morue salée (dessalage 24-48 h)|3", f"600 g|de pommes de terre|{PDT}|3", f"3 gousses|d'ail|{AIL}|2", f"15 cl|d'huile d'olive|{HO}|2", f"15 cl|de lait chaud|{LAIT}|2", f"1 c. à s.|de chapelure|Chapelure|1"],
  ["**Dessaler.** 24 h dans l'eau froide changée 4 fois.", "**Pocher.** 8 min à frémissement ; émiette sans peau ni arêtes. Cuis les pommes de terre.",
   "**Monter.** Écrase pommes de terre, morue et ail ; ajoute huile et lait en alternance : purée souple.", "**Gratiner.** Chapelure, 15 min à 210 °C."],
  age=1, profil=["poisson"], fetes=["Repas de famille"])

K("tielle_setoise", "Tielle sétoise", "Tielle", "France › Occitanie › Sète", "P", 2, 6, 40, 45, "€€", "Moule à tarte haut, four.",
  "Une tourte à pâte levée garnie de calamars à la tomate épicée : le casse-croûte des quais de Sète.",
  ["1|pâte à pizza (recette liée)|SUB:pate_pizza|3", "600 g|de calamars en lanières|Calamar / encornet|3", f"400 g|de tomates pelées|{PELEES}|2", f"2|oignons|{OIG}|1", f"3 gousses|d'ail|{AIL}|1",
   f"1 c. à c.|de paprika|{PAPRIKA}|1", f"1 pincée|de piment|{CAYENNE}|1", f"3 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Garniture.** Oignons et ail fondus, calamars 5 min, tomates, épices ; 30 min jusqu'à ce que ce soit épais. Refroidis.", "**Monter.** Deux tiers de pâte dans le moule, garniture, couvercle de pâte, soude les bords en les roulant.", "**Cuire.** 40 min à 200 °C, doré à la tomate (badigeonne avec le jus)."],
  age=3, profil=["poisson"], sa=["Citronnade"])

K("blanquette_poulet", "Blanquette de poulet express", "Blanquette", "France › Île-de-France", "P", 1, 4, 20, 35, "€€", "Cocotte.",
  "Toute la douceur de la blanquette, en 1 heure, avec du poulet : sauce blanche citronnée, champignons, carottes.",
  [f"4|blancs de poulet|{BLANC_P}|3", f"3|carottes|{CAROTTE}|2", "250 g|de champignons|Champignon de Paris|2", f"1|oignon|{OIG}|1", f"20 cl|de crème|{CF}|2", "1|jaune d'œuf|Jaune d'œuf|1",
   f"30 g|de beurre + 30 g de farine|{BEURRE}|1", f"½|citron|{CIT}|1", f"1|bouquet garni|{LAURIER}|1"],
  ["**Pocher.** Poulet en morceaux, carottes et oignon couverts d'eau froide avec bouquet garni, 25 min.", "**Roux.** Beurre et farine 2 min ; ajoute 50 cl du bouillon filtré, épaissis. Champignons 10 min.",
   "**Lier.** Hors du feu, crème + jaune + citron. Remets poulet et carottes, sans bouillir. Avec du riz."],
  age=1, cats=["enfants"], profil=["leger", "gras"])

K("tarte_poireaux", "Flamiche aux poireaux", "Flamiche picarde", "France › Hauts-de-France › Picardie", "P", 1, 6, 25, 40, "€", "Moule à tarte, sauteuse.",
  "Des poireaux fondus au beurre dans une tarte crémeuse : la douceur du Nord.",
  ["1|pâte brisée (recette liée)|SUB:pate_brisee|3", "4|poireaux|Poireau|3", f"40 g|de beurre|{BEURRE}|2", f"2|œufs|{OEUF}|2", f"20 cl|de crème|{CF}|2", f"1 pincée|de muscade|{MUSC}|0"],
  ["**Poireaux.** Émincés, fondus 20 min au beurre à couvert, sans colorer.", "**Appareil.** Œufs + crème + muscade, poireaux.", "**Cuire.** 35 min à 180 °C."],
  age=1, cats=["enfants"], profil=["leger"], zw=[])

K("welsh", "Welsh du Nord", "Welsh rarebit", "France › Hauts-de-France › Nord", "P", 1, 4, 15, 15, "€€", "Plats individuels, casserole, four.",
  "Pain, cheddar fondu à la bière et à la moutarde, gratiné ; avec un œuf et des frites.",
  [f"4 tranches|de pain de campagne|Pain de campagne / complet|2", "400 g|de cheddar râpé|Cheddar|3", "20 cl|de bière blonde|Bière (blonde, brune, blanche)|2", f"1 c. à s.|de moutarde|{DIJON}|1",
   f"4|œufs (facultatif)|{OEUF}|1?", f"1 pincée|de poivre|{POIVRE}|0"],
  ["**Fondre.** Bière chaude, cheddar en remuant, moutarde, poivre : crème épaisse.", "**Gratiner.** Pain au fond du plat, nappe, 10 min à 220 °C sous le gril. Œuf au plat dessus."],
  var=[("Sans alcool", ["alcohol"], {"Bière (blonde, brune, blanche)": [("Bière 0,0 % / vin désalcoolisé", 1.0)]},
        "Bière → **bière sans alcool 0,0 %** (même amertume maltée) ou bouillon + 1 c. à c. de sauce Worcestershire. **À tester**.")],
  age=None, kids="✓ dès 3 ans en version 0,0 %.", profil=["gras"], sa=["Bière 0,0 %"])

K("potjevleesch_volaille", "Potjevleesch (terrine flamande de volaille)", "Potjevleesch", "France › Hauts-de-France › Flandre", "E", 2, 8, 30, 180, "€€", "Terrine en terre, four.",
  "Viandes blanches en gelée vinaigrée, servies froides avec des frites chaudes. Version poulet, lapin et veau, sans porc.",
  ["600 g|de cuisses de poulet désossées|Cuisse / pilon de poulet|3", "600 g|de lapin|Lapin|3", "400 g|de veau|Épaule / tendron de veau|2", f"2|oignons|{OIG}|1", f"25 cl|de vinaigre de vin blanc|Vinaigre de vin rouge / blanc|2",
   f"25 cl|de vin blanc|Vin blanc|1", "4 feuilles|de gélatine de bœuf ou agar-agar|Gélatine de bœuf / poisson, agar-agar, pectine|1", f"2 branches|de thym + 2 feuilles de laurier|{LAURIER}|1"],
  ["**Monter.** Viandes en morceaux, oignons, herbes, en couches dans la terrine ; verse vin, vinaigre et 20 cl d'eau avec la gélatine trempée.", "**Cuire.** Couvert, 3 h à 160 °C.", "**Prendre.** 24 h au frigo. Tranches froides avec frites chaudes."],
  var=[("Sans alcool", ["alcohol"], {"Vin blanc": [("Jus de pomme / raisin / orange (pur jus)", 0.5), ("Bouillon d'os maison (bœuf/volaille)", 0.5)]}, "Vin blanc → **½ jus de raisin blanc + ½ bouillon**. **À tester**.")],
  keep="5 jours au frigo.", age=3, profil=["acide"], fetes=["Repas de famille"])

K("galette_pdt_berrichonne", "Galette aux pommes de terre du Berry", "Galette de pommes de terre berrichonne", "France › Centre-Val de Loire › Berry", "A", 1, 6, 20, 35, "€", "Plaque, four.",
  "Une pâte feuilletée rapide faite avec de la purée : dorée, fondante, parfaite avec une salade.",
  [f"400 g|de purée de pommes de terre (reste)|{PDT}|3", f"250 g|de farine|{F55}|2", f"150 g|de beurre mou|{BEURRE}|2", f"1|œuf|{OEUF}|1", f"1 c. à c.|de sel|{SEL}|0"],
  ["**Pâte.** Mélange purée, farine, beurre, sel. Étale, plie en trois, étale de nouveau (deux fois).", "**Cuire.** Disque de 2 cm, quadrillé, doré à l'œuf ; 35 min à 200 °C."],
  age=1, cats=["zero_dechet", "enfants"], profil=["gras"])

K("colombo_poulet", "Colombo de poulet", "Colombo", "France › Outre-mer › Antilles", "P", 1, 6, 30, 50, "€€", "Cocotte.",
  "Le curry antillais : poudre de colombo grillée, légumes fondants, citron vert et un soupçon de piment.",
  [f"1,2 kg|de cuisses de poulet|{CUISSE}|3", "3 c. à s.|de poudre de colombo|Colombo (mélange antillais)|3", "1|christophine ou courgette|Chayotte / christophine|2", "1|aubergine|Aubergine|1", f"3|pommes de terre|{PDT}|2",
   f"2|oignons|{OIG}|1", f"3 gousses|d'ail|{AIL}|1", f"2|citrons verts|{CITV}|2", "1|piment antillais entier (non percé)|Piment antillais / scotch bonnet|1", f"2 c. à s.|d'huile|{HN}|1", f"1 branche|de thym|{THYM}|0"],
  ["**Mariner.** Poulet, jus d'un citron vert, ail, sel, 1 h.", "**Dorer.** Poulet puis oignons ; colombo 1 min.", "**Mijoter.** Légumes en cubes, eau à mi-hauteur, thym et piment entier ; 45 min. Retire le piment ; citron vert au service. Avec du riz."],
  age=3, kids="✓ dès 3 ans : le piment entier non percé ne fait que parfumer.", profil=["epice"], sa=["Jus de goyave"], a=["Rhum arrangé (avec modération)"])

K("blaff_poisson", "Blaff de poisson", "Blaff", "France › Outre-mer › Antilles", "P", 1, 4, 20, 20, "€€", "Faitout.",
  "Poisson poché dans un court-bouillon citronné, aillé et pimenté : léger et très parfumé.",
  ["4|darnes de dorade ou de bar|Dorade|3", f"4|citrons verts|{CITV}|3", f"4 gousses|d'ail|{AIL}|2", "2|cives ou oignons nouveaux|Oignon nouveau / cébette|1", "1|piment antillais|Piment antillais / scotch bonnet|1", f"2 branches|de thym + 1 de persil|{THYM}|1", "2|clous de girofle|Clou de girofle|0"],
  ["**Mariner.** Poisson, jus de 2 citrons, ail écrasé, sel, 30 min.", "**Court-bouillon.** 1 L d'eau, cives, herbes, girofle, piment entier, 10 min.", "**Pocher.** Poisson 8 min. Jus de citron frais au service, avec riz blanc."],
  age=3, profil=["poisson", "leger", "acide"])

K("feroce_avocat", "Féroce d'avocat", "Féroce", "France › Outre-mer › Martinique", "E", 1, 4, 15, 0, "€", "Fourchette, bol.",
  "Avocat écrasé avec de la morue émiettée, du manioc et du piment : une entrée martiniquaise relevée.",
  ["2|avocats mûrs|Avocat|3", "150 g|de morue dessalée pochée|Morue salée (dessalage 24-48 h)|3", "4 c. à s.|de farine de manioc|Farofa / farine de manioc torréfiée|1", f"1|citron vert|{CITV}|2", f"1 gousse|d'ail|{AIL}|1", "½|piment antillais|Piment antillais / scotch bonnet|1", f"2 c. à s.|d'huile|{HN}|1"],
  ["**Écraser.** Avocat, citron vert, ail, piment haché.", "**Lier.** Morue émiettée, huile, farine de manioc : pâte épaisse. Sers frais en boule."],
  age=None, profil=["poisson", "epice"], fetes=["Apéritif dînatoire"])

K("rougail_saucisses", "Rougail saucisses (saucisses de volaille fumées)", "Rougail saucisses", "France › Outre-mer › La Réunion", "P", 1, 6, 20, 45, "€€", "Cocotte.",
  "Saucisses fumées mijotées dans une sauce tomate-oignon au curcuma et au gingembre. Ici avec des saucisses de volaille, et un peu de paprika fumé pour le boucané.",
  ["8|saucisses de volaille fumées|Saucisse de bœuf / de veau / de volaille|3", f"6|tomates|{TOM}|3", f"3|oignons|{OIG}|2", f"4 gousses|d'ail|{AIL}|1", f"1 morceau|de gingembre|{GING}|1", f"1 c. à c.|de curcuma|{CURC}|1",
   f"1 c. à c.|de paprika fumé|{PFUME}|1", f"1|piment|{PIMENT}|1", f"2 c. à s.|d'huile|{HN}|1", f"2 branches|de thym|{THYM}|0"],
  ["**Saucisses.** Pique-les, blanchis 5 min, coupe en tronçons et dore-les.", "**Rougail.** Oignons dorés, ail-gingembre pilés, curcuma, paprika fumé, tomates concassées, thym, piment.", "**Mijoter.** 30 min à feu doux jusqu'à ce que la sauce attache un peu. Riz, grains (haricots rouges) et rougail tomate."],
  age=3, profil=["epice", "gras"], sa=["Jus de letchi"], kids="✓ dès 3 ans sans le piment.")

K("cari_poulet", "Cari de poulet réunionnais", "Cari poulet", "France › Outre-mer › La Réunion", "P", 1, 6, 20, 50, "€", "Cocotte.",
  "Le plat du dimanche réunionnais : poulet au safran péi (curcuma), ail, gingembre et tomate.",
  [f"1,5 kg|de poulet en morceaux|{CUISSE}|3", f"4|tomates|{TOM}|2", f"2|oignons|{OIG}|2", f"6 gousses|d'ail|{AIL}|2", f"1 morceau|de gingembre|{GING}|2", f"2 c. à c.|de curcuma|{CURC}|2", f"2 branches|de thym|{THYM}|1", f"2 c. à s.|d'huile|{HN}|1"],
  ["**Dorer.** Poulet salé bien doré dans l'huile.", "**Base.** Oignons, ail et gingembre pilés, curcuma 1 min (sans brûler).", "**Mijoter.** Tomates, thym, un verre d'eau ; 40 min à couvert puis 10 min découvert."],
  age=1, cats=["enfants"], profil=["epice"])

K("poisson_cru_coco", "Poisson cru au lait de coco (Tahiti)", "Ia ota", "France › Outre-mer › Polynésie", "E", 1, 4, 20, 15, "€€€", "Saladier, couteau bien aiguisé.",
  "Thon très frais « cuit » au citron vert, légumes croquants et lait de coco : la fraîcheur des îles.",
  ["500 g|de thon rouge ou albacore extra-frais|Thon (frais)|3", f"4|citrons verts|{CITV}|3", f"20 cl|de lait de coco|{COCO}|3", "1|concombre|Concombre|2", f"2|tomates|{TOM}|1", f"1|carotte|{CAROTTE}|1", "1|oignon nouveau|Oignon nouveau / cébette|1", f"1 pincée|de sel|{SEL}|0"],
  ["**Mariner.** Thon en cubes de 2 cm, jus des citrons, sel ; 10 à 15 min au frais, il blanchit en surface.", "**Égoutter.** Retire la moitié du jus.", "**Finir.** Légumes en petits dés, lait de coco ; sers très froid."],
  tips=["⚠️ Poisson cru : extra-frais ou congelé 7 jours à −20 °C (anisakis). Déconseillé femmes enceintes et jeunes enfants."], keep="À manger tout de suite.", age=None, profil=["poisson", "leger", "acide"])

K("flan_coco", "Flan coco (Antilles)", "Flan coco", "France › Outre-mer › Antilles", "D", 1, 8, 15, 50, "€", "Moule à cake ou à charlotte, four, bain-marie.",
  "Un flan dense et lisse au lait concentré et à la noix de coco, nappé de caramel.",
  ["1 boîte (397 g)|de lait concentré sucré|Lait concentré sucré / non sucré|3", f"40 cl|de lait de coco|{COCO}|3", f"4|œufs|{OEUF}|2", "60 g|de noix de coco râpée|Noix de coco râpée|2", f"100 g|de sucre (caramel)|{SUCRE}|1", f"1 pincée|de vanille|{VAN}|0"],
  ["**Caramel.** Sucre + 2 c. à s. d'eau, blond foncé ; verse dans le moule.", "**Appareil.** Fouette le reste, verse.", "**Cuire.** 50 min à 170 °C au bain-marie. Une nuit au frigo, démoule."],
  age=1, cats=["enfants"], profil=["sucre"], fetes=["Repas de famille"])

K("bokit_volaille", "Bokits (pains frits guadeloupéens)", "Bokit", "France › Outre-mer › Guadeloupe", "Pa", 2, 8, 30, 90, "€", "Poêle profonde ou friteuse, saladier.",
  "Des pains frits gonflés qu'on ouvre et garnit : poulet, crudités, sauce chien, fromage…",
  [f"500 g|de farine|{F55}|3", "25 cl|d'eau tiède|-|0", f"5 g|de levure boulangère|{LEV}|1", f"1 c. à c.|de levure chimique|{LEVC}|1", f"30 g|de beurre fondu|{BEURRE}|1", f"1 c. à c.|de sel|{SEL}|0", "1 L|d'huile de friture|Huile d'arachide|1"],
  ["**Pâte.** Pétris tout 10 min ; pousse 1 h.", "**Former.** 8 boules aplaties à 1 cm ; 20 min de repos.", "**Frire.** 3 min par face à 170 °C : ils gonflent. Égoutte, ouvre, garnis."],
  age=3, cats=["pains"], profil=["gras"], fetes=["Barbecue d'été"])
