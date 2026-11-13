// Cuisine du dimanche (audit famille nombreuse, 13/11/2026) : 3 ou 4 plats de la semaine préparés d'un coup, en 2 heures
// environ, dans l'ordre d'un cuisinier (mise en place commune, cuissons longues lancées d'abord, four, puis plaques),
// rangés au frais ou au congélateur selon le jour où on les mange. NON TESTÉ en cuisine (Tome 7 §2).
import { RECIPE_BY_ID, RECIPES } from "./data";
import { prepAhead } from "./planner";
import { norm } from "./text";
import type { Recipe } from "./types";

/** Combien de jours un plat cuit tient au frigo, et s'il se congèle (d'après sa fiche « Conservation »). */
export function keeping(r: Recipe): { days: number; freeze: boolean } {
  const t = norm(r.storage ?? "");
  const m = t.match(/(\d+) jours? au frigo/) ?? t.match(/(\d+) jours?/);
  return { days: /le jour meme/.test(t) && !m ? 0 : m ? +m[1] : 0, freeze: /congel/.test(t) };
}

/** Un plat qui vaut la peine d'être cuisiné à l'avance : il tient au moins 3 jours (ou se congèle) et ne se sert pas minute.
 *  Le type de plat (soufflé, tartare, carpaccio) se lit dans le titre, pas dans les étapes : sinon « soufflé » (le dessus
 *  qui gonfle) ou « souffler » (sur un plat chaud) dans n'importe quelle recette matche à tort. */
export const batchable = (r: Recipe) => {
  const k = keeping(r);
  const minute = /souffle|tartare(?! de)|carpaccio/.test(norm(r.title)) || /a la minute/.test(norm(r.title + " " + r.steps.join(" ")));
  return r.role === "plat" && !minute && (k.days >= 3 || k.freeze);
};

export type Phase = "long" | "four" | "plaques";
/** Où se passe l'essentiel de la cuisson : un mijotage long se lance en premier, le four tourne pendant ce temps. */
export function phaseOf(r: Recipe): Phase {
  const t = norm(r.steps.join(" "));
  if (r.rest >= 45 && /mijot|fremiss|braise|cocotte|a couvert/.test(t)) return "long";
  if (/\bfour\b|gratin|enfourne|\d{3} ?.?c/.test(t)) return "four";
  return "plaques";
}

export interface BatchPlan {
  recipes: Recipe[];
  veg: string[];
  phases: Record<Phase, Recipe[]>;
  minutes: number; // durée estimée de la séance
  storage: { r: Recipe; where: string; warn: boolean }[];
}

/** Un plat cuisiné le jour de la séance tient-il jusqu'au jour où on compte le manger (`d` jours plus tard) ?
 *  Un plat qui se congèle est toujours sûr ; sinon il faut que le frigo tienne au moins jusque-là. */
export const safeForDay = (r: Recipe, d: number): boolean => {
  const k = keeping(r);
  return k.freeze || d <= k.days;
};

/** Ce qu'on écrit sous un plat de la séance : où le ranger, et une alerte si le délai avant le repas dépasse ce que le
 *  frigo garantit (un plat qui ne se congèle pas et qu'on prévoit de manger après sa limite de fraîcheur). */
function storageNote(r: Recipe, d: number): { where: string; warn: boolean } {
  const k = keeping(r);
  const FREEZE = { where: "au congélateur, en portions ; la veille au soir, le passer au frigo pour qu'il décongèle", warn: false };
  if (d <= Math.min(k.days, 3)) return { where: `au frigo (mangé dans ${d} jour${d > 1 ? "s" : ""}, il tient ${k.days} jours)`, warn: false };
  if (d <= k.days) return { where: `au frigo (il tient ${k.days} jours ; prépare-le si possible plus près du repas)`, warn: false };
  if (k.freeze) return FREEZE;
  return { where: `ne tient que ${k.days} jour${k.days > 1 ? "s" : ""} au frigo : trop tôt pour un repas dans ${d} jours. Cuisine-le plutôt la veille ou l'avant-veille`, warn: true };
}

/** Le déroulé de la séance pour les plats choisis ; `eatDays[id]` = dans combien de jours, à partir de la séance, on
 *  compte manger chacun (0 = le jour même). */
export function batchPlan(ids: string[], eatDays: Record<string, number> = {}): BatchPlan {
  const recipes = ids.map((id) => RECIPE_BY_ID[id]).filter(Boolean) as Recipe[];
  const phases: Record<Phase, Recipe[]> = { long: [], four: [], plaques: [] };
  for (const r of recipes) phases[phaseOf(r)].push(r);
  // en parallèle, une séance dure la mise en place commune, plus le temps actif cumulé allégé de ce qui cuit seul
  const active = recipes.reduce((a, r) => a + r.active, 0);
  const longest = Math.max(0, ...recipes.map((r) => r.rest));
  const minutes = Math.round((20 + Math.max(active * 0.8, longest)) / 5) * 5;
  const storage = recipes.map((r) => ({ r, ...storageNote(r, eatDays[r.id] ?? 2) }));
  return { recipes, veg: prepAhead(ids).veg, phases, minutes, storage };
}

/** Plats à proposer quand la semaine n'en contient pas assez : faciles, pour les enfants, qui tiennent et se réchauffent. */
export function batchSuggestions(exclude: Set<string>, ok: (r: Recipe) => boolean, n = 8): Recipe[] {
  return RECIPES.filter((r) => batchable(r) && !exclude.has(r.id) && ok(r) && r.level <= 2 && r.age !== null && r.age <= 3)
    .sort((a, b) => b.rest - a.rest || a.id.localeCompare(b.id))
    .slice(0, n);
}

/** Les règles de rangement, les mêmes à chaque séance. */
export const RANGEMENT = [
  "Tout ce qui est cuit refroidit à découvert moins de 2 heures avant d'aller au frigo (un grand plat se partage en boîtes plates pour refroidir plus vite).",
  "Une boîte par repas, étiquetée : le nom du plat et la date du jour.",
  "Ce qui se mange après mercredi va au congélateur ; on le passe au frigo la veille au soir.",
  "Au moment du repas : réchauffé une seule fois, jusqu'à être fumant à cœur (63 °C au moins) ; les restes réchauffés ne se gardent pas.",
];
