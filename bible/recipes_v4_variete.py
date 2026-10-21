# -*- coding: utf-8 -*-
"""Vague 5 · Audit gourmet (21/10/2026), recommandations 4, 7 et 9 : les accompagnements de base (reliés aux plats et ajoutés
aux courses), les poissons du quotidien, les légumes d'hiver en plat, les desserts d'hiver, la vraie paella valenciana et le
plateau de fromages des repas de fête. Écrites au niveau étalon (une durée et un repère par étape). NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

VR = ("Sans alcool", ["alcohol"], {"Vin rouge": [("Jus de pomme / raisin / orange (pur jus)", 0.9), ("Vinaigre de vin rouge / blanc", 0.03)]},
      "Vin rouge → **jus de raisin rouge + 1 c. à s. de vinaigre de vin** : la couleur et le fruit. **À tester**.")
EVENING = "Le jour même ; les restes 2 jours au frigo."

# ———————————————————————————————— Accompagnements de base
K("riz_nature", "Riz blanc parfait (par absorption)", "Riz nature", "Asie de l'Est", "A", 1, 4, 5, 20, "€", "Casserole avec couvercle.",
  "Le riz qui accompagne la moitié des plats du monde, grain détaché, jamais collant : la méthode par absorption, sans égoutter.",
  [f"300 g|de riz long (basmati ou thaï)|{RIZ}|3", "45 cl|d'eau (1,5 fois le volume du riz)|-|2", f"1 pincée|de sel|{SEL}|1", f"10 g|de beurre (facultatif)|{BEURRE}|0?"],
  ["**Rincer.** Riz dans une passoire sous l'eau froide, en frottant, jusqu'à ce que l'eau soit claire (1 min) : c'est l'amidon qui fait coller.",
   "**Cuire.** Riz, eau froide et sel portés à ébullition à découvert ; dès que ça bout, couvercle et feu au plus bas, 12 min sans soulever : l'eau a disparu, de petits trous se forment en surface.",
   "**Reposer.** Hors du feu, 5 min toujours couvert : la vapeur finit la cuisson.",
   "**Égrener.** À la fourchette, une noisette de beurre si tu veux."],
  tips=["Riz complet : 2 fois son volume d'eau et 35 min.", "Refroidis vite les restes et garde-les 24 h au plus : riz sauté le lendemain."],
  keep="24 h au frigo, refroidi en moins d'1 h.", age=1, cats=["enfants"], tech=["Cuire le riz"])

K("semoule_nature", "Semoule de couscous moelleuse", "Semoule nature", "Maghreb › Algérie", "A", 1, 4, 5, 10, "€", "Saladier, film ou assiette.",
  "La semoule moyenne gonflée hors du feu, beurrée et égrenée : 10 minutes pour accompagner tajines, ragoûts et merguez.",
  ["300 g|de semoule moyenne|Semoule de couscous|3", "30 cl|d'eau ou de bouillon bouillant|-|2", f"20 g|de beurre (ou 2 c. à s. d'huile d'olive)|{BEURRE}|2", f"1 pincée|de sel|{SEL}|1"],
  ["**Mouiller.** Semoule, sel et un filet d'huile frottés entre les mains ; liquide bouillant versé d'un coup à hauteur.",
   "**Gonfler.** Couvert, 5 min : le liquide est absorbé.",
   "**Égrener.** Beurre en dés, égrenée à la fourchette puis entre les paumes : chaque grain se sépare. Goûte, sale."],
  tips=["Pour un couscous de fête, la semoule passe à la vapeur : voir le couscous royal."], keep="3 jours au frigo ; 2 min au micro-ondes avec une cuillère d'eau.", age=1, cats=["enfants"])

K("pates_nature", "Pâtes au beurre et parmesan (cuisson juste)", "Pâtes nature", "Europe du Sud › Italie", "A", 1, 4, 5, 12, "€", "Grande casserole.",
  "Des pâtes fraîches ou sèches cuites dans beaucoup d'eau bien salée, liées d'un peu d'eau de cuisson, de beurre et de parmesan : l'accompagnement des daubes, lapins et ragoûts.",
  [f"400 g|de tagliatelles ou de pâtes courtes|{PATES}|3", f"30 g|de beurre|{BEURRE}|2", f"40 g|de parmesan|{PARM}|1", f"1 c. à s.|de gros sel pour 4 l d'eau|{SEL}|1"],
  ["**Eau.** 4 l d'eau à gros bouillon, puis le sel : elle doit avoir le goût d'une soupe bien assaisonnée.",
   "**Cuire.** Pâtes, remuées la première minute (elles ne collent pas) ; 1 min de moins que le paquet : tendres avec un cœur à peine ferme. Garde une tasse d'eau.",
   "**Lier.** Égouttées sans rincer, beurre, parmesan et 3 c. à s. d'eau de cuisson, remuées 30 s : brillantes."],
  tips=["Ne rince jamais les pâtes chaudes : l'amidon fait tenir la sauce."], keep="Le jour même.", age=1, cats=["enfants"], tech=["Pâtes"])

K("pommes_vapeur", "Pommes de terre vapeur au persil", "Pommes vapeur", "France", "A", 1, 4, 10, 25, "€", "Cuit-vapeur ou casserole avec panier.",
  "Des pommes de terre à chair ferme cuites à la vapeur, tendres et entières, roulées dans le beurre et le persil : l'accompagnement des poissons et des plats en sauce.",
  [f"800 g|de pommes de terre à chair ferme (charlotte, roseval)|{PDT}|3", f"20 g|de beurre|{BEURRE}|1", f"1 c. à s.|de persil haché|{PERSIL}|1", f"1 pincée|de fleur de sel|{SEL}|1"],
  ["**Préparer.** Épluchées (ou brossées si nouvelles), coupées en morceaux égaux de la taille d'un œuf (elles cuisent en même temps).",
   "**Cuire.** Panier au-dessus de l'eau frémissante, couvert, 20-25 min : la pointe du couteau entre sans résistance.",
   "**Finir.** Beurre fondu, persil, fleur de sel."],
  keep="2 jours au frigo ; en salade ou sautées le lendemain.", age=1, cats=["enfants", "vegetarien"])

# ———————————————————————————————— Poissons du quotidien
K("maquereaux_four_moutarde", "Maquereaux au four, moutarde et citron", "Maquereaux au four", "France › Bretagne", "P", 1, 4, 15, 15, "€", "Plat à four.",
  "Le maquereau, poisson gras bon marché et plein d'oméga-3, en filets badigeonnés de moutarde à l'ancienne, rôtis 12 minutes : la moutarde et le citron équilibrent sa richesse.",
  ["8|filets de maquereau|Maquereau|3", f"2 c. à s.|de moutarde à l'ancienne|{DIJON}|2", f"1|citron|{CIT}|2", f"1|oignon rouge|Oignon rouge|1", f"2 c. à s.|d'huile d'olive|{HO}|1", f"1 c. à s.|de persil|{PERSIL}|1", f"1 pincée|de sel|{SEL}|1"],
  ["**Préparer.** Filets passés du bout des doigts pour sentir les arêtes, retirées à la pince ; salés, posés peau dessous sur l'oignon émincé huilé.",
   "**Badigeonner.** Moutarde étalée sur la chair, rondelles de citron.",
   "**Cuire.** 12 min à 200 °C : la chair devient opaque et se détache en feuillets.",
   "**Servir.** Persil, jus de citron, pommes vapeur ou salade de lentilles."],
  tips=["Demande au poissonnier de lever les filets.", "Les restes émiettés font des rillettes avec du fromage frais."],
  keep="2 jours au frigo.", age=3, cats=["express"], profil=["poisson"], side="pommes_vapeur")

K("sardines_poelees_persillade", "Sardines poêlées en persillade", "Sardines persillade", "France › Provence-Alpes-Côte d'Azur", "P", 1, 4, 15, 8, "€", "Grande poêle.",
  "Des sardines fraîches ouvertes en portefeuille, saisies côté peau puis arrosées d'une persillade à l'ail et au citron : cinq minutes de cuisson, un goût de vacances.",
  ["16|sardines fraîches en filets (ou en portefeuille)|Sardine (fraîche / conserve)|3", f"2 gousses|d'ail|{AIL}|1", f"1 bouquet|de persil|{PERSIL}|2", f"1|citron|{CIT}|2", f"3 c. à s.|d'huile d'olive|{HO}|1", f"2 c. à s.|de farine|{F55}|1", f"1 pincée|de sel|{SEL}|1"],
  ["**Préparer.** Filets séchés, salés, farinés côté peau seulement (elle croustille sans coller).",
   "**Saisir.** Poêle très chaude, huile, côté peau 2 min sans bouger : peau dorée qui se décolle seule ; 30 s côté chair.",
   "**Persillade.** Hors du feu, ail et persil hachés dans la poêle chaude, 20 s (l'ail ne doit pas brunir), jus de citron, versée sur les sardines."],
  tips=["Sardines entières : le poissonnier les vide, ou on les grille au barbecue 3 min par face."], keep="Le jour même.", age=3, cats=["express"], profil=["poisson"], side="achat:Baguette tradition")

K("lieu_croute_herbes", "Lieu noir en croûte d'herbes et de chapelure", "Lieu en croûte", "France", "P", 1, 4, 15, 15, "€", "Plat à four.",
  "Des pavés de lieu noir, poisson blanc abordable, sous une croûte croustillante de chapelure, parmesan et herbes : les enfants l'adorent, il ne sèche pas.",
  ["4|pavés de lieu noir (ou merlu)|Colin, lieu noir, merlu|3", "60 g|de chapelure ou de pain rassis mixé|Chapelure|2", f"30 g|de parmesan|{PARM}|1", f"1 bouquet|de persil et ciboulette|{PERSIL}|2", f"40 g|de beurre fondu|{BEURRE}|2", f"1|citron (zeste)|{CIT}|1", f"1 c. à c.|de moutarde|{DIJON}|1", f"1 pincée|de sel|{SEL}|1"],
  ["**Croûte.** Chapelure, parmesan, herbes hachées, zeste, beurre fondu : un sable humide qui se tient pressé.",
   "**Monter.** Pavés salés dans le plat beurré, fine couche de moutarde (la croûte colle), croûte tassée sur 5 mm.",
   "**Cuire.** 15 min à 200 °C : croûte dorée, chair opaque qui se détache en lamelles.",
   "**Servir.** Quartiers de citron ; riz, purée ou légumes rôtis."],
  tips=["Pain rassis mixé à la place de la chapelure : anti-gaspi et meilleur."], keep="2 jours au frigo.", age=1, cats=["enfants", "zero_dechet"], profil=["poisson"], side="riz_nature")

K("papillotes_poisson_legumes", "Papillotes de poisson aux petits légumes", "Papillotes", "France", "P", 1, 4, 20, 15, "€€", "Papier sulfurisé, plaque.",
  "Le poisson blanc cuit à l'étuvée dans son papier avec des julienne de légumes, citron et herbes : rien ne sèche, tout garde son goût, et chacun ouvre sa papillote.",
  ["4|filets de cabillaud ou de lieu|Cabillaud / morue fraîche|3", f"2|carottes|{CAROTTE}|2", "1|courgette|Courgette|2", "1|poireau (le blanc)|Poireau|1", f"1|citron|{CIT}|1", f"20 g|de beurre|{BEURRE}|1", "1 c. à s.|d'aneth ou de ciboulette|Aneth|1", f"1 pincée|de sel|{SEL}|1"],
  ["**Légumes.** En fins bâtonnets (julienne) : ils cuisent en même temps que le poisson.",
   "**Monter.** Feuille de papier de 30 cm : lit de légumes salés, filet salé, rondelle de citron, noisette de beurre, herbes ; bords repliés serrés en demi-lune.",
   "**Cuire.** 15 min à 200 °C : la papillote gonfle.",
   "**Servir.** Ouverte à table (attention à la vapeur) : chair nacrée, qui s'effeuille."],
  tips=["Poisson surgelé : décongelé au frigo, bien séché, 3 min de plus."], keep=EVENING, age=1, cats=["enfants"], profil=["poisson", "leger"], side="riz_nature")

K("merlu_beurre_blanc_poireaux", "Merlu poché, fondue de poireaux", "Merlu aux poireaux", "France › Pays de la Loire", "P", 2, 4, 25, 20, "€€", "Sauteuse, casserole large.",
  "Le merlu, poisson tendre et fin, poché à frémissement dans un court-bouillon, servi sur une fondue de poireaux à la crème citronnée : doux et soyeux.",
  ["4|pavés de merlu|Colin, lieu noir, merlu|3", "4|poireaux|Poireau|3", f"20 cl|de crème|{CF}|2", f"30 g|de beurre|{BEURRE}|2", f"1|citron|{CIT}|1", f"1|bouquet garni + 1 oignon|{LAURIER}|1", f"1 pincée|de sel|{SEL}|1"],
  ["**Fondue.** Poireaux émincés et lavés, beurre, sel, couvert, 15 min à feu doux : fondants, sans couleur ; crème et jus de citron, 3 min.",
   "**Court-bouillon.** 1 l d'eau salée, oignon, bouquet garni, 10 min de frémissement.",
   "**Pocher.** Merlu, frémissement à peine visible, 6-8 min : opaque à cœur, il se détache en lamelles. Jamais d'ébullition (il se défait).",
   "**Servir.** Merlu égoutté sur la fondue, poivre, un trait de citron."],
  keep=EVENING, age=1, cats=["enfants"], profil=["poisson"], side="pommes_vapeur")

# ———————————————————————————————— Légumes d'hiver en plat
K("potimarron_farci_quinoa", "Potimarron rôti farci au quinoa, feta et noix", "Potimarron farci", "France", "P", 1, 4, 25, 50, "€", "Plaque, four.",
  "Des demi-potimarrons rôtis (la peau se mange), remplis de quinoa aux herbes, feta, noix et canneberges : un plat végétarien de fête d'automne.",
  ["2|potimarrons moyens|Potimarron|3", "150 g|de quinoa|Quinoa|3", "150 g|de feta|Feta|2", "50 g|de noix|Noix|1", "30 g|de raisins secs ou canneberges|Raisins secs|1", f"1 bouquet|de persil|{PERSIL}|1", f"3 c. à s.|d'huile d'olive|{HO}|1", f"1 c. à c.|de cumin|{CUMIN}|1", f"1 pincée|de sel|{SEL}|1"],
  ["**Rôtir.** Potimarrons coupés en deux, graines retirées (gardées : grillées, elles se grignotent) ; huile, sel, cumin ; face coupée en dessous, 35 min à 200 °C : la pointe du couteau entre comme dans du beurre.",
   "**Quinoa.** Rincé, cuit 12 min dans 2 fois son volume d'eau salée, égoutté.",
   "**Farce.** Quinoa, feta émiettée, noix concassées, raisins, persil, huile.",
   "**Gratiner.** Farce tassée dans les demi-potimarrons, 10 min au four : la feta dore."],
  tips=["Les graines rincées, séchées, huilées et salées, 10 min au four : un apéritif."], keep="2 jours au frigo.", age=1, cats=["vegetarien", "zero_dechet"], fetes=["Halloween"])

K("gratin_celeri_noix", "Gratin de céleri-rave et pommes de terre aux noix", "Gratin de céleri", "France", "P", 1, 6, 25, 60, "€", "Plat à gratin, mandoline (ou couteau).",
  "Le céleri-rave, doux et parfumé, en fines tranches avec des pommes de terre, cuit dans le lait et la crème à l'ail, couvert de comté et de noix : le gratin d'hiver qui change du dauphinois.",
  ["1|céleri-rave (800 g)|Céleri-rave|3", f"600 g|de pommes de terre|{PDT}|2", f"50 cl|de lait|{LAIT}|2", f"20 cl|de crème|{CF}|2", f"100 g|de comté râpé|{GRUY}|2", "50 g|de noix|Noix|1", f"1 gousse|d'ail|{AIL}|1", f"1 pincée|de muscade|Noix de muscade|0", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Trancher.** Céleri et pommes de terre épluchés, en tranches de 3 mm (mandoline).",
   "**Précuire.** Lait, crème, ail écrasé, sel, muscade portés à frémissement ; tranches dedans 10 min : le liquide épaissit (l'amidon), les tranches s'assouplissent.",
   "**Monter.** Plat frotté d'ail, tranches et leur crème, comté, noix concassées.",
   "**Cuire.** 45 min à 180 °C : doré, la lame entre sans résistance. 10 min de repos."],
  keep="3 jours au frigo.", age=1, cats=["vegetarien", "enfants"])

K("poelee_panais_pois_chiches", "Poêlée de panais, carottes et pois chiches rôtis au miel et cumin", "Légumes racines rôtis", "France", "P", 1, 4, 15, 35, "€", "Plaque, four.",
  "Panais, carottes et oignons rouges rôtis jusqu'à caraméliser avec des pois chiches croustillants, miel, cumin, et une sauce yaourt-citron : un plat complet et végétarien avec les légumes d'hiver.",
  ["4|panais|Panais / rutabaga|3", f"4|carottes|{CAROTTE}|2", "2|oignons rouges|Oignon rouge|1", f"400 g|de pois chiches cuits|{POIS}|2", f"1 c. à s.|de miel|{MIEL}|1", f"1 c. à c.|de cumin|{CUMIN}|1", f"4 c. à s.|d'huile d'olive|{HO}|2", f"150 g|de yaourt grec + ½ citron|{GREC}|2", f"1 pincée|de sel|{SEL}|1"],
  ["**Couper.** Panais et carottes en bâtonnets égaux, oignons en quartiers ; pois chiches égouttés et séchés (sinon ils ne croustillent pas).",
   "**Rôtir.** Huile, cumin, sel ; plaque en une seule couche (entassés, ils cuisent à la vapeur), 25 min à 210 °C.",
   "**Laquer.** Miel en filet, 10 min : bords caramélisés, pois chiches croustillants.",
   "**Sauce.** Yaourt, jus de citron, sel ; sur les légumes au service."],
  keep="3 jours au frigo.", age=1, cats=["vegetarien", "enfants"], side="semoule_nature")

K("veloute_topinambour", "Velouté de topinambours, noisettes grillées", "Velouté de topinambours", "France", "So", 1, 4, 20, 30, "€", "Faitout, mixeur.",
  "Le topinambour a un goût d'artichaut et de noisette : en velouté avec un peu de pomme de terre et de crème, c'est une soupe d'hiver délicate.",
  ["600 g|de topinambours|Topinambour|3", f"1|pomme de terre|{PDT}|1", f"1|oignon|{OIG}|1", f"80 cl|de bouillon de légumes|{BOUILLON}|2", f"10 cl|de crème|{CF}|1", "30 g|de noisettes|Noisette|1?", f"20 g|de beurre|{BEURRE}|1", f"1 pincée|de sel|{SEL}|1"],
  ["**Éplucher.** Topinambours brossés et pelés à l'économe, en morceaux, dans l'eau citronnée (ils noircissent à l'air).",
   "**Suer.** Oignon au beurre 5 min sans colorer ; topinambours et pomme de terre, 3 min.",
   "**Cuire.** Bouillon, 25 min : tendres.",
   "**Mixer.** Avec la crème, 2 min : très lisse. Goûte, sale. Noisettes grillées à sec 3 min, concassées dessus."],
  tips=["Le topinambour peut être indigeste pour certains : une pomme de terre dans la soupe et une cuisson complète aident."], keep="3 jours au frigo ; se congèle.", age=1, cats=["vegetarien", "enfants"])

K("chou_braise_saucisses", "Chou vert braisé aux saucisses de volaille", "Chou braisé", "France › Auvergne-Rhône-Alpes", "P", 1, 4, 20, 50, "€", "Cocotte.",
  "Un chou vert blanchi puis braisé doucement avec carottes et saucisses, jusqu'à devenir fondant et doux : le plat d'hiver économique des fermes, ici avec des saucisses de volaille.",
  ["1|chou vert frisé|Chou vert / frisé / kale|3", "4|saucisses de volaille (ou de bœuf)|Saucisse de bœuf / de veau / de volaille|3", f"3|carottes|{CAROTTE}|2", f"1|oignon|{OIG}|1", f"30 cl|de bouillon|{BOUILLON}|2", f"20 g|de beurre|{BEURRE}|1", f"1|bouquet garni|{LAURIER}|1", f"1 pincée|de sel|{SEL}|1"],
  ["**Blanchir.** Chou en 8 quartiers, 5 min dans l'eau bouillante salée (il perd son amertume), égoutté.",
   "**Saucisses.** Dorées 5 min au beurre ; oignon et carottes en rondelles 5 min.",
   "**Braiser.** Chou, bouquet, bouillon ; couvert, 40 min à feu doux : le chou est fondant et a bu le bouillon. Goûte, poivre."],
  keep="3 jours au frigo.", age=1, cats=["enfants"], side="pommes_vapeur")

# ———————————————————————————————— Desserts d'hiver
K("poires_pochees_vin_epices", "Poires pochées au vin et aux épices", "Poires au vin", "France › Bourgogne-Franche-Comté", "D", 1, 6, 20, 40, "€", "Casserole juste à la taille des poires.",
  "Des poires entières pochées dans un vin rouge sucré à la cannelle, à l'orange et au poivre, jusqu'à devenir rubis et fondantes ; le sirop réduit les nappe.",
  ["6|poires fermes (conférence, williams)|Poire|3", "75 cl|de vin rouge fruité|Vin rouge|3", f"150 g|de sucre|{SUCRE}|2", "1|orange (zeste en bandes)|Orange|1", f"1|bâton de cannelle + 2 clous de girofle + 4 grains de poivre|{CANN}|1", "1|gousse de vanille|Vanille (gousse)|1?"],
  ["**Sirop.** Vin, sucre, zeste, épices, vanille fendue : 5 min à frémissement, le sucre a fondu.",
   "**Pocher.** Poires épluchées en gardant la queue, debout dans le sirop (couvertes, sinon arrosées), 25-35 min à frémissement : la lame entre sans résistance.",
   "**Infuser.** Hors du feu, une nuit si possible : elles deviennent rubis jusqu'au cœur.",
   "**Napper.** Sirop réduit 10 min à gros bouillon : sirupeux, il nappe la cuillère."],
  var=[VR], keep="4 jours au frigo dans leur sirop.", age=None, kids="✓ dès 3 ans en version sans alcool.", profil=["sucre"], fetes=["Noël", "Repas de famille"])

K("tarte_bourdaloue", "Tarte Bourdaloue (poires et crème d'amande)", "Tarte Bourdaloue", "France › Île-de-France › Paris", "D", 2, 8, 30, 50, "€€", "Moule à tarte 24 cm, four.",
  "Des demi-poires pochées en éventail sur une crème d'amande moelleuse, dans une pâte sucrée : la tarte de pâtisserie parisienne la plus réconfortante de l'hiver.",
  ["1|pâte sucrée (recette liée)|SUB:pate_sucree|3", "6|demi-poires pochées (ou au sirop)|Poire|3", f"100 g|de beurre mou|{BEURRE}|2", f"100 g|de sucre|{SUCRE}|2", "100 g|de poudre d'amande|Farine d'amande / poudre d'amande|2", f"2|œufs|{OEUF}|2", "30 g|d'amandes effilées|Amande (entière, effilée, poudre)|1", f"2 c. à s.|de confiture d'abricot (nappage)|Confiture / gelée|1?"],
  ["**Fond.** Pâte foncée, 30 min au frais.",
   "**Crème d'amande.** Beurre mou et sucre fouettés 2 min, poudre d'amande, œufs un à un : crème lisse et légère.",
   "**Garnir.** Crème étalée sur la pâte crue ; demi-poires bien égouttées, tranchées finement et poussées en éventail ; amandes effilées.",
   "**Cuire.** 40-45 min à 170 °C : la crème d'amande gonfle autour des poires et dore.",
   "**Napper.** Tiède, confiture d'abricot chauffée au pinceau : brillante."],
  keep="3 jours au frais.", age=1, profil=["sucre"], fetes=["Repas de famille"], tech=["Pâte sucrée"])

K("coings_rotis_miel", "Coings rôtis au miel et à la vanille", "Coings rôtis", "France", "D", 1, 4, 15, 75, "€", "Plat à four.",
  "Le coing, immangeable cru, devient rose, parfumé et fondant après une longue cuisson au four avec miel, beurre et vanille : un dessert d'automne oublié.",
  ["2|gros coings|Coing|3", f"4 c. à s.|de miel|{MIEL}|2", f"40 g|de beurre|{BEURRE}|2", "1|gousse de vanille|Vanille (gousse)|1", f"1|orange (jus)|Orange|1", f"20 cl|de crème ou de yaourt grec|{GREC}|1?"],
  ["**Préparer.** Coings frottés (leur duvet), coupés en quartiers, cœur dur retiré (couteau solide : c'est très ferme). On garde la peau.",
   "**Rôtir.** Plat beurré, quartiers, miel, jus d'orange, vanille fendue, 10 cl d'eau ; couvert d'aluminium, 45 min à 170 °C : les quartiers s'attendrissent et rosissent.",
   "**Caraméliser.** Découvert, 20-30 min en arrosant : chair rosée, translucide, sirop épais.",
   "**Servir.** Tièdes, avec crème ou yaourt."],
  tips=["Les pelures et les cœurs, cuits 30 min dans l'eau, donnent une gelée naturelle."], keep="4 jours au frigo.", age=1, cats=["enfants", "zero_dechet"], profil=["sucre"])

K("mont_blanc_verrines", "Mont-blanc en verrines (marrons et chantilly)", "Mont-blanc", "France › Auvergne-Rhône-Alpes", "D", 1, 6, 20, 30, "€€", "Batteur, poche à douille fine (ou presse-purée), verrines.",
  "Une meringue croquante, une chantilly peu sucrée et des vermicelles de crème de marrons : le dessert de salon de thé, en verrines sans cuisson ni difficulté.",
  ["500 g|de crème de marrons vanillée|Châtaigne (fraîche, crème, purée)|3", f"30 cl|de crème fleurette très froide|{CL}|3", "6|petites meringues (ou recette liée)|SUB:meringues|2", f"1 c. à s.|de sucre glace|Sucre glace|1", "50 g|de chocolat noir (facultatif)|Chocolat noir|0?"],
  ["**Chantilly.** Crème et bol au froid 15 min ; fouettée avec le sucre glace jusqu'à former des pics souples (pas plus : elle tournerait en beurre).",
   "**Monter.** Meringue émiettée au fond, chantilly.",
   "**Vermicelles.** Crème de marrons à la poche à douille fine (ou au presse-purée) en fils sur la chantilly.",
   "**Servir.** 30 min au frais ; copeaux de chocolat."],
  keep="Le jour même.", age=1, cats=["enfants"], profil=["sucre"], fetes=["Noël"])

# ———————————————————————————————— Paella valenciana et plateau de fromages
K("paella_valenciana_traditionnelle", "Paella valenciana (poulet, lapin, haricots)", "Paella valenciana", "Europe du Sud › Espagne › Valence", "P", 2, 6, 40, 40, "€€", "Grande poêle large et plate (paellera 38 cm ou plus).",
  "La vraie paella de Valence, celle des familles le dimanche : poulet et lapin dorés, haricots plats et gros haricots blancs, tomate râpée, safran, romarin, un riz qui cuit sans qu'on y touche et accroche juste ce qu'il faut au fond (le socarrat). Pas de fruits de mer.",
  [f"600 g|de cuisses de poulet en morceaux|{CUISSE}|3", "600 g|de lapin en morceaux|Lapin|3", "400 g|de riz rond (bomba ou à paella)|Riz rond / sushi|3", "200 g|de haricots verts plats|Haricots verts|2", "200 g|de gros haricots blancs cuits (garrofó)|Haricots blancs / lingots|2",
   f"2|tomates mûres râpées|{TOM}|2", "1 pincée|de safran + 1 c. à c. de paprika|Safran (pistils)|2", f"1 branche|de romarin|{THYM}|1", f"8 c. à s.|d'huile d'olive|{HO}|2", f"1 c. à s.|de sel|{SEL}|1"],
  ["**Dorer.** Huile dans la paellera, viandes salées, 15 min à feu moyen en les retournant : dorées de partout (c'est le goût du bouillon).",
   "**Légumes.** Haricots plats en tronçons 5 min ; viandes poussées sur les bords, tomate râpée et paprika au centre, 5 min : la tomate devient une pâte sombre.",
   "**Bouillon.** 1,5 l d'eau, haricots blancs, safran, sel ; 20 min à frémissement : un bouillon un peu trop salé (le riz l'absorbera). Goûte.",
   "**Riz.** Versé en croix, réparti d'un geste, **et on ne remue plus jamais**. Feu vif 8 min, puis moyen 8 min ; romarin posé dessus les 5 dernières minutes.",
   "**Socarrat.** 1 à 2 min à feu vif à la fin : ça crépite et sent le grillé sans brûler, le fond caramélise.",
   "**Reposer.** Hors du feu, couvert d'un torchon, 5 min. Servie dans la poêle, avec des quartiers de citron."],
  tips=["Une poêle plus grande vaut mieux qu'un riz épais : 1 à 2 cm de riz au plus.", "Pas de lapin : tout en poulet. Pas de garrofó : lingots ou cocos."],
  keep="Le jour même.", age=1, cats=["enfants"], fetes=["Repas de famille"])

K("plateau_fromages", "Composer un plateau de fromages", "Plateau de fromages", "France", "A", 1, 8, 15, 60, "€€€", "Planche, couteaux.",
  "Le service qui distingue un repas de fête à la française : entre le plat et le dessert, trois à cinq fromages de familles différentes, du plus doux au plus fort, avec pain, fruits et noix.",
  ["150 g|de pâte molle (camembert, brie)|Camembert / brie|3", f"150 g|de pâte pressée (comté, beaufort)|{GRUY}|3", "120 g|de persillé (roquefort, bleu)|Roquefort / bleu|2", "120 g|de chèvre (bûche, crottin)|Chèvre (frais, bûche)|2",
   "1|pain de campagne ou aux noix|Pain de campagne / complet|2", "1 grappe|de raisin ou des figues|Raisin|1", "50 g|de noix|Noix|1", f"2 c. à s.|de miel ou de confiture|{MIEL}|0?"],
  ["**Choisir.** Une famille de chaque : une pâte molle, une pâte pressée, un persillé, un chèvre ; 40 à 60 g par personne en tout (80 g si c'est le plat).",
   "**Tempérer.** Sortis du frigo 1 h avant, emballage retiré : à température, ils libèrent leurs arômes.",
   "**Disposer.** Du plus doux au plus fort dans le sens des aiguilles d'une montre, un couteau par fromage (le bleu parfume tout).",
   "**Accompagner.** Pain tranché, raisin, noix, un peu de miel pour le bleu ou le chèvre."],
  tips=["Pour les enfants et les femmes enceintes : fromages au lait pasteurisé ou pâtes pressées cuites (comté, beaufort).", "Les restes, emballés dans du papier, font un gratin de pâtes ou une soupe à l'oignon."],
  keep="Chaque fromage dans son papier, au bas du frigo.", age=3, fetes=["Repas de famille", "Noël"], cats=["fetes"])
