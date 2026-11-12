# -*- coding: utf-8 -*-
"""Photos des classiques français ajoutés par l'audit « fin gourmet » (12/11/2026). Licences libres seulement
(Commons, Openverse), jamais générées.
Usage : ATLAS_DB=candidats_v11.json ATLAS_WORKERS=2 .venv/Scripts/python.exe collect_v11.py"""
import collect_v2 as C
Q = {
 "steak_au_poivre": ["steak au poivre", "pepper steak cream sauce"], "canard_orange": ["canard à l'orange", "duck à l'orange"], "tete_de_veau_gribiche": ["tête de veau", "calf's head gribiche"],
 "pate_en_croute": ["pâté en croûte", "pate en croute slice"], "foie_gras_mi_cuit": ["foie gras terrine", "foie gras toast"], "waterzoi_poulet": ["waterzooi", "waterzooi chicken"],
 "andouillette_moutarde": ["andouillette", "andouillette moutarde"], "boudin_noir_pommes": ["boudin noir pommes", "black pudding apples"], "pommes_dauphine": ["pommes dauphine", "dauphine potatoes"],
 "pommes_anna": ["pommes Anna", "potatoes Anna"], "pommes_boulangere": ["pommes boulangère", "boulangere potatoes"], "vichyssoise": ["vichyssoise", "cold leek potato soup"],
 "artichauts_vinaigrette": ["artichoke vinaigrette", "artichaut vinaigrette"], "cuisses_grenouilles_persillade": ["cuisses de grenouilles", "frog legs garlic parsley"], "cervelle_de_canut": ["cervelle de canut", "fromage blanc herbs Lyon"],
 "ris_de_veau_morilles": ["ris de veau", "sweetbreads morels"], "rognons_veau_moutarde": ["rognons de veau", "veal kidneys mustard"], "foie_veau_persillade": ["foie de veau", "calf liver persillade"],
 "civet_chevreuil": ["civet de chevreuil", "venison stew"], "pintade_choux": ["pintade au chou", "guinea fowl cabbage"], "pigeon_petits_pois": ["pigeon petits pois", "roast pigeon peas"],
 "fond_brun_veau": ["veal stock", "fond brun"], "fond_blanc_volaille": ["chicken stock pot", "white stock"], "fumet_poisson": ["fish stock", "fumet de poisson"], "court_bouillon": ["court-bouillon", "court bouillon pot"],
 "sauce_mornay": ["Mornay sauce", "sauce Mornay"], "sauce_bordelaise": ["entrecôte bordelaise", "bordelaise sauce"], "sauce_choron": ["sauce Choron", "béarnaise tomato sauce"],
 "sauce_ravigote": ["sauce ravigote", "ravigote"], "sauce_soubise": ["sauce Soubise", "onion cream sauce"], "sauce_morilles": ["morels cream sauce", "poulet au vin jaune morilles"],
 "sauce_poivrade": ["sauce poivrade", "game sauce pepper"], "raie_beurre_noisette_capres": ["raie aux câpres", "skate wing capers"], "truite_amandes": ["truite aux amandes", "trout almonds"],
 "maquereaux_vin_blanc": ["maquereaux au vin blanc", "marinated mackerel white wine"], "thon_basquaise": ["thon basquaise", "tuna piperade"], "langoustines_mayonnaise": ["langoustines", "langoustines mayonnaise"],
 "homard_grille_beurre": ["grilled lobster", "homard grillé"], "tourteau_mayonnaise": ["tourteau", "brown crab mayonnaise"], "encornets_persillade": ["encornets persillade", "squid garlic parsley"],
 "bulots_aioli": ["bulots", "whelks mayonnaise"], "pate_a_choux": ["pâte à choux", "choux pastry"], "religieuse_chocolat": ["religieuse", "religieuse pastry"],
 "saint_honore": ["Saint-Honoré gâteau", "gâteau Saint-Honoré"], "opera": ["gâteau opéra", "opera cake"], "bavarois_framboise": ["bavarois", "raspberry bavarois"],
 "peche_melba": ["pêche Melba", "peach melba"], "vacherin_glace": ["vacherin glacé", "vacherin meringue ice cream"], "succes_praline": ["dacquoise", "succès praliné"],
 "merveilleux": ["merveilleux", "merveilleux meringue"], "puits_amour": ["puits d'amour", "puits d'amour pâtisserie"], "nonnettes_dijon": ["nonnettes", "pain d'épices nonnettes"],
 "calissons_aix": ["calissons", "calisson d'Aix"], "pates_de_fruits": ["pâtes de fruits", "pate de fruit"], "pain_aux_raisins": ["pain aux raisins", "pain aux raisins viennoiserie"],
 "pain_viennois": ["pain viennois", "viennese bread baguette"], "pralines_roses": ["pralines roses", "pink pralines Lyon"], "civet_lievre": ["civet de lièvre", "hare stew"],
 "daube_sanglier": ["daube de sanglier", "wild boar stew"], "faisan_chou_cocotte": ["faisan", "roast pheasant"], "pithiviers_amandes": ["pithiviers", "pithiviers pastry"],
 "sauce_diable": ["sauce diable", "devil sauce"], "sauce_charcutiere": ["sauce charcutière", "pork chop mustard gherkin sauce"],
}
C.ALL = {f"recette/{k}": v for k, v in Q.items()}
if __name__ == "__main__":
    db, keys = C.collect("")
    C.sheets(db, keys, "v11/")
