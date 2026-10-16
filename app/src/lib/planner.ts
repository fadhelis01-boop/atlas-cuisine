// Planificateur de la semaine (audit, priorité 🔴 4) : menus de la semaine, courses regroupées avec quantités
// additionnées, restes d'un jour réutilisés le lendemain (moteur zéro déchet) et préparation à l'avance (cuisine en lot).
import { INGREDIENTS, RECIPES, RECIPE_BY_ID } from "./data";
import { flatten, verdict } from "./engine";
import { seasonFit, type Zone } from "./season";
import { norm, scaleQty } from "./text";
import type { Leftover, Profile, Recipe } from "./types";
import { isFish, isRich, kidFriendly, starchOf } from "./famille";

export type Slot = "midi" | "soir";
export interface DayPlan { midi?: string; soir?: string }
export type WeekPlan = Record<string, DayPlan>; // clé : date ISO « 2026-10-19 »

const iso = (d: Date) => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
/** Les 7 jours à venir à partir d'aujourd'hui (offset 0), puis les 7 suivants (offset 1) : jamais de jours déjà passés (audit famille). */
export function weekDays(offset = 0, today = new Date()): string[] {
  const d = new Date(today); d.setDate(d.getDate() + offset * 7);
  return Array.from({ length: 7 }, (_, i) => { const x = new Date(d); x.setDate(d.getDate() + i); return iso(x); });
}
export const DAY_NAMES = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"];
/** Nom du jour d'une date ISO (la semaine glissante ne commence plus forcément un lundi). */
export const dayName = (iso: string) => DAY_NAMES[(new Date(`${iso}T12:00:00`).getDay() + 6) % 7];
/** Coût indicatif par part selon l'indicateur de la fiche (€, €€, €€€) : un ordre de grandeur pour un budget, pas un prix. */
export const COST_PER_PART: Record<string, number> = { "€": 2, "€€": 4, "€€€": 7 };

/** Protéine principale, pour varier d'un repas à l'autre. */
export function proteinOf(r: Recipe): string {
  const refs = r.ingredients.filter((l) => l.ref && l.weight >= 2).map((l) => norm(l.ref!)).join(" ");
  if (/saumon|cabillaud|morue|thon|sardine|maquereau|dorade|bar |sole|lieu|colin|lotte|poisson|crevette|gambas|moule|calamar|saint jacques/.test(refs)) return "poisson";
  if (/poulet|volaille|dinde|canard|pintade|caille/.test(refs)) return "volaille";
  if (/boeuf|veau|paleron|joue|steak|rumsteck|bavette|hache|jarret|cote de/.test(refs)) return "boeuf";
  if (/agneau|gigot|mouton|chevre \//.test(refs)) return "agneau";
  if (/porc|lardons|jambon|saucisse de toulouse|chorizo \(/.test(refs)) return "porc";
  if (/oeuf/.test(refs)) return "oeufs";
  return "vegetal";
}

// un reste qui vaut la peine d'être signalé : pas un demi-oignon ni une pincée d'épice
const TRIVIAL = /^(Ail|Oignon|Échalote|Sel|Poivre|Huile|Sucre|Beurre|Persil|Coriandre|Thym|Laurier|Ciboulette|Menthe|Basilic)/;
const useful = (l: Leftover[]) => l.filter((x) => !TRIVIAL.test(x.ref) && !/^(Épices|Herbes|Huiles)/.test(INGREDIENTS[x.ref]?.section ?? ""));

export interface AutoOptions { slots: Slot[]; weekdayMax: number; zone: Zone; profile: Profile; leftovers: Record<string, Leftover[]> | null; seed?: number }

/** Remplit les cases vides : plats de saison (tiers le mieux classé), rapides en semaine, protéines variées,
 *  et quand un plat laisse un reste (ex. demi-chou, blancs d'œufs), le repas suivant qui l'utilise est favorisé. */
export function autoPlan(days: string[], plan: WeekPlan, o: AutoOptions): WeekPlan {
  const out: WeekPlan = structuredClone(plan);
  // plats du foyer : profil (porc, alcool, allergies) ET enfants (âge, piment) — audit famille
  const ok = RECIPES.filter((r) => r.role === "plat" && verdict(r, o.profile).availability !== "hidden" && kidFriendly(r, o.profile));
  const fit = new Map(ok.map((r) => [r.id, seasonFit(r, o.zone).score]));
  const pool = [...ok].sort((a, b) => (fit.get(b.id)! - fit.get(a.id)!)).slice(0, Math.max(60, Math.round(ok.length * 0.45)));
  const used = new Set(Object.values(out).flatMap((d) => [d.midi, d.soir]).filter(Boolean) as string[]);
  let rnd = (o.seed ?? Date.now()) % 2147483647 || 7;
  const random = () => (rnd = (rnd * 16807) % 2147483647) / 2147483647;
  let prev: Recipe | null = null;
  // équilibre (repères PNNS) : féculents variés, poisson et légumineuses 2 fois, un seul plat très riche
  const placed = Object.values(out).flatMap((d) => [d.midi, d.soir]).filter(Boolean).map((id) => RECIPE_BY_ID[id!]).filter(Boolean) as Recipe[];
  const count = { fish: placed.filter(isFish).length, legumes: placed.filter((r) => starchOf(r) === "légumineuses").length, rich: placed.filter(isRich).length, starch: new Map<string, number>() };
  for (const r of placed) { const st = starchOf(r); if (st) count.starch.set(st, (count.starch.get(st) ?? 0) + 1); }
  const totalSlots = days.length * o.slots.length;
  let filled = 0;
  for (const [, day] of days.entries()) {
    const dow = new Date(`${day}T12:00:00`).getDay();
    const weekend = dow === 0 || dow === 6;
    for (const slot of o.slots) {
      const cur = out[day]?.[slot];
      if (cur) { prev = RECIPE_BY_ID[cur] ?? prev; continue; }
      const leftRefs = new Set(prev && o.leftovers ? useful(o.leftovers[prev.id] ?? []).map((l) => l.ref) : []);
      const cands = pool.filter((r) => !used.has(r.id) && (weekend || r.active + r.rest <= o.weekdayMax || (slot === "soir" && r.active <= 25 && r.rest <= 60)));
      if (!cands.length) continue;
      const progress = (filled + 1) / totalSlots; // plus la semaine avance, plus les manques pèsent
      const score = (r: Recipe) => {
        const st = starchOf(r); const n = st ? count.starch.get(st) ?? 0 : 0;
        return fit.get(r.id)! + random() * 3
          + (prev && proteinOf(prev) === proteinOf(r) ? -4 : 0) + (prev && prev.macro === r.macro ? -1.5 : 0)
          + (r.ingredients.some((l) => l.ref && leftRefs.has(l.ref)) ? 2.5 : 0) // le reste d'hier aide, sans écraser l'équilibre
          + (st && prev && starchOf(prev) === st ? -3 : 0) + (st && st !== "légumineuses" && n >= 2 ? -3 * (n - 1) : 0)
          + (isRich(r) ? (count.rich >= 1 ? -8 : -1) : 0)
          + (isFish(r) && count.fish < 2 ? 2 + 3 * progress : 0)
          + (st === "légumineuses" && count.legumes < 2 ? 2 + 3 * progress : 0);
      };
      const best = cands.reduce((a, b) => (score(b) > score(a) ? b : a));
      out[day] = { ...out[day], [slot]: best.id };
      used.add(best.id); prev = best; filled++;
      const st = starchOf(best); if (st) count.starch.set(st, (count.starch.get(st) ?? 0) + 1);
      if (isFish(best)) count.fish++; if (st === "légumineuses") count.legumes++; if (isRich(best)) count.rich++;
    }
  }
  return out;
}

/** Le plat du jour précédent laisse-t-il un reste que ce plat utilise ? (texte pour l'affichage) */
export function leftoverLink(prevId: string | undefined, id: string | undefined, leftovers: Record<string, Leftover[]> | null): string | null {
  if (!prevId || !id || !leftovers) return null;
  const r = RECIPE_BY_ID[id]; const lo = useful(leftovers[prevId] ?? []);
  const hit = lo.find((l) => r?.ingredients.some((x) => x.ref === l.ref));
  return hit ? hit.ref.split(" / ")[0].split(" (")[0].toLowerCase() : null;
}

// ---------------------------------------------------------------- courses regroupées
const FRAC: Record<string, number> = { "½": 0.5, "¼": 0.25, "¾": 0.75, "⅓": 1 / 3, "⅔": 2 / 3 };
const UNIT: [RegExp, string, number][] = [[/^kg\b/, "g", 1000], [/^g\b/, "g", 1], [/^l\b/i, "cl", 100], [/^dl\b/, "cl", 10], [/^cl\b/, "cl", 1], [/^ml\b/, "cl", 0.1],
  [/^c\. à s\./, "c. à s.", 1], [/^c\. à c\./, "c. à c.", 1]];
function parseQty(q: string): { n: number; unit: string } | null {
  const m = q.trim().replace(",", ".").match(/^(\d+(?:\.\d+)?)?\s*([½¼¾⅓⅔])?\s*(.*)$/);
  if (!m || (!m[1] && !m[2])) return null;
  const n = (m[1] ? parseFloat(m[1]) : 0) + (m[2] ? FRAC[m[2]] : 0);
  const rest = m[3].trim();
  if (!rest) return { n, unit: "" };
  for (const [rx, u, f] of UNIT) if (rx.test(rest)) return { n: n * f, unit: u };
  return null;
}
const fmt = (n: number, unit: string) => {
  if (unit === "g" && n >= 1000) return `${(n / 1000).toLocaleString("fr-FR", { maximumFractionDigits: 2 })} kg`;
  if (unit === "cl" && n >= 100) return `${(n / 100).toLocaleString("fr-FR", { maximumFractionDigits: 2 })} L`;
  if (unit === "g") return `${n >= 100 ? Math.ceil(n / 50) * 50 : Math.ceil(n / 10) * 10} g`; // on achète au poids rond
  if (unit === "") return String(Math.ceil(n - 0.15)); // à la pièce : 4,8 oignons → 5 ; 1,1 → 1
  if (unit.startsWith("c. à")) { const h = Math.max(0.5, Math.round(n * 2) / 2); return `${h === 0.5 ? "½" : String(h).replace(".5", " ½")} ${unit}`; }
  return `${n.toLocaleString("fr-FR", { maximumFractionDigits: 1 })}${unit ? " " + unit : ""}`;
};
// produits qu'on a en général au placard : on rappelle d'en avoir, sans quantité d'achat
const PANTRY = /^(Épices|Huiles|Condiments)/;
const PANTRY_KEEP = /palme|arachide|coco|tahini|miso|gochujang|pâte de curry|harissa/i;

export interface ShopLine { ref: string; label: string; section: string; from: string[] }
/** Liste de courses d'un ensemble de recettes (avec facteur de portions) : un article par produit, quantités additionnées quand c'est possible. */
export function consolidate(items: { id: string; factor: number }[]): ShopLine[] {
  const by = new Map<string, { sums: Map<string, number>; other: string[]; from: Set<string> }>();
  for (const { id, factor } of items) {
    const r = RECIPE_BY_ID[id]; if (!r) continue;
    for (const l of flatten(r.ingredients)) {
      if (!l.ref || l.optional) continue;
      const e = by.get(l.ref) ?? { sums: new Map<string, number>(), other: [] as string[], from: new Set<string>() };
      const q = parseQty(scaleQty(l.qty, factor));
      if (q) e.sums.set(q.unit, (e.sums.get(q.unit) ?? 0) + q.n);
      else e.other.push(`${scaleQty(l.qty, factor)} ${l.label}`.trim());
      e.from.add(r.title.split(" (")[0]);
      by.set(l.ref, e);
    }
  }
  return [...by].map(([ref, e]) => {
    const name = ref.split(" (")[0];
    const section = INGREDIENTS[ref]?.section ?? "Autres";
    const sums = [...e.sums].filter(([u]) => !(u.startsWith("c. à") && e.sums.size > 1 && [...e.sums.keys()].some((x) => !x.startsWith("c. à")))).map(([u, n]) => fmt(n, u));
    if (PANTRY.test(section) && !PANTRY_KEEP.test(ref) && ![...e.sums.keys()].some((u) => u === "cl" || u === "g")) return { ref, section, from: [...e.from], label: `${name} (vérifie ton placard)` };
    return { ref, section, from: [...e.from], label: `${name}${sums.length ? " : " + sums.join(" + ") : ""}${e.other.length ? (sums.length ? " + " : " : ") + e.other.join(" + ") : ""}` };
  }).sort((a, b) => a.section.localeCompare(b.section) || a.label.localeCompare(b.label));
}

// ---------------------------------------------------------------- préparation à l'avance (cuisine en lot)
const AHEAD = /marin|pate (a pain|a pizza|brisee|sucree)|petri|bouillon|fumet|sauce|pesto|vinaigrette|chermoula|nokoss|creme patissiere|repos une nuit|la veille|une nuit|tremper|trempe/;
export interface PrepTask { recipe: string; task: string }
/** Ce qui peut se préparer le dimanche (ou la veille) pour les repas de la semaine, et les légumes à laver et couper d'un coup. */
export function prepAhead(ids: string[]): { tasks: PrepTask[]; veg: string[] } {
  const tasks: PrepTask[] = [];
  const veg = new Map<string, number>();
  for (const id of ids) {
    const r = RECIPE_BY_ID[id]; if (!r) continue;
    for (const s of r.steps) if (AHEAD.test(norm(s))) { tasks.push({ recipe: r.title.split(" (")[0], task: s.replace(/\*\*/g, "") }); break; }
    for (const l of flatten(r.ingredients)) if (l.ref && /Légumes/.test(INGREDIENTS[l.ref]?.section ?? "") && !/Ail|Oignon|Échalote/.test(l.ref)) veg.set(l.ref.split(" / ")[0].split(" (")[0], (veg.get(l.ref) ?? 0) + 1);
  }
  return { tasks, veg: [...veg.keys()] };
}
