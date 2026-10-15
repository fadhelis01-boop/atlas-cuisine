# -*- coding: utf-8 -*-
"""Sujets photo du dictionnaire illustré : une requête anglaise par fiche (bible/dico_*.py), identifiant = slug du nom."""
import os, re, sys, unicodedata
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "bible"))
from dictionnaire_data import DICO as _D

SPECIAL = {"Poiré": "poire-boisson"}  # collision avec « Poire »

def slug(name):
    if name in SPECIAL: return SPECIAL[name]
    s = unicodedata.normalize("NFKD", name.replace("œ", "oe").replace("Œ", "Oe")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:60]

DICO = {slug(k): [v[0]] for k, v in _D.items()}
