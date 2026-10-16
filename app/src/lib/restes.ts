// Cuisine des restes (audit du chef, 16/10/2026). Complète le zéro déchet « ingrédient par ingrédient » (ce qu'il reste d'un
// produit cru entamé) : ici on part de ce qui est DÉJÀ CUIT ou entamé dans le frigo (poulet rôti, riz, purée, pain rassis,
// fruits trop mûrs…) et on propose une entrée, un plat, un sandwich, un dessert, ou un menu complet qui les réunit.
// Règles validées respectées : rien au porc ni à l'alcool dans les idées, liens vers des fiches filtrés par le profil (verdict),
// tutoiement, repères par les sens. Idées de cuisinier NON TESTÉES (Tome 7 §2), sauf quand elles renvoient à une fiche.
import { RECIPE_BY_ID, RECIPES } from "./data";
import { verdict } from "./engine";
import type { Profile, Recipe } from "./types";
import { norm } from "./text";

export type Course = "entree" | "plat" | "sandwich" | "dessert";
export const COURSES: { id: Course; label: string; icon: string }[] = [
  { id: "entree", label: "Entrée", icon: "leaf" }, { id: "plat", label: "Plat", icon: "pot" },
  { id: "sandwich", label: "Sandwich", icon: "bread" }, { id: "dessert", label: "Dessert", icon: "cake" },
];

export interface IdeeReste {
  course: Course;
  title: string;
  how: string;             // la méthode en une ou deux phrases, avec un repère
  recipe?: string;         // fiche ATLAS liée
  with?: string[];         // autres restes qui s'y marient (pour composer un menu)
  adds?: string[];         // allergènes ajoutés par l'idée (codes UE du Tome 3)
  minutes: number;
}
export interface Reste {
  id: string;
  name: string;
  group: "viande" | "poisson" | "feculent" | "legume" | "pain" | "oeuf" | "laitier" | "fruit" | "sucre" | "base";
  flesh: boolean;          // viande ou poisson : masqué pour un profil végétarien
  allergens: string[];
  days: number;            // conservation au frigo après cuisson (jours)
  keep: string;
  safety?: string;
  match: RegExp;           // reconnaît ce reste dans une recette ATLAS (titre + ingrédients normalisés)
  ideas: IdeeReste[];
}

const FRIGO3 = "3 jours au frigo dans une boîte fermée, mis au froid moins de 2 h après la cuisson.";
export const RESTES: Reste[] = [
  { id: "volaille", name: "Poulet rôti, volaille cuite", group: "viande", flesh: true, allergens: [], days: 3,
    keep: FRIGO3 + " Effiloché, il se congèle 3 mois.", safety: "Réchauffe une seule fois, jusqu'à ce que ce soit brûlant au cœur (74 °C).",
    match: /poulet|volaille|dinde|pintade|chapon/,
    ideas: [
      { course: "entree", title: "Salade César", how: "Le poulet en lamelles sur romaine, croûtons et sauce César : un reste devient une entrée de bistrot.", recipe: "salade_cesar_poulet", with: ["pain"], adds: ["GL", "OE", "LA", "PO"], minutes: 15 },
      { course: "entree", title: "Bouillon de la carcasse", how: "La carcasse, un oignon, une carotte, 2 h à frémissement : la base d'un velouté ou d'un risotto.", recipe: "bouillon_volaille", minutes: 15 },
      { course: "plat", title: "Riz cantonais", how: "Avec le riz de la veille : tout sauté à feu vif, œuf brouillé, petits pois.", recipe: "riz_cantonais", with: ["riz"], adds: ["OE", "SO"], minutes: 20 },
      { course: "plat", title: "Croquetas de poulet", how: "Effiloché dans une béchamel épaisse, refroidi, pané, frit : le grand classique espagnol des restes.", recipe: "croquetas", adds: ["GL", "LA", "OE"], minutes: 50 },
      { course: "plat", title: "Enchiladas", how: "Roulé dans des tortillas, sauce tomate pimentée et fromage, 20 min au four.", recipe: "enchiladas_poulet", with: ["tortillas"], adds: ["GL", "LA"], minutes: 35 },
      { course: "sandwich", title: "Wrap croquant", how: "Tortilla, poulet, crudités, sauce yaourt : roulé serré, coupé en biais.", recipe: "wrap_poulet_croquant", with: ["tortillas", "legumes_crus"], adds: ["GL", "LA"], minutes: 10 },
      { course: "sandwich", title: "Croque au pesto", how: "Pain de mie, pesto, poulet, mozzarella, doré à la poêle sous un poids.", recipe: "croque_poulet_pesto", with: ["fromages"], adds: ["GL", "LA", "FC"], minutes: 10 },
    ] },
  { id: "viande_rotie", name: "Rôti de bœuf, gigot, steak cuit", group: "viande", flesh: true, allergens: [], days: 3, keep: FRIGO3,
    safety: "Viande rosée : à manger froide ou juste tiédie ; ne la recuis pas longtemps, elle durcit.",
    match: /roti de boeuf|gigot|cote de boeuf|entrecote|rumsteck|bavette|steak/,
    ideas: [
      { course: "entree", title: "Salade de bœuf à la thaïe", how: "Tranches très fines, oignon rouge, menthe, coriandre ; sauce citron vert, sauce de poisson, piment, un peu de sucre.", adds: ["PO"], minutes: 15 },
      { course: "plat", title: "Hachis Parmentier", how: "La viande hachée au couteau, revenue avec un oignon et un peu de jus, sous une purée gratinée.", recipe: "hachis_parmentier", with: ["puree"], adds: ["LA"], minutes: 45 },
      { course: "plat", title: "Émincé sauté minute", how: "En lanières, 1 min dans un wok fumant avec légumes et sauce soja : juste réchauffé, jamais recuit.", with: ["legumes_cuits", "riz"], adds: ["SO", "GL"], minutes: 15 },
      { course: "sandwich", title: "Sandwich rosbif", how: "Pain de campagne, moutarde, tranches fines, cornichons, roquette : le classique anglais du lundi.", with: ["pain"], adds: ["GL", "MO"], minutes: 5 },
    ] },
  { id: "mijote", name: "Viande mijotée (bourguignon, pot-au-feu, daube, tajine)", group: "viande", flesh: true, allergens: [], days: 4,
    keep: "4 jours au frigo, souvent meilleur le lendemain ; 3 mois au congélateur avec sa sauce.", safety: "Réchauffe à frémissement, jamais tiède : un mijoté se réchauffe une seule fois.",
    match: /bourguignon|pot au feu|daube|mijot|ragout|tajine|carbonnade|navarin|blanquette|goulash|joue|jarret|paleron/,
    ideas: [
      { course: "entree", title: "Salade de pot-au-feu", how: "Bœuf froid en dés, pommes de terre, échalote, cornichons, persil, vinaigrette moutardée.", with: ["pdt"], adds: ["MO"], minutes: 15 },
      { course: "plat", title: "Hachis Parmentier", how: "La viande effilochée liée de sa sauce sous une purée : le parmentier le plus goûteux qui soit.", recipe: "hachis_parmentier", with: ["puree"], adds: ["LA"], minutes: 40 },
      { course: "plat", title: "Empanadas", how: "Effiloché, un peu de sauce réduite, dans une pâte brisée ou à empanadas, 20 min au four.", recipe: "empanadas", adds: ["GL", "OE"], minutes: 45 },
      { course: "plat", title: "Pâtes au ragù de restes", how: "La viande effilochée dans sa sauce allongée d'une louche d'eau de cuisson, sur des pâtes larges, parmesan.", with: ["pates"], adds: ["GL", "LA"], minutes: 20 },
      { course: "sandwich", title: "Effiloché en pain brioché", how: "Viande réchauffée dans sa sauce réduite (elle doit coller), pain brioché toasté, oignons pickles.", with: ["brioche"], adds: ["GL", "OE", "LA"], minutes: 15 },
    ] },
  { id: "bolognaise", name: "Sauce bolognaise, chili, viande hachée cuite", group: "viande", flesh: true, allergens: [], days: 3, keep: FRIGO3 + " Se congèle 3 mois.",
    match: /bolognaise|chili con carne|ragu|keftedes|kefta|boulettes/,
    ideas: [
      { course: "plat", title: "Lasagnes", how: "Bolognaise, béchamel, pâtes à lasagnes, fromage : 40 min au four.", recipe: "lasagnes_bolognaise", adds: ["GL", "LA", "OE"], minutes: 60 },
      { course: "plat", title: "Pommes de terre farcies", how: "Pommes de terre cuites évidées, remplies de sauce, fromage, 15 min au four.", with: ["pdt", "fromages"], adds: ["LA"], minutes: 25 },
      { course: "plat", title: "Empanadas", how: "Sauce bien réduite (elle ne doit pas couler), en chaussons, 20 min au four.", recipe: "empanadas", adds: ["GL", "OE"], minutes: 45 },
      { course: "sandwich", title: "Sloppy joe", how: "Sauce réduite avec un trait de ketchup, dans un pain à burger toasté, cornichons.", adds: ["GL"], minutes: 10 },
    ] },
  { id: "poisson", name: "Poisson cuit", group: "poisson", flesh: true, allergens: ["PO"], days: 2,
    keep: "2 jours au frigo maximum.", safety: "Le poisson cuit se garde moins longtemps que la viande : 48 h, réchauffé une seule fois. Odeur forte ou d'ammoniaque : on jette.",
    match: /poisson|saumon|cabillaud|colin|lieu noir|dorade|bar\b|thon|maquereau|morue|merlu/,
    ideas: [
      { course: "entree", title: "Rillettes de poisson", how: "Émietté à la fourchette avec fromage frais, citron, ciboulette, poivre : sur des toasts.", adds: ["LA"], minutes: 10 },
      { course: "plat", title: "Croquettes de poisson", how: "Poisson et purée à parts égales, œuf, herbes, chapelure, poêlées : dorées et moelleuses.", recipe: "croquettes_poisson", with: ["puree"], adds: ["GL", "OE"], minutes: 30 },
      { course: "plat", title: "Parmentier de poisson", how: "Poisson émietté avec épinards et un peu de crème, sous une purée gratinée.", with: ["puree"], adds: ["LA"], minutes: 35 },
      { course: "plat", title: "Brandade express", how: "Poisson blanc écrasé avec pommes de terre, ail et huile d'olive chaude, gratiné.", recipe: "brandade", with: ["pdt"], minutes: 30 },
      { course: "sandwich", title: "Tacos de poisson", how: "Tortillas chaudes, poisson réchauffé 1 min, chou cru, sauce yaourt-citron vert.", recipe: "tacos_poisson_express", with: ["tortillas"], adds: ["GL", "LA"], minutes: 15 },
    ] },
  { id: "riz", name: "Riz cuit", group: "feculent", flesh: false, allergens: [], days: 1,
    keep: "24 h au frigo, refroidi en moins d'1 h (étalé dans un plat).", safety: "Le riz cuit laissé tiède fabrique une toxine que la cuisson ne détruit pas (Bacillus cereus) : au frigo vite, 24 h maximum, réchauffé une seule fois et brûlant.",
    match: /\briz\b|risotto|pilaf|biryani|paella/,
    ideas: [
      { course: "entree", title: "Arancini", how: "Riz lié d'un peu de parmesan et d'œuf, boulettes avec un dé de mozzarella au cœur, panées, frites.", recipe: "arancini", with: ["fromages"], adds: ["GL", "LA", "OE"], minutes: 40 },
      { course: "entree", title: "Salade de riz", how: "Riz froid, thon ou pois chiches, maïs, tomates, vinaigrette.", recipe: "salade_riz_thon_mais", adds: ["PO"], minutes: 10 },
      { course: "plat", title: "Riz sauté aux restes", how: "Wok très chaud, riz froid égrené (le riz de la veille ne colle pas), tous les restes de légumes et de viande, œuf.", recipe: "riz_saute_restes", with: ["legumes_cuits", "volaille"], adds: ["OE", "SO"], minutes: 15 },
      { course: "plat", title: "Nasi goreng", how: "Le riz sauté indonésien au kecap manis, œuf au plat dessus.", recipe: "nasi_goreng", adds: ["OE", "SO"], minutes: 20 },
      { course: "dessert", title: "Riz au lait express", how: "Riz cuit, lait, sucre, vanille, 15 min à feu doux en remuant : crémeux. Avec des fruits trop mûrs poêlés.", with: ["fruits"], adds: ["LA"], minutes: 20 },
    ] },
  { id: "pates", name: "Pâtes cuites", group: "feculent", flesh: false, allergens: ["GL"], days: 3, keep: FRIGO3,
    match: /pates|spaghetti|penne|tagliatelle|macaroni|fusilli|lasagne/,
    ideas: [
      { course: "entree", title: "Salade de pâtes au pesto", how: "Pâtes froides, pesto, tomates cerises, mozzarella, roquette.", recipe: "salade_pates_pesto_tomates", adds: ["LA", "FC"], minutes: 10 },
      { course: "plat", title: "Gratin de pâtes", how: "Pâtes, béchamel ou crème, bouts de fromage, restes de légumes, 20 min à 200 °C : gratiné.", recipe: "gratin_pates_restes", with: ["fromages", "legumes_cuits"], adds: ["LA"], minutes: 30 },
      { course: "plat", title: "Frittata di pasta", how: "Pâtes mélangées à 4 œufs battus et du parmesan, cuites à la poêle comme une galette épaisse, retournée : croustillante dehors.", with: ["fromages"], adds: ["OE", "LA"], minutes: 20 },
    ] },
  { id: "puree", name: "Purée de pommes de terre", group: "feculent", flesh: false, allergens: ["LA"], days: 3, keep: FRIGO3,
    match: /puree|parmentier|aligot/,
    ideas: [
      { course: "entree", title: "Velouté minute", how: "Purée détendue avec du bouillon chaud, un poireau fondu, mixée : un velouté en 10 min.", with: ["bouillon", "legumes_cuits"], minutes: 15 },
      { course: "plat", title: "Croquettes de restes", how: "Purée, un œuf, fromage râpé, herbes ; boulettes panées et dorées.", recipe: "croquettes_restes", with: ["fromages"], adds: ["GL", "OE"], minutes: 30 },
      { course: "plat", title: "Galettes de purée", how: "Purée + 1 œuf + 2 c. à s. de farine, palets dorés au beurre 3 min par face ; un œuf au plat dessus.", adds: ["OE", "GL"], minutes: 20 },
      { course: "plat", title: "Hachis Parmentier", how: "La couverture idéale de tous les restes de viande ou de lentilles.", recipe: "hachis_parmentier", with: ["mijote", "viande_rotie"], minutes: 40 },
    ] },
  { id: "pdt", name: "Pommes de terre cuites (vapeur, à l'eau, au four)", group: "feculent", flesh: false, allergens: [], days: 3, keep: FRIGO3,
    match: /pomme de terre|pommes de terre|patate/,
    ideas: [
      { course: "entree", title: "Salade de pommes de terre", how: "En rondelles, arrosées de bouillon chaud et de vinaigrette, oignon, ciboulette : à la souabe.", recipe: "kartoffelsalat", minutes: 15 },
      { course: "plat", title: "Rösti", how: "Râpées froides, galette épaisse dorée au beurre 10 min par face.", recipe: "rosti", adds: ["LA"], minutes: 25 },
      { course: "plat", title: "Tortilla espagnole", how: "En tranches, avec un oignon fondu, dans 6 œufs battus, cuite doucement puis retournée.", recipe: "tortilla_espanola", adds: ["OE"], minutes: 25 },
      { course: "plat", title: "Pommes de terre sautées", how: "En cubes, poêle chaude, huile, sans y toucher 4 min : croûte dorée ; ail et persil à la fin.", minutes: 15 },
    ] },
  { id: "legumes_cuits", name: "Légumes cuits ou rôtis, ratatouille", group: "legume", flesh: false, allergens: [], days: 3, keep: FRIGO3,
    match: /ratatouille|legumes|courgette|aubergine|poivron|brocoli|chou fleur|carotte|epinard|haricots verts|tian|briam/,
    ideas: [
      { course: "entree", title: "Velouté", how: "Légumes + bouillon à hauteur, 10 min, mixés ; un trait de crème ou d'huile d'olive.", with: ["bouillon"], minutes: 15 },
      { course: "entree", title: "Tartinade", how: "Légumes rôtis mixés avec pois chiches ou fromage frais, citron, cumin : sur du pain grillé.", with: ["legumineuses", "pain"], adds: ["LA"], minutes: 10 },
      { course: "plat", title: "Frittata", how: "Légumes dans 6 œufs battus et du fromage, poêle puis 5 min sous le gril : gonflée et dorée.", recipe: "frittata_courgettes", with: ["fromages"], adds: ["OE", "LA"], minutes: 20 },
      { course: "plat", title: "Cake salé", how: "Farine, œufs, lait, huile, fromage, légumes en dés : 45 min au four, pour le pique-nique.", recipe: "cake_sale", adds: ["GL", "OE", "LA"], minutes: 60 },
      { course: "plat", title: "Crumble salé", how: "Légumes au fond, pâte sablée farine-beurre-parmesan émiettée dessus, 25 min au four.", recipe: "crumble_sale_legumes", adds: ["GL", "LA"], minutes: 40 },
      { course: "plat", title: "Œufs cocotte à la ratatouille", how: "Ratatouille chaude dans des ramequins, un œuf cassé dessus, 8 min au four : jaune coulant.", adds: ["OE"], minutes: 15 },
      { course: "sandwich", title: "Quesadillas", how: "Légumes et fromage entre deux tortillas, dorées à sec 2 min par face.", recipe: "quesadillas_haricots_fromage", with: ["tortillas", "fromages"], adds: ["GL", "LA"], minutes: 10 },
    ] },
  { id: "legumes_crus", name: "Légumes crus fatigués, salade, herbes qui fanent", group: "legume", flesh: false, allergens: [], days: 2,
    keep: "Les ranimer d'abord : 20 min dans l'eau glacée (salade, herbes, carottes, céleri retrouvent leur croquant).",
    safety: "Moisissure, odeur aigre ou partie gluante : on coupe largement, et si c'est étendu, on jette.",
    match: /salade|herbes|carotte|celeri|concombre|tomate|poireau/,
    ideas: [
      { course: "entree", title: "Soupe du fond du frigo", how: "Tous les légumes en morceaux, un oignon, eau à hauteur, 20 min, mixés.", recipe: "minestrone", minutes: 30 },
      { course: "entree", title: "Pesto ou sauce verte", how: "Herbes fanées, fanes, ail, huile, parmesan ou noix, mixés : se garde 5 jours sous une couche d'huile.", recipe: "pesto", adds: ["LA", "FC"], minutes: 10 },
      { course: "plat", title: "Crumble de légumes", how: "Les légumes coupés, rôtis 15 min, puis couverts de crumble au parmesan.", recipe: "crumble_sale_legumes", adds: ["GL", "LA"], minutes: 45 },
      { course: "sandwich", title: "Pickles rapides pour les sandwichs", how: "Légumes en fines lamelles, vinaigre chaud sucré-salé versé dessus : croquants dès 30 min, 2 semaines au frigo.", minutes: 10 },
    ] },
  { id: "legumineuses", name: "Lentilles, pois chiches, haricots cuits", group: "feculent", flesh: false, allergens: [], days: 4, keep: "4 jours au frigo dans leur jus ; 3 mois au congélateur.",
    match: /lentille|pois chiche|haricots (rouges|blancs|noirs)|dal|houmous|feves/,
    ideas: [
      { course: "entree", title: "Houmous", how: "Pois chiches (ou haricots blancs), tahini, citron, ail, un glaçon, mixés 3 min : très lisse.", recipe: "houmous", adds: ["SE"], minutes: 10 },
      { course: "entree", title: "Salade de lentilles", how: "Lentilles, échalote, persil, vinaigrette moutardée ; un œuf mollet dessus.", recipe: "salade_lentilles", adds: ["MO"], minutes: 10 },
      { course: "plat", title: "Boulettes de lentilles", how: "Lentilles écrasées, chapelure, œuf, épices ; boulettes dorées puis mijotées dans la sauce tomate.", recipe: "boulettes_lentilles_tomate", with: ["sauce_tomate"], adds: ["GL", "OE"], minutes: 35 },
      { course: "plat", title: "Shakshuka aux haricots", how: "Haricots dans une sauce tomate épicée, œufs pochés dedans.", recipe: "shakshuka_haricots_blancs", with: ["sauce_tomate"], adds: ["OE"], minutes: 25 },
      { course: "sandwich", title: "Quesadillas aux haricots", how: "Haricots écrasés, fromage, coriandre entre deux tortillas dorées.", recipe: "quesadillas_haricots_fromage", with: ["tortillas", "fromages"], adds: ["GL", "LA"], minutes: 10 },
    ] },
  { id: "pain", name: "Pain rassis (baguette, campagne, pain de mie)", group: "pain", flesh: false, allergens: ["GL"], days: 5,
    keep: "Dans un sac en tissu ; ou tranché et congelé (il se grille directement).", safety: "Une tache de moisissure : on jette toute la tranche, le pain de mie entier s'il est moelleux (la moisissure s'étend sans se voir).",
    match: /pain|baguette|tartine|croute/,
    ideas: [
      { course: "entree", title: "Panzanella", how: "Pain rassis en cubes, tomates mûres, oignon rouge, basilic, huile et vinaigre : 20 min de repos, le pain boit le jus.", recipe: "panzanella", with: ["legumes_crus"], minutes: 20 },
      { course: "entree", title: "Soupe à l'oignon gratinée", how: "Oignons longuement caramélisés, bouillon, croûtons de pain rassis et fromage gratiné.", recipe: "soupe_oignon", with: ["bouillon", "fromages"], adds: ["LA"], minutes: 60 },
      { course: "plat", title: "Pain perdu salé", how: "Trempé dans œufs-lait, poêlé, garni de légumes, fromage ou œuf au plat.", recipe: "pain_perdu_sale", with: ["fromages", "legumes_cuits"], adds: ["OE", "LA"], minutes: 20 },
      { course: "sandwich", title: "Bruschetta", how: "Tranches grillées frottées d'ail, huile d'olive, tomates ou légumes rôtis dessus.", with: ["legumes_cuits"], minutes: 10 },
      { course: "dessert", title: "Pain perdu", how: "Trempé dans œufs, lait, sucre, vanille ; doré au beurre ; plus le pain est sec, meilleur il est.", recipe: "pain_perdu", with: ["fruits"], adds: ["OE", "LA"], minutes: 15 },
      { course: "dessert", title: "Pudding au pain", how: "Pain en morceaux, lait sucré, œufs, raisins ou fruits trop mûrs, 40 min au four 170 °C.", with: ["fruits", "laitages"], adds: ["OE", "LA"], minutes: 50 },
    ] },
  { id: "brioche", name: "Brioche, croissants, viennoiseries de la veille", group: "pain", flesh: false, allergens: ["GL", "OE", "LA"], days: 3,
    keep: "Dans un sac fermé ; congelées le jour même, elles se réchauffent 5 min au four.", match: /brioche|croissant|viennoiserie|pain au lait/,
    ideas: [
      { course: "dessert", title: "Pain perdu brioché", how: "Le meilleur pain perdu : brioche épaisse, trempage court, caramélisée au beurre et sucre.", recipe: "pain_perdu", with: ["fruits"], minutes: 15 },
      { course: "dessert", title: "Croissants aux amandes (bostock)", how: "Coupés en deux, imbibés de sirop, crème d'amande, amandes effilées, 15 min au four.", adds: ["FC"], minutes: 25 },
      { course: "sandwich", title: "Croissant dinde-fromage", how: "Ouvert, jambon de dinde, fromage, béchamel ou crème, 8 min au four.", with: ["fromages"], minutes: 12 },
    ] },
  { id: "tortillas", name: "Tortillas, pitas, naans, pains plats", group: "pain", flesh: false, allergens: ["GL"], days: 4, keep: "Dans leur sachet fermé ; se congèlent à plat.",
    match: /tortilla|pita|naan|lavash|chapati|paratha|wrap/,
    ideas: [
      { course: "entree", title: "Fattouche", how: "Pain grillé ou frit en morceaux dans une salade de crudités au sumac et citron.", recipe: "fattouche", with: ["legumes_crus"], minutes: 15 },
      { course: "plat", title: "Chilaquiles", how: "Tortillas en triangles dorées, mijotées 2 min dans une sauce verte, œuf et fromage dessus.", recipe: "chilaquiles_verts", adds: ["OE", "LA"], minutes: 25 },
      { course: "plat", title: "Kottu roti", how: "Pains plats en lanières sautés avec œuf, légumes et restes de curry, hachés à la spatule.", recipe: "kottu_roti", with: ["legumes_cuits", "volaille"], adds: ["OE"], minutes: 20 },
      { course: "sandwich", title: "Pizza tortilla", how: "Sauce tomate, fromage, restes de légumes, 8 min à 220 °C : croustillante.", recipe: "pizza_tortilla", with: ["sauce_tomate", "fromages"], adds: ["LA"], minutes: 12 },
    ] },
  { id: "semoule", name: "Semoule, couscous, quinoa, boulgour cuits", group: "feculent", flesh: false, allergens: ["GL"], days: 3, keep: FRIGO3,
    match: /semoule|couscous|quinoa|boulgour|taboule/,
    ideas: [
      { course: "entree", title: "Taboulé", how: "Graine froide, beaucoup de persil et menthe, tomates, citron, huile d'olive.", recipe: "taboule_semoule", with: ["legumes_crus"], minutes: 15 },
      { course: "plat", title: "Galettes de semoule aux légumes", how: "Graine + 1 œuf + fromage râpé + légumes en dés, palets dorés à la poêle.", with: ["legumes_cuits", "fromages"], adds: ["OE", "LA"], minutes: 20 },
      { course: "dessert", title: "Seffa express", how: "Couscous réchauffé à la vapeur avec du beurre, sucre glace, cannelle, raisins et amandes : le couscous sucré du Maroc.", adds: ["LA", "FC"], minutes: 15 },
    ] },
  { id: "fromages", name: "Bouts de fromages", group: "laitier", flesh: false, allergens: ["LA"], days: 7,
    keep: "Chaque morceau dans du papier (pas de film, il étouffe) ; les croûtes de parmesan se gardent pour les soupes.", safety: "Fromage dur moisi : on retire 1 cm autour. Fromage frais ou mou moisi : on jette.",
    match: /fromage|comte|gruyere|emmental|parmesan|mozzarella|chevre|feta|raclette|reblochon/,
    ideas: [
      { course: "entree", title: "Gougères", how: "Pâte à choux et fromage râpé, petites boules dorées : l'apéritif bourguignon.", recipe: "gougeres", adds: ["GL", "OE"], minutes: 45 },
      { course: "plat", title: "Gratin de pâtes aux bouts de fromage", how: "Tous les fromages râpés ou en dés dans une béchamel, sur des pâtes, gratiné.", recipe: "gratin_pates_restes", with: ["pates"], adds: ["GL"], minutes: 30 },
      { course: "sandwich", title: "Croque au four", how: "Pain de mie, béchamel, fromages mélangés, jambon de dinde ou légumes, 10 min au four.", with: ["pain"], adds: ["GL"], minutes: 15 },
    ] },
  { id: "laitages", name: "Yaourts, crème, lait proches de la date", group: "laitier", flesh: false, allergens: ["LA"], days: 2,
    keep: "Date limite (DLC) : avant la date, sans exception pour la crème et le lait frais. Yaourt nature : souvent bon quelques jours après s'il n'est pas bombé ni aigre.",
    match: /yaourt|creme|lait\b/,
    ideas: [
      { course: "dessert", title: "Gâteau au yaourt", how: "Le pot sert de mesure : 1 yaourt, 2 de sucre, 3 de farine, 3 œufs, ½ d'huile.", recipe: "gateau_yaourt", adds: ["GL", "OE"], minutes: 45 },
      { course: "dessert", title: "Panna cotta", how: "Crème et lait sucrés, vanille, gélatine ou agar-agar : prise en 4 h, coulis de fruits.", recipe: "panna_cotta", with: ["fruits"], minutes: 15 },
      { course: "plat", title: "Marinade au yaourt", how: "Yaourt, épices, citron : attendrit le poulet en 2 h (tandoori, kebabs).", recipe: "marinade_tandoori", minutes: 10 },
      { course: "entree", title: "Sauce yaourt aux herbes", how: "Yaourt, herbes hachées, citron, ail : pour les crudités, les grillades, les falafels.", recipe: "sauce_yaourt_herbes", with: ["legumes_crus"], minutes: 5 },
    ] },
  { id: "blancs", name: "Blancs d'œufs", group: "oeuf", flesh: false, allergens: ["OE"], days: 3, keep: "3 jours au frigo dans un bocal fermé ; 3 mois au congélateur (étiquette avec le nombre).",
    match: /jaune d.oeuf|jaunes|mayonnaise|creme anglaise|carbonara|creme brulee|creme patissiere/,
    ideas: [
      { course: "dessert", title: "Meringues", how: "Blancs montés, deux fois leur poids de sucre, four 100 °C 1 h 30 : sèches et légères.", recipe: "meringues", minutes: 20 },
      { course: "dessert", title: "Financiers", how: "Blancs, poudre d'amande, beurre noisette, sucre glace : moelleux et dorés.", recipe: "financiers", adds: ["FC", "LA", "GL"], minutes: 30 },
      { course: "plat", title: "Panure légère", how: "Blancs battus à la fourchette à la place de l'œuf entier pour paner poisson ou poulet.", minutes: 5 },
    ] },
  { id: "jaunes", name: "Jaunes d'œufs", group: "oeuf", flesh: false, allergens: ["OE"], days: 1, keep: "24 h au frigo, couverts d'un peu d'eau froide (ils ne croûtent pas).",
    safety: "Jaunes crus : pas pour les femmes enceintes, les petits et les personnes fragiles.", match: /blanc d.oeuf|blancs|meringue|financier|macaron|pavlova/,
    ideas: [
      { course: "entree", title: "Mayonnaise maison", how: "Un jaune, moutarde, huile en filet en fouettant : ferme et brillante.", recipe: "mayonnaise", adds: ["MO"], minutes: 10 },
      { course: "dessert", title: "Crème brûlée", how: "Jaunes, crème, sucre, vanille, 1 h au four doux, sucre caramélisé au moment de servir.", recipe: "creme_brulee", adds: ["LA"], minutes: 20 },
      { course: "dessert", title: "Crème anglaise", how: "Jaunes et sucre blanchis, lait vanillé chaud, cuite à 83 °C sans bouillir : elle nappe la cuillère.", adds: ["LA"], minutes: 20 },
    ] },
  { id: "fruits", name: "Fruits trop mûrs (bananes, pommes, poires, fraises, pêches)", group: "fruit", flesh: false, allergens: [], days: 2,
    keep: "Les abîmés à part (ils font mûrir les autres) ; épluchés et coupés, ils se congèlent pour les smoothies et les gâteaux.",
    safety: "Taches brunes et chair molle : c'est bon. Moisissure, odeur de fermentation ou de vinaigre : on jette (les petits fruits moisis contaminent toute la barquette).",
    match: /banane|pomme\b|pommes|poire|fraise|peche|abricot|mangue|fruits/,
    ideas: [
      { course: "dessert", title: "Banana bread", how: "Plus les bananes sont noires, plus il est bon : écrasées, œufs, sucre, farine, 50 min au four.", recipe: "banana_bread", adds: ["GL", "OE"], minutes: 60 },
      { course: "dessert", title: "Crumble", how: "Fruits en morceaux, pâte farine-beurre-sucre émiettée, 30 min au four : jus qui bouillonne.", recipe: "crumble_pommes_mures", adds: ["GL", "LA"], minutes: 40 },
      { course: "dessert", title: "Compote", how: "Fruits en morceaux, un fond d'eau, 20 min à couvert, écrasés ; sucre seulement si besoin.", recipe: "compote_pommes_poires", minutes: 25 },
      { course: "dessert", title: "Smoothie", how: "Fruits congelés en morceaux, yaourt ou lait, mixés : glacé sans glaçons.", recipe: "smoothie_fruits_abimes", with: ["laitages"], adds: ["LA"], minutes: 5 },
      { course: "plat", title: "Chutney pour viandes", how: "Fruits en dés, oignon, vinaigre de cidre, sucre, gingembre, 40 min : avec le poulet rôti ou le fromage.", with: ["volaille", "fromages"], minutes: 45 },
      { course: "sandwich", title: "Tartine beurre de cacahuète-banane", how: "Pain grillé, beurre de cacahuète, banane mûre écrasée, un filet de miel.", recipe: "tartines_beurre_cacahuete_banane", with: ["pain"], adds: ["AR", "GL"], minutes: 5 },
    ] },
  { id: "gateau", name: "Gâteau, biscuits secs, crêpes en trop", group: "sucre", flesh: false, allergens: ["GL", "OE", "LA"], days: 4,
    keep: "Gâteau sec : 4 jours dans une boîte en métal. Crêpes : 2 jours au frigo, filmées.", match: /gateau|biscuit|cake|crepe|madeleine|genoise/,
    ideas: [
      { course: "dessert", title: "Verrines façon trifle", how: "Gâteau en dés imbibé de jus de fruits, crème fouettée ou yaourt, fruits : en couches dans des verres.", with: ["fruits", "laitages"], minutes: 15 },
      { course: "dessert", title: "Base de cheesecake ou de crumble", how: "Biscuits mixés avec du beurre fondu : fond tassé, ou crumble express sur des fruits.", with: ["fruits"], minutes: 10 },
      { course: "plat", title: "Crêpes roulées gratinées", how: "Crêpes garnies d'épinards et fromage (ou de poulet), roulées, béchamel dessus, 20 min au four.", with: ["volaille", "fromages", "legumes_cuits"], minutes: 30 },
    ] },
  { id: "chocolat", name: "Chocolat entamé (tablettes, chocolat de Pâques)", group: "sucre", flesh: false, allergens: ["LA"], days: 60,
    keep: "Au sec et au frais (pas au frigo) ; le blanchiment gris est du beurre de cacao remonté : il reste bon.", match: /chocolat/,
    ideas: [
      { course: "dessert", title: "Mousse au chocolat", how: "Chocolat fondu, jaunes, blancs montés : 4 h au frais.", recipe: "mousse_chocolat", adds: ["OE"], minutes: 20 },
      { course: "dessert", title: "Fondant", how: "Chocolat, beurre, œufs, sucre, une cuillère de farine : 12 min au four, cœur coulant.", recipe: "fondant_chocolat", adds: ["OE", "GL"], minutes: 25 },
      { course: "dessert", title: "Pâte à tartiner maison", how: "Chocolat, noisettes grillées, un peu d'huile et de lait concentré, mixés.", recipe: "pate_tartiner_maison", adds: ["FC"], minutes: 15 },
    ] },
  { id: "bouillon", name: "Bouillon, jus de cuisson, eau des légumes", group: "base", flesh: false, allergens: [], days: 3,
    keep: "3 jours au frigo ; en bacs à glaçons au congélateur (un glaçon = une sauce).", match: /bouillon|pot au feu|poule au pot|fumet/,
    ideas: [
      { course: "plat", title: "Risotto", how: "Le bouillon chaud versé louche par louche sur le riz nacré : crémeux sans crème.", recipe: "risotto_champignons", adds: ["LA"], minutes: 30 },
      { course: "entree", title: "Velouté", how: "Base de tous les veloutés : légumes + bouillon, mixés.", recipe: "veloute_potiron", with: ["legumes_cuits", "puree"], minutes: 30 },
      { course: "plat", title: "Soupe de nouilles", how: "Bouillon brûlant, nouilles, restes de viande ou de tofu, cébette, un œuf mollet.", with: ["volaille", "mijote"], adds: ["GL", "OE"], minutes: 15 },
    ] },
  { id: "sauce_tomate", name: "Sauce tomate maison ou en bocal entamée", group: "base", flesh: false, allergens: [], days: 4,
    keep: "Bocal entamé : 4 jours au frigo ; ou en portions au congélateur.", match: /sauce tomate|tomates pelees|coulis|passata/,
    ideas: [
      { course: "plat", title: "Shakshuka", how: "Sauce tomate épicée, poivrons, œufs pochés dedans, feta : avec du pain.", recipe: "shakshuka", adds: ["OE"], minutes: 25 },
      { course: "sandwich", title: "Pizza tortilla", how: "Sauce, fromage, garnitures, 8 min au four très chaud.", recipe: "pizza_tortilla", with: ["tortillas", "fromages"], adds: ["GL", "LA"], minutes: 12 },
      { course: "entree", title: "Soupe de tomate", how: "Sauce allongée de bouillon, un trait de crème, basilic ; croûtons de pain rassis.", recipe: "soupe_tomate_express", with: ["bouillon", "pain"], minutes: 15 },
    ] },
];

export const RESTE_BY_ID: Record<string, Reste> = Object.fromEntries(RESTES.map((r) => [r.id, r]));

/** Idées compatibles avec le profil : végétarien, allergies, fiches liées non adaptées. */
export function ideasFor(reste: Reste, p: Profile, course?: Course): IdeeReste[] {
  if (p.vegetarian && reste.flesh) return [];
  if (reste.allergens.some((a) => p.allergens.includes(a))) return [];
  return reste.ideas.filter((i) => (!course || i.course === course)
    && !(i.adds ?? []).some((a) => p.allergens.includes(a))
    && !(i.recipe && (!RECIPE_BY_ID[i.recipe] || verdict(RECIPE_BY_ID[i.recipe], p).availability === "hidden")));
}

export interface MenuRestes { entree?: { reste: Reste; idea: IdeeReste }; plat?: { reste: Reste; idea: IdeeReste }; dessert?: { reste: Reste; idea: IdeeReste }; fallback?: Recipe }

/** Compose un menu complet : un reste différent par service quand c'est possible, en préférant les idées qui en réunissent plusieurs. */
export function buildMenu(selected: string[], p: Profile): MenuRestes {
  const restes = selected.map((id) => RESTE_BY_ID[id]).filter(Boolean);
  const main = new Set<string>(); const side = new Set<string>(); // reste vedette d'un service / reste d'accompagnement
  const pick = (course: Course) => {
    let best: { reste: Reste; idea: IdeeReste; score: number } | null = null;
    for (const r of restes) for (const idea of ideasFor(r, p, course)) {
      const score = (main.has(r.id) ? -10 : side.has(r.id) ? -4 : 0) + (idea.with ?? []).filter((w) => selected.includes(w) && !main.has(w)).length * 3 + (idea.recipe ? 1 : 0) - idea.minutes / 60;
      if (!best || score > best.score) best = { reste: r, idea, score };
    }
    if (best) { main.add(best.reste.id); for (const w of best.idea.with ?? []) if (selected.includes(w)) side.add(w); }
    return best ? { reste: best.reste, idea: best.idea } : undefined;
  };
  const plat = pick("plat"); const entree = pick("entree"); const dessert = pick("dessert");
  // pas de reste sucré : un dessert du placard, rapide et adapté au foyer
  const fallback = dessert ? undefined : RECIPES.find((r) => r.role === "dessert" && r.level === 1 && r.active <= 15 && r.rest <= 30
    && verdict(r, p).availability === "ok" && /compote|yaourt|fruit|riz au lait|smoothie|mousse/.test(norm(r.title)));
  return { entree, plat, dessert, fallback };
}

/** Les restes qu'une fiche ATLAS laisse probablement (pour le lien « Il en reste ? » de la fiche). */
export function restesOfRecipe(r: Recipe): Reste[] {
  if (r.role === "autre") return []; // boissons, sauces, pains, bases
  const text = norm(`${r.title} ${r.ingredients.map((l) => l.ref ?? "").join(" ")}`);
  const found = RESTES.filter((x) => !["blancs", "jaunes", "laitages", "legumes_crus", "chocolat", "fromages", "sauce_tomate", "tortillas", "brioche", "gateau", "fruits", "pain"].includes(x.id) && x.match.test(text));
  return found.slice(0, 3);
}

/** Âge d'un reste enregistré (jours entiers depuis la cuisson) et alerte de conservation. */
export function resteStatus(id: string, cooked: string, today = new Date()): { age: number; left: number; level: "ok" | "bientot" | "jeter" } {
  const r = RESTE_BY_ID[id];
  const age = Math.floor((today.getTime() - new Date(cooked).getTime()) / 86400000);
  const left = (r?.days ?? 3) - age;
  return { age, left, level: left < 0 ? "jeter" : left <= 0 ? "bientot" : "ok" };
}
