# -*- coding: utf-8 -*-
"""Audit gourmet (21/10/2026) : photos candidates des 20 fiches de recipes_v4_variete.py (licences libres, Wikimedia
Commons et Openverse), planches planches_v2/v7_NNN.jpg. Les 31 classiques réécrits gardent leur photo (mêmes identifiants).
Usage : ATLAS_DB=candidats_v7.json .venv/Scripts/python.exe collect_v7.py"""
import os, re
import collect_v2 as C
from subjects import ALL

HERE = os.path.dirname(os.path.abspath(__file__))
NEW = set(re.findall(r'^K\("([^"]+)"', open(os.path.join(HERE, "..", "bible", "recipes_v4_variete.py"), encoding="utf-8").read(), re.M))
# requêtes : le français d'abord, puis l'anglais (Flickr et Commons trouvent mieux)
Q = {
    "riz_nature": ["bol de riz blanc", "steamed white rice bowl"], "semoule_nature": ["semoule couscous", "plain couscous bowl"],
    "pates_nature": ["pâtes au beurre parmesan", "buttered pasta parmesan"], "pommes_vapeur": ["pommes de terre vapeur persil", "boiled potatoes parsley"],
    "maquereaux_four_moutarde": ["maquereau au four", "baked mackerel"], "sardines_poelees_persillade": ["sardines grillées persil", "grilled sardines parsley"],
    "lieu_croute_herbes": ["poisson croûte d'herbes", "herb crusted fish fillet"], "papillotes_poisson_legumes": ["papillote poisson", "fish en papillote"],
    "merlu_beurre_blanc_poireaux": ["merlu poireaux", "hake leeks"], "potimarron_farci_quinoa": ["potimarron farci", "stuffed red kuri squash"],
    "gratin_celeri_noix": ["gratin céleri-rave", "celeriac gratin"], "poelee_panais_pois_chiches": ["panais rôtis", "roasted parsnips chickpeas"],
    "veloute_topinambour": ["velouté topinambour", "jerusalem artichoke soup"], "chou_braise_saucisses": ["chou braisé saucisses", "braised cabbage sausages"],
    "poires_pochees_vin_epices": ["poires au vin", "pears poached in red wine"], "tarte_bourdaloue": ["tarte bourdaloue", "pear almond tart"],
    "coings_rotis_miel": ["coings rôtis", "baked quince"], "mont_blanc_verrines": ["mont-blanc dessert", "mont blanc chestnut dessert"],
    "paella_valenciana_traditionnelle": ["paella valenciana", "paella valenciana rabbit chicken"], "plateau_fromages": ["plateau de fromages", "french cheese platter"],
}
assert set(Q) == NEW, NEW ^ set(Q)
C.ALL = {f"recette/{k}": v for k, v in Q.items()}
print(len(C.ALL), "sujets")
db, keys = C.collect("")
C.sheets(db, keys, "v7/")
