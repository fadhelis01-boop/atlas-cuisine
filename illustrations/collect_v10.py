# -*- coding: utf-8 -*-
"""Photos des fiches ajoutées le 11-12/11/2026 (Togo, haoussa, Le Riz Jaune, Eryn, végétariens, italien TikTok).
Recherche en anglais ou sous le nom d'origine. Photos sous licence libre seulement (Commons, Openverse), jamais générées.
Usage : ATLAS_DB=candidats_v10.json ATLAS_WORKERS=2 .venv/Scripts/python.exe collect_v10.py"""
import collect_v2 as C
Q = {
 # Togo, haoussa
 "akoume": ["akple corn dough", "banku"], "gboma_dessi": ["gboma dessi", "spinach stew Togo"], "ademe_dessi": ["ademe sauce", "jute leaves stew"],
 "fetri_dessi": ["okra soup Togo", "okra stew seafood"], "azi_dessi": ["groundnut soup chicken", "peanut soup West Africa"], "koklo_meme": ["grilled chicken Togo", "West African grilled chicken"],
 "djenkoume": ["djenkoume", "red corn dough"], "fufu_igname": ["pounded yam", "fufu"], "koliko": ["yam chips", "fried yam"],
 "pinon": ["gari tomato", "eba"], "klaklou": ["plantain fritters", "kaklo"], "atchomon": ["chin chin", "chin chin snack"],
 "yaji": ["suya spice", "yaji spice"], "suya_poulet": ["chicken suya", "suya skewers"], "tsire_agneau": ["tsire", "suya meat skewers"],
 "kilishi": ["kilishi", "dried meat jerky Nigeria"], "balangu": ["balangu", "grilled ram meat Nigeria"], "dambun_nama": ["dambun nama", "meat floss"],
 "masa_haoussa": ["masa rice cakes", "waina"], "dan_wake": ["dan wake", "bean dumplings Nigeria"], "miyan_taushe": ["miyan taushe", "pumpkin soup Nigeria"],
 "ayimolou": ["rice and beans Togo", "waakye"], "abobo": ["beans palm oil gari", "red red beans"],
 # Le Riz Jaune
 "boeuf_sauce_huitre": ["beef oyster sauce", "oyster sauce beef stir fry"], "boeuf_gingembre": ["ginger beef scallion", "ginger scallion beef"], "boeuf_brocoli": ["beef and broccoli", "Chinese beef broccoli"],
 "chop_suey_boeuf": ["beef chop suey", "chop suey"], "tigre_qui_pleure": ["crying tiger beef", "suea rong hai"], "poulet_citron_chinois": ["Chinese lemon chicken", "lemon chicken"],
 "poulet_orange": ["orange chicken", "orange chicken rice"], "ailes_poulet_aigre_douce": ["sweet and sour chicken wings", "sticky chicken wings"], "crevettes_sauce_piquante": ["chili prawns", "spicy shrimp stir fry"],
 "crevettes_sel_poivre": ["salt and pepper shrimp", "salt pepper prawns"], "chou_chinois_farci_volaille": ["stuffed napa cabbage rolls", "cabbage rolls steamed"], "katsudon_poulet": ["katsudon", "chicken katsudon"],
 "katsu_sando": ["katsu sando", "katsu sandwich"], "vermicelles_soja_sautes": ["stir fried glass noodles", "glass noodles chicken"], "yum_woon_sen": ["yum woon sen", "glass noodle salad Thai"],
 "ha_kao": ["har gow", "har gow dim sum"], "siu_mai": ["siu mai", "shumai"], "raviolis_frits_crevettes": ["fried wontons", "fried wonton shrimp"],
 "baozi_poeles_poulet": ["sheng jian bao", "pan fried buns"], "soupe_pekinoise": ["hot and sour soup", "suan la tang"], "soupe_oeuf_chinoise": ["egg drop soup", "egg flower soup"],
 "soupe_tomate_oeuf_chinoise": ["tomato egg drop soup", "tomato egg soup"], "soupe_mais_chinoise": ["corn egg drop soup", "Chinese corn soup"], "poulet_concombre_saute": ["stir fried cucumber", "cucumber chicken stir fry"],
 "kimchi_blanc": ["baek kimchi", "white kimchi"], "yaki_onigiri": ["yaki onigiri", "grilled rice ball"], "tteok_maison": ["garaetteok", "rice cake sticks"],
 "udon_maison": ["homemade udon", "udon noodles"], "feuilles_raviolis_maison": ["dumpling wrappers", "homemade dumpling wrappers"], "sauce_sriracha_maison": ["sriracha sauce", "homemade sriracha"],
 "chips_crevettes": ["prawn crackers", "krupuk"], "nouilles_biang_biang": ["biangbiang noodles", "biang biang mian"], "korokke": ["korokke", "Japanese croquette"],
 "bubble_tea": ["bubble tea", "brown sugar bubble tea"], "mochi_glace": ["mochi ice cream", "mochi ice"], "nougat_chinois": ["peanut sesame nougat", "Chinese peanut candy"],
 "jian_dui": ["jian dui", "sesame balls"], "perles_coco": ["coconut balls glutinous rice", "nuo mi ci"], "taiyaki": ["taiyaki", "taiyaki red bean"],
 "kkwabaegi": ["kkwabaegi", "twisted doughnuts Korean"], "gateaux_de_lune_coco_matcha": ["snow skin mooncake", "mooncake"],
 # Eryn
 "pates_chevre_miel": ["goat cheese pasta honey", "goat cheese pasta"], "pates_burrata_pesto": ["burrata pesto pasta", "pasta burrata"], "burrata_pesto_rosso": ["burrata", "burrata appetizer"],
 "pates_crevettes_pesto_rosso": ["shrimp pasta sun dried tomato pesto", "shrimp penne"], "pates_riz_sautees_carottes": ["stir fried rice noodles carrot", "fried rice noodles egg"], "gyozas_poulet_cheddar": ["gyoza", "pan fried gyoza"],
 "raviolis_boeuf_fromage": ["beef dumplings pan fried", "half moon dumplings"], "nam_tok_boeuf": ["nam tok", "Thai beef salad"], "chevre_miel_barbecue": ["grilled goat cheese honey", "baked goat cheese"],
 "sandwich_champignons_chevre": ["mushroom goat cheese sandwich", "mushroom sandwich"], "mont_dor_champignons_epinards": ["Mont d'Or cheese baked", "vacherin Mont d'Or"], "sorbet_coco_antillais": ["coconut sorbet", "coconut ice cream"],
 # végétariens
 "tofu_aigre_doux": ["sweet and sour tofu", "sweet sour tofu pineapple"], "tofu_sauce_piquante": ["spicy tofu stir fry", "chili tofu"], "tofu_chou_chinois_saute": ["napa cabbage stir fry", "cabbage tofu stir fry"],
 "nouilles_froides_sesame": ["cold sesame noodles", "liang mian"], "pajeon": ["pajeon", "Korean scallion pancake"], "korokke_mais_fromage": ["corn croquettes", "cream croquettes corn"],
 "udon_gochujang_legumes": ["gochujang udon", "stir fried udon vegetables"], "nouilles_tomate_oeuf": ["tomato egg noodles", "tomato egg noodle soup"],
 # italien TikTok
 "gricia_version": ["pasta alla gricia", "gricia"], "pasta_e_patate": ["pasta e patate", "pasta with potatoes"], "pici_aglione": ["pici all'aglione", "pici pasta"],
 "fettuccine_burro_asperges": ["fettuccine alfredo butter parmesan", "fettuccine asparagus"], "pasta_pecorara": ["pasta alla pecorara", "pasta ricotta vegetables"], "linguine_crabe": ["linguine crab", "spaghetti granchio"],
 "penne_arrabbiata": ["penne all'arrabbiata", "penne arrabbiata"], "linguine_moules_scarole": ["linguine mussels", "pasta cozze"], "pasta_burro_alici": ["pasta anchovies butter", "spaghetti anchovy breadcrumbs"],
 "rigatoni_brocoli_saucisse": ["pasta broccoli sausage", "orecchiette broccoli salsiccia"], "paccheri_crevettes_tomates_cerises": ["paccheri shrimp", "paccheri gamberi"], "ravioli_courge_gorgonzola": ["pumpkin ravioli", "butternut squash ravioli"],
 "trippa_romana": ["trippa alla romana", "tripe tomato Rome"], "filet_poivre_vert": ["beef fillet green pepper sauce", "steak au poivre"], "alici_marinate": ["alici marinate", "marinated anchovies"],
 "polpo_lesso_salade": ["octopus potato salad", "insalata di polpo"], "impepata_cozze": ["impepata di cozze", "mussels pepper"], "mozzarella_in_carrozza": ["mozzarella in carrozza", "fried mozzarella sandwich"],
 "panzerotti": ["panzerotti", "panzerotto"], "mozzarella_in_purgatorio": ["mozzarella tomato sauce baked", "mozzarella in tomato sauce"], "uova_in_purgatorio": ["uova in purgatorio", "eggs in tomato sauce"],
}
C.ALL = {f"recette/{k}": v for k, v in Q.items()}
if __name__ == "__main__":
    db, keys = C.collect("")
    C.sheets(db, keys, "v10/")
