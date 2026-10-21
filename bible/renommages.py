# -*- coding: utf-8 -*-
"""Recettes renommées (audit dév/UX 2026-10-21 §3.7) : quand l'identifiant d'une fiche change, ajouter ici
« ancien → nouveau ». L'application suit le nouveau nom dans les favoris, le carnet, la semaine et l'historique de chacun,
au lieu de faire disparaître la recette en silence. Ne jamais retirer une ligne : un téléphone peut ne pas avoir ouvert
ATLAS depuis longtemps."""
RENAMES = {
    # 2026-10-22 : doublons fusionnés (même plat écrit deux fois), la version la plus complète est gardée
    "misir_wot": "misir_wat",
    "carbonade_flamande": "carbonnade_flamande",
    "marinade_adobo": "adobo_poulet",
}
