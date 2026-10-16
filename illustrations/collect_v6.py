# -*- coding: utf-8 -*-
"""Pique-nique (16/10/2026) : photos candidates des fiches recipes_v3_piquenique.py,
planches planches_v2/v6_NNN.jpg. Usage : ATLAS_DB=candidats_v6.json .venv/Scripts/python.exe collect_v6.py"""
import os, re
import collect_v2 as C
from subjects import ALL

HERE = os.path.dirname(os.path.abspath(__file__))
NEW = set()
import glob
for f in glob.glob(os.path.join(HERE, "..", "bible", "recipes_v3_piquenique.py")):
    NEW |= set(re.findall(r'^K\("([^"]+)"', open(f, encoding="utf-8").read(), re.M))
C.ALL = {k: v for k, v in ALL.items() if (k.startswith("recette/") and k.split("/", 1)[1] in NEW) or k == "rubrique/pique_nique"}
print(len(C.ALL), "sujets")
db, keys = C.collect("")
C.sheets(db, keys, "v6/")
