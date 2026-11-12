# -*- coding: utf-8 -*-
"""Audit « fin gourmet, cuisine française » (12/11/2026) : poissons et crustacés de la côte, fonds de base et grandes
sauces dérivées qui manquaient (le socle de la cuisine française). Recettes de référence réécrites avec les repères
ATLAS. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

VB = ("Sans alcool", ["alcohol"], {"Vin blanc": [("Fumet de poisson maison", 0.8), ("Vinaigre de cidre", 0.05)]}, "Vin blanc → **fumet + 1 c. à c. de vinaigre de cidre** : l'acidité est gardée. **À tester**.")
VBV = ("Sans alcool", ["alcohol"], {"Vin blanc": [("Bouillon d'os maison (bœuf/volaille)", 0.8), ("Vinaigre de cidre", 0.05)]}, "Vin blanc → **bouillon + 1 c. à c. de vinaigre de cidre**. **À tester**.")
VR = ("Sans alcool", ["alcohol"], {"Vin rouge": [("Bouillon d'os maison (bœuf/volaille)", 0.5), ("Jus de raisin / pomme (pur jus)", 0.4), ("Vinaigre de vin rouge / blanc", 0.05)]},
      "Vin rouge → **fond + jus de raisin + un trait de vinaigre**. **À tester**.")
ECHA = "Échalote"; FL = "Crème fleurette (liquide)"; FUMET = "Fumet de poisson maison"; ESTR = "Estragon"; CERF = "Cerfeuil"

# ---------------- Fonds et bases ----------------
K("fond_brun_veau", "Fond brun de veau (la base des sauces brunes)", "Fond brun", "France › Cuisine de base", "Ba", 2, 10, 30, 300, "€", "Plaque de four, grande marmite, chinois.",
  "La base des grandes sauces : des os de veau et des légumes rôtis jusqu'à brunir, mouillés d'eau et cuits très longtemps à frémissement, puis réduits. En glaçons au congélateur, il transforme n'importe quelle sauce.",
  ["2 kg|d'os de veau concassés (et un pied de veau)|Pied de veau / de bœuf|3", f"2|carottes|{CAROTTE}|2", f"2|oignons|{OIG}|2", "1|branche de céleri|Céleri-branche|1", f"2 c. à s.|de concentré de tomate|{CONC}|1", "1|bouquet garni|Laurier|1", f"2|gousses d'ail|{AIL}|1"],
  ["**Rôtir.** Os sur la plaque, four 220 °C 40 min ; légumes en gros morceaux ajoutés 20 min avant : brun foncé, pas brûlé.",
   "**Pincer.** Concentré étalé sur les os, 5 min au four : il fonce (le goût et la couleur).",
   "**Mouiller.** Dans la marmite, plaque déglacée à l'eau, eau froide à hauteur (4 L), bouquet, ail ; à frémissement, écumé souvent, 4 à 5 h sans sel ni couvercle.",
   "**Réduire.** Passé au chinois, dégraissé froid, réduit de moitié : il nappe légèrement la cuillère ; en bacs à glaçons."],
  tips=["Jamais de sel dans un fond : il se concentre à la réduction.", "L'ébullition trouble le fond : quelques bulles seulement."], keep="5 jours au frigo ; 6 mois congelé en glaçons.", age=1, cats=["sauces"], profil=[], tech=["Écumer", "Réduire", "Mixer et filtrer"])
K("fond_blanc_volaille", "Fond blanc de volaille", "Fond blanc", "France › Cuisine de base", "Ba", 1, 10, 20, 180, "€", "Grande marmite, chinois.",
  "Le bouillon clair des sauces blanches, blanquettes et risottos : carcasses de volaille blanchies puis cuites doucement avec des légumes, sans coloration.",
  ["1,5 kg|de carcasses et ailes de volaille|Canard entier / carcasse|3", f"2|carottes|{CAROTTE}|1", "1|blanc de poireau|Poireau|1", f"1|oignon piqué d'un clou de girofle|{OIG}|1", "1|branche de céleri|Céleri-branche|1", "1|bouquet garni|Laurier|1"],
  ["**Blanchir.** Carcasses à l'eau froide, à ébullition 2 min, égouttées, rincées : le fond restera clair.",
   "**Cuire.** Eau froide à hauteur (3 L), légumes, bouquet ; frémissement 2 h 30, écumé.",
   "**Passer.** Au chinois, sans presser.",
   "**Dégraisser.** Une nuit au frigo : la graisse figée s'enlève d'un geste."],
  keep="4 jours au frigo ; 6 mois congelé.", age=1, cats=["sauces"], profil=["leger"], tech=["Faire un bouillon", "Écumer"])
K("fumet_poisson", "Fumet de poisson", "Fumet", "France › Cuisine de base", "Ba", 1, 8, 15, 30, "€", "Casserole, chinois.",
  "Le bouillon des sauces au poisson, en trente minutes : arêtes et têtes de poissons blancs, échalote, champignons, vin blanc. Jamais plus de 30 min, sinon il devient amer.",
  ["1 kg|d'arêtes et têtes de poissons blancs (sole, merlan, bar), ouïes retirées|Cabillaud / morue fraîche|3", f"2|échalotes|{ECHA}|1", "100 g|de parures de champignons|Champignon de Paris|1", "15 cl|de vin blanc sec|Vin blanc|2", f"20 g|de beurre|{BEURRE}|1", "1|bouquet garni|Laurier|1"],
  ["**Dégorger.** Arêtes 30 min dans l'eau froide (le sang part), ouïes retirées.",
   "**Suer.** Beurre, échalotes, champignons, arêtes, 4 min sans coloration.",
   "**Mouiller.** Vin blanc, réduit 2 min ; eau froide à hauteur (1,5 L), bouquet ; frémissement 20 min, écumé.",
   "**Passer.** Au chinois fin, sans presser ; réduit de moitié pour une sauce."],
  var=[("Sans alcool", ["alcohol"], {"Vin blanc": [("Vinaigre de cidre", 0.05)]}, "Vin blanc → **un trait de vinaigre de cidre ou de citron** dans l'eau. **À tester**.")],
  keep="2 jours au frigo ; 3 mois congelé.", age=1, cats=["sauces"], profil=["poisson", "leger"], tech=["Suer", "Écumer"])
K("court_bouillon", "Court-bouillon pour pocher poissons et crustacés", "Court-bouillon", "France › Cuisine de base", "Ba", 1, 6, 10, 30, "€", "Grande marmite.",
  "Le liquide parfumé où l'on poche saumon, raie, langoustines ou homard : eau, vin blanc ou vinaigre, légumes, poivre et herbes, cuits 20 minutes avant d'y plonger le poisson.",
  [f"2 L|d'eau|-|0", "25 cl|de vin blanc (ou 5 cl de vinaigre)|Vin blanc|2", f"2|carottes|{CAROTTE}|1", f"1|oignon|{OIG}|1", "1|bouquet garni|Laurier|1", f"1 c. à c.|de poivre en grains|{POIVRE}|1", f"30 g|de gros sel|{SEL}|1"],
  ["**Tailler.** Carottes et oignon en rondelles fines.",
   "**Cuire.** Tout dans l'eau froide, ébullition, 20 min de frémissement : le goût passe dans l'eau.",
   "**Tiédir ou non.** Poisson entier : départ dans le court-bouillon froid ; crustacés et filets : bouillon frémissant.",
   "**Pocher.** Sans jamais bouillir : le poisson resterait sec et se déferait."],
  var=[("Sans alcool", ["alcohol"], {"Vin blanc": [("Vinaigre de cidre", 0.2)]}, "Vin blanc → **5 cl de vinaigre de cidre**. **À tester**.")],
  keep="Le jour même.", age=1, cats=["sauces"], profil=["leger"], tech=["Pocher"])

# ---------------- Sauces dérivées ----------------
K("sauce_mornay", "Sauce Mornay (béchamel au fromage)", "Sauce Mornay", "France › Sauces", "S", 1, 6, 5, 15, "€", "Casserole, fouet.",
  "La béchamel enrichie de jaune d'œuf et de fromage râpé : la sauce des gratins, des croque-monsieur, des endives et des œufs Florentine.",
  ["50 cl|de béchamel chaude (fiche Béchamel)|SUB:bechamel|3", f"80 g|de gruyère ou comté râpé|{GRUY}|2", f"1|jaune d'œuf|Jaune d'œuf|1", f"1 pincée|de muscade|{MUSC}|0"],
  ["**Béchamel.** Chaude, nappante.",
   "**Fromage.** Hors du feu, en pluie en tournant : fondu, lisse.",
   "**Jaune.** Battu avec une cuillère de sauce, puis dans la casserole : plus riche, plus dorée au four.",
   "**Assaisonner.** Muscade, poivre ; nappe et gratine aussitôt."],
  keep="2 jours au frigo, filmée au contact.", age=1, cats=["sauces", "vegetarien", "enfants"], profil=["gras"], tech=["Roux"])
K("sauce_bordelaise", "Sauce bordelaise (vin rouge, échalote, moelle)", "Sauce bordelaise", "France › Nouvelle-Aquitaine", "S", 2, 4, 15, 40, "€€", "Casserole, chinois.",
  "La sauce de l'entrecôte à la bordelaise : vin rouge réduit avec l'échalote et le thym, monté au fond brun, et des rondelles de moelle pochées.",
  [f"3|échalotes|{ECHA}|2", "40 cl|de vin rouge de Bordeaux|Vin rouge|3", "30 cl|de fond brun (fiche Fond brun)|SUB:fond_brun_veau|3", "2|os à moelle|Os à moelle|1?", f"1|branche de thym|{THYM}|1", f"30 g|de beurre froid|{BEURRE}|1"],
  ["**Réduire.** Échalotes ciselées, vin, thym, poivre concassé : réduit aux trois quarts, presque sec.",
   "**Mouiller.** Fond brun, 15 min : réduit à la nappe ; passé au chinois.",
   "**Moelle.** Sortie des os (à tremper 1 h avant), en rondelles, pochée 1 min dans l'eau salée frémissante.",
   "**Monter.** Hors du feu, beurre froid en tournant : brillante ; moelle dedans."],
  var=[VR], keep="2 jours au frigo.", age=None, kids="✓ dès 3 ans en version sans alcool.", cats=["sauces"], profil=["viande_rouge", "acide"], tech=["Réduire", "Monter au beurre"])
K("sauce_choron", "Sauce Choron (béarnaise à la tomate)", "Sauce Choron", "France › Sauces", "S", 2, 4, 10, 15, "€", "Bain-marie, fouet.",
  "Une béarnaise à laquelle on ajoute une fondue de tomate très réduite : rose, parfumée à l'estragon, pour les viandes grillées et les poissons.",
  ["1|bol de sauce béarnaise (fiche Béarnaise)|SUB:sauce_bearnaise|3", f"2|tomates|{TOM}|2", f"1 c. à c.|de concentré|{CONC}|1", f"1 c. à c.|d'huile d'olive|{HO}|0"],
  ["**Fondue de tomate.** Tomates mondées, épépinées, concassées ; huile, concentré, 10 min : très réduite, sèche.",
   "**Refroidir.** Tiède (chaude, elle trancherait la sauce).",
   "**Mélanger.** 2 c. à s. de fondue dans la béarnaise tiède, en fouettant : rose, lisse.",
   "**Garder.** Au bain-marie tiède (pas chaud), à servir dans l'heure."],
  tips=["Œufs à peine cuits : jaunes de poules pondeuses récentes ; femme enceinte et jeunes enfants : à éviter."], keep="À servir dans l'heure.", age=None, kids="Pour les adultes (jaunes peu cuits).", cats=["sauces", "vegetarien"], profil=["gras", "acide"])
K("sauce_ravigote", "Sauce ravigote (vinaigrette aux herbes, câpres et cornichons)", "Sauce ravigote", "France › Sauces", "S", 1, 4, 10, 0, "€", "Bol.",
  "Une vinaigrette relevée et pleine d'herbes (cerfeuil, estragon, ciboulette, persil), de câpres, de cornichons et d'échalote : pour la tête de veau, le pot-au-feu froid, les poissons pochés.",
  [f"2 c. à s.|de vinaigre de vin|Vinaigre de vin rouge / blanc|2", f"6 c. à s.|d'huile|{HN}|2", f"1 c. à c.|de moutarde|{DIJON}|1", f"1|échalote|{ECHA}|1", "1 c. à s.|de câpres|Câpres|1", "4|cornichons|Cornichon|1", "1|bouquet d'herbes (cerfeuil, estragon, ciboulette, persil)|Cerfeuil|2"],
  ["**Base.** Moutarde, vinaigre, sel, poivre ; huile en filet en fouettant.",
   "**Hacher.** Échalote ciselée, câpres et cornichons hachés, herbes ciselées au dernier moment (elles noircissent).",
   "**Mélanger.** Tout ensemble : sauce épaisse de garniture.",
   "**Servir.** Aussitôt, sur viande ou poisson tiède."],
  keep="1 jour au frigo (herbes à ajouter au moment).", age=3, cats=["sauces", "vegetarien"], profil=["acide"])
K("sauce_soubise", "Sauce Soubise (crème d'oignons)", "Sauce Soubise", "France › Sauces", "S", 1, 6, 10, 40, "€", "Casserole, mixeur.",
  "Des oignons fondus très longtemps au beurre sans colorer, liés à la béchamel ou à la crème et mixés : une sauce douce et sucrée pour les côtes de veau, les œufs, le gigot.",
  [f"600 g|d'oignons|{OIG}|3", f"40 g|de beurre|{BEURRE}|2", f"20 cl|de crème|{FL}|2", f"1 pincée|de muscade|{MUSC}|0"],
  ["**Blanchir.** Oignons émincés, 3 min à l'eau bouillante, égouttés (ils seront plus doux).",
   "**Étuver.** Beurre, oignons, sel, à couvert, feu très doux 30 min en remuant : fondus, blancs, pas dorés.",
   "**Lier.** Crème, 5 min.",
   "**Mixer.** Très lisse ; muscade, poivre blanc."],
  keep="3 jours au frigo.", age=1, cats=["sauces", "vegetarien", "enfants"], profil=["sucre", "gras"], tech=["Faire suer"])
K("sauce_morilles", "Sauce aux morilles et au vin jaune (version sans alcool possible)", "Sauce aux morilles", "France › Bourgogne-Franche-Comté", "S", 2, 4, 15, 25, "€€€", "Casserole.",
  "La sauce du poulet au vin jaune et aux morilles du Jura : des morilles réhydratées, une réduction de vin jaune et d'échalote, de la crème. Pour la volaille, le veau, les pâtes fraîches.",
  ["30 g|de morilles séchées|Cèpe / girolle / morille|3", f"2|échalotes|{ECHA}|1", "10 cl|de vin jaune (ou vin blanc sec)|Vin blanc|2", f"30 cl|de crème|{FL}|3", f"20 g|de beurre|{BEURRE}|1"],
  ["**Réhydrater.** Morilles 30 min dans l'eau tiède, rincées une à une (sable), eau filtrée gardée.",
   "**Suer.** Beurre, échalotes, morilles, 5 min.",
   "**Réduire.** Vin, réduit de moitié ; eau des morilles, réduit encore.",
   "**Crème.** 8 min : nappante ; sel, poivre."],
  tips=["Les morilles se mangent toujours bien cuites : crues ou peu cuites, elles sont toxiques."], var=[VBV], keep="2 jours au frigo.", age=3, cats=["sauces", "vegetarien"], fetes=["Noël"], profil=["gras"])
K("sauce_poivrade", "Sauce poivrade (pour le gibier)", "Sauce poivrade", "France › Sauces", "S", 2, 6, 15, 45, "€€", "Casserole, chinois.",
  "La sauce brune et poivrée du gibier : une mirepoix rissolée, déglacée au vinaigre et à la marinade, mouillée de fond, relevée de poivre concassé en fin de cuisson.",
  [f"1|carotte|{CAROTTE}|1", f"1|oignon|{OIG}|1", f"2 c. à s.|de vinaigre de vin|Vinaigre de vin rouge / blanc|2", "25 cl|de vin rouge ou de marinade du gibier|Vin rouge|2", "40 cl|de fond brun (fiche Fond brun)|SUB:fond_brun_veau|3", f"1 c. à c.|de poivre concassé|{POIVRE}|2", f"30 g|de beurre|{BEURRE}|1", "4|baies de genièvre|Baies de genièvre|1?"],
  ["**Mirepoix.** Carotte et oignon en petits dés, 10 g de beurre, 8 min : bien dorés.",
   "**Déglacer.** Vinaigre, réduit à sec ; vin, réduit de moitié.",
   "**Mouiller.** Fond, genièvre, 25 min ; poivre les 5 dernières minutes (plus tôt, il devient âcre).",
   "**Passer et monter.** Chinois, puis reste de beurre en tournant."],
  var=[VR], keep="3 jours au frigo.", age=None, kids="✓ dès 6 ans en version sans alcool, peu poivrée.", cats=["sauces"], profil=["viande_rouge", "epice", "acide"])

# ---------------- Poissons et crustacés ----------------
K("raie_beurre_noisette_capres", "Aile de raie au beurre noisette et aux câpres", "Raie aux câpres", "France › Cuisine de bistrot", "P", 1, 2, 10, 15, "€€", "Sauteuse, petite poêle.",
  "L'aile de raie pochée dans un court-bouillon, la peau retirée, arrosée d'un beurre noisette mousseux aux câpres, au persil et au citron : un classique de brasserie, chair nacrée en lamelles.",
  ["2|ailes de raie (300 g) pelées|Raie|3", "1|court-bouillon (fiche Court-bouillon) ou eau vinaigrée|-|1", f"60 g|de beurre|{BEURRE}|2", "2 c. à s.|de câpres|Câpres|2", f"1|citron|{CIT}|1", f"1/2|botte de persil|{PERSIL}|1"],
  ["**Pocher.** Court-bouillon frémissant, raie 10 à 12 min sans bouillir : la chair se détache du cartilage.",
   "**Égoutter.** Délicatement, peau restante retirée, sur assiettes chaudes.",
   "**Beurre noisette.** Beurre à feu moyen jusqu'à mousser et sentir la noisette, couleur blonde ; câpres, jus de citron (ça crépite), persil.",
   "**Arroser.** Aussitôt, pommes vapeur à côté."],
  tips=["La raie doit sentir la mer, jamais l'ammoniaque."], keep="À manger tout de suite.", age=3, cats=[], profil=["poisson", "acide", "gras"], tech=["Pocher", "Cuisson du poisson"], side="pommes_vapeur")
K("truite_amandes", "Truite aux amandes", "Truite aux amandes", "France › Auvergne-Rhône-Alpes", "P", 1, 2, 10, 12, "€€", "Grande poêle.",
  "La truite meunière des rivières : farinée, dorée au beurre, puis couverte d'amandes effilées grillées dans le beurre noisette et d'un trait de citron.",
  ["2|truites vidées (300 g)|Truite|3", "50 g|d'amandes effilées|Amande (entière, effilée, poudre)|2", f"60 g|de beurre|{BEURRE}|2", f"3 c. à s.|de farine|{F55}|1", f"1|citron|{CIT}|1", f"1/2|botte de persil|{PERSIL}|1"],
  ["**Fariner.** Truites rincées, épongées, salées dedans et dehors, farinées, excédent tapoté.",
   "**Cuire.** 30 g de beurre moussant, 5 à 6 min par face : peau dorée, la nageoire dorsale se tire sans effort.",
   "**Amandes.** Reste du beurre, amandes, 2 min : blondes, beurre noisette ; jus de citron.",
   "**Servir.** Amandes et beurre sur les truites, persil, pommes vapeur."],
  tips=["Fruits à coque (amandes) : allergène."], keep="À manger tout de suite.", age=3, cats=["express"], profil=["poisson", "gras"], tech=["Cuisson du poisson"], side="pommes_vapeur")
K("maquereaux_vin_blanc", "Maquereaux au vin blanc", "Maquereaux au vin blanc", "France › Bretagne", "E", 1, 6, 20, 1450, "€", "Plat creux, casserole.",
  "Les filets de maquereau cuits dans une marinade chaude au vin blanc, vinaigre, carottes, oignons et aromates, puis servis froids le lendemain : l'entrée de la côte bretonne.",
  ["6|maquereaux en filets|Maquereau|3", "50 cl|de vin blanc sec|Vin blanc|3", f"10 cl|de vinaigre de cidre|{CIDRE}|2", f"2|carottes|{CAROTTE}|1", f"1|oignon|{OIG}|1", f"1|citron|{CIT}|1", "1|bouquet garni|Laurier|1", f"1 c. à c.|de poivre en grains|{POIVRE}|1", "1 c. à c.|de graines de coriandre|Coriandre (graines)|1"],
  ["**Marinade.** Vin, vinaigre, carottes et oignon en rondelles fines, citron en tranches, aromates, sel ; 10 min d'ébullition.",
   "**Cuire.** Filets serrés peau dessus dans le plat, marinade bouillante versée dessus : la chair blanchit.",
   "**Refroidir.** Filmé, 24 h au frigo.",
   "**Servir.** Froid, avec les carottes, un peu de marinade et du pain."],
  var=[VB], keep="4 jours au frigo dans la marinade.", age=None, kids="✓ dès 3 ans en version sans alcool, arêtes ôtées.", cats=[], profil=["poisson", "acide"])
K("thon_basquaise", "Thon à la basquaise", "Thon basquaise", "France › Nouvelle-Aquitaine", "P", 1, 4, 20, 35, "€€", "Sauteuse.",
  "Des pavés de thon germon saisis, puis mijotés brièvement dans une piperade aux poivrons, tomates et piment d'Espelette : la cuisine de Saint-Jean-de-Luz.",
  ["4|pavés de thon (150 g)|Thon (frais)|3", f"3|poivrons (rouges et verts)|{POIVRON}|3", f"4|tomates|{TOM}|2", f"2|oignons|{OIG}|1", f"2|gousses d'ail|{AIL}|1", "1 c. à c.|de piment d'Espelette|Piment d'Espelette|1", f"4 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Piperade.** Oignons émincés et poivrons en lanières, huile, 15 min : fondants ; ail, tomates concassées, Espelette, sel, 15 min.",
   "**Saisir.** Thon salé, poêle fumante, 1 min par face : doré dehors, rouge dedans.",
   "**Mijoter.** Dans la piperade, couvert, 4 à 5 min : rosé à cœur (cuit trop, il sèche).",
   "**Servir.** Riz blanc ou pommes vapeur."],
  keep="1 jour au frigo.", age=3, cats=["leger"], profil=["poisson", "epice"], side="riz_nature")
K("langoustines_mayonnaise", "Langoustines au court-bouillon, mayonnaise", "Langoustines mayonnaise", "France › Bretagne", "E", 1, 4, 10, 10, "€€€", "Grande marmite.",
  "Les langoustines vivantes plongées dans un court-bouillon très salé, juste le temps de les cuire, servies tièdes avec une mayonnaise maison : le goût sucré de la mer.",
  ["1 kg|de langoustines (vivantes ou très fraîches)|Langoustines|3", "1|court-bouillon (fiche Court-bouillon) ou eau de mer|-|1", "1|bol de mayonnaise (fiche Mayonnaise)|SUB:mayonnaise|2", f"1|citron|{CIT}|1"],
  ["**Bouillon.** Court-bouillon ou eau salée à 35 g/L, à grosse ébullition.",
   "**Cuire.** Langoustines, retour à l'ébullition, 2 min (moyennes) à 3 min (grosses) : la queue se recourbe.",
   "**Tiédir.** Égouttées sur un plat, 5 min.",
   "**Servir.** Tièdes, mayonnaise, citron, pain de seigle."],
  tips=["Crustacés : allergène majeur.", "Cuites trop longtemps, la chair devient cotonneuse."], keep="1 jour au frigo (cuites).", age=3, cats=[], fetes=["Noël", "Nouvel An"], profil=["poisson"])
K("homard_grille_beurre", "Homard grillé au beurre d'herbes", "Homard grillé", "France › Bretagne", "P", 3, 2, 20, 15, "€€€", "Grande marmite, four en position grill, couteau lourd.",
  "Le homard bleu breton précuit 3 minutes, fendu en deux, grillé au four sous un beurre aux herbes et à l'ail : la chair reste juteuse. Pour les grandes occasions.",
  ["2|homards bleus vivants (500 g)|Homard|3", f"80 g|de beurre mou|{BEURRE}|3", f"1|gousse d'ail|{AIL}|1", f"1/2|botte de persil|{PERSIL}|1", f"1 c. à s.|d'estragon|{ESTR}|1", f"1|citron|{CIT}|1"],
  ["**Précuire.** Homards 20 min au congélateur (ils s'endorment), puis 3 min dans l'eau bouillante très salée ; refroidis dans l'eau glacée.",
   "**Fendre.** Dans la longueur au couteau lourd, poche de la tête et intestin retirés ; pinces cassées et précuites 3 min de plus.",
   "**Beurre.** Beurre mou, ail râpé, herbes, citron, sel, poivre ; étalé sur la chair.",
   "**Griller.** Sous le grill, 6 à 8 min : chair blanche et opaque, beurre bouillonnant ; aussitôt."],
  tips=["Crustacés : allergène majeur."], keep="À manger tout de suite.", age=6, cats=[], fetes=["Noël", "Nouvel An", "Saint-Valentin"], profil=["poisson", "gras"], tech=["Décortiquer", "Griller"])
K("tourteau_mayonnaise", "Tourteau mayonnaise", "Tourteau", "France › Bretagne", "E", 2, 4, 30, 25, "€€", "Grande marmite, casse-noix, pique.",
  "Le gros crabe breton cuit au court-bouillon, décortiqué à table ou à l'avance : la chair blanche des pinces, le corail crémeux de la carapace, une mayonnaise et du pain de seigle.",
  ["2|tourteaux vivants (800 g)|Crabe / tourteau|3", f"35 g|de gros sel par litre d'eau|{SEL}|1", "1|bol de mayonnaise (fiche Mayonnaise)|SUB:mayonnaise|2", f"1|citron|{CIT}|1"],
  ["**Cuire.** Départ à l'eau froide très salée (il ne perd pas ses pattes), à ébullition puis 18 à 20 min de frémissement pour 800 g.",
   "**Refroidir.** Carapace en bas, 30 min.",
   "**Ouvrir.** Pattes et pinces détachées et cassées ; plastron soulevé, « doigts » gris (branchies) jetés ; chair blanche et partie crémeuse récupérées.",
   "**Servir.** Avec la mayonnaise, le citron, pain de seigle."],
  tips=["Crustacés : allergène majeur."], keep="1 jour au frigo (cuit).", age=3, cats=[], fetes=["Noël"], profil=["poisson"])
K("encornets_persillade", "Encornets sautés en persillade", "Encornets persillade", "France › Occitanie", "P", 1, 4, 15, 8, "€€", "Grande poêle.",
  "Des encornets nettoyés, taillés en anneaux, saisis à feu très vif deux minutes et enrobés d'ail et de persil : tendres s'ils sont saisis vite, caoutchouteux s'ils cuisent trop.",
  ["800 g|d'encornets nettoyés|Calamar / encornet|3", f"4|gousses d'ail|{AIL}|1", f"1|botte de persil|{PERSIL}|2", f"4 c. à s.|d'huile d'olive|{HO}|1", "1 pincée|de piment d'Espelette|Piment d'Espelette|1?", f"1|citron|{CIT}|1"],
  ["**Préparer.** Corps en anneaux, tentacules gardés ; très bien épongés (sinon ils bouillent).",
   "**Saisir.** Poêle fumante, huile, en deux fois, 2 min : opaques, légèrement dorés.",
   "**Persillade.** Ail et persil hachés, Espelette, 30 s.",
   "**Servir.** Citron, aussitôt."],
  tips=["Mollusques : allergène."], keep="À manger tout de suite.", age=3, cats=["express", "leger"], profil=["poisson", "leger"])
K("bulots_aioli", "Bulots, aïoli", "Bulots mayo", "France › Normandie", "E", 1, 4, 10, 30, "€", "Marmite.",
  "L'apéritif des ports normands : des bulots cuits dans un court-bouillon bien relevé, servis tièdes ou froids avec un aïoli ou une mayonnaise, à piquer avec une épingle.",
  ["1 kg|de bulots vivants|Bulots / bigorneaux|3", "1|court-bouillon (fiche Court-bouillon)|-|1", "1|bol d'aïoli (fiche Aïoli)|SUB:aioli_provencal|2"],
  ["**Dégorger.** Bulots 2 h dans l'eau froide salée, brossés, rincés.",
   "**Cuire.** Court-bouillon froid, à frémissement, 20 min (au-delà, ils durcissent) ; refroidis dans le bouillon.",
   "**Égoutter.**",
   "**Servir.** Avec l'aïoli et des piques."],
  tips=["Mollusques : allergène."], keep="2 jours au frigo.", age=3, cats=[], fetes=["Apéritif dînatoire"], profil=["poisson"])
