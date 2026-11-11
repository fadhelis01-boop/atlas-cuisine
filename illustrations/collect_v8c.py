# -*- coding: utf-8 -*-
"""Photos des fiches des auteurs des favoris du 10/11/2026. Usage : ATLAS_DB=candidats_v8c.json .venv/Scripts/python.exe collect_v8c.py"""
import collect_v2 as C
Q = {"creme_balsamique_maison": ["balsamic glaze", "balsamic reduction"], "stracciatella_maison": ["stracciatella cheese", "burrata"],
     "beurre_cacahuete_maison": ["peanut butter jar", "homemade peanut butter"], "tuiles_parmesan": ["parmesan crisps", "frico"],
     "persillade_frigo": ["persillade", "chopped parsley garlic"], "sucre_glace_maison": ["powdered sugar", "icing sugar"],
     "beignets_fourres_pate_tartiner": ["Nutella doughnuts", "filled doughnuts"], "boules_fromage_croustillantes": ["cheese balls fried", "fried cheese balls"],
     "poulet_crousty_riz": ["crispy chicken rice bowl", "fried chicken rice"], "onion_rings": ["onion rings", "fried onion rings"],
     "pate_foie_volaille": ["chicken liver pâté", "chicken liver pate"], "boulettes_viande_pommes_de_terre": ["meatballs potatoes tomato stew", "meatball stew"],
     "riz_viande_hachee": ["rice with minced meat", "beef rice pilaf"], "spaghetti_boulettes_poisson": ["fish balls tomato sauce", "fish meatballs pasta"],
     "spaghetti_sautes_crevettes": ["stir fried spaghetti shrimp", "shrimp spaghetti"], "boisson_mangue_ananas": ["mango pineapple smoothie", "mango smoothie"],
     "riz_haricots_rouges_legumes": ["rice and kidney beans", "rice and beans"], "spaghetti_sautes_legumes_oeufs": ["stir fried spaghetti vegetables", "fried noodles egg vegetables"]}
C.ALL = {f"recette/{k}": v for k, v in Q.items()}
if __name__ == "__main__":
    db, keys = C.collect("")
    C.sheets(db, keys, "v8c/")
