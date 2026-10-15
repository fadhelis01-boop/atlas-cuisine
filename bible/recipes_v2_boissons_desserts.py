# -*- coding: utf-8 -*-
"""Vague 2 · Boissons (sans alcool : cocktails, limonades, boissons chaudes du monde) et desserts simples."""
from recipes_v2_base import *

BX = "France › Boissons maison"; DS = "France › Desserts simples"

def drink(id, title, origin, region, intro, ing, steps, age=1, cats=("boissons", "enfants"), fetes=(), profil=("sucre",), kids=None, keep="À boire tout de suite.", tips=()):
    K(id, title, origin, region, "B", 1, 4, 10, 0, "€", "Pichet, cuillère, glaçons.", intro, ing, steps, age=age, cats=list(cats), fetes=list(fetes), profil=list(profil), kids=kids, keep=keep, tips=tips)

drink("virgin_mojito", "Virgin mojito", "Mojito sin alcohol", "Amérique latine & Caraïbes › Cuba",
  "Menthe fraîche pilée, citron vert, sucre de canne et eau pétillante : toute la fraîcheur du mojito, sans rhum.",
  ["20|feuilles de menthe|Menthe|3", f"2|citrons verts|{CITV}|3", "4 c. à s.|de sucre de canne|Sucre blanc / roux / cassonade / vergeoise|2", "1 L|d'eau pétillante|-|0", "1 grand verre|de glace pilée|-|0"],
  ["**Piler.** Menthe, citron vert en quartiers et sucre dans le pichet (sans broyer les feuilles).", "**Allonger.** Glace pilée, eau pétillante, remue."], fetes=["Barbecue d'été", "Anniversaire"], profil=("acide", "sucre"))
drink("limonade_maison", "Limonade maison", "Limonade", BX,
  "Citrons pressés, sirop de sucre et eau gazeuse : acidulée et vraiment désaltérante.",
  [f"4|citrons|{CIT}|3", f"100 g|de sucre|{SUCRE}|2", "1 L|d'eau gazeuse froide|-|0", "4|feuilles de menthe ou de basilic|Menthe|1?"],
  ["**Sirop.** Sucre + 10 cl d'eau chaude + zeste d'un citron, refroidi.", "**Mélanger.** Jus, sirop, eau gazeuse, glace."], fetes=["Barbecue d'été", "Anniversaire"], profil=("acide", "sucre"))
drink("the_glace_peche", "Thé glacé à la pêche maison", "Thé glacé", BX,
  "Thé infusé à froid toute la nuit (jamais amer), pêches mûres et un peu de miel.",
  ["4 sachets|de thé noir ou vert|Thé noir fumé (lapsang)|2", "2|pêches mûres|Pêche / nectarine|3", f"2 c. à s.|de miel|{MIEL}|1", f"½|citron|{CIT}|1", "1 L|d'eau froide|-|0"],
  ["**Infuser à froid.** Thé dans l'eau froide, 8 h au frigo.", "**Pêches.** Mixées avec miel et citron, filtrées, mélangées au thé."], age=None, kids="Contient de la théine : plutôt dès 12 ans (ou version rooibos pour les petits).", keep="2 jours au frigo.")
drink("horchata", "Horchata de riz à la cannelle", "Horchata de arroz", "Amérique latine & Caraïbes › Mexique",
  "Une boisson lactée végétale de riz trempé, cannelle et vanille, servie très froide.",
  ["150 g|de riz long|Riz long / basmati / thaï|3", f"1|bâton de cannelle|{CANN}|2", f"80 g|de sucre|{SUCRE}|2", "1 L|d'eau|-|0", f"1 pincée|de vanille|{VAN}|1"],
  ["**Tremper.** Riz + cannelle dans 50 cl d'eau chaude, une nuit.", "**Mixer.** Longtemps, filtrer finement ; reste d'eau, sucre, vanille. Très froid."], keep="3 jours au frigo.")
drink("agua_fresca_pasteque", "Agua fresca pastèque-citron vert", "Agua fresca de sandía", "Amérique latine & Caraïbes › Mexique",
  "Pastèque mixée, citron vert, un peu d'eau : la boisson des marchés mexicains.",
  ["1 kg|de pastèque|Melon / pastèque|3", f"2|citrons verts|{CITV}|2", "50 cl|d'eau froide|-|0", f"2 c. à s.|de sucre (selon goût)|{SUCRE}|0?", "4|feuilles de menthe|Menthe|0?"],
  ["**Mixer.** Pastèque sans graines, filtrée ; citron, eau, sucre. Glace."], fetes=["Barbecue d'été"], profil=("leger", "sucre"))
drink("ginger_beer", "Ginger beer maison (sans alcool, express)", "Ginger beer", "Europe du Nord & Centrale › Royaume-Uni",
  "Un sirop de gingembre frais, citron et sucre allongé d'eau gazeuse : piquant et rafraîchissant, sans fermentation.",
  [f"100 g|de gingembre frais|{GING}|3", f"150 g|de sucre|{SUCRE}|2", f"2|citrons verts|{CITV}|2", "1 L|d'eau gazeuse|-|0"],
  ["**Sirop.** Gingembre râpé + sucre + 25 cl d'eau, 10 min ; infuse 30 min ; filtre.", "**Servir.** 1 volume de sirop, 3 d'eau gazeuse, citron vert, glace."], keep="Sirop : 2 semaines au frigo.", profil=("epice", "sucre"))
drink("sirop_menthe_maison", "Sirop de menthe fraîche (sans colorant)", "Sirop de menthe", BX,
  "La vraie menthe infusée dans un sirop : vert pâle naturel et goût franc. Avec de l'eau fraîche ou du lait (diabolo, menthe-lait).",
  ["1 gros bouquet|de menthe|Menthe|3", f"500 g|de sucre|{SUCRE}|3", "50 cl|d'eau|-|0", f"½|citron|{CIT}|1"],
  ["**Infuser.** Menthe dans l'eau bouillante hors du feu, 1 h (ou une nuit).", "**Sirop.** Filtre, sucre, 5 min de frémissement, citron. Bouteille."], keep="1 mois au frigo.")
drink("punch_fruits", "Punch de fruits sans alcool", "Punch", "France › Outre-mer › Antilles",
  "Jus de fruits exotiques, sirop de canne, citron vert, cannelle et muscade : le punch des fêtes, pour tous.",
  ["50 cl|de jus d'ananas|Ananas|3", "50 cl|de jus de goyave ou de mangue|Goyave / litchi|2", "25 cl|de jus d'orange|Orange|2", f"2|citrons verts|{CITV}|2", "4 c. à s.|de sirop de canne|Mélasse / sirop de canne|1", f"1 pincée|de cannelle et de muscade|{CANN}|1", "50 cl|d'eau gazeuse|-|0"],
  ["**Mélanger.** Jus, sirop, épices, citron ; 2 h au frais.", "**Servir.** Eau gazeuse au dernier moment, fruits en dés."], fetes=["Anniversaire", "Noël", "Repas de famille"])
drink("sangria_sans_alcool", "Sangria sans alcool", "Sangría sin alcohol", "Europe du Sud › Espagne",
  "Jus de raisin rouge, orange, cannelle et fruits en morceaux qui marinent : couleur et goût de la sangria.",
  ["1 L|de jus de raisin rouge|Jus de raisin / pomme (pur jus)|3", "2|oranges|Orange|2", "1|pomme|Pomme|1", f"1|citron|{CIT}|1", f"1|bâton de cannelle|{CANN}|1", "50 cl|d'eau gazeuse|-|0"],
  ["**Macérer.** Jus, fruits en dés, cannelle, 4 h au frais.", "**Servir.** Eau gazeuse, glace."], fetes=["Barbecue d'été", "Repas de famille"])
drink("ayran", "Ayran (yaourt salé)", "Ayran", "Moyen-Orient & Caucase › Turquie",
  "Yaourt battu avec de l'eau fraîche et une pincée de sel, mousseux : la boisson des kebabs et des grillades.",
  [f"300 g|de yaourt|{YAO}|3", "30 cl|d'eau glacée|-|0", f"1 pincée|de sel|{SEL}|0", "4|feuilles de menthe (facultatif)|Menthe|0?"],
  ["**Fouetter.** Ou mixer jusqu'à mousseux."], profil=("leger",))
drink("cafe_frappe", "Café frappé grec", "Frappé", "Europe du Sud › Grèce",
  "Café soluble battu en mousse épaisse avec sucre et un peu d'eau, allongé d'eau glacée et de lait.",
  ["2 c. à c.|de café soluble|-|0", f"2 c. à c.|de sucre|{SUCRE}|1", f"5 cl|de lait|{LAIT}|1", "15 cl|d'eau glacée + glaçons|-|0"],
  ["**Mousser.** Café + sucre + 3 c. à s. d'eau au shaker ou mini-fouet : mousse ferme.", "**Servir.** Glaçons, eau, lait."], age=None, kids="Caféine : pour les adultes.", cats=("boissons",))
drink("lait_or", "Lait d'or (curcuma, gingembre, cannelle)", "Haldi doodh", "Asie du Sud › Inde",
  "Lait chaud au curcuma, gingembre, cannelle et poivre, adouci au miel : la boisson du soir.",
  [f"50 cl|de lait (ou lait végétal)|{LAIT}|3", f"1 c. à c.|de curcuma|{CURC}|2", f"1 morceau|de gingembre|{GING}|1", f"1 pincée|de cannelle + poivre|{CANN}|1", f"1 c. à c.|de miel|{MIEL}|1"],
  ["**Chauffer.** Tout sauf le miel, 5 min à frémissement ; filtre, miel."], profil=("epice",), kids="✓ dès 1 an (miel dès 1 an).")
drink("chocolat_mexicain", "Chocolat chaud mexicain à la cannelle", "Champurrado ligero", "Amérique latine & Caraïbes › Mexique",
  "Chocolat noir, cannelle et une pointe de piment, fouetté jusqu'à mousser : épicé et réconfortant.",
  [f"50 cl|de lait|{LAIT}|3", f"80 g|de chocolat noir|{CHOCO}|3", f"1|bâton de cannelle|{CANN}|2", f"1 c. à s.|de sucre|{SUCRE}|1", f"1 pincée|de piment (adultes)|{CAYENNE}|0?"],
  ["**Infuser.** Lait + cannelle, 5 min.", "**Fouetter.** Chocolat, sucre, mousse."], fetes=["Noël", "Halloween"])
drink("jus_vert", "Jus vert pomme-concombre-épinard", "Jus vert", BX,
  "Pomme, concombre, épinards, citron et gingembre mixés : fraîcheur et vitamines, sans extracteur.",
  ["2|pommes|Pomme|3", "1|concombre|Concombre|2", "1 poignée|d'épinards|Épinard|2", f"½|citron|{CIT}|1", f"1 petit morceau|de gingembre|{GING}|1", "20 cl|d'eau froide|-|0"],
  ["**Mixer.** Tout, 1 min ; filtre si tu veux un jus lisse (garde la pulpe pour un cake)."], cats=("boissons", "zero_dechet"), profil=("leger", "acide"))
drink("milkshake_vanille", "Milk-shake vanille-fraise", "Milkshake", "Amérique du Nord › États-Unis",
  "Glace vanille, lait froid et fraises mixés : épais, à la paille.",
  ["4 boules|de glace vanille|Crème fleurette (liquide)|3", f"30 cl|de lait froid|{LAIT}|3", "200 g|de fraises|Fraise|2"],
  ["**Mixer.** Tout, 30 s."], fetes=["Anniversaire"])

K("mousse_citron", "Mousse légère au citron", "Mousse au citron", DS, "D", 1, 6, 20, 180, "€", "Casserole, batteur.",
  "Une crème au citron allégée de crème fouettée : acidulée, aérienne, sans œuf cru.",
  [f"3|citrons|{CIT}|3", f"3|œufs|{OEUF}|2", f"120 g|de sucre|{SUCRE}|2", f"25 cl|de crème|{CL}|2", f"20 g|de maïzena|Fécule de maïs (maïzena)|1"],
  ["**Crème citron.** Jus + zestes, œufs, sucre, maïzena, épaissis sur feu doux ; refroidie.", "**Alléger.** Crème montée incorporée. 3 h au frais."], age=1, cats=["enfants"], profil=["acide", "sucre"], tech=["Chantilly"])

K("salade_fruits_menthe", "Salade de fruits frais au sirop de menthe", "Salade de fruits", DS, "D", 1, 6, 20, 30, "€", "Saladier.",
  "Fruits de saison en morceaux, sirop léger citron-menthe : le dessert le plus frais.",
  ["1 kg|de fruits de saison|Fraise|3", f"50 g|de sucre|{SUCRE}|1", f"1|citron|{CIT}|1", "10|feuilles de menthe|Menthe|1"],
  ["**Sirop.** Sucre + 10 cl d'eau chaude + menthe, refroidi.", "**Mélanger.** Fruits, citron, sirop, 30 min au frais."], age=1, cats=["enfants", "zero_dechet"], profil=["leger", "sucre"])

K("poires_belle_helene", "Poires Belle-Hélène", "Poires Belle-Hélène", DS, "D", 1, 4, 20, 25, "€€", "Casserole.",
  "Poires pochées à la vanille, boule de glace vanille et sauce chocolat chaude : le classique d'Escoffier.",
  ["4|poires|Poire|3", f"150 g|de sucre|{SUCRE}|1", "1|gousse de vanille|Vanille (gousse)|1", f"150 g|de chocolat noir|{CHOCO}|2", f"15 cl|de crème|{CL}|1", "4 boules|de glace vanille|Crème fleurette (liquide)|2", "30 g|d'amandes effilées grillées|Amande (entière, effilée, poudre)|1"],
  ["**Pocher.** Poires pelées dans 1 L d'eau + sucre + vanille, 20 min ; refroidies.", "**Sauce.** Crème chaude sur chocolat.", "**Servir.** Poire, glace, sauce chaude, amandes."], age=1, cats=["enfants"], profil=["sucre"], tech=["Ganache"])

K("pommes_au_four", "Pommes au four, beurre et cassonade", "Pommes au four", DS, "D", 1, 4, 10, 35, "€", "Plat à four.",
  "Pommes évidées, garnies de beurre, cassonade, cannelle et raisins, rôties jusqu'à fondre dans leur jus caramélisé.",
  ["4|pommes (reinette, boskoop)|Pomme|3", f"40 g|de beurre|{BEURRE}|2", "4 c. à s.|de cassonade|Sucre blanc / roux / cassonade / vergeoise|2", "30 g|de raisins secs ou noix|Raisins secs|1", f"1 c. à c.|de cannelle|{CANN}|1"],
  ["**Évider.** Pommes entaillées en ceinture, cœur retiré.", "**Garnir.** Beurre, sucre, cannelle, raisins.", "**Cuire.** 35 min à 180 °C, arrose avec le jus."], age=1, cats=["enfants"], profil=["sucre"])

K("tarte_fine_pommes", "Tarte fine aux pommes", "Tarte fine aux pommes", DS, "D", 1, 6, 15, 30, "€", "Plaque.",
  "Feuilletage très fin, pommes en lamelles serrées, beurre et sucre : croustillant et caramélisé.",
  ["1|pâte feuilletée|Pâte feuilletée (prête)|3", "4|pommes|Pomme|3", f"30 g|de beurre fondu|{BEURRE}|1", f"3 c. à s.|de sucre|{SUCRE}|1", "2 c. à s.|de confiture d'abricot (nappage)|Confiture / gelée|1"],
  ["**Monter.** Pâte piquée, pommes en lamelles fines en rosace serrée.", "**Cuire.** Beurre, sucre, 30 min à 200 °C.", "**Napper.** Confiture chaude au pinceau."], age=1, cats=["enfants"], profil=["sucre"])

K("gateau_chocolat_famille", "Gâteau au chocolat de famille (sans balance)", "Gâteau au chocolat", DS, "G", 1, 8, 15, 30, "€", "Moule à manqué.",
  "Le gâteau au chocolat le plus simple : 1 tablette, 1 plaquette de beurre (moitié), 4 œufs, sucre et farine.",
  [f"200 g|de chocolat noir|{CHOCO}|3", f"125 g|de beurre|{BEURRE}|2", f"4|œufs|{OEUF}|2", f"125 g|de sucre|{SUCRE}|2", f"60 g|de farine|{F55}|1"],
  ["**Fondre.** Chocolat et beurre.", "**Mélanger.** Œufs + sucre, chocolat, farine.", "**Cuire.** 25-30 min à 180 °C."], age=1, cats=["enfants"], fetes=["Anniversaire"], profil=["sucre"])

K("verrines_speculoos", "Verrines spéculoos-mascarpone-pommes caramélisées", "Verrines", DS, "D", 1, 6, 20, 120, "€", "Verrines, poêle.",
  "Biscuits émiettés, crème légère au mascarpone, pommes poêlées au caramel : un dessert de fête sans four.",
  ["150 g|de spéculoos|Biscuits (spéculoos, sablés)|2", "250 g|de mascarpone|Mascarpone|3", f"15 cl|de crème|{CL}|2", "50 g|de sucre glace|Sucre glace|1", "3|pommes|Pomme|2", f"20 g|de beurre + 30 g de sucre|{BEURRE}|1"],
  ["**Pommes.** En dés, poêlées au beurre et sucre jusqu'à caramel.", "**Crème.** Mascarpone + crème + sucre glace fouettés.", "**Monter.** Biscuits, pommes, crème, biscuits. 2 h au frais."], age=1, cats=["enfants"], fetes=["Noël", "Anniversaire"], profil=["sucre"], tech=["Chantilly"])

K("crepes_froment_sucre", "Crêpes fines au sucre-citron, caramel beurre salé", "Crêpes sucrées", "France › Bretagne", "D", 1, 6, 10, 20, "€", "Poêle à crêpes.",
  "Les crêpes de la Chandeleur, nappées de caramel au beurre salé maison ou de sucre et citron.",
  ["12|crêpes|SUB:crepes_bretonnes|3", "1 pot|de caramel beurre salé (voir caramels mous, cuit à 108 °C)|SUB:caramels_beurre_sale|2", f"1|citron|{CIT}|1", f"2 c. à s.|de sucre|{SUCRE}|1"],
  ["**Garnir.** Crêpe chaude, caramel ou sucre + citron, pliée en quatre."], age=1, cats=["enfants"], fetes=["Chandeleur"], profil=["sucre"])

K("glace_vanille_sans_sorbetiere", "Glace vanille sans sorbetière", "Glace à la vanille", DS, "D", 1, 8, 15, 360, "€", "Batteur, boîte, congélateur.",
  "Crème fouettée et lait concentré sucré à la vanille : une glace crémeuse sans machine ni cristaux.",
  [f"40 cl|de crème entière très froide|{CL}|3", "1 boîte (397 g)|de lait concentré sucré|Lait concentré sucré / non sucré|3", "1|gousse de vanille|Vanille (gousse)|2"],
  ["**Fouetter.** Crème en chantilly ferme.", "**Mélanger.** Lait concentré vanillé, incorporé délicatement.", "**Congeler.** 6 h. Variantes : pépites, fruits, praliné, caramel."],
  keep="1 mois au congélateur.", age=1, cats=["enfants"], fetes=["Anniversaire", "Barbecue d'été"], profil=["sucre", "gras"], tech=["Chantilly"])

K("sorbet_fraise", "Sorbet fraise express", "Sorbet", DS, "D", 1, 4, 5, 0, "€", "Mixeur puissant.",
  "Fraises surgelées mixées avec un peu de sucre glace et de citron : un sorbet en 2 minutes.",
  ["400 g|de fraises surgelées|Fraise|3", "60 g|de sucre glace|Sucre glace|2", f"½|citron|{CIT}|1", "3 c. à s.|d'eau ou de yaourt|-|0"],
  ["**Mixer.** Tout, par à-coups, en raclant : texture de sorbet. Aussitôt."], age=1, cats=["enfants", "zero_dechet"], fetes=["Barbecue d'été"], profil=["sucre", "acide"])
