# -*- coding: utf-8 -*-
"""Audit des manques TikTok (13/11/2026, §5 priorité 4, tendances virales) et correctif de part végétarienne : les
fiches carnées ajoutées aux priorités 2 et 3 (sisig, lechon, kare-kare, asado, bangers and mash, haggis, bandeja
paisa, completo italiano) ont fait baisser la part de plats végétariens sous le seuil mesuré (test 63, ≥ 33 %).
Ces 4 fiches la rétablissent, et sont elles-mêmes des classiques très vus sur TikTok. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

GR = "Europe du Sud › Grèce"; CN = "Asie de l'Est › Chine"; MA = "Afrique du Nord › Maghreb"; IN = "Asie du Sud › Inde"
FETA = "Feta"; TOMCERISE = "Tomate cerise"; EPINARD = "Épinard"

K("pates_feta_au_four", "Pâtes au four feta et tomates cerises (baked feta pasta)", "Baked feta pasta", GR, "P", 1, 4, 10, 30, "€€",
  "Plat à gratin, casserole.",
  "Le plat devenu viral sur TikTok en une nuit : un bloc de feta entier noyé de tomates cerises et d'huile d'olive, "
  "rôti au four jusqu'à ce que les tomates éclatent et que la feta fonde en crème, mélangé ensuite à des pâtes "
  "chaudes pour une sauce instantanée sans avoir touché une casserole de sauce.",
  [f"400 g|de pâtes courtes (penne, fusilli)|{PATES}|3", f"400 g|de tomates cerises|{TOMCERISE}|3",
   f"200 g|de feta, en un seul bloc|{FETA}|3", f"6 c. à s.|d'huile d'olive|{HO}|2", f"3 gousses|d'ail, écrasées|{AIL}|1",
   f"1 c. à c.|de flocons de piment (facultatif)|{CAYENNE}|1?", "1|petit bouquet de basilic|Basilic|1",
   f"-|sel, poivre|{SEL}|1"],
  ["**Préparer.** Four à 200 °C. Tomates cerises et ail dans un plat à gratin, arrosés d'huile d'olive, salés et "
   "poivrés ; bloc de feta posé entier au centre, arrosé lui aussi d'huile et de piment.",
   "**Rôtir.** 25 à 30 min : les tomates éclatent et rendent leur jus, la feta se colore et devient crémeuse en "
   "surface tout en restant ferme à l'intérieur.",
   "**Pâtes.** Cuites al dente pendant ce temps, dans une eau bien salée ; 15 cl d'eau de cuisson réservés.",
   "**Mélanger.** Feta écrasée à la fourchette directement dans son plat chaud pour qu'elle se défasse en crème "
   "avec les tomates et l'huile ; pâtes égouttées versées dedans avec un peu d'eau de cuisson, bien mélangées "
   "jusqu'à ce que la sauce nappe chaque pâte.",
   "**Servir.** Basilic ciselé par-dessus, aussitôt."],
  tips=["Le plat doit être assez profond pour que l'huile ne déborde pas à la cuisson.",
        "Sans basilic frais, du persil plat fait très bien l'affaire."],
  keep="2 jours au frigo ; se réchauffe à la poêle avec un peu d'eau.", age=2, kids="✓ dès 2 ans.",
  cats=["enfants", "vegetarien", "express"], profil=["gras", "acide"])
K("nouilles_a_lail", "Nouilles à l'ail façon TikTok (beurre, ail doré, soja et parmesan)", "Garlic noodles", CN, "P", 1, 4, 10, 10, "€",
  "Grande poêle ou wok.",
  "Le plat d'accompagnement devenu plat à part entière sur TikTok : des nouilles enrobées d'un beurre à l'ail "
  "longuement doré, relevé de sauce soja et d'un nuage de parmesan, prêt en moins de 20 minutes.",
  [f"350 g|de nouilles chinoises fraîches ou de spaghetti|{PATES}|3", f"60 g|de beurre|{BEURRE}|2",
   f"8 gousses|d'ail, hachées très fin|{AIL}|3", f"3 c. à s.|de sauce soja|{SOJA}|2", f"1 c. à c.|de sucre|{SUCRE}|1",
   f"1 c. à c.|de vinaigre de riz|Vinaigre de riz|1", f"40 g|de parmesan râpé|{PARM}|2",
   f"2|cébettes, ciselées|Oignon nouveau / cébette|1"],
  ["**Nouilles.** Cuites selon le paquet, égouttées, 10 cl d'eau de cuisson réservés.",
   "**Ail doré.** Beurre fondu à feu doux dans une grande poêle ; ail haché ajouté, 4 à 5 min en remuant sans "
   "arrêt : il doit dorer tout doucement et parfumer sans jamais brunir ni amérir.",
   "**Sauce.** Soja, sucre et vinaigre de riz ajoutés, 30 secondes.",
   "**Mélanger.** Nouilles versées dans la poêle avec un peu d'eau de cuisson, bien enrobées ; parmesan incorporé "
   "hors du feu, il doit fondre en crème légère sans grumeaux.",
   "**Servir.** Cébettes ciselées par-dessus, aussitôt, bien chaud."],
  tips=["L'ail brûlé devient amer et gâche tout le plat : feu doux et on ne le quitte pas des yeux.",
        "Avec des lamelles de poulet ou de tofu sautées à part, posées dessus, ça devient un repas complet."],
  keep="À manger aussitôt (les nouilles collent en refroidissant).", age=2, kids="✓ dès 2 ans.",
  cats=["enfants", "vegetarien", "express"], profil=["gras"])
K("saag_paneer", "Saag paneer (épinards aux épices et dés de fromage frais indien)", "साग पनीर", IN, "P", 1, 4, 20, 20, "€€",
  "Mixeur ou blender, sauteuse.",
  "Le classique végétarien des restaurants indiens : une purée d'épinards aux épices chaudes, légèrement crémée, "
  "dans laquelle on fait juste tiédir des dés de paneer doré. Avec du riz ou une naan pour saucer.",
  [f"800 g|d'épinards frais (ou 500 g surgelés)|{EPINARD}|3", f"250 g|de paneer, en dés|Paneer|3",
   f"1|oignon, haché|{OIG}|1", f"3 gousses|d'ail, hachées|{AIL}|1", f"2 cm|de gingembre frais, haché|{GING}|1",
   f"1 c. à c.|de cumin|{CUMIN}|1", f"1 c. à c.|de curcuma|{CURC}|1", f"1/2 c. à c.|de cayenne|{CAYENNE}|1?",
   f"4 c. à s.|de crème fraîche (facultatif)|{CF}|1?", f"3 c. à s.|de ghee ou d'huile|{HN}|1", f"-|sel|{SEL}|1"],
  ["**Épinards.** Lavés, blanchis 2 min à l'eau bouillante (ou décongelés), égouttés et mixés grossièrement : une "
   "purée épaisse avec encore un peu de texture.",
   "**Paneer doré.** Dés de paneer dorés 3 à 4 min à la poêle avec un peu de ghee, sur toutes les faces ; réservés.",
   "**Base.** Reste du ghee ; oignon, ail et gingembre fondus 6 min ; épices ajoutées 1 min, le temps qu'elles "
   "embaument.",
   "**Réunir.** Épinards mixés versés dans la poêle, 5 min à feu doux ; crème fraîche incorporée si utilisée ; "
   "sel ajusté.",
   "**Finir.** Dés de paneer remis dans les épinards, 3 min juste pour les tiédir sans qu'ils durcissent."],
  tips=["Le paneer devient caoutchouteux s'il cuit trop longtemps dans la sauce : on l'y remet juste à la fin.",
        "Sans paneer trouvé : la recette maison de paneer (fromage frais pressé) est rapide et déjà dans l'appli."],
  keep="3 jours au frigo.", age=1, kids="✓ dès 1 an.", cats=["enfants", "vegetarien"], profil=["epice", "gras"],
  tech=["Faire un fromage frais maison (chenna, paneer, ricotta express)"])
