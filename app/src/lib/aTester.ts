// Protocole d'essai en cuisine (audit gourmet 2026-10-21, recommandation 10). Aucune fiche d'ATLAS n'a été cuisinée :
// on commence par les 30 plats que « Ma semaine » propose le plus souvent (simulation de 26 semaines, test 80), car ce
// sont eux qu'un foyer rencontrera d'abord. Liste à régénérer si le planificateur change (voir la sortie du test 80).
import { RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

export const PRIORITE: string[] = [
  "moules_frites", "curry_pois_chiches_express", "fiskefrikadeller", "curry_legumes_coco", "spaghetti_sautes_crevettes", "shakshuka_verte_feta", "muffins_oeufs_legumes", "bacalhau_bras",
  "dhal_epinards_coco", "linguine_moules_scarole", "thiou_poulet", "yasai_kare", "fiskesuppe", "chana_masala", "chop_suey_boeuf", "salade_haricots_blancs_thon",
  "anda_curry", "choucroute_mer", "thukpa", "crevettes_coco_citron_vert", "nouilles_sautees_legumes_oeuf", "gratin_chou_fleur_lentilles", "nikujaga", "falafels",
  "goan_fish_curry", "pad_see_ew", "moules_normande", "pyttipanna_boeuf", "encornets_persillade", "dal_tadka",
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
