// Barre « Ajouter un ingrédient » du frigo (retour d'usage du 22/10/2026 : « à quoi sert la barre ? »). Les mots de tous
// les jours doivent trouver le bon produit : « fromage » → emmental, mozzarella, feta… (et pas le fromage de tête),
// « oeuf » → œufs (et pas le bœuf), « pdt » → pommes de terre. On cherche au début des mots, pas au milieu.
import { INGREDIENT_NAMES, INGREDIENTS } from "./data";
import { STAPLES } from "./engine";
import { norm } from "./text";

/** Mots courants → produits du référentiel, dans l'ordre où on les propose. */
const SYNONYMS: [RegExp, string[]][] = [
  [/^fromages?$/, ["Gruyère / comté / emmental / beaufort", "Mozzarella / burrata", "Feta", "Parmesan / Parmigiano", "Chèvre (frais, bûche)", "Camembert / brie", "Cheddar",
    "Roquefort / bleu", "Ricotta", "Fromage à tartiner / fondu", "Fromage blanc / faisselle", "Reblochon / raclette / mont-d'or", "Cantal / saint-nectaire / tomme", "Halloumi"]],
  [/^poulets?$/, ["Cuisse / pilon de poulet", "Blanc de poulet", "Poulet entier", "Ailes de poulet"]],
  [/^(pdt|patates?|pommes? de terre)$/, ["Pomme de terre", "Patate douce"]],
  [/^(oeufs?|oeuf)$/, ["Œuf entier (frais)", "Jaune d'œuf", "Blanc d'œuf"]],
  [/^(viande hachee?|hache|steak hache|steaks haches)$/, ["Bœuf haché", "Agneau haché"]],
  [/^steaks?$/, ["Steak / bifteck", "Bœuf haché", "Entrecôte", "Rumsteck"]],
  [/^viandes?$/, ["Bœuf haché", "Steak / bifteck", "Cuisse / pilon de poulet", "Blanc de poulet", "Paleron", "Épaule d'agneau", "Dinde (escalope, cuisse, filet)"]],
  [/^poissons?$/, ["Cabillaud / morue fraîche", "Saumon (frais, pavé)", "Colin, lieu noir, merlu", "Thon en conserve", "Sardine (fraîche / conserve)", "Maquereau", "Dorade"]],
  [/^cremes?$/, ["Crème fraîche", "Crème fleurette (liquide)", "Crème épaisse", "Crème de soja / avoine"]],
  [/^laits?$/, ["Lait entier / demi-écrémé / écrémé", "Lait de coco / crème de coco", "Lait concentré sucré / non sucré"]],
  [/^huiles?$/, ["Huile d'olive vierge extra", "Huile de tournesol / colza"]],
  [/^pates?$/, ["Pâtes sèches (spaghetti, penne…)", "Pâtes fraîches aux œufs", "Lasagnes"]],
  [/^pains?$/, ["Pain de campagne / complet", "Baguette tradition", "Pain de mie", "Pain rassis (réservé)", "Pain pita / libanais"]],
  [/^salades?$/, ["Salade (laitue, batavia)", "Roquette / mâche", "Chicorée / frisée"]],
  [/^oignons?$/, ["Oignon jaune", "Oignon rouge", "Oignon nouveau / cébette"]],
  [/^herbes?$/, ["Persil plat / frisé", "Coriandre fraîche", "Basilic", "Ciboulette", "Menthe", "Aneth"]],
  [/^jambons?$/, ["Jambon de dinde / de poulet", "Jambon blanc", "Jambon cru (Bayonne, Parme, serrano)"]],
  [/^(lardons?)$/, ["Lardons de dinde / de volaille fumés", "Lardons"]],
  [/^(tomates? en boite|tomates? pelees?|coulis|passata)$/, ["Coulis / passata / tomates pelées", "Concentré de tomate"]],
  [/^(haricots?)$/, ["Haricots verts", "Haricots rouges / noirs", "Haricots blancs / lingots"]],
  [/^(chocolat)$/, ["Chocolat noir", "Chocolat au lait", "Chocolat blanc"]],
  [/^nouilles?$/, ["Nouilles chinoises aux œufs", "Nouilles de riz / vermicelles", "Nouilles udon", "Nouilles ramen", "Nouilles soba", "Vermicelles de haricots mungo"]],
  [/^(pate a tarte|pates? a tarte|pate brisee|pate sablee|pate sucree)$/, ["Pâte brisée / sablée (prête)", "Pâte feuilletée (prête)"]],
  [/^(pate feuilletee|feuilletage)$/, ["Pâte feuilletée (prête)"]],
  [/^(pate a pizza|pate pizza)$/, ["Pâte à pizza (prête)"]],
  [/^(brick|bricks?|feuilles? de brick|filo|phyllo)$/, ["Pâte filo / feuilles de brick", "Pâte de brick / ouarka"]],
  [/^(lait de coco|creme de coco|coco)$/, ["Lait de coco / crème de coco", "Noix de coco râpée"]],
  [/^saumons?$/, ["Saumon (frais, pavé)", "Saumon fumé"]],
  [/^crevettes?$/, ["Crevettes (cuites/crues)", "Crevettes séchées"]],
];

const words = (s: string) => norm(s).split(/[^a-z0-9]+/).filter(Boolean);
const sing = (w: string) => (w.length > 3 ? w.replace(/[sx]$/, "") : w);
const INDEX = INGREDIENT_NAMES.map((n) => ({ n, w: words(n).map(sing), first: sing(words(n)[0] ?? "") }));
const pork = (n: string) => INGREDIENTS[n]?.derivs?.pork === "certain";
/** Formes transformées d'un produit, proposées après le produit lui-même sauf si on les tape. */
const PROCESSED = /\b(seche|sechee|seches|sechees|fume|fumee|fumes|fumees|en poudre|deshydrate|marine|confit|rillettes|pate de|oeufs de)\b/;

/** Ingrédients du référentiel pour ce que la personne tape (8 au plus), les plus probables d'abord. */
export function findIngredients(q: string, exclude: readonly string[] = [], common: readonly string[] = [], max = 8): string[] {
  const nq = norm(q).trim().replace(/\s+/g, " ");
  if (nq.length < 2) return [];
  const skip = new Set(exclude);
  const scores = new Map<string, number>();
  const add = (n: string, s: number) => { if (!skip.has(n) && INGREDIENTS[n]) scores.set(n, Math.max(scores.get(n) ?? -Infinity, s)); };
  for (const [re, refs] of SYNONYMS) if (re.test(nq)) refs.forEach((n, i) => add(n, 1000 - i));
  const qw = nq.split(" ").map(sing);
  for (const { n, w, first } of INDEX) {
    // chaque mot tapé doit commencer un mot du produit (« oeuf » ne trouve pas « boeuf »)
    if (!qw.every((x) => w.some((y) => y.startsWith(x)))) continue;
    let s = 100 + (first.startsWith(qw[0]) ? 40 : 0) + (w.includes(qw[0]) ? 20 : 0) + (common.includes(n) || STAPLES.has(n) ? 30 : 0) - n.length / 10;
    if (pork(n)) s -= 80; // le porc passe après (ATLAS est d'abord sans porc)
    // « crevettes » → les crevettes, pas d'abord les crevettes séchées ; « saumon » → le pavé, pas le fumé (12/11/2026)
    const nn = norm(n);
    if (PROCESSED.test(nn) && !PROCESSED.test(nq)) s -= 30;
    if (words(n.split(" (")[0].split(" / ")[0]).map(sing).join(" ") === qw.join(" ")) s += 25; // le nom exact
    add(n, s);
  }
  return [...scores].sort((a, b) => b[1] - a[1]).slice(0, max).map(([n]) => n);
}
