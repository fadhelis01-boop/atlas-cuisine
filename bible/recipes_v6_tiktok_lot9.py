# -*- coding: utf-8 -*-
"""Vague 9 (suite) · Plats végétariens ATLAS, jumeaux des favoris carnés du 04/11/2026 (orzo cajun, burger César,
ramen miso-curry, kebab maison) : ils gardent un tiers du catalogue sans viande ni poisson (audit UX 2026-10-16). Recettes
ATLAS, sans vidéo d'origine. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

K("orzo_one_pot_tomates_feta", "Orzo en une casserole aux tomates cerises, feta et basilic", "Orzo one pot", "Europe du Sud › Grèce", "P", 1, 4, 10, 20, "€", "Sauteuse avec couvercle.",
  "Le pendant végétarien de l'orzo au poulet : des pâtes langues d'oiseau cuites dans le bouillon avec des tomates cerises qui éclatent, finies avec de la feta qui fond à moitié, du citron et du basilic. Un dîner en 30 minutes, une seule casserole.",
  [f"300 g|d'orzo (langues d'oiseau)|{PATES}|3", "300 g|de tomates cerises|Tomate cerise|3", "150 g|de feta|Feta|2", "75 cl|de bouillon de légumes|Bouillon cube légumes|2", f"1|oignon et 2 gousses d'ail|{OIG}|1", "2|poignées d'épinards|Épinard|1", f"1|citron (zeste et jus)|{CIT}|2", "1|petit bouquet de basilic|Basilic|1", f"2 c. à s.|d'huile d'olive|{HO}|1", "1 pincée|de flocons de piment|Flocons de piment|1?"],
  ["**Base.** Huile, oignon émincé, 4 min : fondu ; ail, piment, 30 s ; orzo, 1 min : nacré.",
   "**Cuire.** Tomates cerises entières, bouillon chaud, sel ; couvert, 12 min à feu doux en remuant 2 fois : orzo tendre, tomates éclatées, presque plus de liquide.",
   "**Finir.** Épinards, 1 min : tombés ; zeste et jus de citron ; la moitié de la feta émiettée, mélangée : crémeux.",
   "**Servir.** Reste de feta, basilic, un filet d'huile d'olive."],
  keep="2 jours au frigo ; bon froid en salade.", age=1, cats=["vegetarien", "express", "enfants"], profil=["acide", "leger"])
K("burger_halloumi_croustillant", "Burger au halloumi croustillant, salade César végétarienne", "Halloumi burger", "Europe du Sud › Chypre", "P", 1, 4, 20, 10, "€€", "Poêle, 3 assiettes creuses.",
  "Le jumeau végétarien du burger César au poulet : d'épaisses tranches de halloumi panées au panko et dorées à la poêle (il ne fond pas, il croustille), une romaine à la sauce César sans anchois, parmesan et citron.",
  ["2|blocs de halloumi (2 × 250 g)|Halloumi|3", "4|pains burger|SUB:pains_burger|3", f"40 g|de farine|{F55}|1", f"1|œuf|{OEUF}|1", "80 g|de panko|Chapelure|2", "4 c. à s.|de mayonnaise|SUB:mayonnaise|2", f"1 c. à c.|de moutarde|{DIJON}|1", f"40 g|de parmesan (ou pecorino végétarien)|{PARM}|1", "1|cœur de romaine|Salade (laitue, batavia)|2", f"1/2|citron|{CIT}|2", f"4 c. à s.|d'huile|{HN}|1"],
  ["**Couper.** Halloumi en 4 tranches de 1,5 cm, séchées au papier absorbant.",
   "**Paner.** Farine, œuf battu, panko pressé.",
   "**Dorer.** 4 c. à s. d'huile, feu moyen, 2 min par face : panure dorée, cœur chaud et souple.",
   "**Sauce et monter.** Mayonnaise, moutarde, parmesan, jus de citron, 1 c. à s. d'eau ; romaine émincée enrobée ; pain toasté, sauce, halloumi, salade, poivre."],
  tips=["Le parmesan est fait avec de la présure animale : pour un repas strictement végétarien, prendre un fromage à pâte dure à présure végétale."],
  keep="Le jour même.", age=3, cats=["vegetarien", "enfants"], profil=["gras", "acide"])
K("ramen_miso_legumes_tofu", "Ramen miso au tofu grillé, champignons et pak-choï", "Miso ramen végétarien", "Asie de l'Est › Japon", "P", 1, 2, 20, 15, "€€", "Casserole, poêle.",
  "Un bol de ramen végétarien : un bouillon de légumes au miso, à l'ail et au gingembre, des nouilles, du tofu ferme grillé et laqué au soja, des champignons poêlés, du pak-choï et un œuf mollet.",
  ["2|portions de nouilles ramen|Nouilles ramen|3", "200 g|de tofu ferme|Tofu (ferme / soyeux)|3", "2 c. à s.|de miso blanc|Miso|2", "60 cl|de bouillon de légumes|Bouillon cube légumes|2", "150 g|de champignons (shiitake ou de Paris)|Shiitake|2", "2|pak-choï|Chou chinois / pak-choï|1", f"2|œufs|{OEUF}|1", f"2|gousses d'ail et 2 cm de gingembre|{GING}|1", f"2 c. à s.|de sauce soja|{SOJA}|1", "1 c. à c.|de vinaigre de riz|Vinaigre de riz|1", "1|cébette et 1 c. à c. d'huile de sésame|Oignon nouveau / cébette|1"],
  ["**Œufs.** 6 min 30 dans l'eau bouillante, eau glacée ; écalés.",
   "**Tofu.** Pressé 10 min, en tranches ; poêle chaude huilée, 3 min par face : doré ; 1 c. à s. de soja, 30 s : laqué.",
   "**Bouillon.** Ail et gingembre râpés, 1 min ; champignons, 4 min : dorés ; bouillon, pak-choï coupé en deux, 3 min ; hors du feu, miso délayé, soja, vinaigre de riz.",
   "**Servir.** Nouilles cuites 3 à 4 min, égouttées, dans les bols ; bouillon, légumes, tofu, œuf, cébette, sésame."],
  keep="Bouillon : 2 jours au frigo, nouilles à cuire au moment.", age=3, cats=["vegetarien"], profil=["acide"])
K("kebab_chou_fleur_epice", "Kebab de chou-fleur rôti aux épices, sauce blanche et pickles d'oignon", "Kebab végétarien", "France › Food fusion", "P", 1, 4, 20, 30, "€", "Plaque, papier cuisson.",
  "Le kebab sans viande : un chou-fleur en fines tranches rôti à four très chaud avec la marinade du kebab au poulet (yaourt, concentré de tomate, paprika, cumin), dans un pain pita avec sauce blanche, crudités et oignons rouges marinés.",
  ["1|chou-fleur|Chou-fleur|3", "4|pains pita (ou pains kebab maison)|Pain pita / libanais|3", f"100 g|de yaourt grec|{GREC}|2", f"1 c. à s.|de concentré de tomate|{CONC}|1", f"1 c. à c.|de paprika et de cumin|{PAPRIKA}|1", f"3 c. à s.|d'huile d'olive|{HO}|1", "4 c. à s.|de sauce blanche|SUB:sauce_blanche|2", "1|oignon rouge|Oignon rouge|1", "2 c. à s.|de vinaigre de cidre|Vinaigre de cidre|2", "1|salade et 2 tomates|Salade (laitue, batavia)|1"],
  ["**Pickles.** Oignon rouge en lamelles, vinaigre, pincée de sel : 20 min, il devient rose.",
   "**Mariner.** Chou-fleur en tranches de 1 cm et fleurettes, enrobé de yaourt, concentré, épices, huile, sel.",
   "**Rôtir.** Étalé sans se chevaucher, 25 à 30 min à 230 °C, retourné à mi-cuisson : bords noircis, cœur tendre à la pointe du couteau.",
   "**Monter.** Pita réchauffée, sauce blanche, chou-fleur, salade, tomate, pickles d'oignon."],
  keep="Chou-fleur rôti : 2 jours au frigo.", age=3, cats=["vegetarien", "enfants"], profil=["acide", "epice"])
