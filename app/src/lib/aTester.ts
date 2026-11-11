// Protocole d'essai en cuisine (audit gourmet 2026-10-21, recommandation 10). Aucune fiche d'ATLAS n'a été cuisinée :
// on commence par les 30 plats que « Ma semaine » propose le plus souvent (simulation de 26 semaines, test 80), car ce
// sont eux qu'un foyer rencontrera d'abord. Liste à régénérer si le planificateur change (voir la sortie du test 80).
import { RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

export const PRIORITE: string[] = [
  "moules_frites", "gratin_chou_fleur_lentilles", "nikujaga", "curry_legumes_coco", "chop_suey_boeuf", "vermicelles_riz_sautes_legumes", "curry_pois_chiches_express", "fiskefrikadeller",
  "bacalhau_bras", "dhal_epinards_coco", "linguine_moules_scarole", "thiou_poulet", "choucroute_mer", "parippu", "boeuf_oignons_saute", "bar_croute_macadamia",
  "poisson_braise_camerounais", "stamppot_boerenkool", "lo_mein_chou_legumes", "shakshuka_verte_feta", "atakilt_wat", "burger_vegetarien_haricots", "pyttipanna_boeuf", "kottu_roti",
  "fiskesuppe", "moules_normande", "white_chicken_chili", "ful_medames", "pancit_bihon", "curry_fidjien_legumes",
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
