# -*- coding: utf-8 -*-
"""Vague 2 · Le quotidien français (rapide, économique, de saison) et l'anti-gaspi."""
from recipes_v2_base import *

QF = "France › Cuisine du quotidien"; AG = "France › Anti-gaspi"

K("poireaux_vinaigrette", "Poireaux vinaigrette, œuf mimosa", "Poireaux vinaigrette", QF, "E", 1, 4, 15, 15, "€", "Casserole.",
  "Poireaux fondants tièdes, vinaigrette moutardée et œuf dur râpé : le bistrot à la maison.",
  ["8|petits poireaux|Poireau|3", f"2|œufs durs|{OEUF}|2", f"1 c. à s.|de moutarde|{DIJON}|1", "2 c. à s.|de vinaigre de vin|Vinaigre de vin rouge / blanc|1", f"6 c. à s.|d'huile|{HN}|2", "1 c. à s.|de ciboulette|Ciboulette|1"],
  ["**Cuire.** Poireaux ficelés, 12-15 min à l'eau salée ; égouttés.", "**Vinaigrette.** Moutarde, vinaigre, sel, huile.", "**Servir.** Tièdes, vinaigrette, œuf râpé, ciboulette."],
  age=1, cats=["zero_dechet"], profil=["leger", "acide"], tips=["Les verts de poireaux : soupe, bouillon cube maison, quiche."])

K("celeri_remoulade", "Céleri rémoulade", "Céleri rémoulade", QF, "E", 1, 4, 15, 30, "€", "Râpe fine.",
  "Céleri-rave râpé dans une mayonnaise moutardée : croquant, frais, de l'automne au printemps.",
  ["½|céleri-rave|Céleri-rave|3", f"4 c. à s.|de mayonnaise|SUB:mayonnaise|2", f"1 c. à s.|de moutarde|{DIJON}|1", f"½|citron|{CIT}|1", f"1 c. à s.|de persil|{PERSIL}|0"],
  ["**Râper.** Finement, citronné aussitôt (il noircit).", "**Mélanger.** Mayonnaise, moutarde, sel ; 30 min au frais."], age=3, profil=["gras"])

K("carottes_rapees", "Carottes râpées à l'orange", "Carottes râpées", QF, "E", 1, 4, 10, 0, "€", "Râpe.",
  "Carottes râpées, jus d'orange, huile et raisins secs : sucré-acidulé, les enfants adorent.",
  [f"500 g|de carottes|{CAROTTE}|3", "1|orange|Orange|2", f"3 c. à s.|d'huile d'olive|{HO}|1", "40 g|de raisins secs|Raisins secs|1", f"1 c. à s.|de persil|{PERSIL}|0"],
  ["**Râper.** Finement.", "**Assaisonner.** Jus d'orange, huile, sel, raisins."], age=1, cats=["enfants"], profil=["leger"])

K("taboule_semoule", "Taboulé à la semoule (façon française)", "Taboulé à la française", QF, "E", 1, 6, 20, 60, "€", "Saladier.",
  "La version française du taboulé : semoule, tomates, concombre, menthe, citron et huile d'olive.",
  ["250 g|de semoule moyenne|Semoule de blé (fine/moyenne)|3", f"3|tomates|{TOM}|2", "1|concombre|Concombre|2", "1 bouquet|de menthe|Menthe|2", f"1 bouquet|de persil|{PERSIL}|1", f"2|citrons|{CIT}|2", f"6 c. à s.|d'huile d'olive|{HO}|2"],
  ["**Gonfler.** Semoule + jus de citron + huile + 20 cl d'eau froide salée, 30 min.", "**Mélanger.** Légumes en dés, herbes ; 30 min au frais."],
  age=1, cats=["enfants"], fetes=["Barbecue d'été"], profil=["leger"])

K("salade_lentilles", "Salade de lentilles, échalote et moutarde", "Salade de lentilles", QF, "E", 1, 4, 10, 25, "€", "Casserole.",
  "Lentilles vertes tièdes, vinaigrette moutardée, échalote, carotte et persil : simple et rassasiant.",
  ["250 g|de lentilles vertes|Lentilles vertes / brunes|3", f"1|carotte|{CAROTTE}|1", f"2|échalotes|{ECH}|1", f"1 c. à s.|de moutarde|{DIJON}|1", "2 c. à s.|de vinaigre de xérès|Vinaigre de xérès|1", f"5 c. à s.|d'huile|{HN}|1", f"1 bouquet|de persil|{PERSIL}|1"],
  ["**Cuire.** Lentilles et carotte en dés, eau froide, 20-25 min ; sel en fin.", "**Assaisonner.** Tièdes avec vinaigrette, échalotes, persil."], age=1, profil=["leger"])

K("soupe_poireaux_pdt", "Soupe poireaux-pommes de terre", "Potage parmentier", QF, "So", 1, 6, 15, 30, "€", "Faitout, mixeur.",
  "La soupe la plus simple : poireaux fondus, pommes de terre, un peu de crème. Douce et veloutée.",
  ["3|poireaux|Poireau|3", f"4|pommes de terre|{PDT}|3", f"30 g|de beurre|{BEURRE}|1", f"10 cl|de crème|{CF}|1", f"1,2 L|d'eau ou de bouillon|{BOUILLON}|1"],
  ["**Fondre.** Poireaux au beurre 10 min.", "**Cuire.** Pommes de terre, eau, 20 min ; mixe, crème."], age=1, cats=["enfants"], profil=["leger"], kids="✓ dès 6 mois, sans sel ni crème.")

K("veloute_champignons", "Velouté de champignons", "Velouté de champignons", QF, "So", 1, 4, 15, 25, "€", "Casserole, mixeur.",
  "Champignons dorés d'abord (c'est le goût), puis mixés avec bouillon et crème : soyeux.",
  ["500 g|de champignons|Champignon de Paris|3", f"1|oignon|{OIG}|1", f"1|pomme de terre|{PDT}|1", f"80 cl|de bouillon|{BOUILLON}|2", f"10 cl|de crème|{CF}|2", f"20 g|de beurre|{BEURRE}|1"],
  ["**Dorer.** Champignons à feu vif au beurre, oignon.", "**Cuire.** Pomme de terre, bouillon, 20 min ; mixe, crème."], age=1, cats=["enfants"], profil=["gras"])

K("cake_sale", "Cake salé olives-feta-tomates séchées", "Cake salé", QF, "P", 1, 8, 15, 45, "€", "Moule à cake.",
  "Le cake des pique-niques et apéritifs : base unique, garnitures à volonté (restes compris).",
  [f"180 g|de farine|{F55}|3", f"3|œufs|{OEUF}|2", f"10 cl|de lait|{LAIT}|1", f"10 cl|d'huile d'olive|{HO}|1", f"1 sachet|de levure|{LEVC}|1", "100 g|de feta|Feta|2", "80 g|d'olives|Olives (vertes / noires)|1", "60 g|de tomates séchées|Tomate|1", f"80 g|de fromage râpé|{GRUY}|1"],
  ["**Pâte.** Farine + levure, œufs, lait, huile.", "**Garnir.** Tout en dés.", "**Cuire.** 45 min à 180 °C."],
  age=1, cats=["enfants", "zero_dechet"], fetes=["Apéritif dînatoire"], profil=["gras"])

K("tarte_tomates_moutarde", "Tarte fine tomates-moutarde", "Tarte à la tomate", QF, "P", 1, 6, 15, 35, "€", "Moule à tarte.",
  "Pâte brisée, moutarde, tomates en rondelles, herbes de Provence, huile d'olive : l'été en tarte.",
  ["1|pâte brisée|SUB:pate_brisee|3", f"6|tomates|{TOM}|3", f"3 c. à s.|de moutarde|{DIJON}|2", f"80 g|de fromage râpé|{GRUY}|1", "1 c. à c.|d'herbes de Provence|Herbes de Provence|1", f"2 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Monter.** Pâte, moutarde, fromage, tomates épongées en rosace.", "**Cuire.** 35 min à 200 °C, herbes, huile."], age=3, cats=["enfants"], profil=["acide"])

K("gratin_courgettes", "Gratin de courgettes", "Gratin de courgettes", QF, "A", 1, 4, 15, 35, "€", "Plat à gratin.",
  "Courgettes poêlées puis gratinées dans une crème aux œufs et au fromage.",
  ["1 kg|de courgettes|Courgette|3", f"2|œufs|{OEUF}|2", f"20 cl|de crème|{CF}|2", f"80 g|de fromage râpé|{GRUY}|2", f"1 gousse|d'ail|{AIL}|1", f"2 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Poêler.** Rondelles 10 min (elles rendent leur eau), ail.", "**Gratiner.** Œufs + crème + fromage, 25 min à 190 °C."], age=1, cats=["enfants"], profil=["leger"])

K("tian_provencal", "Tian provençal", "Tian", "France › Provence-Alpes-Côte d'Azur", "A", 1, 6, 20, 60, "€", "Plat à four.",
  "Rondelles de courgettes, tomates et aubergines en rangs serrés sur un lit d'oignons, rôties à l'huile d'olive.",
  ["2|courgettes|Courgette|2", f"4|tomates|{TOM}|2", "1|aubergine|Aubergine|2", f"2|oignons|{OIG}|1", f"2 gousses|d'ail|{AIL}|1", "1 c. à c.|d'herbes de Provence|Herbes de Provence|1", f"6 c. à s.|d'huile d'olive|{HO}|2"],
  ["**Lit.** Oignons fondus au fond.", "**Ranger.** Rondelles alternées debout.", "**Cuire.** Huile, herbes, sel, 1 h à 180 °C."], age=1, cats=["enfants"], fetes=["Barbecue d'été"], profil=["leger"])

K("endives_jambon_dinde", "Endives au jambon (de dinde), béchamel", "Chicons au gratin", "France › Hauts-de-France", "P", 1, 4, 20, 35, "€", "Plat à gratin.",
  "Endives fondantes roulées dans du jambon, nappées de béchamel au fromage : le gratin du Nord. Version jambon de dinde.",
  ["8|endives|Endive|3", "8 tranches|de jambon de dinde|Jambon de dinde / de poulet|2", "1|recette de béchamel|SUB:bechamel|3", f"100 g|de fromage râpé|{GRUY}|2", f"1 c. à c.|de sucre|{SUCRE}|0"],
  ["**Endives.** Braisées 20 min à couvert avec beurre et une pincée de sucre (moins amères) ; pressées.", "**Rouler.** Dans le jambon.", "**Gratiner.** Béchamel, fromage, 25 min à 200 °C."],
  age=1, cats=["enfants"], profil=["gras"])

K("lentilles_saucisses", "Lentilles aux saucisses (de volaille)", "Petit salé aux lentilles (version volaille)", QF, "P", 1, 4, 15, 40, "€", "Cocotte.",
  "Lentilles vertes mijotées avec carottes et saucisses fumées de volaille : le goût du petit salé sans porc.",
  ["300 g|de lentilles vertes|Lentilles vertes / brunes|3", "6|saucisses de volaille fumées|Saucisse de bœuf / de veau / de volaille|3", f"2|carottes|{CAROTTE}|1", f"1|oignon piqué de girofle|{OIG}|1", f"1|bouquet garni|{LAURIER}|1", f"1 c. à c.|de paprika fumé|{PFUME}|1"],
  ["**Mijoter.** Lentilles, légumes, bouquet garni, paprika fumé, eau à hauteur ×2, 25 min.", "**Saucisses.** Piquées, 15 min dedans."], age=1, cats=["enfants"], profil=["leger"])

K("croquettes_restes", "Croquettes de restes (purée, viande, fromage)", "Croquettes de restes", AG, "P", 1, 4, 20, 10, "€", "Poêle, 3 assiettes.",
  "Purée de la veille, restes de viande ou de légumes et fromage, panés et dorés : les restes deviennent un plat à part entière.",
  [f"400 g|de purée (reste)|{PDT}|3", "200 g|de restes de viande, poisson ou légumes|-|2", f"60 g|de fromage râpé|{GRUY}|1", f"2|œufs|{OEUF}|1", "80 g|de chapelure (pain rassis mixé)|Chapelure|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Mélanger.** Purée, restes hachés, fromage, 1 œuf.", "**Paner.** Boulettes, œuf, chapelure.", "**Dorer.** 3 min par face."],
  age=1, cats=["enfants", "zero_dechet"], profil=["gras"], tech=["Paner"])

K("chips_epluchures", "Chips d'épluchures", "Chips d'épluchures", AG, "A", 1, 4, 10, 15, "€", "Plaque, four.",
  "Les pelures de pommes de terre, carottes, panais, bien lavées : croustillantes au four avec sel et paprika.",
  ["300 g|d'épluchures de légumes bio bien lavés|Pomme de terre|3", f"2 c. à s.|d'huile d'olive|{HO}|2", f"1 c. à c.|de paprika fumé|{PFUME}|1", "1 c. à c.|de fleur de sel|Sel fin / gros sel / fleur de sel|0"],
  ["**Sécher.** Épluchures bien épongées.", "**Cuire.** Huile, épices, en une couche, 12-15 min à 200 °C en remuant."], age=3, cats=["zero_dechet", "enfants"], profil=["gras"], tips=["Pas d'épluchures de pommes de terre vertes ou germées (solanine)."])

K("soupe_fanes", "Soupe de fanes de radis ou de carottes", "Soupe de fanes", AG, "So", 1, 4, 10, 20, "€", "Casserole, mixeur.",
  "Les fanes qu'on jette ont un goût de légume concentré : avec une pomme de terre, une soupe verte et poivrée.",
  ["2 bottes|de fanes de radis ou carottes|Radis rose|3", f"2|pommes de terre|{PDT}|2", f"1|oignon|{OIG}|1", f"1 L|de bouillon|{BOUILLON}|2", f"5 cl|de crème|{CF}|1"],
  ["**Cuire.** Oignon, pommes de terre, bouillon 15 min ; fanes lavées 5 min.", "**Mixer.** Crème."], age=1, cats=["zero_dechet"], profil=["leger"])

K("pain_perdu_sale", "Pain perdu salé (croque du lendemain)", "Pain perdu salé", AG, "P", 1, 4, 10, 10, "€", "Poêle.",
  "Pain rassis trempé dans les œufs battus au lait et fromage, doré : avec une salade, un dîner en 15 minutes.",
  ["8 tranches|de pain rassis|Pain rassis (réservé)|3", f"3|œufs|{OEUF}|2", f"20 cl|de lait|{LAIT}|1", f"80 g|de fromage râpé|{GRUY}|2", "1 c. à s.|d'herbes|Ciboulette|1", f"20 g|de beurre|{BEURRE}|1"],
  ["**Tremper.** Œufs, lait, fromage, herbes, sel, poivre.", "**Dorer.** 3 min par face au beurre."], age=1, cats=["zero_dechet", "enfants"], profil=["gras"])

K("croutons_chapelure", "Croûtons et chapelure maison", "Croûtons", AG, "Ba", 1, 6, 10, 15, "€", "Plaque, mixeur.",
  "Le pain rassis devient croûtons à l'ail pour soupes et salades, ou chapelure pour paner et gratiner.",
  ["300 g|de pain rassis|Pain rassis (réservé)|3", f"3 c. à s.|d'huile d'olive|{HO}|2", f"1 gousse|d'ail|{AIL}|1", "1 c. à c.|d'herbes de Provence|Herbes de Provence|1"],
  ["**Croûtons.** Dés, huile, ail, herbes, 12 min à 180 °C.", "**Chapelure.** Pain séché au four 20 min à 120 °C puis mixé ; bocal."],
  keep="Croûtons 1 semaine ; chapelure 2 mois au sec.", age=1, cats=["zero_dechet"], profil=["gras"])

K("quiche_frigo_vide", "Quiche frigo-vide", "Quiche aux restes", AG, "P", 1, 6, 15, 40, "€", "Moule à tarte.",
  "La base crème-œufs qui accueille tous les restes : légumes cuits, fromage en fin de vie, viande, herbes.",
  ["1|pâte brisée|SUB:pate_brisee|3", f"3|œufs|{OEUF}|2", f"20 cl|de crème ou lait|{CF}|2", "300 g|de restes (légumes, viande, poisson)|-|2", f"80 g|de fromage (fonds de frigo)|{GRUY}|2", f"1 pincée|de muscade|{MUSC}|0"],
  ["**Garnir.** Restes en dés sur la pâte.", "**Appareil.** Œufs, crème, fromage, muscade, sel.", "**Cuire.** 40 min à 180 °C."],
  age=1, cats=["zero_dechet", "enfants"], profil=["gras"])

K("gratin_pates_restes", "Gratin de pâtes de la veille", "Gratin de pâtes", AG, "P", 1, 4, 10, 20, "€", "Plat à gratin.",
  "Pâtes cuites, un fond de sauce tomate ou de crème, des légumes, du fromage : gratinées, elles sont meilleures que la veille.",
  [f"500 g|de pâtes cuites|{PATES}|3", f"20 cl|de crème ou sauce tomate|{CF}|2", f"2|œufs|{OEUF}|1", f"100 g|de fromage râpé|{GRUY}|2", "150 g|de légumes ou de viande en restes|Courgette|1?"],
  ["**Mélanger.** Pâtes, crème + œufs, restes.", "**Gratiner.** Fromage, 20 min à 200 °C."], age=1, cats=["zero_dechet", "enfants"], profil=["gras"])

K("confiture_peaux_bananes", "Chutney de peaux de bananes", "Chutney de peaux de banane", AG, "S", 2, 8, 20, 40, "€", "Casserole.",
  "Les peaux de bananes bio, bouillies puis cuites avec oignon, épices et vinaigre : un chutney surprenant, inspiré des cuisines indiennes.",
  ["4|peaux de bananes bio bien lavées|Banane|3", f"1|oignon|{OIG}|1", "5 cl|de vinaigre de cidre|Vinaigre de cidre|1", "60 g|de cassonade|Sucre blanc / roux / cassonade / vergeoise|2", f"1 morceau|de gingembre|{GING}|1", f"½ c. à c.|de curcuma + cumin|{CURC}|1"],
  ["**Blanchir.** Peaux sans les extrémités, 10 min ; hachées.", "**Cuire.** Avec oignon, épices, sucre, vinaigre, 30 min."], keep="2 semaines au frigo.", age=3, cats=["zero_dechet", "sauces"], profil=["sucre", "acide"])

K("bouillon_parures", "Bouillon de parures (carcasses, arêtes, croûtes)", "Bouillon de parures", AG, "Ba", 1, 8, 10, 120, "€", "Faitout.",
  "Carcasse de poulet rôti, croûte de parmesan, queues de persil, fanes : on garde tout dans un sac au congélateur, et on fait ce bouillon.",
  ["1|carcasse de poulet (rôti ou cru)|Canard entier / carcasse|3", "1|croûte de parmesan|Parmesan / Parmigiano|1", "500 g|de parures de légumes (fanes, queues, verts de poireau)|Poireau|2", f"1|oignon avec la peau (couleur)|{OIG}|1", f"1|bouquet garni|{LAURIER}|1"],
  ["**Cuire.** Tout, 2,5 L d'eau froide, frémissement 2 h, écume.", "**Filtrer.** Refroidis vite, dégraisse."], keep="4 jours ou 3 mois congelé.", age=1, cats=["zero_dechet"], profil=["leger"], tech=["Bouillon"])

K("tartinade_fanes_pois", "Houmous de petits pois et fanes", "Houmous de petits pois", AG, "E", 1, 6, 10, 5, "€", "Mixeur.",
  "Petits pois, tahini, citron, menthe et les cosses tendres ou les fanes : une tartinade verte de printemps.",
  ["300 g|de petits pois|Petits pois / pois gourmands|3", "2 c. à s.|de tahini|Tahini (purée de sésame)|2", f"1|citron|{CIT}|1", "6|feuilles de menthe|Menthe|1", f"1 gousse|d'ail|{AIL}|1", f"4 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Cuire.** Petits pois 4 min, eau glacée.", "**Mixer.** Tout, sel."], age=1, cats=["zero_dechet", "enfants"], fetes=["Apéritif dînatoire"], profil=["leger"])

K("riz_saute_restes", "Riz sauté du frigo", "Riz sauté", AG, "P", 1, 2, 10, 10, "€", "Wok ou poêle.",
  "Le riz froid de la veille, un œuf, les fonds de légumes et un peu de sauce soja : le dîner anti-gaspi en 10 minutes.",
  [f"400 g|de riz cuit froid|{RIZ}|3", f"2|œufs|{OEUF}|2", "200 g|de restes de légumes (petits pois, carottes, poivron)|Petits pois / pois gourmands|2", f"2 c. à s.|de sauce soja|{SOJA}|2", "2|oignons nouveaux|Oignon nouveau / cébette|1", f"2 c. à s.|d'huile|{HN}|1"],
  ["**Œufs.** Brouillés vite, réservés.", "**Sauter.** Légumes, riz à feu vif 4 min, soja.", "**Finir.** Œufs, oignons."], age=1, cats=["zero_dechet", "enfants"], profil=["leger"], tech=["Sauter au wok"])

K("gateau_pain_rassis", "Pudding au pain rassis (diplomate des familles)", "Pudding", AG, "D", 1, 8, 15, 45, "€", "Moule.",
  "Pain ou brioche rassis, lait, œufs, sucre et raisins : le gâteau anti-gaspi de toutes les grands-mères.",
  ["300 g|de pain ou brioche rassis|Pain rassis (réservé)|3", f"50 cl|de lait|{LAIT}|2", f"3|œufs|{OEUF}|2", f"100 g|de sucre|{SUCRE}|2", "60 g|de raisins secs|Raisins secs|1", f"1 pincée|de cannelle|{CANN}|0"],
  ["**Tremper.** Pain dans le lait chaud, 15 min ; écrase.", "**Mélanger.** Œufs, sucre, raisins.", "**Cuire.** Moule caramélisé ou beurré, 45 min à 180 °C."], age=1, cats=["zero_dechet", "enfants"], profil=["sucre"])

K("smoothie_fruits_abimes", "Compote-smoothie des fruits abîmés", "Smoothie anti-gaspi", AG, "B", 1, 4, 10, 0, "€", "Mixeur.",
  "Fruits trop mûrs ou talés, débarrassés des parties abîmées, mixés avec un yaourt : rien ne se perd.",
  ["500 g|de fruits trop mûrs (bananes, pommes, poires, fraises)|Banane|3", f"250 g|de yaourt|{YAO}|2", f"20 cl|de lait|{LAIT}|1", f"1 c. à c.|de miel (facultatif)|{MIEL}|0?"],
  ["**Mixer.** Tout. Se congèle en bâtonnets glacés."], age=1, cats=["zero_dechet", "boissons", "enfants"], profil=["sucre"])
