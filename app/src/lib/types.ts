// Types des données exportées depuis la bible (bible/export_app_data.py).

export type DerivLevel = "certain" | "possible" | "trace";

export interface IngredientRef {
  allergens: string[]; // sûrs (codes Tome 3 : GL, CR, OE, PO, AR, SO, LA, FC, CE, MO, SE, SU, LU, MM)
  maybe: string[]; // possibles selon la marque
  derivs: { pork?: DerivLevel; alcohol?: DerivLevel; animal?: DerivLevel };
  dispo: string; // 🟢 supermarché · 🟡 rayon monde/bio · 🟠 épicerie spécialisée · 🔴 difficile
  section: string; // famille du référentiel, sert aussi de rayon pour la liste de courses
  note: string; // notes du Tome 3 (substitut sans alcool, alternative…)
  slug: string; // fiche du dictionnaire illustré (/ingredient/<slug>)
  season: number[]; // mois de récolte en France métropolitaine (vide = toute l'année ou produit transformé)
}

export interface RecipeLine {
  qty: string;
  label: string;
  ref: string | null; // nom exact du Tome 3, « SUB:id » pour une sous-recette, null = eau / hors référentiel
  weight: number; // 0 optionnel/assaisonnement … 3 structurant
  optional: boolean;
  replaces?: string; // version adaptée : ligne d'origine remplacée (« 750 ml de vin rouge »)
}

export interface Variant {
  name: string;
  constraints: string[]; // "pork" | "alcohol" (vide = autre adaptation, ex. sans œuf)
  tested: boolean;
  note: string;
  replace: Record<string, [string, number][]>;
}

export type MacroId =
  | "france" | "europe_sud" | "europe_nord" | "maghreb" | "afrique" | "moyen_orient"
  | "asie_sud" | "asie_est" | "asie_sud_est" | "amerique_nord" | "amerique_latine" | "oceanie" | "fusion";

export type Role = "entree" | "plat" | "dessert" | "boisson" | "autre";

export interface Recipe {
  id: string;
  title: string;
  origin: string;
  regionPath: string[];
  macro: MacroId;
  kind: string;
  role: Role;
  level: number;
  portions: number;
  active: number;
  rest: number;
  cost: string;
  equipment: string;
  intro: string;
  ingredients: RecipeLine[];
  steps: string[];
  tips: string[];
  variants: Variant[];
  storage: string;
  zeroWaste: string[];
  drinksNoAlcohol: string[];
  drinksAlcohol: string[];
  techniques: string[];
  kids: string;
  age: number | null;
  cats: string[];
  fetes: string[];
  profile: string[];
  tests: string;
  source: string;
  verified: "A" | "B" | "C";
  leftovers: Leftover[]; // ingrédients entamés et quoi en faire (Tome 12 §6)
  videos: VideoLink[]; // vidéos existantes (favoris TikTok, Cooking with Morgane) liées à la fiche
  fusionNote?: string; // « Food fusion » : de quelles traditions la recette est le mélange
}

export interface Leftover {
  ref: string; line: string; sold: string;
  parts: { part: string; keep: string; ideas: { kind: "repas" | "plat" | "conserver" | "hors"; text: string; recipe: string | null }[] }[];
}

export interface VideoLink { url: string; title: string; source: string; author: string; embed: string; pork: boolean; alcohol: boolean }

export interface Rule {
  replaces: string;
  items: [string, number][];
  satisfies: ("pork" | "alcohol")[];
  status: "draft" | "testing" | "validated" | "retired";
  note: string;
}

export interface CatalogueEntry {
  title: string;
  macro: MacroId;
  region: string;
  type: string;
  level: string;
  pork: string;
  alcohol: string;
  kids: string;
  notes: string;
}

export interface ImportEntry {
  lang?: "en" | "de" | "nl"; // titre et vidéo dans une autre langue (chaînes YouTube étrangères)
  title: string;
  url: string;
  source: string;
  author: string;
  cat: string;
  sub: string;
  pork: boolean;
  alcohol: boolean;
  fete: boolean;
  photo: boolean;
  embed: string; // « tt:<id> » (TikTok), « yt:<id> » (YouTube) ou vide (non intégrable)
  from?: string; // catégorie d'origine d'un import reclassé en « Food fusion »
}

/** Profil de foyer (Tome 1 §3.3). */
export interface Profile {
  noPork: boolean;
  alcohol: "allowed" | "standard" | "strict"; // standard : pas d'alcool ajouté ; strict : ni dérivés ni traces
  strict: boolean; // doute (« possible ») = exclusion
  vegetarian: boolean;
  allergens: string[];
  adult: boolean; // a confirmé avoir 18 ans : accords avec alcool visibles (si alcool permis)
  kidsAge: number | null; // âge du plus jeune enfant du foyer
  equipment: string[];
  onboarded: boolean;
}
