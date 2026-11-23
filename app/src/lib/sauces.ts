// Coin sauces, audit « amateur indécis », chef senior (21/11/2026) : la page affichait 113 fiches `cats: ["sauces"]`
// dans une liste plate, sans classement ni filtre — et plus d'un tiers n'étaient pas des sauces (marinades, mélanges
// d'épices secs, bouillons, fonds, et même des frites). Liste organisée à la main, uniquement de vraies sauces,
// classées par famille comme le demande justement l'amateur indécis : fast-food, classiques de France, monde.
import { curatedRecipes } from "./catalog";
import type { Recipe } from "./types";

export type SauceFamily = "fastfood" | "france" | "monde";

export const SAUCE_FAMILY_LABEL: Record<SauceFamily, string> = {
  fastfood: "Fast-food & snack",
  france: "Classiques de France",
  monde: "Sauces du monde",
};

export interface SauceEntry {
  id: string;
  family: SauceFamily;
}

export const SAUCES: SauceEntry[] = [
  // ---- Fast-food & snack (friteries franco-belges + chaînes américaines)
  { id: "sauce_algerienne", family: "fastfood" },
  { id: "sauce_samourai", family: "fastfood" },
  { id: "sauce_blanche", family: "fastfood" },
  { id: "sauce_burger", family: "fastfood" },
  { id: "sauce_barbecue", family: "fastfood" },
  { id: "sauce_andalouse", family: "fastfood" },
  { id: "ketchup", family: "fastfood" },
  { id: "sauce_americaine_belge", family: "fastfood" },
  { id: "sauce_brazil", family: "fastfood" },
  { id: "sauce_facon_giant", family: "fastfood" },
  { id: "sauce_facon_big_tasty", family: "fastfood" },
  { id: "sauce_cheddar", family: "fastfood" },
  { id: "sauce_cocktail", family: "fastfood" },
  { id: "sauce_moutarde_miel", family: "fastfood" },
  { id: "sauce_big_mac", family: "fastfood" },
  { id: "sauce_chick_fil_a", family: "fastfood" },
  { id: "sauce_alabama_blanche", family: "fastfood" },
  { id: "sauce_yum_yum", family: "fastfood" },
  { id: "sauce_douce_acidulee_mcdo", family: "fastfood" },
  // ---- Classiques de France (bistrot, sauces mères, régionales)
  { id: "mayonnaise", family: "france" },
  { id: "bechamel", family: "france" },
  { id: "vinaigrette", family: "france" },
  { id: "moutarde_maison", family: "france" },
  { id: "beurre_maitre_hotel", family: "france" },
  { id: "beurre_blanc", family: "france" },
  { id: "tapenade", family: "france" },
  { id: "sauce_tartare", family: "france" },
  { id: "mayo_curry", family: "france" },
  { id: "mayo_herbes", family: "france" },
  { id: "mayo_safran", family: "france" },
  { id: "dijonnaise", family: "france" },
  { id: "sauce_bearnaise", family: "france" },
  { id: "sauce_hollandaise", family: "france" },
  { id: "sauce_roquefort", family: "france" },
  { id: "sauce_poivre", family: "france" },
  { id: "sauce_yaourt_herbes", family: "france" },
  { id: "ketchup_betterave", family: "france" },
  { id: "sauce_gribiche", family: "france" },
  { id: "sauce_vierge", family: "france" },
  { id: "sauce_champignons", family: "france" },
  { id: "persillade_frigo", family: "france" },
  { id: "sauce_diable", family: "france" },
  { id: "sauce_charcutiere", family: "france" },
  { id: "sauce_mornay", family: "france" },
  { id: "sauce_bordelaise", family: "france" },
  { id: "sauce_choron", family: "france" },
  { id: "sauce_ravigote", family: "france" },
  { id: "sauce_soubise", family: "france" },
  { id: "sauce_morilles", family: "france" },
  { id: "sauce_poivrade", family: "france" },
  { id: "sauce_veloute", family: "france" },
  { id: "sauce_espagnole", family: "france" },
  { id: "sauce_perigueux", family: "france" },
  { id: "sauce_chasseur", family: "france" },
  { id: "aioli", family: "france" },
  { id: "remoulade_francaise", family: "france" },
  // ---- Sauces du monde
  { id: "harissa", family: "monde" },
  { id: "pesto", family: "monde" },
  { id: "pates_pesto", family: "monde" },
  { id: "sauce_tomate", family: "monde" },
  { id: "tzatziki", family: "monde" },
  { id: "nokoss", family: "monde" },
  { id: "chermoula", family: "monde" },
  { id: "chimichurri", family: "monde" },
  { id: "sauce_chien", family: "monde" },
  { id: "sauce_piri_piri", family: "monde" },
  { id: "sweet_chili", family: "monde" },
  { id: "sauce_satay", family: "monde" },
  { id: "nuoc_cham", family: "monde" },
  { id: "chutney_mangue", family: "monde" },
  { id: "huile_pimentee", family: "monde" },
  { id: "sauce_tahini", family: "monde" },
  { id: "toum", family: "monde" },
  { id: "sauce_aigre_douce", family: "monde" },
  { id: "salsa_verde", family: "monde" },
  { id: "romesco", family: "monde" },
  { id: "raita", family: "monde" },
  { id: "pico_de_gallo", family: "monde" },
  { id: "mojo_canario", family: "monde" },
  { id: "sauce_cesar", family: "monde" },
  { id: "creme_balsamique_maison", family: "monde" },
  { id: "ajvar", family: "monde" },
  { id: "sauce_sriracha_maison", family: "monde" },
  { id: "sauce_tonkatsu", family: "monde" },
  { id: "sauce_unagi", family: "monde" },
  { id: "ssamjang", family: "monde" },
  { id: "zhug", family: "monde" },
  { id: "baba_ganoush", family: "monde" },
  { id: "banana_ketchup", family: "monde" },
  { id: "mayonnaise_japonaise", family: "monde" },
];

export const sauceRecipes = (f?: SauceFamily): (Recipe & { entry: SauceEntry })[] => curatedRecipes(SAUCES, (s) => !f || s.family === f);
