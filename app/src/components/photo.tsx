import { useState, useSyncExternalStore } from "react";
import imagesJson from "../data/images.json";

// Photos d'illustration (illustrations/process.py) : WebP en 400/800/1200 px, recadrées 4:3, étalonnées,
// avec la couleur dominante comme fond pendant le chargement et le crédit de l'auteur·e (licences libres).
// Le manifeste chargé au démarrage ne garde que l'essentiel ; les crédits (auteur·e, licence, source) sont chargés
// à la première photo affichée avec son crédit (audit dév 🟠 8 : démarrage plus léger avec 1 000+ photos).
export interface PhotoMeta { path: string; sizes: number[]; color: string; kind?: "photo" | "ia"; avif?: 1 }
export interface PhotoCredit { author: string; license: string; licenseUrl: string; page: string; source: string; title: string }
export const IMAGES = imagesJson as unknown as Record<string, PhotoMeta>;

let CREDITS: Record<string, PhotoCredit> | null = null;
let credP: Promise<Record<string, PhotoCredit>> | null = null;
const credListeners = new Set<() => void>();
export function loadCredits(): Promise<Record<string, PhotoCredit>> {
  credP ??= import("../data/credits.json").then((m) => { CREDITS = m.default as unknown as Record<string, PhotoCredit>; credListeners.forEach((l) => l()); return CREDITS; });
  return credP;
}
export function useCredits(): Record<string, PhotoCredit> | null {
  return useSyncExternalStore((cb) => { credListeners.add(cb); void loadCredits(); return () => { credListeners.delete(cb); }; }, () => CREDITS);
}
export const photoOf = (key: string): PhotoMeta | undefined => IMAGES[key];

// AVIF lisible par ce navigateur ? (pour télécharger le bon format hors connexion)
let avifP: Promise<boolean> | null = null;
export function supportsAvif(): Promise<boolean> {
  avifP ??= new Promise((ok) => {
    const i = new Image(); i.onload = () => ok(i.width === 2); i.onerror = () => ok(false);
    i.src = "data:image/avif;base64,AAAAIGZ0eXBhdmlmAAAAAGF2aWZtaWYxbWlhZk1BMUIAAADrbWV0YQAAAAAAAAAhaGRscgAAAAAAAAAAcGljdAAAAAAAAAAAAAAAAAAAAAAOcGl0bQAAAAAAAQAAAB5pbG9jAAAAAEQAAAEAAQAAAAEAAAETAAAAJgAAAChpaW5mAAAAAAABAAAAGmluZmUCAAAAAAEAAGF2MDFDb2xvcgAAAABqaXBycAAAAEtpcGNvAAAAFGlzcGUAAAAAAAAAAgAAAAIAAAAQcGl4aQAAAAADCAgIAAAADGF2MUOBAAwAAAAAE2NvbHJuY2x4AAEADQAGgAAAABdpcG1hAAAAAAAAAAEAAQQBAoMEAAAALm1kYXQSAAoIGAA2iAhoNCAyGBxHh4Xd0000wsAAAJA1jjx+yg1QWM/bnA==";
  });
  return avifP;
}

/** <img> responsive ; `sizes` décrit la largeur affichée pour que le téléphone ne télécharge que la taille utile. */
export function Photo({ k, alt, sizes = "(min-width: 900px) 33vw, 100vw", className = "", eager = false }: { k: string; alt: string; sizes?: string; className?: string; eager?: boolean }) {
  const m = IMAGES[k];
  const [loaded, setLoaded] = useState(false);
  const [failed, setFailed] = useState(false);
  if (!m || failed) return null;
  const srcSet = (ext: string) => m.sizes.map((w) => `./${m.path}-${w}.${ext} ${w}w`).join(", ");
  const img = (
    <img
      className={`photo ${loaded ? "loaded" : ""} ${className}`}
      src={`./${m.path}-${m.sizes[Math.min(1, m.sizes.length - 1)]}.webp`}
      srcSet={srcSet("webp")} sizes={sizes} alt={alt} width={4} height={3}
      loading={eager ? "eager" : "lazy"} decoding="async" style={{ backgroundColor: m.color }}
      onLoad={() => setLoaded(true)} onError={() => setFailed(true)}
    />
  );
  // AVIF (≈ 30 % plus léger) pour les navigateurs qui le lisent, WebP sinon ; <picture> laisse le navigateur choisir
  return m.avif ? <picture className="photo-pic"><source type="image/avif" srcSet={srcSet("avif")} sizes={sizes} />{img}</picture> : img;
}

/** Crédit obligatoire (CC BY / BY-SA) : auteur·e, licence, lien vers l'original. */
export function Credit({ k, note = true }: { k: string; note?: boolean }) {
  const credits = useCredits();
  const p = IMAGES[k];
  const m = credits?.[k];
  if (!p) return null;
  if (!m && p.kind !== "ia") return <p className="credit">Photo sous licence libre{note && " · photo d'illustration : le plat peut différer de la recette ATLAS"}</p>;
  return (
    <p className="credit">
      {p.kind === "ia" || !m ? "Image générée par IA (ATLAS)" : <>Photo : {m.author || "Auteur·e inconnu·e"}, <a href={m.licenseUrl || m.page} target="_blank" rel="noopener noreferrer">{m.license}</a>, via <a href={m.page} target="_blank" rel="noopener noreferrer">{m.source}</a></>}
      {note && <> · photo d'illustration : le plat peut différer de la recette ATLAS</>}
    </p>
  );
}
