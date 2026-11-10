// Protocole d'essai en cuisine (audit gourmet 2026-10-21, recommandation 10). Aucune fiche d'ATLAS n'a été cuisinée :
// on commence par les 30 plats que « Ma semaine » propose le plus souvent (simulation de 26 semaines, test 80), car ce
// sont eux qu'un foyer rencontrera d'abord. Liste à régénérer si le planificateur change (voir la sortie du test 80).
import { RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

export const PRIORITE: string[] = [
  "moules_frites", "white_chicken_chili", "fiskefrikadeller", "curry_legumes_coco", "nouilles_sautees_boeuf", "locro_vegetarien", "goan_fish_curry", "bacalhau_bras",
  "gratin_celeri_noix", "salade_haricots_blancs_thon", "pancit_bihon", "fiskesuppe", "berkoukes_legumes", "bunny_chow_haricots", "cassolettes_crevettes_poireaux", "curry_fidjien_legumes",
  "falafels", "pyttipanna_boeuf", "pasta_genovese", "spaetzle_fromage", "nikujaga", "vermicelles_riz_sautes_legumes", "atakilt_wat", "moules_marinieres",
  "arayes_boeuf_feta", "shiro_wat", "bar_croute_sel", "choucroute_mer", "kottu_roti", "raclette_maison",
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
