// Favoris TikTok du 04/11/2026 (+ vidéos de 2 auteurs ; TikTok bloquait les autres profils ce jour-là) et 4 plats
// végétariens ATLAS jumeaux des favoris carnés. Suite lancée par tests/engine.test.ts (npm test).
import { readFileSync } from "node:fs";
import { RECIPE_BY_ID } from "../src/lib/data";
import { evaluate } from "../src/lib/engine";
import { check } from "./helpers";

type Det = { credit?: { author: string; url: string }[]; videos?: { url: string }[] };
const detail = JSON.parse(readFileSync("src/data/recipes_detail.json", "utf8")) as Record<string, Det>;
const imports = JSON.parse(readFileSync("src/data/imports.json", "utf8")) as { url: string; cat: string }[];

const CREDITED = ["kebab_poulet_pain_maison", "riz_saute_boeuf_asiatique", "orzo_poulet_cajun", "widjila", "crispy_chicken_caesar_burger",
  "ramen_miso_curry_coco_boeuf", "rougag_dajaj", "tartine_sardines_oeufs_mollets", "poulet_croustillant_airfryer", "cheese_naan",
  "mayonnaise_oeufs_durs", "sauce_verte_entrecote", "piment_camerounais", "rillettes_poulet_legeres", "tiramisu_creme_brulee",
  "chocolat_chaud_italien", "hot_honey_chicken_burger", "frites_chargees_poulet", "carrot_cake_mascarpone"];
const VEG_TWINS = ["orzo_one_pot_tomates_feta", "burger_halloumi_croustillant", "ramen_miso_legumes_tofu", "kebab_chou_fleur_epice", "frites_chargees_haricots"];

// —— 108 : fiches créditées présentes, jumeaux végétariens vraiment sans viande ni poisson
const missing = CREDITED.filter((id) => !RECIPE_BY_ID[id] || !detail[id]?.credit?.length);
const notVeg = VEG_TWINS.filter((id) => !RECIPE_BY_ID[id] || RECIPE_BY_ID[id].role !== "plat" || evaluate(RECIPE_BY_ID[id]).flesh.length > 0);
const newPlats = [...CREDITED, ...VEG_TWINS].map((id) => RECIPE_BY_ID[id]).filter((r) => r?.role === "plat");
const vegCount = newPlats.filter((r) => evaluate(r).flesh.length === 0).length;
console.log("   favoris du 04/11 :", CREDITED.length, "fiches créditées ·", newPlats.length, "plats dont", vegCount, "végétariens · manquantes :", [...missing, ...notVeg].join(", ") || "aucune");
check("108 favoris du 04/11 : 19 fiches créditées et 5 plats végétariens jumeaux des plats carnés",
  missing.length === 0 && notVeg.length === 0 && vegCount >= 5);

// —— 109 : chaque vidéo d'origine est dans la bibliothèque et rangée avec sa fiche (jamais dans « À vérifier »)
const byUrl = new Map(imports.map((i) => [i.url, i.cat]));
const origin = CREDITED.flatMap((id) => detail[id].credit!.map((c) => c.url));
const absent = origin.filter((u) => !byUrl.has(u));
const vague = origin.filter((u) => byUrl.get(u) === "a_verifier");
console.log("   bibliothèque 04/11 : vidéos d'origine", origin.length, "· absentes", absent.length, "· « À vérifier »", vague.length);
check("109 bibliothèque : les vidéos d'origine des fiches du 04/11 y sont toutes, aucune dans « À vérifier »", absent.length === 0 && vague.length === 0);
