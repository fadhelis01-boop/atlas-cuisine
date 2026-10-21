// Protocole d'essai en cuisine (audit gourmet 2026-10-21, recommandation 10). Aucune fiche d'ATLAS n'a été cuisinée :
// on commence par les 30 plats que « Ma semaine » propose le plus souvent (simulation de 26 semaines, test 80), car ce
// sont eux qu'un foyer rencontrera d'abord. Liste à régénérer si le planificateur change (voir la sortie du test 80).
import { RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

export const PRIORITE: string[] = [
  "moules_frites", "curry_pois_chiches_express", "bar_croute_sel", "curry_legumes_coco", "crevettes_coco_citron_vert", "gratin_chou_fleur_lentilles", "hot_pot_familial", "falafels",
  "moqueca", "bowl_tofu_croustillant", "larb_poulet", "tacos_al_pastor", "moules_marinieres", "bunny_chow_haricots", "bacalhau_bras", "shakshuka_haricots_blancs",
  "breakfast_burrito", "lobio", "sapasui", "spaghetti_aglio_olio", "chilaquiles_verts", "tacos_poisson_express", "maharagwe", "salade_haricots_blancs_thon",
  "dibi", "choucroute_mer", "stamppot_boerenkool", "spaghetti_vongole", "shakshuka", "nasi_goreng",
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
