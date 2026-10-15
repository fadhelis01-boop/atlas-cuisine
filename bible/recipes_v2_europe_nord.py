# -*- coding: utf-8 -*-
"""Vague 2 · Europe du Nord & Centrale : Royaume-Uni, Irlande, Belgique, Allemagne, Europe centrale, Scandinavie, Europe de l'Est."""
from recipes_v2_base import *

M = "Europe du Nord & Centrale"

K("fish_and_chips", "Fish and chips (pâte à la bière ou pétillante)", "Fish and chips", f"{M} › Royaume-Uni", "P", 2, 4, 30, 20, "€€", "Friteuse ou casserole profonde, thermomètre.",
  "Un poisson blanc nacré sous une pâte très croustillante, des frites épaisses et une sauce tartare.",
  ["4|filets de cabillaud épais|Cabillaud / morue fraîche|3", f"1 kg|de pommes de terre|{PDT}|3", f"200 g|de farine|{F55}|2", "25 cl|de bière blonde très froide|Bière (blonde, brune, blanche)|2",
   f"1 c. à c.|de levure chimique|{LEVC}|1", "2 L|d'huile de friture|Huile d'arachide|1", f"1|citron|{CIT}|1"],
  ["**Frites.** Bâtonnets épais, 1re friture 8 min à 150 °C, égoutte.", "**Pâte.** Farine, levure, sel, bière glacée : fouette juste, quelques grumeaux.",
   "**Poisson.** Sèche-le, farine-le, trempe, plonge 6 min à 180 °C, doré.", "**Frites.** 2e friture 3 min à 180 °C. Sel, citron, tartare."],
  var=[("Sans alcool", ["alcohol"], {"Bière (blonde, brune, blanche)": [("Bière 0,0 % / vin désalcoolisé", 1.0)]}, "Bière → **bière 0,0 % ou eau gazeuse glacée** : les bulles et le froid font le croustillant. **À tester**.")],
  age=3, cats=["enfants"], kids="✓ dès 3 ans avec la pâte à l'eau gazeuse.", profil=["poisson", "gras"])

K("shepherds_pie", "Shepherd's pie (hachis d'agneau)", "Shepherd's pie", f"{M} › Royaume-Uni", "P", 1, 6, 30, 40, "€€", "Plat à gratin, sauteuse.",
  "Agneau haché mijoté aux légumes et à la sauce Worcestershire, sous une purée striée gratinée.",
  ["700 g|d'agneau haché|Agneau haché|3", f"1,2 kg|de pommes de terre|{PDT}|3", f"2|carottes|{CAROTTE}|1", f"1|oignon|{OIG}|1", "150 g|de petits pois|Petits pois / pois gourmands|1", f"1 c. à s.|de concentré de tomate|{CONC}|1",
   "1 c. à s.|de sauce Worcestershire|Sauce Worcestershire|2", f"30 cl|de bouillon|{BOUILLON}|1", f"60 g|de beurre|{BEURRE}|2", f"10 cl|de lait|{LAIT}|1", "60 g|de cheddar râpé|Cheddar|1"],
  ["**Garniture.** Oignon, carottes, agneau doré ; concentré, Worcestershire, bouillon ; 20 min. Petits pois.", "**Purée.** Beurre, lait, sel.", "**Monter.** Purée striée à la fourchette, cheddar ; 25 min à 200 °C."],
  tips=["La sauce Worcestershire contient des anchois : à signaler aux allergiques au poisson."], age=1, cats=["enfants"], profil=["viande_rouge"])

K("scones", "Scones et crème", "Scones", f"{M} › Royaume-Uni", "G", 1, 10, 15, 15, "€", "Plaque, emporte-pièce.",
  "Petits pains briochés qui s'ouvrent en deux, avec confiture et crème épaisse : le cream tea.",
  [f"350 g|de farine|{F55}|3", f"85 g|de beurre froid|{BEURRE}|2", f"3 c. à s.|de sucre|{SUCRE}|1", f"1 sachet|de levure chimique|{LEVC}|1", f"17 cl|de lait|{LAIT}|2", "1 c. à s.|de jus de citron|Jus de citron (bouteille)|0", "1 pot|de confiture de fraises|Confiture / gelée|1", "20 cl|de crème épaisse|Crème épaisse|2"],
  ["**Sabler.** Farine, levure, sucre, beurre froid du bout des doigts : sable.", "**Lier.** Lait + citron, mélange sans pétrir. Étale à 3 cm.", "**Cuire.** Ronds de 6 cm, dorés au lait, 12 min à 220 °C : ils doublent."],
  age=1, cats=["enfants"], profil=["sucre"], sa=["Thé noir"])

K("crumble_pommes_mures", "Crumble pommes-mûres", "Apple and blackberry crumble", f"{M} › Royaume-Uni", "D", 1, 6, 15, 35, "€", "Plat à four.",
  "Fruits fondants sous un sable croustillant beurré : le dessert de l'automne anglais.",
  ["6|pommes|Pomme|3", "200 g|de mûres (ou fruits rouges surgelés)|Framboise / mûre / myrtille|2", f"150 g|de farine|{F55}|2", f"100 g|de beurre froid|{BEURRE}|2", f"100 g|de cassonade|{SUCRE}|2", "40 g|de flocons d'avoine|Avoine (flocons)|1", f"1 pincée|de cannelle|{CANN}|0"],
  ["**Fruits.** Pommes en cubes + mûres + cannelle dans le plat.", "**Crumble.** Farine, avoine, sucre, beurre en sable grossier.", "**Cuire.** 35 min à 190 °C : bouillonnant sur les bords."],
  age=1, cats=["enfants", "zero_dechet"], profil=["sucre"])

K("irish_stew", "Irish stew", "Irish stew", f"{M} › Irlande", "P", 1, 6, 25, 120, "€€", "Cocotte.",
  "L'agneau, les pommes de terre et les oignons, longuement mijotés : le bouillon épaissit tout seul.",
  ["1,2 kg|de collier ou d'épaule d'agneau|Collier d'agneau|3", f"1,2 kg|de pommes de terre|{PDT}|3", f"3|oignons|{OIG}|2", f"3|carottes|{CAROTTE}|2", f"2 branches|de thym|{THYM}|1", f"1 bouquet|de persil|{PERSIL}|1"],
  ["**Monter.** Couches de pommes de terre, agneau, oignons, carottes, thym, sel.", "**Cuire.** Eau à hauteur, 2 h à petit frémissement à couvert. Persil."],
  age=1, profil=["viande_rouge"], fetes=["Repas de famille"])

K("soda_bread", "Soda bread irlandais", "Soda bread", f"{M} › Irlande", "Pa", 1, 8, 10, 40, "€", "Plaque, four.",
  "Un pain sans levure ni pétrissage, levé au bicarbonate et au lait fermenté : prêt en 50 minutes.",
  ["450 g|de farine complète et blanche (moitié-moitié)|Farine T110 / T150 (complète)|3", "40 cl|de lait ribot (ou lait + 1 c. à s. de citron)|Lait ribot / lait fermenté|2", "1 c. à c.|de bicarbonate|Bicarbonate de soude|1", f"1 c. à c.|de sel|{SEL}|0"],
  ["**Mélanger.** Farines, bicarbonate, sel ; lait ribot ; pâte collante, ne pétris pas.", "**Former.** Boule, croix profonde au couteau.", "**Cuire.** 40 min à 210 °C : sonne creux dessous."],
  age=1, cats=["pains"], profil=["leger"])

K("moules_frites", "Moules-frites à la belge", "Mosselen met friet", f"{M} › Belgique", "P", 1, 4, 20, 15, "€€", "Grande cocotte, friteuse.",
  "Moules marinières au céleri et aux échalotes, frites croustillantes cuites deux fois.",
  ["3 kg|de moules|Moules|3", f"1,2 kg|de pommes de terre bintje|{PDT}|3", "2|branches de céleri|Céleri-branche|2", f"3|échalotes|{ECH}|1", f"30 g|de beurre|{BEURRE}|1", f"10 cl|de vin blanc (facultatif)|Vin blanc|1?", f"1 bouquet|de persil|{PERSIL}|1", "2 L|d'huile de friture|Huile d'arachide|1"],
  ["**Frites.** Deux bains : 150 °C 7 min, puis 180 °C 2 min.", "**Moules.** Céleri et échalotes fondus au beurre, moules, vin ; couvre, feu vif, 5 min en secouant : toutes ouvertes. Persil."],
  tips=["Jette les moules ouvertes avant cuisson et fermées après."], age=3, profil=["poisson"], a=["Bière blanche"], sa=["Bière 0,0 %"])

K("stoemp", "Stoemp aux carottes", "Stoemp", f"{M} › Belgique › Bruxelles", "A", 1, 4, 15, 25, "€", "Casserole, presse-purée.",
  "Une purée rustique de pommes de terre écrasée avec un légume (carottes, poireaux, épinards) et du beurre.",
  [f"800 g|de pommes de terre|{PDT}|3", f"500 g|de carottes|{CAROTTE}|3", f"1|oignon|{OIG}|1", f"40 g|de beurre|{BEURRE}|2", f"1 pincée|de muscade|{MUSC}|0"],
  ["**Cuire.** Pommes de terre, carottes et oignon ensemble 25 min.", "**Écraser.** Grossièrement avec le beurre, muscade, sel, poivre."],
  age=1, cats=["enfants", "zero_dechet"], profil=["leger"])

K("speculoos_maison", "Speculoos maison", "Speculaas", f"{M} › Belgique", "G", 1, 40, 25, 15, "€", "Plaque, emporte-pièces.",
  "Biscuits croquants à la cassonade et aux épices de Noël : la base du célèbre tartinable.",
  [f"250 g|de farine|{F55}|3", "150 g|de vergeoise brune ou cassonade|Sucre blanc / roux / cassonade / vergeoise|3", f"125 g|de beurre mou|{BEURRE}|2", f"1|œuf|{OEUF}|1", f"1 c. à c.|de cannelle|{CANN}|2", "½ c. à c.|de quatre-épices|Quatre-épices|1", "½ c. à c.|de bicarbonate|Bicarbonate de soude|0"],
  ["**Pâte.** Beurre + vergeoise, œuf, farine, épices, bicarbonate. 2 h au frais (ou une nuit).", "**Découper.** Étale à 3 mm, formes.", "**Cuire.** 12 min à 180 °C."],
  keep="3 semaines en boîte métallique.", age=1, cats=["enfants", "fetes"], fetes=["Noël", "Saint-Nicolas"], profil=["sucre"])

K("liege_gaufres", "Gaufres de Liège", "Gaufres de Liège", f"{M} › Belgique › Liège", "G", 2, 12, 30, 90, "€€", "Gaufrier à gaufres de Liège (ou classique).",
  "Une pâte briochée parsemée de sucre perlé qui caramélise dans le gaufrier : croustillant et fondant.",
  [f"500 g|de farine|{F45}|3", f"10 cl|de lait tiède|{LAIT}|2", f"3|œufs|{OEUF}|2", f"250 g|de beurre mou|{BEURRE}|3", f"10 g|de levure boulangère sèche|{LEV}|1", "200 g|de sucre perlé (ou sucre en morceaux concassé)|Sucre blanc / roux / cassonade / vergeoise|3", f"1 pincée|de vanille, sel|{VAN}|0"],
  ["**Pâte.** Farine, lait, levure, œufs, sel, vanille ; incorpore le beurre en morceaux. Pousse 1 h.", "**Sucre.** Ajoute le sucre perlé, 12 boules, 15 min de repos.", "**Cuire.** 3 min par gaufre : bien caramélisées. Attention, le sucre est brûlant."],
  age=3, cats=["enfants"], profil=["sucre", "gras"], fetes=["Anniversaire"])

K("currywurst_volaille", "Currywurst (saucisses de volaille)", "Currywurst", f"{M} › Allemagne › Berlin", "P", 1, 4, 15, 15, "€", "Poêle, casserole.",
  "Le snack berlinois : saucisse grillée en tronçons sous une sauce tomate-curry sucrée-épicée.",
  ["8|saucisses de volaille ou de bœuf|Saucisse de bœuf / de veau / de volaille|3", f"300 g|de passata|{PELEES}|2", "3 c. à s.|de ketchup|Ketchup|1", f"2 c. à c.|de curry + pour saupoudrer|{CUR}|2", f"1 c. à c.|de paprika|{PAPRIKA}|1", f"1|oignon|{OIG}|1", f"1 c. à s.|de sucre|{SUCRE}|1", f"1 c. à s.|de vinaigre|{CIDRE}|1"],
  ["**Sauce.** Oignon râpé, curry, paprika, passata, ketchup, sucre, vinaigre, 10 min ; mixe.", "**Saucisses.** Grillées, en tronçons, nappées, curry au tamis. Avec frites ou pain."],
  age=3, cats=["enfants"], profil=["epice", "sucre"])

K("spaetzle_fromage", "Käsespätzle (spätzle gratinés à l'oignon frit)", "Käsespätzle", f"{M} › Allemagne › Souabe", "P", 2, 4, 25, 20, "€", "Casserole, râpe à spätzle ou passoire, poêle.",
  "Pâtes fraîches irrégulières en couches avec fromage fondu et oignons croustillants : la tartiflette souabe.",
  ["1|recette de spätzle (recette liée)|SUB:spatzle|3", "200 g|d'emmental ou de bergkäse râpé|Gruyère / comté / emmental / beaufort|3", f"3|oignons|{OIG}|2", f"40 g|de beurre|{BEURRE}|2", "1 c. à s.|de ciboulette|Ciboulette|0"],
  ["**Oignons.** En rondelles fines, dorés au beurre 15 min jusqu'à croustillants.", "**Couches.** Spätzle chauds et fromage en alternance dans un plat chaud.", "**Finir.** 5 min au four, oignons dessus, ciboulette."],
  age=1, cats=["enfants"], profil=["gras"])

K("apfelstrudel", "Apfelstrudel (strudel aux pommes)", "Apfelstrudel", f"{M} › Autriche › Vienne", "D", 2, 8, 30, 40, "€", "Plaque, torchon, pinceau.",
  "Pommes, raisins, cannelle et chapelure grillée au beurre roulés dans une pâte fine : avec la pâte filo, c'est facile.",
  ["8|feuilles de filo|Pâte filo / feuilles de brick|3", "1 kg|de pommes acidulées|Pomme|3", "60 g|de raisins secs|Raisins secs|1", f"80 g|de sucre|{SUCRE}|2", f"1 c. à c.|de cannelle|{CANN}|2", "60 g|de chapelure|Chapelure|1", f"100 g|de beurre fondu|{BEURRE}|2", "1 c. à s.|de sucre glace|Sucre glace|0"],
  ["**Garniture.** Pommes en fines lamelles, sucre, cannelle, raisins, jus de citron.", "**Chapelure.** Dorée dans 40 g de beurre.", "**Rouler.** Feuilles beurrées superposées, chapelure, pommes sur un tiers ; roule à l'aide du torchon.", "**Cuire.** 40 min à 190 °C. Sucre glace, tiède."],
  age=1, cats=["enfants"], profil=["sucre"], fetes=["Noël"], sa=["Chocolat chaud viennois"])

K("goulash", "Goulash hongrois", "Gulyás", f"{M} › Hongrie", "P", 1, 6, 30, 120, "€€", "Cocotte.",
  "Bœuf mijoté avec beaucoup d'oignons et de paprika doux, carvi et poivrons : une soupe-ragoût rouge et profonde.",
  ["1,2 kg|de paleron en cubes|Paleron|3", f"4|oignons|{OIG}|3", f"3 c. à s.|de paprika doux de Hongrie|{PAPRIKA}|3", "1 c. à c.|de carvi|Carvi / fenouil / anis vert (graines)|1", f"2|poivrons|{POIVRON}|2", f"2|tomates|{TOM}|1", f"3|pommes de terre|{PDT}|2", f"3 c. à s.|d'huile|{HN}|1", f"2 gousses|d'ail|{AIL}|1"],
  ["**Oignons.** Fondus doucement 15 min jusqu'à dorés.", "**Paprika.** Hors du feu (il brûle vite), puis la viande, carvi, ail ; eau à hauteur. 1 h 30.", "**Légumes.** Poivrons, tomates, pommes de terre ; 30 min."],
  keep="4 jours au frigo ; meilleur le lendemain.", age=1, profil=["viande_rouge", "epice"], fetes=["Repas de famille"])

K("pierogi", "Pierogi pommes de terre-fromage", "Pierogi ruskie", f"{M} › Pologne", "P", 2, 6, 60, 15, "€", "Rouleau, verre, grande casserole.",
  "Des raviolis polonais farcis de purée au fromage frais et oignon frit, poêlés au beurre.",
  [f"400 g|de farine|{F55}|3", "20 cl|d'eau tiède|-|0", f"1|œuf|{OEUF}|1", f"500 g|de pommes de terre|{PDT}|3", "250 g|de fromage blanc égoutté|Fromage blanc / faisselle|2", f"2|oignons|{OIG}|2", f"60 g|de beurre|{BEURRE}|2", f"10 cl|de crème fraîche (service)|{CF}|1"],
  ["**Pâte.** Farine, eau, œuf, sel, 2 c. à s. d'huile ; pétris 5 min, repos 30 min.", "**Farce.** Purée + fromage blanc + un oignon frit, poivre.", "**Façonner.** Ronds de 8 cm, farce, soude en demi-lune en pinçant.", "**Cuire.** 3 min après remontée dans l'eau salée, puis poêlés au beurre avec le 2e oignon. Crème."],
  keep="Crus, se congèlent 3 mois.", age=1, cats=["enfants"], profil=["gras"])

K("bortsch", "Bortsch (soupe de betterave)", "Borchtch", f"{M} › Ukraine", "So", 1, 6, 30, 60, "€", "Faitout.",
  "Une soupe rubis de betterave, chou et bœuf, aigre-douce, avec une cuillère de crème et de l'aneth.",
  ["3|betteraves crues|Betterave (crue/cuite)|3", "¼|chou blanc|Chou blanc / rouge|2", f"2|carottes|{CAROTTE}|1", f"2|pommes de terre|{PDT}|1", f"1|oignon|{OIG}|1", "500 g|de bœuf (jarret ou paleron)|Jarret de bœuf|2",
   f"2 c. à s.|de concentré de tomate|{CONC}|1", f"2 c. à s.|de vinaigre|{CIDRE}|1", "1 bouquet|d'aneth|Aneth|1", f"15 cl|de crème|{CF}|1"],
  ["**Bouillon.** Bœuf dans 2 L d'eau, 1 h.", "**Légumes.** Betteraves en julienne revenues avec carotte, oignon, concentré et vinaigre (garde la couleur).", "**Finir.** Pommes de terre, chou, légumes au bouillon, 20 min. Bœuf effiloché, crème, aneth."],
  age=1, profil=["acide"], kids="✓ dès 1 an.")

K("kanelbullar", "Kanelbullar (brioches à la cannelle)", "Kanelbulle", f"{M} › Suède", "G", 2, 16, 40, 120, "€", "Plaque, rouleau.",
  "Des brioches roulées à la cannelle et à la cardamome, au sucre perlé : la pause fika suédoise.",
  [f"500 g|de farine|{F45}|3", f"25 cl|de lait tiède|{LAIT}|2", f"75 g|de beurre mou + 75 g (garniture)|{BEURRE}|2", f"80 g|de sucre + 60 g (garniture)|{SUCRE}|2", f"7 g|de levure|{LEV}|1", "1 c. à c.|de cardamome moulue|Cardamome|2", f"2 c. à s.|de cannelle|{CANN}|2", f"1|œuf (dorure)|{OEUF}|1"],
  ["**Pâte.** Farine, lait, levure, sucre, cardamome, sel, beurre ; pétris 10 min ; pousse 1 h.", "**Garnir.** Rectangle, beurre mou + sucre + cannelle ; roule, tranches de 2 cm.", "**Pousser et cuire.** 40 min dans des caissettes ; dorure, sucre ; 10 min à 220 °C."],
  age=1, cats=["enfants"], profil=["sucre"], sa=["Café", "Chocolat chaud"])

K("boulettes_suedoises", "Boulettes suédoises, sauce crème", "Köttbullar", f"{M} › Suède", "P", 1, 4, 30, 20, "€€", "Poêle.",
  "Petites boulettes moelleuses à la sauce crème, purée et airelles : comme à Stockholm (et ailleurs).",
  [f"500 g|de bœuf et veau hachés|{HACHE}|3", "40 g|de chapelure|Chapelure|1", f"10 cl|de lait|{LAIT}|1", f"1|oignon râpé|{OIG}|1", f"1|œuf|{OEUF}|1", f"25 cl|de bouillon de bœuf|{BOUILLON}|2", f"15 cl|de crème|{CL}|2", "1 c. à s.|de sauce soja|Sauce soja claire|1", "4 c. à s.|de confiture d'airelles ou de canneberges|Confiture / gelée|1"],
  ["**Boulettes.** Chapelure trempée dans le lait, viande, oignon, œuf, sel, piment de la Jamaïque si tu en as ; boules de 3 cm.", "**Dorer.** 10 min en roulant.", "**Sauce.** Bouillon, crème, soja ; réduis jusqu'à nappant, remets les boulettes. Avec purée et confiture."],
  age=1, cats=["enfants"], profil=["viande_rouge", "gras"])

K("gravlax", "Saumon gravlax à l'aneth", "Gravlax", f"{M} › Suède", "E", 1, 8, 15, 2880, "€€€", "Plat, film, poids.",
  "Saumon mariné 48 h au sel, sucre et aneth : soyeux, à trancher très finement, avec une sauce moutarde-miel.",
  ["800 g|de filet de saumon avec peau (congelé 7 jours avant)|Saumon (frais, pavé)|3", "80 g|de gros sel|Sel fin / gros sel / fleur de sel|2", f"80 g|de sucre|{SUCRE}|2", "1 gros bouquet|d'aneth|Aneth|3", f"1 c. à c.|de poivre concassé|{POIVRE}|1", f"2 c. à s.|de moutarde + 1 de miel (sauce)|{DIJON}|1"],
  ["**Mariner.** Sel + sucre + poivre ; couvre la chair, aneth dessus. Filme, sous un poids, 48 h au frigo ; retourne toutes les 12 h.", "**Rincer.** Essuie, recouvre d'aneth haché. Tranches très fines en biais.", "**Sauce.** Moutarde, miel, aneth, huile."],
  tips=["⚠️ Poisson cru : congélation 7 jours à −20 °C au préalable (anisakis) ; déconseillé femmes enceintes et jeunes enfants."], keep="5 jours au frigo.", age=None, fetes=["Noël"], profil=["poisson"])

K("smorrebrod", "Smørrebrød (tartines danoises)", "Smørrebrød", f"{M} › Danemark", "P", 1, 4, 25, 0, "€€", "Planche.",
  "Des tartines ouvertes sur pain de seigle, très garnies : œuf-crevettes, saumon fumé-radis, rôti de bœuf-pickles…",
  ["8 tranches|de pain de seigle|Farine de seigle|2", f"40 g|de beurre|{BEURRE}|1", f"4|œufs durs|{OEUF}|2", "200 g|de crevettes cuites|Crevettes (cuites/crues)|2", "150 g|de saumon fumé|Saumon fumé|2", "6|radis|Radis rose|1", "1 bouquet|d'aneth|Aneth|1", "4 c. à s.|de mayonnaise maison|Jaune d'œuf|1", f"1|citron|{CIT}|1"],
  ["**Base.** Pain beurré bord à bord.", "**Garnir.** Œuf en rondelles + crevettes + mayo + aneth ; saumon + radis + citron. Sers aussitôt, à la fourchette."],
  age=3, profil=["poisson", "leger"], fetes=["Apéritif dînatoire"])

K("kasha", "Kasha de sarrasin aux champignons", "Kasha", f"{M} › Russie", "A", 1, 4, 10, 20, "€", "Casserole.",
  "Le sarrasin grillé cuit comme un riz, au beurre et aux champignons : rustique, sans gluten, plein de goût.",
  ["250 g|de sarrasin grillé (kasha)|Sarrasin (grain, farine)|3", "250 g|de champignons|Champignon de Paris|2", f"1|oignon|{OIG}|1", f"30 g|de beurre|{BEURRE}|2", "50 cl|d'eau|-|0", "1 c. à s.|d'aneth|Aneth|0"],
  ["**Toaster.** Sarrasin 2 min à sec.", "**Cuire.** Eau bouillante salée, couvert, 15 min à feu doux ; repos 5 min.", "**Finir.** Oignon et champignons dorés au beurre, mélangés. Aneth."],
  age=1, profil=["leger"], kids="✓ dès 1 an ; sans gluten.")

K("blinis_saumon", "Blinis maison", "Bliny", f"{M} › Russie", "A", 1, 30, 20, 60, "€", "Poêle à blinis ou poêle.",
  "Petites crêpes épaisses et aérées, au sarrasin et à la levure : avec crème, saumon fumé ou œufs de truite.",
  ["125 g|de farine de sarrasin|Farine de sarrasin|2", f"125 g|de farine de blé|{F55}|2", f"30 cl|de lait tiède|{LAIT}|2", f"2|œufs (séparés)|{OEUF}|2", f"5 g|de levure|{LEV}|1", f"20 g|de beurre fondu|{BEURRE}|1", f"1 pincée|de sel et sucre|{SEL}|0"],
  ["**Pâte.** Farines, lait, levure, jaunes, sel, sucre, beurre ; 1 h de pousse.", "**Blancs.** En neige, incorporés.", "**Cuire.** Petites louches, 1 min par face : bulles, puis retourne."],
  age=1, cats=["enfants", "fetes"], fetes=["Noël", "Nouvel An", "Apéritif dînatoire"], profil=["leger"])
