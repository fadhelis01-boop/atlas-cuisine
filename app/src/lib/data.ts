import { useSyncExternalStore } from "react";
import ingredientsJson from "../data/ingredients.json";
import recipesRaw from "../data/recipes.json?raw";
import renamesJson from "../data/renames.json";
import rulesJson from "../data/rules.json";
import catalogueJson from "../data/catalogue.json";
import { setRenames } from "./store";
import { markDetails } from "./mesures";
import { lazyRetry } from "./chunkRetry";
import type { CatalogueEntry, ImportEntry, IngredientRef, Leftover, MacroId, Recipe, Rule } from "./types";

export const INGREDIENTS = ingredientsJson as unknown as Record<string, IngredientRef>;
// Démarrage léger (audit dév/UX 2026-10-21 §2.1) : l'index (cartes, recherche, moteur, planificateur) est lu en JSON.parse,
// deux fois plus rapide qu'un littéral JavaScript ; le détail d'une fiche arrive juste après le premier affichage.
const DETAIL_EMPTY = { steps: [] as string[], intro: "", videos: [] as Recipe["videos"], tips: [] as string[], equipment: "", storage: "", source: "", verified: "" };
// Ingrédients de l'index en tableaux [réf., poids, facultatif?, allergènes du libellé?] : la réf. est le rang de l'ingrédient dans
// ingredients.json (même ordre de clés), sauf « SUB:… » et null. Quantité et libellé arrivent avec le détail (mergeDetails) ;
// en attendant, le libellé est le nom de l'ingrédient (assez pour les rangées de l'accueil et les filtres).
type PackedLine = [number | string | null, number, (0 | 1)?, string?];
const ING_KEYS = Object.keys(INGREDIENTS);
const shortName = (ref: string | null) => (ref ? (ref.startsWith("SUB:") ? ref.slice(4).replace(/_/g, " ") : ref.split(" (")[0].split(" / ")[0]).toLowerCase() : "");
// « kids » omis de l'index quand il vaut exactement la phrase par défaut (déduite de l'âge) : reconstruite ici, pour
// alléger le budget de démarrage sans rien changer pour les pages qui lisent r.kids (audit budget 20/11/2026).
const defaultKids = (age: number | null) => (age != null ? `✓ dès ${age} an${age > 1 ? "s" : ""}.` : null);
export const RECIPES = (JSON.parse(recipesRaw) as (Omit<Recipe, "ingredients"> & { ingredients: PackedLine[] })[]).map(
  (r) =>
    Object.assign(r, {
      ...DETAIL_EMPTY,
      ...r,
      kids: r.kids || defaultKids(r.age),
      ingredients: r.ingredients.map(([rf, weight, opt, al]) => {
        const ref = typeof rf === "number" ? ING_KEYS[rf] : rf;
        return {
          qty: "",
          label: shortName(ref),
          ref,
          weight,
          optional: opt === 1,
          ...(al
            ? {
                extra: al.split(",").filter((a) => !a.startsWith("?")),
                maybeExtra: al
                  .split(",")
                  .filter((a) => a.startsWith("?"))
                  .map((a) => a.slice(1)),
              }
            : {}),
        };
      }),
    }) as unknown as Recipe,
);
setRenames(renamesJson as Record<string, string>);
export const RULES = rulesJson as unknown as Rule[];
export const CATALOGUE = catalogueJson as unknown as CatalogueEntry[];
// Bibliothèque de vidéos classées (3 000 et plus) : chargée à la demande pour garder l'ouverture de l'application rapide.
let IMP: ImportEntry[] | null = null;
let impP: Promise<ImportEntry[]> | null = null;
const impListeners = new Set<() => void>();
export function loadImports(): Promise<ImportEntry[]> {
  impP ??= lazyRetry(() => import("../data/imports.json"))().then((m) => {
    IMP = m.default as unknown as ImportEntry[];
    impListeners.forEach((l) => l());
    return IMP;
  });
  return impP;
}
const NO_IMPORTS: ImportEntry[] = [];
export function useImportLibrary(): ImportEntry[] {
  return useSyncExternalStore(
    (cb) => {
      impListeners.add(cb);
      void loadImports();
      return () => {
        impListeners.delete(cb);
      };
    },
    () => IMP ?? NO_IMPORTS,
  );
}

export const RECIPE_BY_ID: Record<string, Recipe> = Object.fromEntries(RECIPES.map((r) => [r.id, r]));

type Detail = Partial<Pick<Recipe, "steps" | "intro" | "videos" | "tips" | "equipment" | "storage" | "credit" | "kidHelp" | "source" | "verified" | "prot">> & { lines?: [string, string][] };
// Démarrage léger, suite (audit dév senior 21/11/2026 §1) : le détail de 1600+ fiches ne se télécharge plus en un seul
// bloc de 2 Mo qui bloquait l'affichage de n'importe quelle fiche le temps de recevoir les étapes des 1600 autres.
// Il est coupé en 12 lots (export_app_data.py, même fonction de répartition `shardOf`) ; une fiche ne charge que le
// sien (`useRecipeDetail`), les écrans qui balaient tout le catalogue (Ma semaine, menus, Bien choisir, Enfants)
// chargent les 12 (`useDetails`).
const SHARD_N = 12;
const shardOf = (id: string): number => {
  let s = 0;
  for (let i = 0; i < id.length; i++) s += id.charCodeAt(i);
  return s % SHARD_N;
};
// 12 imports statiques plutôt qu'un `import.meta.glob` (propre à Vite) : marche aussi sous rolldown (tests, smoke),
// qui rend chaque chunk de lot repérable au build sans transformation spéciale.
const SHARD_LOADERS: (() => Promise<string>)[] = [
  () => import("../data/recipes_detail_0.json?raw").then((m) => m.default as unknown as string),
  () => import("../data/recipes_detail_1.json?raw").then((m) => m.default as unknown as string),
  () => import("../data/recipes_detail_2.json?raw").then((m) => m.default as unknown as string),
  () => import("../data/recipes_detail_3.json?raw").then((m) => m.default as unknown as string),
  () => import("../data/recipes_detail_4.json?raw").then((m) => m.default as unknown as string),
  () => import("../data/recipes_detail_5.json?raw").then((m) => m.default as unknown as string),
  () => import("../data/recipes_detail_6.json?raw").then((m) => m.default as unknown as string),
  () => import("../data/recipes_detail_7.json?raw").then((m) => m.default as unknown as string),
  () => import("../data/recipes_detail_8.json?raw").then((m) => m.default as unknown as string),
  () => import("../data/recipes_detail_9.json?raw").then((m) => m.default as unknown as string),
  () => import("../data/recipes_detail_10.json?raw").then((m) => m.default as unknown as string),
  () => import("../data/recipes_detail_11.json?raw").then((m) => m.default as unknown as string),
];
const shardLoaded = new Array<boolean>(SHARD_N).fill(false);
const shardPromises = new Array<Promise<void> | undefined>(SHARD_N);
const shardListeners: Set<() => void>[] = Array.from({ length: SHARD_N }, () => new Set());
let DETAILS = false; // vrai une fois que chaque fiche a son détail (par lots dans l'appli, en un coup dans les tests)
const detailedIds = new Set<string>(); // par id, pas par `r.steps !== undefined` : RECIPES part déjà de steps: [] (DETAIL_EMPTY)
const detLs = new Set<() => void>();
/** Complète les fiches avec leur détail (étapes, introduction, vidéos, conseils, matériel, conservation). Marque
 *  `detailsReady()` vrai une fois que chaque fiche en a un, que ça vienne des 12 lots (l'appli) ou d'un seul appel
 *  avec le fichier complet (les tests, qui ne passent jamais par `loadShard`). */
export function mergeDetails(d: Record<string, Detail>) {
  for (const [id, { lines, ...x }] of Object.entries(d)) {
    const r = RECIPE_BY_ID[id];
    if (!r) continue;
    Object.assign(r, x);
    lines?.forEach(([qty, label], i) => {
      const l = r.ingredients[i];
      if (l) {
        l.qty = qty;
        l.label = label;
      }
    }); // quantités et libellés
    detailedIds.add(id);
  }
  markDetails();
  if (detailedIds.size >= RECIPES.length && !DETAILS) {
    DETAILS = true;
    detLs.forEach((l) => l());
  }
}
function loadShard(i: number): Promise<void> {
  // lazyRetry (audit dév/UX senior 23/11/2026) : même recharge de secours que les pages, si ce lot a disparu
  // depuis un déploiement entre-temps.
  shardPromises[i] ??= lazyRetry(SHARD_LOADERS[i])().then((raw) => {
    mergeDetails(JSON.parse(raw) as Record<string, Detail>);
    shardLoaded[i] = true;
    shardListeners[i].forEach((l) => l());
  });
  return shardPromises[i]!;
}
/** Charge le détail d'une seule fiche. */
export function loadDetailFor(id: string): Promise<void> {
  return loadShard(shardOf(id));
}
/** Charge le détail de toutes les fiches : pour les écrans qui balaient tout le catalogue (Ma semaine, menus, Bien
 *  choisir, Enfants), pas pour une fiche seule (voir `useRecipeDetail`). */
export function loadAllDetails(): Promise<void> {
  return Promise.all(Array.from({ length: SHARD_N }, (_, i) => loadShard(i))).then(() => undefined);
}
export const detailsReady = () => DETAILS;
/** Pour un écran qui balaie tout le catalogue : vrai quand les 12 lots sont là. `active=false` ne déclenche pas le
 *  chargement (route qui n'en a pas besoin pour l'instant), juste la lecture de l'état déjà connu. */
export function useDetails(active = true): boolean {
  return useSyncExternalStore(
    (cb) => {
      detLs.add(cb);
      if (active) void loadAllDetails();
      return () => {
        detLs.delete(cb);
      };
    },
    () => DETAILS,
  );
}
/** Pour une seule fiche (recette, mode cuisine) : vrai dès que SON lot est chargé, pas besoin d'attendre les 11 autres. */
export function useRecipeDetail(id: string | undefined): boolean {
  const i = id ? shardOf(id) : -1;
  return useSyncExternalStore(
    (cb) => {
      if (i < 0) return () => {};
      shardListeners[i].add(cb);
      void loadShard(i);
      return () => {
        shardListeners[i].delete(cb);
      };
    },
    () => i < 0 || shardLoaded[i],
  );
}
export const INGREDIENT_NAMES = Object.keys(INGREDIENTS);

export const MACROS: { id: MacroId; name: string; emoji: string; icon: string; blurb: string }[] = [
  { id: "france", name: "France", emoji: "🥖", icon: "bread", blurb: "Régions, terroirs et Outre-mer : de la galette bretonne aux accras antillais." },
  { id: "europe_sud", name: "Europe du Sud", emoji: "🍅", icon: "tomato", blurb: "Italie, Espagne, Portugal, Grèce : huile d'olive, tomates, herbes." },
  {
    id: "europe_nord",
    name: "Europe du Nord, Centrale & de l'Est",
    emoji: "🥨",
    icon: "pretzel",
    blurb: "Belgique, Allemagne, Scandinavie, Europe de l'Est : pains, choux, fumaisons.",
  },
  { id: "maghreb", name: "Maghreb & Égypte", emoji: "🍵", icon: "teapot", blurb: "Algérie, Maroc, Tunisie, Égypte : épices douces, semoule, tajines et thé à la menthe." },
  { id: "afrique", name: "Afrique subsaharienne", emoji: "🌶️", icon: "pot", blurb: "Sénégal, Mali, Côte d'Ivoire, Nigeria, Éthiopie : mafés, yassa, jollof, bissap." },
  { id: "moyen_orient", name: "Moyen-Orient & Caucase", emoji: "🧆", icon: "pomegranate", blurb: "Liban, Turquie, Iran, Syrie : mezzés, herbes fraîches, grenade et sésame." },
  { id: "asie_sud", name: "Asie du Sud", emoji: "🍛", icon: "curry", blurb: "Inde, Pakistan, Sri Lanka : dals, currys, pains plats, lassi." },
  { id: "asie_est", name: "Asie de l'Est", emoji: "🥢", icon: "chopsticks", blurb: "Chine, Japon, Corée, Taïwan : riz, nouilles, sautés, fermentations." },
  { id: "asie_sud_est", name: "Asie du Sud-Est", emoji: "🍜", icon: "noodles", blurb: "Thaïlande, Vietnam, Indonésie, Philippines : herbes, citron vert, lait de coco." },
  { id: "amerique_nord", name: "Amérique du Nord", emoji: "🍔", icon: "burger", blurb: "États-Unis, Canada, cuisine cajun : barbecue, pancakes, comfort food." },
  { id: "amerique_latine", name: "Amérique latine & Caraïbes", emoji: "🌮", icon: "taco", blurb: "Mexique, Brésil, Pérou, Antilles : maïs, haricots, piments, agrumes." },
  { id: "oceanie", name: "Océanie", emoji: "🥝", icon: "kiwi", blurb: "Australie, Nouvelle-Zélande, Pacifique." },
  {
    id: "fusion",
    name: "Food fusion",
    emoji: "🌐",
    icon: "fusion",
    blurb:
      "Les recettes qui mélangent plusieurs traditions ou dont l'origine ne tient pas dans un seul pays : tex-mex, pizza au butter chicken, fish & chips en feuille de riz, couscous-tiep…",
  },
];
export const MACRO_BY_ID = Object.fromEntries(MACROS.map((m) => [m.id, m])) as Record<MacroId, (typeof MACROS)[number]>;

/** Rubriques des imports classés (TikTok, sites) → libellé. */
export const IMPORT_CATS: Record<string, string> = {
  afrique: "Afrique de l'Ouest & centrale",
  maghreb: "Maghreb",
  moyen_orient: "Moyen-Orient, Turquie & Balkans",
  asie: "Asie",
  italie: "Italie",
  france: "France",
  europe: "Europe (autres)",
  ameriques: "Amériques & Caraïbes",
  street_food: "Street food maison",
  pains: "Pains, pâtes & bases",
  sauces: "Sauces & marinades",
  fait_maison: "Fait maison sans additifs",
  desserts: "Desserts & pâtisserie",
  boissons: "Boissons",
  techniques: "Techniques & astuces",
  zero_dechet: "Zéro déchet",
  fetes: "Fêtes",
  fusion: "Food fusion",
  a_verifier: "À vérifier",
  autre: "Autre",
};

/** Correspondance rubrique d'import → macro-région de l'atlas (pour « Dans tes imports »). */
export const IMPORT_CAT_TO_MACRO: Record<string, MacroId[]> = {
  afrique: ["afrique"],
  maghreb: ["maghreb"],
  moyen_orient: ["moyen_orient"],
  asie: ["asie_est", "asie_sud", "asie_sud_est"],
  italie: ["europe_sud"],
  france: ["france"],
  europe: ["europe_nord", "europe_sud"],
  ameriques: ["amerique_nord", "amerique_latine"],
  fusion: ["fusion"],
};

export const ALLERGENS: Record<string, string> = {
  GL: "Gluten",
  CR: "Crustacés",
  OE: "Œufs",
  PO: "Poissons",
  AR: "Arachide",
  SO: "Soja",
  LA: "Lait",
  FC: "Fruits à coque",
  CE: "Céleri",
  MO: "Moutarde",
  SE: "Sésame",
  SU: "Sulfites",
  LU: "Lupin",
  MM: "Mollusques",
};

export const CATEGORY_LABEL: Record<string, string> = {
  pains: "Pains, pâtes & bases",
  sauces: "Sauces maison",
  fetes: "Fêtes",
  enfants: "Enfants",
  zero_dechet: "Zéro déchet",
  boissons: "Boissons",
  techniques: "Techniques",
  fusion: "Food fusion",
  express: "Express (20 min)",
  brunch: "Petit-déjeuner & brunch",
  salade: "Salades complètes",
  vegetarien: "Végétarien",
  pique_nique: "Pique-nique",
};

/** Recettes d'une entrée de l'atlas (la « Food fusion » est une rubrique transversale, pas une macro-région). */
export const recipesOfMacro = (id: MacroId) => RECIPES.filter((r) => (id === "fusion" ? r.cats.includes("fusion") : r.macro === id));

// Restes zéro déchet de chaque recette (Tome 12 §6) : 35 % des données de recettes, chargés seulement quand une fiche s'ouvre.
let LEFT: Record<string, Leftover[]> | null = null;
let leftP: Promise<Record<string, Leftover[]>> | null = null;
const leftListeners = new Set<() => void>();
export function loadLeftovers(): Promise<Record<string, Leftover[]>> {
  leftP ??= lazyRetry(() => import("../data/leftovers.json"))().then((m) => {
    LEFT = m.default as unknown as Record<string, Leftover[]>;
    leftListeners.forEach((l) => l());
    return LEFT;
  });
  return leftP;
}
const NO_LEFT: Leftover[] = [];
// Liste complète des vidéos d'une fiche : chargée à l'ouverture d'une fiche, pas au démarrage (audit famille)
let VIDS: Record<string, Recipe["videos"]> | null = null;
let vidP: Promise<Record<string, Recipe["videos"]>> | null = null;
const vidListeners = new Set<() => void>();
export function loadRecipeVideos() {
  vidP ??= lazyRetry(() => import("../data/recipe_videos.json"))().then((m) => {
    VIDS = m.default as unknown as Record<string, Recipe["videos"]>;
    vidListeners.forEach((l) => l());
    return VIDS;
  });
  return vidP;
}
export function useRecipeVideos(r: Recipe): Recipe["videos"] {
  return useSyncExternalStore(
    (cb) => {
      vidListeners.add(cb);
      void loadRecipeVideos();
      return () => {
        vidListeners.delete(cb);
      };
    },
    () => VIDS?.[r.id] ?? r.videos,
  );
}
export function useLeftovers(id: string): Leftover[] | null {
  return useSyncExternalStore(
    (cb) => {
      leftListeners.add(cb);
      void loadLeftovers();
      return () => {
        leftListeners.delete(cb);
      };
    },
    () => (LEFT ? (LEFT[id] ?? NO_LEFT) : null),
  );
}
