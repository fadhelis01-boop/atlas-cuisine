# -*- coding: utf-8 -*-
"""Deuxième passe des photos de l'audit gourmet : les 8 fiches sans candidate juste au premier tour (autres requêtes).
Usage : ATLAS_DB=candidats_v7b.json .venv/Scripts/python.exe collect_v7b.py"""
import collect_v2 as C
Q = {
    "riz_nature": ["plain white rice", "cooked basmati rice"], "semoule_nature": ["couscous grain", "couscous semolina plain"],
    "pommes_vapeur": ["boiled potatoes", "steamed potatoes"], "merlu_beurre_blanc_poireaux": ["fish beurre blanc", "white fish leeks"],
    "gratin_celeri_noix": ["celeriac", "gratin dauphinois"], "poelee_panais_pois_chiches": ["roasted parsnips", "parsnips carrots roasted"],
    "chou_braise_saucisses": ["braised cabbage", "cabbage and sausages"], "coings_rotis_miel": ["quince dessert", "poached quince"],
}
C.ALL = {f"recette/{k}": v for k, v in Q.items()}
db, keys = C.collect("")
C.sheets(db, keys, "v7b/")
