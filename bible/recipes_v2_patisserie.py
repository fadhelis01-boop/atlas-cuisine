# -*- coding: utf-8 -*-
"""Vague 2 · Pâtisserie et viennoiserie françaises (cahier du chef pâtissier : recettes de maison, gestes de pro)."""
from recipes_v2_base import *

IDF = "France › Île-de-France › Paris"
CP = "SUB:creme_patissiere"

K("creme_patissiere", "Crème pâtissière vanille", "Crème pâtissière", IDF, "Ba", 1, 6, 15, 60, "€", "Casserole à fond épais, fouet, film.",
  "La crème de base des choux, éclairs, millefeuilles et tartes aux fruits : onctueuse, vanillée, prête en 15 minutes.",
  [f"50 cl|de lait entier|{LAIT}|3", "4|jaunes d'œufs|Jaune d'œuf|3", f"100 g|de sucre|{SUCRE}|2", f"40 g|de maïzena|Fécule de maïs (maïzena)|2", "1|gousse de vanille|Vanille (gousse)|2", f"25 g|de beurre|{BEURRE}|1"],
  ["**Infuser.** Porte le lait à ébullition avec la gousse fendue et grattée.", "**Blanchir.** Fouette jaunes et sucre jusqu'à ce qu'ils pâlissent, ajoute la maïzena.",
   "**Cuire.** Verse la moitié du lait chaud dessus en fouettant, remets tout dans la casserole ; fouette sans arrêt : dès les premiers bouillons, compte 1 min.", "**Refroidir.** Hors du feu, le beurre ; étale dans un plat, film au contact, frigo 1 h. Fouette-la avant usage pour la lisser."],
  keep="48 h au frigo, filmée au contact.", age=1, cats=["enfants"], profil=["sucre"], tech=["Crème pâtissière"],
  zw=[("Blancs d'œufs restants", "→ meringues, financiers ou macarons (recettes liées).")])

K("eclairs_chocolat", "Éclairs au chocolat", "Éclair", IDF, "D", 2, 12, 45, 35, "€", "Poche à douille 12-14 mm, plaque, casserole.",
  "Une pâte à choux croustillante, une crème pâtissière au chocolat noir et un glaçage brillant : l'éclair de pâtisserie, chez toi.",
  ["25 cl|d'eau et lait (moitié-moitié)|-|0", f"100 g|de beurre|{BEURRE}|2", f"140 g|de farine|{F55}|2", f"4|œufs|{OEUF}|2", f"1 pincée|de sel et 1 c. à c. de sucre|{SEL}|0",
   f"1|recette de crème pâtissière (liée)|{CP}|3", f"120 g|de chocolat noir|{CHOCO}|3", f"10 cl|de crème|{CL}|1"],
  ["**Choux.** Eau, lait, beurre, sel, sucre à ébullition ; farine d'un coup, dessèche 1 min ; hors du feu, les œufs un à un jusqu'au « bec d'oiseau ».",
   "**Pocher.** Bâtons de 12 cm, dorure, raies à la fourchette ; 35 min à 170 °C sans ouvrir le four. Refroidis sur grille.",
   "**Crème.** Fais fondre 70 g de chocolat dans la crème pâtissière chaude.", "**Garnir.** 2 petits trous dessous, remplis à la poche.", "**Glaçage.** 50 g de chocolat + crème chaude, trempe le dessus des éclairs, 30 min au frais."],
  keep="24 h au frigo (la pâte ramollit ensuite).", age=1, cats=["enfants"], fetes=["Anniversaire"], profil=["sucre", "gras"], tech=["Pâte à choux", "Crème pâtissière", "Ganache"])

K("chouquettes", "Chouquettes", "Chouquette", IDF, "G", 1, 30, 20, 25, "€", "Poche ou 2 cuillères, plaque.",
  "Des petits choux creux couverts de sucre perlé : le goûter des boulangeries parisiennes.",
  ["25 cl|d'eau|-|0", f"100 g|de beurre|{BEURRE}|2", f"150 g|de farine|{F55}|3", f"4|œufs|{OEUF}|3", f"1 c. à s.|de sucre|{SUCRE}|1", "80 g|de sucre perlé (ou en morceaux concassé)|Sucre blanc / roux / cassonade / vergeoise|2"],
  ["**Pâte à choux.** Comme pour les éclairs (eau, beurre, sucre, sel, farine, desséchée, puis œufs).", "**Dresser.** Petites boules de 3 cm, dorure, sucre perlé généreux.", "**Cuire.** 25 min à 180 °C, bien dorées."],
  age=1, cats=["enfants"], profil=["sucre"], tech=["Pâte à choux"], fetes=["Anniversaire"])

K("profiteroles", "Profiteroles, sauce chocolat chaude", "Profiteroles", IDF, "D", 2, 6, 30, 30, "€€", "Poche, plaque, casserole.",
  "Choux garnis de glace vanille, nappés d'une sauce chocolat chaude au moment de servir.",
  ["1|recette de pâte à choux (voir chouquettes)|SUB:chouquettes|3", "50 cl|de glace vanille|Crème fleurette (liquide)|3", f"150 g|de chocolat noir|{CHOCO}|3", f"15 cl|de crème|{CL}|2", "30 g|d'amandes effilées grillées|Amande (entière, effilée, poudre)|1"],
  ["**Choux.** Boules de 4 cm, sans sucre perlé, 25 min à 180 °C.", "**Sauce.** Crème chaude sur le chocolat haché, lisse.", "**Servir.** Choux coupés, boule de glace, sauce chaude, amandes."],
  age=1, cats=["enfants"], fetes=["Anniversaire", "Repas de famille"], profil=["sucre", "gras"], tech=["Pâte à choux", "Ganache"])

K("paris_brest", "Paris-Brest (crème mousseline pralinée)", "Paris-Brest", f"France › Île-de-France › Maisons-Laffitte", "D", 3, 8, 60, 45, "€€", "Poche à douille cannelée, batteur, plaque.",
  "Une couronne de pâte à choux aux amandes, garnie d'une crème mousseline au praliné : un sommet de gourmandise.",
  ["1|recette de pâte à choux|SUB:chouquettes|3", "30 g|d'amandes effilées|Amande (entière, effilée, poudre)|1", f"1|recette de crème pâtissière|{CP}|3", f"125 g|de beurre mou|{BEURRE}|2", "150 g|de praliné maison|Praliné / pâte de noisette|3", "1 c. à s.|de sucre glace|Sucre glace|0"],
  ["**Couronne.** Trace un cercle de 22 cm ; poche 2 boudins collés et un 3e dessus. Amandes, 40 min à 170 °C, puis 5 min four entrouvert.",
   "**Mousseline.** Crème pâtissière tiède + praliné ; fouette le beurre pommade et ajoute la crème en 3 fois : légère et ferme.", "**Monter.** Coupe la couronne en deux, garnis en rosaces, couvercle, sucre glace. 1 h au frais."],
  keep="48 h au frigo.", age=3, fetes=["Anniversaire", "Repas de famille"], profil=["sucre", "gras"], tech=["Pâte à choux", "Crème pâtissière", "Praliné"])

K("pate_sucree", "Pâte sucrée aux amandes", "Pâte sucrée", IDF, "Ba", 1, 8, 15, 120, "€", "Saladier, rouleau, cercle 24 cm.",
  "Le fond de tarte des pâtissiers : fin, friable, qui ne se rétracte pas.",
  [f"200 g|de farine|{F55}|3", f"110 g|de beurre mou|{BEURRE}|3", "70 g|de sucre glace|Sucre glace|2", "25 g|de poudre d'amande|Farine d'amande / poudre d'amande|1", f"1|œuf|{OEUF}|2", f"1 pincée|de sel|{SEL}|0"],
  ["**Crémage.** Beurre, sucre glace, amande, sel ; puis l'œuf.", "**Farine.** D'un coup, mélange juste. Aplatis, 2 h au frais.", "**Foncer.** 3 mm, pique, 30 min au congélateur, puis cuis à blanc 20-25 min à 165 °C."],
  keep="Crue : 3 jours au frigo, 2 mois congelée.", age=1, cats=["enfants"], profil=["sucre"], tech=["Pâte sucrée"])

K("tarte_fraises", "Tarte aux fraises", "Tarte aux fraises", IDF, "D", 1, 8, 30, 25, "€€", "Cercle 24 cm.",
  "Fond sablé, crème pâtissière vanillée, fraises de saison serrées et un nappage léger.",
  ["1|pâte sucrée (recette liée)|SUB:pate_sucree|3", f"½|recette de crème pâtissière|{CP}|3", "500 g|de fraises|Fraise|3", "2 c. à s.|de confiture de fraises ou de groseilles|Confiture / gelée|1"],
  ["**Fond.** Cuit à blanc et refroidi.", "**Garnir.** Crème pâtissière lissée, fraises coupées en deux serrées.", "**Nappage.** Confiture chauffée avec 1 c. à s. d'eau, au pinceau."],
  keep="24 h au frigo.", age=1, cats=["enfants"], fetes=["Anniversaire", "Repas de famille"], profil=["sucre"], tech=["Pâte sucrée", "Crème pâtissière"])

K("tarte_chocolat", "Tarte au chocolat noir", "Tarte au chocolat", IDF, "D", 1, 8, 25, 140, "€€", "Cercle 24 cm.",
  "Une ganache fondante au chocolat noir dans un fond sablé : intense, lisse, brillante.",
  ["1|pâte sucrée (recette liée)|SUB:pate_sucree|3", f"200 g|de chocolat noir 60-70 %|{CHOCO}|3", f"20 cl|de crème|{CL}|2", f"5 cl|de lait|{LAIT}|1", f"1|œuf|{OEUF}|1", f"30 g|de beurre|{BEURRE}|1", "1 pincée|de fleur de sel|Sel fin / gros sel / fleur de sel|0"],
  ["**Fond.** Cuit à blanc.", "**Ganache.** Crème + lait chauds sur chocolat, émulsionne ; à 40 °C, l'œuf battu et le beurre.", "**Cuire.** Coule et enfourne 15 min à 120 °C : centre encore tremblotant. 2 h à température ambiante."],
  age=1, fetes=["Anniversaire", "Saint-Valentin"], profil=["sucre", "gras"], tech=["Ganache", "Pâte sucrée"])

K("millefeuille", "Millefeuille vanille", "Mille-feuille", IDF, "D", 3, 8, 45, 30, "€€", "2 plaques, papier cuisson, poche.",
  "Feuilletage caramélisé, crème légère vanillée : le grand classique, monté juste avant de servir.",
  ["1|pâte feuilletée pur beurre|Pâte feuilletée (prête)|3", f"1|recette de crème pâtissière|{CP}|3", f"20 cl|de crème fleurette montée|{CL}|2", "50 g|de sucre glace|Sucre glace|1"],
  ["**Feuilletage.** Étale, pique, entre deux plaques (il ne gonfle pas) : 25 min à 190 °C ; sucre glace et 3 min sous le gril pour caraméliser. Coupe 3 rectangles égaux.",
   "**Crème diplomate.** Crème pâtissière lissée + chantilly.", "**Monter.** Feuille, crème à la poche, feuille, crème, feuille caramélisée dessus. Coupe au couteau-scie."],
  keep="À manger dans les 4 h (le feuilletage ramollit).", age=1, fetes=["Repas de famille"], profil=["sucre", "gras"], tech=["Feuilletage", "Crème pâtissière", "Chantilly"])

K("flan_patissier", "Flan pâtissier", "Flan parisien", IDF, "D", 1, 8, 20, 300, "€", "Moule à manqué haut 22 cm.",
  "Un flan dense et vanillé, dessus brûlé, sur une pâte brisée : le roi des vitrines de boulangerie.",
  ["1|pâte brisée (recette liée)|SUB:pate_brisee|2", f"75 cl|de lait|{LAIT}|3", f"25 cl|de crème|{CL}|2", f"4|œufs|{OEUF}|2", f"180 g|de sucre|{SUCRE}|2", f"80 g|de maïzena|Fécule de maïs (maïzena)|2", "2|gousses de vanille|Vanille (gousse)|2"],
  ["**Crème.** Lait + crème vanillés bouillants ; sur œufs, sucre, maïzena ; épaissis 1 min en fouettant.", "**Cuire.** Coule dans la pâte, 50 min à 180 °C : dessus bien doré, voire tacheté.", "**Repos.** 4 h au frigo avant de couper."],
  age=1, cats=["enfants"], profil=["sucre"], tech=["Crème pâtissière"])

K("fraisier", "Fraisier", "Fraisier", IDF, "D", 3, 10, 75, 240, "€€€", "Cercle 22 cm, rhodoïd (ou papier cuisson), batteur.",
  "Génoise imbibée, crème mousseline vanille et fraises entières en vitrine : le gâteau d'anniversaire du printemps.",
  [f"4|œufs (génoise)|{OEUF}|2", f"120 g|de sucre (génoise)|{SUCRE}|2", f"120 g|de farine|{F55}|2", f"1|recette de crème pâtissière|{CP}|3", f"150 g|de beurre mou|{BEURRE}|2", "750 g|de fraises|Fraise|3", f"10 cl|de sirop (sucre + eau + citron)|{SUCRE}|1", "100 g|de pâte d'amande (facultatif)|Pâte d'amande / massepain|1?"],
  ["**Génoise.** Œufs + sucre au bain-marie à 45 °C, puis fouettés jusqu'au ruban ; farine à la spatule ; 25 min à 180 °C. Coupe en 2 disques.",
   "**Mousseline.** Crème pâtissière tiède, puis beurre pommade en 3 fois.", "**Monter.** Cercle chemisé : disque imbibé, fraises coupées en deux contre la paroi (face coupée vers l'extérieur), crème, fraises entières, crème, 2e disque imbibé, fine couche de crème.",
   "**Prise.** 4 h au frais ; pâte d'amande étalée dessus, décor de fraises."],
  keep="48 h au frigo.", age=1, fetes=["Anniversaire"], profil=["sucre", "gras"], tech=["Génoise", "Crème pâtissière"])

K("macarons_framboise", "Macarons framboise", "Macaron parisien", IDF, "G", 3, 30, 60, 90, "€€", "Balance précise, poche, tapis ou papier cuisson, thermomètre.",
  "Coques lisses et croquantes, cœur moelleux, ganache framboise acidulée : le macaron parisien, méthode meringue italienne.",
  ["150 g|de poudre d'amande|Farine d'amande / poudre d'amande|3", "150 g|de sucre glace|Sucre glace|2", "110 g|de blancs d'œufs vieillis 24 h (en 2 fois 55 g)|Blanc d'œuf|3", f"150 g|de sucre|{SUCRE}|2",
   "150 g|de framboises|Framboise / mûre / myrtille|2", "150 g|de chocolat blanc|Chocolat blanc|2", "1 pointe|de colorant naturel (betterave en poudre, facultatif)|Betterave (crue/cuite)|0?"],
  ["**Tant pour tant.** Amande + sucre glace mixés brièvement, tamisés, mélangés à 55 g de blancs crus.", "**Meringue italienne.** Sucre + 4 cl d'eau à 118 °C sur 55 g de blancs mousseux ; fouette jusqu'à 45 °C.",
   "**Macaronner.** Meringue dans le tant pour tant, écrase à la maryse jusqu'au ruban brillant.", "**Coques.** Disques de 3 cm, tapote, croûtage 30 min, 13 min à 150 °C.",
   "**Ganache.** Framboises écrasées chauffées, versées sur le chocolat blanc, émulsionne ; froid 2 h. Garnis, puis 24 h au frigo (ils deviennent moelleux)."],
  keep="5 jours au frigo, 1 mois congelés.", age=3, fetes=["Saint-Valentin", "Anniversaire"], profil=["sucre"], tech=["Macaronnage", "Meringue italienne", "Ganache"])

K("financiers", "Financiers au beurre noisette", "Financier", IDF, "G", 1, 16, 15, 15, "€", "Moules à financiers ou mini-muffins.",
  "Petits gâteaux aux blancs d'œufs, à l'amande et au beurre noisette : moelleux dedans, croustillants sur les bords.",
  ["4|blancs d'œufs (120 g)|Blanc d'œuf|3", "125 g|de sucre glace|Sucre glace|2", "50 g|de poudre d'amande|Farine d'amande / poudre d'amande|2", f"40 g|de farine|{F55}|1", f"100 g|de beurre|{BEURRE}|3"],
  ["**Beurre noisette.** Cuis le beurre jusqu'à ce qu'il mousse et sente la noisette (brun clair) ; filtre.", "**Pâte.** Sucre, amande, farine, blancs juste mélangés (sans monter), puis beurre tiède.", "**Cuire.** Moules aux ¾, 12-15 min à 200 °C : bords dorés."],
  keep="5 jours en boîte.", age=1, cats=["enfants", "zero_dechet"], profil=["sucre"], tips=["La recette qui utilise les blancs restants d'une crème pâtissière."])

K("creme_caramel", "Crème renversée au caramel", "Crème caramel", IDF, "D", 1, 6, 15, 280, "€", "Ramequins ou moule, bain-marie.",
  "Un flan aux œufs lisse et ferme, nappé de son caramel : le dessert des grands-mères.",
  [f"75 cl|de lait|{LAIT}|3", f"4|œufs + 2 jaunes|{OEUF}|3", f"120 g|de sucre|{SUCRE}|2", f"100 g|de sucre (caramel)|{SUCRE}|2", "1|gousse de vanille|Vanille (gousse)|1"],
  ["**Caramel.** Ambré, coulé au fond des ramequins.", "**Crème.** Lait vanillé chaud sur œufs + sucre, filtré.", "**Cuire.** Au bain-marie, 40 min à 150 °C. 4 h au frais ; démoule en passant une lame."],
  age=1, cats=["enfants"], profil=["sucre"], tech=["Caramel"])

K("charlotte_fraises", "Charlotte aux fraises", "Charlotte", IDF, "D", 2, 8, 35, 360, "€€", "Moule à charlotte, batteur.",
  "Biscuits cuillère imbibés, mousse légère aux fraises : un gâteau sans cuisson.",
  ["30|biscuits cuillère|Boudoirs / biscuits cuillère|3", "500 g|de fraises|Fraise|3", f"30 cl|de crème|{CL}|2", "250 g|de mascarpone ou fromage blanc|Mascarpone|2", "80 g|de sucre glace|Sucre glace|1", "2 g|d'agar-agar|Gélatine de bœuf / poisson, agar-agar, pectine|1", f"10 cl|de sirop (sucre + eau)|{SUCRE}|1"],
  ["**Mousse.** 250 g de fraises mixées, chauffées 2 min avec l'agar-agar, tiédies ; chantilly au mascarpone + sucre glace, mélangée.", "**Monter.** Biscuits trempés 1 s dans le sirop contre les parois, mousse, fraises en morceaux, biscuits.", "**Prise.** 6 h au frais, sous une assiette. Démoule, fraises dessus."],
  age=1, cats=["enfants"], fetes=["Anniversaire"], profil=["sucre"], tech=["Chantilly"])

K("tropezienne", "Tarte tropézienne", "Tarte tropézienne", "France › Provence-Alpes-Côte d'Azur › Saint-Tropez", "D", 2, 8, 40, 180, "€€", "Cercle 24 cm, batteur.",
  "Brioche au sucre perlé coupée en deux, crème diplomate à la fleur d'oranger : le gâteau de la Côte d'Azur.",
  ["1|pâte à brioche (recette liée)|SUB:brioche|3", f"1|recette de crème pâtissière|{CP}|3", f"20 cl|de crème montée|{CL}|2", "2 c. à s.|d'eau de fleur d'oranger|Eau de fleur d'oranger|2", "40 g|de sucre perlé|Sucre blanc / roux / cassonade / vergeoise|1"],
  ["**Brioche.** Disque de 24 cm, pousse 1 h 30, dorure, sucre perlé ; 25 min à 170 °C.", "**Crème.** Pâtissière froide lissée + fleur d'oranger + chantilly.", "**Monter.** Coupe la brioche en deux, sirop léger à la fleur d'oranger, crème, couvercle. 2 h au frais."],
  age=1, fetes=["Anniversaire"], profil=["sucre"], tech=["Crème pâtissière", "Brioche"])

K("croissants", "Croissants pur beurre", "Croissant", IDF, "Pa", 3, 12, 90, 900, "€", "Rouleau, règle, papier cuisson.",
  "Croissants feuilletés et alvéolés, faits sur deux jours sans difficulté : le froid fait le travail.",
  [f"500 g|de farine T45|{F45}|3", f"25 cl|de lait froid|{LAIT}|2", f"60 g|de sucre|{SUCRE}|1", f"10 g|de levure sèche|{LEV}|1", f"10 g|de sel|{SEL}|0", f"280 g|de beurre de tourage (dont 30 g dans la pâte)|{BEURRE}|3", f"1|œuf (dorure)|{OEUF}|1"],
  ["**J-1, détrempe.** Farine, lait, sucre, levure, sel, 30 g de beurre : pâte lisse, 5 min. Une nuit au frigo.", "**Tourage.** Beurre en carré 15 cm entre deux papiers ; enferme-le dans la pâte ; un tour double, 30 min au frais, un tour simple, 30 min.",
   "**Façonner.** Étale à 4 mm, triangles de 10 × 25 cm, entaille la base, roule sans serrer.", "**Apprêt.** 2 h à 25 °C maximum : ils doublent et tremblent. Dorure.", "**Cuire.** 16 min à 180 °C, bien dorés."],
  keep="Crus façonnés : 1 mois au congélateur (apprêt une nuit au frigo).", age=1, cats=["pains", "enfants"], profil=["gras"], tech=["Tourage"])

K("pains_chocolat", "Pains au chocolat (chocolatines)", "Pain au chocolat", IDF, "Pa", 3, 12, 90, 900, "€", "Rouleau, règle.",
  "La même pâte que les croissants, roulée autour de deux barres de chocolat.",
  ["1|recette de pâte à croissants (liée)|SUB:croissants|3", "24|bâtons de chocolat noir|Chocolat noir|3", f"1|œuf|{OEUF}|1"],
  ["**Découper.** Pâte tourée à 4 mm, rectangles de 8 × 15 cm.", "**Rouler.** Un bâton, un tour, un 2e bâton, roule jusqu'au bout, soudure dessous.", "**Apprêt et cuisson.** 2 h à 25 °C, dorure, 16 min à 180 °C."],
  age=1, cats=["pains", "enfants"], profil=["sucre", "gras"], tech=["Tourage"])

K("chaussons_pommes", "Chaussons aux pommes", "Chausson aux pommes", "France › Hauts-de-France", "G", 1, 8, 25, 25, "€", "Plaque, emporte-pièce cannelé.",
  "Feuilletage croustillant et compote maison de pommes : la viennoiserie des goûters.",
  ["2|pâtes feuilletées|Pâte feuilletée (prête)|3", "6|pommes|Pomme|3", f"50 g|de sucre|{SUCRE}|1", f"20 g|de beurre|{BEURRE}|1", f"1|œuf|{OEUF}|1", f"1 pincée|de cannelle|{CANN}|0"],
  ["**Compote.** Pommes en dés, beurre, sucre, 15 min : épaisse, avec des morceaux. Refroidis.", "**Façonner.** Ovales de 14 cm, compote sur une moitié, ferme en pinçant, dorure, raies au couteau, trou d'aération.", "**Cuire.** 25 min à 200 °C."],
  age=1, cats=["enfants", "zero_dechet"], profil=["sucre"], tips=["Pommes abîmées : idéal pour la compote."])

K("palmiers", "Palmiers", "Palmier", IDF, "G", 1, 30, 15, 15, "€", "Plaque.",
  "Feuilletage roulé dans le sucre qui caramélise : deux ingrédients, un biscuit croustillant.",
  ["1|pâte feuilletée|Pâte feuilletée (prête)|3", f"100 g|de sucre|{SUCRE}|3"],
  ["**Sucrer.** Étale la pâte sur du sucre, saupoudre aussi dessus, passe le rouleau.", "**Rouler.** Les deux bords vers le centre, puis rabats l'un sur l'autre ; 20 min au congélateur.", "**Cuire.** Tranches de 1 cm, 8 min à 200 °C, retourne, 5 min."],
  keep="1 semaine en boîte.", age=1, cats=["enfants", "zero_dechet"], profil=["sucre"], tips=["Chutes de feuilletage : parfaites pour les palmiers."])

K("sables_bretons", "Sablés bretons au beurre salé", "Sablé breton", "France › Bretagne", "G", 1, 20, 20, 75, "€", "Cercles ou moules à muffins, plaque.",
  "Épais, friables, au beurre demi-sel : la base de nombreuses tartes de pâtissier.",
  ["4|jaunes d'œufs|Jaune d'œuf|2", f"160 g|de sucre|{SUCRE}|2", f"200 g|de beurre demi-sel mou|{BEURRE}|3", f"230 g|de farine|{F55}|3", f"10 g|de levure chimique|{LEVC}|1"],
  ["**Pâte.** Jaunes + sucre blanchis, beurre, farine + levure : pâte très molle. 1 h au frais.", "**Former.** Boudin, rondelles de 1 cm dans des cercles beurrés.", "**Cuire.** 15-18 min à 170 °C, dorés."],
  keep="2 semaines en boîte.", age=1, cats=["enfants"], profil=["sucre", "gras"])

K("tuiles_amandes", "Tuiles aux amandes", "Tuile aux amandes", IDF, "G", 1, 25, 15, 10, "€", "Plaque, rouleau à pâtisserie (pour la forme).",
  "Biscuits très fins et croustillants, courbés à la sortie du four : idéals avec une glace ou une mousse.",
  ["2|blancs d'œufs|Blanc d'œuf|2", f"80 g|de sucre|{SUCRE}|2", f"30 g|de farine|{F55}|1", f"30 g|de beurre fondu|{BEURRE}|1", "80 g|d'amandes effilées|Amande (entière, effilée, poudre)|3"],
  ["**Pâte.** Blancs + sucre sans fouetter, farine, beurre, amandes.", "**Étaler.** Petits tas aplatis à la fourchette, très fins.", "**Cuire.** 6-8 min à 180 °C ; aussitôt posées sur un rouleau pour les courber."],
  age=3, cats=["zero_dechet"], profil=["sucre"])

K("quatre_quarts", "Quatre-quarts breton", "Quatre-quarts", "France › Bretagne", "G", 1, 8, 10, 45, "€", "Moule à cake.",
  "Quatre ingrédients à poids égal : œufs, beurre, sucre, farine. Simple, moelleux, parfait pour le goûter.",
  [f"4|œufs (environ 220 g)|{OEUF}|3", f"220 g|de beurre demi-sel fondu|{BEURRE}|3", f"220 g|de sucre|{SUCRE}|2", f"220 g|de farine|{F55}|2", f"1 c. à c.|de levure chimique|{LEVC}|0"],
  ["**Mélanger.** Jaunes + sucre, beurre, farine + levure ; blancs montés incorporés.", "**Cuire.** 45 min à 170 °C."],
  age=1, cats=["enfants"], profil=["sucre", "gras"])

K("gateau_nantais", "Gâteau nantais", "Gâteau nantais", "France › Pays de la Loire › Nantes", "G", 1, 8, 15, 40, "€", "Moule à manqué.",
  "Un gâteau dense aux amandes, imbibé et glacé : version sans alcool au sirop d'orange.",
  [f"125 g|de beurre mou|{BEURRE}|2", f"150 g|de sucre|{SUCRE}|2", "125 g|de poudre d'amande|Farine d'amande / poudre d'amande|3", f"3|œufs|{OEUF}|2", f"40 g|de farine|{F55}|1", f"1|orange (jus et zeste)|Orange|2", "100 g|de sucre glace (glaçage)|Sucre glace|1"],
  ["**Pâte.** Beurre + sucre, amande, œufs un à un, farine, zeste.", "**Cuire.** 40 min à 170 °C.", "**Imbiber et glacer.** Jus d'orange tiède sur gâteau chaud ; refroidi, glaçage sucre glace + 2 c. à s. de jus."],
  age=1, cats=["enfants"], profil=["sucre"])

K("crepes_suzette", "Crêpes Suzette", "Crêpes Suzette", IDF, "D", 2, 4, 20, 10, "€€", "Grande poêle.",
  "Crêpes pliées en quatre dans un beurre d'orange caramélisé : flambées au Grand Marnier, ou nappées d'un sirop d'orange épicé.",
  ["8|crêpes (recette liée)|SUB:crepes_bretonnes|3", f"3|oranges (jus et zeste)|Orange|3", f"60 g|de beurre|{BEURRE}|2", f"60 g|de sucre|{SUCRE}|2", "4 cl|de Grand Marnier|Grand Marnier / Cointreau / triple sec|1"],
  ["**Beurre Suzette.** Sucre caramélisé blond, beurre, zeste et jus : réduis jusqu'à sirop.", "**Crêpes.** Pliées en quatre dans la poêle, retournées dans le sirop.", "**Flamber.** Liqueur chauffée, flambée hors de la hotte (ou version sans alcool)."],
  var=[("Sans alcool", ["alcohol"], {"Grand Marnier / Cointreau / triple sec": [("Orange", 0.5), ("Vanille (gousse)", 0.1), ("Cardamome", 0.1)]},
        "Grand Marnier → **zeste d'orange supplémentaire + 2 graines de cardamome écrasées + ½ gousse de vanille** infusés dans le sirop : l'amertume parfumée de la liqueur. Pas de flambage. **À tester**.")],
  age=None, kids="✓ dès 3 ans en version sans alcool.", fetes=["Chandeleur"], profil=["sucre"])

K("pain_epices", "Pain d'épices au miel", "Pain d'épices", "France › Bourgogne-Franche-Comté › Dijon", "G", 1, 10, 15, 60, "€", "Moule à cake.",
  "Moelleux, sombre, parfumé au miel et aux épices ; meilleur après 2 jours.",
  [f"250 g|de miel|{MIEL}|3", f"250 g|de farine (moitié seigle si possible)|{F55}|3", f"15 cl|de lait|{LAIT}|2", "50 g|de cassonade|Sucre blanc / roux / cassonade / vergeoise|1", f"1|œuf|{OEUF}|1", "1 sachet|de bicarbonate (1 c. à c.)|Bicarbonate de soude|1", "2 c. à c.|de mélange quatre-épices + cannelle + anis|Quatre-épices|2", "1|zeste d'orange|Orange|1"],
  ["**Fondre.** Miel, lait, sucre tièdes.", "**Mélanger.** Farine, bicarbonate, épices ; liquide, œuf, zeste.", "**Cuire.** 1 h à 160 °C. Emballe dans un film une fois tiède."],
  keep="2 semaines emballé.", age=1, cats=["enfants"], fetes=["Noël"], profil=["sucre"], kids="✓ dès 1 an (miel cuit, mais dès 1 an par prudence).")

K("bugnes", "Bugnes lyonnaises", "Bugne", "France › Auvergne-Rhône-Alpes › Lyon", "G", 2, 30, 30, 60, "€", "Rouleau, roulette, friteuse.",
  "Beignets fins et croustillants de Mardi gras, saupoudrés de sucre glace.",
  [f"250 g|de farine|{F55}|3", f"2|œufs|{OEUF}|2", f"50 g|de beurre mou|{BEURRE}|1", f"30 g|de sucre|{SUCRE}|1", f"1 c. à c.|de levure chimique|{LEVC}|0", "1|zeste de citron + 1 c. à s. de fleur d'oranger|Eau de fleur d'oranger|1", "1 L|d'huile de friture|Huile d'arachide|1", "2 c. à s.|de sucre glace|Sucre glace|1"],
  ["**Pâte.** Tout mélanger, 1 h de repos.", "**Découper.** Étale à 2 mm, losanges, fente au centre, passe un coin dedans.", "**Frire.** 1 min par face à 180 °C, sucre glace."],
  age=3, cats=["enfants"], fetes=["Chandeleur"], profil=["sucre", "gras"], tech=["Frire"])
