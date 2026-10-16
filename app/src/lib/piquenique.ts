// Rubrique Pique-nique (16/10/2026) : ce qui voyage bien, pour les enfants et pour les grands, classiques, originaux et du
// monde, avec la sécurité (froid, soleil), le transport, le zéro déchet et les restes. Les nouvelles fiches portent la
// catégorie « pique_nique » ; les fiches déjà au catalogue qui s'y prêtent sont listées ici. Repères NON TESTÉS (Tome 7 §2).
import { RECIPES, RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

/** Fiches déjà au catalogue qui voyagent bien (froides ou tièdes, sans mayonnaise crue, faciles à transporter). */
export const DEJA: string[] = [
  "pan_bagnat", "cake_sale", "taboule_libanais", "taboule_semoule", "onigiri", "empanadas", "quiche_epinards_feta", "quiche_poireaux",
  "quiche_frigo_vide", "tortilla_espanola", "focaccia", "wrap_poulet_croquant", "wrap_houmous_legumes", "samoussas_legumes", "salade_pates_pesto_tomates",
  "salade_riz_thon_mais", "muffins_oeufs_legumes", "muffins_myrtilles", "cookies_avoine_banane", "cookies_chocolat", "madeleines", "financiers", "brownies",
  "sables_bretons", "banana_bread", "gateau_yaourt", "limonade_maison", "the_glace_peche", "citronnade_menthe", "bissap", "houmous", "tzatziki", "falafels",
  "pissaladiere", "fougasse_olives", "salade_lentilles", "rouleaux_printemps", "dolma_riz", "tarte_tomates_moutarde", "frittata_courgettes",
  "kuku_sabzi", "mercimek_kofte", "gazpacho", "kartoffelsalat", "lahmacun", "socca", "meat_pie_australien", "chips_epluchures",
  "pickles_oignons_rouges", "salade_quinoa_feta_grenade", "spanakopita", "borek_fromage", "fatayer_epinards", "baba_ghanoush", "muhammara",
];

export const piqueNique = (): Recipe[] => {
  const ids = new Set([...RECIPES.filter((r) => r.cats.includes("pique_nique")).map((r) => r.id), ...DEJA.filter((id) => RECIPE_BY_ID[id])]);
  return [...ids].map((id) => RECIPE_BY_ID[id]);
};

export const SWEET = (r: Recipe) => r.role === "dessert" || r.kind.startsWith("Goûter");
export const FILTRES: { id: string; label: string; test: (r: Recipe) => boolean }[] = [
  { id: "tout", label: "Tout", test: () => true },
  { id: "enfants", label: "Pour les enfants", test: (r) => r.age !== null && r.age <= 3 },
  { id: "adultes", label: "Pour les grands", test: (r) => r.age === null || r.age >= 3 },
  { id: "classiques", label: "Classiques", test: (r) => r.macro === "france" || /pan bagnat|taboule|cake sale|quiche|salade de|tortilla|chips/.test(r.title.toLowerCase()) },
  { id: "monde", label: "Du monde", test: (r) => r.macro !== "france" && !SWEET(r) && r.role !== "boisson" },
  { id: "vege", label: "Végétarien", test: (r) => r.cats.includes("vegetarien") },
  { id: "douceurs", label: "Douceurs", test: SWEET },
  { id: "boissons", label: "Boissons", test: (r) => r.role === "boisson" },
  { id: "zero", label: "Anti-gaspi", test: (r) => r.cats.includes("zero_dechet") || r.zeroWaste.length > 0 },
];

/** Paniers tout faits : une entrée ou un plat salé, quelque chose à grignoter, une douceur, une boisson. */
export const PANIERS: { id: string; title: string; for: string; ids: string[] }[] = [
  { id: "enfants", title: "Le panier des enfants", for: "Tout se mange avec les doigts, rien ne pique, ils peuvent tout préparer avec toi.", ids: ["pinwheels_tortilla", "brochettes_caprese_melon", "pizza_scrolls", "energy_balls_dattes", "eau_infusee_epluchures"] },
  { id: "classique", title: "Le pique-nique à la française", for: "Les valeurs sûres, à préparer la veille.", ids: ["pain_surprise", "terrine_legumes", "taboule_semoule", "tarte_courgette_chevre", "sables_bretons", "citronnade_menthe"] },
  { id: "monde", title: "Le tour du monde sur la nappe", for: "Un plat par continent, tous froids.", ids: ["onigirazu", "bocadillo_tortilla", "muffuletta_vege", "dolma_riz", "cornish_pasty", "the_glace_peche"] },
  { id: "grands", title: "Le pique-nique des grands", for: "Plus relevé, à partager entre adultes.", ids: ["brochettes_poulet_tandoori_froid", "ajitama", "courgettes_scapece", "muhammara", "crackers_pain_rassis", "flapjacks"] },
  { id: "antigaspi", title: "Le panier anti-gaspi", for: "Avec ce qui reste dans le frigo et le placard.", ids: ["bocadillo_tortilla", "taboule_chou_fleur", "crackers_pain_rassis", "barres_cereales_maison", "banana_bread", "eau_infusee_epluchures"] },
];

export const SECURITE: string[] = [
  "Glacière ou sac isotherme avec deux pains de glace (ou des bouteilles d'eau congelées, qui serviront de boisson fraîche ensuite).",
  "Hors du froid : 2 h au plus, 1 h s'il fait plus de 32 °C. Ce qui est resté au soleil ne se rapporte pas à la maison.",
  "Pas de mayonnaise crue, de crème pâtissière, de tiramisu ni de poisson cru en plein air : vinaigrette, yaourt, houmous et pesto tiennent bien mieux.",
  "Viandes et œufs : bien cuits la veille et refroidis vite au frigo, jamais tièdes dans la glacière.",
  "Une boîte par préparation : un plat qui fuit contamine le reste. Les crudités à part des viandes.",
  "Mains : un savon solide et une bouteille d'eau pour se rincer, ou un gel hydroalcoolique.",
  "Avant 4 ans : raisins et tomates cerises coupés en deux dans la longueur, pas de fruits à coque entiers, pas de popcorn.",
  "Allergies : une étiquette sur chaque boîte quand des enfants d'autres familles partagent la nappe.",
];

export const SAC: [string, string][] = [
  ["La veille", "Cuire, refroidir, mettre en boîtes ; congeler les bouteilles d'eau ; vérifier les pains de glace."],
  ["Dans la glacière", "Au fond le plus froid (viandes, œufs, laitages), au-dessus les salades, en haut les fruits et les douceurs."],
  ["Dans le panier", "Nappe, torchons (qui servent aussi d'emballage), couverts et gobelets réutilisables, une planche et un couteau, un sac pour les déchets, du sel."],
  ["Sur place", "Ouvrir la glacière le moins possible, la mettre à l'ombre, servir les plats froids en premier."],
];

export const ZERO: string[] = [
  "Boîtes en verre ou en inox, bocaux, et emballages en tissu ciré à la place du film et de l'aluminium.",
  "Torchons pour envelopper les sandwichs : ils servent ensuite de serviettes.",
  "Gourdes et carafes plutôt que des bouteilles jetables ; l'eau infusée se fait avec les épluchures d'agrumes et les tiges d'herbes.",
  "Parts à la bonne taille : on prévoit pour le nombre de personnes, pas « au cas où » ; ce qui revient au frais se mange le soir même.",
  "Pelures et noyaux dans un sac à part pour le compost ; rien ne reste sur l'herbe.",
];

/** Restes du frigo qui deviennent un pique-nique (relié à la cuisine des restes). */
export const RESTES_PN: [string, string, string][] = [
  ["riz", "Riz de la veille (24 h au plus)", "Salade de riz, onigiri, onigirazu"],
  ["volaille", "Poulet rôti", "Wraps, club sandwich, pinwheels"],
  ["pates", "Pâtes cuites", "Salade de pâtes à la grecque ou au pesto"],
  ["pdt", "Pommes de terre cuites", "Tortilla espagnole, salade souabe"],
  ["legumes_cuits", "Légumes cuits ou grillés", "Terrine, frittata, muffuletta, cake salé"],
  ["pain", "Pain rassis", "Crackers aux herbes, pan bagnat, bocadillo"],
  ["fruits", "Fruits trop mûrs", "Banana bread, boules d'énergie, eau infusée"],
];

/** La gamelle (école, travail) : ce qui change par rapport au pique-nique. */
export const GAMELLE: string[] = [
  "Plat chaud : un thermos alimentaire préchauffé 5 min à l'eau bouillante, rempli brûlant le matin, garde chaud jusqu'à midi.",
  "Plat à réchauffer : au micro-ondes jusqu'à ce que ce soit brûlant au cœur, en remuant à mi-chemin ; une seule fois.",
  "Le riz de la veille ne voyage pas tiède : frigo, puis glacière ou réchauffé brûlant.",
  "Pour les petits mangeurs : plusieurs petites boîtes (bento) plutôt qu'une grande, avec un aliment qu'ils connaissent à chaque fois.",
];
