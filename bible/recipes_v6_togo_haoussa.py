# -*- coding: utf-8 -*-
"""Vague 9 (suite) · 11/11/2026 : cuisine du Togo et viandes grillées et épices haoussa (nord du Nigeria et Niger), à la
demande du propriétaire. Fiches ATLAS rédigées d'après les recettes de référence (Wikipédia « Togolese cuisine » et
« Hausa cuisine », blogs de cuisine ouest-africaine), réécrites avec les repères ATLAS. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

TG = "Afrique subsaharienne › Togo"
HA = "Afrique subsaharienne › Nigeria"
PALME = "Huile de palme rouge"; FUME = "Poisson fumé / séché"; CREV_S = "Crevettes séchées"; SCOTCH = "Piment scotch bonnet"
FMAIS = "Farine de maïs"; ARA = "Cacahuète / arachide"; CUBE = "Bouillon cube bœuf"; PDO = "Poudre d'ail / d'oignon"

# ---------------- Togo ----------------
K("akoume", "Akoumé (pâte de maïs à la togolaise)", "Akoumé / akplè", TG, "A", 2, 4, 10, 15, "€", "Casserole à fond épais, spatule en bois solide.",
  "La pâte de maïs qu'on mange presque tous les jours au Togo : de la farine de maïs cuite dans l'eau en la travaillant à la spatule jusqu'à une boule lisse et ferme, qu'on prend avec les doigts pour saucer le gboma, l'adémé ou le fétri.",
  [f"400 g|de farine de maïs fine (blanche de préférence)|{FMAIS}|3", "1,2 L|d'eau|-|0", f"1 pincée|de sel|{SEL}|0"],
  ["**Bouillie.** Délaye 100 g de farine dans 40 cl d'eau froide ; porte le reste d'eau salée à ébullition, verse le mélange en remuant : bouillie lisse, 5 min.",
   "**Épaissir.** Ajoute le reste de farine en pluie en tournant énergiquement à la spatule, feu moyen : la pâte se décolle des bords.",
   "**Travailler.** Écrase la pâte contre la paroi et retourne-la 5 min, en ajoutant un peu d'eau chaude si elle reste granuleuse : lisse, ferme, brillante.",
   "**Couvrir.** Couvercle, feu très doux 5 min ; forme des boules avec une louche mouillée, sers chaud."],
  tips=["La spatule doit passer partout au fond : la pâte attache vite et prend un goût de brûlé."], keep="1 jour au frigo filmé ; réchauffée à la vapeur.", age=1, cats=["vegetarien"], profil=[])
K("gboma_dessi", "Gboma dessi (sauce aux épinards, bœuf et poisson fumé)", "Gboma dessi", TG, "P", 2, 6, 30, 60, "€€", "Grande marmite, mixeur.",
  "La sauce verte du Togo : des feuilles de gboma (une morelle) ou des épinards cuits dans une base tomate-oignon-piment à l'huile de palme, avec du bœuf et du poisson fumé. Avec de l'akoumé ou du riz.",
  ["800 g|de bœuf à mijoter (paleron) en cubes|Paleron|3", "1 kg|d'épinards frais (ou feuilles de gboma)|Épinard|3", f"200 g|de poisson fumé|{FUME}|2", f"3|tomates|{TOM}|2", f"2|oignons|{OIG}|2", f"1|piment scotch bonnet|{SCOTCH}|1", f"2 cm|de gingembre|{GING}|1", f"3|gousses d'ail|{AIL}|1", f"10 cl|d'huile de palme rouge|{PALME}|2", f"1|cube de bouillon|{CUBE}|1", f"2 c. à s.|de crevettes séchées moulues|{CREV_S}|1?"],
  ["**Viande.** Bœuf, 1 oignon émincé, ail, gingembre, sel, cube, 50 cl d'eau ; mijote 40 min : tendre, bouillon gardé.",
   "**Base.** Mixe tomates, l'autre oignon et le piment ; huile de palme chauffée sans fumer, purée versée, 15 min à feu moyen : l'huile remonte en surface.",
   "**Assembler.** Viande et bouillon, poisson fumé émietté sans arêtes, crevettes ; 10 min.",
   "**Verdure.** Épinards lavés, hachés grossièrement, pressés ; dans la sauce, 8 à 10 min : vert foncé, fondants. Rectifie le sel."],
  tips=["Huile de palme : ne la laisse pas fumer, elle devient âcre.", "Pour les enfants : piment entier, retiré avant de servir."], keep="3 jours au frigo ; se congèle 3 mois.", age=1, cats=["enfants"], profil=["viande_rouge", "epice"], kids="✓ dès 1 an, piment entier retiré, poisson bien épluché.", side="akoume")
K("ademe_dessi", "Adémé dessi (sauce aux feuilles de corète et au gombo)", "Adémé", TG, "P", 2, 6, 25, 40, "€€", "Marmite, couteau.",
  "La sauce gluante et parfumée des feuilles de corète (adémé, la même plante que la mloukhiya), avec du gombo, du poisson fumé et de la viande. Elle se mange avec l'akoumé, qu'on y trempe.",
  ["500 g|de feuilles de corète (fraîches ou surgelées)|-|3", "300 g|de gombos|Gombo|2", "600 g|de bœuf ou de chèvre en morceaux|Chèvre / cabri|3", f"200 g|de poisson fumé|{FUME}|2", f"2|tomates|{TOM}|1", f"1|oignon|{OIG}|1", f"1|piment scotch bonnet|{SCOTCH}|1", f"8 cl|d'huile de palme rouge|{PALME}|2", f"1|cube de bouillon|{CUBE}|1", "1 pincée|de bicarbonate (facultatif)|-|0?"],
  ["**Viande.** Morceaux, oignon, sel, cube, 60 cl d'eau ; mijote 45 min : tendre.",
   "**Sauce.** Tomates et piment mixés, huile de palme ; dans la viande avec le poisson émietté, 10 min.",
   "**Gombo.** En fines rondelles, 5 min : il épaissit le bouillon.",
   "**Corète.** Feuilles hachées très fin (une pincée de bicarbonate garde le vert), 8 min sans couvrir : sauce verte, filante."],
  tips=["Feuilles de corète : rayon surgelé des épiceries africaines ou orientales (mloukhiya)."], keep="2 jours au frigo.", age=1, cats=[], profil=["viande_rouge", "epice"], kids="✓ dès 1 an, sans piment, viande effilochée.", side="akoume")
K("fetri_dessi", "Fétri dessi (sauce gombo au poisson et aux crevettes)", "Fétri dessi", TG, "P", 2, 6, 25, 35, "€€", "Marmite.",
  "La sauce gombo du Togo et du Bénin : beaucoup de gombos hachés, une base tomate à l'huile de palme, du poisson fumé, des crevettes et souvent du crabe. Filante et parfumée, avec l'akoumé.",
  ["500 g|de gombos|Gombo|3", "400 g|de crevettes crues|Crevettes (cuites/crues)|3", f"250 g|de poisson fumé|{FUME}|2", f"3|tomates|{TOM}|2", f"1|oignon|{OIG}|1", f"1|piment scotch bonnet|{SCOTCH}|1", f"2 cm|de gingembre|{GING}|1", f"8 cl|d'huile de palme rouge|{PALME}|2", f"2 c. à s.|de crevettes séchées moulues|{CREV_S}|1", "1|cube de bouillon de poisson|Bouillon cube volaille|1"],
  ["**Base.** Tomates, oignon, piment, gingembre mixés ; huile de palme, purée, 15 min : l'huile remonte.",
   "**Bouillon.** 50 cl d'eau, cube, crevettes séchées, poisson fumé émietté ; 10 min.",
   "**Gombo.** Haché fin (au couteau ou par impulsions au mixeur), 8 min en remuant : la sauce devient filante.",
   "**Crevettes.** Décortiquées, 3 min : roses ; sel."],
  tips=["Crustacés : allergène majeur."], keep="2 jours au frigo.", age=1, cats=[], profil=["poisson", "epice"], kids="✓ dès 1 an, piment entier retiré.", side="akoume")
K("azi_dessi", "Azi dessi (poulet à la sauce d'arachide, Togo)", "Azi dessi", TG, "P", 1, 6, 20, 55, "€", "Cocotte.",
  "La sauce arachide togolaise : du poulet mijoté dans une sauce tomate liée à la pâte d'arachide, avec piment et gingembre. Plus fluide que le mafé, on la mange avec l'akoumé, le fufu ou du riz.",
  ["1,5 kg|de morceaux de poulet|Cuisse / pilon de poulet|3", "200 g|de pâte d'arachide|Pâte d'arachide|3", f"3|tomates|{TOM}|2", f"2 c. à s.|de concentré|{CONC}|1", f"2|oignons|{OIG}|2", f"1|piment scotch bonnet|{SCOTCH}|1", f"2 cm|de gingembre|{GING}|1", f"3|gousses d'ail|{AIL}|1", f"1|cube de bouillon|{CUBE}|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Dorer.** Poulet salé, huile, 8 min : doré ; oignon émincé, 5 min.",
   "**Sauce.** Tomates, ail, gingembre mixés, concentré ; 10 min. 1 L d'eau, cube, piment entier.",
   "**Lier.** Pâte d'arachide délayée dans une louche de bouillon ; 35 min à feu doux en remuant souvent : l'huile d'arachide perle en surface.",
   "**Servir.** Avec l'akoumé ou du riz."],
  tips=["⚠️ Arachide : allergène majeur.", "Remue souvent : la pâte d'arachide attache au fond."], keep="3 jours au frigo ; se congèle.", age=1, cats=["enfants"], profil=["gras"], kids="✓ dès 1 an (sans allergie à l'arachide), piment retiré.", side="akoume")
K("koklo_meme", "Koklo mémé (poulet grillé à la togolaise, marinade piment-gingembre)", "Koklo mémé", TG, "P", 1, 4, 20, 50, "€", "Four ou barbecue, mixeur.",
  "Le poulet grillé des maquis de Lomé : mariné dans une pâte d'oignon, d'ail, de gingembre et de piment, grillé jusqu'à la peau croustillante, servi avec de l'akoumé, des frites d'igname ou du riz et une sauce tomate pimentée.",
  ["1|poulet en 8 morceaux (ou 1,4 kg de cuisses)|Poulet entier|3", f"1|oignon|{OIG}|2", f"4|gousses d'ail|{AIL}|1", f"4 cm|de gingembre|{GING}|2", f"1|piment scotch bonnet|{SCOTCH}|1", f"1 c. à c.|de thym|{THYM}|1", f"1|cube de bouillon|{CUBE}|1", f"3 c. à s.|d'huile|{HN}|1", f"1|citron|{CIT}|1"],
  ["**Marinade.** Oignon, ail, gingembre, piment, thym, cube émietté, huile mixés ; frotte le poulet incisé, 2 h au frigo (ou une nuit).",
   "**Précuire.** Four 200 °C, 30 min, peau dessus.",
   "**Griller.** Sous le grill ou au barbecue, 10 à 15 min en retournant : peau dorée et croustillante ; jus clair à cœur (75 °C).",
   "**Servir.** Citron, oignon cru émincé, sauce tomate pimentée à part."],
  tips=["Pour les enfants : la marinade sans piment pour leurs morceaux."], keep="2 jours au frigo.", age=1, cats=["enfants"], fetes=["Barbecue d'été"], profil=["epice"], kids="✓ dès 1 an, marinade sans piment, viande effilochée.")
K("djenkoume", "Djenkoumé (pâte rouge de maïs à la tomate)", "Djenkoumé", TG, "P", 2, 4, 20, 30, "€", "Cocotte à fond épais, spatule en bois.",
  "La « pâte rouge » du sud du Togo : la farine de maïs cuite non pas dans l'eau mais dans une sauce tomate-oignon-piment bien relevée, qui lui donne sa couleur et son goût. On la sert avec du poulet frit ou grillé et des oignons crus.",
  [f"300 g|de farine de maïs|{FMAIS}|3", f"4|tomates|{TOM}|2", f"3 c. à s.|de concentré|{CONC}|2", f"2|oignons|{OIG}|2", f"1|piment scotch bonnet|{SCOTCH}|1", f"2 cm|de gingembre|{GING}|1", f"2|gousses d'ail|{AIL}|1", f"8 cl|d'huile|{HN}|1", f"1|cube de bouillon|{CUBE}|1", "4|morceaux de poulet grillé ou frit, pour servir|Cuisse / pilon de poulet|2"],
  ["**Sauce.** Tomates, 1 oignon, piment, ail, gingembre mixés ; huile, l'autre oignon émincé, 3 min ; purée et concentré, 15 min : rouge foncé, l'huile remonte.",
   "**Bouillon.** 90 cl d'eau, cube, sel ; à ébullition.",
   "**Pâte.** Farine en pluie en tournant vivement, feu moyen ; travaille 8 min à la spatule : pâte lisse, rouge, qui se décolle.",
   "**Reposer.** Couvert, feu très doux 5 min ; en boules, avec le poulet et des oignons crus."],
  tips=["La pâte doit être un peu plus molle que l'akoumé : ajoute de l'eau chaude si elle se casse."], keep="1 jour au frigo.", age=2, cats=[], profil=["epice"], kids="✓ dès 2 ans, piment retiré avant de mixer une part.")
K("fufu_igname", "Foufou d'igname (igname pilée)", "Fufu", TG, "A", 2, 4, 20, 25, "€", "Casserole, pilon et mortier (ou robot à pâte).",
  "L'igname bouillie puis pilée jusqu'à une boule élastique et lisse : l'accompagnement des sauces légères (sauce graine, sauce claire, azi dessi). À la maison, le robot à pâte remplace le mortier.",
  ["1,2 kg|d'igname|Igname|3", "10 cl|d'eau de cuisson|-|0"],
  ["**Cuire.** Igname pelée (gants : la peau gratte), en gros morceaux, eau froide non salée ; 20 à 25 min : la lame entre sans résistance.",
   "**Piler.** Égoutte en gardant l'eau ; pile chaud au mortier ou au robot (crochet), par petites quantités.",
   "**Lisser.** Mouille le pilon d'eau de cuisson et travaille 5 min : pâte élastique, sans grumeaux, qui colle au doigt sans s'y défaire.",
   "**Former.** En boules avec les mains mouillées ; sers tout de suite, chaud."],
  tips=["L'igname se pile chaude : froide, elle devient granuleuse."], keep="Le jour même.", age=1, cats=["vegetarien"], profil=[])
K("koliko", "Koliko (frites d'igname, sauce piment)", "Koliko", TG, "A", 1, 4, 15, 15, "€", "Casserole à friture, thermomètre.",
  "Les frites d'igname vendues le soir dans les rues de Lomé et d'Accra : bâtonnets épais, croustillants dehors et farineux dedans, avec une sauce piment à l'oignon et à la tomate.",
  ["1 kg|d'igname|Igname|3", "1 L|d'huile de friture|Huile d'arachide|2", f"1|oignon|{OIG}|1", f"1|tomate|{TOM}|1", f"1|piment frais|{PIMENT}|1", f"1 pincée|de sel|{SEL}|0"],
  ["**Couper.** Igname pelée en bâtonnets de 1,5 cm, rincée, épongée.",
   "**Précuire.** 5 min dans l'eau bouillante salée : la pointe du couteau entre ; égoutte et laisse sécher 10 min.",
   "**Frire.** 175 °C, par petites quantités, 6 à 8 min : dorées, croustillantes ; sel.",
   "**Sauce.** Oignon, tomate et piment mixés, 5 min dans 2 c. à s. d'huile ; à côté."],
  tips=["Huile chaude : poêle loin des enfants, jamais d'eau dedans."], keep="À manger tout de suite.", age=2, cats=["vegetarien"], profil=["gras", "epice"], kids="✓ dès 2 ans, sans la sauce piment.")
K("pinon", "Pinon (pâte de gari à la sauce tomate)", "Pinon / piron", TG, "A", 1, 4, 10, 15, "€", "Casserole, spatule.",
  "Au Togo et au Bénin, le gari (semoule de manioc grillée) cuit dans une sauce tomate-oignon donne une pâte rouge et moelleuse en quelques minutes : l'accompagnement du poisson frit et du poulet grillé.",
  ["250 g|de gari (semoule de manioc)|Manioc / attiéké / garri|3", f"3|tomates|{TOM}|2", f"2 c. à s.|de concentré|{CONC}|1", f"1|oignon|{OIG}|1", f"1|piment frais|{PIMENT}|1", f"4 c. à s.|d'huile|{HN}|1", f"1|cube de bouillon|{CUBE}|1"],
  ["**Sauce.** Tomates, oignon, piment mixés ; huile, concentré, 10 min : réduite.",
   "**Bouillon.** 50 cl d'eau, cube, sel ; à ébullition.",
   "**Gari.** En pluie hors du feu en tournant : il gonfle aussitôt ; remets 2 min à feu doux en écrasant : pâte souple.",
   "**Servir.** En dôme, avec du poisson frit ou du poulet."],
  tips=["Trop ferme : une louche d'eau chaude ; trop molle : une poignée de gari."], keep="1 jour au frigo.", age=2, cats=["vegetarien", "express"], profil=["epice"], kids="✓ dès 2 ans, sans piment.")
K("klaklou", "Klaklou (beignets de banane plantain mûre)", "Klaklou / klaklo", TG, "G", 1, 4, 15, 15, "€", "Casserole à friture.",
  "Des petits beignets de plantain bien mûr écrasé, liés d'un peu de farine, relevés de piment et de gingembre : sucrés-pimentés, croustillants dehors, fondants dedans. Au goûter ou avec des cacahuètes.",
  ["3|bananes plantain très mûres (peau noire)|Plantain (banane à cuire)|3", f"60 g|de farine|{F55}|2", f"1 c. à c.|de gingembre râpé|{GING}|1", f"1 pincée|de piment en poudre|{CAYENNE}|1?", f"1 pincée|de sel|{SEL}|0", "1 L|d'huile de friture|Huile d'arachide|2"],
  ["**Écraser.** Plantains épluchés écrasés à la fourchette : purée.",
   "**Lier.** Farine, gingembre, piment, sel : pâte épaisse qui tient sur la cuillère.",
   "**Frire.** 170 °C, cuillerées de pâte, 4 min en retournant : brun foncé (le plantain caramélise).",
   "**Égoutter.** Sur papier absorbant ; tièdes."],
  tips=["Huile chaude : poêle loin des enfants."], keep="Le jour même.", age=2, cats=["vegetarien", "enfants"], profil=["sucre", "gras"], kids="✓ dès 2 ans, sans piment.")
K("atchomon", "Atchomon (petits biscuits frits croquants, Togo et Bénin)", "Atchomon", TG, "G", 1, 8, 25, 20, "€", "Rouleau, casserole à friture.",
  "Les petits dés de pâte sucrée frits jusqu'à être durs et croquants, vendus en sachets dans les rues de Lomé et Cotonou : un grignotage qui se garde longtemps.",
  [f"400 g|de farine|{F55}|3", f"100 g|de sucre|{SUCRE}|2", f"1|œuf|{OEUF}|1", f"50 g|de beurre fondu|{BEURRE}|1", f"1/2 c. à c.|de levure chimique|{LEVC}|1", f"1 pincée|de muscade|{MUSC}|0", "12 cl|de lait|Lait entier / demi-écrémé / écrémé|1", "1 L|d'huile de friture|Huile d'arachide|2"],
  ["**Pâte.** Farine, sucre, levure, muscade ; œuf, beurre, lait : pâte ferme et lisse, 5 min.",
   "**Étaler.** 5 mm d'épaisseur ; coupe en dés de 1 cm.",
   "**Frire.** 165 °C, par poignées, 6 à 8 min en remuant : brun doré, durs au toucher.",
   "**Refroidir.** Étalés sur papier : ils durcissent encore."],
  tips=["Petits enfants : dés durs, à éviter avant 4 ans (fausse route)."], keep="2 semaines en boîte hermétique.", age=4, cats=["enfants"], profil=["sucre", "gras"], kids="✓ dès 4 ans (dés durs).")

# ---------------- Haoussa ----------------
K("yaji", "Yaji (mélange d'épices suya haoussa)", "Yaji / poudre suya", HA, "Ba", 1, 12, 10, 5, "€", "Poêle, mixeur ou moulin à épices.",
  "La base de toutes les grillades haoussa : des cacahuètes grillées réduites en poudre presque sèche (à la place du kuli-kuli, le tourteau d'arachide), du piment, du gingembre, de l'oignon et de l'ail en poudre. Pour enrober le suya, le tsire, le kilishi, ou à saupoudrer au service.",
  [f"150 g|de cacahuètes grillées non salées|{ARA}|3", f"2 c. à s.|de piment en poudre (moins pour un yaji doux)|{CAYENNE}|2", "2 c. à s.|de gingembre en poudre|Gingembre (poudre)|2", f"1 c. à s.|de poudre d'oignon|{PDO}|1", f"1 c. à c.|de poudre d'ail|{PDO}|1", f"1 c. à s.|de paprika|{PAPRIKA}|1", f"2|cubes de bouillon|{CUBE}|1", "4|clous de girofle|Clou de girofle|0?", f"1 c. à c.|de sel|{SEL}|0"],
  ["**Torréfier.** Cacahuètes 3 min à la poêle sèche : parfumées ; refroidies.",
   "**Moudre.** Par impulsions courtes avec les cubes et le girofle : poudre fine (trop longtemps, elle tourne en beurre).",
   "**Dégraisser.** Étale sur du papier absorbant 1 h, presse : plus sèche, elle accroche mieux à la viande.",
   "**Mélanger.** Épices, sel ; en bocal sec."],
  tips=["⚠️ Arachide : allergène majeur.", "Doux pour les enfants : 1 c. à c. de piment au lieu de 2 c. à s."], keep="1 mois en bocal fermé, au sec et à l'abri de la lumière.", age=3, cats=["sauces"], profil=["epice"], kids="✓ dès 3 ans en version douce, sans allergie à l'arachide.")
K("suya_poulet", "Suya de poulet (tsire kaza, brochettes au yaji)", "Tsiren kaza", HA, "P", 1, 4, 20, 15, "€", "Brochettes, barbecue ou grill.",
  "Le suya à la volaille : des lanières de blanc ou de haut de cuisse huilées, roulées dans le yaji, grillées sur la braise et resaupoudrées au service, avec oignon rouge, tomate et concombre.",
  ["700 g|de hauts de cuisse ou de blancs de poulet|Blanc de poulet|3", "6 c. à s.|de yaji (fiche Yaji)|Cacahuète / arachide|3", f"3 c. à s.|d'huile|{HN}|1", "1|oignon rouge|Oignon rouge|1", f"2|tomates|{TOM}|1", "1/2|concombre|Concombre|1", f"1/2|citron|{CIT}|1"],
  ["**Couper.** Poulet en lanières fines (1 cm) ; brochettes trempées 30 min si en bois.",
   "**Enrober.** Lanières huilées, 4 c. à s. de yaji, piquées en accordéon ; 1 h au frigo.",
   "**Griller.** Braise vive ou grill, 4 à 5 min par face en badigeonnant d'huile : croûte brune, cœur blanc nacré, jus clair.",
   "**Servir.** Reste de yaji, oignon rouge, tomate, concombre, citron."],
  tips=["⚠️ Arachide : allergène majeur."], keep="2 jours au frigo.", age=3, cats=["enfants"], fetes=["Barbecue d'été"], profil=["epice"], kids="✓ dès 3 ans avec un yaji doux.")
K("tsire_agneau", "Tsire d'agneau (brochettes haoussa au yaji)", "Tsire", HA, "P", 1, 4, 20, 15, "€€", "Brochettes, barbecue.",
  "Au nord du Nigeria et au Niger, le tsire se fait souvent avec du mouton : de petits morceaux de gigot ou d'épaule, gras compris, enrobés de yaji et grillés lentement sur la braise jusqu'à la croûte épicée.",
  ["800 g|de gigot ou d'épaule d'agneau en cubes de 2 cm|Gigot d'agneau|3", "6 c. à s.|de yaji (fiche Yaji)|Cacahuète / arachide|3", f"3 c. à s.|d'huile d'arachide|Huile d'arachide|1", f"1 c. à c.|de poudre d'oignon|{PDO}|1", "1|oignon rouge|Oignon rouge|1", f"2|tomates|{TOM}|1"],
  ["**Mariner.** Cubes, huile, poudre d'oignon, sel, 4 c. à s. de yaji ; 2 h au frigo.",
   "**Embrocher.** En alternant maigre et gras, sans serrer.",
   "**Griller.** Braise moyenne, 12 à 15 min en tournant et en badigeonnant d'huile : croûte brune, rosé à cœur.",
   "**Servir.** Yaji, oignon rouge, tomate."],
  tips=["⚠️ Arachide : allergène majeur."], keep="2 jours au frigo.", age=3, fetes=["Barbecue d'été", "Ramadan / Aïd"], profil=["viande_rouge", "epice"], kids="✓ dès 3 ans avec un yaji doux, viande bien cuite.")
K("kilishi", "Kilishi (feuilles de bœuf séchées au yaji, version four)", "Kilishi", HA, "E", 3, 8, 40, 300, "€€€", "Four à chaleur tournante, grilles, thermomètre de four.",
  "La viande séchée de Kano : du bœuf tranché en feuilles très fines, séché, enduit d'une pâte d'arachide épicée, séché encore puis passé rapidement sur la braise. À la maison, le four à basse température remplace le soleil, en chauffant d'abord la viande à cœur pour la sécurité.",
  ["1 kg|de tende de tranche ou de rumsteck très maigre|Rumsteck|3", "100 g|de pâte d'arachide|Pâte d'arachide|2", "4 c. à s.|de yaji (fiche Yaji)|Cacahuète / arachide|2", f"1|oignon|{OIG}|1", f"2 c. à s.|de sucre|{SUCRE}|1", f"1 c. à c.|de gingembre râpé|{GING}|1", f"1|cube de bouillon|{CUBE}|1"],
  ["**Trancher.** Bœuf 1 h au congélateur, puis en feuilles de 2 à 3 mm dans le sens des fibres, tout le gras retiré.",
   "**Premier séchage.** Feuilles à plat sur grilles, four 120 °C 15 min (la viande dépasse 71 °C), puis 75 °C chaleur tournante, porte entrouverte, 2 h : sèches, encore souples.",
   "**Enduire.** Pâte d'arachide, yaji, oignon mixé, sucre, gingembre, cube, un peu d'eau : crème épaisse ; badigeonne les deux faces.",
   "**Second séchage.** 75 °C, 1 h 30 à 2 h : enrobage sec au toucher ; 2 min sous le grill par face, sans brûler."],
  tips=["⚠️ Arachide : allergène majeur.", "Sécurité : la première chauffe à 120 °C est indispensable ; jamais de séchage à l'air libre à la maison.", "Petits enfants : morceaux durs, à éviter avant 6 ans."],
  keep="1 mois en boîte hermétique au frais, à l'abri de l'humidité (au frigo s'il reste souple).", age=6, cats=[], fetes=["Apéritif dînatoire"], profil=["viande_rouge", "epice"], kids="✓ dès 6 ans (viande dure).")
K("balangu", "Balangu (mouton grillé à la haoussa)", "Balangu", HA, "P", 2, 6, 25, 75, "€€", "Barbecue à couvercle ou four, papier sulfurisé.",
  "Le grand morceau de mouton des fêtes haoussa : de longues lanières d'épaule ou de gigot, cuites doucement près des braises jusqu'à être fondantes dans leur gras, puis saisies et roulées dans le yaji. Avec oignons, tomates et concombre.",
  ["1,5 kg|d'épaule d'agneau désossée, en lanières de 4 cm|Épaule d'agneau|3", f"2|oignons|{OIG}|2", f"4 cm|de gingembre|{GING}|1", f"4|gousses d'ail|{AIL}|1", f"1|cube de bouillon|{CUBE}|1", "5 c. à s.|de yaji (fiche Yaji)|Cacahuète / arachide|2", f"3 c. à s.|d'huile d'arachide|Huile d'arachide|1", f"2|tomates|{TOM}|1", "1/2|concombre|Concombre|1"],
  ["**Mariner.** 1 oignon, gingembre, ail, cube mixés ; frotte la viande salée, 2 h au frigo.",
   "**Cuire doucement.** En papillote de papier sulfurisé mouillé (ou à couvert près des braises), four 160 °C, 1 h : fondante, le gras a fondu.",
   "**Saisir.** Sors des papillotes, huile, braise vive ou grill, 4 min par face : croûte brune.",
   "**Yaji.** Roule aussitôt dans le yaji ; avec l'autre oignon cru, tomate, concombre."],
  tips=["⚠️ Arachide : allergène majeur."], keep="2 jours au frigo.", age=3, fetes=["Ramadan / Aïd", "Barbecue d'été"], profil=["viande_rouge", "epice", "gras"], kids="✓ dès 3 ans, sans yaji fort, viande effilochée.")
K("dambun_nama", "Dambun nama (effiloché de bœuf frit et sec, au yaji)", "Dambun nama", HA, "E", 2, 8, 40, 90, "€€", "Cocotte, mortier ou robot, grande poêle.",
  "La « viande en fil » haoussa : du bœuf bouilli avec oignon et épices, pilé jusqu'à des fibres fines, puis frit à sec en remuant jusqu'à devenir léger, doré et croustillant. Il se garde et se grignote avec du pain, du riz ou de la bouillie.",
  ["1 kg|de bœuf maigre (paleron dégraissé ou tende)|Paleron|3", f"2|oignons|{OIG}|2", f"3 cm|de gingembre|{GING}|1", f"3|gousses d'ail|{AIL}|1", f"2|cubes de bouillon|{CUBE}|1", "3 c. à s.|de yaji (fiche Yaji)|Cacahuète / arachide|2", f"10 cl|d'huile|{HN}|1"],
  ["**Bouillir.** Bœuf en gros morceaux, 1 oignon, gingembre, ail, cubes, eau à hauteur ; 1 h 15 : très tendre, presque sec en fin de cuisson.",
   "**Piler.** Au mortier ou par impulsions au robot, par petites quantités : fibres fines et aériennes ; effiloche le reste à la fourchette.",
   "**Frire à sec.** Huile, l'autre oignon râpé 2 min ; viande, feu moyen, 15 à 20 min en remuant sans arrêt : dorée, légère, croustillante.",
   "**Assaisonner.** Yaji ; étale sur un plateau garni de papier : sèche à l'air 30 min."],
  tips=["⚠️ Arachide : allergène majeur (yaji)."], keep="2 semaines en boîte hermétique au frigo.", age=3, cats=[], profil=["viande_rouge", "epice"], kids="✓ dès 3 ans avec un yaji doux.")
K("masa_haoussa", "Masa (galettes de riz fermenté haoussa)", "Masa / waina", HA, "A", 2, 6, 25, 30, "€", "Mixeur, poêle à alvéoles (type æbleskiver) ou petite poêle.",
  "Les petites galettes rondes du nord du Nigeria : du riz trempé et mixé avec un peu de riz cuit, levé à la levure, cuit en poêle à alvéoles. Moelleuses, légèrement acidulées, avec une soupe (miyan taushe), du suya ou du miel.",
  ["400 g|de riz rond|Riz rond / sushi|3", "100 g|de riz cuit|Riz rond / sushi|1", f"5 g|de levure boulangère sèche|{LEV}|1", f"2 c. à s.|de sucre|{SUCRE}|1", f"1 pincée|de sel|{SEL}|0", f"1/2 c. à c.|de levure chimique|{LEVC}|1", f"5 c. à s.|d'huile|{HN}|1"],
  ["**Tremper.** Riz cru, eau à hauteur, une nuit.",
   "**Mixer.** Égoutté, avec le riz cuit et 20 cl d'eau : pâte lisse et épaisse ; levure, sucre ; 3 h dans un endroit tiède : bulles en surface.",
   "**Lever.** Sel et levure chimique au dernier moment.",
   "**Cuire.** Alvéoles huilées chaudes, une louche de pâte, couvercle, 3 min ; retourne, 2 min : dorées des deux côtés, moelleuses dedans."],
  tips=["Sans poêle à alvéoles : petites galettes épaisses dans une poêle à blinis."], keep="1 jour ; se réchauffent à la poêle.", age=1, cats=["vegetarien", "enfants"], profil=[])
