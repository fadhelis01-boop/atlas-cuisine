// Audit gourmet : étalons, accompagnements, fêtes, planificateur, protéines, acidité, vocabulaire, photos (tests 76 et suivants)
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


// 76-82 audit gourmet (21/10/2026)
const ETALONS = ["blanquette_veau", "coq_au_vin", "pot_au_feu", "daube_provencale", "navarin_agneau", "poule_au_pot", "hachis_parmentier", "gigot_sept_heures", "tartiflette",
  "cassoulet_volaille", "poulet_basquaise", "joues_boeuf_carottes", "souris_agneau", "confit_canard_maison", "bouillabaisse_express", "soupe_oignon", "lapin_moutarde", "sole_meuniere",
  "creme_brulee", "ile_flottante", "tarte_tatin", "baba_savarin", "clafoutis_cerises", "tarte_citron_meringuee", "osso_buco", "lasagnes_bolognaise", "risotto_champignons",
  "cacio_e_pepe", "panna_cotta", "moussaka", "butter_chicken"];
const NOUVELLES = ["riz_nature", "semoule_nature", "pates_nature", "pommes_vapeur", "maquereaux_four_moutarde", "sardines_poelees_persillade", "lieu_croute_herbes",
  "papillotes_poisson_legumes", "merlu_beurre_blanc_poireaux", "potimarron_farci_quinoa", "gratin_celeri_noix", "poelee_panais_pois_chiches", "veloute_topinambour",
  "chou_braise_saucisses", "poires_pochees_vin_epices", "tarte_bourdaloue", "coings_rotis_miel", "mont_blanc_verrines", "paella_valenciana_traditionnelle", "plateau_fromages"];
// une étape « de cuisson » parle de feu, de four ou de temps ; elle doit donner une durée ET un repère des sens
const COOKS = /\b(mijot|fremi|poch|saisi|dore|dorer|rotir|rotis|braise|grill|gratin|frire|frit|cuire|cuis|cuit|cuites|bouillir|ebullition|reduire|reduite|caramelis|vapeur|poele|four)/;
const NOT_COOK = /^\W*(servir|monter|preparer|egrener|garnir|fermer|conserver|saler|rincer|verifier|plat|pommes|legumes|choisir|disposer|accompagner|temperer|couper|trancher|badigeonner|parer|farce|farcir|marin|egoutter|vermicelles|creme de|infuser|reposer|refroidir|froid|prendre|couler|finir|lier|napper|demouler|tasser|melanger|griller les|pain)/;
const REPERE = /dore|croustill|fondant|nappe|translucide|tendre|brillant|epais|°c|se detache|cede|lisse|gonfl|opaque|blond|brun|colore|reduit|sirupeux|ferme|prise?\b|tremble|caramel|odeur|sent|crepite|grille|bulles|bouillonn|fond|ambre|nacre|s.ecrase|cuillere|resistance|entier|jus clair|noisette|mousse|ondule|sillon|perle|rubis|rose|souple|sable|pics|bec|clair|fremi|goute|gout|brulant|absorbe|disparu|trous|sec\b|seche|tiede|chaud|couleur|sombre|evapor|sans color|colle|elastique|reduit|epaissi|ambr|cuites? a|al dente|cœur|coeur|ferme/;
const DUREE = /\d+\s*(?:à\s*\d+\s*)?(?:min|h)\b|\d+\s*s\b|une nuit|toute la nuit/;
const weakSteps = (ids: string[]) => ids.flatMap((id) => RECIPE_BY_ID[id].steps.filter((st) => COOKS.test(norm(st)) && !NOT_COOK.test(norm(st)) && !(DUREE.test(st) && REPERE.test(norm(st)))).map((st) => `${id}: ${st.slice(0, 90)}`));
const weakE = weakSteps(ETALONS), weakN = weakSteps(NOUVELLES);
console.log("   étalons :", ETALONS.length, "· étapes de cuisson sans durée ou sans repère :", weakE.length + weakN.length); for (const w of weakE.concat(weakN)) console.log("      ·", w);
check("76 classiques réécrits au niveau étalon : ≥ 4 étapes, une astuce au moins, chaque étape de cuisson a une durée et un repère ; idem pour les nouvelles fiches",
  ETALONS.every((id) => RECIPE_BY_ID[id] && RECIPE_BY_ID[id].steps.length >= 4 && RECIPE_BY_ID[id].tips.length >= 1 && RECIPE_BY_ID[id].steps.join(" ").length >= 450)
  && NOUVELLES.every((id) => !!RECIPE_BY_ID[id]) && weakE.length === 0 && weakN.length === 0);

// ingrédients cités dans les étapes mais absents de la liste (sous-recettes comprises)
const OMIS: [string, RegExp][] = [["persil", /persil/], ["ciboulette", /ciboulette/], ["coriandre", /coriandre/], ["basilic", /basilic/], ["menthe", /menthe/], ["aneth", /aneth/],
  ["citron", /citron|lime/], ["sucre", /sucre|miel|sirop|cassonade|vergeoise/], ["ail", /\bail\b|ail \(/], ["gingembre", /gingembre/], ["cebette", /cebette|oignon nouveau/],
  ["beurre", /beurre|ghee/], ["parmesan", /parmesan|grana/], ["echalote", /echalote/], ["muscade", /muscade/], ["cannelle", /cannelle/], ["cumin", /cumin/], ["thym", /thym/], ["laurier", /laurier|bouquet garni/]];
const FIGURE: Record<string, string> = { soupe_oignon: "sucre", potimarron_farci_quinoa: "beurre", mont_blanc_verrines: "beurre" };
const linesDeep = (r: Recipe, d = 0): string => r.ingredients.map((l) => (l.ref?.startsWith("SUB:") && d < 2 && RECIPE_BY_ID[l.ref.slice(4)] ? linesDeep(RECIPE_BY_ID[l.ref.slice(4)], d + 1) : `${l.ref ?? ""} ${l.label}`)).join(" ");
const omis = RECIPES.flatMap((r) => {
  const st = norm(r.steps.join(" ")); const have = norm(linesDeep(r));
  return OMIS.filter(([w, rx]) => new RegExp(`\\b${w}s?\\b`).test(st) && !rx.test(have) && FIGURE[r.id] !== w
    && !(w === "beurre" && /beurre (noisette|de |d.)/.test(st)) && !(w === "citron" && /citron vert/.test(st) && /citron vert|lime/.test(have))).map(([w]) => `${r.id}:${w}`);
});
console.log("   ingrédients oubliés dans les listes :", omis.length, omis.slice(0, 6).join(", "));
check("77 aucune fiche n'utilise dans ses étapes un ingrédient courant absent de sa liste (persil, sucre, ail, beurre, citron…)", omis.length === 0);

const withSide = RECIPES.filter((r) => r.role === "plat" && r.side);
const blanqShop = consolidate([{ id: "blanquette_veau", factor: 1 }]);
console.log("   accompagnements reliés :", withSide.length, "plats · blanquette → courses avec", blanqShop.some((l) => /Riz/.test(l.ref)) ? "riz" : "SANS riz");
check("78 accompagnements : au moins 100 plats reliés à une fiche ou à un produit, tous existants, et ils rejoignent les courses",
  withSide.length >= 100 && withSide.every((r) => r.side!.startsWith("achat:") ? INGREDIENT_NAMES.includes(r.side!.slice(6)) : !!RECIPE_BY_ID[r.side!])
  && blanqShop.some((l) => /Riz/.test(l.ref)) && consolidate([{ id: "tartiflette", factor: 1 }]).some((l) => /Salade/.test(l.ref)));

// menus de fête
const anchors = ["boeuf_bourguignon", "blanquette_veau", "couscous_royal", "pad_thai", "tartiflette", "risotto_champignons", "poulet_roti", "tajine_agneau_pruneaux"];
const menus = anchors.map((a) => composeMenus(a, P0));
const desserts = menus.flat().map((m) => m.courses.find((c) => c.role === "dessert")?.recipe).filter(Boolean) as Recipe[];
const breakfastDessert = desserts.filter((d) => d.cats.includes("brunch") || /bircher|muesli|porridge|granola|smoothie|chia/.test(norm(d.title)));
const dupWithin = menus.filter((ms) => new Set(ms.map((m) => m.courses.find((c) => c.role === "dessert")?.recipe.id)).size < ms.length).length;
const maxSame = Math.max(...[...desserts.reduce((m, d) => m.set(d.id, (m.get(d.id) ?? 0) + 1), new Map<string, number>()).values()]);
const cheese = menus.flat().filter((m) => m.courses.some((c) => c.recipe.id === "plateau_fromages"));
const starchy = menus.flat().filter((m) => { const e = m.courses.find((c) => c.role === "entree")?.recipe; const pl = m.courses.find((c) => c.role === "plat")?.recipe; return e && pl && starchOf(e) && starchOf(pl) && starchOf(e) !== "légumineuses"; });
console.log("   menus de fête :", desserts.length, "desserts · petit-déjeuner", breakfastDessert.length, "· même dessert au plus", maxSame, "fois · fromage dans", cheese.length, "menus · féculent sur féculent", starchy.length);
check("79 menus de fête : jamais de petit-déjeuner en dessert, 3 desserts différents par plat, un même dessert au plus 3 fois sur 24, fromage dans les menus français classiques, pas de féculent sur féculent",
  breakfastDessert.length === 0 && dupWithin === 0 && maxSame <= 3 && cheese.length >= 4 && starchy.length === 0
  && composeMenus("blanquette_veau", P0)[0].courses.map((c) => c.role).join(",") === "entree,plat,autre,dessert");

// planificateur sur 26 semaines avec sa mémoire
const hist: Record<string, string> = {}; const freqW = new Map<string, number>(); let bigTwice = 0, satBad = 0, sunMenus = 0, sundays = 0;
for (let w = 0; w < 26; w++) {
  const ds = weekDays(0, new Date(Date.UTC(2026, 0, 5 + w * 7, 12)));
  const first = new Date(`${ds[0]}T12:00:00`).getTime();
  const recent = new Set(Object.entries(hist).filter(([, d]) => first - new Date(`${d}T12:00:00`).getTime() < 56 * 86400000).map(([id]) => id));
  const pl = autoPlan(ds, {}, { slots: ["midi", "soir"], weekdayMax: 45, zone: "nord", profile: P0, leftovers: LEFT, seed: 7919 * (w + 1), recent, sundayMenu: true });
  for (const d of ds) {
    const dow = new Date(`${d}T12:00:00`).getDay();
    const ids = [pl[d]?.midi, pl[d]?.soir].filter(Boolean) as string[];
    for (const id of ids) { freqW.set(id, (freqW.get(id) ?? 0) + 1); hist[id] = d; }
    if ((dow === 0 || dow === 6) && ids.filter((id) => isBigDish(RECIPE_BY_ID[id])).length > 1) bigTwice++;
    if (dow === 6 && pl[d]?.midi) { const r = RECIPE_BY_ID[pl[d]!.midi!]; if (!(r.cats.includes("brunch") || r.active + r.rest <= 30)) satBad++; }
    if (dow === 0) { sundays++; if (pl[d]?.entree && pl[d]?.dessert) sunMenus++; }
  }
}
const maxW = Math.max(...freqW.values());
console.log("   semaines (26, avec mémoire) :", freqW.size, "plats distincts · plat le plus fréquent", maxW, "fois · deux grands plats le même jour", bigTwice, "· samedi midi long", satBad, "· menus du dimanche", sunMenus + "/" + sundays);
console.log("   à tester en priorité :", JSON.stringify([...freqW].sort((a, b) => b[1] - a[1]).slice(0, 30).map(([id]) => id)));
check("80 semaine variée sur 6 mois : ≥ 180 plats différents, aucun plus de 7 fois, un seul grand plat par jour de week-end, samedi midi rapide ou brunch, menu complet chaque dimanche",
  freqW.size >= 180 && maxW <= 7 && bigTwice === 0 && satBad === 0 && sunMenus === sundays);

check("81 D21 et authenticité : osso buco et gigot de sept heures avec leur vin blanc et une variante sans alcool ; la vraie paella valenciana (poulet, lapin) existe",
  ["osso_buco", "gigot_sept_heures"].every((id) => RECIPE_BY_ID[id].ingredients.some((l) => l.ref === "Vin blanc") && RECIPE_BY_ID[id].variants.some((v) => v.constraints.includes("alcohol")))
  && RECIPE_BY_ID["paella_valenciana_traditionnelle"].ingredients.some((l) => l.ref === "Lapin") && RECIPE_BY_ID["coq_au_vin"].rest >= 180 + 600);

const kidsPlan = autoPlan(weekDays(0, new Date("2026-10-19T12:00:00")), {}, { slots: ["soir"], weekdayMax: 45, zone: "nord", profile: P0, leftovers: LEFT, seed: 3, kidsVerdict: { moules_frites: "non", shakshuka: "non" } });
check("82 carnet « les enfants n'ont pas aimé » : le plat ne revient plus dans la semaine", !Object.values(kidsPlan).some((d) => d.soir === "moules_frites" || d.soir === "shakshuka"));


// recommandation 10 : protocole d'essai, d'abord les plats les plus proposés par « Ma semaine »
const top45 = new Set([...freqW].sort((a, b) => b[1] - a[1]).slice(0, 45).map(([id]) => id));
const inTop = PRIORITE.filter((id) => top45.has(id)).length;
console.log("   à tester en priorité :", PRIORITE.length, "plats ·", inTop, "parmi les 45 plus proposés de la simulation · protocole en", PROTOCOLE.length, "points");
check("83 à tester en priorité : 30 plats existants, distincts, qui restent parmi les plus proposés par le planificateur (sinon régénérer la liste)",
  PRIORITE.length === 30 && new Set(PRIORITE).size === 30 && PRIORITE.every((id) => RECIPE_BY_ID[id]?.role === "plat") && inTop >= 22 && PROTOCOLE.length >= 5);

// —— points ouverts de l'audit gourmet, réglés le 21/10/2026 ——
// protéines : estimation par part (accompagnement compris), portions chiches relevées, repère qui dit quoi ajouter
const platsG = RECIPES.filter((r) => r.role === "plat");
const withProt = platsG.filter((r) => r.prot != null);
const sortedP = withProt.map((r) => r.prot!).sort((a, b) => a - b); const medP = sortedP[Math.floor(sortedP.length / 2)];
const RELEVES = ["salade_piemontaise", "tartines_sardines_citron", "tempura_legumes_crevettes", "tagliatelles_saumon_citron", "salade_lentilles_saumon_fume", "croque_poulet_pesto",
  "japchae", "nouilles_sautees_boeuf", "lasagnes_bolognaise", "riz_saute_ananas", "yaki_udon", "kottu_roti", "pastitsio", "cornish_pasty", "tahchin", "riz_cantonais", "chou_braise_saucisses"];
const light = withProt.filter((r) => r.prot! < 15);
const hintOk = withProt.every((r) => { const b = balanceOf(r) ?? ""; return b.includes(`environ ${r.prot} g`) && (r.prot! >= 15 || (/léger/.test(b) && /un œuf/.test(b))); });
console.log("   protéines : médiane", medP, "g par part ·", light.length, "plats légers, avec quoi ajouter · portions relevées :", RELEVES.map((id) => `${id} ${RECIPE_BY_ID[id].prot}`).slice(0, 4).join(", "), "…");
check("84 protéines : chaque plat chiffré (sauf ceux comptés à la pièce), médiane ≥ 20 g, portions chiches relevées à ≥ 15 g, le repère d'équilibre donne la valeur et quoi ajouter quand c'est léger",
  withProt.length >= platsG.length - 10 && medP >= 20 && RELEVES.every((id) => (RECIPE_BY_ID[id].prot ?? 99) >= 15) && hintOk);

// acidité : chaque plat a un élément acide (dans la recette, ses sous-recettes ou à table), sinon la raison écrite de s'en passer
const ACID = /citron|lime|vinaigre|tomate|yaourt|yogourt|cornichon|capre|tamarin|grenade|vin |vin$|vin blanc|vin rouge|cidre|biere|moutarde|creme fraiche|fromage blanc|labneh|kefir|sumac|ponzu|nuoc|kimchi|choucroute|orange|pommes? (?!de terre)|ananas|mangue verte|amchur|pickles|achards|lait ribot|ribot|fermente|miso|worcestershire|ketchup|bbq|barbecue|chutney|agrume|pamplemousse|kiwi|rhubarbe|groseille|cranberr|canneberge|airelle|vermouth|xeres|marsala|pulque|feta|chevre|salsa|tabasco|piment.*vinaigre|sriracha|gochujang|doenjang|rouille|aioli|mayonnaise|kaffir|combava|yuzu|limette|verjus|gari\b|gingembre marine|tzatziki/;
const deepText = (r: Recipe, d = 0): string => r.ingredients.map((l) => (l.ref?.startsWith("SUB:") && d < 2 && RECIPE_BY_ID[l.ref.slice(4)]
  ? deepText(RECIPE_BY_ID[l.ref.slice(4)], d + 1) + " " + RECIPE_BY_ID[l.ref.slice(4)].steps.join(" ") : `${l.ref ?? ""} ${l.label}`)).join(" ");
const flat = platsG.filter((r) => !ACID.test(norm(`${deepText(r)} ${r.steps.join(" ")}`)));
const sansRaison = flat.filter((r) => !r.sansAcide);
const acidAdded = RECIPES.filter((r) => r.acideAjoute);
console.log("   acidité : plats sans élément acide", flat.length, "· sans raison écrite :", sansRaison.length, sansRaison.slice(0, 6).map((r) => r.id).join(", "), "· lentilles :", RECIPE_BY_ID.lentilles_saucisses.steps.at(-1)!.slice(-70));
check("85 acidité : aucun plat sans élément acide ni raison de tradition ; les exceptions restent rares (≤ 20) et expliquées",
  sansRaison.length === 0 && flat.length <= 20 && flat.every((r) => (r.sansAcide ?? "").length > 30)
  && RECIPE_BY_ID.lentilles_saucisses.ingredients.some((l) => /vinaigre/i.test(l.label)) && RECIPE_BY_ID.falafels.ingredients.some((l) => !!l.ref?.startsWith("Tahini"))
  // un filet d'acide ne change pas les badges : ni trace d'alcool, ni allergène ajouté par l'acide choisi
  && acidAdded.length >= 50 && acidAdded.every((r) => { const ing = INGREDIENTS[r.acideAjoute!]; return !!ing && !ing.derivs?.alcohol && !(ing.allergens ?? []).length; }));

// vocabulaire du métier : expliqué à la première apparition dans l'étape (fiche) et dans le lexique
const JARGON: [string, string][] = [["Roux", "bechamel"], ["Mantecare", "risotto_milanese"], ["Singer", "coq_au_vin"], ["À hauteur", "mafe_boeuf"], ["Napper / à la nappe", "blanquette_veau"],
  ["Bouquet garni", "boeuf_bourguignon"], ["Sucs", "boeuf_bourguignon"], ["Paner à l'anglaise", "tonkatsu_poulet"], ["Filmer au contact", "creme_patissiere"]];
const jOk = JARGON.filter(([t, id]) => RECIPE_BY_ID[id] && RECIPE_BY_ID[id].steps.some((st) => termsIn(st).some((x) => x.term === t)));
const glossHits = RECIPES.filter((r) => termsIn(r.steps.join(" ")).length > 0).length;
console.log("   lexique :", GLOSSAIRE.length, "termes · mots du métier expliqués dans l'étape :", jOk.length + "/" + JARGON.length, JARGON.filter((j) => !jOk.includes(j)).map(([t]) => t).join(", "), "· fiches avec au moins un geste expliqué :", glossHits);
check("86 vocabulaire : roux, mantecare, singer, à hauteur, à la nappe… expliqués là où l'étape les emploie ; au moins 85 termes au lexique",
  jOk.length === JARGON.length && GLOSSAIRE.length >= 85 && !termsIn("Sers la glace vanille avec des glaçons").some((t) => /Glacer/.test(t.term)));

// photos des nouvelles fiches : sous licence libre (aucune image générée, D19)
const IMG = images as Record<string, { kind?: string; license?: string }>;
const NEW_PHOTOS = NOUVELLES.filter((id) => IMG[`recette/${id}`]);
console.log("   photos des 20 nouvelles fiches :", NEW_PHOTOS.length, "· sans photo juste :", NOUVELLES.filter((id) => !NEW_PHOTOS.includes(id)).join(", "));
check("87 photos : au moins 17 des 20 nouvelles fiches illustrées par une photo sous licence libre (les autres gardent l'illustration de leur catégorie)",
  NEW_PHOTOS.length >= 17 && NEW_PHOTOS.every((id) => /^CC|domaine public|public domain/i.test((credits as Record<string, { license?: string }>)[`recette/${id}`]?.license ?? "")));
