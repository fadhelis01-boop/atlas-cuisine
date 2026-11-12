# -*- coding: utf-8 -*-
"""Audit « fin gourmet, cuisine française » (12/11/2026), suite : les derniers classiques absents (lièvre, sanglier,
faisan, pithiviers, sauces diable et charcutière). Réécrits avec les repères ATLAS. NON TESTÉS (Tome 7 §2)."""
from recipes_v2_base import *

VR = ("Sans alcool", ["alcohol"], {"Vin rouge": [("Bouillon d'os maison (bœuf/volaille)", 0.5), ("Jus de raisin / pomme (pur jus)", 0.4), ("Vinaigre de vin rouge / blanc", 0.05)]},
      "Vin rouge → **bouillon + jus de raisin + un trait de vinaigre**. **À tester**.")
VB = ("Sans alcool", ["alcohol"], {"Vin blanc": [("Bouillon d'os maison (bœuf/volaille)", 0.8), ("Vinaigre de cidre", 0.05)]}, "Vin blanc → **bouillon + 1 c. à c. de vinaigre de cidre**. **À tester**.")
ECHA = "Échalote"

K("civet_lievre", "Civet de lièvre (sauce liée au foie et au chocolat noir)", "Civet de lièvre", "France › Centre-Val de Loire", "P", 3, 6, 40, 1620, "€€€", "Grande cocotte.",
  "Le plat de chasse le plus réputé de Sologne : le lièvre mariné au vin rouge, mijoté longuement, la sauce liée (traditionnellement au sang, ici au foie mixé et au chocolat noir), avec des lardons et des champignons.",
  ["1|lièvre découpé (2,5 kg), avec le foie|-|3", "75 cl|de vin rouge corsé|Vin rouge|3", "150 g|de lardons|Lardons|2", "250 g|de champignons|Champignon de Paris|2", f"2|oignons|{OIG}|1", f"2|carottes|{CAROTTE}|1", "1|bouquet garni|Laurier|1", f"2 c. à s.|de farine|{F55}|1", f"30 g|de chocolat noir|{CHOCO}|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Mariner (la veille).** Morceaux, vin, oignons et carottes en rondelles, bouquet ; 24 h au frais ; foie gardé à part, filmé.",
   "**Saisir.** Morceaux égouttés, épongés, dans l'huile fumante, en plusieurs fois : bien bruns ; lardons dorés ; singer (farine, 1 min).",
   "**Mijoter.** Marinade bouillie et écumée versée dessus, sel ; feu doux 2 h 30 à 3 h : la chair se détache ; champignons poêlés en fin.",
   "**Lier.** Foie mixé avec une louche de sauce, puis chocolat râpé, hors du feu en tournant, sans bouillir : sauce brune, brillante, nappante."],
  tips=["Le civet est encore meilleur le lendemain.", "Commande le lièvre chez un volailler-gibier, en saison de chasse (automne)."],
  var=[VR, ("Sans porc", ["pork"], {"Lardons": [("Lardons de dinde / de volaille fumés", 1.0)]}, "Lardons → **lardons de dinde fumés**. **À tester**.")],
  keep="3 jours au frigo ; se congèle.", age=None, kids="✓ dès 6 ans en version sans alcool.", fetes=["Noël", "Repas de famille"], profil=["viande_rouge"], tech=["Mariner", "Lier à la farine", "Mijoter"])
K("daube_sanglier", "Daube de sanglier aux cèpes", "Daube de sanglier", "France › Corse", "P", 2, 6, 40, 1620, "€€€", "Grande cocotte.",
  "Le sanglier de Corse et des Cévennes : épaule marinée au vin rouge avec genièvre et aromates, mijotée des heures avec des cèpes, jusqu'à ce que la viande fonde. Avec une polenta ou des pâtes fraîches.",
  ["1,5 kg|d'épaule de sanglier en morceaux|Sanglier|3", "75 cl|de vin rouge corsé|Vin rouge|3", "300 g|de cèpes (frais, surgelés, ou 40 g secs)|Cèpe / girolle / morille|2", f"2|oignons|{OIG}|1", f"2|carottes|{CAROTTE}|1", f"4|gousses d'ail|{AIL}|1", "8|baies de genièvre|Baies de genièvre|1", "1|bouquet garni|Laurier|1", f"2 c. à s.|de concentré de tomate|{CONC}|1", f"3 c. à s.|d'huile d'olive|{HO}|1"],
  ["**Mariner.** Viande, vin, légumes, ail, genièvre écrasé, bouquet ; 24 h au frais.",
   "**Saisir.** Viande épongée, huile fumante, en plusieurs fois : bien brune ; concentré, 1 min.",
   "**Mijoter.** Marinade bouillie et écumée, sel ; feu très doux 3 h : la viande s'écrase à la fourchette.",
   "**Cèpes.** Poêlés à l'huile, ajoutés les 30 dernières minutes ; sauce réduite à la nappe."],
  tips=["Le sanglier se cuit toujours à cœur (mijoté long) : le gibier sauvage peut porter des parasites."], var=[VR],
  keep="3 jours au frigo ; se congèle.", age=None, kids="✓ dès 3 ans en version sans alcool.", fetes=["Repas de famille", "Noël"], profil=["viande_rouge"], tech=["Mariner", "Mijoter"])
K("faisan_chou_cocotte", "Faisan en cocotte aux raisins et au chou", "Faisan en cocotte", "France › Hauts-de-France", "P", 2, 4, 30, 70, "€€€", "Cocotte.",
  "Le faisan, maigre et parfumé, doré puis cuit à couvert pour rester moelleux, avec des raisins frais et un chou braisé. Le plat de chasse le plus doux.",
  ["1|faisan (1,2 kg) prêt à cuire|-|3", "1|petit chou vert|Chou vert / frisé / kale|2", "250 g|de raisins blancs|Raisin|2", f"40 g|de beurre|{BEURRE}|2", f"20 cl|de fond de volaille|{BOUILLON}|1", f"1|oignon|{OIG}|1", "4|baies de genièvre|Baies de genièvre|1?", f"1/2|citron|{CIT}|1"],
  ["**Brider.** Faisan salé, bridé, enveloppé d'une feuille de chou blanchie : il ne sèche pas.",
   "**Dorer.** Cocotte, beurre, 10 min sur toutes les faces ; réservé ; oignon, chou blanchi en lanières, genièvre, fond.",
   "**Cuire.** Faisan sur le chou, couvert, four 180 °C 45 min : cuisses à 75 °C, blancs encore juteux ; 10 min de repos.",
   "**Raisins.** Dans la cocotte 5 min : brillants ; un trait de citron ; faisan découpé sur le chou, raisins et jus autour."],
  keep="2 jours au frigo.", age=3, cats=[], fetes=["Repas de famille", "Noël"], profil=["leger", "sucre"], tech=["Rôtir"])
K("pithiviers_amandes", "Pithiviers (feuilleté à la crème d'amande)", "Pithiviers", "France › Centre-Val de Loire", "D", 2, 8, 30, 45, "€€", "Plaque, pinceau, couteau.",
  "Le gâteau de la ville de Pithiviers, ancêtre de la galette des rois : deux disques de pâte feuilletée enfermant une crème d'amande, dorés et rayés en rosace.",
  ["2|pâtes feuilletées (pur beurre)|Pâte feuilletée (prête)|3", "100 g|de poudre d'amande|Amande (entière, effilée, poudre)|3", f"100 g|de beurre mou|{BEURRE}|2", f"100 g|de sucre|{SUCRE}|2", f"2|œufs + 1 jaune (dorure)|{OEUF}|2", "2 cl|de rhum (facultatif)|Rhum ambré / blanc|1?"],
  ["**Crème d'amande.** Beurre mou et sucre fouettés, œufs un à un, poudre d'amande, rhum : crème lisse ; 30 min au frais.",
   "**Monter.** Un disque sur plaque, crème en dôme à 3 cm du bord, bord mouillé, second disque soudé en chassant l'air ; bord chiqueté (petites entailles au dos d'un couteau).",
   "**Décorer.** Dorure, 20 min au frais, seconde dorure ; rosace tracée de la pointe du couteau du centre vers le bord, sans percer ; une cheminée au centre.",
   "**Cuire.** Four 190 °C 35 à 40 min : gonflé, doré profond ; tiède."],
  tips=["Fruits à coque (amandes) : allergène majeur."], var=[("Sans alcool", ["alcohol"], {"Rhum ambré / blanc": [("Poudre de vanille", 0.1)]}, "Rhum → **vanille ou eau de fleur d'oranger**. **À tester**.")],
  keep="2 jours, réchauffé 10 min au four.", age=2, cats=["vegetarien", "fetes"], fetes=["Épiphanie", "Repas de famille"], profil=["sucre", "gras"], tech=["Feuilletage"])
K("sauce_diable", "Sauce diable (échalote, vinaigre, poivre)", "Sauce diable", "France › Sauces", "S", 1, 4, 10, 20, "€", "Casserole.",
  "Une sauce brune relevée pour les volailles grillées et les restes de viande : échalote et vinaigre réduits à sec, fond brun, une pointe de cayenne et de moutarde.",
  [f"2|échalotes|{ECHA}|2", "5 cl|de vinaigre de vin|Vinaigre de vin rouge / blanc|2", "25 cl|de fond brun (fiche Fond brun)|SUB:fond_brun_veau|3", f"1 pincée|de cayenne|{CAYENNE}|1", f"1 c. à c.|de moutarde|{DIJON}|1", f"20 g|de beurre froid|{BEURRE}|1"],
  ["**Réduire.** Échalotes ciselées, vinaigre, poivre concassé : réduit à sec.",
   "**Mouiller.** Fond brun, 10 min : nappant.",
   "**Relever.** Cayenne, moutarde, hors du feu.",
   "**Monter.** Beurre froid en tournant : brillante ; sur un poulet grillé ou des tranches de bœuf."],
  keep="3 jours au frigo.", age=6, cats=["sauces"], profil=["epice", "acide"], tech=["Réduire", "Monter au beurre"])
K("sauce_charcutiere", "Sauce charcutière (moutarde et cornichons)", "Sauce charcutière", "France › Sauces", "S", 1, 4, 10, 20, "€", "Casserole.",
  "La sauce brune piquante des côtes de porc et des saucisses grillées : oignon et vin blanc réduits, fond brun, moutarde et cornichons en julienne. Aussi bonne avec du veau ou de la volaille.",
  [f"1|oignon|{OIG}|2", "10 cl|de vin blanc|Vin blanc|2", "25 cl|de fond brun (fiche Fond brun)|SUB:fond_brun_veau|3", f"1 c. à s.|de moutarde forte|{DIJON}|2", "6|cornichons|Cornichon|2", f"20 g|de beurre|{BEURRE}|1"],
  ["**Fondre.** Oignon ciselé, beurre, 5 min : blond.",
   "**Réduire.** Vin blanc, réduit de moitié.",
   "**Mouiller.** Fond brun, 10 min : nappant.",
   "**Finir.** Hors du feu (la moutarde ne doit pas bouillir) : moutarde, cornichons en julienne."],
  var=[VB], keep="3 jours au frigo.", age=3, cats=["sauces"], profil=["acide"], tech=["Réduire"])
