// Protocole d'essai en cuisine (audit gourmet 2026-10-21, recommandation 10). Aucune fiche d'ATLAS n'a été cuisinée :
// on commence par les 30 plats que « Ma semaine » propose le plus souvent (simulation de 26 semaines, test 80), car ce
// sont eux qu'un foyer rencontrera d'abord. Liste à régénérer si le planificateur change (voir la sortie du test 80).
import { RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

export const PRIORITE: string[] = [
  "moules_frites", "gratin_chou_fleur_lentilles", "nikujaga", "curry_legumes_coco", "parippu", "bacalhau_bras", "dhal_epinards_coco", "cassolettes_crevettes_poireaux",
  "curry_pois_chiches_express", "fiskefrikadeller", "chou_oeufs_saute", "spaghetti_sautes_legumes_oeufs", "moules_marinieres", "fiskesuppe", "falafels", "moqueca",
  "shiro_wat", "poke_bowl_saumon", "saumon_cajun_noirci", "shakshuka_verte_feta", "poisson_braise_camerounais", "pancit_bihon", "dal_tadka", "caldou_poisson",
  "nasi_goreng", "ramen_miso_legumes_tofu", "tortilla_espanola", "spaghetti_aglio_olio", "lu_sipi_agneau_coco", "rougag_dajaj",
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
