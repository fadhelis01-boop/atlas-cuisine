# -*- coding: utf-8 -*-
"""Vague 2 · France (1/3) : Bretagne, Normandie, Nord, Est."""
from recipes_v2_base import *

K("far_breton", "Far breton aux pruneaux", "Farz forn", "France › Bretagne", "D", 1, 8, 15, 75, "€", "Saladier, fouet, plat à gratin beurré, four.",
  "Un flan dense et moelleux, caramélisé sur les bords, avec des pruneaux fondants : le dessert du dimanche en Bretagne.",
  ["250 g|de pruneaux dénoyautés|Pruneaux|3", f"125 g|de farine|{F55}|3", f"4|œufs|{OEUF}|3", f"75 cl|de lait entier|{LAIT}|3",
   f"125 g|de sucre|{SUCRE}|2", f"40 g|de beurre demi-sel (moule et dessus)|{BEURRE}|2", f"1 pincée|de sel|{SEL}|0"],
  ["**Four.** Préchauffe à 200 °C (th. 6-7) et beurre généreusement le plat.", "**Pâte.** Fouette farine, sucre, sel et œufs, puis verse le lait petit à petit : la pâte doit être lisse et très liquide.",
   "**Pruneaux.** Répartis-les dans le plat et verse la pâte par-dessus.", "**Cuisson.** 15 min à 200 °C, puis 45 min à 180 °C (th. 6), jusqu'à ce que le dessus soit bien doré et le centre pris.",
   "**Service.** Laisse tiédir : le far se tient en refroidissant. Parsème de quelques noisettes de beurre."],
  tips=["Pruneaux trop secs : fais-les gonfler 10 min dans un thé chaud, puis égoutte."], age=1, cats=["enfants"], profil=["sucre"], sa=["Cidre doux sans alcool (jus de pomme pétillant)", "Lait ribot"], a=["Cidre brut"])

K("kouign_amann", "Kouign-amann simplifié (pâte à pain du boulanger)", "Kouign-amann", "France › Bretagne", "D", 3, 8, 40, 150, "€", "Rouleau, moule à manqué de 24 cm, four.",
  "Une galette feuilletée et caramélisée au beurre salé. Version maison avec une pâte à pain simple : croustillante dehors, fondante dedans.",
  [f"300 g|de farine|{F55}|3", "180 ml|d'eau tiède|-|0", f"5 g|de levure boulangère|{LEV}|1", f"5 g|de sel|{SEL}|0",
   f"200 g|de beurre demi-sel bien froid|{BEURRE}|3", f"180 g|de sucre|{SUCRE}|3"],
  ["**Pâte.** Pétris farine, eau, levure et sel 8 min. Laisse lever 1 h.", "**Beurre.** Étale la pâte en rectangle, pose le beurre aplati au centre, replie en portefeuille.",
   "**Tours.** Étale en long, saupoudre d'un tiers du sucre, replie en trois. Repos 15 min au frais. Recommence deux fois.",
   "**Moule.** Étale en carré, ramène les coins vers le centre et pose dans le moule beurré. Laisse lever 30 min.",
   "**Cuisson.** 35 à 40 min à 200 °C (th. 6-7), jusqu'à un caramel ambré. ⚠️ Le caramel brûle : démoule tiède, sur du papier cuisson."],
  tips=["Si le beurre perce la pâte, remets 15 min au frigo avant de continuer."], keep="2 jours à température ambiante ; se réchauffe 5 min au four.", age=6, profil=["sucre", "gras"], fetes=["Repas de famille"])

K("cotriade", "Cotriade (soupe de poissons bretonne)", "Kaoteriad", "France › Bretagne", "P", 2, 6, 30, 40, "€€", "Grande cocotte, écumoire.",
  "La bouillabaisse des pêcheurs bretons : pommes de terre fondantes, poissons du jour, beurre et herbes. On sert le bouillon sur du pain, puis le poisson.",
  [f"1 kg|de poissons variés (cabillaud, lieu, maquereau)|Cabillaud / morue fraîche|3", "500 g|de moules|Moules|1?", f"800 g|de pommes de terre|{PDT}|3",
   f"2|oignons|{OIG}|2", f"40 g|de beurre|{BEURRE}|2", f"1|bouquet garni (thym, laurier)|{LAURIER}|1", "1,5 L|d'eau|-|0",
   f"1 c. à s.|de vinaigre de cidre|{CIDRE}|1", f"6 tranches|de pain de campagne grillé|Pain de campagne / complet|2", f"1|pincée de sel et de poivre|{SEL}|0"],
  ["**Base.** Fais fondre les oignons émincés dans le beurre 5 min. Ajoute l'eau, le bouquet garni, sel, poivre.", "**Pommes de terre.** Ajoute-les en gros morceaux et cuis 15 min.",
   "**Poissons.** Ajoute d'abord les poissons fermes en tronçons, 6 min, puis les plus tendres et les moules, 4 min. Le poisson doit à peine s'effeuiller.",
   "**Service.** Verse le bouillon sur le pain grillé ; sers poissons et pommes de terre à part, avec une vinaigrette au cidre."],
  tips=["Garde les têtes et arêtes : elles font un fumet pour une prochaine soupe."], age=3, profil=["poisson"], sa=["Eau pétillante citronnée"], a=["Muscadet"])

K("moules_normande", "Moules à la normande (crème et cidre)", "Moules à la normande", "France › Normandie", "P", 1, 4, 20, 10, "€€", "Grand faitout avec couvercle.",
  "Des moules ouvertes au cidre, nappées de crème et d'échalote : prêtes en 10 minutes, avec des frites ou du pain.",
  ["2 kg|de moules de bouchot|Moules|3", f"3|échalotes|{ECH}|2", f"20 cl|de cidre brut|Cidre|2", f"20 cl|de crème fraîche|{CF}|2",
   f"20 g|de beurre|{BEURRE}|1", f"½ botte|de persil|{PERSIL}|1", f"1 pincée|de poivre|{POIVRE}|0"],
  ["**Moules.** Gratte-les et jette celles qui restent ouvertes quand on tape dessus.", "**Échalotes.** Fais-les fondre dans le beurre 3 min.",
   "**Cuisson.** Ajoute le cidre et les moules, couvre, feu vif 5 min en secouant : elles s'ouvrent. Jette celles restées fermées.",
   "**Sauce.** Retire les moules, ajoute la crème au jus, fais bouillir 2 min, poivre, persil. Verse sur les moules."],
  tips=["Pas de sel : les moules le sont déjà."], keep="À manger aussitôt ; ne se réchauffe pas.", age=3, profil=["poisson", "gras"],
  sa=["Jus de pomme pétillant"], a=["Cidre brut"], tech=["Déglacer"])

K("poulet_vallee_auge", "Poulet vallée d'Auge", "Poulet vallée d'Auge", "France › Normandie", "P", 2, 4, 25, 45, "€€", "Sauteuse ou cocotte.",
  "Du poulet doré, une sauce crème-champignons parfumée au cidre et aux pommes : le plat du dimanche normand.",
  [f"1|poulet en 8 morceaux (ou 4 cuisses)|{CUISSE}|3", "250 g|de champignons de Paris|Champignon de Paris|2", f"2|pommes|Pomme|2",
   f"25 cl|de cidre brut|Cidre|2", f"5 cl|de calvados (facultatif)|Calvados|0?", f"20 cl|de crème fraîche|{CF}|2", f"30 g|de beurre|{BEURRE}|1",
   f"2|échalotes|{ECH}|1", f"1 pincée|de sel et de poivre|{SEL}|0"],
  ["**Dorer.** Fais dorer le poulet salé dans le beurre 10 min. Réserve.", "**Base.** Fais revenir échalotes et champignons 5 min, déglace au cidre (et au calvados).",
   "**Mijoter.** Remets le poulet, couvre et cuis 30 min à feu doux. ⚠️ 74 °C à cœur.", "**Pommes.** Pendant ce temps, poêle les quartiers de pommes au beurre 8 min.",
   "**Sauce.** Ajoute la crème, laisse réduire 5 min à découvert. Sers avec les pommes."],
  age=3, profil=["gras"], sa=["Jus de pomme pétillant"], a=["Cidre brut"], tech=["Déglacer", "Saisir"], fetes=["Repas de famille"])

K("camembert_roti", "Camembert rôti au miel et aux noix", "Camembert rôti", "France › Normandie", "A", 1, 4, 5, 20, "€", "Four, petit plat ou la boîte en bois du camembert.",
  "Un camembert fondant à souhait, à partager avec des pommes de terre ou du pain grillé. Le plat d'hiver le plus simple qui soit.",
  ["1|camembert au lait cru, dans sa boîte en bois|Camembert / brie|3", f"1 c. à s.|de miel|{MIEL}|1", "4|cerneaux de noix|Noix|1",
   f"1 branche|de thym|{THYM}|0", "1|baguette ou des pommes de terre vapeur|Baguette tradition|2"],
  ["**Four.** Préchauffe à 200 °C (th. 6-7).", "**Préparer.** Retire le papier, remets le camembert dans sa boîte, entaille le dessus en croix.",
   "**Garnir.** Verse le miel, ajoute noix et thym.", "**Cuire.** 15 à 20 min, jusqu'à ce que le cœur soit coulant. Sers aussitôt avec le pain."],
  tips=["⚠️ Lait cru : déconseillé aux femmes enceintes et aux jeunes enfants ; prends un camembert au lait pasteurisé."], keep="À manger tout de suite.", age=None, profil=["gras"], fetes=["Apéritif dînatoire", "Noël"],
  sa=["Jus de pomme"], a=["Cidre"])

K("tarte_normande", "Tarte normande aux pommes", "Tarte normande", "France › Normandie", "D", 2, 8, 25, 40, "€", "Moule à tarte, four.",
  "Des pommes posées sur une pâte brisée, nappées d'une crème aux œufs qui dore au four : le goût des goûters de grand-mère.",
  ["1|pâte brisée (recette liée)|SUB:pate_brisee|3", f"4|pommes (reinettes ou golden)|Pomme|3", f"2|œufs|{OEUF}|2", f"20 cl|de crème fraîche|{CF}|2",
   f"80 g|de sucre|{SUCRE}|2", f"1 sachet|de sucre vanillé|Sucre vanillé|0", f"1 pincée|de cannelle|{CANN}|0?"],
  ["**Fond.** Étale la pâte dans le moule, pique-la, cuis 10 min à 180 °C (th. 6).", "**Pommes.** Coupe-les en quartiers fins et range-les en rosace.",
   "**Crème.** Fouette œufs, sucres et crème. Verse sur les pommes.", "**Cuisson.** 30 min à 180 °C, jusqu'à ce que la crème soit dorée et prise."],
  age=2, profil=["sucre"], sa=["Jus de pomme"], a=["Cidre doux"], cats=["enfants"])

K("teurgoule", "Teurgoule (riz au lait à la cannelle)", "Teurgoule", "France › Normandie", "D", 1, 8, 10, 300, "€", "Grande terrine allant au four.",
  "Un riz au lait cuit très lentement au four : dessous crémeux, dessus en croûte caramélisée à la cannelle.",
  [f"150 g|de riz rond|Riz rond / sushi|3", f"2 L|de lait entier|{LAIT}|3", f"180 g|de sucre|{SUCRE}|2", f"2 c. à c.|de cannelle|{CANN}|1", f"1 pincée|de sel|{SEL}|0"],
  ["**Four.** Préchauffe à 150 °C (th. 5).", "**Mélanger.** Dans la terrine, mélange riz cru, sucre, cannelle et sel, puis verse le lait.",
   "**Cuisson longue.** 5 h au four, sans remuer : une croûte brune se forme. C'est elle qui fait la teurgoule.", "**Service.** Tiède ou froid, à la cuillère."],
  tips=["La terrine doit être grande : le lait monte au début."], keep="4 jours au frigo.", age=1, cats=["enfants"], profil=["sucre"])

K("rillettes_maquereau", "Rillettes de maquereau au citron", "Rillettes de maquereau", "France › Bretagne", "E", 1, 6, 10, 0, "€", "Bol, fourchette.",
  "Une tartinade iodée et fraîche, prête en 10 minutes, avec des boîtes de maquereau.",
  ["2 boîtes|de filets de maquereau au naturel (240 g égouttés)|Maquereau|3", f"150 g|de fromage frais|Fromage blanc / faisselle|2", f"1|citron (jus et zeste)|{CIT}|1",
   f"1 c. à s.|de ciboulette|Ciboulette|1", f"1 c. à c.|de moutarde|{DIJON}|1", f"1 pincée|de poivre|{POIVRE}|0"],
  ["**Émietter.** Égoutte et émiette le maquereau en retirant la peau.", "**Mélanger.** Ajoute fromage frais, moutarde, jus et zeste de citron, ciboulette, poivre.",
   "**Servir.** Bien frais, sur du pain grillé ou des bâtonnets de légumes."],
  age=2, cats=["enfants", "fetes"], fetes=["Apéritif dînatoire"], profil=["poisson", "leger"], sa=["Citronnade"], a=["Muscadet"])

K("beurre_blanc", "Beurre blanc nantais", "Beurre blanc", "France › Pays de la Loire", "S", 2, 4, 20, 0, "€", "Petite casserole, fouet.",
  "La sauce des poissons de Loire : échalote réduite, beurre monté. Onctueuse et acidulée.",
  [f"3|échalotes ciselées très fin|{ECH}|2", f"10 cl|de vin blanc sec|Vin blanc|2", f"3 c. à s.|de vinaigre de vin blanc|Vinaigre de vin rouge / blanc|1",
   f"200 g|de beurre demi-sel bien froid, en dés|{BEURRE}|3", f"1 pincée|de poivre blanc|{POIVRE}|0"],
  ["**Réduction.** Fais réduire échalotes, vin et vinaigre à feu doux jusqu'à ce qu'il reste 2 c. à s. de liquide.",
   "**Monter.** Feu très doux : ajoute le beurre froid dés par dés en fouettant ; la sauce épaissit et blanchit.", "**Servir.** Aussitôt, sur un poisson poché ou des légumes. Elle ne doit jamais bouillir."],
  var=[("Sans alcool", ["alcohol"], {"Vin blanc": [("Fumet de poisson maison", 1.0), ("Citron", 0.1)], "Vinaigre de vin rouge / blanc": [("Vinaigre de cidre", 1.0)]},
        "Vin blanc → **fumet de poisson + 1 c. à c. de citron** ; vinaigre de vin → **vinaigre de cidre**. **À tester**.")],
  keep="À servir tout de suite (tiède, au bain-marie, 30 min maximum).", age=3, cats=["sauces"], profil=["gras"], tech=["Réduire", "Monter au beurre"])

K("carbonade_flamande", "Carbonade flamande", "Stoofvlees", "France › Hauts-de-France", "P", 2, 6, 30, 150, "€€", "Cocotte en fonte, four.",
  "Du bœuf fondant mijoté à la bière brune et au pain d'épices : sucré-amer, profond, réconfortant. Avec des frites.",
  [f"1,2 kg|de paleron en gros cubes|Paleron|3", f"3|oignons|{OIG}|2", f"75 cl|de bière brune|Bière (blonde, brune, blanche)|3",
   f"3 tranches|de pain d'épices tartinées de moutarde|Pain de campagne / complet|2", f"2 c. à s.|de cassonade|{SUCRE}|1",
   f"2 c. à s.|de vinaigre de cidre|{CIDRE}|1", f"2|feuilles de laurier et du thym|{LAURIER}|1", f"30 g|de beurre|{BEURRE}|1", f"1 c. à c.|de moutarde|{DIJON}|1", f"1 pincée|de sel et de poivre|{SEL}|0"],
  ["**Saisir.** Fais dorer la viande en 3 fois dans le beurre. Réserve.", "**Oignons.** Fais-les fondre 10 min, ajoute la cassonade.",
   "**Monter.** Remets la viande, verse la bière et le vinaigre, ajoute herbes et pain d'épices côté moutarde dessous.", "**Mijoter.** 2 h 30 au four à 150 °C (th. 5), couvert. Le pain fond et lie la sauce."],
  var=[("Sans alcool", ["alcohol"], {"Bière (blonde, brune, blanche)": [("Bouillon d'os maison (bœuf/volaille)", 0.8), ("Jus de raisin / pomme (pur jus)", 0.2)]},
        "Bière → **600 ml de bouillon + 150 ml de jus de pomme**, et 1 c. à s. de vinaigre de cidre en plus. **À tester**.")],
  age=3, profil=["viande_rouge", "sucre"], sa=["Jus de raisin rouge"], a=["Bière brune"], tech=["Saisir", "Mijoter"], fetes=["Repas de famille"])

K("gaufres", "Gaufres croustillantes", "Gaufres", "France › Hauts-de-France", "G", 1, 6, 20, 60, "€", "Gaufrier, saladier, fouet.",
  "Des gaufres légères, dorées et croustillantes, pour le goûter ou la Chandeleur.",
  [f"250 g|de farine|{F55}|3", f"2|œufs|{OEUF}|2", f"40 cl|de lait|{LAIT}|3", f"80 g|de beurre fondu|{BEURRE}|2", f"40 g|de sucre|{SUCRE}|1",
   f"1 sachet|de levure chimique|{LEVC}|1", f"1 pincée|de sel|{SEL}|0"],
  ["**Pâte.** Mélange farine, sucre, levure, sel. Ajoute œufs, puis lait peu à peu, puis beurre fondu.", "**Repos.** 1 h si possible.",
   "**Cuisson.** Gaufrier bien chaud et graissé : 1 louche, 3 à 4 min, jusqu'à ce qu'elles soient dorées."],
  age=2, cats=["enfants", "pains"], fetes=["Chandeleur", "Anniversaire"], profil=["sucre"], sa=["Chocolat chaud"])

K("oeufs_mayonnaise", "Œufs mayonnaise", "Œufs mayonnaise", "France › Île-de-France", "E", 1, 4, 15, 10, "€", "Casserole, bol, fouet.",
  "L'entrée de bistrot par excellence : des œufs durs juste cuits et une vraie mayonnaise maison.",
  [f"6|œufs|{OEUF}|3", "1|mayonnaise maison (recette liée)|SUB:mayonnaise|3", "quelques feuilles|de salade|Salade (laitue, batavia)|1", f"1 pincée|de paprika|{PAPRIKA}|0"],
  ["**Œufs.** 10 min dans l'eau bouillante, puis eau glacée. Écale.", "**Dresser.** Coupe en deux, pose sur la salade, nappe de mayonnaise, paprika."],
  age=None, kids="✓ dès 3 ans avec une mayonnaise sans œuf ou à l'œuf pasteurisé.", profil=["gras"], tech=["Cuire un œuf"])

K("steak_frites", "Steak frites, beurre maître d'hôtel", "Steak frites", "France › Île-de-France", "P", 1, 4, 20, 15, "€€", "Poêle épaisse, four ou friteuse.",
  "Un steak bien saisi, des frites maison et un beurre persillé qui fond dessus : le classique des brasseries.",
  [f"4|steaks (bavette ou entrecôte)|Bavette|3", "1|frites maison (recette liée)|SUB:frites_maison|3", f"60 g|de beurre mou|{BEURRE}|2",
   f"2 c. à s.|de persil haché|{PERSIL}|1", f"½|citron (jus)|{CIT}|1", f"1 c. à s.|d'huile|{HN}|1", f"1 pincée|de fleur de sel et de poivre|{SEL}|0"],
  ["**Beurre.** Mélange beurre, persil, citron, poivre ; roule en boudin et mets au frais.", "**Viande.** Sors-la 30 min avant. Poêle très chaude, huile.",
   "**Cuisson.** 2 min par face pour saignant, 3 pour à point. Laisse reposer 3 min. ⚠️ Enfants : bien cuit.", "**Service.** Une rondelle de beurre sur chaque steak, frites à côté."],
  age=3, profil=["viande_rouge", "gras"], sa=["Eau pétillante citronnée"], a=["Vin rouge léger"], tech=["Saisir", "Laisser reposer une viande"])

K("croque_monsieur", "Croque-monsieur à la béchamel", "Croque-monsieur", "France › Île-de-France", "P", 1, 4, 15, 10, "€", "Four (gril), plaque.",
  "Pain de mie, jambon, béchamel et fromage gratiné : le croque de café, doré et fondant.",
  [f"8 tranches|de pain de mie|Pain de mie|3", f"4 tranches|de jambon blanc|Jambon blanc|3", "1|béchamel (½ recette liée)|SUB:bechamel|2",
   f"150 g|d'emmental râpé|{GRUY}|2", f"20 g|de beurre|{BEURRE}|1"],
  ["**Monter.** Beurre le pain, pose jambon et un peu de fromage, ferme.", "**Napper.** Étale la béchamel dessus et le reste du fromage.",
   "**Gratiner.** 10 min sous le gril à 220 °C, jusqu'à ce que ce soit doré et bouillonnant."],
  age=2, cats=["enfants"], profil=["gras"], sa=["Jus de pomme"])

K("flammekueche", "Flammekueche (tarte flambée)", "Flammekueche", "France › Grand Est › Alsace", "P", 1, 4, 20, 10, "€", "Four le plus chaud possible, plaque.",
  "Une pâte très fine, de la crème, des oignons et des lardons, cuite en quelques minutes : croustillante et fondante.",
  ["2|pâtons de pâte à pizza (recette liée)|SUB:pate_pizza|3", f"200 g|de crème épaisse|Crème épaisse|3", f"100 g|de fromage blanc|Fromage blanc / faisselle|2",
   f"2|oignons émincés très fin|{OIG}|2", f"150 g|de lardons fumés|Lardons|2", f"1 pincée|de muscade, sel, poivre|{MUSC}|0"],
  ["**Four.** Au maximum avec la plaque dedans, 30 min.", "**Crème.** Mélange crème, fromage blanc, muscade, sel, poivre.",
   "**Monter.** Étale la pâte très finement, couvre de crème, d'oignons et de lardons.", "**Cuire.** 7 à 10 min, jusqu'à ce que les bords soient dorés et cloqués."],
  age=3, profil=["gras"], sa=["Jus de pomme pétillant"], a=["Bière blonde", "Riesling"])

K("spatzle", "Spätzle au beurre noisette", "Spätzle", "France › Grand Est › Alsace", "A", 2, 4, 25, 10, "€", "Casserole, passoire à gros trous ou râpe, poêle.",
  "Des petites pâtes fraîches irrégulières, poêlées au beurre : l'accompagnement idéal des plats en sauce.",
  [f"300 g|de farine|{F55}|3", f"4|œufs|{OEUF}|3", "10 cl|d'eau|-|0", f"40 g|de beurre|{BEURRE}|2", f"1 pincée|de muscade et de sel|{MUSC}|0"],
  ["**Pâte.** Mélange farine, œufs, eau, muscade, sel : une pâte épaisse et lisse.", "**Cuisson.** Fais tomber la pâte dans l'eau bouillante salée à travers une passoire à gros trous. Égoutte dès qu'ils remontent.",
   "**Poêler.** Fais blondir le beurre, ajoute les spätzle, 3 min."],
  age=1, cats=["enfants", "pains"], profil=["gras"])

K("bretzels", "Bretzels maison", "Bretzel", "France › Grand Est › Alsace", "Pa", 2, 8, 40, 90, "€", "Casserole large, plaque, four.",
  "Des bretzels dorés à la croûte brillante et au gros sel, grâce à un bain de bicarbonate (sans soude, sans danger).",
  [f"500 g|de farine|{F55}|3", "280 ml|d'eau tiède|-|0", f"7 g|de levure boulangère|{LEV}|1", f"10 g|de sel|{SEL}|0", f"30 g|de beurre mou|{BEURRE}|1",
   f"4 c. à s.|de bicarbonate (pour 2 L d'eau)|Bicarbonate de soude|1", f"1 c. à s.|de gros sel|{SEL}|0"],
  ["**Pâte.** Pétris tout (sauf bicarbonate et gros sel) 8 min. Lève 1 h.", "**Façonner.** 8 boudins de 50 cm plus épais au centre ; croise les extrémités et rabats-les sur le ventre.",
   "**Bain.** Plonge chaque bretzel 20 s dans l'eau frémissante au bicarbonate. Égoutte.", "**Cuire.** Gros sel, 15 min à 220 °C (th. 7-8), jusqu'à un brun profond."],
  age=4, cats=["pains"], profil=["sucre"], sa=["Lait"], a=["Bière blonde"])

K("madeleines", "Madeleines à la bosse", "Madeleines de Commercy", "France › Grand Est › Lorraine", "G", 1, 20, 15, 70, "€", "Moule à madeleines, saladier, four.",
  "Le choc thermique (pâte froide, four chaud) fait la fameuse bosse. Moelleuses, au beurre et au citron.",
  [f"2|œufs|{OEUF}|3", f"100 g|de sucre|{SUCRE}|2", f"100 g|de farine|{F55}|3", f"100 g|de beurre fondu|{BEURRE}|3", f"1 c. à c.|de levure chimique|{LEVC}|1", f"1|citron (zeste)|{CIT}|1", f"1 c. à s.|de miel|{MIEL}|1?"],
  ["**Pâte.** Fouette œufs et sucre, ajoute farine, levure, zeste, miel, puis le beurre fondu tiède.", "**Froid.** Au moins 1 h au frigo (la nuit, c'est mieux).",
   "**Cuire.** Moule beurré, pâte aux ¾, 4 min à 230 °C puis 6 min à 180 °C. Démoule aussitôt."],
  age=2, cats=["enfants"], profil=["sucre"], sa=["Chocolat chaud", "Thé"])
