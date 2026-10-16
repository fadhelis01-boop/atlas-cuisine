# -*- coding: utf-8 -*-
"""Vague 4 · Audit du chef (16/10/2026) : Italie par régions (Latium, Campanie, Toscane, Piémont, Lombardie, Sicile, Pouilles),
Espagne, Portugal et Grèce : les classiques du catalogue du Tome 4 encore sans fiche. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

IT = "Europe du Sud › Italie"; ES = "Europe du Sud › Espagne"; PT = "Europe du Sud › Portugal"; GR = "Europe du Sud › Grèce"
VB = ("Sans alcool", ["alcohol"], {"Vin blanc": [("Bouillon d'os maison (bœuf/volaille)", 0.8), ("Citron", 0.1)]}, "Vin blanc → **bouillon + un trait de citron**. **À tester**.")
VR = ("Sans alcool", ["alcohol"], {"Vin rouge": [("Bouillon d'os maison (bœuf/volaille)", 0.7), ("Jus de raisin / pomme (pur jus)", 0.2), ("Vinaigre de vin rouge / blanc", 0.05)]}, "Vin rouge → **bouillon + un peu de jus de raisin + un trait de vinaigre**. **À tester**.")

K("bucatini_amatriciana", "Pâtes à l'amatriciana", "Bucatini all'amatriciana", f"{IT} › Latium › Amatrice", "P", 1, 4, 10, 15, "€€", "Poêle, casserole.",
  "Joue de porc croustillante, tomate, piment et pecorino : la sauce emblématique de Rome. La version sans porc utilise des lardons de dinde fumés.",
  [f"400 g|de bucatini ou spaghetti|{PATES}|3", "150 g|de guanciale (ou poitrine fumée)|Guanciale|3", f"400 g|de tomates pelées|{PELEES}|2", f"1 pincée|de piment|Flocons de piment|1", "60 g|de pecorino|Pecorino|2", "5 cl|de vin blanc (facultatif)|Vin blanc|1?"],
  ["**Fondre.** Guanciale en lardons, poêle froide puis feu moyen, 6 min : la graisse fond, il devient croustillant et doré.",
   "**Sauce.** Vin (il s'évapore), tomates écrasées, piment ; 10 min à frémissement.", "**Lier.** Pâtes al dente et un peu d'eau de cuisson dans la sauce, 1 min ; pecorino hors du feu."],
  age=6, var=[("Sans porc", ["pork"], {"Guanciale": [("Lardons de dinde / de volaille fumés", 1.0)]}, "Guanciale → **lardons de dinde fumés + 1 c. à s. d'huile d'olive** (ils sont maigres). **À tester**."), VB], tech=["cuire les pâtes"])

K("gnocchi_sorrentina", "Gnocchi à la sorrentine", "Gnocchi alla sorrentina", f"{IT} › Campanie › Sorrente", "P", 1, 4, 10, 25, "€", "Plat à four.",
  "Gnocchi, sauce tomate au basilic et mozzarella, gratinés dans un plat en terre : le dimanche à Sorrente, en 35 minutes.",
  ["800 g|de gnocchi|Gnocchi|3", f"600 g|de sauce tomate|{PELEES}|2", "2 boules|de mozzarella|Mozzarella / burrata|2", f"40 g|de parmesan|{PARM}|1", "1 bouquet|de basilic|Basilic|1", f"1 gousse|d'ail|{AIL}|1"],
  ["**Sauce.** Ail dans l'huile, tomates, basilic, 10 min.", "**Mélanger.** Gnocchi cuits 2 min (ils remontent), égouttés, dans la sauce.", "**Gratiner.** Plat, mozzarella, parmesan ; 220 °C, 12 min : filant et doré."],
  age=1, cats=["enfants", "vegetarien"])

K("ribollita", "Ribollita (soupe toscane au pain)", "Ribollita", f"{IT} › Toscane", "So", 1, 6, 25, 60, "€", "Faitout.",
  "Haricots blancs, chou kale (cavolo nero), légumes et pain rassis « rebouillis » : la soupe épaisse et généreuse des paysans toscans. Anti-gaspi par excellence.",
  ["400 g|de haricots blancs cuits|Haricots blancs / lingots|3", "1 botte|de chou kale|Chou vert / frisé / kale|2", f"2|carottes|{CAROTTE}|1", "2 branches|de céleri|Céleri-branche|1", f"1|oignon|{OIG}|1", f"400 g|de tomates pelées|{PELEES}|1", "4 tranches|de pain rassis|Pain rassis (réservé)|2", f"6 c. à s.|d'huile d'olive|{HO}|2", f"1 c. à c.|de thym|{THYM}|0"],
  ["**Soffritto.** Oignon, carottes, céleri en petits dés, 10 min dans l'huile : tendres.", "**Mijoter.** Tomates, kale émincé, la moitié des haricots écrasés, l'autre entière, 1,5 l d'eau ; 45 min.",
   "**Épaissir.** Pain en morceaux, 10 min : la soupe devient presque une purée. Huile d'olive crue au service. Encore meilleure le lendemain."],
  age=1, cats=["vegetarien", "zero_dechet"], profil=["leger"])

K("vitello_tonnato", "Vitello tonnato", "Vitello tonnato", f"{IT} › Piémont", "E", 2, 6, 30, 50, "€€€", "Cocotte, mixeur.",
  "Rôti de veau cuit doucement, tranché fin et nappé d'une sauce au thon, câpres et anchois : l'entrée froide des étés piémontais.",
  ["800 g|de rôti de veau|Rôti de veau|3", "1 boîte (160 g)|de thon à l'huile|Thon en conserve|3", "4 c. à s.|de mayonnaise|SUB:mayonnaise|2", "1 c. à s.|de câpres|Câpres|1", "3|filets d'anchois|Anchois (filets, conserve)|1?", f"1|citron|{CIT}|1", f"1|carotte|{CAROTTE}|1", f"1|oignon|{OIG}|1"],
  ["**Cuire.** Veau dans l'eau frémissante salée avec carotte et oignon, 45 min (60 °C à cœur au thermomètre) ; refroidi dans le bouillon.",
   "**Sauce.** Thon, mayonnaise, câpres, anchois, citron, 3 c. à s. de bouillon, mixés : crème lisse.", "**Dresser.** Veau en tranches très fines, nappé, câpres ; 2 h au frais."],
  age=6, fetes=["Barbecue d'été", "Repas de famille"], profil=["poisson"])

K("cannoli_ricotta", "Cannoli siciliens à la ricotta (coques du commerce ou maison)", "Cannoli", f"{IT} › Sicile", "D", 2, 12, 30, 15, "€€", "Poche à douille, tubes à cannoli (pour la version maison).",
  "Coques croustillantes garnies minute de ricotta sucrée, pistaches et pépites de chocolat : le dessert de fête sicilien. Version simple : coques achetées ou gaufrettes roulées.",
  ["12|coques à cannoli (épicerie italienne) ou cigarettes russes|Biscuits (spéculoos, sablés)|3", "500 g|de ricotta bien égouttée|Ricotta|3", "80 g|de sucre glace|Sucre glace|2", "50 g|de pépites de chocolat|Pépites de chocolat|1", "30 g|de pistaches|Pistache|1", "1 zeste|d'orange|Orange|1"],
  ["**Égoutter.** Ricotta une nuit dans une passoire avec un torchon : sinon la crème coule.", "**Crème.** Ricotta lissée au fouet avec sucre glace et zeste ; pépites.",
   "**Garnir.** Au dernier moment (la coque ramollit en 1 h) ; extrémités dans les pistaches hachées, sucre glace."], age=3, fetes=["Anniversaire", "Noël"], profil=["sucre"])

K("pasta_e_fagioli", "Pâtes aux haricots (pasta e fagioli)", "Pasta e fagioli", f"{IT} › Vénétie", "So", 1, 4, 15, 30, "€", "Faitout.",
  "Une soupe-repas épaisse : haricots borlotti, tomate, romarin et petites pâtes cuites dedans. Le plat du pauvre devenu classique.",
  ["400 g|de haricots borlotti ou rouges cuits|Haricots rouges / noirs|3", f"150 g|de petites pâtes (ditalini)|{PATES}|3", f"1|oignon|{OIG}|1", "1 branche|de céleri|Céleri-branche|1", f"2 c. à s.|de concentré de tomate|{CONC}|1", f"1 branche|de romarin|{THYM}|1", f"4 c. à s.|d'huile d'olive|{HO}|1", f"40 g|de parmesan|{PARM}|1?"],
  ["**Base.** Oignon et céleri 8 min, concentré, romarin ; haricots, 1 l d'eau, 15 min ; écrase un tiers des haricots.", "**Pâtes.** Dedans, 10 min en remuant : c'est épais et crémeux.", "**Servir.** Huile crue, poivre, parmesan."],
  age=1, cats=["vegetarien", "enfants"])

K("pollo_cacciatora", "Poulet chasseur à l'italienne", "Pollo alla cacciatora", f"{IT} › Toscane", "P", 1, 4, 20, 45, "€€", "Cocotte.",
  "Poulet mijoté avec tomates, olives, romarin, ail et un peu de vin : le plat des chasseurs, rustique et parfumé.",
  [f"8|morceaux de poulet|{CUISSE}|3", f"400 g|de tomates pelées|{PELEES}|2", "60 g|d'olives noires|Olives (vertes / noires)|1", f"1|oignon|{OIG}|1", f"2 gousses|d'ail|{AIL}|1", f"1 branche|de romarin|{THYM}|1", "12 cl|de vin rouge|Vin rouge|1", f"1|poivron|{POIVRON}|1?"],
  ["**Dorer.** Poulet salé, 10 min : peau dorée ; réservé.", "**Sauce.** Oignon, ail, poivron, 5 min ; vin réduit de moitié ; tomates, romarin.", "**Mijoter.** Poulet, couvert 35 min ; olives 5 min. Polenta ou pain."],
  age=3, var=[VR], fetes=["Repas de famille"])

K("scaloppine_limone", "Escalopes de veau au citron (scaloppine al limone)", "Scaloppine al limone", f"{IT} › Lombardie › Milan", "P", 1, 4, 10, 10, "€€", "Poêle.",
  "Escalopes fines farinées, saisies, et une sauce minute beurre-citron-câpres : un dîner chic en 20 minutes.",
  ["8|escalopes fines de veau (ou de dinde)|Escalope de veau|3", f"40 g|de farine|{F55}|1", f"40 g|de beurre|{BEURRE}|2", f"1|citron|{CIT}|2", "1 c. à s.|de câpres|Câpres|1?", "8 cl|de vin blanc ou de bouillon|Vin blanc|1", f"1 c. à s.|de persil|{PERSIL}|1"],
  ["**Saisir.** Escalopes farinées (secoue l'excès), beurre moussant, 1 min par face : dorées ; au chaud.", "**Sauce.** Vin dans la poêle, gratte les sucs, 1 min ; jus de citron, beurre froid en morceaux en remuant : sauce brillante.",
   "**Servir.** Escalopes nappées, câpres, persil."], age=3, var=[VB], tech=["saisir", "déglacer"])

K("risotto_milanese", "Risotto à la milanaise (au safran)", "Risotto alla milanese", f"{IT} › Lombardie › Milan", "P", 2, 4, 30, 0, "€€", "Sauteuse.",
  "Riz crémeux au safran doré, beurre et parmesan : l'accompagnement de l'osso buco, ou un plat à lui seul.",
  ["320 g|de riz à risotto|Riz à risotto (arborio, carnaroli)|3", "1 dose (0,2 g)|de safran|Safran (pistils)|2", "1 l|de bouillon de volaille chaud|Bouillon cube volaille|2", f"1|oignon|{OIG}|1", f"60 g|de beurre|{BEURRE}|2", f"60 g|de parmesan|{PARM}|2", "10 cl|de vin blanc|Vin blanc|1"],
  ["**Nacrer.** Oignon haché fin 3 min au beurre ; riz 2 min : translucide sur les bords ; vin, il s'évapore.", "**Cuire.** Bouillon louche par louche en remuant, 17 min ; safran infusé dans une louche de bouillon à mi-cuisson.",
   "**Mantecare.** Hors du feu, beurre froid et parmesan, remue vivement : crémeux, il ondule (« all'onda »)."], age=3, var=[VB], tech=["nacrer"])

K("spaghetti_vongole", "Spaghetti aux palourdes", "Spaghetti alle vongole", f"{IT} › Campanie › Naples", "P", 2, 4, 15, 15, "€€", "Grande poêle avec couvercle.",
  "Palourdes ouvertes à l'ail, au piment et au persil, leur jus iodé qui enrobe les spaghetti : le plat de la Saint-Sylvestre napolitaine.",
  [f"400 g|de spaghetti|{PATES}|3", "1 kg|de palourdes|Palourdes / coques|3", f"3 gousses|d'ail|{AIL}|2", f"1 pincée|de piment|Flocons de piment|1", f"1 bouquet|de persil|{PERSIL}|2", f"5 c. à s.|d'huile d'olive|{HO}|2", "10 cl|de vin blanc|Vin blanc|1"],
  ["**Dégorger.** Palourdes 1 h dans l'eau froide salée : elles rejettent le sable.", "**Ouvrir.** Ail et piment dans l'huile, palourdes, vin ; couvert 3-4 min : elles s'ouvrent (jette les fermées).",
   "**Lier.** Spaghetti cuits 2 min de moins, finis 2 min dans le jus en remuant : la sauce devient légèrement crémeuse ; persil."],
  age=6, profil=["poisson"], var=[VB], tech=["moules et coquillages"])

K("bruschetta_tomates", "Bruschetta aux tomates et basilic", "Bruschetta al pomodoro", f"{IT} › Latium", "E", 1, 4, 15, 5, "€", "Grille ou four.",
  "Pain grillé frotté à l'ail, tomates mûres en dés, basilic et huile d'olive : l'antipasto de l'été, à faire minute.",
  ["8 tranches|de pain de campagne|Pain de campagne / complet|3", f"4|tomates mûres|{TOM}|3", f"1 gousse|d'ail|{AIL}|1", "8 feuilles|de basilic|Basilic|1", f"4 c. à s.|d'huile d'olive|{HO}|2"],
  ["**Tomates.** En petits dés, sel, huile, basilic ; 10 min.", "**Griller.** Pain doré, frotté à l'ail cru.", "**Garnir.** Au dernier moment (sinon le pain ramollit)."],
  age=3, cats=["vegetarien"], fetes=["Apéritif dînatoire", "Barbecue d'été"], profil=["leger"])

K("salade_caprese", "Salade caprese", "Insalata caprese", f"{IT} › Campanie › Capri", "E", 1, 4, 10, 0, "€€", "Plat.",
  "Tomate, mozzarella di bufala, basilic, huile d'olive : les couleurs du drapeau italien, et rien d'autre. La qualité des produits fait tout.",
  [f"4|tomates mûres|{TOM}|3", "2 boules|de mozzarella di bufala|Mozzarella / burrata|3", "1 bouquet|de basilic|Basilic|2", f"4 c. à s.|d'huile d'olive|{HO}|2", f"1 pincée|de fleur de sel|{SEL}|1"],
  ["**Trancher.** Tomates et mozzarella en tranches de même épaisseur.", "**Alterner.** Tomate, mozzarella, feuille de basilic ; fleur de sel, poivre, huile. Pas de vinaigre balsamique dans la vraie recette."],
  age=1, cats=["vegetarien"], fetes=["Barbecue d'été"], profil=["leger"])

K("cantucci", "Cantucci aux amandes", "Cantucci di Prato", f"{IT} › Toscane › Prato", "G", 1, 30, 20, 40, "€", "Four, plaque.",
  "Biscuits cuits deux fois, croquants et pleins d'amandes : à tremper dans le café ou un vin doux.",
  [f"250 g|de farine|{F55}|3", f"150 g|de sucre|{SUCRE}|2", f"2|œufs|{OEUF}|2", "150 g|d'amandes entières|Amande (entière, effilée, poudre)|3", f"1 c. à c.|de levure chimique|{LEVC}|1", "1 zeste|d'orange|Orange|1"],
  ["**Pâte.** Tout mélangé : pâte collante ; deux boudins de 4 cm sur la plaque.", "**Première cuisson.** 180 °C, 25 min : dorés ; 10 min de repos.",
   "**Seconde cuisson.** Tranchés en biais (1 cm), à plat, 10-12 min : secs et croquants."], age=3, cats=["enfants"], profil=["sucre"], keep="1 mois dans une boîte en fer.")

K("torta_della_nonna", "Torta della nonna (tarte de grand-mère à la crème)", "Torta della nonna", f"{IT} › Toscane", "D", 2, 8, 35, 40, "€€", "Moule à tarte 24 cm.",
  "Deux disques de pâte sablée au citron enfermant une crème pâtissière, pignons et sucre glace : la tarte des dimanches toscans.",
  ["2|pâtes sablées|Pâte brisée / sablée (prête)|3", "50 cl|de crème pâtissière|SUB:creme_patissiere|3", "1 zeste|de citron|Citron|1", "40 g|de pignons|Pignons de pin|2", "2 c. à s.|de sucre glace|Sucre glace|1", f"1|œuf (dorure)|{OEUF}|1"],
  ["**Crème.** Pâtissière parfumée au zeste, refroidie.", "**Monter.** Pâte dans le moule, crème, second disque soudé ; dorure, pignons.", "**Cuire.** 180 °C, 40 min : doré. Froid, sucre glace."],
  age=3, fetes=["Repas de famille"], profil=["sucre"], tech=["foncer une pâte", "crème pâtissière"])

K("calzone", "Calzone tomate-mozzarella-champignons", "Calzone", f"{IT} › Campanie › Naples", "P", 1, 4, 20, 15, "€", "Four, plaque.",
  "La pizza repliée en chausson : sauce tomate, mozzarella, champignons et jambon de dinde (ou ricotta), bien gonflée et dorée.",
  ["500 g|de pâte à pizza|SUB:pate_pizza|3", f"200 g|de sauce tomate|{PELEES}|2", "2 boules|de mozzarella|Mozzarella / burrata|2", "150 g|de champignons|Champignon de Paris|1", "100 g|de jambon de dinde (ou ricotta)|Jambon de dinde / de poulet|1?", f"1 pincée|d'origan|Origan frais / sec|0"],
  ["**Étaler.** 4 disques de 22 cm ; garniture sur une moitié, sans aller au bord.", "**Fermer.** Plie, soude en roulant le bord ; une petite entaille dessus.", "**Cuire.** Four au maximum (250 °C), 12-15 min : gonflé et doré."],
  age=3, cats=["enfants"])

K("tagliatelle_ragu", "Tagliatelles au ragù bolognais", "Tagliatelle al ragù", f"{IT} › Émilie-Romagne › Bologne", "P", 1, 6, 30, 120, "€€", "Cocotte.",
  "Le vrai ragù de Bologne : bœuf mijoté deux heures avec soffritto, un peu de tomate et de lait, servi avec des tagliatelles (jamais des spaghetti).",
  ["500 g|de bœuf haché|Bœuf haché|3", "500 g|de tagliatelles|Pâtes fraîches aux œufs|3", f"1|carotte|{CAROTTE}|1", "1 branche|de céleri|Céleri-branche|1", f"1|oignon|{OIG}|1", f"3 c. à s.|de concentré de tomate|{CONC}|2", f"15 cl|de lait|{LAIT}|1", "10 cl|de vin rouge|Vin rouge|1", f"60 g|de parmesan|{PARM}|1"],
  ["**Soffritto.** Carotte, céleri, oignon en tout petits dés, 10 min.", "**Viande.** 10 min à feu vif en émiettant : elle grésille ; vin, réduit ; concentré, lait, 30 cl d'eau.",
   "**Mijoter.** 2 h à couvert, à peine frémissant : la sauce est épaisse et brillante. Avec les tagliatelles, parmesan."], age=1, cats=["enfants"], var=[VR], fetes=["Repas de famille"])

K("carpaccio_boeuf", "Carpaccio de bœuf, roquette et parmesan", "Carpaccio", f"{IT} › Vénétie › Venise", "E", 1, 4, 20, 30, "€€€", "Couteau bien aiguisé, film.",
  "Filet de bœuf tranché très fin, citron, huile d'olive, roquette et copeaux de parmesan : inventé au Harry's Bar de Venise en 1950.",
  ["300 g|de filet ou rumsteck très frais|Rumsteck|3", "2 poignées|de roquette|Roquette / mâche|2", f"40 g|de parmesan|{PARM}|2", f"1|citron|{CIT}|1", f"4 c. à s.|d'huile d'olive|{HO}|2", "1 c. à s.|de câpres|Câpres|1?"],
  ["**Raffermir.** Viande filmée 30 min au congélateur : elle se tranche beaucoup plus fin.", "**Trancher.** Le plus fin possible, aplati entre deux films au rouleau.", "**Assaisonner.** Au dernier moment : citron, huile, sel, poivre, roquette, parmesan."],
  age=None, kids="Viande crue : déconseillé aux enfants, aux femmes enceintes et aux personnes fragiles.", fetes=["Saint-Valentin"], profil=["leger"])

# ——— Espagne, Portugal, Grèce ———
K("pisto_manchego", "Pisto manchego (ratatouille espagnole, œuf au plat)", "Pisto manchego", f"{ES} › Castille-La Manche", "P", 1, 4, 20, 40, "€", "Sauteuse.",
  "Courgettes, poivrons, oignon et tomate fondus lentement à l'huile d'olive, couronnés d'un œuf au plat : le cousin espagnol de la ratatouille.",
  ["2|courgettes|Courgette|2", f"2|poivrons|{POIVRON}|2", f"2|oignons|{OIG}|1", f"500 g|de tomates|{TOM}|2", f"4|œufs|{OEUF}|2", f"5 c. à s.|d'huile d'olive|{HO}|2"],
  ["**Fondre.** Oignons et poivrons 10 min ; courgettes 10 min.", "**Mijoter.** Tomates pelées concassées, sel, 20 min : confit.", "**Servir.** Œufs au plat dessus, pain."],
  age=1, cats=["vegetarien"], profil=["leger"])

K("pulpo_gallega", "Poulpe à la galicienne", "Pulpo a la gallega", f"{ES} › Galice", "E", 2, 4, 15, 50, "€€€", "Grand faitout.",
  "Poulpe tendre en rondelles sur des pommes de terre, huile d'olive, gros sel et paprika fumé : le plat des fêtes de village galiciennes.",
  ["1,2 kg|de poulpe (décongelé : la congélation l'attendrit)|Poulpe / seiche|3", f"4|pommes de terre|{PDT}|2", f"1 c. à s.|de paprika fumé|{PFUME}|2", f"6 c. à s.|d'huile d'olive|{HO}|2", f"1 c. à c.|de gros sel|{SEL}|1"],
  ["**Cuire.** Poulpe plongé trois fois 3 s dans l'eau bouillante (les tentacules frisent), puis 45 min à frémissement : la pointe d'un couteau entre sans résistance.",
   "**Pommes de terre.** Cuites 20 min dans l'eau du poulpe.", "**Dresser.** Rondelles de poulpe aux ciseaux sur les pommes de terre, huile, paprika, gros sel."],
  age=6, fetes=["Apéritif dînatoire"], profil=["poisson"])

K("sardines_grillees_portugal", "Sardines grillées à la portugaise", "Sardinhas assadas", f"{PT} › Lisbonne", "P", 1, 4, 10, 8, "€", "Barbecue, plancha ou gril du four.",
  "Sardines entières au gros sel, grillées sur la braise, sur une tranche de pain qui boit le jus : la Saint-Antoine à Lisbonne.",
  ["12|sardines fraîches|Sardine (fraîche / conserve)|3", "1 c. à s.|de gros sel|Sel fin / gros sel / fleur de sel|2", f"2|poivrons grillés (salade)|{POIVRON}|1", f"1|citron|{CIT}|1", "4 tranches|de pain de campagne|Pain de campagne / complet|1"],
  ["**Saler.** Sardines entières (non vidées, c'est la tradition ; ou vidées), gros sel, 20 min.", "**Griller.** Braise très chaude, 3-4 min par face : peau qui cloque et noircit par endroits.", "**Servir.** Sur le pain, citron, salade de poivrons."],
  age=6, fetes=["Barbecue d'été"], profil=["poisson"])

K("keftedes", "Keftedes (boulettes grecques à la menthe)", "Keftedes", GR, "P", 1, 4, 25, 15, "€", "Poêle.",
  "Boulettes de bœuf à la menthe, à l'origan et à l'oignon râpé, dorées à la poêle : en mezzé avec tzatziki ou en plat avec pommes de terre.",
  ["500 g|de bœuf haché|Bœuf haché|3", f"1|oignon râpé|{OIG}|1", "2 tranches|de pain rassis trempé|Pain rassis (réservé)|1", f"1|œuf|{OEUF}|1", "½ bouquet|de menthe|Menthe|2", f"1 c. à c.|d'origan|Origan frais / sec|1", f"30 g|de farine|{F55}|1", "200 g|de tzatziki|Tzatziki|1"],
  ["**Mélanger.** Viande, oignon râpé avec son jus, pain pressé, œuf, herbes, sel ; 30 min au frais.", "**Former.** Boulettes de la taille d'une noix, roulées dans la farine.", "**Cuire.** Huile chaude, 6-8 min en les roulant : dorées partout."],
  age=3, cats=["enfants"], fetes=["Apéritif dînatoire"])

K("fasolada", "Fasolada (soupe de haricots grecque)", "Fasolada", GR, "So", 1, 6, 15, 60, "€", "Faitout.",
  "La soupe nationale grecque : haricots blancs, tomate, carotte, céleri et beaucoup d'huile d'olive. Simple, nourrissante, végétalienne.",
  ["400 g|de haricots blancs cuits|Haricots blancs / lingots|3", f"2|carottes|{CAROTTE}|1", "2 branches|de céleri|Céleri-branche|1", f"1|oignon|{OIG}|1", f"2 c. à s.|de concentré de tomate|{CONC}|1", f"8 c. à s.|d'huile d'olive|{HO}|2", f"1|citron|{CIT}|1?"],
  ["**Base.** Légumes en petits dés 10 min dans la moitié de l'huile.", "**Mijoter.** Concentré, haricots, 1,2 l d'eau, 45 min : épaisse.", "**Finir.** Reste d'huile crue, sel, poivre, citron ; olives et feta à côté."],
  age=1, cats=["vegetarien"], profil=["leger"])

K("pastitsio", "Pastitsio (gratin de pâtes grec)", "Pastítsio", GR, "P", 2, 8, 45, 45, "€€", "Grand plat à four.",
  "Pâtes, sauce à la viande parfumée à la cannelle et épaisse béchamel gratinée : la « lasagne » grecque des repas de famille.",
  [f"400 g|de pâtes longues creuses (ou penne)|{PATES}|3", "500 g|de bœuf haché|Bœuf haché|3", f"400 g|de tomates pelées|{PELEES}|2", f"1|oignon|{OIG}|1", f"1 c. à c.|de cannelle|{CANN}|1", "70 cl|de béchamel|SUB:bechamel|3", f"80 g|de fromage râpé|{GRUY}|1", f"2|œufs|{OEUF}|1"],
  ["**Sauce.** Oignon, viande 8 min, tomates, cannelle, sel ; 20 min : épaisse.", "**Pâtes.** Cuites aux deux tiers, mélangées à la moitié du fromage et un œuf.",
   "**Monter et cuire.** Pâtes, viande, pâtes ; béchamel mélangée au second œuf ; fromage ; 180 °C, 45 min ; 20 min de repos pour couper net."],
  age=1, cats=["enfants"], fetes=["Repas de famille"], tech=["faire un roux"])

K("loukoumades", "Loukoumades (beignets grecs au miel)", "Loukoumádes", GR, "D", 1, 30, 20, 60, "€", "Casserole profonde, thermomètre, 2 cuillères.",
  "Petites boules de pâte levée frites, arrosées de sirop de miel, cannelle et noix : les beignets des fêtes grecques depuis l'Antiquité.",
  [f"250 g|de farine|{F55}|3", f"7 g|de levure boulangère|{LEV}|2", f"25 cl|d'eau tiède|-|2", f"150 g|de miel|{MIEL}|3", f"1 c. à c.|de cannelle|{CANN}|1", "40 g|de noix|Noix|1", "1 l|d'huile de friture|Huile de tournesol / colza|2"],
  ["**Pâte.** Farine, levure, sel, eau : pâte collante ; 1 h au chaud : bullée.", "**Frire.** Boules prises à la cuillère mouillée, huile à 175 °C, 3 min : dorées et gonflées.", "**Napper.** Miel chauffé avec 3 c. à s. d'eau, cannelle, noix."],
  age=1, cats=["enfants"], profil=["sucre"], tech=["frire en sécurité"])

K("salmorejo", "Salmorejo (crème froide de tomate de Cordoue)", "Salmorejo cordobés", f"{ES} › Andalousie › Cordoue", "So", 1, 4, 15, 60, "€", "Mixeur.",
  "Tomates mûres, pain, ail et huile d'olive mixés en une crème froide épaisse, avec œuf dur et jambon (ou thon) : plus onctueux que le gaspacho.",
  ["1 kg|de tomates très mûres|Tomate|3", "150 g|de pain de la veille|Pain rassis (réservé)|2", f"1 gousse|d'ail|{AIL}|1", f"10 cl|d'huile d'olive|{HO}|2", "1 c. à s.|de vinaigre de xérès|Vinaigre de xérès|1", f"2|œufs durs|{OEUF}|1", "50 g|de jambon cru ou de thon|Thon en conserve|1?"],
  ["**Mixer.** Tomates, pain, ail, sel, longuement ; huile en filet : crème épaisse et orangée.", "**Rafraîchir.** 1 h au frigo.", "**Servir.** Œuf dur haché, thon ou jambon, filet d'huile."],
  age=1, cats=["zero_dechet"], fetes=["Barbecue d'été"], profil=["leger"])

K("albondigas_tomate", "Albóndigas en sauce tomate", "Albóndigas", ES, "P", 1, 4, 25, 25, "€", "Sauteuse.",
  "Boulettes de bœuf à l'ail et au persil, dorées puis mijotées dans une sauce tomate au paprika : la tapa la plus populaire d'Espagne.",
  ["500 g|de bœuf haché|Bœuf haché|3", f"1|œuf|{OEUF}|1", "40 g|de chapelure|Chapelure|1", f"2 gousses|d'ail|{AIL}|1", f"½ bouquet|de persil|{PERSIL}|1", f"400 g|de tomates pelées|{PELEES}|2", f"1|oignon|{OIG}|1", f"1 c. à c.|de paprika fumé|{PFUME}|1"],
  ["**Boulettes.** Viande, œuf, chapelure, ail, persil, sel ; 20 boulettes dorées à la poêle.", "**Sauce.** Oignon 5 min, paprika, tomates, 10 min.", "**Mijoter.** Boulettes dans la sauce, 15 min. Avec du pain ou du riz."],
  age=3, cats=["enfants"], fetes=["Apéritif dînatoire"])

K("pollo_al_ajillo", "Poulet à l'ail à l'espagnole", "Pollo al ajillo", f"{ES} › Andalousie", "P", 1, 4, 15, 30, "€€", "Grande poêle avec couvercle.",
  "Morceaux de poulet dorés avec une tête d'ail entière en chemise, laurier, un trait de vin ou de bouillon : l'ail devient doux et fondant.",
  [f"1 kg|de morceaux de poulet|{CUISSE}|3", f"1 tête|d'ail|{AIL}|3", f"2|feuilles de laurier|{LAURIER}|1", "10 cl|de vin blanc (ou bouillon)|Vin blanc|1", f"5 c. à s.|d'huile d'olive|{HO}|2", f"1 c. à s.|de persil|{PERSIL}|1"],
  ["**Dorer.** Poulet salé, 12 min à feu moyen : bien doré.", "**Ail.** Gousses en chemise écrasées, laurier, 5 min.", "**Mijoter.** Vin, couvert 15 min : jus clair ; persil. L'ail se presse sur le pain."],
  age=3, var=[VB])
