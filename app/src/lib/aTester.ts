// Protocole d'essai en cuisine (audit gourmet 2026-10-21, recommandation 10). Aucune fiche d'ATLAS n'a été cuisinée :
// on commence par les 30 plats que « Ma semaine » propose le plus souvent (simulation de 26 semaines, test 80), car ce
// sont eux qu'un foyer rencontrera d'abord. Liste à régénérer si le planificateur change (voir la sortie du test 80).
import { RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

export const PRIORITE: string[] = [
  "moules_frites", "thiou_poulet", "moqueca", "curry_legumes_coco", "larb_poulet", "bunny_chow_haricots", "hot_pot_familial", "gratin_celeri_noix",
  "crevettes_coco_citron_vert", "white_chicken_chili", "cassolettes_crevettes_poireaux", "shakshuka_haricots_blancs", "bacalhau_bras", "shakshuka", "choucroute_mer", "curry_pois_chiches_express",
  "goan_fish_curry", "anda_curry", "spaghetti_vongole", "bar_croute_sel", "frijoles_negros_cubanos", "moules_normande", "fiskesuppe", "risotto_courge_sauge",
  "lecso", "tacos_papa_rajas", "pap_chakalaka", "chili_con_carne", "salade_poulet_mangue_thai", "dorade_four",
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
