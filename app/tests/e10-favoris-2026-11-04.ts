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

// —— 110 : vidéos populaires des 14 autres auteurs (lus plus tard le 04/11) : fiches créditées, vidéos rangées avec leur fiche
const AUTEURS = ["pates_poulet_boursin", "tenders_poulet_sauce_canes", "foutou_sauce_graine", "hamburger_helper_maison", "salade_sardines_avocat_herbes",
  "ramen_tom_yum_cremeux_poulet", "pain_charge_cameroun", "pepper_soup_agneau", "poulet_farci_epinards_mozzarella", "couscous_tfaya_boeuf", "pasta_alfredo_poulet",
  "boeuf_wellington_sans_porc", "karantika", "omelette_frites_algerienne", "vermicelles_riz_sautes_legumes", "lo_mein_chou_legumes", "udon_champignons_ail_croustillant",
  "ramen_coreen_champignons_cremeux", "pates_butternut_rotie_ail", "beignets_haricots_bouillie", "felfla", "bricks_poulet_curry_olives", "beignets_crevettes_panes",
  "corn_dog_coreen_pain_mie", "gateau_qui_pleure", "cheesecake_speculoos_verrines", "sfenj", "beignets_banane_cameroun", "sauce_facon_giant", "sauce_facon_big_tasty"];
const VEG_AUTEURS = ["karantika", "omelette_frites_algerienne", "vermicelles_riz_sautes_legumes", "lo_mein_chou_legumes", "udon_champignons_ail_croustillant",
  "ramen_coreen_champignons_cremeux", "pates_butternut_rotie_ail", "beignets_haricots_bouillie"];
const manque = AUTEURS.filter((id) => !RECIPE_BY_ID[id] || !detail[id]?.credit?.length);
const pasVeg = VEG_AUTEURS.filter((id) => RECIPE_BY_ID[id]?.role !== "plat" || evaluate(RECIPE_BY_ID[id]).flesh.length > 0);
const orig2 = AUTEURS.flatMap((id) => detail[id]?.credit?.map((c) => c.url) ?? []);
const mal = orig2.filter((u) => !byUrl.has(u) || byUrl.get(u) === "a_verifier");
console.log("   auteurs du 04/11 :", AUTEURS.length, "fiches ·", VEG_AUTEURS.length, "plats végétariens · vidéos d'origine", orig2.length, "· mal rangées", mal.length, [...manque, ...pasVeg].join(", "));
check("110 auteurs du 04/11 : 30 fiches créditées (dont 8 plats végétariens), vidéos d'origine rangées avec leur fiche", manque.length === 0 && pasVeg.length === 0 && mal.length === 0);

// —— 111 : vidéos hors recette de comptes de cuisine (piscine, restaurant, conseils santé…) jamais publiées
const HORS = ["@lacuisinedes.m.and.ms/video/7506052529042640150", "@lacuisinedes.m.and.ms/video/7488696198107286806", "@totamsachikaroberts/video/7693395788768103693",
  "@simplylemmons/video/7597883531729112351", "@dishcovery_/video/7506262878631005462", "@mohamedcheikh_/video/7577098829535808791"];
const publiees = HORS.filter((p) => byUrl.has("https://www.tiktok.com/" + p));
check("111 vidéos hors recette des comptes de cuisine : absentes de la bibliothèque publiée", publiees.length === 0);
