# -*- coding: utf-8 -*-
"""Vague 3 · Classiques manquants et régions sous-représentées (audit UX du 16/10/2026) :
salade César (lot salades), fajitas, shawarma, poulet pané, cordon bleu, raclette, tarte aux pommes ;
Océanie, Asie du Sud-Est, Afrique de l'Est, Amérique latine. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

QF = "France › Cuisine du quotidien"; AU = "Océanie › Australie"; NZ = "Océanie › Nouvelle-Zélande"; SM = "Océanie › Samoa"
MY = "Asie du Sud-Est › Malaisie"; ID = "Asie du Sud-Est › Indonésie"; PH = "Asie du Sud-Est › Philippines"; VN = "Asie du Sud-Est › Vietnam"
KE = "Afrique subsaharienne › Kenya"; ET = "Afrique subsaharienne › Éthiopie"; TZ = "Afrique subsaharienne › Tanzanie"

# ——— Classiques demandés par les débutants ———
K("fajitas_poulet", "Fajitas au poulet et aux poivrons", "Fajitas de pollo", "Amérique du Nord › États-Unis › Tex-Mex", "P", 1, 4, 20, 12, "€€", "Grande poêle ou plancha.",
  "Lanières de poulet marinées citron vert-épices, poivrons et oignons saisis à feu vif, tortillas chaudes, guacamole et crème : chacun garnit la sienne.",
  [f"3|blancs de poulet|{BLANC_P}|3", "8|tortillas de blé|Tortillas de blé|3", f"3|poivrons de couleurs|{POIVRON}|2", f"2|oignons|{OIG}|1", "2 c. à c.|de mélange fajitas (ou cumin + paprika + origan)|Mélange tex-mex / fajitas|2", f"2|citrons verts|{CITV}|1", "1|avocat|Avocat|1?", f"4 c. à s.|de crème|{CF}|1?", f"½ bouquet|de coriandre|{CORI}|1?"],
  ["**Mariner.** Poulet en lanières, épices, jus d'un citron vert, huile, sel, 10 min.", "**Saisir.** Poêle fumante : poulet 5 min, réservé ; poivrons et oignons en lanières 5 min : colorés mais croquants ; poulet remis.",
   "**Servir.** Tortillas chauffées, avocat écrasé au citron vert, crème, coriandre ; chacun roule la sienne."],
  age=3, cats=["enfants"], fetes=["Apéritif dînatoire", "Anniversaire"], profil=["epice"])

K("shawarma_poulet", "Shawarma de poulet au four, sauce à l'ail", "Shawarma djaj", "Moyen-Orient › Liban", "P", 1, 4, 20, 25, "€€", "Four, plaque.",
  "Cuisses de poulet marinées aux épices (cumin, paprika, cannelle, citron), rôties puis émincées, dans un pain avec toum, pickles et tomates.",
  [f"6|cuisses de poulet désossées|{CUISSE}|3", "4|pains libanais|Pain pita / libanais|3", f"1 c. à c.|de cumin|{CUMIN}|1", f"1 c. à c.|de paprika|{PAPRIKA}|1", f"½ c. à c.|de cannelle|{CANN}|1", f"1|citron|{CIT}|1", f"125 g|de yaourt|{YAO}|1", "4 c. à s.|de toum (ou sauce yaourt-ail)|SUB:toum|2", "4|cornichons ou navets au vinaigre|Cornichons, oignons au vinaigre|1", f"2|tomates|{TOM}|1"],
  ["**Mariner.** Poulet, yaourt, épices, citron, ail, sel ; 1 h (ou la veille).", "**Rôtir.** 220 °C, 25 min, puis 3 min sous le gril : bords grillés et caramélisés ; émincé finement.",
   "**Rouler.** Pain, toum, poulet, tomates, pickles ; roulé serré, 1 min à la poêle."], age=3, profil=["epice"])

K("poulet_pane_croustillant", "Poulet pané croustillant au four", "Poulet pané", QF, "P", 1, 4, 20, 20, "€", "Four, plaque, 3 assiettes creuses.",
  "Lanières de poulet passées dans la farine, l'œuf et la chapelure au parmesan, cuites au four : croustillantes sans friture.",
  [f"4|blancs de poulet|{BLANC_P}|3", "100 g|de chapelure (ou panko)|Panko|3", f"30 g|de parmesan|{PARM}|1", f"2|œufs|{OEUF}|2", f"50 g|de farine|{F55}|2", f"1 c. à c.|de paprika|{PAPRIKA}|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Paner.** Lanières dans la farine, puis l'œuf battu salé, puis la chapelure au parmesan et paprika (une main sèche, une main mouillée).", "**Cuire.** Plaque huilée, un filet d'huile dessus ; 210 °C, 18-20 min en retournant à mi-cuisson : dorés, jus clair.",
   "**Servir.** Citron, sauce yaourt ou ketchup maison, frites au four."], age=1, cats=["enfants"], tech=["paner à l'anglaise"])

K("cordon_bleu_dinde", "Cordon bleu maison (dinde, jambon de dinde, emmental)", "Cordon bleu", "Europe du Nord › Suisse", "P", 2, 4, 30, 15, "€€", "Poêle, 3 assiettes, film.",
  "Escalope aplatie, roulée autour de jambon et de fromage, panée et dorée : le cordon bleu fait maison, sans porc ici, filant au cœur.",
  ["4|escalopes de dinde fines|Dinde (escalope, cuisse, filet)|3", "4 tranches|de jambon de dinde|Jambon de dinde / de poulet|2", f"4 tranches|d'emmental|{GRUY}|2", f"2|œufs|{OEUF}|2", f"50 g|de farine|{F55}|1", "100 g|de chapelure|Chapelure|2", f"30 g|de beurre|{BEURRE}|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Aplatir.** Escalopes entre deux films, au fond d'une casserole : 5 mm d'épaisseur.", "**Garnir et fermer.** Jambon et fromage sur une moitié, plie, presse les bords ; farine, œuf, chapelure (deux couches sur les bords pour que le fromage ne s'échappe pas).",
   "**Cuire.** Huile et beurre moyens, 6-7 min par face : bien doré ; 2 min de repos."], age=3, cats=["enfants"], tech=["paner à l'anglaise"])

K("raclette_maison", "Raclette à la maison (sans appareil possible)", "Raclette", "Europe du Nord › Suisse › Valais", "P", 1, 6, 15, 25, "€€", "Appareil à raclette, ou plat à four.",
  "Fromage à raclette fondu sur des pommes de terre en robe des champs, cornichons, oignons au vinaigre et viande séchée : le dîner d'hiver convivial.",
  ["1,2 kg|de fromage à raclette|Reblochon / raclette / mont-d'or|3", "1,5 kg|de petites pommes de terre|Pomme de terre|3", "200 g|de viande séchée (Grisons, bresaola)|Viande des Grisons / bresaola|2", "1 bocal|de cornichons et oignons au vinaigre|Cornichons, oignons au vinaigre|1", "1|salade verte|Salade (laitue, batavia)|1", f"1 pincée|de poivre|{POIVRE}|0"],
  ["**Pommes de terre.** Avec la peau, 20-25 min à l'eau salée : la lame entre sans forcer ; gardées au chaud sous un torchon.", "**Fondre.** Dans les poêlons de l'appareil, ou en tranches sur un plat au four sous le gril (3 min : ça bulle).",
   "**Servir.** Le fromage nappé sur les pommes de terre ouvertes, poivre, cornichons, viande, salade verte (indispensable)."],
  age=3, cats=["enfants"], fetes=["Repas de famille", "Noël"], profil=["gras"], keep="Les restes de fromage : en croque-monsieur ou en gratin de pâtes.", a=["Vin blanc de Savoie (apremont)"], sa=["Infusion à la verveine"])

K("tarte_aux_pommes_compote", "Tarte aux pommes de grand-mère (compote et lamelles)", "Tarte aux pommes", QF, "D", 1, 8, 30, 40, "€", "Moule à tarte, four.",
  "Pâte sablée, une couche de compote maison, des lamelles de pommes en rosace dorées au beurre et au sucre : la tarte de toutes les familles.",
  ["1|pâte brisée ou sablée|Pâte brisée / sablée (prête)|3", "6|pommes (dont 2 pour la compote)|Pomme|3", f"40 g|de sucre|{SUCRE}|1", f"30 g|de beurre|{BEURRE}|1", f"½ c. à c.|de cannelle|{CANN}|1?", "2 c. à s.|de confiture d'abricot (nappage)|Confiture / gelée|1?"],
  ["**Compote.** 2 pommes en dés, 2 c. à s. d'eau, 10 g de sucre, 10 min couvert : écrasées à la fourchette.", "**Monter.** Pâte dans le moule piquée, compote, 4 pommes en fines lamelles en rosace serrée ; beurre en noisettes, sucre, cannelle.",
   "**Cuire.** 190 °C, 40 min : bords bien dorés, pommes légèrement caramélisées ; confiture chauffée au pinceau."], age=1, cats=["enfants"], fetes=["Repas de famille"], profil=["sucre"], tech=["foncer une pâte"])

# ——— Océanie ———
K("meat_pie_australien", "Meat pie australien", "Aussie meat pie", AU, "P", 2, 6, 40, 35, "€€", "Moules à tartelette (ou un moule à tourte), four.",
  "La tourte individuelle des stades australiens : bœuf haché mijoté en sauce brune épaisse, pâte brisée dessous, feuilletée dessus, et ketchup.",
  [f"600 g|de bœuf haché|{HACHE}|3", "1|pâte brisée|Pâte brisée / sablée (prête)|2", "1|pâte feuilletée|Pâte feuilletée (prête)|2", f"1|oignon|{OIG}|1", "40 cl|de bouillon de bœuf|Bouillon cube bœuf|2", "2 c. à s.|de sauce Worcestershire|Sauce Worcestershire|1", f"2 c. à s.|de concentré de tomate|{CONC}|1", f"2 c. à s.|de farine|{F55}|1", f"1|œuf (dorure)|{OEUF}|1"],
  ["**Garniture.** Oignon, viande 8 min : dorée ; farine 1 min ; bouillon, sauces ; 20 min : très épaisse (elle ne doit pas couler). Refroidir.",
   "**Monter.** Pâte brisée dans les moules, garniture, couvercle de feuilletée soudé à l'eau ; une entaille, dorure.", "**Cuire.** 200 °C, 30-35 min : gonflé et doré."],
  age=3, cats=["enfants"], fetes=["Anniversaire"], sa=["Ginger beer maison"])

K("damper", "Damper (pain du bush australien)", "Damper", AU, "Pa", 1, 6, 10, 30, "€", "Four (ou cocotte en fonte).",
  "Le pain des stockmen australiens, cuit autrefois dans les braises : farine, levure chimique, beurre et lait, prêt en 40 minutes, sans pétrissage.",
  [f"450 g|de farine|{F55}|3", f"4 c. à c.|de levure chimique|{LEVC}|2", f"60 g|de beurre froid|{BEURRE}|2", f"30 cl|de lait|{LAIT}|2", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Sabler.** Farine, levure, sel ; beurre en dés frotté du bout des doigts : sable grossier.", "**Former.** Lait d'un coup, mélange juste ; boule aplatie, croix au couteau.",
   "**Cuire.** 200 °C, 30 min : creux quand on tape dessous. Tiède avec beurre et golden syrup (ou miel)."], age=1, cats=["pains", "enfants"])

K("sapasui", "Sapasui (vermicelles sautés samoans)", "Sapasui", SM, "P", 1, 4, 20, 15, "€", "Wok ou grande sauteuse.",
  "Le chop suey des îles Samoa, plat de toutes les fêtes : vermicelles de soja, bœuf (ou poulet), légumes, sauce soja et gingembre.",
  ["200 g|de vermicelles de soja|Vermicelles de haricots mungo|3", f"400 g|de bœuf en lanières (ou poulet)|Rumsteck|3", f"1|oignon|{OIG}|1", f"2|carottes|{CAROTTE}|1", "¼|chou|Chou blanc / rouge|1", f"4 c. à s.|de sauce soja|{SOJA}|2", "1 morceau (3 cm)|de gingembre|Gingembre frais|1", f"2 gousses|d'ail|{AIL}|1"],
  ["**Tremper.** Vermicelles 10 min dans l'eau chaude, égouttés, coupés aux ciseaux.", "**Sauter.** Viande 3 min à feu vif ; ail, gingembre, légumes en lanières 4 min.",
   "**Lier.** Vermicelles, soja, un verre d'eau ; 5 min en remuant : ils boivent la sauce et deviennent brillants."], age=3, fetes=["Repas de famille"])

K("palusami", "Palusami (feuilles au lait de coco)", "Palusami", SM, "E", 1, 4, 20, 40, "€€", "Plat à four, papier aluminium.",
  "Paquets de feuilles vertes garnis d'oignon et de crème de coco, cuits au four jusqu'à devenir fondants : le plat du four polynésien (umu).",
  ["400 g|de feuilles de taro, de manioc ou d'épinard|Feuilles de manioc / de patate douce|3", "40 cl|de crème de coco|Lait de coco / crème de coco|3", f"1|oignon|{OIG}|2", f"1|citron vert|{CITV}|1", f"1 pincée|de sel|{SEL}|1"],
  ["**Garnir.** Feuilles en coupelles (plusieurs épaisseurs), oignon émincé, crème de coco salée et citronnée.", "**Fermer.** Chaque paquet dans du papier aluminium.", "**Cuire.** 180 °C, 40 min : feuilles fondantes, crème épaisse. Avec du taro, de la patate douce ou du riz."],
  age=1, cats=["vegetarien"], profil=["gras"])

K("pikelets", "Pikelets (petites crêpes épaisses)", "Pikelets", NZ, "G", 1, 20, 10, 15, "€", "Poêle.",
  "Les petites crêpes épaisses du goûter néo-zélandais : une pâte simple, cuites en ronds de la taille d'une paume, avec beurre et confiture.",
  [f"200 g|de farine|{F55}|3", f"2 c. à c.|de levure chimique|{LEVC}|2", f"1|œuf|{OEUF}|2", f"20 cl|de lait|{LAIT}|2", f"40 g|de sucre|{SUCRE}|1", f"20 g|de beurre fondu|{BEURRE}|1"],
  ["**Pâte.** Farine, levure, sucre ; œuf, lait, beurre : épaisse, sans grumeaux.", "**Cuire.** Cuillerées dans la poêle beurrée moyenne ; retourne quand des bulles apparaissent (1-2 min), puis 1 min.", "**Servir.** Tièdes, beurre et confiture."],
  age=1, cats=["enfants", "brunch"], profil=["sucre"])

K("soupe_potiron_australienne", "Soupe de potiron rôti à l'australienne", "Pumpkin soup", AU, "So", 1, 6, 15, 40, "€", "Four, casserole, mixeur.",
  "Potiron rôti au four avec oignon et ail, mixé avec du bouillon et une pointe de muscade : la soupe préférée des Australiens.",
  ["1,2 kg|de potiron ou butternut|Butternut / courge musquée|3", f"1|oignon|{OIG}|2", f"3 gousses|d'ail|{AIL}|1", "1 l|de bouillon de légumes|Bouillon cube légumes|2", f"1 pincée|de muscade|{MUSC}|1", f"10 cl|de crème|{CF}|1?", "2 c. à s.|de graines de courge|Graines de tournesol / courge|1?"],
  ["**Rôtir.** Potiron en morceaux, oignon, ail en chemise ; huile, sel ; 200 °C, 35 min : caramélisé sur les bords.", "**Mixer.** Avec le bouillon chaud, ail pressé hors de sa peau, muscade : très lisse.", "**Servir.** Crème en tourbillon, graines grillées."],
  age=1, cats=["enfants", "vegetarien"], profil=["leger"])

K("poulet_hangi_four", "Poulet et légumes racines façon hangi (au four)", "Hāngī", NZ, "P", 1, 6, 25, 90, "€€", "Grand plat à four, papier aluminium.",
  "Le hangi maori cuit dans un four creusé dans la terre ; à la maison : poulet, patate douce (kumara), potiron et chou cuits longtemps à l'étouffée, fondants et fumés.",
  [f"6|cuisses de poulet|{CUISSE}|3", "3|patates douces|Patate douce|2", "600 g|de potiron|Potiron / citrouille|2", f"4|pommes de terre|{PDT}|2", "¼|chou vert|Chou vert / frisé / kale|1", f"2 c. à c.|de paprika fumé|{PFUME}|1", f"1 c. à c.|de thym|{THYM}|1", "20 cl|d'eau|-|1"],
  ["**Préparer.** Légumes en gros morceaux au fond du plat, poulet dessus, paprika fumé (pour le goût de la terre), thym, sel, eau.",
   "**Étouffer.** Feuilles de chou par-dessus, papier aluminium bien serré.", "**Cuire.** 170 °C, 1 h 30 : la viande se détache, les légumes fondent ; 10 min découvert pour dorer."],
  age=1, cats=["enfants"], fetes=["Repas de famille"])

# ——— Asie du Sud-Est ———
K("mee_goreng", "Mee goreng (nouilles sautées malaisiennes)", "Mee goreng mamak", MY, "P", 1, 2, 15, 8, "€", "Wok.",
  "Nouilles jaunes sautées à la sauce soja sucrée, sambal, tofu, chou, œuf et citron vert : le plat de rue des échoppes mamak.",
  ["300 g|de nouilles aux œufs|Nouilles chinoises aux œufs|3", "2 c. à s.|de kecap manis|Kecap manis|2", f"1 c. à s.|de sauce soja|{SOJA}|1", "1 c. à c.|de sambal oelek|Sambal oelek|1", "100 g|de tofu|Tofu (ferme / soyeux)|1", "¼|chou chinois|Chou chinois / pak-choï|1", f"2|œufs|{OEUF}|2", f"1|citron vert|{CITV}|1", f"2 gousses|d'ail|{AIL}|1"],
  ["**Préparer.** Nouilles cuites 3 min, égouttées ; tofu en dés doré.", "**Sauter.** Ail, sambal 30 s ; chou 1 min ; œufs brouillés ; nouilles et sauces, 2 min : elles brillent et caramélisent un peu.", "**Servir.** Citron vert pressé."],
  age=6, profil=["epice"], tech=["wok"])

K("gado_gado", "Gado-gado (légumes, œuf et sauce cacahuète)", "Gado-gado", f"{ID} › Java", "P", 1, 4, 30, 15, "€", "Casserole, mixeur.",
  "Légumes cuits et crus, pommes de terre, œuf dur, tofu et une sauce cacahuète épaisse au citron vert : complet, végétarien, festif.",
  [f"4|pommes de terre|{PDT}|2", "200 g|de haricots verts|Haricots verts|2", "200 g|de chou|Chou blanc / rouge|1", "100 g|de germes de soja|Germes de soja|1", f"4|œufs durs|{OEUF}|2", "200 g|de tofu|Tofu (ferme / soyeux)|2", "150 g|de beurre de cacahuète|Beurre de cacahuète|3", "1 c. à s.|de kecap manis|Kecap manis|1", f"1|citron vert|{CITV}|1", f"1|piment|{PIMENT}|1?"],
  ["**Cuire.** Pommes de terre 15 min, haricots 6 min, chou 2 min ; tofu en dés doré.", "**Sauce.** Beurre de cacahuète, kecap manis, citron vert, piment, eau chaude : épaisse et nappante.", "**Dresser.** Légumes en tas, œufs, tofu, germes crus ; sauce par-dessus."],
  age=3, cats=["vegetarien"], profil=["gras"])

K("satay_poulet", "Satay de poulet, sauce cacahuète", "Sate ayam", f"{ID} › Madura", "P", 1, 4, 25, 10, "€€", "Brochettes, gril ou poêle-gril.",
  "Petites brochettes de poulet marinées au curcuma et à la citronnelle, grillées, avec une sauce cacahuète : le snack des marchés de nuit.",
  [f"600 g|de cuisses de poulet désossées|{CUISSE}|3", f"1 c. à c.|de curcuma|{CURC}|1", "1 tige|de citronnelle|Citronnelle|1", f"2 c. à s.|de sauce soja|{SOJA}|1", f"1 c. à s.|de sucre|{SUCRE}|1", "4 c. à s.|de sauce satay|SUB:sauce_satay|2", "½|concombre|Concombre|1?"],
  ["**Mariner.** Poulet en petits cubes, curcuma, citronnelle hachée fin, soja, sucre, 30 min ; piqué sur brochettes trempées.", "**Griller.** 8-10 min en retournant : bords caramélisés, cuit à cœur.", "**Servir.** Sauce satay tiède, concombre."],
  age=3, cats=["enfants"], fetes=["Barbecue d'été", "Apéritif dînatoire"])

K("adobo_poulet", "Adobo de poulet (Philippines)", "Adobong manok", PH, "P", 1, 4, 15, 40, "€", "Cocotte.",
  "Le plat national philippin : poulet mijoté dans le vinaigre, la sauce soja, l'ail, le laurier et le poivre, puis réduit jusqu'à laquer.",
  [f"8|morceaux de poulet (cuisses, pilons)|{CUISSE}|3", "10 cl|de vinaigre (cidre ou riz)|Vinaigre de cidre|2", f"8 c. à s.|de sauce soja|{SOJA}|2", f"1 tête|d'ail|{AIL}|2", f"3 feuilles|de laurier|{LAURIER}|1", "1 c. à c.|de poivre en grains|Poivre noir / blanc / vert|1", f"1 c. à s.|de sucre|{SUCRE}|1"],
  ["**Mariner.** Poulet, vinaigre, soja, ail écrasé, laurier, poivre, 30 min (facultatif).", "**Mijoter.** Tout dans la cocotte avec 20 cl d'eau, 30 min sans remuer au début (le vinaigre s'adoucit).",
   "**Laquer.** Poulet sorti et doré à la poêle ; sauce réduite avec le sucre jusqu'à napper ; remets le poulet. Riz blanc."], age=3, profil=["acide"])

K("sinigang_crevettes", "Sinigang aux crevettes (soupe aigre au tamarin)", "Sinigang na hipon", PH, "So", 1, 4, 15, 20, "€€", "Faitout.",
  "Bouillon acidulé au tamarin, tomates, radis, haricots verts, épinards et crevettes : la soupe réconfortante des Philippines.",
  ["400 g|de crevettes crues|Crevettes (cuites/crues)|3", "2 c. à s.|de pâte de tamarin|Pâte de tamarin|2", f"2|tomates|{TOM}|1", f"1|oignon|{OIG}|1", "1|radis daikon (ou 6 radis)|Radis noir / daikon|1", "150 g|de haricots verts|Haricots verts|1", "100 g|d'épinards|Épinard|1", "2 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|2"],
  ["**Bouillon.** 1,5 l d'eau, oignon, tomates en quartiers, 10 min ; tamarin délayé, sauce de poisson : franchement acide.", "**Légumes.** Radis en rondelles 5 min, haricots 3 min.", "**Finir.** Crevettes 2 min (roses), épinards ; riz à part."],
  age=3, profil=["acide", "poisson", "leger"])

K("banh_xeo", "Bánh xèo (crêpes croustillantes vietnamiennes)", "Bánh xèo", f"{VN} › Sud", "P", 2, 4, 30, 20, "€€", "Poêle anti-adhésive 26 cm avec couvercle.",
  "Crêpe fine à la farine de riz, au curcuma et au lait de coco, croustillante, garnie de crevettes et de germes de soja, mangée dans une feuille de salade avec des herbes et du nuoc-cham.",
  ["200 g|de farine de riz|Farine de riz / riz gluant|3", "20 cl|de lait de coco|Lait de coco / crème de coco|2", f"1 c. à c.|de curcuma|{CURC}|1", "300 g|de crevettes|Crevettes (cuites/crues)|2", "200 g|de germes de soja|Germes de soja|2", "1|salade|Salade (laitue, batavia)|1", "1 bouquet|de menthe|Menthe|1", "8 c. à s.|de nuoc-cham|SUB:nuoc_cham|2", f"2|cébettes|Oignon nouveau / cébette|1"],
  ["**Pâte.** Farine de riz, curcuma, lait de coco, 30 cl d'eau, sel, cébette : fluide comme une pâte à crêpe ; 30 min de repos.",
   "**Cuire.** Poêle très chaude huilée : crevettes 1 min, louche de pâte en tournant (ça grésille), germes ; couvert 2 min, découvert 3 min : les bords décollent et croustillent ; plie en deux.",
   "**Manger.** Un morceau dans une feuille de salade avec la menthe, trempé dans le nuoc-cham."], age=6, fetes=["Apéritif dînatoire"])

K("ga_kho_gung", "Poulet caramélisé au gingembre (gà kho gừng)", "Gà kho gừng", VN, "P", 1, 4, 15, 30, "€", "Cocotte ou sauteuse.",
  "Morceaux de poulet mijotés dans un caramel salé à la sauce de poisson et au gingembre : sucré-salé, laqué, à manger sur du riz.",
  [f"800 g|de cuisses de poulet en morceaux|{CUISSE}|3", "1 morceau (6 cm)|de gingembre|Gingembre frais|2", f"3 c. à s.|de sucre|{SUCRE}|2", "3 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|2", f"1|échalote|{ECH}|1", f"1 c. à c.|de poivre|{POIVRE}|1", f"2|cébettes|Oignon nouveau / cébette|1"],
  ["**Caramel.** Sucre et 2 c. à s. d'eau, à sec, jusqu'à brun ambré (odeur de noisette) ; hors du feu, sauce de poisson (attention, ça crache).",
   "**Mijoter.** Poulet, gingembre en bâtonnets, échalote, 15 cl d'eau, couvert 20 min, puis découvert 10 min : la sauce réduit et laque.", "**Servir.** Poivre, cébette, riz."],
  age=3, tech=["caramel"])

K("lumpia_poulet", "Lumpia (rouleaux frits philippins au poulet)", "Lumpiang shanghai", PH, "E", 2, 24, 40, 15, "€", "Poêle profonde, thermomètre.",
  "Rouleaux fins comme des cigares, farcis de poulet haché, carotte et oignon, frits jusqu'à être très croustillants : avec une sauce aigre-douce.",
  [f"400 g|de poulet haché|{BLANC_P}|3", "24|feuilles de brick ou de riz|Pâte filo / feuilles de brick|3", f"1|carotte|{CAROTTE}|1", f"1|oignon|{OIG}|1", f"2 gousses|d'ail|{AIL}|1", f"1|œuf|{OEUF}|1", f"1 c. à s.|de sauce soja|{SOJA}|1", "1 l|d'huile de friture|Huile d'arachide|2", "1 bol|de sauce aigre-douce|SUB:sauce_aigre_douce|1?"],
  ["**Farce.** Poulet, carotte et oignon râpés fin, ail, œuf, soja, poivre.", "**Rouler.** Un boudin fin de farce sur une feuille, roulé serré, bords collés à l'eau.",
   "**Frire.** 170 °C, 5-6 min : doré et cuit à cœur ; égoutté sur papier. Sauce à part."], age=3, cats=["enfants"], fetes=["Anniversaire", "Apéritif dînatoire"], tech=["frire en sécurité"])

# ——— Afrique de l'Est ———
K("pilau_epices", "Pilau aux épices (riz de la côte swahilie)", "Pilau", f"{TZ} › Zanzibar", "P", 1, 6, 20, 30, "€€", "Cocotte avec couvercle.",
  "Riz cuit avec bœuf (ou poulet), oignons dorés et le mélange pilau (cumin, cardamome, cannelle, clou, poivre) : le plat des fêtes de Zanzibar à Nairobi.",
  [f"400 g|de riz basmati|{RIZ}|3", "500 g|de bœuf en cubes (ou poulet)|Paleron|3", f"2|oignons|{OIG}|2", f"3 gousses|d'ail|{AIL}|1", "1 morceau|de gingembre|Gingembre frais|1", f"1 c. à c.|de cumin|{CUMIN}|1", "4|gousses de cardamome|Cardamome|1", f"1|bâton de cannelle|{CANN}|1", "4|clous de girofle|Clou de girofle|1", f"2|tomates|{TOM}|1?"],
  ["**Viande.** Mijotée 40 min dans 80 cl d'eau salée avec l'ail et le gingembre ; garde le bouillon.", "**Oignons.** Dorés 10 min (bien bruns : ils donnent la couleur) ; épices 1 min ; viande ; riz rincé 2 min.",
   "**Cuire.** 70 cl de bouillon, couvert, feu très doux 15 min ; 10 min de repos. Avec un kachumbari (tomate-oignon-piment)."],
  age=3, fetes=["Ramadan / Aïd", "Repas de famille"], profil=["epice"])

K("sukuma_wiki", "Sukuma wiki (chou kale sauté à la tomate)", "Sukuma wiki", KE, "A", 1, 4, 10, 10, "€", "Sauteuse.",
  "« Ce qui fait tenir la semaine » en swahili : chou kale émincé sauté avec oignon et tomate, le légume de tous les repas kenyans, avec l'ugali.",
  ["1 botte|de chou kale (ou chou vert)|Chou vert / frisé / kale|3", f"1|oignon|{OIG}|2", f"2|tomates|{TOM}|2", f"1 pincée|de piment|{CAYENNE}|1?", f"2 c. à s.|d'huile|{HN}|1"],
  ["**Émincer.** Le kale en lanières très fines (roulé puis coupé).", "**Sauter.** Oignon 4 min, tomates 3 min : une petite sauce ; kale, sel, 5 min : tendre mais encore vert.", "**Servir.** Avec ugali, riz ou chapati."],
  age=1, cats=["vegetarien", "enfants"], profil=["leger"])

K("ugali", "Ugali (pâte ferme de maïs)", "Ugali", KE, "A", 1, 4, 5, 10, "€", "Casserole à fond épais, spatule solide.",
  "Farine de maïs blanc cuite dans l'eau jusqu'à former une pâte ferme qu'on mange avec les doigts en saucant ragoûts et légumes : le pain de l'Afrique de l'Est.",
  ["250 g|de farine de maïs (blanche si possible)|Farine de maïs|3", "60 cl|d'eau|-|3", f"1 pincée|de sel|{SEL}|1"],
  ["**Cuire.** Eau salée à ébullition ; farine en pluie en remuant ; ça épaissit vite.", "**Travailler.** Feu doux, 6-8 min en écrasant et retournant contre la paroi à la spatule : la pâte se détache des bords et forme une boule.",
   "**Servir.** Démoulée en dôme ; on en prend un morceau, on y creuse un creux du pouce pour saucer."], age=1, cats=["vegetarien"])

K("nyama_choma", "Nyama choma (viande grillée kényane, kachumbari)", "Nyama choma", KE, "P", 1, 6, 20, 30, "€€", "Barbecue ou gril du four.",
  "La grillade du week-end au Kenya : agneau (ou chèvre, bœuf) mariné au citron et à l'ail, grillé lentement, servi avec kachumbari (salade tomate-oignon-piment).",
  ["1,2 kg|d'épaule ou de côtelettes d'agneau|Épaule d'agneau|3", f"2|citrons|{CIT}|2", f"4 gousses|d'ail|{AIL}|1", f"3|tomates|{TOM}|2", "1|oignon rouge|Oignon rouge|1", f"1|piment|{PIMENT}|1", f"½ bouquet|de coriandre|{CORI}|1"],
  ["**Mariner.** Viande en morceaux, citron, ail, sel, 1 h.", "**Griller.** Braise moyenne (ou gril du four), 25-30 min en retournant : croûte dorée, cœur juteux.",
   "**Kachumbari.** Tomates et oignon en petits dés, piment, coriandre, citron, sel ; avec l'ugali."], age=3, fetes=["Barbecue d'été"])

K("mandazi", "Mandazi (beignets swahilis à la cardamome)", "Mandazi", f"{TZ} › Côte swahilie", "G", 1, 20, 25, 45, "€", "Casserole profonde, thermomètre.",
  "Beignets triangulaires au lait de coco et à la cardamome, légers et dorés : le petit-déjeuner et le goûter de toute la côte est-africaine, avec un chai.",
  [f"400 g|de farine|{F55}|3", "20 cl|de lait de coco|Lait de coco / crème de coco|2", f"60 g|de sucre|{SUCRE}|1", f"1 c. à c.|de levure boulangère|{LEV}|2", "½ c. à c.|de cardamome moulue|Cardamome|1", f"1|œuf|{OEUF}|1", "1 l|d'huile de friture|Huile d'arachide|2"],
  ["**Pâte.** Tout mélangé, pétri 5 min : souple ; 45 min au chaud : elle gonfle.", "**Couper.** Étalée sur 1 cm, disques coupés en quatre triangles.", "**Frire.** 170 °C, 2 min par face : gonflés et dorés ; égouttés."],
  age=1, cats=["enfants", "brunch"], fetes=["Ramadan / Aïd"], profil=["sucre"], tech=["frire en sécurité"])

K("shiro_wat", "Shiro (crème de pois chiche éthiopienne au berbéré)", "Shiro wat", ET, "P", 1, 4, 10, 20, "€", "Casserole.",
  "Farine de pois chiche cuite en crème épaisse avec oignon, ail, tomate et berbéré : le plat des jours de jeûne en Éthiopie, végétalien, à saucer avec l'injera ou du pain.",
  ["100 g|de farine de pois chiche|Farine de pois chiche (besan)|3", f"2|oignons|{OIG}|2", f"3 gousses|d'ail|{AIL}|1", f"1|tomate|{TOM}|1", "1 c. à s.|de berbéré|Berbéré|2", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Base.** Oignons hachés très fin, cuits à sec 5 min puis avec l'huile 5 min ; ail, tomate, berbéré 2 min.", "**Épaissir.** 60 cl d'eau ; farine en pluie en fouettant.", "**Cuire.** 10-15 min à feu doux en remuant : crème lisse et épaisse ; sel."],
  age=3, cats=["vegetarien"], profil=["epice"])

K("injera", "Injera (galette fermentée de teff)", "Injera", ET, "Pa", 3, 10, 30, 2880, "€€", "Grande poêle anti-adhésive avec couvercle, bocal.",
  "La grande crêpe spongieuse et acidulée qui sert d'assiette et de couvert en Éthiopie : farine de teff fermentée deux à trois jours.",
  ["300 g|de farine de teff|Teff|3", "60 cl|d'eau|-|3", f"1 pincée|de levure boulangère|{LEV}|1", f"1 pincée|de sel|{SEL}|1"],
  ["**Fermenter.** Teff, eau, levure : pâte fluide, couverte d'un torchon, 2 à 3 jours à température ambiante : elle sent aigre et fait des bulles.",
   "**Cuire.** Sel ; une louche en spirale dans la poêle chaude sans matière grasse ; dès que des trous apparaissent partout, couvercle 1 min : sans retourner.",
   "**Servir.** Les plats (shiro, misir wot, doro wat) posés directement dessus."], age=1, cats=["pains"], keep="2 jours, emballée.")

# ——— Amérique latine ———
K("arroz_con_pollo", "Arroz con pollo (riz au poulet latino)", "Arroz con pollo", "Amérique latine › Pérou", "P", 1, 6, 25, 35, "€€", "Cocotte.",
  "Le riz au poulet de toute l'Amérique latine : poulet doré, riz cuit dans un bouillon vert à la coriandre (Pérou), petits pois, poivron et maïs.",
  [f"6|cuisses de poulet|{CUISSE}|3", f"400 g|de riz|{RIZ}|3", "1 bouquet|de coriandre|Coriandre fraîche|2", f"1|poivron|{POIVRON}|1", "150 g|de petits pois|Petits pois / pois gourmands|1", "100 g|de maïs|Maïs doux|1", f"1|oignon|{OIG}|1", f"3 gousses|d'ail|{AIL}|1", "80 cl|de bouillon de volaille|Bouillon cube volaille|2"],
  ["**Dorer.** Poulet 8 min, réservé ; oignon, ail, poivron 5 min.", "**Bouillon vert.** Coriandre mixée avec 20 cl de bouillon ; versée avec le reste du bouillon et le riz.",
   "**Cuire.** Poulet par-dessus, couvert 20 min à feu doux ; petits pois et maïs 5 min ; repos 5 min."], age=1, cats=["enfants"], fetes=["Repas de famille"])

K("gallo_pinto", "Gallo pinto (riz aux haricots noirs)", "Gallo pinto", "Amérique latine › Costa Rica", "P", 1, 4, 15, 10, "€", "Sauteuse.",
  "Riz et haricots noirs sautés avec oignon, poivron, coriandre et un peu de sauce Worcestershire : le petit-déjeuner national du Costa Rica, avec un œuf.",
  [f"400 g|de riz cuit (de la veille)|{RIZ}|3", "400 g|de haricots noirs|Haricots rouges / noirs|3", f"1|oignon|{OIG}|1", f"1|poivron rouge|{POIVRON}|1", f"½ bouquet|de coriandre|{CORI}|1", "1 c. à s.|de sauce Worcestershire|Sauce Worcestershire|1?", f"4|œufs (facultatif)|{OEUF}|1?"],
  ["**Base.** Oignon et poivron 5 min.", "**Sauter.** Haricots avec un peu de leur jus 3 min ; riz, sauce, 5 min : le riz prend la couleur des haricots.", "**Servir.** Coriandre ; œuf au plat, avocat, plantain."],
  age=1, cats=["vegetarien", "brunch", "zero_dechet"])

K("ropa_vieja", "Ropa vieja (bœuf effiloché cubain)", "Ropa vieja", "Amérique latine › Cuba", "P", 1, 6, 25, 150, "€€", "Cocotte.",
  "« Vieux vêtements » : bœuf mijoté longtemps puis effiloché dans une sauce tomate aux poivrons, oignon, cumin et olives. Avec riz, haricots noirs et plantain.",
  ["1,2 kg|de paleron ou bavette|Paleron|3", f"2|poivrons|{POIVRON}|2", f"2|oignons|{OIG}|2", f"400 g|de tomates pelées|{PELEES}|2", f"4 gousses|d'ail|{AIL}|1", f"1 c. à c.|de cumin|{CUMIN}|1", "80 g|d'olives vertes|Olives (vertes / noires)|1", f"2|feuilles de laurier|{LAURIER}|1"],
  ["**Mijoter.** Bœuf dans l'eau salée avec laurier, 2 h : il se défait à la fourchette ; effiloché.", "**Sauce.** Oignons et poivrons en lanières 8 min, ail, cumin, tomates, 20 cl du bouillon ; 10 min.",
   "**Finir.** Bœuf et olives, 15 min : la viande boit la sauce."], age=3, fetes=["Repas de famille"])
