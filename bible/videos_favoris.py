# -*- coding: utf-8 -*-
"""Favoris TikTok du 22/10/2026 et vidéos populaires des créateurs suivis : vidéos d'un plat DÉJÀ au catalogue (doublons),
rattachées à la fiche existante au lieu d'en créer une seconde. Relu à la main ; export_app_data.py les place juste après
la vidéo d'origine d'une fiche créditée, avant les vidéos trouvées par mots-clés."""

EN_PLUS = {
    "tiramisu": ["https://www.tiktok.com/@on_est_gourmands/video/7434200919992044832"],
    "chouquettes": ["https://www.tiktok.com/@lessecretsdegeoffrey/video/7558044102621711638", "https://www.tiktok.com/@lessecretsdegeoffrey/video/7627811887043955990"],
    "flan_patissier": ["https://www.tiktok.com/@dadyeats/video/7629424670533504278"],
    "shakshuka": ["https://www.tiktok.com/@comment_cuisiner/video/7472433118587161879"],
    "chich_taouk": ["https://www.tiktok.com/@lesgourmandisesdeloubna/video/7623041187984837910"],
    "oeufs_mimosa": ["https://www.tiktok.com/@comment_cuisiner/video/7584872463906016514"],
    "brioche": ["https://www.tiktok.com/@nicolaslepatissier/video/7631618917953228054"],
    "mousse_chocolat": ["https://www.tiktok.com/@nicolaslepatissier/video/7652398832365456673"],
    "attieke_poisson": ["https://www.tiktok.com/@cookwithbash/video/7512702148895902998", "https://www.tiktok.com/@cookwithbash/video/7645994199116008736"],
    "nuggets_maison": ["https://www.tiktok.com/@lesgourmandisesdeloubna/video/7574853556767886614", "https://www.tiktok.com/@comment_cuisiner/video/7636436087736454422"],
    "spaghetti_aglio_olio": ["https://www.tiktok.com/@bortipastabar/video/7683610348443782430"],
    "gateau_chocolat_famille": ["https://www.tiktok.com/@on_est_gourmands/video/7398190365330738464"],
    "fondant_chocolat": ["https://www.tiktok.com/@comment_cuisiner/video/7601567252269272342", "https://www.tiktok.com/@comment_cuisiner/video/7679102287385513248"],
    "jollof_rice": ["https://www.tiktok.com/@dadyeats/video/7639031335524273440", "https://www.tiktok.com/@dadyeats/video/7652022523722321185"],
    "poulet_yassa": ["https://www.tiktok.com/@comment_cuisiner/video/7533268279947791638"],
    "frango_piri": ["https://www.tiktok.com/@comment_cuisiner/video/7535865860389653782"],
    "thiakry": ["https://www.tiktok.com/@niangcook/video/7694697218556562721"],
    "boeuf_bourguignon": ["https://www.tiktok.com/@comment_cuisiner/video/7548489996135730455"],
    "nems_poulet": ["https://www.tiktok.com/@jerome.cuisine/video/7464552519591578902", "https://www.tiktok.com/@olivier.lin1/video/7695431670148680982", "https://www.tiktok.com/@jerome.cuisine/video/7616347425703316758"],
    "crepes_bretonnes": ["https://www.tiktok.com/@jerome.cuisine/video/7209601384424017157"],
    "pate_sucree": ["https://www.tiktok.com/@lessecretsdegeoffrey/video/7465039226652888342", "https://www.tiktok.com/@lessecretsdegeoffrey/video/7692102269608758561"],
    "poulet_kung_pao": ["https://www.tiktok.com/@olivier.lin1/video/7644616858217319702"],
    "japchae": ["https://www.tiktok.com/@olivier.lin1/video/7635599991964224790"],
    # même plat, autre vidéo de l'auteur crédité
    "mloukhiya": ["https://www.tiktok.com/@cookwithbash/video/7473945291176103190"],
    "tangia_marrakchia": ["https://www.tiktok.com/@recipes.elyanna04/video/7632762951606357270"],
    "crepe_cake_chocolat": ["https://www.tiktok.com/@on_est_gourmands/video/7195242445771132165", "https://www.tiktok.com/@on_est_gourmands/video/7350700353681100064"],
    "brioches_roulees_pate_tartiner": ["https://www.tiktok.com/@on_est_gourmands/video/7360345042348805408"],
}

# Favoris du 29/10/2026 et vidéos populaires de leurs auteurs : doublons d'un plat déjà au catalogue (relu à la main).
T = "https://www.tiktok.com/"
EN_PLUS_2026_10_29 = {
    "buttermilk_fried_chicken": [T + "@food.by.ibtissam/video/7587827288931142914", T + "@food.by.ibtissam/video/7559244481061555478"],
    "burger_maison": [T + "@food.by.ibtissam/video/7624920806392483094", T + "@food.by.ibtissam/video/7676137410773798176"],
    "shawarma_poulet": [T + "@food.by.ibtissam/video/7536978150643993879", T + "@food.by.ibtissam/video/7595993338566724886"],
    "brownies": [T + "@dinewithtwo/video/7567767793823763726"],
    "banana_bread": [T + "@dinewithtwo/video/7600435612528676126"],
    "cheeseburger_bombs": [T + "@dinewithtwo/video/7698005789201485070"],
    "attieke_poisson": [T + "@les.delice.d.ines/video/7536718495128603926", T + "@les.delice.d.ines/video/7580500765853142294"],
    "mayonnaise": [T + "@lardoise_porto_vecchio/video/7521259673719196950", T + "@lardoise_porto_vecchio/video/7484219316544539926", T + "@lardoise_porto_vecchio/video/7627521965812665622"],
    "aligot": [T + "@chesterfoodies/video/7422337174529461536", T + "@chesterfoodies/video/7662370900422954273"],
    "taboule_chou_fleur": [T + "@chesterfoodies/video/7654604752155725089"],
    "boeuf_bourguignon": [T + "@chesterfoodies/video/7423397331313216800", T + "@chesterfoodies/video/7679078839695215904"],
    "poulet_gaston_gerard": [T + "@chesterfoodies/video/7558530229078166806"],
    "soupe_oignon": [T + "@chesterfoodies/video/7427868141243469088"],
    "kedjenou": [T + "@les.delice.d.ines/video/7632622925568511234"],
    "pot_au_feu": [T + "@chesterfoodies/video/7425644785106472224"],
    "joues_boeuf_carottes": [T + "@chesterfoodies/video/7686875054948257057"],
    "tartiflette": [T + "@chesterfoodies/video/7678323490331577633"],
    "moussaka": [T + "@chesterfoodies/video/7677598088294337824"],
    "welsh": [T + "@chesterfoodies/video/7657547377854778656"],
    "bouillon_parures": [T + "@chesterfoodies/video/7696428061352381728"],
    "pickles_oignons_rouges": [T + "@lardoise_porto_vecchio/video/7646823808002706720"],
    "soupe_corse": [T + "@lardoise_porto_vecchio/video/7595846139077758230"],
    "pesto": [T + "@lardoise_porto_vecchio/video/7690875875805383968"],
    "the_glace_peche": [T + "@lardoise_porto_vecchio/video/7655669566386851105"],
    "adana_kebab": [T + "@food.by.ibtissam/video/7699148731186220321"],
    "sauce_burger": [T + "@lardoise_porto_vecchio/video/7700508131188690208", T + "@lardoise_porto_vecchio/video/7694593443263204640"],
    "sauce_algerienne": [T + "@lardoise_porto_vecchio/video/7583010721311624470", T + "@lardoise_porto_vecchio/video/7694980997271571745"],
    "sauce_poivre": [T + "@lardoise_porto_vecchio/video/7697241079808003361"],
    "vinaigrette": [T + "@lardoise_porto_vecchio/video/7583254947211545858", T + "@lardoise_porto_vecchio/video/7692371372147871009"],
    "bouillon_cube_maison": [T + "@lardoise_porto_vecchio/video/7688645663600495904"],
    "bouillon_legumes": [T + "@lardoise_porto_vecchio/video/7697926335582178592"],
    "sirop_menthe_maison": [T + "@lardoise_porto_vecchio/video/7686814575567703328"],
    "ketchup": [T + "@lardoise_porto_vecchio/video/7689776215929916704"],
    "salade_cesar_poulet": [T + "@lardoise_porto_vecchio/video/7633383719184715030"],
    "citronnade_menthe": [T + "@chefsquare/video/7668340432400649505"],
    "chai_masala": [T + "@chefsquare/video/7559537076341902614"],
    "falafels": [T + "@chefsquare/video/7566674397885369622"],
    "gratin_dauphinois": [T + "@hoplabretz/video/7619633614401195286"],
    "kartoffelsalat": [T + "@hoplabretz/video/7661229012781468950"],
    "bouchees_reine": [T + "@hoplabretz/video/7627792048732622102"],
    "carbonnade_flamande": [T + "@chesterfoodies/video/7642738597606493462"],
}
for _k, _v in EN_PLUS_2026_10_29.items():
    EN_PLUS[_k] = EN_PLUS.get(_k, []) + [u for u in _v if u not in EN_PLUS.get(_k, [])]

# Favoris du 04/11/2026 : doublons d'un plat déjà au catalogue (relu à la main).
EN_PLUS_2026_11_04 = {
    "sauce_chien": [T + "@jerome.cuisine/video/7703893892554296609"],
    "mayonnaise": [T + "@lardoise_porto_vecchio/video/7702846394905759008"],
    "sauce_curry_mango": [T + "@doscolafries/video/7703128211764301089"],
    "gigot_sept_heures": [T + "@qistoh/video/7670879439273659681"],
    "riz_saute_oeuf_express": [T + "@sosoya06/video/7704041039232879904"],
    "wrap_poulet_croquant": [T + "@zoyacooks7/video/7691391691617553696", T + "@zoyacooks7/video/7695849265750428961", T + "@zoyacooks7/video/7686568572369374497"],
    "burger_maison": [T + "@zoyacooks7/video/7693986679845063968"],
    "crevettes_coco_citron_vert": [T + "@zoyacooks7/video/7689542036965297440"],
    "poulet_frit_coreen": [T + "@sosoya06/video/7693472639456709920"],
    "steak_frites": [T + "@sosoya06/video/7694389690262228256"],
    "tartiflette": [T + "@sosoya06/video/7698285917739552032"],
    # 14 autres auteurs, lus le même jour (onglet « Populaire ») : vidéos de plats déjà dans ATLAS
    "plov": [T + "@ammey.food/video/7511742942386736406"],
    "tajine_poulet_olives": [T + "@ammey.food/video/7452398735688011030", T + "@ammey.food/video/7477247753098218774"],
    "tteokbokki": [T + "@ammey.food/video/7473535108264267030"],
    "poulet_yassa": [T + "@ammey.food/video/7439036993134202144"],
    "poulet_miel_ail_citron": [T + "@wellbraintips/video/7677648269509545246"],
    "mayonnaise_oeufs_durs": [T + "@wellbraintips/video/7686176859817643295", T + "@wellbraintips/video/7686908602052889886", T + "@wellbraintips/video/7684963433246215454", T + "@wellbraintips/video/7688441807146863903"],
    "cheesecake_yaourt": [T + "@wellbraintips/video/7680984557847432478"],
    "mafe_boeuf": [T + "@mohamedcheikh_/video/7659091554132413729"],
    "sauce_algerienne": [T + "@mohamedcheikh_/video/7431240014941490465"],
    "thiebou_yapp": [T + "@mohamedcheikh_/video/7656708048978726177"],
    "pastels_thon": [T + "@mohamedcheikh_/video/7664175387231948065", T + "@latelierdekhady/video/7682415146198699296"],
    "thiakry": [T + "@mohamedcheikh_/video/7663802750341336353"],
    "brioche": [T + "@lescasserolesdebineta/video/7417753492539854112"],
    "fataya": [T + "@lescasserolesdebineta/video/7462677829243686166"],
    "millefeuille": [T + "@lescasserolesdebineta/video/7587369340438121750"],
    "pain_au_lait": [T + "@lescasserolesdebineta/video/7519473682452942102"],
    "crepes_froment_sucre": [T + "@latelierdekhady/video/7674206904402349345"],
    "riz_cantonais_vegetarien": [T + "@latelierdekhady/video/7676053356627905824"],
    "attieke_poisson": [T + "@latelierdekhady/video/7672700182030519584"],
    "joues_boeuf_carottes": [T + "@latelierdekhady/video/7684936210359258401"],
    "thieboudienne": [T + "@latelierdekhady/video/7668755548883520800"],
    "buttermilk_fried_chicken": [T + "@simplylemmons/video/7599714638128827678", T + "@simplylemmons/video/7614270410846113055"],
    "burger_maison": [T + "@zoyacooks7/video/7693986679845063968", T + "@simplylemmons/video/7593867958732983583", T + "@qistoh/video/7254224406489206043", T + "@lacuisinedes.m.and.ms/video/7524992890456673559"],
    "orzo_poulet_cajun": [T + "@simplylemmons/video/7673597228384029982"],
    "tartines_sardines_citron": [T + "@totamsachikaroberts/video/7609029820181237006"],
    "tartine_sardines_oeufs_mollets": [T + "@totamsachikaroberts/video/7688576618075376909"],
    "salade_concombre_sesame": [T + "@sandencuisine/video/7639309876841270561"],
    "char_siu_poulet": [T + "@sandencuisine/video/7572145508911828246"],
    "dumplings_vapeur_legumes": [T + "@sandencuisine/video/7604435176562674966"],
    "riz_poulet_hainan": [T + "@sandencuisine/video/7552929831441206550"],
    "sauce_gombo_ivoirienne": [T + "@tiaghohilson/video/7692423086125108512"],
    "couscous_sept_legumes": [T + "@gourmmy/video/7636002326624488736"],
    "rfissa": [T + "@gourmmy/video/7574889120284101910"],
    "mechoui_four": [T + "@gourmmy/video/6951364123473038598"],
    "tangia_marrakchia": [T + "@gourmmy/video/7464917413906156822"],
    "medaillons_courgette_farcis": [T + "@qistoh/video/7259416246456683803"],
    "brochettes_boeuf_comte": [T + "@qistoh/video/7507291338623192342"],
    "crispy_chicken_caesar_burger": [T + "@qistoh/video/7259787910214372635"],
    "oeufs_cocotte": [T + "@qistoh/video/7241974201509350682"],
    "steak_frites": [T + "@sosoya06/video/7694389690262228256", T + "@qistoh/video/7213783224646946054"],
    "attieke_poisson": [T + "@latelierdekhady/video/7672700182030519584", T + "@tiaghohilson/video/7680237158719933728"],
    "ca_kho_to": [T + "@totamsachikaroberts/video/7627260892115111182"],
    "char_siu_poulet": [T + "@sandencuisine/video/7572145508911828246", T + "@sandencuisine/video/7700922284093017377"],
    "dumplings_vapeur_legumes": [T + "@sandencuisine/video/7604435176562674966", T + "@sandencuisine/video/7575121207201107202"],
    "ramen_miso_curry_coco_boeuf": [T + "@dishcovery_/video/7668998549098515715"],
    "boules_pomme_terre_mozzarella": [T + "@ammey.food/video/7549953973948828931"],
    "oeufs_brouilles_saumon_toast": [T + "@lacuisinedes.m.and.ms/video/7503107055838956822"],
    "thiebou_yapp": [T + "@mohamedcheikh_/video/7656708048978726177", T + "@latelierdekhady/video/7692752062030843168"],
    "sauce_tartare": [T + "@doscolafries/video/7674587766176664865"],
    "riz_saute_restes": [T + "@totamsachikaroberts/video/7657006717674212622"],
}
for _k, _v in EN_PLUS_2026_11_04.items():
    EN_PLUS[_k] = EN_PLUS.get(_k, []) + [u for u in _v if u not in EN_PLUS.get(_k, [])]

# favoris ajoutés entre le 04/11 et le 10/11/2026 : plats déjà dans ATLAS
EN_PLUS_2026_11_10 = {
    "croque_monsieur": [T + "@homerafaim/video/7706264703768612129"],
    "kebab_poulet_pain_maison": [T + "@ammey.food/video/7704370056569867553"],
    "croissants": [T + "@leo_hokfelt/video/7701991524896165142"],
    "poulet_roti": [T + "@lacuisinedemarina/video/7705078336464211232"],
    "sauce_tartare": [T + "@doscolafries/video/7674587766176664865", T + "@doscolafries/video/7697668755345739041"],
}
for _k, _v in EN_PLUS_2026_11_10.items():
    EN_PLUS[_k] = EN_PLUS.get(_k, []) + [u for u in _v if u not in EN_PLUS.get(_k, [])]

# auteurs des favoris du 10/11 (onglet « Populaire », lu le 10/11) : plats déjà dans ATLAS
EN_PLUS_2026_11_10_AUTEURS = {
    "nuggets_maison": [T + "@homerafaim/video/7677972329040858401"],
    "poulet_frit_coreen": [T + "@homerafaim/video/7677238645341883681"],
    "brochettes_boeuf_comte": [T + "@homerafaim/video/7679817167528873249"],
    "tenders_poulet_sauce_canes": [T + "@homerafaim/video/7677601530890997025", T + "@homerafaim/video/7676216816753986849"],
    "frites_maison": [T + "@homerafaim/video/7679029815994780961", T + "@amscooking/video/7690302572925701408"],
    "beignets_fourres_pate_tartiner": [T + "@homerafaim/video/7680245103423769889"],
    "gnocchi_gorgonzola_noix": [T + "@amscooking/video/7695857987784609056"],
    "pulled_chicken": [T + "@amscooking/video/7697376732860419361"],
    "magret_cerises": [T + "@amscooking/video/7598253878513093910", T + "@amscooking/video/7670285420260756768"],
    "nems_poulet": [T + "@dbzfaitmaison/video/7564414039711878422"],
    "focaccia": [T + "@dbzfaitmaison/video/7615631439471660291"],
    "puff_puff": [T + "@lacuisinedemarina/video/7593007659444374806"],
    "crepes_salees_enfants": [T + "@lacuisinedemarina/video/7572219324560198934"],
    "poisson_braise_camerounais": [T + "@lacuisinedemarina/video/7683930014949281057"],
    "jus_gingembre": [T + "@lacuisinedemarina/video/7692098813539978528"],
    "gratin_dauphinois": [T + "@leo_hokfelt/video/7703217604739075350"],
    "kebab_poulet_pain_maison": [T + "@ammey.food/video/7704370056569867553", T + "@leo_hokfelt/video/7705693803096722710"],
    "croissants": [T + "@leo_hokfelt/video/7701991524896165142", T + "@leo_hokfelt/video/7701991547415432470"],
}
for _k, _v in EN_PLUS_2026_11_10_AUTEURS.items():
    EN_PLUS[_k] = EN_PLUS.get(_k, []) + [u for u in _v if u not in EN_PLUS.get(_k, [])]

# 11/11/2026 : vidéos de recettes d'@erynshow déjà dans ATLAS
EN_PLUS_2026_11_11 = {
    "brochettes_boeuf_comte": [T + "@erynshow/video/7597169119452089622"],
}
for _k, _v in EN_PLUS_2026_11_11.items():
    EN_PLUS[_k] = EN_PLUS.get(_k, []) + [u for u in _v if u not in EN_PLUS.get(_k, [])]

# 11/11/2026 (suite) : vidéos de @lerizjaune et d'@erynshow rattachées à des fiches existantes ou nouvelles
EN_PLUS_2026_11_11B = {
    "gnocchi_gorgonzola_noix": [T + "@erynshow/video/7658739670422949152"],
    "gratin_ravioles": [T + "@erynshow/video/7608298481429630230"],
    "camembert_roti": [T + "@erynshow/video/7649013606276762912"],
    "pad_see_ew": [T + "@lerizjaune/video/7456104504191159574", T + "@erynshow/video/7617734013897280790"],
    "rouleaux_printemps": [T + "@erynshow/video/7612715880786496790"],
    "nouilles_beurre_cacahuete": [T + "@erynshow/video/7686369515050896673"],
    "sandwich_raclette_piquant": [T + "@erynshow/video/7646827372561435936"],
    "bubble_tea": [T + "@erynshow/video/7600122349500796182"],
    "chevre_miel_barbecue": [T + "@erynshow/video/7648646487194242337"],
    "boeuf_oignons_saute": [T + "@lerizjaune/video/7178912652024958214"],
    "nouilles_sautees_boeuf": [T + "@lerizjaune/video/7409332187104939296"],
    "vermicelles_soja_sautes": [T + "@lerizjaune/video/7508041440107236630"],
    "soupe_oeuf_chinoise": [T + "@lerizjaune/video/7305450085322738977"],
    "soupe_tomate_oeuf_chinoise": [T + "@lerizjaune/video/7702876538647186720"],
}
for _k, _v in EN_PLUS_2026_11_11B.items():
    EN_PLUS[_k] = EN_PLUS.get(_k, []) + [u for u in _v if u not in EN_PLUS.get(_k, [])]

# 11/11/2026 (suite) : cuisine italienne la plus vue (Max Mariola, GialloZafferano, Charlène & Francesca) sur des fiches existantes
_MM = T + "@chefmaxmariola/video/"; _CF = T + "@charlene_et_francesca/video/"; _GZ = T + "@giallozafferano/video/"
EN_PLUS_2026_11_11C = {
    "spaghetti_carbonara": [_MM + "7136878183244205318", _MM + "7172154197243186438", _CF + "7398471628159470880", _CF + "7290144031898635552"],
    "polpette_sugo": [_MM + "7203406118717115653"],
    "bucatini_amatriciana": [_MM + "7154780400844426502"],
    "pasta_alfredo_poulet": [_MM + "7292828979549981984"],
    "spaghetti_pomodoro_express": [_MM + "7157626384527953157"],
    "gnocchi_sorrentina": [_MM + "7162455620220718342"],
    "cacio_e_pepe": [_MM + "7234168952308436250"],
    "spaghetti_vongole": [_MM + "7149838585842109701"],
    "spaghetti_aglio_olio": [_MM + "7215996310057438469"],
    "tagliatelle_ragu": [_MM + "7305833732018064673"],
    "lasagnes_bolognaise": [_MM + "7323985505081740577", _CF + "7289415126611004705"],
    "carpaccio_boeuf": [_MM + "7243090200644160795"],
    "salade_caprese": [_MM + "7130297284088073477"],
    "pates_alla_norma": [_MM + "7266844307598937376"],
    "pates_puttanesca": [_MM + "7201826395998162181"],
    "risotto_champignons": [_MM + "7319176671494442272"],
    "pates_citron_parmesan": [_MM + "7211915409719676166"],
    "gnocchi_maison": [_CF + "7322045778455776545"],
    "bruschetta_tomates": [_CF + "7397382932848971041"],
    "crema_caffe": [_GZ + "7226305803144236315"],
    "pasta_e_patate": [_CF + "7602197034715729174"],
}
for _k, _v in EN_PLUS_2026_11_11C.items():
    EN_PLUS[_k] = EN_PLUS.get(_k, []) + [u for u in _v if u not in EN_PLUS.get(_k, [])]

# 12/11/2026 : vidéos asiatiques les plus vues de @cooking.with.morgane, @ryuji_tiktok_ et @cookingwithlynja rattachées aux fiches existantes
_MG = T + "@cooking.with.morgane/video/"; _RY = T + "@ryuji_tiktok_/video/"; _LY = T + "@cookingwithlynja/video/"
EN_PLUS_2026_11_12 = {
    "lok_lak": [_MG + "7348830791700434208"],
    "poulet_general_tao": [_MG + "7338858657053953313", _MG + "7606999825560767766"],
    "nems_poulet": [_MG + "7351723319235841313", _MG + "7614452329470856471"],
    "riz_saute_oeuf_express": [_MG + "7415152684530928929"],
    "riz_cantonais": [_MG + "7372601909863140641", _MG + "7333187090882120993"],
    "bao_poulet": [_MG + "7580769886985587990"],
    "chips_crevettes": [_MG + "7355960654211157280"],
    "ha_kao": [_MG + "7527674093936692502"],
    "beignets_crevettes_panes": [_MG + "7366654752639241504"],
    "rouleaux_printemps": [_MG + "7645676890904087840"],
    "tamago_sando": [_MG + "7604553403720535318"],
    "nuoc_cham": [_MG + "7354361499839728929", _MG + "7656490594109312288"],
    "tigre_qui_pleure": [_MG + "7564445925473553686", _MG + "7480985093411048726"],
    "poulet_frit_coreen": [_MG + "7361486363117571361"],
    "chop_suey_boeuf": [_MG + "7468594659451817238"],
    "soupe_wonton_poulet": [_MG + "7358182122323987744"],
    "feuilles_raviolis_maison": [_MG + "7600083682740702486"],
    "pad_see_ew": [_MG + "7483909539583200514"],
    "poulet_citronnelle_citron": [_MG + "7684186507468459296"],
    "salade_concombre_sesame": [_MG + "7663899389831810337"],
    "ramen_shoyu": [_MG + "7582931485292891414"],
    "huile_pimentee": [_MG + "7601573239524969750"],
    "takoyaki": [_MG + "7414493180265090336"],
    "momo_legumes": [_MG + "7416735318767930657"],
    "banh_mi": [_MG + "7424169186265517345"],
    "char_siu_poulet": [_MG + "7377390029905104160"],
    "pad_thai": [_MG + "7382980613697064224"],
    "bo_bun": [_MG + "7395597625979931937"],
    "ajitama": [_RY + "7601061699965275412", _MG + "7401152307649367328"],
    "udon_maison": [_MG + "7359964211100880160"],
    "maki_maison": [_MG + "7364315341683543329"],
    "tsukune": [_MG + "7637467511058894102"],
    "chapati": [_MG + "7657823924096388385"],
    "gyoza": [_MG + "7432347014785994017", _MG + "7643528911640415520"],
    "nouilles_sautees_boeuf": [_MG + "7635241550796180758", _MG + "7553168364844125462"],
    "nouilles_sautees_legumes_oeuf": [_MG + "7369249165576031520", _MG + "7440122598249254176", _MG + "7606289975046458646"],
    "boeuf_oignons_saute": [_MG + "7554416557456100630"],
    "poulet_citron_chinois": [_MG + "7443400151160343840"],
    "salade_japonaise_pommes_de_terre": [_MG + "7702761937280535840"],
    "karaage": [_RY + "7500505952542674183"],
    "kulfi": [_LY + "7094639677898034475"],
}
for _k, _v in EN_PLUS_2026_11_12.items():
    EN_PLUS[_k] = EN_PLUS.get(_k, []) + [u for u in _v if u not in EN_PLUS.get(_k, [])]
