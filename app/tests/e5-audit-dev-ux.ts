// Audit développement et UI/UX du 21/10/2026 (bible/AUDIT_DEV_UX_2026-10-21.md) : sécurité, état local, partage,
// démarrage léger, navigation, photos publiées. Suite lancée par tests/engine.test.ts (npm test).
import { readFileSync } from "node:fs";
import { RECIPES, RECIPE_BY_ID, detailsReady } from "../src/lib/data";
import { safeHref, safeUrl, sanitizeState } from "../src/lib/safe";
import { SCHEMA, type State, getState, mergeState, migrate, readBackup, setState } from "../src/lib/store";
import { decodeShare, encodeShare, mergeShopping, mergeWeek, weekToIcs } from "../src/lib/partage";
import { findOrphans } from "../src/lib/orphans";
import { NO_TAB, TABS, cookHref, tabOf } from "../src/lib/nav";
import { installDue } from "../src/lib/install";
import { NOISE } from "../src/lib/errlog";
import { PUBLISHED_AVIF, PUBLISHED_WEBP } from "../src/components/photo";
import { check } from "./helpers";

// —— 88 liens : seuls http et https passent, à l'affichage comme à la restauration
const evil = ["javascript:alert(document.cookie)", " JavaScript:alert(1)", "data:text/html,<script>alert(1)</script>", "vbscript:x", "//evil.example", "file:///etc/passwd"];
console.log("   liens refusés :", evil.filter((u) => safeUrl(u) === null).length + "/" + evil.length, "· https accepté :", safeUrl("https://www.tiktok.com/@a/video/1") !== null);
check("88 sécurité : un lien javascript:, data:, vbscript: ou sans protocole n'est jamais rendu cliquable ; un lien https l'est",
  evil.every((u) => safeUrl(u) === null && safeHref(u) === "#") && safeUrl("https://www.youtube.com/watch?v=x") === "https://www.youtube.com/watch?v=x");

// —— 89 sauvegarde piégée : nettoyée, comptée, jamais acceptée telle quelle
const trap = {
  profile: { noPork: true, alcohol: "<img src=x>", allergens: ["AR", 42], onboarded: true },
  favorites: ["blanquette_veau", "../../etc", "<script>"],
  imports: [{ url: "javascript:alert(1)", title: "piège" }, { url: "https://www.tiktok.com/@chef/video/123", title: "ok", steps: ["a", 3] }],
  recipeVideos: { blanquette_veau: ["javascript:alert(1)", "https://youtu.be/abc"] },
  week: { "2026-10-22": { midi: "blanquette_veau", soir: "<b>x</b>" }, "pas-une-date": { midi: "x" } },
  journal: { blanquette_veau: { rating: 99, note: "trop salé", date: "2026-10-20" } },
};
const { state: clean, report } = sanitizeState(trap);
const cs = clean as Partial<State>;
console.log("   sauvegarde piégée :", JSON.stringify(report.counts), "· écartés", report.dropped);
check("89 restauration : profil typé, favoris et semaine sans identifiant douteux, imports et vidéos sans lien javascript:, note bornée à 5 ; fichier non ATLAS refusé",
  report.ok && cs.profile!.alcohol === "allowed" && cs.profile!.allergens.length === 1 && cs.favorites!.join() === "blanquette_veau"
  && cs.imports!.length === 1 && cs.imports![0].steps.length === 1 && cs.recipeVideos!.blanquette_veau.join() === "https://youtu.be/abc"
  && Object.keys(cs.week!).join() === "2026-10-22" && !cs.week!["2026-10-22"].soir && cs.journal!.blanquette_veau.rating === 5 && report.dropped >= 5
  && !readBackup("{pas du json").report.ok && !readBackup(JSON.stringify({ hello: 1 })).report.ok);

// —— 90 état local : version, migration avec renommage, fusion sans perte, copie à la demande
const v1 = migrate({ favorites: ["ancien_nom", "ratatouille"], journal: { ancien_nom: { rating: 4, note: "", date: "2026-01-01" } }, week: { "2026-10-22": { midi: "ancien_nom" } } } as Partial<State>, { ancien_nom: "blanquette_veau" });
const mine = migrate({ favorites: ["ratatouille"], journal: { ratatouille: { rating: 3, note: "ici", date: "2026-10-20" } }, week: { "2026-10-22": { midi: "pot_au_feu" } },
  shopping: [{ id: "1", ref: null, label: "Lait", from: "", done: false, section: "x" }] } as Partial<State>);
const merged = mergeState(mine, { favorites: ["blanquette_veau"], journal: { ratatouille: { rating: 5, note: "ailleurs", date: "2026-10-21" } },
  week: { "2026-10-22": { midi: "moussaka" }, "2026-10-23": { soir: "moussaka" } }, shopping: [{ id: "2", ref: null, label: "lait", from: "", done: false, section: "x" }, { id: "3", ref: null, label: "Pain", from: "", done: false, section: "x" }] });
const before = getState();
setState((s) => { s.favorites = [...s.favorites, "ratatouille"]; });
const after = getState();
console.log("   état : version", v1.version, "· renommage", v1.favorites.join(","), "· fusion", merged.favorites.join(","), "· courses", merged.shopping.map((x) => x.label).join(","));
check("90 état local : version de schéma posée, recette renommée suivie partout, fusion sans rien perdre (le plus récent gagne, la semaine locale reste), branches non touchées partagées",
  v1.version === SCHEMA && v1.favorites[0] === "blanquette_veau" && !!v1.journal!.blanquette_veau && v1.week!["2026-10-22"].midi === "blanquette_veau"
  && merged.favorites.join() === "ratatouille,blanquette_veau" && merged.journal!.ratatouille.note === "ailleurs" && merged.week!["2026-10-22"].midi === "pot_au_feu"
  && merged.week!["2026-10-23"].soir === "moussaka" && merged.shopping.map((x) => x.label).join() === "Lait,Pain"
  && after.imports === before.imports && after.journal === before.journal && after.favorites !== before.favorites);

// —— 91 partage dans le foyer : lien aller-retour, données reçues vérifiées, fusion polie, agenda valide
const code = await encodeShare({ v: 1, kind: "courses", shopping: [{ label: "200 g de beurre", section: "Crèmerie", ref: "Beurre doux / demi-sel", from: "Ma semaine" }] });
const back = await decodeShare(code);
const weekCode = await encodeShare({ v: 1, kind: "semaine", week: { "2026-10-22": { midi: "blanquette_veau" }, "2026-13-99": { midi: "x" } } });
const backWeek = await decodeShare(weekCode);
const forged = await decodeShare("p" + btoa(JSON.stringify({ v: 1, kind: "semaine", week: { "2026-10-22": { midi: "<script>alert(1)</script>" } } })));
const ms = mergeShopping([{ id: "a", ref: null, label: "200 g de beurre", from: "", done: false, section: "" }], [{ label: "200 g de beurre", section: "", ref: null, from: "" }, { label: "Œufs", section: "", ref: null, from: "" }], () => "n");
const mw = mergeWeek({ "2026-10-22": { midi: "pot_au_feu" } }, { "2026-10-22": { midi: "moussaka", soir: "ratatouille" } });
const ics = weekToIcs({ "2026-10-22": { midi: "blanquette_veau", soir: "ratatouille", entree: "veloute_topinambour" } }, (id) => RECIPE_BY_ID[id]?.title, (id) => `https://x/#/recette/${id}`, new Date("2026-10-21T10:00:00Z"));
console.log("   partage : lien de", code.length, "caractères · semaine", JSON.stringify(backWeek?.week), "· agenda", (ics.match(/BEGIN:VEVENT/g) ?? []).length, "repas");
check("91 partage : la liste et la semaine font l'aller-retour dans un lien, un lien forgé est nettoyé, la fusion n'écrase rien, l'agenda .ics est conforme (CRLF, 2 événements, virgules échappées)",
  code.startsWith("z") && back?.shopping?.[0].label === "200 g de beurre" && JSON.stringify(backWeek?.week) === JSON.stringify({ "2026-10-22": { midi: "blanquette_veau" } })
  && !!forged && Object.keys(forged.week!["2026-10-22"]).length === 0 && (await decodeShare("zpas-du-base64!!")) === null
  && ms.added === 1 && mw.week["2026-10-22"].midi === "pot_au_feu" && mw.week["2026-10-22"].soir === "ratatouille" && mw.added === 1
  && ics.includes("\r\n") && (ics.match(/BEGIN:VEVENT/g) ?? []).length === 2 && /DTSTART:20261022T120000/.test(ics) && ics.replace(/\r\n /g, "").includes("menu : Velouté de topinambours\\, noisettes grillées\\, "));

// —— 92 démarrage léger : l'index ne porte plus le détail des fiches, le détail couvre toutes les fiches
const indexRaw = readFileSync("src/data/recipes.json", "utf8");
const detail = JSON.parse(readFileSync("src/data/recipes_detail.json", "utf8")) as Record<string, { steps: string[] }>;
const budget = readFileSync("scripts/budget.mjs", "utf8").match(/const BUDGET = (\d+)/)?.[1];
console.log("   démarrage : index", (indexRaw.length / 1024).toFixed(0), "Ko sans étapes ·", Object.keys(detail).length, "fiches détaillées · plafond", budget, "Ko compressés");
check("92 démarrage : l'index des recettes n'embarque ni étapes, ni introductions, ni vidéos ; chaque fiche a son détail ; plafond de poids contrôlé au build",
  !/"steps":|"intro":|"videos":|"tips":/.test(indexRaw) && RECIPES.every((r) => detail[r.id]?.steps?.length > 0) && detailsReady() && Number(budget) <= 400);

// —— 93 navigation : chaque écran allume le bon onglet, la semaine a le sien, le profil reste atteignable
const app = readFileSync("src/App.tsx", "utf8");
const routes = [...app.matchAll(/case "([a-z-]*)":/g)].map((m) => m[1]);
const orphanRoutes = routes.filter((r) => !tabOf(r) && !NO_TAB.includes(r) && !["profil", "credits"].includes(r));
console.log("   onglets :", TABS.map((t) => t.label).join(" · "), "· écrans sans onglet :", orphanRoutes.join(",") || "aucun", "· semaine →", tabOf("semaine")?.label, "· restes →", tabOf("restes")?.label);
check("93 navigation : 5 onglets dont « Ma semaine », chaque écran rattaché (sauf fiche et mode cuisine), Restes et Courses sous la semaine, Bien choisir sous le frigo",
  TABS.length === 5 && tabOf("semaine")?.label === "Ma semaine" && tabOf("courses")?.label === "Ma semaine" && tabOf("restes")?.label === "Ma semaine"
  && tabOf("bien-choisir")?.label === "Frigo" && tabOf("pique-nique")?.label === "Explorer" && orphanRoutes.length === 0 && tabOf("recette") === null);

// —— 94 petits défauts réglés : portions transmises au mode cuisine, recettes disparues signalées, invitation à installer, journal sans bruit
const orph = findOrphans(migrate({ favorites: ["blanquette_veau", "fiche_supprimee"], week: { "2026-10-22": { soir: "autre_disparue", midi: "ratatouille" } } } as Partial<State>));
const withData = migrate({ favorites: ["a", "b", "c"] } as Partial<State>);
console.log("   cuisiner :", cookHref("blanquette_veau", 6, false), "· disparues :", orph.join(","));
check("94 finitions : les deux boutons « Cuisiner » gardent les portions, les recettes disparues sont repérées, l'invitation à installer vise l'iPhone non installé avec des données, le journal ignore les échecs de mise à jour hors ligne",
  cookHref("blanquette_veau", 6, false) === "/cuisine/blanquette_veau?portions=6" && cookHref("x", 2, true).endsWith("&adapte=1")
  && orph.sort().join() === "autre_disparue,fiche_supprimee"
  && installDue(withData, true, false) && !installDue(withData, true, true) && !installDue(withData, false, false) && !installDue(migrate({} as Partial<State>), true, false)
  && !installDue({ ...withData, installNudge: new Date().toISOString() }, true, false)
  && NOISE.test("TypeError: Failed to update a ServiceWorker for scope") && !NOISE.test("TypeError: Cannot read properties of undefined"));

// —— 95 publication : photos en AVIF 400/800 + WebP 400, politique de sécurité sans eval ni script en ligne
const vite = readFileSync("vite.config.ts", "utf8");
const csp = vite.match(/export const CSP = \[([\s\S]*?)\]\.join/)?.[1] ?? "";
const prune = readFileSync("scripts/prune-photos.mjs", "utf8");
console.log("   publication : AVIF", PUBLISHED_AVIF.join("/"), "+ WebP", PUBLISHED_WEBP, "· CSP", csp.includes("frame-src") ? "avec lecteurs vidéo limités" : "?");
check("95 publication : tailles publiées cohérentes avec le tri des fichiers, CSP posée au build (script-src 'self', pas d'unsafe-eval, object-src 'none', cadres YouTube nocookie et TikTok seulement)",
  PUBLISHED_AVIF.join() === "400,800" && PUBLISHED_WEBP === 400 && /-1200\\\.\(webp\|avif\)\$\|-800\\\.webp\$/.test(prune)
  && csp.includes("\"script-src 'self'\"") && !csp.includes("unsafe-eval") && csp.includes("object-src 'none'")
  && /frame-src https:\/\/www\.youtube-nocookie\.com https:\/\/www\.tiktok\.com"/.test(csp) && vite.includes("contentSecurityPolicy()"));
