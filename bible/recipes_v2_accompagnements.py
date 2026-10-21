# -*- coding: utf-8 -*-
"""Vague 2 · Accompagnements de base et classiques français manquants (pour compléter menus et composeur)."""
from recipes_v2_base import *

AC = "France › Accompagnements"; QF = "France › Cuisine du quotidien"

K("puree_maison", "Purée maison au beurre", "Purée de pommes de terre", AC, "A", 1, 4, 10, 25, "€", "Casserole, presse-purée.",
  "Pommes de terre farineuses, lait chaud, beurre froid : la vraie purée lisse, sans mixeur (qui la rend élastique).",
  [f"1 kg|de pommes de terre farineuses (bintje)|{PDT}|3", f"20 cl|de lait chaud|{LAIT}|2", f"80 g|de beurre froid|{BEURRE}|2", f"1 pincée|de muscade|{MUSC}|0"],
  ["**Cuire.** Départ eau froide salée, 20-25 min.", "**Écraser.** Au presse-purée, chaud ; dessèche 1 min sur le feu.", "**Monter.** Beurre froid en dés, puis lait chaud, muscade."], age=1, cats=["enfants"], profil=["gras"], kids="✓ dès 6 mois sans sel.")
K("pommes_terre_four", "Pommes de terre rôties croustillantes", "Pommes de terre rôties", AC, "A", 1, 4, 10, 45, "€", "Plaque.",
  "Précuites, secouées pour abîmer les bords, rôties à l'huile : croûte craquante, cœur fondant.",
  [f"1 kg|de pommes de terre|{PDT}|3", f"4 c. à s.|d'huile d'olive|{HO}|2", f"4 gousses|d'ail en chemise|{AIL}|1", f"2 branches|de romarin|{THYM}|1"],
  ["**Précuire.** Quartiers 8 min à l'eau salée ; égoutte, secoue dans la casserole.", "**Rôtir.** Huile chaude sur la plaque, 40 min à 220 °C en retournant une fois."], age=1, cats=["enfants"], profil=["gras"])
K("haricots_verts_persillade", "Haricots verts à la persillade", "Haricots verts persillés", AC, "A", 1, 4, 10, 10, "€", "Casserole, poêle.",
  "Haricots cuits à l'anglaise (verts et croquants), sautés au beurre avec ail et persil.",
  ["500 g|de haricots verts|Haricots verts|3", f"20 g|de beurre|{BEURRE}|1", f"1 gousse|d'ail|{AIL}|1", f"1 c. à s.|de persil|{PERSIL}|1"],
  ["**Cuire.** Eau bouillante très salée, 6-8 min ; eau glacée (couleur).", "**Sauter.** Beurre, ail, persil, 2 min."], age=1, cats=["enfants"], profil=["leger"])
K("carottes_vichy", "Carottes Vichy", "Carottes Vichy", AC, "A", 1, 4, 10, 25, "€", "Sauteuse avec couvercle.",
  "Carottes glacées au beurre et au sucre dans peu d'eau : brillantes et fondantes.",
  [f"800 g|de carottes|{CAROTTE}|3", f"30 g|de beurre|{BEURRE}|2", f"1 c. à c.|de sucre|{SUCRE}|1", f"1 c. à s.|de persil|{PERSIL}|0"],
  ["**Glacer.** Rondelles, eau à mi-hauteur, beurre, sucre, sel ; couvert 15 min, puis découvert jusqu'à évaporation : elles brillent."], age=1, cats=["enfants"], profil=["sucre"])
K("petits_pois_carottes", "Petits pois-carottes à la française", "Petits pois à la française", AC, "A", 1, 4, 10, 20, "€", "Sauteuse.",
  "Petits pois, carottes, oignons nouveaux et laitue étuvés au beurre : doux et printaniers.",
  ["500 g|de petits pois|Petits pois / pois gourmands|3", f"3|carottes|{CAROTTE}|2", "6|oignons nouveaux|Oignon nouveau / cébette|1", "½|laitue|Salade (laitue, batavia)|1", f"30 g|de beurre|{BEURRE}|1", f"1 pincée|de sucre|{SUCRE}|0"],
  ["**Étuver.** Tout, 10 cl d'eau, couvert 20 min à feu doux."], age=1, cats=["enfants"], profil=["leger"])
K("riz_pilaf", "Riz pilaf", "Riz pilaf", AC, "A", 1, 4, 5, 20, "€", "Casserole avec couvercle.",
  "Riz nacré au beurre avec oignon puis cuit au bouillon, couvert : grains bien séparés.",
  [f"250 g|de riz long|{RIZ}|3", f"1|oignon|{OIG}|1", f"20 g|de beurre|{BEURRE}|1", f"40 cl|de bouillon chaud|{BOUILLON}|2", "1|feuille de laurier|Laurier|0"],
  ["**Nacrer.** Oignon, riz 2 min dans le beurre.", "**Cuire.** Bouillon (1,5 volume), laurier, couvert 17 min ; repos 5 min."], age=1, cats=["enfants"], profil=["leger"], tech=["Cuire le riz"])
K("polenta_cremeuse", "Polenta crémeuse au parmesan", "Polenta", "Europe du Sud › Italie › Vénétie", "A", 1, 4, 5, 15, "€", "Casserole, fouet.",
  "Semoule de maïs cuite dans le lait et le bouillon, finie au beurre et parmesan : crémeuse comme une purée.",
  ["200 g|de polenta|Polenta / semoule de maïs|3", f"50 cl|de lait|{LAIT}|2", f"50 cl|de bouillon|{BOUILLON}|2", f"30 g|de beurre|{BEURRE}|1", f"50 g|de parmesan|{PARM}|2"],
  ["**Cuire.** Polenta en pluie dans le liquide bouillant en fouettant ; 10 min à feu doux.", "**Finir.** Beurre, parmesan."], age=1, cats=["enfants"], profil=["gras"])
K("chou_rouge_pommes", "Chou rouge braisé aux pommes", "Chou rouge aux pommes", "Europe du Nord & Centrale › Allemagne", "A", 1, 6, 15, 60, "€", "Cocotte.",
  "Chou rouge mijoté avec pommes, oignon, vinaigre et un peu de sucre : aigre-doux, pour volailles et gibiers.",
  ["1|chou rouge|Chou blanc / rouge|3", "2|pommes|Pomme|2", f"1|oignon|{OIG}|1", "5 cl|de vinaigre de cidre|Vinaigre de cidre|2", f"2 c. à s.|de sucre|{SUCRE}|1", "2|clous de girofle + 1 feuille de laurier|Clou de girofle|1", f"30 g|de beurre|{BEURRE}|1"],
  ["**Fondre.** Oignon au beurre.", "**Braiser.** Chou émincé, pommes, vinaigre, sucre, épices, 10 cl d'eau, couvert 1 h."], age=1, fetes=["Noël"], profil=["acide", "sucre"])
K("champignons_persilles", "Champignons persillés", "Champignons à la persillade", AC, "A", 1, 4, 10, 10, "€", "Poêle.",
  "Champignons saisis à feu vif sans les serrer, ail et persil : dorés, pas bouillis.",
  ["500 g|de champignons|Champignon de Paris|3", f"20 g|de beurre + 1 c. à s. d'huile|{BEURRE}|1", f"2 gousses|d'ail|{AIL}|1", f"1 bouquet|de persil|{PERSIL}|1"],
  ["**Saisir.** Feu vif, en une couche, sans saler ; 6 min.", "**Finir.** Sel, ail, persil, 1 min."], age=1, cats=["enfants"], profil=["leger"])
K("semoule_legumes", "Semoule aux légumes et raisins", "Semoule parfumée", "Afrique du Nord › Maroc", "A", 1, 4, 10, 10, "€", "Saladier, poêle.",
  "Semoule gonflée au bouillon, petits légumes poêlés, raisins et amandes : l'accompagnement des grillades.",
  ["250 g|de semoule moyenne|Semoule de couscous|3", f"25 cl|de bouillon chaud|{BOUILLON}|2", "1|courgette|Courgette|1", f"1|carotte|{CAROTTE}|1", "40 g|de raisins secs|Raisins secs|1", "30 g|d'amandes effilées|Amande (entière, effilée, poudre)|1", f"1 c. à c.|de ras el-hanout|Ras el-hanout|1", f"2 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Gonfler.** Semoule + huile + bouillon, couvert 5 min, égrenée.", "**Légumes.** En petits dés poêlés avec l'épice, amandes, raisins ; mélangés."], age=1, cats=["enfants"], profil=["leger"])
K("gratin_chou_fleur", "Gratin de chou-fleur", "Chou-fleur gratiné", AC, "A", 1, 4, 15, 25, "€", "Plat à gratin.",
  "Chou-fleur juste tendre, béchamel au fromage, gratiné : l'accompagnement qui fait aimer le chou.",
  ["1|chou-fleur|Chou-fleur|3", "1|recette de béchamel|SUB:bechamel|2", f"80 g|de fromage râpé|{GRUY}|2", f"1 pincée|de muscade|{MUSC}|0"],
  ["**Cuire.** Bouquets 8 min à l'eau salée.", "**Gratiner.** Béchamel, fromage, 20 min à 200 °C."], age=1, cats=["enfants"], profil=["gras"])
K("salade_chevre_chaud", "Salade de chèvre chaud au miel", "Salade de chèvre chaud", QF, "E", 1, 4, 10, 8, "€", "Plaque, four.",
  "Toasts de chèvre gratinés au miel et thym sur une salade aux noix, vinaigrette balsamique.",
  ["8 tranches|de baguette|Baguette tradition|2", "200 g|de bûche de chèvre|Chèvre (frais, bûche)|3", f"2 c. à s.|de miel|{MIEL}|1", "1|salade (mesclun)|Roquette / mâche|2", "40 g|de noix|Noix|1", "2 c. à s.|de vinaigre balsamique|Vinaigre balsamique|1", f"4 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Toasts.** Chèvre sur pain, miel, thym, 6-8 min sous le gril.", "**Salade.** Vinaigrette, noix, toasts chauds dessus."], age=3, profil=["gras"])
K("veloute_butternut_coco", "Velouté de butternut au lait de coco", "Velouté de courge", QF, "So", 1, 6, 15, 30, "€", "Faitout, mixeur.",
  "Courge butternut, carotte, gingembre et lait de coco : un velouté orange, doux et légèrement épicé.",
  ["1|courge butternut|Butternut / courge musquée|3", f"2|carottes|{CAROTTE}|1", f"1|oignon|{OIG}|1", f"1 morceau|de gingembre|{GING}|1", f"20 cl|de lait de coco|{COCO}|2", f"80 cl|de bouillon|{BOUILLON}|2", f"1 pincée|de curry|{CUR}|1"],
  ["**Cuire.** Tout en morceaux (sauf coco), 25 min.", "**Mixer.** Coco, sel."], age=1, cats=["enfants"], profil=["leger"], kids="✓ dès 6 mois sans sel ni curry.")
K("soupe_lentilles_corail", "Soupe de lentilles corail au cumin (mercimek)", "Mercimek çorbası", "Moyen-Orient & Caucase › Turquie", "So", 1, 4, 10, 25, "€", "Casserole, mixeur.",
  "Lentilles corail, carotte, oignon, cumin, mixées et relevées d'un beurre au paprika et de citron.",
  ["250 g|de lentilles corail|Lentilles corail|3", f"1|carotte|{CAROTTE}|1", f"1|oignon|{OIG}|1", f"1 c. à c.|de cumin|{CUMIN}|2", f"1 L|de bouillon|{BOUILLON}|2", f"20 g|de beurre + 1 c. à c. de paprika|{BEURRE}|1", f"1|citron|{CIT}|1"],
  ["**Cuire.** Tout 20 min ; mixe.", "**Servir.** Beurre fondu au paprika en filet, citron."], age=1, cats=["enfants"], fetes=["Ramadan / Aïd"], profil=["leger"])
K("soupe_poisson_rouille", "Soupe de poissons, rouille et croûtons", "Soupe de poissons", "France › Provence-Alpes-Côte d'Azur › Marseille", "So", 2, 6, 30, 50, "€€", "Faitout, moulin à légumes ou mixeur, chinois.",
  "Petits poissons de roche (ou parures et têtes), tomate, fenouil et safran, mixés et filtrés : une soupe profonde avec rouille et croûtons aillés.",
  ["1,2 kg|de poissons de soupe ou têtes et arêtes|Fumet / bouillon de poisson|3", f"3|tomates|{TOM}|2", "1|bulbe de fenouil|Fenouil|1", f"2|oignons + 1 poireau|{OIG}|1", f"4 gousses|d'ail|{AIL}|1", "1 pincée|de safran|Safran (pistils)|2", f"1 c. à s.|de concentré|{CONC}|1", f"5 c. à s.|d'huile d'olive|{HO}|1", "1|recette de rouille (mayonnaise au safran)|SUB:mayo_safran|2", "1|recette de croûtons|SUB:croutons_chapelure|1"],
  ["**Suer.** Légumes à l'huile, concentré ; poissons, 10 min en remuant.", "**Cuire.** 2 L d'eau, safran, 30 min.", "**Passer.** Mixe et filtre en pressant fort.", "**Servir.** Croûtons frottés d'ail, rouille, fromage râpé."],
  age=3, cats=["zero_dechet"], profil=["poisson"], tech=["Fumet"])
K("tourte_poulet_champignons", "Tourte poulet-champignons", "Chicken and mushroom pie", QF, "P", 1, 6, 30, 40, "€€", "Moule à tourte.",
  "Poulet et champignons dans une sauce crémeuse, sous un couvercle de pâte feuilletée dorée.",
  ["2|pâtes feuilletées|Pâte feuilletée (prête)|3", f"500 g|de poulet en dés|{BLANC_P}|3", "300 g|de champignons|Champignon de Paris|2", f"1|oignon|{OIG}|1", f"20 cl|de crème|{CF}|2", f"10 cl|de bouillon|{BOUILLON}|1", f"1 c. à s.|de maïzena|Fécule de maïs (maïzena)|1", f"1|œuf|{OEUF}|1"],
  ["**Garniture.** Poulet doré, oignon, champignons, bouillon, crème, maïzena : épaisse. Refroidie.", "**Monter.** Pâte, garniture, couvercle, cheminée, dorure.", "**Cuire.** 35 min à 200 °C."], age=1, cats=["enfants"], profil=["gras"])
K("filet_lieu_beurre_blanc", "Filet de lieu au beurre blanc, riz", "Lieu au beurre blanc", "France › Pays de la Loire › Nantes", "P", 1, 4, 15, 15, "€€", "Poêle, casserole.",
  "Un poisson blanc abordable, rôti côté peau, nappé du beurre blanc nantais.",
  ["4|filets de lieu noir|Colin, lieu noir, merlu|3", "1|recette de beurre blanc|SUB:beurre_blanc|3", f"250 g|de riz|{RIZ}|2", f"1 c. à s.|d'huile|{HN}|1"],
  ["**Poisson.** Côté peau, 5 min, retourne 1 min.", "**Servir.** Riz, poisson, beurre blanc."], age=1, cats=["enfants"], profil=["poisson"], tech=["Cuisson du poisson"])
