# -*- coding: utf-8 -*-
"""Dictionnaire illustré des ingrédients (Tome 13 §8) : réunit les 4 parties et vérifie la couverture du Tome 3."""
from dico_1 import D1
from dico_2 import D2
from dico_3 import D3, ALIAS
from dico_4 import D4

DICO = {**D1, **D2, **D3, **D4}
