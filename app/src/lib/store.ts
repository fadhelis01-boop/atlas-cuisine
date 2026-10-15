import { useSyncExternalStore } from "react";
import type { Profile } from "./types";

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
  settings: { theme: "auto" | "light" | "dark"; textScale: number; readableFont: boolean; rate: number; voiceURI: string | null; units: "metric"; zone: "auto" | "nord" | "sud" | "tropical" };
  recent: string[];
  learned?: string[]; // étapes du parcours « J'apprends à cuisiner » validées
  journal?: Record<string, { rating: number; note: string; date: string }>; // mon carnet : note et remarques après avoir cuisiné
  week?: Record<string, { midi?: string; soir?: string }>; // planificateur : date ISO → plats du midi et du soir
  weekPrefs?: { people: number; slots: ("midi" | "soir")[]; weekdayMax: number };
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
  try { localStorage.setItem(KEY, JSON.stringify(state)); } catch { /* stockage plein ou bloqué : l'app continue en mémoire */ }
  listeners.forEach((l) => l());
}
export function useStore<T>(sel: (s: State) => T): T {
  return useSyncExternalStore((cb) => { listeners.add(cb); return () => listeners.delete(cb); }, () => sel(state));
}
export const useProfile = () => useStore((s) => s.profile);

export const uid = () => Math.random().toString(36).slice(2, 10) + Date.now().toString(36).slice(-4);

export function toggleFavorite(id: string) {
  setState((s) => { s.favorites = s.favorites.includes(id) ? s.favorites.filter((x) => x !== id) : [id, ...s.favorites]; });
}
export function pushRecent(id: string) {
  setState((s) => { s.recent = [id, ...s.recent.filter((x) => x !== id)].slice(0, 12); });
}
export function exportData(): string { return JSON.stringify(state, null, 2); }
export function importData(json: string) {
  const s = JSON.parse(json) as State;
  if (!s || typeof s !== "object" || !("profile" in s)) throw new Error("Fichier non reconnu");
  setState(() => ({ ...structuredClone(DEFAULT), ...s }));
}
export function resetAll() { setState(() => structuredClone(DEFAULT)); }
