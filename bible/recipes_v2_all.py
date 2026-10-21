# -*- coding: utf-8 -*-
"""Vague 2 (Tome 13) : importe tous les lots. Ajouter ici chaque nouveau fichier recipes_v2_*.py."""
import importlib, glob, os
HERE = os.path.dirname(os.path.abspath(__file__))
for f in sorted(glob.glob(os.path.join(HERE, "recipes_v2_*.py")) + glob.glob(os.path.join(HERE, "recipes_v3_*.py")) + glob.glob(os.path.join(HERE, "recipes_v4_*.py")) + glob.glob(os.path.join(HERE, "recipes_v5_*.py"))):  # v3 : audit du chef (16/10/2026) ; v4 : audit gourmet (21/10/2026)
    name = os.path.basename(f)[:-3]
    if name not in ("recipes_v2_base", "recipes_v2_all"):
        importlib.import_module(name)
