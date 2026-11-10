// Planificateur de la semaine (audit, priorité 🔴 4) : menus de la semaine, courses regroupées avec quantités
// additionnées, restes d'un jour réutilisés le lendemain (moteur zéro déchet) et préparation à l'avance (cuisine en lot).
import { INGREDIENTS, RECIPES, RECIPE_BY_ID } from "./data";
import { flatten, verdict } from "./engine";
import { seasonFit, type Zone } from "./season";
import { norm, scaleQty } from "./text";
import type { Leftover, Profile, Recipe } from "./types";
import { isFish, isRich, kidFriendly, kidsOf, starchOf, totalMin } from "./famille";
import { composeMenus } from "./menu";

export type Slot = "midi" | "soir";
export interface DayPlan { midi?: string; soir?: string; entree?: string; dessert?: string } // entrée et dessert : menu du dimanche midi
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
const TRIVIAL = /^(Ail|Oignon|Échalote|Sel|Poivre|Huile|Sucre|Beurre|Persil|Coriandre|Thym|Laurier|Ciboulette|Menthe|Basilic|Citron|Gingembre|Crème fraîche)/;
const useful = (l: Leftover[]) => l.filter((x) => !TRIVIAL.test(x.ref) && !/^(Épices|Herbes|Huiles)/.test(INGREDIENTS[x.ref]?.section ?? ""));

export interface AutoOptions {
  slots: Slot[]; weekdayMax: number; zone: Zone; profile: Profile; leftovers: Record<string, Leftover[]> | null; seed?: number;
  recent?: Set<string>;   // plats proposés ces 6 dernières semaines (audit gourmet) : ils ne reviennent pas
  sundayMenu?: boolean;   // dimanche midi : entrée et dessert ajoutés au grand plat
  kidsVerdict?: Record<string, "oui" | "non">; // carnet : « les enfants ont aimé » (bonus) ou non (écarté)
  today?: string;         // date du jour (AAAA-MM-JJ) : pas de plat « à lancer la veille » pour ce soir (audit chef + famille)
}

/** Un « grand plat » : long ou de fête. Un seul par jour de week-end (audit gourmet). */
export const isBigDish = (r: Recipe) => r.active + r.rest > 90 || (r.level >= 2 && r.fetes.length > 0);

/** Remplit les cases vides. Plats de saison (moitié la mieux classée), rapides en semaine, protéines et régions variées,
 *  équilibre (féculents, poisson, légumineuses), pas de plat vu ces 4 dernières semaines, tirage pondéré (jamais toujours
 *  le même « meilleur »). Week-end : un seul grand plat par jour, samedi midi rapide ou brunch, dimanche midi en menu complet.
 *  Quand un plat laisse un reste (ex. demi-chou, blancs d'œufs), le repas suivant qui l'utilise est favorisé. */
export function autoPlan(days: string[], plan: WeekPlan, o: AutoOptions): WeekPlan {
  const out: WeekPlan = structuredClone(plan);
  // plats du foyer : profil (porc, alcool, allergies) ET enfants (âge, piment) — audit famille
  const ok = RECIPES.filter((r) => r.role === "plat" && verdict(r, o.profile).availability !== "hidden" && kidFriendly(r, o.profile));
  const fit = new Map(ok.map((r) => [r.id, seasonFit(r, o.zone).score]));
  const pool = [...ok].sort((a, b) => (fit.get(b.id)! - fit.get(a.id)!)).slice(0, Math.max(110, Math.round(ok.length * 0.8)));
  const used = new Set(Object.values(out).flatMap((d) => [d.midi, d.soir]).filter(Boolean) as string[]);
  const recent = o.recent ?? new Set<string>();
  let rnd = (o.seed ?? Date.now()) % 2147483647 || 7;
  const random = () => (rnd = (rnd * 16807) % 2147483647) / 2147483647;
  let prev: Recipe | null = null;
  // équilibre (repères PNNS) : féculents variés, poisson et légumineuses 2 fois, un seul plat très riche
  const placed = Object.values(out).flatMap((d) => [d.midi, d.soir]).filter(Boolean).map((id) => RECIPE_BY_ID[id!]).filter(Boolean) as Recipe[];
  const count = { fish: placed.filter(isFish).length, legumes: placed.filter((r) => starchOf(r) === "légumineuses").length, rich: placed.filter(isRich).length,
    starch: new Map<string, number>(), macro: new Map<string, number>() };
  for (const r of placed) { const st = starchOf(r); if (st) count.starch.set(st, (count.starch.get(st) ?? 0) + 1); count.macro.set(r.macro, (count.macro.get(r.macro) ?? 0) + 1); }
  const totalSlots = days.length * o.slots.length;
  // audit chef + famille : avec des enfants, un soir de semaine se compte en temps total (à table vers 19 h 15) ;
  // le même produit principal ne revient pas dans la semaine (moules deux jours de suite) ; peu de produits d'épicerie du monde
  const kidsHome = kidsOf(o.profile).some((a) => a < 11);
  const mainOf = (r: Recipe) => r.ingredients.filter((l) => l.weight >= 3 && l.ref && /^(Viandes|Poissons|Porc)/.test(INGREDIENTS[l.ref]?.section ?? "")).map((l) => l.ref!);
  const specialOf = (r: Recipe) => r.ingredients.filter((l) => l.ref && !l.optional && l.weight >= 1
      && (/Produits du monde/.test(INGREDIENTS[l.ref]?.section ?? "") || /🟠|🔴/.test(INGREDIENTS[l.ref]?.dispo ?? ""))
    && !/^(Épices|Herbes)/.test(INGREDIENTS[l.ref]?.section ?? "")).map((l) => l.ref!);
  const mains = new Set(placed.flatMap(mainOf));
  const specials = new Set(placed.flatMap(specialOf));
  let filled = 0;
  for (const day of days) {
    const dow = new Date(`${day}T12:00:00`).getDay();
    const weekend = dow === 0 || dow === 6;
    for (const slot of o.slots) {
      const cur = out[day]?.[slot];
      if (cur) { prev = RECIPE_BY_ID[cur] ?? prev; continue; }
      const other = out[day]?.[slot === "midi" ? "soir" : "midi"];
      const bigToday = !!other && !!RECIPE_BY_ID[other] && isBigDish(RECIPE_BY_ID[other]);
      const leftRefs = new Set(prev && o.leftovers ? useful(o.leftovers[prev.id] ?? []).map((l) => l.ref) : []);
      const fits = (r: Recipe) => {
        if (used.has(r.id)) return false;
        if (o.today && day <= o.today && r.veille) return false;          // trempage, marinade d'une nuit : trop tard pour ce soir
        const t = totalMin(r);
        if (!weekend) return t <= o.weekdayMax || (!kidsHome && slot === "soir" && r.active <= 25 && r.rest + (r.avance ?? 0) <= 60);
        if (bigToday) return t <= 45 && !isBigDish(r);  // un seul grand plat par jour
        if (dow === 6 && slot === "midi") return r.cats.includes("brunch") || t <= 30; // samedi midi : brunch ou rapide
        if (dow === 0 && slot === "soir") return t <= 40;  // dimanche soir : léger, on a cuisiné à midi
        return true;
      };
      let cands = pool.filter((r) => fits(r) && !recent.has(r.id) && o.kidsVerdict?.[r.id] !== "non");
      if (cands.length < 6) cands = pool.filter(fits); // garde-fou : jamais de case vide à cause de la mémoire
      if (!cands.length) continue;
      const progress = (filled + 1) / totalSlots; // plus la semaine avance, plus les manques pèsent
      const score = (r: Recipe) => {
        const st = starchOf(r); const n = st ? count.starch.get(st) ?? 0 : 0;
        return fit.get(r.id)!
          + (prev && proteinOf(prev) === proteinOf(r) ? -4 : 0) + (prev && prev.macro === r.macro ? -1.5 : 0)
          + ((count.macro.get(r.macro) ?? 0) >= 2 ? -4 : 0)                    // rotation des cuisines du monde
          + (r.ingredients.some((l) => l.ref && leftRefs.has(l.ref)) ? 2.5 : 0) // le reste d'hier aide, sans écraser l'équilibre
          + (st && prev && starchOf(prev) === st ? -3 : 0) + (st && st !== "légumineuses" && n >= 2 ? -3 * (n - 1) : 0)
          + (isRich(r) ? (count.rich >= 1 ? -8 : -1) : 0)
          + (isFish(r) && count.fish < 2 ? 2 + 3 * progress : 0)
          + (st === "légumineuses" && count.legumes < 2 ? 2 + 3 * progress : 0)
          + (dow === 0 && slot === "midi" && isBigDish(r) ? 3 : 0)           // le dimanche midi, le grand plat de la semaine
          + (o.kidsVerdict?.[r.id] === "oui" ? 2 : 0)                         // plébiscité par les enfants
          + (mainOf(r).some((m) => mains.has(m)) ? -8 : 0)                     // même produit principal déjà dans la semaine
          + -2.5 * Math.max(0, specials.size + specialOf(r).filter((x) => !specials.has(x)).length - 3) * (specialOf(r).some((x) => !specials.has(x)) ? 1 : 0);
      };
      // tirage pondéré parmi les 24 meilleurs : varié d'une semaine à l'autre, sans sacrifier la cohérence
      const top = cands.map((r) => [r, score(r)] as const).sort((a, b) => b[1] - a[1]).slice(0, 24);
      const weights = top.map(([, s]) => Math.exp((s - top[0][1]) / 2.6));
      let pick = random() * weights.reduce((a, b) => a + b, 0);
      let best = top[0][0];
      for (let i = 0; i < top.length; i++) { pick -= weights[i]; if (pick <= 0) { best = top[i][0]; break; } }
      out[day] = { ...out[day], [slot]: best.id };
      used.add(best.id); prev = best; filled++;
      mainOf(best).forEach((m) => mains.add(m)); specialOf(best).forEach((x) => specials.add(x));
      const st = starchOf(best); if (st) count.starch.set(st, (count.starch.get(st) ?? 0) + 1);
      count.macro.set(best.macro, (count.macro.get(best.macro) ?? 0) + 1);
      if (isFish(best)) count.fish++; if (st === "légumineuses") count.legumes++; if (isRich(best)) count.rich++;
    }
    // dimanche midi : un vrai repas de famille, entrée et dessert accordés au plat (composeur de menus)
    const sun = out[day]?.midi;
    if (o.sundayMenu && dow === 0 && sun && !out[day]?.entree && !out[day]?.dessert) {
      const m = composeMenus(sun, o.profile).find((x) => x.name === "Classique");
      if (m) out[day] = { ...out[day], entree: m.courses.find((c) => c.role === "entree")?.recipe.id, dessert: m.courses.find((c) => c.role === "dessert")?.recipe.id };
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
// audit chef + famille : ce qu'on compte au supermarché (gousses, bouquets, pavés…) s'additionne aussi
const NOUNS: [RegExp, string][] = [[/^gousses?\b/, "gousse"], [/^t[eê]tes?\b/, "tête"], [/^bouquets?\b/, "bouquet"], [/^bottes?\b/, "botte"], [/^branches?\b/, "branche"],
  [/^tiges?\b/, "tige"], [/^brins?\b/, "brin"], [/^(bo[iî]tes?|bocal|bocaux)\b/, "boîte"], [/^tranches?\b/, "tranche"], [/^pav[ée]s?\b/, "pavé"], [/^filets?\b/, "filet"],
  [/^sachets?\b/, "sachet"], [/^morceaux?\b/, "morceau"], [/^feuilles?\b/, "feuille"], [/^poign[ée]es?\b/, "poignée"], [/^pinc[ée]es?\b/, "pincée"]];
const nounOf = (s: string) => { const t = s.trim().replace(/^(de |d'|d’)/, ""); for (const [rx, u] of NOUNS) if (rx.test(t)) return u; return null; };
// poids moyen d'une pièce (g) : « 8 oignons + 800 g » devient un seul poids
const PIECE_G: [RegExp, number][] = [[/^Oignon/, 150], [/^Pomme de terre/, 180], [/^Carotte/, 120], [/^Tomate$/, 120], [/^Courgette/, 250], [/^Poivron/, 180],
  [/^Aubergine/, 300], [/^Échalote/, 30], [/^Pomme$/, 180], [/^Poireau/, 200], [/^Navet/, 150], [/^Patate douce/, 300], [/^Concombre/, 350]];
function parseQty(q: string): { n: number; unit: string } | null {
  const m = q.trim().replace(",", ".").replace(/^(\d+ )?1\/2\b/, "$1½").replace(/^(\d+ )?1\/4\b/, "$1¼")
      .replace(/^(\d+ )?3\/4\b/, "$1¾").replace(/^(\d+ )?1\/3\b/, "$1⅓").match(/^(\d+(?:\.\d+)?)?\s*([½¼¾⅓⅔])?\s*(.*)$/);
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
  if (unit === "gousse") { const k = Math.ceil(n - 0.15); return k >= 8 ? `${k} gousses (≈ ${Math.ceil(k / 10)} tête${k > 10 ? "s" : ""})` : `${k} gousse${k > 1 ? "s" : ""}`; }
  if (unit === "pincée") return "quelques pincées";
  if (["bouquet", "botte", "tête", "boîte", "pavé", "filet", "sachet", "tranche", "branche", "tige", "brin", "feuille", "morceau", "poignée"].includes(unit)) {
    const k = Math.max(1, Math.ceil(n - 0.15)); return `${k} ${unit}${k > 1 ? (unit === "morceau" ? "x" : "s") : ""}`; }
  if (unit.startsWith("c. à")) { const h = Math.max(0.5, Math.round(n * 2) / 2); return `${h === 0.5 ? "½" : String(h).replace(".5", " ½")} ${unit}`; }
  return `${n.toLocaleString("fr-FR", { maximumFractionDigits: 1 })}${unit ? " " + unit : ""}`;
};
// produits qu'on a en général au placard : on rappelle d'en avoir, sans quantité d'achat
const PANTRY = /^(Épices|Huiles|Condiments)/;
const PANTRY_KEEP = /palme|arachide|coco|tahini|miso|gochujang|pâte de curry|harissa/i;

export interface ShopLine { ref: string; label: string; section: string; from: string[] }
/** Liste de courses d'un ensemble de recettes (avec facteur de portions) : un article par produit, quantités additionnées quand c'est possible. */
export function consolidate(items: { id: string; factor: number }[], month = new Date().getMonth() + 1): ShopLine[] {
  const by = new Map<string, { sums: Map<string, number>; other: string[]; from: Set<string> }>();
  // accompagnement relié (audit gourmet) : sa fiche s'ajoute aux courses avec le même nombre de parts
  const withSides = items.flatMap((it) => {
    const side = RECIPE_BY_ID[it.id]?.side;
    if (!side || side.startsWith("achat:")) return [it];
    const sr = RECIPE_BY_ID[side]; const r = RECIPE_BY_ID[it.id];
    return sr && r ? [it, { id: side, factor: (it.factor * r.portions) / sr.portions }] : [it];
  });
  const buys = items.map((it) => RECIPE_BY_ID[it.id]?.side).filter((x): x is string => !!x && x.startsWith("achat:")).map((x) => x.slice(6));
  for (const { id, factor } of withSides) {
    const r = RECIPE_BY_ID[id]; if (!r) continue;
    for (const l of flatten(r.ingredients)) {
      if (!l.ref || l.optional) continue;
      const e = by.get(l.ref) ?? { sums: new Map<string, number>(), other: [] as string[], from: new Set<string>() };
      const sq = scaleQty(l.qty, factor);
      let q = parseQty(sq);
      if (!q) { const m = sq.replace(",", ".").replace(/^1\/2\b/, "½").replace(/^1\/4\b/, "¼").replace(/^3\/4\b/, "¾").match(/^(\d+(?:\.\d+)?)?\s*([½¼¾⅓⅔])?\s*(.+)$/);
            const u = m && (m[1] || m[2]) ? nounOf(m[3]) : null;
        if (m && u) q = { n: (m[1] ? parseFloat(m[1]) : 0) + (m[2] ? FRAC[m[2]] : 0), unit: u }; }
      else if (q.unit === "") { const u = nounOf(l.label); if (u) q = { n: q.n, unit: u }; }
      if (q) e.sums.set(q.unit, (e.sums.get(q.unit) ?? 0) + q.n);
      else e.other.push(`${scaleQty(l.qty, factor)} ${l.label}`.trim());
      e.from.add(r.title.split(" (")[0]);
      by.set(l.ref, e);
    }
  }
  for (const ref of buys) { const e = by.get(ref) ?? { sums: new Map<string, number>(), other: [] as string[], from: new Set<string>() }; e.other.push("pour accompagner"); e.from.add("accompagnement"); by.set(ref, e); }
  return [...by].map(([ref, e]) => {
    const name = ref.split(" (")[0];
    const section = INGREDIENTS[ref]?.section ?? "Autres";
    // pièces + grammes d'un légume courant : un seul poids, et le nombre de pièces en repère
    if (e.sums.has("tête") && e.sums.has("gousse")) { e.sums.set("gousse", e.sums.get("gousse")! + 10 * e.sums.get("tête")!); e.sums.delete("tête"); }
    if (e.sums.has("botte") && e.sums.has("bouquet")) { e.sums.set("bouquet", e.sums.get("bouquet")! + e.sums.get("botte")!); e.sums.delete("botte"); }
    e.other = [...new Set(e.other)];
    const pg = PIECE_G.find(([rx]) => rx.test(ref))?.[1];
    if (pg && e.sums.has("g") && e.sums.has("")) { e.sums.set("g", e.sums.get("g")! + e.sums.get("")! * pg); e.sums.delete(""); }
    const sums = [...e.sums].filter(([u]) => !(u.startsWith("c. à") && e.sums.size > 1 && [...e.sums.keys()].some((x) => !x.startsWith("c. à")))).map(([u, n]) => fmt(n, u));
    if (PANTRY.test(section) && !PANTRY_KEEP.test(ref) && ![...e.sums.keys()].some((u) => u === "cl" || u === "g")) return { ref, section, from: [...e.from], label: `${name} (vérifie ton placard)` };
    // audit chef + famille : en hiver, la tomate fraîche n'a pas de goût ; en boîte, elle fait mieux dans un plat cuit
    const winterTomato = /^Tomate/.test(ref) && (INGREDIENTS[ref]?.season?.length ?? 0) > 0 && !INGREDIENTS[ref]!.season!.includes(month)
        ? " (hors saison : pour les plats cuits, des tomates pelées en boîte sont meilleures)" : "";
    return { ref, section, from: [...e.from],
        label: `${name}${sums.length ? " : " + sums.join(" + ") : ""}${e.other.length ? (sums.length ? " + " : " : ") + e.other.join(" + ") : ""}${winterTomato}` };
  }).sort((a, b) => a.section.localeCompare(b.section) || a.label.localeCompare(b.label));
}

// ---------------------------------------------------------------- préparation à l'avance (cuisine en lot)
const AHEAD = /marin|pate (a pain|a pizza|brisee|sucree)|petri|bouillon|fumet|sauce|pesto|vinaigrette|chermoula|nokoss|creme patissiere|repos une nuit|la veille|une nuit|tremper|trempe/;
const LAST_MINUTE = /\bfrire\b|friture|frits?\b|servir|dresser|au dernier moment|aussitot|tout de suite/;
const NOT_AHEAD = /Ail|Oignon|Échalote|Pomme de terre|Tomate|Avocat|Salade|Champignon|Aubergine|Concombre|Roquette|Endive|Épinard|Cresson|Patate douce|Céleri-rave|Artichaut/;
/** Une étape qui se fait vraiment à l'avance : nommée (« Sauce. », « Mariner. »…) par un geste d'avance, jamais une cuisson
 *  minute ni une marinade de moins d'une heure (un poisson au citron vert ne se marine pas la veille). */
function aheadStep(step: string, headOnly = false): boolean {
  const t = norm(step); const head = norm(step.replace(/\*\*/g, "").split(/[.:]/)[0]);
  if (!(AHEAD.test(head) || (!headOnly && AHEAD.test(t))) || LAST_MINUTE.test(t) || /rosiss|saisi|a la minute/.test(t)) return false;
  if (/marin/.test(head)) { const m = t.match(/(\d+) ?(h|min)\b/); if (!m || (m[2] === "min" && +m[1] < 60)) return false; }
  return true;
}
export interface PrepTask { recipe: string; task: string }
/** Ce qui peut se préparer le dimanche (ou la veille) pour les repas de la semaine, et les légumes à laver et couper d'un coup. */
export function prepAhead(ids: string[]): { tasks: PrepTask[]; veg: string[] } {
  const tasks: PrepTask[] = [];
  const veg = new Map<string, number>();
  for (const id of ids) {
    const r = RECIPE_BY_ID[id]; if (!r) continue;
    // audit chef + famille : ce qui DOIT se faire la veille passe d'abord ; on ne frit ni ne dresse à l'avance
    if (r.veille) tasks.push({ recipe: r.title.split(" (")[0], task: `À lancer la veille : ${r.veille}.` });
    else {
      // d'abord une étape dont le titre est un geste d'avance (« Sauce. », « Bouillon. »), sinon une étape qui en contient un
      const s = r.steps.find((x) => aheadStep(x, true)) ?? r.steps.find((x) => aheadStep(x));
      if (s) tasks.push({ recipe: r.title.split(" (")[0], task: s.replace(/\*\*/g, "") });
    }
    // seuls les légumes fermes se coupent à l'avance : pas la pomme de terre (elle noircit), ni la tomate (elle rend son eau)
    for (const l of flatten(r.ingredients)) if (l.ref && /Légumes/.test(INGREDIENTS[l.ref]?.section ?? "") && !NOT_AHEAD.test(l.ref))
        veg.set(l.ref.split(" / ")[0].split(" (")[0], (veg.get(l.ref) ?? 0) + 1);
  }
  return { tasks, veg: [...veg.keys()] };
}
