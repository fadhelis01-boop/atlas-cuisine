# -*- coding: utf-8 -*-
"""Photos des 33 fiches de l'audit street food (12/11/2026). Licences libres seulement.
Usage : ATLAS_DB=candidats_v16.json ATLAS_WORKERS=3 .venv/Scripts/python.exe collect_v16.py"""
import collect_v2 as C
Q = {
 "esquites": ["esquites", "esquite cup Mexico", "corn in a cup Mexican"], "tlayuda": ["tlayuda", "tlayudas Oaxaca", "tlayuda oaxaqueña"],
 "sopes": ["sopes mexicanos", "sopes food", "sope Mexican"], "hot_dog_maison": ["hot dog", "hot dog onions mustard", "hot dog bun"],
 "philly_cheesesteak": ["Philly cheesesteak", "cheesesteak sandwich", "cheesesteak Philadelphia"], "anticuchos": ["anticuchos", "anticucho Peru", "anticuchos de corazón"],
 "choripan": ["choripán", "choripan chimichurri", "choripan Argentina"], "coxinha": ["coxinha", "coxinhas", "coxinha de frango"],
 "acaraje": ["acarajé", "acaraje Bahia", "acarajé Salvador"], "salchipapa": ["salchipapa", "salchipapas", "salchipapa Peru"],
 "doubles_trinidad": ["doubles Trinidad", "doubles channa", "Trinidad doubles food"], "jamaican_patty": ["Jamaican patty", "Jamaican beef patty", "beef patties Jamaica"],
 "galette_saucisse_volaille": ["galette-saucisse", "galette saucisse Rennes", "galette saucisse"], "panisse": ["panisse", "panisses Marseille", "chickpea fries"],
 "suppli": ["supplì", "suppli Rome", "supplì al telefono"], "piadina": ["piadina", "piadina romagnola", "piadina sandwich"],
 "langos": ["lángos", "langos Hungary", "lángos sour cream cheese"], "zapiekanka": ["zapiekanka", "zapiekanki", "zapiekanka Kraków"],
 "trdelnik": ["trdelník", "trdelnik Prague", "chimney cake"], "sabich": ["sabich", "sabich sandwich", "sabich pita"],
 "kumpir": ["kumpir", "kumpir Ortaköy", "stuffed baked potato Turkish"], "tantuni": ["tantuni", "tantuni Mersin", "tantuni dürüm"],
 "balik_ekmek": ["balık ekmek", "balik ekmek Eminönü", "fish sandwich Istanbul"], "bambalouni": ["bambalouni", "bambaloni Tunisia", "Tunisian doughnut"],
 "mahjouba": ["mhadjeb", "mahjouba", "m'hadjeb Algeria"], "rolex_ouganda": ["rolex Uganda", "Ugandan rolex", "rolex street food Kampala"],
 "akara_niebe": ["akara", "akara bean fritters", "accara Senegal"], "jianbing": ["jianbing", "jian bing", "煎饼果子"],
 "eomuk_tang": ["eomuk", "odeng skewers", "fish cake skewers Korea"], "martabak_manis": ["martabak manis", "terang bulan", "martabak manis chocolate"],
 "roujiamo_boeuf": ["roujiamo", "rou jia mo", "肉夹馍"], "egg_waffle": ["egg waffle Hong Kong", "gai daan jai", "bubble waffle"],
 "dan_bing": ["dan bing", "Taiwanese egg crepe", "蛋餅"],
}
C.ALL = {f"recette/{k}": v for k, v in Q.items()}
if __name__ == "__main__":
    db, keys = C.collect("")
    C.sheets(db, keys, "v16/")
