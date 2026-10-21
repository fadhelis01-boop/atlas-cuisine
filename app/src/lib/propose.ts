// « Je n'ai pas d'idée, propose-moi » (audit UX 🟠 6) : trois suggestions en un geste, selon l'heure,
// la saison du lieu, le temps disponible et ce qu'il y a dans le frigo. Trois cuisines différentes.
// Retour d'usage 2026-10-22 : la saison écrasait le hasard (7 recettes sur 60 propositions, moules-frites à chaque appui).
// Désormais : saison et frigo donnent un bonus borné, le tirage est pondéré et les 45 dernières idées sont écartées.
import { flatten } from "./engine";
import { seasonFit, type Zone } from "./season";
import { norm } from "./text";
import type { Recipe } from "./types";
import { pickVaried } from "./variete";

export interface Proposal { r: Recipe; why: [icon: string, text: string][] }

const BREAKFAST = new RegExp(["bircher|muesli|porridge|granola|overnight|smoothie|chia|pancake|crepe|gaufre|pain perdu|tartine|parfait",
  "yaourt|congee|oeufs|omelette|shakshuka|brioche|croissant|chausson|muffin|banana bread|cake|scone|bagel|msemen|baghrir|beignet|galette"].join("|"));
const isDrink = (r: Recipe) => r.role === "boisson" || r.kind === "Boisson";
const sweet = (r: Recipe) => !isDrink(r) && (r.role === "dessert" || r.kind === "Goûter / dessert");
// un plat salé n'est un petit-déjeuner que s'il en est un vrai (œufs brouillés, shakshuka, congee…), pas une salade aux œufs durs
const BREAKFAST_PLAT = /omelette|oeufs brouill|oeufs (au plat|cocotte|mollets|benedicte)|shakshuka|menemen|congee|chilaquiles|breakfast|huevos|tartine|toast|pancake|crepe|galette|porridge/;
const breakfast = (r: Recipe) => !isDrink(r) && r.role !== "autre" && (r.cats.includes("brunch")
  || (r.role === "plat" ? BREAKFAST_PLAT.test(norm(`${r.title} ${r.id}`)) && r.active + r.rest <= 30
    : BREAKFAST.test(norm(`${r.title} ${r.id}`)) && (r.role === "dessert" || r.cats.includes("pains"))));

/** Le moment de la journée décide du type de recette : plat aux repas, petit-déjeuner le matin, goûter l'après-midi. Jamais une boisson seule. */
export function momentOf(hour: number): { label: string; test: (r: Recipe) => boolean } {
  const plat = (r: Recipe) => r.role === "plat";
  if (hour >= 5 && hour < 11) return { label: "pour le petit-déjeuner ou le brunch", test: breakfast };
  if (hour >= 14 && hour < 18) return { label: "pour le goûter", test: sweet };
  if (hour >= 23 || hour < 5) return { label: "pour une petite faim", test: (r) => plat(r) && r.active + r.rest <= 25 };
  return { label: hour < 14 ? "pour midi" : "pour ce soir", test: plat };
}

export interface ProposeOptions { hour: number; zone: Zone; maxMinutes: number; fridge: string[]; seed: number; recent?: ReadonlySet<string> }

export function propose(list: Recipe[], o: ProposeOptions): Proposal[] {
  const m = momentOf(o.hour);
  const fridge = new Set(o.fridge);
  const cands = list.filter((r) => m.test(r) && r.active + r.rest <= o.maxMinutes).map((r) => {
    const fit = seasonFit(r, o.zone);
    const used = [...new Set(flatten(r.ingredients).filter((l) => l.ref && fridge.has(l.ref) && l.weight >= 1).map((l) => l.ref!))];
    // bonus borné : un plat de saison sort plus souvent, il ne sort pas à chaque fois
    const score = Math.max(-2, Math.min(4, fit.score)) * 0.6 + Math.min(3, used.length) * 2.5;
    return { r, fit, used, score };
  });
  const picked = pickVaried(cands, 3, { seed: o.seed, score: (x) => x.score, temperature: 1.6, recent: o.recent, id: (x) => x.r.id, distinct: (x) => x.r.macro });
  return picked.map((x) => {
    const why: [string, string][] = [];
    if (x.used.length) why.push(["fridge", `avec ton ${x.used.slice(0, 2).map((n) => n.split(/ \/ | \(/)[0].toLowerCase()).join(" et ")}`]);
    if (x.fit.inSeason.length) why.push(["sprout", `${x.fit.inSeason.slice(0, 2).map((n) => n.split(/ \/ | \(/)[0].toLowerCase()).join(", ")} de saison`]);
    else if (x.fit.mood) why.push(x.fit.mood === "chaud" ? ["flame", "réconfortant"] : ["snowflake", "frais"]);
    why.push(["timer", `${x.r.active + x.r.rest} min en tout`]);
    return { r: x.r, why };
  });
}
