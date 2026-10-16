// Normalisation et recherche tolérante (Tome 1 §6.2) : accents, ligatures, translittérations, petites fautes.

export function norm(s: string): string {
  return s
    .toLowerCase()
    .replace(/œ/g, "oe").replace(/æ/g, "ae")
    .normalize("NFD").replace(/[̀-ͯ]/g, "")
    .replace(/[’']/g, " ")
    .replace(/[^a-z0-9؀-ۿऀ-ॿ฀-๿぀-ヿ一-鿿 ]+/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

/** Synonymes culinaires et translittérations courantes : chaque groupe est équivalent. */
const SYN: string[][] = [
  ["tajine", "tagine", "tajin", "tagin"], ["thieboudienne", "thieb", "tieb", "tiep", "ceebu jen", "thiebou"], ["boeuf", "beef"],
  ["pad thai", "phat thai", "padthai"], ["mafe", "maafe", "tigadeguena"], ["yassa", "yasa"], ["couscous", "kuskus", "seksu"],
  ["chakchouka", "shakshuka", "shakshouka"], ["houmous", "hummus", "humus"], ["taboule", "tabbouleh", "tabouleh"],
  ["msemen", "msmen", "rghaif"], ["naan", "nan"], ["chorba", "shorba", "jari", "harira"], ["courgette", "zucchini"],
  ["aubergine", "eggplant"], ["coriandre", "cilantro"], ["crevette", "shrimp", "gambas"], ["poulet", "chicken", "djej", "dajaj"],
  ["agneau", "lamb", "mouton"], ["pates", "pasta", "spaghetti"], ["pizza", "pizze"], ["frites", "fries", "pommes frites"],
  ["mayonnaise", "mayo"], ["sauce blanche", "sauce kebab"], ["bissap", "hibiscus", "jamaica", "karkade", "foléré"],
  ["gingembre", "ginger", "gnamakoudji"], ["dal", "dhal", "daal"], ["teriyaki", "teriyak"], ["crepe", "crepes", "krampouezh"],
  ["galette", "galettes", "sarrasin", "ble noir"], ["pain", "bread", "khobz"], ["sans porc", "halal"], ["guacamole", "guaca"],
];
const SYN_MAP = new Map<string, string[]>();
SYN.forEach((g) => g.forEach((w) => SYN_MAP.set(w, g)));

function lev(a: string, b: string, max: number): number {
  if (Math.abs(a.length - b.length) > max) return max + 1;
  let prev = Array.from({ length: b.length + 1 }, (_, i) => i);
  for (let i = 1; i <= a.length; i++) {
    const cur = [i];
    let best = i;
    for (let j = 1; j <= b.length; j++) {
      cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
      best = Math.min(best, cur[j]);
    }
    if (best > max) return max + 1;
    prev = cur;
  }
  return prev[b.length];
}

/** Score de correspondance d'une requête dans un texte (0 = pas de correspondance). */
export function matchScore(query: string, text: string): number {
  const q = norm(query);
  if (!q) return 0;
  const t = norm(text);
  if (t === q) return 130;
  if (t.includes(q)) return (t.startsWith(q) ? 100 : 80) + (t.split(" ")[0] === q ? 15 : 0) - Math.min(10, t.length / 20);
  const words = t.split(" ");
  let score = 0;
  for (const qw of q.split(" ")) {
    if (qw.length < 2) continue;
    const variants = SYN_MAP.get(qw) ?? [qw];
    let best = 0;
    for (const v of variants) {
      if (v.includes(" ") ? t.includes(v) : words.some((w) => w.startsWith(v))) best = Math.max(best, 30);
      else if (!SYN_MAP.has(qw) && v.length >= 5 && words.some((w) => lev(w.slice(0, v.length + 1), v, v.length >= 7 ? 2 : 1) <= (v.length >= 7 ? 2 : 1))) best = Math.max(best, 18);
    }
    if (!best) return 0; // chaque mot de la requête doit trouver un écho
    score += best;
  }
  return score;
}

export function search<T>(items: T[], query: string, fields: (x: T) => string[], limit = 50): T[] {
  if (!norm(query)) return [];
  return items
    .map((x) => ({ x, s: Math.max(0, ...fields(x).map((f, i) => matchScore(query, f) * (i === 0 ? 1.2 : 1))) }))
    .filter((r) => r.s > 0)
    .sort((a, b) => b.s - a.s)
    .slice(0, limit)
    .map((r) => r.x);
}

/** Supprime le gras Markdown des fiches (« **Mise en place.** »). */
export const plain = (s: string) => s.replace(/\*\*/g, "");

export function minutes(m: number): string {
  if (m < 60) return `${m} min`;
  const h = Math.floor(m / 60), r = m % 60;
  return r ? `${h} h ${String(r).padStart(2, "0")}` : `${h} h`;
}

/** Repère les durées dans le texte d'une étape (« 10 min », « 1 h 30 », « 2 à 3 min ») pour les minuteurs. */
export function durationsIn(text: string): { label: string; seconds: number }[] {
  const out: { label: string; seconds: number }[] = [];
  const re = /(\d+(?:,\d+)?)\s*(?:à\s*(\d+(?:,\d+)?)\s*)?(h|heures?|min|minutes?|s\b|secondes?)(?:\s*(\d{1,2})(?!\s*°))?/gi;
  for (const m of plain(text).matchAll(re)) {
    const a = parseFloat(m[1].replace(",", "."));
    const b = m[2] ? parseFloat(m[2].replace(",", ".")) : a;
    const unit = m[3].toLowerCase();
    let sec = unit.startsWith("h") ? b * 3600 + (m[4] ? parseInt(m[4]) * 60 : 0) : unit.startsWith("min") ? b * 60 : b;
    if (unit.startsWith("h") && b > 24) continue;
    if (sec < 5 || sec > 86400) continue;
    sec = Math.round(sec);
    out.push({ label: m[0].trim(), seconds: sec });
  }
  return out;
}

/** Mise à l'échelle simple des quantités (« 1,2 kg » × 1,5). Les quantités non numériques restent telles quelles. */
const MEASURE = /^\s*(g|kg|mg|ml|cl|dl|l|L|c\.|cuill|pinc|cm|mm|tasse|verre|bol|poign|brin|feuille|tranche|filet|trait|zeste|bâton|baton|sachet|cube|botte|bouquet)/i;
function fmtFrac(v: number): string {
  const r = Math.round(v * 4) / 4;
  const frac = ({ 0.25: "¼", 0.5: "½", 0.75: "¾" } as Record<number, string>)[r % 1];
  return Math.floor(r) ? (frac ? `${Math.floor(r)} ${frac}` : String(Math.floor(r))) : frac ?? String(Math.round(v * 10) / 10).replace(".", ",");
}
/** Quantité recalculée pour un autre nombre de portions. Les mesures (g, ml, cuillères…) gardent des fractions ;
 *  les quantités à la pièce (œufs, oignons, gousses) s'arrondissent à l'entier : on ne casse pas « 1 ½ œuf »
 *  (audit UX 2026-10-16 §2.8). */
const PLURAL: Record<string, string> = { pincée: "pincées", gousse: "gousses", tranche: "tranches", feuille: "feuilles", branche: "branches", boîte: "boîtes", poignée: "poignées", tige: "tiges", botte: "bottes", brin: "brins", bâton: "bâtons", sachet: "sachets", verre: "verres", tasse: "tasses", bol: "bols", cube: "cubes", morceau: "morceaux", filet: "filets", zeste: "zestes", bouquet: "bouquets" };
export function scaleQty(qty: string, factor: number): string {
  if (factor === 1) return qty;
  const out = scaleQtyRaw(qty, factor);
  // accord : « 2 pincées », « 3 gousses »
  return out.replace(/^(\d+(?:,\d+)?(?: [½¼¾])?)\s+([a-zàâäéèêëîïôöûüç]+)/i, (m, n: string, w: string) => (parseFloat(n.replace(",", ".")) >= 2 && PLURAL[w] ? `${n} ${PLURAL[w]}` : m));
}
function scaleQtyRaw(qty: string, factor: number): string {
  const FR: Record<string, number> = { "½": 0.5, "¼": 0.25, "¾": 0.75 };
  return qty.replace(/(\d+(?:,\d+)?|½|¼|¾)/, (m, _g, off: number, all: string) => {
    const v = (FR[m] ?? parseFloat(m.replace(",", "."))) * factor;
    if (v >= 100) return String(Math.round(v / 10) * 10);
    if (v >= 10) return String(Math.round(v));
    if (m.includes(",")) return String(Math.round(v * 10) / 10).replace(".", ","); // « 1,2 kg » reste décimal
    const after = all.slice(off + m.length);
    const piece = !MEASURE.test(after) && !FR[m]; // « 3 », « 3 œufs », « 2 gousses »…
    if (piece) return String(Math.max(1, Math.round(v)));
    return fmtFrac(v);
  });
}

/** Les nombres d'une étape suivent les portions (« les 3 œufs » → « les 2 œufs ») ; jamais les temps, températures ou tailles. */
const STEP_QTY = /(\d+(?:,\d+)?)(\s*)(g|kg|ml|cl|dl|l|c\. à s\.|c\. à c\.|cuillères?|pincées?|œufs?|oeufs?|jaunes?|blancs?|gousses?|oignons?|échalotes?|tomates?|citrons?|pommes?|carottes?|courgettes?|poivrons?|bananes?|tranches?|filets?|cuisses?|escalopes?|feuilles?|verres?|tasses?)(?![a-zà-ÿ])/gi;
export function scaleStep(step: string, factor: number): string {
  if (factor === 1) return step;
  return step.replace(STEP_QTY, (_m, n: string, sp: string, unit: string) => `${scaleQty(n + sp + unit, factor).replace(/\s+$/, "")}`);
}

/** Découpe une étape en gestes unitaires pour le mode cuisine (une action par écran) : phrases et points-virgules,
 *  en gardant le titre en gras (« **Sauce.** ») devant chaque morceau. Les morceaux trop courts restent groupés. */
export function splitStep(step: string): string[] {
  const m = step.match(/^(\*\*[^*]+\*\*)\s*/);
  const label = m ? m[1] : "";
  const body = m ? step.slice(m[0].length) : step;
  const parts = body.split(/(?<=[.;!?])\s+(?=[A-ZÀÂÉÈÊÎÔÛÇ0-9«(])|;\s+/).map((x) => x.trim()).filter(Boolean);
  const out: string[] = [];
  for (const p of parts) { if (out.length && (p.length < 28 || out[out.length - 1].length < 28)) out[out.length - 1] += " " + p; else out.push(p); }
  if (out.length <= 1) return [step];
  return out.map((p, k) => `${label ? `${label.replace(/\.?\*\*$/, "")} (${k + 1}/${out.length}).** ` : ""}${p.replace(/^./, (c) => c.toUpperCase())}`);
}

/** Nom court d'un geste pour un minuteur : le titre en gras de l'étape (« Choux (2/3) »), sinon ses premiers mots. */
export function gestureLabel(step: string, n: number): string {
  const b = step.match(/^\*\*(.+?)\.?\*\*/);
  if (b) return b[1].replace(/\.$/, "");
  const words = plain(step).replace(/[,;:.].*$/, "").split(/\s+/).slice(0, 5).join(" ");
  return words.length > 3 ? words : `étape ${n}`;
}

/** Préchauffage : à quelle étape enfourne-t-on, et à quelle température ? (pour prévenir une étape avant) */
export function ovenPlan(steps: string[]): { at: number; temp: string } | null {
  // four nommé, ou une température de four (≥ 120 °C) qui n'est ni un bain de friture, ni un sucre cuit, ni une température à cœur
  const isOven = (s: string) => /enfourn|au four|four (chaud|à|préchauffé)|gratine/i.test(s)
    || (/(1[2-9]\d|2[0-7]\d) ?°C/.test(s) && !/huile|friture|frit|cœur|coeur|sucre|sirop|caramel|thermomètre/i.test(s));
  const at = steps.findIndex(isOven);
  if (at < 0) return null;
  const t = steps[at].match(/(\d{2,3}) ?°C/) ?? steps.slice(0, at).join(" ").match(/(\d{3}) ?°C/);
  return t ? { at, temp: `${t[1]} °C` } : null;
}

/** Mots plutôt que symboles (audit UX 2026-10-16 §2.8) : « ●○○ » et « €€ » ne parlent pas à un débutant. */
export const levelLabel = (n: number) => (n <= 1 ? "Facile" : n === 2 ? "Moyen" : "Difficile");
export const costLabel = (c: string) => (c === "€" ? "Économique" : c === "€€" ? "Prix moyen" : "Pour les grandes occasions");
