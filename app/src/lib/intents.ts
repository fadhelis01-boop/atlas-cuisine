// Recherche par intention (audit UX 2026-10-16 §2.6) : on ne cherche pas toujours un nom de plat,
// mais une situation (« rapide », « végétarien », « pas cher », « apéro », « sans four »…). Les mots reconnus
// deviennent des filtres ; le reste de la requête est cherché normalement.
import { evaluate } from "./engine";
import { ovenPlan, norm } from "./text";
import type { Recipe } from "./types";

export interface Intent { id: string; label: string; test: (r: Recipe) => boolean }
const veg = (r: Recipe) => evaluate(r).flesh.length === 0;
const BREAKFAST = /pancake|porridge|granola|crepe|gaufre|brunch|muesli|oeufs? (brouill|cocotte|benedicte|mollet)|toast|pain perdu|smoothie|overnight|chia|tartine|shakshuka|menemen|omelette|bol |bowl/;

const RULES: [RegExp, Intent][] = [
  [/\b(rapide|rapides|vite|express|presse|pressee|en 15 min|15 min|20 min|minute)\b/, { id: "rapide", label: "rapide (≤ 30 min)", test: (r) => r.active + r.rest <= 30 }],
  [/\b(vegetarien|vegetarienne|vege|veggie|sans viande|vegan|vegetal)\b/, { id: "vege", label: "végétarien", test: veg }],
  [/\b(pas cher|economique|petit budget|budget|bon marche|pas chere)\b/, { id: "eco", label: "pas cher", test: (r) => r.cost === "€" }],
  [/\b(apero|aperitif|apéro|tapas|amuse bouche|finger food)\b/, { id: "apero", label: "apéro", test: (r) => r.fetes.includes("Apéritif dînatoire") || (r.role === "entree" && r.active <= 30) }],
  [/\b(sans four|pas de four|sans cuisson au four|a la poele|plaque)\b/, { id: "nofour", label: "sans four", test: (r) => !ovenPlan(r.steps) && !/four|enfourn/i.test(r.equipment) }],
  [/\b(sans cuisson|cru|crue|no cook)\b/, { id: "cru", label: "sans cuisson", test: (r) => r.rest <= 5 && !/cui|four|poele|feu|bouill|fri/i.test(r.steps.join(" ")) }],
  [/\b(facile|facil|simple|debutant|debutante|inratable|basique)\b/, { id: "facile", label: "facile", test: (r) => r.level === 1 }],
  [/\b(dessert|desserts|sucre|sucree|gouter|patisserie)\b/, { id: "dessert", label: "dessert", test: (r) => r.role === "dessert" }],
  [/\b(entree|entrees)\b/, { id: "entree", label: "entrée", test: (r) => r.role === "entree" }],
  [/\b(plat|plats|diner|dejeuner|ce soir|soir|repas)\b/, { id: "plat", label: "plat", test: (r) => r.role === "plat" }],
  [/\b(boisson|boissons|cocktail|mocktail|jus|a boire)\b/, { id: "boisson", label: "boisson", test: (r) => r.role === "boisson" }],
  [/\b(petit dej|petit dejeuner|brunch|matin|breakfast)\b/, { id: "brunch", label: "petit-déjeuner, brunch", test: (r) => r.cats.includes("brunch") || BREAKFAST.test(norm(r.title)) || (r.role === "dessert" && r.active <= 20 && /pain|crepe|gaufre|yaourt|fruit/.test(norm(r.title))) }],
  [/\b(enfant|enfants|bebe|kids|famille)\b/, { id: "enfants", label: "pour les enfants", test: (r) => r.age !== null && r.age <= 3 }],
  [/\b(leger|legere|light|healthy|sain|equilibre)\b/, { id: "leger", label: "léger", test: (r) => r.profile.includes("leger") }],
  [/\b(epice|epicee|piquant|piquante|releve)\b/, { id: "epice", label: "épicé", test: (r) => r.profile.includes("epice") }],
  [/\b(poisson|fruits de mer)\b/, { id: "mer", label: "poisson", test: (r) => r.profile.includes("poisson") }],
  [/\b(fete|fetes|reception|invites|anniversaire)\b/, { id: "fete", label: "pour recevoir", test: (r) => r.fetes.length > 0 }],
  [/\b(soupe|soupes|veloute|potage)\b/, { id: "soupe", label: "soupe", test: (r) => /soupe|veloute|potage|bouillon|harira|chorba|pho|ramen|laksa|bortsch|gazpacho|minestrone/.test(norm(r.title)) }],
  [/\b(salade|salades)\b/, { id: "salade", label: "salade", test: (r) => r.cats.includes("salade") || /salade|taboule|bowl|poke|fattouche|panzanella/.test(norm(r.title)) }],
];

/** Sépare une requête en intentions reconnues et en texte restant à chercher. */
export function parseIntents(q: string): { intents: Intent[]; rest: string } {
  let t = ` ${norm(q)} `;
  const intents: Intent[] = [];
  for (const [rx, it] of RULES) {
    if (rx.test(t)) { intents.push(it); t = t.replace(new RegExp(rx.source, "g"), " "); }
  }
  // mots de liaison restants (« un dessert facile pour ce soir »)
  const rest = t.replace(/\b(un|une|des|de|du|le|la|les|pour|avec|et|a|au|aux|en|qui|quoi|recette|recettes|idee|idees|je|veux|cherche|faire|manger|cuisiner)\b/g, " ").replace(/\s+/g, " ").trim();
  return { intents, rest };
}

/** Distance d'édition (fautes de frappe lourdes : « creppe » → « crêpe »). */
export function editDistance(a: string, b: string): number {
  const d = Array.from({ length: a.length + 1 }, (_, i) => [i, ...Array(b.length).fill(0)]);
  for (let j = 1; j <= b.length; j++) d[0][j] = j;
  for (let i = 1; i <= a.length; i++) for (let j = 1; j <= b.length; j++)
    d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
  return d[a.length][b.length];
}

/** Rattrapage : recettes dont un mot du titre est à 1-2 fautes d'un mot de la requête. */
export function fuzzyRecipes(list: Recipe[], q: string): Recipe[] {
  const words = norm(q).split(" ").filter((w) => w.length >= 4);
  if (!words.length) return [];
  return list.filter((r) => {
    const tw = norm(r.title).split(" ").filter((w) => w.length >= 3);
    return words.every((w) => tw.some((x) => editDistance(w, x.length > w.length + 2 ? x.slice(0, w.length + 1) : x) <= (w.length >= 6 ? 2 : 1)));
  });
}
