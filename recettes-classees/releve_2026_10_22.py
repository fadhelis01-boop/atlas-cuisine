# -*- coding: utf-8 -*-
"""Classe les vidéos lues le 22/10/2026 : favoris TikTok ajoutés depuis le 14/10 (compte connecté par le propriétaire) et
vidéos les plus populaires des créateurs suivis (onglet « Populaire » de leur profil public). Écrit
favoris_createurs_2026-10-22_classes.md au format de tiktok_favoris_classes.md, lu par bible/export_app_data.py.
Seuls le lien, l'auteur et un titre court tiré de la légende sont publiés (crédit + lien, rien n'est copié).
Les favoris hors cuisine n'ont jamais été relevés (ils restent privés)."""
import json, os, re
from classement import ALCOHOL, PORK, clean, nrm, section_from_fiche, section_of
from hors_cuisine import is_hors_cuisine

HERE = os.path.dirname(os.path.abspath(__file__))
DB = json.load(open(os.path.join(HERE, "prive", "legendes_tiktok.json"), encoding="utf-8"))
ORDER = ["🎉", "🌍 Afrique", "🌍 Maghreb", "🌍 Moyen-Orient", "🌏 Asie", "🌍 Europe : Italie", "🌍 Europe : autres", "🇫🇷 France", "🌎 Amériques", "🍔", "🥖", "🥫", "🍯", "🍰", "🥤", "🔪", "♻️", "❓"]

def title_of(desc):
    t = re.sub(r"#\S+|@\S+", " ", desc or "")
    # le titre s'arrête avant la liste d'ingrédients (« 200 g de… », « Pour la base… »)
    first = re.split(r"\n|ingr[ée]dients?\s*:?|🛒|📝|recipe\s*:|\s\d+(?:[.,]\d+)?\s?(?:g|gr|kg|ml|cl|l)\b|\b(?:pour|for) (?:la|le|les|the) (?:base|pâte|crème|farce|sauce)\b",
                     t, flags=re.I)[0]
    return clean(first) or clean(t)

groups, kept, skipped = {}, 0, 0
for url, v in DB.items():
    if v.get("missing") or v.get("section") not in ("relevé 22/10", "profil créateur"): continue
    if is_hors_cuisine(url): continue  # favori hors cuisine : jamais publié
    desc = v.get("desc", "")
    t = title_of(desc)
    sec = section_of(t + " " + desc[:200])
    if sec and sec.startswith("❓"): sec = section_from_fiche(url) or sec  # vidéo d'une fiche : la rubrique de la fiche
    if sec and sec.startswith("❓"):  # titre trop vague : on lit plus loin dans la légende (sans les rubriques boissons/techniques, trop faciles à déclencher)
        alt = section_of(desc[:700])
        if alt and not alt.startswith(("❓", "🥤", "🔪")): sec = alt
    if sec is None or len(t) < 4 or re.search(r"\bCOSORI\b|mon allié au quotidien", desc): skipped += 1; continue  # publicité d'appareil, pas une recette
    n = nrm(desc).replace("demi-sel", "")  # beurre demi-sel, pas petit salé
    tags = (" · 🐖 porc probable" if PORK.search(n) else "") + (" · 🍷 alcool" if ALCOHOL.search(n) else "")
    photo = " · carrousel photo" if "/photo/" in url else ""
    groups.setdefault(sec, []).append((int((v.get("stats") or {}).get("collectCount") or 0), f"- [{t}]({url}) · @{v.get('author')}{photo}{tags}"))
    kept += 1

o = ["# 📲 Favoris TikTok du 22/10/2026 et vidéos populaires des créateurs suivis, classés pour ATLAS\n",
     "> Relevé le 22/10/2026 : les favoris ajoutés depuis le 14/10 (compte connecté par le propriétaire) et, pour les créateurs suivis, "
     "les vidéos les plus populaires de leur profil public. Une page à la fois, sans contourner la protection de TikTok.",
     f"> **{kept} vidéos de cuisine classées**, {skipped} écartées (hors recette ou légende trop vague). Les favoris hors cuisine ne sont pas relevés.",
     "> Liens crédités uniquement : les vidéos se lisent dans ATLAS par l'intégration officielle de TikTok ; rien n'est copié.",
     "> Triées par nombre d'enregistrements dans chaque rubrique.\n"]
for sec in sorted(groups, key=lambda s: next((i for i, p in enumerate(ORDER) if s.startswith(p)), 99)):
    rows = sorted(groups[sec], key=lambda x: -x[0])
    o.append(f"\n## {sec} ({len(rows)})\n"); o += [r for _, r in rows]
open(os.path.join(HERE, "favoris_createurs_2026-10-22_classes.md"), "w", encoding="utf-8").write("\n".join(o) + "\n")
print(kept, "classées ;", skipped, "écartées ;", {k: len(v) for k, v in groups.items()})
