// Retour d'usage du 22/10/2026 : « Propose-moi » et les autres idées variaient peu ; le nombre de vrais plats semblait faible.
// Suite lancée par tests/engine.test.ts (npm test).
import { readFileSync } from "node:fs";
import { RECIPES, RECIPE_BY_ID } from "../src/lib/data";
import { momentOf, propose } from "../src/lib/propose";
import { dailyPick, pickVaried, shuffled } from "../src/lib/variete";
import { check } from "./helpers";

// —— 96 « Propose-moi » : 20 appuis d'affilée, avec la mémoire de l'appli
const press = (hour: number, maxMinutes: number) => {
  let recent: string[] = []; const seen = new Map<string, number>(); let repeats = 0; let drinks = 0; let sameMacro = 0;
  for (let i = 0; i < 20; i++) {
    const res = propose(RECIPES, { hour, zone: "nord", maxMinutes, fridge: [], seed: 1000 + i * 7919, recent: new Set(recent) });
    if (new Set(res.map((p) => p.r.macro)).size < res.length) sameMacro++;
    for (const p of res) { if (recent.includes(p.r.id)) repeats++; if (p.r.role === "boisson" || p.r.kind === "Boisson") drinks++; seen.set(p.r.id, (seen.get(p.r.id) ?? 0) + 1); }
    recent = [...res.map((p) => p.r.id), ...recent].slice(0, 45);
  }
  return { distinct: seen.size, max: Math.max(...seen.values()), repeats, drinks, sameMacro };
};
const midi = press(12, 45), soir = press(19, 20), matin = press(8, 45), gouter = press(16, 45);
console.log("   propose-moi (20 appuis) : midi", JSON.stringify(midi), "· soir 20 min", JSON.stringify(soir), "· matin", JSON.stringify(matin), "· goûter", JSON.stringify(gouter));
check("96 « Propose-moi » : au moins 45 recettes différentes sur 60 propositions au repas, jamais une boisson le matin ou au goûter, trois cuisines différentes à chaque appui, la mémoire évite les répétitions",
  midi.distinct >= 45 && soir.distinct >= 40 && matin.distinct >= 35 && gouter.distinct >= 35 && midi.max <= 3
  && matin.drinks + gouter.drinks === 0 && midi.sameMacro === 0 && midi.repeats <= 3
  && !momentOf(8).test(RECIPE_BY_ID.salade_riz_thon_mais) && momentOf(8).test(RECIPE_BY_ID.upma));

// —— 97 blocs « du jour » : un vrai renouvellement d'un jour à l'autre, et un tirage pondéré qui ne sort pas toujours les mêmes
const pool = RECIPES.filter((r) => r.role === "plat").map((r) => r.id);
const day = 86400000; const t0 = Date.UTC(2026, 9, 22, 12);
let overlap = 0;
for (let d = 0; d < 14; d++) { const a = new Set(dailyPick(pool, 12, 5, t0 + d * day)); overlap += dailyPick(pool, 12, 5, t0 + (d + 1) * day).filter((x) => a.has(x)).length; }
const weights = Array.from({ length: 50 }, (_, i) => i);
const tops = new Set(Array.from({ length: 40 }, (_, k) => pickVaried(weights, 1, { seed: k * 101 + 7, score: (x) => x / 10, temperature: 2 })[0]));
console.log("   blocs du jour : recettes communes entre deux jours consécutifs", (overlap / 14).toFixed(1), "sur 12 · tirage pondéré : ", tops.size, "gagnants différents sur 40 tirages");
check("97 idées du jour : moins de 2 recettes sur 12 en commun d'un jour au suivant, même jour = même liste, le tirage pondéré favorise sans figer",
  overlap / 14 < 2 && dailyPick(pool, 12, 5, t0).join() === dailyPick(pool, 12, 5, t0 + 3600000).join() && tops.size >= 10
  && shuffled([1, 2, 3, 4, 5], 1).join() !== shuffled([1, 2, 3, 4, 5], 2).join());

// —— 98 catalogue : de vrais plats, sans doublon, dans chaque région
const plats = RECIPES.filter((r) => r.role === "plat");
const byMacro = (m: string) => plats.filter((r) => r.macro === m).length;
const renames = JSON.parse(readFileSync("src/data/renames.json", "utf8")) as Record<string, string>;
const titles = new Map<string, number>(); for (const r of plats) { const k = r.title.toLowerCase().replace(/\(.*\)/, "").trim(); titles.set(k, (titles.get(k) ?? 0) + 1); }
const dupTitles = [...titles].filter(([, n]) => n > 1).map(([k]) => k);
console.log("   catalogue :", RECIPES.length, "fiches ·", plats.length, "plats · Océanie", byMacro("oceanie"), "· Amérique du Nord", byMacro("amerique_nord"), "· Amérique latine", byMacro("amerique_latine"),
  "· Moyen-Orient", byMacro("moyen_orient"), "· Maghreb", byMacro("maghreb"), "· Afrique", byMacro("afrique"), "· titres en double :", dupTitles.join(", ") || "aucun");
check("98 catalogue : au moins 520 plats, chaque grande région à 25 plats ou plus (Océanie 15), les doublons fusionnés sont suivis par la table de renommage, aucun titre en double",
  plats.length >= 520 && byMacro("oceanie") >= 15 && ["amerique_nord", "amerique_latine", "moyen_orient", "maghreb", "afrique", "asie_sud", "asie_sud_est", "asie_est", "europe_nord"].every((m) => byMacro(m) >= 25)
  && ["misir_wot", "carbonade_flamande", "marinade_adobo"].every((id) => !RECIPE_BY_ID[id] && !!RECIPE_BY_ID[renames[id]]) && dupTitles.length === 0);
