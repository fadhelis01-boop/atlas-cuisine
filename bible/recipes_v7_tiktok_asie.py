# -*- coding: utf-8 -*-
"""Vague TikTok « cuisines d'Asie » (12/11/2026) : les recettes les plus vues de Cooking with Morgane
(@cooking.with.morgane, autrice de « Cuisines d'Asie »), de Ryuji (@ryuji_tiktok_) et de Lynja (@cookingwithlynja), absentes
d'ATLAS. Les ingrédients suivent la légende publiée ; les étapes sont réécrites avec les repères ATLAS ; chaque fiche
renvoie à sa vidéo. Le porc et l'alcool restent quand l'autrice les met, avec leur version adaptée. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *
from recipes_v6_tiktok_plats import C

TT = "https://www.tiktok.com/"
def V(author, vid):
    return (f"@{author}", f"{TT}@{author}/video/{vid}")
def M(vid):
    return V("cooking.with.morgane", vid)

CN = "Asie de l'Est › Chine"; JP = "Asie de l'Est › Japon"; KR = "Asie de l'Est › Corée"; VN = "Asie du Sud-Est › Vietnam"; TH = "Asie du Sud-Est › Thaïlande"
HUITRE = "Sauce d'huître"; SES = "Huile de sésame (grillée)"; CEB = "Oignon nouveau / cébette"; FMAI = "Fécule de maïs (maïzena)"
SHAO = ("Sans alcool", ["alcohol"], {"Vin Shaoxing": [("Bouillon d'os maison (bœuf/volaille)", 0.8), ("Vinaigre de riz", 0.1)]},
        "Shaoxing → **bouillon + un trait de vinaigre de riz** (Morgane donne aussi son propre substitut sans alcool en vidéo). **À tester**.")
SAKE = ("Sans alcool", ["alcohol"], {"Saké / saké de cuisine": [("Bouillon cube volaille", 1.0)]}, "Saké → **bouillon de volaille**. **À tester**.")
MIRIN = ("Sans alcool", ["alcohol"], {"Mirin": [("Jus de pomme / raisin / orange (pur jus)", 0.8), ("Vinaigre de riz", 0.1)]}, "Mirin → **jus de pomme + un trait de vinaigre de riz**. **À tester**.")

# ———————————————————————————————— Cooking with Morgane
K("poulet_caramelise_viet", "Poulet caramélisé à la vietnamienne (version de Morgane, 3,3 M de vues)", "Thịt rim", VN, "P", 1, 4, 15, 25, "€", "Sauteuse ou wok.",
  "La recette la plus simple et la plus vue de Cooking with Morgane : des lamelles de viande marinées à l'ail et à la sauce de poisson, puis cuites jusqu'à ce que le sucre caramélise et laque la viande. Elle conseille aussi la version au poulet.",
  ["500 g|de hauts de cuisse de poulet désossés (Morgane fait aussi l'échine de porc)|Cuisse / pilon de poulet|3", f"3 gousses|d'ail|{AIL}|1", "2 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|2",
   f"2 c. à s.|de sucre|{SUCRE}|2", f"1/4 c. à c.|de sel|{SEL}|1", f"1/4 c. à c.|de poivre moulu|{POIVRE}|1", f"3 c. à s.|d'huile de tournesol|{HN}|1", f"400 g|de riz jasmin (à part)|{RIZ}|2"],
  ["**Trancher.** Poulet en lamelles de 1 cm (20 min au congélateur avant, il se tranche mieux) ; ail haché.",
   "**Mariner.** Viande, ail, sauce de poisson, la moitié du sucre, sel, poivre : 15 min.",
   "**Saisir.** Huile chaude, viande étalée en une couche, 3 min sans toucher : elle colore ; retournée, 3 min.",
   "**Caraméliser.** Reste du sucre, 3 c. à s. d'eau, 5 à 8 min à feu moyen en remuant : le jus réduit en caramel brun qui enrobe, poulet cuit à cœur (74 °C). Avec le riz et un concombre."],
  tips=["Le sucre brûle vite à la fin : baisse le feu dès que le jus devient sirupeux.", "La vidéo d'origine est à l'échine de porc ; Morgane la fait aussi au poulet, comme ici."],
  keep="3 jours au frigo.", age=3, kids="✓ dès 3 ans.", profil=["sucre", "gras"], tech=["Caraméliser"], credit=C(M("7443833006688619798")))
K("raviolis_sans_pliage_grilles", "Raviolis grillés sans pliage (version de Morgane, 1,8 M de vues)", "Raviolis sans pliage", CN, "P", 1, 4, 30, 15, "€", "Grande poêle avec couvercle.",
  "Pour ceux qui redoutent le pliage : des feuilles à wonton simplement roulées autour d'une farce de poulet au gingembre et au poireau, saisies côte à côte dans la poêle puis cuites à la vapeur, dessous doré et croustillant.",
  ["400 g|de hauts de cuisse de poulet hachés (ou autre viande hachée)|Cuisse / pilon de poulet|3", "30|feuilles à raviolis wonton|Pâte à gyoza / wonton|3", f"2 gousses|d'ail|{AIL}|1",
   f"2 c. à s.|de sauce soja claire|{SOJA}|1", "1 c. à s.|de saké de cuisine|Saké / saké de cuisine|1", f"1 c. à c.|de gingembre râpé|{GING}|1", f"1 c. à c.|de sucre|{SUCRE}|1",
   "1|blanc de poireau|Poireau|1", f"3|cébettes|{CEB}|1", f"1|œuf|{OEUF}|1", f"1 c. à s.|de fécule de maïs|{FMAI}|1", f"2 c. à s.|d'huile de tournesol|{HN}|1", f"2 c. à s.|d'huile de sésame|{SES}|1"],
  ["**Farce.** Poulet, ail, gingembre, soja, saké, sucre, sel, poivre, œuf, fécule : battus 2 min dans un seul sens, collants ; poireau et cébettes ciselés très fin.",
   "**Rouler.** Une c. à c. bombée de farce en boudin sur le bord d'une feuille, roulée en cigare, bords humidifiés, extrémités laissées ouvertes.",
   "**Griller.** Huiles dans la poêle, raviolis serrés côte à côte, 2 min à feu moyen : dessous doré.",
   "**Vapeur.** 10 cl d'eau, couvercle aussitôt, 6 min ; découvert, 1 à 2 min : l'eau s'évapore, le dessous recroustille, farce cuite à cœur (74 °C). Retournés d'un bloc sur l'assiette."],
  tips=["Serre-les bien dans la poêle : ils se soutiennent et forment une seule galette croustillante.", "Sauce : soja, vinaigre de riz, un peu d'huile pimentée."],
  var=[SAKE], keep="Crus, se congèlent à plat.", age=3, kids="✓ dès 3 ans.", profil=["gras"], tech=["Plier les raviolis"], credit=C(M("7504713151183621398"), M("7691939151393885473")))
K("boeuf_saute_oeuf", "Bœuf sauté à l'œuf (huá dàn niúròu, version de Morgane)", "Huá dàn niúròu", CN + " › Canton", "P", 2, 4, 20, 25, "€€", "Wok.",
  "Un classique cantonais : des lamelles de bœuf très tendres, marinées et saisies, puis enveloppées d'œufs à peine pris, soyeux, au gingembre et à la cébette. Prêt en un quart d'heure une fois la viande marinée.",
  ["400 g|de bœuf tendre (filet, tende de tranche)|Rumsteck|3", f"5|œufs|{OEUF}|3", f"1 c. à s. + 1/2|de sauce soja claire|{SOJA}|1", f"1 c. à s. + 1/2|de sauce d'huître|{HUITRE}|1",
   "1 c. à s.|de vin Shaoxing|Vin Shaoxing|1", f"1/2 c. à s.|de fécule de maïs|{FMAI}|1", f"5 gousses|d'ail|{AIL}|1", f"1 c. à s.|de gingembre râpé|{GING}|1", "1|piment doux ou fort|Piment frais (divers)|1?",
   f"2|cébettes|{CEB}|1", f"6 c. à s.|d'huile de tournesol|{HN}|1", f"400 g|de riz (à part)|{RIZ}|2"],
  ["**Mariner.** Bœuf en fines lamelles contre le fil ; sel, poivre, Shaoxing, 1 c. à s. de soja, 1 c. à s. d'huître, fécule, 1 c. à s. d'huile : 20 min.",
   "**Saisir.** Wok fumant, 2 c. à s. d'huile, bœuf étalé, 40 s par face : à peine rosé ; réservé.",
   "**Aromates.** Ail, gingembre, piment, blanc de cébette, 30 s ; bœuf remis, reste de soja et d'huître, poivre ; réservé.",
   "**Œufs.** Battus avec une pincée de sel ; reste de l'huile, feu moyen ; œufs versés, poussés lentement à la spatule 20 s ; bœuf ajouté, 20 s : œufs encore baveux et brillants. Vert de cébette, sur le riz."],
  tips=["Les œufs continuent de cuire dans l'assiette : retire du feu quand ils sont encore coulants par endroits."],
  var=[SHAO], keep="Le jour même.", age=3, kids="✓ dès 3 ans, sans piment.", profil=["viande_rouge"], tech=["Sauter au wok", "Mariner"], credit=C(M("7562201787063684374")))
K("poulet_sel_poivre", "Beignets de poulet sel et poivre (version de Morgane)", "Jiāoyán jī", CN + " › Taïwan", "P", 2, 4, 25, 30, "€", "Casserole profonde, thermomètre.",
  "Des morceaux de poulet marinés à l'ail, enrobés d'une pâte légère au curcuma et au paprika, frits deux fois puis saupoudrés de poivre noir concassé et de sel : croustillants, très parfumés.",
  [f"500 g|de chair de poulet (hauts de cuisse)|{CUISSE}|3", f"100 g|de farine de blé|{F55}|2", f"50 g|de fécule de maïs|{FMAI}|2", f"1 c. à c.|de levure chimique|{LEVC}|1",
   f"1/4 c. à c.|de paprika|{PAPRIKA}|1", f"1/4 c. à c.|de curcuma|{CURC}|1", "1/2 c. à s.|de vin Shaoxing (facultatif)|Vin Shaoxing|1?", f"3 gousses|d'ail|{AIL}|1",
   f"1 c. à c.|de poivre noir concassé|{POIVRE}|1", f"1/4 c. à c.|de sel|{SEL}|1", f"60 cl|d'huile de friture|{HN}|1"],
  ["**Mariner.** Poulet en morceaux de 3 cm, sel, poivre, ail râpé, Shaoxing : 20 min.",
   "**Pâte.** Farine, fécule, levure, paprika, curcuma, sel, 1 c. à s. d'huile, 15 cl d'eau : fluide comme une pâte à crêpes épaisse.",
   "**Frire.** Huile à 170 °C ; morceaux enrobés, en petites quantités, 4 min : pâles et pris ; égouttés.",
   "**Recroustiller.** Huile à 190 °C, 1 min : dorés, croustillants ; poulet cuit à cœur (74 °C). Aussitôt, poivre concassé et sel."],
  tips=["La double friture fait tout : la première cuit, la seconde sèche la croûte."],
  var=[SHAO], keep="Le jour même ; 10 min au four à 200 °C pour les recroustiller.", age=3, kids="✓ dès 3 ans, peu de poivre.", profil=["gras", "epice"], tech=["Frire"], credit=C(M("7694698547446287649")))
K("goong_ob_woon_sen", "Goong ob woon sen (vermicelles aux crevettes en cocotte, Thaïlande)", "Kung op wun sen", TH, "P", 2, 4, 20, 20, "€€", "Cocotte en fonte ou sauteuse avec couvercle.",
  "Un grand classique thaï que Morgane a fait découvrir : des crevettes posées sur des aromates et un peu de viande, sur des vermicelles transparents qui cuisent à l'étouffée en buvant toute la sauce soja-huître poivrée.",
  ["200 g|de vermicelles de haricot mungo|Vermicelles de haricots mungo|3", "450 g|de crevettes crues|Crevettes (cuites/crues)|3", "200 g|de chair de poulet en fines tranches (Morgane met aussi de la poitrine de porc)|Cuisse / pilon de poulet|2",
   f"3 c. à s.|de sauce d'huître|{HUITRE}|2", f"3 c. à s.|de sauce soja claire (+ 1 c. à c. de foncée)|{SOJA}|2", f"1/2 c. à s.|de sucre|{SUCRE}|1", f"1 c. à s.|d'huile de sésame|{SES}|1",
   "2 c. à s.|de vin Shaoxing|Vin Shaoxing|1", f"30 g|de gingembre|{GING}|1", f"30 g|d'ail|{AIL}|1", f"3|cébettes|{CEB}|1", "30 g|de céleri en branche|Céleri-branche|1", f"10 g|de coriandre|{CORI}|1",
   "1/2 c. à s.|de poivre du Sichuan ou noir|Poivre du Sichuan|1"],
  ["**Tremper.** Vermicelles 10 min dans l'eau tiède, égouttés, coupés en deux ; mélangés avec sauces, sucre, sésame, Shaoxing et 10 cl d'eau.",
   "**Fond.** Tranches de viande au fond de la cocotte froide ; gingembre en lamelles, ail écrasé, poivre, céleri et cébettes en tronçons par-dessus.",
   "**Étuver.** Vermicelles et leur sauce, crevettes sur le dessus ; couvert, feu moyen 10 à 12 min : la viande grésille, les vermicelles boivent tout, les crevettes sont roses et opaques.",
   "**Servir.** Mélangé à table, coriandre ; poulet cuit à cœur (74 °C)."],
  tips=["Ne soulève pas le couvercle : c'est la vapeur qui cuit les crevettes.", "La viande au fond protège les vermicelles et parfume le plat ; elle peut accrocher un peu, c'est voulu."],
  var=[SHAO],
  keep="1 jour au frigo.", age=3, kids="✓ dès 3 ans, poivre à part.", profil=["poisson", "epice"], credit=C(M("7666765896744062240")))
K("niu_rou_bing", "Galettes feuilletées au bœuf (niú ròu bǐng, version de Morgane)", "Niú ròu bǐng", CN, "P", 2, 8, 50, 30, "€", "Grande poêle avec couvercle.",
  "Des galettes croustillantes du nord de la Chine : une pâte à l'eau étirée très fine et huilée, roulée pour former des couches, fourrée de bœuf haché au cumin et à la cive, aplatie et dorée à la poêle.",
  [f"400 g|de farine de blé|{F55}|3", "22 cl|d'eau tiède|-|2", f"300 g|de bœuf haché|{'Bœuf haché'}|3", f"1 gousse|d'ail|{AIL}|1", "100 g|de cive ou de cébette|Ciboulette|1",
   f"1/2 c. à c.|de cumin|{CUMIN}|1", f"1 c. à s.|de sauce soja claire|{SOJA}|1", f"1 c. à s.|de sauce d'huître|{HUITRE}|1", f"1 c. à c.|de fécule de maïs|{FMAI}|1", f"4 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Pâte.** Farine, sel, eau tiède : pétrie 8 min, très souple ; 30 min huilée sous un bol ; coupée en 8.",
   "**Farce.** Bœuf, ail, cumin, soja, huître, fécule, poivre, 3 c. à s. d'eau : battue 2 min ; cive hachée au dernier moment.",
   "**Feuilleter.** Chaque pâton étiré sur le plan huilé en long ruban très fin ; farce étalée sur la moitié, ruban roulé en escargot, extrémité rentrée dessous ; 10 min de repos, aplati à 1,5 cm.",
   "**Cuire.** Poêle huilée, feu moyen, couvert, 4 min par face : dorées, gonflées, bœuf cuit à cœur (70 °C) ; ou 3 min par face puis 7 min au four à 200 °C."],
  tips=["Une pâte très souple et bien reposée s'étire sans se déchirer : c'est elle qui fait les couches.", "Morgane les fait aussi au poulet."],
  keep="2 jours au frigo ; crues, se congèlent.", age=3, kids="✓ dès 3 ans.", profil=["gras", "viande_rouge"], tech=["Pétrir"], credit=C(M("7346930828313742625")))
K("aehobak_jeon", "Aehobak jeon (galettes coréennes à la courgette)", "Aehobak-jeon", KR, "E", 1, 2, 15, 15, "€", "Poêle.",
  "Un jeon (galette) traditionnel coréen avec peu d'ingrédients : courgettes en fine julienne salées, liées d'une pâte légère, dorées à la poêle, servies avec une sauce soja-vinaigre-gochugaru.",
  ["2|courgettes|Courgette|3", f"150 g|de farine de blé|{F55}|2", f"1 c. à c.|de sel|{SEL}|1", f"4 c. à s.|d'huile de tournesol|{HN}|1", f"1 c. à s.|d'huile de sésame|{SES}|1",
   f"1 gousse|d'ail (sauce)|{AIL}|1", f"1 c. à c.|de sucre (sauce)|{SUCRE}|1", "1 c. à c.|de gochugaru (sauce)|Gochugaru|1?", f"1 c. à s.|de sauce soja claire (sauce)|{SOJA}|1",
   "1 c. à s.|de vinaigre de riz (sauce)|Vinaigre de riz|1", "1/2 c. à c.|de sésame grillé (sauce)|Sésame (blanc/noir)|1"],
  ["**Dégorger.** Courgettes en fine julienne, ½ c. à c. de sel, 10 min : elles rendent leur eau (garde-la).",
   "**Pâte.** Farine, reste du sel, poivre, 30 cl d'eau (dont celle des courgettes) : lisse ; courgettes mêlées.",
   "**Cuire.** Poêle chaude, huiles, moitié de la pâte étalée finement ; 4 min : bords dorés ; retournée, 3 min en pressant : croustillante.",
   "**Sauce.** Ail râpé, sucre, gochugaru, soja, vinaigre, sésame. Galettes coupées en parts, sauce à côté."],
  tips=["Étale fin : un jeon épais reste pâteux au centre."],
  keep="Le jour même.", age=1, kids="✓ dès 1 an, sauce sans piment.", cats=["vegetarien", "express"], profil=["leger"], credit=C(M("7434909739877698848")))
K("banh_cuon", "Bánh cuốn (crêpes de riz vapeur farcies, Vietnam)", "Bánh cuốn", VN + " › Hanoï", "P", 3, 4, 50, 20, "€", "Poêle antiadhésive avec couvercle, pinceau.",
  "Des crêpes de riz fines comme une feuille, souples et translucides, roulées autour d'une farce de viande, d'oignon et de champignons noirs, avec des échalotes frites et la sauce nước chấm. Pâte sans gluten.",
  ["150 g|de farine de riz|Farine de riz / riz gluant|3", "150 g|de fécule de tapioca (ou de maïs)|Fécule de maïs (maïzena)|2", f"1 c. à c.|de sel|{SEL}|1", f"4 c. à s.|d'huile de tournesol|{HN}|1",
   "300 g|de poulet haché (ou de porc, comme à Hanoï)|Cuisse / pilon de poulet|3", "20 g|de champignons noirs séchés|Champignon noir séché|1", f"1|oignon|{OIG}|1", f"3 gousses|d'ail|{AIL}|1",
   "3 brins|de ciboulette|Ciboulette|1", "1 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|1", f"1 c. à s.|de sauce d'huître|{HUITRE}|1", "6 c. à s.|de nước chấm|SUB:nuoc_cham|2", f"2 c. à s.|d'échalotes frites|{ECH}|1?"],
  ["**Pâte.** Farine de riz, fécule, sel, 2 c. à s. d'huile, 1 l d'eau : très liquide ; 30 min de repos ; remuer avant chaque crêpe.",
   "**Farce.** Champignons trempés 20 min, hachés ; oignon et ail revenus 3 min ; poulet 6 min en l'émiettant : plus de rose (74 °C) ; sauce de poisson, huître, poivre.",
   "**Crêpe.** Poêle à feu moyen, huilée au pinceau ; une petite louche tournée en couche très fine ; couvercle 1 min : translucide, sans dorer.",
   "**Rouler.** Retournée sur une planche huilée, une cuillerée de farce, roulée ; ciboulette.",
   "**Servir.** Tièdes, nappées de nước chấm, échalotes frites, herbes."],
  tips=["Une crêpe trop épaisse devient caoutchouteuse : la louche doit juste couvrir le fond.", "La fécule de tapioca rend la crêpe plus souple que celle de maïs."],
  keep="Le jour même.", age=3, kids="✓ dès 3 ans.", profil=["leger"], credit=C(M("7700253537174916385")))
K("oeufs_crevettes_cantonais", "Œufs brouillés aux crevettes à la cantonaise (huá dàn xiā rén)", "Huá dàn xiā rén", CN + " › Canton", "P", 1, 4, 15, 5, "€€", "Wok ou poêle.",
  "Peu d'ingrédients, cinq minutes de cuisson : des crevettes saisies juste ce qu'il faut, enveloppées d'œufs soyeux, à peine pris. Morgane montre les deux petits trucs qui font la texture : la fécule sur les crevettes, le vinaigre dans les œufs.",
  ["400 g|de crevettes crues entières|Crevettes (cuites/crues)|3", f"6|œufs|{OEUF}|3", "1/2 c. à c.|de vinaigre de riz blanc|Vinaigre de riz|1", f"1 c. à c.|de fécule de maïs|{FMAI}|1",
   f"1|cébette|{CEB}|1", f"3 c. à s.|d'huile de tournesol|{HN}|1", f"400 g|de riz (à part)|{RIZ}|2"],
  ["**Crevettes.** Décortiquées, incisées sur le dos et déveinées ; sel, poivre, fécule : 10 min.",
   "**Œufs.** Battus avec le vinaigre, sel, ½ c. à c. de fécule délayée dans 1 c. à s. d'eau : ils resteront tendres.",
   "**Saisir.** Wok chaud, 1 c. à s. d'huile, crevettes 1 min 30 : roses et recourbées ; réservées.",
   "**Lier.** Reste de l'huile, feu moyen-doux ; œufs, poussés lentement en grands plis ; à mi-prise, crevettes ; feu coupé quand les œufs sont encore brillants. Cébette, sur le riz."],
  tips=["Retire les crevettes dès qu'elles sont roses : elles finissent de cuire dans les œufs."],
  keep="Le jour même.", age=3, kids="✓ dès 3 ans.", cats=["express"], profil=["poisson", "leger"], credit=C(M("7478990242012400919")))
K("mayonnaise_japonaise", "Mayonnaise japonaise maison (façon Kewpie)", "Mayonēzu", JP, "S", 1, 10, 10, 0, "€", "Bocal étroit, mixeur plongeant.",
  "Plus crémeuse, un peu sucrée et plus acidulée que la mayonnaise française : celle des tamago sando, okonomiyaki, takoyaki et tonkatsu. Morgane la fait avec un œuf entier, au mixeur, en une minute.",
  [f"1|œuf entier très frais|{OEUF}|3", "1 c. à s.|de mirin|Mirin|1", "1 c. à s.|de vinaigre de riz (ou jus de citron)|Vinaigre de riz|1", f"1/2 c. à c.|de sel|{SEL}|1", "22 cl|d'huile de colza|Huile de tournesol / colza|3"],
  ["**Base.** Œuf, mirin, vinaigre, sel au fond du bocal étroit.",
   "**Huile.** Versée d'un coup par-dessus ; 1 min de repos : elle se pose.",
   "**Monter.** Mixeur plongeant au fond, sans bouger 10 s : la mayonnaise prend en bas ; remonté lentement.",
   "**Ajuster.** Goûte : une pointe de vinaigre en plus si tu l'aimes plus acidulée ; en pot fermé au frais."],
  tips=["Œuf cru : pas pour les enfants de moins de 6 ans, les femmes enceintes ni les personnes fragiles.", "Elle se garde 3 jours au frigo."],
  var=[MIRIN], keep="3 jours au frigo, bocal fermé.", age=6, kids="✓ dès 6 ans (œuf cru).", cats=["sauces"], profil=["gras", "acide"], tech=["Émulsionner"], credit=C(M("7603772491345005846")))
K("poulet_caramel_croustillant", "Poulet au caramel croustillant (version de Morgane)", "Poulet caramel croustillant", CN, "P", 2, 4, 25, 25, "€", "Casserole profonde, wok.",
  "Une version très vue du poulet au caramel : des morceaux enrobés de blanc d'œuf et de fécule, frits croustillants, puis vite laqués d'un caramel à l'ail, au gingembre, à la sauce soja et à la sauce de poisson.",
  [f"400 g|de filets de volaille|{BLANC_P}|3", f"1|blanc d'œuf|{OEUF}|1", f"80 g|de fécule de maïs|{FMAI}|2", "1 c. à s.|de vin Shaoxing|Vin Shaoxing|1", f"1 c. à s. + 1/2|de sauce soja claire|{SOJA}|1",
   "1 c. à c.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|1", f"2 c. à s.|de sucre|{SUCRE}|2", f"3 gousses|d'ail|{AIL}|1", f"1 c. à c.|de gingembre râpé|{GING}|1",
   "2 c. à s.|d'échalotes frites (facultatif)|Échalote|1?", f"60 cl|d'huile de friture|{HN}|1", f"400 g|de riz (à part)|{RIZ}|2"],
  ["**Mariner.** Poulet en cubes, sel, poivre, Shaoxing, ½ c. à s. de soja, blanc d'œuf : 15 min ; puis roulé dans la fécule.",
   "**Frire.** Huile à 175 °C, en deux fois, 5 min : dorés et croustillants, 74 °C à cœur ; égouttés.",
   "**Caramel.** Sucre à sec dans le wok, ambré ; ail et gingembre 10 s ; soja, sauce de poisson, 1 c. à c. de fécule délayée dans 7,5 cl d'eau : bouillonne, nappe.",
   "**Laquer.** Poulet jeté dedans, 20 s en sautant : enrobé, encore croustillant. Échalotes frites, riz."],
  tips=["Laque au tout dernier moment, juste avant de servir : la croûte ramollit vite dans la sauce."],
  var=[SHAO], keep="Le jour même.", age=3, kids="✓ dès 3 ans.", profil=["sucre", "gras"], tech=["Frire", "Caraméliser"], credit=C(M("7334752683682729249")))

# ———————————————————————————————— Ryuji (@ryuji_tiktok_) : plats de maison japonais parmi ses plus vus
K("tenshindon", "Tenshindon (omelette au crabe sur riz, sauce brillante)", "Tenshin-don", JP, "P", 1, 2, 10, 10, "€", "Poêle, petite casserole.",
  "Un plat « chinois du Japon » des cantines : une omelette moelleuse au crabe et à la cébette posée sur un bol de riz, nappée d'une sauce sucrée-acidulée liée à la fécule. Ryuji en a fait une version minimaliste vue des millions de fois.",
  [f"3|œufs|{OEUF}|3", "80 g|de chair de crabe (ou surimi)|Crevettes (cuites/crues)|2", f"2|cébettes|{CEB}|1", f"300 g|de riz rond cuit|Riz rond / sushi|3", f"1 c. à s.|de sauce soja|{SOJA}|1",
   f"1 c. à s.|de sucre|{SUCRE}|1", "1 c. à s.|de vinaigre de riz|Vinaigre de riz|1", "1 c. à c.|de ketchup (facultatif)|Ketchup|1?", f"1 c. à c.|de fécule de maïs|{FMAI}|1",
   "1/2|cube de bouillon de volaille|Bouillon cube volaille|1", f"1 c. à s.|d'huile|{HN}|1", f"1 c. à c.|d'huile de sésame|{SES}|1"],
  ["**Riz.** Riz rond rincé jusqu'à eau presque claire, cuit avec 1,1 fois son volume d'eau ; en bols.",
   "**Sauce.** 12 cl d'eau, bouillon, soja, sucre, vinaigre, ketchup, fécule délayée : à frémissement en remuant 1 min, brillante et nappante.",
   "**Omelette.** Œufs battus avec crabe émietté et cébette ; poêle bien chaude, huile ; versés d'un coup, remués 15 s puis laissés prendre 30 s : dessous pris, dessus baveux.",
   "**Monter.** Omelette glissée sur le riz, sauce par-dessus, huile de sésame."],
  tips=["La sauce doit napper sans être collante : allonge d'eau si elle épaissit trop."],
  keep="Le jour même.", age=1, kids="✓ dès 1 an.", cats=["express"], profil=["sucre", "acide"], credit=C(V("ryuji_tiktok_", "7262263304075087122")))
K("niku_daikon", "Niku daikon (radis blanc mijoté au bœuf, Japon)", "Niku daikon", JP, "P", 1, 4, 15, 40, "€", "Cocotte ou sauteuse avec couvercle.",
  "Un plat mijoté de la cuisine familiale japonaise : du daikon en épais tronçons qui boit un bouillon sucré-salé de soja et de mirin, avec des lamelles de bœuf. Un des « vrais bons » plats maison que Ryuji remet en avant.",
  ["600 g|de daikon (radis blanc)|Radis noir / daikon|3", "250 g|de bœuf en fines tranches|Rumsteck|2", f"3 c. à s.|de sauce soja|{SOJA}|2", "2 c. à s.|de mirin|Mirin|1",
   f"1 c. à s.|de sucre|{SUCRE}|1", "1 c. à s.|de saké|Saké / saké de cuisine|1", f"1 morceau (3 cm)|de gingembre|{GING}|1", "40 cl|de dashi ou d'eau|Dashi (instantané)|1", f"1 c. à s.|d'huile|{HN}|1"],
  ["**Daikon.** Épluché épais, en demi-rondelles de 2 cm ; 10 min à l'eau frémissante : il perd son âcreté ; égoutté.",
   "**Saisir.** Huile, bœuf, gingembre en lamelles, 1 min : il change de couleur.",
   "**Mijoter.** Daikon, dashi, saké, mirin, sucre ; à frémissement 10 min ; soja ; papier cuisson posé au contact (otoshibuta), 20 min : daikon translucide et brun.",
   "**Reposer.** Hors du feu 15 min : le daikon boit le bouillon en refroidissant. Avec du riz."],
  tips=["Le goût entre en refroidissant : c'est encore meilleur réchauffé le lendemain."],
  var=[("Sans alcool", ["alcohol"], {"Mirin": [("Jus de pomme / raisin / orange (pur jus)", 0.8), ("Vinaigre de riz", 0.1)], "Saké / saké de cuisine": [("Bouillon cube volaille", 1.0)]},
        "Mirin → **jus de pomme + un trait de vinaigre de riz** ; saké → **bouillon**. **À tester**.")],
  keep="3 jours au frigo.", age=1, kids="✓ dès 1 an, en version sans alcool.", profil=["leger", "sucre"], tech=["Mijoter"], credit=C(V("ryuji_tiktok_", "7279348437231930626")))
K("piman_nikuzume", "Piman no nikuzume (poivrons farcis à la japonaise)", "Pīman no nikuzume", JP, "P", 1, 4, 20, 20, "€", "Poêle avec couvercle.",
  "Les poivrons farcis des bentos japonais : des demi-poivrons verts farcis de viande hachée à l'oignon, saisis côté viande puis cuits à couvert, laqués d'une sauce ketchup-sauce Worcestershire. Une recette phare de Ryuji.",
  [f"4|poivrons verts|{POIVRON}|3", f"300 g|de bœuf haché (ou mélange)|{'Bœuf haché'}|3", f"1/2|oignon|{OIG}|1", "3 c. à s.|de chapelure (panko)|Panko|1", f"1|œuf|{OEUF}|1",
   f"1 c. à s.|de fécule de maïs|{FMAI}|1", "2 c. à s.|de ketchup|Ketchup|1", "1 c. à s.|de sauce Worcestershire|Sauce Worcestershire|1", f"1 c. à c.|de sauce soja|{SOJA}|1", f"1 c. à s.|d'huile|{HN}|1"],
  ["**Farce.** Viande, oignon haché fin, panko, œuf, sel, poivre : malaxée 1 min.",
   "**Farcir.** Poivrons coupés en deux, épépinés, intérieur poudré de fécule (la farce adhère) ; farce tassée, bombée.",
   "**Cuire.** Poêle huilée, côté viande en dessous, 4 min : bien dorée ; retournés, 3 c. à s. d'eau, couvert, 6 min à feu doux : viande à 70 °C à cœur.",
   "**Laquer.** Ketchup, Worcestershire, soja dans la poêle, 1 min en nappant."],
  tips=["La fécule à l'intérieur du poivron empêche la farce de se détacher à la cuisson."],
  keep="2 jours au frigo ; parfait en bento.", age=3, kids="✓ dès 3 ans.", profil=["sucre"], credit=C(V("ryuji_tiktok_", "7409208446823795988")))

# ———————————————————————————————— Lynja (@cookingwithlynja)
K("tanghulu", "Tanghulu (fruits en brochettes au sucre craquant, Pékin)", "Táng húlu", CN + " › Pékin", "G", 2, 6, 20, 10, "€", "Petite casserole, brochettes en bois, thermomètre à sucre, bol d'eau glacée.",
  "La friandise d'hiver des rues de Pékin, devenue phénomène mondial (le « Grape Tanghulu » de Lynja dépasse les 47 millions de vues) : des fruits en brochettes plongés dans un sucre cuit au cassé, qui durcit en coque de verre.",
  ["300 g|de fruits fermes et bien secs (raisins, fraises, clémentines en quartiers)|Fraise|3", f"200 g|de sucre|{SUCRE}|3", "10 cl|d'eau|-|2"],
  ["**Préparer.** Fruits lavés puis séchés parfaitement (une goutte d'eau et le sucre glisse) ; 3 à 4 par brochette.",
   "**Cuire le sucre.** Sucre et eau à feu moyen, sans remuer, 10 à 12 min jusqu'à 150 °C (cassé) : une goutte dans l'eau glacée casse net comme du verre ; il doit rester clair.",
   "**Tremper.** Casserole inclinée, brochette roulée une fois dans le sucre, en une seconde.",
   "**Figer.** 10 s dans l'eau glacée, ou posée sur papier cuisson : coque fine et craquante. À manger dans l'heure."],
  tips=["Sucre à 150 °C : danger de brûlure grave, pas d'enfant à côté de la casserole.", "Par temps humide la coque colle : mange-les vite."],
  keep="Dans l'heure.", age=3, kids="✓ dès 3 ans à manger, jamais près du sucre cuit. Raisins coupés en deux pour les petits (risque d'étouffement).", cats=["vegetarien", "enfants"], profil=["sucre"],
  tech=["Caramel et cuissons du sucre"], credit=C(V("cookingwithlynja", "7065711141372267822")))
