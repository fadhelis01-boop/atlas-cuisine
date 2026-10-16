// L'équipement du profil sert enfin à quelque chose (audit famille 2026-10-16) : sur une fiche, ce qu'on fait sans tel
// appareil, et la cuisson express quand on a un autocuiseur. Repères de cuisinier, NON TESTÉS (Tome 7 §2).
import { norm } from "./text";
import type { Profile, Recipe } from "./types";

export const EQUIPEMENTS: [string, string][] = [
  ["four", "Four"], ["plaques", "Plaques (gaz, induction, vitro)"], ["poele", "Poêle"], ["casserole", "Casseroles"], ["cocotte", "Cocotte en fonte"],
  ["autocuiseur", "Autocuiseur (Cocotte-Minute)"], ["mijoteuse", "Mijoteuse"], ["microondes", "Micro-ondes"],
  ["mixeur", "Mixeur plongeur"], ["robot", "Robot pétrisseur"], ["airfryer", "Airfryer"], ["wok", "Wok"], ["thermometre", "Thermomètre de cuisson"],
];

const SANS: [string, RegExp, string][] = [
  ["four", /\bfour\b/, "Pas de four : cette recette en a besoin pour cuire ; choisis-en une autre ou cuis à la cocotte couverte sur feu doux quand c'est un mijoté."],
  ["wok", /\bwok\b/, "Pas de wok : ta plus grande poêle, très chaude, et cuis en deux fois pour que ça saisisse au lieu de bouillir."],
  ["thermometre", /thermom/, "Pas de thermomètre : suis les repères des étapes (jus clair, couleur, bulles) et coupe un morceau au centre en cas de doute."],
  ["robot", /robot/, "Pas de robot : pétris à la main, 10 min de plus, jusqu'à ce que la pâte soit lisse et se détache des doigts."],
  ["mixeur", /mixeur|blender/, "Pas de mixeur : presse-purée, fourchette ou moulin à légumes ; la texture sera plus rustique."],
  ["cocotte", /cocotte/, "Pas de cocotte en fonte : un faitout à fond épais, couvercle bien fermé, feu plus doux."],
];

/** Notes d'équipement à afficher sous « Matériel » (seulement pour ce qui manque ou ce qui aide). */
export function equipmentNotes(r: Recipe, p: Profile): string[] {
  const eq = norm(`${r.equipment} ${r.steps.join(" ")}`);
  const out = SANS.filter(([k, rx]) => !p.equipment.includes(k) && rx.test(eq)).map(([, , t]) => t);
  if (p.equipment.includes("autocuiseur")) {
    const tip = r.tips.find((t) => /autocuiseur/i.test(t));
    if (tip) out.unshift(`Avec ton autocuiseur : ${tip.replace(/\*\*Autocuiseur\*\*\s*:\s*/i, "").replace(/\*\*/g, "")}`);
  }
  if (p.equipment.includes("mijoteuse") && r.active + r.rest >= 120 && /mijot|frem|feu (tres )?doux/.test(eq)) out.push("Avec ta mijoteuse : après l'étape où l'on saisit, tout dans la cuve, position basse 8 h ou haute 4 h ; réduis la sauce à la casserole si elle est trop liquide.");
  return out;
}
