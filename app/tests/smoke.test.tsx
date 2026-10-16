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
  const bad = text.includes("Oups, cette page a un souci") || text.includes("Page introuvable") || errors.some((e) => /Warning|Error|Maximum update/.test(e) && !/act\(/.test(e));
  if (bad) { failed++; origError(`FAIL [${pass}] page /${r} :`, text.includes("Oups") ? "écran d'erreur" : text.includes("introuvable") ? "page introuvable" : errors[0]); }
  else if (pass === "famille") console.log(`PASS page /${r} (${text.length} caractères)`);
}
}
await act(async () => { root.unmount(); });
console.log(`\n${2 * ROUTES.length - failed} rendus sur ${2 * ROUTES.length} sans erreur (${ROUTES.length} pages, profil famille puis nouvel utilisateur)`);
process.exit(failed ? 1 : 0);
