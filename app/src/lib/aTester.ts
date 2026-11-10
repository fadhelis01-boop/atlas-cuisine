// Protocole d'essai en cuisine (audit gourmet 2026-10-21, recommandation 10). Aucune fiche d'ATLAS n'a été cuisinée :
// on commence par les 30 plats que « Ma semaine » propose le plus souvent (simulation de 26 semaines, test 80), car ce
// sont eux qu'un foyer rencontrera d'abord. Liste à régénérer si le planificateur change (voir la sortie du test 80).
import { RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

export const PRIORITE: string[] = [
  "moules_frites", "gratin_celeri_noix", "boeuf_oignons_saute", "spaetzle_fromage", "pollo_al_ajillo", "dhal_epinards_coco", "sundubu_jjigae", "shiro_wat",
  "curry_legumes_coco", "bacalhau_bras", "ful_medames", "cassolettes_crevettes_poireaux", "curry_pois_chiches_express", "raclette_maison", "moqueca", "bamia_gombo",
  "chou_oeufs_saute", "moules_normande", "matoke", "dakgalbi", "fiskesuppe", "kottu_roti", "shakshuka_verte_feta", "ramen_coreen_champignons_cremeux",
  "lo_mein_chou_legumes", "pates_pesto_vert_poireau", "pyttipanna_boeuf", "bunny_chow_haricots", "vermicelles_riz_sautes_legumes", "anda_curry",
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
