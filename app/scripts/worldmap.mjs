// Génère src/data/worldmap.json : la carte du monde du pictogramme « pays d'origine » de chaque fiche.
// Source : Natural Earth 1:110m (domaine public) via le paquet world-atlas ; projection Natural Earth, Antarctique retirée,
// chemins arrondis au dixième. Les petits pays absents du 1:110m (Singapour, Samoa…) et les régions (Bretagne, Sichuan…)
// sont des points. Usage : node scripts/worldmap.mjs (à relancer seulement si POINTS change).
import { readFileSync, writeFileSync } from "node:fs";
import { feature } from "topojson-client";
import { geoNaturalEarth1, geoPath, geoCentroid, geoArea } from "d3-geo";

const W = 360, H = 175;
const topo = JSON.parse(readFileSync(new URL("../node_modules/world-atlas/countries-110m.json", import.meta.url)));
const fc = feature(topo, topo.objects.countries);
fc.features = fc.features.filter((f) => f.properties.name !== "Antarctica" && f.properties.name !== "Fr. S. Antarctic Lands");
const proj = geoNaturalEarth1().fitExtent([[2, 2], [W - 2, H - 2]], fc);
const path = geoPath(proj).digits(1);

// régions et petits territoires : [latitude, longitude]
export const POINTS = {
  // France métropolitaine et outre-mer
  "Bretagne": [48.2, -2.9], "Normandie": [49.1, 0], "Hauts-de-France": [50, 2.8], "Île-de-France": [48.85, 2.35], "Grand Est": [48.6, 5.8],
  "Bourgogne-Franche-Comté": [47.2, 4.8], "Centre-Val de Loire": [47.5, 1.7], "Pays de la Loire": [47.4, -0.8], "Nouvelle-Aquitaine": [45.2, 0.2],
  "Occitanie": [43.7, 2.2], "Auvergne-Rhône-Alpes": [45.5, 4.5], "Provence-Alpes-Côte d'Azur": [43.9, 6.1], "Corse": [42.1, 9],
  "Antilles": [15.5, -61.3], "Martinique": [14.64, -61], "Guadeloupe": [16.25, -61.55], "Réunion": [-21.1, 55.5], "La Réunion": [-21.1, 55.5],
  "Guyane": [4, -53], "Mayotte": [-12.8, 45.15], "Polynésie française": [-17.65, -149.4], "Tahiti": [-17.65, -149.4],
  // petits pays et territoires
  "Singapour": [1.35, 103.82], "Hong Kong": [22.3, 114.17], "Samoa": [-13.8, -172.1], "Tonga": [-21.2, -175.2], "Hawaï": [20.8, -156.3],
  "Maurice": [-20.2, 57.5], "Cap-Vert": [15.1, -23.6], "Malte": [35.9, 14.4], "Caraïbes": [18, -72],
  // régions d'Asie
  "Shanghai": [31.2, 121.5], "Sichuan": [30.6, 104], "Canton": [23.1, 113.3], "Hunan": [28.2, 112.9], "Xinjiang": [41.8, 85], "Pékin": [39.9, 116.4],
  "Dongbei": [45, 126], "Chine du Nord": [38, 114], "Yunnan": [25, 101.5], "Osaka": [34.7, 135.5], "Tokyo": [35.7, 139.7], "Hokkaido": [43.1, 142.6], "Okinawa": [26.3, 127.8],
  "Goa": [15.4, 74], "Cachemire": [34.1, 74.8], "Tamil Nadu": [11.1, 78.6], "Maharashtra": [19.7, 75.7], "Karnataka": [15.3, 75.7], "Kerala": [10.5, 76.3],
  "Pendjab": [31, 75.3], "Bengale": [22.9, 88], "Gujarat": [22.3, 71.2], "Rajasthan": [26.9, 73.8], "Saïgon": [10.8, 106.7], "Hanoï": [21, 105.85], "Huế": [16.46, 107.6],
  "Penang": [5.4, 100.3], "Isan": [15.5, 103.5], "Bali": [-8.4, 115.2], "Java": [-7.3, 110], "Sumatra": [0.5, 101.5],
  // régions d'Europe et des Amériques
  "Sicile": [37.5, 14], "Campanie": [40.85, 14.25], "Pouilles": [41, 16.5], "Vénétie": [45.4, 12.3], "Toscane": [43.4, 11.1], "Ligurie": [44.3, 8.9],
  "Émilie-Romagne": [44.5, 11.3], "Latium": [41.9, 12.5], "Piémont": [45, 7.9], "Lombardie": [45.6, 9.7], "Sardaigne": [40, 9], "Rome": [41.9, 12.5], "Naples": [40.85, 14.25],
  "Baléares": [39.6, 2.9], "Pays basque": [43.2, -2.4], "Andalousie": [37.4, -5], "Catalogne": [41.6, 1.6], "Galice": [42.8, -8], "Valence": [39.5, -0.4],
  "Louisiane": [30.9, -92], "Nouvelle-Angleterre": [43.5, -71.5], "Sud": [33, -86], "Sud-Ouest": [34, -108], "Québec": [46.8, -71.2],
};

const d = {}, c = {};
for (const f of fc.features) {
  const name = f.properties.name;
  const p = path(f);
  if (!p) continue;
  d[name] = p;
  // centroïde du plus grand morceau (la France ne doit pas glisser vers la Guyane)
  let best = f;
  if (f.geometry.type === "MultiPolygon") {
    const parts = f.geometry.coordinates.map((co) => ({ type: "Feature", geometry: { type: "Polygon", coordinates: co } }));
    best = parts.sort((a, b) => geoArea(b) - geoArea(a))[0];
  }
  c[name] = proj(geoCentroid(best)).map((v) => Math.round(v * 10) / 10);
}
// fond de carte en un seul tracé (vignettes des fiches : un seul <symbol> partagé, cf. OriginMap.tsx)
const landTopo = JSON.parse(readFileSync(new URL("../node_modules/world-atlas/land-110m.json", import.meta.url)));
const landFc = feature(landTopo, landTopo.objects.land);
const land = geoPath(proj).digits(0)({ type: "FeatureCollection", features: landFc.features.map((f) => ({ ...f, geometry: { ...f.geometry,
  coordinates: f.geometry.type === "MultiPolygon" ? f.geometry.coordinates.filter((p) => p[0].every(([, lat]) => lat > -60)) : f.geometry.coordinates } })) });
const pts = Object.fromEntries(Object.entries(POINTS).map(([k, [lat, lon]]) => [k, proj([lon, lat]).map((v) => Math.round(v * 10) / 10)]));
writeFileSync(new URL("../src/data/worldmap.json", import.meta.url), JSON.stringify({ w: W, h: H, d, c, pts, land }));
console.log("worldmap.json :", Object.keys(d).length, "pays,", Object.keys(pts).length, "points,", JSON.stringify({ d, c, pts, land }).length, "octets");
