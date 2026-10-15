import { useSyncExternalStore } from "react";
import ingredientsJson from "../data/ingredients.json";
import recipesJson from "../data/recipes.json";
import rulesJson from "../data/rules.json";
import catalogueJson from "../data/catalogue.json";
import type { CatalogueEntry, ImportEntry, IngredientRef, Leftover, MacroId, Recipe, Rule } from "./types";

export const INGREDIENTS = ingredientsJson as unknown as Record<string, IngredientRef>;
export const RECIPES = recipesJson as unknown as Recipe[];
export const RULES = rulesJson as unknown as Rule[];
export const CATALOGUE = catalogueJson as unknown as CatalogueEntry[];
// Bibliothèque de vidéos classées (3 000 et plus) : chargée à la demande pour garder l'ouverture de l'application rapide.
let IMP: ImportEntry[] | null = null;
let impP: Promise<ImportEntry[]> | null = null;
const impListeners = new Set<() => void>();
export function loadImports(): Promise<ImportEntry[]> {
  impP ??= import("../data/imports.json").then((m) => { IMP = m.default as unknown as ImportEntry[]; impListeners.forEach((l) => l()); return IMP; });
  return impP;
}
const NO_IMPORTS: ImportEntry[] = [];
export function useImportLibrary(): ImportEntry[] {
  return useSyncExternalStore((cb) => { impListeners.add(cb); void loadImports(); return () => { impListeners.delete(cb); }; }, () => IMP ?? NO_IMPORTS);
}

export const RECIPE_BY_ID: Record<string, Recipe> = Object.fromEntries(RECIPES.map((r) => [r.id, r]));
export const INGREDIENT_NAMES = Object.keys(INGREDIENTS);

export const MACROS: { id: MacroId; name: string; emoji: string; blurb: string }[] = [
  { id: "france", name: "France", emoji: "🥖", blurb: "Régions, terroirs et Outre-mer : de la galette bretonne aux accras antillais." },
  { id: "europe_sud", name: "Europe du Sud", emoji: "🍅", blurb: "Italie, Espagne, Portugal, Grèce : huile d'olive, tomates, herbes." },
  { id: "europe_nord", name: "Europe du Nord, Centrale & de l'Est", emoji: "🥨", blurb: "Belgique, Allemagne, Scandinavie, Europe de l'Est : pains, choux, fumaisons." },
  { id: "maghreb", name: "Maghreb & Égypte", emoji: "🍵", blurb: "Algérie, Maroc, Tunisie, Égypte : épices douces, semoule, tajines et thé à la menthe." },
  { id: "afrique", name: "Afrique subsaharienne", emoji: "🌶️", blurb: "Sénégal, Mali, Côte d'Ivoire, Nigeria, Éthiopie : mafés, yassa, jollof, bissap." },
  { id: "moyen_orient", name: "Moyen-Orient & Caucase", emoji: "🧆", blurb: "Liban, Turquie, Iran, Syrie : mezzés, herbes fraîches, grenade et sésame." },
  { id: "asie_sud", name: "Asie du Sud", emoji: "🍛", blurb: "Inde, Pakistan, Sri Lanka : dals, currys, pains plats, lassi." },
  { id: "asie_est", name: "Asie de l'Est", emoji: "🥢", blurb: "Chine, Japon, Corée, Taïwan : riz, nouilles, sautés, fermentations." },
  { id: "asie_sud_est", name: "Asie du Sud-Est", emoji: "🍜", blurb: "Thaïlande, Vietnam, Indonésie, Philippines : herbes, citron vert, lait de coco." },
  { id: "amerique_nord", name: "Amérique du Nord", emoji: "🍔", blurb: "États-Unis, Canada, cuisine cajun : barbecue, pancakes, comfort food." },
  { id: "amerique_latine", name: "Amérique latine & Caraïbes", emoji: "🌮", blurb: "Mexique, Brésil, Pérou, Antilles : maïs, haricots, piments, agrumes." },
  { id: "oceanie", name: "Océanie", emoji: "🥝", blurb: "Australie, Nouvelle-Zélande, Pacifique." },
  { id: "fusion", name: "Food fusion", emoji: "🌐", blurb: "Les recettes qui mélangent plusieurs traditions ou dont l'origine ne tient pas dans un seul pays : tex-mex, pizza au butter chicken, fish & chips en feuille de riz, couscous-tiep…" },
];
export const MACRO_BY_ID = Object.fromEntries(MACROS.map((m) => [m.id, m])) as Record<MacroId, (typeof MACROS)[number]>;

/** Rubriques des imports classés (TikTok, sites) → libellé. */
export const IMPORT_CATS: Record<string, string> = {
  afrique: "Afrique de l'Ouest & centrale", maghreb: "Maghreb", moyen_orient: "Moyen-Orient, Turquie & Balkans", asie: "Asie",
  italie: "Italie", france: "France", europe: "Europe (autres)", ameriques: "Amériques & Caraïbes", street_food: "Street food maison",
  pains: "Pains, pâtes & bases", sauces: "Sauces & marinades", fait_maison: "Fait maison sans additifs", desserts: "Desserts & pâtisserie",
  boissons: "Boissons", techniques: "Techniques & astuces", zero_dechet: "Zéro déchet", fetes: "Fêtes", fusion: "Food fusion", a_verifier: "À vérifier", autre: "Autre",
};

/** Correspondance rubrique d'import → macro-région de l'atlas (pour « Dans tes imports »). */
export const IMPORT_CAT_TO_MACRO: Record<string, MacroId[]> = {
  afrique: ["afrique"], maghreb: ["maghreb"], moyen_orient: ["moyen_orient"], asie: ["asie_est", "asie_sud", "asie_sud_est"],
  italie: ["europe_sud"], france: ["france"], europe: ["europe_nord", "europe_sud"], ameriques: ["amerique_nord", "amerique_latine"], fusion: ["fusion"],
};

export const ALLERGENS: Record<string, string> = {
  GL: "Gluten", CR: "Crustacés", OE: "Œufs", PO: "Poissons", AR: "Arachide", SO: "Soja", LA: "Lait", FC: "Fruits à coque",
  CE: "Céleri", MO: "Moutarde", SE: "Sésame", SU: "Sulfites", LU: "Lupin", MM: "Mollusques",
};

export const CATEGORY_LABEL: Record<string, string> = {
  pains: "Pains, pâtes & bases", sauces: "Sauces maison", fetes: "Fêtes", enfants: "Enfants", zero_dechet: "Zéro déchet",
  boissons: "Boissons", techniques: "Techniques", fusion: "Food fusion",
};

/** Recettes d'une entrée de l'atlas (la « Food fusion » est une rubrique transversale, pas une macro-région). */
export const recipesOfMacro = (id: MacroId) => RECIPES.filter((r) => (id === "fusion" ? r.cats.includes("fusion") : r.macro === id));

// Restes zéro déchet de chaque recette (Tome 12 §6) : 35 % des données de recettes, chargés seulement quand une fiche s'ouvre.
let LEFT: Record<string, Leftover[]> | null = null;
let leftP: Promise<Record<string, Leftover[]>> | null = null;
const leftListeners = new Set<() => void>();
export function loadLeftovers(): Promise<Record<string, Leftover[]>> {
  leftP ??= import("../data/leftovers.json").then((m) => { LEFT = m.default as unknown as Record<string, Leftover[]>; leftListeners.forEach((l) => l()); return LEFT; });
  return leftP;
}
const NO_LEFT: Leftover[] = [];
export function useLeftovers(id: string): Leftover[] | null {
  return useSyncExternalStore((cb) => { leftListeners.add(cb); void loadLeftovers(); return () => { leftListeners.delete(cb); }; }, () => (LEFT ? LEFT[id] ?? NO_LEFT : null));
}
