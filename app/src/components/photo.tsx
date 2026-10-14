import { useState } from "react";
import imagesJson from "../data/images.json";

// Photos d'illustration (illustrations/process.py) : WebP en 400/800/1200 px, recadrées 4:3, étalonnées,
// avec la couleur dominante comme fond pendant le chargement et le crédit de l'auteur·e (licences libres).
export interface PhotoMeta {
  path: string; sizes: number[]; color: string; author: string; license: string; licenseUrl: string;
  page: string; source: string; title: string; kind: "photo" | "ia";
}
export const IMAGES = imagesJson as unknown as Record<string, PhotoMeta>;
export const photoOf = (key: string): PhotoMeta | undefined => IMAGES[key];

/** <img> responsive ; `sizes` décrit la largeur affichée pour que le téléphone ne télécharge que la taille utile. */
export function Photo({ k, alt, sizes = "(min-width: 900px) 33vw, 100vw", className = "", eager = false }: { k: string; alt: string; sizes?: string; className?: string; eager?: boolean }) {
  const m = IMAGES[k];
  const [loaded, setLoaded] = useState(false);
  const [failed, setFailed] = useState(false);
  if (!m || failed) return null;
  const srcSet = m.sizes.map((w) => `./${m.path}-${w}.webp ${w}w`).join(", ");
  return (
    <img
      className={`photo ${loaded ? "loaded" : ""} ${className}`}
      src={`./${m.path}-${m.sizes[Math.min(1, m.sizes.length - 1)]}.webp`}
      srcSet={srcSet} sizes={sizes} alt={alt} width={4} height={3}
      loading={eager ? "eager" : "lazy"} decoding="async" style={{ backgroundColor: m.color }}
      onLoad={() => setLoaded(true)} onError={() => setFailed(true)}
    />
  );
}

/** Crédit obligatoire (CC BY / BY-SA) : auteur·e, licence, lien vers l'original. */
export function Credit({ k, note = true }: { k: string; note?: boolean }) {
  const m = IMAGES[k];
  if (!m) return null;
  return (
    <p className="credit">
      {m.kind === "ia" ? "Image générée par IA (ATLAS)" : <>Photo : {m.author}, <a href={m.licenseUrl || m.page} target="_blank" rel="noopener noreferrer">{m.license}</a>, via <a href={m.page} target="_blank" rel="noopener noreferrer">{m.source}</a></>}
      {note && <> · photo d'illustration : le plat peut différer de la recette ATLAS</>}
    </p>
  );
}
