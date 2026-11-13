# -*- coding: utf-8 -*-
"""Photos des 42 fiches de l'audit des manques TikTok (13/11/2026, AUDIT_MANQUES_TIKTOK_2026-11-13.md). Licences libres
seulement. Usage : ATLAS_DB=candidats_v18.json ATLAS_WORKERS=3 .venv/Scripts/python.exe collect_v18.py"""
import collect_v2 as C
Q = {
 # desserts manquants
 "rasmalai": ["rasmalai", "rasmalai dessert indian"],
 "gajar_halwa": ["gajar halwa", "carrot halwa indian dessert"],
 "barfi": ["barfi indian sweet", "kaju barfi"],
 "ladoo": ["besan ladoo", "ladoo indian sweet"],
 "falooda": ["falooda dessert", "falooda drink rose"],
 "maamoul": ["maamoul cookies", "maamoul dates lebanese"],
 "qatayef": ["qatayef dessert", "atayef ramadan"],
 "sutlac": ["sütlaç turkish rice pudding", "turkish rice pudding baked"],
 "halo_halo": ["halo halo dessert", "halo-halo filipino shaved ice"],
 "leche_flan": ["leche flan filipino", "filipino flan caramel"],
 "bibingka": ["bibingka filipino rice cake", "bibingka christmas"],
 "turon": ["turon banana filipino", "turon lumpia dessert"],
 "quindim": ["quindim brazilian dessert"],
 "picarones": ["picarones peru dessert", "picarones donuts"],
 # Philippines et classiques
 "sisig": ["sisig filipino", "pork sisig sizzling"],
 "lechon_kawali": ["lechon kawali", "crispy pork belly filipino"],
 "kare_kare": ["kare-kare filipino", "kare kare peanut stew"],
 "dosa_instantane": ["dosa indian crepe", "masala dosa"],
 "xiaolongbao": ["xiaolongbao", "soup dumplings chinese"],
 "asado_argentin": ["asado argentina", "argentinian bbq grill beef"],
 "bangers_mash": ["bangers and mash"],
 "haggis_facon_maison": ["haggis neeps tatties", "haggis scottish"],
 "bandeja_paisa": ["bandeja paisa"],
 "patacones": ["patacones tostones plantain", "tostones fried plantain"],
 "bunuelos_colombianos": ["buñuelos colombianos", "colombian bunuelos christmas"],
 "obleas_dulce_de_leche": ["obleas colombianas", "obleas dulce de leche wafer"],
 "completo_italiano": ["completo italiano chilean hot dog", "chilean hotdog avocado"],
 # correctif végé
 "pates_feta_au_four": ["baked feta pasta"],
 "nouilles_a_lail": ["garlic noodles"],
 "saag_paneer": ["saag paneer"],
 # tendances virales
 "smash_burger": ["smash burger"],
 "dalgona_coffee": ["dalgona coffee"],
 "butter_board": ["butter board appetizer"],
 "chaffle": ["chaffle keto waffle"],
 "baked_oats": ["baked oats breakfast"],
 "birria_ramen": ["birria ramen"],
 "chocolat_dubai": ["dubai chocolate bar", "kunafa chocolate pistachio"],
 "cinnamon_rolls": ["cinnamon rolls frosting"],
 "red_velvet_cake": ["red velvet cake"],
 "trifle_anglais": ["english trifle dessert"],
 "corn_ribs": ["corn ribs"],
 "cronut": ["cronut pastry"],
}
C.ALL = {f"recette/{k}": v for k, v in Q.items()}
if __name__ == "__main__":
    db, keys = C.collect("")
    C.sheets(db, keys, "v18/")
