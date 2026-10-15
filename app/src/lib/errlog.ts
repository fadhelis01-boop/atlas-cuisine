// Journal d'erreurs local (audit dév 🟢) : les 20 dernières erreurs, gardées sur l'appareil seulement,
// consultables et copiables depuis le profil pour signaler un problème. Rien n'est envoyé.
const KEY = "atlas-errors-v1";
export interface ErrEntry { at: string; where: string; msg: string }

export function readErrors(): ErrEntry[] {
  try { return JSON.parse(localStorage.getItem(KEY) ?? "[]") as ErrEntry[]; } catch { return []; }
}
export function logError(where: string, e: unknown) {
  try {
    const msg = (e instanceof Error ? `${e.name}: ${e.message}` : String(e)).slice(0, 300);
    const list = [{ at: new Date().toISOString(), where: where.slice(0, 80), msg }, ...readErrors()].slice(0, 20);
    localStorage.setItem(KEY, JSON.stringify(list));
  } catch { /* stockage indisponible : on n'insiste pas */ }
}
export function clearErrors() { try { localStorage.removeItem(KEY); } catch { /* idem */ } }
export function installErrorLog() {
  addEventListener("error", (e) => logError(location.hash || "/", e.error ?? e.message));
  addEventListener("unhandledrejection", (e) => logError(location.hash || "/", e.reason));
}
