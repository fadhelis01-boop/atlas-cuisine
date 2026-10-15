// Aide au débutant (audit 🔴 2) : sel dosé et repères visuels, calculés pour toutes les fiches.
// Le sel : environ 1,2 g par portion de plat (0,8 g pour une entrée), moitié moins si la recette contient déjà
// des ingrédients salés. Ce sont des repères de départ, à ajuster en goûtant. NON TESTÉ en cuisine (Tome 7 §2).
import { flatten } from "./engine";
import { norm } from "./text";
import type { Recipe } from "./types";

const SALTY = /sauce soja|soja|nuoc|nam pla|poisson \(sauce|anchois|lardons|jambon|bacon|chorizo|pancetta|feta|parmesan|pecorino|roquefort|olive|capre|bouillon cube|cube|morue salee|halloumi|miso|kimchi|fromage|saucisse|merguez|pastrami|cornichon|citron confit/;

export interface SaltDose { text: string; grams: number; water: boolean }

/** Dose de sel indicative pour une fiche salée qui n'en indique pas (null si la fiche dose déjà, ou n'est pas salée). */
export function saltDose(r: Recipe, portions = r.portions): SaltDose | null {
  if (!(r.role === "plat" || r.role === "entree" || /Accompagnement/.test(r.kind))) return null;
  const lines = flatten(r.ingredients);
  if (lines.some((l) => l.ref?.startsWith("Sel"))) return null;
  const salty = lines.some((l) => SALTY.test(norm(`${l.ref ?? ""} ${l.label}`)));
  const per = (r.role === "entree" ? 0.8 : 1.2) * (salty ? 0.5 : 1);
  const grams = Math.max(0.5, Math.round(per * portions * 2) / 2);
  const steps = norm(r.steps.join(" "));
  const water = /eau (bouillante )?salee|pates|spaghetti|nouilles|blanchi|eau bouillante/.test(steps);
  const spoon = grams >= 4.5 ? `${Math.round(grams / 5 * 2) / 2} c. à c. rase`.replace(".5", " ½").replace(/^0 ½/, "½") : grams >= 2 ? "½ c. à c. rase" : grams >= 1 ? "2 pincées" : "1 pincée";
  const text = `${spoon} (≈ ${String(grams).replace(".", ",")} g)${salty ? " : la recette contient déjà des ingrédients salés, goûte avant d'en ajouter" : ""}. Un tiers en début de cuisson, le reste à la fin en goûtant.`;
  return { text, grams, water };
}

// Repères visuels : ce qu'on doit voir, sentir ou entendre pour savoir que le geste est réussi.
const CUES: [RegExp, string][] = [
  [/fais (suer|fondre) (l |les |un |une )?(oignon|echalote|poireau)|oignons? (fondu|translucide)|fais revenir l oignon/, "Oignon prêt : translucide et souple, sans coloration (5 à 8 min à feu moyen)."],
  [/caramelis(e|er) (les |l )?oignon|oignons? (bien )?(dore|caramelise|confit)/, "Oignons caramélisés : brun doré, fondants, 20 à 30 min à feu doux ; ajoute un fond d'eau s'ils attachent."],
  [/fremi|fremissement/, "Frémissement : de petites bulles éclatent doucement à la surface, sans gros bouillons."],
  [/ebullition|porte a ebullition|bouillir/, "Ébullition : de grosses bulles qui continuent même quand tu remues."],
  [/reduis|reduire|reduction|nappe/, "Sauce assez réduite : elle nappe le dos d'une cuillère et ton doigt y laisse une trace nette."],
  [/dore|dorer|colore|saisis|saisir/, "Bien doré : une croûte brun noisette ; ne bouge pas la pièce avant qu'elle se décolle seule de la poêle."],
  [/al dente/, "Al dente : goûte 1 min avant le temps du paquet, le centre doit encore résister sous la dent."],
  [/enfourne|au four|gratine/, "Cuit au four : dessus doré, bords qui bouillonnent ; la pointe d'un couteau entre sans résistance."],
  [/pate (lisse|souple|homogene)|petri/, "Pâte bien pétrie : lisse, souple, elle se détache des parois et reprend sa forme quand tu l'appuies."],
  [/double de volume|laisse pousser|\bleve(e|r)?\b|laisse lever|pointage/, "Pousse finie : la pâte a doublé ; un doigt fariné y laisse un creux qui remonte lentement."],
  [/monte(r)? (les )?blancs|neige ferme|bec d oiseau/, "Blancs fermes : ils ne glissent pas quand tu retournes le bol et forment un bec qui tient."],
  [/emulsion|mayonnaise|vinaigrette|monte au beurre/, "Émulsion réussie : brillante, homogène, sans gouttes d'huile en surface."],
  [/(un|le|en) caramel|caramel (blond|ambre)|cuis le sucre|sucre (fond|blond)/, "Caramel prêt : couleur ambrée, odeur de noisette ; au-delà (brun foncé, fumée) il devient amer."],
  [/a coeur|thermometre|jusqu a cuisson|jus clair/, "Viande cuite : jus clair quand tu piques la partie épaisse (volaille), ou température à cœur atteinte au thermomètre."],
  [/frire|friture|\bfrit|bain d huile/, "Friture à bonne température : un morceau de pain y dore en 40 s ; pas de fumée."],
];

export function cuesIn(step: string, max = 2): string[] {
  const s = norm(step);
  const out: string[] = [];
  for (const [rx, cue] of CUES) if (rx.test(s) && !out.includes(cue)) { out.push(cue); if (out.length >= max) break; }
  return out;
}
