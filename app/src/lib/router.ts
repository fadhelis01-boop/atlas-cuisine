import { useSyncExternalStore } from "react";

// Routeur par ancre (#/…) : fonctionne hors connexion, dans un sous-dossier (GitHub Pages) et en mode installé.
export interface Route { path: string[]; query: URLSearchParams }

function parse(): Route {
  const h = location.hash.replace(/^#\/?/, "");
  const [p, q] = h.split("?");
  return { path: p.split("/").filter(Boolean).map(decodeURIComponent), query: new URLSearchParams(q ?? "") };
}
let current = parse();
const ls = new Set<() => void>();
// Position de défilement mémorisée dans chaque entrée d'historique : un nouvel écran s'ouvre en haut,
// un retour arrière retrouve l'endroit où l'on était dans une longue liste (audit UX 2026-10-16 §2.2).
let saveT = 0;
window.addEventListener("scroll", () => {
  clearTimeout(saveT);
  saveT = window.setTimeout(() => { try { history.replaceState({ ...(history.state ?? {}), y: window.scrollY }, ""); } catch { /* quota */ } }, 120);
}, { passive: true });
let moves = 0; // changements d'écran depuis l'ouverture : « Retour » ne doit pas faire quitter l'application
window.addEventListener("hashchange", () => {
  moves++;
  current = parse(); ls.forEach((l) => l());
  const y = (history.state as { y?: number } | null)?.y;
  if (typeof y !== "number") { window.scrollTo(0, 0); return; }
  // le contenu (pages chargées à la demande, listes) arrive en plusieurs temps : on réessaie brièvement
  let tries = 0;
  const restore = () => { window.scrollTo(0, y); if (Math.abs(window.scrollY - y) > 4 && tries++ < 20) setTimeout(restore, 50); };
  requestAnimationFrame(restore);
});
/** Remonte en haut (changement d'écran sans changement d'adresse, ex. fin de l'accueil de bienvenue). */
export const toTop = () => window.scrollTo(0, 0);

export const useRoute = () => useSyncExternalStore((cb) => { ls.add(cb); return () => ls.delete(cb); }, () => current);
export const go = (to: string) => { location.hash = to.startsWith("#") ? to : `#${to}`; };
export const href = (to: string) => `#${to}`;

/** Retour : l'écran précédent dans l'application s'il existe, sinon l'écran parent indiqué. */
export function goBack(fallback: string) { if (moves > 0) history.back(); else go(fallback); }
