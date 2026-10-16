import { Icon } from "./icons";
import { useEffect, useRef, useSyncExternalStore } from "react";
import type { ImportEntry } from "../lib/types";

// Lecture des vidéos dans l'application.
// - TikTok : intégration officielle (www.tiktok.com/embed/v2/<id>) ;
// - YouTube : youtube-nocookie.com (pas de cookie publicitaire tant que la vidéo n'est pas lancée).
// Rien n'est chargé chez TikTok ou YouTube avant que l'on appuie sur ▶ (RGPD, Tome 1 §19.1).
// Les carrousels photo TikTok et les liens courts (vm.tiktok.com) ne sont pas intégrables : ils s'ouvrent dans l'application d'origine.

export interface PlayableVideo { title: string; url: string; embed: string; source: string; author?: string }

/** « tt:<id> », « yt:<id> » ou « ys:<id> » (YouTube Short, vertical) à partir d'un lien, ou chaîne vide si la vidéo n'est pas intégrable. */
export function embedOf(url: string): string {
  const ys = url.match(/youtube\.com\/shorts\/([\w-]{11})/);
  if (ys) return `ys:${ys[1]}`;
  const tt = url.match(/tiktok\.com\/@[^/]+\/video\/(\d+)/) ?? url.match(/tiktok\.com\/(?:player\/v1|embed(?:\/v2)?)\/(\d+)/);
  if (tt) return `tt:${tt[1]}`;
  const yt = url.match(/(?:youtube(?:-nocookie)?\.com\/(?:watch\?(?:.*&)?v=|embed\/|shorts\/|live\/)|youtu\.be\/)([\w-]{11})/);
  if (yt) return `yt:${yt[1]}`;
  return "";
}

function playerSrc(embed: string): string {
  const [kind, id] = embed.split(":");
  // embed/v2 : intégration officielle qui fonctionne aussi hors du domaine tiktok.com (le lecteur player/v1 a échoué au test)
  if (kind === "tt") return `https://www.tiktok.com/embed/v2/${id}?lang=fr-FR`;
  if (kind === "yt" || kind === "ys") return `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0&playsinline=1`;
  return "";
}

let current: PlayableVideo | null = null;
const ls = new Set<() => void>();
export function playVideo(v: PlayableVideo) {
  if (!v.embed) { window.open(v.url, "_blank", "noopener"); return; }
  current = v; ls.forEach((l) => l());
}
export function closeVideo() { current = null; ls.forEach((l) => l()); }
const useCurrent = () => useSyncExternalStore((cb) => { ls.add(cb); return () => ls.delete(cb); }, () => current);

/** Lecteur en surimpression, monté une fois dans l'application et dans le mode cuisine. */
export function VideoHost() {
  const v = useCurrent();
  const close = useRef<HTMLButtonElement>(null);
  useEffect(() => {
    if (!v) return;
    close.current?.focus();
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && closeVideo();
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [v]);
  if (!v) return null;
  const vertical = v.embed.startsWith("tt:") || v.embed.startsWith("ys:");
  return (
    <div className="video-layer" role="dialog" aria-modal="true" aria-label={`Vidéo : ${v.title}`} onClick={closeVideo}>
      <div className={`video-box ${vertical ? "vertical" : ""}`} onClick={(e) => e.stopPropagation()}>
        <div className="video-head">
          <span className="video-title">{v.title}</span>
          <button ref={close} className="btn small ghost" onClick={closeVideo} aria-label="Fermer la vidéo"><Icon name="close" size={18} /></button>
        </div>
        <iframe src={playerSrc(v.embed)} title={v.title} allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowFullScreen referrerPolicy="strict-origin-when-cross-origin" />
        <p className="small video-foot">
          {v.source}{v.author && v.source === "TikTok" ? ` · @${v.author}` : v.author && v.author !== v.source ? ` · ${v.author}` : ""} · vidéo de son auteur·e, lue depuis {v.embed.startsWith("tt:") ? "TikTok" : "YouTube"}.{" "}
          <a href={v.url} target="_blank" rel="noopener noreferrer">Ouvrir dans {v.embed.startsWith("tt:") ? "TikTok" : "YouTube"}</a>
        </p>
      </div>
    </div>
  );
}

/** Bouton ▶ (lecture dans l'appli) ou ↗ (ouverture externe si la vidéo n'est pas intégrable). */
export function PlayButton({ v, label }: { v: PlayableVideo; label?: string }) {
  return (
    <button className="play" onClick={() => playVideo(v)} aria-label={`${v.embed ? "Lire" : "Ouvrir"} la vidéo : ${v.title}`}>
      {v.embed ? "▶" : "↗"}{label ? ` ${label}` : ""}
    </button>
  );
}

/** Ligne de liste pour un favori importé : lecture dans l'appli + lien vers l'original. */
export function ImportRow({ i, extra }: { i: ImportEntry; extra?: string }) {
  const v = { title: i.title, url: i.url, embed: i.embed, source: i.source, author: i.author };
  return (
    <li className="import-row">
      <PlayButton v={v} />
      <span>
        <a href={i.url} target="_blank" rel="noopener noreferrer">{i.title}</a>{" "}
        <span className="meta">· {i.source === "TikTok" ? `@${i.author}` : i.source === "YouTube" ? `▶ ${i.author}` : i.source}{i.lang ? ` · ${{ en: "🇬🇧 en anglais", de: "🇩🇪 en allemand", nl: "🇳🇱 en néerlandais" }[i.lang]}` : ""}{i.embed?.startsWith("ys:") ? " · short" : ""}{i.sub ? ` · ${i.sub}` : ""}{i.pork ? " · 🐖" : ""}{i.alcohol ? " · 🍷" : ""}{i.fete ? " · 🎉" : ""}{i.photo ? " · photos" : ""}{extra ? ` · ${extra}` : ""}</span>
      </span>
    </li>
  );
}
