// Audit chef + famille du 10/11/2026 (bible/AUDIT_CHEF_FAMILLE_2026-11-10.md) : allergènes, conservation, âge hérité,
// « à lancer la veille ». Suite lancée par tests/engine.test.ts (npm test).
import { RECIPES, RECIPE_BY_ID } from "../src/lib/data";
import { evaluate } from "../src/lib/engine";
import { propose } from "../src/lib/propose";
import { autoPlan, weekDays } from "../src/lib/planner";
import { norm } from "../src/lib/text";
import type { Profile } from "../src/lib/types";
import { check } from "./helpers";

// —— 112 : les allergènes écrits dans un libellé sont dans la fiche (lignes composées séparées ou détectées)
const has = (id: string, a: string) => { const e = evaluate(RECIPE_BY_ID[id]); return e.allergens.has(a) || e.maybeAllergens.has(a); };
const CASES: [string, string][] = [["blanquette_veau", "GL"], ["blanquette_poulet", "GL"], ["moussaka", "GL"], ["bao_poulet", "AR"], ["poulet_general_tao", "SE"],
  ["ramen_miso_legumes_tofu", "SE"], ["lasagnes_bolognaise", "CE"], ["pot_au_feu", "CE"], ["beignets_crevettes_panes", "LA"], ["rouleaux_printemps", "AR"], ["mansaf_simple", "FC"]];
const WORDS: [string, RegExp][] = [["AR", /cacahuete|arachide/], ["SE", /sesame|tahini/], ["CE", /celeri/], ["GL", /\bfarine\b(?! de (riz|mais|pois|manioc|sarrasin|coco|chataigne|teff))|chapelure|panko/]];
const missAl = CASES.filter(([id, a]) => !has(id, a)).map(([id, a]) => `${id}:${a}`);
const missWords = RECIPES.flatMap((r) => r.ingredients.filter((l) => !l.ref?.startsWith("SUB:")).flatMap((l) => WORDS.filter(([a, rx]) => rx.test(norm(l.label)) && !/sans /.test(norm(l.label)) && !has(r.id, a)).map(([a]) => `${r.id}:${a}`)));
console.log("   allergènes des libellés : cas de l'audit manquants", missAl.length, "· mots d'allergène sans allergène", missWords.length, [...missAl, ...missWords].slice(0, 6).join(", "));
check("112 allergènes : ceux qu'un libellé nomme (« beurre + farine », « coriandre et cacahuètes ») sont dans la fiche", missAl.length === 0 && missWords.length === 0);

// —— 113 : conservation des aliments fragiles (poisson, fruits de mer, riz cuit, œuf cru) jamais plus longue que la règle
const days = (s: string) => { const m = s.match(/(\d+) jours?/); return m ? +m[1] : /semaine|mois/.test(s) ? 7 : /24 h|le jour même|tout de suite/.test(s) ? 1 : null; };
const tooLong = RECIPES.filter((r) => {
  const d = days(r.storage.split(/[.;]/)[0]); if (d === null) return false;
  if (r.rawEgg) return d > 1;
  if ((r.role === "plat" || r.role === "entree") && r.ingredients.some((l) => l.ref?.startsWith("Riz") ) && !/riz au lait|teurgoule/.test(norm(r.title))) return d > 1;
  return false;
}).map((r) => r.id);
console.log("   conservation : fiches au-delà de la règle", tooLong.length, tooLong.slice(0, 6).join(", "), "· riz cantonais :", RECIPE_BY_ID.riz_cantonais.storage.slice(0, 40));
check("113 conservation : œuf cru et riz cuit 24 h au plus ; plus de « 3 jours » par défaut sur ces fiches", tooLong.length === 0 && !/^3 jours/.test(RECIPE_BY_ID.moules_marinieres.storage));

// —— 114 : l'âge d'un plat tient compte de ses sous-recettes ; la mayonnaise maison donne la consigne « du commerce »
const subsOf = (id: string): string[] => RECIPE_BY_ID[id].ingredients.filter((l) => l.ref?.startsWith("SUB:")).map((l) => l.ref!.slice(4)).filter((s) => RECIPE_BY_ID[s]);
const younger = RECIPES.filter((r) => r.age !== null && subsOf(r.id).some((s) => { const sr = RECIPE_BY_ID[s]; return sr.age !== null && sr.age > r.age! && !sr.kids.startsWith("✓✓"); })).map((r) => r.id);
const mayoKids = RECIPES.filter((r) => r.age !== null && subsOf(r.id).includes("mayonnaise") && !/commerce/.test(r.kids)).map((r) => r.id);
console.log("   âge hérité : plats plus jeunes qu'une sous-recette", younger.length, "· mayonnaise sans consigne", mayoKids.length, [...younger, ...mayoKids].slice(0, 5).join(", "));
check("114 âge : jamais plus jeune qu'une sous-recette ; mayonnaise maison → consigne « mayonnaise du commerce » pour les petits", younger.length === 0 && mayoKids.length === 0 && RECIPE_BY_ID.sauce_facon_giant.rawEgg === true);

// —— 115 : à lancer la veille : repéré, jamais proposé pour ce soir, ni planifié le jour même
const flagged = ["falafels", "riz_cantonais", "tameya", "chich_taouk", "gallo_pinto", "brandade"].filter((id) => !RECIPE_BY_ID[id].veille);
const props = Array.from({ length: 40 }, (_, i) => propose(RECIPES, { hour: 19, zone: "nord", maxMinutes: 45, fridge: [], seed: 977 * (i + 1) })).flat();
const tonightBad = props.filter((p) => p.r.veille).map((p) => p.r.id);
const fam: Profile = { noPork: false, alcohol: "allowed", strict: false, vegetarian: false, allergens: [], adult: true, kidsAge: 4, equipment: ["four", "plaques", "poele", "casserole", "mixeur"], onboarded: true, household: { adults: 2, kids: [4, 8] } } as Profile;
let todayBad = 0, longWeekday = 0, sameMain = 0;
for (let s = 1; s <= 12; s++) {
  const ds = weekDays(0, new Date("2026-11-10T12:00:00"));
  const pl = autoPlan(ds, {}, { slots: ["soir"], weekdayMax: 45, zone: "nord", profile: fam, leftovers: null, seed: 6151 * s, today: ds[0] });
  if (RECIPE_BY_ID[pl[ds[0]]?.soir ?? ""]?.veille) todayBad++;
  for (const d of ds) { const r = RECIPE_BY_ID[pl[d]?.soir ?? ""]; const dow = new Date(`${d}T12:00:00`).getDay(); if (r && dow >= 1 && dow <= 5 && r.active + r.rest + (r.avance ?? 0) > 45) longWeekday++; }
  const mains = ds.flatMap((d) => RECIPE_BY_ID[pl[d]?.soir ?? ""]?.ingredients.filter((l) => l.weight >= 3 && /moule|palourde|poulpe|crevette/i.test(l.ref ?? "")).map((l) => l.ref) ?? []);
  sameMain += mains.length - new Set(mains).size;
}
console.log("   la veille :", RECIPES.filter((r) => r.veille).length, "fiches · non repérées", flagged.join(", ") || "aucune", "· proposées ce soir", tonightBad.length, "· planifiées le jour même", todayBad, "· soirs > 45 min (enfants)", longWeekday, "· coquillages répétés", sameMain);
check("115 à lancer la veille : repéré, ni proposé ce soir, ni planifié le jour même ; soirs de semaine ≤ 45 min en tout avec des enfants",
  flagged.length === 0 && tonightBad.length === 0 && todayBad === 0 && longWeekday === 0 && sameMain === 0);

// —— 116 : liste de courses : gousses, bouquets, pièces et grammes additionnés (plus de « 2 gousses + 1 ½ gousses + … »)
import { consolidate } from "../src/lib/planner";
import { kidFriendly, youngAdultOnly } from "../src/lib/famille";
import { INGREDIENTS } from "../src/lib/data";
const WEEK = ["nikujaga", "thiou_poulet", "maharagwe", "white_chicken_chili", "pancit_bihon", "chou_braise_saucisses", "moules_frites", "chilaquiles_verts", "pasta_genovese", "saumon_teriyaki"];
const shopW = consolidate(WEEK.map((id) => ({ id, factor: 3 / RECIPE_BY_ID[id].portions })), 11);
const garlic = shopW.find((l) => l.ref === "Ail")?.label ?? "";
const messy = shopW.filter((l) => /^(Ail|Persil|Coriandre|Oignon jaune|Pomme de terre)/.test(l.ref) && / \+ /.test(l.label)).map((l) => l.label);
console.log("   courses :", shopW.length, "lignes ·", garlic, "· lignes encore composées :", messy.length, messy.slice(0, 2).join(" | "));
check("116 courses : l'ail en gousses (et têtes), les herbes en bouquets, oignons et pommes de terre en un seul poids", messy.length === 0 && /gousses/.test(garlic));

// —— 117 : saisons justes (épinard et cresson l'hiver, citron au placard) ; café et alcool peu cuit écartés pour les moins de 6 ans
const four: Profile = { ...fam, household: { adults: 2, kids: [4] }, kidsAge: 4 } as Profile;
const seasonOk = INGREDIENTS["Épinard"].season.includes(11) && INGREDIENTS["Cresson"].season.includes(1) && INGREDIENTS["Citron"].season.length === 0;
const kidsOk = youngAdultOnly(RECIPE_BY_ID.moules_marinieres) && !kidFriendly(RECIPE_BY_ID.moules_marinieres, four) && !youngAdultOnly(RECIPE_BY_ID.boeuf_bourguignon)
  && !youngAdultOnly(RECIPE_BY_ID.gateau_anniversaire_choco);
console.log("   saisons :", seasonOk ? "épinard, cresson, citron justes" : "À CORRIGER", "· moins de 6 ans : moules marinières écartées, bourguignon gardé, gâteau d'anniversaire à l'eau :", kidsOk);
check("117 saisons corrigées ; café et alcool peu cuit écartés pour un enfant de moins de 6 ans, vin mijoté 2 h permis", seasonOk && kidsOk);

// —— 118 : la famille au quotidien : congélation dite, enfants qui aident, lait cru signalé, dessert de semaine léger
const plats = RECIPES.filter((r) => r.role === "plat");
const freeze = plats.filter((r) => /cong[eèé]l/i.test(r.storage)).length;
const help = RECIPES.filter((r) => r.kidHelp || /particip/.test(r.kids)).length;
const rawMilk = RECIPE_BY_ID.tartiflette.tips.some((t) => /enceinte/.test(t));
const light = RECIPES.filter((r) => r.role === "dessert" && r.profile.includes("leger")).length;
console.log("   famille : congélation", freeze, "plats · enfants qui aident", help, "fiches · lait cru signalé", rawMilk, "· desserts légers", light);
check("118 famille : ≥ 150 plats disent s'ils se congèlent, ≥ 300 fiches disent ce que les enfants font, lait cru signalé, ≥ 15 desserts légers", freeze >= 150 && help >= 300 && rawMilk && light >= 15);

// —— 119 : photos des fiches écrites d'après TikTok (10/11/2026) : sous licence libre, créditées, manifeste compact relu
import { IMAGES } from "../src/components/photo";
const credited = RECIPES.filter((r) => r.credit?.length);
const withPhoto = credited.filter((r) => IMAGES[`recette/${r.id}`]);
const okMeta = withPhoto.every((r) => { const m = IMAGES[`recette/${r.id}`]; return m.path === `img/recette/${r.id}` && m.sizes.length > 0 && /^#/.test(m.color); });
console.log("   photos des fiches TikTok :", withPhoto.length, "sur", credited.length, "· manifeste relu :", okMeta);
check("119 photos : au moins 110 fiches TikTok illustrées par une photo libre, chemins et tailles relus depuis le manifeste compact", withPhoto.length >= 110 && okMeta);
