# -*- coding: utf-8 -*-
"""Vague 2 · Sauces : sauces à frites (inspiration : sélection Femme Actuelle des sauces pour frites, noms seulement)
et grandes sauces françaises simplifiées. Toutes sans additifs. Base mayonnaise = recette ATLAS « mayonnaise »."""
from recipes_v2_base import *

SB = "France › Sauces"
MAYO = "SUB:mayonnaise"
OEUF_TIP = ["⚠️ Base de mayonnaise à l'œuf cru : publics fragiles exclus ; version sans œuf cru : yaourt grec + moutarde + huile montés au mixeur."]

def sauce_mayo(id, title, origin, intro, extra, steps, region=SB, tips=(), age=3, kids=None, profil=("gras",), fetes=()):
    K(id, title, origin, region, "S", 1, 6, 10, 15, "€", "Bol, fouet.", intro, [f"20 cl|de mayonnaise maison (recette liée)|{MAYO}|3"] + extra, steps,
      tips=list(OEUF_TIP) + list(tips), keep="2 jours au frigo.", age=age, kids=kids or "✓ dès 3 ans avec la version sans œuf cru.", cats=["sauces"], profil=list(profil), fetes=list(fetes), tech=["Émulsionner"])

sauce_mayo("sauce_tartare", "Sauce tartare", "Sauce tartare",
  "Mayonnaise aux cornichons, câpres, échalote et herbes : pour poisson pané, fish and chips, frites.",
  ["4|cornichons|Cornichon|2", "1 c. à s.|de câpres|Câpres|2", f"1|échalote|{ECH}|1", "1 c. à s.|de ciboulette et d'estragon|Ciboulette|1", f"1 c. à c.|de moutarde|{DIJON}|1"],
  ["**Hacher.** Cornichons, câpres, échalote, herbes très finement.", "**Mélanger.** À la mayonnaise avec la moutarde ; 15 min au frais."])
sauce_mayo("mayo_curry", "Mayonnaise au curry", "Sauce curry",
  "Douce, dorée, légèrement épicée : la sauce des frites à la belge et des sandwichs au poulet.",
  [f"1 c. à s.|de curry doux maison|{CUR}|2", f"1 c. à c.|de miel|{MIEL}|1", f"1 c. à c.|de jus de citron|{CIT}|0"],
  ["**Torréfier.** Le curry 30 s à sec (il perd son goût de poudre crue).", "**Mélanger.** À la mayonnaise avec miel et citron."], profil=("gras", "epice"))
sauce_mayo("mayo_herbes", "Mayonnaise aux herbes fraîches", "Sauce verte",
  "Persil, ciboulette, estragon et cerfeuil hachés : verte, fraîche, pour poissons froids et pommes de terre.",
  [f"1 bouquet|de persil|{PERSIL}|2", "½ bouquet|de ciboulette|Ciboulette|1", "4 branches|d'estragon|Estragon|1", "4 branches|de cerfeuil|Cerfeuil|1", f"½|citron|{CIT}|1"],
  ["**Herbes.** Blanchies 10 s, refroidies dans l'eau glacée, pressées, mixées : sauce bien verte.", "**Mélanger.** À la mayonnaise, citron."], profil=("gras", "leger"))
sauce_mayo("mayo_safran", "Mayonnaise au safran (rouille express)", "Rouille",
  "Safran, ail, piment et pomme de terre écrasée : la sauce de la soupe de poissons, sur des croûtons.",
  ["1 pincée|de safran infusé dans 1 c. à s. d'eau chaude|Safran (pistils)|2", f"2 gousses|d'ail|{AIL}|2", f"1|petite pomme de terre cuite|{PDT}|1", f"1 pincée|de piment d'Espelette|Piment d'Espelette|1"],
  ["**Piler.** Ail, pomme de terre, safran, piment.", "**Mélanger.** À la mayonnaise."], region="France › Provence-Alpes-Côte d'Azur › Marseille", profil=("gras", "epice"))
sauce_mayo("sauce_cocktail", "Sauce cocktail (sans alcool)", "Sauce cocktail",
  "Mayonnaise, ketchup maison et une pointe de Worcestershire : pour avocat-crevettes et frites. La version d'origine contient un trait de cognac ; un peu de jus d'orange le remplace.",
  ["2 c. à s.|de ketchup maison|SUB:ketchup|2", "1 c. à c.|de sauce Worcestershire|Sauce Worcestershire|1", "1 c. à s.|de jus d'orange|Orange|1", "1 pincée|de paprika|Paprika doux|0", "1 trait|de Tabasco|Tabasco / sauce piquante|0?"],
  ["**Mélanger.** Tout, au frais 15 min."], profil=("gras", "sucre"))
sauce_mayo("dijonnaise", "Sauce dijonnaise", "Dijonnaise",
  "Mayonnaise bien relevée à la moutarde de Dijon et à l'ancienne : pour viandes froides, frites, sandwichs.",
  [f"1 c. à s.|de moutarde de Dijon|{DIJON}|2", "1 c. à s.|de moutarde à l'ancienne|Moutarde à l'ancienne|2", f"1 c. à c.|de miel|{MIEL}|0"],
  ["**Mélanger.** Tout."], region="France › Bourgogne-Franche-Comté › Dijon", profil=("gras", "epice"))
sauce_mayo("sauce_americaine_belge", "Sauce américaine (à la belge)", "Sauce américaine belge",
  "La sauce des friteries belges : mayonnaise, tomate, échalote, câpres, un peu de cerfeuil (rien à voir avec le homard).",
  [f"1 c. à s.|de concentré de tomate|{CONC}|2", f"1|échalote|{ECH}|1", "1 c. à c.|de câpres|Câpres|1", "1 c. à s.|de cerfeuil|Cerfeuil|1", f"1 pincée|de paprika|{PAPRIKA}|0"],
  ["**Mélanger.** Tout, échalote et câpres très finement hachées."], region="Europe du Nord & Centrale › Belgique")
sauce_mayo("sauce_brazil", "Sauce brazil (ananas-curry)", "Sauce brazil",
  "La sauce sucrée-épicée des friteries belges : mayonnaise, ananas, curry, ketchup.",
  ["80 g|d'ananas en tout petits dés|Ananas|3", f"1 c. à c.|de curry|{CUR}|1", "1 c. à s.|de ketchup maison|SUB:ketchup|1"],
  ["**Mélanger.** Tout ; 30 min au frais."], region="Europe du Nord & Centrale › Belgique", profil=("gras", "sucre"))

K("sauce_bearnaise", "Sauce béarnaise", "Béarnaise", "France › Nouvelle-Aquitaine › Béarn", "S", 2, 4, 25, 0, "€€", "Casserole, bol, fouet, bain-marie.",
  "Jaunes d'œufs montés au beurre et à la réduction d'estragon-échalote : la sauce de la côte de bœuf et des frites.",
  [f"3|jaunes d'œufs|Jaune d'œuf|3", f"150 g|de beurre clarifié tiède|{BEURRE}|3", f"2|échalotes|{ECH}|2", "1 bouquet|d'estragon|Estragon|3", "5 cl|de vinaigre de vin blanc|Vinaigre de vin rouge / blanc|2", f"1 c. à c.|de poivre concassé|{POIVRE}|1", "1 c. à s.|de cerfeuil|Cerfeuil|0"],
  ["**Réduction.** Échalotes hachées, la moitié de l'estragon, vinaigre, 5 cl d'eau, poivre : réduis aux ¾ ; refroidis, filtre.", "**Sabayon.** Jaunes + réduction + 1 c. à s. d'eau, au bain-marie, fouettés jusqu'à mousseux et épais (60-65 °C, pas plus).",
   "**Monter.** Hors du feu, le beurre tiède en filet en fouettant.", "**Finir.** Estragon et cerfeuil hachés, sel. Garde au tiède (pas au chaud)."],
  tips=["Sauce qui tranche : un glaçon et fouette fort, ou repars d'un jaune neuf et ajoute la sauce tranchée petit à petit."], keep="À servir tout de suite.", age=3, cats=["sauces"], profil=["gras", "acide"], tech=["Émulsionner"])

K("sauce_hollandaise", "Sauce hollandaise (et mousseline)", "Hollandaise", SB, "S", 2, 4, 15, 0, "€€", "Bol, bain-marie, fouet.",
  "Jaunes et beurre montés au citron : pour asperges, poissons, œufs Bénédicte. Avec de la crème fouettée, elle devient mousseline.",
  [f"3|jaunes d'œufs|Jaune d'œuf|3", f"150 g|de beurre clarifié tiède|{BEURRE}|3", f"½|citron|{CIT}|2", f"1 pincée|de sel et de cayenne|{SEL}|0"],
  ["**Sabayon.** Jaunes + 2 c. à s. d'eau au bain-marie, fouettés jusqu'à épais.", "**Monter.** Beurre en filet hors du feu.", "**Assaisonner.** Citron, sel, cayenne."],
  keep="À servir tout de suite.", age=3, cats=["sauces"], profil=["gras"], tech=["Émulsionner"])

K("sauce_roquefort", "Sauce au roquefort", "Sauce au roquefort", "France › Occitanie › Aveyron", "S", 1, 4, 10, 5, "€€", "Casserole.",
  "Crème et roquefort fondus, poivre : pour steak, pommes de terre au four, frites.",
  ["100 g|de roquefort|Roquefort / bleu|3", f"20 cl|de crème|{CF}|3", f"1 pincée|de poivre|{POIVRE}|0", f"1|échalote (facultatif)|{ECH}|1?"],
  ["**Fondre.** Échalote fondue, crème, roquefort émietté, à feu doux jusqu'à nappant. Poivre ; pas de sel."],
  keep="2 jours au frigo.", age=3, cats=["sauces"], profil=["gras"], tips=["Lait cru : déconseillé femmes enceintes (bleu au lait pasteurisé possible)."])

K("sauce_poivre", "Sauce au poivre", "Sauce au poivre", SB, "S", 1, 4, 10, 10, "€€", "Poêle (celle de la viande).",
  "Poivre concassé, déglaçage et crème : la sauce du steak-frites de bistrot. Le cognac traditionnel est remplacé, au choix.",
  [f"2 c. à s.|de poivre noir concassé (ou vert en saumure)|{POIVRE}|3", f"20 cl|de crème|{CF}|3", f"10 cl|de bouillon de bœuf|{BOUILLON}|2", "3 cl|de cognac (facultatif)|Cognac / armagnac / brandy|1?", f"1|échalote|{ECH}|1"],
  ["**Sucs.** Dans la poêle de la viande, échalote et poivre 1 min.", "**Déglacer.** Cognac (flambé) ou bouillon, réduis.", "**Crème.** Réduis jusqu'à nappant, jus de repos de la viande."],
  var=[("Sans alcool", ["alcohol"], {"Cognac / armagnac / brandy": [("Bouillon d'os maison (bœuf/volaille)", 0.7), ("Vinaigre balsamique", 0.1)]}, "Cognac → **bouillon + ½ c. à c. de vinaigre balsamique** : profondeur et légère acidité. **À tester**.")],
  keep="2 jours au frigo.", age=3, cats=["sauces"], profil=["gras", "epice"], tech=["Déglacer"])

K("sauce_cheddar", "Sauce cheddar (pour frites et nachos)", "Cheese sauce", "Amérique du Nord › États-Unis", "S", 1, 6, 10, 5, "€", "Casserole, fouet.",
  "Une vraie sauce fromage lisse et coulante, sans fondu industriel : lait, un peu de maïzena et du cheddar.",
  ["200 g|de cheddar affiné râpé|Cheddar|3", f"25 cl|de lait|{LAIT}|2", f"1 c. à s.|de maïzena|Fécule de maïs (maïzena)|1", f"1 c. à c.|de moutarde|{DIJON}|1", f"1 pincée|de paprika|{PAPRIKA}|0"],
  ["**Lier.** Lait + maïzena à frémissement, épaissi.", "**Fondre.** Hors du feu, le cheddar par poignées, moutarde, paprika : lisse."],
  keep="2 jours au frigo (réchauffe avec un peu de lait).", age=1, cats=["sauces", "enfants"], profil=["gras"])

K("sauce_aigre_douce", "Sauce aigre-douce", "Sauce aigre-douce", "Asie de l'Est › Chine › Canton", "S", 1, 6, 10, 10, "€", "Casserole.",
  "Ananas, vinaigre, sucre, ketchup et soja : brillante, pour poulet ou crevettes panés, nems et frites.",
  ["20 cl|de jus d'ananas|Ananas|3", "5 cl|de vinaigre de riz ou de cidre|Vinaigre de riz|2", f"3 c. à s.|de sucre|{SUCRE}|2", "2 c. à s.|de ketchup maison|SUB:ketchup|2", f"1 c. à s.|de sauce soja|{SOJA}|1", f"1 c. à s.|de maïzena|Fécule de maïs (maïzena)|1"],
  ["**Chauffer.** Tout sauf la maïzena.", "**Lier.** Maïzena délayée, 1 min d'ébullition."],
  keep="1 semaine au frigo.", age=1, cats=["sauces", "enfants"], profil=["sucre", "acide"])

K("sauce_yaourt_herbes", "Sauce yaourt-herbes-citron", "Sauce au yaourt", SB, "S", 1, 6, 10, 0, "€", "Bol.",
  "La sauce légère des frites au four, des falafels et des légumes rôtis : yaourt, herbes, citron, ail.",
  [f"250 g|de yaourt grec|{GREC}|3", "1 bouquet|de ciboulette et d'aneth|Ciboulette|2", f"½|citron|{CIT}|1", f"1 gousse|d'ail|{AIL}|1", f"1 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Mélanger.** Tout, sel, poivre."], keep="3 jours au frigo.", age=1, cats=["sauces", "enfants"], profil=["leger", "acide"])

K("ketchup_betterave", "Ketchup de betterave", "Ketchup de betterave", SB, "S", 1, 10, 10, 30, "€", "Casserole, mixeur.",
  "Un ketchup rubis, moins sucré, aux épices douces : surprenant avec des frites de patate douce.",
  ["400 g|de betteraves cuites|Betterave (crue/cuite)|3", "1|pomme|Pomme|2", f"1|oignon rouge|Oignon rouge|1", "8 cl|de vinaigre de cidre|Vinaigre de cidre|2", "60 g|de cassonade|Sucre blanc / roux / cassonade / vergeoise|2", f"½ c. à c.|de cannelle, girofle, gingembre|{CANN}|1", f"1 c. à c.|de sel|{SEL}|0"],
  ["**Cuire.** Tout en morceaux, 25 min.", "**Mixer.** Très lisse ; réduis encore si trop liquide."],
  keep="1 mois au frigo.", age=1, cats=["sauces", "enfants"], profil=["sucre", "acide"])

K("sauce_gribiche", "Sauce gribiche", "Gribiche", SB, "S", 1, 6, 15, 10, "€", "Bol, casserole.",
  "Une mayonnaise aux jaunes d'œufs durs, cornichons, câpres et herbes : sans œuf cru, pour tête de veau, poissons froids, poireaux.",
  [f"3|œufs durs|{OEUF}|3", f"1 c. à s.|de moutarde|{DIJON}|1", f"15 cl|d'huile|{HN}|2", "4|cornichons|Cornichon|1", "1 c. à s.|de câpres|Câpres|1", f"1 bouquet|de persil, cerfeuil, estragon|{PERSIL}|1", "1 c. à s.|de vinaigre|Vinaigre de vin rouge / blanc|1"],
  ["**Base.** Jaunes durs écrasés avec moutarde et vinaigre ; huile en filet en fouettant.", "**Garniture.** Blancs hachés, cornichons, câpres, herbes."],
  keep="2 jours au frigo.", age=1, cats=["sauces"], profil=["gras", "acide"], tech=["Émulsionner"])

K("sauce_vierge", "Sauce vierge", "Sauce vierge", "France › Provence-Alpes-Côte d'Azur", "S", 1, 4, 10, 30, "€", "Bol.",
  "Tomates en petits dés, huile d'olive, basilic, citron, tiédis : pour poissons et légumes grillés.",
  [f"3|tomates|{TOM}|3", f"8 c. à s.|d'huile d'olive|{HO}|3", "1 bouquet|de basilic|Basilic|2", f"1|échalote|{ECH}|1", f"½|citron|{CIT}|1", "1 c. à s.|de câpres ou d'olives|Olives (vertes / noires)|1?"],
  ["**Couper.** Tomates épépinées en dés, échalote, basilic.", "**Infuser.** Avec l'huile et le citron, 30 min ; tiédis juste avant de servir."],
  keep="1 jour au frigo.", age=1, cats=["sauces", "enfants"], profil=["leger"])

K("salsa_verde", "Salsa verde italienne", "Salsa verde", "Europe du Sud › Italie › Piémont", "S", 1, 6, 10, 0, "€", "Couteau.",
  "Persil, câpres, anchois, ail, moutarde, vinaigre et huile : pour viandes bouillies, poissons, pommes de terre.",
  [f"1 bouquet|de persil|{PERSIL}|3", "1 c. à s.|de câpres|Câpres|2", "2|filets d'anchois|Anchois (filets, conserve)|1", f"1 gousse|d'ail|{AIL}|1", "30 g|de mie de pain trempée au vinaigre|Pain rassis (réservé)|1", f"1 c. à c.|de moutarde|{DIJON}|1", f"10 cl|d'huile d'olive|{HO}|2"],
  ["**Hacher.** Tout au couteau, finement.", "**Lier.** Avec la moutarde et l'huile."], keep="3 jours au frigo.", age=3, cats=["sauces", "zero_dechet"], profil=["acide"])

K("romesco", "Sauce romesco", "Salsa romesco", "Europe du Sud › Espagne › Catalogne", "S", 1, 8, 15, 30, "€", "Four, mixeur.",
  "Poivrons et tomates grillés, amandes, ail et pimentón : pour légumes grillés, poissons et calçots.",
  [f"2|poivrons rouges|{POIVRON}|3", f"2|tomates|{TOM}|2", f"1 tête|d'ail|{AIL}|1", "60 g|d'amandes grillées|Amande (entière, effilée, poudre)|2", "1 tranche|de pain grillé|Pain rassis (réservé)|1", f"1 c. à c.|de paprika fumé|{PFUME}|1", "2 c. à s.|de vinaigre de xérès|Vinaigre de xérès|1", f"8 c. à s.|d'huile d'olive|{HO}|2"],
  ["**Griller.** Poivrons, tomates, ail 30 min à 220 °C ; pèle.", "**Mixer.** Avec amandes, pain, paprika, vinaigre, huile : texture un peu granuleuse."],
  keep="5 jours au frigo.", age=3, cats=["sauces"], fetes=["Barbecue d'été"], profil=["epice"])

K("raita", "Raïta concombre-menthe", "Raita", "Asie du Sud › Inde", "S", 1, 6, 10, 0, "€", "Bol, râpe.",
  "Yaourt, concombre, menthe et cumin grillé : la sauce fraîche qui calme les plats épicés.",
  [f"400 g|de yaourt|{YAO}|3", "½|concombre|Concombre|2", "10|feuilles de menthe|Menthe|2", f"½ c. à c.|de cumin grillé|{CUMIN}|1", f"1 pincée|de sel|{SEL}|0"],
  ["**Mélanger.** Concombre râpé et pressé, menthe ciselée, cumin, sel."], keep="2 jours au frigo.", age=1, cats=["sauces", "enfants"], profil=["leger"])

K("pico_de_gallo", "Pico de gallo", "Pico de gallo", "Amérique latine & Caraïbes › Mexique", "S", 1, 6, 15, 15, "€", "Couteau.",
  "Tomate, oignon, coriandre, piment et citron vert, en petits dés : la salsa fraîche des tacos.",
  [f"4|tomates|{TOM}|3", "½|oignon blanc ou rouge|Oignon rouge|2", f"1 bouquet|de coriandre|{CORI}|2", f"1|piment jalapeño ou vert|{PIMENT}|1", f"1|citron vert|{CITV}|2", f"½ c. à c.|de sel|{SEL}|0"],
  ["**Couper.** Tout en petits dés réguliers.", "**Repos.** 15 min avec sel et citron vert."], keep="1 jour au frigo.", age=1, cats=["sauces", "enfants"], profil=["leger", "acide"], kids="✓ dès 1 an sans piment.")

K("sauce_champignons", "Sauce crème aux champignons", "Sauce forestière", SB, "S", 1, 4, 10, 15, "€", "Poêle.",
  "Champignons dorés, échalote, crème et persil : pour volailles, escalopes, pâtes, steaks.",
  ["300 g|de champignons|Champignon de Paris|3", f"1|échalote|{ECH}|1", f"20 cl|de crème|{CF}|2", f"10 cl|de bouillon|{BOUILLON}|1", f"20 g|de beurre|{BEURRE}|1", f"1 c. à s.|de persil|{PERSIL}|0"],
  ["**Dorer.** Champignons à feu vif au beurre (sans les serrer), échalote.", "**Napper.** Bouillon, crème, réduis jusqu'à nappant. Persil."],
  keep="2 jours au frigo.", age=1, cats=["sauces", "enfants"], profil=["gras"])

K("sauce_moutarde_miel", "Sauce moutarde-miel", "Honey mustard", "Amérique du Nord › États-Unis", "S", 1, 6, 5, 0, "€", "Bol.",
  "Moutarde, miel et yaourt (ou mayonnaise) : pour nuggets, salades, frites de patate douce.",
  [f"3 c. à s.|de moutarde de Dijon|{DIJON}|3", f"2 c. à s.|de miel|{MIEL}|3", f"4 c. à s.|de yaourt grec|{GREC}|2", f"1 c. à c.|de jus de citron|{CIT}|0"],
  ["**Mélanger.** Tout."], keep="1 semaine au frigo.", age=1, cats=["sauces", "enfants"], profil=["sucre"], kids="✓ dès 1 an (miel interdit avant 1 an).")

K("mojo_canario", "Mojo rojo et mojo verde", "Mojo", "Europe du Sud › Espagne › Canaries", "S", 1, 8, 10, 0, "€", "Mortier ou mixeur.",
  "Les deux sauces des Canaries pour pommes de terre ridées : rouge au paprika et piment, verte à la coriandre.",
  [f"6 gousses|d'ail|{AIL}|2", f"2 c. à c.|de paprika fumé (rouge)|{PFUME}|2", f"1 bouquet|de coriandre (verte)|{CORI}|2", f"1 c. à c.|de cumin|{CUMIN}|1", "4 c. à s.|de vinaigre|Vinaigre de vin rouge / blanc|2", f"15 cl|d'huile d'olive|{HO}|2", f"1 c. à c.|de gros sel|{SEL}|0"],
  ["**Rouge.** Pile 3 gousses d'ail, sel, cumin, paprika, piment ; vinaigre et huile.", "**Verte.** Pile 3 gousses d'ail, sel, coriandre ; vinaigre et huile."],
  keep="1 semaine au frigo.", age=3, cats=["sauces"], profil=["acide", "epice"])
