# -*- coding: utf-8 -*-
"""Vague 2 · Boulangerie maison (pains du quotidien) et cuisine des enfants (à faire avec eux, ou pour eux)."""
from recipes_v2_base import *

BL = "France › Boulangerie"; EN = "France › Cuisine des enfants"
T65 = "Farine de blé T65 (tradition)"

K("pain_campagne_levain", "Pain de campagne au levain", "Pain au levain", BL, "Pa", 3, 10, 40, 1440, "€", "Banneton ou saladier + torchon, cocotte en fonte, lame.",
  "Une croûte épaisse qui chante, une mie alvéolée légèrement acidulée, qui se garde une semaine : le pain des boulangers, chez toi.",
  [f"400 g|de farine T65|{T65}|3", "100 g|de farine de seigle ou T80|Farine de seigle|2", "350 g|d'eau tiède|-|0", "100 g|de levain actif|Levain (maison)|3", f"10 g|de sel|{SEL}|1"],
  ["**Autolyse.** Farines + 330 g d'eau, 1 h.", "**Pétrir.** Levain, sel, reste d'eau ; 4 séries de rabats toutes les 30 min.", "**Pointage.** 3-4 h à 24 °C : +50 % de volume, bulles.",
   "**Façonner.** Boule serrée, banneton fariné, une nuit au frigo (12-16 h).", "**Cuire.** Cocotte préchauffée à 250 °C ; grigne ; 20 min couvert, 25 min découvert à 230 °C."],
  keep="1 semaine dans un torchon ; tranché, se congèle.", age=1, cats=["pains"], profil=["leger"], tech=["Levain", "Autolyse", "Pointage, rabats", "Créer de la vapeur"])

K("pain_complet", "Pain complet moelleux (moule)", "Pain complet", BL, "Pa", 1, 10, 15, 180, "€", "Moule à cake.",
  "Un pain complet sans façonnage compliqué, cuit en moule : parfait pour les tartines et les sandwichs.",
  ["500 g|de farine complète T150|Farine T110 / T150 (complète)|3", "38 cl|d'eau tiède|-|0", f"7 g|de levure|{LEV}|1", f"10 g|de sel|{SEL}|1", f"1 c. à s.|de miel|{MIEL}|1", "40 g|de graines (tournesol, lin)|Graines de tournesol / courge|1?"],
  ["**Pâte.** Tout mélanger, pétrir 8 min (pâte collante).", "**Pousse.** 1 h 30.", "**Moule.** Huilé, pâte tassée, graines, 45 min.", "**Cuire.** 40 min à 210 °C ; démoule, 5 min à nu."],
  keep="5 jours.", age=1, cats=["pains", "enfants"], profil=["leger"], tech=["Pétrir"])

K("pain_au_lait", "Petits pains au lait", "Pain au lait", BL, "Pa", 1, 12, 25, 150, "€", "Plaque.",
  "Petits pains moelleux et légèrement sucrés, pour le goûter avec une barre de chocolat.",
  [f"500 g|de farine|{F45}|3", f"25 cl|de lait tiède|{LAIT}|2", f"1|œuf|{OEUF}|1", f"60 g|de beurre mou|{BEURRE}|2", f"50 g|de sucre|{SUCRE}|1", f"7 g|de levure|{LEV}|1", f"8 g|de sel|{SEL}|0"],
  ["**Pétrir.** Tout sauf le beurre 8 min, puis le beurre 5 min.", "**Pousse.** 1 h 30.", "**Façonner.** 12 boudins, apprêt 45 min ; dorure, entailles aux ciseaux.", "**Cuire.** 15 min à 180 °C."],
  age=1, cats=["pains", "enfants"], profil=["sucre"], tech=["Brioche"])

K("fougasse_olives", "Fougasse aux olives et herbes", "Fougasse", "France › Provence-Alpes-Côte d'Azur", "Pa", 1, 6, 20, 120, "€", "Plaque, coupe-pâte.",
  "Un pain plat ajouré, croustillant, parfumé aux olives et aux herbes de Provence : à partager à l'apéritif.",
  [f"400 g|de farine T65|{T65}|3", "26 cl|d'eau|-|0", f"5 g|de levure|{LEV}|1", f"8 g|de sel|{SEL}|0", "100 g|d'olives noires|Olives (vertes / noires)|2", "1 c. à s.|d'herbes de Provence|Herbes de Provence|1", f"5 c. à s.|d'huile d'olive|{HO}|2"],
  ["**Pâte.** Pétris, ajoute olives et herbes ; pousse 1 h 30.", "**Former.** Ovale aplati, entailles en épi écartées du doigt.", "**Cuire.** Huile, 20 min à 230 °C."],
  age=1, cats=["pains"], fetes=["Apéritif dînatoire"], profil=["gras"])

K("bagels", "Bagels", "Bagel", "Amérique du Nord › États-Unis › New York", "Pa", 2, 8, 40, 120, "€", "Grande casserole, plaque.",
  "Pochés puis cuits au four : mie dense, croûte brillante. Au saumon et fromage frais, ou en sandwich.",
  [f"500 g|de farine T65|{T65}|3", "28 cl|d'eau tiède|-|0", f"7 g|de levure|{LEV}|1", f"10 g|de sel|{SEL}|1", f"1 c. à s.|de miel (pâte) + 2 (pochage)|{MIEL}|1", "2 c. à s.|de sésame ou pavot|Sésame (blanc/noir)|1"],
  ["**Pâte ferme.** Pétris 10 min ; pousse 1 h.", "**Former.** 8 boules, trou au doigt élargi à 4 cm ; 20 min.", "**Pocher.** Eau bouillante miellée, 1 min par face.", "**Cuire.** Graines, 20 min à 220 °C."],
  age=1, cats=["pains"], profil=["leger"])

K("ciabatta", "Ciabatta", "Ciabatta", "Europe du Sud › Italie › Vénétie", "Pa", 2, 2, 20, 1080, "€", "Bac huilé, plaque.",
  "Un pain très hydraté à grosses alvéoles, croûte fine : sans pétrissage, avec du temps.",
  [f"500 g|de farine T65|{T65}|3", "40 cl|d'eau|-|0", f"2 g|de levure|{LEV}|1", f"10 g|de sel|{SEL}|1", f"1 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Mélanger.** Tout, 3 séries de rabats à 30 min d'écart ; une nuit au frigo.", "**Diviser.** Sur plan bien fariné, 2 rectangles sans dégazer ; 1 h.", "**Cuire.** 25 min à 240 °C avec vapeur."],
  age=1, cats=["pains"], profil=["leger"], tech=["Pointage, rabats", "Hydratation"])

K("pains_burger", "Pains à burger briochés", "Burger buns", BL, "Pa", 1, 8, 20, 150, "€", "Plaque.",
  "Moelleux, dorés, au sésame : ils changent tout dans un burger maison.",
  [f"500 g|de farine|{F45}|3", f"20 cl|de lait tiède|{LAIT}|2", f"1|œuf + 1 pour dorer|{OEUF}|1", f"50 g|de beurre|{BEURRE}|2", f"30 g|de sucre|{SUCRE}|1", f"7 g|de levure|{LEV}|1", f"9 g|de sel|{SEL}|0", "1 c. à s.|de sésame|Sésame (blanc/noir)|1"],
  ["**Pâte.** Pétris 10 min ; pousse 1 h 30.", "**Bouler.** 8 boules aplaties ; 1 h.", "**Cuire.** Dorure, sésame, 15 min à 190 °C."],
  age=1, cats=["pains", "enfants"], profil=["sucre"])

K("pain_sans_gluten", "Pain sans gluten aux graines", "Pain sans gluten", BL, "Pa", 1, 10, 15, 75, "€", "Moule à cake.",
  "Un pain moelleux sans blé, à base de farines de riz et de sarrasin et de psyllium ou graines de lin : pour les intolérants.",
  ["250 g|de farine de riz|Farine de riz / riz gluant|3", "100 g|de farine de sarrasin|Farine de sarrasin|2", "50 g|de fécule de pomme de terre|Fécule de pomme de terre|1", "30 g|de graines de lin moulues (ou 15 g de psyllium)|Graines de lin / chia / chanvre|2", "45 cl|d'eau tiède|-|0", f"7 g|de levure|{LEV}|1", f"8 g|de sel|{SEL}|0", f"2 c. à s.|d'huile|{HO}|1"],
  ["**Gel.** Lin moulu + eau, 10 min.", "**Pâte.** Tout mélanger : pâte épaisse comme un cake.", "**Pousse.** Dans le moule, 45 min.", "**Cuire.** 50 min à 210 °C, refroidi avant de couper."],
  tips=["Vérifie que levure et fécule sont certifiées sans gluten pour les cœliaques."], age=1, cats=["pains"], profil=["leger"])

K("pain_mais_cornbread", "Cornbread (pain de maïs)", "Cornbread", "Amérique du Nord › États-Unis", "Pa", 1, 8, 10, 25, "€", "Poêle en fonte ou moule carré.",
  "Un pain rapide au maïs, doré, légèrement sucré : avec le chili ou au petit-déjeuner.",
  ["150 g|de polenta fine|Polenta / semoule de maïs|3", f"120 g|de farine|{F55}|2", f"25 cl|de lait ribot ou lait|{LAIT}|2", f"2|œufs|{OEUF}|1", f"60 g|de beurre fondu|{BEURRE}|2", f"2 c. à s.|de miel|{MIEL}|1", f"2 c. à c.|de levure chimique|{LEVC}|1"],
  ["**Mélanger.** Secs et humides, juste.", "**Cuire.** Moule beurré chaud, 22 min à 200 °C."], age=1, cats=["pains", "enfants"], profil=["sucre"])

K("nuggets_maison", "Nuggets de poulet maison au four", "Nuggets", EN, "P", 1, 4, 25, 18, "€", "Plaque, 3 assiettes.",
  "Du vrai blanc de poulet en morceaux, pané aux cornflakes ou au panko et cuit au four : croustillant sans friture.",
  [f"500 g|de blancs de poulet|{BLANC_P}|3", "80 g|de panko ou cornflakes écrasés|Panko|2", f"40 g|de parmesan râpé|{PARM}|1", f"1|œuf|{OEUF}|1", f"40 g|de farine|{F55}|1", f"1 c. à c.|de paprika doux|{PAPRIKA}|1", f"2 c. à s.|d'huile|{HN}|1"],
  ["**Couper.** Morceaux de 3 cm, sel.", "**Paner.** Farine, œuf, panko + parmesan + paprika (les enfants adorent le faire).", "**Cuire.** Sur plaque huilée, huile en filet, 18 min à 210 °C en retournant à mi-cuisson."],
  age=1, cats=["enfants"], profil=["leger"], tech=["Paner"])

K("croquettes_poisson", "Croquettes de poisson et pommes de terre", "Fish cakes", EN, "P", 1, 4, 25, 15, "€", "Poêle.",
  "Poisson et purée en galettes dorées : la façon la plus simple de faire aimer le poisson.",
  ["400 g|de cabillaud ou colin cuit|Colin, lieu noir, merlu|3", f"400 g|de purée de pommes de terre|{PDT}|3", f"1|œuf|{OEUF}|1", "1 c. à s.|de ciboulette|Ciboulette|1", f"½|citron (zeste)|{CIT}|1", "60 g|de chapelure|Chapelure|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Mélanger.** Poisson émietté (sans arêtes), purée, œuf, zeste, ciboulette, sel.", "**Former.** 8 galettes, chapelure.", "**Dorer.** 4 min par face."],
  age=1, cats=["enfants", "zero_dechet"], profil=["poisson"])

K("pates_sauce_legumes_caches", "Pâtes à la sauce tomate aux légumes cachés", "Sauce aux légumes cachés", EN, "P", 1, 6, 15, 30, "€", "Casserole, mixeur.",
  "Une sauce tomate lisse qui contient carotte, courgette, poivron et lentilles corail : les enfants n'y voient que du rouge.",
  [f"500 g|de pâtes|{PATES}|3", f"700 g|de passata|{PELEES}|3", f"2|carottes|{CAROTTE}|2", "1|courgette|Courgette|1", f"1|poivron rouge|{POIVRON}|1", "60 g|de lentilles corail|Lentilles corail|1", f"1|oignon|{OIG}|1", f"2 c. à s.|d'huile d'olive|{HO}|1", "1 poignée|de basilic|Basilic|1", f"40 g|de parmesan|{PARM}|1"],
  ["**Cuire.** Oignon, légumes en dés, lentilles, passata, 25 cl d'eau, 25 min.", "**Mixer.** Très lisse.", "**Servir.** Avec les pâtes, parmesan."],
  keep="4 jours ; se congèle en portions.", age=1, cats=["enfants"], profil=["leger"])

K("mini_pizzas", "Mini-pizzas à garnir soi-même", "Mini pizzas", EN, "P", 1, 12, 30, 15, "€", "Plaques, emporte-pièce.",
  "Atelier pizza : chacun garnit ses disques de pâte. Idéal pour les anniversaires.",
  ["1|pâte à pizza|SUB:pate_pizza|3", f"200 g|de sauce tomate|{PELEES}|2", "200 g|de mozzarella|Mozzarella / burrata|2", "300 g|de garnitures (jambon de dinde, champignons, olives, poivrons, maïs)|Jambon de dinde / de poulet|1", "1 c. à c.|d'origan|Origan frais / sec|0"],
  ["**Disques.** Pâte étalée, ronds de 10 cm.", "**Garnir.** Sauce, fromage, garnitures choisies.", "**Cuire.** 10-12 min à 240 °C."],
  age=3, cats=["enfants"], fetes=["Anniversaire"], profil=["gras"])

K("gateau_marbre", "Gâteau marbré chocolat-vanille", "Gâteau marbré", EN, "G", 1, 8, 20, 45, "€", "Moule à cake.",
  "Le gâteau des goûters, moelleux, aux deux pâtes entremêlées.",
  [f"200 g|de farine|{F55}|3", f"150 g|de sucre|{SUCRE}|2", f"150 g|de beurre mou|{BEURRE}|2", f"3|œufs|{OEUF}|2", f"10 cl|de lait|{LAIT}|1", f"1 sachet|de levure|{LEVC}|1", "2 c. à s.|de cacao|Cacao en poudre non sucré|2", f"1 pincée|de vanille|{VAN}|1"],
  ["**Pâte.** Beurre + sucre, œufs, farine + levure, lait.", "**Diviser.** Moitié vanille, moitié cacao.", "**Marbrer.** En alternance dans le moule, un coup de fourchette en zigzag.", "**Cuire.** 45 min à 170 °C."],
  age=1, cats=["enfants"], profil=["sucre"])

K("muffins_myrtilles", "Muffins aux myrtilles", "Blueberry muffins", "Amérique du Nord › États-Unis", "G", 1, 12, 15, 22, "€", "Moule à muffins, caissettes.",
  "Muffins bombés, moelleux, pleins de fruits : la règle d'or est de ne presque pas mélanger.",
  [f"280 g|de farine|{F55}|3", f"150 g|de sucre|{SUCRE}|2", f"2|œufs|{OEUF}|1", f"20 cl|de lait ou yaourt|{YAO}|2", f"8 cl|d'huile|{HN}|1", f"2 c. à c.|de levure|{LEVC}|1", "200 g|de myrtilles|Framboise / mûre / myrtille|3"],
  ["**Mélanger.** Secs d'un côté, humides de l'autre, réunis en 10 coups de spatule ; myrtilles farinées.", "**Cuire.** Caissettes pleines, 5 min à 210 °C puis 17 min à 180 °C (ça fait le dôme)."],
  age=1, cats=["enfants"], profil=["sucre"])

K("compote_pommes_poires", "Compote pommes-poires sans sucre ajouté", "Compote", EN, "D", 1, 6, 15, 20, "€", "Casserole.",
  "Des fruits mûrs, un peu d'eau, une pointe de vanille : pas besoin de sucre.",
  ["6|pommes|Pomme|3", "3|poires|Poire|2", "5 cl|d'eau|-|0", f"1 pincée|de vanille ou de cannelle|{VAN}|1"],
  ["**Cuire.** Fruits en morceaux, eau, couvert 20 min.", "**Écraser.** Ou mixer pour les plus petits."],
  keep="5 jours au frigo ; congélation en portions.", age=1, cats=["enfants", "zero_dechet"], profil=["sucre"], kids="✓ dès 6 mois, lisse, sans cannelle.")

K("smoothie_banane_fraise", "Smoothie banane-fraise", "Smoothie", EN, "B", 1, 2, 5, 0, "€", "Mixeur.",
  "Fruits, yaourt et lait, mixés : un goûter qui ressemble à un milk-shake.",
  ["1|banane|Banane|3", "150 g|de fraises (fraîches ou surgelées)|Fraise|3", f"125 g|de yaourt|{YAO}|2", f"15 cl|de lait|{LAIT}|2"],
  ["**Mixer.** Tout, 1 min."], age=1, cats=["enfants", "boissons", "zero_dechet"], profil=["sucre"], tips=["Bananes trop mûres : coupe-les en rondelles et congèle-les pour les smoothies."])

K("crepes_salees_enfants", "Crêpes roulées jambon-fromage (dinde)", "Crêpes roulées", EN, "P", 1, 4, 20, 10, "€", "Poêle, plat à four.",
  "Crêpes garnies de jambon de dinde et de fromage, roulées et gratinées à la béchamel : un dîner que les enfants réclament.",
  ["8|crêpes|SUB:crepes_bretonnes|3", "8 tranches|de jambon de dinde|Jambon de dinde / de poulet|2", "150 g|de fromage râpé|Gruyère / comté / emmental / beaufort|2", "1|recette de béchamel|SUB:bechamel|2"],
  ["**Rouler.** Crêpe, jambon, fromage, roulée.", "**Gratiner.** Plat, béchamel, fromage, 15 min à 200 °C."],
  age=1, cats=["enfants", "zero_dechet"], fetes=["Chandeleur"], profil=["gras"])

K("puree_couleurs", "Purées de couleurs (orange, verte, violette)", "Purées de légumes", EN, "A", 1, 6, 15, 25, "€", "Casserole, presse-purée.",
  "Purée de pommes de terre mêlée à un légume coloré : carotte, petits pois-brocoli, betterave. On mange avec les yeux.",
  [f"800 g|de pommes de terre|{PDT}|3", f"300 g|de carottes (orange)|{CAROTTE}|2", "300 g|de brocoli ou petits pois (verte)|Brocoli|2", "1|betterave cuite (violette)|Betterave (crue/cuite)|1", f"40 g|de beurre|{BEURRE}|2", f"20 cl|de lait|{LAIT}|2"],
  ["**Cuire.** Légumes séparément.", "**Écraser.** Pommes de terre avec beurre et lait, partagées en 3, chacune avec son légume."],
  age=1, cats=["enfants"], profil=["leger"], kids="✓ dès 6 mois, sans sel.")

K("croque_legumes_pizza", "Croque-monsieur pizza", "Croque pizza", EN, "P", 1, 4, 10, 10, "€", "Four ou appareil à croque.",
  "Pain de mie, sauce tomate, mozzarella, origan : le croque qui sent la pizza, prêt en 10 minutes.",
  ["8 tranches|de pain de mie|Pain de mie|3", f"4 c. à s.|de sauce tomate|{PELEES}|2", "150 g|de mozzarella|Mozzarella / burrata|2", "4 tranches|de jambon de dinde (facultatif)|Jambon de dinde / de poulet|1?", "1 c. à c.|d'origan|Origan frais / sec|1"],
  ["**Monter.** Pain, sauce, mozzarella, jambon, pain.", "**Cuire.** 10 min à 200 °C en retournant, ou 4 min dans l'appareil."],
  age=1, cats=["enfants"], profil=["gras"])

K("brochettes_fruits_chocolat", "Brochettes de fruits, trempette chocolat", "Brochettes de fruits", EN, "D", 1, 6, 15, 0, "€", "Piques en bois (bouts arrondis).",
  "Les enfants enfilent eux-mêmes les fruits ; une petite sauce au chocolat pour tremper.",
  ["1 kg|de fruits variés (fraises, banane, raisin, melon, kiwi)|Fraise|3", f"100 g|de chocolat au lait|Chocolat au lait|2", f"10 cl|de crème|{CL}|1"],
  ["**Enfiler.** Fruits en morceaux sur piques.", "**Trempette.** Crème chaude sur chocolat."],
  age=3, cats=["enfants"], fetes=["Anniversaire"], profil=["sucre"])

K("cookies_avoine_banane", "Cookies avoine-banane (2 ingrédients + pépites)", "Cookies à la banane", EN, "G", 1, 12, 10, 15, "€", "Plaque.",
  "Banane mûre écrasée et flocons d'avoine : des cookies sans sucre ajouté ni œuf, à faire avec les tout-petits.",
  ["2|bananes très mûres|Banane|3", "150 g|de flocons d'avoine|Avoine (flocons)|3", "40 g|de pépites de chocolat ou raisins secs|Pépites de chocolat|1?", f"1 pincée|de cannelle|{CANN}|0"],
  ["**Mélanger.** Banane écrasée, avoine, cannelle, pépites.", "**Cuire.** Petits tas aplatis, 15 min à 180 °C."],
  age=1, cats=["enfants", "zero_dechet"], profil=["sucre"], kids="✓ dès 1 an (sans pépites avant 3 ans).")

K("soupe_alphabet", "Soupe de légumes aux pâtes alphabet", "Soupe alphabet", EN, "So", 1, 6, 15, 30, "€", "Faitout, mixeur.",
  "Un velouté doux de légumes et des petites lettres à pêcher : on écrit son prénom dans l'assiette.",
  [f"3|carottes|{CAROTTE}|2", f"2|pommes de terre|{PDT}|2", "1|courgette|Courgette|1", "1|poireau|Poireau|1", f"1 L|de bouillon de légumes|{BOUILLON}|2", "80 g|de pâtes alphabet|Pâtes sèches (spaghetti, penne…)|2", f"10 g|de beurre|{BEURRE}|1"],
  ["**Cuire.** Légumes 25 min, mixés.", "**Pâtes.** 6 min dans la soupe. Beurre."], age=1, cats=["enfants"], profil=["leger"])
