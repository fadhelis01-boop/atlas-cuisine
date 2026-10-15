// Saisonnalité (Tome 13 §9) : le menu du jour suit les saisons du lieu où l'application est utilisée.
// Le lieu n'est jamais demandé ni envoyé : on déduit la zone du fuseau horaire de l'appareil (Intl), et l'utilisateur
// peut la corriger dans son profil. Calendrier des produits = récolte locale en France métropolitaine (Tome 3,
// dictionnaire) ; hémisphère sud : décalé de 6 mois ; zone tropicale : pas d'hiver, on privilégie le frais et les
// produits tropicaux toute l'année.
import { INGREDIENTS } from "./data";
import type { Recipe } from "./types";
import { norm } from "./text";

export type Zone = "nord" | "sud" | "tropical";
export type ZoneSetting = "auto" | Zone;

const SOUTH = /^(Australia|Antarctica)\/|^Pacific\/(Auckland|Chatham)|^America\/(Argentina|Santiago|Montevideo|Asuncion|Sao_Paulo|Punta_Arenas)|^Africa\/(Johannesburg|Maseru|Mbabane|Windhoek|Gaborone)|^Atlantic\/(Stanley|South_Georgia)|^Indian\/Kerguelen/;
const TROPICAL = /^America\/(Martinique|Guadeloupe|Cayenne|Port_of_Spain|Barbados|Santo_Domingo|Puerto_Rico|Havana|Jamaica|Port-au-Prince|Panama|Bogota|Caracas|Guayaquil|Lima|Manaus|Belem|Fortaleza|Recife|Bahia|Cancun|Merida|Belize|Guatemala|El_Salvador|Tegucigalpa|Managua|Costa_Rica|St_|Anguilla|Antigua|Aruba|Curacao|Dominica|Grenada|Marigot|Montserrat|Tortola|Lower_Princes|Kralendijk|Paramaribo|Guyana)|^Indian\/(Reunion|Mayotte|Mauritius|Comoro|Antananarivo|Maldives|Mahe|Chagos)|^Pacific\/(Tahiti|Noumea|Wallis|Fiji|Apia|Port_Moresby|Guadalcanal|Efate|Tongatapu|Marquesas|Gambier|Honolulu|Guam|Palau)|^Africa\/(Dakar|Abidjan|Bamako|Conakry|Lome|Lagos|Accra|Ouagadougou|Niamey|Douala|Libreville|Kinshasa|Brazzaville|Lubumbashi|Bangui|Ndjamena|Malabo|Sao_Tome|Porto-Novo|Banjul|Bissau|Freetown|Monrovia|Nouakchott|Addis_Ababa|Nairobi|Kampala|Dar_es_Salaam|Kigali|Bujumbura|Mogadishu|Djibouti|Asmara|Khartoum|Juba|Luanda|Lusaka|Harare|Blantyre|Maputo)|^Asia\/(Bangkok|Ho_Chi_Minh|Saigon|Phnom_Penh|Vientiane|Jakarta|Makassar|Jayapura|Pontianak|Manila|Kuala_Lumpur|Singapore|Brunei|Colombo|Kolkata|Calcutta|Dhaka|Yangon|Rangoon|Dili)/;

/** Zone déduite du fuseau horaire de l'appareil (aucune donnée envoyée). */
export function detectZone(): Zone {
  let tz = "";
  try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone || ""; } catch { /* navigateur ancien */ }
  if (TROPICAL.test(tz)) return "tropical";
  if (SOUTH.test(tz)) return "sud";
  return "nord";
}
export const zoneOf = (s: ZoneSetting | undefined): Zone => (!s || s === "auto" ? detectZone() : s);
export const ZONE_LABEL: Record<Zone, string> = {
  nord: "Hémisphère nord tempéré (France métropolitaine, Europe, Maghreb, Amérique du Nord, Asie de l'Est)",
  sud: "Hémisphère sud tempéré (Australie, Nouvelle-Zélande, Afrique du Sud, Argentine, Chili…) : saisons inversées",
  tropical: "Zone tropicale (Antilles, Guyane, Réunion, Mayotte, Polynésie, Afrique de l'Ouest et centrale, Asie du Sud-Est…)",
};

/** Mois « équivalent France » : dans l'hémisphère sud, janvier correspond à juillet. */
export const localMonth = (zone: Zone, d = new Date()) => (zone === "sud" ? ((d.getMonth() + 6) % 12) + 1 : d.getMonth() + 1);
export type Season = "hiver" | "printemps" | "ete" | "automne" | "tropiques";
export function seasonOf(zone: Zone, d = new Date()): Season {
  if (zone === "tropical") return "tropiques";
  const m = localMonth(zone, d);
  return m === 12 || m <= 2 ? "hiver" : m <= 5 ? "printemps" : m <= 8 ? "ete" : "automne";
}
export const SEASON_LABEL: Record<Season, string> = { hiver: "hiver", printemps: "printemps", ete: "été", automne: "automne", tropiques: "saison chaude toute l'année" };

const COMFORT = /soupe|veloute|potage|bouillon|harira|chorba|bortsch|garbure|pot-au-feu|daube|bourguignon|blanquette|navarin|cassoulet|tartiflette|fondue|raclette|aligot|truffade|gratin|hachis|parmentier|goulash|carbonade|baeckeoffe|choucroute|mijot|ragout|stew|joue|souris|7 heures|sept heures|confit|lasagne|moussaka|chili|curry|dal|ramen|pho|chocolat chaud|chai|lait d.or|tajine|couscous|mafe|ndole|rendang/;
const FRESH = /salade|gaspacho|gazpacho|ceviche|tartare|carpaccio|poke|taboule|fattouche|panzanella|pan bagnat|crudit|sorbet|glace|granite|smoothie|limonade|citronnade|mojito|agua|the glace|horchata|bissap|ginger|brochette|grill|barbecue|plancha|souvlaki|kofta|poisson cru|kokoda|som tam|rouleaux de printemps|bo bun|tzatziki|raita|elote|pico/;
const TROPICAL_PRODUCE = new Set(["Mangue", "Ananas", "Banane", "Plantain (banane à cuire)", "Papaye", "Fruit de la passion", "Goyave / litchi", "Noix de coco fraîche", "Lait de coco / crème de coco",
  "Citron vert", "Patate douce", "Igname", "Taro / madère", "Manioc / yuca", "Chayotte / christophine", "Gombo (okra)", "Piment antillais / scotch bonnet", "Avocat", "Gingembre frais", "Citronnelle"]);

export interface SeasonFit { score: number; inSeason: string[]; outSeason: string[]; mood: "chaud" | "frais" | null }

/** Adéquation d'une recette à la saison : produits de saison (+), hors saison (−), plat réconfortant ou frais selon le climat. */
export function seasonFit(r: Recipe, zone: Zone, d = new Date()): SeasonFit {
  const m = localMonth(zone, d);
  const s = seasonOf(zone, d);
  let score = 0; const inSeason: string[] = []; const outSeason: string[] = [];
  for (const l of r.ingredients) {
    if (!l.ref || l.ref.startsWith("SUB:") || l.optional) continue;
    const ing = INGREDIENTS[l.ref];
    if (zone === "tropical") { if (TROPICAL_PRODUCE.has(l.ref) && l.weight >= 1) { score += 1.5; inSeason.push(l.ref); } continue; }
    if (!ing?.season?.length || l.weight < 1) continue;
    if (ing.season.includes(m)) { score += l.weight >= 2 ? 2 : 1; inSeason.push(l.ref); }
    else if (l.weight >= 2) { score -= l.weight === 3 ? 3.5 : 2; outSeason.push(l.ref); }
  }
  const t = norm(r.title);
  const comfort = COMFORT.test(t) || (r.role === "plat" && r.rest >= 90);
  const fresh = FRESH.test(t) || r.profile.includes("leger") && r.role === "entree";
  let mood: SeasonFit["mood"] = null;
  if (s === "hiver") { if (comfort) { score += 3; mood = "chaud"; } if (fresh && !comfort) score -= 2; }
  if (s === "automne") { if (comfort) { score += 1.5; mood = "chaud"; } }
  if (s === "ete" || s === "tropiques") { if (fresh) { score += 3; mood = "frais"; } if (comfort && /soupe|veloute|fondue|raclette|tartiflette|pot-au-feu|choucroute|aligot|chocolat chaud/.test(t)) score -= 3; }
  if (s === "printemps" && fresh) score += 1;
  return { score, inSeason: [...new Set(inSeason)], outSeason: [...new Set(outSeason)], mood };
}

/** Produits de saison du mois pour la zone (fruits, légumes, herbes, poissons et fromages qui ont un calendrier). */
export function marketOfMonth(zone: Zone, d = new Date()): string[] {
  if (zone === "tropical") return [...TROPICAL_PRODUCE].filter((n) => INGREDIENTS[n]);
  const m = localMonth(zone, d);
  return Object.entries(INGREDIENTS).filter(([, v]) => v.season?.includes(m) && v.season.length <= 9).map(([n]) => n);
}

export const MONTHS = ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."];
export const MONTHS_FULL = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"];
