# -*- coding: utf-8 -*-
"""Audit « amateur de pains, brioches et pâtisserie maison » (22/11/2026, AUDIT_PATISSERIE_AMATEUR_2026-11-22.md §1).
Appliqué par export_app_data.py après les étapes réécrites : la pousse d'une pâte levée dépend fortement de la
température de la cuisine (une pâte en cuisine froide met bien plus longtemps qu'annoncé) ; une étape qui ne donne
qu'une durée fixe, sans repère visuel, laisse un amateur sortir une pâte qui n'a pas assez levé. Un repère visuel est
ajouté aux étapes de pousse qui n'en ont encore aucun, en plus de la durée déjà donnée (jamais à la place)."""
import re, unicodedata

def _n(s):
    return unicodedata.normalize("NFD", s.replace("œ", "oe").replace("Œ", "Oe")).encode("ascii", "ignore").decode().lower()

POUSSE = re.compile(r"pousse|apprêt|apprets|\blev[eé]|laisse lever")
VISUAL = re.compile(r"doubl|tremble|rebondit|gonfl|bulle|a pris du volume|volume double")
CUE_PHRASE = " Repère plus fiable que l'heure : la pâte a doublé de volume et rebondit lentement quand tu l'enfonces du doigt."

def proofing_visual_cue(d):
    """Ajoute un repère visuel aux étapes de pousse qui n'en ont aucun ; renvoie le nombre d'étapes complétées."""
    added = 0
    steps = list(d["steps"])
    for i, s in enumerate(steps):
        if not POUSSE.search(_n(s)) or VISUAL.search(_n(s)):
            continue
        s = s.rstrip()
        steps[i] = s + ("" if s.endswith((".", ":", ";")) else ".") + CUE_PHRASE
        added += 1
    if added:
        d["steps"] = steps
    return added

def apply(recipes):
    stats = {"pousse": 0}
    for d in recipes:
        stats["pousse"] += proofing_visual_cue(d)
    return stats
