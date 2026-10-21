# -*- coding: utf-8 -*-
"""Vague 2 · France (2/3) : Est, Bourgogne, Alpes, Lyonnais, Provence, Corse."""
from recipes_v2_base import *

K("baeckeoffe_volaille", "Baeckeoffe de la semaine (version simple)", "Baeckeoffe", "France › Grand Est › Alsace", "P", 2, 6, 30, 180, "€€", "Grande cocotte en fonte avec couvercle, four.",
  "Viandes marinées, pommes de terre et oignons cuits ensemble très longtemps au four : tout fond. Ici en version bœuf-agneau, le porc d'origine étant facultatif.",
  [f"600 g|de paleron en cubes|Paleron|3", "600 g|d'épaule d'agneau en cubes|Épaule d'agneau|3", f"1,5 kg|de pommes de terre en rondelles|{PDT}|3", f"3|oignons|{OIG}|2",
   f"2|carottes|{CAROTTE}|1", f"1|poireau|Poireau|1", f"50 cl|de vin blanc d'Alsace|Vin blanc|2", f"2 gousses|d'ail|{AIL}|1", f"1|bouquet garni|{LAURIER}|1", f"1 c. à c.|de sel, poivre|{SEL}|0"],
  ["**Marinade.** La veille, mets les viandes avec oignons, ail, bouquet garni et vin au frais.", "**Couches.** Dans la cocotte : pommes de terre, viandes et légumes, pommes de terre, en salant chaque couche. Verse la marinade.",
   "**Cuisson.** Couvre (un cordon de pâte farine-eau autour du couvercle garde la vapeur) et enfourne 3 h à 160 °C (th. 5-6)."],
  keep="3 jours au frigo ; meilleur réchauffé.", age=3, profil=["viande_rouge"], fetes=["Repas de famille"], sa=["Jus de raisin blanc"], a=["Riesling"])

K("kougelhopf", "Kougelhopf (version facile)", "Kougelhopf", "France › Grand Est › Alsace", "G", 2, 10, 30, 180, "€", "Moule à kougelhopf ou à savarin, robot ou saladier.",
  "Une brioche aux raisins et aux amandes, sucrée de glace : le petit-déjeuner des dimanches alsaciens.",
  [f"500 g|de farine|{F45}|3", f"20 cl|de lait tiède|{LAIT}|2", f"2|œufs|{OEUF}|2", f"120 g|de beurre mou|{BEURRE}|2", f"80 g|de sucre|{SUCRE}|2",
   f"7 g|de levure boulangère|{LEV}|1", f"100 g|de raisins secs|Raisins secs|2", f"30 g|d'amandes entières|Amande (entière, effilée, poudre)|1", f"8 g|de sel|{SEL}|0", f"1 c. à s.|de sucre glace|Sucre glace|0"],
  ["**Pâte.** Pétris farine, lait, levure, œufs, sucre et sel 10 min ; ajoute le beurre, 5 min encore ; puis les raisins.", "**Pousse.** 1 h 30, couvert.",
   "**Moule.** Beurre-le, place une amande dans chaque creux, dépose la pâte en couronne. Lève 1 h.", "**Cuisson.** 40 min à 180 °C (th. 6). Démoule tiède, sucre glace."],
  age=2, cats=["pains", "fetes"], fetes=["Noël", "Pâques"], profil=["sucre"], sa=["Chocolat chaud"])

K("oeufs_meurette", "Œufs en meurette (sauce vin rouge)", "Œufs en meurette", "France › Bourgogne-Franche-Comté", "E", 2, 4, 30, 20, "€€", "Casserole, poêle, écumoire.",
  "Des œufs pochés nappés d'une sauce au vin rouge, lardons et champignons, sur un croûton aillé.",
  [f"8|œufs très frais|{OEUF}|3", f"50 cl|de vin rouge de Bourgogne|Vin rouge|3", f"100 g|de lardons|Lardons|2", "150 g|de champignons|Champignon de Paris|1",
   f"2|échalotes|{ECH}|1", f"30 g|de beurre + 1 c. à s. de farine|{BEURRE}|1", f"4 tranches|de pain de campagne grillé et frotté d'ail|Pain de campagne / complet|2", f"1 c. à s.|de vinaigre|{CIDRE}|0"],
  ["**Sauce.** Fais revenir lardons, échalotes et champignons, verse le vin et réduis de moitié. Lie avec le beurre manié (beurre + farine) : la sauce nappe.",
   "**Pocher.** Eau frémissante vinaigrée : casse chaque œuf dans une tasse, verse doucement, 3 min. Égoutte.", "**Servir.** Œuf sur le croûton, nappe de sauce brûlante."],
  age=None, profil=["gras", "viande_rouge"], a=["Bourgogne rouge"], sa=["Jus de raisin rouge"], tech=["Pocher des œufs", "Réduire"])

K("gougeres", "Gougères au comté", "Gougères", "France › Bourgogne-Franche-Comté", "A", 2, 30, 25, 25, "€", "Casserole, cuillère en bois, plaque, four.",
  "Des choux salés au fromage, légers et dorés, à servir tièdes à l'apéritif.",
  ["25 cl|d'eau|-|0", f"80 g|de beurre|{BEURRE}|2", f"150 g|de farine|{F55}|3", f"4|œufs|{OEUF}|3", f"120 g|de comté râpé|{GRUY}|3", f"1 pincée|de sel, poivre, muscade|{MUSC}|0"],
  ["**Panade.** Porte eau, beurre et sel à ébullition. Hors du feu, verse la farine d'un coup et remue ; remets 1 min sur le feu pour dessécher.",
   "**Œufs.** Hors du feu, ajoute les œufs un à un : la pâte doit être brillante et former un ruban. Ajoute le fromage.",
   "**Dresser et cuire.** Petites boules espacées, 25 min à 190 °C (th. 6-7). N'ouvre pas le four avant 20 min."],
  age=2, cats=["fetes", "enfants"], fetes=["Apéritif dînatoire", "Noël"], profil=["gras"], tech=["Pâte à choux"], sa=["Jus de raisin blanc pétillant"], a=["Crémant"])

K("escargots_bourgogne", "Escargots au beurre persillé", "Escargots de Bourgogne", "France › Bourgogne-Franche-Comté", "E", 1, 4, 20, 10, "€€", "Plat à escargots ou petits ramequins, four.",
  "Des escargots baignés de beurre à l'ail et au persil : on saucer avec du pain jusqu'à la dernière goutte.",
  ["48|escargots en conserve, rincés|Escargots|3", f"200 g|de beurre mou|{BEURRE}|3", f"3 gousses|d'ail|{AIL}|2", f"1 botte|de persil|{PERSIL}|2", f"1|échalote|{ECH}|1", f"1 pincée|de sel, poivre|{SEL}|0"],
  ["**Beurre.** Hache ail, échalote et persil ; mélange au beurre, sel, poivre.", "**Garnir.** Un escargot par alvéole (ou 6 par ramequin), recouvre de beurre.",
   "**Four.** 8 à 10 min à 220 °C, jusqu'à ce que le beurre grésille. Avec du pain."],
  age=None, fetes=["Noël"], profil=["gras"], a=["Chablis"], sa=["Eau pétillante"])

K("gratin_comte", "Gratin de pommes de terre au comté", "Gratin comtois", "France › Bourgogne-Franche-Comté", "A", 1, 6, 20, 60, "€", "Plat à gratin, four.",
  "Pommes de terre fondantes, crème et un comté qui gratine en croûte dorée.",
  [f"1,2 kg|de pommes de terre|{PDT}|3", f"200 g|de comté râpé|{GRUY}|3", f"40 cl|de crème liquide|{CL}|2", f"20 cl|de lait|{LAIT}|2", f"1 gousse|d'ail|{AIL}|1", f"1 pincée|de muscade, sel, poivre|{MUSC}|0"],
  ["**Couches.** Frotte le plat à l'ail ; alterne rondelles fines de pommes de terre et comté, salé et poivré.", "**Napper.** Verse crème et lait muscadés.",
   "**Cuire.** 1 h à 180 °C (th. 6), jusqu'à ce qu'un couteau entre seul et que le dessus soit doré."],
  age=1, cats=["enfants"], profil=["gras"], fetes=["Noël", "Repas de famille"])

K("fondue_savoyarde", "Fondue savoyarde", "Fondue savoyarde", "France › Auvergne-Rhône-Alpes › Savoie", "P", 1, 6, 20, 15, "€€€", "Caquelon et réchaud (ou casserole épaisse).",
  "Trois fromages fondus avec du vin blanc, du pain qu'on y trempe : le plat convivial de l'hiver.",
  [f"400 g|de beaufort râpé|{GRUY}|3", f"400 g|de comté râpé|{GRUY}|3", f"400 g|d'emmental de Savoie râpé|{GRUY}|3", f"40 cl|de vin blanc de Savoie|Vin blanc|3",
   f"1 gousse|d'ail|{AIL}|1", f"1 c. à c.|de maïzena|Fécule de maïs (maïzena)|1", "1 kg|de pain de campagne rassis en cubes|Pain rassis (réservé)|3", f"1 pincée|de poivre et de muscade|{MUSC}|0"],
  ["**Caquelon.** Frotte-le à l'ail, verse le vin et chauffe sans bouillir.", "**Fondre.** Ajoute les fromages poignée par poignée en remuant en huit.",
   "**Lier.** Ajoute la maïzena délayée dans un peu d'eau, poivre, muscade : la fondue doit être lisse et filante.", "**Servir.** Sur le réchaud ; chacun trempe son pain en tournant."],
  var=[("Sans alcool", ["alcohol"], {"Vin blanc": [("Lait entier / demi-écrémé / écrémé", 0.7), ("Citron", 0.05)]},
        "Vin blanc → **30 cl de lait + 2 c. à s. de jus de citron** (ou de bouillon) ; l'acidité empêche le fromage de faire des fils trop élastiques. **À tester**.")],
  keep="Le reste : en gratin ou sur des pommes de terre le lendemain.", age=None, kids="✓ dès 3 ans en version sans alcool (le vin cuit garde de l'alcool).", fetes=["Noël", "Repas de famille"], profil=["gras"], cats=["zero_dechet"],
  sa=["Thé noir chaud", "Eau"], a=["Vin blanc de Savoie"])

K("gratin_crozets", "Gratin de crozets (ou petites pâtes) au beaufort", "Croziflette", "France › Auvergne-Rhône-Alpes › Savoie", "A", 1, 4, 15, 30, "€", "Casserole, plat à gratin.",
  "Les petites pâtes carrées de Savoie, nappées de crème et de beaufort, gratinées. Avec des pâtes courtes si tu n'en trouves pas.",
  [f"400 g|de crozets ou de petites pâtes|{PATES}|3", f"25 cl|de crème liquide|{CL}|2", f"150 g|de beaufort râpé|{GRUY}|3", f"1|oignon|{OIG}|1", f"1 pincée|de sel, poivre|{SEL}|0"],
  ["**Pâtes.** Cuis-les al dente.", "**Mélange.** Mélange avec l'oignon fondu, la crème et la moitié du fromage.", "**Gratiner.** Reste du fromage dessus, 15 min à 200 °C."],
  age=1, cats=["enfants"], profil=["gras"])

K("salade_lyonnaise", "Salade lyonnaise", "Salade lyonnaise", "France › Auvergne-Rhône-Alpes › Lyonnais", "E", 1, 4, 20, 10, "€", "Poêle, casserole, saladier.",
  "Frisée croquante, lardons chauds, croûtons à l'ail et un œuf poché qui coule : une entrée qui fait un repas.",
  ["1|frisée|Chicorée / frisée|3", f"200 g|de lardons|Lardons|3", f"4|œufs|{OEUF}|3", f"2 tranches|de pain rassis en dés|Pain rassis (réservé)|2", f"1 gousse|d'ail|{AIL}|1",
   f"3 c. à s.|d'huile + 1 de vinaigre de vin|{HN}|1", f"1 c. à c.|de moutarde|{DIJON}|1"],
  ["**Croûtons.** Dore le pain avec l'ail dans l'huile.", "**Lardons.** Fais-les dorer ; déglace avec le vinaigre (c'est la vinaigrette chaude).",
   "**Œufs.** Poche-les 3 min.", "**Monter.** Frisée, moutarde et huile, lardons chauds avec leur jus, croûtons, œuf posé dessus."],
  age=None, profil=["gras", "acide"], cats=["zero_dechet"], sa=["Eau pétillante"], a=["Beaujolais"])

K("aligot", "Aligot", "Aligot", "France › Occitanie › Aubrac", "A", 2, 6, 30, 25, "€€", "Casserole, presse-purée, spatule en bois.",
  "Une purée qu'on étire au fromage frais de tomme jusqu'à ce qu'elle file sur un mètre. Spectaculaire et réconfortante.",
  [f"1 kg|de pommes de terre farineuses|{PDT}|3", "400 g|de tomme fraîche (ou cantal jeune + mozzarella)|Cantal / saint-nectaire / tomme|3", f"20 cl|de crème|{CF}|2",
   f"50 g|de beurre|{BEURRE}|2", f"1 gousse|d'ail râpé|{AIL}|1", f"1 pincée|de sel, poivre|{SEL}|0"],
  ["**Purée.** Cuis les pommes de terre, écrase-les avec beurre, crème et ail, à feu très doux.", "**Filer.** Ajoute la tomme en lamelles et remue en huit, en soulevant, 10 min : la purée devient élastique et brillante.",
   "**Servir.** Aussitôt, avec des saucisses (de volaille ou de bœuf si besoin)."],
  keep="Ne se réchauffe pas bien : à manger tout de suite.", age=1, profil=["gras"], fetes=["Repas de famille"])

K("truffade", "Truffade auvergnate", "Truffade", "France › Auvergne-Rhône-Alpes › Auvergne", "P", 1, 4, 20, 30, "€", "Grande poêle.",
  "Pommes de terre poêlées et cantal fondu, avec ou sans lardons : le plat du buron.",
  [f"1 kg|de pommes de terre|{PDT}|3", "300 g|de tome fraîche ou de cantal jeune|Cantal / saint-nectaire / tomme|3", f"100 g|de lardons (facultatif)|Lardons|0?",
   f"2 gousses|d'ail|{AIL}|1", f"2 c. à s.|de graisse de canard ou d'huile|Graisse de canard|1", f"1 c. à s.|de persil|{PERSIL}|0"],
  ["**Poêler.** Fais dorer les pommes de terre en lamelles dans la graisse 20 min, avec l'ail (et les lardons).", "**Fondre.** Ajoute le fromage en lamelles, remue jusqu'à ce qu'il file.",
   "**Galette.** Laisse dorer 3 min sans toucher, retourne sur un plat. Persil."],
  age=2, profil=["gras"], sa=["Eau"])

K("pissaladiere", "Pissaladière", "Pissaladiera", "France › Provence-Alpes-Côte d'Azur › Nice", "P", 2, 6, 30, 70, "€", "Plaque, sauteuse, four.",
  "Une pâte à pain fine sous des oignons confits fondants, des anchois et des olives noires.",
  ["1|pâte à pizza (recette liée)|SUB:pate_pizza|3", f"1,5 kg|d'oignons|{OIG}|3", f"4 c. à s.|d'huile d'olive|{HO}|2", "12|filets d'anchois|Anchois (filets, conserve)|2",
   "20|olives noires|Olives (vertes / noires)|1", f"2 branches|de thym|{THYM}|1"],
  ["**Oignons.** Fais-les confire 45 min à feu doux à couvert dans l'huile avec le thym : ils doivent être fondants, pas grillés.", "**Monter.** Étale la pâte, couvre d'oignons, croisillons d'anchois, olives.",
   "**Cuire.** 20 min à 220 °C (th. 7-8)."],
  age=3, profil=["poisson"], fetes=["Apéritif dînatoire"], sa=["Citronnade"], a=["Rosé de Provence"])

K("salade_nicoise", "Salade niçoise", "Salada nissarda", "France › Provence-Alpes-Côte d'Azur › Nice", "E", 1, 4, 20, 10, "€€", "Saladier, casserole.",
  "Tomates, œufs, thon, anchois, olives, crudités : sans pomme de terre ni haricots cuits dans la version niçoise d'origine.",
  [f"6|tomates|{TOM}|3", f"4|œufs durs|{OEUF}|2", "200 g|de thon au naturel|Thon en conserve|2", "8|filets d'anchois|Anchois (filets, conserve)|1",
   "1|poivron vert|Poivron (rouge/jaune/vert)|1", "1|concombre|Concombre|1", "12|olives noires|Olives (vertes / noires)|1", f"4 c. à s.|d'huile d'olive|{HO}|2", f"1 pincée|de sel|{SEL}|0"],
  ["**Œufs.** 10 min dans l'eau bouillante.", "**Couper.** Tomates en quartiers salés, poivron en fines lamelles, concombre en rondelles.",
   "**Dresser.** Légumes, thon, œufs en quartiers, anchois, olives ; huile d'olive au dernier moment."],
  age=3, profil=["leger", "poisson"], fetes=["Barbecue d'été"], sa=["Citronnade à la menthe"], a=["Rosé de Provence"])

K("pan_bagnat", "Pan bagnat", "Pan bagnat", "France › Provence-Alpes-Côte d'Azur › Nice", "P", 1, 4, 20, 30, "€", "Couteau à pain, film.",
  "La salade niçoise dans un pain rond imbibé d'huile d'olive : le sandwich de plage le plus parfumé de France.",
  [f"4|petits pains ronds|Pain de campagne / complet|3", f"3|tomates|{TOM}|2", "160 g|de thon|Thon en conserve|2", f"2|œufs durs|{OEUF}|2", f"½|poivron vert|{POIVRON}|1",
   f"1|oignon nouveau|Oignon nouveau / cébette|1", "8|olives|Olives (vertes / noires)|1", f"4 c. à s.|d'huile d'olive|{HO}|2", f"1 gousse|d'ail|{AIL}|1"],
  ["**Pain.** Ouvre, frotte d'ail, arrose d'huile.", "**Garnir.** Tomates salées, poivron, oignon, thon, œuf, olives.", "**Presser.** Referme, filme et laisse 30 min sous un poids : le pain boit les jus."],
  age=3, cats=["enfants"], profil=["poisson", "leger"], fetes=["Barbecue d'été"])

K("socca", "Socca (galette de pois chiches)", "Socca", "France › Provence-Alpes-Côte d'Azur › Nice", "A", 1, 4, 5, 120, "€", "Grande plaque ou poêle en fonte, four au maximum.",
  "Une galette fine de farine de pois chiches, croustillante sur les bords, poivrée : naturellement sans gluten.",
  [f"200 g|de farine de pois chiches|Farine de pois chiche (besan)|3", "40 cl|d'eau|-|0", f"4 c. à s.|d'huile d'olive|{HO}|2", f"1 c. à c.|de sel et beaucoup de poivre|{SEL}|0"],
  ["**Pâte.** Fouette farine, eau, sel et 2 c. à s. d'huile. Repos 2 h.", "**Chauffer.** Plaque huilée 10 min dans le four à 270 °C.",
   "**Cuire.** Verse une couche fine, 10 min, puis 2 min sous le gril. Poivre généreusement, coupe en morceaux irréguliers."],
  age=1, cats=["enfants"], profil=["gras"], fetes=["Apéritif dînatoire"], kids="✓ dès 1 an ; sans gluten, mais pois chiches (légumineuse).")

K("soupe_pistou", "Soupe au pistou", "Sòupa au pistou", "France › Provence-Alpes-Côte d'Azur", "So", 2, 6, 30, 45, "€", "Faitout, mortier ou mixeur.",
  "Une soupe de légumes d'été et de haricots, relevée au dernier moment d'un pistou basilic-ail-huile d'olive.",
  [f"2|courgettes|Courgette|2", f"2|carottes|{CAROTTE}|2", f"2|pommes de terre|{PDT}|2", "200 g|de haricots verts|Haricots verts|2", "250 g|de haricots blancs cuits|Haricots blancs / lingots|2",
   f"2|tomates|{TOM}|1", f"100 g|de petites pâtes|{PATES}|1", "1 botte|de basilic|Basilic|3", f"3 gousses|d'ail|{AIL}|2", f"8 c. à s.|d'huile d'olive|{HO}|2", f"60 g|de parmesan|{PARM}|1"],
  ["**Légumes.** Coupe tout en dés, couvre d'eau salée (2 L), 30 min.", "**Pâtes.** Ajoute haricots et pâtes, 10 min.",
   "**Pistou.** Pile basilic, ail, sel, puis l'huile et le parmesan.", "**Servir.** Hors du feu, une cuillère de pistou dans chaque bol."],
  age=1, cats=["enfants", "zero_dechet"], profil=["leger"], fetes=["Barbecue d'été"])

K("aioli_provencal", "Le grand aïoli", "Aiòli", "France › Provence-Alpes-Côte d'Azur", "P", 2, 6, 40, 30, "€€", "Mortier ou bol, fouet, cuit-vapeur ou casserole.",
  "Morue pochée, légumes vapeur et œufs durs autour d'une mayonnaise à l'ail très relevée : le repas du vendredi en Provence.",
  [f"800 g|de cabillaud ou de morue dessalée|Cabillaud / morue fraîche|3", f"6|pommes de terre|{PDT}|2", f"6|carottes|{CAROTTE}|2", "300 g|de haricots verts|Haricots verts|2",
   f"6|œufs|{OEUF}|2", f"1 tête|d'ail (aïoli)|{AIL}|3", "2|jaunes d'œufs|Jaune d'œuf|3", f"30 cl|d'huile d'olive douce|{HO}|3", f"½|citron|{CIT}|1"],
  ["**Aïoli.** Pile 6 gousses d'ail avec du sel en pâte, ajoute les jaunes, puis l'huile en filet en fouettant. Citron.",
   "**Légumes.** Cuis-les à la vapeur, chacun son temps. Œufs durs 10 min.", "**Poisson.** Poche 8 min dans l'eau frémissante avec laurier.", "**Servir.** Tout sur un grand plat, l'aïoli au centre."],
  tips=["⚠️ Œuf cru : publics fragiles exclus ; aïoli sans œuf : pomme de terre cuite écrasée + ail + huile."], age=None, kids="✓ dès 3 ans avec un aïoli sans œuf cru.", profil=["poisson", "gras"], fetes=["Repas de famille"])

K("tapenade", "Tapenade noire", "Tapenada", "France › Provence-Alpes-Côte d'Azur", "A", 1, 6, 10, 0, "€", "Mixeur.",
  "Olives noires, câpres, anchois et huile d'olive : la tartinade de l'apéritif provençal.",
  ["250 g|d'olives noires dénoyautées|Olives (vertes / noires)|3", "2 c. à s.|de câpres|Câpres|2", "4|filets d'anchois|Anchois (filets, conserve)|1", f"1 gousse|d'ail|{AIL}|1",
   f"6 c. à s.|d'huile d'olive|{HO}|2", f"½|citron|{CIT}|1"],
  ["**Mixer.** Par à-coups, olives, câpres, anchois, ail, citron ; ajoute l'huile en filet. Garde un peu de texture."],
  keep="1 semaine au frigo, couverte d'huile.", age=3, cats=["sauces"], fetes=["Apéritif dînatoire"], profil=["poisson"])

K("veau_olives_corse", "Veau aux olives (Corse)", "Vitellu à l'alivi", "France › Corse", "P", 2, 6, 25, 90, "€€", "Cocotte.",
  "Un sauté de veau mijoté à la tomate et aux olives, parfumé d'herbes du maquis.",
  [f"1,2 kg|d'épaule de veau en cubes|Épaule / tendron de veau|3", "150 g|d'olives vertes et noires|Olives (vertes / noires)|2", f"400 g|de tomates pelées|{PELEES}|2",
   f"2|oignons|{OIG}|2", f"3 gousses|d'ail|{AIL}|1", f"20 cl|de vin blanc|Vin blanc|2", f"2 branches|de romarin et de thym|{THYM}|1", f"3 c. à s.|d'huile d'olive|{HO}|1", f"1 pincée|de sel, poivre|{SEL}|0"],
  ["**Saisir.** Dore le veau dans l'huile, réserve.", "**Base.** Oignons, ail, déglace au vin, ajoute tomates et herbes.", "**Mijoter.** Remets la viande, 1 h 15 à couvert ; olives les 15 dernières minutes."],
  age=3, profil=["viande_rouge"], sa=["Jus de raisin rouge"], a=["Vin corse"])

K("fiadone", "Fiadone (gâteau corse au brocciu)", "Fiadone", "France › Corse", "D", 1, 8, 15, 40, "€", "Moule à manqué, four.",
  "Un gâteau sans farine, léger et citronné, au fromage frais corse (ou à la ricotta).",
  [f"500 g|de brocciu ou de ricotta égouttée|Ricotta|3", f"4|œufs|{OEUF}|3", f"150 g|de sucre|{SUCRE}|2", f"1|citron (zeste)|{CIT}|2"],
  ["**Mélanger.** Fouette œufs et sucre, ajoute fromage et zeste.", "**Cuire.** 40 min à 180 °C (th. 6), jusqu'à ce que le dessus soit doré.", "**Servir.** Froid."],
  age=1, cats=["enfants"], profil=["leger", "sucre"], kids="✓ dès 1 an ; naturellement sans gluten.")
