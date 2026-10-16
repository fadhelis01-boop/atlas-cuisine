# -*- coding: utf-8 -*-
"""Vague 3 · Petits-déjeuners et brunchs du monde (audit UX du 16/10/2026 : « ≈ 14 petits-déjeuners, trou dans la journée »).
NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

QF = "France › Cuisine du quotidien"; UK = "Europe du Nord › Royaume-Uni"; US = "Amérique du Nord › États-Unis"
BR = ["brunch"]

K("porridge_flocons_avoine", "Porridge crémeux, banane et cannelle", "Porridge", f"{UK} › Écosse", "G", 1, 2, 3, 6, "€", "Casserole.",
  "Flocons d'avoine cuits doucement dans le lait jusqu'à devenir crémeux, banane, cannelle et miel : chaud, doux, il tient jusqu'à midi.",
  ["80 g|de flocons d'avoine|Flocons d'avoine (porridge)|3", f"40 cl|de lait (ou boisson végétale)|{LAIT}|3", "1|banane|Banane|2", f"1 pincée|de cannelle|{CANN}|1", f"1 c. à s.|de miel|{MIEL}|1", f"1 pincée|de sel|{SEL}|0"],
  ["**Cuire.** Flocons, lait et sel dans la casserole, feu doux 5-6 min en remuant : ça épaissit et devient crémeux.",
   "**Garnir.** Banane en rondelles, cannelle, miel ; quelques noix si tu en as."],
  age=1, cats=BR + ["enfants"], profil=["sucre", "leger"], tips=["Plus épais ou plus fluide : ajoute du lait en fin de cuisson jusqu'à la texture que tu aimes."])

K("overnight_oats_fruits", "Overnight oats aux fruits rouges", "Overnight oats", US, "G", 1, 2, 5, 480, "€", "Bocaux.",
  "Préparés la veille en 5 minutes, les flocons gonflent dans le lait et le yaourt pendant la nuit : un petit-déjeuner frais à emporter.",
  ["80 g|de flocons d'avoine|Flocons d'avoine (porridge)|3", f"15 cl|de lait|{LAIT}|2", f"125 g|de yaourt|{YAO}|2", "1 c. à s.|de graines de chia (facultatif)|Graines de lin / chia / chanvre|1?", "150 g|de fruits rouges (frais ou surgelés)|Framboise / mûre / myrtille|2", f"1 c. à s.|de miel|{MIEL}|1"],
  ["**Mélanger.** Flocons, lait, yaourt, chia, miel dans deux bocaux.", "**Reposer.** Une nuit au frigo : c'est épais et crémeux.", "**Garnir.** Fruits rouges le matin."],
  age=3, cats=BR, profil=["leger"], keep="2 jours au frigo, fermé.")

K("granola_maison", "Granola maison aux noix et au miel", "Granola", US, "G", 1, 10, 10, 25, "€", "Four, plaque.",
  "Flocons, noix, graines, miel et huile, dorés au four en grappes croustillantes : bien moins sucré que celui du commerce.",
  ["300 g|de flocons d'avoine|Flocons d'avoine (porridge)|3", "100 g|de noix ou amandes|Noix|2", "50 g|de graines de courge ou tournesol|Graines de tournesol / courge|1", f"100 g|de miel|{MIEL}|2", f"5 c. à s.|d'huile neutre|{HN}|2", f"1 c. à c.|de cannelle|{CANN}|1", "80 g|de raisins secs|Raisins secs|1?", f"1 pincée|de sel|{SEL}|0"],
  ["**Mélanger.** Flocons, noix concassées, graines, cannelle, sel ; miel et huile tiédis versés dessus.", "**Cuire.** Étalé sur la plaque, 160 °C, 25 min en remuant à mi-cuisson : doré et parfumé.",
   "**Refroidir.** Sans toucher : il durcit en grappes ; raisins secs ensuite."], age=3, cats=BR, keep="1 mois dans un bocal fermé.", profil=["sucre"])

K("bircher_muesli", "Bircher muesli à la pomme râpée", "Birchermüesli", "Europe du Nord › Suisse", "G", 1, 2, 10, 480, "€", "Saladier, râpe.",
  "La recette du docteur Bircher (Zurich, 1900) : flocons trempés, pomme râpée, yaourt, citron et noisettes.",
  ["80 g|de flocons d'avoine|Flocons d'avoine (porridge)|3", "1|pomme|Pomme|3", f"125 g|de yaourt|{YAO}|2", f"10 cl|de lait|{LAIT}|1", f"½|citron|{CIT}|1", "30 g|de noisettes|Noisette|1", f"1 c. à s.|de miel|{MIEL}|1"],
  ["**Tremper.** Flocons et lait, une nuit au frigo.", "**Le matin.** Pomme râpée avec sa peau, citron, yaourt, miel.", "**Servir.** Noisettes concassées."],
  age=1, cats=BR + ["enfants"], profil=["leger"])

K("pancakes_banane_avoine", "Pancakes banane-avoine sans farine", "Banana oat pancakes", US, "G", 1, 2, 8, 10, "€", "Mixeur, poêle.",
  "Banane, œufs et flocons d'avoine mixés, cuits en petits pancakes moelleux : sans sucre ajouté, sans farine.",
  ["2|bananes mûres|Banane|3", f"2|œufs|{OEUF}|3", "60 g|de flocons d'avoine|Flocons d'avoine (porridge)|3", f"½ c. à c.|de levure chimique|{LEVC}|1", f"1 pincée|de cannelle|{CANN}|0", f"1 c. à c.|d'huile|{HN}|1"],
  ["**Mixer.** Tout, 30 s : pâte épaisse.", "**Cuire.** Petites louches dans la poêle huilée, feu moyen ; retourne quand des bulles crèvent la surface (2 min), puis 1 min.", "**Servir.** Fruits, yaourt ou un filet de miel."],
  age=1, cats=BR + ["enfants"], profil=["sucre"])

K("pudding_chia_coco", "Pudding de chia au lait de coco et à la mangue", "Chia pudding", "Océanie › Australie", "G", 1, 2, 5, 240, "€€", "Bocaux.",
  "Les graines de chia gonflent dans le lait de coco et font une crème : à préparer la veille, avec de la mangue fraîche.",
  ["4 c. à s.|de graines de chia|Graines de lin / chia / chanvre|3", "25 cl|de lait de coco|Lait de coco / crème de coco|3", "1|mangue|Mangue|2", f"1 c. à s.|de sirop d'érable ou de miel|{MIEL}|1", f"½|citron vert|{CITV}|1?"],
  ["**Mélanger.** Chia, lait de coco, sirop ; remue 1 min, puis encore une fois 10 min plus tard (sinon il fait des grumeaux).", "**Reposer.** 4 h ou une nuit au frigo : ça prend comme une crème.", "**Servir.** Mangue en dés, zeste de citron vert."],
  age=3, cats=BR, profil=["sucre"])

K("smoothie_bowl_fruits_rouges", "Smoothie bowl aux fruits rouges", "Smoothie bowl", "Amérique latine › Brésil", "G", 1, 2, 10, 0, "€", "Mixeur.",
  "Un smoothie épais de fruits surgelés et banane, mangé à la cuillère, avec granola et fruits frais par-dessus.",
  ["250 g|de fruits rouges surgelés|Framboise / mûre / myrtille|3", "1|banane (congelée de préférence)|Banane|3", f"100 g|de yaourt|{YAO}|2", "4 c. à s.|de granola|SUB:granola_maison|1?", "1 c. à s.|de noix de coco râpée|Noix de coco râpée|1?"],
  ["**Mixer.** Fruits surgelés, banane, yaourt : très épais (ajoute un peu de lait seulement si le mixeur bloque).", "**Garnir.** Dans un bol, granola, coco, fruits frais en rangs."],
  age=1, cats=BR + ["enfants", "boissons"], profil=["leger"])

K("tartine_ricotta_miel_figues", "Tartines ricotta, figues et miel", "Bruschetta dolce", "Europe du Sud › Italie", "G", 1, 2, 5, 3, "€€", "Grille-pain.",
  "Pain grillé, ricotta fraîche, figues (ou poire), miel et noix : le brunch italien en 8 minutes.",
  ["2 tranches|de pain de campagne|Pain de campagne / complet|2", "150 g|de ricotta|Ricotta|3", "3|figues (ou 1 poire)|Figue (fraîche)|2", f"2 c. à s.|de miel|{MIEL}|1", "20 g|de noix|Noix|1"],
  ["**Griller.** Le pain.", "**Garnir.** Ricotta généreuse, figues en quartiers, noix, miel en filet."], age=3, cats=BR)

K("huevos_rancheros", "Huevos rancheros", "Huevos rancheros", "Amérique latine › Mexique", "P", 1, 2, 10, 15, "€", "Poêle.",
  "Le petit-déjeuner des ranchs mexicains : œufs au plat sur tortilla, sauce tomate pimentée, haricots et avocat.",
  [f"4|œufs|{OEUF}|3", "4|tortillas de maïs|Tortillas de maïs|3", f"400 g|de tomates pelées|{PELEES}|2", f"1|oignon|{OIG}|1", f"1|piment|{PIMENT}|1", "200 g|de haricots noirs|Haricots rouges / noirs|2", "1|avocat|Avocat|1?", f"½ bouquet|de coriandre|{CORI}|1"],
  ["**Sauce.** Oignon et piment 3 min, tomates, 10 min : épaisse ; sel.", "**Œufs.** Au plat, 3 min : jaune coulant ; tortillas chauffées à sec.", "**Dresser.** Tortilla, haricots chauds, œufs, sauce, avocat, coriandre."],
  age=3, cats=BR, profil=["epice"])

K("breakfast_burrito", "Breakfast burrito (œufs, pommes de terre, fromage)", "Breakfast burrito", "Amérique du Nord › États-Unis › Nouveau-Mexique", "P", 1, 2, 10, 15, "€", "Poêle.",
  "Œufs brouillés, pommes de terre rissolées, fromage et salsa roulés dans une tortilla : le brunch à emporter du sud-ouest américain.",
  ["2|grandes tortillas de blé|Tortillas de blé|3", f"4|œufs|{OEUF}|3", f"2|pommes de terre|{PDT}|2", "60 g|de cheddar|Cheddar|2", "4 c. à s.|de salsa|Salsa du commerce|1", f"1|poivron|{POIVRON}|1?"],
  ["**Rissoler.** Pommes de terre en petits dés, 12 min à la poêle huilée couverte puis découverte : tendres et dorées ; sel, paprika.",
   "**Œufs.** Brouillés crémeux.", "**Rouler.** Tortilla chaude, pommes de terre, œufs, fromage, salsa ; replie et roule serré ; 1 min par face à la poêle."],
  age=3, cats=BR)

K("congee_riz", "Congee (porridge de riz salé)", "Zhōu", "Asie de l'Est › Chine", "P", 1, 4, 10, 60, "€", "Casserole.",
  "Le petit-déjeuner de toute l'Asie : riz cuit longtemps dans beaucoup d'eau jusqu'à devenir une crème, garni de gingembre, cébette et œuf.",
  [f"120 g|de riz|{RIZ}|3", "1 morceau (3 cm)|de gingembre|Gingembre frais|2", f"3|cébettes|Oignon nouveau / cébette|1", f"2 c. à s.|de sauce soja|{SOJA}|1", f"4|œufs mollets (facultatif)|{OEUF}|1?", "1 c. à c.|d'huile de sésame|Huile de sésame (grillée)|1", "1,5 l|de bouillon (ou d'eau)|Bouillon cube volaille|2"],
  ["**Cuire.** Riz rincé, bouillon et gingembre en lamelles ; frémissement 1 h en remuant de temps en temps : les grains éclatent et font une crème.",
   "**Assaisonner.** Sel ; plus fluide ou plus épais selon ton goût (eau).", "**Garnir.** Cébette, soja, huile de sésame, œuf mollet coupé en deux."],
  age=1, cats=BR + ["enfants"], profil=["leger"])

K("tamagoyaki", "Tamagoyaki (omelette roulée japonaise)", "Tamagoyaki", "Asie de l'Est › Japon", "E", 2, 2, 15, 0, "€", "Poêle (rectangulaire de préférence), baguettes.",
  "Fines couches d'omelette sucrée-salée roulées les unes sur les autres : un rouleau moelleux, tranché, pour le petit-déjeuner ou le bento.",
  [f"4|œufs|{OEUF}|3", f"1 c. à s.|de sucre|{SUCRE}|1", f"1 c. à c.|de sauce soja|{SOJA}|1", "1 c. à s.|de mirin (facultatif)|Mirin|1?", f"1 c. à s.|d'huile|{HN}|1"],
  ["**Battre.** Œufs, sucre, soja, mirin, sans faire mousser.", "**Rouler.** Poêle huilée feu moyen-doux ; une fine couche ; quand elle est presque prise, roule-la vers toi ; pousse le rouleau au fond, nouvelle couche en soulevant le rouleau pour qu'elle passe dessous ; recommence 4-5 fois.",
   "**Former.** Roulé serré dans un papier cuisson 5 min ; tranché."], age=1, cats=BR + ["enfants"], tech=["omelette baveuse"])

K("baghrir", "Baghrir (crêpes mille trous)", "Baghrir", "Afrique du Nord › Maroc", "G", 1, 15, 15, 45, "€", "Mixeur, poêle anti-adhésive.",
  "Crêpes de semoule cuites d'un seul côté, couvertes de petits trous qui boivent le beurre fondu au miel : le petit-déjeuner du Ramadan et des fêtes.",
  ["250 g|de semoule fine|Semoule de blé (fine/moyenne)|3", f"100 g|de farine|{F55}|2", f"1 c. à c.|de levure boulangère|{LEV}|2", f"1 c. à c.|de levure chimique|{LEVC}|1", "50 cl|d'eau tiède|-|2", f"50 g|de beurre|{BEURRE}|2", f"4 c. à s.|de miel|{MIEL}|2"],
  ["**Mixer.** Semoule, farine, levures, sel et eau tiède, 2 min : pâte fluide ; 30 min au chaud : elle mousse.",
   "**Cuire.** Une louche dans la poêle moyenne, sans retourner : des trous apparaissent partout ; quand le dessus n'est plus brillant (2 min), c'est cuit.",
   "**Napper.** Beurre fondu avec le miel, versé sur les crêpes empilées."], age=1, cats=BR + ["enfants"], fetes=["Ramadan / Aïd"], profil=["sucre"])

K("muffins_oeufs_legumes", "Muffins aux œufs, épinards et fromage", "Egg muffins", US, "P", 1, 6, 10, 20, "€", "Moule à muffins, four.",
  "Œufs battus avec épinards, poivron et fromage, cuits en petits moules : à préparer d'avance, se réchauffent en 30 s.",
  [f"8|œufs|{OEUF}|3", "100 g|d'épinards|Épinard|2", f"1|poivron|{POIVRON}|1", f"80 g|de fromage râpé|{GRUY}|2", f"5 cl|de lait|{LAIT}|1"],
  ["**Préchauffer.** Four 180 °C ; moule huilé.", "**Répartir.** Légumes hachés et fromage dans les moules ; œufs battus avec lait, sel, poivre, aux trois quarts.", "**Cuire.** 18-20 min : gonflés, pris au centre (la lame ressort propre)."],
  age=1, cats=BR + ["enfants"], keep="4 jours au frigo ; 30 s au micro-ondes.")

K("tartine_labneh_zaatar", "Tartines de labneh, zaatar et légumes croquants", "Labneh w zaatar", "Moyen-Orient › Liban", "E", 1, 2, 8, 0, "€", "Planche.",
  "Fromage de yaourt épais, zaatar, huile d'olive, concombre, tomate et menthe sur pain plat : le petit-déjeuner libanais.",
  ["200 g|de labneh (ou yaourt grec égoutté)|Labneh|3", "2|pains libanais|Pain pita / libanais|2", "1 c. à s.|de zaatar|Zaatar|2", f"3 c. à s.|d'huile d'olive|{HO}|2", "½|concombre|Concombre|1", f"1|tomate|{TOM}|1", "6 feuilles|de menthe|Menthe|1", "6|olives|Olives (vertes / noires)|1?"],
  ["**Étaler.** Labneh sur l'assiette, creusé à la cuillère.", "**Arroser.** Huile d'olive, zaatar.", "**Servir.** Avec le pain, les légumes en tranches, menthe et olives."],
  age=3, cats=BR, profil=["leger"])

K("kaiserschmarrn", "Kaiserschmarrn (crêpe déchirée de l'empereur)", "Kaiserschmarrn", "Europe du Nord › Autriche", "D", 2, 3, 15, 10, "€", "Grande poêle.",
  "Une crêpe épaisse et soufflée, déchirée à la spatule dans la poêle et caramélisée, avec compote : le brunch des refuges autrichiens.",
  [f"4|œufs|{OEUF}|3", f"125 g|de farine|{F55}|3", f"25 cl|de lait|{LAIT}|2", f"30 g|de sucre|{SUCRE}|1", f"30 g|de beurre|{BEURRE}|2", "40 g|de raisins secs|Raisins secs|1?", "2 c. à s.|de sucre glace|Sucre glace|1", "4 c. à s.|de compote|Compote sans sucre ajouté|1"],
  ["**Pâte.** Jaunes, farine, lait, pincée de sel : lisse ; blancs montés avec le sucre, incorporés délicatement.", "**Cuire.** Beurre, pâte (2 cm d'épaisseur), raisins, feu moyen couvert 5 min : le dessous dore ; retourne par quarts.",
   "**Déchirer.** En morceaux avec deux spatules, 2 min : ils caramélisent. Sucre glace, compote."], age=1, cats=BR + ["enfants"], profil=["sucre"], tech=["monter des blancs", "incorporer délicatement"])

K("dutch_baby", "Dutch baby (pancake soufflé au four)", "Dutch baby", US, "D", 1, 3, 5, 20, "€", "Poêle allant au four (fonte), mixeur.",
  "Une pâte à crêpe versée dans une poêle brûlante au four : elle gonfle comme un nuage et retombe en coupe dorée. Citron et sucre glace.",
  [f"3|œufs|{OEUF}|3", f"70 g|de farine|{F55}|3", f"15 cl|de lait|{LAIT}|2", f"30 g|de beurre|{BEURRE}|2", f"1|citron|{CIT}|1", "2 c. à s.|de sucre glace|Sucre glace|1", "150 g|de fruits rouges (facultatif)|Framboise / mûre / myrtille|1?"],
  ["**Chauffer.** Poêle vide au four à 220 °C, 10 min.", "**Pâte.** Œufs, farine, lait, pincée de sel, 30 s au mixeur.", "**Cuire.** Beurre dans la poêle brûlante, pâte d'un coup ; 18 min sans ouvrir : très gonflé et doré. Citron, sucre glace, fruits."],
  age=1, cats=BR + ["enfants"], profil=["sucre"])

K("chilaquiles_verts", "Chilaquiles (chips de tortilla en sauce, œuf)", "Chilaquiles", "Amérique latine › Mexique", "P", 1, 2, 10, 12, "€", "Poêle.",
  "Triangles de tortilla dorés, mijotés une minute dans une sauce tomate-piment, fromage, crème, oignon rouge et œuf : l'anti-gaspi mexicain du matin.",
  ["6|tortillas de maïs (un peu rassises)|Tortillas de maïs|3", f"400 g|de tomates pelées|{PELEES}|2", f"1|piment|{PIMENT}|1", f"1 gousse|d'ail|{AIL}|1", f"2|œufs|{OEUF}|2", "60 g|de feta ou queso fresco|Queso fresco / cotija|1", f"3 c. à s.|de crème|{CF}|1", "¼|oignon rouge|Oignon rouge|1"],
  ["**Chips.** Tortillas en triangles, dorées à la poêle huilée ou au four : croustillantes.", "**Sauce.** Tomates, piment, ail mixés, 8 min à frémissement ; les chips 1 min dedans (elles restent un peu croquantes).",
   "**Garnir.** Œuf au plat, fromage, crème, oignon, coriandre."], age=3, cats=BR + ["zero_dechet"], profil=["epice"])

K("tartines_beurre_cacahuete_banane", "Tartines beurre de cacahuète, banane et miel", "PB & banana toast", US, "G", 1, 2, 5, 2, "€", "Grille-pain.",
  "Pain complet grillé, beurre de cacahuète, banane, miel et cannelle : énergie pour toute la matinée.",
  ["2 tranches|de pain complet|Pain de campagne / complet|2", "2 c. à s.|de beurre de cacahuète|Beurre de cacahuète|3", "1|banane|Banane|3", f"1 c. à c.|de miel|{MIEL}|1", f"1 pincée|de cannelle|{CANN}|0"],
  ["**Griller.** Le pain.", "**Tartiner.** Beurre de cacahuète, banane en rondelles, miel, cannelle."], age=3, cats=BR + ["enfants"], profil=["gras", "sucre"])

K("yaourt_fruits_granola_parfait", "Verrines yaourt, fruits et granola", "Parfait", US, "G", 1, 2, 8, 0, "€", "Verrines.",
  "Couches de yaourt grec, fruits frais et granola croustillant : le petit-déjeuner qui se monte en 8 minutes et se mange avec les yeux.",
  [f"300 g|de yaourt grec|{GREC}|3", "200 g|de fruits frais de saison|Fraise|2", "6 c. à s.|de granola|SUB:granola_maison|2", f"2 c. à c.|de miel|{MIEL}|1"],
  ["**Monter.** Yaourt, fruits, granola, recommence.", "**Finir.** Miel ; le granola au dernier moment pour qu'il reste croquant."], age=1, cats=BR + ["enfants"], profil=["leger"])

K("oeufs_cocotte_epinards_saumon", "Œufs cocotte aux épinards et au saumon fumé", "Œufs cocotte", QF, "E", 1, 4, 10, 12, "€€", "Ramequins, plat à four.",
  "Œuf cuit au bain-marie sur un lit d'épinards et de saumon fumé, crème et ciboulette : à tremper avec des mouillettes.",
  [f"4|œufs|{OEUF}|3", "100 g|d'épinards|Épinard|2", "80 g|de saumon fumé|Saumon fumé|2", f"4 c. à s.|de crème|{CF}|2", "1 c. à s.|de ciboulette|Ciboulette|1"],
  ["**Préchauffer.** Four 180 °C ; ramequins beurrés.", "**Garnir.** Épinards tombés à la poêle, saumon, 1 c. à s. de crème, l'œuf cassé dessus.", "**Cuire.** Au bain-marie 10-12 min : blanc pris, jaune coulant. Ciboulette."],
  age=3, cats=BR, profil=["poisson"], tech=["œufs cocotte"])
