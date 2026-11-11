# -*- coding: utf-8 -*-
"""Vague 9 (suite) · 11/11/2026 : le favori TikTok ajouté depuis le 10/11 (ajvar, @alonimhotep) et les vidéos de recettes
d'@erynshow (profil ouvert par le propriétaire). Les légendes d'Eryn donnent rarement la recette : la fiche suit la recette
de référence du plat montré, la vidéo est créditée. Réécrites, NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *
from recipes_v6_tiktok_plats import C

TT = "https://www.tiktok.com/"
def V(author, vid):
    return (f"@{author}", f"{TT}@{author}/video/{vid}")

K("ajvar", "Ajvar (purée de poivrons et d'aubergines grillés, Balkans)", "Ajvar", "Europe du Sud › Serbie", "S", 2, 12, 30, 90, "€", "Four en position grill, grande casserole, mixeur ou moulin à légumes, bocaux.",
  "La tartinade rouge des Balkans, faite à l'automne en grandes quantités : des poivrons rouges et des aubergines grillés jusqu'à noircir, pelés, hachés puis mijotés longtemps avec de l'ail, de l'huile, un peu de vinaigre. Sur du pain, avec des grillades, des œufs, du fromage blanc.",
  [f"1,5 kg|de poivrons rouges (8 à 10)|{POIVRON}|3", "2|grosses aubergines|Aubergine|3", f"5|gousses d'ail|{AIL}|1", f"1|piment frais (facultatif)|{PIMENT}|1?", f"16 cl|d'huile de tournesol|{HN}|2", f"2 c. à s.|de vinaigre de cidre|{CIDRE}|1", f"1 c. à c.|de sucre|{SUCRE}|1"],
  ["**Griller.** Poivrons et aubergines entiers sous le grill du four, 30 à 40 min en les retournant : peau noire et cloquée partout, chair effondrée ; poivrons 10 min sous un torchon.",
   "**Peler.** Peau et pépins retirés, chair égouttée 15 min dans une passoire (l'eau rendue délaye le goût).",
   "**Hacher.** Au moulin à légumes ou par impulsions au mixeur, avec l'ail : purée un peu rustique, pas lisse.",
   "**Mijoter.** Casserole, la moitié de l'huile, purée, sel, sucre ; feu doux, 45 min à 1 h en remuant souvent et en ajoutant le reste d'huile peu à peu : elle épaissit et brille, une cuillère y laisse un sillon ; vinaigre en fin.",
   "**Conserver.** En bocaux propres, couvert d'un filet d'huile."],
  tips=["Remuer souvent en fin de cuisson : épaissie, la purée attache et éclabousse (couvercle entrouvert)."], keep="2 semaines au frigo, couvert d'huile ; se congèle 6 mois.", age=1, cats=["vegetarien", "sauces"], fetes=["Barbecue d'été", "Apéritif dînatoire"], profil=["acide", "leger"],
  credit=C(V("alonimhotep", "7706217221613227297")))
K("sandwich_raclette_piquant", "Sandwich chaud à la raclette, oignons confits et piment", "Sandwich raclette", "France › Food fusion", "P", 1, 4, 15, 15, "€€", "Poêle, four en position grill.",
  "Le sandwich de la flemme qui a fait des millions de vues : une baguette garnie de fromage à raclette fondu sous le grill, d'oignons confits à la poêle, de cornichons et d'un piment (ou de sauce pimentée), à manger brûlant.",
  ["1|baguette|Baguette tradition|3", "300 g|de fromage à raclette en tranches|Reblochon / raclette / mont-d'or|3", f"2|oignons|{OIG}|2", f"20 g|de beurre|{BEURRE}|1", "6|cornichons|Cornichon|1", f"1|piment frais (ou 1 c. à c. de sauce pimentée)|{PIMENT}|1", f"1 c. à c.|de moutarde|{DIJON}|1", "1|salade verte|Salade (laitue, batavia)|1"],
  ["**Oignons.** Émincés, beurre, sel, 15 min à feu doux en remuant : fondants et dorés.",
   "**Garnir.** Baguette coupée en 4 tronçons ouverts, moutarde, oignons, cornichons en lamelles, fines rondelles de piment, raclette en couche épaisse.",
   "**Gratiner.** Sous le grill, 4 à 5 min : fromage fondu, bouillonnant, doré par endroits.",
   "**Servir.** Refermé, tout de suite, salade à côté."],
  tips=["Femme enceinte : un fromage à raclette au lait pasteurisé.", "Pour les enfants : sans piment."], keep="À manger tout de suite.", age=3, cats=["vegetarien", "express"], profil=["gras", "epice"],
  credit=C(V("erynshow", "7578967697149447446")))
K("pates_chorizo_creme", "Pâtes au chorizo et à la tomate crémeuse (chorizo de bœuf ou de volaille)", "Pasta chorizo", "Europe du Sud › Espagne", "P", 1, 4, 10, 15, "€", "Grande poêle, casserole.",
  "Les pâtes « simple et efficace » : des rondelles de chorizo saisies jusqu'à rendre leur huile rouge, un peu d'ail et de concentré, une touche de crème, et des pâtes liées avec l'eau de cuisson. Le chorizo de bœuf ou de volaille remplace celui de porc.",
  [f"350 g|de pâtes courtes|{PATES}|3", "150 g|de chorizo de bœuf ou de volaille|Chorizo de bœuf ou de volaille|3", f"2|gousses d'ail|{AIL}|1", f"2 c. à s.|de concentré de tomate|{CONC}|1", f"15 cl|de crème liquide|{CL}|2", f"40 g|de parmesan|{PARM}|1", "1|petit bouquet de persil|Persil plat / frisé|1", f"1/2|citron|{CIT}|1"],
  ["**Pâtes.** Eau bouillante salée, cuites 1 min de moins que le paquet ; 20 cl d'eau de cuisson gardés.",
   "**Chorizo.** Rondelles fines dans la poêle froide, feu moyen, 4 min : elles grillent et rendent une huile rouge.",
   "**Sauce.** Ail râpé, 30 s ; concentré, 1 min : il fonce ; crème, 10 cl d'eau de cuisson, 2 min : nappante.",
   "**Lier.** Pâtes, parmesan, 1 min à feu doux : brillantes ; persil, un trait de citron."],
  tips=["Le chorizo est salé : saler l'eau des pâtes, pas la sauce."], keep="1 jour au frigo.", age=3, cats=["enfants", "express"], profil=["gras", "epice"],
  credit=C(V("erynshow", "7688422280258407712")))
K("tataki_boeuf", "Tataki de bœuf (saisi minute, sauce ponzu, ail croustillant)", "Gyū no tataki", "Asie de l'Est › Japon", "E", 2, 4, 20, 20, "€€€", "Poêle en fonte, couteau bien affûté.",
  "Un pavé de bœuf saisi à feu très vif sur toutes ses faces, refroidi, puis tranché très fin : la croûte grillée, le cœur cru et rouge. Avec une sauce ponzu, de l'ail en lamelles frit, de la cébette et du sésame.",
  ["500 g|de bœuf très frais (rumsteck ou filet, en pavé épais)|Rumsteck|3", "6 c. à s.|de sauce ponzu (ou soja + citron)|Sauce ponzu|2", f"4|gousses d'ail|{AIL}|1", f"2 cm|de gingembre|{GING}|1", "2|cébettes|Oignon nouveau / cébette|1", "1 c. à s.|de sésame|Sésame (blanc/noir)|1", f"2 c. à s.|d'huile|{HN}|1", f"1/2|citron vert|{CITV}|1"],
  ["**Ail croustillant.** Ail en lamelles fines dans l'huile froide, feu doux, 3 min : blond ; égoutté (il brunit hors du feu).",
   "**Saisir.** Pavé salé, poivré ; poêle fumante, 1 min par face, côtés compris : croûte brune partout, cœur cru.",
   "**Refroidir.** Aussitôt dans un bain d'eau glacée 1 min (ou au frigo 20 min) : la cuisson s'arrête ; épongé.",
   "**Trancher.** En tranches de 3 mm contre les fibres, en éventail ; ponzu, gingembre râpé, cébette, sésame, ail croustillant, citron vert."],
  tips=["Viande crue à cœur : très fraîche, achetée le jour même ; pas pour les enfants de moins de 6 ans, les femmes enceintes ni les personnes âgées."],
  keep="À manger tout de suite.", age=None, kids="Viande crue à cœur : pour les adultes et les grands enfants.", cats=[], fetes=["Apéritif dînatoire"], profil=["acide", "viande_rouge"],
  credit=C(V("erynshow", "7675810781979544865")))
K("enoki_ail_soja", "Champignons enoki sautés à l'ail, au soja et au beurre", "Enoki sautés", "Asie de l'Est › Corée", "E", 1, 2, 5, 5, "€", "Poêle.",
  "Les longs champignons blancs en grappe, sautés quelques minutes avec beaucoup d'ail, du soja, une noix de beurre et un peu de piment : fondants et légèrement croquants, à manger sur du riz ou en accompagnement.",
  ["200 g|de champignons enoki (ou de pleurotes en lanières)|Pleurote|3", f"3|gousses d'ail|{AIL}|1", f"1 c. à s.|de sauce soja|{SOJA}|2", f"15 g|de beurre|{BEURRE}|1", "1|cébette|Oignon nouveau / cébette|1", "1 pincée|de flocons de piment|Flocons de piment|1?", f"1 c. à c.|d'huile|{HN}|1", f"1/2|citron vert|{CITV}|1"],
  ["**Préparer.** Pied terreux des enoki coupé, grappe séparée en petits bouquets ; ail haché.",
   "**Saisir.** Poêle chaude huilée, enoki étalés, 2 min sans remuer : ils dorent dessous.",
   "**Assaisonner.** Beurre, ail, 1 min ; soja, piment, 30 s : brillants.",
   "**Servir.** Cébette, un trait de citron vert, sur du riz chaud."],
  tips=["Les enoki se mangent toujours cuits (risque de listeria quand ils sont crus)."], keep="Le jour même.", age=3, cats=["vegetarien", "express"], profil=["gras", "acide"],
  credit=C(V("erynshow", "7232746604367858970")))
K("avocats_saumon_fume_fromage_frais", "Avocats garnis au saumon fumé et au fromage frais", "Avocat saumon-Philadelphia", "France › Food fusion", "E", 1, 4, 10, 0, "€€", "Couteau, cuillère.",
  "La « recette flemme » d'Eryn : des demi-avocats garnis de fromage frais, de saumon fumé, de citron et d'aneth, avec du sésame et une pointe de piment. Une entrée sans cuisson en dix minutes, ou un déjeuner avec du pain.",
  ["2|avocats mûrs|Avocat|3", "150 g|de saumon fumé|Saumon fumé|3", "100 g|de fromage frais nature (type Philadelphia)|Fromage à tartiner / fondu|2", f"1/2|citron|{CIT}|1", "1|branche d'aneth|Aneth|1", "1 c. à c.|de sésame|Sésame (blanc/noir)|1?", "1 pincée|de piment d'Espelette|Piment d'Espelette|1?"],
  ["**Ouvrir.** Avocats coupés en deux, noyau retiré, chair arrosée de citron (elle ne noircit pas).",
   "**Garnir.** Une cuillère de fromage frais dans le creux, saumon fumé en rubans par-dessus.",
   "**Assaisonner.** Aneth, poivre, sésame, piment, un trait de citron.",
   "**Servir.** Aussitôt, avec du pain grillé."],
  tips=["Femme enceinte : saumon fumé déconseillé (listeria)."], keep="À manger tout de suite.", age=3, cats=["express", "brunch"], profil=["gras", "poisson", "acide"],
  credit=C(V("erynshow", "7693994300459207969")))
