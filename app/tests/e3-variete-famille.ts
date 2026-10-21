// Variété, audit du chef, D21, restes, Bien choisir, mijotés, familles, pique-nique (tests 63 à 75)
// Suite lancée par tests/engine.test.ts (npm test).
import { INGREDIENTS, INGREDIENT_NAMES, RECIPES, RECIPE_BY_ID, loadImports, loadLeftovers, mergeDetails } from "../src/lib/data";
import recipeDetail from "../src/data/recipes_detail.json";
import { evaluate, evaluateLines, flatten, suggest, verdict } from "../src/lib/engine";
import { classify, linksFromExport } from "../src/lib/classify";
import { embedOf } from "../src/components/video";
import { gestureLabel, norm, ovenPlan, splitStep } from "../src/lib/text";
import { TECHNIQUES, techniqueFor } from "../src/lib/techniques";
import { dishEmoji } from "../src/components/art";
import { rescueFor } from "../src/lib/rescue";
import { GLOSSAIRE, termsIn } from "../src/lib/glossaire";
import { PARCOURS } from "../src/lib/parcours";
import { substitutOf } from "../src/lib/substituts";
import { RESTES, buildMenu, ideasFor, restesOfRecipe, resteStatus } from "../src/lib/restes";
import { RAYONS, RATTRAPAGES, choixOf } from "../src/lib/marche";
import { ADOUCI, defaultPortions, householdPortions, kidFriendly, starchOf, weekBalance, isRich } from "../src/lib/famille";
import { DEJA, PANIERS, piqueNique } from "../src/lib/piquenique";
import { equipmentNotes } from "../src/lib/equipement";
import { backupDue } from "../src/lib/store";
import { composeMenus } from "../src/lib/menu";
import { isBigDish } from "../src/lib/planner";
import { balanceOf, finishFor } from "../src/lib/dressage";
import { cuesIn, saltDose } from "../src/lib/cues";
import { fuzzyRecipes, parseIntents } from "../src/lib/intents";
import etapes from "../src/data/etapes.json";
import imagesCore from "../src/data/images.json";
import credits from "../src/data/credits.json";
import imagesMore from "../src/data/images_more.json";
import { autoPlan, consolidate, prepAhead, proteinOf, weekDays } from "../src/lib/planner";
import { PRIORITE, PROTOCOLE } from "../src/lib/aTester";
import type { Profile, Recipe, RecipeLine, Rule } from "../src/lib/types";
import { ET, IM, IMPORT_LIBRARY, L, LEFT, P, P0, base, check, images, mk, pa, plats } from "./helpers";

const vegShare = plats.filter((r) => evaluate(r).flesh.length === 0).length / plats.length;
console.log("   variété : plats ≤ 30 min", plats.filter((r) => r.active + r.rest <= 30).length, "· végétariens", Math.round(vegShare * 100) + " %", "· brunch", RECIPES.filter((r) => r.cats.includes("brunch")).length, "· Océanie", RECIPES.filter((r) => r.macro === "oceanie").length);
check("63 variété (audit UX 2026-10-16) : ≥ 90 plats en 30 min, ≥ 33 % de plats végétariens, ≥ 20 brunchs, ≥ 20 salades repas, ≥ 12 recettes d'Océanie, France < 45 %",
  plats.filter((r) => r.active + r.rest <= 30).length >= 90 && vegShare >= 0.33 && RECIPES.filter((r) => r.cats.includes("brunch")).length >= 20
  && RECIPES.filter((r) => r.cats.includes("salade")).length >= 20 && RECIPES.filter((r) => r.macro === "oceanie").length >= 12 && RECIPES.filter((r) => r.macro === "france").length / RECIPES.length < 0.45);
check("57 préparation à l'avance : au moins une tâche et des légumes à couper d'un coup", pa.tasks.length >= 1 && pa.veg.length >= 2);

// 65-67 audit du chef (16/10/2026) : classiques manquants, règle D21, ingrédients rares remplaçables
const CLASSIQUES = ["bucatini_amatriciana", "risotto_milanese", "spaghetti_vongole", "vitello_tonnato", "souffle_fromage", "moules_marinieres", "bouchees_reine",
  "wiener_schnitzel", "boeuf_stroganov", "gumbo_poulet", "tourtiere_quebec", "mole_poblano_simple", "moqueca", "gyudon", "tempura_legumes_crevettes", "japchae",
  "poulet_tikka_masala", "massaman_poulet", "tom_yum_crevettes", "couscous_royal", "pastilla_poulet", "tajine_agneau_pruneaux", "fesenjan", "dolma_riz",
  "canard_laque_four", "apple_pie", "baba_ghanoush", "couscous_sept_legumes", "thali_vegetarien", "egusi_soup"];
const manquants = CLASSIQUES.filter((id) => !RECIPE_BY_ID[id]);
check("65 audit du chef : 30 grands classiques présents, ≤ 10 ingrédients (12 pour un plat de fête, hors sel, poivre et garnitures facultatives) et ≥ 3 étapes (Tome 13 §0)" + (manquants.length ? " — manquent " + manquants.join(",") : ""),
  manquants.length === 0 && CLASSIQUES.every((id) => RECIPE_BY_ID[id].ingredients.filter((l) => !l.optional && !/^(Sel|Poivre)/.test(l.ref ?? "")).length <= (RECIPE_BY_ID[id].fetes.length ? 12 : 10) && RECIPE_BY_ID[id].steps.length >= 3));
const d21 = ["sarmale_boeuf", "dan_dan_noodles", "griot_poulet", "bigos_volaille", "full_english_volaille", "tourtiere_quebec", "zha_jiang_mian", "stamppot_boerenkool",
  "fabada_version", "choucroute_garnie_version", "cocido_madrileno_version", "tripes_caen_version", "pollo_pibil"];
check("66 D21 : les versions des plats où le porc est structurant n'en contiennent pas (porc seulement en option signalée)",
  d21.every((id) => evaluateLines(RECIPE_BY_ID[id].ingredients.filter((l) => !l.optional)).pork === "ok"));
const rares = ["Gochujang", "Galanga", "Pâte de tamarin", "Mirin", "Berbéré", "Mélasse de grenade", "Aji amarillo", "Poivre du Sichuan", "Huile pimentée chinoise",
  "Shichimi togarashi", "Mélange cajun", "Feuille de bananier", "Paneer", "Sumac", "Tomatille / nopal", "Piment scotch bonnet"];
check("67 ingrédients rares : chacun a un substitut de supermarché affiché sur la fiche", rares.every((r) => !!substitutOf(r) && INGREDIENT_NAMES.includes(r)));

// 69-70 cuisine des restes et guide « Bien choisir » (16/10/2026)
const ideasAll = RESTES.flatMap((r) => r.ideas);
const menuR = buildMenu(["volaille", "riz", "fruits"], P0);
const interdit = /\b(lardons?|porc|bacon|chorizo|vin|rhum|biere|calvados|cidre doux)\b/;
console.log("   restes :", RESTES.length, "types ·", ideasAll.length, "idées ·", ideasAll.filter((i) => i.recipe).length, "liées à une fiche · menu :", menuR.entree?.reste.id, menuR.plat?.reste.id, menuR.dessert?.reste.id);
check("69 restes : fiches liées existantes, ≥ 3 idées par reste, 4 services couverts, menu à 3 restes distincts, végétarien sans chair, riz jeté après 24 h, rien au porc ni à l'alcool",
  ideasAll.every((i) => !i.recipe || !!RECIPE_BY_ID[i.recipe]) && RESTES.every((r) => r.ideas.length >= 3)
  && (["entree", "plat", "sandwich", "dessert"] as const).every((c) => ideasAll.filter((i) => i.course === c).length >= 8)
  && !!menuR.entree && !!menuR.plat && !!menuR.dessert && new Set([menuR.entree.reste.id, menuR.plat.reste.id, menuR.dessert.reste.id]).size === 3
  && RESTES.filter((r) => r.flesh).every((r) => ideasFor(r, { ...P0, vegetarian: true }).length === 0)
  && ideasFor(RESTES.find((r) => r.id === "pain")!, { ...P0, allergens: ["GL"] }).length === 0
  && resteStatus("riz", new Date(Date.now() - 2 * 86400000).toISOString()).level === "jeter"
  && restesOfRecipe(RECIPE_BY_ID["poulet_roti"]).some((x) => x.id === "volaille")
  && ideasAll.every((i) => !interdit.test(norm(`${i.title} ${i.how}`))));
check("70 bien choisir : ingrédients du guide présents au Tome 3, chaque rattrapage de produit animal dit quand jeter, conseil affiché au dictionnaire",
  RAYONS.every((r) => r.items.every((c) => c.refs.every((x) => INGREDIENT_NAMES.includes(x))))
  && RATTRAPAGES.filter((x) => /viande|poisson/.test(x.id)).every((x) => !!x.jeter) && !!choixOf("Avocat") && !!choixOf("Bœuf haché"));

// 68 mijotés longs (audit du chef, suite) : trouvables par « mijoté », tripes en version sans alcool, autocuiseur indiqué
const mij = parseIntents("un plat mijoté");
const mijotes = RECIPES.filter((r) => mij.intents.every((i) => i.test(r)));
console.log("   mijotés :", mijotes.length, "· végétariens", mijotes.filter((r) => evaluate(r).flesh.length === 0).length,
  "· manquent", ["tripes_caen_version", "fabada_version", "kuru_fasulye"].filter((id) => !mijotes.some((r) => r.id === id)).join(",") || "aucun");
check("68 mijotés : « mijoté » trouve au moins 40 plats dont les tripes, la fabada et des mijotés végétariens ; tripes sans alcool ; autocuiseur indiqué",
  mij.intents.some((i) => i.id === "mijote") && mijotes.length >= 40 && ["tripes_caen_version", "fabada_version", "kuru_fasulye"].every((id) => mijotes.some((r) => r.id === id))
  && evaluate(RECIPE_BY_ID["tripes_caen_version"]).alcohol === "ok" && RECIPE_BY_ID["fabada_version"].tips.some((t) => /Autocuiseur/.test(t)));

// 71-75 audit famille (16/10/2026) et pique-nique
const fam: Profile = { noPork: false, alcohol: "allowed", strict: false, vegetarian: false, allergens: [], adult: true, kidsAge: 4, equipment: ["four", "plaques", "poele", "casserole", "mixeur"], onboarded: true, household: { adults: 2, kids: [4, 9] } };
const famDays = weekDays(0, new Date("2026-10-16T12:00:00"));
let spicy = 0, adultOnly = 0, worstStarch = 0, rich = 0, fishW = 0, legW = 0, mealsN = 0;
for (let sd = 1; sd <= 20; sd++) {
  const pl = autoPlan(famDays, {}, { slots: ["midi", "soir"], weekdayMax: 45, zone: "nord", profile: fam, leftovers: LEFT, seed: sd * 7919 });
  const rs = famDays.flatMap((d) => [pl[d]?.midi, pl[d]?.soir]).filter(Boolean).map((id) => RECIPE_BY_ID[id!]);
  mealsN += rs.length;
  spicy += rs.filter((r) => r.profile.includes("epice") && !ADOUCI.test(norm(r.kids))).length;
  adultOnly += rs.filter((r) => r.age === null || r.age > 4).length;
  const b = weekBalance(rs);
  worstStarch = Math.max(worstStarch, ...Object.entries(b.starches).filter(([k]) => k !== "légumineuses").map(([, n]) => n));
  rich = Math.max(rich, rs.filter(isRich).length); fishW += b.fish; legW += b.legumes;
}
console.log("   famille :", mealsN, "repas ·", spicy, "épicés ·", adultOnly, "d'adulte · féculent max", worstStarch, "· riches max", rich, "· poisson/sem", (fishW / 20).toFixed(1), "· légumineuses/sem", (legW / 20).toFixed(1));
check("71 semaine famille (enfant de 4 ans) : rien d'épicé sans adaptation ni de plat d'adulte, au plus 1 plat très riche, féculent au plus 5 fois sur 14, poisson et légumineuses près de 2 fois",
  spicy === 0 && adultOnly === 0 && rich <= 1 && worstStarch <= 5 && fishW / 20 >= 1.5 && legW / 20 >= 1.5);
check("72 foyer : 2 adultes + enfants de 4 et 9 ans = 3 parts ; un plat s'ouvre sur 3 parts, un gâteau garde sa recette ; jours à venir uniquement",
  householdPortions(fam) === 3 && defaultPortions(RECIPE_BY_ID["hachis_parmentier"], fam) === 3 && defaultPortions(RECIPE_BY_ID["banana_bread"], fam) === RECIPE_BY_ID["banana_bread"].portions
  && famDays[0] === "2026-10-16" && kidFriendly(RECIPE_BY_ID["pates_sauce_legumes_caches"], fam) && !kidFriendly(RECIPE_BY_ID["carpaccio_boeuf"], fam));
const badAge = RECIPES.filter((r) => r.profile.includes("epice") && r.age !== null && r.age <= 5 && !ADOUCI.test(norm(r.kids)));
check("73 âges : aucune fiche épicée marquée « dès 5 ans ou moins » sans dire comment l'adoucir" + (badAge.length ? " — " + badAge.slice(0, 5).map((r) => r.id).join(",") : ""), badAge.length === 0);
const lunch = parseIntents("lunchbox"); const picky = parseIntents("enfant difficile légumes"); const congel = parseIntents("batch cooking");
const vis = (q: ReturnType<typeof parseIntents>) => RECIPES.filter((r) => q.intents.every((i) => i.test(r))).length;
console.log("   recherche parents : lunchbox", vis(lunch), "· légumes cachés", vis(picky), "· congélation", vis(congel));
check("74 recherche de parents : « lunchbox », « enfant difficile légumes », « batch cooking » donnent des recettes ; équipement : notes sans wok et autocuiseur",
  vis(lunch) >= 20 && vis(picky) >= 10 && picky.intents.some((i) => i.id === "caches") && vis(congel) >= 30
  && equipmentNotes(RECIPE_BY_ID["pad_thai"], { ...fam, equipment: ["plaques"] }).some((t) => /wok/.test(t))
  && equipmentNotes(RECIPE_BY_ID["fabada_version"], { ...fam, equipment: ["autocuiseur"] }).some((t) => /autocuiseur/.test(t)));
const pn = piqueNique();
const newPn = RECIPES.filter((r) => r.cats.includes("pique_nique"));
console.log("   pique-nique :", pn.length, "recettes dont", newPn.length, "nouvelles");
check("75 pique-nique : ≥ 20 nouvelles fiches, toutes les fiches et paniers existent, rien à la mayonnaise crue ni au poisson cru, au moins 10 pour les enfants, rappel de sauvegarde actif",
  newPn.length >= 20 && DEJA.every((id) => !!RECIPE_BY_ID[id]) && PANIERS.every((pa) => pa.ids.every((id) => !!RECIPE_BY_ID[id]))
  && pn.every((r) => !r.ingredients.some((l) => l.ref === "SUB:mayonnaise" || l.ref === "Mayonnaise industrielle")) && !pn.some((r) => /sashimi|tartare|ceviche|carpaccio/.test(r.id))
  && pn.filter((r) => r.age !== null && r.age <= 3).length >= 10
  && backupDue({ favorites: ["a", "b", "c"], journal: {}, imports: [], week: {}, menus: [], settings: {} } as never) && !backupDue({ favorites: [], journal: {}, imports: [], week: {}, menus: [], settings: {} } as never));
