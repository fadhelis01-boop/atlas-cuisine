// Protocole d'essai en cuisine (audit gourmet 2026-10-21, recommandation 10). Aucune fiche d'ATLAS n'a été cuisinée :
// on commence par les 30 plats que « Ma semaine » propose le plus souvent (simulation de 26 semaines, test 80), car ce
// sont eux qu'un foyer rencontrera d'abord. Liste à régénérer si le planificateur change (voir la sortie du test 80).
import { RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

export const PRIORITE: string[] = [
  "curry_pois_chiches_express", "moules_frites", "curry_legumes_coco", "pancit_bihon", "eomuk_tang", "moules_marinieres", "thiou_poulet", "atakilt_wat",
  "thukpa", "curry_fidjien_legumes", "linguine_moules_scarole", "salade_haricots_blancs_thon", "yasai_kare", "shakshuka_verte_feta", "vermicelles_riz_sautes_legumes", "moqueca",
  "dhal_epinards_coco", "ramen_coreen_champignons_cremeux", "bacalhau_bras", "fiskesuppe", "anda_curry", "parippu", "gado_gado", "locro_vegetarien",
  "choripan", "cocido_madrileno_version", "bar_croute_sel", "raclette_maison", "sukiyaki", "pasta_e_patate",
];

/** Ce qu'on note à chaque essai, dans « Mon carnet » de la fiche. */
export const PROTOCOLE: string[] = [
  "Suis la fiche à la lettre une première fois, sans corriger en route.",
  "Chronomètre la préparation et la cuisson : écris l'écart avec les temps annoncés.",
  "Vérifie chaque repère (couleur, odeur, texture) : arrive-t-il au moment dit ?",
  "Goûte avant de servir : sel, acidité, piquant. Note ce que tu as dû ajouter.",
  "Note les quantités : restes, assiettes trop justes, ingrédient en trop ou manquant.",
  "Note sur 5 et écris ce qu'il faut changer, puis exporte le carnet.",
];

export const aTester = (): Recipe[] => PRIORITE.map((id) => RECIPE_BY_ID[id]).filter(Boolean);
