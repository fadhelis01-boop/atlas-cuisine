// Socle commun des tests du moteur (audit dév/UX 2026-10-21 §4) : imports, données, fonction check et fixtures partagées.
// Chaque suite (e1 à e4) a sa propre portée : deux contrôles ne peuvent plus se télescoper sur un nom de variable.
import { INGREDIENTS, INGREDIENT_NAMES, RECIPES, RECIPE_BY_ID, loadImports, loadLeftovers, mergeDetails } from "../src/lib/data";
import recipeDetail from "../src/data/recipes_detail.json";
import { evaluate, evaluateLines, flatten, suggest, verdict } from "../src/lib/engine";
import { classify, linksFromExport } from "../src/lib/classify";
import { embedOf } from "../src/components/video";
import { gestureLabel, norm, ovenPlan, splitStep } from "../src/lib/text";
import { TECHNIQUES, techniqueFor } from "../src/lib/techniques";
import { dishEmoji } from "../src/components/art";
import { rescueFor } from "../src/lib/rescue";
import { GLOSSAIRE, termsIn } from "../src/lib/glossaire";
import { PARCOURS } from "../src/lib/parcours";
import { substitutOf } from "../src/lib/substituts";
import { RESTES, buildMenu, ideasFor, restesOfRecipe, resteStatus } from "../src/lib/restes";
import { RAYONS, RATTRAPAGES, choixOf } from "../src/lib/marche";
import { ADOUCI, defaultPortions, householdPortions, kidFriendly, starchOf, weekBalance, isRich } from "../src/lib/famille";
import { DEJA, PANIERS, piqueNique } from "../src/lib/piquenique";
import { equipmentNotes } from "../src/lib/equipement";
import { backupDue } from "../src/lib/store";
import { composeMenus } from "../src/lib/menu";
import { isBigDish } from "../src/lib/planner";
import { balanceOf, finishFor } from "../src/lib/dressage";
import { cuesIn, saltDose } from "../src/lib/cues";
import { fuzzyRecipes, parseIntents } from "../src/lib/intents";
import etapes from "../src/data/etapes.json";
import imagesCore from "../src/data/images.json";
import credits from "../src/data/credits.json";
import imagesMore from "../src/data/images_more.json";
import { autoPlan, consolidate, prepAhead, proteinOf, weekDays } from "../src/lib/planner";
import { PRIORITE, PROTOCOLE } from "../src/lib/aTester";
import type { Profile, Recipe, RecipeLine, Rule } from "../src/lib/types";

export const IMPORT_LIBRARY = await loadImports();
export const LEFT = await loadLeftovers();
export const images = { ...imagesCore, ...imagesMore };
mergeDetails(recipeDetail as Parameters<typeof mergeDetails>[0]); // détail des fiches (chargé à la demande dans l'appli)

let passed = 0;
export const passedCount = () => passed;
export function check(name: string, cond: boolean) {
  console.log((cond ? "PASS " : "FAIL ") + name);
  if (!cond) { process.exitCode = 1; throw new Error(name); }
  passed++;
}
export const base: Profile = { noPork: false, alcohol: "allowed", strict: false, vegetarian: false, allergens: [], adult: true, kidsAge: null, equipment: [], onboarded: true };
export const P = (o: Partial<Profile>): Profile => ({ ...base, ...o });
export const L = (ref: string | null, weight = 2, optional = false): RecipeLine => ({ qty: "", label: ref ?? "eau", ref, weight, optional });
export const mk = (id: string, lines: RecipeLine[], extra: Partial<Recipe> = {}): Recipe =>
  ({ ...RECIPE_BY_ID["ratatouille"], id, title: id, ingredients: lines, variants: [], ...extra });
// partagés entre suites
export const ET = etapes as Record<string, { k: string; c: string }[]>;
export const IM = images as Record<string, { avif?: number }>;
export const plats = RECIPES.filter((r) => r.role === "plat");
export const P0 = { noPork: false, alcohol: "allowed" as const, strict: false, vegetarian: false, allergens: [] as string[], adult: false, kidsAge: null, equipment: ["four", "plaques", "poele", "casserole", "mixeur"], onboarded: true };

export const pa = prepAhead(["pot_au_feu", "pates_pesto", "salade_lentilles"]);
