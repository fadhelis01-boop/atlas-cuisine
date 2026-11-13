// Protocole d'essai en cuisine (audit gourmet 2026-10-21, recommandation 10). Aucune fiche d'ATLAS n'a été cuisinée :
// on commence par les 30 plats que « Ma semaine » propose le plus souvent (simulation de 26 semaines, test 80), car ce
// sont eux qu'un foyer rencontrera d'abord. Liste à régénérer si le planificateur change (voir la sortie du test 80).
import { RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

export const PRIORITE: string[] = [
  "moules_frites",
  "curry_pois_chiches_express",
  "curry_legumes_coco",
  "lieu_croute_herbes",
  "eomuk_tang",
  "thiou_poulet",
  "spaghetti_sautes_crevettes",
  "bacalhau_bras",
  "falafels",
  "vindaloo",
  "linguine_moules_scarole",
  "laxpudding",
  "fiskesuppe",
  "shakshuka_verte_feta",
  "moules_normande",
  "parippu",
  "salade_haricots_blancs_thon",
  "pyttipanna_boeuf",
  "spaghetti_sautes_legumes_oeufs",
  "chop_suey_boeuf",
  "moqueca",
  "mafe_vegetarien",
  "atakilt_wat",
  "vermicelles_riz_sautes_legumes",
  "pommes_terre_hache_poele",
  "dhal_epinards_coco",
  "bar_croute_sel",
  "yaki_udon",
  "raclette_maison",
  "sukiyaki",
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
