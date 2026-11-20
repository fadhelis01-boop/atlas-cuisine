# -*- coding: utf-8 -*-
"""Coin marinades (audit UI/UX senior, 20/11/2026) : la rubrique Marinades n'avait que 7 bases dispersées dans les
sauces et condiments, aucune pour l'agneau, les crevettes ou le tofu, et aucune n'expliquait le geste du cure à sec
(gravlax) à côté de la marinade liquide classique. 6 fiches nouvelles comblent ces angles morts, chacune réutilisable
sur n'importe quelle pièce de viande/poisson du même type, pas liée à un seul plat fini. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

MAG = "Afrique du Nord › Maghreb"; CU = "Amérique latine & Caraïbes › Cuba"; VN = "Asie du Sud-Est › Vietnam"
MX = "Amérique latine › Mexique"; CN = "Asie de l'Est › Chine"; SU = "Europe du Nord › Suède"
GAMBAS = "Gambas / bouquet"; AGNEAU_MORCEAUX = "Gigot d'agneau"
FILET_PORC = "Filet mignon de porc"; CITRONNELLE = "Citronnelle"; NUOCMAM = "Sauce de poisson (nuoc-mâm, nam pla)"
TOFU_F = "Tofu (ferme / soyeux)"; SAUMON_PAVE = "Saumon (frais, pavé)"; HARISSA = "Harissa (tube/pâte)"

K("harissa_marinade_agneau", "Marinade harissa-citron pour agneau (Maghreb)", "Marinade pour agneau grillé", MAG, "Ba", 1, 6, 10, 240, "€",
  "Saladier, fouet.",
  "La marinade qui manquait au coin marinades pour l'agneau : harissa, citron, cumin et coriandre, pour des "
  "brochettes, un gigot en morceaux ou des côtelettes grillées. Elle attendrit autant qu'elle parfume.",
  [f"3 c. à s.|de harissa|{HARISSA}|2", f"4 c. à s.|d'huile d'olive|{HO}|2", f"1|citron (jus et zeste)|{CIT}|1",
   f"4 gousses|d'ail, écrasées|{AIL}|1", f"1 c. à c.|de cumin|{CUMIN}|1", f"1/2 bouquet|de coriandre, hachée|{CORI}|1",
   f"1 c. à c.|de miel|{MIEL}|1?", f"1 kg|d'agneau en morceaux ou en côtelettes (pour l'exemple)|{AGNEAU_MORCEAUX}|3",
   f"-|sel|{SEL}|1"],
  ["**Mélanger.** Harissa, huile, jus et zeste de citron, ail, cumin, coriandre et miel fouettés ensemble en une "
   "marinade homogène et bien rouge.",
   "**Entailler.** Pièces d'agneau légèrement entaillées en surface (elles absorbent mieux) ; enrobées "
   "généreusement de marinade avec les mains, dans un plat ou un sac de congélation.",
   "**Reposer.** Au moins 4 h au frigo, idéalement toute une nuit : la viande se détend et prend bien le goût. "
   "Sortie 20 min avant la cuisson pour revenir à température.",
   "**Griller.** Au barbecue, au gril de four ou à la poêle très chaude, selon la pièce et son épaisseur ; "
   "l'excédent de marinade est essuyé avant de griller (il brûlerait sinon)."],
  tips=["Plus elle repose longtemps (jusqu'à 24 h), plus l'agneau est parfumé et tendre : ne te presse pas sur "
        "ce point.", "Cette même marinade convient aussi au poulet ou au bœuf à griller."],
  keep="Marinade seule, 5 jours au frigo ; viande marinée, 2 jours crue ou cuite.", age=3,
  kids="✓ dès 3 ans, en version moins pimentée (moitié moins de harissa).", cats=["sauces"], profil=["epice", "acide"])
K("mojo_cubain_porc", "Mojo cubain pour porc (ail, citron vert, cumin, origan)", "Mojo criollo", CU, "Ba", 1, 6, 10, 180, "€",
  "Saladier, fouet.",
  "La marinade de tous les rôtis de porc cubains : beaucoup d'ail, du citron vert, du cumin et de l'origan dans "
  "l'huile d'olive, qui pénètre la viande et donne au porc rôti ou grillé son goût si reconnaissable des "
  "Caraïbes.",
  [f"12 gousses|d'ail, écrasées en pâte|{AIL}|2", f"4|citrons verts (jus)|Citron vert|2", f"1|orange (jus)|Orange|1",
   f"10 cl|d'huile d'olive|{HO}|2", f"2 c. à c.|de cumin|{CUMIN}|1", "1 c. à c.|d'origan séché|Origan frais / sec|1",
   f"1 kg|de filet ou d'épaule de porc (pour l'exemple)|{FILET_PORC}|3", f"-|sel, poivre|{SEL}|1"],
  ["**Pâte d'ail.** Ail écrasé au plat du couteau avec une pincée de gros sel jusqu'à une pâte lisse (ça évite les "
   "morceaux d'ail brûlé à la cuisson).",
   "**Mélanger.** Pâte d'ail, jus de citron vert et d'orange, huile, cumin et origan fouettés ensemble ; sel, "
   "poivre.",
   "**Entailler et mariner.** Viande piquée de petits trous au couteau (la marinade pénètre plus profond) ; "
   "enrobée généreusement ; au moins 3 h au frigo, mieux toute une nuit pour une pièce épaisse.",
   "**Cuire.** Rôtie au four ou grillée selon la pièce, arrosée de marinade restante en début de cuisson "
   "seulement (jamais en fin, sur une viande déjà cuite, à cause du porc cru qui y a trempé)."],
  tips=["Le mélange citron vert + orange est la vraie signature du mojo : le citron vert seul est plus acide et "
        "moins rond.", "Sans porc : le même mojo convient très bien au poulet ou aux crevettes, temps de repos "
        "divisé par deux."],
  var=[("Sans porc", ["pork"], {FILET_PORC: [("Cuisse / pilon de poulet", 1.0)]}, "Porc → **poulet**, même marinade, repos réduit à 1 h 30. **À tester**.")],
  keep="Marinade seule, 5 jours au frigo ; viande marinée, 2 jours crue.", age=2, kids="✓ dès 2 ans.",
  cats=["sauces"], profil=["acide"])
K("porc_citronnelle_vietnamien", "Marinade vietnamienne à la citronnelle (bò/thịt nướng xả)", "Thịt nướng xả", VN, "Ba", 1, 6, 15, 120, "€",
  "Mixeur ou mortier, saladier.",
  "La marinade des grillades de rue vietnamiennes : citronnelle pilée, ail, échalote, sauce poisson et sucre, "
  "pour du porc, du poulet ou du bœuf coupé fin, grillé fumant sur un vermicelle froid ou dans un bánh mì.",
  [f"3 tiges|de citronnelle, cœur tendre haché fin|{CITRONNELLE}|2", f"4 gousses|d'ail, hachées|{AIL}|1",
   f"2|échalotes, hachées|{ECH}|1", f"3 c. à s.|de sauce de poisson|{NUOCMAM}|2", f"2 c. à s.|de cassonade|{SUCRE}|1",
   f"2 c. à s.|d'huile|{HN}|1", f"1 c. à c.|de poivre noir moulu|{POIVRE}|1",
   f"800 g|de porc, de poulet ou de bœuf, en fines tranches (pour l'exemple)|{FILET_PORC}|3"],
  ["**Piler.** Citronnelle, ail et échalote pilés au mortier ou mixés avec un peu d'huile jusqu'à une pâte "
   "grossière et parfumée : c'est elle qui porte tout le goût.",
   "**Mélanger.** Pâte de citronnelle, sauce poisson, cassonade, huile et poivre mélangés en une marinade "
   "épaisse.",
   "**Mariner.** Viande en tranches fines enrobée généreusement ; 1 h à 2 h au frigo suffisent (les tranches "
   "fines prennent vite le goût, inutile de laisser toute une nuit).",
   "**Griller.** Très vif, à la poêle, au gril ou au barbecue, par petites fournées sans entasser : 2 à 3 min par "
   "face, bords caramélisés et légèrement noircis par endroits (c'est voulu, ça fait le goût fumé)."],
  tips=["Des tranches fines et toutes de la même épaisseur grillent uniformément en quelques minutes : demande "
        "au boucher si besoin.", "Cette marinade convient à peu près à toutes les viandes à griller : porc, "
        "poulet, bœuf, même un tofu ferme pour une version végétarienne."],
  var=[("Sans porc", ["pork"], {FILET_PORC: [("Cuisse / pilon de poulet", 1.0)]}, "Porc → **poulet ou bœuf**, mêmes proportions. **À tester**.")],
  keep="Marinade seule, 4 jours au frigo ; viande marinée, 1 jour crue.", age=3, kids="✓ dès 3 ans.",
  cats=["sauces"], profil=["acide", "sucre"])
K("crevettes_citron_vert_marinade", "Marinade ail-citron vert pour crevettes grillées", "Camarones al mojo de ajo", MX, "Ba", 1, 6, 10, 20, "€",
  "Saladier.",
  "La marinade express des crevettes de bord de mer mexicaines : ail, citron vert, piment et coriandre, à peine "
  "20 minutes de repos (les crustacés n'en demandent pas plus), puis une poêle brûlante.",
  [f"4 gousses|d'ail, écrasées|{AIL}|2", f"2|citrons verts (jus)|Citron vert|2", f"3 c. à s.|d'huile d'olive|{HO}|1",
   f"1/2 c. à c.|de piment en poudre|{CAYENNE}|1?", f"1/2 bouquet|de coriandre, hachée|{CORI}|1?",
   f"700 g|de grosses crevettes décortiquées (pour l'exemple)|{GAMBAS}|3", f"-|sel|{SEL}|1"],
  ["**Mélanger.** Ail, jus de citron vert, huile, piment et coriandre fouettés ensemble.",
   "**Mariner court.** Crevettes enrobées de marinade, sel ; 15 à 20 min au frigo au maximum : plus longtemps, "
   "l'acidité du citron commence à « cuire » la chair comme un ceviche et elle devient élastique à la cuisson.",
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
