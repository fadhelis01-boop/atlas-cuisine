# -*- coding: utf-8 -*-
"""Troisième passe (12/11/2026) sur toutes les fiches encore sans photo : on cherche sous le nom d'origine (origin), le
titre sans parenthèses et le contenu des parenthèses (manquantes_v15.json), plus des mots-clés choisis à la main pour les
fiches TikTok d'Asie. Licences libres seulement.
Usage : ATLAS_DB=candidats_v15.json ATLAS_WORKERS=3 .venv/Scripts/python.exe collect_v15.py"""
import json
import collect_v2 as C
Q = json.load(open("manquantes_v15.json", encoding="utf8"))
Q.update({
 "porc_caramelise_viet": ["thit kho", "caramelized pork belly Vietnamese", "braised pork caramel sauce"],
 "boeuf_saute_oeuf": ["beef and egg rice", "stir fried beef egg", "huadan niurou"],
 "goong_ob_woon_sen": ["glass noodles shrimp clay pot", "shrimp vermicelli clay pot", "Thai glass noodle prawns"],
 "mayonnaise_japonaise": ["homemade mayonnaise jar", "mayonnaise", "mayonnaise in bowl"],
})
C.ALL = {f"recette/{k}": v for k, v in Q.items()}
if __name__ == "__main__":
    db, keys = C.collect("")
    C.sheets(db, keys, "v15/")
