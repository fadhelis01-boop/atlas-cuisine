# -*- coding: utf-8 -*-
"""Classe les vidéos des comptes TikTok @lacuisinedemarina (cuisine camerounaise) et @niangcook (cuisine sénégalaise),
relevées le 15/10/2026 (TikTok n'affiche sur le web que les 67 et 18 vidéos les plus récentes de ces comptes).
Tri MANUEL d'après la légende ; HC = hors recette (annonces, publicité, vie du compte), non retenu.
Écrit createurs_tiktok_classes.md au format de tiktok_favoris_classes.md (lu par bible/export_app_data.py)."""
import json, re

D = json.load(open("createurs_tiktok_brut.json", encoding="utf-8"))
A, B, BO, DE, TE, ST, IT, AV, HC = "afrique", "boissons", "boissons", "desserts", "techniques", "street_food", "italie", "a_verifier", "HC"
MARINA = [A, AV, HC, A, B, AV, A, A, A, A, A, A, B, A, IT, DE, TE, A, ST, A, HC, B, A, HC, AV, B, ST, A, A, AV,
          A, A, A, A, AV, HC, AV, A, A, HC, HC, A, DE, A, A, TE, HC, HC, A, A, A, HC, A, HC, TE, A, A, A, HC, AV,
          A, ST, A, A, A, A, A]
NIANG = [HC, HC, HC, DE, A, HC, A, A, A, AV, A, AV, DE, B, AV, A, HC, B]
assert len(MARINA) == len(D["marina"]) and len(NIANG) == len(D["niang"])
PORK = {("marina", 18)}  # pain farci au jambon

LAB = {A: "🌍 Afrique de l'Ouest & centrale", B: "🥤 Boissons", DE: "🍰 Desserts & pâtisserie", TE: "🔪 Techniques & astuces",
       ST: "🍔 Street food & fast-food fait maison", IT: "🌍 Europe : Italie", AV: "❓ À vérifier (légende vide ou insuffisante)"}

def title(c):
    s = re.sub(r"créé par .*$", "", c, flags=re.I)
    s = re.sub(r"#\S+", "", s); s = re.sub(r"https?:\S+", "", s)
    s = re.sub(r"\s+", " ", s).replace("[", "(").replace("]", ")").strip(" ·-")
    if len(s) > 110: s = s[:107].rsplit(" ", 1)[0] + "…"
    return s or "(sans légende)"

groups, kept, hc = {}, 0, 0
for acc, cats, handle in (("marina", MARINA, "lacuisinedemarina"), ("niang", NIANG, "niangcook")):
    for i, (x, c) in enumerate(zip(D[acc], cats)):
        if c == HC: hc += 1; continue
        tags = " · 🐖 porc probable" if (acc, i) in PORK else ""
        photo = " · carrousel photo" if "/photo/" in x["url"] else ""
        groups.setdefault(c, []).append(f"- [{title(x['caption'])}]({x['url']}) · @{handle}{photo}{tags}")
        kept += 1

o = ["# 📲 Comptes TikTok « La cuisine de Marina » et « NiangCook », classés pour ATLAS\n",
     f"> Relevé le 15/10/2026 : {len(D['marina'])} vidéos de @lacuisinedemarina (cuisine camerounaise) et {len(D['niang'])} de @niangcook (cuisine sénégalaise), "
     "soit **toutes celles que TikTok affiche sur le web** pour ces comptes (le chargement s'arrête ensuite ; la protection anti-robot de TikTok n'a pas été contournée).",
     f"> **{kept} recettes retenues**, {hc} vidéos hors recette écartées (annonces, vente d'épices, livre, restaurant, rappels de notification). Tri manuel d'après la légende.",
     "> Liens crédités uniquement : les vidéos se lisent dans ATLAS par l'intégration officielle de TikTok ; rien n'est copié.\n"]
for c in (A, ST, IT, DE, B, TE, AV):
    if c in groups:
        o.append(f"\n## {LAB[c]} ({len(groups[c])})\n"); o += groups[c]
open("createurs_tiktok_classes.md", "w", encoding="utf-8").write("\n".join(o) + "\n")
print(kept, "retenues ;", hc, "écartées ;", {k: len(v) for k, v in groups.items()})
