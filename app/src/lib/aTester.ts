// Protocole d'essai en cuisine (audit gourmet 2026-10-21, recommandation 10). Aucune fiche d'ATLAS n'a été cuisinée :
// on commence par les 30 plats que « Ma semaine » propose le plus souvent (simulation de 26 semaines, test 80), car ce
// sont eux qu'un foyer rencontrera d'abord. Liste à régénérer si le planificateur change (voir la sortie du test 80).
import { RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

export const PRIORITE: string[] = [
  "moules_frites",
  "curry_pois_chiches_express",
  "bar_croute_sel",
  "curry_legumes_coco",
  "chop_suey_boeuf",
  "cassolettes_crevettes_poireaux",
  "bunny_chow_haricots",
  "fiskesuppe",
  "orecchiette_brocoli_ail",
  "bacalhau_bras",
  "nikujaga",
  "pyttipanna_boeuf",
  "spaghetti_sautes_legumes_oeufs",
  "shakshuka_verte_feta",
  "linguine_moules_scarole",
  "thiou_poulet",
  "falafels",
  "thukpa",
  "dhal_epinards_coco",
  "encornets_persillade",
  "islak_burger",
  "atakilt_wat",
  "white_chicken_chili",
  "eomuk_tang",
  "dal_tadka",
  "bamia_gombo",
  "rolex_ouganda",
  "ash_reshteh",
  "frites_chargees_haricots",
  "choucroute_mer",
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
