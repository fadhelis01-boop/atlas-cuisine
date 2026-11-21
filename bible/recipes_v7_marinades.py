# -*- coding: utf-8 -*-
"""Coin marinades (audit UI/UX senior, 20/11/2026 ; audit chef senior, 21/11/2026) : la rubrique Marinades n'avait que
7 bases dispersées dans les sauces et condiments, aucune pour l'agneau, les crevettes ou le tofu, et aucune n'expliquait
le geste du cure à sec (gravlax) à côté de la marinade liquide classique. Comblé une première fois avec 6 fiches
réutilisables sur n'importe quelle pièce de viande/poisson du même type, pas liée à un seul plat fini.
Audit chef senior du 21/11 : 5 de ces fiches (agneau, porc cubain, porc vietnamien, shawarma, crevettes) avaient
dérivé en mini-recettes figées (la pièce de viande en ingrédient structurant, jusqu'à la cuisson et au dressage) —
remises en marinades génériques, la viande ne reste que dans le texte des étapes, comme `marinade_bulgogi`. Trois
angles morts comblés en plus : la marinade au vin rouge (la plus classique de toutes en cuisine française, déjà
utilisée par `coq_au_vin`, `daube_provencale`, `civet_lievre`, `lievre_royale` sans jamais être elle-même une fiche),
une marinade pour légume à griller (aubergine, le Tofu & légumes du coin n'avait que le tofu) et une pour des fruits
de mer autres que la crevette (calamars). NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *
from recipes_v6_tiktok_plats import C

TT = "https://www.tiktok.com/"
def V(author, vid):
    return (f"@{author}", f"{TT}@{author}/video/{vid}")

MAG = "Afrique du Nord › Maghreb"; CU = "Amérique latine & Caraïbes › Cuba"; VN = "Asie du Sud-Est › Vietnam"
MX = "Amérique latine › Mexique"; CN = "Asie de l'Est › Chine"; SU = "Europe du Nord › Suède"
US = "Amérique du Nord › États-Unis"; FR_BISTROT = "France › Cuisine de bistrot"; JP = "Asie de l'Est › Japon"
ES = "Europe du Sud › Espagne"
CITRONNELLE = "Citronnelle"; NUOCMAM = "Sauce de poisson (nuoc-mâm, nam pla)"
TOFU_F = "Tofu (ferme / soyeux)"; SAUMON_PAVE = "Saumon (frais, pavé)"; HARISSA = "Harissa (tube/pâte)"
AUBERGINE = "Aubergine"; CALAMAR = "Calamar / encornet"

K("harissa_marinade_agneau", "Marinade harissa-citron pour agneau (Maghreb)", "Marinade pour agneau grillé", MAG, "Ba", 1, 6, 10, 240, "€",
  "Saladier, fouet.",
  "La marinade qui manquait au coin marinades pour l'agneau : harissa, citron, cumin et coriandre, pour des "
  "brochettes, un gigot en morceaux ou des côtelettes grillées. Elle attendrit autant qu'elle parfume.",
  [f"3 c. à s.|de harissa|{HARISSA}|2", f"4 c. à s.|d'huile d'olive|{HO}|2", f"1|citron (jus et zeste)|{CIT}|1",
   f"4 gousses|d'ail, écrasées|{AIL}|1", f"1 c. à c.|de cumin|{CUMIN}|1", f"1/2 bouquet|de coriandre, hachée|{CORI}|1",
   f"1 c. à c.|de miel|{MIEL}|1?", f"-|sel|{SEL}|1"],
  ["**Mélanger.** Harissa, huile, jus et zeste de citron, ail, cumin, coriandre et miel fouettés ensemble en une "
   "marinade homogène et bien rouge, pour environ 1 kg d'agneau en morceaux, en côtelettes ou en brochettes.",
   "**Entailler.** Pièces d'agneau légèrement entaillées en surface (elles absorbent mieux) ; enrobées "
   "généreusement de marinade avec les mains, dans un plat ou un sac de congélation.",
   "**Reposer.** Au moins 4 h au frigo, idéalement toute une nuit : la viande se détend et prend bien le goût. "
   "Sortie 20 min avant la cuisson pour revenir à température.",
   "**Griller.** Au barbecue, au gril de four ou à la poêle très chaude, selon la pièce et son épaisseur ; "
   "l'excédent de marinade est essuyé avant de griller (il brûlerait sinon)."],
  tips=["Plus elle repose longtemps (jusqu'à 24 h), plus l'agneau est parfumé et tendre : ne te presse pas sur "
        "ce point.", "Cette même marinade convient aussi au poulet ou au bœuf à griller, sans rien changer aux "
        "proportions."],
  keep="Marinade seule, 5 jours au frigo ; viande marinée, 2 jours crue ou cuite.", age=3,
  kids="✓ dès 3 ans, en version moins pimentée (moitié moins de harissa).", cats=["sauces"], profil=["epice", "acide"])
K("mojo_cubain_porc", "Mojo cubain pour porc (ail, citron vert, cumin, origan)", "Mojo criollo", CU, "Ba", 1, 6, 10, 180, "€",
  "Saladier, fouet.",
  "La marinade de tous les rôtis de porc cubains : beaucoup d'ail, du citron vert, du cumin et de l'origan dans "
  "l'huile d'olive, qui pénètre la viande et donne au porc rôti ou grillé son goût si reconnaissable des "
  "Caraïbes.",
  [f"12 gousses|d'ail, écrasées en pâte|{AIL}|2", f"4|citrons verts (jus)|Citron vert|2", f"1|orange (jus)|Orange|1",
   f"10 cl|d'huile d'olive|{HO}|2", f"2 c. à c.|de cumin|{CUMIN}|1", "1 c. à c.|d'origan séché|Origan frais / sec|1",
   f"-|sel, poivre|{SEL}|1"],
  ["**Pâte d'ail.** Ail écrasé au plat du couteau avec une pincée de gros sel jusqu'à une pâte lisse (ça évite les "
   "morceaux d'ail brûlé à la cuisson).",
   "**Mélanger.** Pâte d'ail, jus de citron vert et d'orange, huile, cumin et origan fouettés ensemble ; sel, "
   "poivre. Pour environ 1 kg de filet ou d'épaule de porc, de poulet ou de crevettes.",
   "**Entailler et mariner.** Viande piquée de petits trous au couteau (la marinade pénètre plus profond) ; "
   "enrobée généreusement ; au moins 3 h au frigo pour le porc (1 h 30 pour du poulet, 20 min pour des crevettes), "
   "mieux toute une nuit pour une pièce épaisse.",
   "**Cuire.** Rôtie au four ou grillée selon la pièce, arrosée de marinade restante en début de cuisson "
   "seulement (jamais en fin, sur une viande déjà cuite, à cause du cru qui y a trempé)."],
  tips=["Le mélange citron vert + orange est la vraie signature du mojo : le citron vert seul est plus acide et "
        "moins rond.", "Sans porc : le même mojo convient très bien au poulet (repos 1 h 30) ou aux crevettes "
        "(repos 20 min)."],
  keep="Marinade seule, 5 jours au frigo ; viande marinée, 2 jours crue.", age=2, kids="✓ dès 2 ans.",
  cats=["sauces"], profil=["acide"])
K("porc_citronnelle_vietnamien", "Marinade vietnamienne à la citronnelle (bò/thịt nướng xả)", "Thịt nướng xả", VN, "Ba", 1, 6, 15, 120, "€",
  "Mixeur ou mortier, saladier.",
  "La marinade des grillades de rue vietnamiennes : citronnelle pilée, ail, échalote, sauce poisson et sucre, "
  "pour du porc, du poulet ou du bœuf coupé fin, grillé fumant sur un vermicelle froid ou dans un bánh mì.",
  [f"3 tiges|de citronnelle, cœur tendre haché fin|{CITRONNELLE}|2", f"4 gousses|d'ail, hachées|{AIL}|1",
   f"2|échalotes, hachées|{ECH}|1", f"3 c. à s.|de sauce de poisson|{NUOCMAM}|2", f"2 c. à s.|de cassonade|{SUCRE}|1",
   f"2 c. à s.|d'huile|{HN}|1", f"1 c. à c.|de poivre noir moulu|{POIVRE}|1"],
  ["**Piler.** Citronnelle, ail et échalote pilés au mortier ou mixés avec un peu d'huile jusqu'à une pâte "
   "grossière et parfumée : c'est elle qui porte tout le goût.",
   "**Mélanger.** Pâte de citronnelle, sauce poisson, cassonade, huile et poivre mélangés en une marinade "
   "épaisse, pour environ 800 g de porc, de poulet, de bœuf ou de tofu ferme, en fines tranches.",
   "**Mariner.** Viande en tranches fines enrobée généreusement ; 1 h à 2 h au frigo suffisent (les tranches "
   "fines prennent vite le goût, inutile de laisser toute une nuit).",
   "**Griller.** Très vif, à la poêle, au gril ou au barbecue, par petites fournées sans entasser : 2 à 3 min par "
   "face, bords caramélisés et légèrement noircis par endroits (c'est voulu, ça fait le goût fumé)."],
  tips=["Des tranches fines et toutes de la même épaisseur grillent uniformément en quelques minutes : demande "
        "au boucher si besoin.", "Cette marinade convient à peu près à toutes les viandes à griller : porc, "
        "poulet, bœuf, même un tofu ferme pour une version végétarienne."],
  keep="Marinade seule, 4 jours au frigo ; viande marinée, 1 jour crue.", age=3, kids="✓ dès 3 ans.",
  cats=["sauces"], profil=["acide", "sucre"])
K("crevettes_citron_vert_marinade", "Marinade ail-citron vert pour crevettes grillées", "Camarones al mojo de ajo", MX, "Ba", 1, 6, 10, 20, "€",
  "Saladier.",
  "La marinade express des crevettes de bord de mer mexicaines : ail, citron vert, piment et coriandre, à peine "
  "20 minutes de repos (les crustacés n'en demandent pas plus), puis une poêle brûlante.",
  [f"4 gousses|d'ail, écrasées|{AIL}|2", f"2|citrons verts (jus)|Citron vert|2", f"3 c. à s.|d'huile d'olive|{HO}|1",
   f"1/2 c. à c.|de piment en poudre|{CAYENNE}|1?", f"1/2 bouquet|de coriandre, hachée|{CORI}|1?", f"-|sel|{SEL}|1"],
  ["**Mélanger.** Ail, jus de citron vert, huile, piment et coriandre fouettés ensemble, pour environ 700 g de "
   "grosses crevettes décortiquées ou de lamelles de poisson blanc ferme.",
   "**Mariner court.** Crevettes (ou poisson) enrobées de marinade, sel ; 15 à 20 min au frigo au maximum : plus "
   "longtemps, l'acidité du citron commence à « cuire » la chair comme un ceviche et elle devient élastique à la "
   "cuisson.",
   "**Cuire très vif.** Poêle ou plancha brûlante, crevettes égouttées de leur marinade, 90 secondes à 2 min par "
   "face selon la taille : roses et opaques, encore souples, jamais plus.",
   "**Servir.** Aussitôt, avec un quartier de citron vert et le reste de coriandre."],
  tips=["Ne jamais laisser des crevettes plus de 20-30 min dans une marinade acide : contrairement à une viande, "
        "elles « cuisent » chimiquement et durcissent.", "La même marinade convient à des lamelles de poisson "
        "blanc ferme, même temps de repos."],
  keep="Marinade seule, 3 jours au frigo ; crevettes marinées, à cuire le jour même.", age=3,
  kids="✓ dès 3 ans, sans piment.", cats=["sauces"], profil=["acide"])
K("tofu_marinade_soja_gingembre", "Marinade soja-gingembre pour tofu (et légumes à griller)", "Tofu marinade", CN, "Ba", 1, 6, 10, 30, "€",
  "Saladier.",
  "La marinade végétarienne du coin marinades : soja, gingembre, ail et une pointe de sucre, pour un tofu ferme "
  "pressé qui dore et caramélise à la poêle ou au four comme une viande marinée. Aussi bonne sur des légumes "
  "fermes à griller (aubergine, champignons).",
  [f"300 g|de tofu ferme, pressé 20 min puis coupé en tranches ou en cubes|{TOFU_F}|3", f"4 c. à s.|de sauce soja|{SOJA}|2",
   f"2 c. à s.|d'huile de sésame|Huile de sésame (grillée)|1", f"2 cm|de gingembre frais, râpé|{GING}|1",
   f"2 gousses|d'ail, écrasées|{AIL}|1", f"1 c. à c.|de miel ou de sirop d'érable|{MIEL}|1",
   f"1 c. à s.|de vinaigre de riz|Vinaigre de riz|1?"],
  ["**Presser le tofu.** Enveloppé dans un torchon propre, un poids dessus, 20 min : il rend son eau et absorbe "
   "bien mieux la marinade ensuite.",
   "**Mélanger.** Soja, huile de sésame, gingembre, ail, miel et vinaigre de riz fouettés ensemble.",
   "**Mariner.** Tofu coupé enrobé de marinade, 20 à 30 min à température ambiante (le tofu n'a pas besoin du "
   "frigo pour une marinade courte comme celle-ci) en le retournant une fois à mi-temps.",
   "**Cuire.** Doré à la poêle bien chaude avec un peu d'huile, 3 à 4 min par face, ou au four à 200 °C 20 min en "
   "le retournant : bords caramélisés, légèrement croustillants."],
  tips=["Le pressage est l'étape qu'on saute trop souvent : sans lui, le tofu rend de l'eau à la cuisson au lieu "
        "de dorer.", "La même marinade fonctionne très bien sur des tranches d'aubergine ou des champignons "
        "entiers à griller."],
  keep="Marinade seule, 1 semaine au frigo ; tofu mariné, 2 jours.", age=1, kids="✓ dès 1 an.",
  cats=["sauces", "vegetarien"], profil=["acide", "sucre"])
K("gravlax_saumon_marinade", "Gravlax de saumon (marinade sèche au sel, sucre et aneth)", "Gravlax", SU, "E", 2, 8, 15, 2880, "€€€",
  "Plat ou plaque, film alimentaire, poids (boîtes de conserve ou planche lestée).",
  "La marinade scandinave qui n'utilise aucun liquide : un pavé de saumon enseveli sous un mélange de gros sel, "
  "de sucre et d'aneth, qui en 2 à 3 jours au frigo « cuit » la chair par le sel seul, sans aucune chaleur. "
  "Tranché finement comme un saumon fumé, pour les toasts et les blinis.",
  [f"800 g|de saumon, en un ou deux pavés avec la peau, sans arêtes|{SAUMON_PAVE}|3", f"100 g|de gros sel|{SEL}|3",
   f"100 g|de sucre|{SUCRE}|3", f"2 c. à s.|de poivre noir concassé|{POIVRE}|1", f"1 gros bouquet|d'aneth, grossièrement haché|Aneth|3",
   f"3 c. à s.|de vodka ou d'aquavit (facultatif, pour la conservation et le parfum)|-|1?"],
  ["**Préparer.** Saumon vérifié du bout des doigts (arêtes retirées à la pince), épongé.",
   "**Mélanger la marinade sèche.** Gros sel, sucre et poivre mélangés ; la moitié étalée dans un plat, l'aneth "
   "haché par-dessus.",
   "**Enfouir.** Pavé de saumon posé côté chair sur l'aneth, arrosé d'alcool si utilisé ; reste du mélange "
   "sel-sucre étalé généreusement sur le dessus pour bien le couvrir.",
   "**Presser.** Filmé hermétiquement, un poids posé dessus (planche et boîtes de conserve) ; 48 à 72 h au "
   "frigo, retourné une fois par jour : le sel fait sortir l'eau, qu'on voit s'accumuler dans le plat.",
   "**Rincer et trancher.** Sorti du sel, rincé rapidement à l'eau froide pour enlever l'excédent, séché ; "
   "tranché très fin en biais, comme un saumon fumé."],
  tips=["Plus le poisson est épais, plus il faut de temps : 48 h pour un pavé fin, 72 h pour une grosse pièce. Au "
        "doigt, la chair doit être ferme, plus du tout molle comme du cru.", "Le sel ne doit jamais être lésiné : "
        "c'est lui, et lui seul, qui rend ce poisson cru sans danger à manger — pas de cuisson à la chaleur ici."],
  keep="5 jours au frigo une fois tranché, bien enveloppé ; se congèle entier avant tranchage.", age=4,
  kids="Pour les grands à partir de 4 ans ; à éviter pour les femmes enceintes et les personnes fragiles (poisson "
       "cru, même salé).", cats=[], fetes=["Noël et Nouvel An"], profil=["acide", "sucre"])
K("marinade_rouge_africaine", "Marinade rouge ouest-africaine (tomate, ail, piment)", "Marinade rouge", "Afrique subsaharienne › Côte d'Ivoire", "Ba", 1, 8, 15, 120, "€",
  "Mixeur.",
  "La marinade qui revient dans toutes les cuisines d'Afrique de l'Ouest sous un nom différent : concentré de "
  "tomate, ail, gingembre et piment mixés avec un bouillon cube, pour un poulet ou un poisson qui part au four "
  "ou au grill avec une couleur et un goût profonds dès la sortie du four.",
  [f"4 c. à s.|de concentré de tomate|{CONC}|2", f"8 gousses|d'ail|{AIL}|2", f"3 cm|de gingembre frais|{GING}|1",
   f"2|piments frais (plus ou moins selon le goût)|{PIMENT}|1", f"2|cubes de bouillon, émiettés|Bouillon cube volaille|1",
   f"4 c. à s.|d'huile|{HN}|2", f"1 c. à c.|de paprika|{PAPRIKA}|1", f"-|sel|{SEL}|1"],
  ["**Mixer.** Ail, gingembre et piments mixés avec un peu d'huile jusqu'à une pâte fine.",
   "**Finir.** Concentré de tomate, cubes émiettés, paprika et sel ajoutés, mixés de nouveau : pâte rouge "
   "épaisse et homogène.",
   "**Mariner.** Poulet ou poisson entaillé, enrobé généreusement de la pâte avec les mains ; au moins 2 h au "
   "frigo, mieux toute une nuit pour un poulet entier.",
   "**Cuire.** Au four (200 °C, 25 à 35 min selon la pièce), au grill ou à la poêle (20 à 25 min en retournant) ; la "
   "pâte colore et caramélise en surface tout en gardant la chair juteuse dessous."],
  tips=["Cette marinade se congèle très bien en portions : en préparer le double et en garder pour la prochaine "
        "fois.", "Sur un poisson entier, elle se glisse aussi dans deux ou trois entailles profondes pour "
        "parfumer jusqu'à l'arête."],
  keep="1 semaine au frigo ; plusieurs mois au congélateur en portions.", age=3,
  kids="✓ dès 3 ans, moins pimenté.", cats=["sauces"], profil=["epice", "acide"],
  credit=C(V("dadyeats", "7623101280000511254")))
K("shawarma_marinade", "Marinade shawarma (yaourt, citron, concentré de tomate, épices)", "Marinade shawarma", "Moyen-Orient › Liban", "Ba", 1, 6, 10, 240, "€",
  "Saladier, fouet.",
  "La marinade du shawarma de rue libanais : un yaourt qui attendrit, du concentré de tomate pour la couleur et "
  "le fond de goût, de l'ail fumé et des épices shawarma. Distincte du tandoori indien (pas de curcuma ni de "
  "piment fort) et du tzatziki-ail de la chich taouk.",
  [f"4 c. à s.|de yaourt nature|{YAO}|2", f"4 c. à s.|d'huile d'olive|{HO}|2", f"1/2|citron (jus)|{CIT}|1",
   f"4 gousses|d'ail, écrasées|{AIL}|1", f"1 c. à c.|de concentré de tomate|{CONC}|1",
   f"1 c. à s.|d'épices à shawarma (cumin, paprika, cannelle, curcuma à parts égales)|{CUMIN}|1", f"-|sel, poivre|{SEL}|1"],
  ["**Mélanger.** Yaourt, huile, jus de citron, ail, concentré de tomate et épices fouettés ensemble ; sel, "
   "poivre. Pour environ 1 kg de hauts de cuisse de poulet désossés, en lamelles.",
   "**Mariner.** Poulet (ou agneau, même proportions) en lamelles enrobé généreusement ; au moins 4 h au frigo, "
   "idéalement toute une nuit pour que l'acidité du yaourt attendrisse bien la viande.",
   "**Empiler et cuire.** Lamelles empilées sur une broche verticale improvisée (ou simplement sautées très "
   "chaudes à la poêle, en plusieurs fois sans entasser) jusqu'à bien dorées et légèrement croustillantes sur "
   "les bords.",
   "**Servir.** Tranché fin, en pain pita avec une sauce à l'ail et des crudités."],
  tips=["Le concentré de tomate est ce qui distingue vraiment cette marinade du tandoori ou du tikka indiens : "
        "ne le saute pas, c'est lui qui donne la couleur et le goût caractéristiques.", "Sans broche, empiler les "
        "lamelles marinées sur une pique à brochette et les griller au four donne un résultat très proche."],
  keep="Marinade seule, 4 jours au frigo ; poulet mariné, 2 jours cru.", age=3, kids="✓ dès 3 ans.",
  cats=["sauces"], profil=["acide"], credit=C(V("lesgourmandisesdeloubna", "7608906113584614689")))
K("velveting_poulet_chinois", "Velouté de poulet à la chinoise (marinade pour sauté au wok)", "Velveting", "Asie de l'Est › Chine", "Ba", 2, 4, 10, 20, "€",
  "Saladier, wok.",
  "La technique des restaurants chinois qui rend le poulet bluffant de tendreté dans un sauté au wok : une courte "
  "marinade à la fécule, au blanc d'œuf et à une pincée de bicarbonate, qui forme une fine enveloppe protectrice "
  "autour de chaque morceau pendant la cuisson très vive.",
  [f"500 g|de blanc de poulet, en fines lanières|{BLANC_P}|3", f"1|blanc d'œuf|Blanc d'œuf|2",
   f"2 c. à c.|de fécule de maïs (maïzena)|Fécule de maïs (maïzena)|2", f"1 c. à s.|de sauce soja claire|{SOJA}|1",
   f"1/4 c. à c.|de bicarbonate de soude|Bicarbonate de soude|1", f"1 c. à c.|d'huile de sésame|Huile de sésame (grillée)|1?",
   f"-|poivre blanc|{POIVRE}|1?"],
  ["**Mélanger.** Poulet, blanc d'œuf, fécule, soja, bicarbonate et huile de sésame mélangés à la main dans un "
   "saladier jusqu'à ce que chaque lanière soit uniformément enrobée d'une pellicule légèrement collante.",
   "**Reposer.** 20 à 30 min au frigo (pas plus d'une heure : le bicarbonate finirait par rendre la texture trop "
   "molle).",
   "**Pré-cuire.** Juste avant le sauté : lanières plongées 30 à 45 secondes dans l'eau frémissante ou l'huile "
   "tiède (120 °C), séparées à la spatule, puis égouttées — c'est cette étape qui « scelle » l'enveloppe.",
   "**Sauter.** Ajoutées en toute fin dans le wok très chaud avec la sauce du plat, 1 à 2 min seulement : elles "
   "restent moelleuses et nacrées, jamais sèches, même en les réchauffant."],
  tips=["Le bicarbonate est la vraie astuce : il attendrit les fibres en quelques minutes, mais une pincée "
        "suffit — trop en mettre donne un goût savonneux.", "Cette marinade est une étape technique, pas un plat "
        "en soi : elle se termine toujours par un sauté au wok avec d'autres ingrédients et une sauce."],
  keep="Poulet enrobé cru, 4 h au frigo avant la pré-cuisson.", age=3, kids="✓ dès 3 ans.", cats=["sauces"],
  profil=["acide"], credit=C(V("wokundgluck", "7578490268094057750")))
K("bbq_rub_americain", "BBQ rub américain (épices sèches, sans marinade liquide)", "BBQ dry rub", US, "Ba", 1, 10, 10, 30, "€",
  "Bol, fouet ou bocal à secouer.",
  "Le troisième geste du coin marinades, après la marinade liquide et le cure à sec du gravlax : un mélange "
  "d'épices et de sucre roux appliqué sec, sans aucun liquide, qui forme une croûte parfumée et caramélisée à la "
  "cuisson lente au four ou au barbecue — la base de toutes les côtes de porc et poitrines fumées américaines.",
  [f"2 c. à s.|de paprika|{PAPRIKA}|2", f"1 c. à s.|de paprika doux (ou fumé)|{PFUME}|1",
   f"1/2 c. à c.|de piment de Cayenne (facultatif)|{CAYENNE}|1?", f"4 c. à s.|de sucre roux (cassonade)|{SUCRE}|2",
   f"1 c. à s.|de sel|{SEL}|1", f"1 c. à c.|de poivre noir moulu|{POIVRE}|1", f"1/2 c. à c.|de cumin moulu|{CUMIN}|1",
   f"2 c. à s.|de poudre d'ail et d'oignon mélangées|Poudre d'ail / d'oignon|1"],
  ["**Mélanger.** Tous les ingrédients mélangés ensemble dans un bol, en écrasant les éventuels grumeaux de "
   "cassonade à la fourchette.",
   "**Conserver.** Versé dans un bocal hermétique à l'abri de la lumière : il se garde plusieurs mois, comme un "
   "mélange d'épices.",
   "**Appliquer.** Massé généreusement sur la viande crue et bien sèche (jamais mouillée, sinon il ne forme pas "
   "de croûte), sur toutes les faces ; laissé reposer à température ambiante 30 min à 1 h avant de cuire, ou "
   "toute une nuit au frigo pour une pièce épaisse.",
   "**Cuire.** Au four très doux (110-130 °C, 3 à 5 h selon l'épaisseur), ou au barbecue à couvercle fermé le même "
   "temps : le sucre caramélise lentement en une croûte sombre et collante (le fameux « bark »), sans jamais brûler "
   "à cette température."],
  tips=["Contrairement à une marinade liquide, le rub n'attendrit pas la viande : c'est la cuisson longue et "
        "douce qui s'en charge, pas les épices.", "Se prépare en grande quantité à l'avance : il ne s'abîme pas "
        "au placard."],
  keep="6 mois dans un bocal fermé, à l'abri de la lumière.", age=3, kids="✓ dès 3 ans.", cats=["sauces"], profil=["epice", "sucre"],
  credit=C(V("jerome.cuisine", "7625975845227842819")))
K("marinade_vin_rouge", "Marinade au vin rouge (marinade crue, pour braisés et gibier)", "Marinade crue", FR_BISTROT, "Ba", 1, 8, 15, 720, "€",
  "Grand saladier ou sac de congélation, film alimentaire.",
  "La plus ancienne des marinades françaises, et la seule du coin à ne pas chercher à attendrir vite : carottes, "
  "oignon, ail et bouquet garni infusent une nuit entière dans du vin rouge avec la viande, qui en ressort "
  "parfumée et légèrement colorée, prête pour un civet ou un braisé long. C'est cette marinade, telle quelle, "
  "que suivent déjà le coq au vin, la daube provençale, le civet de lièvre et le lièvre à la royale.",
  [f"75 cl|de vin rouge corsé|Vin rouge|3", f"2|carottes, en rondelles|{CAROTTE}|1", f"2|oignons, émincés|{OIG}|1",
   f"4 gousses|d'ail, écrasées|{AIL}|1", f"1|bouquet garni (thym, laurier, persil)|{LAURIER}|1",
   f"1 c. à c.|de poivre en grains|{POIVRE}|1", f"2 c. à s.|d'huile|{HN}|1?"],
  ["**Préparer.** Vin, légumes, ail, bouquet garni et poivre mélangés dans un grand saladier ou un sac de "
   "congélation refermable.",
   "**Mariner.** Viande en morceaux (bœuf à braiser, gibier à poil ou à plumes) immergée dans le mélange, "
   "couverte ou fermée ; 12 à 24 h au frigo, en la retournant une ou deux fois si elle n'est pas totalement "
   "immergée.",
   "**Égoutter et éponger.** Viande sortie de la marinade, bien épongée avec du papier absorbant : elle doit "
   "être sèche pour bien dorer à la poêle, sans quoi elle bout au lieu de saisir.",
   "**Filtrer et garder.** Marinade filtrée, légumes réservés à part : ils serviront de base aromatique au "
   "braisé, et le vin filtré mouillera la cuisson — jamais cru, toujours porté à ébullition au moins 2 min avec "
   "le reste de la recette."],
  tips=["Contrairement aux marinades rapides du coin, celle-ci ne cherche pas à attendrir en quelques heures : "
        "c'est la cuisson longue qui s'en charge ensuite, la marinade ne fait que parfumer et commencer à "
        "assouplir les fibres.", "Un vin qu'on accepterait de boire donne toujours une meilleure marinade qu'un "
        "vin de cuisine industriel : pas besoin d'une grande bouteille, mais pas le fond d'une bouteille tournée "
        "non plus."],
  keep="Viande marinée, 2 jours crue au frigo dans sa marinade.", age=4,
  kids="Pour les grands à partir de 4 ans, dans un plat cuisiné (l'alcool s'évapore à la cuisson longue).",
  cats=["sauces"], profil=["acide"])
K("marinade_miso_aubergine", "Marinade miso-gingembre pour légumes à griller (aubergine, nasu dengaku)", "Dengaku", JP, "Ba", 1, 4, 10, 15, "€",
  "Bol, pinceau de cuisine.",
  "La marinade qui manquait aux légumes dans le coin Marinades, au-delà du tofu : un miso sucré-salé au sésame "
  "et au gochujang, badigeonné sur de l'aubergine quadrillée et passée au four jusqu'à fondante — le dengaku "
  "japonais, mais tout aussi bon sur du chou-fleur ou des champignons portobello entiers.",
  [f"2 c. à c.|de miso|Miso|2", f"2 c. à s.|d'huile de sésame|Huile de sésame (grillée)|2",
   f"2 c. à c.|de sucre|{SUCRE}|1", f"1 c. à s.|de sauce soja|{SOJA}|1", f"1 c. à c.|de gochujang|Gochujang|1?",
   f"1 c. à s.|d'huile pimentée|Huile pimentée chinoise|1?", f"1 c. à s.|de graines de sésame|Sésame (blanc/noir)|1?"],
  ["**Mélanger.** Miso, huile de sésame, sucre, sauce soja et gochujang fouettés ensemble en une pâte lisse, "
   "pour 2 aubergines ou un légume ferme équivalent.",
   "**Quadriller.** Aubergines coupées en deux dans la longueur, chair quadrillée au couteau sans percer la "
   "peau (la marinade pénètre mieux, la cuisson est plus régulière) ; légèrement salées 10 min puis épongées.",
   "**Badigeonner et cuire.** Chair huilée, cuite au four à 180 °C environ 15 min (chair tendre), puis "
   "badigeonnée généreusement de marinade au pinceau et remise 10 à 15 min : le dessus caramélise sans brûler.",
   "**Servir.** Graines de sésame et, si utilisée, une pointe d'huile pimentée par-dessus ; avec du riz."],
  tips=["Quadriller la chair sans percer la peau est le geste qui change tout : sans lui, l'aubergine reste "
        "ferme au centre pendant que le dessus caramélise déjà.", "La même marinade badigeonnée fonctionne très "
        "bien sur du chou-fleur en tranches épaisses ou des champignons portobello entiers."],
  keep="Marinade seule, 1 semaine au frigo.", age=2, kids="✓ dès 2 ans, sans gochujang ni huile pimentée.",
  cats=["sauces", "vegetarien"], profil=["sucre", "epice"], credit=C(V("chey__nese", "7235677059203206427")))
K("marinade_calamars_citron_persillade", "Marinade citron-persillade pour calamars et fruits de mer", "Calamares a la plancha", ES, "Ba", 1, 4, 15, 15, "€",
  "Poêle, bol.",
  "La marinade-sauce des calamars grillés à l'espagnole, servie des deux côtés : l'ail doucement infusé dans "
  "l'huile parfume d'abord la cuisson à la plancha, puis finit en vinaigrette citronnée persillée sur les "
  "calamars tout juste saisis — fonctionne aussi sur des moules ou des noix de Saint-Jacques poêlées.",
  [f"4 c. à s.|d'huile d'olive|{HO}|2", f"3 gousses|d'ail, hachées fin|{AIL}|1", f"1 c. à s.|de jus de citron|{CIT}|1",
   f"1/2 bouquet|de persil plat, haché|{PERSIL}|1", f"1 c. à c.|de paprika doux|{PAPRIKA}|1?", f"-|sel, poivre|{SEL}|1"],
  ["**Infuser l'huile.** Ail haché à froid dans l'huile, chauffé à feu moyen jusqu'à peine doré (il amère s'il "
   "brûle) ; retiré du feu aussitôt.",
   "**Finir la sauce.** Huile à l'ail tiédie, jus de citron, persil et paprika mélangés ; sel, poivre. Pour "
   "environ 600 g de calamars nettoyés, de moules décoquillées ou de noix de Saint-Jacques.",
   "**Saisir.** Calamars épongés, quadrillés côté intérieur, poêle ou plancha très chaude avec un filet de "
   "l'huile aromatisée ; 1 min par face pour une pièce moyenne — au-delà, ils deviennent caoutchouteux.",
   "**Napper.** Reste de la sauce versé sur les calamars tout juste saisis, servis aussitôt."],
  tips=["L'ail ne doit jamais frire : à peine doré et hors du feu, sinon toute la sauce devient amère.",
        "Calamars encore fermes après cuisson : les laisser tremper 30 à 60 min dans un peu de lait avant de les "
        "sécher et de les saisir attendrit la chair."],
  keep="Sauce seule, 2 jours au frigo ; fruits de mer marinés, à cuire le jour même.", age=3, kids="✓ dès 3 ans.",
  cats=["sauces"], profil=["acide"], credit=C(V("poesiadefogon", "7630912118165998870")))
