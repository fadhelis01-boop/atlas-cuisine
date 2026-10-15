# -*- coding: utf-8 -*-
"""Sujets à illustrer et requêtes de recherche (Wikimedia Commons, Openverse).
Chaque sujet : id → (type, [requêtes]). Les requêtes anglaises trouvent souvent de meilleures photos sur Flickr."""

RECIPES = {
 "tajine_poulet_olives": ["tajine poulet olives citron confit", "chicken tagine olives preserved lemon"],
 "poulet_yassa": ["poulet yassa", "chicken yassa senegal"],
 "dal_tadka": ["dal tadka", "red lentil dal"],
 "spaghetti_carbonara": ["spaghetti carbonara", "carbonara pasta"],
 "boeuf_bourguignon": ["boeuf bourguignon", "beef bourguignon"],
 "pad_thai": ["pad thai shrimp", "pad thai"],
 "ratatouille": ["ratatouille", "ratatouille provencal"],
 "baguette_24h": ["baguette tradition pain", "french baguettes bread"],
 "mayonnaise": ["mayonnaise maison", "homemade mayonnaise bowl"],
 "sauce_algerienne": ["sauce algérienne", "spicy mayonnaise sauce bowl"],
 "crepes_bretonnes": ["crêpes bretonnes", "french crepes"],
 "pain_cocotte": ["no knead bread dutch oven", "pain cocotte"],
 "pate_pizza": ["pizza dough balls", "pâte à pizza"],
 "pizza_margherita": ["pizza margherita", "margherita pizza napoletana"],
 "naan": ["naan bread", "garlic naan"],
 "pain_pita": ["pita bread", "pain pita"],
 "focaccia": ["focaccia rosemary", "focaccia genovese"],
 "msemen": ["msemen", "meloui msemen moroccan"],
 "batbout": ["batbout", "moroccan batbout bread"],
 "galette_complete": ["galette complète sarrasin", "galette bretonne buckwheat egg ham"],
 "pancakes": ["pancakes stack", "american pancakes"],
 "pain_de_mie": ["pain de mie", "white sandwich bread loaf"],
 "brioche": ["brioche", "brioche loaf"],
 "pate_brisee": ["pâte brisée", "shortcrust pastry tart shell"],
 "chapati": ["chapati", "roti chapati"],
 "tortillas_ble": ["flour tortillas", "tortillas de harina"],
 "ketchup": ["homemade ketchup", "ketchup bowl"],
 "sauce_samourai": ["sauce samouraï", "sriracha mayonnaise"],
 "sauce_blanche": ["sauce blanche kebab yaourt", "garlic yogurt sauce"],
 "sauce_burger": ["burger sauce", "big mac sauce"],
 "sauce_barbecue": ["barbecue sauce", "bbq sauce bowl"],
 "sauce_andalouse": ["sauce andalouse", "andalouse sauce"],
 "harissa": ["harissa", "harissa paste"],
 "pesto": ["pesto genovese", "basil pesto mortar"],
 "sauce_tomate": ["sauce tomate maison", "tomato sauce pot basil"],
 "bechamel": ["béchamel", "bechamel sauce"],
 "vinaigrette": ["vinaigrette", "vinaigrette dressing"],
 "tzatziki": ["tzatziki", "tzatziki greek"],
 "frites_maison": ["frites belges", "french fries"],
 "bouillon_volaille": ["bouillon de poule", "chicken stock pot"],
 "bouillon_legumes": ["bouillon de légumes", "vegetable broth"],
 "mafe_poulet": ["mafé", "maafe peanut stew"],
 "chorba": ["chorba frik", "chorba soup"],
 "salade_carottes_cumin": ["salade de carottes marocaine", "moroccan carrot salad"],
 "houmous": ["houmous", "hummus plate"],
 "taboule_libanais": ["taboulé libanais", "tabbouleh"],
 "shakshuka": ["chakchouka", "shakshuka"],
 "riz_cantonais": ["riz cantonais", "yangzhou fried rice"],
 "poulet_teriyaki": ["poulet teriyaki", "chicken teriyaki"],
 "chili_con_carne": ["chili con carne", "chili con carne bowl"],
 "guacamole": ["guacamole", "guacamole molcajete"],
 "accras_morue": ["accras de morue", "accras"],
 "quiche_lorraine": ["quiche lorraine", "quiche"],
 "gratin_dauphinois": ["gratin dauphinois", "potatoes au gratin"],
 "veloute_potiron": ["velouté de potiron", "pumpkin soup"],
 "poulet_roti": ["poulet rôti", "roast chicken"],
 "mousse_chocolat": ["mousse au chocolat", "chocolate mousse"],
 "meringues": ["meringues", "meringue cookies"],
 "pain_perdu": ["pain perdu", "french toast"],
 "banana_bread": ["banana bread", "banana bread loaf"],
 "tiramisu": ["tiramisu", "tiramisu dessert"],
 "gateau_yaourt": ["gâteau au yaourt", "yogurt cake"],
 "oranges_cannelle": ["oranges cannelle", "orange salad cinnamon"],
 "riz_au_lait": ["riz au lait", "rice pudding"],
 "galette_rois": ["galette des rois", "galette des rois frangipane"],
 "bissap": ["bissap", "hibiscus drink"],
 "citronnade_menthe": ["citronnade menthe", "mint lemonade"],
 "lassi_mangue": ["mango lassi", "lassi mangue"],
 "the_menthe": ["thé à la menthe", "moroccan mint tea"],
 "jus_gingembre": ["jus de gingembre", "ginger juice drink"],
}

TECHNIQUES = {
 "tenir-couteau": ["chef knife cutting board", "chopping vegetables knife"],
 "ciseler-oignon": ["dicing onion", "chopped onion cutting board"],
 "ciseler-herbes": ["chopping herbs", "chopped parsley"],
 "emincer": ["julienne vegetables", "sliced vegetables cutting board"],
 "saisir": ["searing meat pan", "seared steak pan"],
 "faire-revenir": ["sauteing onions", "onions frying pan"],
 "deglacer": ["deglazing pan", "pan sauce"],
 "mijoter": ["dutch oven stew", "braising pot"],
 "rotir-volaille": ["roast chicken oven", "roasted chicken tray"],
 "cuire-pates": ["boiling pasta pot", "cooking spaghetti"],
 "cuire-riz": ["cooked rice pot", "steamed rice bowl"],
 "emulsionner": ["whisking mayonnaise", "whisk bowl emulsion"],
 "roux-bechamel": ["roux pan butter flour", "white sauce whisk"],
 "reduire": ["sauce reduction pan", "simmering sauce"],
 "bouillon": ["stock pot vegetables", "making broth"],
 "oeufs-cuissons": ["boiled eggs", "soft boiled egg"],
 "separer-oeuf": ["egg whites whipped", "beaten egg whites"],
 "incorporer": ["folding batter spatula", "folding egg whites"],
 "bain-marie": ["melting chocolate bowl", "bain marie chocolate"],
 "pate-brisee": ["rolling pastry dough", "tart dough rolling pin"],
 "pate-crepes": ["crepe pan cooking", "making crepes"],
 "petrir": ["kneading dough", "bread dough hands"],
 "pointage": ["proofing dough bowl", "risen dough"],
 "faconner": ["shaping bread dough", "shaping baguette"],
 "vapeur-four": ["scoring bread", "bread oven baking"],
 "poele-tres-chaude": ["flatbread pan cooking", "naan cast iron"],
 "frire": ["deep frying", "frying pan oil"],
 "torrefier": ["toasting spices pan", "whole spices"],
 "infuser": ["tea infusion", "hibiscus tea infusion"],
 "degorger-dessaler": ["peeled orange segments", "citrus supreme"],
 "securite-temperatures": ["meat thermometer", "food thermometer"],
 "laquer-cuisson-peau": ["crispy chicken skin pan", "glazed chicken"],
 "wok": ["wok stir fry", "stir fry flames"],
}

REGIONS = {
 "france": ["french cuisine table", "cuisine française plat"], "europe_sud": ["italian food table", "mediterranean food"],
 "europe_nord": ["german bread bakery", "scandinavian food"], "maghreb": ["moroccan food table", "couscous"],
 "afrique": ["senegalese food", "jollof rice"], "moyen_orient": ["mezze", "lebanese mezze"],
 "asie_sud": ["indian thali", "indian curry"], "asie_est": ["japanese food", "dim sum"],
 "asie_sud_est": ["thai food", "vietnamese pho"], "amerique_nord": ["american barbecue", "burger"],
 "amerique_latine": ["mexican tacos", "mexican food"], "oceanie": ["pavlova", "new zealand food"],
 "fusion": ["fusion cuisine", "korean tacos"],
}

RUBRIQUES = {
 "pains": ["bakery bread loaves", "artisan bread"], "sauces": ["sauces bowls", "condiments"], "enfants": ["children cooking", "kids baking"],
 "fetes": ["festive dinner table", "christmas dinner table"], "zero_dechet": ["vegetable scraps compost", "leftovers"],
 "techniques": ["chef cooking kitchen", "cooking class"], "imports": ["smartphone recipe kitchen", "food video phone"],
 "frigo": ["open refrigerator vegetables", "fresh vegetables market"], "explorer": ["spices market", "world spices"],
}

FETES = {
 "epiphanie": ["galette des rois"], "chandeleur": ["crêpes chandeleur", "crepes stack"], "nouvel-an-chinois": ["chinese new year dumplings", "chinese new year food"],
 "saint-valentin": ["valentine dinner", "chocolate dessert hearts"], "ramadan": ["iftar table", "ramadan iftar"], "aid-kebir": ["eid al adha food", "tabaski"],
 "paques": ["easter brunch", "easter eggs chocolate"], "fete-meres": ["family lunch table", "mother's day breakfast"], "barbecue": ["barbecue grill summer", "bbq grill"],
 "halloween": ["halloween pumpkins", "pumpkin soup halloween"], "diwali": ["diwali sweets", "diwali food"], "noel": ["christmas dinner", "christmas table food"],
 "anniversaire": ["birthday cake", "birthday party food"], "aperitif": ["aperitif tapas", "appetizers platter"],
}

ALL = {**{f"recette/{k}": v for k, v in RECIPES.items()}, **{f"technique/{k}": v for k, v in TECHNIQUES.items()},
       **{f"region/{k}": v for k, v in REGIONS.items()}, **{f"rubrique/{k}": v for k, v in RUBRIQUES.items()}, **{f"fete/{k}": v for k, v in FETES.items()}}

# Vague 2 (Tome 13) et dictionnaire illustré des ingrédients
from subjects_v2 import RECIPES_V2
ALL.update({f"recette/{k}": v for k, v in RECIPES_V2.items()})
try:
    from dico_subjects import DICO
    ALL.update({f"ingredient/{k}": v for k, v in DICO.items()})
except ImportError:
    pass
