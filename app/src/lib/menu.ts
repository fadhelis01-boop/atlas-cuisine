// Composeur de menu à partir d'un plat (Tome 1 §12.3) : entrée, plat, dessert + boissons.
// Critères : régime du foyer, cohérence régionale, équilibre (léger → riche → léger), pas de répétition
// de l'ingrédient dominant, zéro déchet (sous-produits réutilisés, bottes d'herbes partagées), temps actif total.
import { RECIPES, RECIPE_BY_ID } from "./data";
import { refsOf, verdict } from "./engine";
import { ACCORDS } from "./content";
import type { Profile, Recipe, Role } from "./types";

export interface MenuProposal {
  name: "Classique" | "Léger" | "Audacieux";
  courses: { role: Role; recipe: Recipe; adapted: boolean }[];
  score: number;
  reasons: string[];
  zeroWaste: string[];
  activeTotal: number;
  drinks: { sa: string[]; a: string[]; why: string };
}

/** Sous-produits : une recette en laisse, une autre les consomme. */
const BYPRODUCTS: { from: string; leftover: string; to: string }[] = [
  { from: "Jaune d'œuf", leftover: "blancs d'œufs", to: "Blanc d'œuf" },
  { from: "Pois chiches (secs / bocal)", leftover: "aquafaba (jus de pois chiches)", to: "Aquafaba (eau de pois chiches)" },
  { from: "Poulet entier", leftover: "carcasse", to: "Bouillon d'os maison (bœuf/volaille)" },
];
/** Produits vendus en botte ou en entier : les partager entre plats évite d'en jeter la moitié. */
const PERISHABLE_SHARE = new Set([
  "Persil plat / frisé", "Coriandre fraîche", "Menthe", "Basilic", "Ciboulette", "Aneth", "Citron", "Citron vert", "Orange",
  "Yaourt grec", "Yaourt nature", "Crème fraîche", "Crème fleurette (liquide)", "Lait entier / demi-écrémé / écrémé", "Oignon nouveau / cébette",
  "Poivron (rouge/jaune/vert)", "Concombre", "Tomate", "Gingembre frais", "Mozzarella / burrata",
]);

const isLight = (r: Recipe) => r.profile.includes("leger") || r.profile.includes("acide");
const isRich = (r: Recipe) => r.profile.includes("gras") || r.profile.includes("viande_rouge");
const dominant = (r: Recipe) => new Set(r.ingredients.filter((l) => l.weight === 3 && l.ref && !l.ref.startsWith("SUB:")).map((l) => l.ref!));

function pairScore(a: Recipe, b: Recipe, mode: MenuProposal["name"]) {
  let s = 0;
  const why: string[] = [];
  const zw: string[] = [];
  if (a.macro === b.macro) { s += mode === "Audacieux" ? -2 : 3; if (mode !== "Audacieux") why.push("même région"); }
  else if (mode === "Audacieux") s += 2;
  if (a.regionPath[2] && a.regionPath[2] === b.regionPath[2]) s += 2;
  const da = dominant(a), db = dominant(b);
  const rep = [...da].filter((x) => db.has(x));
  s -= 4 * rep.length; // pas le même ingrédient dominant deux fois
  const ra = new Set(refsOf(a)), rb = new Set(refsOf(b));
  for (const bp of BYPRODUCTS) {
    if ((ra.has(bp.from) && rb.has(bp.to)) || (rb.has(bp.from) && ra.has(bp.to))) { s += 5; zw.push(`les ${bp.leftover} de l'un servent à l'autre`); }
  }
  const shared = [...ra].filter((x) => rb.has(x) && PERISHABLE_SHARE.has(x));
  if (shared.length) { s += Math.min(3, shared.length); zw.push(`ingrédients partagés : ${shared.map((x) => x.split(" (")[0].split(" /")[0].toLowerCase()).join(", ")}`); }
  return { s, why, zw };
}

export function composeMenus(anchorId: string, p: Profile): MenuProposal[] {
  const anchor = RECIPE_BY_ID[anchorId];
  if (!anchor) return [];
  const usable = (r: Recipe) => {
    const v = verdict(r, p);
    return v.availability === "hidden" ? null : { r, adapted: v.availability === "adaptable" };
  };
  const pool = (role: Role) => RECIPES.filter((r) => r.role === role && r.id !== anchor.id).map(usable).filter(Boolean) as { r: Recipe; adapted: boolean }[];
  const anchorRole: Role = anchor.role === "autre" ? "plat" : anchor.role;
  const roles: Role[] = (["entree", "plat", "dessert"] as Role[]).filter((x) => x !== anchorRole);
  const out: MenuProposal[] = [];
  for (const mode of ["Classique", "Léger", "Audacieux"] as const) {
    const chosen: { role: Role; recipe: Recipe; adapted: boolean }[] = [{ role: anchorRole, recipe: anchor, adapted: usable(anchor)?.adapted ?? false }];
    const reasons: string[] = [];
    const zeroWaste: string[] = [];
    let total = 0;
    for (const role of roles) {
      const used = new Set(out.flatMap((m) => m.courses.filter((c) => c.role === role).map((c) => c.recipe.id)));
      let best: { r: Recipe; adapted: boolean; s: number; why: string[]; zw: string[] } | null = null;
      for (const c of pool(role)) {
        let s = 0; const why: string[] = []; const zw: string[] = [];
        for (const ch of chosen) { const ps = pairScore(ch.recipe, c.r, mode); s += ps.s; why.push(...ps.why); zw.push(...ps.zw); }
        if (isRich(anchor) && isLight(c.r)) { s += 3; why.push("léger après un plat riche"); }
        if (mode === "Léger") s += isLight(c.r) ? 4 : isRich(c.r) ? -4 : 0;
        if (c.adapted) s -= 1; // une version adaptée « à tester » passe après une recette d'origine conforme
        if (used.has(c.r.id)) s -= 6; // varier les trois propositions
        s -= Math.max(0, c.r.active - 40) / 20;
        if (!best || s > best.s) best = { ...c, s, why, zw };
      }
      if (best) {
        chosen.push({ role, recipe: best.r, adapted: best.adapted });
        total += best.s;
        reasons.push(...best.why);
        zeroWaste.push(...best.zw);
      }
    }
    const order: Role[] = ["entree", "plat", "dessert"];
    chosen.sort((a, b) => order.indexOf(a.role) - order.indexOf(b.role));
    const main = chosen.find((c) => c.role === "plat")?.recipe ?? anchor;
    const prof = main.profile.find((x) => ACCORDS[x]) ?? "leger";
    const acc = ACCORDS[prof];
    const sa = [...new Set([...main.drinksNoAlcohol, ...acc.sa])].slice(0, 4);
    const a = [...new Set([...main.drinksAlcohol, ...acc.a])].slice(0, 3);
    out.push({
      name: mode, courses: chosen, score: Math.round(total), reasons: [...new Set(reasons)], zeroWaste: [...new Set(zeroWaste)],
      activeTotal: chosen.reduce((s, c) => s + c.recipe.active, 0), drinks: { sa, a, why: acc.why },
    });
  }
  return out;
}
