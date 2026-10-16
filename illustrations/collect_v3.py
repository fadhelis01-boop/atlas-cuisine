# -*- coding: utf-8 -*-
"""Vague 3 (audit UX du 16/10/2026) : photos candidates des fiches ajoutées (express, brunch, salades, végétarien, monde 3),
planches planches_v2/v3_NNN.jpg. Usage : ATLAS_DB=candidats_v3.json .venv/Scripts/python.exe collect_v3.py"""
import os, re
import collect_v2 as C
from subjects import ALL

HERE = os.path.dirname(os.path.abspath(__file__))
NEW = set()
for f in ("express", "brunch", "salades", "vege", "monde3"):
    NEW |= set(re.findall(r'^K\("([^"]+)"', open(os.path.join(HERE, "..", "bible", f"recipes_v2_{f}.py"), encoding="utf-8").read(), re.M))
C.ALL = {k: v for k, v in ALL.items() if k.startswith("recette/") and k.split("/", 1)[1] in NEW}
print(len(C.ALL), "sujets")
db, keys = C.collect("recette/")
C.sheets(db, keys, "v3/")
