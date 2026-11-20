# -*- coding: utf-8 -*-
"""Photos des 6 nouvelles marinades (coin Marinades, 20/11/2026). Licences libres seulement.
Usage : ATLAS_DB=candidats_v20.json ATLAS_WORKERS=3 .venv/Scripts/python.exe collect_v20.py"""
import collect_v2 as C
Q = {
 "harissa_marinade_agneau": ["lamb skewers grilled harissa", "marinated lamb chops grilled"],
 "mojo_cubain_porc": ["mojo criollo pork cuban", "cuban roast pork garlic"],
 "porc_citronnelle_vietnamien": ["vietnamese grilled pork lemongrass", "thit nuong vietnamese bbq"],
 "crevettes_citron_vert_marinade": ["grilled shrimp garlic lime", "camarones al mojo de ajo"],
 "tofu_marinade_soja_gingembre": ["marinated grilled tofu soy ginger", "tofu steak grilled"],
 "gravlax_saumon_marinade": ["gravlax salmon cured dill", "gravlax sliced salmon"],
}
C.ALL = {f"recette/{k}": v for k, v in Q.items()}
if __name__ == "__main__":
    db, keys = C.collect("")
    C.sheets(db, keys, "v20/")
