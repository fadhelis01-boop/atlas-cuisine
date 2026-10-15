// Parcours du débutant (Tome 13 §11) : chaque étape = un geste (fiche technique) + une ou deux recettes pour le pratiquer.
// Une étape est validée quand l'une de ses recettes a été cuisinée en mode cuisine, ou à la main.
export const PARCOURS: { id: string; title: string; why: string; techs: string[]; recipes: string[] }[] = [
  { id: "couteau", title: "Tenir son couteau et couper", why: "Couper vite, régulier et sans se blesser : la base de tout.", techs: ["tenir-couteau", "ciseler-oignon", "ciseler-herbes"], recipes: ["salade_grecque", "taboule_semoule"] },
  { id: "oeufs", title: "Maîtriser les œufs", why: "Cinq minutes, un résultat immédiat : on apprend à régler le feu.", techs: ["oeufs-temperatures", "omelette-brouilles"], recipes: ["omelette_fines_herbes", "oeufs_mimosa"] },
  { id: "pates-riz", title: "Pâtes et riz parfaits", why: "Les accompagnements de tous les jours, sans colle ni grumeaux.", techs: ["cuire-pates", "cuire-riz"], recipes: ["spaghetti_aglio_olio", "riz_pilaf"] },
  { id: "revenir", title: "Faire revenir et construire une sauce", why: "Oignon fondu, ail, tomate : la moitié des plats du monde commence ainsi.", techs: ["faire-revenir"], recipes: ["sauce_tomate", "pates_sauce_legumes_caches"] },
  { id: "soupe", title: "Bouillon et soupes", why: "Économique, zéro déchet, et on apprend l'assaisonnement.", techs: ["bouillon"], recipes: ["soupe_poireaux_pdt", "veloute_butternut_coco"] },
  { id: "emulsion", title: "Émulsions : mayonnaise et vinaigrette", why: "Comprendre pourquoi une sauce « prend » ou « tranche ».", techs: ["emulsionner"], recipes: ["mayonnaise", "vinaigrette"] },
  { id: "saisir", title: "Saisir et déglacer", why: "La croûte dorée et la sauce minute qui va avec.", techs: ["saisir", "deglacer", "cuisson-viande-rouge"], recipes: ["steak_frites", "poulet_basse_temp"] },
  { id: "rotir", title: "Rôtir au four", why: "Le plat du dimanche : peau croustillante, chair juteuse.", techs: ["rotir-volaille", "rotir-viande-four"], recipes: ["poulet_roti", "pommes_terre_four"] },
  { id: "mijoter", title: "Mijoter", why: "Transformer un morceau bon marché en plat fondant.", techs: ["mijoter"], recipes: ["blanquette_poulet", "joues_boeuf_carottes"] },
  { id: "poisson", title: "Cuire le poisson sans le dessécher", why: "Nacré, juteux : deux minutes font toute la différence.", techs: ["cuissons-poisson", "vapeur-papillote"], recipes: ["saumon_peau_croustillante", "cabillaud_papillote"] },
  { id: "bechamel", title: "Roux, béchamel et gratins", why: "La sauce blanche lisse, base des gratins et des lasagnes.", techs: ["roux-bechamel"], recipes: ["gratin_chou_fleur", "lasagnes_bolognaise"] },
  { id: "pain", title: "Pétrir et faire lever", why: "Pain, pizza, naan : tout le monde peut y arriver.", techs: ["petrir", "pointage"], recipes: ["pain_complet", "pate_pizza"] },
  { id: "patisserie", title: "Pâtisserie de base", why: "Mélanger sans faire retomber, monter des blancs, cuire juste.", techs: ["incorporer", "separer-oeuf", "bain-marie"], recipes: ["gateau_yaourt", "mousse_chocolat"] },
  { id: "tarte", title: "Pâte à tarte et crème pâtissière", why: "Le duo des tartes de pâtissier.", techs: ["pate-sucree", "creme-patissiere"], recipes: ["tarte_fraises", "flan_patissier"] },
  { id: "choux", title: "La pâte à choux", why: "Le premier vrai défi de pâtisserie, et une grande fierté.", techs: ["pate-a-choux", "creme-chantilly-ganache-montee"], recipes: ["chouquettes", "eclairs_chocolat"] },
];
