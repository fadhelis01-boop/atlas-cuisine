# -*- coding: utf-8 -*-
"""Dictionnaire illustré, complément (16/10/2026) : photos candidates des fiches encore sans image (hors alcools et porc),
en priorité les ingrédients exotiques. Planches planches_v2/ing2_NNN.jpg. Usage : ATLAS_DB=candidats_ing2.json .venv/Scripts/python.exe collect_ing2.py"""
import json, os
import collect_v2 as C
from subjects import ALL

HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(HERE, "..", "app", "src", "data")
more = json.load(open(os.path.join(APP, "images_more.json"), encoding="utf-8"))
dico = json.load(open(os.path.join(APP, "dico.json"), encoding="utf-8"))
SKIP = {"Lardons", "Coppa / capocollo", "Os / couenne de jambon (bouillon)", "Vin rouge", "Vin moelleux / liquoreux", "Vermouth", "Cidre", "Poiré",
        "Calvados", "Rhum ambré / blanc", "Whisky / bourbon", "Vodka", "Gin / genièvre", "Tequila", "Kirsch / eaux-de-vie de fruits",
        "Grand Marnier / Cointreau / triple sec", "Amaretto", "Liqueur de café", "Crème de whisky / liqueur crémeuse", "Cerises / fruits « à l'eau-de-vie » ",
        "Cerises / fruits « à l'eau-de-vie »", "Cachaça / pisco", "Arôme amande amère / rhum / « arômes »"}
want = {f"ingredient/{s}" for s, d in dico.items() if f"ingredient/{s}" not in more and d["name"] not in SKIP}
C.ALL = {k: v for k, v in ALL.items() if k in want}
print(len(C.ALL), "sujets", flush=True)
db, keys = C.collect("ingredient/")
C.sheets(db, keys, "ing2/")
