// Minuteurs multiples et nommés (Tome 1 §8.5). L'échéance est enregistrée (heure de fin) : le minuteur
// survit à un rechargement ou à une fermeture de l'application. Sonnerie + vibration + notification si autorisée.
// Limite web : sur iPhone, une application web en arrière-plan ne peut pas sonner ; la notification
// et l'alerte au retour dans l'application prennent le relais (voir Profil > À propos).
import { useEffect, useState } from "react";
import { getState, setState, uid, useStore } from "./store";

export function startTimer(label: string, seconds: number, recipeId: string | null = null) {
  void askNotification();
  setState((s) => { s.timers.push({ id: uid(), label, endAt: Date.now() + seconds * 1000, recipeId, done: false }); });
}
export const removeTimer = (id: string) => setState((s) => { s.timers = s.timers.filter((t) => t.id !== id); });
export const addTime = (id: string, sec: number) => setState((s) => { const t = s.timers.find((x) => x.id === id); if (t) { t.endAt += sec * 1000; t.done = false; } });

async function askNotification() {
  try { if ("Notification" in window && Notification.permission === "default") await Notification.requestPermission(); } catch { /* non pris en charge */ }
}

let ctx: AudioContext | null = null;
export function ring() {
  try {
    ctx ??= new (window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext)();
    const t0 = ctx.currentTime;
    for (let i = 0; i < 6; i++) {
      const o = ctx.createOscillator(), g = ctx.createGain();
      o.frequency.value = i % 2 ? 660 : 880;
      g.gain.setValueAtTime(0.0001, t0 + i * 0.35);
      g.gain.exponentialRampToValueAtTime(0.4, t0 + i * 0.35 + 0.02);
      g.gain.exponentialRampToValueAtTime(0.0001, t0 + i * 0.35 + 0.3);
      o.connect(g).connect(ctx.destination);
      o.start(t0 + i * 0.35); o.stop(t0 + i * 0.35 + 0.32);
    }
  } catch { /* audio indisponible */ }
  try { navigator.vibrate?.([300, 150, 300, 150, 600]); } catch { /* */ }
}

async function notify(label: string) {
  try {
    if (!("Notification" in window) || Notification.permission !== "granted") return;
    const reg = await navigator.serviceWorker?.getRegistration();
    const opts = { body: "Le minuteur est terminé.", icon: "./icons/icon-192.png", tag: "atlas-timer", requireInteraction: true } as NotificationOptions;
    if (reg) await reg.showNotification(`⏰ ${label}`, opts);
    else new Notification(`⏰ ${label}`, opts);
  } catch { /* */ }
}

/** Boucle unique qui vérifie les échéances (lancée par l'App). */
export function useTimerLoop() {
  useEffect(() => {
    const tick = () => {
      const due = getState().timers.filter((t) => !t.done && t.endAt <= Date.now());
      if (!due.length) return;
      setState((s) => { s.timers.forEach((t) => { if (due.some((d) => d.id === t.id)) t.done = true; }); });
      ring();
      due.forEach((t) => void notify(t.label));
    };
    tick();
    const h = setInterval(tick, 1000);
    document.addEventListener("visibilitychange", tick);
    return () => { clearInterval(h); document.removeEventListener("visibilitychange", tick); };
  }, []);
}

export function useNow(ms = 1000) {
  const [now, setNow] = useState(Date.now());
  useEffect(() => { const h = setInterval(() => setNow(Date.now()), ms); return () => clearInterval(h); }, [ms]);
  return now;
}

export const useTimers = () => useStore((s) => s.timers);

export function fmtLeft(ms: number) {
  const s = Math.max(0, Math.ceil(ms / 1000));
  const h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), r = s % 60;
  return h ? `${h}:${String(m).padStart(2, "0")}:${String(r).padStart(2, "0")}` : `${m}:${String(r).padStart(2, "0")}`;
}

/** Garde l'écran allumé en mode cuisine (Wake Lock API ; Safari iOS 16.4+). */
export function useWakeLock(on: boolean) {
  useEffect(() => {
    if (!on || !("wakeLock" in navigator)) return;
    let lock: { release: () => Promise<void> } | null = null;
    const req = async () => { try { lock = await (navigator as unknown as { wakeLock: { request: (t: string) => Promise<{ release: () => Promise<void> }> } }).wakeLock.request("screen"); } catch { /* refusé */ } };
    void req();
    const vis = () => document.visibilityState === "visible" && void req();
    document.addEventListener("visibilitychange", vis);
    return () => { document.removeEventListener("visibilitychange", vis); void lock?.release(); };
  }, [on]);
}
