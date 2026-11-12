# -*- coding: utf-8 -*-
"""Photos des 16 fiches TikTok « cuisines d'Asie » (12/11/2026 : Cooking with Morgane, Ryuji, Lynja). Licences libres seulement.
Usage : ATLAS_DB=candidats_v14.json ATLAS_WORKERS=2 .venv/Scripts/python.exe collect_v14.py"""
import collect_v2 as C
Q = {
 "porc_caramelise_viet": ["thit rim", "Vietnamese caramelized pork", "caramel pork Vietnam"],
 "raviolis_sans_pliage_grilles": ["pan fried dumplings", "potstickers", "guotie"],
 "loc_lac": ["lok lak", "beef lok lak Cambodia", "loc lac"],
 "boeuf_saute_oeuf": ["beef with scrambled eggs Cantonese", "beef egg stir fry", "滑蛋牛肉"],
 "poulet_sel_poivre": ["salt and pepper chicken", "Taiwanese popcorn chicken", "yan su ji"],
 "goong_ob_woon_sen": ["goong ob woon sen", "baked shrimp glass noodles", "kung op wun sen"],
 "niu_rou_bing": ["niu rou bing", "beef pancake Chinese", "xian bing"],
 "aehobak_jeon": ["hobak jeon", "zucchini jeon", "Korean zucchini pancake"],
 "banh_cuon": ["banh cuon", "bánh cuốn", "Vietnamese steamed rice rolls"],
 "oeufs_crevettes_cantonais": ["shrimp scrambled eggs", "scrambled eggs with shrimp Chinese", "滑蛋虾仁"],
 "mayonnaise_japonaise": ["Kewpie mayonnaise", "Japanese mayonnaise", "mayonnaise bowl"],
 "poulet_caramel_croustillant": ["crispy caramel chicken", "honey garlic chicken crispy", "sweet glazed fried chicken"],
 "tenshindon": ["tenshindon", "tenshin-don", "crab omelette rice"],
 "niku_daikon": ["daikon nimono", "simmered daikon beef", "buri daikon"],
 "piman_nikuzume": ["stuffed green peppers Japanese", "piman nikuzume", "stuffed peppers meat"],
 "tanghulu": ["tanghulu", "bingtanghulu", "candied hawthorn skewer"],
}
C.ALL = {f"recette/{k}": v for k, v in Q.items()}
if __name__ == "__main__":
    db, keys = C.collect("")
    C.sheets(db, keys, "v14/")
