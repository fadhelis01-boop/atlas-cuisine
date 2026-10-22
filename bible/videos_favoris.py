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
