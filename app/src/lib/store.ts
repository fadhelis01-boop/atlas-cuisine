import { useSyncExternalStore } from "react";
import type { Profile } from "./types";
import { toast } from "./toast";
import { type RestoreReport, sanitizeState } from "./safe";

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
  journal?: Record<string, { rating: number; note: string; date: string; kids?: "oui" | "non" }>; // kids : les enfants ont aimé (audit gourmet) // mon carnet : note et remarques après avoir cuisiné
  week?: Record<string, { midi?: string; soir?: string; entree?: string; dessert?: string }>; // planificateur : date ISO → plats du midi et du soir
  pantry?: string[]; // placard supposé toujours présent (frigo), modifiable
  weekPrefs?: { people: number; slots: ("midi" | "soir")[]; weekdayMax: number };
  restes?: { id: string; cooked: string }[]; // mes restes cuits : type de reste (lib/restes.ts) + date de cuisson, pour l'alerte de conservation
  weekHistory?: Record<string, string>; // plat → dernière date où il a été planifié (mémoire de 8 semaines du planificateur)
  usage?: Record<string, number>; // écrans ouverts (compteur local, jamais envoyé ; joint à l'export du carnet si la personne le veut)
  shareUsage?: boolean; // joindre ce compteur à l'export du carnet d'essais
  installNudge?: string; // date de l'invitation à installer ATLAS (iPhone)
  version?: number; // version du schéma de l'état (migrations)
}

const KEY = "atlas-state-v1";
const DEFAULT: State = {
  profile: { noPork: false, alcohol: "allowed", strict: false, vegetarian: false, allergens: [], adult: false, kidsAge: null, equipment: ["four", "plaques", "poele", "casserole", "mixeur"], onboarded: false },
  favorites: [], fridge: [], shopping: [], imports: [], menus: [], timers: [], cooked: {}, recipeVideos: {}, recent: [],
  settings: { theme: "auto", textScale: 1, readableFont: false, rate: 1, voiceURI: null, units: "metric", zone: "auto" },
};

/** Version du schéma : à augmenter quand un champ change de forme, avec son étape dans `migrate` (audit dév/UX 2026-10-21). */
export const SCHEMA = 2;
/** Met à niveau un état enregistré par une version plus ancienne d'ATLAS. Chaque étape est testée (tests du moteur). */
export function migrate(raw: Partial<State>, renames: Record<string, string> = {}): State {
  const s = { ...structuredClone(DEFAULT), ...raw, profile: { ...DEFAULT.profile, ...raw.profile }, settings: { ...DEFAULT.settings, ...raw.settings } } as State;
  const v = raw.version ?? 1;
  if (v < 2) { // v1 → v2 : champs facultatifs créés une fois pour toutes
    s.journal ??= {}; s.week ??= {}; s.weekHistory ??= {}; s.usage ??= {};
  }
  // recettes renommées (table écrite par l'export de la bible) : favoris, carnet, semaine, historique suivent le nouveau nom
  const rn = (id: string) => renames[id] ?? id;
  if (Object.keys(renames).length) {
    s.favorites = [...new Set(s.favorites.map(rn))];
    s.recent = [...new Set(s.recent.map(rn))];
    s.journal = Object.fromEntries(Object.entries(s.journal ?? {}).map(([k, e]) => [rn(k), e]));
    s.cooked = Object.fromEntries(Object.entries(s.cooked).map(([k, n]) => [rn(k), n]));
    s.weekHistory = Object.fromEntries(Object.entries(s.weekHistory ?? {}).map(([k, d]) => [rn(k), d]));
    for (const d of Object.values(s.week ?? {})) for (const f of ["midi", "soir", "entree", "dessert"] as const) if (d[f]) d[f] = rn(d[f]!);
  }
  s.version = SCHEMA;
  return s;
}

let RENAMES: Record<string, string> = {};
/** Table des recettes renommées (fournie au démarrage par data.ts, pour ne pas lier le store aux données). */
export function setRenames(r: Record<string, string>) { RENAMES = r; if (Object.keys(r).length) state = migrate(state, r); }

function load(): State {
  try {
    const raw = localStorage.getItem(KEY);
    if (!raw) return { ...structuredClone(DEFAULT), version: SCHEMA };
    return migrate(JSON.parse(raw) as Partial<State>, RENAMES);
  } catch {
    return { ...structuredClone(DEFAULT), version: SCHEMA };
  }
}

let state: State = load();
const listeners = new Set<() => void>();

export function getState() { return state; }
/** Modifie l'état. Seules les branches lues par `fn` sont copiées (copie à la demande, audit dév/UX 2026-10-21) :
 *  cocher une course ne recopie plus les centaines d'imports. `fn` peut aussi renvoyer un état entier (restauration). */
export function setState(fn: (s: State) => State | void) {
  const touched: Record<string, unknown> = {};
  const base = state as unknown as Record<string, unknown>;
  const draft = new Proxy(base, {
    get: (_t, k: string) => { if (!(k in touched)) touched[k] = structuredClone(base[k]); return touched[k]; },
    set: (_t, k: string, v) => { touched[k] = v; return true; },
    deleteProperty: (_t, k: string) => { touched[k] = undefined; return true; },
  }) as unknown as State;
  const ret = fn(draft);
  state = ret && ret !== draft ? ret : ({ ...base, ...touched } as unknown as State);
  scheduleSave();
  listeners.forEach((l) => l());
}

// Écriture groupée (audit famille) : une rafale de changements = une seule écriture, et toujours avant que la page se ferme.
// Si la mémoire de l'appareil est pleine ou bloquée, on prévient une fois au lieu de perdre les changements en silence.
let saveTimer: ReturnType<typeof setTimeout> | null = null;
let warned = false;
let lastWritten: string | null = null;
function flush() {
  if (saveTimer) { clearTimeout(saveTimer); saveTimer = null; }
  try { const json = JSON.stringify(state); if (json !== lastWritten) { localStorage.setItem(KEY, json); lastWritten = json; } warned = false; }
  catch {
    if (!warned) { warned = true; toast("Mémoire de l'appareil pleine ou bloquée : tes derniers changements ne sont pas enregistrés. Exporte tes données (Profil) et supprime des vidéos importées.", { ms: 12000 }); }
  }
}
function scheduleSave() { if (!saveTimer) saveTimer = setTimeout(flush, 250); }
if (typeof window !== "undefined") {
  // deux onglets ouverts : chacun reprend les changements de l'autre au lieu de les écraser (audit dév/UX 2026-10-21)
  window.addEventListener("storage", (e) => {
    if (e.key !== KEY || !e.newValue || e.newValue === lastWritten) return;
    try { state = migrate(JSON.parse(e.newValue) as Partial<State>, RENAMES); lastWritten = e.newValue; listeners.forEach((l) => l()); } catch { /* écriture partielle : la suivante suffira */ }
  });
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
/** Restauration en deux temps : lecture et nettoyage d'abord (aperçu), puis fusion ou remplacement au choix. */
export function readBackup(json: string): { incoming: Partial<State>; report: RestoreReport } {
  let raw: unknown;
  try { raw = JSON.parse(json); } catch { return { incoming: {}, report: { ok: false, error: "Ce fichier n'est pas lisible (JSON invalide).", counts: {}, dropped: 0 } }; }
  const { state: clean, report } = sanitizeState(raw);
  return { incoming: clean as Partial<State>, report };
}
/** Fusion : rien de ce qui est sur l'appareil n'est perdu ; en cas de conflit, l'entrée la plus récente gagne. */
export function mergeState(cur: State, inc: Partial<State>): State {
  const s = structuredClone(cur);
  s.favorites = [...new Set([...s.favorites, ...(inc.favorites ?? [])])];
  const jr = { ...(inc.journal ?? {}) };
  for (const [k, e] of Object.entries(s.journal ?? {})) if (!jr[k] || (jr[k].date ?? "") < (e.date ?? "")) jr[k] = e;
  s.journal = jr;
  const urls = new Set(s.imports.map((i) => i.url));
  s.imports = [...s.imports, ...(inc.imports ?? []).filter((i) => !urls.has(i.url))];
  s.week = { ...(inc.week ?? {}), ...(s.week ?? {}) }; // les jours déjà planifiés ici restent
  const labels = new Set(s.shopping.map((x) => x.label.toLowerCase()));
  s.shopping = [...s.shopping, ...(inc.shopping ?? []).filter((x) => !labels.has(x.label.toLowerCase()))];
  const menuIds = new Set(s.menus.map((m) => m.id));
  s.menus = [...s.menus, ...(inc.menus ?? []).filter((m) => !menuIds.has(m.id))];
  for (const [k, n] of Object.entries(inc.cooked ?? {})) s.cooked[k] = Math.max(s.cooked[k] ?? 0, n);
  for (const [k, l] of Object.entries(inc.recipeVideos ?? {})) s.recipeVideos[k] = [...new Set([...(s.recipeVideos[k] ?? []), ...l])];
  for (const [k, d] of Object.entries(inc.weekHistory ?? {})) if (!s.weekHistory?.[k] || s.weekHistory[k] < d) (s.weekHistory ??= {})[k] = d;
  s.learned = [...new Set([...(s.learned ?? []), ...(inc.learned ?? [])])];
  return s;
}
export function restoreBackup(inc: Partial<State>, mode: "merge" | "replace") {
  setState(() => (mode === "merge" ? mergeState(state, inc) : migrate({ ...inc, settings: { ...state.settings, ...inc.settings } }, RENAMES)));
}
/** Remplacement direct après nettoyage (tests, compatibilité), ou erreur lisible. */
export function importData(json: string) {
  const { incoming, report } = readBackup(json);
  if (!report.ok) throw new Error(report.error);
  restoreBackup(incoming, "replace");
}
export function resetAll() { setState(() => ({ ...structuredClone(DEFAULT), version: SCHEMA })); }
