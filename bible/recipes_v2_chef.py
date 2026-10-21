# -*- coding: utf-8 -*-
"""Vague 2 · Cahier du chef : viandes, volailles, poissons, fruits de mer et œufs, pour pratiquer les cuissons."""
from recipes_v2_base import *

FR = "France › Cuisine de chef"

K("cote_boeuf", "Côte de bœuf, beurre maître d'hôtel", "Côte de bœuf", FR, "P", 2, 4, 15, 40, "€€€", "Poêle en fonte, four, thermomètre sonde.",
  "Une pièce épaisse saisie puis finie au four jusqu'à la cuisson voulue, reposée, tranchée : la leçon de cuisson de la viande rouge.",
  ["1|côte de bœuf de 1,2 kg (5 cm d'épaisseur)|Côte de bœuf|3", f"40 g|de beurre|{BEURRE}|2", f"4 gousses|d'ail|{AIL}|1", f"4 branches|de thym|{THYM}|1", "1 c. à s.|de fleur de sel|Sel fin / gros sel / fleur de sel|1", f"1 c. à c.|de poivre concassé|{POIVRE}|1", "1 rondelle par personne|de beurre maître d'hôtel|SUB:beurre_maitre_hotel|1"],
  ["**Tempérer.** Sors-la 1 h avant, sèche-la ; sale juste avant.", "**Saisir.** Poêle fumante, 3 min par face et sur le gras ; beurre, ail, thym, arrose 2 min.",
   "**Four.** 150 °C jusqu'à 48 °C à cœur pour saignant (20-25 min), 53 °C pour à point.", "**Repos.** 15 min sous aluminium : la température monte de 4 °C. Tranche contre les fibres, fleur de sel, poivre, beurre."],
  keep="Restes : 2 jours au frigo ; froids en salade ou en sandwich.", age=None, kids="✓ dès 3 ans, tranches bien cuites aux extrémités.", fetes=["Barbecue d'été", "Repas de famille"], profil=["viande_rouge"], tech=["Cuisson de la viande", "Arroser", "Repos de la viande"])

K("poulet_crapaudine", "Poulet en crapaudine au citron et à l'ail", "Poulet en crapaudine", FR, "P", 2, 4, 20, 45, "€€", "Ciseaux à volaille, plaque, four.",
  "Le poulet ouvert à plat cuit deux fois plus vite et uniformément : peau croustillante partout, chair juteuse.",
  ["1|poulet de 1,6 kg|Poulet entier|3", f"2|citrons|{CIT}|2", f"6 gousses|d'ail|{AIL}|2", f"4 branches|de thym|{THYM}|1", f"3 c. à s.|d'huile d'olive|{HO}|1", f"1 c. à s.|de gros sel|{SEL}|0"],
  ["**Ouvrir.** Coupe de part et d'autre de la colonne aux ciseaux (garde-la pour le bouillon), aplatis en appuyant sur le bréchet.", "**Assaisonner.** Sel sous la peau et dessus, huile, citron, ail, thym.", "**Cuire.** Peau dessus, 45 min à 220 °C : 74 °C dans la cuisse. Repos 10 min."],
  age=1, cats=["enfants"], fetes=["Barbecue d'été"], profil=["leger"], tech=["Découper un poulet", "Rôtir"])

K("poulet_basse_temp", "Suprêmes de volaille basse température, jus réduit", "Suprême de volaille", FR, "P", 2, 4, 15, 75, "€€", "Four, thermomètre sonde, poêle.",
  "Des blancs de poulet juteux comme jamais : saisis côté peau, cuits doucement au four jusqu'à 74 °C pile, jus déglacé.",
  [f"4|suprêmes de poulet avec peau|{BLANC_P}|3", f"30 g|de beurre|{BEURRE}|2", f"20 cl|de bouillon de volaille|{BOUILLON}|2", f"2 branches|de thym|{THYM}|1", f"1|échalote|{ECH}|1"],
  ["**Saumure.** 1 h dans 1 L d'eau + 60 g de sel + 30 g de sucre (facultatif mais spectaculaire).", "**Saisir.** Côté peau, 5 min jusqu'à doré croustillant.", "**Four.** Côté peau dessus, 100 °C jusqu'à 74 °C à cœur (45-60 min).", "**Jus.** Échalote dans la poêle, bouillon, gratte, réduis ; beurre froid."],
  age=1, cats=["enfants"], profil=["leger"], tech=["Saumure", "Basse température", "Déglacer"])

K("bar_croute_sel", "Bar en croûte de sel", "Loup en croûte de sel", FR, "P", 1, 4, 15, 30, "€€€", "Plat à four, maillet.",
  "Le poisson entier cuit à l'étouffée dans une coque de sel : chair nacrée, juteuse, jamais trop salée.",
  ["1|bar de 1,2 kg vidé, non écaillé|Bar / loup|3", "2 kg|de gros sel|Sel fin / gros sel / fleur de sel|2", "2|blancs d'œufs|Blanc d'œuf|1", f"1|citron|{CIT}|1", "1 bouquet|de fenouil ou aneth|Fenouil|1", f"5 cl|d'huile d'olive|{HO}|1"],
  ["**Sel.** Gros sel + blancs + un peu d'eau : sable mouillé.", "**Enfermer.** Couche de sel, poisson farci de citron et herbes, couvre entièrement en tassant.", "**Cuire.** 30 min à 220 °C (10 min de plus par 500 g ; 55 °C à cœur).", "**Ouvrir.** Casse la croûte à table, lève la peau, filets ; huile d'olive."],
  age=1, fetes=["Repas de famille", "Noël"], profil=["poisson"], tech=["Cuisson du poisson", "Lever les filets"])

K("saumon_peau_croustillante", "Pavé de saumon peau croustillante, sauce vierge", "Saumon unilatéral", FR, "P", 1, 4, 10, 10, "€€", "Poêle anti-adhésive ou acier.",
  "Peau craquante comme une chips, chair nacrée : la cuisson unilatérale côté peau.",
  ["4|pavés de saumon avec peau, écaillés|Saumon (frais, pavé)|3", "1|recette de sauce vierge|SUB:sauce_vierge|2", f"1 c. à s.|d'huile|{HN}|1", "1 pincée|de fleur de sel|Sel fin / gros sel / fleur de sel|0"],
  ["**Préparer.** Peau séchée et salée, 10 min ; chair à température.", "**Cuire.** Poêle chaude huilée, côté peau, presse 20 s ; feu moyen 6-8 min jusqu'à ce que la chair soit opaque aux ⅔.", "**Finir.** Retourne 30 s (ou pas). Peau dessus, sauce vierge à côté."],
  age=1, cats=["enfants"], profil=["poisson"], tech=["Cuisson du poisson", "Côté peau"])

K("cabillaud_papillote", "Cabillaud en papillote, légumes et citron", "Papillote de cabillaud", FR, "P", 1, 4, 15, 15, "€€", "Papier cuisson, plaque.",
  "Cuisson douce à la vapeur dans sa papillote : le poisson garde son jus, les légumes leur couleur. Zéro vaisselle.",
  ["4|dos de cabillaud|Cabillaud / morue fraîche|3", "2|courgettes en julienne|Courgette|2", f"2|carottes en julienne|{CAROTTE}|1", f"1|citron|{CIT}|2", "1 bouquet|d'aneth ou de basilic|Aneth|1", f"4 c. à s.|d'huile d'olive|{HO}|1", f"4 c. à s.|de vin blanc ou d'eau|-|0"],
  ["**Monter.** Feuille de papier, légumes, poisson salé, rondelle de citron, herbes, huile, liquide.", "**Fermer.** En demi-lune, bord roulé serré.", "**Cuire.** 12-15 min à 200 °C : elle gonfle. On l'ouvre à table."],
  age=1, cats=["enfants"], profil=["poisson", "leger"], tech=["Papillote"])

K("saint_jacques_poelees", "Saint-Jacques poêlées, purée de panais", "Noix de Saint-Jacques poêlées", FR, "P", 2, 4, 25, 25, "€€€", "Poêle, casserole, mixeur.",
  "Noix saisies 1 minute par face, croûte dorée et cœur translucide, sur une purée de panais douce et sucrée.",
  ["16|noix de Saint-Jacques|Coquilles Saint-Jacques|3", "600 g|de panais|Panais / rutabaga|3", f"20 cl|de lait|{LAIT}|1", f"40 g|de beurre|{BEURRE}|2", f"½|citron|{CIT}|1", f"1 c. à s.|d'huile|{HN}|1"],
  ["**Purée.** Panais cuits dans le lait salé, mixés avec 20 g de beurre.", "**Noix.** Sèches, salées au dernier moment ; poêle fumante, 1 min 30 par face sans les toucher ; beurre, arrose 20 s.", "**Servir.** Sur la purée, citron."],
  age=3, fetes=["Noël", "Saint-Valentin"], profil=["poisson", "gras"], tech=["Saint-Jacques"])

K("dorade_four", "Dorade au four, fenouil et olives", "Dorade rôtie", "Europe du Sud › Grèce", "P", 1, 4, 15, 30, "€€", "Plat à four.",
  "Dorades entières sur un lit de fenouil, tomates cerises et olives, rôties : simple, parfumé, festif.",
  ["2|dorades de 500 g vidées, écaillées|Dorade|3", "2|bulbes de fenouil|Fenouil|2", "250 g|de tomates cerises|Tomate cerise|1", "16|olives|Olives (vertes / noires)|1", f"1|citron|{CIT}|1", "1 c. à c.|d'origan|Origan frais / sec|1", f"5 c. à s.|d'huile d'olive|{HO}|2"],
  ["**Lit.** Fenouil émincé, huile, sel, 10 min à 200 °C.", "**Poisson.** Entaillé, salé, citron et herbes dans le ventre, posé dessus avec tomates et olives.", "**Cuire.** 20-25 min : l'arête dorsale se détache."],
  age=1, profil=["poisson"], tech=["Cuisson du poisson"])

K("maquereaux_grilles", "Maquereaux grillés, moutarde et citron", "Maquereaux grillés", "France › Bretagne", "P", 1, 4, 10, 10, "€", "Gril ou poêle.",
  "Le poisson bleu le moins cher, riche en oméga-3, grillé à la peau croustillante avec une sauce moutarde : simple et bon.",
  ["4|maquereaux en filets|Maquereau|3", f"2 c. à s.|de moutarde à l'ancienne|Moutarde à l'ancienne|2", f"1|citron|{CIT}|2", f"2 c. à s.|d'huile|{HN}|1", f"1 c. à s.|de persil|{PERSIL}|0"],
  ["**Griller.** Filets côté peau, 3-4 min ; retourne 30 s.", "**Sauce.** Moutarde, citron, huile, persil."],
  age=1, cats=["zero_dechet"], profil=["poisson"], tech=["Cuisson du poisson"])

K("tataki_thon", "Tataki de thon au sésame", "Maguro tataki", "Asie de l'Est › Japon", "E", 1, 4, 15, 5, "€€€", "Poêle très chaude.",
  "Un pavé de thon saisi 30 secondes par face, cru au centre, en croûte de sésame, avec une sauce ponzu.",
  ["400 g|de thon albacore extra-frais en pavé|Thon (frais)|3", "4 c. à s.|de sésame blanc et noir|Sésame (blanc/noir)|2", f"4 c. à s.|de sauce soja|{SOJA}|2", f"1|citron vert|{CITV}|1", f"1 c. à c.|de gingembre râpé|{GING}|1", "2|oignons nouveaux|Oignon nouveau / cébette|1"],
  ["**Enrober.** Thon huilé roulé dans le sésame.", "**Saisir.** 30 s par face, poêle fumante. Eau glacée 10 s, sèche.", "**Trancher.** 1 cm ; sauce soja-citron vert-gingembre, oignons."],
  tips=["⚠️ Centre cru : thon extra-frais ou congelé ; déconseillé femmes enceintes et jeunes enfants."], age=None, profil=["poisson"], tech=["Cuisson du poisson"])

K("bisque_crevettes", "Bisque express de crevettes (avec les carapaces)", "Bisque de crevettes", FR, "So", 2, 4, 20, 30, "€€", "Casserole, mixeur, chinois.",
  "Une bisque crémeuse faite avec les têtes et carapaces qu'on jette d'habitude : le goût de la mer, zéro déchet.",
  ["500 g|de têtes et carapaces de crevettes|Crevettes (cuites/crues)|3", f"1|carotte + 1 échalote|{CAROTTE}|1", f"2 c. à s.|de concentré|{CONC}|2", f"2|tomates|{TOM}|1", f"15 cl|de crème|{CF}|2", f"1 c. à s.|de riz (pour lier)|{RIZ}|1", f"2 c. à s.|d'huile d'olive|{HO}|1", f"1 pincée|de piment d'Espelette|Piment d'Espelette|1"],
  ["**Rôtir.** Carapaces dans l'huile très chaude 5 min en écrasant ; légumes, concentré.", "**Cuire.** 1 L d'eau, riz, tomates, 25 min.", "**Mixer.** Tout, filtre en pressant ; crème, Espelette."],
  age=3, cats=["zero_dechet"], profil=["poisson", "gras"], tech=["Crevettes", "Fumet"])

K("calamars_romana", "Calamars à la romaine", "Calamari fritti", "Europe du Sud › Italie", "E", 1, 4, 15, 10, "€€", "Casserole profonde, thermomètre.",
  "Anneaux de calamar en friture légère, tendres et croustillants, avec citron et sauce tartare.",
  ["600 g|de calamars en anneaux|Calamar / encornet|3", f"100 g|de farine + 50 g de semoule fine|{F55}|2", "1 L|d'huile|Huile d'arachide|1", f"1|citron|{CIT}|1", "1|recette de sauce tartare|SUB:sauce_tartare|1"],
  ["**Sécher.** Calamars bien épongés.", "**Fariner.** Farine + semoule, secoue l'excès.", "**Frire.** 1 min 30 à 180 °C, petites quantités. Sel, citron."],
  age=3, cats=["enfants"], fetes=["Apéritif dînatoire"], profil=["poisson", "gras"], tech=["Calamar", "Frire"])

K("oeufs_benedicte", "Œufs Bénédicte (saumon fumé ou dinde)", "Eggs Benedict", f"{FR}", "P", 2, 2, 20, 10, "€€", "Casserole, bol, grille-pain.",
  "Muffin toasté, saumon fumé, œuf poché coulant et sauce hollandaise : le brunch par excellence.",
  [f"4|œufs très frais|{OEUF}|3", "2|muffins anglais (ou tranches de brioche)|Brioche|2", "4 tranches|de saumon fumé ou de jambon de dinde|Saumon fumé|2", "1|recette de sauce hollandaise|SUB:sauce_hollandaise|3", f"1 c. à s.|de vinaigre|Vinaigre blanc|0", "1 c. à s.|de ciboulette|Ciboulette|0"],
  ["**Hollandaise.** Prête, gardée tiède.", "**Pocher.** Eau frémissante vinaigrée, tourbillon, œuf, 3 min.", "**Monter.** Muffin toasté, saumon, œuf, hollandaise, ciboulette."],
  age=None, kids="✓ dès 3 ans avec œufs bien pochés et hollandaise cuite à 70 °C.", profil=["gras"], tech=["Œuf poché", "Émulsionner"])

K("oeufs_cocotte", "Œufs cocotte à la crème et aux champignons", "Œufs en cocotte", FR, "E", 1, 4, 10, 12, "€", "Ramequins, plat à bain-marie.",
  "Un œuf au blanc juste pris et au jaune coulant sur une crème aux champignons, avec des mouillettes.",
  [f"4|œufs|{OEUF}|3", f"10 cl|de crème|{CF}|2", "100 g|de champignons poêlés|Champignon de Paris|2", f"10 g|de beurre|{BEURRE}|1", "1 c. à s.|de ciboulette|Ciboulette|1", f"4 tranches|de pain grillé|Pain de campagne / complet|1"],
  ["**Monter.** Ramequins beurrés, champignons, crème salée, œuf.", "**Cuire.** Bain-marie, 12 min à 180 °C : blanc pris, jaune tremblotant.", "**Servir.** Ciboulette, mouillettes."],
  age=None, kids="✓ dès 1 an, cuit 15 min (jaune pris).", cats=["enfants"], profil=["gras"], tech=["Œuf cocotte"])

K("omelette_fines_herbes", "Omelette baveuse aux fines herbes", "Omelette aux fines herbes", FR, "P", 1, 1, 5, 2, "€", "Poêle 20 cm, spatule.",
  "Trois œufs, du beurre, des herbes : roulée, lisse dehors, crémeuse dedans. La mesure de la maîtrise du feu.",
  [f"3|œufs|{OEUF}|3", f"10 g|de beurre|{BEURRE}|2", "1 c. à s.|de ciboulette, persil, cerfeuil, estragon|Ciboulette|2", f"1 pincée|de sel|{SEL}|0"],
  ["**Battre.** Juste à la fourchette, sel, herbes.", "**Cuire.** Beurre moussant, œufs, remue vivement en secouant 30 s ; laisse prendre 20 s.", "**Rouler.** En inclinant, en trois ; retourne sur l'assiette, couture dessous."],
  age=1, cats=["enfants"], profil=["leger"], tech=["Omelette"], kids="✓ dès 1 an, bien cuite.")

K("oeufs_mimosa", "Œufs mimosa", "Œufs mimosa", FR, "E", 1, 6, 20, 10, "€", "Casserole, tamis.",
  "Des œufs durs garnis de leur jaune à la mayonnaise et saupoudrés de jaune tamisé : l'entrée des repas de famille.",
  [f"6|œufs|{OEUF}|3", f"3 c. à s.|de mayonnaise|SUB:mayonnaise|2", f"1 c. à c.|de moutarde|{DIJON}|1", "1 c. à s.|de ciboulette|Ciboulette|1", f"1 pincée|de paprika|{PAPRIKA}|0"],
  ["**Cuire.** 10 min, eau glacée, écale.", "**Garnir.** Coupe en deux ; jaunes (sauf 2) écrasés avec mayonnaise, moutarde ; remplis les blancs.", "**Mimosa.** 2 jaunes passés au tamis dessus, ciboulette."],
  age=3, cats=["enfants", "fetes"], fetes=["Pâques", "Repas de famille"], profil=["gras"], tech=["Cuisson des œufs"])

K("oeufs_brouilles_cremeux", "Œufs brouillés crémeux sur pain grillé", "Œufs brouillés", FR, "P", 1, 2, 5, 8, "€", "Casserole, spatule.",
  "Cuits très doucement en remuant, ils restent en petits grumeaux soyeux : avec ciboulette, sur une tartine.",
  [f"5|œufs|{OEUF}|3", f"20 g|de beurre froid|{BEURRE}|2", f"1 c. à s.|de crème|{CF}|1", "1 c. à s.|de ciboulette|Ciboulette|1", f"2 tranches|de pain de campagne|Pain de campagne / complet|2"],
  ["**Cuire.** Œufs battus + 10 g de beurre dans une casserole à feu doux, en remuant sans cesse 6-8 min ; hors du feu dès qu'ils sont encore un peu coulants.", "**Arrêter.** Crème et reste de beurre froid, sel, ciboulette. Sur le pain grillé."],
  age=1, cats=["enfants"], profil=["gras"], tech=["Œufs brouillés"])

K("oeuf_parfait_petits_pois", "Œuf parfait, crème de petits pois", "Œuf parfait 64 °C", FR, "E", 2, 4, 15, 50, "€€", "Grande casserole, thermomètre (ou four vapeur).",
  "L'œuf cuit 45 min à 64 °C : blanc et jaune ont la même texture crémeuse. Sur une crème de petits pois et des croûtons.",
  [f"4|œufs extra-frais|{OEUF}|3", "300 g|de petits pois|Petits pois / pois gourmands|3", f"10 cl|de crème|{CF}|1", "4|feuilles de menthe|Menthe|1", "1 tranche|de pain en croûtons|Pain rassis (réservé)|1"],
  ["**Œufs.** Dans l'eau maintenue à 64 °C (thermomètre, ajuste le feu), 45 min.", "**Crème.** Petits pois cuits 5 min, mixés avec crème et menthe.", "**Servir.** Crème, œuf cassé dessus, croûtons, fleur de sel."],
  tips=["⚠️ Œuf peu cuit : déconseillé femmes enceintes, jeunes enfants, personnes âgées fragiles."], age=None, profil=["leger"], tech=["Œuf parfait"])
