// Lecture audio des recettes (Tome 1 §8.6, Tome 6 §8) avec la synthèse vocale du système
// (AVSpeechSynthesizer sur iPhone/iPad/Mac via Safari, voix Google/Microsoft ailleurs) : fonctionne hors connexion.
import { getState } from "./store";
import { plain } from "./text";

const NUM: Record<number, string> = {
  0: "zéro", 1: "un", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit", 9: "neuf", 10: "dix",
};

/** Lexique de prononciation (extrait du Tome 6 §8.3) : graphie → ce que la voix doit dire. */
const LEXIQUE: [RegExp, string][] = [
  [/\btajine\b/gi, "tajine"], [/\bmafé\b/gi, "mafé"], [/\bnaan\b/gi, "nane"], [/\bpad thaï\b/gi, "pad taï"], [/\bgnocchi\b/gi, "gnoki"],
  [/\bmsemen\b/gi, "msémen"], [/\bbatbout\b/gi, "batboute"], [/\bchorba\b/gi, "chorba"], [/\bfrik\b/gi, "frik"],
  [/\bghee\b/gi, "guie"], [/\bdal\b/gi, "dâl"], [/\bteriyaki\b/gi, "téryaki"], [/\bmirin\b/gi, "mirine"],
  [/\bwok\b/gi, "wok"], [/\bchapati\b/gi, "tchapati"], [/\btahini\b/gi, "tahini"], [/\bharissa\b/gi, "harissa"], [/\bbissap\b/gi, "bissap"],
  [/\bguanciale\b/gi, "gouantchalé"], [/\bpecorino\b/gi, "pécorino"], [/\bfocaccia\b/gi, "focatcha"], [/\bpanzanella\b/gi, "pantsanèla"],
  [/\bbouquet garni\b/gi, "bouquet garni"], [/\bth\.\s*(\d+)(?:-(\d+))?/gi, "thermostat $1"],
];

/** Texte écrit → texte à dire : « 1/2 » → « un demi », « c. à s. » → « cuillère à soupe », « 180 °C » → « 180 degrés »… */
export function speakable(input: string): string {
  let s = plain(input);
  s = s.replace(/⚠️/g, "Attention :").replace(/[✓✅🟡⛔🔄❗•→]/g, " ");
  s = s.replace(/\bc\. à s\./gi, "cuillère à soupe").replace(/\bc\. à c\./gi, "cuillère à café");
  s = s.replace(/\bcàs\b/gi, "cuillère à soupe").replace(/\bcàc\b/gi, "cuillère à café");
  s = s.replace(/½/g, " et demi").replace(/¼/g, " et quart").replace(/¾/g, " trois quarts");
  s = s.replace(/(^|\s)et demi/g, "$1un demi").replace(/(^|\s)et quart/g, "$1un quart");
  s = s.replace(/(\d+)\s*\/\s*(\d+)/g, (_, a, b) => (b === "2" ? `${NUM[+a] ?? a} demi` : b === "3" ? `${NUM[+a] ?? a} tiers` : b === "4" ? `${NUM[+a] ?? a} quart` : `${a} sur ${b}`));
  s = s.replace(/(\d+)\s*°\s*C/g, "$1 degrés").replace(/(\d+)\s*°/g, "$1 degrés");
  s = s.replace(/(\d+(?:,\d+)?)\s*kg\b/g, "$1 kilos").replace(/(\d+(?:,\d+)?)\s*g\b/g, "$1 grammes");
  s = s.replace(/(\d+(?:,\d+)?)\s*cl\b/g, "$1 centilitres").replace(/(\d+(?:,\d+)?)\s*ml\b/g, "$1 millilitres").replace(/(\d+(?:,\d+)?)\s*L\b/g, "$1 litres");
  s = s.replace(/(\d+)\s*cm\b/g, "$1 centimètres").replace(/(\d+)\s*mm\b/g, "$1 millimètres");
  s = s.replace(/(\d+)\s*h\s*(\d+)/g, "$1 heure $2").replace(/(\d+)\s*h\b/g, "$1 heures").replace(/(\d+)\s*min\b/g, "$1 minutes").replace(/(\d+)\s*s\b/g, "$1 secondes");
  s = s.replace(/(\d+)\s*%/g, "$1 pour cent").replace(/\s*×\s*/g, " fois ");
  for (const [re, rep] of LEXIQUE) s = s.replace(re, rep);
  return s.replace(/\s+/g, " ").trim();
}

export const ttsAvailable = () => typeof window !== "undefined" && "speechSynthesis" in window;

export function frenchVoices(): SpeechSynthesisVoice[] {
  if (!ttsAvailable()) return [];
  return speechSynthesis.getVoices().filter((v) => v.lang.toLowerCase().startsWith("fr"));
}

function pickVoice(): SpeechSynthesisVoice | undefined {
  const { voiceURI } = getState().settings;
  const fr = frenchVoices();
  return fr.find((v) => v.voiceURI === voiceURI) ?? fr.find((v) => v.lang === "fr-FR" && /premium|enhanced|natural|neural|amélior/i.test(v.name)) ?? fr.find((v) => v.lang === "fr-FR") ?? fr[0];
}

/** Lit une suite de phrases ; renvoie une fonction d'arrêt. onIndex reçoit l'index en cours de lecture. */
export function speak(parts: string[], opts: { onIndex?: (i: number) => void; onEnd?: () => void } = {}): () => void {
  if (!ttsAvailable()) { opts.onEnd?.(); return () => undefined; }
  speechSynthesis.cancel();
  let stopped = false;
  const voice = pickVoice();
  const rate = getState().settings.rate;
  const next = (i: number) => {
    if (stopped) return;
    if (i >= parts.length) { opts.onEnd?.(); return; }
    const u = new SpeechSynthesisUtterance(speakable(parts[i]));
    u.lang = "fr-FR";
    if (voice) u.voice = voice;
    u.rate = rate;
    u.onstart = () => opts.onIndex?.(i);
    u.onend = () => next(i + 1);
    u.onerror = () => next(i + 1);
    speechSynthesis.speak(u);
  };
  next(0);
  return () => { stopped = true; speechSynthesis.cancel(); };
}

export const stopSpeaking = () => ttsAvailable() && speechSynthesis.cancel();

// ---------------------------------------------------------------- commandes vocales (mode cuisine)
type Cmd = "suivant" | "precedent" | "repete" | "pause" | "lecture" | { minutes: number };
interface SR { lang: string; continuous: boolean; interimResults: boolean; start(): void; stop(): void; onresult: ((e: { results: ArrayLike<ArrayLike<{ transcript: string }> & { isFinal: boolean }> }) => void) | null; onend: (() => void) | null; onerror: ((e: { error: string }) => void) | null }

export const voiceCommandsAvailable = () =>
  typeof window !== "undefined" && ("SpeechRecognition" in window || "webkitSpeechRecognition" in window);

export function parseCommand(t: string): Cmd | null {
  const s = t.toLowerCase();
  const m = s.match(/minuteur\s+(?:de\s+)?(\d+|un|une|deux|trois|quatre|cinq|six|sept|huit|neuf|dix|quinze|vingt|trente)\s*(minute|min|heure)?/);
  if (m) {
    const words: Record<string, number> = { un: 1, une: 1, deux: 2, trois: 3, quatre: 4, cinq: 5, six: 6, sept: 7, huit: 8, neuf: 9, dix: 10, quinze: 15, vingt: 20, trente: 30 };
    const n = words[m[1]] ?? parseInt(m[1]);
    return { minutes: m[2]?.startsWith("heure") ? n * 60 : n };
  }
  if (/\b(suivant|suivante|après|continue)\b/.test(s)) return "suivant";
  if (/\b(précédent|précédente|retour|avant)\b/.test(s)) return "precedent";
  if (/\b(répète|répéter|encore|redis)\b/.test(s)) return "repete";
  if (/\b(pause|stop|arrête|tais-toi|silence)\b/.test(s)) return "pause";
  if (/\b(lis|lecture|reprends|lire)\b/.test(s)) return "lecture";
  return null;
}

/** Écoute continue, uniquement pendant le mode cuisine et signalée à l'écran (Tome 7 §6.2). */
export function listen(onCmd: (c: Cmd, heard: string) => void, onState: (on: boolean, err?: string) => void): () => void {
  const Ctor = (window as unknown as { SpeechRecognition?: new () => SR; webkitSpeechRecognition?: new () => SR }).SpeechRecognition
    ?? (window as unknown as { webkitSpeechRecognition?: new () => SR }).webkitSpeechRecognition;
  if (!Ctor) { onState(false, "La reconnaissance vocale n'est pas disponible sur ce navigateur."); return () => undefined; }
  let active = true;
  const rec = new Ctor();
  rec.lang = "fr-FR";
  rec.continuous = true;
  rec.interimResults = false;
  rec.onresult = (e) => {
    const r = e.results[e.results.length - 1];
    if (!r.isFinal) return;
    const heard = r[0].transcript;
    const c = parseCommand(heard);
    if (c) onCmd(c, heard);
  };
  rec.onerror = (e) => { if (e.error === "not-allowed") { active = false; onState(false, "Micro refusé : autorise-le dans les réglages du navigateur."); } };
  rec.onend = () => { if (active) { try { rec.start(); } catch { /* déjà relancé */ } } else onState(false); };
  try { rec.start(); onState(true); } catch { onState(false, "Impossible de démarrer l'écoute."); }
  return () => { active = false; rec.stop(); };
}
