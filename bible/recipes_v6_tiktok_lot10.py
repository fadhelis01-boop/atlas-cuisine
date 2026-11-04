# -*- coding: utf-8 -*-
"""Vague 9 (fin) · Auteurs des favoris du 04/11/2026 qu'on a pu lire (@zoyacooks7, @sosoya06 ; TikTok a bloqué les
listes des autres profils ce jour-là). Fiches réécrites et créditées, plus un jumeau végétarien. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *
from recipes_v6_tiktok_plats import C

K("hot_honey_chicken_burger", "Burger de poulet croustillant au « hot honey » (miel pimenté), mayo à l'ail", "Hot honey chicken burger", "Amérique du Nord › États-Unis", "P", 2, 4, 30, 20, "€€", "Casserole à friture, thermomètre, petite casserole.",
  "Une des vidéos les plus enregistrées de @zoyacooks7 : du poulet mariné au lait ribot pimenté, pané deux fois (farine et fécule) pour une croûte très craquante, frit puis enrobé d'un glaçage beurre-miel-sauce piquante, avec une mayonnaise à l'ail et des pickles.",
  [f"500 g|de blancs de poulet en 4 escalopes|{BLANC_P}|3", "4|pains burger|SUB:pains_burger|3", f"30 cl|de lait (+ 1 c. à s. de vinaigre blanc : lait ribot)|{LAIT}|2", f"1|œuf|{OEUF}|1", f"150 g|de farine|{F55}|2", "150 g|de fécule de maïs|Fécule de maïs (maïzena)|2", f"1 c. à s.|de paprika (+ ail et oignon en poudre)|{PAPRIKA}|1", "4 c. à s.|de sauce piquante (type sriracha)|Sriracha|2", f"3 c. à s.|de miel|{MIEL}|2", f"60 g|de beurre|{BEURRE}|1", "6 c. à s.|de mayonnaise à l'ail (mayonnaise + 1 gousse râpée + citron)|SUB:mayonnaise|2", "8|rondelles de cornichon|Cornichon|1", f"1 l|d'huile de friture|{HN}|1"],
  ["**Mariner.** Lait, vinaigre, 2 c. à s. de sauce piquante, œuf, épices, sel ; poulet dedans, 30 à 40 min.",
   "**Paner deux fois.** Farine, fécule et épices mélangées ; poulet dans la panure, retrempé dans la marinade, de nouveau dans la panure en pressant : croûte épaisse et écailleuse.",
   "**Frire.** 6 à 7 min à 170 °C : doré foncé, 74 °C à cœur ; sur une grille.",
   "**Glacer.** Beurre fondu, miel, reste de sauce piquante, 1 min à frémir : sirop brillant ; poulet enrobé au pinceau, un peu gardé pour les pains.",
   "**Monter.** Pain toasté, mayo à l'ail, poulet, cornichons ; dessus du pain badigeonné de glaçage."],
  keep="Le jour même.", age=6, cats=[], profil=["gras", "sucre", "epice", "acide"], tech=["Frire en sécurité"],
  credit=C(("@zoyacooks7", "https://www.tiktok.com/@zoyacooks7/video/7697673481445510432")))
K("frites_chargees_poulet", "Frites chargées au poulet, fromage fondu et sauce burger épicée", "Loaded fries", "Europe du Nord › Royaume-Uni", "P", 1, 3, 25, 35, "€", "Plaque, poêle, bol.",
  "Le plat qu'on commande d'habitude au snack, à la maison : des frites au four, des tranches de fromage fondues dessus, des aiguillettes de poulet dorées, oignon et cébette, et une sauce mayonnaise-ketchup-chili-moutarde bien relevée et citronnée.",
  [f"800 g|de pommes de terre|{PDT}|3", f"4|aiguillettes de poulet|{BLANC_P}|3", "4|tranches de cheddar|Cheddar|2", "6 c. à s.|de mayonnaise|SUB:mayonnaise|2", "1 c. à s.|de ketchup|Ketchup|1", "1 c. à s.|de sriracha (+ 1 c. à s. de sauce chili douce)|Sriracha|1", f"1 c. à s.|de moutarde|{DIJON}|1", f"1/2|citron|{CIT}|2", f"1|petit oignon et 1 cébette|{OIG}|1", f"1/2|bouquet de coriandre ou de persil|{CORI}|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Frites.** Pommes de terre en bâtonnets, rincées et séchées, 2 c. à s. d'huile, sel ; 30 à 35 min à 220 °C, retournées à mi-cuisson : dorées et croustillantes.",
   "**Poulet.** Salé, paprika, 3 min par face à la poêle chaude : doré, 74 °C à cœur ; en morceaux.",
   "**Sauce.** Mayonnaise, ketchup, sriracha, chili doux, moutarde, jus de citron, sel, poivre : rose et relevée.",
   "**Charger.** Fromage sur les frites chaudes, 2 min au four : fondu ; poulet, oignon haché fin, cébette, sauce en filets, herbes."],
  keep="Le jour même.", age=6, cats=[], profil=["gras", "epice", "acide"],
  credit=C(("@zoyacooks7", "https://www.tiktok.com/@zoyacooks7/video/7585263872601230614")))
K("frites_chargees_haricots", "Frites chargées végétariennes (haricots rouges épicés, cheddar, avocat)", "Loaded fries végétariennes", "Europe du Nord › Royaume-Uni", "P", 1, 3, 20, 35, "€", "Plaque, casserole.",
  "Le jumeau végétarien des frites chargées : des frites au four couvertes de cheddar fondu, de haricots rouges mijotés au cumin et au paprika fumé, d'un avocat écrasé au citron vert et d'oignon rouge mariné.",
  [f"800 g|de pommes de terre|{PDT}|3", "1|boîte de haricots rouges (400 g)|Haricots rouges / noirs|3", "100 g|de cheddar râpé|Cheddar|2", "1|avocat|Avocat|2", f"1|citron vert|{CITV}|2", "1/2|oignon rouge|Oignon rouge|1", f"1 c. à c.|de cumin et de paprika fumé|{CUMIN}|1", f"3 c. à s.|de coulis de tomate|{PELEES}|1", f"1/2|bouquet de coriandre|{CORI}|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Frites.** Bâtonnets rincés et séchés, huile, sel ; 30 à 35 min à 220 °C, retournés à mi-cuisson : dorés.",
   "**Haricots.** Égouttés, 1 c. à s. d'huile, épices 30 s, coulis, 8 min à petit feu : ils épaississent et s'écrasent un peu.",
   "**Garnitures.** Avocat écrasé avec la moitié du citron vert et du sel ; oignon rouge émincé dans le reste du jus, 10 min.",
   "**Charger.** Cheddar sur les frites, 2 min au four : fondu ; haricots, avocat, oignon, coriandre."],
  keep="Le jour même.", age=3, cats=["vegetarien", "enfants"], profil=["acide", "epice"])
K("carrot_cake_mascarpone", "Carrot cake aux noix, glaçage mascarpone (façon coffee-shop)", "Carrot cake", "Amérique du Nord › États-Unis", "G", 1, 10, 25, 45, "€€", "Moule à cake ou carré de 22 cm, râpe, batteur.",
  "Le carrot cake des coffee-shops : moelleux, épicé à la cannelle, plein de carottes râpées, de poudre d'amande et de noix, et couvert d'un glaçage au mascarpone et à la vanille.",
  [f"250 g|de carottes râpées fin|{CAROTTE}|3", f"3|œufs|{OEUF}|2", f"120 g|de sucre roux|{SUCRE}|2", f"15 cl|d'huile de tournesol|{HN}|2", f"150 g|de farine|{F55}|2", "50 g|de poudre d'amande|Amande (entière, effilée, poudre)|1", f"1|sachet de levure chimique|{LEVC}|1", f"2 c. à c.|de cannelle|{CANN}|1", "100 g|de cerneaux de noix (ou de pécan)|Noix|2", "250 g|de mascarpone|Mascarpone|2", f"50 g|de sucre glace|Sucre glace|1", f"1/2 c. à c.|de vanille en poudre|{VAN}|1", f"1/2|citron (zeste)|{CIT}|1"],
  ["**Pâte.** Œufs et sucre fouettés 2 min : mousseux ; huile en filet ; farine, amande, levure, cannelle, pincée de sel ; carottes et noix concassées.",
   "**Cuire.** Moule chemisé, 40 à 50 min à 180 °C : brun doré, lame qui ressort sèche ; refroidi complètement sur une grille (sinon le glaçage coule).",
   "**Glaçage.** Mascarpone froid, sucre glace, vanille, zeste, 1 min au batteur : ferme et lisse ; 15 min au frais.",
   "**Finir.** Étalé en vagues sur le gâteau, noix dessus ; au frais."],
  tips=["L'arôme de vanille liquide contient de l'alcool : vanille en poudre ou sucre vanillé à la place."],
  keep="4 jours au frigo.", age=1, cats=["enfants"], fetes=["Anniversaire"], profil=["sucre"],
  credit=C(("@sosoya06", "https://www.tiktok.com/@sosoya06/video/7690134976435604768")))
