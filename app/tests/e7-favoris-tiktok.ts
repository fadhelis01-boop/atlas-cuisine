// Favoris TikTok du 22/10/2026 : recettes enregistrées par le propriétaire (et vidéos populaires des créateurs suivis)
// réécrites en fiches ATLAS, créditées. Suite lancée par tests/engine.test.ts (npm test).
import { readFileSync } from "node:fs";
import { RECIPES, RECIPE_BY_ID } from "../src/lib/data";
import { evaluate } from "../src/lib/engine";
import { norm } from "../src/lib/text";
import { check } from "./helpers";

type Det = { steps: string[]; videos?: { url: string; author: string }[]; credit?: { author: string; url: string }[]; intro: string };
const detail = JSON.parse(readFileSync("src/data/recipes_detail.json", "utf8")) as Record<string, Det>;
const imports = JSON.parse(readFileSync("src/data/imports.json", "utf8")) as { url: string }[];
const fav = Object.entries(detail).filter(([, d]) => d.credit?.length).map(([id, d]) => ({ id, d, r: RECIPE_BY_ID[id] }));

// —— 99 crédit : chaque fiche tirée d'une vidéo nomme son auteur, renvoie à la vidéo et la met en tête de ses vidéos
const badCredit = fav.filter(({ d }) => !d.credit!.every((c) => /^@[\w.]+$/.test(c.author) && /^https:\/\/www\.tiktok\.com\/@[\w.]+\/video\/\d+$/.test(c.url) && c.url.includes(c.author + "/"))
  || d.videos?.[0]?.url !== d.credit![0].url);
const inLibrary = fav.filter(({ d }) => imports.some((i) => i.url === d.credit![0].url)).length;
console.log("   favoris TikTok :", fav.length, "fiches créditées ·", new Set(fav.flatMap(({ d }) => d.credit!.map((c) => c.author))).size, "créateurs ·", inLibrary, "vidéos d'origine aussi dans la bibliothèque · crédits mal formés :", badCredit.map((x) => x.id).join(", ") || "aucun");
check("99 favoris TikTok : au moins 40 fiches, chaque crédit nomme le compte et pointe vers sa vidéo (même compte), la vidéo d'origine est la première de la fiche",
  fav.length >= 40 && badCredit.length === 0 && fav.every(({ r }) => !!r && r.source.includes("vague 2")));

// —— 100 règles ATLAS : pas de porc dans la fiche (seulement en version), alcool seulement avec sa variante sans alcool,
//         au moins 4 étapes, chaque étape de cuisson chiffrée, pas de doublon de plat avec le catalogue
// une étape de cuisson s'annonce par son titre en gras (« **Rôtir.** », « **Mijoter.** »…)
const COOK = /^\W*(cuire|precuire|rotir|saisir|dorer|mijoter|frire|premiere friture|seconde friture|frire deux fois|griller|gratiner|pocher|braiser|reduire|confire|poeler|laquer|vapeur|fondre|sauter|bouillir|caramelis)/;
const DUREE = /\d+\s*(?:à\s*\d+\s*)?(?:min|h)\b|\d+\s*s\b|une nuit/;
const issues = fav.flatMap(({ id, d, r }) => {
  const e = evaluate(r); const out: string[] = [];
  if (e.pork === "violates") out.push(`${id}:porc`);
  if (e.alcohol === "violates" && !r.variants.some((v) => v.constraints.includes("alcohol"))) out.push(`${id}:alcool sans variante`);
  if (d.steps.length < 4) out.push(`${id}:étapes`);
  for (const st of d.steps) if (COOK.test(norm(st)) && !DUREE.test(st) && !/^\W*(servir|monter|garnir|rouler|melanger|assembler)/.test(norm(st))) out.push(`${id}:durée « ${st.slice(0, 40)} »`);
  return out;
});
const key = (s: string) => norm(s).replace(/\(.*\)/, "").replace(/[^a-z ]/g, " ").replace(/\s+/g, " ").trim();
const origins = new Map<string, string[]>(); for (const r of RECIPES) { const k = key(r.origin.split("·")[0]); if (k.length > 3) origins.set(k, [...(origins.get(k) ?? []), r.id]); }
const dupOrigin = fav.filter(({ r }) => (origins.get(key(r.origin.split("·")[0])) ?? []).length > 1).map(({ id }) => id);
console.log("   règles :", issues.length, "écarts", issues.slice(0, 6).join(" ; "), "· même nom d'origine qu'une autre fiche :", dupOrigin.join(", ") || "aucun");
check("100 favoris TikTok adaptés : jamais de porc, l'alcool toujours avec sa variante sans alcool, ≥ 4 étapes, chaque cuisson chiffrée, aucun plat déjà au catalogue sous le même nom",
  issues.length === 0 && dupOrigin.length === 0);
