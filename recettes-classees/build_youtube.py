# -*- coding: utf-8 -*-
"""Classe les vidéos des chaînes YouTube demandées (relevé du 15/10/2026, youtube_brut.json : vidéos et Shorts les plus récents)
dans les catégories de la bible. Tri AUTOMATIQUE d'après le titre (mots-clés français, anglais, allemands, néerlandais),
avec la cuisine de la chaîne comme catégorie par défaut. Hors recette (vlogs, annonces, concours, livres) écarté.
Écrit createurs_youtube_classes.md (lu par bible/export_app_data.py). Liens crédités seulement : rien n'est copié."""
import json, re, unicodedata
from collections import OrderedDict, Counter

D = json.load(open("youtube_brut.json", encoding="utf-8"))

CHANNELS = OrderedDict([  # handle → (nom affiché, langue des titres, catégorie par défaut, présentation)
 ("lerizjaune", ("Le Riz Jaune", "fr", "asie", "cuisines d'Asie en français (Chine, Thaïlande, Laos, Vietnam, Japon, Corée)")),
 ("lacuisinedemarina1039", ("La cuisine de Marina", "fr", "afrique", "cuisine camerounaise et d'Afrique centrale")),
 ("lardoiseportovecchio", ("L'Ardoise Porto-Vecchio", "fr", "fait_maison", "chef corse : fait maison contre l'industriel, sauces, bistrot")),
 ("armandhasanpapaj", ("Armand Hasanpapaj", "fr", "pains", "pains, viennoiseries et cuisine des Balkans")),
 ("alexcook.in4", ("AlexCook'in", "fr", "france", "plats familiaux rapides")),
 ("britneybreaksbread3824", ("Britney Breaks Bread", "en", "desserts", "pâtisserie et comfort food américaine (en anglais)")),
 ("TinasKitchenworld", ("Tinas Kitchenworld", "de", "pains", "pains, brioches et gâteaux des Balkans et d'Allemagne (en allemand)")),
 ("aisletotokyo", ("Shota Horii · Aisle to Tokyo", "en", "asie", "100 recettes japonaises du quotidien (en anglais)")),
 ("Cookwithbash", ("CookWithBash", "fr", "maghreb", "cuisine algérienne, maghrébine et du monde")),
 ("Chester_Foodies", ("ChesterFoodies", "fr", "france", "cuisine française familiale et franc-comtoise")),
 ("Dishcovery_", ("Dishcovery", "en", "asie", "nouilles et plats asiatiques fusion (en anglais)")),
 ("CookwithNabeela", ("Cook with Nabeela", "en", "asie", "cuisine pakistanaise, indienne et du monde (en anglais)")),
 ("kookmutsjes", ("Kookmutsjes", "nl", "desserts", "pâtisseries, gâteaux et snacks (néerlandais/anglais)")),
])
LANG = {"en": "🇬🇧 en anglais", "de": "🇩🇪 en allemand", "nl": "🇳🇱 en néerlandais"}

from classement import *  # règles de tri communes

groups, stats, hc = OrderedDict(), Counter(), Counter()
for h, (name, lang, default, _) in CHANNELS.items():
    for v in D.get(h, {}).get("videos", []):
        t = clean(v["title"]); n = nrm(t)
        if len(n) < 4 or HC.search(n): hc[name] += 1; continue
        cat = next((c for c, rx in CAT_RULES if re.search(rx, n)), None)
        if cat is None: cat = "a_verifier" if JUNK.search(n) else default
        if cat == "asie":
            sub = next(s for s, rx in ASIE_SUB if re.search(rx, n))
            if h == "CookwithNabeela" and sub == "Chine & Taïwan" and not re.search(r"chinese|chow|noodle|manchurian|fried rice", n): sub = "Inde & Pakistan"
            key = f"🌏 Asie : {sub}"
        else:
            key = {"afrique": "🌍 Afrique de l'Ouest & centrale", "maghreb": "🌍 Maghreb", "moyen_orient": "🌍 Moyen-Orient, Turquie & Balkans", "italie": "🌍 Europe : Italie",
                   "france": "🇫🇷 France", "ameriques": "🌎 Amériques", "street_food": "🍔 Street food & fast-food fait maison", "pains": "🥖 Pains, pâtes & bases",
                   "sauces": "🥫 Sauces maison", "fait_maison": "🍯 Fait maison sans additifs", "desserts": "🍰 Desserts & pâtisserie", "boissons": "🥤 Boissons",
                   "techniques": "🔪 Techniques & astuces", "zero_dechet": "♻️ Zéro déchet", "a_verifier": "❓ À vérifier (titre trop vague)"}[cat]
        url = f"https://www.youtube.com/shorts/{v['id']}" if v.get("short") else f"https://www.youtube.com/watch?v={v['id']}"
        flags = (" · 🐖 porc probable" if PORK.search(n) else "") + (" · 🍷 alcool" if ALCOHOL.search(n) else "") + (f" · {LANG[lang]}" if lang in LANG else "") + (" · short" if v.get("short") else "")
        groups.setdefault(key, []).append(f"- [{t}]({url}) · ▶ {name}{flags}")
        stats[name] += 1

o = ["# ▶ Chaînes YouTube de recettes, classées pour ATLAS\n",
     "> Relevé du 15/10/2026 (vidéos et Shorts les plus récents de chaque chaîne, 400 au plus). Tri **automatique** d'après le titre ; "
     f"**{sum(stats.values())} recettes retenues**, {sum(hc.values())} vidéos hors recette écartées (vlogs, annonces, concours, livres, voyages).",
     "> Liens crédités uniquement : les vidéos se lisent dans ATLAS par le lecteur officiel de YouTube (youtube-nocookie) ; rien n'est copié. "
     "Les titres étrangers sont gardés dans leur langue (signalés). 🐖 / 🍷 : porc ou alcool repérés dans le titre (à vérifier dans la vidéo).\n",
     "## Lire ce fichier\n", "| Chaîne | Spécialité | Retenues | Écartées |", "|---|---|---|---|"]
for h, (name, lang, default, desc) in CHANNELS.items():
    o.append(f"| [{name}]({D.get(h, {}).get('url', '') or 'https://www.youtube.com/@' + h}) | {desc} | {stats[name]} | {hc[name]} |")
order = ["🇫🇷 France", "🌍 Afrique de l'Ouest & centrale", "🌍 Maghreb", "🌍 Moyen-Orient, Turquie & Balkans"] + sorted(k for k in groups if k.startswith("🌏")) + \
        ["🌍 Europe : Italie", "🌎 Amériques", "🍔 Street food & fast-food fait maison", "🥖 Pains, pâtes & bases", "🥫 Sauces maison", "🍯 Fait maison sans additifs",
         "🍰 Desserts & pâtisserie", "🥤 Boissons", "🔪 Techniques & astuces", "♻️ Zéro déchet", "❓ À vérifier (titre trop vague)"]
for k in order:
    if k in groups:
        o.append(f"\n## {k} ({len(groups[k])})\n"); o += groups[k]
open("createurs_youtube_classes.md", "w", encoding="utf-8").write("\n".join(o) + "\n")
print(sum(stats.values()), "retenues ;", sum(hc.values()), "écartées")
print({k: len(v) for k, v in groups.items()})
print(dict(hc))
