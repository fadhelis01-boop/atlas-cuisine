// Protocole d'essai en cuisine (audit gourmet 2026-10-21, recommandation 10). Aucune fiche d'ATLAS n'a été cuisinée :
// on commence par les 30 plats que « Ma semaine » propose le plus souvent (simulation de 26 semaines, test 80), car ce
// sont eux qu'un foyer rencontrera d'abord. Liste à régénérer si le planificateur change (voir la sortie du test 80).
import { RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

export const PRIORITE: string[] = [
  "moules_frites", "gratin_chou_fleur_lentilles", "salade_haricots_blancs_thon", "gratin_celeri_noix", "locro_vegetarien", "goan_fish_curry", "poisson_braise_camerounais", "curry_legumes_coco",
  "moules_marinieres", "curry_pois_chiches_express", "spaetzle_fromage", "bacalhau_bras", "kofta_grillees", "dhal_epinards_coco", "fiskesuppe", "shakshuka_verte_feta",
  "spanakorizo", "moqueca", "nikujaga", "bar_croute_sel", "bamia_gombo", "udon_sautees_legumes", "pyttipanna_boeuf", "ful_medames",
  "misir_wat", "chana_masala", "salade_lentilles_saumon_fume", "moules_normande", "bar_croute_macadamia", "atakilt_wat",
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
