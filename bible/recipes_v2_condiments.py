# -*- coding: utf-8 -*-
"""Vague 2 · Condiments, bases et marinades maison, sans additifs (bouillon cube, nokoss, épices, marinades du monde)."""
from recipes_v2_base import *

KEEP_F = "1 mois au frigo dans un bocal propre."

K("bouillon_cube_maison", "Bouillon « cube » maison de légumes (pâte)", "Bouillon de légumes concentré", "France › Cuisine de base", "Ba", 1, 40, 25, 25, "€", "Mixeur, sauteuse, bocaux.",
  "Tout le goût d'un bouillon cube, sans exhausteur, sans huile de palme, sans arôme : des légumes, des herbes et du sel qui conserve. 1 c. à c. pour 50 cl d'eau.",
  [f"2|carottes|{CAROTTE}|2", "1|poireau|Poireau|2", "2|branches de céleri avec feuilles|Céleri-branche|2", f"1|oignon|{OIG}|2", f"2|tomates|{TOM}|1", f"4 gousses|d'ail|{AIL}|1", f"1 bouquet|de persil|{PERSIL}|1", f"2 branches|de thym + 1 feuille de laurier|{THYM}|1", "150 g|de gros sel (15 % du poids des légumes)|Sel fin / gros sel / fleur de sel|3", f"1 c. à s.|d'huile d'olive|{HO}|0"],
  ["**Mixer.** Tous les légumes et herbes très finement (environ 1 kg), avec le sel.", "**Réduire.** 20-25 min à feu moyen en remuant, jusqu'à ce que l'eau s'évapore et que la pâte se détache des bords.", "**Conserver.** En bocal ébouillanté, tassé, filet d'huile dessus."],
  keep="6 mois au frigo (grâce au sel) ; ou en glaçons au congélateur.", age=None, kids="✓ dès 1 an, très dilué (c'est très salé : pas de sel en plus).", cats=["sauces", "zero_dechet"], profil=["leger"], tech=["Bouillon cube"],
  tips=["Version volaille : ajoute 200 g de blanc de poulet haché cuit avec les légumes ; congèle-la.", "Fanes de carottes, verts de poireaux et queues de persil : parfaits ici."])

K("bouillon_poudre_maison", "Bouillon en poudre maison (légumes séchés)", "Bouillon en poudre", "France › Cuisine de base", "Ba", 1, 50, 20, 480, "€", "Four (chaleur tournante), mixeur, bocal hermétique.",
  "Une poudre à saupoudrer dans soupes, riz et sauces : légumes séchés au four, mixés avec sel, herbes et levure maltée.",
  [f"3|carottes|{CAROTTE}|2", "1|poireau|Poireau|2", "1|branche de céleri|Céleri-branche|2", f"2|oignons|{OIG}|2", "6|champignons de Paris|Champignon de Paris|2", f"1 bouquet|de persil|{PERSIL}|1", "60 g|de sel fin|Sel fin / gros sel / fleur de sel|2", f"1 c. à c.|de curcuma|{CURC}|1", "2 c. à s.|de levure maltée (paillettes, facultatif)|Malt d'orge (poudre)|1?"],
  ["**Trancher.** Légumes et champignons en lamelles de 2 mm.", "**Sécher.** 6-8 h au four à 60 °C porte entrouverte : ils doivent casser net.", "**Mixer.** En poudre fine avec sel, curcuma, levure maltée. Bocal bien sec."],
  keep="6 mois au sec, à l'abri de la lumière.", age=None, kids="✓ dès 1 an, en petite quantité.", cats=["sauces", "zero_dechet"], profil=["leger"], tech=["Bouillon cube"])

K("nokoss", "Nokoss sénégalais", "Nokoss (roof)", "Afrique subsaharienne › Sénégal", "Ba", 1, 10, 15, 0, "€", "Mortier ou mixeur.",
  "La pâte aromatique de la cuisine sénégalaise : ail, oignon, poivron, piment, persil, poivre. Elle farcit le poisson du thiéboudienne et parfume yassa, mafé, sauces.",
  [f"1 tête|d'ail|{AIL}|3", f"1|oignon|{OIG}|2", f"1|poivron vert|{POIVRON}|2", "1|piment antillais (selon goût)|Piment antillais / scotch bonnet|2", f"1 bouquet|de persil|{PERSIL}|2", "2|oignons nouveaux|Oignon nouveau / cébette|1", f"1 c. à c.|de poivre noir|{POIVRE}|1", "1 c. à c.|de pâte de bouillon maison (ou de sel)|SUB:bouillon_cube_maison|1", f"2 c. à s.|d'huile|{HN}|1"],
  ["**Piler.** Ail, oignons, poivron, piment, persil, poivre, bouillon : pâte grossière, pas une purée.", "**Utiliser.** Entaille un poisson et glisse le nokoss dans les fentes ; ou une cuillère dans une sauce en début de cuisson."],
  keep="1 semaine au frigo sous une couche d'huile ; 3 mois en glaçons.", age=3, kids="✓ dès 3 ans sans piment (mets-le entier dans la sauce).", cats=["sauces"], profil=["epice"], tech=["Nokoss"])

K("marinade_yassa", "Marinade yassa (citron, oignon, moutarde)", "Yassa", "Afrique subsaharienne › Sénégal › Casamance", "Ba", 1, 6, 15, 240, "€", "Saladier.",
  "Citron, moutarde et beaucoup d'oignons : pour poulet, poisson ou agneau ; les oignons deviennent ensuite la sauce.",
  [f"4|oignons émincés|{OIG}|3", f"4|citrons (jus)|{CIT}|3", f"3 c. à s.|de moutarde|{DIJON}|2", f"4 gousses|d'ail|{AIL}|1", "1|piment antillais entier|Piment antillais / scotch bonnet|1", f"5 c. à s.|d'huile|{HN}|1", f"1 c. à c.|de poivre|{POIVRE}|0", "2|feuilles de laurier|Laurier|0"],
  ["**Mélanger.** Tout, avec la viande (2 à 12 h) ou le poisson (30 min).", "**Cuire.** Grille la viande ; fais fondre les oignons de la marinade 20 min, ajoute la viande et un verre d'eau, 20 min (voir poulet yassa)."],
  age=3, cats=["sauces"], profil=["acide"], tech=["Marinade"])

K("chermoula", "Chermoula (marinade marocaine pour poisson)", "Chermoula", "Afrique du Nord › Maroc", "Ba", 1, 6, 10, 30, "€", "Mixeur ou couteau.",
  "Coriandre, persil, ail, cumin, paprika, citron et huile d'olive : la marinade verte des poissons et tajines de la mer.",
  [f"1 bouquet|de coriandre|{CORI}|3", f"1 bouquet|de persil|{PERSIL}|2", f"4 gousses|d'ail|{AIL}|2", f"2 c. à c.|de cumin|{CUMIN}|2", f"2 c. à c.|de paprika|{PAPRIKA}|2", f"1 pincée|de piment|{CAYENNE}|1", f"1|citron (jus) + ½ citron confit|{CIT}|2", f"8 c. à s.|d'huile d'olive|{HO}|2", f"1 c. à c.|de sel|{SEL}|0"],
  ["**Mixer.** Herbes, ail, épices, citron, huile, sel (texture de pesto).", "**Mariner.** Poisson 30 min, poulet 2 h. Garde-en un peu pour servir."],
  keep="4 jours au frigo.", age=1, cats=["sauces"], profil=["epice", "acide"], tech=["Marinade"])

K("marinade_tandoori", "Marinade tandoori au yaourt", "Tandoori masala", "Asie du Sud › Inde › Pendjab", "Ba", 1, 6, 10, 360, "€", "Saladier.",
  "Le yaourt attendrit, les épices colorent : poulet, crevettes ou paneer grillés, sans colorant.",
  [f"250 g|de yaourt grec|{GREC}|3", f"1 morceau|de gingembre râpé|{GING}|2", f"4 gousses|d'ail râpé|{AIL}|2", "1 c. à s.|de garam masala|Garam masala|2", f"2 c. à c.|de paprika (pour la couleur)|{PAPRIKA}|2", f"1 c. à c.|de cumin + ½ de curcuma|{CUMIN}|1", f"½ c. à c.|de piment|{CAYENNE}|1", f"1|citron|{CIT}|1", f"1 c. à c.|de sel|{SEL}|0"],
  ["**Mélanger.** Tout.", "**Mariner.** Poulet entaillé 6-12 h ; crevettes 30 min.", "**Cuire.** Four très chaud (240 °C) ou gril : bords noircis."],
  keep="2 jours au frigo (sans viande).", age=3, cats=["sauces"], profil=["epice"], tech=["Marinade"])

K("marinade_jerk", "Marinade jerk jamaïcaine", "Jerk", "Amérique latine & Caraïbes › Jamaïque", "Ba", 1, 6, 15, 720, "€", "Mixeur.",
  "Piment, quatre-épices, thym, oignons verts et citron vert : la marinade fumée-épicée du poulet grillé jamaïcain.",
  ["6|oignons nouveaux|Oignon nouveau / cébette|3", "1-2|piments antillais|Piment antillais / scotch bonnet|3", f"4 gousses|d'ail|{AIL}|1", f"1 morceau|de gingembre|{GING}|1", "1 c. à s.|de quatre-épices (piment de la Jamaïque)|Quatre-épices|2", f"1 c. à s.|de thym|{THYM}|2", f"2|citrons verts|{CITV}|2", f"3 c. à s.|de sauce soja|{SOJA}|1", "2 c. à s.|de cassonade|Sucre blanc / roux / cassonade / vergeoise|1", f"3 c. à s.|d'huile|{HN}|1"],
  ["**Mixer.** Tout en pâte.", "**Mariner.** Cuisses de poulet entaillées 12-24 h.", "**Cuire.** Barbecue, zone indirecte, couvercle fermé, 40 min."],
  age=None, cats=["sauces"], profil=["epice"], tech=["Marinade"])

K("marinade_bulgogi", "Marinade bulgogi (Corée)", "Bulgogi yangnyeom", "Asie de l'Est › Corée", "Ba", 1, 4, 10, 60, "€", "Râpe, saladier.",
  "Sauce soja, poire râpée (elle attendrit), ail, sésame : pour un bœuf émincé caramélisé en 3 minutes.",
  [f"6 c. à s.|de sauce soja|{SOJA}|3", "1|poire râpée|Poire|3", f"4 gousses|d'ail|{AIL}|2", f"2 c. à s.|de sucre|{SUCRE}|1", "2 c. à s.|d'huile de sésame|Huile de sésame (grillée)|2", "2|oignons nouveaux|Oignon nouveau / cébette|1", "1 c. à s.|de sésame grillé|Sésame (blanc/noir)|1", f"1 pincée|de poivre|{POIVRE}|0"],
  ["**Mélanger.** Tout.", "**Mariner.** 600 g de bœuf très finement émincé (passé 30 min au congélateur pour trancher fin), 1 à 4 h.", "**Cuire.** Poêle très chaude, par petites quantités, 2-3 min. Avec riz et feuilles de salade."],
  age=1, cats=["sauces"], profil=["sucre"], tech=["Marinade"])

K("chimichurri", "Chimichurri", "Chimichurri", "Amérique latine & Caraïbes › Argentine", "S", 1, 8, 10, 30, "€", "Couteau, bocal.",
  "Persil, origan, ail, piment, vinaigre et huile : la sauce-marinade verte des grillades argentines.",
  [f"1 gros bouquet|de persil plat|{PERSIL}|3", "1 c. à s.|d'origan séché|Origan frais / sec|2", f"4 gousses|d'ail|{AIL}|2", "1 c. à c.|de flocons de piment|Flocons de piment|1", "5 cl|de vinaigre de vin rouge|Vinaigre de vin rouge / blanc|2", f"12 cl|d'huile d'olive|{HO}|2", f"1 c. à c.|de sel|{SEL}|0"],
  ["**Hacher.** Persil et ail au couteau (pas au mixeur : la texture compte).", "**Mélanger.** Tout ; 30 min de repos. Sur la viande avant et après la cuisson."],
  keep="1 semaine au frigo.", age=3, cats=["sauces"], fetes=["Barbecue d'été"], profil=["acide"], tech=["Marinade"])

K("marinade_adobo", "Adobo de poulet (Philippines)", "Adobong manok", "Asie du Sud-Est › Philippines", "P", 1, 4, 10, 50, "€", "Cocotte.",
  "Mariné puis mijoté dans le vinaigre, la sauce soja, l'ail et le laurier, puis doré : le plat national philippin.",
  [f"1,2 kg|de cuisses de poulet|{CUISSE}|3", "12 cl|de vinaigre (riz ou cidre)|Vinaigre de cidre|3", f"8 cl|de sauce soja|{SOJA}|3", f"10 gousses|d'ail écrasées|{AIL}|2", "4|feuilles de laurier|Laurier|1", f"1 c. à c.|de poivre en grains|{POIVRE}|1", f"1 c. à s.|de sucre|{SUCRE}|1"],
  ["**Mariner.** Tout, 1 h.", "**Mijoter.** Avec 20 cl d'eau, 35 min (ne remue pas les 5 premières minutes : l'acidité s'adoucit).", "**Dorer.** Sors le poulet, dore-le à la poêle ; réduis la sauce, nappe. Riz blanc."],
  age=1, cats=["enfants"], profil=["acide"], tech=["Marinade"])

K("marinade_provencale", "Marinade provençale pour grillades", "Marinade aux herbes", "France › Provence-Alpes-Côte d'Azur", "Ba", 1, 6, 5, 120, "€", "Saladier.",
  "Huile d'olive, herbes de Provence, ail, zeste de citron : pour agneau, poulet, légumes du barbecue.",
  [f"10 cl|d'huile d'olive|{HO}|3", "2 c. à s.|d'herbes de Provence|Herbes de Provence|3", f"3 gousses|d'ail|{AIL}|2", f"1|citron (zeste + jus)|{CIT}|2", f"1 c. à c.|de poivre|{POIVRE}|1"],
  ["**Mélanger.** Tout (le sel juste avant la cuisson).", "**Mariner.** Agneau 4-12 h, poulet 2-6 h, légumes 30 min."],
  age=1, cats=["sauces", "enfants"], fetes=["Barbecue d'été"], profil=["leger"], tech=["Marinade"])

K("marinade_teriyaki_sauce", "Sauce teriyaki maison (laque)", "Teriyaki", "Asie de l'Est › Japon", "S", 1, 6, 5, 10, "€", "Petite casserole.",
  "Sauce soja, mirin (ou jus de pomme), sucre et gingembre réduits en laque brillante : saumon, poulet, tofu.",
  [f"10 cl|de sauce soja|{SOJA}|3", "10 cl|de mirin|Mirin|2", f"2 c. à s.|de sucre|{SUCRE}|2", f"1 c. à c.|de gingembre râpé|{GING}|1", f"1 c. à c.|de maïzena (facultatif)|Fécule de maïs (maïzena)|0?"],
  ["**Réduire.** Tout à frémissement 5-8 min jusqu'à sirop nappant.", "**Laquer.** En fin de cuisson, badigeonne en 3 couches."],
  var=[("Sans alcool", ["alcohol"], {"Mirin": [("Jus de pomme / raisin / orange (pur jus)", 0.8), ("Vinaigre de riz", 0.1)]}, "Mirin → **8 cl de jus de pomme + 1 c. à c. de vinaigre de riz** : même douceur fruitée. **À tester**.")],
  keep="2 semaines au frigo.", age=3, cats=["sauces"], profil=["sucre"])

K("ras_el_hanout_maison", "Ras el-hanout maison", "Ras el-hanout", "Afrique du Nord › Maroc", "Ba", 1, 30, 15, 0, "€", "Poêle, moulin à épices.",
  "« Le meilleur de l'épicier » : un mélange chaud et floral pour tajines, couscous, légumes rôtis.",
  ["1 c. à s.|de cumin|Cumin (graines / moulu)|2", "1 c. à s.|de coriandre en graines|Coriandre (graines)|2", f"1 c. à s.|de gingembre en poudre|Gingembre (poudre)|2", f"2 c. à c.|de cannelle|{CANN}|2", f"2 c. à c.|de curcuma|{CURC}|1", "1 c. à c.|de poivre noir|Poivre noir / blanc / vert|1", "1 c. à c.|de cardamome|Cardamome|1", "½ c. à c.|de muscade|Noix de muscade|1", "4|clous de girofle|Clou de girofle|1", "1 c. à c.|de paprika|Paprika doux|1", "1 c. à c.|de piment doux|Piment doux (poudre de poivron)|0"],
  ["**Torréfier.** Graines entières 2 min à sec, jusqu'à ce qu'elles sentent.", "**Moudre.** Avec les poudres, tamise. Bocal hermétique."],
  keep="6 mois à l'abri de la lumière.", age=1, cats=["sauces"], profil=["epice"], tech=["Torréfier les épices"])

K("garam_masala_maison", "Garam masala maison", "Garam masala", "Asie du Sud › Inde › Pendjab", "Ba", 1, 30, 15, 0, "€", "Poêle, moulin.",
  "Le mélange chaud du nord de l'Inde, à ajouter en fin de cuisson des currys et dals.",
  ["2 c. à s.|de coriandre en graines|Coriandre (graines)|2", "1 c. à s.|de cumin|Cumin (graines / moulu)|2", "1 c. à s.|de cardamome verte|Cardamome|2", "1 c. à c.|de poivre noir|Poivre noir / blanc / vert|1", "1|bâton de cannelle|Cannelle (bâton / poudre)|1", "1 c. à c.|de clous de girofle|Clou de girofle|1", "½|noix de muscade|Noix de muscade|1", "2|feuilles de laurier|Laurier|0"],
  ["**Torréfier.** Tout 2-3 min à sec, en remuant.", "**Moudre.** Une fois refroidi, très fin."],
  keep="6 mois.", age=1, cats=["sauces"], profil=["epice"], tech=["Torréfier les épices"])

K("curry_poudre_maison", "Curry en poudre maison (doux)", "Curry powder", "Asie du Sud › Inde", "Ba", 1, 30, 15, 0, "€", "Poêle, moulin.",
  "Un curry doux, parfumé et non piquant, adapté aux enfants ; ajoute du piment pour les adultes.",
  ["3 c. à s.|de coriandre en graines|Coriandre (graines)|3", "1 c. à s.|de cumin|Cumin (graines / moulu)|2", f"1 c. à s.|de curcuma|{CURC}|3", "1 c. à c.|de fenugrec|Fenugrec|1", "1 c. à c.|de graines de moutarde|Graines de moutarde|1", "1 c. à c.|de gingembre en poudre|Gingembre (poudre)|1", "½ c. à c.|de poivre noir|Poivre noir / blanc / vert|1", "4|gousses de cardamome|Cardamome|1"],
  ["**Torréfier.** Graines entières 2 min.", "**Moudre.** Avec curcuma et gingembre."],
  keep="6 mois.", age=1, cats=["sauces", "enfants"], profil=["epice"], tech=["Torréfier les épices"])

K("dukkah", "Dukkah (mélange égyptien noisettes-épices)", "Dukkah", "Afrique du Nord › Égypte", "Ba", 1, 15, 15, 0, "€", "Poêle, mortier.",
  "Noisettes, sésame, coriandre et cumin concassés : on trempe le pain dans l'huile d'olive puis dans le dukkah.",
  ["100 g|de noisettes|Noisette|3", "40 g|de sésame|Sésame (blanc/noir)|2", "2 c. à s.|de coriandre en graines|Coriandre (graines)|2", "1 c. à s.|de cumin|Cumin (graines / moulu)|2", "1 c. à c.|de poivre noir|Poivre noir / blanc / vert|1", f"1 c. à c.|de fleur de sel|{SEL}|1"],
  ["**Torréfier.** Noisettes 10 min au four à 160 °C (th. 5-6), jusqu'à ce que la peau craque ; graines et sésame 2 min à la poêle, jusqu'à ce qu'ils sentent bon.", "**Concasser.** Grossièrement au mortier, avec sel et poivre."],
  keep="1 mois en bocal.", age=3, cats=["sauces"], fetes=["Apéritif dînatoire"], profil=["gras"], tips=["⚠️ Fruits à coque et sésame : allergènes."])

K("zaatar_maison", "Zaatar maison", "Za'atar", "Moyen-Orient & Caucase › Liban", "Ba", 1, 15, 10, 0, "€", "Poêle.",
  "Thym, sumac acidulé et sésame grillé : sur une galette huilée (manouché), des œufs, du labneh.",
  ["4 c. à s.|de thym séché (ou origan)|Thym / romarin|3", "2 c. à s.|de sumac|Sumac|3", "2 c. à s.|de sésame grillé|Sésame (blanc/noir)|2", f"1 c. à c.|de sel|{SEL}|0"],
  ["**Mélanger.** Sésame grillé tiède, thym émietté, sumac, sel."],
  keep="3 mois.", age=1, cats=["sauces"], profil=["acide"])

K("berbere_maison", "Berbéré éthiopien", "Berbere", "Afrique subsaharienne › Éthiopie", "Ba", 1, 30, 15, 0, "€", "Poêle, moulin.",
  "Un mélange rouge, piquant et parfumé (piment, fenugrec, cardamome) : la base du doro wat et des lentilles misir.",
  [f"4 c. à s.|de piment doux en poudre|Piment doux (poudre de poivron)|3", f"1 c. à s.|de piment fort|{CAYENNE}|2", "1 c. à c.|de fenugrec|Fenugrec|2", "1 c. à c.|de coriandre en graines|Coriandre (graines)|1", "1 c. à c.|de cardamome|Cardamome|1", "1 c. à c.|de gingembre|Gingembre (poudre)|1", "½ c. à c.|de cannelle et de girofle|Clou de girofle|1", "½ c. à c.|de poivre noir|Poivre noir / blanc / vert|1"],
  ["**Torréfier.** Graines 2 min.", "**Moudre.** Avec les poudres."],
  keep="6 mois.", age=None, cats=["sauces"], profil=["epice"], tech=["Torréfier les épices"])

K("pate_curry_vert", "Pâte de curry vert thaïe maison", "Prik gaeng khiao wan", "Asie du Sud-Est › Thaïlande", "Ba", 2, 8, 25, 0, "€€", "Mortier ou mixeur.",
  "Piments verts, citronnelle, galanga, combava et coriandre : une pâte fraîche bien plus parfumée que celle du commerce, sans conservateur.",
  [f"6|piments verts|{PIMENT}|3", "3|bâtons de citronnelle|Citronnelle|3", "1 morceau|de galanga (ou gingembre)|Galanga|2", "4|feuilles de combava|Feuille de combava (kaffir)|2", f"1 bouquet|de coriandre avec racines|{CORI}|2", f"4|échalotes|{ECH}|2", f"6 gousses|d'ail|{AIL}|1", "1 c. à c.|de cumin + 1 de coriandre en graines|Coriandre (graines)|1", "1 c. à c.|de pâte de crevettes (facultatif)|Pâte de crevettes|1?", f"1 c. à c.|de sel|{SEL}|0"],
  ["**Torréfier.** Graines, puis moudre.", "**Piler.** Tout, des plus durs (citronnelle, galanga) aux plus tendres ; ou mixe avec 2 c. à s. d'huile."],
  keep="1 semaine au frigo ; 3 mois en glaçons.", age=None, cats=["sauces"], profil=["epice"])

K("citrons_confits_maison", "Citrons confits au sel", "Citron confit", "Afrique du Nord › Maroc", "Ba", 1, 8, 15, 43200, "€", "Bocal de 1 L ébouillanté.",
  "Des citrons conservés dans leur jus et le sel : l'écorce devient fondante et parfume tajines, salades, sauces.",
  [f"8|citrons non traités|{CIT}|3", "8 c. à s.|de gros sel|Sel fin / gros sel / fleur de sel|3", f"4|citrons (jus)|{CIT}|2", "2|feuilles de laurier|Laurier|0"],
  ["**Inciser.** Coupe les citrons en croix sans détacher les quartiers ; remplis de gros sel.", "**Tasser.** Dans le bocal en écrasant ; couvre de jus de citron.", "**Attendre.** 4 semaines à température ambiante, retourne le bocal de temps en temps. Utilise l'écorce rincée."],
  keep="1 an au frais une fois ouvert.", age=1, cats=["sauces", "zero_dechet"], profil=["acide"])

K("ghee_maison", "Ghee (beurre clarifié) maison", "Ghee", "Asie du Sud › Inde", "Ba", 1, 20, 5, 25, "€", "Casserole, passoire fine, gaze ou filtre à café.",
  "Le beurre cuit débarrassé de son petit-lait : il ne brûle pas, se garde hors du frigo, goût de noisette.",
  [f"500 g|de beurre doux|{BEURRE}|3"],
  ["**Cuire.** Feu doux, 20-25 min : le beurre mousse, puis devient limpide ; les dépôts au fond dorent.", "**Filtrer.** Dès que ça sent la noisette, à travers une gaze. Bocal sec."],
  keep="3 mois à température ambiante, 1 an au frigo.", age=1, cats=["sauces"], profil=["gras"], tips=["Les dépôts dorés : délicieux sur du riz ou des légumes."])

K("pickles_oignons_rouges", "Pickles d'oignons rouges", "Oignons rouges marinés", "Amérique latine & Caraïbes › Mexique", "S", 1, 10, 10, 120, "€", "Bocal, casserole.",
  "Rose vif, acidulés, croquants : sur tacos, burgers, salades, bowls et sandwichs.",
  ["3|oignons rouges|Oignon rouge|3", "20 cl|de vinaigre de cidre|Vinaigre de cidre|2", "20 cl|d'eau|-|0", f"1 c. à s.|de sucre|{SUCRE}|1", f"1 c. à c.|de sel|{SEL}|1", "1 c. à c.|de poivre en grains + 1 feuille de laurier|Poivre noir / blanc / vert|0"],
  ["**Trancher.** Oignons en fines rondelles, tassés dans le bocal.", "**Saumure.** Vinaigre, eau, sucre, sel, épices à ébullition, versés dessus.", "**Attendre.** 2 h, puis au frigo."],
  keep=KEEP_F, age=3, cats=["sauces"], profil=["acide"])

K("moutarde_maison", "Moutarde maison à l'ancienne", "Moutarde", "France › Bourgogne-Franche-Comté › Dijon", "S", 1, 10, 10, 4320, "€", "Bocal, mixeur.",
  "Graines de moutarde trempées dans le vinaigre, mixées plus ou moins : forte au début, elle s'adoucit en quelques jours.",
  ["60 g|de graines de moutarde jaunes et brunes|Graines de moutarde|3", "10 cl|de vinaigre de cidre|Vinaigre de cidre|2", "5 cl|d'eau|-|0", f"1 c. à c.|de miel|{MIEL}|1", f"1 c. à c.|de sel|{SEL}|0", f"1 pincée|de curcuma|{CURC}|0"],
  ["**Tremper.** Graines dans vinaigre + eau, 24 h.", "**Mixer.** Avec miel, sel, curcuma : peu pour l'ancienne, longtemps pour une moutarde lisse.", "**Mûrir.** 3 jours au frigo avant de l'utiliser."],
  keep="3 mois au frigo.", age=3, cats=["sauces"], profil=["acide", "epice"])

K("sauce_chien", "Sauce chien antillaise", "Sauce chien", "France › Outre-mer › Antilles", "S", 1, 8, 15, 30, "€", "Bol, bouilloire.",
  "Cives, ail, persil, piment, citron vert et huile, ébouillantés : pour poissons et viandes grillés.",
  ["4|oignons nouveaux (cives)|Oignon nouveau / cébette|3", f"3 gousses|d'ail|{AIL}|2", f"1 bouquet|de persil|{PERSIL}|2", "½|piment antillais|Piment antillais / scotch bonnet|2", f"2|citrons verts|{CITV}|2", f"6 c. à s.|d'huile|{HN}|2", "15 cl|d'eau bouillante|-|0", f"1 c. à c.|de sel|{SEL}|0"],
  ["**Hacher.** Très finement cives, ail, persil, piment.", "**Ébouillanter.** Sel, citron, huile, puis l'eau bouillante. 30 min avant de servir."],
  keep="3 jours au frigo.", age=None, cats=["sauces"], fetes=["Barbecue d'été"], profil=["epice", "acide"])

K("sauce_piri_piri", "Huile et sauce piri-piri", "Piri-piri", "Afrique subsaharienne › Mozambique", "S", 1, 10, 15, 1440, "€", "Mixeur, casserole.",
  "Piments rouges, ail, citron, paprika : la sauce piquante du poulet grillé portugais-mozambicain.",
  [f"6|piments rouges frais|{PIMENT}|3", f"1|poivron rouge grillé|{POIVRON}|2", f"4 gousses|d'ail|{AIL}|2", f"1|citron (jus)|{CIT}|2", f"1 c. à c.|de paprika fumé|{PFUME}|1", "1 c. à s.|de vinaigre|Vinaigre de vin rouge / blanc|1", f"10 cl|d'huile d'olive|{HO}|2", "1 c. à c.|d'origan|Origan frais / sec|1"],
  ["**Mixer.** Tout, jusqu'à lisse.", "**Cuire.** 5 min à frémissement (elle se conserve mieux).", "**Utiliser.** En marinade (12 h) et au badigeon."],
  keep="2 semaines au frigo.", age=None, cats=["sauces"], fetes=["Barbecue d'été"], profil=["epice"])

K("sweet_chili", "Sauce sweet chili maison", "Nam chim kai", "Asie du Sud-Est › Thaïlande", "S", 1, 10, 10, 15, "€", "Casserole.",
  "Sucrée, aigre et légèrement piquante, pour nems, poulet frit, crevettes : sans épaississant chimique.",
  [f"4|piments rouges|{PIMENT}|2", f"4 gousses|d'ail|{AIL}|2", "12 cl|de vinaigre de riz|Vinaigre de riz|2", f"150 g|de sucre|{SUCRE}|3", "12 cl|d'eau|-|0", f"1 c. à c.|de sel|{SEL}|0", f"1 c. à s.|de maïzena|Fécule de maïs (maïzena)|1"],
  ["**Hacher.** Piments et ail.", "**Cuire.** Tout sauf la maïzena, 10 min ; ajoute la maïzena délayée, 1 min : nappante."],
  keep="1 mois au frigo.", age=3, cats=["sauces"], profil=["sucre", "epice"])

K("sauce_satay", "Sauce satay (cacahuète)", "Saus kacang", "Asie du Sud-Est › Indonésie", "S", 1, 6, 10, 5, "€", "Casserole.",
  "Cacahuète, lait de coco, soja, citron vert, une pointe de piment : pour brochettes, nouilles et légumes.",
  ["150 g|de beurre de cacahuète|Beurre de cacahuète|3", f"20 cl|de lait de coco|{COCO}|2", f"2 c. à s.|de sauce soja|{SOJA}|2", f"1|citron vert|{CITV}|1", "1 c. à s.|de cassonade|Sucre blanc / roux / cassonade / vergeoise|1", f"1 gousse|d'ail|{AIL}|1", "1 c. à c.|de sambal ou de piment|Sambal oelek|1"],
  ["**Chauffer.** Tout en fouettant, 5 min, jusqu'à lisse. Ajoute de l'eau si trop épais."],
  keep="5 jours au frigo.", age=1, cats=["sauces", "enfants"], profil=["gras"], tips=["⚠️ Arachide : allergène majeur."])

K("nuoc_cham", "Nuoc cham (sauce vietnamienne)", "Nước chấm", "Asie du Sud-Est › Vietnam", "S", 1, 6, 10, 0, "€", "Bol.",
  "Sauce de poisson, citron vert, sucre, ail, piment : la sauce des nems, bò bún et rouleaux de printemps.",
  [f"4 c. à s.|de sauce de poisson|Sauce de poisson (nuoc-mâm, nam pla)|3", f"2|citrons verts|{CITV}|2", f"3 c. à s.|de sucre|{SUCRE}|2", "12 cl|d'eau tiède|-|0", f"2 gousses|d'ail|{AIL}|1", f"1|piment|{PIMENT}|1", "½|carotte en fine julienne|Carotte|0?"],
  ["**Dissoudre.** Sucre dans l'eau tiède.", "**Mélanger.** Nuoc-mâm, citron, ail et piment hachés, carotte. Goûte : équilibre salé-sucré-acide."],
  keep="1 semaine au frigo.", age=3, cats=["sauces"], profil=["acide", "sucre"])

K("chutney_mangue", "Chutney de mangue", "Aam chutney", "Asie du Sud › Inde", "S", 1, 10, 15, 40, "€", "Casserole, bocaux.",
  "Mangue, vinaigre, sucre, gingembre et épices réduits : avec currys, fromages, viandes froides.",
  ["2|mangues pas trop mûres|Mangue|3", "10 cl|de vinaigre de cidre|Vinaigre de cidre|2", "100 g|de cassonade|Sucre blanc / roux / cassonade / vergeoise|2", f"1|oignon|{OIG}|1", f"1 morceau|de gingembre|{GING}|1", "½ c. à c.|de graines de moutarde, cumin, nigelle|Graines de moutarde|1", f"1 pincée|de piment|{CAYENNE}|1"],
  ["**Cuire.** Tout, 40 min à feu doux jusqu'à confit.", "**Mettre en bocaux.** Chaud, dans des bocaux propres."],
  keep="2 mois au frigo.", age=1, cats=["sauces"], profil=["sucre", "acide"])

K("huile_pimentee", "Huile pimentée croustillante (chili crisp)", "Lajiao you", "Asie de l'Est › Chine › Sichuan", "S", 1, 20, 15, 30, "€", "Casserole, bol résistant à la chaleur.",
  "Flocons de piment, ail et échalotes frits, poivre du Sichuan : une huile parfumée à tout mettre, des nouilles aux œufs.",
  [f"25 cl|d'huile neutre|{HN}|3", "40 g|de flocons de piment|Flocons de piment|3", f"6|échalotes émincées|{ECH}|2", f"8 gousses|d'ail émincées|{AIL}|2", "1 c. à s.|de poivre du Sichuan|Poivre du Sichuan|2", "1|badiane + 1 bâton de cannelle|Anis étoilé (badiane)|1", "1 c. à s.|de sésame|Sésame (blanc/noir)|1", f"1 c. à c.|de sucre et de sel|{SEL}|0"],
  ["**Frire.** Échalotes puis ail dans l'huile à feu moyen avec les épices entières, jusqu'à doré (pas brun). Égoutte-les.", "**Infuser.** Huile à 120 °C versée sur le piment, sésame, Sichuan moulu, sucre, sel.", "**Finir.** Remets échalotes et ail croustillants. Refroidis."],
  keep="1 mois au frigo.", age=None, cats=["sauces"], profil=["epice", "gras"])

K("beurre_maitre_hotel", "Beurres composés (maître d'hôtel, ail-persil, Café de Paris simplifié)", "Beurre maître d'hôtel", "France › Cuisine de base", "S", 1, 12, 10, 60, "€", "Bol, film.",
  "Un beurre mou parfumé roulé en boudin : une rondelle sur une viande, un poisson ou des légumes chauds.",
  [f"125 g|de beurre mou|{BEURRE}|3", f"1 bouquet|de persil|{PERSIL}|2", f"½|citron (jus)|{CIT}|1", f"1 gousse|d'ail (facultatif)|{AIL}|1?", f"1 c. à c.|de moutarde (version Café de Paris) + câpres, estragon, curry|{DIJON}|1?", f"1 pincée|de sel, poivre|{SEL}|0"],
  ["**Mélanger.** Beurre, herbes hachées, citron, sel, poivre (et les extras).", "**Rouler.** En boudin dans du film, 1 h au frais. Tranche en rondelles."],
  keep="1 semaine au frigo, 3 mois congelé.", age=1, cats=["sauces", "enfants", "zero_dechet"], profil=["gras"], tips=["Fin de bouquet d'herbes : idéal pour ne rien perdre."])
