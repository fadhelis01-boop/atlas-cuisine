# -*- coding: utf-8 -*-
"""Photos des fiches des favoris du 10/11/2026. Usage : ATLAS_DB=candidats_v8b.json .venv/Scripts/python.exe collect_v8b.py"""
import collect_v2 as C
Q = {"sauce_cesar": ["Caesar dressing", "Caesar salad dressing"], "ballotine_poulet_camembert": ["chicken ballotine", "stuffed chicken roulade"],
     "poisson_braise_camerounais": ["poisson braisé", "grilled whole fish Africa"]}
C.ALL = {f"recette/{k}": v for k, v in Q.items()}
if __name__ == "__main__":
    db, keys = C.collect("")
    C.sheets(db, keys, "v8b/")
