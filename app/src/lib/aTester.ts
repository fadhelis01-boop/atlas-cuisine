// Protocole d'essai en cuisine (audit gourmet 2026-10-21, recommandation 10). Aucune fiche d'ATLAS n'a été cuisinée :
// on commence par les 30 plats que « Ma semaine » propose le plus souvent (simulation de 26 semaines, test 80), car ce
// sont eux qu'un foyer rencontrera d'abord. Liste à régénérer si le planificateur change (voir la sortie du test 80).
import { RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

export const PRIORITE: string[] = [
  "moules_frites", "nikujaga", "curry_legumes_coco", "locro_vegetarien", "chop_suey_boeuf", "bacalhau_bras", "pyttipanna_boeuf", "linguine_moules_scarole",
  "sapasui", "muffins_oeufs_legumes", "dhal_epinards_coco", "tajine_poulet_citron", "fiskefrikadeller", "anda_curry", "bar_croute_macadamia", "salade_haricots_blancs_thon",
  "cassolettes_crevettes_poireaux", "yasai_kare", "fiskesuppe", "falafels", "goan_fish_curry", "pates_pesto_vert_poireau", "shakshuka_verte_feta", "bamia_gombo",
  "chou_oeufs_saute", "curry_pois_chiches_express", "moules_marinieres", "gratin_chou_fleur_lentilles", "lieu_croute_herbes", "kottu_roti",
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
