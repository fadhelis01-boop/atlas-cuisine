// Test de fumée (audit famille 2026-10-16) : chaque page de l'application est rendue pour de vrai (React + DOM simulé)
// avec un profil de famille, et ne doit ni tomber dans l'écran d'erreur, ni écrire d'erreur React dans la console.
// Il attrape ce que les contrôles de logique ne voient pas (boucle infinie d'un sélecteur, rangée d'accueil cassée…).
import { JSDOM } from "jsdom";

const dom = new JSDOM("<!doctype html><html lang=\"fr\"><body><div id=\"root\"></div></body></html>", { url: "https://atlas.test/", pretendToBeVisual: true });
const w = dom.window as unknown as Window & typeof globalThis;
const g = globalThis as Record<string, unknown>;
for (const k of ["window", "document", "navigator", "location", "localStorage", "sessionStorage", "HTMLElement", "Node", "Element", "HTMLInputElement",
  "Event", "KeyboardEvent", "MouseEvent", "CustomEvent", "getComputedStyle", "history", "HashChangeEvent", "requestAnimationFrame", "cancelAnimationFrame", "DOMParser", "Blob", "URL"] as const) {
  try { g[k] = (w as unknown as Record<string, unknown>)[k]; } catch { /* lecture seule dans Node : on garde celle de Node */ }
}
// API absentes du DOM simulé
w.matchMedia = ((q: string) => ({ matches: false, media: q, addEventListener() {}, removeEventListener() {}, addListener() {}, removeListener() {}, onchange: null, dispatchEvent: () => false })) as never;
w.scrollTo = (() => undefined) as never;
(w.HTMLElement.prototype as { scrollIntoView?: () => void }).scrollIntoView = () => undefined;
class IO { observe() {} unobserve() {} disconnect() {} takeRecords() { return []; } }
g.IntersectionObserver = w.IntersectionObserver = IO as never;
g.ResizeObserver = (w as unknown as Record<string, unknown>).ResizeObserver = IO;
g.IS_REACT_ACT_ENVIRONMENT = true;

// profil d'une famille de 4, déjà accueillie, avec une semaine planifiée et un reste au frigo
localStorage.setItem("atlas-state-v1", JSON.stringify({
  profile: { noPork: true, alcohol: "standard", strict: false, vegetarian: false, allergens: ["FC"], allergensWarn: ["AR"], adult: true, kidsAge: 4, equipment: ["four", "plaques", "poele", "casserole", "autocuiseur"], onboarded: true, household: { adults: 2, kids: [4, 9] } },
  favorites: ["hachis_parmentier", "crepes_bretonnes", "pain_surprise"], restes: [{ id: "riz", cooked: "2026-10-10" }],
}));

const errors: string[] = [];
const origError = console.error;
console.error = (...a: unknown[]) => { errors.push(a.map(String).join(" ").slice(0, 300)); };

const ROUTES = ["", "explorer", "region/france", "recherche?q=lunchbox", "recherche?q=enfant%20difficile%20legumes", "frigo", "courses", "recette/hachis_parmentier",
  "recette/tripes_caen_version", "cuisine/hachis_parmentier", "techniques", "pains", "sauces", "fetes", "zero-dechet", "enfants", "imports", "biblio", "profil",
  "credits", "apprendre", "semaine", "recettes", "dictionnaire", "ingredient/avocat", "restes?r=volaille,riz,fruits", "bien-choisir", "pique-nique"];

const { createRoot } = await import("react-dom/client");
const { act } = await import("react");
const { default: App } = await import("../src/App");
const React = await import("react");
const root = createRoot(document.getElementById("root")!);
const settle = async () => { for (let i = 0; i < 30; i++) { await act(async () => { await new Promise((r) => setTimeout(r, 15)); }); if (!document.body.textContent?.includes("Chargement")) break; } };

const store = await import("../src/lib/store");
let failed = 0;
await act(async () => { root.render(React.createElement(App)); });
// deux passages : la famille (profil rempli, restes, favoris) puis un nouvel utilisateur (tout vide : les cas « liste vide »)
for (const pass of ["famille", "nouveau"] as const) {
  if (pass === "nouveau") await act(async () => { store.resetAll(); store.setState((st) => { st.profile.onboarded = true; }); });
for (const r of ROUTES) {
  errors.length = 0;
  await act(async () => { location.hash = `#/${r}`; w.dispatchEvent(new w.HashChangeEvent("hashchange")); });
  await settle();
  const text = document.body.textContent ?? "";
  const bad = text.includes("Oups, cette page a un souci") || text.includes("Page introuvable") || text.includes("Chargement…") || errors.some((e) => /Warning|Error|Maximum update/.test(e) && !/act\(/.test(e));
  if (bad) { failed++; origError(`FAIL [${pass}] page /${r} :`, text.includes("Oups") ? "écran d'erreur" : text.includes("introuvable") ? "page introuvable" : text.includes("Chargement…") ? "toujours en chargement" : errors[0]); }
  else if (pass === "famille") console.log(`PASS page /${r} (${text.length} caractères)`);
}
}
// —— parcours avec de vrais clics (audit dév/UX 2026-10-21 §4) : ce que les rendus seuls ne prouvent pas
const go = async (h: string) => { await act(async () => { location.hash = `#/${h}`; w.dispatchEvent(new w.HashChangeEvent("hashchange")); }); await settle(); await act(async () => { await new Promise((r) => setTimeout(r, 120)); }); };
const click = async (el: Element | null | undefined) => { if (!el) throw new Error("élément introuvable"); await act(async () => { (el as HTMLElement).click(); }); await settle(); };
const byText = (sel: string, t: string) => [...document.querySelectorAll(sel)].find((e) => e.textContent?.includes(t));
let parcours = 0;
const step = (name: string, ok: boolean, detail = "") => { if (ok) { parcours++; console.log(`PASS parcours : ${name}`); } else { failed++; origError(`FAIL parcours : ${name} ${detail}`); } };
try {
  // 1. portions : les deux boutons « Cuisiner » emportent le nombre choisi
  await go("recette/blanquette_veau");
  await click(document.querySelector('.cook-sticky button[aria-label="Plus de portions"]'));
  const n = document.querySelector(".cook-sticky .portions strong")?.textContent;
  const hrefs = [...document.querySelectorAll(".cook-sticky a.btn, a.cook-cta")].map((a) => a.getAttribute("href"));
  step("les portions choisies passent au mode cuisine, par les deux boutons", hrefs.length === 2 && hrefs.every((x) => x?.includes(`portions=${n}`)), JSON.stringify(hrefs));
  // 2. changement d'écran : titre de l'onglet et focus sur le contenu
  await go("semaine");
  step("le titre de l'onglet suit l'écran et le focus va au contenu", document.title === "Ma semaine · ATLAS" && document.activeElement?.id === "contenu", `${document.title} / ${document.activeElement?.id}`);
  // 3. lien d'évitement : il donne le focus au contenu sans changer d'écran
  const hashBefore = location.hash;
  (document.activeElement as HTMLElement | null)?.blur();
  await click(document.querySelector("a.skip"));
  step("« Aller au contenu » ne casse plus la navigation", location.hash === hashBefore && document.activeElement?.id === "contenu", location.hash);
  // 4. semaine → courses
  await click(byText("button", "Compléter les cases vides"));
  await click(byText("button", "Mettre la semaine dans la liste de courses"));
  step("une semaine proposée part dans la liste de courses", store.getState().shopping.length > 5, String(store.getState().shopping.length));
  // 5. liste reçue par lien : rien n'est ajouté sans le demander, puis ajout sans doublon
  const { encodeShare } = await import("../src/lib/partage");
  const before = store.getState().shopping.length;
  await go(`partage?d=${await encodeShare({ v: 1, kind: "courses", shopping: [{ label: "Farine de châtaigne (test)", section: "Épicerie", ref: null, from: "Un proche" }] })}`);
  const untouched = store.getState().shopping.length === before && document.body.textContent?.includes("Farine de châtaigne (test)");
  await click(byText("button", "Ajouter à ma liste"));
  step("une liste reçue s'affiche, puis s'ajoute à la mienne sur demande", !!untouched && store.getState().shopping.some((x) => x.label === "Farine de châtaigne (test)") && location.hash.startsWith("#/courses"));
  // 6. onglet juste : la cuisine des restes est rangée sous « Ma semaine »
  await go("restes");
  step("chaque écran allume son onglet (Restes → Ma semaine)", document.querySelector(".nav .tab.on .tab-lb")?.textContent === "Ma semaine", document.querySelector(".nav .tab.on .tab-lb")?.textContent ?? "aucun");
  // 7. fin de l'accueil de bienvenue : l'adresse ne change pas, le titre de l'onglet doit suivre quand même
  await act(async () => { store.setState((st) => { st.profile.onboarded = false; }); });
  await go("recette/tarte_tatin");
  const welcome = document.title;
  await act(async () => { store.setState((st) => { st.profile.onboarded = true; }); });
  await settle(); await act(async () => { await new Promise((r) => setTimeout(r, 150)); });
  step("le titre suit la sortie de l'accueil de bienvenue", welcome.startsWith("Bienvenue") && document.title === "Tarte Tatin · ATLAS", `${welcome} → ${document.title}`);
} catch (e) { failed++; origError("FAIL parcours :", (e as Error).message); }
console.log(`${parcours} parcours sur 7`);
await act(async () => { root.unmount(); });
console.log(`\n${2 * ROUTES.length - failed} rendus sur ${2 * ROUTES.length} sans erreur (${ROUTES.length} pages, profil famille puis nouvel utilisateur)`);
process.exit(failed ? 1 : 0);
