// Partage dans le foyer (audit dév/UX 2026-10-21 §2.7) : l'un planifie, l'autre fait les courses. Sans serveur, fidèle au
// « rien ne quitte le téléphone » : la liste ou la semaine voyage DANS le lien (compressée), l'autre téléphone l'ouvre,
// voit ce qu'il reçoit et choisit d'ajouter. La semaine s'exporte aussi dans l'agenda (.ics).
import type { ShoppingItem, State } from "./store";
import { isDay } from "./safe";

export interface SharePayload {
  v: 1;
  kind: "courses" | "semaine";
  from?: string; // prénom ou « la famille », facultatif
  shopping?: { label: string; section: string; ref: string | null; from: string }[];
  week?: Record<string, { midi?: string; soir?: string; entree?: string; dessert?: string }>;
}

const toB64u = (b: Uint8Array) => btoa(String.fromCharCode(...b)).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
const fromB64u = (s: string) => Uint8Array.from(atob(s.replace(/-/g, "+").replace(/_/g, "/")), (c) => c.charCodeAt(0));

async function pipe(data: Uint8Array, stream: CompressionStream | DecompressionStream): Promise<Uint8Array> {
  const out = new Response(new Blob([data as BlobPart]).stream().pipeThrough(stream));
  return new Uint8Array(await out.arrayBuffer());
}

/** Encode : « z » + deflate quand le navigateur sait compresser, sinon « p » + texte brut (toujours lisible). */
export async function encodeShare(p: SharePayload): Promise<string> {
  const raw = new TextEncoder().encode(JSON.stringify(p));
  if (typeof CompressionStream !== "undefined") {
    try { return "z" + toB64u(await pipe(raw, new CompressionStream("deflate-raw"))); } catch { /* repli ci-dessous */ }
  }
  return "p" + toB64u(raw);
}

const ID = /^[a-z0-9_]{1,80}$/;
/** Décode et vérifie : un lien reçu est une donnée extérieure, rien n'est accepté sans contrôle. */
export async function decodeShare(d: string): Promise<SharePayload | null> {
  try {
    if (d.length > 60000) return null;
    const bytes = fromB64u(d.slice(1));
    const json = d[0] === "z" ? new TextDecoder().decode(await pipe(bytes, new DecompressionStream("deflate-raw"))) : d[0] === "p" ? new TextDecoder().decode(bytes) : null;
    if (!json) return null;
    const x = JSON.parse(json) as Partial<SharePayload>;
    if (x.v !== 1 || (x.kind !== "courses" && x.kind !== "semaine")) return null;
    const str = (v: unknown, n: number) => (typeof v === "string" ? v.slice(0, n) : "");
    const out: SharePayload = { v: 1, kind: x.kind, from: str(x.from, 40) || undefined };
    if (Array.isArray(x.shopping)) out.shopping = x.shopping.slice(0, 300).filter((i) => i && typeof i.label === "string")
      .map((i) => ({ label: str(i.label, 200), section: str(i.section, 80) || "Autres", ref: typeof i.ref === "string" ? i.ref.slice(0, 120) : null, from: str(i.from, 120) }));
    if (x.week && typeof x.week === "object") {
      out.week = {};
      for (const [k, v] of Object.entries(x.week).slice(0, 60)) {
        if (!isDay(k) || !v || typeof v !== "object") continue;
        const o: Record<string, string> = {};
        for (const f of ["midi", "soir", "entree", "dessert"]) { const id = (v as Record<string, unknown>)[f]; if (typeof id === "string" && ID.test(id)) o[f] = id; }
        out.week[k] = o;
      }
    }
    return out;
  } catch { return null; }
}

export const shareUrl = (code: string) => `${location.origin}${location.pathname}#/partage?d=${code}`;

/** Ajoute la liste reçue : seulement ce qui manque (même libellé déjà présent et non coché = ignoré). */
export function mergeShopping(cur: ShoppingItem[], inc: NonNullable<SharePayload["shopping"]>, uid: () => string): { list: ShoppingItem[]; added: number } {
  const have = new Set(cur.filter((i) => !i.done).map((i) => i.label.toLowerCase()));
  const add = inc.filter((i) => !have.has(i.label.toLowerCase())).map((i) => ({ id: uid(), ref: i.ref, label: i.label, from: i.from, done: false, section: i.section }));
  return { list: [...cur, ...add], added: add.length };
}
/** Ajoute la semaine reçue : les cases déjà remplies ici ne bougent pas. */
export function mergeWeek(cur: NonNullable<State["week"]>, inc: NonNullable<SharePayload["week"]>): { week: NonNullable<State["week"]>; added: number } {
  const week = structuredClone(cur); let added = 0;
  for (const [day, d] of Object.entries(inc)) for (const [f, id] of Object.entries(d) as [keyof typeof d, string][]) {
    week[day] ??= {};
    if (!week[day][f]) { week[day][f] = id; added++; }
  }
  return { week, added };
}

/** Agenda (.ics, RFC 5545) : un événement par repas, heure locale « flottante » (midi 12 h, soir 19 h 30). */
export function weekToIcs(week: NonNullable<State["week"]>, titleOf: (id: string) => string | undefined, link: (id: string) => string, stamp = new Date()): string {
  const esc = (t: string) => t.replace(/\\/g, "\\\\").replace(/;/g, "\\;").replace(/,/g, "\\,").replace(/\n/g, "\\n");
  const fold = (l: string) => { const out: string[] = []; let x = l; while (x.length > 74) { out.push(x.slice(0, 74)); x = " " + x.slice(74); } out.push(x); return out.join("\r\n"); };
  const ts = stamp.toISOString().replace(/[-:]/g, "").replace(/\.\d+/, "");
  const ev: string[] = [];
  for (const [day, d] of Object.entries(week).sort()) {
    const ymd = day.replace(/-/g, "");
    for (const [slot, at, end] of [["midi", "120000", "130000"], ["soir", "193000", "203000"]] as const) {
      const id = d[slot]; const t = id && titleOf(id);
      if (!id || !t) continue;
      const extra = slot === "midi" && (d.entree || d.dessert) ? ` (menu : ${[d.entree, id, d.dessert].filter(Boolean).map((x) => titleOf(x!) ?? "").filter(Boolean).join(", ")})` : "";
      ev.push(["BEGIN:VEVENT", `UID:atlas-${ymd}-${slot}-${id}@atlas-cuisine`, `DTSTAMP:${ts}`, `DTSTART:${ymd}T${at}`, `DTEND:${ymd}T${end}`,
        fold(`SUMMARY:${esc(`${slot === "midi" ? "Midi" : "Soir"} : ${t}`)}`), fold(`DESCRIPTION:${esc(`Recette ATLAS${extra} : ${link(id)}`)}`), "END:VEVENT"].join("\r\n"));
    }
  }
  return ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//ATLAS//Ma semaine//FR", "CALSCALE:GREGORIAN", ...ev, "END:VCALENDAR", ""].join("\r\n");
}
