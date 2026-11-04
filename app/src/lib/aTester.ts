// Protocole d'essai en cuisine (audit gourmet 2026-10-21, recommandation 10). Aucune fiche d'ATLAS n'a été cuisinée :
// on commence par les 30 plats que « Ma semaine » propose le plus souvent (simulation de 26 semaines, test 80), car ce
// sont eux qu'un foyer rencontrera d'abord. Liste à régénérer si le planificateur change (voir la sortie du test 80).
import { RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

export const PRIORITE: string[] = [
  "moules_frites", "bar_croute_sel", "curry_legumes_coco", "goan_fish_curry", "ramen_miso_legumes_tofu", "fiskesuppe", "arayes_boeuf_feta", "poulet_citronnelle_express",
  "moules_marinieres", "curry_fidjien_legumes", "pyttipanna_boeuf", "bunny_chow_haricots", "ca_kho_to", "spaghetti_vongole", "parippu", "cassolettes_crevettes_poireaux",
  "choucroute_mer", "thiou_poulet", "tortilla_espanola", "nasi_goreng", "aji_de_gallina", "falafels", "nikujaga", "atakilt_wat",
  "moqueca", "curry_pois_chiches_express", "fiskefrikadeller", "islak_burger", "chilaquiles_verts", "laxpudding",
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
