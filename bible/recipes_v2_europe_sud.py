# -*- coding: utf-8 -*-
"""Vague 2 · Europe du Sud : Italie, Espagne, Portugal, Grèce."""
from recipes_v2_base import *

M = "Europe du Sud"

K("spaghetti_aglio_olio", "Spaghetti aglio, olio e peperoncino", "Spaghetti aglio, olio e peperoncino", f"{M} › Italie › Campanie", "P", 1, 4, 10, 12, "€", "Grande casserole, poêle.",
  "Ail doré, huile d'olive, piment et persil : le plat de minuit italien, prêt en 15 minutes.",
  [f"400 g|de spaghetti|{PATES}|3", f"6 gousses|d'ail|{AIL}|3", f"8 c. à s.|d'huile d'olive|{HO}|3", f"1|piment sec ou frais|{PIMENT}|1", f"1 bouquet|de persil|{PERSIL}|1", f"1 c. à s.|de gros sel (eau)|{SEL}|0"],
  ["**Pâtes.** Eau très salée, spaghetti al dente ; garde une louche d'eau de cuisson.", "**Ail.** Lamelles d'ail et piment dans l'huile froide, feu doux : blond, jamais brun.",
   "**Lier.** Pâtes + eau de cuisson dans la poêle, saute 1 min : l'huile devient crémeuse. Persil."],
  age=3, cats=["enfants"], profil=["gras", "epice"], kids="✓ dès 3 ans sans piment.")

K("cacio_e_pepe", "Pâtes cacio e pepe", "Cacio e pepe", f"{M} › Italie › Latium", "P", 2, 4, 10, 12, "€€", "Casserole, poêle, bol.",
  "Pecorino, poivre noir grillé et eau des pâtes : trois ingrédients, une crème soyeuse.",
  [f"400 g|de spaghetti ou tonnarelli|{PATES}|3", "150 g|de pecorino romano finement râpé|Pecorino|3", f"2 c. à c.|de poivre noir concassé|{POIVRE}|2"],
  ["**Pâtes.** Cuis dans peu d'eau peu salée (le pecorino est salé). Garde 30 cl d'eau.", "**Poivre.** Toaste-le 1 min à sec dans la poêle, ajoute une louche d'eau.",
   "**Crème.** Bol : pecorino + un peu d'eau tiède (pas bouillante) → pâte lisse.", "**Lier.** Pâtes dans la poêle hors du feu, crème de pecorino, remue vite en ajoutant de l'eau jusqu'à ce que ce soit nappant."],
  age=3, profil=["gras"])

K("pates_pesto", "Pesto alla genovese maison", "Pesto genovese", f"{M} › Italie › Ligurie", "S", 1, 4, 10, 0, "€€", "Mortier ou mixeur (bol froid).",
  "Basilic, pignons, ail, parmesan, pecorino et huile d'olive : un vert vif quand il est fait minute.",
  ["60 g|de basilic (feuilles)|Basilic|3", "30 g|de pignons|Pignons de pin|2", f"1 gousse|d'ail|{AIL}|1", f"40 g|de parmesan|{PARM}|2", "20 g|de pecorino|Pecorino|1", f"10 cl|d'huile d'olive douce|{HO}|2", f"1 pincée|de gros sel|{SEL}|0"],
  ["**Piler.** Ail et sel, puis basilic par poignées en tournant, pignons.", "**Finir.** Fromages, puis l'huile en filet. Au mixeur : à-coups courts, bol passé au froid, pour ne pas noircir le basilic."],
  keep="3 jours au frigo sous une couche d'huile ; 3 mois congelé en glaçons.", age=1, cats=["sauces", "enfants"], profil=["gras"])

K("risotto_champignons", "Risotto aux champignons", "Risotto ai funghi", f"{M} › Italie › Lombardie", "P", 2, 4, 35, 0, "€€", "Sauteuse, casserole (bouillon).",
  "Riz crémeux nappé de parmesan et de champignons dorés : le secret est de remuer et d'ajouter le bouillon peu à peu.",
  ["320 g|de riz à risotto|Riz à risotto (arborio, carnaroli)|3", "400 g|de champignons (Paris et pleurotes)|Champignon de Paris|3", f"1,2 L|de bouillon de volaille chaud|{BOUILLON}|2", f"1|échalote|{ECH}|1",
   f"10 cl|de vin blanc|Vin blanc|1", f"60 g|de parmesan|{PARM}|2", f"50 g|de beurre|{BEURRE}|2", f"1 c. à s.|de persil|{PERSIL}|0"],
  ["**Champignons.** Dore-les à feu vif avec un peu de beurre ; réserve.", "**Nacrer.** Échalote fondue, riz 2 min jusqu'à ce qu'il soit translucide. Vin, laisse évaporer.",
   "**Cuire.** Bouillon louche par louche en remuant, 18 min : le riz est tendre avec un cœur légèrement ferme.", "**Mantecare.** Hors du feu, beurre froid et parmesan, remue vivement, couvre 2 min. Champignons et persil."],
  var=[("Sans alcool", ["alcohol"], {"Vin blanc": [("Jus de citron (bouteille)", 0.1), ("Bouillon d'os maison (bœuf/volaille)", 0.9)]}, "Vin blanc → **bouillon + 1 c. à s. de jus de citron** (acidité). **À tester**.")],
  age=1, cats=["enfants"], profil=["gras"], kids="✓ dès 1 an en version sans alcool.")

K("lasagnes_bolognaise", "Lasagnes à la bolognaise", "Lasagne alla bolognese", f"{M} › Italie › Émilie-Romagne", "P", 2, 8, 45, 150, "€€", "Cocotte, casserole, plat à gratin.",
  "Ragù mijoté longuement, béchamel, pâtes et parmesan : on prend le temps du dimanche, le reste est simple.",
  [f"600 g|de bœuf haché|{HACHE}|3", "250 g|de lasagnes|Lasagnes|3", f"800 g|de tomates pelées|{PELEES}|2", f"1|carotte|{CAROTTE}|1", "1|branche de céleri|Céleri-branche|1", f"1|oignon|{OIG}|1",
   f"25 cl|de lait (ragù)|{LAIT}|1", f"60 cl|de lait (béchamel)|{LAIT}|2", f"60 g|de beurre + 60 g de farine|{BEURRE}|2", f"100 g|de parmesan|{PARM}|2", f"1 pincée|de muscade|{MUSC}|0"],
  ["**Ragù.** Carotte, céleri, oignon hachés fins 10 min ; viande jusqu'à ce qu'elle grésille ; 25 cl de lait, laisse absorber ; tomates. 2 h à feu très doux.",
   "**Béchamel.** Beurre, farine, lait chaud, muscade : nappante.", "**Monter.** Ragù, pâtes, ragù, béchamel, parmesan… 4 couches, finir béchamel-parmesan.", "**Cuire.** 40 min à 180 °C ; 15 min de repos avant de couper."],
  keep="4 jours au frigo ; se congèle en parts.", age=1, cats=["enfants"], profil=["viande_rouge", "gras"], fetes=["Repas de famille"])

K("saltimbocca_dinde", "Saltimbocca de dinde à la sauge", "Saltimbocca alla romana", f"{M} › Italie › Latium", "P", 1, 4, 15, 10, "€€", "Poêle, cure-dents.",
  "Escalopes fines, sauge et jambon cru, dorées et déglacées : version dinde avec viande des Grisons, le saveur est là.",
  ["8|escalopes fines de dinde ou de veau|Dinde (escalope, cuisse, filet)|3", "8 tranches|de viande des Grisons ou jambon cru|Viande des Grisons / bresaola|2", "8|feuilles de sauge|Sauge|2", f"30 g|de beurre|{BEURRE}|2", f"10 cl|de vin blanc ou de bouillon|{BOUILLON}|1", f"1 c. à s.|de farine|{F55}|0"],
  ["**Monter.** Sur chaque escalope : tranche de viande séchée, feuille de sauge, cure-dent.", "**Dorer.** Farine légère côté viande, 2 min par face au beurre.", "**Sauce.** Déglace au bouillon, gratte, réduis 1 min, nappe."],
  age=3, profil=["leger"])

K("caponata", "Caponata sicilienne", "Caponata", f"{M} › Italie › Sicile", "A", 1, 6, 30, 30, "€", "Sauteuse.",
  "Aubergines dorées en aigre-doux avec céleri, olives et câpres : meilleure froide, le lendemain.",
  ["3|aubergines|Aubergine|3", "2|branches de céleri|Céleri-branche|1", f"1|oignon|{OIG}|1", f"300 g|de tomates pelées|{PELEES}|2", "60 g|d'olives vertes|Olives (vertes / noires)|1", "2 c. à s.|de câpres|Câpres|1",
   "4 c. à s.|de vinaigre de vin|Vinaigre de vin rouge / blanc|2", f"2 c. à s.|de sucre|{SUCRE}|1", f"8 c. à s.|d'huile d'olive|{HO}|2", "1 poignée|de basilic|Basilic|1"],
  ["**Aubergines.** En cubes salés 20 min, épongés, dorés à l'huile.", "**Base.** Oignon et céleri 10 min, tomates, olives, câpres, 10 min.", "**Aigre-doux.** Aubergines, vinaigre et sucre, 5 min. Basilic, refroidis."],
  keep="5 jours au frigo.", age=3, profil=["acide", "sucre"], fetes=["Apéritif dînatoire", "Barbecue d'été"])

K("panzanella", "Panzanella toscane", "Panzanella", f"{M} › Italie › Toscane", "E", 1, 4, 20, 20, "€", "Saladier.",
  "La salade anti-gaspi : pain rassis gorgé de jus de tomates, oignon rouge, concombre et basilic.",
  ["300 g|de pain rassis|Pain rassis (réservé)|3", f"6|tomates bien mûres|{TOM}|3", "1|concombre|Concombre|1", "1|oignon rouge|Oignon rouge|1", "1 poignée|de basilic|Basilic|2", f"6 c. à s.|d'huile d'olive|{HO}|2", "2 c. à s.|de vinaigre de vin rouge|Vinaigre de vin rouge / blanc|1", f"1 c. à c.|de sel|{SEL}|0"],
  ["**Jus.** Tomates en morceaux, salées : 15 min, elles rendent leur eau.", "**Pain.** En gros cubes, mélangé aux tomates, huile, vinaigre.", "**Finir.** Concombre, oignon émincé, basilic ; 20 min de repos."],
  age=3, cats=["zero_dechet"], profil=["leger", "acide"], fetes=["Barbecue d'été"])

K("panna_cotta", "Panna cotta vanille, coulis de fruits rouges", "Panna cotta", f"{M} › Italie › Piémont", "D", 1, 6, 15, 240, "€", "Casserole, verrines.",
  "Une crème prise tremblotante, vanillée, et un coulis acidulé : se prépare la veille.",
  [f"50 cl|de crème|{CL}|3", f"60 g|de sucre|{SUCRE}|2", "1|gousse de vanille|Vanille (gousse)|2", "2 g|d'agar-agar (ou 3 feuilles de gélatine de poisson)|Gélatine de bœuf / poisson, agar-agar, pectine|1", "250 g|de fruits rouges|Framboise / mûre / myrtille|2"],
  ["**Crème.** Chauffe crème, sucre, vanille grattée et agar-agar ; bouillir 2 min en fouettant.", "**Prendre.** Verrines, 4 h au frigo.", "**Coulis.** Fruits + 1 c. à s. de sucre mixés, filtrés."],
  age=1, cats=["enfants"], profil=["sucre", "gras"], fetes=["Saint-Valentin"])

K("polpette_sugo", "Boulettes à la sauce tomate (polpette al sugo)", "Polpette al sugo", f"{M} › Italie › Pouilles", "P", 1, 4, 30, 30, "€", "Sauteuse.",
  "Des boulettes moelleuses (grâce au pain trempé) qui mijotent dans la tomate : avec des pâtes ou du pain.",
  [f"500 g|de bœuf haché|{HACHE}|3", "80 g|de mie de pain rassis|Pain rassis (réservé)|2", f"10 cl|de lait|{LAIT}|1", f"1|œuf|{OEUF}|1", f"40 g|de parmesan|{PARM}|1", f"1 bouquet|de persil|{PERSIL}|1", f"700 g|de passata|{PELEES}|3", f"2 gousses|d'ail|{AIL}|1", f"3 c. à s.|d'huile d'olive|{HO}|1", "1 poignée|de basilic|Basilic|1"],
  ["**Boulettes.** Pain trempé dans le lait et pressé, viande, œuf, parmesan, persil, sel : boules de 4 cm, mains mouillées.", "**Sauce.** Ail dans l'huile, passata, basilic, 10 min.",
   "**Mijoter.** Boulettes crues dans la sauce, 20 min à couvert sans remuer les 10 premières minutes."],
  age=1, cats=["enfants", "zero_dechet"], profil=["viande_rouge"])

K("minestrone", "Minestrone", "Minestrone", f"{M} › Italie › Lombardie", "So", 1, 6, 25, 40, "€", "Faitout.",
  "La soupe-plat de tous les légumes du moment, avec haricots et petites pâtes, et une croûte de parmesan qui parfume.",
  [f"2|carottes|{CAROTTE}|2", "2|branches de céleri|Céleri-branche|1", f"1|oignon|{OIG}|1", "2|courgettes|Courgette|2", f"2|pommes de terre|{PDT}|1", "¼|chou vert|Chou vert / frisé / kale|1",
   "250 g|de haricots blancs ou borlotti cuits|Haricots blancs / lingots|2", f"400 g|de tomates pelées|{PELEES}|2", f"100 g|de petites pâtes|{PATES}|1", "1|croûte de parmesan (facultatif)|Parmesan / Parmigiano|1?", f"3 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Base.** Oignon, carotte, céleri 10 min dans l'huile.", "**Légumes.** Le reste en dés, tomates, 1,5 L d'eau, croûte de parmesan ; 25 min.", "**Finir.** Haricots et pâtes 10 min. Filet d'huile au service."],
  age=1, cats=["enfants", "zero_dechet"], profil=["leger"])

K("tortilla_espanola", "Tortilla de patatas", "Tortilla española", f"{M} › Espagne", "P", 2, 6, 20, 35, "€", "Poêle anti-adhésive 24 cm, assiette.",
  "Une omelette épaisse de pommes de terre confites à l'huile et d'oignon, moelleuse à cœur.",
  [f"800 g|de pommes de terre|{PDT}|3", f"6|œufs|{OEUF}|3", f"1|oignon|{OIG}|2", f"25 cl|d'huile d'olive (pour confire, réutilisable)|{HO}|2", f"1 c. à c.|de sel|{SEL}|0"],
  ["**Confire.** Pommes de terre en fines lamelles et oignon 20 min dans l'huile à feu moyen : tendres, peu colorées. Égoutte (garde l'huile).",
   "**Mélanger.** Dans les œufs battus salés, 10 min de repos.", "**Cuire.** Poêle huilée, 4 min à feu moyen ; retourne avec une assiette, 3 min. Cœur juste pris."],
  age=1, cats=["enfants"], profil=["gras"], fetes=["Apéritif dînatoire"], kids="✓ dès 1 an, bien cuite au centre.")

K("gazpacho", "Gaspacho andalou", "Gazpacho", f"{M} › Espagne › Andalousie", "So", 1, 6, 15, 120, "€", "Mixeur.",
  "Une soupe crue et glacée de tomates, poivron, concombre, pain et huile d'olive : l'été en verre.",
  [f"1 kg|de tomates très mûres|{TOM}|3", f"1|poivron vert|{POIVRON}|1", "1|concombre|Concombre|1", f"1 gousse|d'ail|{AIL}|1", "60 g|de pain rassis|Pain rassis (réservé)|1", f"10 cl|d'huile d'olive|{HO}|2", "3 c. à s.|de vinaigre de xérès|Vinaigre de xérès|2", f"1 c. à c.|de sel|{SEL}|0"],
  ["**Mixer.** Tout, très longtemps, jusqu'à lisse et émulsionné (l'huile en dernier).", "**Froid.** 2 h au frigo. Sers avec des petits dés de légumes."],
  age=1, cats=["enfants", "zero_dechet"], profil=["leger", "acide"], fetes=["Barbecue d'été"])

K("paella_valenciana", "Paella au poulet et aux fruits de mer", "Paella", f"{M} › Espagne › Valence", "P", 2, 6, 40, 30, "€€€", "Grande poêle à paella ou sauteuse large.",
  "Un riz rond safrané qui cuit sans remuer et forme une croûte dorée au fond (le socarrat).",
  ["400 g|de riz rond|Riz rond / sushi|3", f"6|cuisses de poulet en morceaux|{CUISSE}|3", "12|gambas|Gambas / bouquet|2", "500 g|de moules|Moules|2", f"1|poivron rouge|{POIVRON}|1", "150 g|de haricots verts plats|Haricots verts|1",
   f"2|tomates râpées|{TOM}|1", "0,2 g|de safran|Safran (pistils)|2", f"1 c. à c.|de paprika fumé|{PFUME}|1", f"1,2 L|de bouillon chaud|{BOUILLON}|2", f"6 c. à s.|d'huile d'olive|{HO}|1", f"1|citron|{CIT}|1"],
  ["**Dorer.** Poulet salé 15 min dans l'huile ; poivron et haricots 5 min ; tomate et paprika.", "**Riz.** Étale-le, bouillon safrané bouillant ; ne remue plus jamais.",
   "**Cuire.** 10 min à feu vif, 8 min à feu doux ; pose gambas et moules à mi-cuisson.", "**Socarrat.** 1 min à feu vif à la fin (ça crépite). Repos 5 min sous un torchon. Citron."],
  age=3, profil=["poisson"], fetes=["Repas de famille", "Barbecue d'été"], sa=["Limonade maison"], a=["Rosé d'Espagne"])

K("patatas_bravas", "Patatas bravas", "Patatas bravas", f"{M} › Espagne › Madrid", "A", 1, 4, 20, 40, "€", "Plaque, casserole.",
  "Des pommes de terre croustillantes, une sauce tomate pimentée au paprika fumé, et un peu d'aïoli.",
  [f"1 kg|de pommes de terre|{PDT}|3", f"4 c. à s.|d'huile d'olive|{HO}|2", f"300 g|de passata|{PELEES}|2", f"2 c. à c.|de paprika fumé|{PFUME}|2", f"1 pincée|de piment|{CAYENNE}|1", f"1 gousse|d'ail|{AIL}|1", "1 c. à s.|de vinaigre de xérès|Vinaigre de xérès|1"],
  ["**Pommes de terre.** Cubes précuits 7 min à l'eau, égouttés et secoués (bords rugueux), huile, sel ; 35 min à 220 °C.", "**Sauce brava.** Ail, paprika, piment 30 s dans l'huile, passata, vinaigre ; 10 min.", "**Servir.** Sauce dessus, aïoli à côté."],
  age=3, profil=["epice"], fetes=["Apéritif dînatoire"])

K("gambas_ajillo", "Gambas al ajillo", "Gambas al ajillo", f"{M} › Espagne › Andalousie", "E", 1, 4, 10, 5, "€€", "Cassolette ou petite poêle.",
  "Crevettes saisies dans l'huile d'olive à l'ail et au piment, à saucer avec du pain.",
  ["400 g|de gambas crues décortiquées|Gambas / bouquet|3", f"8 gousses|d'ail|{AIL}|3", f"15 cl|d'huile d'olive|{HO}|2", f"1|piment sec|{PIMENT}|1", f"1 c. à s.|de persil|{PERSIL}|1", f"1 pincée|de sel|{SEL}|0"],
  ["**Parfumer.** Ail en lamelles et piment dans l'huile, feu moyen jusqu'à blond.", "**Saisir.** Gambas 2 min en retournant : roses et juste fermes. Persil, sel ; servir grésillant."],
  age=3, profil=["poisson", "gras"], fetes=["Apéritif dînatoire"])

K("crema_catalana", "Crème catalane", "Crema catalana", f"{M} › Espagne › Catalogne", "D", 1, 6, 15, 180, "€", "Casserole, ramequins plats, chalumeau ou gril.",
  "Une crème au lait parfumée au citron et à la cannelle, cuite sur le feu, au sucre caramélisé craquant.",
  [f"50 cl|de lait|{LAIT}|3", "5|jaunes d'œufs|Jaune d'œuf|3", f"100 g|de sucre + 6 c. à s. pour caraméliser|{SUCRE}|2", f"20 g|de maïzena|Fécule de maïs (maïzena)|1", f"1|zeste de citron|{CIT}|1", f"1|bâton de cannelle|{CANN}|1"],
  ["**Infuser.** Lait, zeste, cannelle à frémissement, 10 min.", "**Crème.** Jaunes, sucre, maïzena ; verse le lait filtré, épaissis en remuant sans bouillir.", "**Froid.** 3 h. Sucre en couche fine, caramélise au chalumeau."],
  age=1, cats=["enfants"], profil=["sucre"])

K("churros", "Churros et chocolat épais", "Churros con chocolate", f"{M} › Espagne › Madrid", "G", 2, 6, 25, 15, "€", "Poche à douille cannelée, friteuse ou casserole profonde.",
  "Une pâte simple frite en bâtons striés, sucrée-cannelle, à tremper dans un chocolat chaud épais.",
  ["25 cl|d'eau|-|0", f"150 g|de farine|{F55}|3", f"1 pincée|de sel|{SEL}|0", f"60 g|de sucre + 1 c. à c. de cannelle|{SUCRE}|1", "1 L|d'huile de friture|Huile d'arachide|1",
   f"150 g|de chocolat noir|{CHOCO}|2", f"50 cl|de lait|{LAIT}|2", f"1 c. à s.|de maïzena|Fécule de maïs (maïzena)|1"],
  ["**Pâte.** Eau bouillante salée sur la farine, mélange énergiquement : pâte lisse et ferme. Tiédis.", "**Frire.** Pousse des bâtons de 12 cm dans l'huile à 180 °C, 2 min par face.", "**Sucre.** Roule-les dans sucre-cannelle.", "**Chocolat.** Lait + chocolat + maïzena délayée, épaissis 3 min."],
  age=3, cats=["enfants"], profil=["sucre", "gras"], fetes=["Anniversaire"])

K("pasteis_nata", "Pastéis de nata", "Pastel de nata", f"{M} › Portugal › Lisbonne", "G", 2, 12, 30, 20, "€€", "Moule à muffins, casserole, four très chaud.",
  "Flans crémeux dans une pâte feuilletée croustillante, tachetés de brûlé : on les mange tièdes avec de la cannelle.",
  ["1|pâte feuilletée|Pâte feuilletée (prête)|3", f"25 cl|de lait|{LAIT}|2", f"20 cl|de crème|{CL}|2", "4|jaunes d'œufs|Jaune d'œuf|3", f"120 g|de sucre|{SUCRE}|2", f"20 g|de maïzena|Fécule de maïs (maïzena)|1", f"1|zeste de citron + 1 bâton de cannelle|{CIT}|1"],
  ["**Fonds.** Roule la pâte en boudin serré, 12 tranches ; écrase chacune au pouce dans les alvéoles, bords fins.", "**Crème.** Lait, crème, maïzena, sucre, zeste, cannelle épaissis ; hors du feu, les jaunes.",
   "**Cuire.** Remplis aux ¾ ; 15 min à 250 °C (le plus chaud possible) : dessus taché de noir."],
  age=3, profil=["sucre", "gras"], sa=["Café"])

K("bacalhau_bras", "Bacalhau à Brás", "Bacalhau à Brás", f"{M} › Portugal › Lisbonne", "P", 1, 4, 30, 15, "€€", "Grande poêle.",
  "Morue effilochée, allumettes de pommes de terre et oignon, liés aux œufs brouillés, olives et persil.",
  ["400 g|de morue dessalée|Morue salée (dessalage 24-48 h)|3", f"500 g|de pommes de terre (allumettes frites ou paille)|{PDT}|3", f"6|œufs|{OEUF}|2", f"2|oignons|{OIG}|2", f"2 gousses|d'ail|{AIL}|1", "12|olives noires|Olives (vertes / noires)|1", f"6 c. à s.|d'huile d'olive|{HO}|1", f"1 c. à s.|de persil|{PERSIL}|1"],
  ["**Morue.** Pochée 5 min, effilochée.", "**Oignons.** Fondus doucement avec l'ail ; morue 5 min.", "**Lier.** Pommes paille, puis œufs battus hors du feu fort : crémeux, pas secs. Olives, persil."],
  age=1, profil=["poisson"])

K("caldo_verde", "Caldo verde (soupe au chou)", "Caldo verde", f"{M} › Portugal › Minho", "So", 1, 6, 15, 30, "€", "Faitout, mixeur plongeant.",
  "Une soupe de pommes de terre mixée, du chou très finement ciselé et un filet d'huile d'olive. Le chorizo est remplacé par un chorizo de bœuf.",
  [f"800 g|de pommes de terre|{PDT}|3", "300 g|de chou kale ou vert, en chiffonnade très fine|Chou vert / frisé / kale|3", f"1|oignon|{OIG}|1", f"2 gousses|d'ail|{AIL}|1", "100 g|de chorizo de bœuf en rondelles|Chorizo de bœuf ou de volaille|1?", f"4 c. à s.|d'huile d'olive|{HO}|2"],
  ["**Base.** Pommes de terre, oignon, ail dans 1,5 L d'eau salée, 20 min ; mixe.", "**Chou.** Ajoute la chiffonnade 5 min : vert vif.", "**Servir.** Rondelles de chorizo poêlées, huile d'olive."],
  age=1, profil=["leger"])

K("moussaka", "Moussaka", "Mousakás", f"{M} › Grèce", "P", 2, 8, 50, 60, "€€", "Plat à gratin, poêle, casserole.",
  "Aubergines rôties, agneau à la cannelle et tomate, béchamel épaisse dorée : réconfortant et parfumé.",
  ["4|aubergines|Aubergine|3", "700 g|d'agneau ou de bœuf haché|Agneau haché|3", f"400 g|de tomates pelées|{PELEES}|2", f"2|oignons|{OIG}|1", f"1 c. à c.|de cannelle|{CANN}|1", "1 c. à c.|d'origan|Origan frais / sec|1",
   f"60 cl|de lait|{LAIT}|2", f"60 g|de beurre + 60 g de farine|{BEURRE}|2", f"2|jaunes d'œufs|Jaune d'œuf|1", f"60 g|de parmesan ou kefalotyri|{PARM}|1", f"4 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Aubergines.** Tranches huilées, 25 min à 220 °C (pas de friture : plus léger).", "**Viande.** Oignons, viande, cannelle, origan, tomates ; 20 min.", "**Béchamel.** Épaisse, avec jaunes et fromage hors du feu.", "**Monter.** Aubergines, viande, aubergines, béchamel ; 45 min à 180 °C. Repos 20 min."],
  age=1, profil=["viande_rouge", "gras"], fetes=["Repas de famille"])

K("souvlaki_poulet", "Souvlaki de poulet et pita", "Souvlaki", f"{M} › Grèce", "P", 1, 4, 25, 15, "€€", "Brochettes, gril ou poêle-gril.",
  "Brochettes marinées au citron et à l'origan, pita chaude, tzatziki, tomate et oignon rouge.",
  [f"700 g|de blanc ou de haut de cuisse de poulet|{BLANC_P}|3", f"1|citron|{CIT}|2", "2 c. à c.|d'origan|Origan frais / sec|2", f"3 gousses|d'ail|{AIL}|1", f"4 c. à s.|d'huile d'olive|{HO}|1",
   "4|pains pita|Pain pita / libanais|2", f"2|tomates|{TOM}|1", "1|oignon rouge|Oignon rouge|1", "1 bol|de tzatziki (recette liée)|SUB:tzatziki|2"],
  ["**Mariner.** Cubes de poulet, citron, origan, ail, huile, sel ; 1 h minimum.", "**Griller.** En brochettes, 10 min en tournant : bords dorés.", "**Servir.** Pita chaude, poulet, tzatziki, tomate, oignon."],
  age=3, cats=["enfants"], profil=["leger"], fetes=["Barbecue d'été"])

K("salade_grecque", "Salade grecque (horiatiki)", "Horiatikí", f"{M} › Grèce", "E", 1, 4, 15, 0, "€", "Saladier.",
  "Tomates, concombre, poivron, oignon rouge, olives et un bloc de feta à l'origan : sans laitue, comme au village.",
  [f"4|tomates|{TOM}|3", "1|concombre|Concombre|2", f"1|poivron vert|{POIVRON}|1", "1|oignon rouge|Oignon rouge|1", "200 g|de feta en bloc|Feta|3", "12|olives de Kalamata|Olives (vertes / noires)|1", "1 c. à c.|d'origan|Origan frais / sec|1", f"5 c. à s.|d'huile d'olive|{HO}|2"],
  ["**Couper.** Légumes en gros morceaux, sel.", "**Dresser.** Olives, feta entière dessus, origan, huile généreuse. Le jus au fond se saucé avec du pain."],
  age=1, cats=["enfants"], profil=["leger"], fetes=["Barbecue d'été"])

K("spanakopita", "Spanakopita (feuilleté épinards-feta)", "Spanakópita", f"{M} › Grèce", "P", 2, 8, 30, 45, "€€", "Plat à four, pinceau.",
  "Épinards, feta et herbes entre des couches de filo dorées au beurre : croustillant et fondant.",
  ["1 kg|d'épinards frais (ou 600 g surgelés)|Épinard|3", "250 g|de feta|Feta|3", "12|feuilles de filo|Pâte filo / feuilles de brick|3", "4|oignons nouveaux|Oignon nouveau / cébette|1", "1 bouquet|d'aneth|Aneth|1", f"2|œufs|{OEUF}|1", f"80 g|de beurre fondu|{BEURRE}|2"],
  ["**Farce.** Épinards fondus et bien pressés, oignons, aneth, feta émiettée, œufs, poivre.", "**Monter.** 6 feuilles beurrées, farce, 6 feuilles beurrées ; prédécoupe en parts.", "**Cuire.** 45 min à 180 °C, bien doré."],
  age=1, cats=["enfants"], profil=["gras"], fetes=["Apéritif dînatoire"])

K("yaourt_miel_noix", "Yaourt grec, miel et noix", "Giaoúrti me méli", f"{M} › Grèce", "D", 1, 4, 5, 0, "€", "Bols.",
  "Le dessert le plus simple de Grèce : un yaourt épais, un miel de thym et des noix grillées.",
  [f"500 g|de yaourt grec|{GREC}|3", f"4 c. à s.|de miel|{MIEL}|3", "60 g|de noix|Noix|2"],
  ["**Noix.** Grille-les 3 min à sec.", "**Servir.** Yaourt, miel en filet, noix concassées."],
  age=1, cats=["enfants"], profil=["sucre"], kids="✓ dès 1 an (miel interdit avant 1 an).")
