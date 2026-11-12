# -*- coding: utf-8 -*-
"""Audit « fin gourmet, cuisine française » (12/11/2026, bible/AUDIT_FIN_GOURMET_FRANCE_2026-11-12.md) : les classiques
de bistrot, de terroir, d'abats et de gibier qui manquaient. Recettes de référence réécrites avec les repères ATLAS
(temps, signes de cuisson, températures à cœur). Le porc et l'alcool restent dans la recette d'origine avec leur version
adaptée quand elle existe. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

VR = ("Sans alcool", ["alcohol"], {"Vin rouge": [("Bouillon d'os maison (bœuf/volaille)", 0.5), ("Jus de raisin / pomme (pur jus)", 0.4), ("Vinaigre de vin rouge / blanc", 0.05)]},
      "Vin rouge → **bouillon + jus de raisin + un trait de vinaigre** : la sauce garde sa profondeur et son acidité. **À tester**.")
VB = ("Sans alcool", ["alcohol"], {"Vin blanc": [("Bouillon d'os maison (bœuf/volaille)", 0.8), ("Vinaigre de cidre", 0.05)]}, "Vin blanc → **bouillon + 1 c. à c. de vinaigre de cidre**. **À tester**.")
COGNAC_SA = ("Sans alcool", ["alcohol"], {"Cognac / armagnac / brandy": [("Bouillon d'os maison (bœuf/volaille)", 1.0)]}, "Cognac → **un peu de fond de veau** pour déglacer ; pas de flambage. **À tester**.")
FOND = "Fond de veau / de volaille (poudre)"; ECHA = "Échalote"; CF_ = "Crème fraîche"; FL = "Crème fleurette (liquide)"

# ---------------- Bistrot ----------------
K("steak_au_poivre", "Steak au poivre, sauce au cognac", "Steak au poivre", "France › Cuisine de bistrot", "P", 2, 2, 10, 15, "€€€", "Poêle en fonte ou à fond épais, mortier.",
  "Le monument des brasseries : un pavé épais enrobé de poivre concassé, saisi, flambé au cognac, et une sauce montée à la crème dans les sucs. Le poivre doit être concassé gros, jamais moulu fin.",
  ["2|pavés de rumsteck ou filet (200 g, 3 cm)|Rumsteck|3", f"2 c. à s.|de poivre noir en grains|{POIVRE}|2", "4 cl|de cognac|Cognac / armagnac / brandy|2", f"15 cl|de crème fraîche épaisse|{CF_}|2", f"10 cl|de fond de veau|{FOND}|1", f"20 g|de beurre|{BEURRE}|1", f"1 c. à s.|d'huile|{HN}|1"],
  ["**Poivre.** Grains concassés au mortier (ou au fond d'une casserole) : gros éclats ; viande sortie 30 min avant, pressée dans le poivre sur les deux faces, salée au dernier moment.",
   "**Saisir.** Huile fumante, 2 min 30 par face sans toucher, beurre en fin pour arroser : croûte brune, saignant (52 °C) ou à point (57 °C) ; réserve sous aluminium.",
   "**Flamber.** Hors du feu, cognac dans la poêle ; flamme allumée à la longue allumette, hotte coupée, cheveux attachés : elle s'éteint seule.",
   "**Sauce.** Fond, sucs grattés, 1 min ; crème, 2 min : nappante ; jus de repos ajouté ; viande nappée, frites ou pommes sautées."],
  tips=["Ne sale qu'au dernier moment : le sel tire le jus avant la saisie.", "Flamber : jamais au-dessus de la flamme du gaz, toujours hors du feu, enfants loin."],
  var=[COGNAC_SA], keep="Le jour même.", age=None, kids="✓ dès 6 ans en version sans alcool, poivre retiré de leur part.", fetes=["Saint-Valentin"], profil=["viande_rouge", "gras", "epice"], tech=["Saisir", "Déglacer"])
K("canard_orange", "Canard à l'orange (sauce bigarade)", "Canard à l'orange", "France › Cuisine de bistrot", "P", 3, 4, 40, 90, "€€€", "Plat à rôtir, casserole, zesteur.",
  "Le grand classique de la cuisine bourgeoise : un canard rôti rosé, une sauce aigre-douce à base d'un caramel déglacé au vinaigre (gastrique), de jus d'orange et de fond, relevée de zestes blanchis.",
  ["1|canard (2 kg) ou 2 magrets + 2 cuisses|Canard : magret, cuisse|3", "4|oranges (dont 2 non traitées)|Orange|3", f"40 g|de sucre|{SUCRE}|1", f"4 c. à s.|de vinaigre de vin|Vinaigre de vin rouge / blanc|1", f"30 cl|de fond de volaille ou de veau|{FOND}|2", "3 cl|de Grand Marnier (facultatif)|Grand Marnier / Cointreau / triple sec|1?", f"30 g|de beurre froid|{BEURRE}|1", f"1 c. à c.|de fécule|Fécule de maïs (maïzena)|1"],
  ["**Rôtir.** Canard salé, peau piquée sans toucher la chair, four 200 °C 20 min puis 180 °C 50 min en arrosant : cuisses à 80 °C, filets rosés ; repos 15 min sous aluminium.",
   "**Zestes.** De 2 oranges en fine julienne, blanchis 2 min trois fois (l'amertume part) ; jus des 4 oranges.",
   "**Gastrique.** Sucre et 2 c. à s. d'eau en caramel blond, vinaigre (attention aux projections), jus d'orange, fond : 10 min, réduit de moitié ; fécule délayée, liqueur, 1 min.",
   "**Monter.** Hors du feu, beurre froid en morceaux en tournant : sauce brillante ; zestes, quartiers d'orange pelés à vif ; canard découpé, nappé."],
  tips=["Garde la graisse du canard : elle fait les meilleures pommes sautées."], keep="2 jours au frigo (sauce à part).", age=3, cats=[], fetes=["Noël", "Repas de famille"], profil=["gras", "sucre", "acide"], tech=["Rôtir", "Monter au beurre"],
  var=[("Sans alcool", ["alcohol"], {"Grand Marnier / Cointreau / triple sec": [("Jus de pomme / raisin / orange (pur jus)", 1.0)]}, "Grand Marnier → **zeste et jus d'orange en plus**. **À tester**.")])
K("tete_de_veau_gribiche", "Tête de veau, sauce gribiche", "Tête de veau", "France › Cuisine de bistrot", "P", 2, 6, 30, 180, "€€", "Grande marmite.",
  "Le plat des amateurs d'abats : une tête de veau roulée (achetée prête chez le tripier), cuite longuement dans un bouillon aromatique, servie tiède avec la langue, des pommes vapeur et une sauce gribiche aux câpres et cornichons.",
  ["1,5 kg|de tête de veau roulée et ficelée (avec la langue)|-|3", f"2|carottes|{CAROTTE}|1", f"2|oignons piqués de clous de girofle|{OIG}|1", "1|bouquet garni|Laurier|1", f"2 c. à s.|de farine|{F55}|1", f"1|citron|{CIT}|1", f"1 kg|de pommes de terre|{PDT}|2", "1|bol de sauce gribiche (fiche Gribiche)|SUB:sauce_gribiche|2"],
  ["**Blanchir.** Tête et langue à l'eau froide, à ébullition 5 min, égouttées, rincées : les impuretés partent.",
   "**Blanc de cuisson.** Eau froide, farine délayée, jus de citron (la chair reste blanche), carottes, oignons, bouquet, gros sel ; à frémissement, 2 h 30 à 3 h : une lame entre sans aucune résistance.",
   "**Langue.** Pelée tiède, en tranches.",
   "**Servir.** Tête en tranches épaisses, langue, pommes vapeur, un peu de bouillon chaud dessus, gribiche à part."],
  tips=["Commande la tête de veau roulée chez le boucher ou le tripier, quelques jours avant."], keep="3 jours au frigo dans son bouillon.", age=6, cats=[], fetes=["Repas de famille"], profil=["gras", "acide"], tech=["Pocher"], side="pommes_vapeur")
K("pate_en_croute", "Pâté en croûte maison (volaille et veau, ou porc)", "Pâté en croûte", "France › Cuisine de bistrot", "E", 3, 10, 90, 1500, "€€€", "Moule à pâté à charnière (ou à cake), hachoir, thermomètre.",
  "Le chef-d'œuvre de charcuterie : une pâte brisée foncée dans un moule, une farce de viandes marinées et une pièce de volaille au centre, cuite à cœur à 68 °C, puis coulée de gelée. Ici une version volaille-veau ; la recette traditionnelle mêle le porc.",
  [f"500 g|de pâte brisée (ou fiche Pâte brisée)|SUB:pate_brisee|3", "500 g|d'épaule de veau|Épaule / tendron de veau|3", "400 g|de poitrine de porc (ou cuisse de volaille désossée)|Poitrine de porc (fraîche)|3", "2|blancs de volaille|Blanc de poulet|2", "100 g|de foies de volaille|Foies / gésiers de volaille|1", f"2|échalotes|{ECHA}|1", "1 c. à c.|de quatre-épices|Quatre-épices|1", "4 cl|de cognac (facultatif)|Cognac / armagnac / brandy|1?", f"1|jaune d'œuf (dorure)|{OEUF}|1", "25 cl|de bouillon + 3 feuilles de gélatine|Gélatine alimentaire|1", "60 g|de pistaches|Pistache|1?"],
  ["**Mariner (la veille).** Viandes en dés, foies, échalotes, épices, cognac, 16 g de sel par kilo de viande ; blancs à part, salés ; une nuit au frais.",
   "**Farce.** Hachoir grille moyenne (ou robot par impulsions), pistaches : farce qui se tient ; 1 cuillère cuite à la poêle pour goûter le sel.",
   "**Monter.** Moule chemisé de pâte, farce, blancs au centre, farce ; couvercle de pâte soudé, 2 cheminées en papier, dorure ; four 200 °C 15 min puis 170 °C 1 h à 1 h 15 : 68 °C à cœur.",
   "**Gelée.** Tiède, bouillon chaud gélifié coulé par les cheminées ; 24 h au frigo avant de trancher épais."],
  tips=["Le thermomètre est indispensable : 68 °C à cœur, ni plus (sec) ni moins (sécurité).", "Tranche avec un couteau-scie, la croûte reste nette."],
  var=[("Sans porc", ["pork"], {"Poitrine de porc (fraîche)": [("Cuisse / pilon de poulet", 1.0)]}, "Poitrine de porc → **cuisses de volaille désossées avec la peau** : le gras de la peau garde la farce moelleuse. **À tester**."),
       ("Sans alcool", ["alcohol"], {"Cognac / armagnac / brandy": [("Bouillon d'os maison (bœuf/volaille)", 1.0)]}, "Cognac → **une cuillère de bouillon**. **À tester**.")],
  keep="5 jours au frigo, filmé.", age=3, cats=[], fetes=["Noël", "Apéritif dînatoire", "Repas de famille"], profil=["gras"], tech=["Foncer"])
K("foie_gras_mi_cuit", "Foie gras de canard mi-cuit en terrine", "Foie gras mi-cuit", "France › Nouvelle-Aquitaine", "E", 3, 8, 40, 2880, "€€€", "Petite terrine, thermomètre, plat à bain-marie.",
  "Le foie gras des fêtes fait à la maison : un lobe déveiné, assaisonné de sel et de poivre, cuit très doucement au bain-marie jusqu'à 50 °C à cœur, pressé et mûri deux jours. Fondant, rosé, sans goût de gras.",
  ["1|lobe de foie gras de canard cru extra (500 g)|-|3", "7 g|de sel fin|Sel fin / gros sel / fleur de sel|2", f"2 g|de poivre blanc|{POIVRE}|1", "1 g|de sucre|Sucre blanc / roux / cassonade / vergeoise|1", "2 cl|d'armagnac ou de porto (facultatif)|Porto|1?"],
  ["**Déveiner.** Foie 1 h à température ambiante (souple) ; lobes ouverts, veines tirées délicatement avec la pointe d'un couteau, sans hacher le foie.",
   "**Assaisonner.** Sel, poivre, sucre, alcool ; tassé dans la terrine en chassant l'air, filmé, 12 h au frigo.",
   "**Cuire.** Bain-marie à 70 °C (eau frémissante dans le four à 90 °C), 35 à 45 min : 50 °C à cœur au thermomètre ; la graisse jaune perle.",
   "**Presser et mûrir.** Planchette et poids léger 12 h ; graisse récupérée versée dessus ; 2 jours au frigo avant de servir, en tranches au couteau trempé dans l'eau chaude."],
  tips=["Femme enceinte : foie gras mi-cuit déconseillé (cuisson basse).", "Sers avec un pain de campagne grillé et une pincée de fleur de sel."],
  var=[("Sans alcool", ["alcohol"], {"Porto": [("Jus de raisin / pomme (pur jus)", 0.5)]}, "Porto → **rien, ou une cuillère de jus de raisin**. **À tester**.")],
  keep="1 semaine au frigo sous sa graisse.", age=None, kids="Pour les adultes et les grands enfants (foie gras peu cuit).", fetes=["Noël", "Nouvel An"], profil=["gras"], tech=["Bain-marie"])
K("waterzoi_poulet", "Waterzoï de poulet (gantois)", "Waterzooi", "France › Hauts-de-France", "P", 2, 6, 30, 50, "€€", "Grande cocotte.",
  "La soupe-repas flamande : du poulet poché avec des légumes en julienne (poireau, carotte, céleri), un bouillon lié à la crème et au jaune d'œuf. Doux, velouté, servi en assiette creuse avec des pommes vapeur.",
  ["1|poulet fermier en 8 morceaux|Poulet entier|3", "2|poireaux (blanc)|Poireau|2", f"3|carottes|{CAROTTE}|2", "1/4|de céleri-rave|Céleri-rave|1", f"20 cl|de crème fleurette|{FL}|2", f"2|jaunes d'œufs|Jaune d'œuf|1", f"1 L|de bouillon de volaille|{BOUILLON}|2", f"30 g|de beurre|{BEURRE}|1", f"1/2|botte de persil|{PERSIL}|1", f"1|citron|{CIT}|1"],
  ["**Légumes.** En fine julienne ; beurre, 8 min à couvert à feu doux : ils suent sans colorer.",
   "**Pocher.** Poulet sur les légumes, bouillon à hauteur, sel ; frémissement 35 min : cuisses à 80 °C ; morceaux réservés au chaud.",
   "**Lier.** Crème et jaunes battus, une louche de bouillon chaud dedans, puis dans la cocotte hors du feu, en remuant ; à feu très doux 2 min sans bouillir : nappant.",
   "**Servir.** Poulet en assiette creuse, bouillon et légumes, persil, un trait de citron ; pommes vapeur."],
  tips=["La liaison aux jaunes ne doit jamais bouillir : elle tournerait en œufs brouillés."], keep="2 jours au frigo (réchauffé doucement).", age=1, cats=["enfants"], fetes=["Repas de famille"], profil=["leger", "gras"], tech=["Pocher", "Lier une sauce"], side="pommes_vapeur")
K("andouillette_moutarde", "Andouillette à la moutarde, pommes sautées", "Andouillette", "France › Cuisine de bistrot", "P", 1, 2, 10, 25, "€€", "Poêle, plat allant au four.",
  "Le plat des bouchons lyonnais et de Troyes, pour amateurs : une andouillette AAAAA, entaillée, grillée puis passée au four avec une sauce à la moutarde et à l'échalote. Pas de version sans porc : c'est l'essence du plat.",
  ["2|andouillettes (AAAAA de préférence)|Andouille / andouillette|3", f"2|échalotes|{ECHA}|1", f"2 c. à s.|de moutarde de Dijon|{DIJON}|2", f"15 cl|de crème|{CF_}|2", "10 cl|de vin blanc|Vin blanc|1", f"500 g|de pommes de terre|{PDT}|2", f"20 g|de beurre|{BEURRE}|1"],
  ["**Entailler.** Andouillettes piquées et incisées en biais (elles n'éclatent pas) ; poêle, beurre, 8 min en tournant : dorées.",
   "**Sauce.** Échalotes 2 min, vin blanc, réduit de moitié ; crème, moutarde, 2 min.",
   "**Four.** Andouillettes dans la sauce, four 180 °C 12 min : sauce bouillonnante, peau croustillante.",
   "**Servir.** Avec des pommes sautées au beurre et une salade."],
  var=[VB], keep="Le jour même.", age=None, kids="Pour les adultes (goût puissant).", cats=[], profil=["gras", "acide"])
K("boudin_noir_pommes", "Boudin noir aux pommes", "Boudin aux pommes", "France › Normandie", "P", 1, 4, 10, 20, "€", "Deux poêles.",
  "Le boudin noir doucement poêlé, servi avec des quartiers de pomme caramélisés au beurre : le sucré-salé normand de l'hiver, avec une purée.",
  ["4|boudins noirs|Boudin noir|3", "4|pommes (reinette, boskoop)|Pomme|3", f"40 g|de beurre|{BEURRE}|2", f"1 c. à s.|de sucre|{SUCRE}|1", f"1 pincée|de cannelle|{CANN}|0?"],
  ["**Pommes.** Pelées, en quartiers ; beurre moussant, 10 min en retournant : dorées, tendres ; sucre, cannelle, 2 min : caramélisées.",
   "**Boudin.** Piqué, poêle à feu doux avec une noix de beurre, 8 à 10 min en le tournant délicatement : chaud au cœur, la peau tient.",
   "**Ne pas brusquer.** Feu doux : à feu vif, le boudin éclate.",
   "**Servir.** Avec les pommes et une purée maison."],
  keep="Le jour même.", age=3, cats=[], fetes=["Noël"], profil=["gras", "sucre"], side="puree_maison")

# ---------------- Pommes de terre ----------------
K("pommes_dauphine", "Pommes dauphine (pâte à choux et purée)", "Pommes dauphine", "France › Cuisine de chef", "A", 3, 6, 40, 30, "€", "Casserole, poche ou deux cuillères, friteuse.",
  "Deux tiers de purée sèche, un tiers de pâte à choux, frits en petites quenelles : croustillantes dehors, aériennes dedans. Le garniture des grands rôtis.",
  [f"500 g|de pommes de terre farineuses|{PDT}|3", "25 cl|d'eau|-|0", f"80 g|de beurre|{BEURRE}|2", f"125 g|de farine|{F55}|2", f"4|œufs|{OEUF}|2", f"1 pincée|de muscade|{MUSC}|0", "1 L|d'huile de friture|Huile d'arachide|2"],
  ["**Purée.** Pommes de terre cuites en robe des champs, pelées, passées au moulin, desséchées 3 min à feu doux : très sèche.",
   "**Choux.** Eau, beurre, sel à ébullition ; farine d'un coup, dessèche 1 min ; hors du feu, œufs un à un : pâte lisse qui fait le ruban en V.",
   "**Mélanger.** Purée et pâte à choux, muscade, poivre : appareil souple.",
   "**Frire.** 170 °C, quenelles formées à deux cuillères, 4 à 5 min : gonflées, dorées ; égouttées, salées."],
  tips=["Huile chaude : loin des enfants."], keep="Crues : 1 mois au congélateur, frites sans décongeler.", age=2, cats=["vegetarien", "enfants"], fetes=["Noël", "Repas de famille"], profil=["gras"], tech=["Pâte à choux", "Frire"])
K("pommes_anna", "Pommes Anna (gâteau de pommes de terre au beurre)", "Pommes Anna", "France › Cuisine de chef", "A", 2, 6, 25, 50, "€", "Poêle allant au four (fonte), mandoline.",
  "Des rondelles fines de pommes de terre disposées en rosace, beurrées couche par couche, cuites à la poêle puis au four : un gâteau doré et croustillant dehors, fondant dedans.",
  [f"1,2 kg|de pommes de terre à chair ferme|{PDT}|3", "100 g|de beurre clarifié|Graisse de canard / beurre clarifié|3", f"1 c. à c.|de thym|{THYM}|1?"],
  ["**Trancher.** Pommes de terre en rondelles de 2 mm à la mandoline, séchées dans un torchon (non lavées : l'amidon colle les couches).",
   "**Monter.** Poêle beurrée, rosace serrée, beurre fondu, sel, poivre à chaque couche.",
   "**Cuire.** Feu moyen 10 min (le dessous dore), pressé avec une spatule ; four 200 °C 40 min : une lame entre sans résistance.",
   "**Retourner.** Sur une assiette d'un geste ; en parts."],
  tips=["Mandoline : protège-doigts toujours."], keep="1 jour ; réchauffée au four.", age=1, cats=["vegetarien"], profil=["gras"])
K("pommes_boulangere", "Pommes boulangère (au bouillon et aux oignons)", "Pommes boulangère", "France › Cuisine de bistrot", "A", 1, 6, 20, 60, "€", "Plat à gratin.",
  "Les pommes de terre que l'on mettait autrefois dans le four du boulanger sous le gigot : en rondelles avec des oignons fondus, mouillées de bouillon, dorées dessus et fondantes dessous.",
  [f"1,2 kg|de pommes de terre|{PDT}|3", f"3|oignons|{OIG}|2", f"50 cl|de bouillon de volaille|{BOUILLON}|2", f"40 g|de beurre|{BEURRE}|1", f"1 c. à c.|de thym|{THYM}|1", f"2|gousses d'ail|{AIL}|1", f"1|feuille de laurier|{LAURIER}|0"],
  ["**Oignons.** Émincés, 20 g de beurre, 12 min à feu doux : fondants, blonds.",
   "**Monter.** Plat frotté d'ail, rondelles de 3 mm et oignons en couches, thym, sel, poivre ; bouillon chaud à hauteur, laurier, reste de beurre en noisettes.",
   "**Cuire.** Four 180 °C 1 h : le bouillon est absorbé, le dessus doré et croustillant.",
   "**Servir.** Avec un gigot ou un poulet rôti, dont le jus coule dessus."],
  keep="2 jours au frigo.", age=1, cats=["vegetarien", "enfants"], profil=["leger"])

# ---------------- Entrées ----------------
K("vichyssoise", "Vichyssoise (velouté froid de poireaux et pommes de terre)", "Vichyssoise", "France › Auvergne-Rhône-Alpes", "E", 1, 6, 20, 30, "€", "Cocotte, mixeur.",
  "Le potage poireaux-pommes de terre servi glacé, très lisse, à la crème et à la ciboulette : une entrée d'été élégante.",
  ["4|blancs de poireaux|Poireau|3", f"400 g|de pommes de terre|{PDT}|2", f"30 g|de beurre|{BEURRE}|1", f"1 L|de bouillon de volaille|{BOUILLON}|2", f"20 cl|de crème fleurette|{FL}|2", "1/2|botte de ciboulette|Ciboulette|1"],
  ["**Suer.** Poireaux émincés, beurre, 10 min à couvert, feu doux : fondants, sans couleur.",
   "**Cuire.** Pommes de terre en dés, bouillon, sel, 20 min.",
   "**Mixer.** Très finement, passé au chinois ; crème : velouté nappant.",
   "**Glacer.** 4 h au frigo ; rectifie le sel (le froid l'atténue), ciboulette ciselée."],
  keep="2 jours au frigo.", age=1, cats=["enfants", "leger"], fetes=["Barbecue d'été"], profil=["leger"], tech=["Suer"])
K("artichauts_vinaigrette", "Artichauts vinaigrette", "Artichauts", "France › Bretagne", "E", 1, 4, 10, 35, "€", "Grande casserole.",
  "Le gros artichaut breton cuit à l'eau, dont on trempe chaque feuille dans une vinaigrette moutardée, jusqu'au cœur : une entrée de printemps lente et conviviale.",
  ["4|artichauts camus|Artichaut|3", f"1|citron|{CIT}|1", f"1 c. à s.|de moutarde|{DIJON}|1", f"2 c. à s.|de vinaigre de vin|Vinaigre de vin rouge / blanc|1", f"6 c. à s.|d'huile|{HN}|1", f"1|échalote|{ECHA}|1"],
  ["**Préparer.** Queue cassée à la main (elle tire les fibres), base frottée de citron.",
   "**Cuire.** Grande eau bouillante salée citronnée, tête en bas, 30 à 40 min : une feuille du centre se détache sans effort.",
   "**Égoutter.** Tête en bas, 5 min.",
   "**Vinaigrette.** Moutarde, vinaigre, sel, échalote ciselée, huile en filet ; tiède ou froid."],
  keep="1 jour au frigo (cuits).", age=2, cats=["vegetarien", "leger"], profil=["acide", "leger"])
K("cuisses_grenouilles_persillade", "Cuisses de grenouilles en persillade", "Grenouilles persillade", "France › Auvergne-Rhône-Alpes", "E", 1, 4, 15, 10, "€€", "Grande poêle.",
  "La spécialité de la Dombes : des cuisses de grenouilles farinées, sautées au beurre jusqu'à dorer, puis enrobées d'ail et de persil. La chair, fine comme celle d'un poulet, se mange avec les doigts.",
  ["800 g|de cuisses de grenouilles (surgelées)|-|3", f"60 g|de beurre|{BEURRE}|2", f"4|gousses d'ail|{AIL}|1", f"1|botte de persil|{PERSIL}|2", f"3 c. à s.|de farine|{F55}|1", f"1|citron|{CIT}|1"],
  ["**Décongeler.** Une nuit au frigo, épongées très sèches.",
   "**Fariner.** Salées, poivrées, farine, excédent tapoté.",
   "**Sauter.** Beurre moussant, à feu vif, en deux fois, 3 min par face : dorées, chair qui se détache de l'os.",
   "**Persillade.** Ail et persil hachés ensemble, 30 s dans la poêle : parfumée sans brûler ; citron."],
  keep="À manger tout de suite.", age=3, cats=[], profil=["gras"])
K("cervelle_de_canut", "Cervelle de canut (fromage blanc aux herbes, Lyon)", "Cervelle de canut", "France › Auvergne-Rhône-Alpes", "E", 1, 4, 10, 60, "€", "Saladier, fouet.",
  "La spécialité des bouchons lyonnais : un fromage blanc égoutté battu avec échalote, ciboulette, persil, un trait de vinaigre et d'huile. Avec des pommes vapeur ou du pain grillé.",
  ["400 g|de fromage blanc en faisselle|Fromage blanc / faisselle|3", f"2|échalotes|{ECHA}|1", "1/2|botte de ciboulette|Ciboulette|1", f"1/2|botte de persil|{PERSIL}|1", f"1 c. à s.|de vinaigre de vin|Vinaigre de vin rouge / blanc|1", f"2 c. à s.|d'huile de noix ou d'olive|{HO}|1", f"10 cl|de crème fraîche|{CF_}|1"],
  ["**Égoutter.** Faisselle 1 h dans une passoire.",
   "**Battre.** Au fouet avec la crème : lisse et aérien.",
   "**Assaisonner.** Échalotes ciselées très fin, herbes, vinaigre, huile, sel, poivre généreux.",
   "**Reposer.** 1 h au frais ; avec des pommes vapeur tièdes."],
  keep="2 jours au frigo.", age=1, cats=["vegetarien", "leger"], fetes=["Apéritif dînatoire"], profil=["acide", "leger"])

# ---------------- Abats ----------------
K("ris_de_veau_morilles", "Ris de veau aux morilles", "Ris de veau aux morilles", "France › Cuisine de chef", "P", 3, 4, 40, 30, "€€€", "Casserole, poêle, poids.",
  "L'abat le plus fin : des ris de veau dégorgés, blanchis, pressés, puis dorés au beurre noisette et servis avec une sauce crémée aux morilles. Le plat des grandes occasions.",
  ["600 g|de ris de veau|-|3", "30 g|de morilles séchées (ou 200 g fraîches)|Cèpe / girolle / morille|3", f"2|échalotes|{ECHA}|1", f"25 cl|de crème|{FL}|2", f"15 cl|de fond de veau|{FOND}|1", f"40 g|de beurre|{BEURRE}|2", f"2 c. à s.|de farine|{F55}|1", "4 cl|de vin jaune ou de madère (facultatif)|Madère / marsala / xérès|1?"],
  ["**Dégorger et blanchir.** Ris 4 h dans l'eau froide changée souvent ; eau froide salée, à frémissement 3 min ; rafraîchis, peau et nerfs retirés, pressés entre deux plaques avec un poids 2 h au frigo.",
   "**Morilles.** Réhydratées 30 min dans l'eau tiède, rincées (sable), eau filtrée gardée.",
   "**Sauce.** Beurre, échalotes, morilles 3 min ; alcool, eau des morilles, fond, réduit de moitié ; crème, 5 min : nappante.",
   "**Dorer.** Ris en escalopes épaisses, farinés, beurre noisette, 3 min par face : dorés, moelleux ; nappés de sauce."],
  tips=["Achète les ris chez le boucher, la veille ; les morilles doivent toujours être bien cuites (crues, elles sont toxiques)."],
  var=[("Sans alcool", ["alcohol"], {"Madère / marsala / xérès": [("Bouillon d'os maison (bœuf/volaille)", 1.0)]}, "Madère → **un peu plus de fond**. **À tester**.")],
  keep="Le jour même.", age=6, cats=[], fetes=["Noël", "Repas de famille"], profil=["gras"], tech=["Dégorger"])
K("rognons_veau_moutarde", "Rognons de veau à la moutarde", "Rognons à la moutarde", "France › Cuisine de bistrot", "P", 2, 4, 20, 10, "€€", "Grande poêle.",
  "Les rognons de veau dégraissés, coupés en morceaux, saisis très vite pour rester rosés, puis nappés d'une sauce à la crème et à la moutarde. Avec du riz ou des pâtes fraîches.",
  ["800 g|de rognons de veau|-|3", f"2|échalotes|{ECHA}|1", f"2 c. à s.|de moutarde de Dijon (+ 1 à l'ancienne)|{DIJON}|2", f"20 cl|de crème|{CF_}|2", "4 cl|de cognac (facultatif)|Cognac / armagnac / brandy|1?", f"20 g|de beurre|{BEURRE}|1", f"1 c. à s.|d'huile|{HN}|1", f"1/2|botte de persil|{PERSIL}|1"],
  ["**Parer.** Graisse et nerfs blancs retirés, rognons en morceaux de 3 cm.",
   "**Saisir.** Poêle fumante, huile, 2 min en remuant : saisis, rosés ; dans une passoire 5 min (ils rendent un jus amer, jeté).",
   "**Sauce.** Beurre, échalotes 2 min, cognac, crème, 3 min ; hors du feu, moutardes.",
   "**Réchauffer.** Rognons 1 min dans la sauce, sans bouillir (ils durcissent) ; persil."],
  var=[COGNAC_SA], keep="Le jour même.", age=6, cats=["express"], profil=["gras", "acide"])
K("foie_veau_persillade", "Foie de veau poêlé, persillade et vinaigre de framboise", "Foie de veau", "France › Cuisine de bistrot", "P", 1, 2, 10, 6, "€€€", "Poêle.",
  "Une tranche épaisse de foie de veau, farinée, saisie rosée au beurre, déglacée d'un trait de vinaigre et parsemée de persillade : le classique des brasseries, avec une purée.",
  ["2|tranches de foie de veau (1,5 cm)|Foie de veau|3", f"2 c. à s.|de farine|{F55}|1", f"30 g|de beurre|{BEURRE}|2", f"1 c. à s.|de vinaigre de framboise ou de vin|Vinaigre de vin rouge / blanc|1", f"1|gousse d'ail|{AIL}|1", f"1/2|botte de persil|{PERSIL}|1"],
  ["**Fariner.** Tranches épongées, farinées, excédent tapoté ; sel au dernier moment.",
   "**Saisir.** Beurre moussant, 1 min 30 par face : doré dehors, rosé dedans (cuit trop, il devient sec et granuleux).",
   "**Déglacer.** Vinaigre dans la poêle chaude, ail et persil hachés, 20 s.",
   "**Servir.** Nappé, avec une purée."],
  keep="À manger tout de suite.", age=3, cats=["express"], profil=["gras", "acide"], side="puree_maison")

# ---------------- Gibier, volailles fines ----------------
K("civet_chevreuil", "Civet de chevreuil", "Civet de chevreuil", "France › Grand Est", "P", 2, 6, 40, 1560, "€€€", "Grande cocotte.",
  "Le plat de chasse par excellence : le chevreuil mariné une nuit dans le vin rouge aux aromates, saisi, puis mijoté longuement ; sauce liée, garniture de champignons et de petits oignons, avec des spätzle ou une purée de céleri.",
  ["1,5 kg|d'épaule de chevreuil en morceaux|Cerf / biche / chevreuil|3", "75 cl|de vin rouge corsé|Vin rouge|3", f"2|carottes|{CAROTTE}|1", f"2|oignons|{OIG}|1", "8|baies de genièvre|Baies de genièvre|1", "1|bouquet garni|Laurier|1", f"2 c. à s.|de farine|{F55}|1", "250 g|de champignons|Champignon de Paris|2", f"30 g|de chocolat noir (facultatif)|{CHOCO}|1?", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Mariner (la veille).** Viande, vin, carottes, oignons, genièvre écrasé, bouquet ; 12 à 24 h au frais.",
   "**Saisir.** Viande égouttée, épongée, en plusieurs fois dans l'huile fumante : bien brune ; singer (farine, 1 min).",
   "**Mijoter.** Marinade portée à ébullition et écumée, versée dessus, sel ; 2 h 30 à feu doux : la viande s'effiloche ; champignons poêlés en fin.",
   "**Lier.** Sauce réduite à la nappe, chocolat fondu dedans (rond, profond) ; rectifie, poivre."],
  tips=["Encore meilleur le lendemain."], var=[VR], keep="3 jours au frigo ; se congèle.", age=None, kids="✓ dès 3 ans en version sans alcool.", fetes=["Noël", "Repas de famille"], profil=["viande_rouge"], tech=["Mariner", "Lier à la farine", "Mijoter"])
K("pintade_choux", "Pintade rôtie au chou et aux lardons", "Pintade au chou", "France › Auvergne-Rhône-Alpes", "P", 2, 4, 30, 75, "€€", "Cocotte.",
  "La pintade, plus parfumée que le poulet, rôtie en cocotte puis finie sur un lit de chou vert braisé aux lardons et aux carottes : un plat de dimanche d'hiver.",
  ["1|pintade fermière (1,4 kg)|Pintade|3", "1|chou vert frisé|Chou vert / frisé / kale|3", "150 g|de lardons|Lardons|2", f"2|carottes|{CAROTTE}|1", f"1|oignon|{OIG}|1", f"30 g|de beurre|{BEURRE}|1", f"20 cl|de bouillon|{BOUILLON}|1", "4|baies de genièvre|Baies de genièvre|1?"],
  ["**Blanchir.** Chou en quartiers, 5 min à l'eau bouillante salée ; égoutté, pressé.",
   "**Dorer.** Pintade salée, beurre, cocotte, 10 min sur toutes les faces ; réservée. Lardons, oignon, carottes 5 min.",
   "**Braiser.** Chou, genièvre, bouillon ; pintade posée dessus, couvercle, four 180 °C 1 h : cuisses à 80 °C.",
   "**Servir.** Découpée sur le chou, jus de cuisson dessus."],
  var=[("Sans porc", ["pork"], {"Lardons": [("Lardons de dinde / de volaille fumés", 1.0)]}, "Lardons → **lardons de dinde fumés**. **À tester**.")],
  keep="2 jours au frigo.", age=1, cats=["enfants"], fetes=["Repas de famille"], profil=["gras"], kids="✓ dès 1 an, chair effilochée.")
K("pigeon_petits_pois", "Pigeon rôti aux petits pois à la française", "Pigeon aux petits pois", "France › Cuisine de chef", "P", 3, 2, 30, 25, "€€€", "Cocotte, poêle.",
  "Le pigeonneau rôti rosé, le jus réduit avec ses abattis, et des petits pois à la française (laitue, petits oignons, beurre). Chair rouge et tendre, à servir rosée.",
  ["2|pigeonneaux prêts à cuire|-|3", "400 g|de petits pois (frais ou surgelés)|Petits pois / pois gourmands|3", "1|cœur de laitue|Salade (laitue, batavia)|1", "8|petits oignons|Oignon nouveau / cébette|1", f"50 g|de beurre|{BEURRE}|2", f"15 cl|de fond de volaille|{FOND}|1", f"1 c. à c.|de sucre|{SUCRE}|0"],
  ["**Rôtir.** Pigeons salés, bridés ; cocotte, beurre, 3 min par face ; four 200 °C 10 à 12 min : filets à 55 °C (rosés) ; repos 8 min.",
   "**Petits pois.** Beurre, oignons 3 min, petits pois, laitue émincée, sucre, sel, 5 cl d'eau ; à couvert 10 min : tendres et brillants.",
   "**Jus.** Cocotte dégraissée, fond, sucs grattés, réduit 3 min : sirupeux ; une noix de beurre.",
   "**Découper.** Filets et cuisses levés, sur les petits pois, jus autour."],
  tips=["Le pigeon se mange rosé : cuit trop, il devient sec et prend un goût de foie."], keep="Le jour même.", age=3, cats=[], fetes=["Saint-Valentin", "Repas de famille"], profil=["viande_rouge", "gras"], tech=["Rôtir"])
