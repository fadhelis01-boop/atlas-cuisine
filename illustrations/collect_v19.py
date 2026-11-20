# -*- coding: utf-8 -*-
"""Photos des 22 fiches des favoris du 20/11/2026, + 4 reprises avec de meilleurs mots-clés (obleas, chaffle, baked
oats, nouilles à l'ail). Licences libres seulement. Usage :
ATLAS_DB=candidats_v19.json ATLAS_WORKERS=3 .venv/Scripts/python.exe collect_v19.py"""
import collect_v2 as C
Q = {
 "agnamahogo": ["cassava leaves coconut milk madagascar", "ravitoto"],
 "galette_oignons_pdt_fromage": ["potato onion gratin galette", "caramelized onion potato pie"],
 "paleron_boeuf_confit_7h": ["slow cooked beef chuck pot roast", "braised beef shoulder"],
 "pain_a_kebab_turc": ["turkish kebab bread ekmek", "pide bread kebab"],
 "tchantchanga": ["tchantchanga benin brochette", "beninese beef skewers"],
 "somun": ["somun bread bosnian", "bosnian flatbread cevapi"],
 "pain_brochette_ivoirien": ["pain brochette abidjan", "ivorian beef skewer sandwich"],
 "limonade_suisse": ["swiss lemonade limmilemonade", "creamy lemonade milk"],
 "duchess_potatoes": ["duchess potatoes"],
 "cube_bouillon_maison": ["homemade stock paste", "homemade bouillon cube vegetables"],
 "choukouya_poulet": ["choukouya poulet ivoirien", "grilled chicken ivorian maquis"],
 "riz_au_gras_togolais": ["riz au gras togo", "west african jollof rice simple"],
 "borani_banjan": ["borani banjan afghan eggplant", "afghan eggplant yogurt"],
 "panuzzo": ["panuzzo italian stuffed bread", "calzone panino cotto"],
 "french_dip_sandwich": ["french dip sandwich au jus"],
 "eclair_cake_sans_cuisson": ["no bake eclair cake", "chocolate eclair cake icebox"],
 "gnocchi_pain_rassis": ["bread gnocchi canederli", "stale bread dumplings italian"],
 "jambon_dinde_maison": ["homemade turkey ham", "homemade cooked ham slices"],
 "sauce_ranch_maison": ["ranch dressing homemade"],
 "crepes_gari_coco": ["cassava semolina pancake coconut", "gari pancake africa"],
 "chou_fleur_roti_feta_menthe": ["whole roasted cauliflower whipped feta", "roasted cauliflower feta pomegranate"],
 "tarte_poireaux_burrata_pistache": ["leek tart burrata", "rustic leek galette"],
 # reprises avec de meilleurs mots-clés
 "obleas_dulce_de_leche": ["obleas colombianas", "oblea bogota dulce de leche", "colombian wafer sandwich"],
 "chaffle": ["chaffle keto waffle sandwich", "cheese egg waffle keto"],
 "baked_oats": ["baked oats ramekin breakfast", "baked oatmeal single serving"],
 "nouilles_a_lail": ["buttery garlic noodles", "vietnamese garlic noodles parmesan"],
}
C.ALL = {f"recette/{k}": v for k, v in Q.items()}
if __name__ == "__main__":
    db, keys = C.collect("")
    C.sheets(db, keys, "v19/")
