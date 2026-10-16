// Contenus éditoriaux des rubriques transversales, repris de la bible (Tome 1 §7.6, §12, §13).

/** Calendrier festif (Tome 1 §12.1). month : 1-12 (approximatif pour les fêtes mobiles, signalé). */
export interface Fete { name: string; when: string; month: number | null; traditions: string; tag: string; ideas: string[] }
export const FETES: Fete[] = [
  { name: "Épiphanie", when: "Début janvier", month: 1, tag: "Épiphanie", traditions: "La galette des rois partagée en famille ; le plus jeune, sous la table, désigne les parts.", ideas: ["galette_rois", "citronnade_menthe"] },
  { name: "Chandeleur", when: "2 février", month: 2, tag: "Chandeleur", traditions: "Des crêpes à volonté ; on les fait sauter en tenant une pièce pour la prospérité.", ideas: ["crepes_bretonnes", "galette_complete", "pancakes"] },
  { name: "Nouvel An chinois", when: "Fin janvier ou février (calendrier lunaire)", month: 2, tag: "Nouvel An chinois", traditions: "Raviolis, nouilles pour la longévité, poisson entier pour l'abondance.", ideas: ["riz_cantonais", "poulet_teriyaki"] },
  { name: "Saint-Valentin", when: "14 février", month: 2, tag: "Saint-Valentin", traditions: "Un dîner à deux, souvent avec un dessert au chocolat.", ideas: ["mousse_chocolat", "tiramisu"] },
  { name: "Ramadan, ftour et Aïd el-Fitr", when: "Mois lunaire (dates variables, à vérifier chaque année)", month: null, tag: "Ramadan / Aïd", traditions: "Rupture du jeûne avec dattes, lait ou jus, une soupe (chorba, harira), des pains et feuilletés ; l'Aïd se fête avec pâtisseries et thé.", ideas: ["chorba", "msemen", "batbout", "the_menthe", "bissap", "oranges_cannelle", "tajine_poulet_olives"] },
  { name: "Aïd el-Kébir (Tabaski)", when: "Calendrier lunaire, 70 jours après l'Aïd el-Fitr", month: null, tag: "Ramadan / Aïd", traditions: "Le mouton partagé avec la famille, les voisins et les plus démunis ; au Sénégal, la Tabaski.", ideas: ["poulet_yassa", "mafe_poulet", "bissap"] },
  { name: "Pâques", when: "Mars ou avril", month: 4, tag: "Pâques", traditions: "Agneau, œufs en chocolat, brioches tressées.", ideas: ["brioche", "mousse_chocolat"] },
  { name: "Fête des mères et des pères", when: "Mai et juin", month: 5, tag: "Repas de famille", traditions: "Le plat préféré du parent fêté, cuisiné par les enfants.", ideas: ["gateau_yaourt", "quiche_lorraine", "pizza_margherita"] },
  { name: "Barbecue d'été et 14 juillet", when: "Juin à août", month: 7, tag: "Barbecue d'été", traditions: "Grillades, salades, sauces maison, boissons fraîches.", ideas: ["sauce_barbecue", "taboule_libanais", "tzatziki", "guacamole", "citronnade_menthe", "jus_gingembre"] },
  { name: "Halloween", when: "31 octobre", month: 10, tag: "Halloween", traditions: "Potirons, soupes orangées, gâteaux décorés.", ideas: ["veloute_potiron", "banana_bread"] },
  { name: "Diwali", when: "Octobre ou novembre", month: 11, tag: "Diwali", traditions: "Fête des lumières en Inde : douceurs, pains frits, currys de légumes.", ideas: ["dal_tadka", "naan", "lassi_mangue"] },
  { name: "Noël et Nouvel An", when: "24-25 et 31 décembre", month: 12, tag: "Noël", traditions: "Réveillon, plats mijotés ou rôtis, entrées festives, bûche ou desserts au chocolat.", ideas: ["accras_morue", "boeuf_bourguignon", "gratin_dauphinois", "veloute_potiron", "mousse_chocolat", "jus_gingembre"] },
  { name: "Anniversaire", when: "Toute l'année", month: null, tag: "Anniversaire", traditions: "Un buffet facile, un gâteau, des boissons maison sans alcool pour tout le monde.", ideas: ["focaccia", "pizza_margherita", "chili_con_carne", "gateau_yaourt", "bissap"] },
  { name: "Apéritif dînatoire", when: "Toute l'année", month: null, tag: "Apéritif dînatoire", traditions: "Des bouchées à partager, préparées à l'avance.", ideas: ["houmous", "guacamole", "focaccia", "accras_morue", "tzatziki"] },
];

/** Quantités par convive (repères de départ, Tome 1 §12.2 ; à ajuster). */
export const PAR_CONVIVE = [
  ["Apéritif (bouchées)", "5 à 8 pièces"], ["Entrée", "150 g (salade) à 250 ml (soupe)"], ["Viande ou poisson (plat)", "150 à 180 g sans os ; 250 g avec os"],
  ["Accompagnement", "200 g cuit (riz : 70 g cru)"], ["Pain", "¼ de baguette"], ["Dessert", "1 part ; −15 % si 3 desserts différents"], ["Boissons sans alcool", "0,75 à 1 L par personne"],
];

/** Anatomie des ingrédients (Tome 1 §13.1, Tome 3 §17.4) avec renvoi aux recettes qui valorisent chaque partie. */
export const ANATOMIE: { ing: string; parts: string; uses: string; recipes: string[] }[] = [
  { ing: "Poireau", parts: "Blanc, vert, racines", uses: "Blanc : poêlée, vinaigrette. Vert et racines : bouillon, soupe, chips.", recipes: ["bouillon_legumes", "bouillon_volaille"] },
  { ing: "Carotte, radis, betterave", parts: "Fanes, épluchures", uses: "Fanes : pesto, soupe. Épluchures propres : bouillon.", recipes: ["pesto", "bouillon_legumes"] },
  { ing: "Pain rassis", parts: "Mie, croûte", uses: "Pain perdu, chapelure, croûtons, panzanella.", recipes: ["pain_perdu"] },
  { ing: "Œuf", parts: "Blancs, jaunes, coquilles", uses: "Blancs : meringues, mousse. Jaunes : mayonnaise, crème. Coquilles : compost.", recipes: ["meringues", "mayonnaise", "mousse_chocolat"] },
  { ing: "Poulet entier", parts: "Chair, carcasse, peau, gras", uses: "Carcasse : bouillon. Restes : riz sauté, salade. Gras : pommes de terre sautées.", recipes: ["poulet_roti", "bouillon_volaille", "riz_cantonais"] },
  { ing: "Agrumes", parts: "Zeste, jus, peau", uses: "Zestes : sucre aromatisé, gâteau. Jus : citronnade. Peaux : écorces confites.", recipes: ["citronnade_menthe", "gateau_yaourt", "oranges_cannelle"] },
  { ing: "Parmesan", parts: "Croûte", uses: "Dans une soupe, un risotto ou une sauce tomate.", recipes: ["sauce_tomate"] },
  { ing: "Champignons", parts: "Pieds", uses: "Bouillon, duxelles.", recipes: ["bouillon_legumes"] },
  { ing: "Pommes de terre", parts: "Épluchures", uses: "Chips au four.", recipes: ["frites_maison"] },
  { ing: "Courges (potiron, potimarron)", parts: "Graines, peau", uses: "Graines grillées ; peau du potimarron mixée dans le velouté.", recipes: ["veloute_potiron"] },
  { ing: "Bananes très mûres", parts: "Chair", uses: "Banana bread, pancakes, lassi.", recipes: ["banana_bread", "pancakes"] },
  { ing: "Herbes fanées", parts: "Feuilles, tiges", uses: "Pesto, sauce blanche, bouillon, glaçons d'herbes.", recipes: ["pesto", "sauce_blanche", "taboule_libanais"] },
  { ing: "Pois chiches (bocal)", parts: "Jus (aquafaba)", uses: "Mayonnaise sans œuf, meringues véganes.", recipes: ["houmous", "mayonnaise"] },
  { ing: "Riz ou pâtes cuits", parts: "Restes", uses: "Riz sauté, galettes, gratin (attention, riz : frigo, 24 h maximum).", recipes: ["riz_cantonais"] },
  { ing: "Tomates trop mûres, poivrons fripés", parts: "Chair", uses: "Sauce tomate, chakchouka, ketchup.", recipes: ["sauce_tomate", "shakshuka", "ketchup"] },
  { ing: "Huile de friture", parts: "Huile filtrée", uses: "Réutilisable 5-6 fois si claire ; jamais à l'évier (déchetterie).", recipes: ["frites_maison"] },
];

/** Conservation de référence (Tome 3 §17.2, repères prudents). */
export const CONSERVATION = [
  ["Mayonnaise et sauces à l'œuf cru", "3 jours au frigo (≤ 4 °C)"], ["Sauces au yaourt", "3 à 4 jours"], ["Bouillon maison", "4 jours au frigo, 6 mois au congélateur"],
  ["Riz cuit", "24 h au frigo, refroidi en moins de 2 h"], ["Plats mijotés", "3 à 4 jours au frigo, 3 mois au congélateur"], ["Pâte à pizza ou à pain crue", "3 jours au frigo, 2 mois au congélateur"],
  ["Huiles aromatisées à l'ail ou aux herbes", "Attention : au frigo, 4 jours maximum (risque de botulisme)"], ["Herbes fraîches", "Dans un verre d'eau au frigo, ou hachées en glaçons dans l'huile"],
];

export const DLC_DDM = "DLC (« à consommer jusqu'au ») : date impérative pour les produits frais, à respecter. DDM (« à consommer de préférence avant ») : le produit reste consommable après, il perd seulement en qualité (pâtes, riz, conserves, biscuits).";

/** Règles de sécurité enfants (Tome 1 §7.6). */
export const SECURITE_ENFANTS = [
  "Miel interdit avant 12 mois (botulisme infantile).",
  "Pas de sel ajouté avant 1 an ; sucre et épices fortes en petites doses ensuite.",
  "Risque d'étouffement avant 4 ans : fruits à coque entiers, raisins et tomates cerises entiers, saucisses en rondelles, popcorn → couper en long, mixer.",
  "Pas d'œuf cru (mayonnaise, mousse au chocolat, tiramisu), pas de viande hachée ou de poisson peu cuits, pas de lait cru pour les jeunes enfants.",
  "Jamais d'alcool, même cuit ou en extrait (vanille liquide) : ATLAS propose les versions sans alcool.",
  "L'application ne remplace pas l'avis du pédiatre pour la diversification.",
];

export const PETIT_CHEF: { age: string; tasks: string }[] = [
  { age: "3-5 ans", tasks: "Laver les légumes, déchirer la salade, mélanger, étaler du beurre, former des boulettes, garnir une pizza, mesurer au pot de yaourt." },
  { age: "6-8 ans", tasks: "Peser, casser un œuf, pétrir, couper avec un couteau à bout rond, plier un msemen, dresser des meringues." },
  { age: "9-12 ans", tasks: "Éplucher, râper (avec attention), utiliser le mixeur sous contrôle, suivre une recette complète." },
  { age: "Jamais seuls", tasks: "Friture, four à haute température, couteaux aiguisés, flamme, mandoline." },
];

/** Accords boissons par profil dominant du plat (Tome 1 §12.4). Deux colonnes, la sans-alcool toujours présente. */
export const ACCORDS: Record<string, { sa: string[]; a: string[]; why: string }> = {
  gras: { why: "Plat riche : une boisson vive (acidité, bulles) rafraîchit la bouche.", sa: ["Eau pétillante citronnée", "Jus de pomme pétillant", "Citronnade à la menthe", "Thé vert froid"], a: ["Vin blanc vif", "Cidre brut", "Bière blonde"] },
  epice: { why: "Plat épicé : du lacté ou du fruité calme le piquant.", sa: ["Lassi à la mangue", "Lait ribot", "Jus de mangue", "Thé glacé"], a: ["Vin blanc demi-sec", "Bière légère"] },
  poisson: { why: "Poisson et fruits de mer : fraîcheur et légère acidité.", sa: ["Eau infusée au concombre", "Jus de pomme et gingembre", "Tonic"], a: ["Vin blanc sec", "Muscadet"] },
  viande_rouge: { why: "Viande rouge, mijotés : fruits rouges et tanins doux.", sa: ["Jus de raisin rouge ou de grenade", "Infusion de rooibos", "Thé noir"], a: ["Vin rouge structuré"] },
  chocolat: { why: "Dessert chocolaté : amertume et fruits rouges.", sa: ["Café", "Chocolat chaud", "Jus de cerise"], a: ["Vin doux naturel"] },
  sucre: { why: "Dessert sucré : une boisson peu sucrée pour équilibrer.", sa: ["Thé", "Café", "Infusion"], a: ["Cidre doux"] },
  leger: { why: "Plat léger : boissons fraîches et florales.", sa: ["Thé à la menthe", "Citronnade", "Bissap"], a: ["Vin rosé"] },
  acide: { why: "Plat acidulé : douceur et rondeur.", sa: ["Jus de pomme", "Thé à la menthe"], a: ["Vin blanc rond"] },
};

export const EVIN = "L'abus d'alcool est dangereux pour la santé. À consommer avec modération.";
