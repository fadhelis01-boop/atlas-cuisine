// « Je n'ai pas d'idée, propose-moi » (audit UX 🟠 6) : trois suggestions en un geste, selon l'heure,
// la saison du lieu, le temps disponible et ce qu'il y a dans le frigo. Trois cuisines différentes.
import { flatten } from "./engine";
import { seasonFit, type Zone } from "./season";
import type { Recipe } from "./types";

export interface Proposal { r: Recipe; why: string[] }

/** Le moment de la journée décide du type de recette : plat aux repas, goûter l'après-midi et le matin. */
export function momentOf(hour: number): { label: string; test: (r: Recipe) => boolean } {
  const plat = (r: Recipe) => r.role === "plat";
  const sweet = (r: Recipe) => r.role === "dessert" || r.kind === "Goûter / dessert" || (r.role === "boisson" && r.kind !== "Sauce");
  if (hour >= 5 && hour < 11) return { label: "pour le petit-déjeuner ou le brunch", test: (r) => sweet(r) && r.active <= 25 };
  if (hour >= 14 && hour < 18) return { label: "pour le goûter", test: sweet };
  if (hour >= 23 || hour < 5) return { label: "pour une petite faim", test: (r) => plat(r) && r.active + r.rest <= 25 };
  return { label: hour < 14 ? "pour midi" : "pour ce soir", test: plat };
}

export function propose(list: Recipe[], o: { hour: number; zone: Zone; maxMinutes: number; fridge: string[]; seed: number }): Proposal[] {
  const m = momentOf(o.hour);
  const fridge = new Set(o.fridge);
  let rnd = (o.seed % 2147483647) || 11;
  const random = () => (rnd = (rnd * 16807) % 2147483647) / 2147483647;
  const scored = list.filter((r) => m.test(r) && r.active + r.rest <= o.maxMinutes).map((r) => {
    const fit = seasonFit(r, o.zone);
    const used = [...new Set(flatten(r.ingredients).filter((l) => l.ref && fridge.has(l.ref) && l.weight >= 1).map((l) => l.ref!))];
    return { r, fit, used, score: fit.score * 1.5 + used.length * 2.5 + random() * 3 };
  }).sort((a, b) => b.score - a.score);
  const out: Proposal[] = [];
  for (const x of scored) {
    if (out.length === 3) break;
    if (out.some((p) => p.r.macro === x.r.macro)) continue; // trois cuisines différentes
    const why: string[] = [];
    if (x.used.length) why.push(`🧊 avec ton ${x.used.slice(0, 2).map((n) => n.split(/ \/ | \(/)[0].toLowerCase()).join(" et ")}`);
    if (x.fit.inSeason.length) why.push(`🌱 ${x.fit.inSeason.slice(0, 2).map((n) => n.split(/ \/ | \(/)[0].toLowerCase()).join(", ")} de saison`);
    else if (x.fit.mood) why.push(x.fit.mood === "chaud" ? "🔥 réconfortant" : "❄️ frais");
    why.push(`⏱ ${x.r.active + x.r.rest} min en tout`);
    out.push({ r: x.r, why });
  }
  return out;
}
