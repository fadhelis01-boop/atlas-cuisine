# -*- coding: utf-8 -*-
"""Photos des 42 fiches de l'audit « cuisines d'Asie » (12/11/2026). Licences libres seulement (Commons, Openverse).
Usage : ATLAS_DB=candidats_v13.json ATLAS_WORKERS=2 .venv/Scripts/python.exe collect_v13.py"""
import collect_v2 as C
Q = {
 "xiao_long_bao": ["xiaolongbao", "soup dumplings Shanghai", "xiao long bao steamer"],
 "hong_shao_rou": ["hong shao rou", "red braised pork belly", "braised pork belly Chinese"],
 "agneau_cumin_xinjiang": ["cumin lamb stir fry", "ziran lamb", "Xinjiang lamb dish"],
 "mantou": ["mantou steamed bun", "Chinese steamed buns plain", "mantou bread"],
 "dan_tat": ["egg tart Hong Kong", "dan tat", "Chinese egg tarts"],
 "takoyaki": ["takoyaki", "takoyaki Osaka", "octopus balls Japanese"],
 "sukiyaki": ["sukiyaki", "sukiyaki pot", "sukiyaki beef"],
 "yakisoba": ["yakisoba", "yakisoba noodles", "Japanese fried noodles"],
 "dorayaki": ["dorayaki", "dorayaki red bean", "Japanese pancake red bean"],
 "agedashi_tofu": ["agedashi tofu", "agedashi dofu", "fried tofu dashi"],
 "samgyetang": ["samgyetang", "ginseng chicken soup Korean", "samgye-tang"],
 "jajangmyeon": ["jajangmyeon", "jjajangmyeon", "black bean noodles Korean"],
 "doenjang_jjigae": ["doenjang jjigae", "soybean paste stew Korean", "doenjang-jjigae"],
 "hotteok": ["hotteok", "Korean sweet pancake", "hoddeok"],
 "buuz": ["buuz", "Mongolian dumplings", "buuz Mongolia"],
 "vindaloo": ["vindaloo", "pork vindaloo", "Goan vindaloo"],
 "khichdi": ["khichdi", "khichri rice lentils", "kichari"],
 "poha": ["poha", "kanda poha", "poha breakfast India"],
 "rava_idli": ["rava idli", "idli", "idli sambar"],
 "vada_pav": ["vada pav", "vada pao Mumbai", "batata vada"],
 "pani_puri": ["pani puri", "golgappa", "panipuri"],
 "rasam": ["rasam", "rasam soup", "tomato rasam"],
 "kulfi": ["kulfi", "kulfi pistachio", "kulfi ice cream"],
 "jalebi": ["jalebi", "jalebi sweets", "jilapi"],
 "dal_bhat": ["dal bhat", "dal bhat Nepal", "Nepali thali"],
 "momo_legumes": ["momo dumplings Nepal", "momos", "Nepali momo"],
 "thukpa": ["thukpa", "thukpa noodle soup", "Tibetan noodle soup"],
 "shorshe_maach": ["shorshe ilish", "mustard fish curry Bengali", "shorshe maach"],
 "panang_poulet": ["panang curry", "phanaeng curry chicken", "panang chicken"],
 "gai_yang": ["gai yang", "kai yang grilled chicken", "Thai grilled chicken"],
 "com_tam": ["com tam", "cơm tấm", "broken rice Vietnamese pork chop"],
 "bun_bo_hue": ["bun bo Hue", "bún bò Huế", "Hue beef noodle soup"],
 "cha_ca_hanoi": ["cha ca La Vong", "chả cá Hà Nội", "Hanoi turmeric fish dill"],
 "char_kway_teow": ["char kway teow", "char kuey teow", "fried flat rice noodles Penang"],
 "kaya_toast": ["kaya toast", "kaya toast Singapore", "kaya butter toast"],
 "mohinga": ["mohinga", "mohinga Burmese", "Burmese fish noodle soup"],
 "lagman": ["lagman", "laghman noodles", "lagman Uzbek"],
 "nasu_dengaku": ["nasu dengaku", "miso glazed eggplant", "eggplant dengaku"],
 "teh_tarik": ["teh tarik", "pulled tea Malaysia", "teh tarik glass"],
 "cha_yen": ["Thai iced tea", "cha yen", "Thai tea"],
 "ca_phe_sua_da": ["ca phe sua da", "Vietnamese iced coffee", "cà phê sữa đá"],
 "boricha": ["boricha", "barley tea", "roasted barley tea"],
}
C.ALL = {f"recette/{k}": v for k, v in Q.items()}
if __name__ == "__main__":
    db, keys = C.collect("")
    C.sheets(db, keys, "v13/")
