# -*- coding: utf-8 -*-
"""Vague 4 · Audit du chef (16/10/2026) : classiques français de famille et de bistrot manquants, régions peu couvertes
(Corse, Pays basque, Nord, Franche-Comté, Languedoc). Catalogue du Tome 4 et règles D21 (porc indissociable : nom d'origine
+ « version », variantes sans porc/sans alcool « à tester »). NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

IDF = "France › Île-de-France › Bistrot"; QF = "France › Cuisine du quotidien"; NO = "France › Normandie"; NPC = "France › Hauts-de-France"
FC = "France › Bourgogne-Franche-Comté"; PB = "France › Nouvelle-Aquitaine › Pays basque"; CO = "France › Corse"; AL = "France › Grand Est › Alsace"
VB = ("Sans alcool", ["alcohol"], {"Vin blanc": [("Bouillon d'os maison (bœuf/volaille)", 0.8), ("Vinaigre de cidre", 0.05)]}, "Vin blanc → **bouillon + 1 c. à c. de vinaigre de cidre** : l'acidité est gardée. **À tester**.")

K("souffle_fromage", "Soufflé au fromage", "Soufflé au fromage", IDF, "P", 2, 4, 25, 30, "€", "Moule à soufflé 18 cm (ou 4 ramequins), batteur.",
  "Une béchamel épaisse au comté, des blancs montés, et le four fait le reste : le soufflé monte haut et doré. On le sert tout de suite, il n'attend pas.",
  [f"40 g|de beurre|{BEURRE}|2", f"40 g|de farine|{F55}|2", f"25 cl|de lait|{LAIT}|2", f"4|œufs|{OEUF}|3", f"100 g|de comté râpé|{GRUY}|3", f"1 pincée|de muscade|{MUSC}|0"],
  ["**Préparer.** Four 200 °C ; moule beurré au pinceau du bas vers le haut (le soufflé grimpe le long des traits), puis fariné.",
   "**Béchamel.** Beurre + farine 1 min, lait d'un coup en fouettant, 2 min : très épaisse ; hors du feu, jaunes, fromage, sel, muscade.",
   "**Blancs.** Montés fermes avec une pincée de sel ; un quart mélangé vivement à la béchamel, le reste incorporé délicatement à la spatule, en soulevant.",
   "**Cuire.** Rempli aux trois quarts, pouce passé sur le bord (il monte droit) ; 25-30 min sans ouvrir : très gonflé et doré. À table immédiatement."],
  age=3, tech=["faire un roux", "monter des blancs", "incorporer délicatement"], tips=["N'ouvre pas le four avant 20 min : un courant d'air et il retombe."])

K("bouchees_reine", "Bouchées à la reine (vol-au-vent au poulet)", "Bouchées à la reine", IDF, "P", 1, 4, 30, 20, "€€", "Casserole, sauteuse, four.",
  "Croustades feuilletées garnies de poulet, champignons et quenelles dans une sauce suprême crémeuse : le classique des repas de famille.",
  ["4|croustades feuilletées (bouchées) du commerce|Pâte feuilletée (prête)|3", f"2|blancs de poulet|{BLANC_P}|3", "250 g|de champignons de Paris|Champignon de Paris|2", "40 cl|de bouillon de volaille|Bouillon cube volaille|2", f"30 g|de beurre|{BEURRE}|1", f"30 g|de farine|{F55}|1", f"15 cl|de crème|{CF}|2", f"1|jaune d'œuf|Jaune d'œuf|1", f"½|citron|{CIT}|1"],
  ["**Pocher.** Poulet en dés, 10 min dans le bouillon frémissant ; champignons en quartiers 5 min au beurre avec un filet de citron.",
   "**Sauce suprême.** Roux beurre-farine, bouillon de cuisson filtré en fouettant, 5 min ; crème et jaune hors du feu : nappante et brillante.",
   "**Garnir.** Poulet et champignons dans la sauce ; croustades chauffées 8 min à 180 °C, garnies à ras ; servies aussitôt avec du riz ou une salade."],
  age=3, cats=["enfants"], fetes=["Repas de famille", "Noël"], tech=["faire un roux"])

K("moules_marinieres", "Moules marinières", "Moules marinières", NO, "P", 1, 4, 15, 8, "€€", "Grand faitout avec couvercle.",
  "Moules ouvertes en quelques minutes avec échalote, vin blanc et persil, et le jus qu'on boit à la cuillère : un plat de fête qui coûte peu.",
  ["2 kg|de moules|Moules|3", f"3|échalotes|{ECH}|2", "20 cl|de vin blanc sec|Vin blanc|2", f"30 g|de beurre|{BEURRE}|1", f"1 bouquet|de persil|{PERSIL}|2", f"2|feuilles de laurier|{LAURIER}|0", f"1 pincée|de poivre|{POIVRE}|0"],
  ["**Laver.** Moules grattées, ébarbées ; jette celles qui sont cassées ou restent ouvertes quand on les tapote.",
   "**Ouvrir.** Échalotes 2 min au beurre, vin, laurier, moules ; couvert, feu vif, 5-6 min en secouant : elles s'ouvrent.",
   "**Servir.** Persil haché, poivre (pas de sel : les moules le sont) ; jette celles restées fermées ; frites ou pain."],
  age=3, cats=["zero_dechet"], profil=["poisson"], var=[("Sans alcool", ["alcohol"], {"Vin blanc": [("Fumet de poisson maison", 0.9), ("Citron", 0.1)]}, "Vin blanc → **fumet ou eau + jus d'un demi-citron**. **À tester**.")],
  tips=["Le jus restant : filtré, il fait une base de soupe de poisson ou de risotto."], tech=["moules et coquillages"])

K("choucroute_mer", "Choucroute de la mer", "Choucroute de la mer", AL, "P", 2, 4, 25, 40, "€€€", "Cocotte, casserole.",
  "La choucroute alsacienne sans charcuterie : chou fermenté au beurre et aux baies de genièvre, poissons nobles pochés et beurre blanc. Sans porc par nature.",
  ["1 kg|de choucroute crue|Chou blanc / rouge|3", "600 g|de poissons (cabillaud, saumon, haddock)|Cabillaud / morue fraîche|3", "200 g|de saumon|Saumon (frais, pavé)|2", "300 g|de crevettes|Crevettes (cuites/crues)|1?", f"1|oignon|{OIG}|1", "6|baies de genièvre|Baies de genièvre|1", f"40 g|de beurre|{BEURRE}|2", "25 cl|de fumet de poisson|Fumet de poisson maison|2", "4 c. à s.|de beurre blanc|SUB:beurre_blanc|2?"],
  ["**Chou.** Rincé et pressé ; oignon fondu au beurre, chou, genièvre, fumet ; couvert 35 min à feu doux : tendre et doré par endroits.",
   "**Poissons.** En gros morceaux, pochés 6-8 min à frémissement dans un fond de fumet : nacrés au cœur.",
   "**Dresser.** Chou au centre, poissons et crevettes autour, beurre blanc à part, pommes de terre vapeur."],
  age=6, fetes=["Repas de famille"], profil=["poisson"], tech=["cuissons du poisson"])

K("sole_normande", "Filets de sole à la normande (simplifiés)", "Sole normande", NO, "P", 2, 4, 25, 15, "€€€", "Plat à four, casserole.",
  "Filets de sole pochés, sauce crème-champignons au jus de cuisson et moules : le grand classique normand, ramené à 40 minutes.",
  ["8|filets de sole (ou limande)|Sole, limande|3", "250 g|de champignons|Champignon de Paris|2", "500 g|de moules (facultatif)|Moules|1?", f"20 cl|de crème|{CF}|2", "15 cl|de cidre ou de vin blanc|Cidre|2", f"1|échalote|{ECH}|1", f"20 g|de beurre|{BEURRE}|1", f"1|jaune d'œuf|Jaune d'œuf|1"],
  ["**Pocher.** Filets roulés dans un plat beurré, échalote, cidre ; papier sulfurisé ; 180 °C, 10-12 min : blancs et fermes.",
   "**Sauce.** Jus de cuisson réduit de moitié avec les champignons ; crème, 3 min ; hors du feu, jaune : nappante.",
   "**Servir.** Sauce sur les filets, moules ouvertes autour, persil."],
  age=6, profil=["poisson"], var=[("Sans alcool", ["alcohol"], {"Cidre": [("Jus de pomme / raisin / orange (pur jus)", 0.5), ("Fumet de poisson maison", 0.5)]}, "Cidre → **moitié jus de pomme, moitié fumet**. **À tester**.")])

K("flamiche_maroilles", "Tarte au maroilles (flamiche)", "Flamiche au maroilles", f"{NPC} › Avesnois", "P", 1, 6, 20, 25, "€€", "Moule à tarte, four.",
  "Pâte brisée, crème, œufs et tranches de maroilles fondant : la tarte du Nord, puissante et généreuse, avec une salade verte bien vinaigrée.",
  ["1|pâte brisée|Pâte brisée / sablée (prête)|3", "½|maroilles (ou munster, reblochon)|Reblochon / raclette / mont-d'or|3", f"2|œufs|{OEUF}|2", f"20 cl|de crème|{CF}|2", f"1|oignon|{OIG}|1?", f"1 pincée|de poivre|{POIVRE}|0"],
  ["**Foncer.** Pâte dans le moule, piquée ; oignon fondu étalé (facultatif).", "**Garnir.** Œufs battus avec la crème, poivre (pas de sel) ; maroilles en tranches avec la croûte.", "**Cuire.** 200 °C, 25 min : gonflée, dorée, le fromage coule."],
  age=6, fetes=["Apéritif dînatoire"], profil=["gras"], tech=["foncer une pâte"])

K("poulet_comte_champignons", "Poulet comtois au comté et aux champignons", "Poulet comtois", FC, "P", 1, 4, 20, 40, "€€", "Cocotte.",
  "Poulet doré, champignons, crème et comté râpé qui lie la sauce : la version de tous les jours du poulet au vin jaune.",
  [f"4|cuisses de poulet|{CUISSE}|3", "300 g|de champignons (ou morilles séchées)|Champignon de Paris|2", f"25 cl|de crème|{CF}|2", f"80 g|de comté râpé|{GRUY}|2", "10 cl|de vin blanc (ou vin jaune)|Vin blanc|1", f"1|échalote|{ECH}|1", f"20 g|de beurre|{BEURRE}|1"],
  ["**Dorer.** Cuisses salées, peau dessous, 8 min : bien dorées ; retourne 3 min.", "**Mijoter.** Échalote, vin, 2 min ; couvert 25 min à feu doux.",
   "**Sauce.** Champignons poêlés à part ; crème et comté dans la cocotte, 5 min : la sauce nappe ; champignons."], age=3, var=[VB], fetes=["Repas de famille"])

K("axoa_veau", "Axoa de veau (Pays basque)", "Axoa", PB, "P", 1, 4, 20, 40, "€€", "Sauteuse.",
  "Veau haché au couteau, mijoté avec oignons, piments doux et piment d'Espelette : le plat des jours de marché d'Espelette.",
  ["800 g|d'épaule de veau|Épaule / tendron de veau|3", f"2|oignons|{OIG}|2", f"3|poivrons (ou piments doux)|{POIVRON}|2", f"2 gousses|d'ail|{AIL}|1", "1 c. à c.|de piment d'Espelette|Piment d'Espelette|2", f"20 cl|de bouillon|{BOUILLON}|1", f"2 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Hacher.** Le veau au couteau en petits dés (ou demande au boucher un hachage gros).", "**Fondre.** Oignons, poivrons, ail 10 min : très tendres.", "**Mijoter.** Viande 5 min, Espelette, bouillon ; 30 min à petit feu. Avec pommes de terre vapeur."],
  age=3, profil=["epice"])

K("gratin_macaronis", "Gratin de macaronis au fromage", "Gratin de macaronis", QF, "P", 1, 4, 15, 25, "€", "Plat à gratin.",
  "Macaronis dans une béchamel légère au fromage, gratinés : le plat qui réconcilie tous les enfants avec la table.",
  [f"300 g|de macaronis|{PATES}|3", f"40 cl|de lait|{LAIT}|2", f"30 g|de beurre|{BEURRE}|1", f"30 g|de farine|{F55}|1", f"120 g|de fromage râpé|{GRUY}|3", f"1 pincée|de muscade|{MUSC}|0"],
  ["**Cuire.** Macaronis 2 min de moins que le paquet.", "**Béchamel.** Roux, lait, 5 min ; muscade, sel, deux tiers du fromage.", "**Gratiner.** Pâtes + sauce dans le plat, fromage ; 200 °C, 20 min : croûte dorée qui croustille."],
  age=1, cats=["enfants"], tech=["faire un roux"])

K("croustade_pommes_gasconne", "Croustade aux pommes (pastis gascon simplifié)", "Pastis gascon", "France › Occitanie › Gascogne", "D", 2, 8, 30, 35, "€€", "Moule à manqué, four.",
  "Feuilles de pâte filo beurrées et froissées sur des pommes caramélisées, parfum de fleur d'oranger : la version maison de la croustade gasconne.",
  ["8|feuilles de brick ou de filo|Pâte filo / feuilles de brick|3", "5|pommes|Pomme|3", f"80 g|de beurre fondu|{BEURRE}|2", f"60 g|de sucre|{SUCRE}|2", "1 c. à s.|d'eau de fleur d'oranger|Eau de fleur d'oranger|1", "2 c. à s.|d'armagnac (facultatif)|Cognac / armagnac / brandy|1?"],
  ["**Pommes.** En lamelles, poêlées 8 min au beurre avec 30 g de sucre : dorées ; fleur d'oranger (et armagnac).",
   "**Monter.** 4 feuilles beurrées et sucrées en étoile dans le moule ; pommes ; les autres feuilles froissées en voilages dessus, beurrées, sucrées.",
   "**Cuire.** 180 °C, 25-30 min : feuilles dorées et cassantes. Tiède."], age=3, fetes=["Repas de famille"], profil=["sucre"])

K("bourride_setoise", "Bourride de poisson blanc à l'aïoli", "Bourride", "France › Occitanie › Sète", "P", 2, 4, 30, 20, "€€", "Faitout.",
  "Poisson blanc poché dans un bouillon parfumé, puis sauce liée à l'aïoli : le cousin onctueux de la bouillabaisse, plus simple.",
  ["800 g|de poisson blanc ferme (lotte, cabillaud)|Lotte|3", f"1|poireau|Poireau|1", f"1|oignon|{OIG}|1", "1 morceau|de fenouil|Fenouil|1", "1 zeste|d'orange|Orange|1", "6 c. à s.|d'aïoli|SUB:aioli_provencal|3", f"2|jaunes d'œuf|Jaune d'œuf|1", "8 tranches|de pain grillé|Pain de campagne / complet|1"],
  ["**Bouillon.** Légumes émincés, zeste d'orange, 1 l d'eau salée, 15 min.", "**Pocher.** Poisson en tronçons 8 min à frémissement ; réservé au chaud.",
   "**Lier.** Aïoli et jaunes dans une casserole, bouillon chaud versé peu à peu en fouettant, à feu très doux sans bouillir : la sauce nappe. Sur le poisson et le pain."],
  age=6, profil=["poisson"], tech=["émulsionner"])

K("petit_sale_lentilles", "Petit salé aux lentilles (version volaille fumée possible)", "Petit salé aux lentilles", "France › Auvergne-Rhône-Alpes › Auvergne", "P", 1, 4, 20, 90, "€€", "Faitout.",
  "Poitrine demi-sel fondante et lentilles vertes du Puy mijotées ensemble : le plat de bistrot d'hiver. Le porc est au cœur du plat ; une version volaille fumée est proposée.",
  ["800 g|de petit salé (poitrine demi-sel)|Poitrine de porc (fraîche)|3", "300 g|de lentilles vertes du Puy|Lentilles vertes / brunes|3", f"2|carottes|{CAROTTE}|1", f"1|oignon piqué d'un clou de girofle|{OIG}|1", f"1|bouquet garni (thym, laurier)|{THYM}|1", f"1 c. à s.|de moutarde|{DIJON}|1"],
  ["**Dessaler.** Petit salé couvert d'eau froide, porté à ébullition 5 min, égoutté.", "**Mijoter.** Viande, oignon, bouquet, eau à hauteur, 1 h à frémissement.",
   "**Lentilles.** Avec les carottes en rondelles, 30 min : tendres, encore entières ; goûte avant de saler. Moutarde à table."],
  age=3, var=[("Sans porc (version)", ["pork"], {"Poitrine de porc (fraîche)": [("Poitrine de dinde fumée", 0.6), ("Cuisse / pilon de poulet", 0.5)]}, "Petit salé → **poitrine de dinde fumée + cuisses de poulet**, ajoutées 35 min avant la fin : le goût fumé est gardé. **À tester**.")])

K("veloute_dubarry", "Velouté Du Barry (chou-fleur)", "Crème Du Barry", IDF, "So", 1, 4, 15, 25, "€", "Casserole, mixeur.",
  "Le velouté de chou-fleur de la cuisine classique, crémeux et délicat, avec quelques bouquets rôtis et de la ciboulette.",
  ["1|chou-fleur|Chou-fleur|3", f"1|pomme de terre|{PDT}|1", f"1|oignon|{OIG}|1", "80 cl|de bouillon de légumes|Bouillon cube légumes|2", f"15 cl|de crème|{CF}|2", "1 c. à s.|de ciboulette|Ciboulette|1"],
  ["**Suer.** Oignon 5 min au beurre, sans coloration.", "**Cuire.** Chou-fleur (garde 8 petits bouquets) et pomme de terre, bouillon, 20 min.", "**Mixer.** Très lisse ; crème ; bouquets rôtis à la poêle et ciboulette en finition."],
  age=1, cats=["enfants", "vegetarien"], profil=["leger"])

K("tomates_farcies", "Tomates farcies à la provençale", "Tomates farcies", "France › Provence-Alpes-Côte d'Azur", "P", 1, 4, 30, 50, "€", "Plat à four.",
  "Grosses tomates garnies de farce bœuf-veau aux herbes et à l'ail, cuites sur un lit de riz qui boit leur jus : le plat d'été de toutes les grands-mères.",
  [f"8|grosses tomates|{TOM}|3", f"400 g|de bœuf haché (ou bœuf-veau)|{HACHE}|3", f"1|oignon|{OIG}|1", f"2 gousses|d'ail|{AIL}|1", f"½ bouquet|de persil|{PERSIL}|1", "1 tranche|de pain rassis trempé dans le lait|Pain rassis (réservé)|1", f"1|œuf|{OEUF}|1", f"100 g|de riz|{RIZ}|2", f"3 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Évider.** Chapeaux coupés, pulpe retirée et hachée ; tomates salées à l'envers 10 min.", "**Farce.** Viande, oignon, ail, persil, pain pressé, œuf, sel, poivre.",
   "**Cuire.** Riz cru au fond du plat avec la pulpe et 20 cl d'eau ; tomates farcies, chapeaux ; huile ; 180 °C, 50 min : farce cuite, riz tendre."],
  age=3, cats=["enfants"], fetes=["Repas de famille"])

K("tarte_sucre_nord", "Tarte au sucre du Nord (à la vergeoise)", "Tarte au sucre", f"{NPC} › Flandre", "D", 1, 8, 20, 120, "€", "Moule à tarte, four.",
  "Une pâte briochée, une couche de vergeoise brune, du beurre et un peu de crème : caramélisée, fondante, la tarte des ducasses flamandes.",
  [f"250 g|de farine|{F55}|3", f"5 g|de levure boulangère|{LEV}|2", f"1|œuf|{OEUF}|2", f"10 cl|de lait tiède|{LAIT}|1", f"60 g|de beurre|{BEURRE}|2", "120 g|de vergeoise brune|Sucre blanc / roux / cassonade / vergeoise|3", f"4 c. à s.|de crème|{CF}|1"],
  ["**Pâte.** Farine, levure, œuf, lait, 30 g de beurre mou, sel : pétrie 5 min ; 1 h 30 au chaud : doublée.", "**Garnir.** Étalée dans le moule ; vergeoise, beurre en noisettes, crème en filet.",
   "**Cuire.** 200 °C, 20 min : le sucre fond et caramélise. Tiède."], age=1, cats=["enfants"], fetes=["Repas de famille"], profil=["sucre"], tech=["pétrir une brioche"])

K("gratin_savoyard", "Gratin savoyard (pommes de terre au bouillon)", "Gratin savoyard", "France › Auvergne-Rhône-Alpes › Savoie", "A", 1, 6, 20, 70, "€", "Plat à gratin.",
  "Le cousin du dauphinois : pommes de terre cuites au bouillon (et non à la crème), beaufort entre les couches. Plus léger, très parfumé.",
  ["1,2 kg|de pommes de terre|Pomme de terre|3", "150 g|de beaufort ou comté|Gruyère / comté / emmental / beaufort|3", "50 cl|de bouillon de volaille|Bouillon cube volaille|2", f"40 g|de beurre|{BEURRE}|1", f"1 gousse|d'ail|{AIL}|1", f"1 pincée|de muscade|{MUSC}|0"],
  ["**Préparer.** Plat frotté à l'ail, beurré ; pommes de terre en rondelles fines (non lavées : l'amidon lie).", "**Monter.** Couches pommes de terre, fromage, poivre, muscade ; bouillon à hauteur, beurre en noisettes.",
   "**Cuire.** 180 °C, 1 h 10 : le bouillon est absorbé, le dessus doré ; la lame entre sans résistance."], age=1, cats=["enfants", "vegetarien"], fetes=["Noël"])

K("soupe_corse", "Soupe corse aux haricots et aux légumes", "Suppa corsa", CO, "So", 1, 6, 25, 80, "€", "Faitout.",
  "La soupe paysanne de montagne : haricots, chou, pommes de terre, oignon, herbes du maquis et pâtes, servie épaisse avec du fromage de brebis.",
  ["200 g|de haricots blancs secs (ou 2 boîtes)|Haricots blancs / lingots|3", "¼|chou vert|Chou vert / frisé / kale|2", f"3|pommes de terre|{PDT}|2", f"2|carottes|{CAROTTE}|1", f"1|oignon|{OIG}|1", f"2 gousses|d'ail|{AIL}|1", f"80 g|de petites pâtes|{PATES}|1", f"1 c. à c.|de thym|{THYM}|1", f"40 g|de pecorino ou brebis|Pecorino|1?"],
  ["**Base.** Haricots trempés une nuit (ou en boîte) ; oignon et ail 5 min dans l'huile d'olive.", "**Mijoter.** Légumes en morceaux, haricots, herbes, 2 l d'eau ; 1 h (20 min avec des haricots en boîte).",
   "**Finir.** Pâtes 10 min ; soupe épaisse ; fromage râpé et un filet d'huile."], age=1, cats=["vegetarien"], profil=["leger"])
