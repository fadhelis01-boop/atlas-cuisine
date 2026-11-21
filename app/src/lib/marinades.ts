// Coin marinades (audit UI/UX senior, 20/11/2026) : les marinades étaient dispersées dans les sauces et condiments,
// sans vue d'ensemble par type de viande/poisson ni temps de repos visible. Cette rubrique les réunit, classées par
// protéine puis par pays, chacune réutilisable sur la pièce de son choix (pas liée à un seul plat fini).
import { RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

export type Protein = "boeuf" | "agneau" | "porc" | "volaille" | "poisson" | "crevettes" | "vegetal" | "oeuf";

export const PROTEIN_LABEL: Record<Protein, string> = {
  boeuf: "Bœuf",
  agneau: "Agneau",
  porc: "Porc",
  volaille: "Volaille",
  poisson: "Poisson",
  crevettes: "Crevettes & fruits de mer",
  vegetal: "Tofu & légumes",
  oeuf: "Œufs",
};

export interface MarinadeEntry {
  id: string;
  proteins: Protein[];
  cure?: boolean; // marinade sèche (sel + sucre) qui « cuit » sans chaleur, pas une marinade liquide classique
  dry?: boolean; // rub sec (épices + sucre) appliqué sans liquide, mais qui a toujours besoin d'une cuisson normale ensuite
  acid?: boolean; // ceviche : l'acide « cuit » chimiquement sans aucune chaleur, 4e geste à côté de liquide/cure/rub
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
  { id: "porc_citronnelle_vietnamien", proteins: ["porc", "boeuf", "volaille", "vegetal"] },
  { id: "crevettes_citron_vert_marinade", proteins: ["crevettes", "poisson"] },
  { id: "tofu_marinade_soja_gingembre", proteins: ["vegetal"] },
  { id: "gravlax_saumon_marinade", proteins: ["poisson"], cure: true },
  { id: "marinade_rouge_africaine", proteins: ["volaille", "poisson"] },
  { id: "shawarma_marinade", proteins: ["volaille", "agneau"] },
  { id: "velveting_poulet_chinois", proteins: ["volaille"] },
  { id: "bbq_rub_americain", proteins: ["porc", "volaille"], dry: true },
  { id: "marinade_vin_rouge", proteins: ["boeuf", "agneau"] },
  { id: "marinade_miso_aubergine", proteins: ["vegetal"] },
  { id: "marinade_calamars_citron_persillade", proteins: ["crevettes"] },
  { id: "ajitama", proteins: ["oeuf"] },
  { id: "poisson_cru_fidji", proteins: ["poisson"], acid: true },
  { id: "poisson_cru_tahitienne", proteins: ["poisson"], acid: true },
];

/** Marinades déjà écrites dans la bible comme étapes de vraies recettes, trop nombreuses (plus de cent) pour
 * toutes devenir des fiches du coin, mais dont les familles manquaient totalement ici (chef senior 21/11/2026) :
 * babeurre, achiote-agrumes, vinaigre-ail-laurier philippin, glaçage hoisin chinois, sauce d'huître cambodgienne.
 * Un lien direct vers la recette plutôt qu'une fiche dupliquée. */
export interface OtherMarinade {
  id: string;
  family: string;
}
export const OTHER_MARINADES: OtherMarinade[] = [
  { id: "buttermilk_fried_chicken", family: "Babeurre (États-Unis)" },
  { id: "pollo_pibil", family: "Achiote et agrumes (Yucatán, Mexique)" },
  { id: "tacos_al_pastor", family: "Achiote, piments séchés et ananas (al pastor, Mexique)" },
  { id: "adobo_poulet", family: "Vinaigre, soja, ail et laurier (adobo, Philippines)" },
  { id: "char_siu_poulet", family: "Glaçage hoisin (char siu, Chine)" },
  { id: "lok_lak", family: "Sauce d'huître et poivre-citron (Cambodge)" },
];

export const marinadeRecipes = (p?: Protein): (Recipe & { entry: MarinadeEntry })[] =>
  MARINADES.filter((m) => !p || m.proteins.includes(p))
    .map((m) => (RECIPE_BY_ID[m.id] ? { ...RECIPE_BY_ID[m.id], entry: m } : null))
    .filter((r): r is Recipe & { entry: MarinadeEntry } => !!r);

/** Marinade express « à la louche » (pas une fiche complète : pas de région, pas de filtre allergène) : proportions pour
 * environ 500 g de viande, volaille, poisson ou légumes, trouvée dans les favoris TikTok (UI/UX 21/11/2026) — gardée à
 * côté des marinades complètes plutôt que transformée en 12 fiches quasi identiques qui auraient noyé la rubrique. */
export interface QuickMarinade {
  id: string;
  name: string;
  ingredients: string[];
}
export const QUICK_MARINADES: QuickMarinade[] = [
  { id: "miel_moutarde", name: "Miel-moutarde", ingredients: ["1 c. à s. de miel", "1 c. à s. d'huile", "1 c. à c. de moutarde", "½ c. à c. de paprika"] },
  { id: "ail_persil", name: "Ail & persil", ingredients: ["2 c. à s. d'huile d'olive", "2 c. à s. de jus de citron", "1 gousse d'ail", "1 c. à s. de persil"] },
  { id: "citron_herbes", name: "Citron & herbes", ingredients: ["Jus de ½ citron", "2 c. à s. d'huile d'olive", "1 gousse d'ail", "1 c. à c. de thym ou origan"] },
  { id: "paprika_fume_express", name: "Paprika fumé", ingredients: ["2 c. à s. d'huile", "1 c. à c. de paprika fumé", "1 c. à c. de miel", "1 gousse d'ail"] },
  { id: "soja_miel", name: "Soja & miel", ingredients: ["2 c. à s. de sauce soja", "1 c. à s. de miel", "1 c. à s. d'huile", "½ c. à c. de gingembre"] },
  { id: "curry_coco_express", name: "Curry & coco", ingredients: ["10 cl de crème de coco", "1 c. à c. de curry", "Zeste de ½ citron vert", "1 c. à s. d'huile"] },
  { id: "barbecue_express", name: "Barbecue", ingredients: ["3 c. à s. de ketchup", "1 c. à s. de miel", "1 c. à s. de sauce soja", "1 c. à c. de paprika fumé"] },
  { id: "herbes_provence_express", name: "Herbes de Provence", ingredients: ["2 c. à s. d'huile d'olive", "1 c. à c. d'herbes de Provence", "1 gousse d'ail", "1 c. à c. de jus de citron"] },
  { id: "orange_gingembre", name: "Orange & gingembre", ingredients: ["4 c. à s. de jus d'orange", "1 c. à s. de sauce soja", "1 c. à c. de miel", "½ c. à c. de gingembre"] },
  { id: "oignon_epices", name: "Oignon & épices", ingredients: ["½ oignon haché", "2 c. à s. d'huile d'olive", "1 c. à c. de paprika", "½ c. à c. de cumin"] },
  { id: "speciale_grillades", name: "Spéciale grillades", ingredients: ["2 c. à s. de sauce soja", "1 c. à s. de vinaigre de riz", "1 c. à c. de miel", "½ c. à c. de gingembre"] },
  { id: "balsamique_thym", name: "Balsamique & thym", ingredients: ["2 c. à s. d'huile d'olive", "1 c. à s. de crème balsamique", "1 c. à c. de concentré de tomate", "½ c. à c. de thym"] },
];
export const QUICK_MARINADES_CREDIT = { author: "@les.petites.fiche", url: "https://www.tiktok.com/@les.petites.fiche/photo/7708056823709846817" };

/** Assaisonnements secs par aliment (pas par viande précise comme les marinades) : la question posée en cuisine n'est pas
 * toujours « quelle marinade pour mon agneau » mais aussi « qu'est-ce que je saupoudre sur mon riz/mes pommes de
 * terre » — un angle mort du coin Marinades, chef senior 21/11/2026. Pas de liquide, pas de repos : prêts à l'emploi. */
export interface SpiceMix {
  id: string;
  name: string;
  ingredients: string[];
  use: string;
}
export const SPICE_MIXES: SpiceMix[] = [
  {
    id: "epices_pommes_de_terre",
    name: "Pommes de terre (rôties ou sautées)",
    ingredients: ["1 c. à c. de paprika", "1 c. à c. d'ail semoule", "1 c. à c. de persil séché", "½ c. à c. de poivre", "gros sel"],
    use: "Mélangé à l'huile avant de rôtir, ou saupoudré en fin de cuisson à la poêle, pour 500 g de pommes de terre.",
  },
  {
    id: "epices_riz",
    name: "Riz (nature ou pilaf)",
    ingredients: ["1 c. à c. de cumin moulu", "½ c. à c. de curcuma", "1 c. à c. de coriandre moulue", "1 feuille de laurier"],
    use: "Ajouté à sec dans l'eau de cuisson du riz (1 verre de riz), ou revenu 30 s dans le beurre avant d'ajouter le riz pour un pilaf.",
  },
  {
    id: "epices_poulet",
    name: "Poulet (rôti, grillé ou en morceaux)",
    ingredients: ["1 c. à c. de paprika fumé", "1 c. à c. d'ail semoule", "½ c. à c. d'oignon semoule", "½ c. à c. de thym", "poivre"],
    use: "Massé directement sur la peau ou la chair crue, pour 500 g de poulet, avant four ou poêle.",
  },
  {
    id: "epices_boeuf",
    name: "Bœuf (steak, haché ou mijoté)",
    ingredients: ["1 c. à c. de cumin moulu", "1 c. à c. de coriandre moulue", "1 c. à c. de poivre noir concassé", "½ c. à c. de paprika fumé"],
    use: "Massé sur la viande crue avant saisie, ou ajouté en début de cuisson pour un mijoté, pour 500 g de bœuf.",
  },
];

/** Repères de cuisinier, valables pour n'importe quelle marinade liquide (pas pour un cure à sec comme le gravlax). */
export const REPERES_MARINADE: [string, string][] = [
  ["Un acide (citron, vinaigre, yaourt)", "attendrit et parfume, mais une pièce fine ou un fruit de mer y « cuit » au-delà de 30 min : jamais toute une nuit pour des crevettes ou du poisson."],
  ["Toujours au frigo", "jamais sur le plan de travail, même « juste une heure » : la marinade reste un aliment cru en train d'attendre."],
  ["Jeter la marinade qui a touché la viande crue", "ou la faire bouillir au moins 2 min avant de l'utiliser en sauce de service — jamais crue sur une viande déjà cuite."],
  ["Essuyer l'excédent avant de griller", "la marinade qui dégouline brûle et noircit avant que la viande ne soit cuite à cœur."],
  ["Entailler ou piquer les pièces épaisses", "la marinade ne pénètre que quelques millimètres ; sur un gigot ou un rôti, elle ne parfume vraiment qu'en surface sans ce geste."],
  [
    "Saler tôt, sauf la marinade sèche",
    "le sel d'une marinade liquide peut rester plusieurs heures sans assécher ; à l'inverse, un cure comme le gravlax EST le sel : jamais de raccourci sur son temps de repos.",
  ],
  [
    "Un rub sec n'attendrit pas",
    "contrairement à une marinade liquide ou à un cure, un rub d'épices (BBQ) ne fait que parfumer et croûter en surface : c'est la cuisson longue et douce qui attendrit la viande, pas le rub.",
  ],
  [
    "Le ceviche est un 4e geste, pas un oubli de la cuisson",
    "un poisson ou un fruit de mer très frais, coupé fin et mariné dans beaucoup d'acide (citron vert), « cuit » " +
      "chimiquement en 10 à 20 min sans aucune chaleur : c'est voulu, à condition de ne jamais dépasser ce temps " +
      "(voir kokoda, poisson cru tahitien) — différent d'une marinade acide ordinaire qui, elle, cuit toujours ensuite.",
  ],
];
