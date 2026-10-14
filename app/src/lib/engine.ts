// Moteur diététique, de substitution et de suggestion.
// Portage TypeScript de bible/atlas_engine.py (implémentation de référence des Tomes 1-3-8).
// Invariants (Tome 2 §4, Tome 8) :
//  1. un ingrédient inconnu n'est JAMAIS « ok » ;
//  2. une version adaptée est toujours RE-VÉRIFIÉE après substitution ;
//  3. les ingrédients facultatifs comptent pour le régime ;
//  4. les sous-recettes transmettent leurs dérivés et allergènes.
import { INGREDIENTS, RECIPE_BY_ID, RULES } from "./data";
import type { DerivLevel, IngredientRef, Profile, Recipe, RecipeLine, Rule } from "./types";
import { scaleQty } from "./text";

export type Status = "ok" | "trace" | "uncertain" | "violates";
const ORDER: Record<Status, number> = { ok: 0, trace: 1, uncertain: 2, violates: 3 };

export interface Evaluation {
  pork: Status;
  alcohol: Status;
  allergens: Set<string>;
  maybeAllergens: Set<string>;
  unknown: string[];
  offenders: { pork: string[]; alcohol: string[] };
  confidence: "A" | "B" | "C";
  flesh: string[]; // viande, poisson, gélatine, bouillons de viande… (végétarien)
  rennet: string[]; // fromages à présure animale (avertissement végétarien)
}

type Line = Pick<RecipeLine, "ref" | "weight" | "optional">;
type Lookup = (name: string) => IngredientRef | undefined;

const FLESH_SECTIONS = ["Viandes & volailles", "Porc, charcuterie", "Poissons, crustacés"];
const FLESH_EXTRA = new Set([
  "Gélatine alimentaire", "Graisse de canard", "Graisse de canard / beurre clarifié", "Graisse de bœuf / suif", "Bouillon cube volaille",
  "Bouillon cube bœuf", "Bouillon liquide (type fond)", "Fond de veau / de volaille (poudre)", "Bouillon d'os maison (bœuf/volaille)",
  "Fumet de poisson maison", "Sauce de poisson (nuoc-mâm, nam pla)", "Sauce d'huître", "Sauce Worcestershire", "Pâte de crevettes",
  "Dashi (instantané)", "Dashi maison (kombu + katsuobushi)", "Bonite séchée (katsuobushi)", "Poisson fumé / séché", "Crevettes séchées",
  "Morue salée", "Sauce XO", "Merguez", "Chorizo mexicain",
]);
const VEGGIE_IN_MEAT_SECTION = new Set(["Champignons fumés / tempeh fumé", "Paprika fumé + huile", "Gélatine de bœuf / poisson, agar-agar, pectine"]);
const RENNET = new Set(["Parmesan / Parmigiano", "Pecorino"]);

export function isFlesh(name: string, ing: IngredientRef): boolean {
  if (VEGGIE_IN_MEAT_SECTION.has(name)) return false;
  return FLESH_EXTRA.has(name) || FLESH_SECTIONS.some((s) => ing.section.startsWith(s));
}

/** Aplatit les lignes (sous-recettes incluses). Détecte les cycles. */
export function* walk(lines: Line[], stack: string[] = []): Generator<Line> {
  for (const ln of lines) {
    if (ln.ref?.startsWith("SUB:")) {
      const id = ln.ref.slice(4);
      if (stack.includes(id)) throw new Error(`cycle de sous-recettes : ${[...stack, id].join(" -> ")}`);
      const sub = RECIPE_BY_ID[id];
      if (!sub) throw new Error(`sous-recette inconnue : ${id}`);
      yield* walk(sub.ingredients, [...stack, id]);
    } else yield ln;
  }
}

export function evaluateLines(lines: Line[], opts: { imported?: boolean; lookup?: Lookup } = {}): Evaluation {
  const lookup: Lookup = opts.lookup ?? ((n) => INGREDIENTS[n]);
  const res: Evaluation = {
    pork: "ok", alcohol: "ok", allergens: new Set(), maybeAllergens: new Set(), unknown: [],
    offenders: { pork: [], alcohol: [] }, confidence: "A", flesh: [], rennet: [],
  };
  const bump = (kind: "pork" | "alcohol", st: Status, id: string) => {
    if (ORDER[st] > ORDER[res[kind]]) res[kind] = st;
    if (st !== "ok" && !res.offenders[kind].includes(id)) res.offenders[kind].push(id);
  };
  for (const ln of walk(lines)) {
    if (ln.ref === null) continue; // eau, café… : implicite (rapport d'écarts du Tome 11)
    const ing = lookup(ln.ref);
    if (!ing) {
      res.unknown.push(ln.ref);
      bump("pork", "uncertain", ln.ref);
      bump("alcohol", "uncertain", ln.ref);
      res.confidence = "C";
      continue;
    }
    for (const kind of ["pork", "alcohol"] as const) {
      const lvl: DerivLevel | undefined = ing.derivs[kind];
      if (lvl === "certain") bump(kind, "violates", ln.ref);
      else if (lvl === "possible") bump(kind, "uncertain", ln.ref);
      else if (lvl === "trace") bump(kind, "trace", ln.ref);
    }
    ing.allergens.forEach((a) => res.allergens.add(a)); // les facultatifs comptent aussi
    ing.maybe.forEach((a) => res.maybeAllergens.add(a));
    if (isFlesh(ln.ref, ing) && !res.flesh.includes(ln.ref)) res.flesh.push(ln.ref);
    if (RENNET.has(ln.ref) && !res.rennet.includes(ln.ref)) res.rennet.push(ln.ref);
    // Tout le référentiel est en confiance « C » (brouillon, Tome 3 §1.5) : les badges le disent.
    res.confidence = "C";
  }
  if (opts.imported) res.confidence = "C";
  return res;
}

export const evaluate = (r: Recipe) => evaluateLines(r.ingredients);

/** Contraintes actives d'un profil. */
export function constraintsOf(p: Profile): ("pork" | "alcohol")[] {
  const c: ("pork" | "alcohol")[] = [];
  if (p.noPork) c.push("pork");
  if (p.alcohol !== "allowed") c.push("alcohol");
  return c;
}

export type Availability = "ok" | "ok_warning" | "adaptable" | "hidden";

export interface Verdict {
  availability: Availability;
  reasons: string[]; // pourquoi la recette d'origine ne convient pas
  warnings: string[]; // doutes à vérifier (étiquettes)
  adapted: Adapted | null; // version adaptée re-vérifiée
}

export interface Adapted {
  lines: RecipeLine[];
  source: "curated" | "generic";
  variantName: string;
  notes: string[]; // ce qui a été remplacé, en clair
  tested: boolean; // false = « substitution à tester » (Tome 7 §3.2)
  newAllergens: string[];
}

/** Évalue une évaluation contre le profil : liste des violations et des doutes. */
function check(ev: Evaluation, p: Profile) {
  const reasons: string[] = [];
  const warnings: string[] = [];
  if (p.noPork) {
    if (ev.pork === "violates") reasons.push("contient du porc");
    else if (ev.pork === "uncertain") (p.strict ? reasons : warnings).push("porc possible (à vérifier sur l'étiquette)");
  }
  if (p.alcohol !== "allowed") {
    const strictAlc = p.alcohol === "strict" || p.strict;
    if (ev.alcohol === "violates") reasons.push("contient de l'alcool");
    else if (ev.alcohol === "uncertain") (strictAlc ? reasons : warnings).push("alcool possible");
    else if (ev.alcohol === "trace" && p.alcohol === "strict") reasons.push("traces d'alcool (fermentation, vinaigre de vin…)");
  }
  for (const a of p.allergens) if (ev.allergens.has(a)) reasons.push(`allergène : ${a}`);
  for (const a of p.allergens) if (!ev.allergens.has(a) && ev.maybeAllergens.has(a)) warnings.push(`allergène possible selon la marque : ${a}`);
  if (p.vegetarian && ev.flesh.length) reasons.push("contient de la viande ou du poisson");
  if (p.vegetarian && ev.rennet.length) warnings.push("fromage à présure animale");
  if (ev.unknown.length) warnings.push("ingrédient non référencé");
  return { reasons, warnings };
}

/** Ligne de remplacement : quantité recalculée avec le ratio de la règle, libellé lisible, trace de l'original. */
function substituted(ln: RecipeLine, ref: string, ratio: number): RecipeLine {
  const n = parseFloat((ln.qty.match(/\d+(?:,\d+)?/)?.[0] ?? "").replace(",", "."));
  const tiny = ratio <= 0.01 || (!Number.isNaN(n) && n * ratio < 0.25);
  const qty = tiny ? "1 pincée" : Number.isNaN(n) ? ln.qty : scaleQty(ln.qty, ratio);
  const name = ref.split(" (")[0];
  const low = name.charAt(0).toLowerCase() + name.slice(1);
  // « 150 g de lardons », « 45 ml d'huile », « 1 pincée de paprika »
  const de = /[a-zà-ÿ.]$/i.test(qty) ? (/^[aeiouyéèêàâîôûœh]/i.test(low) ? "d'" : "de ") : "";
  return { ...ln, ref, qty, label: de + low, replaces: `${ln.qty} ${ln.label}`.trim() };
}

function rewrite(lines: RecipeLine[], replace: Record<string, [string, number][]>): RecipeLine[] {
  return lines.flatMap((ln) => (ln.ref && replace[ln.ref] ? replace[ln.ref].map(([ref, ratio]) => substituted(ln, ref, ratio)) : [ln]));
}

/** Aplatit les sous-recettes d'un niveau pour que les règles génériques puissent les atteindre. */
function flatten(lines: RecipeLine[]): RecipeLine[] {
  return lines.flatMap((ln) => (ln.ref?.startsWith("SUB:") ? flatten(RECIPE_BY_ID[ln.ref.slice(4)].ingredients) : [ln]));
}

/** Verdict complet pour un profil, avec version adaptée vérifiée si possible (Tome 1 §7.1 et §7.5). */
export function verdict(r: Recipe, p: Profile, rules: Rule[] = RULES): Verdict {
  const ev = evaluate(r);
  const { reasons, warnings } = check(ev, p);
  if (!reasons.length) return { availability: warnings.length ? "ok_warning" : "ok", reasons, warnings, adapted: null };

  const tryLines = (lines: RecipeLine[]) => {
    const ev2 = evaluateLines(lines);
    const c = check(ev2, p);
    return c.reasons.length ? null : { ev2, warnings: c.warnings };
  };
  // 1) variantes de la fiche (curation chef), seules puis combinées
  const vs = r.variants;
  // une variante « combinée » (ex. sans porc ET sans alcool) reprend les explications des variantes qu'elle combine
  const notesOf = (v: (typeof vs)[number]) => {
    const parts = v.constraints.length > 1 ? vs.filter((x) => x !== v && x.constraints.length && x.constraints.every((c) => v.constraints.includes(c))).map((x) => x.note) : [];
    return parts.length ? parts : [v.note];
  };
  const combos: { name: string; replace: Record<string, [string, number][]>; notes: string[]; tested: boolean }[] = vs.map((v) => ({
    name: v.name, replace: v.replace, notes: notesOf(v), tested: v.tested,
  }));
  if (vs.length > 1) combos.push({ name: vs.map((v) => v.name).join(" + "), replace: Object.assign({}, ...vs.map((v) => v.replace)), notes: vs.map((v) => v.note), tested: vs.every((v) => v.tested) });
  for (const c of combos) {
    const lines = rewrite(r.ingredients, c.replace);
    const ok = tryLines(lines);
    if (ok) {
      return {
        availability: "adaptable", reasons, warnings: ok.warnings,
        adapted: { lines, source: "curated", variantName: c.name, notes: c.notes, tested: c.tested, newAllergens: [...ok.ev2.allergens].filter((a) => !ev.allergens.has(a)) },
      };
    }
  }
  // 2) règles génériques par fonction (Tome 1 §7.5) sur les seuls ingrédients fautifs
  const flat = flatten(r.ingredients);
  const evFlat = evaluateLines(flat);
  const kinds = constraintsOf(p);
  const offenders = new Set(kinds.flatMap((k) => evFlat.offenders[k]));
  const replace: Record<string, [string, number][]> = {};
  const notes: string[] = [];
  for (const rule of rules) {
    if (rule.status === "retired" || !offenders.has(rule.replaces) || replace[rule.replaces]) continue;
    if (!rule.satisfies.some((s) => kinds.includes(s))) continue;
    replace[rule.replaces] = rule.items;
    notes.push(`${rule.replaces} → ${rule.note}`);
  }
  // un ingrédient facultatif fautif sans règle peut simplement être retiré
  for (const id of offenders) {
    if (replace[id]) continue;
    const line = flat.find((l) => l.ref === id);
    if (line?.optional) { replace[id] = []; notes.push(`${id} (facultatif) → à supprimer`); }
  }
  if (Object.keys(replace).length) {
    const lines = rewrite(flat, replace);
    const ok = tryLines(lines);
    if (ok) {
      return {
        availability: "adaptable", reasons, warnings: ok.warnings,
        adapted: { lines, source: "generic", variantName: "Version adaptée automatiquement", notes, tested: rules.every((x) => x.status === "validated"), newAllergens: [...ok.ev2.allergens].filter((a) => !ev.allergens.has(a)) },
      };
    }
  }
  return { availability: "hidden", reasons, warnings, adapted: null };
}

// ---------------------------------------------------------------- suggestion par ingrédients (Tome 1 §6.3)
/** Placard de base : ne comptent jamais comme « manquants ». */
export const STAPLES = new Set([
  "Sel fin / gros sel / fleur de sel", "Poivre noir / blanc / vert", "Huile de tournesol / colza", "Huile d'olive vierge extra",
  "Sucre blanc / roux / cassonade / vergeoise", "Farine de blé T55", "Farine de blé T45", "Vinaigre de cidre", "Moutarde de Dijon",
]);

/** Familles interchangeables pour la suggestion (substitution « crédit 0,8 »). */
const FAMILIES: string[][] = [
  ["Farine de blé T45", "Farine de blé T55", "Farine de blé T65 (tradition)", "Farine de blé T80 (semi-complète)"],
  ["Huile de tournesol / colza", "Huile d'olive vierge extra", "Huile d'arachide", "Huile de pépins de raisin / maïs"],
  ["Yaourt nature", "Yaourt grec", "Fromage blanc / faisselle", "Skyr"],
  ["Crème fleurette (liquide)", "Crème fraîche", "Crème épaisse", "Yaourt grec"], // Tome 3 §16 : crème → yaourt grec
  ["Cuisse / pilon de poulet", "Blanc de poulet", "Poulet entier", "Dinde (escalope, cuisse, filet)"],
  ["Riz long / basmati / thaï", "Riz rond / sushi"],
  ["Oignon jaune", "Oignon rouge", "Échalote"],
  ["Citron", "Citron vert"],
  ["Coriandre fraîche", "Persil plat / frisé"],
  ["Tomate", "Coulis / passata / tomates pelées"],
  ["Beurre doux / demi-sel", "Beurre clarifié / ghee"],
  ["Gruyère / comté / emmental / beaufort", "Cheddar", "Parmesan / Parmigiano"],
  ["Potiron / citrouille", "Potimarron", "Butternut / courge musquée"],
  ["Levure boulangère sèche", "Levure boulangère fraîche"],
];
const FAMILY_OF = new Map<string, string[]>();
FAMILIES.forEach((f) => f.forEach((x) => FAMILY_OF.set(x, [...new Set([...(FAMILY_OF.get(x) ?? []), ...f])])));

export interface Suggestion {
  id: string;
  score: number;
  bucket: "all" | "almost" | "ideas";
  missing: string[];
  substitutes: Record<string, string[]>;
  usesExpiring: string[];
  coverage: number; // part des ingrédients saisis utilisés (mode « je veux tout utiliser »)
}

export function suggest(recipes: Recipe[], have: Set<string>, expiring: Set<string> = new Set(), subCredit = 0.8): Suggestion[] {
  const out: Suggestion[] = [];
  for (const r of recipes) {
    const req = flatten(r.ingredients).filter((l) => l.weight > 0 && !l.optional && l.ref);
    if (!req.length) continue;
    const tot = req.reduce((s, l) => s + l.weight, 0);
    let got = 0;
    const missing: RecipeLine[] = [];
    const substitutes: Record<string, string[]> = {};
    for (const l of req) {
      const ref = l.ref!;
      if (have.has(ref) || STAPLES.has(ref)) got += l.weight;
      else {
        const alt = (FAMILY_OF.get(ref) ?? []).filter((x) => have.has(x));
        if (alt.length) { got += l.weight * subCredit; substitutes[ref] = alt; }
        else missing.push(l);
      }
    }
    let score = (100 * got) / tot;
    score -= 15 * missing.filter((l) => l.weight === 3).length;
    const refs = new Set(req.map((l) => l.ref!));
    const usesExpiring = [...expiring].filter((e) => refs.has(e));
    score += 4 * usesExpiring.length;
    const usedHave = [...have].filter((h) => refs.has(h) || [...refs].some((x) => FAMILY_OF.get(x)?.includes(h))).length;
    const coverage = have.size ? usedHave / have.size : 0;
    if (have.size && !usedHave) continue; // ne propose pas une recette qui n'utilise aucun des ingrédients saisis
    const bucket = !missing.length ? "all" : missing.length <= 2 && !missing.some((l) => l.weight === 3) ? "almost" : score >= 60 ? "ideas" : null;
    if (bucket) out.push({ id: r.id, score: Math.round(score * 10) / 10, bucket, missing: [...new Set(missing.map((l) => l.ref!))], substitutes, usesExpiring, coverage });
  }
  return out.sort((a, b) => b.score - a.score || a.id.localeCompare(b.id));
}

/** Liste plate des ingrédients référencés d'une recette (sous-recettes incluses). */
export const refsOf = (r: Recipe) => [...new Set(flatten(r.ingredients).filter((l) => l.ref).map((l) => l.ref!))];
export { flatten };
