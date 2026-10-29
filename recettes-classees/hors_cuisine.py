# -*- coding: utf-8 -*-
"""Favoris hors cuisine (29/10/2026) : des comptes sans rapport avec la cuisine (finance, IA, emploi, bricolage…) que le
propriétaire a enregistrés s'étaient glissés dans « À vérifier » et étaient publiés. Leur liste reste privée
(prive/hors_cuisine.txt, non publié) ; ce module les retire des listes classées et sert de filtre aux relevés et à l'export.
Usage : python hors_cuisine.py   (nettoie les fichiers *_classes.md et recalcule le nombre de vidéos par rubrique)"""
import glob, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
LIST = os.path.join(HERE, "prive", "hors_cuisine.txt")

def accounts():
    return set(open(LIST, encoding="utf-8").read().split()) if os.path.exists(LIST) else set()

def is_hors_cuisine(url_or_author, _cache=[]):
    if not _cache: _cache.append(accounts())
    m = re.search(r"/@([^/]+)/", url_or_author)
    return (m.group(1) if m else url_or_author.lstrip("@")) in _cache[0]

def clean_file(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    out, removed = [], 0
    for line in lines:
        m = re.match(r"^- \[.*\]\((https://www\.tiktok\.com/@[^)]+)\)", line)
        if m and is_hors_cuisine(m.group(1)): removed += 1; continue
        out.append(line)
    if not removed: return 0
    # nombre de vidéos par rubrique : « ## Titre (N) »
    for i, line in enumerate(out):
        h = re.match(r"^(## .*)\((\d+)\)\s*$", line)
        if h:
            n = 0
            for nxt in out[i + 1:]:
                if nxt.startswith("## "): break
                n += nxt.startswith("- [")
            out[i] = f"{h.group(1)}({n})"
    open(path, "w", encoding="utf-8").write("\n".join(out))
    return removed

if __name__ == "__main__":
    for f in sorted(glob.glob(os.path.join(HERE, "*_classes.md")) + glob.glob(os.path.join(HERE, "*_classees.md"))):
        n = clean_file(f)
        if n: print(os.path.basename(f), ":", n, "vidéos hors cuisine retirées")
