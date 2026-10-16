import { useSyncExternalStore } from "react";
import type { Profile } from "./types";
import { toast } from "./toast";

// État local de l'application, conservé sur l'appareil (localStorage). Aucune donnée ne quitte le téléphone :
// les régimes et allergies sont des données sensibles (Tome 1 §19.1).

export interface FridgeItem { ref: string; dlc: string | null; zone: "frigo" | "placard" | "congelateur"; added: string }
export interface ShoppingItem { id: string; ref: string | null; label: string; from: string; done: boolean; section: string }
export interface MyImport {
  id: string;
  url: string;
  title: string;
  caption: string;
  source: string;
  cat: string;
  macro: string | null;
  pork: "oui" | "non" | "doute";
  alcohol: "oui" | "non" | "doute";
  ingredients: { text: string; ref: string | null }[];
  steps: string[];
  added: string;
  notes: string;
  author?: string; // auteur·e lu·e sur la plateforme (oEmbed)
}
export interface SavedMenu { id: string; name: string; recipeIds: string[]; drinks: string[]; date: string; guests: number }
export interface Timer { id: string; label: string; endAt: number; recipeId: string | null; done: boolean }

export interface State {
  profile: Profile;
  favorites: string[];
  fridge: FridgeItem[];
  shopping: ShoppingItem[];
  imports: MyImport[];
  menus: SavedMenu[];
  timers: Timer[];
  cooked: Record<string, number>; // recette → nombre de fois cuisinée
  recipeVideos: Record<string, string[]>; // recette → liens vidéo ajoutés par l'utilisateur
  settings: { theme: "auto" | "light" | "dark"; textScale: number; readableFont: boolean; rate: number; voiceURI: string | null; units: "metric"; zone: "auto" | "nord" | "sud" | "tropical"; lastBackup?: string; backupNudge?: string };
  recent: string[];
  learned?: string[]; // étapes du parcours « J'apprends à cuisiner » validées
  journal?: Record<string, { rating: number; note: string; date: string }>; // mon carnet : note et remarques après avoir cuisiné
  week?: Record<string, { midi?: string; soir?: string }>; // planificateur : date ISO → plats du midi et du soir
  pantry?: string[]; // placard supposé toujours présent (frigo), modifiable
  weekPrefs?: { people: number; slots: ("midi" | "soir")[]; weekdayMax: number };
  restes?: { id: string; cooked: string }[]; // mes restes cuits : type de reste (lib/restes.ts) + date de cuisson, pour l'alerte de conservation
}

const KEY = "atlas-state-v1";
const DEFAULT: State = {
  profile: { noPork: false, alcohol: "allowed", strict: false, vegetarian: false, allergens: [], adult: false, kidsAge: null, equipment: ["four", "plaques", "poele", "casserole", "mixeur"], onboarded: false },
  favorites: [], fridge: [], shopping: [], imports: [], menus: [], timers: [], cooked: {}, recipeVideos: {}, recent: [],
  settings: { theme: "auto", textScale: 1, readableFont: false, rate: 1, voiceURI: null, units: "metric", zone: "auto" },
};

function load(): State {
  try {
    const raw = localStorage.getItem(KEY);
    if (!raw) return structuredClone(DEFAULT);
    const s = JSON.parse(raw) as Partial<State>;
    return { ...structuredClone(DEFAULT), ...s, profile: { ...DEFAULT.profile, ...s.profile }, settings: { ...DEFAULT.settings, ...s.settings } };
  } catch {
    return structuredClone(DEFAULT);
  }
}

let state: State = load();
const listeners = new Set<() => void>();

export function getState() { return state; }
export function setState(fn: (s: State) => State | void) {
  const draft = structuredClone(state);
  const next = fn(draft) ?? draft;
  state = next;
  scheduleSave();
  listeners.forEach((l) => l());
}

// Écriture groupée (audit famille) : une rafale de changements = une seule écriture, et toujours avant que la page se ferme.
// Si la mémoire de l'appareil est pleine ou bloquée, on prévient une fois au lieu de perdre les changements en silence.
let saveTimer: ReturnType<typeof setTimeout> | null = null;
let warned = false;
function flush() {
  if (saveTimer) { clearTimeout(saveTimer); saveTimer = null; }
  try { localStorage.setItem(KEY, JSON.stringify(state)); warned = false; }
  catch {
    if (!warned) { warned = true; toast("Mémoire de l'appareil pleine ou bloquée : tes derniers changements ne sont pas enregistrés. Exporte tes données (Profil) et supprime des vidéos importées.", { ms: 12000 }); }
  }
}
function scheduleSave() { if (!saveTimer) saveTimer = setTimeout(flush, 250); }
if (typeof window !== "undefined") {
  window.addEventListener("pagehide", flush);
  document.addEventListener("visibilitychange", () => { if (document.visibilityState === "hidden") flush(); });
}

/** Demande au navigateur de ne pas effacer les données d'ATLAS quand l'appareil manque de place (Safari, Chrome). */
export async function askPersistence(): Promise<boolean> {
  try { return (await navigator.storage?.persisted?.()) || (await navigator.storage?.persist?.()) || false; } catch { return false; }
}
/** Faut-il rappeler de sauvegarder ? Données personnelles présentes et dernier export de plus de 30 jours (ou jamais). */
export function backupDue(s: State = state, now = Date.now()): boolean {
  const personal = s.favorites.length + Object.keys(s.journal ?? {}).length + s.imports.length + Object.keys(s.week ?? {}).length + s.menus.length;
  if (personal < 3) return false;
  const last = Math.max(s.settings.lastBackup ? Date.parse(s.settings.lastBackup) : 0, s.settings.backupNudge ? Date.parse(s.settings.backupNudge) : 0);
  return now - last > 30 * 86400000;
}
export function useStore<T>(sel: (s: State) => T): T {
  return useSyncExternalStore((cb) => { listeners.add(cb); return () => listeners.delete(cb); }, () => sel(state));
}
export const useProfile = () => useStore((s) => s.profile);

export const uid = () => Math.random().toString(36).slice(2, 10) + Date.now().toString(36).slice(-4);

export function toggleFavorite(id: string) {
  const was = state.favorites.includes(id);
  setState((s) => { s.favorites = was ? s.favorites.filter((x) => x !== id) : [id, ...s.favorites]; });
  toast(was ? "Retiré de tes recettes" : "Gardé dans Mes recettes", { undo: () => toggleFavoriteSilent(id), link: was ? undefined : { label: "Voir", to: "/biblio" } });
}
function toggleFavoriteSilent(id: string) {
  setState((s) => { s.favorites = s.favorites.includes(id) ? s.favorites.filter((x) => x !== id) : [id, ...s.favorites]; });
}
export function pushRecent(id: string) {
  setState((s) => { s.recent = [id, ...s.recent.filter((x) => x !== id)].slice(0, 12); });
}
export function exportData(): string { setState((s) => { s.settings.lastBackup = new Date().toISOString(); }); return JSON.stringify(state, null, 2); }
export function importData(json: string) {
  const s = JSON.parse(json) as State;
  if (!s || typeof s !== "object" || !("profile" in s)) throw new Error("Fichier non reconnu");
  setState(() => ({ ...structuredClone(DEFAULT), ...s }));
}
export function resetAll() { setState(() => structuredClone(DEFAULT)); }
