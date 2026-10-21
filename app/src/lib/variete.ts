// Variété des idées (retour d'usage 2026-10-22) : « Propose-moi » sortait 7 recettes différentes sur 60 propositions
// (moules-frites 20 fois sur 20) et les blocs « du jour » glissaient d'un cran par jour. Trois outils communs :
// un hasard bien mélangé, un tirage pondéré sans remise, et la mémoire de ce qui a déjà été montré.

/** Générateur pseudo-aléatoire (mulberry32) : bien mélangé même pour des graines voisines (jour 1, jour 2…). */
export function rng(seed: number): () => number {
  let a = (seed ^ 0x9e3779b9) >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
/** Graine du jour pour un bloc donné : change chaque jour, différente d'un bloc à l'autre. */
export const daySeed = (salt: number, now = Date.now()) => Math.floor(now / 86400000) * 1000003 + salt * 7919;
/** Graine neuve à chaque appui (« Autres idées »). */
export const freshSeed = () => (typeof crypto !== "undefined" && crypto.getRandomValues ? crypto.getRandomValues(new Uint32Array(1))[0] : Math.floor(Math.random() * 2 ** 32));

/** Mélange déterministe (même graine = même ordre, graines voisines = ordres sans rapport). */
export function shuffled<T>(list: readonly T[], seed: number): T[] {
  const r = rng(seed); const a = [...list];
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}
/** n éléments du jour, vraiment différents d'un jour à l'autre. */
export const dailyPick = <T,>(list: readonly T[], n: number, salt: number, now = Date.now()) => shuffled(list, daySeed(salt, now)).slice(0, n);

export interface PickOptions<T> {
  seed: number;
  /** poids de base (plus haut = plus probable) ; le hasard garde toujours sa part */
  score?: (x: T) => number;
  /** écart de score qui divise la probabilité par e ≈ 2,7 : plus grand = plus varié */
  temperature?: number;
  /** déjà montrés récemment : fortement écartés (pas interdits, pour ne jamais tomber à court) */
  recent?: ReadonlySet<string>;
  id?: (x: T) => string;
  /** deux choisis ne doivent pas partager cette clé (ex. la cuisine du monde) */
  distinct?: (x: T) => string;
}
/** Tirage pondéré sans remise (Gumbel-max) : les meilleurs sortent plus souvent, jamais toujours les mêmes. */
export function pickVaried<T>(list: readonly T[], n: number, o: PickOptions<T>): T[] {
  const r = rng(o.seed); const temp = o.temperature ?? 2;
  const keyed = list.map((x) => {
    const base = (o.score?.(x) ?? 0) / temp - (o.recent && o.id && o.recent.has(o.id(x)) ? 6 : 0);
    return { x, k: base - Math.log(-Math.log(Math.max(1e-12, r()))) };
  }).sort((a, b) => b.k - a.k);
  const out: T[] = []; const used = new Set<string>();
  for (const { x } of keyed) {
    if (out.length === n) break;
    const d = o.distinct?.(x);
    if (d !== undefined && used.has(d)) continue;
    if (d !== undefined) used.add(d);
    out.push(x);
  }
  return out;
}
