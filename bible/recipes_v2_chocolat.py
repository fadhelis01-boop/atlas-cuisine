# -*- coding: utf-8 -*-
"""Vague 2 · Chocolaterie maison : gâteaux, confiseries et cadeaux pour toutes les occasions."""
from recipes_v2_base import *

CH = "France › Chocolaterie"
LAITCH = "Chocolat au lait"; BLANC = "Chocolat blanc"; CACAO = "Cacao en poudre non sucré"

K("truffes_chocolat", "Truffes au chocolat noir", "Truffe en chocolat", CH, "G", 1, 30, 25, 240, "€€", "Casserole, maryse, cuillère parisienne ou poche.",
  "Une ganache ferme roulée dans le cacao : la confiserie de Noël la plus simple et la plus luxueuse.",
  [f"250 g|de chocolat noir 64-70 %|{CHOCO}|3", f"12,5 cl|de crème entière|{CL}|3", f"25 g|de beurre mou|{BEURRE}|1", f"50 g|de cacao non sucré|{CACAO}|2", "1 pincée|de fleur de sel|Sel fin / gros sel / fleur de sel|0"],
  ["**Ganache.** Crème frémissante sur le chocolat haché en 3 fois, émulsionne ; beurre à 35 °C, sel.", "**Prise.** Filmée au contact, 3 h au frais (ou une nuit).", "**Bouler.** Petites boules de 2 cm, roulées rapidement entre les paumes froides puis dans le cacao."],
  keep="2 semaines au frigo, en boîte.", age=3, fetes=["Noël", "Saint-Valentin"], profil=["sucre", "gras"], tech=["Ganache"],
  tips=["Variantes : zeste d'orange, café, épices de Noël, thé earl grey infusés dans la crème."])

K("mendiants", "Mendiants chocolat-fruits secs", "Mendiant", CH, "G", 2, 30, 30, 30, "€€", "Thermomètre, papier cuisson, poche.",
  "Palets de chocolat tempéré garnis d'une amande, d'une noisette, d'une figue et d'un raisin (les quatre ordres mendiants).",
  [f"300 g|de chocolat noir ou au lait de couverture|{CHOCO}|3", "30|amandes|Amande (entière, effilée, poudre)|1", "30|noisettes|Noisette|1", "30|pistaches|Pistache|1", "30|raisins secs ou cranberries|Raisins secs|1", "8|abricots secs en morceaux|Abricots secs|1", "1|orange confite en dés (facultatif)|Fruits confits|0?"],
  ["**Tempérer.** Fonte à 50 °C, ensemencement jusqu'à 28 °C, remonte à 31 °C.", "**Disques.** Petits disques de 4 cm à la poche sur papier.", "**Garnir.** Avant que le chocolat prenne, pose les fruits secs. 1 h à 17 °C."],
  keep="1 mois en boîte, au frais et au sec.", age=3, fetes=["Noël"], profil=["sucre"], tech=["Tempérer"])

K("rochers_praline", "Rochers praliné-amandes", "Rocher praliné", CH, "G", 2, 25, 35, 120, "€€", "Casserole, plaque, papier cuisson.",
  "Un cœur de praliné croustillant enrobé de chocolat au lait aux amandes grillées : comme une célèbre confiserie, en mieux.",
  ["200 g|de praliné maison|Praliné / pâte de noisette|3", f"100 g|de chocolat au lait|{LAITCH}|2", "50 g|de crêpes dentelle ou de flocons de riz soufflé|Biscuits (spéculoos, sablés)|1", "25|noisettes entières grillées|Noisette|2", f"250 g|de chocolat au lait (enrobage)|{LAITCH}|2", "80 g|d'amandes hachées grillées|Amande (entière, effilée, poudre)|2"],
  ["**Intérieur.** Praliné + 100 g de chocolat au lait fondu + crêpes dentelle émiettées ; 1 h au frais.", "**Bouler.** Une noisette au centre de chaque boule ; 30 min au congélateur.", "**Enrober.** Chocolat tempéré + amandes ; trempe chaque boule, pose sur papier."],
  keep="3 semaines au frais.", age=3, fetes=["Noël", "Pâques"], profil=["sucre", "gras"], tech=["Praliné", "Tempérer"])

K("oeufs_paques_chocolat", "Œufs de Pâques garnis maison", "Œuf de Pâques en chocolat", CH, "G", 3, 4, 60, 120, "€€", "Moules à œufs (polycarbonate ou silicone), thermomètre, pinceau.",
  "Deux demi-coques de chocolat tempéré, garnies de petites fritures et de pralinés, soudées : le cadeau de Pâques fait maison.",
  [f"400 g|de chocolat de couverture noir ou au lait|{CHOCO}|3", "200 g|de petits œufs ou mendiants (garniture)|Pépites de chocolat|2", "1 tube|de chocolat blanc pour décorer|Chocolat blanc|1"],
  ["**Coques.** Chocolat tempéré au pinceau dans les moules (fine couche), 10 min, puis 2e couche ; racle les bords. Cristallisation 1 h à 17 °C.", "**Démouler.** Ils se décollent seuls s'ils sont bien tempérés.",
   "**Souder.** Garnis une moitié, pose rapidement le bord de l'autre sur une plaque tiède et colle.", "**Décor.** Chocolat blanc à la poche, rubans."],
  keep="1 mois au frais (pas au frigo).", age=3, cats=["enfants"], fetes=["Pâques"], profil=["sucre"], tech=["Tempérer", "Mouler"])

K("fondant_chocolat", "Fondant au chocolat (cœur coulant ou fondant)", "Fondant au chocolat", CH, "D", 1, 8, 15, 22, "€", "Moule à manqué ou ramequins.",
  "Le gâteau au chocolat qui a fait le tour du monde : peu de farine, beaucoup de chocolat et de beurre, sous-cuit.",
  [f"200 g|de chocolat noir|{CHOCO}|3", f"150 g|de beurre|{BEURRE}|3", f"150 g|de sucre|{SUCRE}|2", f"4|œufs|{OEUF}|2", f"50 g|de farine|{F55}|1", "1 pincée|de fleur de sel|Sel fin / gros sel / fleur de sel|0"],
  ["**Fondre.** Chocolat et beurre doucement.", "**Mélanger.** Œufs + sucre (sans fouetter longtemps), chocolat, farine, sel.",
   "**Cuire.** Moule 22 cm : 22 min à 180 °C (centre tremblotant) ; ramequins : 9-10 min à 200 °C pour un cœur coulant.", "**Repos.** 10 min avant de démouler."],
  age=1, cats=["enfants"], fetes=["Anniversaire", "Saint-Valentin"], profil=["sucre", "gras"])

K("buche_chocolat", "Bûche de Noël chocolat-praliné", "Bûche de Noël", CH, "D", 2, 10, 60, 240, "€€", "Plaque 30 × 40, batteur, torchon.",
  "Un biscuit roulé au cacao, une mousse au praliné et un glaçage ganache strié : le dessert de Noël, sans moule spécial.",
  [f"4|œufs (biscuit)|{OEUF}|2", f"100 g|de sucre|{SUCRE}|2", f"60 g|de farine|{F55}|1", f"20 g|de cacao|{CACAO}|1", "150 g|de praliné|Praliné / pâte de noisette|2", f"40 cl|de crème entière|{CL}|3", f"200 g|de chocolat noir (ganache)|{CHOCO}|3", f"100 g|de chocolat au lait|{LAITCH}|1"],
  ["**Biscuit.** Œufs + sucre au ruban, farine et cacao tamisés ; 8 min à 200 °C ; roule chaud dans un torchon humide.",
   "**Mousse praliné.** 100 g de chocolat au lait fondu + praliné, 25 cl de crème montée incorporée.", "**Rouler.** Déroule, mousse, roule serré. 2 h au frais.",
   "**Glaçage.** 15 cl de crème chaude sur le chocolat noir ; quand il épaissit, couvre la bûche, stries à la fourchette. Coupe les bouts en biais pour faire des branches."],
  keep="3 jours au frigo.", age=1, fetes=["Noël"], profil=["sucre", "gras"], tech=["Biscuit roulé", "Ganache", "Chantilly"])

K("brownies", "Brownies noix de pécan", "Brownie", "Amérique du Nord › États-Unis", "G", 1, 16, 15, 25, "€", "Moule carré 20 cm.",
  "Fondants, croûte craquelée brillante, noix grillées : le secret est de battre œufs et sucre longuement.",
  [f"200 g|de chocolat noir|{CHOCO}|3", f"150 g|de beurre|{BEURRE}|2", f"200 g|de sucre (moitié cassonade)|{SUCRE}|2", f"3|œufs|{OEUF}|2", f"80 g|de farine|{F55}|1", "100 g|de noix de pécan|Noix de pécan|2", f"1 pincée|de sel|{SEL}|0"],
  ["**Fondre.** Chocolat + beurre.", "**Battre.** Œufs + sucres 5 min (c'est ce qui fait la croûte brillante) ; chocolat, farine, sel, noix grillées.", "**Cuire.** 22-25 min à 180 °C : une lame ressort avec des miettes humides. Refroidis avant de couper."],
  age=1, cats=["enfants"], fetes=["Anniversaire"], profil=["sucre", "gras"])

K("chocolat_chaud_viennois", "Chocolat chaud à l'ancienne (et viennois)", "Chocolat chaud", CH, "B", 1, 4, 10, 0, "€", "Casserole, fouet.",
  "Du vrai chocolat fondu dans du lait, épais et mousseux ; chantilly pour la version viennoise.",
  [f"75 cl|de lait entier|{LAIT}|3", f"150 g|de chocolat noir|{CHOCO}|3", f"1 c. à s.|de cacao|{CACAO}|1", f"2 c. à s.|de sucre|{SUCRE}|1", f"1 pincée|de cannelle|{CANN}|0", f"15 cl|de crème montée (viennois)|{CL}|1?"],
  ["**Chauffer.** Lait, sucre, cacao, cannelle ; hors du feu, le chocolat haché.", "**Mousser.** Fouette vivement (ou mixe) 1 min ; remets à frémir.", "**Servir.** Chantilly dessus pour le viennois."],
  age=1, cats=["enfants", "boissons"], fetes=["Noël"], profil=["sucre"])

K("cookies_chocolat", "Cookies aux pépites de chocolat", "Chocolate chip cookies", "Amérique du Nord › États-Unis", "G", 1, 20, 15, 12, "€", "Plaque.",
  "Bords croustillants, cœur moelleux, gros morceaux de chocolat : le repos de la pâte fait le goût caramel.",
  [f"125 g|de beurre mou|{BEURRE}|2", "150 g|de cassonade|Sucre blanc / roux / cassonade / vergeoise|2", f"1|œuf|{OEUF}|1", f"220 g|de farine|{F55}|2", "½ c. à c.|de bicarbonate|Bicarbonate de soude|1", f"200 g|de chocolat noir en morceaux|{CHOCO}|3", "1 pincée|de fleur de sel|Sel fin / gros sel / fleur de sel|0"],
  ["**Pâte.** Beurre + cassonade, œuf, farine + bicarbonate, chocolat.", "**Repos.** 1 h au frais (idéal : 24 h).", "**Cuire.** Boules de 50 g espacées, 11 min à 180 °C : ils semblent pas cuits au centre, c'est normal. Fleur de sel."],
  age=1, cats=["enfants"], fetes=["Anniversaire"], profil=["sucre"])

K("pate_tartiner_maison", "Pâte à tartiner chocolat-noisette maison", "Pâte à tartiner", CH, "Ba", 1, 12, 20, 0, "€€", "Four, robot puissant, bocal.",
  "Sans huile de palme : noisettes grillées, chocolat au lait et un peu de sucre ; plus de goût, moins de sucre.",
  ["200 g|de noisettes|Noisette|3", f"150 g|de chocolat au lait|{LAITCH}|2", f"50 g|de chocolat noir|{CHOCO}|1", "60 g|de sucre glace|Sucre glace|1", f"1 c. à s.|de cacao|{CACAO}|1", "2 c. à s.|d'huile de noisette ou de colza|Huile de noix / de noisette|1", f"1 pincée|de sel|{SEL}|0"],
  ["**Torréfier.** Noisettes 12 min à 160 °C, frotte-les dans un torchon pour retirer la peau.", "**Mixer.** 5-8 min jusqu'à purée coulante (par à-coups).", "**Finir.** Chocolats fondus, sucre glace, cacao, huile, sel ; mixe encore. En bocal."],
  keep="1 mois à température ambiante (elle durcit au frigo).", age=1, cats=["enfants"], profil=["sucre", "gras"], tips=["⚠️ Fruits à coque : allergie fréquente."])

K("sucettes_chocolat", "Sucettes en chocolat pour enfants", "Sucettes chocolat", CH, "G", 1, 12, 20, 60, "€", "Moules à sucettes ou papier cuisson, bâtonnets.",
  "Un atelier pour les enfants : disques de chocolat sur bâtonnets, décorés de vermicelles, fruits secs, pétales.",
  [f"200 g|de chocolat au lait|{LAITCH}|3", f"100 g|de chocolat blanc|{BLANC}|2", "1 poignée|de décors (fruits lyophilisés, noix de coco, pépites)|Noix de coco râpée|1", "12|bâtonnets|-|0"],
  ["**Fondre.** Doucement au micro-ondes, par 20 s, juste fondu (moins de 32 °C, ça prend vite et brille).", "**Couler.** Disques de 5 cm, bâtonnet dedans, un peu de chocolat dessus.", "**Décorer.** Tout de suite ; 1 h au frais."],
  age=3, cats=["enfants"], fetes=["Anniversaire", "Halloween", "Pâques"], profil=["sucre"])

K("bonbons_coeur_framboise", "Bonbons cœur framboise (Saint-Valentin)", "Bonbons de chocolat moulés", CH, "G", 3, 24, 60, 720, "€€", "Moule à bonbons cœur, thermomètre, poche.",
  "Des coques de chocolat noir tempéré garnies d'une ganache framboise : un cadeau qui fait son effet.",
  [f"300 g|de chocolat noir de couverture (coques)|{CHOCO}|3", "100 g|de framboises (purée filtrée)|Framboise / mûre / myrtille|2", f"120 g|de chocolat au lait|{LAITCH}|2", f"5 cl|de crème|{CL}|1", f"10 g|de beurre|{BEURRE}|1"],
  ["**Coques.** Chocolat tempéré, moule rempli, retourné, raclé ; 30 min à 17 °C.", "**Ganache.** Purée + crème chaudes sur chocolat au lait, beurre ; à 28 °C, remplis les coques aux ¾. Une nuit à 17 °C.", "**Fermer.** Chocolat tempéré, racle, 1 h, démoule."],
  keep="2 semaines au frais.", age=3, fetes=["Saint-Valentin"], profil=["sucre"], tech=["Mouler", "Tempérer", "Ganache"])

K("caramels_beurre_sale", "Caramels mous au beurre salé", "Caramel au beurre salé", "France › Bretagne", "G", 2, 40, 20, 180, "€", "Casserole à fond épais, thermomètre, moule carré, papier cuisson.",
  "Des caramels tendres qui fondent : 2 ingrédients clés, le beurre salé et un thermomètre.",
  [f"200 g|de sucre|{SUCRE}|3", "80 g|de sirop de glucose ou de miel|Sirop de glucose|1", f"20 cl|de crème|{CL}|2", f"80 g|de beurre demi-sel|{BEURRE}|3", "1 c. à c.|de fleur de sel|Sel fin / gros sel / fleur de sel|1"],
  ["**Caramel.** Sucre + glucose à sec jusqu'à ambré.", "**Décuire.** Crème chaude en 3 fois (projections), beurre.", "**Cuire.** Jusqu'à 118-120 °C (mous) en remuant.", "**Prise.** Moule chemisé, fleur de sel, 3 h ; coupe en carrés, papier cristal."],
  keep="1 mois en boîte.", age=3, fetes=["Noël"], profil=["sucre", "gras"], tech=["Caramel"])

K("orangettes", "Orangettes", "Orangette", CH, "G", 2, 40, 45, 1440, "€", "Casserole, grille, thermomètre.",
  "Écorces d'orange confites enrobées de chocolat noir : amer, sucré, fondant.",
  ["4|oranges non traitées|Orange|3", f"400 g|de sucre|{SUCRE}|2", f"200 g|de chocolat noir de couverture|{CHOCO}|3"],
  ["**Écorces.** Lanières de 7 mm, blanchies 3 fois (départ eau froide) pour l'amertume.", "**Confire.** Sirop 400 g de sucre + 40 cl d'eau, frémissement 1 h ; égoutte une nuit sur grille.", "**Enrober.** Chocolat tempéré ; trempe aux ¾, pose sur papier."],
  keep="1 mois en boîte.", age=3, cats=["zero_dechet"], fetes=["Noël"], profil=["sucre", "acide"], tech=["Tempérer"], tips=["Les oranges épluchées : jus, salade d'oranges à la cannelle (recette liée)."])

K("mousse_chocolat_blanc", "Mousse au chocolat blanc et fruits rouges", "Mousse au chocolat blanc", CH, "D", 1, 6, 20, 240, "€", "Batteur, verrines.",
  "Une mousse légère au chocolat blanc, sans œuf cru, sur un coulis de fruits rouges acidulé.",
  [f"200 g|de chocolat blanc|{BLANC}|3", f"30 cl|de crème entière bien froide|{CL}|3", "300 g|de fruits rouges|Framboise / mûre / myrtille|2", f"1 c. à s.|de sucre|{SUCRE}|1", f"½|citron vert (zeste)|{CITV}|1"],
  ["**Chocolat.** Fondu avec 10 cl de crème ; tiédis à 30 °C.", "**Mousse.** 20 cl de crème montée, incorporée en 2 fois.", "**Monter.** Coulis mixé au fond des verrines, mousse, fruits, zeste. 4 h au frais."],
  age=1, cats=["enfants"], fetes=["Saint-Valentin", "Anniversaire"], profil=["sucre"], tech=["Chantilly"])

K("fondue_chocolat", "Fondue au chocolat et fruits", "Fondue au chocolat", CH, "D", 1, 6, 20, 0, "€€", "Caquelon ou casserole, piques.",
  "Un chocolat fondu crémeux et des fruits de saison à tremper : le dessert à partager.",
  [f"200 g|de chocolat noir|{CHOCO}|3", f"100 g|de chocolat au lait|{LAITCH}|2", f"20 cl|de crème|{CL}|2", "1 kg|de fruits (fraises, banane, ananas, poire, clémentine)|Banane|3", "Quelques|guimauves ou dés de brioche|Brioche|1?"],
  ["**Fondue.** Crème chaude sur les chocolats, lisse ; garde au chaud à feu très doux.", "**Fruits.** En morceaux, citronnés pour la banane et la poire. Chacun pique et trempe."],
  age=1, cats=["enfants"], fetes=["Anniversaire", "Saint-Valentin"], profil=["sucre"], tech=["Ganache"])

K("gateau_anniversaire_choco", "Gâteau d'anniversaire au chocolat (layer cake)", "Gâteau d'anniversaire", CH, "D", 2, 12, 50, 240, "€€", "2 moules 20 cm, batteur, spatule coudée.",
  "Deux génoises chocolat moelleuses, ganache montée au chocolat au lait : se décore facilement et tient bien.",
  [f"250 g|de farine|{F55}|2", f"60 g|de cacao|{CACAO}|2", f"250 g|de sucre|{SUCRE}|2", f"3|œufs|{OEUF}|2", "25 cl|de babeurre ou lait + citron|Babeurre|2", f"12 cl|d'huile neutre|{HN}|1", "1 c. à c.|de bicarbonate + 1 de levure|Bicarbonate de soude|1",
   f"25 cl|de café chaud ou d'eau chaude|-|0", f"300 g|de chocolat au lait|{LAITCH}|3", f"50 cl|de crème entière|{CL}|3"],
  ["**J-1, ganache montée.** Crème chaude sur chocolat au lait, une nuit au frigo.", "**Gâteaux.** Secs ensemble ; humides ensemble ; mélange, puis café chaud (pâte liquide). 35 min à 170 °C dans 2 moules.",
   "**Monter.** Fouette la ganache comme une chantilly ; gâteau, ganache, gâteau ; fine couche sur tout le tour, 30 min au frais, 2e couche lisse.", "**Décor.** Fruits, copeaux, bougies."],
  age=1, cats=["enfants"], fetes=["Anniversaire"], profil=["sucre", "gras"], tech=["Ganache montée"])

K("eclats_chocolat", "Fruits secs enrobés et écorces de chocolat (cadeau)", "Bark au chocolat", CH, "G", 1, 10, 20, 60, "€", "Plaque, papier cuisson.",
  "Une plaque de chocolat parsemée de fruits secs, pétales, épices, cassée en éclats : le cadeau gourmand le plus rapide.",
  [f"300 g|de chocolat noir|{CHOCO}|3", f"100 g|de chocolat blanc|{BLANC}|2", "60 g|de pistaches|Pistache|1", "40 g|de canneberges séchées|Canneberges séchées|1", "1 pincée|de fleur de sel|Sel fin / gros sel / fleur de sel|0"],
  ["**Étaler.** Chocolat noir tempéré (ou juste fondu) sur papier, 5 mm.", "**Marbrer.** Filets de chocolat blanc, tracés à la pique.", "**Garnir.** Pistaches, canneberges, sel. 1 h au frais, casse en éclats."],
  keep="1 mois en boîte.", age=3, cats=["enfants"], fetes=["Noël"], profil=["sucre"], tech=["Tempérer"])

K("mousse_chocolat_aquafaba", "Mousse au chocolat sans œuf (aquafaba)", "Mousse au chocolat végétale", CH, "D", 1, 6, 15, 240, "€", "Batteur.",
  "Le jus des pois chiches monte comme des blancs : une mousse légère, sans œuf, pour les allergiques et les végétaliens.",
  ["15 cl|d'aquafaba (jus d'un bocal de pois chiches)|Aquafaba (eau de pois chiches)|3", f"200 g|de chocolat noir|{CHOCO}|3", f"40 g|de sucre|{SUCRE}|1", f"1 c. à c.|de jus de citron|{CIT}|0"],
  ["**Monter.** Aquafaba + citron en neige 5 min, puis le sucre : bec d'oiseau.", "**Mélanger.** Chocolat fondu tiède, incorporé en 3 fois délicatement.", "**Prise.** 4 h au frais."],
  age=1, cats=["enfants", "zero_dechet"], profil=["sucre"], tips=["Les pois chiches égouttés : houmous ou pois chiches grillés (recettes liées)."])

K("tablette_chocolat_maison", "Tablettes de chocolat garnies", "Tablette de chocolat", CH, "G", 2, 4, 30, 90, "€€", "Moules à tablettes (ou boîte plate tapissée de papier), thermomètre.",
  "Tablettes épaisses fourrées au praliné croustillant, ou nature décorées : à offrir dans un joli papier.",
  [f"400 g|de chocolat de couverture|{CHOCO}|3", "150 g|de praliné|Praliné / pâte de noisette|2", "40 g|de crêpes dentelle émiettées|Biscuits (spéculoos, sablés)|1", "50 g|de noisettes grillées|Noisette|1"],
  ["**Coque.** Chocolat tempéré dans le moule, retourné, raclé, 20 min.", "**Garnir.** Praliné + crêpes dentelle, laisse 1 cm de bord.", "**Fermer.** Chocolat tempéré, racle, 2 h à 17 °C, démoule."],
  keep="1 mois au frais.", age=3, fetes=["Noël", "Anniversaire"], profil=["sucre"], tech=["Tempérer", "Mouler", "Praliné"])
