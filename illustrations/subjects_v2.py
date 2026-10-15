# -*- coding: utf-8 -*-
"""Sujets de la vague 2 (Tome 13) : requêtes déduites du nom d'origine et du titre de chaque fiche,
plus un indice anglais quand le nom d'origine est trop générique. Les ingrédients du dictionnaire sont dans dico_subjects.py."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
_R = json.load(open(os.path.join(HERE, "..", "app", "src", "data", "recipes.json"), encoding="utf-8"))

# Indices anglais (Flickr / Commons trouvent mieux) pour les titres français génériques
HINT = {
 "bouillon_cube_maison": "vegetable bouillon paste jar", "bouillon_poudre_maison": "dried vegetables powder", "nokoss": "green seasoning paste mortar",
 "marinade_yassa": "onions lemon mustard marinade", "marinade_tandoori": "tandoori chicken marinade", "marinade_jerk": "jerk chicken",
 "marinade_bulgogi": "bulgogi", "marinade_provencale": "herbs olive oil marinade", "marinade_teriyaki_sauce": "teriyaki sauce", "ras_el_hanout_maison": "ras el hanout spices",
 "garam_masala_maison": "garam masala spices", "curry_poudre_maison": "curry powder spices", "pate_curry_vert": "green curry paste", "ghee_maison": "ghee jar",
 "pickles_oignons_rouges": "pickled red onions", "moutarde_maison": "whole grain mustard", "huile_pimentee": "chili oil", "beurre_maitre_hotel": "maitre d'hotel butter",
 "creme_patissiere": "pastry cream", "pate_sucree": "tart shell pastry", "sauce_chien": "sauce chien", "sauce_cheddar": "cheese sauce", "sauce_aigre_douce": "sweet and sour sauce",
 "sauce_yaourt_herbes": "yogurt herb sauce", "ketchup_betterave": "beetroot ketchup", "mayo_curry": "curry mayonnaise", "mayo_herbes": "green mayonnaise herbs", "mayo_safran": "rouille sauce",
 "nuggets_maison": "homemade chicken nuggets", "croquettes_poisson": "fish cakes", "pates_sauce_legumes_caches": "pasta tomato sauce", "mini_pizzas": "mini pizzas",
 "puree_couleurs": "vegetable puree", "soupe_alphabet": "alphabet soup", "compote_pommes_poires": "apple sauce bowl", "chips_epluchures": "potato peel chips",
 "soupe_fanes": "green soup", "croutons_chapelure": "croutons", "quiche_frigo_vide": "quiche", "gratin_pates_restes": "pasta bake", "riz_saute_restes": "fried rice",
 "eclats_chocolat": "chocolate bark", "tablette_chocolat_maison": "chocolate bar homemade", "sucettes_chocolat": "chocolate lollipops", "bonbons_coeur_framboise": "heart chocolates",
 "gateau_anniversaire_choco": "chocolate layer cake", "gateau_chocolat_famille": "chocolate cake", "puree_maison": "mashed potatoes", "pommes_terre_four": "roasted potatoes",
 "salade_fruits_menthe": "fruit salad", "jus_vert": "green juice", "limonade_maison": "lemonade", "punch_fruits": "fruit punch", "lait_or": "golden milk turmeric",
 "galette_pdt_berrichonne": "potato galette", "poulet_basse_temp": "chicken breast roasted", "oeuf_parfait_petits_pois": "poached egg pea puree",
 "cassoulet_volaille": "cassoulet", "potjevleesch_volaille": "potjevleesch", "rougail_saucisses": "rougail saucisse", "currywurst_volaille": "currywurst",
 "char_siu_poulet": "char siu chicken", "feijoada_light": "feijoada", "baeckeoffe_volaille": "baeckeoffe", "endives_jambon_dinde": "endives au jambon gratin",
 "lentilles_saucisses": "lentils sausages", "spaetzle_fromage": "kasespatzle", "crumble_sale_legumes": "vegetable crumble", "bowl_falafel": "falafel bowl",
 "salade_quinoa_patate_douce": "quinoa sweet potato salad", "smoothie_fruits_abimes": "smoothie", "gateau_pain_rassis": "bread pudding",
}

def clean(s): return re.sub(r"\s*\(.*?\)|«|»", "", s).replace("  ", " ").strip()
RECIPES_V2 = {}
for r in _R:
    if "vague 2" not in r["source"]: continue
    q = [clean(r["origin"]), clean(r["title"])]
    if r["id"] in HINT: q.insert(0, HINT[r["id"]])
    seen = []
    for x in q:
        if x and x.lower() not in [y.lower() for y in seen]: seen.append(x)
    RECIPES_V2[r["id"]] = seen
