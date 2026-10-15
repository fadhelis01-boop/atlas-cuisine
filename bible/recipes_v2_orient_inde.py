# -*- coding: utf-8 -*-
"""Vague 2 · Moyen-Orient & Caucase, Asie du Sud."""
from recipes_v2_base import *

MO = "Moyen-Orient & Caucase"; AS = "Asie du Sud"

K("falafels", "Falafels croustillants", "Falafel", f"{MO} › Liban", "P", 2, 4, 25, 15, "€", "Mixeur, poêle profonde.",
  "Pois chiches crus trempés (jamais cuits), herbes et épices, frits : croustillants dehors, verts et moelleux dedans.",
  [f"250 g|de pois chiches secs trempés 24 h|{POIS}|3", f"1 bouquet|de persil + 1 de coriandre|{PERSIL}|2", f"1|oignon|{OIG}|1", f"4 gousses|d'ail|{AIL}|1", f"2 c. à c.|de cumin + 1 de coriandre moulue|{CUMIN}|2", "½ c. à c.|de bicarbonate|Bicarbonate de soude|1", "1 c. à s.|de sésame|Sésame (blanc/noir)|0", "75 cl|d'huile de friture|Huile de tournesol / colza|1"],
  ["**Mixer.** Pois chiches égouttés crus, herbes, oignon, ail, épices, sel : semoule humide, pas une purée. 1 h au frais.", "**Former.** Bicarbonate, boulettes de 4 cm tassées, sésame.", "**Frire.** 4 min à 175 °C. Avec pita, tahini, salade."],
  age=3, cats=["enfants"], profil=["epice"], tips=["Pois chiches cuits ou en bocal : les falafels se défont."])

K("sauce_tahini", "Sauce tahini citronnée", "Tarator", f"{MO} › Liban", "S", 1, 6, 5, 0, "€", "Bol, fouet.",
  "Purée de sésame, citron, ail et eau glacée : elle blanchit et devient crémeuse en fouettant.",
  ["100 g|de tahini|Tahini (purée de sésame)|3", f"1|citron|{CIT}|2", f"1 gousse|d'ail|{AIL}|1", "8 cl|d'eau glacée|-|0", f"1 pincée|de sel|{SEL}|0"],
  ["**Fouetter.** Tahini + citron (ça épaissit, c'est normal), puis l'eau glacée peu à peu : crème lisse et pâle."],
  keep="5 jours au frigo.", age=1, cats=["sauces"], profil=["gras"], tips=["⚠️ Sésame : allergène."])

K("fattouche", "Fattouche", "Fattoush", f"{MO} › Liban", "E", 1, 4, 15, 10, "€", "Saladier, four.",
  "Salade croquante au pain pita grillé, au sumac et à la mélasse de grenade : anti-gaspi et acidulée.",
  ["2|pains pita rassis|Pain pita / libanais|3", "1|laitue romaine|Salade (laitue, batavia)|2", f"3|tomates|{TOM}|2", "1|concombre|Concombre|2", "6|radis|Radis rose|1", "1 bouquet|de menthe et persil|Menthe|1", "2 c. à c.|de sumac|Sumac|2", f"1|citron|{CIT}|1", "1 c. à s.|de mélasse de grenade (facultatif)|Mélasse de grenade|1?", f"6 c. à s.|d'huile d'olive|{HO}|2"],
  ["**Pain.** En carrés, huilés, 8 min à 200 °C.", "**Salade.** Légumes en morceaux, herbes.", "**Assaisonner.** Citron, mélasse, sumac, huile ; pain au dernier moment."],
  age=3, cats=["zero_dechet"], profil=["leger", "acide"], fetes=["Ramadan / Aïd"])

K("chich_taouk", "Chich taouk (brochettes de poulet)", "Shish tawook", f"{MO} › Liban", "P", 1, 4, 20, 15, "€€", "Brochettes, gril.",
  "Poulet mariné au yaourt, citron, ail et paprika, grillé ; avec une crème d'ail (toum) et des frites.",
  [f"700 g|de blanc ou haut de cuisse de poulet|{BLANC_P}|3", f"150 g|de yaourt|{YAO}|2", f"1|citron|{CIT}|2", f"4 gousses|d'ail|{AIL}|2", f"1 c. à s.|de concentré de tomate|{CONC}|1", f"1 c. à c.|de paprika|{PAPRIKA}|1", f"3 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Mariner.** Tout, 4 h (ou une nuit).", "**Griller.** En brochettes, 12 min."], age=1, cats=["enfants"], fetes=["Barbecue d'été"], profil=["leger"])

K("toum", "Toum (crème d'ail libanaise)", "Toum", f"{MO} › Liban", "S", 2, 10, 15, 0, "€", "Mixeur ou robot.",
  "Une émulsion d'ail, citron et huile, sans œuf, blanche et ferme comme une mayonnaise.",
  [f"1 tête|d'ail (gousses dégermées)|{AIL}|3", f"1|citron|{CIT}|2", f"30 cl|d'huile neutre|{HN}|3", f"1 c. à c.|de sel|{SEL}|0"],
  ["**Mixer.** Ail + sel en pâte.", "**Monter.** Huile en filet très fin, en alternant avec le citron et 2 c. à s. d'eau glacée : elle devient blanche et ferme."],
  keep="1 mois au frigo.", age=3, cats=["sauces"], profil=["gras"], tech=["Émulsionner"])

K("moutabal", "Moutabal (caviar d'aubergine au tahini)", "Mutabbal", f"{MO} › Liban", "E", 1, 6, 15, 40, "€", "Four ou flamme, fourchette.",
  "Aubergines grillées jusqu'à fumer, écrasées avec tahini, citron et ail : fumé et crémeux.",
  ["3|aubergines|Aubergine|3", "3 c. à s.|de tahini|Tahini (purée de sésame)|2", f"1|citron|{CIT}|2", f"1 gousse|d'ail|{AIL}|1", f"3 c. à s.|d'huile d'olive|{HO}|1", "1|grenade (graines)|Grenade|1?"],
  ["**Griller.** Aubergines piquées directement sur la flamme ou sous le gril 30-40 min : peau noire.", "**Écraser.** Chair égouttée, tahini, citron, ail, sel.", "**Servir.** Huile, grenade."],
  keep="4 jours au frigo.", age=1, cats=["enfants"], fetes=["Apéritif dînatoire"], profil=["leger"])

K("kebbe_four", "Kebbé au four", "Kibbeh bil sanieh", f"{MO} › Liban", "P", 2, 8, 40, 40, "€€", "Plat à four.",
  "Deux couches de boulgour et viande, farcies d'agneau aux oignons et pignons, cuites au four : la version facile du kebbé.",
  ["250 g|de boulgour fin|Boulgour fin|3", "700 g|d'agneau ou bœuf haché|Agneau haché|3", f"2|oignons|{OIG}|2", "50 g|de pignons|Pignons de pin|1", "1 c. à c.|de baharat ou de sept-épices|Baharat / tabil|2", f"1 c. à c.|de cannelle|{CANN}|1", f"10 cl|d'huile d'olive|{HO}|1"],
  ["**Pâte.** Boulgour trempé 15 min, pressé, mixé avec 400 g de viande, 1 oignon, épices.", "**Farce.** Reste de viande, oignon, pignons, épices, 10 min.", "**Monter.** Couche, farce, couche ; losanges, huile.", "**Cuire.** 40 min à 190 °C. Avec yaourt."],
  age=1, profil=["viande_rouge"], fetes=["Repas de famille"])

K("mujaddara", "Mujaddara (lentilles, riz et oignons frits)", "Mujaddara", f"{MO} › Liban", "P", 1, 4, 15, 40, "€", "Cocotte, poêle.",
  "Lentilles et riz au cumin, couronnés d'oignons frits croustillants : un plat pauvre devenu culte.",
  ["200 g|de lentilles vertes|Lentilles vertes / brunes|3", f"150 g|de riz|{RIZ}|2", f"4|oignons|{OIG}|3", f"2 c. à c.|de cumin|{CUMIN}|2", f"10 cl|d'huile d'olive|{HO}|2"],
  ["**Oignons.** En fines lamelles, frits 20 min jusqu'à brun foncé et croustillants.", "**Lentilles.** 15 min dans l'eau.", "**Riz.** Ajouté avec cumin et un peu d'huile des oignons, eau à hauteur, 15 min couvert.", "**Servir.** Oignons dessus, yaourt ou salade."],
  age=1, cats=["enfants"], profil=["leger"])

K("manakish_zaatar", "Manakish au zaatar", "Man'ouché", f"{MO} › Liban", "Pa", 1, 6, 20, 90, "€", "Plaque, four très chaud.",
  "Galettes de pâte à pain couvertes de zaatar à l'huile d'olive : le petit-déjeuner libanais.",
  [f"400 g|de farine|{F55}|3", f"7 g|de levure|{LEV}|1", "25 cl|d'eau tiède|-|0", "6 c. à s.|de zaatar maison|SUB:zaatar_maison|3", f"10 cl|d'huile d'olive|{HO}|2"],
  ["**Pâte.** Farine, levure, sel, eau, 2 c. à s. d'huile ; pousse 1 h.", "**Étaler.** 6 galettes de 3 mm ; zaatar mélangé au reste d'huile, du bout des doigts.", "**Cuire.** 6-8 min à 250 °C. Avec tomate, concombre, labneh."],
  age=1, cats=["pains", "enfants"], profil=["gras"])

K("halloumi_pasteque", "Halloumi grillé, pastèque et menthe", "Halloumi with watermelon", f"{MO} › Chypre", "E", 1, 4, 10, 5, "€€", "Poêle.",
  "Fromage grillé salé et pastèque glacée, menthe et citron vert : le contraste parfait de l'été.",
  ["250 g|de halloumi|Halloumi|3", "600 g|de pastèque|Melon / pastèque|3", "10|feuilles de menthe|Menthe|2", f"1|citron vert|{CITV}|1", f"2 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Griller.** Tranches de halloumi à sec, 2 min par face, dorées.", "**Dresser.** Pastèque en cubes, halloumi chaud, menthe, citron vert, huile, poivre."],
  age=1, fetes=["Barbecue d'été"], profil=["leger"])

K("baklava_maison", "Baklava aux noix et pistaches", "Baklava", f"{MO} › Turquie › Gaziantep", "G", 2, 30, 40, 50, "€€", "Plat à four, pinceau.",
  "Feuilles de filo beurrées, noix et pistaches, sirop au citron : croustillant, fondant, à préparer la veille.",
  ["20|feuilles de filo|Pâte filo / feuilles de brick|3", "300 g|de noix et pistaches concassées|Pistache|3", f"200 g|de beurre clarifié fondu|{BEURRE}|3", f"1 c. à c.|de cannelle|{CANN}|1", f"300 g|de sucre (sirop)|{SUCRE}|2", f"1|citron|{CIT}|1", f"2 c. à s.|de miel|{MIEL}|1"],
  ["**Monter.** 10 feuilles beurrées une à une, fruits secs cannelle, 10 feuilles beurrées.", "**Découper.** En losanges jusqu'au fond, avant cuisson.", "**Cuire.** 50 min à 170 °C, bien doré.", "**Sirop.** Sucre, 20 cl d'eau, citron, miel, 10 min ; froid sur baklava chaud. Une nuit."],
  keep="1 semaine à température ambiante.", age=3, fetes=["Ramadan / Aïd"], profil=["sucre", "gras"])

K("lahmacun", "Lahmacun (pizza turque)", "Lahmacun", f"{MO} › Turquie", "P", 2, 6, 30, 90, "€", "Plaque, four très chaud.",
  "Pâte très fine couverte d'agneau haché aux tomates, poivrons et herbes : roulée avec persil, oignon et citron.",
  [f"400 g|de farine|{F55}|3", f"7 g|de levure|{LEV}|1", "300 g|d'agneau ou bœuf haché|Agneau haché|3", f"2|tomates|{TOM}|2", f"1|poivron|{POIVRON}|1", f"1|oignon|{OIG}|1", f"1 c. à s.|de concentré|{CONC}|1", "1 c. à c.|de piment doux (pul biber)|Flocons de piment|1", f"1 bouquet|de persil|{PERSIL}|1", f"1|citron|{CIT}|1"],
  ["**Pâte.** Pain classique, 1 h.", "**Garniture.** Viande crue, légumes mixés et égouttés, concentré, épices, persil.", "**Cuire.** Galettes très fines, garniture en couche mince, 6-8 min à 250 °C.", "**Servir.** Persil, oignon, citron, roulé."],
  age=3, cats=["enfants"], profil=["viande_rouge"])

K("menemen", "Menemen", "Menemen", f"{MO} › Turquie", "P", 1, 2, 10, 15, "€", "Poêle.",
  "Œufs brouillés dans des tomates et poivrons fondus au beurre : le petit-déjeuner turc, à saucer.",
  [f"4|œufs|{OEUF}|3", f"3|tomates|{TOM}|3", f"2|poivrons verts|{POIVRON}|2", f"20 g|de beurre|{BEURRE}|1", "1 pincée|de flocons de piment|Flocons de piment|1", "40 g|de feta (facultatif)|Feta|1?"],
  ["**Fondre.** Poivrons au beurre 5 min, tomates râpées 8 min.", "**Œufs.** Battus, versés, remués doucement juste jusqu'à crémeux."],
  age=1, cats=["enfants"], profil=["leger"])

K("chelo_tahdig", "Riz persan au tahdig", "Chelow ba tahdig", f"{MO} › Iran", "A", 2, 6, 20, 70, "€", "Cocotte anti-adhésive, torchon.",
  "Un riz basmati safrané, léger et parfumé, avec une croûte dorée et croustillante au fond : le trésor de la table iranienne.",
  [f"400 g|de riz basmati|{RIZ}|3", "1 pincée|de safran infusé|Safran (pistils)|2", f"60 g|de beurre ou ghee|{BEURRE}|2", f"2 c. à s.|de yaourt|{YAO}|1", f"2 c. à s.|d'huile|{HN}|1", "1 c. à s.|de gros sel|Sel fin / gros sel / fleur de sel|0"],
  ["**Précuire.** Riz trempé 1 h, 6 min dans beaucoup d'eau salée bouillante, égoutté.", "**Tahdig.** Fond de cocotte : huile, beurre, 3 louches de riz mêlées au yaourt et au safran, tassées.",
   "**Vapeur.** Reste du riz en dôme, trous au manche ; couvercle enveloppé d'un torchon ; 10 min feu moyen puis 45 min feu doux.", "**Démouler.** Retourne : la croûte dorée dessus."],
  age=1, cats=["enfants"], fetes=["Repas de famille", "Nouvel An"], profil=["gras"])

K("khoresh_karafs", "Ragoût d'agneau aux herbes (ghormeh sabzi simplifié)", "Ghormeh sabzi", f"{MO} › Iran", "P", 2, 6, 30, 150, "€€", "Cocotte.",
  "Agneau, haricots rouges et une montagne d'herbes revenues, citron séché : un ragoût vert profond, acidulé.",
  ["800 g|d'agneau en cubes|Épaule d'agneau|3", "250 g|de haricots rouges cuits|Haricots rouges / noirs|2", f"2 bouquets|de persil|{PERSIL}|3", f"1 bouquet|de coriandre|{CORI}|2", "1 bouquet|de ciboulette + quelques feuilles de fenugrec|Ciboulette|2", f"1|oignon|{OIG}|1", f"1 c. à c.|de curcuma|{CURC}|1", f"2|citrons verts (ou citrons séchés)|{CITV}|2", f"5 c. à s.|d'huile|{HN}|1"],
  ["**Herbes.** Hachées, revenues 15 min dans l'huile jusqu'à vert foncé (c'est le goût du plat).", "**Viande.** Oignon, curcuma, agneau doré, eau à hauteur, 1 h.", "**Mijoter.** Herbes, haricots, citrons percés ; 1 h. Avec chelo."],
  age=1, profil=["acide"])

K("khachapuri", "Khachapuri (pain au fromage géorgien)", "Khachapuri adjarouli", f"{MO} › Géorgie", "Pa", 2, 4, 30, 90, "€€", "Plaque, four.",
  "Barques de pâte à pain remplies de fromage fondu, avec un jaune d'œuf et du beurre mélangés à table.",
  [f"400 g|de farine|{F55}|3", f"7 g|de levure|{LEV}|1", f"25 cl|de lait tiède|{LAIT}|1", "250 g|de mozzarella râpée|Mozzarella / burrata|3", "200 g|de feta|Feta|2", "4|jaunes d'œufs|Jaune d'œuf|2", f"40 g|de beurre|{BEURRE}|1"],
  ["**Pâte.** Pain au lait, pousse 1 h.", "**Barques.** Ovales, bords roulés et pincés aux extrémités, garnis de fromages mélangés.", "**Cuire.** 15 min à 230 °C ; jaune au centre, 2 min ; beurre. On mélange et on trempe les bords."],
  age=None, kids="✓ dès 3 ans avec le jaune bien cuit.", profil=["gras"])

K("butter_chicken", "Poulet au beurre (butter chicken)", "Murgh makhani", f"{AS} › Inde › Delhi", "P", 1, 6, 30, 40, "€€", "Four ou poêle, cocotte, mixeur.",
  "Poulet tandoori dans une sauce tomate-beurre-crème douce et parfumée : le curry préféré des enfants.",
  [f"1 kg|de hauts de cuisse de poulet|{CUISSE}|3", "1|recette de marinade tandoori|SUB:marinade_tandoori|2", f"800 g|de tomates pelées|{PELEES}|3", f"60 g|de beurre|{BEURRE}|2", f"15 cl|de crème|{CL}|2", f"1 morceau|de gingembre + 4 gousses d'ail|{GING}|1", "1 c. à c.|de garam masala|Garam masala|1", "1 c. à s.|de fenugrec séché (kasuri methi)|Fenugrec|1", f"1 c. à c.|de miel|{MIEL}|0"],
  ["**Poulet.** Mariné 4 h, grillé 15 min à 240 °C.", "**Sauce.** Beurre, ail-gingembre, tomates, 20 min ; mixe.", "**Finir.** Crème, garam masala, fenugrec émietté, miel, poulet en morceaux, 10 min. Avec naan et riz."],
  age=1, cats=["enfants"], profil=["gras"], kids="✓ dès 1 an, sans piment.")

K("chana_masala", "Chana masala (curry de pois chiches)", "Chole", f"{AS} › Inde › Pendjab", "P", 1, 4, 15, 30, "€", "Cocotte.",
  "Pois chiches dans une sauce épaisse oignon-tomate épicée, relevée d'amchur (ou citron) : végétal et généreux.",
  [f"500 g|de pois chiches cuits|{POIS}|3", f"2|oignons|{OIG}|2", f"3|tomates|{TOM}|2", f"1 morceau|de gingembre + 3 gousses d'ail|{GING}|1", f"1 c. à c.|de cumin graines|{CUMIN}|1", "1 c. à s.|de garam masala|Garam masala|2", f"½ c. à c.|de curcuma|{CURC}|1", f"1|citron|{CIT}|1", f"1 bouquet|de coriandre|{CORI}|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Base.** Cumin dans l'huile, oignons bien dorés, ail-gingembre, tomates, épices : jusqu'à ce que l'huile ressorte.", "**Mijoter.** Pois chiches, 20 cl d'eau, 15 min ; écrase-en quelques-uns.", "**Finir.** Citron, coriandre."],
  age=1, cats=["enfants"], profil=["epice"])

K("palak_paneer", "Palak paneer", "Palak paneer", f"{AS} › Inde › Pendjab", "P", 1, 4, 20, 20, "€€", "Casserole, mixeur, poêle.",
  "Fromage frais grillé dans une crème d'épinards épicée : vert vif et doux.",
  ["500 g|d'épinards|Épinard|3", "250 g|de paneer en cubes|Paneer|3", f"1|oignon|{OIG}|1", f"2|tomates|{TOM}|1", f"1 morceau|de gingembre + 3 gousses d'ail|{GING}|1", "1 c. à c.|de garam masala|Garam masala|1", f"1 c. à c.|de cumin|{CUMIN}|1", f"5 cl|de crème|{CL}|1", "2 c. à s.|de ghee|Ghee|1"],
  ["**Épinards.** Blanchis 1 min, eau glacée, mixés.", "**Base.** Cumin, oignon, ail-gingembre, tomates, épices.", "**Finir.** Épinards, crème, 5 min ; paneer doré à part, ajouté."],
  age=1, cats=["enfants"], profil=["leger"])

K("paneer_maison", "Paneer maison", "Paneer", f"{AS} › Inde", "Ba", 1, 4, 15, 120, "€", "Casserole, torchon fin, poids.",
  "Un fromage frais ferme, fait avec du lait et du citron : il ne fond pas à la cuisson.",
  [f"2 L|de lait entier|{LAIT}|3", f"2|citrons (jus)|{CIT}|2"],
  ["**Cailler.** Lait à ébullition, hors du feu le jus de citron en remuant : le lait se sépare en caillé et petit-lait vert.", "**Égoutter.** Dans un torchon, rince, presse 2 h sous un poids."],
  keep="4 jours au frigo dans l'eau.", age=1, cats=["zero_dechet"], profil=["leger"], tips=["Le petit-lait : pour la pâte à pain, les soupes, ou cuire le riz."])

K("aloo_gobi", "Aloo gobi (chou-fleur et pommes de terre)", "Aloo gobi", f"{AS} › Inde › Pendjab", "A", 1, 4, 15, 30, "€", "Sauteuse avec couvercle.",
  "Chou-fleur et pommes de terre rôtis aux épices et au curcuma, dorés, juste tendres.",
  ["1|chou-fleur|Chou-fleur|3", f"3|pommes de terre|{PDT}|2", f"1|oignon|{OIG}|1", f"1 c. à c.|de cumin graines|{CUMIN}|1", f"1 c. à c.|de curcuma|{CURC}|2", "1 c. à c.|de garam masala|Garam masala|1", f"1 morceau|de gingembre|{GING}|1", f"4 c. à s.|d'huile|{HN}|1", f"1 bouquet|de coriandre|{CORI}|1"],
  ["**Épices.** Cumin, oignon, gingembre, curcuma.", "**Cuire.** Légumes en morceaux, sel, couvert 15 min, puis découvert 10 min pour dorer. Garam masala, coriandre."],
  age=1, cats=["enfants"], profil=["leger"])

K("biryani_poulet", "Biryani de poulet", "Biryani", f"{AS} › Inde › Hyderabad", "P", 3, 6, 50, 60, "€€", "Grande cocotte, papier aluminium.",
  "Poulet mariné aux épices et riz basmati parfumé, cuits ensemble en couches à l'étouffée, oignons frits, safran et menthe.",
  [f"1 kg|de poulet en morceaux|{CUISSE}|3", f"500 g|de riz basmati|{RIZ}|3", f"200 g|de yaourt|{YAO}|2", f"4|oignons|{OIG}|2", "1 c. à s.|de garam masala|Garam masala|2", "1 c. à c.|de cardamome, cannelle, girofle entiers|Cardamome|1", "1 pincée|de safran dans 5 cl de lait|Safran (pistils)|1", "1 bouquet|de menthe et coriandre|Menthe|1", f"1 morceau|de gingembre + 6 gousses d'ail|{GING}|1", "4 c. à s.|de ghee|Ghee|1"],
  ["**Mariner.** Poulet, yaourt, ail-gingembre, garam masala, sel, 2 h.", "**Oignons.** Frits jusqu'à bruns.", "**Riz.** Trempé 30 min, cuit 5 min dans l'eau bouillante salée aux épices entières (aux ⅔).",
   "**Monter.** Poulet cru mariné au fond, la moitié des oignons et herbes, riz, lait safrané, ghee, reste des oignons.", "**Dum.** Couvercle scellé à l'aluminium, 10 min feu moyen, 35 min feu très doux. Repos 10 min."],
  age=1, fetes=["Ramadan / Aïd", "Repas de famille"], profil=["epice"])

K("samoussas_legumes", "Samoussas aux légumes (au four)", "Samosa", f"{AS} › Inde", "E", 2, 20, 40, 20, "€", "Poêle, plaque.",
  "Triangles croustillants de brick farcis de pommes de terre épicées et petits pois.",
  [f"500 g|de pommes de terre cuites|{PDT}|3", "150 g|de petits pois|Petits pois / pois gourmands|2", "10|feuilles de brick|Pâte filo / feuilles de brick|3", f"1|oignon|{OIG}|1", f"1 c. à c.|de cumin + 1 de coriandre moulue|{CUMIN}|1", "1 c. à c.|de garam masala|Garam masala|1", f"1|citron|{CIT}|1", f"1 bouquet|de coriandre|{CORI}|1", f"40 g|de beurre fondu|{BEURRE}|1"],
  ["**Farce.** Oignon, épices, pommes de terre en dés, petits pois, citron, coriandre.", "**Plier.** Bandes de brick beurrées, triangles.", "**Cuire.** 20 min à 200 °C. Avec chutney."],
  age=3, cats=["enfants"], fetes=["Diwali", "Ramadan / Aïd", "Apéritif dînatoire"], profil=["epice"])

K("kheer", "Kheer (riz au lait à la cardamome)", "Kheer", f"{AS} › Inde", "D", 1, 6, 10, 45, "€", "Casserole à fond épais.",
  "Riz cuit longuement dans le lait, cardamome, safran, pistaches et amandes : le dessert des fêtes indiennes.",
  [f"1 L|de lait entier|{LAIT}|3", "80 g|de riz basmati|Riz long / basmati / thaï|2", f"80 g|de sucre|{SUCRE}|2", "4|gousses de cardamome|Cardamome|2", "1 pincée|de safran|Safran (pistils)|1", "30 g|de pistaches et amandes|Pistache|1"],
  ["**Cuire.** Riz rincé dans le lait, feu doux, 40 min en remuant souvent, jusqu'à crémeux.", "**Parfumer.** Sucre, cardamome écrasée, safran, 5 min. Fruits secs. Chaud ou froid."],
  age=1, cats=["enfants"], fetes=["Diwali"], profil=["sucre"])

K("chai_masala", "Masala chai", "Masala chai", f"{AS} › Inde", "B", 1, 4, 5, 10, "€", "Casserole, passoire.",
  "Thé noir bouilli avec lait, gingembre et épices : le thé épicé des gares indiennes.",
  ["2 c. à s.|de thé noir (assam)|Thé noir fumé (lapsang)|2", f"40 cl|de lait|{LAIT}|3", f"1 morceau|de gingembre|{GING}|2", "4|gousses de cardamome|Cardamome|2", f"1|bâton de cannelle|{CANN}|1", "2|clous de girofle|Clou de girofle|1", f"3 c. à s.|de sucre|{SUCRE}|1"],
  ["**Infuser.** Épices écrasées et gingembre dans 40 cl d'eau, 5 min.", "**Thé.** Thé, 2 min ; lait et sucre, porte à ébullition 2 fois. Filtre."],
  age=None, kids="Contient de la théine : pour les adultes et ados.", cats=["boissons"], fetes=["Diwali"], profil=["epice"])

K("dosa_simple", "Uttapam (crêpes épaisses de riz et lentilles)", "Uttapam", f"{AS} › Inde › Tamil Nadu", "P", 2, 8, 20, 960, "€", "Mixeur, poêle.",
  "Crêpes épaisses à la pâte fermentée de riz et de lentilles, garnies d'oignon, tomate et coriandre ; sans gluten.",
  ["300 g|de riz rond|Riz rond / sushi|3", "100 g|de lentilles corail (ou urad dal)|Lentilles corail|2", "½ c. à c.|de fenugrec|Fenugrec|1", f"1|oignon|{OIG}|1", f"2|tomates|{TOM}|1", f"1 bouquet|de coriandre|{CORI}|1", f"1|piment vert|{PIMENT}|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Tremper.** Riz et lentilles avec fenugrec 6 h ; mixe avec un peu d'eau en pâte épaisse ; fermente 10-12 h au chaud.", "**Cuire.** Louche épaisse dans la poêle huilée, garniture dessus, 3 min par face. Avec chutney coco."],
  age=1, profil=["leger"], kids="✓ dès 1 an sans piment ; sans gluten.")

K("dal_makhani", "Dal makhani (lentilles noires crémeuses)", "Dal makhani", f"{AS} › Inde › Pendjab", "P", 1, 6, 15, 120, "€", "Cocotte.",
  "Lentilles noires et haricots rouges mijotés longtemps avec beurre, tomate et crème : velouté et fumé.",
  ["250 g|de lentilles beluga (ou urad entières)|Lentilles noires (beluga)|3", "100 g|de haricots rouges cuits|Haricots rouges / noirs|2", f"400 g|de tomates pelées|{PELEES}|2", f"50 g|de beurre|{BEURRE}|2", f"10 cl|de crème|{CL}|2", f"1 morceau|de gingembre + 4 gousses d'ail|{GING}|1", "1 c. à c.|de garam masala|Garam masala|1", f"1 c. à c.|de paprika fumé|{PFUME}|1"],
  ["**Lentilles.** Trempées une nuit, cuites 1 h.", "**Sauce.** Beurre, ail-gingembre, tomates, épices 15 min.", "**Mijoter.** Tout ensemble 45 min en écrasant un peu ; crème. Plus c'est long, meilleur c'est."],
  age=1, cats=["enfants"], profil=["gras"])

K("lassi_sale", "Lassi salé à la menthe et au cumin", "Namkeen lassi", f"{AS} › Inde", "B", 1, 2, 5, 0, "€", "Mixeur.",
  "Yaourt battu, eau froide, cumin grillé et menthe : la boisson rafraîchissante qui accompagne les plats épicés.",
  [f"300 g|de yaourt|{YAO}|3", "20 cl|d'eau glacée|-|0", f"½ c. à c.|de cumin grillé|{CUMIN}|1", "6|feuilles de menthe|Menthe|1", f"1 pincée|de sel|{SEL}|0"],
  ["**Mixer.** Tout, mousseux. Glaçons."], age=1, cats=["boissons", "enfants"], profil=["leger"])

K("parippu", "Dal curry au lait de coco (Sri Lanka)", "Parippu", f"{AS} › Sri Lanka", "P", 1, 4, 10, 25, "€", "Casserole.",
  "Lentilles corail au lait de coco, curcuma et feuilles de curry : doux, doré, en 30 minutes.",
  ["250 g|de lentilles corail|Lentilles corail|3", f"25 cl|de lait de coco|{COCO}|3", f"1|oignon|{OIG}|1", f"½ c. à c.|de curcuma|{CURC}|1", "10|feuilles de curry (facultatif)|Feuille de curry|1?", "1 c. à c.|de graines de moutarde|Graines de moutarde|1", f"2 gousses|d'ail|{AIL}|1", f"2 c. à s.|d'huile|{HN}|1"],
  ["**Cuire.** Lentilles, curcuma, 50 cl d'eau, 15 min.", "**Coco.** Lait de coco, sel, 5 min.", "**Tadka.** Moutarde, feuilles de curry, oignon, ail dans l'huile, versés dessus."],
  age=1, cats=["enfants"], profil=["leger"])
