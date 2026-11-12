# -*- coding: utf-8 -*-
"""Seconde passe (12/11/2026) : les classiques français restés sans photo juste après collect_v11, et les deux derniers
ajoutés (lièvre à la royale, plateau de fruits de mer), avec d'autres mots-clés (noms français, anglais, italiens).
Licences libres seulement. Usage : ATLAS_DB=candidats_v12.json ATLAS_WORKERS=2 .venv/Scripts/python.exe collect_v12.py"""
import collect_v2 as C
Q = {
 "pommes_anna": ["pommes Anna gratin", "potato galette layered", "pommes de terre Anna"],
 "artichauts_vinaigrette": ["boiled artichoke", "artichaut cuit", "globe artichoke plate"],
 "pigeon_petits_pois": ["pigeonneau rôti", "roast squab", "squab dish"],
 "fond_brun_veau": ["brown stock", "demi-glace", "stockpot bones"],
 "court_bouillon": ["poached fish court bouillon", "court-bouillon poisson", "fish poaching liquid"],
 "sauce_choron": ["béarnaise sauce steak", "sauce béarnaise", "choron sauce"],
 "sauce_poivrade": ["venison sauce", "game meat sauce", "chevreuil sauce"],
 "raie_beurre_noisette_capres": ["skate wing", "aile de raie", "raie au beurre"],
 "maquereaux_vin_blanc": ["marinated mackerel", "maquereaux marinés", "pickled mackerel"],
 "bulots_aioli": ["whelks", "bulots mayonnaise", "plateau bulots"],
 "bavarois_framboise": ["raspberry mousse cake", "bavarois aux fruits", "bavarian cream"],
 "vacherin_glace": ["vacherin dessert", "meringue ice cream cake", "frozen meringue cake"],
 "puits_amour": ["puits d'amour Stohrer", "caramelized cream pastry", "crème brûlée tart"],
 "faisan_chou_cocotte": ["roast pheasant dish", "faisan rôti", "pheasant casserole"],
 "sauce_diable": ["sauce diable poulet", "devilled chicken", "spatchcock chicken sauce"],
 "sauce_charcutiere": ["pork chop sauce", "côte de porc sauce", "pork chop gherkins"],
 "lievre_royale": ["lièvre à la royale", "hare dish", "civet de lièvre"],
 "plateau_fruits_de_mer": ["plateau de fruits de mer", "seafood platter", "fruits de mer plateau"],
}
C.ALL = {f"recette/{k}": v for k, v in Q.items()}
if __name__ == "__main__":
    db, keys = C.collect("")
    C.sheets(db, keys, "v12/")
