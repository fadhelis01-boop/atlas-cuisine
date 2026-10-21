// Mesures locales (audit dév/UX 2026-10-21 §5.7 et §5.8), jamais envoyées :
// - quels écrans servent (compteur par rubrique), joint à l'export du carnet seulement si la personne le demande ;
// - le temps de démarrage sur CET appareil : la seule mesure honnête sur un téléphone d'entrée de gamme est celle qu'il fait lui-même.
import { useEffect } from "react";
import { setState } from "./store";

const PERF_KEY = "atlas-perf-v1";
export interface PerfEntry { at: string; start: number; details: number | null; ua: string }

let detailsAt: number | null = null;
export const markDetails = () => { detailsAt ??= Math.round(performance.now()); };

/** À appeler une fois, quand le premier écran est affiché. */
export function recordStartup() {
  const start = Math.round(performance.now());
  setTimeout(() => {
    try {
      const list = readPerf();
      const e: PerfEntry = { at: new Date().toISOString(), start, details: detailsAt, ua: navigator.userAgent.slice(0, 120) };
      localStorage.setItem(PERF_KEY, JSON.stringify([e, ...list].slice(0, 10)));
    } catch { /* stockage indisponible */ }
  }, 3000); // le détail des fiches a eu le temps d'arriver
}
export function readPerf(): PerfEntry[] {
  try { return JSON.parse(localStorage.getItem(PERF_KEY) ?? "[]") as PerfEntry[]; } catch { return []; }
}
/** Médiane des derniers démarrages (ms), ou null. */
export function medianStartup(list = readPerf()): number | null {
  if (!list.length) return null;
  const s = list.map((x) => x.start).sort((a, b) => a - b);
  return s[Math.floor(s.length / 2)];
}

/** Rubrique d'un écran, pour le compteur (« recette », pas « recette/blanquette_veau ») : rien de personnel. */
export const screenKey = (p0: string | undefined) => p0 || "accueil";
export function useUsageCounter(p0: string | undefined) {
  useEffect(() => {
    const k = screenKey(p0);
    setState((s) => { s.usage = { ...(s.usage ?? {}), [k]: ((s.usage ?? {})[k] ?? 0) + 1 }; });
  }, [p0]);
}
