// « Que cuisiner avec mon frigo ? » (retour d'usage du 22/10/2026 : pas de bouton, des idées sans rapport, rien d'autre à
// proposer si les premières ne plaisent pas). On choisit ce qu'on veut (un plat, une entrée, un dessert ou un menu
// complet), on lance, et chaque appui sur « D'autres idées » en propose de nouvelles sans revenir sur les précédentes.
import { INGREDIENTS } from "./data";
import { refsOf, suggest, type Suggestion } from "./engine";
import { pickVaried } from "./variete";
import type { Recipe } from "./types";

export type Course = "plat" | "entree" | "dessert" | "menu";
export const COURSES: { id: Course; label: string }[] = [
  { id: "plat", label: "Un plat" }, { id: "entree", label: "Une entrée" }, { id: "dessert", label: "Un dessert" }, { id: "menu", label: "Un menu complet" },
];

export interface FridgeIdea {
  r: Recipe;
  s: Suggestion;
  /** ingrédients choisis que la recette utilise (directement ou en remplacement) */
  used: string[];
  score: number;
}

export interface FridgeOptions {
  have: string[];
  pantry: Set<string>;
  expiring?: Set<string>;
  /** temps total maximum, en minutes (0 = sans limite) */
  maxMinutes?: number;
  /** tout utiliser au mieux (anti-gaspi) : les recettes qui prennent plus d'ingrédients choisis passent devant */
  useMost?: boolean;
}

const DERIVED: Record<string, string[]> = {
  "Œuf entier (frais)": ["Jaune d'œuf", "Blanc d'œuf"], "Poulet entier": ["Cuisse / pilon de poulet", "Blanc de poulet", "Ailes de poulet"],
  "Citron": ["Jus de citron (bouteille)"], "Pain de campagne / complet": ["Pain rassis (réservé)"],
};

const ROLE: Record<Exclude<Course, "menu">, Recipe["role"]> = { plat: "plat", entree: "entree", dessert: "dessert" };

/** Toutes les recettes d'un service qui utilisent au moins un ingrédient choisi, notées. */
export function rankFor(recipes: Recipe[], course: Exclude<Course, "menu">, o: FridgeOptions): FridgeIdea[] {
  if (!o.have.length) return [];
  const have = new Set(o.have);
  // ce qu'on tire de ce qu'on a : des œufs donnent des jaunes et des blancs, un poulet entier des cuisses et des blancs
  for (const h of o.have) for (const d of DERIVED[h] ?? []) have.add(d);
  const pool = recipes.filter((r) => r.role === ROLE[course] && (!o.maxMinutes || r.active + r.rest <= o.maxMinutes));
  const byId = new Map(pool.map((r) => [r.id, r]));
  return suggest(pool, have, o.expiring ?? new Set(), 0.8, o.pantry).flatMap((s) => {
    const r = byId.get(s.id)!;
    const refs = new Set(refsOf(r));
    const subs = new Set(Object.values(s.substitutes).flat());
    const used = o.have.filter((h) => refs.has(h) || subs.has(h) || (DERIVED[h] ?? []).some((d) => refs.has(d)));
    if (!used.length) return [];
    // ce qui compte : utiliser ce qu'on a (et d'abord ce qui presse), avoir peu à acheter
    const share = used.length / o.have.length;
    // un ingrédient choisi qui est la base du plat (poulet d'un poulet rôti) compte plus qu'un œuf de liaison
    const weightOf = (h: string) => Math.max(0, ...r.ingredients.filter((l) => l.ref === h || (s.substitutes[l.ref ?? ""] ?? []).includes(h)).map((l) => l.weight));
    const main = used.reduce((t, h) => t + weightOf(h), 0);
    const score = s.score * 0.5 + (o.useMost ? 70 : 40) * share + 8 * Math.min(used.length, 4) + 4 * main - 9 * s.missing.length + 8 * s.usesExpiring.length;
    if (s.missing.length > 4) return [];
    return [{ r, s, used, score }];
  }).sort((a, b) => b.score - a.score);
}

/** Quelques idées variées parmi les meilleures ; `seen` écarte celles déjà montrées (bouton « D'autres idées »). */
export function pickIdeas(ranked: FridgeIdea[], n: number, seed: number, seen: ReadonlySet<string> = new Set()): FridgeIdea[] {
  const fresh = ranked.filter((x) => !seen.has(x.r.id));
  const pool = (fresh.length >= n ? fresh : ranked).slice(0, Math.max(n * 5, 24));
  return pickVaried(pool, n, { seed, score: (x) => x.score / 10, temperature: 1.4, id: (x) => x.r.id, recent: seen, distinct: (x) => x.r.id });
}

export interface FridgeMenu { entree?: FridgeIdea; plat?: FridgeIdea; dessert?: FridgeIdea; leftover: string[] }

/** Menu complet : le plat prend le plus d'ingrédients, l'entrée et le dessert se servent dans ce qui reste et ne
 *  répètent pas l'ingrédient principal du plat. */
export function buildMenu(recipes: Recipe[], o: FridgeOptions, seed: number, seen: ReadonlySet<string> = new Set()): FridgeMenu {
  // le plat du menu prend le plus d'ingrédients possible (mode anti-gaspi) et met en valeur la viande ou le poisson du
  // frigo s'il y en a : c'est ce qu'on ne servira ni en entrée ni en dessert
  const isFlesh = (h: string) => /^(Viandes|Poissons)/.test(INGREDIENTS[h]?.section ?? "");
  const flesh = o.have.filter(isFlesh);
  const plats = rankFor(recipes, "plat", { ...o, useMost: true })
    .map((x) => ({ ...x, score: x.score + (flesh.length && x.used.some(isFlesh) ? 35 : 0) })).sort((a, b) => b.score - a.score);
  const plat = pickIdeas(plats, 1, seed, seen)[0];
  const taken = new Set(plat?.used ?? []);
  const dominant = new Set(plat ? plat.r.ingredients.filter((l) => l.weight === 3 && l.ref).map((l) => l.ref!) : []);
  const side = (course: "entree" | "dessert", salt: number) => {
    // l'entrée et le dessert se servent d'abord dans ce que les autres services n'ont pas pris ; jamais le même
    // ingrédient principal que le plat
    const ranked = rankFor(recipes, course, o)
      .filter((x) => !x.r.ingredients.some((l) => l.weight === 3 && l.ref && dominant.has(l.ref)))
      .map((x) => ({ ...x, score: x.score + 30 * x.used.filter((h) => !taken.has(h)).length - 25 * x.used.filter((h) => taken.has(h)).length
        + (course === "dessert" && x.r.kind === "Dessert" ? 15 : 0) })) // en fin de repas, un vrai dessert plutôt qu'un biscuit de goûter
      .sort((a, b) => b.score - a.score);
    const pick = pickIdeas(ranked, 1, seed + salt, seen)[0];
    pick?.used.forEach((h) => taken.add(h));
    return pick;
  };
  const entree = side("entree", 17);
  const dessert = side("dessert", 31);
  const all = taken;
  return { entree, plat, dessert, leftover: o.have.filter((h) => !all.has(h)) };
}
