// Coin marinades (audit UI/UX senior, 20/11/2026) : les marinades étaient dispersées dans les sauces et condiments,
// sans vue d'ensemble par type de viande/poisson ni temps de repos visible. Cette rubrique les réunit, classées par
// protéine puis par pays, chacune réutilisable sur la pièce de son choix (pas liée à un seul plat fini).
import { RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

export type Protein = "boeuf" | "agneau" | "porc" | "volaille" | "poisson" | "crevettes" | "vegetal";

export const PROTEIN_LABEL: Record<Protein, string> = {
  boeuf: "Bœuf",
  agneau: "Agneau",
  porc: "Porc",
  volaille: "Volaille",
  poisson: "Poisson",
  crevettes: "Crevettes & fruits de mer",
  vegetal: "Tofu & légumes",
};

export interface MarinadeEntry {
  id: string;
  proteins: Protein[];
  cure?: boolean; // marinade sèche (sel + sucre) qui « cuit » sans chaleur, pas une marinade liquide classique
}

export const MARINADES: MarinadeEntry[] = [
  { id: "marinade_yassa", proteins: ["volaille", "poisson"] },
  { id: "marinade_tandoori", proteins: ["volaille"] },
  { id: "marinade_jerk", proteins: ["volaille", "porc"] },
  { id: "marinade_bulgogi", proteins: ["boeuf"] },
  { id: "marinade_provencale", proteins: ["boeuf", "agneau", "porc", "volaille", "poisson"] },
  { id: "marinade_teriyaki_sauce", proteins: ["boeuf", "volaille", "poisson"] },
  { id: "chermoula", proteins: ["poisson"] },
  { id: "harissa_marinade_agneau", proteins: ["agneau", "boeuf", "volaille"] },
  { id: "mojo_cubain_porc", proteins: ["porc", "volaille", "crevettes"] },
  { id: "porc_citronnelle_vietnamien", proteins: ["porc", "boeuf", "volaille"] },
  { id: "crevettes_citron_vert_marinade", proteins: ["crevettes", "poisson"] },
  { id: "tofu_marinade_soja_gingembre", proteins: ["vegetal"] },
  { id: "gravlax_saumon_marinade", proteins: ["poisson"], cure: true },
];

export const marinadeRecipes = (p?: Protein): (Recipe & { entry: MarinadeEntry })[] =>
  MARINADES.filter((m) => !p || m.proteins.includes(p))
    .map((m) => (RECIPE_BY_ID[m.id] ? { ...RECIPE_BY_ID[m.id], entry: m } : null))
    .filter((r): r is Recipe & { entry: MarinadeEntry } => !!r);

/** Repères de cuisinier, valables pour n'importe quelle marinade liquide (pas pour un cure à sec comme le gravlax). */
export const REPERES_MARINADE: [string, string][] = [
  ["Un acide (citron, vinaigre, yaourt)", "attendrit et parfume, mais une pièce fine ou un fruit de mer y « cuit » au-delà de 30 min : jamais toute une nuit pour des crevettes ou du poisson."],
  ["Toujours au frigo", "jamais sur le plan de travail, même « juste une heure » : la marinade reste un aliment cru en train d'attendre."],
  ["Jeter la marinade qui a touché la viande crue", "ou la faire bouillir au moins 2 min avant de l'utiliser en sauce de service — jamais crue sur une viande déjà cuite."],
  ["Essuyer l'excédent avant de griller", "la marinade qui dégouline brûle et noircit avant que la viande ne soit cuite à cœur."],
  ["Entailler ou piquer les pièces épaisses", "la marinade ne pénètre que quelques millimètres ; sur un gigot ou un rôti, elle ne parfume vraiment qu'en surface sans ce geste."],
  ["Saler tôt, sauf la marinade sèche", "le sel d'une marinade liquide peut rester plusieurs heures sans assécher ; à l'inverse, un cure comme le gravlax EST le sel : jamais de raccourci sur son temps de repos."],
];
