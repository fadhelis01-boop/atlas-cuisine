# -*- coding: utf-8 -*-
"""Vague 9 (suite) · 11/11/2026 : plats végétariens ajoutés avec les fiches du Togo, haoussa, de Le Riz Jaune et d'Eryn,
pour garder au moins un tiers de plats sans viande ni poisson (test 63). Plats de référence de ces cuisines, réécrits ;
une vidéo de Le Riz Jaune créditée. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *
from recipes_v6_tiktok_plats import C

TG = "Afrique subsaharienne › Togo"; HA = "Afrique subsaharienne › Nigeria"; CN = "Asie de l'Est › Chine"; KR = "Asie de l'Est › Corée"; JP = "Asie de l'Est › Japon"
PALME = "Huile de palme rouge"; SCOTCH = "Piment scotch bonnet"; CEB = "Oignon nouveau / cébette"; SES = "Huile de sésame (grillée)"
TOFU = "Tofu (ferme / soyeux)"; FPDT = "Fécule de pomme de terre"; CUBEL = "Bouillon cube légumes"

K("ayimolou", "Ayimolou (riz aux haricots à la togolaise, sauce tomate pimentée)", "Ayimolou", TG, "P", 1, 6, 15, 50, "€", "Casserole, poêle.",
  "Le riz-haricots du petit-déjeuner et du déjeuner au Togo : riz et haricots rouges cuits ensemble, servis avec une sauce tomate-oignon pimentée à l'huile, du gari et un œuf dur.",
  ["400 g|de riz long|Riz long / basmati / thaï|3", "250 g|de haricots rouges secs (ou 2 boîtes)|Haricots rouges / noirs|3", f"4|tomates|{TOM}|2", f"2|oignons|{OIG}|2", f"1|piment scotch bonnet|{SCOTCH}|1", f"8 cl|d'huile|{HN}|1", f"6|œufs|{OEUF}|2", "60 g|de gari (facultatif)|Manioc / attiéké / garri|1?", f"1|cube de bouillon de légumes|{CUBEL}|1"],
  ["**Haricots.** Trempés une nuit, cuits 45 min à l'eau non salée : tendres (en boîte : rincés).",
   "**Riz.** Lavé, avec les haricots, 75 cl d'eau, sel ; 18 min à couvert, 10 min de repos.",
   "**Sauce.** Oignons émincés dans l'huile 8 min : dorés ; tomates et piment mixés, cube, 20 min : rouge, l'huile remonte.",
   "**Servir.** Riz-haricots, sauce, œuf dur coupé, une poignée de gari."],
  keep="3 jours au frigo.", age=1, cats=["vegetarien", "enfants"], profil=["epice"], kids="✓ dès 1 an, sauce sans piment.")
K("abobo", "Abobo (haricots à l'huile rouge et au gari, Togo)", "Abobo", TG, "P", 1, 4, 15, 60, "€", "Cocotte.",
  "Les haricots blancs ou niébés cuits très tendres, assaisonnés d'une sauce à l'huile de palme, à l'oignon et au piment, avec du gari pour absorber le jus et parfois des bananes plantain frites.",
  ["400 g|de haricots blancs ou niébés secs|Haricots blancs / lingots|3", f"8 cl|d'huile de palme rouge|{PALME}|2", f"2|oignons|{OIG}|2", f"2|tomates|{TOM}|1", f"1|piment scotch bonnet|{SCOTCH}|1", "80 g|de gari|Manioc / attiéké / garri|2", f"1|cube de bouillon de légumes|{CUBEL}|1", "2|bananes plantain mûres (facultatif)|Plantain (banane à cuire)|1?"],
  ["**Haricots.** Trempés une nuit, cuits 50 min à 1 h : fondants, quelques-uns s'écrasent.",
   "**Sauce.** Huile de palme chauffée sans fumer, oignons 6 min, tomates râpées, piment, cube : 10 min.",
   "**Assembler.** Haricots égouttés (un peu d'eau gardée) dans la sauce, 10 min : crémeux.",
   "**Servir.** Gari parsemé au moment de manger ; plantain frit à côté."],
  keep="3 jours au frigo.", age=1, cats=["vegetarien", "enfants"], profil=["epice"], kids="✓ dès 1 an, sans piment, haricots écrasés.")
K("dan_wake", "Dan wake (boulettes de farine de haricots, huile pimentée et yaji)", "Dan wake", HA, "P", 2, 4, 30, 15, "€", "Grande casserole, écumoire.",
  "Les « fils du haricot » haoussa : une pâte de farine de niébé (ou de pois chiches) et d'eau à la poudre de baobab, pochée en petites boulettes, servie avec une huile pimentée, du yaji, de l'oignon, de la tomate et un œuf dur.",
  ["300 g|de farine de niébé ou de pois chiches|Farine de pois chiche (besan)|3", f"1 c. à c.|de bicarbonate (ou poudre de baobab)|-|0", f"4|œufs durs|{OEUF}|2", f"6 c. à s.|d'huile|{HN}|1", "2 c. à s.|de yaji (fiche Yaji)|Cacahuète / arachide|1", f"1|oignon|{OIG}|1", f"2|tomates|{TOM}|1", "1/2|concombre|Concombre|1"],
  ["**Pâte.** Farine, bicarbonate, sel, 25 cl d'eau versée peu à peu : pâte épaisse qui tient sur la cuillère.",
   "**Pocher.** Eau bouillante salée ; petites cuillerées détachées au doigt mouillé, 8 à 10 min : elles remontent, fermes au centre.",
   "**Égoutter.** À l'écumoire, dans un plat.",
   "**Servir.** Huile chaude, yaji, oignon émincé, tomate, concombre, œuf dur en quartiers."],
  tips=["⚠️ Arachide (yaji) : allergène majeur."], keep="1 jour au frigo.", age=2, cats=["vegetarien"], profil=["epice"], kids="✓ dès 2 ans, yaji doux, coupés.")
K("miyan_taushe", "Miyan taushe végétarienne (soupe haoussa à la courge, arachide et épinards)", "Miyan taushe", HA, "P", 1, 6, 20, 40, "€", "Cocotte, mixeur.",
  "La soupe épaisse du nord du Nigeria : de la courge fondante liée à la pâte d'arachide, avec des épinards et une base tomate-poivron pimentée ; ici sans viande, pour tremper le tuwo, la masa ou du riz.",
  ["800 g|de courge (butternut ou potiron)|Butternut / courge musquée|3", "120 g|de pâte d'arachide|Pâte d'arachide|2", "300 g|d'épinards|Épinard|2", f"3|tomates|{TOM}|2", f"1|poivron rouge|{POIVRON}|1", f"1|oignon|{OIG}|1", f"1|piment scotch bonnet|{SCOTCH}|1", f"6 cl|d'huile|{HN}|1", f"1|cube de bouillon de légumes|{CUBEL}|1"],
  ["**Base.** Tomates, poivron, oignon, piment mixés ; huile, 15 min : l'huile remonte.",
   "**Courge.** En cubes, 50 cl d'eau, cube ; 20 min : fondante ; écrasée en partie.",
   "**Lier.** Pâte d'arachide délayée, 10 min à feu doux en remuant.",
   "**Épinards.** Hachés, 3 min ; sel."],
  tips=["⚠️ Arachide : allergène majeur."], keep="3 jours au frigo ; se congèle.", age=1, cats=["vegetarien", "enfants"], profil=["gras"], kids="✓ dès 1 an, sans piment, sans allergie à l'arachide.", side="masa_haoussa")
K("tofu_aigre_doux", "Tofu croustillant à la sauce aigre-douce, poivrons et ananas", "Tofu aigre-doux", CN, "P", 1, 3, 20, 15, "€", "Poêle, wok.",
  "Le plat aigre-doux des restaurants chinois, avec du tofu enrobé de fécule et poêlé jusqu'à croustiller, des poivrons, de l'oignon et de l'ananas dans une sauce ketchup-vinaigre brillante.",
  [f"400 g|de tofu ferme|{TOFU}|3", f"4 c. à s.|de fécule|{FPDT}|1", f"1|poivron rouge|{POIVRON}|1", f"1|poivron vert|{POIVRON}|1", f"1|oignon|{OIG}|1", "150 g|d'ananas en morceaux|Ananas|2", "4 c. à s.|de ketchup|Ketchup|2", f"2 c. à s.|de vinaigre de riz|Vinaigre de riz|1", f"2 c. à s.|de sucre|{SUCRE}|1", f"1 c. à s.|de sauce soja|{SOJA}|1", f"4 c. à s.|d'huile|{HN}|1"],
  ["**Tofu.** Pressé 15 min entre deux torchons, en cubes, roulé dans la fécule ; poêle huilée, 8 min en retournant : doré partout ; réservé.",
   "**Légumes.** Oignon et poivrons en morceaux, wok chaud, 3 min : croquants ; ananas 1 min.",
   "**Sauce.** Ketchup, vinaigre, sucre, soja, 8 cl d'eau, 1 c. à c. de fécule : versée, 1 min, brillante.",
   "**Napper.** Tofu, 30 s ; tout de suite, avec du riz."],
  keep="1 jour au frigo (le tofu ramollit).", age=2, cats=["vegetarien", "enfants"], profil=["sucre", "acide"], side="riz_nature")
K("tofu_sauce_piquante", "Tofu à la sauce piquante (façon crevettes sauce piquante)", "Tofu sauce piquante", CN, "P", 1, 2, 15, 12, "€", "Poêle, wok.",
  "Le jumeau végétarien des crevettes sauce piquante : du tofu ferme doré, enrobé d'une sauce tomate-soja relevée au piment, à l'ail et au gingembre.",
  [f"400 g|de tofu ferme|{TOFU}|3", f"1/2|oignon|{OIG}|1", f"2|gousses d'ail|{AIL}|1", f"1 cm|de gingembre|{GING}|1", f"1 c. à c.|de concentré|{CONC}|1", "2 c. à s.|de ketchup|Ketchup|1", "1 c. à c.|de pâte de piment|Pâte de piment|1", f"2 c. à s.|de sauce soja|{SOJA}|1", f"1 c. à c.|de sucre|{SUCRE}|1", f"2 c. à s.|de fécule|{FPDT}|1", f"3 c. à s.|d'huile|{HN}|1", f"1|cébette|{CEB}|1"],
  ["**Tofu.** Pressé, en cubes, fécule ; poêle huilée 8 min : doré ; réservé.",
   "**Sauce.** Oignon, ail, gingembre 1 min ; concentré, ketchup, pâte de piment 30 s ; soja, sucre, 10 cl d'eau.",
   "**Lier.** 1 c. à c. de fécule délayée, 1 min.",
   "**Enrober.** Tofu, 1 min ; cébette. Riz blanc."],
  keep="1 jour au frigo.", age=3, cats=["vegetarien", "express"], profil=["epice"], side="riz_nature")
K("tofu_chou_chinois_saute", "Chou chinois sauté au tofu et au vinaigre noir", "Chou chinois au tofu", CN, "P", 1, 2, 15, 10, "€", "Wok.",
  "Le chou chinois saisi à feu vif avec de l'ail et du piment séché, déglacé au vinaigre noir et à la sauce soja, avec du tofu doré : croquant, acidulé, en dix minutes.",
  ["1/2|chou chinois (500 g)|Chou chinois / pak-choï|3", f"250 g|de tofu ferme|{TOFU}|3", f"3|gousses d'ail|{AIL}|1", "2|piments séchés|Flocons de piment|1?", "2 c. à s.|de vinaigre noir chinois|Vinaigre noir chinois (Chinkiang)|2", f"2 c. à s.|de sauce soja|{SOJA}|1", f"1 c. à c.|de sucre|{SUCRE}|1", f"1 c. à c.|de fécule|{FPDT}|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Tofu.** En tranches, poêlé 6 min : doré ; réservé.",
   "**Chou.** Côtes et feuilles séparées, en morceaux ; wok fumant, ail, piment 20 s ; côtes 2 min, feuilles 1 min.",
   "**Déglacer.** Vinaigre sur la paroi chaude, soja, sucre : ça grésille.",
   "**Lier.** Tofu, fécule dans 3 c. à s. d'eau, 30 s : brillant."],
  keep="Le jour même.", age=2, cats=["vegetarien", "express", "leger"], profil=["acide", "leger"], side="riz_nature")
K("nouilles_froides_sesame", "Nouilles froides au sésame (liang mian)", "Liáng miàn", CN, "P", 1, 2, 15, 5, "€", "Casserole, saladier.",
  "Les nouilles d'été chinoises : rincées à l'eau froide, nappées d'une sauce de purée de sésame, soja, vinaigre noir et huile pimentée, avec du concombre en julienne et des cacahuètes.",
  ["200 g|de nouilles chinoises aux œufs|Nouilles chinoises aux œufs|3", "3 c. à s.|de tahini|Tahini (purée de sésame)|2", f"2 c. à s.|de sauce soja|{SOJA}|1", "1 c. à s.|de vinaigre noir chinois|Vinaigre noir chinois (Chinkiang)|1", f"1 c. à c.|de sucre|{SUCRE}|1", "1 c. à c.|d'huile pimentée|Huile pimentée chinoise|1?", f"1|gousse d'ail|{AIL}|1", "1|concombre|Concombre|2", "30 g|de cacahuètes|Cacahuète / arachide|1", f"1|cébette|{CEB}|1"],
  ["**Nouilles.** Cuites selon le paquet, rincées à l'eau froide, égouttées, 1 c. à c. d'huile de sésame.",
   "**Sauce.** Tahini, soja, vinaigre, sucre, ail râpé, 3 c. à s. d'eau : lisse et coulante.",
   "**Concombre.** En julienne fine.",
   "**Servir.** Nouilles, sauce, concombre, cacahuètes concassées, cébette, huile pimentée."],
  tips=["⚠️ Arachide, sésame : allergènes."], keep="1 jour au frigo (sauce à part).", age=2, cats=["vegetarien", "express", "pique_nique"], profil=["acide", "gras"])
K("pajeon", "Pajeon (galette coréenne aux cébettes)", "Pajeon", KR, "P", 1, 2, 15, 10, "€", "Grande poêle.",
  "La galette coréenne des jours de pluie : de longues cébettes prises dans une pâte fine farine-fécule-eau glacée, cuite croustillante à la poêle, coupée en carrés et trempée dans une sauce soja-vinaigre.",
  [f"1|botte de cébettes|{CEB}|3", f"100 g|de farine|{F55}|2", f"30 g|de fécule|{FPDT}|1", f"1|œuf|{OEUF}|1", "1/2|courgette en julienne (facultatif)|Courgette|1?", f"1|piment rouge|{PIMENT}|1?", f"3 c. à s.|de sauce soja|{SOJA}|1", "1 c. à s.|de vinaigre de riz|Vinaigre de riz|1", f"5 c. à s.|d'huile|{HN}|1"],
  ["**Pâte.** Farine, fécule, sel, œuf, 15 cl d'eau glacée : fluide, quelques grumeaux.",
   "**Cébettes.** En tronçons de la largeur de la poêle, couchées dans la poêle huilée chaude ; pâte versée par-dessus, juste pour les lier.",
   "**Cuire.** 4 min : dessous doré ; retourne, filet d'huile sur le bord, 3 min en pressant : croustillant.",
   "**Sauce.** Soja, vinaigre, piment haché ; galette en carrés."],
  keep="Le jour même.", age=1, cats=["vegetarien", "express", "enfants"], profil=["gras"])
K("korokke_mais_fromage", "Korokke au maïs et au fromage (croquettes végétariennes)", "Korokke maïs-fromage", JP, "P", 2, 6, 40, 20, "€", "Casserole à friture.",
  "La croquette japonaise en version douce : purée de pommes de terre, maïs, oignon et fromage fondant, panée au panko et frite ; avec du chou cru et une sauce tonkatsu.",
  [f"500 g|de pommes de terre farineuses|{PDT}|3", "150 g|de maïs doux|Maïs doux|2", "100 g|de cheddar ou de mozzarella|Cheddar|2", f"1/2|oignon|{OIG}|1", f"1|œuf|{OEUF}|1", "80 g|de panko|Panko|1", f"3 c. à s.|de farine|{F55}|1", "50 cl|d'huile de friture|Huile d'arachide|2", "1/8|de chou blanc émincé|Chou blanc / rouge|1"],
  ["**Purée.** Pommes de terre cuites, écrasées sèches ; oignon haché revenu 3 min, maïs, fromage en dés, sel, poivre ; 30 min au frigo.",
   "**Former.** 6 galettes ovales épaisses.",
   "**Paner.** Farine, œuf, panko.",
   "**Frire.** 175 °C, 3 min par face : dorées ; chou cru et sauce à côté."],
  tips=["Huile chaude : loin des enfants."], keep="Crues panées : 1 mois au congélateur.", age=2, cats=["vegetarien", "enfants"], profil=["gras"])
K("udon_gochujang_legumes", "Udon sautées au gochujang et aux légumes", "Udon gochujang", KR, "P", 1, 2, 15, 8, "€", "Wok.",
  "Des udon épaisses sautées avec du chou, des champignons et de la carotte dans une sauce gochujang-miso sucrée et piquante, finies au sésame.",
  ["2|portions d'udon (400 g)|Nouilles udon|3", "1 c. à s.|de gochujang|Gochujang|2", "1 c. à c.|de miso (ou doenjang)|Miso|1", f"1 c. à s.|de sauce soja|{SOJA}|1", f"1 c. à s.|de miel|{MIEL}|1", "1/8|de chou blanc|Chou blanc / rouge|2", "150 g|de champignons de Paris|Champignon de Paris|2", f"1|carotte|{CAROTTE}|1", f"2|gousses d'ail|{AIL}|1", f"1 c. à c.|d'huile de sésame|{SES}|1", "1 c. à c.|de sésame|Sésame (blanc/noir)|1", f"2 c. à s.|d'huile|{HN}|1"],
  ["**Sauce.** Gochujang, miso, soja, miel, 4 c. à s. d'eau.",
   "**Udon.** 1 min dans l'eau bouillante, détachées ; égouttées.",
   "**Légumes.** Wok chaud, ail, carotte en bâtonnets, champignons, chou émincé, 4 min : dorés, encore croquants.",
   "**Sauter.** Udon, sauce, 2 min : enrobées, brillantes ; sésame."],
  keep="1 jour au frigo.", age=3, cats=["vegetarien", "express"], profil=["epice", "sucre"],
  credit=C(("@lerizjaune", "https://www.tiktok.com/@lerizjaune/video/7467980024113794306")))
K("nouilles_tomate_oeuf", "Nouilles à la tomate et à l'œuf (xihongshi jidan mian)", "Nouilles tomate-œuf", CN, "P", 1, 2, 10, 15, "€", "Casserole, poêle.",
  "Le réconfort chinois de tous les jours : des œufs brouillés moelleux et des tomates fondues en sauce, sur des nouilles, avec de la cébette.",
  ["200 g|de nouilles chinoises aux œufs|Nouilles chinoises aux œufs|3", f"3|œufs|{OEUF}|2", f"3|tomates mûres|{TOM}|3", f"1 c. à s.|de ketchup ou de concentré|{CONC}|1", f"1 c. à s.|de sauce soja|{SOJA}|1", f"1 c. à c.|de sucre|{SUCRE}|1", f"2|cébettes|{CEB}|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Œufs.** Battus salés, poêle chaude huilée, remués 30 s : gros morceaux moelleux ; réservés.",
   "**Tomates.** En quartiers, 5 min : elles fondent ; concentré, soja, sucre, 10 cl d'eau : sauce.",
   "**Nouilles.** Cuites selon le paquet, égouttées.",
   "**Assembler.** Œufs dans la sauce, 30 s ; sur les nouilles, cébette."],
  keep="1 jour au frigo.", age=1, cats=["vegetarien", "express", "enfants"], profil=["acide"])
