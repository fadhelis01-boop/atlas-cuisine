# -*- coding: utf-8 -*-
"""Photos des 8 fiches de l'audit famille nombreuse (13/11/2026). Licences libres seulement.
Usage : ATLAS_DB=candidats_v17.json ATLAS_WORKERS=3 .venv/Scripts/python.exe collect_v17.py"""
import collect_v2 as C
Q = {
 "poisson_pane_maison": ["fish fingers homemade", "fish sticks", "breaded fish fingers"],
 "semoule_au_lait": ["semolina pudding", "gâteau de semoule", "semolina milk pudding"],
 "oeuf_coque_mouillettes": ["soft boiled egg soldiers", "oeuf à la coque", "boiled egg toast soldiers"],
 "roti_porc_moutarde_miel": ["roast pork potatoes", "rôti de porc", "pork roast oven"],
 "gratin_poisson_epinards": ["fish gratin spinach", "fish pie spinach", "gratin de poisson"],
 "yaourts_maison": ["homemade yogurt jars", "yaourt maison", "yogurt glass jars"],
 "biscuit_roule_confiture": ["swiss roll jam", "jam roll cake", "biscuit roulé"],
 "frites_legumes_four": ["roasted root vegetable fries", "carrot fries", "parsnip fries"],
}
C.ALL = {f"recette/{k}": v for k, v in Q.items()}
if __name__ == "__main__":
    db, keys = C.collect("")
    C.sheets(db, keys, "v17/")
