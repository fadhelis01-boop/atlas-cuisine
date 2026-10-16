# -*- coding: utf-8 -*-
"""Vague 3 · Salades complètes, un repas à elles seules (audit UX du 16/10/2026 : « ≈ 14 salades complètes »).
Chaque salade associe des légumes, un féculent ou une légumineuse et une protéine. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

QF = "France › Cuisine du quotidien"; US = "Amérique du Nord › États-Unis"; IT = "Europe du Sud › Italie"
SA = ["salade"]

K("salade_cesar_poulet", "Salade César au poulet", "Caesar salad", "Amérique latine › Mexique › Tijuana", "P", 1, 4, 25, 10, "€€", "Poêle, saladier.",
  "Inventée à Tijuana en 1924 : romaine croquante, poulet doré, croûtons à l'ail, parmesan et la sauce César crémeuse au citron.",
  ["1|grosse laitue romaine|Salade (laitue, batavia)|3", f"2|blancs de poulet|{BLANC_P}|3", "3 tranches|de pain rassis|Pain rassis (réservé)|2", f"60 g|de parmesan|{PARM}|2", f"1|jaune d'œuf (ou 3 c. à s. de mayonnaise)|Jaune d'œuf|2", f"1 c. à c.|de moutarde|{DIJON}|1", f"1|citron|{CIT}|1", f"1 gousse|d'ail|{AIL}|1", "4|filets d'anchois (facultatif)|Anchois (filets, conserve)|1?", f"8 c. à s.|d'huile d'olive|{HO}|2"],
  ["**Sauce.** Jaune, moutarde, ail râpé, jus de citron, anchois écrasés ; huile en filet en fouettant : épaisse ; 2 c. à s. de parmesan.",
   "**Croûtons et poulet.** Pain en dés doré à la poêle avec un peu d'huile et d'ail ; poulet saisi 5-6 min par face, tranché.",
   "**Dresser.** Romaine en morceaux enrobée de sauce, poulet, croûtons, copeaux de parmesan."],
  age=3, cats=SA + ["zero_dechet"], profil=["gras"], tips=["Sans anchois, la sauce reste bonne : ajoute 1 c. à c. de câpres hachées pour le côté salé."])

K("salade_quinoa_feta_grenade", "Salade de quinoa, feta, grenade et herbes", "Salade de quinoa", "Moyen-Orient › Food fusion", "P", 1, 4, 20, 12, "€€", "Casserole, saladier.",
  "Quinoa, concombre, herbes, feta, grenade et pistaches, vinaigrette citron-mélasse de grenade : fraîche, colorée, végétarienne.",
  ["200 g|de quinoa|Quinoa|3", "150 g|de feta|Feta|2", "1|grenade|Grenade|2", "½|concombre|Concombre|1", f"1 bouquet|de persil|{PERSIL}|1", "½ bouquet|de menthe|Menthe|1", "40 g|de pistaches|Pistache|1?", f"1|citron|{CIT}|1", f"4 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Cuire.** Quinoa rincé, 12 min à l'eau salée ; égoutté et refroidi.", "**Tailler.** Concombre en dés, herbes hachées, grains de grenade.", "**Assembler.** Jus de citron, huile, sel ; feta émiettée et pistaches au dernier moment."],
  age=3, cats=SA, profil=["leger", "acide"])

K("salade_pates_pesto_tomates", "Salade de pâtes au pesto, tomates et mozzarella", "Insalata di pasta", IT, "P", 1, 4, 15, 10, "€", "Casserole, saladier.",
  "Pâtes courtes, pesto, tomates cerises, mozzarella et roquette : la salade de pique-nique que tout le monde aime.",
  [f"300 g|de pâtes courtes|{PATES}|3", "4 c. à s.|de pesto|Pesto (bocal)|2", "250 g|de tomates cerises|Tomate cerise|2", "1 boule|de mozzarella|Mozzarella / burrata|2", "1 poignée|de roquette|Roquette / mâche|1", f"2 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Cuire.** Pâtes al dente, rincées à l'eau froide, égouttées, un filet d'huile.", "**Mélanger.** Pesto, tomates coupées, mozzarella en dés.", "**Servir.** Roquette au dernier moment."],
  age=1, cats=SA + ["enfants"], fetes=["Barbecue d'été"])

K("salade_riz_thon_mais", "Salade de riz, thon, maïs et œufs", "Salade de riz", QF, "P", 1, 4, 15, 12, "€", "Casserole, saladier.",
  "La salade de riz des étés français : thon, maïs, tomates, poivron, œufs durs et vinaigrette moutardée.",
  [f"250 g|de riz|{RIZ}|3", "1 boîte|de thon|Thon en conserve|2", "150 g|de maïs|Maïs doux|2", f"2|tomates|{TOM}|1", f"1|poivron|{POIVRON}|1", f"3|œufs durs|{OEUF}|2", f"1 c. à s.|de moutarde|{DIJON}|1", "2 c. à s.|de vinaigre|Vinaigre de vin rouge / blanc|1", f"6 c. à s.|d'huile|{HN}|1"],
  ["**Riz.** Cuit à l'eau salée, rincé à l'eau froide, bien égoutté.", "**Vinaigrette.** Moutarde, vinaigre, sel, huile.", "**Mélanger.** Riz, thon, maïs, légumes en dés, œufs en quartiers."],
  age=1, cats=SA + ["enfants"], fetes=["Barbecue d'été"], profil=["poisson"])

K("salade_pois_chiches_concombre", "Salade de pois chiches, concombre et herbes", "Salatet hummus", "Moyen-Orient › Israël", "P", 1, 4, 15, 0, "€", "Saladier.",
  "Pois chiches, tomates, concombre, oignon rouge, persil, sumac et citron : sans cuisson, protéinée, végétarienne.",
  [f"2 boîtes|de pois chiches|{POIS}|3", f"2|tomates|{TOM}|2", "1|concombre|Concombre|2", "½|oignon rouge|Oignon rouge|1", f"1 bouquet|de persil|{PERSIL}|1", "1 c. à c.|de sumac|Sumac|1?", f"1|citron|{CIT}|1", f"4 c. à s.|d'huile d'olive|{HO}|1", "100 g|de feta (facultatif)|Feta|1?"],
  ["**Tailler.** Légumes en petits dés, persil haché.", "**Assaisonner.** Pois chiches rincés, citron, huile, sel, sumac.", "**Reposer.** 10 min : les saveurs se mélangent."],
  age=3, cats=SA, profil=["leger", "acide"])

K("salade_poulet_mangue_thai", "Salade thaïe au poulet et à la mangue", "Yam kai mamuang", "Asie du Sud-Est › Thaïlande", "P", 1, 4, 20, 10, "€€", "Poêle, saladier.",
  "Poulet grillé, mangue, chou, carotte, herbes et cacahuètes, sauce citron vert-sauce de poisson-piment : sucré, acide, salé, piquant.",
  [f"2|blancs de poulet|{BLANC_P}|3", "1|mangue ferme|Mangue|2", "¼|chou chinois|Chou chinois / pak-choï|2", f"1|carotte|{CAROTTE}|1", f"½ bouquet|de coriandre|{CORI}|1", "½ bouquet|de menthe|Menthe|1", "40 g|de cacahuètes|Cacahuète / arachide|1", f"2|citrons verts|{CITV}|2", "2 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|2", f"1|piment|{PIMENT}|1?"],
  ["**Poulet.** Saisi 6 min par face, tranché.", "**Sauce.** Citron vert, sauce de poisson, 1 c. à s. de sucre, piment haché.", "**Assembler.** Légumes et mangue en lanières, herbes, poulet, sauce, cacahuètes concassées."],
  age=6, cats=SA, profil=["acide", "epice", "leger"])

K("salade_soba_sesame", "Salade de nouilles soba au sésame", "Soba salad", "Asie de l'Est › Japon", "P", 1, 4, 15, 5, "€", "Casserole, saladier.",
  "Nouilles de sarrasin froides, edamame, concombre, carotte et sauce sésame-soja-vinaigre de riz : fraîche et végétarienne.",
  ["250 g|de nouilles soba|Nouilles soba|3", "150 g|d'edamame|Edamame|2", "½|concombre|Concombre|1", f"1|carotte|{CAROTTE}|1", f"3 c. à s.|de sauce soja|{SOJA}|2", "2 c. à s.|de vinaigre de riz|Vinaigre de riz|1", "1 c. à s.|d'huile de sésame|Huile de sésame (grillée)|1", "1 c. à s.|de sésame|Sésame (blanc/noir)|1", f"2|cébettes|Oignon nouveau / cébette|1"],
  ["**Cuire.** Soba 4-5 min, rincées à l'eau froide en les frottant : elles ne collent plus.", "**Sauce.** Soja, vinaigre, huile de sésame, 1 c. à c. de sucre.", "**Mélanger.** Légumes en julienne, edamame, sauce, sésame, cébette."],
  age=3, cats=SA, profil=["leger"])

K("salade_betterave_chevre_noix", "Salade de betterave, chèvre, noix et lentilles", "Salade betterave-chèvre", QF, "P", 1, 4, 15, 20, "€", "Casserole, saladier.",
  "Lentilles tièdes, betterave, chèvre frais, noix et vinaigrette au miel : le goût de l'automne, complet et végétarien.",
  ["150 g|de lentilles vertes|Lentilles vertes / brunes|3", "2|betteraves cuites|Betterave (crue/cuite)|2", "120 g|de chèvre frais|Chèvre (frais, bûche)|2", "40 g|de noix|Noix|1", "1 poignée|de mâche|Roquette / mâche|1", f"1 c. à c.|de miel|{MIEL}|1", f"1 c. à s.|de vinaigre de cidre|{CIDRE}|1", "3 c. à s.|d'huile de noix|Huile de noix / de noisette|1"],
  ["**Lentilles.** 20 min à l'eau frémissante (sel à la fin) : tendres mais entières.", "**Vinaigrette.** Miel, vinaigre, sel, huile de noix.", "**Assembler.** Lentilles tièdes assaisonnées, betterave en dés, mâche, chèvre émietté, noix."],
  age=3, cats=SA, profil=["leger"])

K("salade_piemontaise", "Salade piémontaise", "Salade piémontaise", QF, "P", 1, 4, 20, 20, "€", "Casserole, saladier.",
  "Pommes de terre tièdes, œufs durs, tomates, cornichons, jambon de dinde et sauce mayonnaise : le classique des cantines, version maison.",
  [f"800 g|de pommes de terre|{PDT}|3", f"3|œufs durs|{OEUF}|2", f"2|tomates|{TOM}|1", "6|cornichons|Cornichon|1", "120 g|de jambon de dinde (ou blanc)|Jambon de dinde / de poulet|2", "4 c. à s.|de mayonnaise|SUB:mayonnaise|2", f"1 c. à s.|de persil|{PERSIL}|0"],
  ["**Cuire.** Pommes de terre en dés, 15 min à l'eau salée : tendres (la lame entre sans forcer).", "**Mélanger.** Encore tièdes, avec la mayonnaise allongée d'1 c. à s. de vinaigre.", "**Ajouter.** Œufs, tomates, cornichons, jambon en dés, persil."],
  age=1, cats=SA + ["enfants"])

K("salade_cobb", "Salade Cobb", "Cobb salad", f"{US} › Hollywood", "P", 1, 4, 20, 12, "€€", "Poêle, saladier.",
  "Rangs de poulet, œuf dur, avocat, tomate, bleu et bacon de dinde sur salade, vinaigrette moutardée : la salade d'Hollywood (1937).",
  ["1|laitue|Salade (laitue, batavia)|2", f"2|blancs de poulet|{BLANC_P}|3", f"3|œufs durs|{OEUF}|2", "1|avocat|Avocat|2", f"2|tomates|{TOM}|1", "80 g|de bleu|Roquefort / bleu|1", "6 tranches|de bacon de dinde|Bacon de dinde / de bœuf|1?", f"1 c. à c.|de moutarde|{DIJON}|1", f"5 c. à s.|d'huile|{HN}|1", "2 c. à s.|de vinaigre de vin|Vinaigre de vin rouge / blanc|1"],
  ["**Cuire.** Poulet saisi, en dés ; bacon croustillant à la poêle, émietté.", "**Tailler.** Tout en dés réguliers.", "**Dresser.** En rangs sur la salade ; vinaigrette à part, mélangée à table."],
  age=3, cats=SA, profil=["gras"])

K("salade_kale_parmesan", "Salade de chou kale, parmesan et pommes", "Kale salad", f"{US} › Californie", "E", 1, 4, 15, 0, "€", "Saladier.",
  "Le kale massé au citron devient tendre ; pomme croquante, parmesan, graines de courge : une salade d'hiver vitaminée.",
  ["1 botte|de chou kale|Chou vert / frisé / kale|3", "1|pomme|Pomme|2", f"40 g|de parmesan|{PARM}|2", "30 g|de graines de courge|Graines de tournesol / courge|1", f"1|citron|{CIT}|1", f"4 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Masser.** Feuilles sans les côtes, émincées, frottées 2 min avec citron, huile et sel : elles foncent et s'attendrissent.", "**Ajouter.** Pomme en lamelles, copeaux de parmesan, graines grillées."],
  age=3, cats=SA, profil=["leger", "acide"])

K("salade_avocat_crevettes", "Salade avocat, crevettes et pamplemousse", "Salade de crevettes", QF, "E", 1, 4, 15, 0, "€€", "Saladier.",
  "Crevettes, avocat, pamplemousse rose et roquette, sauce citron-ciboulette : fraîche, chic et sans cuisson.",
  ["300 g|de crevettes cuites décortiquées|Crevettes (cuites/crues)|3", "2|avocats|Avocat|2", "1|pamplemousse rose|Pamplemousse|2", "2 poignées|de roquette|Roquette / mâche|1", f"1|citron vert|{CITV}|1", "1 c. à s.|de ciboulette|Ciboulette|1", f"3 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Peler.** Pamplemousse à vif, en suprêmes (sans peau blanche).", "**Tailler.** Avocat en tranches, citronné.", "**Dresser.** Roquette, avocat, crevettes, pamplemousse ; citron vert, huile, sel, ciboulette."],
  age=3, cats=SA, fetes=["Noël", "Saint-Valentin"], profil=["poisson", "leger", "acide"], tech=["peler à vif"])

K("salade_couscous_perle_herbes", "Salade de couscous perlé, légumes rôtis et herbes", "Moghrabieh salad", "Moyen-Orient › Liban", "P", 1, 4, 20, 25, "€", "Four, casserole.",
  "Grosses perles de semoule, légumes rôtis, herbes, citron et feta : une salade tiède et généreuse.",
  ["250 g|de couscous perlé|Couscous perlé (moghrabieh)|3", "1|aubergine|Aubergine|2", f"1|poivron|{POIVRON}|2", "1|courgette|Courgette|1", f"1 bouquet|de persil|{PERSIL}|1", "100 g|de feta|Feta|1?", f"1|citron|{CIT}|1", f"5 c. à s.|d'huile d'olive|{HO}|2", f"1 c. à c.|de cumin|{CUMIN}|1"],
  ["**Rôtir.** Légumes en dés, huile, cumin, sel ; 200 °C, 25 min : dorés.", "**Cuire.** Couscous perlé 8-10 min à l'eau salée, égoutté, huilé.", "**Mélanger.** Tiède : légumes, herbes, citron, feta."],
  age=3, cats=SA, profil=["leger"])

K("salade_haricots_blancs_thon", "Salade de haricots blancs, thon et oignon rouge", "Insalata di fagioli e tonno", f"{IT} › Toscane", "P", 1, 4, 10, 0, "€", "Saladier.",
  "Haricots blancs, thon à l'huile, oignon rouge, persil et huile d'olive : la salade toscane du placard, prête en 10 minutes.",
  ["2 boîtes|de haricots blancs|Haricots blancs / lingots|3", "1 boîte|de thon à l'huile|Thon en conserve|3", "1|oignon rouge|Oignon rouge|2", f"1 bouquet|de persil|{PERSIL}|1", f"4 c. à s.|d'huile d'olive|{HO}|2", "1 c. à s.|de vinaigre de vin|Vinaigre de vin rouge / blanc|1"],
  ["**Oignon.** Émincé fin, 5 min dans le vinaigre : il s'adoucit.", "**Mélanger.** Haricots rincés, thon en gros morceaux, persil, huile, sel, poivre."],
  age=3, cats=SA, profil=["poisson"])

K("salade_tomates_burrata", "Salade de tomates anciennes et burrata", "Insalata di pomodori e burrata", f"{IT} › Pouilles", "E", 1, 4, 10, 0, "€€", "Plat.",
  "Tomates mûres de toutes les couleurs, burrata crémeuse, basilic, huile d'olive et fleur de sel : seulement en saison, avec du bon pain.",
  ["800 g|de tomates mûres (plusieurs variétés)|Tomate|3", "1|burrata (ou mozzarella)|Mozzarella / burrata|3", "1 bouquet|de basilic|Basilic|1", f"4 c. à s.|d'huile d'olive|{HO}|2", "1 c. à s.|de vinaigre balsamique|Vinaigre balsamique|1?"],
  ["**Tailler.** Tomates en tranches et quartiers, salées 5 min.", "**Dresser.** Burrata au centre, ouverte au dernier moment ; basilic, huile, poivre, balsamique."],
  age=1, cats=SA, fetes=["Barbecue d'été"], profil=["leger"])

K("salade_waldorf", "Salade Waldorf (pomme, céleri, noix)", "Waldorf salad", f"{US} › New York", "E", 1, 4, 15, 0, "€", "Saladier.",
  "Créée à l'hôtel Waldorf de New York en 1896 : pomme, céleri branche, raisin, noix et sauce yaourt-mayonnaise.",
  ["2|pommes|Pomme|3", "3 branches|de céleri|Céleri-branche|2", "150 g|de raisin|Raisin|1", "50 g|de noix|Noix|2", f"3 c. à s.|de yaourt|{YAO}|1", "2 c. à s.|de mayonnaise|SUB:mayonnaise|1", f"½|citron|{CIT}|1"],
  ["**Tailler.** Pommes en dés citronnés, céleri émincé, raisins coupés.", "**Lier.** Yaourt, mayonnaise, sel ; noix grillées au dernier moment."], age=3, cats=SA)

K("salade_concombre_sesame", "Concombre frappé à l'ail et au sésame", "Pāi huángguā", "Asie de l'Est › Chine › Sichuan", "E", 1, 4, 10, 10, "€", "Rouleau ou plat du couteau.",
  "Concombre écrasé (pas coupé : la sauce pénètre mieux), ail, vinaigre noir, huile pimentée et sésame : l'entrée froide du Sichuan.",
  ["2|concombres|Concombre|3", f"2 gousses|d'ail|{AIL}|2", "1 c. à s.|de vinaigre noir (ou de riz)|Vinaigre noir chinois (Chinkiang)|2", f"1 c. à s.|de sauce soja|{SOJA}|1", "1 c. à c.|d'huile pimentée|Huile pimentée chinoise|1?", "1 c. à c.|d'huile de sésame|Huile de sésame (grillée)|1", "1 c. à c.|de sésame|Sésame (blanc/noir)|0"],
  ["**Écraser.** Concombre frappé au rouleau, puis en morceaux ; salé 10 min, égoutté.", "**Assaisonner.** Ail, vinaigre, soja, sucre (1 pincée), huiles ; sésame."],
  age=6, cats=SA, profil=["acide", "leger"])

K("salade_mexicaine_haricots_mais", "Salade mexicaine haricots, maïs et avocat", "Ensalada mexicana", "Amérique latine › Mexique", "P", 1, 4, 15, 0, "€", "Saladier.",
  "Haricots rouges, maïs, poivron, tomate, avocat, citron vert et coriandre : colorée, végétarienne, sans cuisson.",
  ["400 g|de haricots rouges|Haricots rouges / noirs|3", "200 g|de maïs|Maïs doux|2", f"1|poivron|{POIVRON}|1", f"2|tomates|{TOM}|1", "1|avocat|Avocat|2", "½|oignon rouge|Oignon rouge|1", f"2|citrons verts|{CITV}|2", f"½ bouquet|de coriandre|{CORI}|1", f"1 c. à c.|de cumin|{CUMIN}|1"],
  ["**Tailler.** Tout en petits dés.", "**Assaisonner.** Citron vert, huile, cumin, sel.", "**Servir.** Avec des chips de tortilla."],
  age=3, cats=SA, fetes=["Barbecue d'été"], profil=["leger"])

K("salade_lentilles_saumon_fume", "Salade de lentilles au saumon fumé et à l'aneth", "Salade lentilles-saumon", QF, "P", 1, 4, 15, 20, "€€", "Casserole, saladier.",
  "Lentilles vertes tièdes, saumon fumé, échalote, aneth et crème citronnée : un plat de bistrot léger.",
  ["200 g|de lentilles vertes|Lentilles vertes / brunes|3", "150 g|de saumon fumé|Saumon fumé|3", f"1|échalote|{ECH}|1", "1 c. à s.|d'aneth|Aneth|1", f"3 c. à s.|de crème|{CF}|1", f"1|citron|{CIT}|1", f"1 c. à c.|de moutarde|{DIJON}|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Lentilles.** 20 min à frémissement, égouttées, salées tièdes.", "**Vinaigrette.** Moutarde, citron, huile, échalote hachée.", "**Assembler.** Lentilles assaisonnées, saumon en lanières, crème citronnée, aneth."],
  age=3, cats=SA, profil=["poisson"])

K("salade_patates_douces_poulet", "Salade tiède de patate douce rôtie, poulet et épinards", "Salade tiède", "Océanie › Nouvelle-Zélande", "P", 1, 4, 15, 25, "€", "Four, saladier.",
  "Patate douce rôtie au paprika, poulet, jeunes épinards, oignon rouge et sauce yaourt-citron : tiède et réconfortante.",
  ["2|patates douces|Patate douce|3", f"2|blancs de poulet|{BLANC_P}|3", "100 g|de jeunes épinards|Épinard|2", "½|oignon rouge|Oignon rouge|1", f"1 c. à c.|de paprika fumé|{PFUME}|1", f"4 c. à s.|de yaourt|{YAO}|1", f"1|citron|{CIT}|1"],
  ["**Rôtir.** Patates douces en cubes, huile, paprika, sel ; 200 °C, 25 min : dorées et tendres.", "**Poulet.** Saisi, tranché.", "**Assembler.** Épinards, patate tiède, poulet, oignon ; sauce yaourt-citron."],
  age=3, cats=SA, profil=["leger"])
