// La famille au centre (audit famille du 16/10/2026) : ce qui convient aux enfants du foyer, combien de parts cuisiner
// quand il y a des enfants, et l'équilibre d'une semaine de repas. Utilisé par l'accueil, la semaine, la recherche et les fiches.
import { evaluate } from "./engine";
import { norm } from "./text";
import type { Profile, Recipe } from "./types";

/** Âges des enfants déclarés (le foyer détaillé, sinon l'âge du plus jeune). */
export function kidsOf(p: Profile): number[] {
  if (p.household?.kids?.length) return p.household.kids;
  return p.kidsAge !== null && p.kidsAge !== undefined ? [p.kidsAge] : [];
}

// une fiche épicée reste possible pour les petits si elle dit comment l'adoucir (piment à part, version douce…)
export const ADOUCI = /sans (le )?piment|piment a part|a part pour les adultes|version douce|doux pour les enfants|sans epices fortes|sans garam/;

/** Un plat que le plus jeune enfant du foyer peut manger (âge de la fiche, piment, plats d'adultes). */
export function kidFriendly(r: Recipe, p: Profile): boolean {
  const kids = kidsOf(p);
  if (!kids.length) return true;
  const youngest = Math.min(...kids);
  if (youngest >= 12) return true;
  if (r.age === null || r.age > Math.max(youngest, 1)) return false;
  if (youngest < 6 && r.profile.includes("epice") && !ADOUCI.test(norm(r.kids ?? ""))) return false;
  return true;
}

/** Parts à cuisiner pour le foyer : un adulte = 1 ; un enfant de moins de 3 ans ≈ ⅓, de 3 à 10 ans ≈ ½, dès 11 ans = 1. */
export function householdPortions(p: Profile): number | null {
  const h = p.household;
  if (!h) return null;
  const kid = h.kids.reduce((a, age) => a + (age < 3 ? 1 / 3 : age < 11 ? 0.5 : 1), 0);
  return Math.max(1, Math.ceil(h.adults + kid - 0.01));
}
export const householdLabel = (p: Profile) => {
  const h = p.household; if (!h) return "";
  const k = h.kids.length;
  const ages = h.kids.length > 1 ? `${h.kids.slice(0, -1).join(", ")} et ${h.kids[h.kids.length - 1]}` : `${h.kids[0]}`;
  return `${h.adults} adulte${h.adults > 1 ? "s" : ""}${k ? ` et ${k} enfant${k > 1 ? "s" : ""} de ${ages} ans` : ""}`;
};

// ---------------------------------------------------------------- équilibre de la semaine
export type Starch = "pomme de terre" | "pâtes" | "riz" | "pain" | "semoule" | "légumineuses" | null;
export function starchOf(r: Recipe): Starch {
  const t = norm(`${r.title} ${r.ingredients.filter((l) => l.weight >= 2).map((l) => l.ref ?? "").join(" ")}`);
  if (/lentille|pois chiche|haricots (rouges|blancs|noirs)|feves|dal\b|pois casses/.test(t)) return "légumineuses";
  if (/pomme de terre|patate|frites|puree|gnocchi|tartiflette|raclette|parmentier|rosti/.test(t)) return "pomme de terre";
  if (/pates|spaghetti|nouilles|tagliatelle|penne|lasagne|macaroni|udon|ramen|ravioli/.test(t)) return "pâtes";
  if (/\briz\b|risotto|paella|biryani|pilaf/.test(t)) return "riz";
  if (/semoule|couscous|boulgour|quinoa/.test(t)) return "semoule";
  if (/pain|tortilla|pita|wrap|burger|pizza|croque|tartine/.test(t)) return "pain";
  return null;
}
/** Plats riches en fromage fondu ou en crème : une fois par semaine suffit. */
export const isRich = (r: Recipe) => /raclette|tartiflette|fondue|aligot|croziflette|reblochon|camembert roti|mont d.or|gratin dauphinois|carbonara|cordon bleu/.test(norm(r.title));
export const isFish = (r: Recipe) => r.profile.includes("poisson");
export const isVegetarian = (r: Recipe) => evaluate(r).flesh.length === 0;

export interface WeekBalance { meals: number; fish: number; legumes: number; vege: number; rich: number; starches: Record<string, number>; tips: string[] }
/** Bilan nutritionnel simple d'une semaine (repères du PNNS : poisson 2 fois, légumineuses 2 fois, peu de plats très riches). */
export function weekBalance(list: Recipe[]): WeekBalance {
  const starches: Record<string, number> = {};
  for (const r of list) { const s = starchOf(r); if (s) starches[s] = (starches[s] ?? 0) + 1; }
  const b = { meals: list.length, fish: list.filter(isFish).length, legumes: starches["légumineuses"] ?? 0, vege: list.filter(isVegetarian).length, rich: list.filter(isRich).length, starches, tips: [] as string[] };
  if (b.meals >= 5) {
    if (b.fish < 2) b.tips.push("Poisson : vise 2 repas par semaine, dont un poisson gras (saumon, maquereau, sardine).");
    if (b.legumes < 2) b.tips.push("Légumineuses : 2 repas par semaine (lentilles, pois chiches, haricots), bon marché et rassasiants.");
    if (b.rich > 1) b.tips.push("Plusieurs plats très riches en fromage ou en crème : garde-en un, et compense avec une soupe ou une salade composée.");
    const top = Object.entries(starches).sort((a, c) => c[1] - a[1])[0];
    if (top && top[1] >= 4) b.tips.push(`${top[0][0].toUpperCase() + top[0].slice(1)} ${top[1]} fois : varie les féculents (riz, pâtes complètes, semoule, pain, légumineuses).`);
  }
  return b;
}

/** Parts proposées par défaut sur une fiche : la taille du foyer pour un plat ou une entrée ; un gâteau, un pain, une sauce
 *  gardent leur recette entière (on ne fait pas « 3 parts » de brioche). */
export function defaultPortions(r: Recipe, p: Profile): number {
  const h = householdPortions(p);
  return h && (r.role === "plat" || r.role === "entree") && r.portions <= 12 ? h : r.portions;
}
