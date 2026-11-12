// Pays d'origine d'une fiche, pour le pictogramme « carte du monde » (12/11/2026). Les libellés de région (en français)
// sont ramenés aux noms de pays de la carte Natural Earth (src/data/worldmap.json, en anglais) ; une région ou un petit
// territoire absent de la carte devient un point (POINTS de scripts/worldmap.mjs). Une étiquette sans pays (« Food fusion »,
// « Cuisine de base ») montre la grande région culinaire entière.
import type { Recipe } from "./types";

const P = (...c: string[]) => c;
export const COUNTRY: Record<string, string[]> = {
  // Afrique
  "Afrique du Sud": P("South Africa"), "Cameroun": P("Cameroon"), "Congo (RDC)": P("Dem. Rep. Congo"), "RD Congo": P("Dem. Rep. Congo"),
  "Côte d'Ivoire": P("Côte d'Ivoire"), "Ghana": P("Ghana"), "Guinée": P("Guinea"), "Kenya": P("Kenya"), "Madagascar": P("Madagascar"), "Mali": P("Mali"),
  "Mozambique": P("Mozambique"), "Nigeria": P("Nigeria"), "Ouganda": P("Uganda"), "Sénégal": P("Senegal"), "Tanzanie": P("Tanzania"), "Togo": P("Togo"),
  "Éthiopie": P("Ethiopia"), "Bénin": P("Benin"), "Burkina Faso": P("Burkina Faso"), "Gabon": P("Gabon"), "Congo": P("Congo"), "Angola": P("Angola"),
  "Afrique de l'Ouest": P("Senegal", "Mali", "Côte d'Ivoire", "Ghana", "Togo", "Benin", "Nigeria", "Burkina Faso", "Guinea", "Niger",
     "Gambia", "Guinea-Bissau", "Sierra Leone", "Liberia", "Mauritania"),
  // Amériques
  "Argentine": P("Argentina"), "Brésil": P("Brazil"), "Chili": P("Chile"), "Colombie": P("Colombia"), "Costa Rica": P("Costa Rica"), "Cuba": P("Cuba"),
  "Haïti": P("Haiti"), "Jamaïque": P("Jamaica"), "Mexique": P("Mexico"), "Pérou": P("Peru"), "Salvador": P("El Salvador"), "Suriname": P("Suriname"),
  "Trinité-et-Tobago": P("Trinidad and Tobago"), "Venezuela": P("Venezuela"), "Porto Rico": P("Puerto Rico"), "République dominicaine": P("Dominican Rep."),
  "Caraïbes": P("Cuba", "Jamaica", "Haiti", "Dominican Rep.", "Puerto Rico", "Trinidad and Tobago"), "Canada": P("Canada"), "États-Unis": P("United States of America"),
  "Hawaï": P("United States of America"),
  // Asie
  "Chine": P("China"), "Corée": P("South Korea"), "Japon": P("Japan"), "Mongolie": P("Mongolia"), "Taïwan": P("Taiwan"), "Bangladesh": P("Bangladesh"),
  "Inde": P("India"), "Népal": P("Nepal"), "Ouzbékistan": P("Uzbekistan"), "Pakistan": P("Pakistan"), "Sri Lanka": P("Sri Lanka"), "Birmanie": P("Myanmar"),
  "Cambodge": P("Cambodia"), "Indonésie": P("Indonesia"), "Laos": P("Laos"), "Malaisie": P("Malaysia"), "Philippines": P("Philippines"),
  "Thaïlande": P("Thailand"), "Vietnam": P("Vietnam"), "Afghanistan": P("Afghanistan"), "Tibet": P("China"),
  // Europe
  "Allemagne": P("Germany"), "Autriche": P("Austria"), "Belgique": P("Belgium"), "Danemark": P("Denmark"), "Finlande": P("Finland"), "Géorgie": P("Georgia"),
  "Hongrie": P("Hungary"), "Irlande": P("Ireland"), "Norvège": P("Norway"), "Pays-Bas": P("Netherlands"), "Pologne": P("Poland"), "Roumanie": P("Romania"),
  "Royaume-Uni": P("United Kingdom"), "Russie": P("Russia"), "Suisse": P("Switzerland"), "Suède": P("Sweden"), "Ukraine": P("Ukraine"), "Chypre": P("Cyprus"),
  "Espagne": P("Spain"), "Grèce": P("Greece"), "Italie": P("Italy"), "Portugal": P("Portugal"), "Serbie": P("Serbia"), "Croatie": P("Croatia"), "Islande": P("Iceland"),
  "Tchéquie": P("Czechia"), "Bulgarie": P("Bulgaria"), "Arménie": P("Armenia"), "Luxembourg": P("Luxembourg"),
  "Balkans": P("Serbia", "Croatia", "Bosnia and Herz.", "Montenegro", "Macedonia", "Albania", "Bulgaria", "Kosovo"),
  "France": P("France"), "Sauces de snack (France, Belgique)": P("France", "Belgium"),
  // Maghreb, Moyen-Orient
  "Algérie": P("Algeria"), "Maroc": P("Morocco"), "Tunisie": P("Tunisia"), "Égypte": P("Egypt"), "Libye": P("Libya"), "Maghreb": P("Algeria", "Morocco", "Tunisia"),
  "Arabie saoudite": P("Saudi Arabia"), "Irak": P("Iraq"), "Iran": P("Iran"), "Israël": P("Israel"), "Jordanie": P("Jordan"), "Liban": P("Lebanon"),
  "Palestine": P("Palestine"), "Syrie": P("Syria"), "Turquie": P("Turkey"), "Yémen": P("Yemen"), "Levant": P("Lebanon", "Syria", "Jordan", "Palestine", "Israel"),
  // Océanie
  "Australie": P("Australia"), "Fidji": P("Fiji"), "Nouvelle-Calédonie": P("New Caledonia"), "Nouvelle-Zélande": P("New Zealand"),
  "Papouasie-Nouvelle-Guinée": P("Papua New Guinea"), "Vanuatu": P("Vanuatu"),
};

// grande région culinaire entière, quand la fiche n'a pas de pays (fusion, bases, recettes régionales larges)
export const MACRO_COUNTRIES: Record<string, string[]> = {
  france: P("France"), europe_sud: P("Italy", "Spain", "Portugal", "Greece", "Cyprus"), europe_nord: P("United Kingdom", "Germany", "Belgium", "Netherlands", "Sweden", "Norway", "Denmark", "Poland"),
  maghreb: P("Algeria", "Morocco", "Tunisia", "Libya", "Egypt"), afrique: COUNTRY["Afrique de l'Ouest"],
  moyen_orient: P("Lebanon", "Syria", "Turkey", "Iran", "Iraq", "Jordan", "Israel", "Palestine"),
  asie_est: P("China", "Japan", "South Korea", "Taiwan", "Mongolia"), asie_sud: P("India", "Pakistan", "Nepal", "Bangladesh", "Sri Lanka"),
  asie_sud_est: P("Thailand", "Vietnam", "Laos", "Cambodia", "Malaysia", "Indonesia", "Philippines", "Myanmar"), amerique_nord: P("United States of America", "Canada"),
  amerique_latine: P("Mexico", "Peru", "Brazil", "Argentina", "Colombia", "Cuba"), oceanie: P("Australia", "New Zealand", "Fiji"), fusion: [],
};

export interface Origine { countries: string[]; point: string | null; label: string; wide: boolean }

/** Pays (noms de la carte) et point précis d'une fiche. */
export function origineOf(r: Pick<Recipe, "regionPath" | "macro">, points?: Record<string, unknown>): Origine {
  const path = r.regionPath.map((s) => s.trim());
  let countries: string[] = [], label = "";
  for (const seg of path) if (COUNTRY[seg]) { countries = COUNTRY[seg]; label = seg; }
  // « Italie (Sicile) » si une région a gardé l'ancienne forme
  if (!countries.length) for (const seg of path) { const m = /^(.+?) \((.+)\)$/.exec(seg); if (m && COUNTRY[m[1]]) { countries = COUNTRY[m[1]]; label = m[1]; } }
  if (!countries.length && path[0] === "France") { countries = COUNTRY.France; label = "France"; }
  let point: string | null = null;
  if (points) for (const seg of [...path].reverse()) {
    const inner = /\((.+)\)$/.exec(seg)?.[1];
    if (points[seg] !== undefined) { point = seg; break; }
    if (inner && points[inner] !== undefined) { point = inner; break; }
  }
  if (point && !countries.length) label = point;
  const wide = !countries.length && !point;
  if (wide) { countries = MACRO_COUNTRIES[r.macro] ?? []; label = path[0] ?? ""; }
  return { countries, point, label, wide };
}
