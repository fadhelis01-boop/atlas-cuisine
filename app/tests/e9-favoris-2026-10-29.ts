// Favoris TikTok du 29/10/2026 et vidéos populaires de leurs auteurs (jamais explorés jusque-là). Suite lancée par
// tests/engine.test.ts (npm test).
import { readFileSync } from "node:fs";
import { RECIPE_BY_ID } from "../src/lib/data";
import { evaluate } from "../src/lib/engine";
import { check } from "./helpers";

type Det = { videos?: { url: string }[]; credit?: { author: string; url: string }[] };
const detail = JSON.parse(readFileSync("src/data/recipes_detail.json", "utf8")) as Record<string, Det>;
const imports = JSON.parse(readFileSync("src/data/imports.json", "utf8")) as { url: string; cat: string; title: string }[];

const NEW = ["cookies_rocher_coeur_noisette", "muffins_double_chocolat_noisette", "lasagnes_montagnardes_raclette", "sauce_gombo_ivoirienne",
  "sandwich_merguez_orientale", "eiersalat", "sauce_curry_mango", "sauce_bourguignonne_fondue", "sirop_citron_maison", "vinaigre_epluchures_pommes",
  "ficelle_picarde_dinde", "potee_chou_version", "hackbraten_alsacien", "salade_boeuf_feta_avocat", "medaillons_courgette_farcis",
  "rouleaux_brick_reblochon_boeuf", "poulet_mayo_ivoirien", "gesiers_sautes_ivoiriens", "garba", "pates_cremeuses_poulet_croustillant",
  "pommes_terre_hache_poele", "gratin_pommes_terre_poulet", "gateau_invisible_courgette_chevre", "pates_mont_dor_champignons",
  "pates_pesto_vert_poireau", "tatin_carottes", "salade_westaf", "fromage_pane_pommes_terre_paprika", "boules_pomme_terre_mozzarella",
  "soupe_froide_concombre_zaatar", "veloute_epluchures_asperges", "smores_cookie_bars", "moelleux_chocolat_poele", "fleurs_pommes_feuilletees",
  "dampfnudeln", "buns_fromage_dinde", "lait_concentre_sucre_maison", "mayonnaise_sans_oeuf", "sirop_fraise_maison"];

// —— 105 : les 39 fiches existent, sont créditées, et les plats végétariens compensent une partie des plats carnés
const missing = NEW.filter((id) => !RECIPE_BY_ID[id] || !detail[id]?.credit?.length);
const plats = NEW.map((id) => RECIPE_BY_ID[id]).filter((r) => r?.role === "plat");
const veg = plats.filter((r) => evaluate(r).flesh.length === 0);
console.log("   favoris du 29/10 :", NEW.length, "fiches ·", plats.length, "plats dont", veg.length, "végétariens · manquantes :", missing.join(", ") || "aucune");
check("105 favoris du 29/10 : 39 fiches créditées, dont au moins 6 plats végétariens",
  missing.length === 0 && veg.length >= 6);

// —— 106 : une vidéo rattachée à une fiche est classée avec la fiche dans la bibliothèque, jamais dans « À vérifier »
const byUrl = new Map(imports.map((i) => [i.url, i.cat]));
const credited = NEW.flatMap((id) => detail[id].credit!.map((c) => c.url)).filter((u) => byUrl.has(u));
const vague = credited.filter((u) => byUrl.get(u) === "a_verifier");
console.log("   bibliothèque : vidéos d'origine des fiches du 29/10 présentes", credited.length, "· encore « À vérifier » :", vague.length);
check("106 bibliothèque : les vidéos d'origine des nouvelles fiches y sont, et aucune n'est rangée dans « À vérifier »",
  credited.length >= 30 && vague.length === 0);

// —— 107 : aucune coordonnée de créateur (téléphone, WhatsApp, courriel) dans les titres de la bibliothèque
const PHONE = /(?:\+33|\b0)[1-9](?:[ .-]?\d{2}){4}\b|whats ?app?\b|\S+@\S+\.\w{2,}/i;
const leaks = imports.filter((i) => PHONE.test(i.title));
console.log("   coordonnées dans les titres de la bibliothèque :", leaks.length);
check("107 bibliothèque : aucun numéro de téléphone, WhatsApp ou courriel de créateur dans les titres publiés", leaks.length === 0);
