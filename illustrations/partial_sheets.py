# -*- coding: utf-8 -*-
"""Planches de choix pour les sujets déjà collectés et pas encore triés (lecture seule de la base de candidates).
Usage : python partial_sheets.py recette/ [lot]   → planches_v2/<lot>_NNN.jpg + <lot>_index.json"""
import json, os, sys, time
import fetch_candidates as F
from collect_v2 import sheets, HERE
from subjects import ALL

prefix, lot = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "lot")
dbp = os.path.join(HERE, os.environ.get("ATLAS_DB", "candidats.json"))
db = json.load(open(dbp, encoding="utf-8"))
sel = json.load(open(os.path.join(HERE, "selections.json"), encoding="utf-8"))
done = set(sel) | set(json.load(open(os.path.join(HERE, "tries.json"), encoding="utf-8"))) if os.path.exists(os.path.join(HERE, "tries.json")) else set(sel)
keys = [k for k in ALL if k.startswith(prefix) and k in db and db[k] and k not in done]
for k in keys:
    for i, c in enumerate(db[k][:8]):
        c["file"] = os.path.join(F.CAND, k.replace("/", "__") + f"__{i}.jpg")
        if not os.path.exists(c["file"]): F.fetch_thumb(c["file"], c["thumb"])
sheets(db, keys, lot + "/")
print(len(keys), "sujets")
