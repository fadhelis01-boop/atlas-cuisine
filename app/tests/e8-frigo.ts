// Retour d'usage du 22/10/2026 : « Que cuisiner avec mon frigo » sans bouton de lancement, idées sans rapport, rien d'autre à
// proposer ; import d'une légende TikTok écrite d'un seul bloc. Suite lancée par tests/engine.test.ts (npm test).
import { RECIPES } from "../src/lib/data";
import { STAPLES } from "../src/lib/engine";
import { buildMenu, pickIdeas, rankFor } from "../src/lib/frigo";
import { classify, matchIngredient } from "../src/lib/classify";
import { check } from "./helpers";

const have = ["Œuf entier (frais)", "Tomate", "Courgette", "Cuisse / pilon de poulet"];
const o = { have, pantry: STAPLES };
const plats = rankFor(RECIPES, "plat", o), entrees = rankFor(RECIPES, "entree", o), desserts = rankFor(RECIPES, "dessert", o);
const first = pickIdeas(plats, 6, 1), next = pickIdeas(plats, 6, 2, new Set(first.map((x) => x.r.id)));
const top10 = plats.slice(0, 10);
console.log("   frigo (œufs, tomate, courgette, poulet) : plats", plats.length, "· entrées", entrees.length, "· desserts", desserts.length,
  "· en tête :", top10.slice(0, 4).map((x) => x.r.id).join(", "), "· 2e série :", next.slice(0, 3).map((x) => x.r.id).join(", "));
check("101 frigo : chaque idée utilise au moins un ingrédient choisi et reste du bon service ; les premières en utilisent plusieurs ; « D'autres idées » n'en répète aucune ; rien sans ingrédient",
  plats.length >= 20 && entrees.length >= 5 && desserts.length >= 5
  && [...plats, ...entrees, ...desserts].every((x) => x.used.length >= 1 && x.s.missing.length <= 4)
  && plats.every((x) => x.r.role === "plat") && desserts.every((x) => x.r.role === "dessert")
  && top10.filter((x) => x.used.length >= 2).length >= 7
  && first.length === 6 && next.length === 6 && !next.some((x) => first.some((y) => y.r.id === x.r.id))
  && rankFor(RECIPES, "plat", { have: [], pantry: STAPLES }).length === 0
  && rankFor(RECIPES, "plat", { ...o, maxMinutes: 30 }).every((x) => x.r.active + x.r.rest <= 30));

const menus = [1, 2, 3, 4, 5].map((s) => buildMenu(RECIPES, o, s));
const complete = menus.filter((m) => m.entree && m.plat && m.dessert);
const repeatsMain = menus.filter((m) => {
  const main = new Set(m.plat?.r.ingredients.filter((l) => l.weight === 3).map((l) => l.ref) ?? []);
  return [m.entree, m.dessert].some((x) => x?.r.ingredients.some((l) => l.weight === 3 && main.has(l.ref)));
}).length;
console.log("   menus du frigo :", menus.map((m) => [m.entree?.r.id, m.plat?.r.id, m.dessert?.r.id].join(" + ")).slice(0, 2).join(" | "), "· ingrédients non utilisés :", menus.map((m) => m.leftover.length).join(","));
check("102 menu complet du frigo : entrée, plat et dessert à chaque fois, jamais le même ingrédient principal que le plat, et des menus différents d'un appui à l'autre",
  complete.length === 5 && repeatsMain === 0 && new Set(menus.map((m) => m.plat!.r.id)).size >= 3);

// —— 103 import : légende d'un seul bloc (cas le plus courant sur TikTok)
const c = classify("La recette du tajine de bœuf, olives, citron confit 🍋 Ingrédients : 600g de viande de boeuf, 1 oignon, 2 pommes de terre, 1 citron confit, 100g d'olives vertes, 1/2 botte de persil, curcuma, cumin, huile d'olive");
console.log("   import d'un bloc :", c.title, "·", c.ingredients.length, "ingrédients ·", c.ingredients.slice(0, 3).map((i) => i.ref).join(", "), "· porc", c.pork);
check("103 import : titre sans la liste, ingrédients d'une ligne découpés aux virgules, bœuf et huile d'olive bien reconnus, un bouillon de bœuf garde son doute",
  c.title === "La recette du tajine de bœuf, olives, citron confit 🍋" && c.ingredients.length >= 9 && c.cat === "maghreb"
  && c.ingredients[0].ref === "Paleron" && c.ingredients.at(-1)!.ref === "Huile d'olive vierge extra"
  && matchIngredient("1 cube de bouillon de bœuf") !== "Paleron" && matchIngredient("2 hauts de cuisse de poulet") === "Cuisse / pilon de poulet");

// —— 104 barre « ajouter un ingrédient » : les mots de tous les jours trouvent le bon produit
import { findIngredients } from "../src/lib/ingredientSearch";
const fi = (q: string) => findIngredients(q);
const probes = { fromage: fi("fromage"), oeuf: fi("oeuf"), pdt: fi("pdt"), lardons: fi("lardons"), creme: fi("crème"), poulet: fi("poulet"), steak: fi("steak haché"), x: fi("zzzz") };
console.log("   barre d'ingrédients :", Object.entries(probes).map(([k, v]) => `${k} → ${v.slice(0, 2).join(" | ") || "rien"}`).join(" · "));
check("104 barre d'ingrédients : « fromage » → fromages (pas de fromage de tête en tête), « oeuf » sans bœuf, « pdt » → pommes de terre, « lardons » → lardons de volaille d'abord, « crème » → crème fraîche, rien d'inventé",
  probes.fromage[0] === "Gruyère / comté / emmental / beaufort" && probes.fromage.length === 8 && !probes.fromage.slice(0, 6).includes("Fromage de tête")
  && probes.oeuf[0] === "Œuf entier (frais)" && !probes.oeuf.some((n) => /Bœuf/.test(n)) && probes.pdt[0] === "Pomme de terre"
  && probes.lardons[0] === "Lardons de dinde / de volaille fumés" && !probes.lardons.some((n) => /Salsifis|Rhum/.test(n))
  && probes.creme[0] === "Crème fraîche" && probes.poulet.includes("Cuisse / pilon de poulet") && probes.steak[0] === "Bœuf haché" && probes.x.length === 0
  && findIngredients("fromage", ["Gruyère / comté / emmental / beaufort"])[0] === "Mozzarella / burrata");
