import { useSyncExternalStore } from "react";

// Retours d'action uniformes (audit UX 2026-10-16 §2.7) : un message discret en bas d'écran, avec « Annuler »
// quand l'action se défait, au lieu des boîtes de confirmation bloquantes du navigateur.
export interface Toast { id: number; text: string; undo?: () => void; link?: { label: string; to: string } }
let toasts: Toast[] = [];
let seq = 0;
const ls = new Set<() => void>();
const emit = () => ls.forEach((l) => l());

export function toast(text: string, opts: { undo?: () => void; link?: { label: string; to: string }; ms?: number } = {}) {
  const t: Toast = { id: ++seq, text, undo: opts.undo, link: opts.link };
  toasts = [...toasts.slice(-1), t];
  emit();
  setTimeout(() => dismiss(t.id), opts.ms ?? (opts.undo ? 6000 : 3500));
}
export function dismiss(id: number) { toasts = toasts.filter((t) => t.id !== id); emit(); }
export const useToasts = () => useSyncExternalStore((cb) => { ls.add(cb); return () => ls.delete(cb); }, () => toasts);
