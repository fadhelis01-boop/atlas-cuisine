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
window.addEventListener("hashchange", () => { current = parse(); ls.forEach((l) => l()); window.scrollTo(0, 0); });

export const useRoute = () => useSyncExternalStore((cb) => { ls.add(cb); return () => ls.delete(cb); }, () => current);
export const go = (to: string) => { location.hash = to.startsWith("#") ? to : `#${to}`; };
export const href = (to: string) => `#${to}`;
