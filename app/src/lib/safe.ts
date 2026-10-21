// Sécurité des données venues de l'extérieur (audit dév/UX 2026-10-21 §1.3) : liens collés par la personne,
// fichiers de sauvegarde restaurés (peut-être reçus d'un proche). Un lien « javascript: » affiché dans un <a> s'exécuterait
// au clic dans l'origine d'ATLAS et pourrait lire le régime et les allergies : on n'accepte que http et https.

/** Le lien s'il est http(s) et bien formé, sinon null. */
export function safeUrl(u: unknown): string | null {
  if (typeof u !== "string") return null;
  const t = u.trim();
  if (t.length > 2048 || !/^https?:\/\//i.test(t)) return null;
  try { const x = new URL(t); return x.protocol === "http:" || x.protocol === "https:" ? x.href : null; } catch { return null; }
}
/** Pour un attribut href : un lien sûr, ou « # » (rien ne se passe). */
export const safeHref = (u: unknown): string => safeUrl(u) ?? "#";

const str = (v: unknown, max = 500): string => (typeof v === "string" ? v.slice(0, max) : "");
const strs = (v: unknown, n = 500, max = 500): string[] => (Array.isArray(v) ? v.filter((x) => typeof x === "string").slice(0, n).map((x: string) => x.slice(0, max)) : []);
const isObj = (v: unknown): v is Record<string, unknown> => !!v && typeof v === "object" && !Array.isArray(v);
const ID = /^[a-z0-9_]{1,80}$/;
/** Une vraie date du calendrier au format AAAA-MM-JJ (« 2026-13-99 » est refusée). */
export const isDay = (k: string) => /^\d{4}-\d{2}-\d{2}$/.test(k) && !Number.isNaN(Date.parse(`${k}T12:00:00Z`)) && new Date(`${k}T12:00:00Z`).toISOString().slice(0, 10) === k;

export interface RestoreReport { ok: boolean; error?: string; counts: Record<string, number>; dropped: number }

/** Nettoie un état restauré : types vérifiés, listes bornées, liens filtrés. Ce qui est douteux est écarté et compté. */
export function sanitizeState(raw: unknown): { state: Record<string, unknown>; report: RestoreReport } {
  let dropped = 0;
  if (!isObj(raw) || !isObj(raw.profile)) return { state: {}, report: { ok: false, error: "Ce fichier n'est pas une sauvegarde ATLAS.", counts: {}, dropped: 0 } };
  const s: Record<string, unknown> = {};
  const p = raw.profile as Record<string, unknown>;
  s.profile = {
    noPork: !!p.noPork, alcohol: ["allowed", "standard", "strict"].includes(p.alcohol as string) ? p.alcohol : "allowed", strict: !!p.strict, vegetarian: !!p.vegetarian,
    allergens: strs(p.allergens, 30, 40), adult: !!p.adult, kidsAge: typeof p.kidsAge === "number" ? p.kidsAge : null,
    equipment: strs(p.equipment, 30, 40), onboarded: !!p.onboarded,
    ...(isObj(p.household) ? { household: { adults: Math.max(1, Math.min(12, Number((p.household as Record<string, unknown>).adults) || 2)), kids: (Array.isArray((p.household as Record<string, unknown>).kids) ? ((p.household as Record<string, unknown>).kids as unknown[]) : []).filter((k) => typeof k === "number").slice(0, 10) } } : {}),
    ...(p.allergensWarn !== undefined ? { allergensWarn: strs(p.allergensWarn, 30, 40) } : {}),
  };
  const ids = (v: unknown) => { const a = strs(v, 2000, 80); const ok = a.filter((x) => ID.test(x)); dropped += a.length - ok.length; return ok; };
  s.favorites = ids(raw.favorites);
  s.recent = ids(raw.recent).slice(0, 12);
  s.learned = strs(raw.learned, 100, 80);
  s.pantry = strs(raw.pantry, 200, 80);
  const list = <T,>(v: unknown, n: number, f: (x: Record<string, unknown>) => T | null): T[] => {
    if (!Array.isArray(v)) return [];
    const out: T[] = [];
    for (const x of v.slice(0, n)) { const y = isObj(x) ? f(x) : null; if (y) out.push(y); else dropped++; }
    return out;
  };
  s.imports = list(raw.imports, 2000, (i) => {
    const url = safeUrl(i.url); if (!url) return null;
    return { id: str(i.id, 40) || Math.random().toString(36).slice(2), url, title: str(i.title, 200), caption: str(i.caption, 4000), source: str(i.source, 40), cat: str(i.cat, 40), macro: typeof i.macro === "string" ? i.macro : null,
      pork: ["oui", "non", "doute"].includes(i.pork as string) ? i.pork : "doute", alcohol: ["oui", "non", "doute"].includes(i.alcohol as string) ? i.alcohol : "doute",
      ingredients: list(i.ingredients, 200, (g) => ({ text: str(g.text, 200), ref: typeof g.ref === "string" ? g.ref : null })), steps: strs(i.steps, 100, 2000),
      added: str(i.added, 40), notes: str(i.notes, 4000), ...(typeof i.author === "string" ? { author: str(i.author, 120) } : {}) };
  });
  s.fridge = list(raw.fridge, 500, (f) => (typeof f.ref === "string" ? { ref: str(f.ref, 120), dlc: typeof f.dlc === "string" ? f.dlc : null, zone: ["frigo", "placard", "congelateur"].includes(f.zone as string) ? f.zone : "frigo", added: str(f.added, 40) } : null));
  s.shopping = list(raw.shopping, 1000, (x) => (typeof x.label === "string" ? { id: str(x.id, 40) || Math.random().toString(36).slice(2), ref: typeof x.ref === "string" ? x.ref : null, label: str(x.label, 200), from: str(x.from, 200), done: !!x.done, section: str(x.section, 80) } : null));
  s.menus = list(raw.menus, 200, (m) => ({ id: str(m.id, 40), name: str(m.name, 120), recipeIds: ids(m.recipeIds), drinks: strs(m.drinks, 20, 80), date: str(m.date, 40), guests: Number(m.guests) || 4 }));
  const rec = (v: unknown, val: (x: unknown) => unknown) => {
    const o: Record<string, unknown> = {};
    if (!isObj(v)) return o;
    for (const [k, x] of Object.entries(v).slice(0, 5000)) { const y = val(x); if (ID.test(k) && y !== undefined) o[k] = y; else dropped++; }
    return o;
  };
  s.cooked = rec(raw.cooked, (x) => (typeof x === "number" ? x : undefined));
  s.recipeVideos = rec(raw.recipeVideos, (x) => { if (!Array.isArray(x)) return undefined; const ok = x.map(safeUrl).filter(Boolean); dropped += x.length - ok.length; return ok; });
  s.journal = rec(raw.journal, (x) => (isObj(x) ? { rating: Math.max(0, Math.min(5, Number(x.rating) || 0)), note: str(x.note, 4000), date: str(x.date, 40), ...(x.kids === "oui" || x.kids === "non" ? { kids: x.kids } : {}) } : undefined));
  s.weekHistory = isObj(raw.weekHistory) ? Object.fromEntries(Object.entries(raw.weekHistory).filter(([k, v]) => ID.test(k) && typeof v === "string").slice(0, 2000)) : {};
  s.week = isObj(raw.week) ? Object.fromEntries(Object.entries(raw.week).filter(([k, v]) => { const ok = isDay(k) && isObj(v); if (!ok) dropped++; return ok; }).slice(0, 400).map(([k, v]) => {
    const d = v as Record<string, unknown>; const o: Record<string, string> = {};
    for (const f of ["midi", "soir", "entree", "dessert"]) { if (typeof d[f] === "string" && ID.test(d[f] as string)) o[f] = d[f] as string; else if (d[f] !== undefined) dropped++; }
    return [k, o];
  })) : {};
  s.restes = list(raw.restes, 200, (x) => (typeof x.id === "string" ? { id: str(x.id, 80), cooked: str(x.cooked, 40) } : null));
  if (isObj(raw.weekPrefs)) s.weekPrefs = raw.weekPrefs;
  if (isObj(raw.settings)) {
    const st = raw.settings as Record<string, unknown>;
    s.settings = { theme: ["auto", "light", "dark"].includes(st.theme as string) ? st.theme : "auto", textScale: Math.max(0.8, Math.min(2, Number(st.textScale) || 1)), readableFont: !!st.readableFont,
      rate: Math.max(0.5, Math.min(2, Number(st.rate) || 1)), voiceURI: typeof st.voiceURI === "string" ? st.voiceURI : null, units: "metric",
      zone: ["auto", "nord", "sud", "tropical"].includes(st.zone as string) ? st.zone : "auto" };
  }
  const counts = { favoris: (s.favorites as string[]).length, carnet: Object.keys(s.journal as object).length, imports: (s.imports as unknown[]).length,
    semaine: Object.keys(s.week as object).length, courses: (s.shopping as unknown[]).length, menus: (s.menus as unknown[]).length };
  return { state: s, report: { ok: true, counts, dropped } };
}
