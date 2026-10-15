# -*- coding: utf-8 -*-
"""Vague 2 · Food fusion et compléments du monde (classiques manquants, plats de rue, végétarien)."""
from recipes_v2_base import *

FU = "France › Food fusion"
# Région d'attache de chaque fiche fusion (lieu où le plat est né ou s'est popularisé) ; la catégorie « fusion » fait le reste.
FU_REGION = {"tacos_lyonnais": "France › Auvergne-Rhône-Alpes › Lyon", "pizza_naan_tikka": "Europe du Nord & Centrale › Royaume-Uni",
  "bao_burger_bulgogi": "Amérique du Nord › États-Unis › Los Angeles", "croque_kimchi": "Amérique du Nord › États-Unis",
  "poke_bowl_saumon": "Océanie › Hawaï", "quesadilla_chevre_miel": "France › Food fusion", "tajine_poulet_coco_curry": "France › Food fusion",
  "croissant_perdu_matcha": "Asie de l'Est › Japon", "sushi_burrito": "Amérique du Nord › États-Unis › San Francisco",
  "shakshuka_verte_feta": "Moyen-Orient & Caucase › Israël"}

def fusion(id, title, origin, intro, ing, steps, kind="P", **kw):
    K(id, title, origin, FU_REGION.get(id, FU), kind, kw.pop("niveau", 1), kw.pop("portions", 4), kw.pop("actif", 20), kw.pop("repos", 20), kw.pop("cost", "€€"), kw.pop("equip", "Poêle, saladier."),
      intro, ing, steps, cats=["fusion"] + kw.pop("cats", []), **kw)

fusion("tacos_lyonnais", "French tacos maison (poulet, frites, sauce fromagère)", "French tacos",
  "Né à Lyon dans les années 2000 : une grande tortilla pliée autour de poulet, frites et sauce fromagère, toastée. Version maison sans additifs.",
  ["4|grandes tortillas de blé|Tortillas de blé|3", f"500 g|de blanc de poulet mariné au curry|{BLANC_P}|3", "1|recette de frites|SUB:frites_maison|2", "1|recette de sauce cheddar|SUB:sauce_cheddar|2", "4 c. à s.|de sauce algérienne maison|SUB:sauce_algerienne|1"],
  ["**Poulet.** Émincé, poêlé au curry.", "**Plier.** Tortilla, sauce, poulet, frites, sauce fromagère ; plie en rectangle.", "**Toaster.** Poêle-gril pressée, 3 min par face."], cats=["enfants"], age=3, profil=["gras"])
fusion("pizza_naan_tikka", "Naan pizza au poulet tikka", "Naan pizza",
  "La pâte à naan comme base de pizza, sauce tikka, poulet mariné, mozzarella et coriandre : l'Inde rencontre Naples.",
  ["4|naans|SUB:naan|3", f"300 g|de poulet mariné tandoori cuit|{BLANC_P}|3", f"200 g|de sauce tomate épicée au garam masala|{PELEES}|2", "150 g|de mozzarella|Mozzarella / burrata|2", "1|oignon rouge|Oignon rouge|1", f"1 bouquet|de coriandre|{CORI}|1", "1 bol|de raïta|SUB:raita|1"],
  ["**Garnir.** Naan, sauce, poulet, oignon, mozzarella.", "**Cuire.** 8 min à 240 °C. Coriandre, raïta en filet."], cats=["enfants"], age=3, profil=["epice"])
fusion("bao_burger_bulgogi", "Burger bulgogi au kimchi", "Bulgogi burger",
  "Un steak haché mariné bulgogi, kimchi, mayonnaise au gochujang, dans un pain brioché : Séoul à New York.",
  [f"600 g|de bœuf haché|{HACHE}|3", "1|recette de marinade bulgogi (moitié)|SUB:marinade_bulgogi|2", "4|pains burger|SUB:pains_burger|2", "150 g|de kimchi|SUB:kimchi_maison|2", f"4 c. à s.|de mayonnaise + 1 c. à s. de gochujang|SUB:mayonnaise|1", "1|concombre|Concombre|1"],
  ["**Steaks.** Viande + 3 c. à s. de marinade, galettes, saisies.", "**Monter.** Mayo épicée, steak, kimchi, concombre."], age=None, profil=["epice", "viande_rouge"])
fusion("croque_kimchi", "Croque-monsieur au kimchi et cheddar", "Kimchi grilled cheese",
  "Pain de mie beurré, cheddar fondant et kimchi acidulé : le grilled cheese qui réveille.",
  ["8 tranches|de pain de mie|Pain de mie|3", "200 g|de cheddar|Cheddar|3", "150 g|de kimchi égoutté|SUB:kimchi_maison|2", f"30 g|de beurre|{BEURRE}|1"],
  ["**Monter.** Pain beurré dehors, cheddar, kimchi, cheddar.", "**Dorer.** Poêle, 3 min par face à feu moyen, couvercle."], age=None, profil=["gras", "acide"])
fusion("poke_bowl_saumon", "Poke bowl au saumon", "Poke bowl",
  "Né à Hawaï, influencé par le Japon : riz vinaigré, saumon mariné soja-sésame, avocat, edamame, mangue, chou.",
  ["300 g|de riz à sushi|Riz rond / sushi|3", "400 g|de saumon extra-frais (ou cuit)|Saumon (frais, pavé)|3", f"4 c. à s.|de sauce soja|{SOJA}|2", "1 c. à s.|d'huile de sésame|Huile de sésame (grillée)|1", "2|avocats|Avocat|2", "150 g|d'edamame|Edamame|1", "1|mangue|Mangue|1", "¼|chou rouge|Chou blanc / rouge|1", "3 c. à s.|de vinaigre de riz|Vinaigre de riz|1"],
  ["**Riz.** Cuit, assaisonné au vinaigre de riz sucré-salé.", "**Saumon.** En dés, soja, sésame, 10 min.", "**Bol.** Riz, saumon, garnitures en quartiers, sésame."], age=None, kids="✓ dès 3 ans avec du saumon cuit.", profil=["poisson", "leger"],
  tips=["⚠️ Poisson cru : extra-frais ou congelé 7 jours ; sinon saumon cuit au four."])
fusion("quesadilla_chevre_miel", "Quesadillas chèvre, miel et thym", "Quesadillas",
  "Tortillas mexicaines garnies de chèvre, miel, thym et noix : un apéritif franco-mexicain.",
  ["8|tortillas de blé|Tortillas de blé|3", "200 g|de chèvre frais ou bûche|Chèvre (frais, bûche)|3", f"2 c. à s.|de miel|{MIEL}|2", f"2 branches|de thym|{THYM}|1", "40 g|de noix|Noix|1", "100 g|de mozzarella|Mozzarella / burrata|1"],
  ["**Garnir.** Demi-tortilla : fromages, miel, thym, noix ; plie.", "**Dorer.** À sec, 2 min par face. Triangles."], age=1, fetes=["Apéritif dînatoire"], profil=["gras", "sucre"])
fusion("tajine_poulet_coco_curry", "Poulet coco-curry aux patates douces (Afrique-Inde)", "Poulet coco-curry",
  "Un mijoté qui mêle mafé, curry indien et cuisine des Antilles : coco, curry, patate douce, cacahuète.",
  [f"1 kg|de hauts de cuisse|{CUISSE}|3", f"40 cl|de lait de coco|{COCO}|3", "2|patates douces|Patate douce|2", f"2 c. à s.|de curry|{CUR}|2", "2 c. à s.|de beurre de cacahuète|Beurre de cacahuète|1", f"1|oignon + gingembre + ail|{OIG}|1", f"2|tomates|{TOM}|1", f"1|citron vert|{CITV}|1", f"1 bouquet|de coriandre|{CORI}|1"],
  ["**Dorer.** Poulet, oignon, ail-gingembre, curry.", "**Mijoter.** Tomates, coco, cacahuète, patates douces, 30 min.", "**Finir.** Citron vert, coriandre."], cats=["enfants"], age=1, profil=["epice"], tips=["⚠️ Arachide."])
fusion("croissant_perdu_matcha", "Croissants perdus au matcha et chocolat blanc", "Pain perdu de croissant",
  "Des croissants rassis trempés dans un lait au matcha, dorés, et nappés de chocolat blanc : Paris-Kyoto au petit-déjeuner.",
  ["4|croissants rassis|SUB:croissants|3", f"2|œufs|{OEUF}|2", f"20 cl|de lait|{LAIT}|2", "1 c. à c.|de matcha|-|1", "60 g|de chocolat blanc|Chocolat blanc|1", f"20 g|de beurre|{BEURRE}|1"],
  ["**Tremper.** Croissants coupés en deux dans œufs + lait + matcha.", "**Dorer.** Au beurre.", "**Napper.** Chocolat blanc fondu."], kind="G", cats=["zero_dechet"], age=None, kids="Matcha = théine : plutôt pour les grands.", profil=["sucre"])
fusion("sushi_burrito", "Sushi burrito", "Sushirrito",
  "Une grande feuille de nori roulée comme un burrito : riz vinaigré, poulet teriyaki ou thon, avocat, crudités.",
  ["4|feuilles de nori|Algue nori|3", "400 g|de riz à sushi cuit vinaigré|Riz rond / sushi|3", "300 g|de poulet teriyaki|SUB:poulet_teriyaki|3", "1|avocat|Avocat|2", f"1|carotte|{CAROTTE}|1", "1|concombre|Concombre|1", f"2 c. à s.|de mayonnaise|SUB:mayonnaise|1"],
  ["**Étaler.** Riz sur ⅔ de la nori.", "**Garnir.** En ligne, poulet, légumes en bâtonnets, mayo.", "**Rouler.** Serré dans du film, coupe en deux."], cats=["enfants"], age=3, profil=["leger"])
fusion("shakshuka_verte_feta", "Chakchouka verte aux épinards et feta", "Green shakshuka",
  "La version moderne, verte : poireaux, épinards, courgette et herbes, œufs pochés et feta. Entre Tunisie et Israël.",
  ["300 g|d'épinards|Épinard|3", "1|poireau|Poireau|2", "1|courgette|Courgette|1", f"4|œufs|{OEUF}|3", "100 g|de feta|Feta|2", f"1 c. à c.|de cumin|{CUMIN}|1", f"1 bouquet|de coriandre|{CORI}|1", f"3 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Fondre.** Poireau, courgette, cumin, épinards.", "**Œufs.** Nids, œufs, couvert 5 min. Feta, herbes."], age=1, profil=["leger"])

K("gnocchi_maison", "Gnocchi de pommes de terre, beurre-sauge", "Gnocchi di patate", "Europe du Sud › Italie › Vénétie", "P", 2, 4, 40, 45, "€", "Presse-purée, grande casserole, poêle.",
  "Gnocchi légers comme des nuages : pommes de terre farineuses cuites au four (moins d'eau), peu de farine.",
  [f"1 kg|de pommes de terre farineuses|{PDT}|3", f"200 g|de farine|{F55}|2", f"1|œuf|{OEUF}|1", f"60 g|de beurre|{BEURRE}|2", "12|feuilles de sauge|Sauge|2", f"40 g|de parmesan|{PARM}|1"],
  ["**Cuire.** Pommes de terre au four, 45 min à 200 °C ; chair passée au presse-purée, tiède.", "**Pâte.** Farine, œuf, sel, sans pétrir : à peine liée.", "**Former.** Boudins, tronçons de 2 cm.", "**Pocher.** Ils remontent : 30 s de plus. Poêlés au beurre-sauge, parmesan."],
  age=1, cats=["enfants"], profil=["gras"])

K("pates_puttanesca", "Spaghetti alla puttanesca", "Spaghetti alla puttanesca", "Europe du Sud › Italie › Campanie", "P", 1, 4, 10, 15, "€", "Casserole, sauteuse.",
  "Tomate, olives, câpres, anchois, ail et piment : une sauce de placard, puissante, prête pendant la cuisson des pâtes.",
  [f"400 g|de spaghetti|{PATES}|3", f"400 g|de tomates pelées|{PELEES}|3", "80 g|d'olives noires|Olives (vertes / noires)|2", "2 c. à s.|de câpres|Câpres|2", "4|filets d'anchois|Anchois (filets, conserve)|2", f"3 gousses|d'ail|{AIL}|1", f"1 pincée|de piment|{CAYENNE}|1", f"4 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Sauce.** Ail, anchois (ils fondent), piment ; tomates, olives, câpres, 10 min.", "**Lier.** Pâtes al dente, eau de cuisson, persil."], age=3, profil=["acide"])

K("pates_alla_norma", "Pâtes alla Norma", "Pasta alla Norma", "Europe du Sud › Italie › Sicile", "P", 1, 4, 20, 25, "€", "Poêle, casserole.",
  "Aubergines frites, sauce tomate au basilic et ricotta salée râpée : le plat de Catane.",
  [f"400 g|de rigatoni|{PATES}|3", "2|aubergines|Aubergine|3", f"500 g|de passata|{PELEES}|2", f"2 gousses|d'ail|{AIL}|1", "1 poignée|de basilic|Basilic|1", "80 g|de ricotta salée ou de feta|Ricotta|2", f"8 c. à s.|d'huile d'olive|{HO}|2"],
  ["**Aubergines.** En cubes, dorées à l'huile.", "**Sauce.** Ail, passata, basilic, 15 min ; aubergines.", "**Servir.** Pâtes, sauce, ricotta râpée."], age=1, cats=["enfants"], profil=["leger"])

K("arancini", "Arancini (boulettes de risotto)", "Arancini", "Europe du Sud › Italie › Sicile", "E", 2, 12, 40, 15, "€", "Casserole profonde.",
  "Risotto de la veille roulé autour d'un cœur de mozzarella, pané, frit : croustillant et filant.",
  ["500 g|de risotto froid (reste)|Riz à risotto (arborio, carnaroli)|3", "100 g|de mozzarella en dés|Mozzarella / burrata|2", f"2|œufs|{OEUF}|1", f"60 g|de farine|{F55}|1", "100 g|de chapelure|Chapelure|2", "1 L|d'huile|Huile d'arachide|1"],
  ["**Former.** Boules de risotto, un dé de mozzarella au centre.", "**Paner.** Farine, œuf, chapelure.", "**Frire.** 4 min à 175 °C."], age=3, cats=["zero_dechet", "enfants"], fetes=["Apéritif dînatoire"], profil=["gras"], tech=["Paner", "Frire"])

K("pain_tomate_catalan", "Pa amb tomàquet (pain à la tomate)", "Pa amb tomàquet", "Europe du Sud › Espagne › Catalogne", "E", 1, 4, 5, 5, "€", "Grille-pain.",
  "Pain grillé frotté d'ail et de tomate mûre, huile d'olive et sel : trois minutes, un bonheur.",
  ["8 tranches|de pain de campagne|Pain de campagne / complet|3", f"2|tomates très mûres|{TOM}|3", f"1 gousse|d'ail|{AIL}|1", f"4 c. à s.|d'huile d'olive|{HO}|2", "1 pincée|de fleur de sel|Sel fin / gros sel / fleur de sel|0"],
  ["**Griller.** Le pain.", "**Frotter.** Ail, puis demi-tomate qu'on écrase dessus.", "**Finir.** Huile, sel."], age=1, cats=["enfants"], fetes=["Apéritif dînatoire"], profil=["leger"])

K("croquetas", "Croquetas de poulet", "Croquetas de pollo", "Europe du Sud › Espagne", "E", 2, 24, 50, 240, "€", "Casserole, poêle profonde.",
  "Béchamel épaisse au poulet effiloché, panée, frite : crémeuse dedans, croustillante dehors. Le tapas anti-gaspi.",
  [f"250 g|de poulet cuit effiloché|{BLANC_P}|3", f"50 cl|de lait|{LAIT}|2", f"70 g|de beurre + 80 g de farine|{BEURRE}|2", f"1|oignon|{OIG}|1", f"2|œufs|{OEUF}|1", "150 g|de chapelure|Chapelure|2", f"1 pincée|de muscade|{MUSC}|0", "1 L|d'huile|Huile d'arachide|1"],
  ["**Béchamel.** Oignon au beurre, farine, lait chaud, 10 min : très épaisse ; poulet. Refroidie 4 h.", "**Former.** Petits boudins, œuf, chapelure.", "**Frire.** 2 min à 180 °C."], age=3, cats=["zero_dechet"], fetes=["Apéritif dînatoire"], profil=["gras"], tech=["Roux", "Paner"])

K("frango_piri", "Poulet piri-piri grillé", "Frango piri-piri", "Europe du Sud › Portugal", "P", 1, 4, 15, 45, "€€", "Barbecue ou four.",
  "Poulet en crapaudine mariné à la sauce piri-piri, grillé et badigeonné : piquant et fumé.",
  ["1|poulet ouvert en crapaudine|Poulet entier|3", "1|recette de sauce piri-piri|SUB:sauce_piri_piri|3", f"1|citron|{CIT}|1"],
  ["**Mariner.** La moitié de la sauce, 12 h.", "**Griller.** Zone indirecte, 40 min ; badigeonne du reste."], age=None, fetes=["Barbecue d'été"], profil=["epice"], tech=["Griller", "Découper un poulet"])

K("kofta_grillees", "Koftas d'agneau grillées, sauce yaourt", "Köfte", "Moyen-Orient & Caucase › Turquie", "P", 1, 4, 20, 10, "€€", "Brochettes plates, gril.",
  "Agneau haché aux herbes, oignon et épices, moulé sur brochettes, grillé ; yaourt à l'ail et pain plat.",
  ["600 g|d'agneau haché|Agneau haché|3", f"1|oignon râpé pressé|{OIG}|1", f"1 bouquet|de persil|{PERSIL}|2", f"1 c. à c.|de cumin + 1 de paprika|{CUMIN}|1", "1 pincée|de cannelle|Cannelle (bâton / poudre)|0", f"200 g|de yaourt grec + 1 gousse d'ail|{GREC}|2", "4|pains pita|Pain pita / libanais|2"],
  ["**Pétrir.** Viande, oignon, herbes, épices, sel, 2 min (ça lie).", "**Mouler.** Saucisses plates sur brochettes, 30 min au frais.", "**Griller.** 8-10 min."], age=1, fetes=["Barbecue d'été"], profil=["viande_rouge"])

K("imam_bayildi", "Imam bayildi (aubergines farcies fondantes)", "İmam bayıldı", "Moyen-Orient & Caucase › Turquie", "P", 1, 4, 25, 60, "€", "Plat à four.",
  "Aubergines confites dans l'huile d'olive, farcies d'oignons, tomates et ail : « l'imam s'est évanoui » de plaisir.",
  ["4|aubergines moyennes|Aubergine|3", f"3|oignons|{OIG}|2", f"4|tomates|{TOM}|2", f"4 gousses|d'ail|{AIL}|1", f"1 bouquet|de persil|{PERSIL}|1", f"10 cl|d'huile d'olive|{HO}|3", f"1 c. à c.|de sucre|{SUCRE}|0"],
  ["**Aubergines.** Pelées en zébrures, fendues, dorées dans l'huile.", "**Farce.** Oignons fondus, ail, tomates, persil, sucre.", "**Cuire.** Farcies, un verre d'eau, 45 min à 180 °C. Tièdes ou froides."], age=1, profil=["leger"])

K("tahchin", "Gâteau de riz safrané au poulet (tahchin)", "Tahchin", "Moyen-Orient & Caucase › Iran", "P", 2, 6, 30, 90, "€€", "Moule à gâteau ou cocotte.",
  "Riz mêlé de yaourt, safran et jaunes d'œufs, cuit au four en gâteau avec un cœur de poulet : la croûte dorée est spectaculaire.",
  [f"400 g|de riz basmati précuit|{RIZ}|3", f"250 g|de yaourt grec|{GREC}|2", "2|jaunes d'œufs|Jaune d'œuf|1", "1 pincée|de safran infusé|Safran (pistils)|2", f"400 g|de poulet cuit effiloché|{BLANC_P}|2", f"60 g|de beurre|{BEURRE}|2", "30 g|de canneberges (ou épine-vinette)|Canneberges séchées|1"],
  ["**Mélanger.** Riz, yaourt, jaunes, safran, sel.", "**Monter.** Moule beurré, moitié du riz, poulet, reste du riz, tassé.", "**Cuire.** Couvert, 1 h 15 à 190 °C ; démoule, canneberges poêlées au beurre."], age=1, fetes=["Repas de famille"], profil=["gras"])

K("pakoras", "Pakoras d'oignons et légumes", "Pakora", "Asie du Sud › Inde", "E", 1, 4, 20, 10, "€", "Casserole profonde.",
  "Beignets de légumes à la farine de pois chiches et aux épices : croustillants, sans gluten.",
  [f"2|oignons émincés|{OIG}|3", "150 g|d'épinards ou chou-fleur|Épinard|2", "150 g|de farine de pois chiches|Farine de pois chiche (besan)|3", f"1 c. à c.|de cumin + ½ de curcuma|{CUMIN}|1", f"1|piment vert|{PIMENT}|1", f"1 bouquet|de coriandre|{CORI}|1", "75 cl|d'huile|Huile de tournesol / colza|1"],
  ["**Pâte.** Légumes + farine + épices + sel, juste assez d'eau pour lier.", "**Frire.** Cuillerées, 4 min à 175 °C."], age=3, fetes=["Diwali", "Ramadan / Aïd"], profil=["epice"], tech=["Frire"])

K("yaki_udon", "Udon sautés au poulet et légumes (yaki udon)", "Yaki udon", "Asie de l'Est › Japon", "P", 1, 4, 15, 10, "€", "Wok.",
  "Nouilles épaisses sautées avec poulet, chou, carotte et sauce soja-mirin : moelleuses, rapides.",
  ["4 portions|de nouilles udon|Nouilles udon|3", f"300 g|de poulet émincé|{BLANC_P}|2", "¼|chou|Chou blanc / rouge|2", f"1|carotte|{CAROTTE}|1", "100 g|de shiitakés|Shiitake|1", f"3 c. à s.|de sauce soja|{SOJA}|2", "1 c. à s.|de mirin|Mirin|1", f"2 c. à s.|d'huile|{HN}|1"],
  ["**Sauter.** Poulet, légumes 4 min.", "**Nouilles.** Udon détendues à l'eau chaude, sauces, 2 min."],
  var=[("Sans alcool", ["alcohol"], {"Mirin": [("Jus de pomme / raisin / orange (pur jus)", 0.8), ("Vinaigre de riz", 0.1)]}, "Mirin → **jus de pomme + un trait de vinaigre de riz**. **À tester**.")],
  age=1, cats=["enfants"], profil=["leger"], tech=["Sauter au wok"])

K("dumplings_vapeur_legumes", "Raviolis vapeur aux légumes (jiaozi)", "Sùcài jiǎozi", "Asie de l'Est › Chine", "E", 2, 30, 50, 10, "€", "Panier vapeur.",
  "Raviolis farcis de chou, champignons, tofu et ciboulette, cuits à la vapeur : légers et parfumés, pour le Nouvel An.",
  ["30|feuilles à raviolis|Pâte à gyoza / wonton|3", "200 g|de chou chinois|Chou chinois / pak-choï|2", "100 g|de shiitakés|Shiitake|2", "150 g|de tofu ferme|Tofu (ferme / soyeux)|2", "1 bouquet|de ciboulette|Ciboulette|1", f"2 c. à s.|de sauce soja|{SOJA}|1", "1 c. à s.|d'huile de sésame|Huile de sésame (grillée)|1", f"1 morceau|de gingembre|{GING}|1"],
  ["**Farce.** Tout haché fin, chou salé et pressé.", "**Plier.** En demi-lune plissée.", "**Vapeur.** Sur papier, 8 min."], age=3, fetes=["Nouvel An chinois"], profil=["leger"])

K("larb_poulet", "Larb de poulet (salade thaïe au poulet haché)", "Larb gai", "Asie du Sud-Est › Laos", "P", 1, 4, 15, 10, "€", "Poêle.",
  "Poulet haché cuit, citron vert, sauce de poisson, échalotes, herbes et riz grillé moulu : dans des feuilles de salade.",
  ["500 g|de poulet haché|Cuisse / pilon de poulet|3", f"3|citrons verts|{CITV}|3", "2 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|2", f"3|échalotes|{ECH}|1", "1 bouquet|de menthe et coriandre|Menthe|2", "2 c. à s.|de riz gluant grillé moulu|Riz gluant|1", "1|laitue|Salade (laitue, batavia)|1", f"1 pincée|de piment|{CAYENNE}|1"],
  ["**Cuire.** Poulet avec 3 c. à s. d'eau, 5 min, sans dorer.", "**Assaisonner.** Tiède : citron, sauce de poisson, piment, échalotes, herbes, riz grillé.", "**Servir.** Dans les feuilles."], age=3, profil=["acide", "leger"])

K("guacamole_mangue", "Guacamole à la mangue", "Guacamole de mango", "Amérique latine & Caraïbes › Mexique", "E", 1, 6, 10, 0, "€", "Fourchette.",
  "Avocat écrasé, mangue en dés, oignon rouge, coriandre, citron vert : sucré-acidulé, très frais.",
  ["3|avocats|Avocat|3", "1|mangue|Mangue|2", "½|oignon rouge|Oignon rouge|1", f"1 bouquet|de coriandre|{CORI}|1", f"2|citrons verts|{CITV}|2", f"1|piment|{PIMENT}|1"],
  ["**Écraser.** Avocat, citron, sel.", "**Mélanger.** Mangue, oignon, coriandre, piment."], age=1, cats=["enfants"], fetes=["Apéritif dînatoire", "Barbecue d'été"], profil=["leger"])

K("elote", "Elote (maïs grillé à la mexicaine)", "Elote", "Amérique latine & Caraïbes › Mexique", "A", 1, 4, 10, 15, "€", "Gril.",
  "Épis de maïs grillés, nappés de mayonnaise au citron vert, fromage râpé et piment : la street-food des soirs d'été.",
  ["4|épis de maïs|Maïs doux|3", f"4 c. à s.|de mayonnaise|SUB:mayonnaise|2", "60 g|de feta ou cotija|Feta|2", f"1|citron vert|{CITV}|1", f"1 c. à c.|de piment doux|{PAPRIKA}|1"],
  ["**Griller.** 12-15 min, tournés.", "**Napper.** Mayonnaise-citron vert, fromage, piment."], age=3, cats=["enfants"], fetes=["Barbecue d'été"], profil=["gras"])

K("black_bean_soup", "Soupe de haricots noirs cubaine", "Sopa de frijoles negros", "Amérique latine & Caraïbes › Cuba", "So", 1, 6, 15, 40, "€", "Faitout, mixeur.",
  "Haricots noirs, sofrito poivron-oignon-ail, cumin et origan, mixés à moitié : épaisse, avec riz et citron vert.",
  ["600 g|de haricots noirs cuits|Haricots noirs|3", f"1|poivron vert|{POIVRON}|2", f"1|oignon|{OIG}|1", f"4 gousses|d'ail|{AIL}|1", f"1 c. à c.|de cumin + origan|{CUMIN}|1", f"1 L|de bouillon|{BOUILLON}|2", f"1|citron vert|{CITV}|1"],
  ["**Sofrito.** Oignon, poivron, ail, épices 10 min.", "**Cuire.** Haricots, bouillon, 25 min ; mixe la moitié.", "**Servir.** Citron vert, crème, coriandre."], age=1, profil=["leger"])

K("banana_pudding", "Banana pudding", "Banana pudding", "Amérique du Nord › États-Unis › Sud", "D", 1, 8, 25, 240, "€", "Plat, casserole.",
  "Couches de crème vanille, bananes et biscuits qui ramollissent, chantilly : le dessert du Sud des États-Unis.",
  ["1|recette de crème pâtissière|SUB:creme_patissiere|3", "4|bananes|Banane|3", "200 g|de biscuits (sablés, boudoirs)|Biscuits (spéculoos, sablés)|2", f"20 cl|de crème montée|{CL}|2"],
  ["**Monter.** Biscuits, bananes en rondelles, crème ; recommence.", "**Finir.** Chantilly, 4 h au frais."], age=1, cats=["enfants"], profil=["sucre"])

K("lamingtons", "Lamingtons (carrés chocolat-coco)", "Lamington", "Océanie › Australie", "G", 1, 16, 30, 30, "€", "Moule carré.",
  "Carrés de génoise trempés dans un glaçage chocolat et roulés dans la noix de coco : le goûter australien.",
  [f"3|œufs|{OEUF}|2", f"100 g|de sucre|{SUCRE}|2", f"100 g|de farine|{F55}|2", f"40 g|de beurre fondu|{BEURRE}|1", "200 g|de sucre glace + 3 c. à s. de cacao|Sucre glace|2", f"10 cl|de lait chaud|{LAIT}|1", "150 g|de noix de coco râpée|Noix de coco râpée|3"],
  ["**Génoise.** Œufs + sucre au ruban, farine, beurre ; 20 min à 180 °C. Froide, en carrés.", "**Glaçage.** Sucre glace, cacao, lait.", "**Enrober.** Trempés, roulés dans la coco."], age=1, cats=["enfants"], fetes=["Anniversaire"], profil=["sucre"], tech=["Génoise"])

K("salade_quinoa_patate_douce", "Salade de quinoa, patate douce et feta", "Salade de quinoa", "Amérique latine & Caraïbes › Pérou", "E", 1, 4, 15, 30, "€", "Plaque, casserole.",
  "Quinoa, patate douce rôtie, feta, grenade et herbes, vinaigrette citron : complète et colorée.",
  ["200 g|de quinoa|Quinoa|3", "2|patates douces|Patate douce|3", "100 g|de feta|Feta|2", "1|grenade|Grenade|1", "1 bouquet|de menthe et persil|Menthe|1", f"1|citron|{CIT}|1", f"5 c. à s.|d'huile d'olive|{HO}|1", f"1 c. à c.|de cumin|{CUMIN}|1"],
  ["**Rôtir.** Patate douce en cubes, cumin, huile, 25 min à 200 °C.", "**Quinoa.** Rincé, 12 min.", "**Mélanger.** Tout, vinaigrette."], age=1, cats=["enfants"], profil=["leger"])

K("bowl_falafel", "Buddha bowl falafels, houmous et légumes rôtis", "Buddha bowl", "Amérique du Nord › États-Unis", "P", 1, 4, 20, 30, "€", "Plaque.",
  "Le bol végétarien complet : falafels, houmous, boulgour, légumes rôtis, pickles, sauce tahini.",
  ["1|recette de falafels|SUB:falafels|3", "1 bol|de houmous|SUB:houmous|2", "200 g|de boulgour|Boulgour|2", "1|chou-fleur|Chou-fleur|2", "1|patate douce|Patate douce|1", "1|recette de pickles d'oignons rouges|SUB:pickles_oignons_rouges|1", "1|recette de sauce tahini|SUB:sauce_tahini|1"],
  ["**Rôtir.** Légumes, 25 min à 210 °C.", "**Bol.** Boulgour, légumes, falafels, houmous, pickles, sauce."], age=3, cats=["fusion", "enfants"], profil=["leger"])

K("crumble_sale_legumes", "Crumble de légumes au parmesan", "Crumble salé", "France › Cuisine du quotidien", "P", 1, 4, 20, 35, "€", "Plat à gratin.",
  "Légumes fondants sous un crumble croustillant au parmesan et aux noisettes : le crumble version plat.",
  ["2|courgettes|Courgette|2", f"3|tomates|{TOM}|2", "1|aubergine|Aubergine|2", f"100 g|de farine|{F55}|2", f"60 g|de parmesan|{PARM}|2", f"70 g|de beurre froid|{BEURRE}|2", "40 g|de noisettes concassées|Noisette|1"],
  ["**Légumes.** En dés, poêlés 10 min.", "**Crumble.** Farine, parmesan, beurre, noisettes en sable.", "**Cuire.** 25 min à 200 °C."], age=1, cats=["enfants"], profil=["gras"])
