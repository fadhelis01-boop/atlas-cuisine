// Contenu : vague 2, techniques, vidéos, lexique, mode cuisine, semaine, dressage, sel, photos, intentions (tests 42 à 62)
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


// 42-46 vague 2 (Tome 13) : volume, techniques de chef, condiments, habillage
const v2 = RECIPES.filter((r) => r.source.includes("vague 2"));
check("42 vague 2 : au moins 500 nouvelles fiches, identifiants uniques", v2.length >= 500 && new Set(RECIPES.map((r) => r.id)).size === RECIPES.length);
check("43 techniques : pâtisserie, chocolat, boulangerie, poissons, viandes, œufs et condiments présents",
  ["Pâtisserie française", "Chocolat", "Boulangerie & viennoiserie", "Poissons & fruits de mer", "Viandes & volailles", "Œufs", "Condiments & marinades maison"].every((f) => TECHNIQUES.some((t) => t.family === f)));
console.log("   techniques sans fiche :", [...new Set(v2.flatMap((r) => r.techniques).filter((t) => !techniqueFor(t)))].join(" ; "));
check("44 techniques des fiches de la vague 2 toutes reliées à une fiche technique", v2.every((r) => r.techniques.every((t) => !!techniqueFor(t))));
const viande = TECHNIQUES.find((t) => t.id === "cuisson-viande-rouge");
check("45 repères de sécurité : viande hachée 70 °C, volaille 74 °C", !!viande?.table?.rows.some(([a, b]) => a.includes("hachée") && b.includes("70 °C"))
  && TECHNIQUES.some((t) => t.steps.join(" ").includes("74 °C")));
check("46 condiments maison (bouillon cube, nokoss) présents ; couverture illustrée pour chaque fiche",
  !!RECIPE_BY_ID["bouillon_cube_maison"] && !!RECIPE_BY_ID["nokoss"] && RECIPES.every((r) => dishEmoji(r).length > 0));

// 47-48 chaînes YouTube (Tome 13 §10)
const ytLib = IMPORT_LIBRARY.filter((i) => i.source === "YouTube");
check("47 YouTube : plus de 1 500 vidéos classées, toutes lisibles dans l'appli, 13 chaînes", ytLib.length > 1500 && ytLib.every((i) => /^y[ts]:[\w-]{11}$/.test(i.embed)) && new Set(ytLib.map((i) => i.author)).size === 13);
check("48 Shorts YouTube reconnus et lus en vertical", embedOf("https://www.youtube.com/shorts/gZQa_cAAfus") === "ys:gZQa_cAAfus" && ytLib.some((i) => i.embed.startsWith("ys:")));

// 49-52 aide au débutant (Tome 13 §11)
check("49 rattrapages : pour des éclairs, « les choux sont retombés » vient en premier ; toute fiche salée a au moins 3 conseils",
  rescueFor(RECIPE_BY_ID["eclairs_chocolat"])[0].problem.includes("choux") && RECIPES.filter((r) => r.role === "plat").every((r) => rescueFor(r).length >= 3));
check("50 lexique : « déglace » et « bec d'oiseau » expliqués", termsIn("Déglace au bouillon").some((t) => t.term === "Déglacer") && termsIn("jusqu'au bec d'oiseau").length > 0);
check("51 lexique : chaque terme renvoie à une fiche technique existante", GLOSSAIRE.every((t) => !t.tech || !!TECHNIQUES.find((x) => x.id === t.tech)));
check("52 parcours débutant : 15 étapes, recettes et techniques existantes", PARCOURS.length === 15 && PARCOURS.every((s) => s.recipes.every((id) => !!RECIPE_BY_ID[id]) && s.techs.every((t) => !!TECHNIQUES.find((x) => x.id === t))));

const sp = splitStep("**Choux.** Eau, lait, beurre, sel, sucre à ébullition ; farine d'un coup, dessèche 1 min ; hors du feu, les œufs un à un jusqu'au « bec d'oiseau ».");
console.log("   découpage :", sp.join(" | "), "· gestes/recette :", (RECIPES.reduce((a, r) => a + r.steps.flatMap(splitStep).length, 0) / RECIPES.length).toFixed(1));
check("53 mode cuisine : une étape dense devient plusieurs gestes, titre conservé ",
  sp.length === 3 && sp.every((x) => x.startsWith("**Choux (")) && RECIPES.reduce((a, r) => a + r.steps.flatMap(splitStep).length, 0) / RECIPES.length > 3.3);

// 54-57 planificateur de la semaine (audit 🔴 4)
const wk = weekDays(0, new Date("2026-10-15T12:00:00"));
const noPork: Profile = { noPork: true, alcohol: "none", strict: true, vegetarian: false, allergens: [], adult: true, kidsAge: null, equipment: ["four", "plaques", "poele", "casserole", "mixeur"], onboarded: true };
const wp = autoPlan(wk, {}, { slots: ["midi", "soir"], weekdayMax: 45, zone: "nord", profile: noPork, leftovers: LEFT, seed: 42 });
const ids = wk.flatMap((d) => [wp[d]?.midi, wp[d]?.soir]).filter(Boolean) as string[];
console.log("   semaine :", wk[0], "→", wk[6], "·", ids.slice(0, 4).join(", "), "…");
check("54 semaine : les 7 jours à venir (jamais de jour passé), 14 repas tous différents, tous des plats compatibles avec le profil",
  wk[0] === "2026-10-15" && wk[6] === "2026-10-21" && ids.length === 14 && new Set(ids).size === 14
  && ids.every((i) => RECIPE_BY_ID[i].role === "plat" && verdict(RECIPE_BY_ID[i], noPork).availability !== "hidden"));
check("55 semaine : le soir en semaine reste rapide ; deux repas de suite ont rarement la même protéine animale",
  wk.filter((d) => ![0, 6].includes(new Date(`${d}T12:00:00`).getDay())).every((d) => { const r = RECIPE_BY_ID[wp[d].soir!]; return r.active + r.rest <= 45 || (r.active <= 25 && r.rest <= 60); })
  && ids.slice(1).filter((x, i) => proteinOf(RECIPE_BY_ID[x]) === proteinOf(RECIPE_BY_ID[ids[i]]) && proteinOf(RECIPE_BY_ID[x]) !== "vegetal").length <= 2);
const shopLines = consolidate([{ id: "omelette_fines_herbes", factor: 1 }, { id: "oeufs_cocotte", factor: 2 }]);
const eggs = shopLines.find((l) => l.from.length === 2);
console.log("   courses :", eggs?.label);
check("56 courses regroupées : un produit commun à deux recettes = une seule ligne qui cite les deux", !!eggs && new Set(shopLines.map((l) => l.ref)).size === shopLines.length);
console.log("   à l'avance :", pa.tasks.map((t) => t.recipe).join(", "), "· légumes :", pa.veg.join(", "));
const fin = (id: string) => finishFor(RECIPE_BY_ID[id]).plate;
console.log("   dressage :", fin("tarte_poireaux").slice(0, 40), "|", fin("tarte_tatin").slice(0, 40), "|", fin("lasagnes_bolognaise").slice(0, 40));
check("58 dressage : chaque fiche a une finition ; tarte salée ≠ tarte sucrée ; le salé sans « goûte » reçoit le rappel",
  RECIPES.every((r) => finishFor(r).plate.length > 40) && fin("tarte_poireaux") !== fin("tarte_tatin") && /tiédir/.test(fin("lasagnes_bolognaise"))
  && /couteau/.test(fin("tarte_tatin")) && RECIPES.filter((r) => r.role === "plat").filter((r) => finishFor(r).taste).length > 150 && !finishFor(RECIPE_BY_ID["tarte_tatin"]).taste);
const oc = ovenPlan(RECIPE_BY_ID["gratin_courgettes"].steps.flatMap(splitStep));
console.log("   minuteur :", gestureLabel(sp[1], 2), "· four :", oc?.temp, "à l'étape", (oc?.at ?? -1) + 1, "· équilibre :", balanceOf(RECIPE_BY_ID["omelette_fines_herbes"]));
check("59 minuteurs nommés par le geste ; préchauffage repéré avant d'enfourner ; repère d'équilibre pour chaque plat",
  gestureLabel(sp[1], 2) === "Choux (2/3)" && !!oc && /°C/.test(oc.temp) && RECIPES.filter((r) => r.role === "plat").every((r) => !!balanceOf(r)) && !!TECHNIQUES.find((t) => t.id === "convertir-mesures") && !!TECHNIQUES.find((t) => t.id === "presenter-une-assiette"));
const savory = RECIPES.filter((r) => r.role === "plat" || r.role === "entree");
const withCue = RECIPES.filter((r) => r.steps.some((st) => cuesIn(st).length > 0)).length;
console.log("   sel :", saltDose(RECIPE_BY_ID["kedjenou"])?.text.slice(0, 50), "| pad thaï :", saltDose(RECIPE_BY_ID["pad_thai"])?.grams, "g · repères visuels sur", withCue, "fiches");
check("60 sel dosé : toute fiche salée a soit une ligne de sel, soit un dosage calculé ; moitié moins avec sauce soja ; repères visuels sur plus de la moitié des fiches",
  savory.every((r) => flatten(r.ingredients).some((l) => l.ref?.startsWith("Sel")) || !!saltDose(r)) && saltDose(RECIPE_BY_ID["pad_thai"])!.grams < saltDose(RECIPE_BY_ID["kedjenou"])!.grams
  && cuesIn("Fais suer l'oignon 5 min").some((c) => c.startsWith("Oignon prêt")) && !cuesIn("Enlève la peau").some((c) => c.startsWith("Pousse")) && withCue > RECIPES.length / 2);
check("61 photos de gestes et d'étapes : chaque sujet existe (technique ou recette), chaque photo est traitée en AVIF, légende sans numéro",
  Object.keys(ET).length >= 40 && Object.entries(ET).every(([k, v]) => (k.startsWith("technique/") ? !!TECHNIQUES.find((t) => t.id === k.slice(10)) : !!RECIPE_BY_ID[k.slice(8)]) && v.every((x) => IM[x.k]?.avif && !/^\d/.test(x.c))));
const pi = parseIntents("un dessert facile et pas cher");
const vegFast = RECIPES.filter((r) => parseIntents("végétarien rapide").intents.every((i) => i.test(r)));
console.log("   intentions :", pi.intents.map((i) => i.id).join(","), "| reste « " + pi.rest + " » · végé rapide :", vegFast.length, "· creppe →", fuzzyRecipes(RECIPES, "creppe").slice(0, 2).map((r) => r.id).join(","));
check("62 recherche par intention : « dessert facile pas cher » compris en 3 filtres sans reste ; « creppe » retrouve des crêpes",
  pi.intents.length === 3 && pi.rest === "" && vegFast.length > 5 && fuzzyRecipes(RECIPES, "creppe").some((r) => /crepe/.test(r.id)) && parseIntents("apéro").intents[0]?.id === "apero");
