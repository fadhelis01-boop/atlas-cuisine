# -*- coding: utf-8 -*-
"""Vague 9 (suite) · 11/11/2026 : cuisine italienne la plus vue sur TikTok. Onglet « Populaire » de @chefmaxmariola
(4,3 M d'abonnés, vidéos de 4 à 38 M de vues), de @giallozafferano (3,1 M) et de @charlene_et_francesca (540 k), plus une
vidéo trouvée par la recherche « recette italienne ». Seuls les plats absents d'ATLAS deviennent des fiches ; les autres
vidéos sont rattachées aux fiches existantes (videos_favoris.EN_PLUS_2026_11_11C). Réécrites, porc remplacé (D21),
créditées. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *
from recipes_v6_tiktok_plats import C

TT = "https://www.tiktok.com/"
def V(author, vid):
    return (f"@{author}", f"{TT}@{author}/video/{vid}")
MM = "chefmaxmariola"; GZ = "giallozafferano"; CF = "charlene_et_francesca"

IT = "Europe du Sud › Italie"; LAZ = "Europe du Sud › Italie › Latium"; CAMP = "Europe du Sud › Italie › Campanie"; TOSC = "Europe du Sud › Italie › Toscane"
PECO = "Pecorino"; MOZZ = "Mozzarella / burrata"; TOMC = "Tomate"; BASIL = "Basilic"; PEP = "Piment frais (divers)"; FLOC = "Flocons de piment"

# ---------- Pâtes ----------
K("gricia_version", "Gricia (version au bacon de bœuf, pecorino et poivre)", "Pasta alla gricia", LAZ, "P", 1, 4, 10, 15, "€€", "Grande poêle, casserole.",
  "L'ancêtre de la carbonara et de l'amatriciana : des pâtes, du pecorino, du poivre et la graisse fondue de la joue de porc. Ici, le guanciale est remplacé par du bacon de bœuf bien gras ; la sauce se fait avec l'eau de cuisson, sans crème.",
  [f"350 g|de rigatoni ou de spaghetti|{PATES}|3", "150 g|de bacon de bœuf (ou de dinde) épais|Bacon de dinde / de bœuf|3", f"80 g|de pecorino romano|{PECO}|3", f"1 c. à c.|de poivre noir concassé|{POIVRE}|2", f"1 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Fondre.** Bacon en lardons épais, poêle froide avec l'huile, feu moyen 8 min : doré, la graisse a fondu ; hors du feu.",
   "**Pâtes.** Eau peu salée (le pecorino l'est), 2 min de moins que le paquet ; 30 cl d'eau de cuisson gardés.",
   "**Crème de pecorino.** Pecorino râpé fin + poivre torréfié 30 s à sec + 5 c. à s. d'eau de cuisson tiède : pâte lisse.",
   "**Mantecare.** Pâtes dans la poêle avec 10 cl d'eau de cuisson, 2 min à feu vif en remuant ; hors du feu, crème de pecorino, on fouette : sauce brillante qui nappe sans grumeaux."],
  tips=["Si le pecorino fait des fils : poêle trop chaude ; laisse tiédir 30 s avant de l'ajouter."], keep="À manger tout de suite.", age=2, cats=["express"], profil=["gras"],
  credit=C(V(MM, "7253110465616694555")))
K("pasta_e_patate", "Pasta e patate à la napolitaine (pâtes et pommes de terre, provola fondante)", "Pasta e patate", CAMP, "P", 1, 4, 15, 35, "€", "Cocotte.",
  "Le plat pauvre de Naples devenu culte : des pommes de terre fondues avec oignon, céleri et tomate, des pâtes mélangées cuites directement dedans, le tout lié par l'amidon et un cœur de provola qui file. Cuillère obligatoire.",
  [f"300 g|de pâtes mélangées (mista)|{PATES}|3", f"600 g|de pommes de terre|{PDT}|3", "150 g|de provola fumée ou de scamorza (ou mozzarella)|Mozzarella / burrata|2", f"1|oignon|{OIG}|1", "1|branche de céleri|Céleri-branche|1", f"1|carotte|{CAROTTE}|1", f"2 c. à s.|de concentré|{CONC}|1", f"40 g|de parmesan (et la croûte si tu en as)|{PARM}|1", f"3 c. à s.|d'huile d'olive|{HO}|1", "1|petit bouquet de basilic|Basilic|1"],
  ["**Base.** Oignon, céleri, carotte hachés fin, huile, 8 min : fondants ; concentré, 1 min.",
   "**Pommes de terre.** En dés de 1 cm, 1 L d'eau chaude, sel, croûte de parmesan ; 15 min : les dés s'écrasent en partie.",
   "**Pâtes.** Directement dedans, 10 à 12 min en remuant souvent et en ajoutant de l'eau chaude à la louche : crémeux, presque un risotto.",
   "**Filer.** Hors du feu : parmesan, provola en dés, couvercle 2 min ; basilic, filet d'huile."],
  tips=["Remue souvent : l'amidon attache au fond."], keep="2 jours au frigo (se raffermit, détendre à l'eau chaude).", age=1, cats=["vegetarien", "enfants"], profil=["gras"],
  credit=C(V(MM, "7165465284973841669")))
K("pici_aglione", "Pici all'aglione (grosses pâtes toscanes roulées main, sauce tomate à l'ail)", "Pici all'aglione", TOSC, "P", 2, 4, 50, 45, "€", "Plan de travail, casserole, poêle.",
  "La pâte la plus simple d'Italie : farine, eau, huile, roulée à la main en gros spaghetti irréguliers ; avec la sauce de Sienne, beaucoup d'ail cuit très doucement dans l'huile puis de la tomate et un peu de piment.",
  [f"400 g|de farine T55 (+ semoule fine pour fariner)|{F55}|3", "20 cl|d'eau|-|0", f"1 c. à s.|d'huile d'olive (pâte) + 6 c. à s. (sauce)|{HO}|2", f"6|gousses d'ail|{AIL}|2", "700 g|de tomates pelées (passata)|Coulis / passata / tomates pelées|3", f"1|petit piment|{PEP}|1?", f"40 g|de pecorino|{PECO}|1"],
  ["**Pâte.** Farine, eau, 1 c. à s. d'huile, sel : 10 min, lisse et ferme ; 30 min filmée.",
   "**Rouler.** Abaisse de 1 cm, lanières de 1 cm roulées sous les paumes du centre vers les bouts : boudins de 3 mm, posés sur la semoule.",
   "**Aglione.** Ail émincé dans l'huile froide, feu très doux 10 min : fondant, jamais doré ; tomates, piment, sel, 20 min : sauce épaisse.",
   "**Cuire.** Pici 5 à 7 min dans l'eau bouillante salée ; dans la sauce 1 min avec un peu d'eau de cuisson ; pecorino."],
  keep="Crus : 1 jour sur semoule au frigo, ou congelés.", age=1, cats=["vegetarien", "enfants"], profil=["acide"], kids="✓ dès 1 an, sans piment.",
  credit=C(V(MM, "7298043806769843488")))
K("fettuccine_burro_asperges", "Fettuccine au beurre et au parmesan, asperges (le vrai Alfredo)", "Fettuccine burro e parmigiano", LAZ, "P", 1, 4, 10, 12, "€€", "Casserole, grande poêle.",
  "L'Alfredo romain d'origine, sans crème : du beurre et du parmesan émulsionnés avec l'eau de cuisson des pâtes, ici avec des pointes d'asperges vertes sautées.",
  [f"350 g|de fettuccine (aux œufs)|Pâtes fraîches aux œufs|3", f"80 g|de beurre|{BEURRE}|3", f"100 g|de parmesan|{PARM}|3", "1|botte d'asperges vertes|Asperge|2", f"1|citron (zeste)|{CIT}|1?"],
  ["**Asperges.** Bout dur cassé, tiges en tronçons, pointes entières ; poêle, 20 g de beurre, 4 min : vertes, croquantes ; sel.",
   "**Pâtes.** Eau salée, 1 min de moins ; 25 cl d'eau de cuisson.",
   "**Émulsion.** Poêle, reste de beurre en morceaux, 10 cl d'eau de cuisson : il fond et blanchit.",
   "**Lier.** Pâtes, parmesan en 3 fois en remuant et en ajoutant de l'eau : sauce crémeuse, nappante ; asperges, zeste, poivre."],
  keep="À manger tout de suite.", age=1, cats=["vegetarien", "express", "enfants"], profil=["gras"],
  credit=C(V(MM, "7228238790626790683")))
K("pasta_pecorara", "Pasta alla pecorara (légumes, ricotta et pecorino, Abruzzes)", "Pasta alla pecorara", "Europe du Sud › Italie › Abruzzes", "P", 1, 4, 20, 30, "€", "Grande poêle, casserole.",
  "La pâte du berger des Abruzzes : courgette, aubergine et poivron en petits dés, une sauce tomate, et de la ricotta fraîche mélangée au moment de servir avec le pecorino. Le guanciale de la recette d'origine est ici laissé de côté.",
  [f"350 g|de pâtes courtes (maccheroni, chitarra)|{PATES}|3", "1|courgette|Courgette|2", "1|aubergine|Aubergine|2", f"1|poivron|{POIVRON}|1", f"1|oignon|{OIG}|1", "400 g|de tomates pelées|Coulis / passata / tomates pelées|2", "200 g|de ricotta|Ricotta|3", f"40 g|de pecorino|{PECO}|2", f"4 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Légumes.** En dés de 1 cm ; huile, oignon 3 min, aubergine 5 min, courgette et poivron 5 min : dorés, tendres.",
   "**Sauce.** Tomates écrasées, sel, 15 min : nappante.",
   "**Ricotta.** Battue à la fourchette avec 3 c. à s. d'eau des pâtes : crémeuse.",
   "**Assembler.** Pâtes al dente dans la sauce, 1 min ; dans les assiettes, ricotta par cuillerées, pecorino, poivre."],
  keep="1 jour au frigo.", age=1, cats=["vegetarien", "enfants"], profil=["acide", "leger"],
  credit=C(V(MM, "7170336095824104710")))
K("linguine_crabe", "Linguine au crabe, tomates cerises et piment", "Linguine al granchio", IT, "P", 2, 4, 25, 20, "€€", "Grande sauteuse, casserole.",
  "Les pâtes de la mer : du crabe (bleu ou tourteau) cuit dans l'huile à l'ail et au piment, de la tomate cerise qui éclate, les linguine finies dans la sauce pour qu'elles en prennent tout le goût.",
  ["350 g|de linguine|Pâtes sèches (spaghetti, penne…)|3", "2|crabes (1 kg) coupés en deux, ou 250 g de chair|Crabe / tourteau|3", "300 g|de tomates cerises|Tomate|2", f"3|gousses d'ail|{AIL}|1", f"1|piment|{PEP}|1", f"5 c. à s.|d'huile d'olive|{HO}|1", f"1/2|botte de persil|{PERSIL}|1", f"1|citron (zeste)|{CIT}|1"],
  ["**Saisir.** Huile, ail écrasé, piment, crabes coupés, 4 min : carapace rouge, l'huile se colore.",
   "**Sauce.** Tomates coupées, 20 cl d'eau, 10 min à couvert : les tomates éclatent ; sel.",
   "**Pâtes.** 3 min de moins que le paquet ; finies 3 min dans la sauce avec de l'eau de cuisson : la sauce les nappe.",
   "**Servir.** Persil, zeste, filet d'huile ; pinces cassées pour la chair."],
  tips=["Crustacés : allergène majeur."], keep="À manger tout de suite.", age=3, cats=[], profil=["poisson", "acide"],
  credit=C(V(MM, "7281315412409634080")))
K("penne_arrabbiata", "Penne all'arrabbiata (tomate, ail et piment)", "Penne all'arrabbiata", LAZ, "P", 1, 4, 5, 20, "€", "Sauteuse, casserole.",
  "« À l'enragée » : une sauce tomate romaine montée à l'ail et au piment rouge dans l'huile d'olive, pour des penne rigate, avec du persil. Rapide et franche.",
  [f"350 g|de penne rigate|{PATES}|3", "500 g|de tomates pelées|Coulis / passata / tomates pelées|3", f"3|gousses d'ail|{AIL}|1", f"1 à 2|piments rouges séchés|{FLOC}|2", f"5 c. à s.|d'huile d'olive|{HO}|1", f"1/2|botte de persil|{PERSIL}|1", f"30 g|de pecorino (facultatif)|{PECO}|1?"],
  ["**Infuser.** Huile, ail écrasé, piment émietté, feu doux 3 min : parfumé, l'ail blond.",
   "**Sauce.** Tomates écrasées à la main, sel, 15 min à feu vif : réduite, l'huile perle.",
   "**Pâtes.** 1 min de moins ; dans la sauce avec une louche d'eau de cuisson, 1 min.",
   "**Servir.** Persil, un filet d'huile crue."],
  keep="2 jours au frigo (la sauce).", age=None, cats=["vegetarien", "express"], profil=["acide", "epice"], kids="Pour les enfants : leur part de sauce avant d'ajouter le piment.",
  credit=C(V(MM, "7146265749819067654")))
K("linguine_moules_scarole", "Linguine aux moules et à la scarole", "Linguine cozze e scarola", CAMP, "P", 2, 4, 25, 15, "€€", "Grande sauteuse avec couvercle.",
  "Un mariage napolitain : les moules ouvertes à l'ail, leur jus filtré, la scarole fondue avec câpres et olives, et les linguine finies dans ce bouillon iodé.",
  ["350 g|de linguine|Pâtes sèches (spaghetti, penne…)|3", "1 kg|de moules|Moules|3", "1/2|scarole (ou frisée)|Chicorée / frisée|2", f"3|gousses d'ail|{AIL}|1", "1 c. à s.|de câpres|Câpres|1", "10|olives noires|Olives (vertes / noires)|1", f"1|piment|{PEP}|1?", f"5 c. à s.|d'huile d'olive|{HO}|1", f"1/2|botte de persil|{PERSIL}|1"],
  ["**Moules.** Grattées, celles qui restent ouvertes jetées ; sauteuse, 2 c. à s. d'huile, ail, couvercle, 4 min : ouvertes ; décortiquées (quelques-unes gardées entières), jus filtré.",
   "**Scarole.** Reste d'huile, ail, piment, scarole émincée, câpres, olives, 6 min : fondue.",
   "**Pâtes.** 2 min de moins ; finies dans la scarole avec le jus des moules, 2 min : il est absorbé.",
   "**Servir.** Moules, persil, poivre."],
  tips=["Mollusques : allergène ; moules restées fermées après cuisson : on les jette."], keep="À manger tout de suite.", age=3, cats=[], profil=["poisson", "acide"],
  credit=C(V(MM, "7249708134904663323")))
K("pasta_burro_alici", "Pâtes au beurre et aux anchois", "Pasta burro e alici", IT, "P", 1, 4, 5, 12, "€", "Casserole, petite poêle.",
  "Trois ingrédients et beaucoup de goût : des anchois fondus dans le beurre jusqu'à disparaître, liés aux pâtes avec l'eau de cuisson, une pointe de citron et de la chapelure dorée pour croquer.",
  [f"350 g|de spaghetti|{PATES}|3", "10|filets d'anchois à l'huile|Anchois (filets, conserve)|3", f"80 g|de beurre|{BEURRE}|3", "4 c. à s.|de chapelure|Chapelure|1", f"1|citron (zeste)|{CIT}|1", f"1/2|botte de persil|{PERSIL}|1?"],
  ["**Chapelure.** 10 g de beurre, chapelure, 3 min : dorée ; réservée.",
   "**Anchois.** Reste du beurre, anchois, feu doux 3 min en écrasant : ils fondent.",
   "**Pâtes.** Eau peu salée (les anchois le sont) ; dans le beurre d'anchois avec 10 cl d'eau de cuisson, 1 min : brillantes.",
   "**Finir.** Zeste, poivre, persil, chapelure au moment de manger."],
  tips=["Poisson : allergène."], keep="À manger tout de suite.", age=3, cats=["express"], profil=["poisson", "gras"],
  credit=C(V(MM, "7188478738886151430")))
K("rigatoni_brocoli_saucisse", "Rigatoni brocoli et saucisse (version saucisse de volaille)", "Rigatoni broccoli e salsiccia", CAMP, "P", 1, 4, 15, 20, "€", "Grande sauteuse, casserole.",
  "Un grand classique du sud : du brocoli cuit avec les pâtes puis écrasé à l'ail et au piment, la chair de saucisse émiettée et dorée, du pecorino. Ici avec une saucisse de volaille ou de veau.",
  [f"350 g|de rigatoni|{PATES}|3", "400 g|de brocoli|Brocoli|3", "300 g|de saucisses de volaille ou de veau|Saucisse de bœuf / de veau / de volaille|3", f"2|gousses d'ail|{AIL}|1", f"1 pincée|de flocons de piment|{FLOC}|1?", f"40 g|de pecorino|{PECO}|1", f"4 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Saucisse.** Chair sortie du boyau, émiettée, huile, 6 min : bien dorée.",
   "**Brocoli.** En bouquets, dans l'eau bouillante salée 5 min, puis les pâtes dans la même eau.",
   "**Ail.** Dans la sauteuse avec la saucisse, piment, 1 min ; brocoli égoutté, écrasé à la cuillère.",
   "**Lier.** Pâtes al dente, une louche d'eau de cuisson, 2 min : crémeux ; pecorino."],
  keep="1 jour au frigo.", age=2, cats=["enfants"], profil=["gras"],
  credit=C(V(MM, "7176597876804570373")))
K("paccheri_crevettes_tomates_cerises", "Paccheri crémeux aux crevettes et tomates cerises", "Paccheri gamberi e pomodorini", CAMP, "P", 1, 4, 20, 20, "€€", "Grande sauteuse, mixeur plongeant.",
  "De gros tubes de pâtes dans une sauce crémeuse sans crème : les têtes et carapaces des crevettes rissolées en fumet, une partie des tomates cerises mixée, les crevettes ajoutées à la fin.",
  ["350 g|de paccheri|Pâtes sèches (spaghetti, penne…)|3", "400 g|de crevettes crues entières|Crevettes (cuites/crues)|3", "400 g|de tomates cerises|Tomate|3", f"2|gousses d'ail|{AIL}|1", f"1|piment|{PEP}|1?", f"5 c. à s.|d'huile d'olive|{HO}|1", "1|bouquet de basilic|Basilic|1"],
  ["**Fumet.** Crevettes décortiquées ; têtes et carapaces dans 2 c. à s. d'huile, 3 min en écrasant, 30 cl d'eau, 10 min ; filtré.",
   "**Sauce.** Huile, ail, piment, tomates coupées, 8 min ; la moitié mixée avec un peu de fumet, remise : sauce rose, crémeuse.",
   "**Pâtes.** 3 min de moins ; finies dans la sauce avec le fumet, 3 min.",
   "**Crevettes.** 2 min à la fin : roses ; basilic, filet d'huile."],
  tips=["Crustacés : allergène majeur."], keep="À manger tout de suite.", age=3, cats=[], profil=["poisson", "acide"],
  credit=C(V(GZ, "7171809666366819589")))
K("ravioli_courge_gorgonzola", "Raviolis à la courge, gorgonzola et noix (pâte fraîche maison)", "Ravioli zucca e gorgonzola", "Europe du Sud › Italie › Lombardie", "P", 3, 4, 60, 40, "€€", "Rouleau ou machine à pâtes, four, poêle.",
  "Une pâte fraîche aux œufs fourrée de courge rôtie, de parmesan et d'une pointe de muscade, servie avec une sauce au gorgonzola fondu dans le beurre et des noix grillées.",
  [f"300 g|de farine (T45 ou semoule fine)|{F45}|3", f"3|œufs|{OEUF}|2", "600 g|de courge butternut|Butternut / courge musquée|3", f"40 g|de parmesan|{PARM}|1", f"1 pincée|de muscade|{MUSC}|0", "120 g|de gorgonzola|Roquefort / bleu|2", f"40 g|de beurre|{BEURRE}|1", "50 g|de cerneaux de noix|Noix|1", "4|feuilles de sauge|-|1?"],
  ["**Farce.** Courge en cubes, 30 min à 200 °C : fondante ; écrasée sèche avec parmesan, muscade, sel ; refroidie.",
   "**Pâte.** Farine, œufs : 10 min, lisse ; 30 min filmée ; étalée en bandes fines (on voit la main au travers).",
   "**Raviolis.** Noisettes de farce tous les 5 cm, bord mouillé, deuxième bande, air chassé autour de la farce, découpés.",
   "**Cuire.** 4 min à l'eau salée frémissante ; poêle : beurre, sauge, gorgonzola, 5 c. à s. d'eau de cuisson : fondu ; raviolis, noix grillées."],
  tips=["Fruits à coque (noix) : allergène.", "Femme enceinte : gorgonzola au lait pasteurisé, bien chaud."], keep="Crus : 1 mois au congélateur (cuits sans décongeler).", age=2, cats=["vegetarien"], fetes=["Repas de famille"], profil=["gras", "sucre"],
  credit=C(V(GZ, "7192922317670993158")))

# ---------- Viandes, abats, poisson ----------
K("trippa_romana", "Trippa alla romana (tripes à la tomate, menthe et pecorino)", "Trippa alla romana", LAZ, "P", 2, 4, 25, 90, "€", "Cocotte.",
  "Les tripes du samedi à Rome : du gras-double précuit, mijoté longuement dans une sauce tomate au céleri et à la carotte, fini avec de la menthe fraîche (la mentuccia) et beaucoup de pecorino.",
  ["1 kg|de tripes de bœuf précuites (gras-double)|Tripes / gras-double de bœuf|3", "700 g|de tomates pelées|Coulis / passata / tomates pelées|3", f"1|oignon|{OIG}|1", f"1|carotte|{CAROTTE}|1", "1|branche de céleri|Céleri-branche|1", "1|bouquet de menthe|Menthe|2", f"60 g|de pecorino|{PECO}|2", f"4 c. à s.|d'huile d'olive|{HO}|1", f"1|piment|{PEP}|1?"],
  ["**Blanchir.** Tripes rincées, 10 min à l'eau bouillante ; en lanières de 1 cm.",
   "**Soffritto.** Huile, oignon, carotte, céleri hachés, 8 min : fondants.",
   "**Mijoter.** Tripes, tomates, piment, sel, 20 cl d'eau ; 1 h 15 à couvert, feu doux : tendres, sauce épaisse.",
   "**Finir.** Hors du feu : menthe ciselée, la moitié du pecorino ; le reste à table."],
  keep="3 jours au frigo, meilleure réchauffée ; se congèle.", age=3, cats=[], profil=["viande_rouge", "acide"],
  credit=C(V(MM, "7178092823575579909")))
K("filet_poivre_vert", "Filet de bœuf au poivre vert", "Filetto al pepe verde", IT, "P", 2, 2, 10, 15, "€€€", "Poêle à fond épais.",
  "Le classique des trattorias : deux pavés de filet saisis, puis une sauce montée dans la poêle avec le poivre vert en saumure, un peu de fond et de crème. Sans alcool ici.",
  ["2|tournedos de filet de bœuf (180 g), ou de rumsteck épais|Rumsteck|3", "1 c. à s.|de poivre vert en saumure|Poivre noir / blanc / vert|2", f"15 cl|de crème|{CL}|2", f"10 cl|de bouillon de bœuf|{BOUILLON}|1", f"20 g|de beurre|{BEURRE}|1", f"1 c. à s.|d'huile|{HN}|1", f"1 c. à c.|de moutarde|{DIJON}|1"],
  ["**Tempérer.** Viande sortie 30 min avant, épongée, salée.",
   "**Saisir.** Poêle fumante, huile, 2 min 30 par face, beurre en fin pour arroser : croûte brune, saignant (52 °C) ; 5 min sous aluminium.",
   "**Sauce.** Dans la même poêle : poivre vert égoutté écrasé à moitié, bouillon (gratte les sucs), 2 min ; crème, moutarde, 3 min : nappante.",
   "**Servir.** Jus de repos dans la sauce, viande nappée."],
  keep="Le jour même.", age=3, cats=[], fetes=["Saint-Valentin"], profil=["viande_rouge", "gras"],
  credit=C(V(MM, "7221939730575887622")))
K("alici_marinate", "Alici marinate (anchois frais marinés au citron)", "Alici marinate", CAMP, "E", 2, 4, 40, 720, "€", "Plat en verre, film.",
  "L'antipasto des côtes italiennes : des filets d'anchois frais « cuits » dans le jus de citron jusqu'à blanchir, puis servis à l'huile d'olive avec ail, persil et piment. La congélation préalable est indispensable.",
  ["500 g|d'anchois frais (ou petites sardines), congelés 7 jours avant|Anchois (filets, conserve)|3", f"4|citrons|{CIT}|3", f"10 cl|d'huile d'olive|{HO}|2", f"2|gousses d'ail|{AIL}|1", f"1/2|botte de persil|{PERSIL}|1", f"1|piment|{PEP}|1?"],
  ["**Sécurité.** Poisson congelé au moins 7 jours à -20 °C (ou acheté « déjà congelé »), décongelé au frigo : élimine le parasite anisakis.",
   "**Lever.** Tête et arête centrale retirées au doigt, filets ouverts en livre, rincés, épongés.",
   "**Mariner.** À plat, couverts de jus de citron, 6 à 12 h au frigo : chair blanche et opaque.",
   "**Assaisonner.** Égouttés, huile, ail émincé, persil, piment ; 1 h avant de servir."],
  tips=["Poisson cru : pas pour les femmes enceintes, les enfants de moins de 6 ans ni les personnes fragiles.", "Poisson : allergène."], keep="2 jours au frigo, couverts d'huile.", age=None, cats=[], fetes=["Apéritif dînatoire"], profil=["poisson", "acide"], kids="Poisson cru : pour les adultes.",
  credit=C(V(MM, "7179154519396273413")))
K("polpo_lesso_salade", "Salade de poulpe et pommes de terre (polpo lesso)", "Insalata di polpo e patate", IT, "P", 2, 4, 20, 60, "€€", "Grande marmite, saladier.",
  "Le poulpe cuit doucement dans son eau jusqu'à être fondant, coupé tiède et mêlé à des pommes de terre, du persil, de l'ail, du citron et de l'huile d'olive. Tiède ou froid.",
  ["1,2 kg|de poulpe (décongelé : plus tendre)|Poulpe / seiche|3", f"600 g|de pommes de terre|{PDT}|3", f"2|citrons|{CIT}|2", f"8 c. à s.|d'huile d'olive|{HO}|2", f"1|gousse d'ail|{AIL}|1", f"1/2|botte de persil|{PERSIL}|1", "1 c. à s.|de câpres|Câpres|1?", f"1|feuille de laurier|{LAURIER}|0"],
  ["**Cuire.** Eau bouillante non salée, laurier ; tentacules trempés 3 fois pour les friser, puis le poulpe entier ; feu doux 45 à 60 min : une fourchette entre sans résistance. Refroidit 20 min dans l'eau.",
   "**Pommes de terre.** En robe des champs, 20 min ; pelées, en morceaux.",
   "**Couper.** Poulpe en tronçons de 2 cm (peau gélatineuse gardée ou non).",
   "**Assaisonner.** Tiède : jus de citron, huile, ail haché, persil, câpres, sel, poivre."],
  tips=["Mollusques : allergène."], keep="2 jours au frigo.", age=3, cats=["leger"], profil=["poisson", "acide", "leger"],
  credit=C(V(MM, "7153292329690926342")))
K("impepata_cozze", "Impepata di cozze (moules au poivre, Naples)", "Impepata di cozze", CAMP, "E", 1, 4, 15, 8, "€€", "Grande cocotte avec couvercle.",
  "L'antipasto napolitain du réveillon : des moules ouvertes à feu vif avec ail, huile et une quantité généreuse de poivre noir, citron et persil, et du pain grillé pour le jus.",
  ["1,5 kg|de moules|Moules|3", f"3|gousses d'ail|{AIL}|1", f"2 c. à c.|de poivre noir concassé|{POIVRE}|2", f"4 c. à s.|d'huile d'olive|{HO}|1", f"2|citrons|{CIT}|2", f"1/2|botte de persil|{PERSIL}|1", "1|pain de campagne|Pain de campagne / complet|1"],
  ["**Moules.** Grattées, ébarbées, rincées ; ouvertes qui ne se ferment pas au toucher : jetées.",
   "**Ouvrir.** Cocotte, huile, ail, 1 min ; moules, couvercle, feu vif 4 à 5 min en secouant : toutes ouvertes.",
   "**Poivrer.** Poivre, jus d'un citron, persil ; 30 s en remuant.",
   "**Servir.** Avec le jus, quartiers de citron, pain grillé."],
  tips=["Mollusques : allergène ; moules restées fermées : on les jette."], keep="À manger tout de suite.", age=3, cats=["express"], fetes=["Noël", "Apéritif dînatoire"], profil=["poisson", "acide", "epice"],
  credit=C(V(GZ, "7180315728069840134")))

# ---------- Mozzarella, œufs, street food ----------
K("mozzarella_in_carrozza", "Mozzarella in carrozza, tomate et basilic (le sandwich caprese croustillant)", "Mozzarella in carrozza", CAMP, "P", 1, 2, 15, 8, "€", "Poêle.",
  "Le croque napolitain : de la mozzarella bien égouttée entre deux tranches de pain de mie, trempé dans l'œuf battu, pané et doré à la poêle ; ici avec tomate et basilic, comme une caprese croustillante.",
  ["4|tranches de pain de mie|Pain de mie|3", "200 g|de mozzarella (bien égouttée)|Mozzarella / burrata|3", f"1|tomate|{TOMC}|1", f"2|œufs|{OEUF}|2", f"3 c. à s.|de lait|{LAIT}|1", "4 c. à s.|de chapelure|Chapelure|1", f"2 c. à s.|de farine|{F55}|1", "6|feuilles de basilic|Basilic|1", f"10 cl|d'huile|{HN}|1"],
  ["**Égoutter.** Mozzarella en tranches, 30 min sur papier absorbant (sinon elle détrempe le pain).",
   "**Monter.** Pain, mozzarella, tomate en tranches fines épongées, basilic, sel, pain ; bords pressés.",
   "**Paner.** Farine sur les bords, œufs battus avec le lait (1 min de trempage par face), chapelure.",
   "**Dorer.** Poêle, 5 mm d'huile, feu moyen, 3 min par face : doré, cœur filant."],
  keep="À manger tout de suite.", age=2, cats=["vegetarien", "express", "enfants"], profil=["gras"],
  credit=C(V(MM, "7310663590455905569")))
K("panzerotti", "Panzerotti (chaussons frits tomate-mozzarella des Pouilles)", "Panzerotti", "Europe du Sud › Italie › Pouilles", "P", 2, 8, 40, 120, "€", "Casserole à friture, rouleau.",
  "Les chaussons de Bari : une pâte à pizza étalée en disques, garnie de tomate et de mozzarella, fermée en demi-lune et frite. Dehors croustillant et gonflé, dedans brûlant et filant.",
  [f"500 g|de farine T55|{F55}|3", f"5 g|de levure boulangère sèche|{LEV}|1", f"30 cl|d'eau tiède|-|0", f"2 c. à s.|d'huile d'olive|{HO}|1", "250 g|de mozzarella|Mozzarella / burrata|3", "250 g|de tomates pelées|Coulis / passata / tomates pelées|2", "1 c. à c.|d'origan|-|1", "1 L|d'huile de friture|Huile d'arachide|2"],
  ["**Pâte.** Farine, levure, eau, huile, sel : 10 min, souple ; 1 h 30 : doublée.",
   "**Garniture.** Tomates égouttées écrasées, origan, sel ; mozzarella en dés épongés.",
   "**Former.** 8 boules étalées en disques de 15 cm ; garniture sur une moitié (sans trop), bord mouillé, refermé, pressé à la fourchette.",
   "**Frire.** 175 °C, 2 min par face : gonflés et dorés ; 3 min avant de mordre (garniture brûlante)."],
  tips=["Huile chaude : loin des enfants ; garniture très chaude, attendre avant de donner aux petits."], keep="Crus : 1 mois au congélateur.", age=3, cats=["vegetarien", "enfants"], fetes=["Anniversaire"], profil=["gras"],
  credit=C(V(GZ, "6917202968811015426")))
K("mozzarella_in_purgatorio", "Mozzarella in purgatorio (mozzarella fondue dans la sauce tomate)", "Mozzarella in purgatorio", CAMP, "P", 1, 2, 5, 15, "€", "Petite poêle avec couvercle.",
  "La mozzarella posée dans une sauce tomate à l'ail et au basilic, couverte jusqu'à fondre et filer : à manger dans la poêle avec du pain grillé.",
  ["250 g|de mozzarella|Mozzarella / burrata|3", "400 g|de tomates pelées|Coulis / passata / tomates pelées|3", f"1|gousse d'ail|{AIL}|1", "1|bouquet de basilic|Basilic|1", f"3 c. à s.|d'huile d'olive|{HO}|1", "1 pincée|de flocons de piment|Flocons de piment|1?", "1|pain de campagne|Pain de campagne / complet|2"],
  ["**Sauce.** Huile, ail, 1 min ; tomates écrasées, sel, basilic, 10 min : réduite.",
   "**Mozzarella.** En grosses tranches posées dans la sauce, couvercle, 4 min à feu doux : fondue, filante.",
   "**Assaisonner.** Basilic, poivre, piment, filet d'huile.",
   "**Servir.** Dans la poêle, pain grillé."],
  keep="À manger tout de suite.", age=1, cats=["vegetarien", "express", "enfants"], profil=["acide", "gras"],
  credit=C(V(CF, "7379579768804625696")))
K("uova_in_purgatorio", "Uova in purgatorio (œufs pochés dans la sauce tomate)", "Uova in purgatorio", CAMP, "P", 1, 2, 5, 20, "€", "Poêle avec couvercle.",
  "Les œufs « au purgatoire » de Naples : pochés dans une sauce tomate à l'ail et au basilic, le blanc pris, le jaune coulant ; avec du pain pour saucer.",
  [f"4|œufs|{OEUF}|3", "400 g|de tomates pelées|Coulis / passata / tomates pelées|3", f"1|gousse d'ail|{AIL}|1", "1|bouquet de basilic|Basilic|1", f"3 c. à s.|d'huile d'olive|{HO}|1", f"20 g|de parmesan|{PARM}|1?", "1 pincée|de flocons de piment|Flocons de piment|1?", "1|pain de campagne|Pain de campagne / complet|2"],
  ["**Sauce.** Huile, ail, 1 min ; tomates, sel, basilic, 10 min : épaissie.",
   "**Creuser.** 4 puits à la cuillère, un œuf dans chacun.",
   "**Pocher.** Couvercle, feu doux, 5 à 6 min : blanc pris, jaune encore tremblant.",
   "**Servir.** Parmesan, basilic, poivre ; pain."],
  tips=["Femme enceinte, jeunes enfants : laisse les jaunes cuire 2 min de plus, bien pris."], keep="À manger tout de suite.", age=1, cats=["vegetarien", "express", "brunch", "enfants"], profil=["acide"], kids="✓ dès 1 an, jaune bien cuit.",
  credit=C(V("latavoladigael", "7426059856005647648")))
