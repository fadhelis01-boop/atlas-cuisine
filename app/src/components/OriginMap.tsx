// Pictogramme « carte du monde » de chaque fiche : le pays d'origine en couleur, un point pour la région ou le petit
// territoire (12/11/2026). La carte (≈ 40 Ko compressés) n'est chargée qu'à l'ouverture d'une fiche, une seule fois.
import { useEffect, useState } from "react";
import { origineOf } from "../lib/origine";
import type { Recipe } from "../lib/types";

interface WorldMap { w: number; h: number; d: Record<string, string>; c: Record<string, [number, number]>; pts: Record<string, [number, number]> }
let cache: WorldMap | null = null;
let pending: Promise<WorldMap> | null = null;
const load = () => (pending ??= import("../data/worldmap.json").then((m) => (cache = (m.default ?? m) as unknown as WorldMap)));

export default function OriginMap({ r }: { r: Pick<Recipe, "regionPath" | "macro" | "title"> }) {
  const [map, setMap] = useState<WorldMap | null>(cache);
  const [big, setBig] = useState(false);
  useEffect(() => { if (!map) load().then(setMap).catch(() => undefined); }, [map]);
  if (!map) return <span className="origin-map placeholder" aria-hidden="true" />;
  const o = origineOf(r, map.pts);
  const on = new Set(o.countries);
  const dot = o.point ? map.pts[o.point] : o.countries.length === 1 && map.c[o.countries[0]] ? map.c[o.countries[0]] : null;
  const where = o.point && o.point !== o.label ? `${o.point} (${o.label})` : o.label;
  const text = o.wide ? `Cuisine de toute la région : ${where}` : `Origine : ${where}`;
  return (
    <button type="button" className={`origin-map${big ? " big" : ""}`} onClick={() => setBig(!big)} aria-pressed={big} aria-label={`${text}. ${big ? "Réduire" : "Agrandir"} la carte`} title={text}>
      <svg viewBox={`0 0 ${map.w} ${map.h}`} role="img" aria-hidden="true" focusable="false">
        {Object.entries(map.d).map(([name, d]) => <path key={name} d={d} className={on.has(name) ? (o.wide ? "om-wide" : "om-on") : "om-land"} />)}
        {dot && <><circle cx={dot[0]} cy={dot[1]} r={big ? 5 : 11} className="om-halo" /><circle cx={dot[0]} cy={dot[1]} r={big ? 2.4 : 5.5} className="om-dot" /></>}
      </svg>
      {big && <span className="om-label">{text}</span>}
    </button>
  );
}
