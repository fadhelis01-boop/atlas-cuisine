# -*- coding: utf-8 -*-
"""Vague 7 (fin) · Vidéos les plus enregistrées lues en dernier (22/10/2026) : cheesecakes de @on_est_gourmands (les vidéos
les plus enregistrées de tout le relevé), risotto cacio e pepe, classiques des traiteurs chinois. Fiches réécrites et
créditées (`credit`). NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *
from recipes_v6_tiktok_plats import C, VB

K("cheesecake_sans_cuisson_chocolat_noisette", "Cheesecake sans cuisson chocolat-noisette (crème au fromage frais et ganache)", "No-bake cheesecake", "Amérique du Nord › États-Unis", "D", 2, 8, 30, 0, "€€", "Moule à charnière de 20 cm, batteur.",
  "Le dessert le plus enregistré de tous les favoris : un fond de biscuits au cacao, une crème au fromage frais allégée de chantilly, et une ganache au chocolat coulée dessus. Pas de four, une nuit au frais.",
  ["200 g|de biscuits au cacao|Biscuits (spéculoos, sablés)|2", f"80 g|de beurre fondu|{BEURRE}|1", "400 g|de fromage frais (type Philadelphia)|Fromage à tartiner / fondu|3", f"30 cl|de crème liquide entière froide (20 + 10)|{CL}|3", "1 c. à s.|de sucre glace|Sucre glace|1", "1/2|gousse de vanille|Vanille (gousse)|1", f"100 g|de chocolat noir ou au lait|{CHOCO}|2", "40 g|de noisettes grillées concassées|Noisette|1"],
  ["**Fond.** Biscuits mixés, beurre fondu : sable humide ; tassé au fond du moule ; 30 min au frais.",
   "**Crème.** Fromage frais, sucre glace, graines de vanille fouettés : lisses ; 20 cl de crème montée en chantilly ferme, incorporée à la maryse : mousse dense ; étalée sur le fond ; 2 h au frais.",
   "**Ganache.** 10 cl de crème portée au frémissement (2 min), versée sur le chocolat haché, 1 min, mélangée : lisse et brillante ; tiédie 10 min, coulée sur la crème.",
   "**Prendre.** Noisettes dessus, une nuit au frais : il se démoule net."],
  tips=["Version pistache (même vidéaste) : 2 c. à s. de pâte de pistache mélangée à du praliné et des crêpes dentelle émiettées sur le fond, crème parfumée à la pistache, sans ganache.",
        "Version caramel : un caramel au beurre salé (120 g de sucre, 80 g de crème, 50 g de beurre demi-sel) refroidi, coulé à la place de la ganache, fond de spéculoos."],
  keep="3 jours au frigo.", age=3, cats=["fetes"], fetes=["Anniversaire", "Repas de famille", "Noël"], profil=["sucre", "chocolat"], tech=["Ganache", "Chantilly"],
  credit=C(("@on_est_gourmands", "https://www.tiktok.com/@on_est_gourmands/video/7559625571702033686"), ("@on_est_gourmands", "https://www.tiktok.com/@on_est_gourmands/video/7504704688407858454"), ("@on_est_gourmands", "https://www.tiktok.com/@on_est_gourmands/video/7692831568049605921")))
K("cheesecake_yaourt", "Cheesecake au yaourt, cuisson courte sans bain-marie", "Cheesecake au yaourt", "Amérique du Nord › États-Unis", "D", 2, 8, 20, 45, "€€", "Cercle ou moule de 20 cm, saladier.",
  "Un cheesecake cuit plus léger que le new-yorkais : la moitié du fromage est remplacée par du yaourt, la cuisson est douce et courte, sans bain-marie. Crémeux, il se découpe parfaitement, nappé d'une pâte à tartiner tiédie.",
  ["200 g|de biscuits (petits-beurre, spéculoos)|Biscuits (spéculoos, sablés)|2", f"80 g|de beurre fondu|{BEURRE}|1", "500 g|de fromage frais (type Philadelphia)|Fromage à tartiner / fondu|3", f"250 g|de yaourt nature|{YAO}|3", f"50 g|de sucre|{SUCRE}|1", f"2|œufs|{OEUF}|2", "1/2|gousse de vanille (graines)|Vanille (gousse)|1", "100 g|de pâte à tartiner noisette (pour finir)|Pâte à tartiner chocolat-noisette|1?"],
  ["**Fond.** Biscuits mixés, beurre fondu, tassés au fond du moule ; 15 min à 170 °C : doré et ferme.",
   "**Appareil.** Fromage, sucre et vanille mélangés à la spatule ; yaourt, puis œufs un à un, sans fouetter fort (pas de bulles) : lisse.",
   "**Cuire.** Sur le fond précuit, 30 min à 150 °C : bords pris, centre qui tremble encore ; 1 h dans le four éteint, porte entrouverte (il ne fend pas).",
   "**Reposer.** Une nuit au frais ; pâte à tartiner tiédie 15 s, coulée dessus au moment de servir."],
  keep="3 jours au frigo.", age=1, cats=["fetes", "enfants"], fetes=["Anniversaire"], profil=["sucre", "acide"],
  credit=C(("@on_est_gourmands", "https://www.tiktok.com/@on_est_gourmands/video/7233449344475696411")))
K("risotto_cacio_e_pepe", "Risotto cacio e pepe (pecorino, parmesan et poivre grillé)", "Risotto cacio e pepe", "Europe du Sud › Italie", "P", 2, 2, 10, 20, "€€", "Sauteuse large, petite poêle.",
  "Le goût des pâtes cacio e pepe dans un risotto : poivre concassé grillé à sec, crème de pecorino et de parmesan montée à l'eau poivrée, ajoutée hors du feu au riz crémeux. Végétarien, très gourmand.",
  ["200 g|de riz carnaroli ou arborio|Riz à risotto (arborio, carnaroli)|3", "75 g|de pecorino râpé fin|Pecorino|3", f"50 g|de parmesan râpé fin|{PARM}|2", f"1 c. à s.|de poivre noir en grains|{POIVRE}|2", f"30 g|de beurre|{BEURRE}|1", "70 cl|de bouillon de légumes chaud|Bouillon cube légumes|2", "8 cl|de vin blanc sec|Vin blanc|1", f"1/2|citron (zeste)|{CIT}|1?"],
  ["**Poivre.** Concassé grossièrement, 1 min à sec dans la petite poêle : il sent fort ; une pincée gardée ; 12 cl d'eau chaude, 1 min : eau poivrée.",
   "**Crème.** Parmesan et ⅔ du pecorino, eau poivrée tiède (pas bouillante) versée peu à peu en fouettant : crème lisse et épaisse.",
   "**Risotto.** Moitié du beurre, riz 1 min : bords translucides ; vin, absorbé ; bouillon louche par louche, 17 min en remuant souvent : grains tendres avec un léger cœur, texture qui ondule.",
   "**Lier.** Hors du feu, reste du beurre et crème de fromage, 1 min en remuant vivement : crémeux et brillant ; reste du pecorino et poivre gardé, zeste si tu veux."],
  tips=["Hors du feu toujours : sur le feu, le pecorino forme des grumeaux."],
  keep="Le jour même.", age=3, cats=["vegetarien"], profil=["gras"], var=[VB],
  credit=C(("@bortipastabar", "https://www.tiktok.com/@bortipastabar/video/7678795001995726111")))
K("poulet_general_tao", "Poulet du Général Tao (croustillant, sauce sucrée-acidulée pimentée)", "Zuǒ zōngtáng jī", "Asie de l'Est › Chine", "P", 2, 4, 30, 20, "€", "Casserole à friture, wok, thermomètre.",
  "Le classique des restaurants chinois d'Amérique du Nord, version maison : hauts de cuisse marinés au blanc d'œuf, frits deux fois pour un croustillant qui tient, enrobés d'une sauce à l'ail, au gingembre, au vinaigre noir et au piment.",
  [f"4|hauts de cuisse désossés (600 g)|{CUISSE}|3", f"1|blanc d'œuf|{OEUF}|1", "80 g|de fécule de pomme de terre (+ ½ c. à s. pour la sauce)|Fécule de pomme de terre|2", f"3|gousses d'ail|{AIL}|1", f"3 cm|de gingembre|{GING}|1", "4|piments séchés|Flocons de piment|1", f"3 c. à s.|de sucre|{SUCRE}|2", f"2 c. à s.|de sauce soja|{SOJA}|2", "2 c. à s.|de vinaigre noir chinois (ou de riz)|Vinaigre noir chinois (Chinkiang)|2", "1|cébette et 1 c. à c. de sésame|Oignon nouveau / cébette|1", "1 l|d'huile de friture|Huile d'arachide|1"],
  ["**Mariner.** Poulet en gros morceaux, sel, poivre, blanc d'œuf, 1 c. à s. de fécule : 30 min.",
   "**Frire deux fois.** Enrobé de fécule ; 3 min à 170 °C : pâle et pris ; 3 min de repos ; 1 min 30 à 190 °C : doré et très croustillant ; égoutté.",
   "**Sauce.** Sucre, soja, vinaigre, ½ c. à s. de fécule, 6 cl d'eau mélangés ; wok, 1 c. à s. d'huile, ail et gingembre râpés, piments, 30 s ; sauce, 1 min : épaisse et brillante.",
   "**Enrober.** Poulet, 20 s en sautant : tout est laqué, encore croustillant ; cébette, sésame ; avec du riz."],
  keep="Le jour même.", age=6, cats=[], profil=["epice", "acide"], tech=["Frire en sécurité"], side="riz_nature",
  credit=C(("@olivier.lin1", "https://www.tiktok.com/@olivier.lin1/video/7677252100778151190")))
K("salade_poulet_traiteur_chinois", "Salade au poulet du traiteur chinois, vinaigrette blanche", "Salade du traiteur chinois", "France › Cuisine du quotidien", "P", 1, 2, 20, 10, "€", "Casserole, saladier, fouet.",
  "La salade des traiteurs chinois de France : batavia émincée très fin et carotte en julienne, rafraîchies dans l'eau glacée, poulet poché, et la fameuse sauce blanche, une mayonnaise sucrée, vinaigrée et allongée d'eau froide.",
  [f"1|blanc de poulet|{BLANC_P}|3", "1|salade batavia|Salade (laitue, batavia)|3", f"1|carotte|{CAROTTE}|1", f"2|jaunes d'œufs|{OEUF}|2", f"1 c. à s.|de moutarde de Dijon|{DIJON}|1", f"3 c. à c.|de sucre|{SUCRE}|1", "2 c. à s.|de vinaigre blanc|Vinaigre blanc|1", f"15 cl|d'huile de tournesol (+ un peu d'olive)|{HN}|2", "1 c. à c.|d'huile de sésame|Huile de sésame (grillée)|1", f"1/2|citron|{CIT}|1", f"1 pincée|de sel|{SEL}|1"],
  ["**Pocher.** Poulet dans l'eau frémissante salée, 3 min ; feu coupé, 12 min dans l'eau chaude : blanc et juteux, 74 °C à cœur ; émincé.",
   "**Croquant.** Batavia émincée fin, carotte en julienne, 10 min dans l'eau glacée ; égouttées, bien essorées.",
   "**Sauce.** Jaunes, moutarde, sucre, sel, poivre, vinaigre ; huile en filet en fouettant : mayonnaise ferme ; 3 à 4 c. à s. d'eau froide : fluide et nappante ; sésame, citron.",
   "**Servir.** Salade, carotte, poulet, sauce généreuse."],
  keep="Sauce : 2 jours au frigo ; salade le jour même.", age=1, cats=["salade", "express"], profil=["leger", "acide"],
  credit=C(("@olivier.lin1", "https://www.tiktok.com/@olivier.lin1/video/7696520585995816194")))

# ———————————————————————————————— plats végétariens (garder au moins un tiers de plats sans viande ni poisson)
K("borek_feuilles_riz", "Börek express au papier de riz et au fromage (à la poêle)", "Börek au papier de riz", "Moyen-Orient › Turquie", "P", 1, 4, 15, 20, "€", "Poêle antiadhésive de 24 cm, grande assiette.",
  "La version rapide du börek qui a fait le tour des réseaux : des feuilles de riz trempées dans un mélange d'œufs, de lait et de yaourt, empilées à la poêle autour d'une couche de fromage. Croustillant dehors, fondant comme une pâte feuilletée dedans.",
  ["20|feuilles de riz (galettes de 22 cm)|Galettes de riz (rice paper)|3", f"2|œufs|{OEUF}|2", f"12 cl|de lait|{LAIT}|1", f"4 c. à s.|de yaourt nature|{YAO}|1", f"4 c. à s.|d'huile neutre|{HN}|1", "150 g|de feta émiettée|Feta|2", "100 g|de mozzarella râpée|Mozzarella / burrata|2", "1|cébette|Oignon nouveau / cébette|1", f"1 noix|de beurre|{BEURRE}|1", f"1/2 c. à c.|de sel|{SEL}|1"],
  ["**Bain.** Œufs, lait, yaourt, huile, sel fouettés dans un plat large.",
   "**Empiler.** Poêle beurrée ; 10 feuilles trempées 5 s chacune dans le bain, posées l'une sur l'autre ; fromages et cébette ; 10 autres feuilles trempées ; reste du bain versé dessus.",
   "**Cuire.** 10 min à feu moyen-doux, couvercle entrouvert, bulles percées au couteau : dessous doré et croustillant.",
   "**Retourner.** À l'aide d'une assiette, 8 min de l'autre côté : doré, le fromage coule ; en parts, avec une salade de tomates."],
  keep="Le jour même.", age=1, cats=["vegetarien", "enfants", "fusion"], profil=["gras"],
  credit=C(("@madeinkatia", "https://www.tiktok.com/@madeinkatia/video/7689481478366973216"), ("@kor_.ay", "https://www.tiktok.com/@kor_.ay/video/7635987751430638881")))
K("galettes_pommes_de_terre_fromage", "Galettes de pommes de terre au fromage fondant (à la poêle)", "Galettes pomme de terre-fromage", "Europe du Nord › Ukraine", "P", 1, 4, 20, 30, "€", "Casserole, poêle.",
  "Des galettes de purée et de farine, fourrées d'un cœur de fromage qui fond, dorées à la poêle : un plat de placard qui plaît à toute la famille, avec de la crème aigre à l'aneth et une salade.",
  [f"800 g|de pommes de terre farineuses|{PDT}|3", f"120 g|de farine|{F55}|2", f"1|œuf|{OEUF}|1", "150 g|de mozzarella ou d'emmental|Mozzarella / burrata|2", f"20 cl|de crème fraîche|{CF}|2", "1 c. à s.|d'aneth ou de ciboulette|Aneth|1", f"3 c. à s.|d'huile|{HN}|1", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Purée.** Pommes de terre à l'eau salée, 20 min : tendres ; écrasées, tiédies 10 min.",
   "**Pâte.** Farine, œuf, sel : pâte souple qui ne colle plus aux mains (un peu de farine si besoin).",
   "**Fourrer.** 8 boules aplaties, un dé de fromage au centre, refermées, aplaties en galettes de 2 cm.",
   "**Dorer.** 4 min par face dans l'huile à feu moyen : croûte dorée, fromage fondu ; crème mélangée à l'aneth et une pincée de sel, à côté."],
  keep="2 jours au frigo ; réchauffées à la poêle.", age=1, cats=["vegetarien", "enfants"], profil=["gras", "acide"],
  credit=C(("@malcomsfood2", "https://www.tiktok.com/@malcomsfood2/video/7621594506248342806")))
K("lobia_curry", "Lobia (curry de haricots cornille à la tomate, Pakistan)", "Lobia masala", "Asie du Sud › Pakistan", "P", 1, 4, 15, 40, "€", "Cocotte.",
  "Le curry de haricots à œil noir des cuisines familiales du Pakistan et de l'Inde du Nord : oignon roussi, tomate, gingembre, ail et épices, haricots mijotés jusqu'à être crémeux. Avec du riz basmati ou des chapatis.",
  ["500 g|de haricots cornille cuits (ou 200 g secs, trempés une nuit)|Haricots blancs / lingots|3", f"2|oignons|{OIG}|2", f"3|tomates|{TOM}|2", f"3|gousses d'ail|{AIL}|1", f"2 cm|de gingembre|{GING}|1", f"1 c. à c.|de cumin en grains|{CUMIN}|1", f"1/2 c. à c.|de curcuma|{CURC}|1", "1 c. à c.|de garam masala|Garam masala|1", f"1/2 c. à c.|de piment en poudre|{CAYENNE}|1", f"1 poignée|de coriandre|{CORI}|1", f"1|citron|{CIT}|1", f"3 c. à s.|d'huile|{HN}|1", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Oignons.** Cumin 30 s dans l'huile chaude : il crépite ; oignons émincés, 10 min : bien dorés.",
   "**Masala.** Ail et gingembre râpés 1 min ; tomates en dés, curcuma, piment, sel, 8 min : l'huile se sépare de la sauce.",
   "**Mijoter.** Haricots et 40 cl d'eau, 20 min à petit feu : quelques haricots écrasés à la cuillère épaississent la sauce, crémeuse.",
   "**Finir.** Garam masala, coriandre, jus de citron ; avec du riz."],
  keep="3 jours au frigo ; se congèle.", age=3, cats=["vegetarien"], profil=["epice"], tech=["Mijoter"], side="riz_nature",
  credit=C(("@cookwithnabeela", "https://www.tiktok.com/@cookwithnabeela/video/7526511565403639062")))
K("masala_omelette", "Omelette masala (oignon, tomate, piment vert, coriandre)", "Masala omelette", "Asie du Sud › Inde", "P", 1, 2, 10, 6, "€", "Poêle.",
  "L'omelette des petits déjeuners indiens et pakistanais : œufs battus avec oignon, tomate, piment vert et coriandre, une pincée de curcuma et de piment, cuite fine et pliée. Avec un paratha, du pain ou du riz.",
  [f"4|œufs|{OEUF}|3", f"1|petit oignon|{OIG}|1", f"1|tomate|{TOM}|1", f"1|piment vert|{PIMENT}|1", f"1 c. à s.|de coriandre|{CORI}|1", f"1 pincée|de curcuma|{CURC}|1", f"1 pincée|de piment en poudre|{CAYENNE}|1", f"1 noix|de beurre ou de ghee|{BEURRE}|1", f"1 pincée|de sel|{SEL}|1", "2|chapatis ou parathas|Atta|1?"],
  ["**Battre.** Œufs, sel, curcuma, piment en poudre ; oignon, tomate épépinée, piment vert et coriandre hachés fin.",
   "**Cuire.** Beurre fondu, omelette étalée, 3 min à feu moyen sans remuer : bords dorés, dessus presque pris.",
   "**Plier.** Retournée ou pliée en deux, 1 min : dorée, cœur juste cuit.",
   "**Servir.** Avec un pain plat chaud et du ketchup, comme dans les rues de Lahore."],
  keep="Le jour même.", age=3, cats=["vegetarien", "express", "brunch"], profil=["epice"],
  credit=C(("@cookwithnabeela", "https://www.tiktok.com/@cookwithnabeela/video/7529124194307558678")))
