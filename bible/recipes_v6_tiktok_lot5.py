# -*- coding: utf-8 -*-
"""Vague 8 · Favoris TikTok ajoutés entre le 22/10 et le 29/10/2026 (compte connecté par le propriétaire). Fiches réécrites
(étapes reformulées, repères et durées ATLAS) et créditées (`credit`) : rien n'est recopié des légendes. Quand la légende
ne donne que le nom du plat, la fiche suit la recette de référence du plat et la vidéo est créditée comme source d'idée.
NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *
from recipes_v6_tiktok_plats import C, VB

DINDE_J = "Jambon de dinde / de poulet"; RACLETTE = "Reblochon / raclette / mont-d'or"; PTN = "Pâte à tartiner chocolat-noisette"

# ———————————————————————————————— goûters et desserts
K("cookies_rocher_coeur_noisette", "Cookies Rocher au cœur coulant noisette, enrobage chocolat au lait et noisettes", "Cookies Rocher", "France › Food fusion", "G", 2, 5, 30, 20, "€€", "Plaque, papier cuisson, petite casserole, congélateur.",
  "Le favori le plus enregistré de la semaine : de gros cookies épais qui cachent une boule de pâte à tartiner congelée (elle reste coulante à la cuisson), trempés une fois refroidis dans un chocolat au lait aux noisettes, comme la confiserie.",
  [f"120 g|de pâte à tartiner noisette (cœurs)|{PTN}|2", f"120 g|de beurre mou|{BEURRE}|2", f"140 g|de sucre (90 g de cassonade + 50 g de blanc)|{SUCRE}|2", f"1|œuf|{OEUF}|1", f"220 g|de farine|{F55}|3", "10 g|de maïzena|Fécule de maïs (maïzena)|1", "1/2 c. à c.|de bicarbonate (+ ½ c. à c. de levure chimique)|Bicarbonate de soude|1", f"100 g|de chocolat noir haché|{CHOCO}|2", "250 g|de chocolat au lait (enrobage)|Chocolat au lait|2", "50 g|de noisettes grillées concassées|Noisette|2", "10 g|d'huile de coco désodorisée|Huile de coco|1", "1|gousse de vanille (graines) ou 1 sachet de sucre vanillé|Vanille (gousse)|1?"],
  ["**Cœurs.** Pâte à tartiner en 5 petits tas sur papier cuisson ; 1 h 30 au congélateur : durs comme des galets.",
   "**Pâte.** Beurre et sucres mélangés 2 min : crème claire ; œuf et vanille ; farine, maïzena, bicarbonate, levure, une pincée de sel, à la spatule juste assez pour ne plus voir de farine ; chocolat haché.",
   "**Fourrer.** 5 boules de 120 g ; chacune aplatie dans la main, un cœur congelé au centre, pâte refermée sans trou ; 30 min au frigo.",
   "**Cuire.** 14 à 17 min à 175 °C (chaleur statique), bien espacés : bords dorés, centre encore pâle et mou ; refroidir complètement sur la plaque (1 h), sinon ils cassent.",
   "**Enrober.** Chocolat au lait fondu au bain-marie (45 °C au plus) avec l'huile de coco, noisettes ; cookies trempés à moitié ou entièrement, sur papier cuisson ; 30 min au frais : enrobage figé et brillant."],
  tips=["La vanille liquide contient de l'alcool : graines de gousse ou sucre vanillé à la place.", "Sans huile de coco : l'enrobage fige aussi, un peu moins brillant."],
  keep="4 jours dans une boîte fermée, au frais l'été.", age=3, cats=["enfants", "fetes"], fetes=["Anniversaire"], profil=["sucre", "chocolat"],
  credit=C(("@on_est_gourmands", "https://www.tiktok.com/@on_est_gourmands/video/7685013248193662241")))
K("muffins_double_chocolat_noisette", "Muffins double chocolat au cœur de pâte à tartiner", "Double chocolate Nutella muffins", "Amérique du Nord › États-Unis", "G", 1, 12, 15, 22, "€", "Moule à 12 muffins, caissettes, 2 saladiers.",
  "Des muffins américains très chocolatés, bien bombés : une pâte au cacao et aux pépites, une cuillerée de pâte à tartiner cachée au milieu, et le four démarré très chaud pour qu'ils montent d'un coup.",
  [f"250 g|de farine|{F55}|3", "40 g|de cacao non sucré|Cacao en poudre non sucré|2", f"150 g|de sucre|{SUCRE}|2", f"2 c. à c.|de levure chimique (+ ½ c. à c. de bicarbonate)|{LEVC}|1", f"2|œufs|{OEUF}|2", f"20 cl|de lait|{LAIT}|2", f"1 c. à s.|de jus de citron (dans le lait)|{CIT}|1", f"10 cl|d'huile neutre|{HN}|2", "150 g|de pépites de chocolat|Pépites de chocolat|2", f"12 c. à c.|de pâte à tartiner noisette|{PTN}|2"],
  ["**Lait ribot.** Lait et jus de citron, 5 min : il épaissit et tranche légèrement (c'est voulu).",
   "**Sec.** Farine, cacao, sucre, levure, bicarbonate, une pincée de sel : mélangés au fouet.",
   "**Humide.** Œufs, lait citronné, huile ; versé sur le sec, mélangé à la spatule 15 s : encore quelques grumeaux, pas plus ; ⅔ des pépites.",
   "**Garnir.** Une cuillerée de pâte au fond de chaque caissette, une cuillère à café de pâte à tartiner, recouverte de pâte jusqu'en haut ; reste des pépites dessus.",
   "**Cuire.** 5 min à 220 °C : ils gonflent ; puis 17 min à 180 °C sans ouvrir : dôme ferme sous le doigt, pique qui ressort avec quelques miettes (le cœur reste fondant)."],
  keep="3 jours dans une boîte fermée.", age=1, cats=["enfants"], fetes=["Anniversaire"], profil=["sucre", "chocolat"],
  credit=C(("@dinewithtwo", "https://www.tiktok.com/@dinewithtwo/video/7683576551744687374")))

# ———————————————————————————————— plats
K("lasagnes_montagnardes_raclette", "Lasagnes montagnardes à la raclette (oignons fondants, version jambon de dinde)", "Lasagnes à la raclette", "France › Bourgogne-Franche-Comté", "P", 2, 6, 35, 40, "€€", "Plat à gratin de 30 cm, casserole, poêle.",
  "Des lasagnes de montagne : oignons fondus et déglacés, jambon, béchamel maison et tranches de raclette entre chaque couche de pâte, gratinées jusqu'à ce que le fromage coule sur les bords. Ici avec du jambon de dinde ; salade verte bien vinaigrée à côté.",
  [f"12|feuilles de lasagne (sans précuisson)|Lasagnes|3", f"400 g|de fromage à raclette en tranches|{RACLETTE}|3", f"6|tranches de jambon de dinde|{DINDE_J}|2", f"3|oignons|{OIG}|2", "10 cl|de vin blanc sec|Vin blanc|1", f"100 g|de beurre (80 g pour la béchamel)|{BEURRE}|2", f"80 g|de farine|{F55}|1", f"80 cl|de lait|{LAIT}|2", f"1 pincée|de muscade|{MUSC}|1", "1|salade verte, vinaigrette moutarde-vinaigre de vin|Vinaigre de vin rouge / blanc|1"],
  ["**Oignons.** Émincés, 20 g de beurre, 15 min à feu moyen : fondants et blonds ; vin blanc, 2 min : il ne reste qu'un fond sirupeux.",
   "**Béchamel.** 80 g de beurre fondu, farine, 2 min en remuant : roux mousseux ; lait froid en fouettant, 8 min : nappe la cuillère ; sel, poivre, muscade.",
   "**Monter.** Béchamel au fond ; lasagnes ; oignons, jambon en lanières, raclette ; béchamel ; on recommence 3 fois ; dernière couche : lasagnes, béchamel, raclette.",
   "**Cuire.** 40 min à 180 °C : dessus doré et bouillonnant, pointe de couteau qui entre sans résistance dans les pâtes ; 10 min de repos pour couper net ; salade vinaigrée à côté."],
  tips=["Version d'origine : jambon blanc de porc (même quantité)."], keep="2 jours au frigo ; se réchauffe au four.", age=3, cats=["enfants"], fetes=["Repas de famille"], profil=["gras"], tech=["Faire un roux"], var=[VB],
  credit=C(("@chesterfoodies", "https://www.tiktok.com/@chesterfoodies/video/7700963226996968736"), ("@chesterfoodies", "https://www.tiktok.com/@chesterfoodies/video/7438657496832675105")))
K("sauce_gombo_ivoirienne", "Sauce gombo à l'ivoirienne (bœuf, poisson fumé, huile de palme)", "Sauce gombo", "Afrique subsaharienne › Côte d'Ivoire", "P", 2, 6, 30, 70, "€€", "Grande marmite, couteau, planche.",
  "La sauce gluante préférée d'Abidjan : viande mijotée, poisson fumé émietté, gombos coupés en rondelles qui lient la sauce, une touche d'huile de palme rouge et du piment entier. Avec du foutou, du riz blanc ou du placali.",
  ["500 g|de gombos frais (ou surgelés)|Gombo (okra)|3", "500 g|de bœuf à mijoter en cubes (paleron)|Paleron|3", "150 g|de poisson fumé (maquereau, chinchard)|Poisson fumé / séché|2", f"2|tomates|{TOM}|2", f"1|oignon|{OIG}|1", f"2|gousses d'ail|{AIL}|1", "1|piment antillais entier|Piment antillais / scotch bonnet|1", "4 c. à s.|d'huile de palme rouge|Huile de palme rouge|2", "1|cube de bouillon|Bouillon cube bœuf|1", f"1|citron vert|{CITV}|1"],
  ["**Viande.** Bœuf, oignon émincé, ail, sel, 1 l d'eau ; 45 min à petit frémissement : tendre à la fourchette.",
   "**Base.** Tomates mixées, cube, poisson fumé émietté sans arêtes, piment entier (non percé) ; 10 min.",
   "**Gombos.** Lavés, bien séchés, coupés en rondelles fines (ou râpés pour une sauce plus filante) ; ajoutés avec l'huile de palme, 15 min à feu doux, sans couvercle, en remuant peu : la sauce file à la cuillère.",
   "**Servir.** Piment retiré ; quelques gouttes de citron vert au moment de servir : la sauce reste gluante mais s'éclaire ; avec foutou, riz ou placali."],
  tips=["Le piment entier parfume sans brûler ; percé, il rend la sauce très forte.", "Plus de liant : une partie des gombos râpés au lieu d'être coupés."],
  keep="2 jours au frigo.", age=6, cats=[], profil=["epice", "acide"], tech=["Mijoter"], side="riz_nature",
  credit=C(("@les.delice.d.ines", "https://www.tiktok.com/@les.delice.d.ines/video/7690862189237898529")))
K("sandwich_merguez_orientale", "Sandwich merguez à l'orientale (poivrons confits, harissa, sauce yaourt-citron)", "Sandwich merguez", "Afrique du Nord › Maghreb", "P", 1, 4, 20, 20, "€", "Poêle, petit bol.",
  "Le sandwich des snacks et des fêtes de quartier : merguez dorées à la poêle, poivrons et oignons fondus dans leur jus épicé, harissa, et une sauce yaourt au citron et à la menthe pour la fraîcheur, dans une baguette ou un pain rond.",
  ["8|merguez (bœuf, agneau)|Merguez (agneau/bœuf)|3", "2|baguettes (ou 4 pains ronds)|Baguette tradition|3", f"2|poivrons|{POIVRON}|2", f"1|oignon|{OIG}|1", "1 c. à c.|de harissa|Harissa|1", f"150 g|de yaourt nature|{YAO}|1", f"1/2|citron|{CIT}|1", "4|feuilles de menthe|Menthe|1", f"1 c. à c.|de cumin|{CUMIN}|1", f"1 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Légumes.** Poivrons et oignon en lanières, huile, cumin, sel, 12 min à feu moyen : fondants et légèrement caramélisés ; harissa, 30 s.",
   "**Merguez.** Piquées 2 fois, dans la poêle sans matière grasse, 8 à 10 min en les tournant : bien dorées, plus de rose au centre.",
   "**Sauce.** Yaourt, jus de citron, menthe ciselée, sel : fraîche et acidulée.",
   "**Monter.** Pain ouvert, réchauffé 2 min au four ; sauce, légumes, merguez, encore un trait de sauce."],
  keep="Le jour même.", age=6, cats=["express"], profil=["epice", "acide", "gras"],
  credit=C(("@chez.zakia77", "https://www.tiktok.com/@chez.zakia77/video/7683845398514896161")))

# ———————————————————————————————— entrées
K("eiersalat", "Eiersalat, salade d'œufs à l'allemande (moutarde, cornichons, ciboulette)", "Eiersalat", "Europe du Nord › Allemagne", "E", 1, 4, 15, 10, "€", "Casserole, saladier.",
  "Le cousin allemand des œufs mimosa : des œufs durs grossièrement hachés, liés d'une sauce à la mayonnaise et au yaourt, relevée de moutarde, de cornichons et de leur vinaigre, et de beaucoup de ciboulette. Sur du pain de seigle ou dans un petit pain.",
  [f"8|œufs|{OEUF}|3", "3 c. à s.|de mayonnaise maison|SUB:mayonnaise|2", f"3 c. à s.|de yaourt nature (ou grec)|{YAO}|1", f"1 c. à s.|de moutarde de Dijon|{DIJON}|1", "4|cornichons + 1 c. à s. de leur vinaigre|Cornichon|2", "1/2|botte de ciboulette|Ciboulette|2", f"1/2|oignon rouge (ou 1 échalote)|Oignon rouge|1", f"1 pincée|de paprika|{PAPRIKA}|1", "4|tranches de pain de seigle ou complet|Pain de campagne / complet|1?"],
  ["**Cuire.** Œufs dans l'eau bouillante, 10 min ; 5 min dans l'eau glacée : jaune bien pris mais encore doré, sans cerne verte ; écalés.",
   "**Sauce.** Mayonnaise, yaourt, moutarde, vinaigre des cornichons, sel, poivre : souple et acidulée.",
   "**Mélanger.** Œufs hachés au couteau en gros morceaux, cornichons et oignon en tout petits dés, ciboulette ; sauce, à la fourchette, sans écraser.",
   "**Reposer.** 30 min au frais : les saveurs se mêlent ; paprika dessus, sur le pain."],
  keep="2 jours au frigo.", age=1, cats=["express", "vegetarien"], profil=["acide"],
  credit=C(("@hoplabretz", "https://www.tiktok.com/@hoplabretz/video/7697612251770998019")))

# ———————————————————————————————— sauces, bases et sirops
K("sauce_curry_mango", "Sauce curry-mangue façon fast-food (sans additifs)", "Sauce curry mango", "France › Food fusion", "S", 1, 6, 10, 5, "€", "Mixeur plongeant, bocal.",
  "La sauce sucrée-épicée des nuggets de fast-food refaite à la maison : mangue mixée, curry doux, une base de mayonnaise allégée au yaourt, et du citron vert pour la fraîcheur. Sans arôme ni épaississant.",
  ["150 g|de mangue bien mûre (fraîche ou surgelée)|Mangue|3", "3 c. à s.|de mayonnaise maison|SUB:mayonnaise|2", f"2 c. à s.|de yaourt nature|{YAO}|1", f"1 c. à c.|de curry doux|{CUR}|2", f"1/2 c. à c.|de curcuma|{CURC}|1", f"1 c. à c.|de miel|{MIEL}|1", f"1/2|citron vert|{CITV}|1", f"1 pincée|de sel|{SEL}|1"],
  ["**Épices.** Curry et curcuma 30 s dans une poêle sèche : ils sentent fort (le goût cru disparaît).",
   "**Mixer.** Mangue, épices, miel, jus de citron vert, sel, 1 min au mixeur : purée très lisse.",
   "**Lier.** Mayonnaise et yaourt à la cuillère : sauce nappante, jaune orangé.",
   "**Reposer.** 30 min au frais : elle épaissit un peu ; ajuster citron et sel."],
  keep="3 jours au frigo (mayonnaise maison).", age=3, cats=["enfants"], profil=["sucre", "epice"],
  credit=C(("@lardoise_porto_vecchio", "https://www.tiktok.com/@lardoise_porto_vecchio/video/7701280291796552992")))
K("sauce_bourguignonne_fondue", "Sauce bourguignonne pour fondue (mayonnaise aux herbes, câpres et cornichons)", "Sauce bourguignonne", "France › Bourgogne", "S", 1, 6, 15, 0, "€", "Bol, fouet ou mixeur plongeant.",
  "La sauce qu'on achète en pot pour la fondue bourguignonne, faite en 5 minutes : une mayonnaise relevée de moutarde forte, d'échalote, de câpres, de cornichons hachés et d'herbes, avec une pointe de concentré de tomate pour la couleur. Pour la viande, les frites, les pommes de terre vapeur.",
  ["1|mayonnaise maison (1 jaune, 20 cl d'huile)|SUB:mayonnaise|3", f"1 c. à s.|de moutarde de Dijon|{DIJON}|2", f"1|échalote|{ECH}|2", "1 c. à s.|de câpres|Câpres|1", "4|cornichons|Cornichon|2", f"1 c. à s.|de persil haché (+ estragon si tu en as)|{PERSIL}|1", f"1 c. à c.|de concentré de tomate|{CONC}|1", "1 c. à c.|de vinaigre de vin|Vinaigre de vin rouge / blanc|1", f"1 pincée|de paprika|{PAPRIKA}|1"],
  ["**Hacher.** Échalote, câpres, cornichons et herbes hachés très fin au couteau.",
   "**Assaisonner.** Mayonnaise ferme, moutarde, concentré de tomate, vinaigre, paprika, au fouet : rose pâle et lisse.",
   "**Mélanger.** Hachis incorporé ; poivre ; elle doit tenir sur la cuillère.",
   "**Reposer.** 1 h au frais : l'échalote se fond dans la sauce."],
  keep="2 jours au frigo.", age=3, cats=[], fetes=["Repas de famille"], profil=["acide", "gras"],
  credit=C(("@lardoise_porto_vecchio", "https://www.tiktok.com/@lardoise_porto_vecchio/video/7699792151818816800")))
K("sirop_citron_maison", "Sirop de citron maison (zestes infusés une nuit)", "Sirop de citron", "France › Cuisine du quotidien", "B", 1, 15, 15, 1440, "€", "Casserole, râpe fine, bouteille en verre.",
  "Un sirop de citron sans arôme ni conservateur : les zestes infusent une nuit dans l'eau bouillie avec le jus, puis on fait fondre le sucre. Une part de sirop pour sept d'eau fraîche ou gazeuse ; aussi dans les thés glacés et sur un gâteau.",
  [f"4|citrons non traités (zestes et jus)|{CIT}|3", f"500 g|de sucre|{SUCRE}|3", "50 cl|d'eau|-|2"],
  ["**Zester.** Zestes râpés directement au-dessus de la casserole d'eau : les huiles parfumées tombent dans l'eau ; jus filtré (sans pépins).",
   "**Infuser.** Eau, zestes et jus portés à ébullition, 1 min ; couvert, une nuit (24 h, c'est encore mieux) : l'eau est jaune pâle et sent fort le citron.",
   "**Sucrer.** Porté à nouveau à ébullition, sucre versé, 2 min en remuant : sirop limpide.",
   "**Conserver.** Filtré, en bouteille ébouillantée, refroidi puis au frigo."],
  keep="1 mois au frigo, bouteille fermée.", age=1, cats=["enfants"], profil=["acide", "sucre"],
  credit=C(("@nicolaslepatissier", "https://www.tiktok.com/@nicolaslepatissier/video/7699158693375495456")))
K("vinaigre_epluchures_pommes", "Vinaigre de pommes maison avec les épluchures (anti-gaspi)", "Vinaigre d'épluchures", "France › Anti-gaspi", "Ba", 2, 1, 15, 60480, "€", "Grand bocal en verre, torchon propre, élastique.",
  "Les épluchures et trognons de pommes d'une tarte deviennent du vinaigre : un peu de sucre et de levure les font fermenter, puis l'air les transforme en vinaigre en quelques semaines. Pour les vinaigrettes et les pickles.",
  ["300 g|d'épluchures et trognons de pommes bio|Pomme|3", "50 cl|d'eau filtrée ou bouillie refroidie|-|3", f"2 c. à s.|de cassonade|{SUCRE}|2", f"5 g|de levure boulangère sèche|{LEV}|1"],
  ["**Mettre en bocal.** Épluchures dans le bocal ébouillanté ; eau et sucre mélangés, levure ; elles doivent être couvertes (une petite assiette pour les maintenir sous l'eau).",
   "**Première fermentation.** Torchon et élastique (l'air doit passer), à l'abri de la lumière, 2 semaines ; remuer chaque jour : de petites bulles, une odeur de cidre.",
   "**Filtrer.** Épluchures retirées, liquide remis dans le bocal propre, torchon, 4 à 6 semaines : un voile gélatineux (la « mère ») se forme, l'odeur devient franchement vinaigrée.",
   "**Mettre en bouteille.** Quand il pique comme un vinaigre : filtré, en bouteille ; la mère se garde pour lancer le suivant."],
  tips=["Moisissure duveteuse (bleue, verte, noire) en surface : tout jeter. Le voile lisse et beige est normal.", "Pendant la première fermentation il contient un peu d'alcool, qui disparaît en devenant vinaigre."],
  keep="Des mois au placard, bouteille fermée.", age=None, cats=[], profil=["acide"], zw=[("Épluchures de pommes", "d'une tarte ou d'une compote : on les congèle au fur et à mesure jusqu'à en avoir 300 g.")],
  credit=C(("@chefsquare", "https://www.tiktok.com/@chefsquare/video/7417860598571994400")))
