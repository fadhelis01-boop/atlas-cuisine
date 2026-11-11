# -*- coding: utf-8 -*-
"""Vague 9 (suite) · 11/11/2026 : autres recettes du profil TikTok d'@erynshow (659 vidéos chargées, les recettes les plus
vues ouvertes une à une ; le titre de la page donne le plat quand la légende est vague). Réécrites avec les repères ATLAS,
créditées. Les sandwichs à la charcuterie de porc et les vidéos de restaurant ne sont pas repris. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *
from recipes_v6_tiktok_plats import C

TT = "https://www.tiktok.com/"
def V(vid):
    return ("@erynshow", f"{TT}@erynshow/video/{vid}")

FF = "France › Food fusion"; IT = "Europe du Sud › Italie"
CHEVRE = "Chèvre (frais, bûche)"; BURRATA = "Mozzarella / burrata"; CEB = "Oignon nouveau / cébette"

K("pates_chevre_miel", "Pâtes crémeuses au chèvre, miel et thym", "Pasta chèvre-miel", FF, "P", 1, 4, 10, 12, "€", "Casserole, poêle.",
  "Une bûche de chèvre fondue avec un peu d'eau de cuisson et de crème, du miel, du thym et des noix : une sauce sucrée-salée qui enrobe les pâtes en dix minutes.",
  [f"350 g|de pâtes courtes|{PATES}|3", f"150 g|de bûche de chèvre|{CHEVRE}|3", f"10 cl|de crème|{CL}|2", f"2 c. à s.|de miel|{MIEL}|2", f"1 c. à c.|de thym|{THYM}|1", "40 g|de cerneaux de noix|Noix|1?", f"1|gousse d'ail|{AIL}|1", f"1 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Pâtes.** Eau bouillante salée, 1 min de moins que le paquet ; 20 cl d'eau de cuisson gardés.",
   "**Sauce.** Huile, ail râpé 30 s ; crème, chèvre en morceaux, 10 cl d'eau de cuisson, à feu doux : il fond, sauce lisse.",
   "**Lier.** Pâtes, thym, 1 min : brillantes, nappées (un peu d'eau si ça épaissit).",
   "**Finir.** Filet de miel, noix concassées, poivre."],
  tips=["Femme enceinte : chèvre au lait pasteurisé, bien chaud.", "Fruits à coque : allergène (noix)."], keep="1 jour au frigo.", age=1, cats=["vegetarien", "express", "enfants"], profil=["gras", "sucre"],
  credit=C(V("7676921325989940513")))
K("pates_burrata_pesto", "Pâtes au pesto et à la burrata", "Pasta burrata-pesto", IT, "P", 1, 4, 10, 12, "€€", "Casserole.",
  "Des pâtes liées au pesto avec un peu d'eau de cuisson, une burrata entière ouverte au centre au moment de servir : la crème du cœur se mêle aux pâtes chaudes.",
  [f"350 g|de pâtes (fusilli, linguine)|{PATES}|3", "1|burrata (125 g)|Mozzarella / burrata|3", "120 g|de pesto au basilic|Pesto (bocal)|2", "150 g|de tomates cerises|Tomate|1", f"30 g|de parmesan|{PARM}|1", "1|poignée de basilic|Basilic|1", f"1 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Pâtes.** Eau bouillante salée, al dente ; 15 cl d'eau de cuisson gardés.",
   "**Tomates.** Coupées en deux, 3 min à la poêle dans l'huile : éclatées.",
   "**Lier.** Hors du feu : pâtes, pesto, parmesan, eau de cuisson peu à peu : crémeuses (le pesto ne doit pas cuire).",
   "**Burrata.** Égouttée, posée au centre, ouverte à la cuillère ; tomates, basilic, poivre."],
  tips=["Pesto : souvent pignons ou noix de cajou (fruits à coque) ; burrata pasteurisée pour la femme enceinte."], keep="Le jour même.", age=1, cats=["vegetarien", "express", "enfants"], profil=["gras"],
  credit=C(V("7603832228673555734")))
K("burrata_pesto_rosso", "Burrata au pesto rosso et pain grillé", "Burrata pesto rosso", IT, "E", 1, 4, 10, 0, "€€", "Grille-pain.",
  "Une burrata posée sur un lit de pesto aux tomates séchées, huile d'olive, basilic et tranches de pain grillé : l'entrée sans cuisson qui fait tout le travail.",
  ["2|burratas (125 g)|Mozzarella / burrata|3", "100 g|de pesto rosso (tomates séchées)|Pesto (bocal)|2", "1|baguette ou pain de campagne|Baguette tradition|2", f"2 c. à s.|d'huile d'olive|{HO}|1", "1|poignée de basilic|Basilic|1", f"1|gousse d'ail|{AIL}|1"],
  ["**Burrata.** Sortie du frigo 20 min avant : plus crémeuse.",
   "**Pain.** Tranché, grillé, frotté d'ail.",
   "**Dresser.** Pesto étalé au fond de l'assiette, burrata au centre, huile, poivre, basilic.",
   "**Servir.** Ouverte à table, avec le pain."],
  tips=["Femme enceinte : burrata au lait pasteurisé."], keep="À manger tout de suite.", age=1, cats=["vegetarien", "express"], fetes=["Apéritif dînatoire"], profil=["gras", "acide"],
  credit=C(V("7682855665345367328")))
K("pates_crevettes_pesto_rosso", "Pâtes aux crevettes, pesto rosso et crème de balsamique", "Pasta crevettes-pesto rosso", FF, "P", 1, 4, 10, 15, "€€", "Casserole, poêle.",
  "Des crevettes saisies à l'ail et au piment d'Espelette, liées au pesto rosso et à l'eau de cuisson des pâtes, un trait de crème de balsamique pour finir.",
  [f"350 g|de pâtes (penne, linguine)|{PATES}|3", "300 g|de crevettes (crues ou cuites)|Crevettes (cuites/crues)|3", "100 g|de pesto rosso|Pesto (bocal)|2", f"1|oignon|{OIG}|1", f"2|gousses d'ail|{AIL}|1", "1 pincée|de piment d'Espelette|Piment d'Espelette|1", "1 c. à s.|de crème de balsamique|Vinaigre balsamique|1", f"2 c. à s.|d'huile d'olive|{HO}|1", "1|poignée de basilic|Basilic|1?"],
  ["**Pâtes.** Eau bouillante salée, 1 min de moins ; 20 cl d'eau de cuisson gardés.",
   "**Crevettes.** Huile, oignon émincé 3 min, ail ; crevettes crues 2 min (cuites : 30 s) : roses ; Espelette.",
   "**Lier.** Pesto rosso, pâtes, eau de cuisson peu à peu, 1 min : nappées, brillantes.",
   "**Finir.** Crème de balsamique en filet, basilic."],
  tips=["Crustacés : allergène majeur."], keep="1 jour au frigo.", age=3, cats=["express"], profil=["poisson", "acide"],
  credit=C(V("7657627646884384032")))
K("pates_riz_sautees_carottes", "Pâtes de riz sautées aux carottes et à l'œuf", "Pâtes de riz sautées", "Asie de l'Est › Chine", "P", 1, 2, 15, 8, "€", "Wok ou grande poêle.",
  "Des nouilles de riz larges sautées avec beaucoup de carottes en julienne, de l'œuf brouillé et de la cébette, dans une sauce soja sucrée : le plat de la flemme, économique et complet.",
  ["200 g|de nouilles de riz larges|Nouilles de riz / vermicelles|3", f"3|carottes|{CAROTTE}|3", f"2|œufs|{OEUF}|2", f"2|cébettes|{CEB}|1", f"2|gousses d'ail|{AIL}|1", f"3 c. à s.|de sauce soja|{SOJA}|2", "1 c. à s.|de kecap manis (ou soja + miel)|Kecap manis|1", f"1 c. à c.|d'huile de sésame|Huile de sésame (grillée)|1", f"2 c. à s.|d'huile|{HN}|1"],
  ["**Nouilles.** Trempées dans l'eau chaude selon le paquet : souples, encore fermes ; égouttées, huilées.",
   "**Œufs.** Brouillés dans le wok, en gros morceaux ; réservés.",
   "**Carottes.** En julienne, ail, 3 min : tendres et croquantes.",
   "**Sauter.** Nouilles, soja, kecap, 3 c. à s. d'eau, 2 min en soulevant ; œufs, cébette, sésame."],
  keep="1 jour au frigo.", age=2, cats=["vegetarien", "express", "enfants"], profil=["sucre"],
  credit=C(V("7662075997679930656")))
K("gyozas_poulet_cheddar", "Gyozas poulet-cheddar (raviolis grillés-vapeur)", "Gyozas cheddar", FF, "P", 2, 4, 40, 10, "€", "Poêle avec couvercle.",
  "Le gyoza revisité : une farce de poulet haché, cébette et cheddar fondant, plissée dans des feuilles à gyoza, grillée puis cuite à la vapeur dans la poêle. Avec une sauce soja-vinaigre.",
  ["30|feuilles à gyoza|Pâte à gyoza / wonton|3", "300 g|de poulet haché|Blanc de poulet|3", "100 g|de cheddar râpé|Cheddar|2", f"2|cébettes|{CEB}|1", f"1 cm|de gingembre|{GING}|1", f"2 c. à s.|de sauce soja (+ 3 pour la sauce)|{SOJA}|1", "2 c. à s.|de vinaigre de riz|Vinaigre de riz|1", f"2 c. à s.|d'huile|{HN}|1"],
  ["**Farce.** Poulet, cheddar, cébette, gingembre, 2 c. à s. de soja : collante.",
   "**Plier.** 1 c. à c. de farce, bord humecté, 5 plis d'un côté pressés contre l'autre.",
   "**Cuire.** Poêle huilée, gyozas serrés, 2 min : dessous doré ; 10 cl d'eau, couvercle, 6 min ; découvert 1 min : croustillants, farce à 75 °C.",
   "**Sauce.** Soja, vinaigre, à part."],
  keep="Crus : 1 mois au congélateur (cuits sans décongeler, 2 min de vapeur en plus).", age=2, cats=["enfants"], profil=["gras"],
  credit=C(V("7676557467786038561")))
K("raviolis_boeuf_fromage", "Raviolis bœuf-fromage maison (feuilles à raviolis, poêlés)", "Raviolis bœuf-fromage", FF, "P", 2, 4, 40, 10, "€€", "Poêle avec couvercle.",
  "Des demi-lunes de pâte à raviolis farcies de bœuf haché épicé et de mozzarella, poêlées puis cuites à la vapeur : un cœur juteux et filant, à tremper dans une sauce soja ou une sauce tomate.",
  ["30|feuilles à raviolis ou à gyoza|Pâte à gyoza / wonton|3", "300 g|de bœuf haché|Bœuf haché|3", "120 g|de mozzarella râpée|Mozzarella / burrata|2", f"1/2|oignon|{OIG}|1", f"1|gousse d'ail|{AIL}|1", f"1 c. à c.|de paprika|{PAPRIKA}|1", f"1 c. à s.|de sauce soja|{SOJA}|1", f"2 c. à s.|d'huile|{HN}|1"],
  ["**Farce.** Bœuf, oignon râpé, ail, paprika, soja, poivre ; mozzarella.",
   "**Plier.** 1 c. à c. de farce, bord humecté, refermé en demi-lune en chassant l'air.",
   "**Cuire.** Poêle huilée, 2 min ; 10 cl d'eau, couvercle, 6 min ; découvert 1 min : dessous croustillant, farce cuite (70 °C).",
   "**Servir.** Sauce soja-vinaigre ou sauce tomate."],
  keep="Crus : 1 mois au congélateur.", age=2, cats=["enfants"], profil=["viande_rouge", "gras"],
  credit=C(V("7624581491091066134")))
K("nam_tok_boeuf", "Salade thaïe de bœuf grillé au riz grillé (nam tok)", "Nam tok neua", "Asie du Sud-Est › Thaïlande", "P", 1, 2, 20, 10, "€€", "Poêle en fonte, poêle sèche, mortier.",
  "Le bœuf grillé tranché, mêlé encore tiède à une sauce citron vert-nuoc-mâm-piment, à l'échalote, aux herbes et à la poudre de riz grillé qui donne son goût toasté. Avec du riz gluant et des crudités.",
  ["350 g|de bavette ou de rumsteck|Bavette|3", "1 c. à s.|de riz gluant cru|Riz gluant|2", "2 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|2", f"2|citrons verts|{CITV}|2", f"1 c. à c.|de sucre|{SUCRE}|1", "1 c. à c.|de flocons de piment|Flocons de piment|1", f"2|échalotes|{ECH}|1", "1|petite botte de menthe|Menthe|1", f"1/2|botte de coriandre|{CORI}|1", f"2|cébettes|{CEB}|1"],
  ["**Riz grillé.** Riz gluant 5 min à la poêle sèche : doré ; pilé en poudre grossière (avant, sinon il ne croque pas).",
   "**Griller.** Bœuf salé, fonte fumante, 3 min par face : saignant à rosé ; 5 min de repos, tranches fines.",
   "**Sauce.** Nuoc-mâm, citron vert, sucre, piment ; jus de la viande.",
   "**Mélanger.** Bœuf tiède, sauce, échalotes émincées, herbes, cébette, riz grillé ; aussitôt."],
  tips=["Pour les enfants : sans piment, viande bien cuite."], keep="Le jour même.", age=3, cats=["leger"], profil=["viande_rouge", "acide", "epice", "leger"],
  credit=C(V("7655001470881844512")))
K("chevre_miel_barbecue", "Chèvre au miel en papillote au barbecue", "Chèvre-miel BBQ", FF, "E", 1, 4, 10, 10, "€", "Barbecue ou four, papier aluminium.",
  "Des rondelles épaisses de bûche de chèvre en papillote avec du miel, du thym, des noix et un peu de piment, posées sur la grille : elles fondent en dix minutes, à étaler sur du pain grillé.",
  ["1|bûche de chèvre (180 g)|Chèvre (frais, bûche)|3", f"2 c. à s.|de miel|{MIEL}|2", f"1 c. à c.|de thym|{THYM}|1", "30 g|de cerneaux de noix|Noix|1?", "1 pincée|de piment d'Espelette|Piment d'Espelette|1?", "1|baguette|Baguette tradition|2", f"1 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Papillotes.** Bûche en 4 rondelles de 3 cm, chacune sur un carré d'aluminium huilé.",
   "**Garnir.** Miel, thym, noix, Espelette ; papillote fermée en laissant de l'air.",
   "**Cuire.** Sur la grille, braise moyenne (ou four 200 °C), 8 à 10 min : le chèvre s'affaisse, fondant.",
   "**Servir.** Ouvert, avec le pain grillé sur la braise."],
  tips=["Femme enceinte : chèvre pasteurisé, bien chaud.", "Fruits à coque : allergène (noix)."], keep="À manger tout de suite.", age=1, cats=["vegetarien"], fetes=["Barbecue d'été", "Apéritif dînatoire"], profil=["gras", "sucre"],
  credit=C(V("7648737287857032481")))
K("sandwich_champignons_chevre", "Sandwich chaud aux champignons et au chèvre", "Sandwich champi-chèvre", FF, "P", 1, 2, 10, 12, "€", "Poêle, four en position grill.",
  "Des champignons poêlés à l'ail et au persil, du chèvre et un filet de miel dans une baguette passée sous le grill : le sandwich chaud, végétarien et fondant.",
  ["1|baguette|Baguette tradition|3", "300 g|de champignons de Paris|Champignon de Paris|3", "120 g|de bûche de chèvre|Chèvre (frais, bûche)|2", f"1|gousse d'ail|{AIL}|1", f"1/2|botte de persil|{PERSIL}|1", f"20 g|de beurre|{BEURRE}|1", f"1 c. à s.|de miel|{MIEL}|1?", "1|poignée de roquette ou de salade|Salade (laitue, batavia)|1"],
  ["**Champignons.** Émincés, poêle chaude, beurre, 6 min sans remuer au début : dorés, l'eau évaporée ; ail, persil, sel.",
   "**Garnir.** Baguette coupée en deux et ouverte, champignons, chèvre en rondelles.",
   "**Gratiner.** Sous le grill, 4 min : chèvre fondu, doré par endroits ; miel.",
   "**Servir.** Salade, refermé."],
  tips=["Femme enceinte : chèvre pasteurisé, bien chaud."], keep="À manger tout de suite.", age=2, cats=["vegetarien", "express"], profil=["gras"],
  credit=C(V("7586268148878298390")))
K("mont_dor_champignons_epinards", "Mont-d'or au four, champignons et épinards", "Mont-d'or garni", "France › Franche-Comté", "P", 1, 4, 15, 25, "€€€", "Four, poêle.",
  "Le mont-d'or rôti dans sa boîte, garni de champignons et d'épinards poêlés, à servir avec des pommes de terre et du pain : la fondue de l'hiver, sans appareil.",
  ["1|mont-d'or (500 g)|Reblochon / raclette / mont-d'or|3", "250 g|de champignons de Paris|Champignon de Paris|2", "200 g|de pousses d'épinards|Épinard|2", f"1|gousse d'ail|{AIL}|1", f"20 g|de beurre|{BEURRE}|1", "1 kg|de pommes de terre|Pomme de terre|3", "1|baguette|Baguette tradition|1"],
  ["**Pommes de terre.** En robe des champs, 25 min à l'eau salée.",
   "**Garniture.** Champignons émincés au beurre 6 min : dorés ; ail, épinards 1 min : tombés ; sel, poivre.",
   "**Mont-d'or.** Boîte emballée d'aluminium au fond, croûte entaillée en croix, garniture enfoncée dans la pâte ; four 200 °C, 20 min : coulant, bouillonnant.",
   "**Servir.** À la cuillère sur les pommes de terre et le pain."],
  tips=["Mont-d'or : fromage au lait cru, déconseillé à la femme enceinte et aux enfants de moins de 5 ans même cuit (prends une version pasteurisée)."], keep="Le jour même.", age=5, cats=["vegetarien"], fetes=["Repas de famille", "Noël"], profil=["gras"],
  kids="✓ dès 5 ans (lait cru) ; plus jeunes : un fromage à pâte molle pasteurisé.",
  credit=C(V("7572650283080191254")))
K("sorbet_coco_antillais", "Sorbet coco à l'antillaise (sans sorbetière)", "Sorbet coco", "France › Outre-mer › Antilles", "D", 1, 6, 15, 300, "€", "Moule, fourchette ou mixeur.",
  "Le sorbet coco des plages antillaises, parfumé à la cannelle, à la muscade et au citron vert : lait de coco et lait concentré mélangés, congelés, griffés à la fourchette toutes les heures jusqu'à être crémeux.",
  ["40 cl|de lait de coco|Lait de coco / crème de coco|3", "200 g|de lait concentré sucré|Lait concentré sucré / non sucré|3", f"20 cl|de lait|{LAIT}|1", f"1|citron vert (zeste)|{CITV}|1", f"1/2 c. à c.|de cannelle|{CANN}|1", f"1 pincée|de muscade|{MUSC}|0", f"1 c. à c.|de vanille|{VAN}|1"],
  ["**Mélanger.** Tout au fouet : lisse.",
   "**Congeler.** Dans un moule plat, 1 h au congélateur.",
   "**Griffer.** Toutes les heures, 3 ou 4 fois, à la fourchette (ou 20 s au mixeur) : les cristaux se cassent, il devient crémeux.",
   "**Servir.** 10 min à température ambiante avant."],
  keep="2 semaines au congélateur.", age=1, cats=["vegetarien", "enfants"], fetes=["Barbecue d'été"], profil=["sucre"],
  credit=C(V("7592699798273182998")))
