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

// —— 120 : auteurs des favoris du 10/11 : 16 fiches créditées, 2 jumeaux végétariens, vidéos d'origine dans la bibliothèque
import { IMPORT_LIBRARY } from "./helpers";
const A1110 = ["creme_balsamique_maison", "stracciatella_maison", "beurre_cacahuete_maison", "tuiles_parmesan", "persillade_frigo", "sucre_glace_maison",
  "beignets_fourres_pate_tartiner", "boules_fromage_croustillantes", "poulet_crousty_riz", "onion_rings", "pate_foie_volaille", "boulettes_viande_pommes_de_terre",
  "riz_viande_hachee", "spaghetti_boulettes_poisson", "spaghetti_sautes_crevettes", "boisson_mangue_ananas"];
const T1110 = ["riz_haricots_rouges_legumes", "spaghetti_sautes_legumes_oeufs"];
const libUrls = new Set(IMPORT_LIBRARY.map((i) => i.url));
const miss1110 = A1110.filter((id) => !RECIPE_BY_ID[id]?.credit?.length || !RECIPE_BY_ID[id].credit!.every((c) => libUrls.has(c.url)));
const twinBad = T1110.filter((id) => !RECIPE_BY_ID[id] || evaluate(RECIPE_BY_ID[id]).flesh.length > 0);
console.log("   auteurs du 10/11 :", A1110.length, "fiches créditées · jumeaux végétariens", T1110.length, "· à revoir :", [...miss1110, ...twinBad].join(", ") || "aucune");
check("120 auteurs du 10/11 : 16 fiches créditées avec leurs vidéos dans la bibliothèque, 2 plats végétariens jumeaux", miss1110.length === 0 && twinBad.length === 0);

// —— 121 : index allégé (11/11/2026) : quantités et libellés seulement dans le détail, remis à leur place après chargement
import { readFileSync as rf121 } from "node:fs";
const idx121 = JSON.parse(rf121("src/data/recipes.json", "utf8")) as { id: string; ingredients: unknown[][] }[];
const noLabels = idx121.every((r) => r.ingredients.every((l) => typeof l[1] === "number"));
const blanq = RECIPE_BY_ID.blanquette_veau.ingredients;
const merged = blanq.some((l) => /farine/.test(l.label) && /\d/.test(l.qty)) && RECIPES.every((r) => r.ingredients.every((l) => l.label.length > 0));
console.log("   index sans libellés :", noLabels, "· libellés remis après le détail :", merged, "· café repéré :", RECIPES.filter((r) => r.cafe).map((r) => r.id).slice(0, 4).join(", "));
check("121 index allégé : quantités et libellés dans le détail, remis à leur place ; café obligatoire repéré dès le démarrage", noLabels && merged && !!RECIPE_BY_ID.tiramisu.cafe);

// 122 retour d'usage 12/11/2026 : « pâte brisée » donnait deux idées, puis plus rien. Le frigo propose maintenant les
// recettes à plus de 4 courses (plus bas), le produit tout prêt vaut la sous-recette maison, les doublons du référentiel
// se reconnaissent, et les mêmes ingrédients ailleurs dans ATLAS prennent le relais quand le service est épuisé.
import { rankFor as rf122, rankElsewhere as re122, pickIdeas as pi122 } from "../src/lib/frigo";
import { findIngredients as fi122 } from "../src/lib/ingredientSearch";
import { STAPLES as st122 } from "../src/lib/engine";
const o122 = (have: string[]) => ({ have, pantry: new Set(st122), maxMinutes: 0 });
const pb = o122(["Pâte brisée / sablée (prête)"]);
const nPb = rf122(RECIPES, "plat", pb).length + rf122(RECIPES, "dessert", pb).length;
const quiche = rf122(RECIPES, "plat", pb).some((x) => x.r.ingredients.some((l) => l.ref === "SUB:pate_brisee"));
const nBoeuf = rf122(RECIPES, "plat", o122(["Bœuf haché"])).length;
const gombo = rf122(RECIPES, "plat", o122(["Gombo"])).length >= rf122(RECIPES, "plat", o122(["Gombo (okra)"])).length - 1;
// tout voir puis « D'autres idées » : la liste du service s'épuise, l'élargissement a encore des idées
const rk = rf122(RECIPES, "plat", pb);
const allSeen = new Set(rk.map((x) => x.r.id));
const exhaustedEmpty = pi122(rk, 6, 1, allSeen).length === 0 && re122(RECIPES, "plat", pb).length >= 6;
const search122 = fi122("crevettes")[0] === "Crevettes (cuites/crues)" && fi122("saumon")[0] === "Saumon (frais, pavé)" && fi122("pâte brisée")[0] === "Pâte brisée / sablée (prête)";
console.log("   frigo : pâte brisée", nPb, "idées (plat + dessert) · bœuf haché", nBoeuf, "plats · ailleurs", re122(RECIPES, "plat", pb).length, "· recherche", fi122("crevettes")[0]);
check("122 frigo : ≥ 15 idées avec une pâte brisée toute prête (dont les fiches à pâte maison), ≥ 30 plats au bœuf haché, "
  + "doublons du référentiel reconnus, élargissement quand le service est épuisé, produit frais avant le transformé",
  nPb >= 15 && quiche && nBoeuf >= 30 && gombo && exhaustedEmpty && search122);

// 123 audit « fin gourmet, cuisine française » (12/11/2026) : les classiques, les fonds et sauces dérivées, le gibier et
// les abats, la grande pâtisserie ; les classiques régionaux au niveau étalon ; un accord régional pour chaque plat de
// terroir ; des régions unifiées ; les gestes de la cuisine classique au lexique.
import detail123 from "../src/data/recipes_detail.json";
import { mergeDetails as md123 } from "../src/lib/data";
import { GLOSSAIRE as G123 } from "../src/lib/glossaire";
md123(detail123 as never);
const FG_IDS = ["steak_au_poivre", "canard_orange", "tete_de_veau_gribiche", "pate_en_croute", "foie_gras_mi_cuit", "pommes_dauphine", "pommes_anna", "pommes_boulangere",
  "fond_brun_veau", "fond_blanc_volaille", "fumet_poisson", "court_bouillon", "sauce_mornay", "sauce_bordelaise", "sauce_choron", "sauce_ravigote", "sauce_soubise", "sauce_poivrade",
  "ris_de_veau_morilles", "rognons_veau_moutarde", "foie_veau_persillade", "civet_chevreuil", "pigeon_petits_pois", "raie_beurre_noisette_capres", "truite_amandes",
  "maquereaux_vin_blanc", "homard_grille_beurre", "langoustines_mayonnaise", "pate_a_choux", "religieuse_chocolat", "saint_honore", "opera", "peche_melba", "vacherin_glace", "pain_aux_raisins",
  "civet_lievre", "daube_sanglier", "lievre_royale", "plateau_fruits_de_mer", "pithiviers_amandes", "sauce_diable", "sauce_charcutiere"];
const missing123 = FG_IDS.filter((id) => !RECIPE_BY_ID[id]);
const ETALONS_FG = ["moules_marinieres", "sole_normande", "bouchees_reine", "blanquette_poulet", "baeckeoffe_volaille", "pissaladiere", "quenelles_nantua_simple", "croque_monsieur", "saint_jacques_poelees"];
const shortFG = ETALONS_FG.filter((id) => (RECIPE_BY_ID[id]?.steps.length ?? 0) < 4)
  .concat(RECIPES.filter((r) => r.macro === "france" && ["plat", "entree", "dessert"].includes(r.role) && ["Plat", "Entrée", "Dessert"].includes(r.kind) && r.steps.length < 4).map((r) => r.id)); // plats, entrées et desserts du quotidien aussi (12/11)
const terroir = RECIPES.filter((r) => r.macro === "france" && r.role === "plat" && !/enfants|quotidien|Anti-gaspi|Food fusion/.test(r.regionPath.join(" ")));
const sansAccord = terroir.filter((r) => !r.drinksAlcohol.length || !r.drinksNoAlcohol.length);
const sansAstuceFR = RECIPES.filter((r) => r.macro === "france" && !r.tips.length).map((r) => r.id); // 12/11 : une astuce par fiche française
const regionsFR = new Set(RECIPES.filter((r) => r.macro === "france").map((r) => r.regionPath[1] ?? "—"));
const termsFG = ["Monter au beurre", "Chinoiser", "Fumet", "Meunière", "Luter"].every((t) => G123.some((g) => g.term === t));
console.log("   fin gourmet : classiques manquants", missing123.length, "· étalons courts", shortFG.join(",") || 0, "· plats de terroir sans accord", sansAccord.length, "/", terroir.length,
  "· régions FR", regionsFR.size, "· fiches FR sans astuce", sansAstuceFR.length);
check("123 fin gourmet : classiques, fonds et sauces, gibier et abats, grande pâtisserie présents ; classiques régionaux en ≥ 4 étapes ; accord régional sur chaque plat de terroir ; régions unifiées ; gestes au lexique",
  !missing123.length && !shortFG.length && !sansAccord.length && !regionsFR.has("Bourgogne") && !regionsFR.has("Franche-Comté") && !regionsFR.has("—") && termsFG && !sansAstuceFR.length);

// 124 audit « chef professionnel senior » (12/11/2026) : la volaille et la viande hachée cuites vite ont un repère à cœur
// chiffré ; pas de faux repère sur le magret, le boudin ou le poulet déjà cuit ; amidon de blé = gluten ; fours et fritures
// chiffrés ; pas de pesées au bol dans une recette.
import { evaluate as ev124 } from "../src/lib/engine";
const core124 = ["souvlaki_poulet", "burger_maison", "escalopes_dinde_champignons", "gyoza", "tacos_al_pastor"].every((id) => RECIPE_BY_ID[id].steps.some((s) => /(74|70) °C/.test(s)));
const noFalse124 = ["magret_cerises", "boudin_noir_pommes", "croque_poulet_pesto", "soupe_alphabet"].every((id) => !RECIPE_BY_ID[id].steps.some((s) => /Volaille cuite à cœur|Viande hachée : 70|Saucisses et porc cuits/.test(s)));
const gluten124 = ev124(RECIPE_BY_ID.ha_kao).allergens.has("GL");
const oven124 = /250 à 280 °C/.test(RECIPE_BY_ID.pizza_margherita.steps.join(" ")) && /170 °C/.test(RECIPE_BY_ID.kelewele.steps.join(" "));
const bol124 = RECIPES.filter((r) => r.ingredients.some((l) => /^\d+(\/\d+)? bols?$/.test(l.qty.trim()) && /^(Farine|Sucre|Riz|Fécule|Semoule)/.test(l.ref ?? "")));
console.log("   chef pro : repères à cœur", core124, "· sans faux repère", noFalse124, "· gluten ha kao", gluten124, "· fours chiffrés", oven124, "· pesées au bol", bol124.map((r) => r.id).join(",") || 0);
check("124 chef pro : cuisson à cœur chiffrée pour la volaille et la viande hachée, sans faux repère ; amidon de blé = gluten ; fours et fritures chiffrés ; pas de pesée au bol",
  core124 && noFalse124 && gluten124 && oven124 && !bol124.length);

// 125 audit « cuisinier senior, cuisines d'Asie » (12/11/2026, bible/AUDIT_CUISINE_ASIATIQUE_2026-11-12.md) : classiques
// de chaque pays présents, pas de faux végétarien (sauce de poisson, dashi à la bonite), riz rincé, wok fumant, régions
// rangées, fiches techniques d'Asie, une boisson conseillée sur chaque plat d'Asie.
import { TECHNIQUES as T125, techniqueFor as tf125 } from "../src/lib/techniques";
const ASIE_IDS = ["xiao_long_bao", "hong_shao_rou", "agneau_cumin_xinjiang", "mantou", "dan_tat", "takoyaki", "sukiyaki", "yakisoba", "dorayaki", "agedashi_tofu",
  "samgyetang", "jajangmyeon", "doenjang_jjigae", "hotteok", "buuz", "vindaloo", "khichdi", "poha", "rava_idli", "vada_pav", "pani_puri", "rasam", "kulfi", "jalebi",
  "dal_bhat", "momo_legumes", "thukpa", "shorshe_maach", "panang_poulet", "gai_yang", "com_tam", "bun_bo_hue", "cha_ca_hanoi", "char_kway_teow", "kaya_toast", "mohinga", "lagman", "nasu_dengaku",
  "teh_tarik", "cha_yen", "ca_phe_sua_da", "boricha"];
const missing125 = ASIE_IDS.filter((id) => !RECIPE_BY_ID[id]);
const asie125 = RECIPES.filter((r) => /^asie/.test(r.macro));
const FISH125 = /Sauce de poisson|Dashi|Bonite|Pâte de crevettes|Crevettes séchées|Anchois|Fumet/;
const fauxVeg125 = RECIPES.filter((r) => r.cats.includes("vegetarien") && r.ingredients.some((l) => !l.optional && FISH125.test(l.ref ?? ""))).map((r) => r.id);
const curry125 = RECIPES.filter((r) => r.cats.includes("vegetarien") && r.ingredients.some((l) => /Pâte de curry/.test(l.ref ?? "") && !/sans crevettes/.test(l.label))).map((r) => r.id);
const riz125 = asie125.filter((r) => r.id !== "nam_tok_boeuf" && r.ingredients.some((l) => /Riz rond|Riz gluant/.test(l.ref ?? "") && l.weight >= 2) && !/rinc|lave|eau claire|tremp/.test(norm(r.steps.join(" ")))).map((r) => r.id);
const wok125 = asie125.filter((r) => !/curry|kai_jeow|kadai/.test(r.id) && /wok/.test(norm(r.equipment + " " + r.steps.join(" "))) && !/fum|feu vif|tres chaud|tres vif|feu maximal|feu fort/.test(norm(r.steps.join(" ")))).map((r) => r.id);
const regions125 = [...new Set(asie125.map((r) => r.regionPath.join(" › ")))].filter((p) => /\(|Ouzbékistan/.test(p) && !p.startsWith("Asie centrale") || p === "Asie de l'Est");
const tech125 = ["dashi", "riz-asie", "plier-raviolis", "tadka", "pate-curry", "nouilles-asie", "lacto-fermentation"].every((id) => T125.some((t) => t.id === id)) && tf125("Riz à sushi")?.id === "riz-asie";
const drinks125 = asie125.filter((r) => r.role === "plat" && !r.drinksNoAlcohol.length).map((r) => r.id);
console.log("   cuisines d'Asie : classiques manquants", missing125.join(",") || 0, "· faux végétariens", [...fauxVeg125, ...curry125].join(",") || 0, "· riz non rincé", riz125.join(",") || 0,
  "· wok sans repère", wok125.join(",") || 0, "· régions", regions125.join(",") || 0, "· techniques", tech125, "· plats sans boisson", drinks125.length);
check("125 cuisines d'Asie : classiques présents, aucun faux végétarien, riz rincé ou trempé, wok fumant, régions rangées, fiches techniques d'Asie, une boisson sur chaque plat",
  !missing125.length && !fauxVeg125.length && !curry125.length && !riz125.length && !wok125.length && !regions125.length && tech125 && !drinks125.length);

// 126 (12/11/2026) : recettes asiatiques les plus vues sur TikTok (Cooking with Morgane, Ryuji, Lynja) en fiches créditées
// ou rattachées ; pictogramme « carte du monde » : chaque fiche a un pays (ou un point) qui existe sur la carte.
import VIDS126 from "../src/data/recipe_videos.json";
import WM126 from "../src/data/worldmap.json";
import { origineOf as orig126 } from "../src/lib/origine";
const TT126 = ["poulet_caramelise_viet", "raviolis_sans_pliage_grilles", "boeuf_saute_oeuf", "poulet_sel_poivre", "goong_ob_woon_sen", "niu_rou_bing", "aehobak_jeon",
  "banh_cuon", "oeufs_crevettes_cantonais", "mayonnaise_japonaise", "poulet_caramel_croustillant", "tenshindon", "niku_daikon", "piman_nikuzume", "tanghulu"];
const V126 = VIDS126 as unknown as Record<string, { url: string }[]>;
const tiktok126 = TT126.filter((id) => !RECIPE_BY_ID[id] || !(V126[id] ?? RECIPE_BY_ID[id].videos).some((v) => /tiktok\.com\/@(cooking\.with\.morgane|ryuji_tiktok_|cookingwithlynja)\//.test(v.url)));
const attach126 = ["poulet_general_tao", "nems_poulet", "riz_cantonais", "gyoza", "pad_thai", "karaage", "kulfi"].filter((id) => !(V126[id] ?? []).some((v) => /cooking\.with\.morgane|ryuji_tiktok_|cookingwithlynja/.test(v.url)));
const W126 = WM126 as unknown as { d: Record<string, string>; pts: Record<string, [number, number]> };
const sansCarte126 = RECIPES.filter((r) => { const o = orig126(r, W126.pts); return (!o.countries.length && !o.point) || o.countries.some((c) => !W126.d[c]); }).map((r) => r.id);
const larges126 = RECIPES.filter((r) => orig126(r, W126.pts).wide).length;
const regParen126 = [...new Set(RECIPES.map((r) => r.regionPath.join(" › ")).filter((p) => /\(/.test(p) && !/\(France, Belgique\)|\(RDC\)/.test(p)))];
const pt126 = orig126(RECIPE_BY_ID.xiao_long_bao, W126.pts).point === "Shanghai" && orig126(RECIPE_BY_ID.kouign_amann ?? RECIPE_BY_ID.crepes_froment_sucre, W126.pts).countries[0] === "France";
console.log("   TikTok Asie : fiches sans vidéo créditée", tiktok126.join(",") || 0, "· fiches sans vidéo rattachée", attach126.join(",") || 0,
  "· carte : sans origine", sansCarte126.length, "· régions entières", larges126, "· régions entre parenthèses", regParen126.join(",") || 0, "· points", pt126);
check("126 TikTok Asie (Morgane, Ryuji, Lynja) en fiches et vidéos ; carte d'origine pour chaque fiche, régions rangées",
  !tiktok126.length && !attach126.length && !sansCarte126.length && larges126 <= 10 && !regParen126.length && pt126);
