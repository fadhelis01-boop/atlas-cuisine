// Finition et dressage (audit, regard du chef 🟠 7) : une ligne de présentation par fiche, et le réflexe
// « goûte et rectifie » pour le salé. Règles par famille de plats, du plus précis au plus général.
// Rédaction NON TESTÉE en cuisine (Tome 7 §2) ; ce sont les gestes classiques de la restauration.
import { INGREDIENTS } from "./data";
import { flatten } from "./engine";
import { norm } from "./text";
import type { Recipe } from "./types";

export interface Finish { taste: string | null; plate: string; green: string | null }

// [motif, finition, pour : s = salé, d = sucré, * = tout]
const RULES: [RegExp, string, "s" | "d" | "*"][] = [
  [/boisson|smoothie|lassi|limonade|jus |the glace|sirop|milkshake|chai|chocolat chaud|horchata|ayran|cafe/, "Verres passés 10 min au congélateur ; la garniture (rondelle d'agrume, feuille de menthe) au bord du verre, ajoutée au moment de servir.", "*"],
  [/sauce|mayo|vinaigrette|pesto|chutney|ketchup|pickles|marinade|chimichurri|salsa|raita|toum|tapenade|houmous|dip/, "Sers à part dans un petit bol, à température ambiante pour une sauce froide (le froid éteint les arômes) ; un filet d'huile ou une pincée d'épice sur le dessus.", "*"],
  [/soupe|veloute|potage|bouillon|harira|pho|ramen|laksa|bortsch|gaspacho|gazpacho|minestrone|tom kha|caldo|bisque|lablabi|tourin|garbure/, "Bols chauds (passés 1 min à l'eau bouillante) ; au dernier moment, un filet d'huile d'olive ou de crème, des herbes ciselées et un tour de moulin à poivre.", "s"],
  [/salade|taboule|carpaccio|ceviche|tartare|poke|fattouche|panzanella|som tam|crudite|carottes rapees|celeri remoulade/, "Assaisonne au dernier moment dans un grand saladier, puis dresse en hauteur sur assiette froide ; garde quelques graines, herbes ou copeaux de fromage pour le dessus.", "s"],
  [/mousse|creme |panna cotta|flan|ile flottante|tiramisu|verrine|riz au lait|kheer|mahalabia|pudding|creme brulee|creme caramel/, "Sers bien froid en verrines ou coupelles ; au moment de servir, un élément croquant (biscuit émietté, fruits secs torréfiés) et un fruit frais ou un zeste.", "d"],
  [/tarte|gateau|cake|fondant|brownie|buche|fraisier|cheesecake|quatre quarts|clafoutis|far |kouign|baba|charlotte|millefeuille|paris brest|eclair|macaron|financier|madeleine|cookie|sable|biscuit|choux|chouquette|profiterole/, "Coupe avec un couteau trempé dans l'eau chaude et essuyé entre chaque part ; sucre glace ou cacao tamisé au dernier moment, jamais à l'avance (il fond).", "d"],
  [/glace|sorbet/, "Sors la glace 5 à 10 min avant pour qu'elle se boule bien ; cuillère trempée dans l'eau chaude, coupes refroidies au congélateur.", "d"],
  [/pain|baguette|brioche|fougasse|focaccia|naan|pita|bagel|ciabatta|bretzel|croissant|viennois/, "Laisse refroidir sur une grille avant de trancher (la mie finit de cuire) ; pour le servir tiède, 5 min au four à 180 °C suffisent.", "*"],
  [/steak|cote de boeuf|entrecote|magret|roti|gigot|souris|carre|poulet roti|crapaudine|brochette|kofta|souvlaki|grill|tataki|chich taouk|currywurst/, "Laisse reposer la viande la moitié de son temps de cuisson, puis tranche contre les fibres ; dispose en éventail sur assiette chaude, le jus en cordon, fleur de sel et poivre au dernier moment.", "s"],
  [/saumon|cabillaud|dorade|bar |sole|lieu|maquereau|sardine|thon|poisson|merlu|truite|saint jacques|gambas|crevette|moule|calamar|bacalhau|morue|brandade/, "Côté peau en haut s'il est croustillant (la sauce dessous, jamais dessus) ; un quartier de citron, de l'aneth ou du persil, une pincée de fleur de sel.", "s"],
  [/pates|spaghetti|risotto|gnocchi|nouilles|udon|ramen|pad thai|yakisoba|tagliatelle|penne|cacio|carbonara/, "Assiettes creuses chaudes ; enroule les pâtes avec une pince et une louche pour faire un nid ; parmesan, herbes ou piment, et un filet d'huile au dernier moment.", "s"],
  [/gratin|tarte|quiche|lasagne|moussaka|hachis|parmentier|tartiflette|pizza|flammekueche|pie|clafoutis sale|cake sale|tian/, "Laisse tiédir 5 à 10 min avant de couper : les parts se tiennent ; une salade verte bien assaisonnée à côté apporte fraîcheur et couleur.", "s"],
  [/tajine|curry|cari|colombo|mafe|yassa|daube|blanquette|bourguignon|ragout|navarin|osso buco|rendang|moambe|chili|dal|chana|stew|goulash|carbonade|poule au pot|pot au feu|mijote|wot|feijoada|cassoulet|couscous|biryani|paella|jollof|thieb/, "Assiettes creuses chaudes ; la viande ou les légumes d'abord, la sauce nappée sans noyer, la garniture (riz, semoule, pain) à côté ; herbes fraîches, zeste ou oignon frit juste avant de servir.", "s"],
];
const DEFAULT_SALE = "Assiette chaude pour un plat chaud, froide pour un plat froid ; essuie les bords avec un papier ; une touche verte (herbes) ou acide (citron) au dernier moment.";
const DEFAULT_SUCRE = "Assiettes à dessert à température ambiante ; un fruit frais, quelques feuilles de menthe ou un zeste au moment de servir.";
const HERBS = /persil|coriandre|ciboulette|basilic|menthe|aneth|cerfeuil|estragon|oignon nouveau|cebette/;

export function finishFor(r: Recipe): Finish {
  const t = norm(`${r.title} ${r.kind} ${r.id.replace(/_/g, " ")}`);
  const sweet = r.role === "dessert" || /dessert|gouter/.test(norm(r.kind));
  const drink = r.role === "boisson";
  const plate = RULES.find(([rx, , k]) => (k === "*" || (k === "d") === sweet) && rx.test(t))?.[1] ?? (sweet ? DEFAULT_SUCRE : DEFAULT_SALE);
  const steps = norm(r.steps.join(" "));
  const salty = !sweet && !drink && !/^(Base|Pain)$/.test(r.kind);
  const taste = salty && !/goute|rectifi/.test(steps)
    ? "Il manque de relief ? une pincée de sel. Lourd ou plat ? un trait de citron ou de vinaigre. Trop acide (tomate) ? une pincée de sucre. Trop salé ? un peu d'eau, de crème ou de pomme de terre."
    : null;
  const hasHerb = flatten(r.ingredients).some((l) => HERBS.test(norm(`${l.ref ?? ""} ${l.label}`)));
  const green = salty && !hasHerb && /Plat|Entrée|Accompagnement/.test(r.kind) ? "Pour la couleur : quelques brins d'herbe fraîche (persil, ciboulette, coriandre) ciselés au dernier moment rendent l'assiette plus appétissante." : null;
  return { taste, plate, green };
}

/** Repère d'équilibre (audit 🟢 9), sans culpabiliser : ce qu'il manque pour un repas complet. */
export function balanceOf(r: Recipe): string | null {
  if (r.role !== "plat") return null;
  const secs = flatten(r.ingredients).filter((l) => l.ref && l.weight >= 1).map((l) => INGREDIENTS[l.ref!]?.section ?? "");
  const veg = secs.some((x) => /^Légumes/.test(x));
  const starch = secs.some((x) => /^(Légumineuses|Farines)/.test(x)) || flatten(r.ingredients).some((l) => /pomme de terre|patate|manioc|igname|plantain|riz|pâtes|semoule|pain/i.test(l.ref ?? ""));
  const prot = secs.some((x) => /^(Viandes|Poissons|Porc|Œufs)/.test(x)) || secs.some((x) => /^Légumineuses/.test(x));
  const add = [!veg && "des légumes ou une salade", !starch && "un féculent (pain, riz, semoule ou pommes de terre)", !prot && "une source de protéines (œuf, légumineuses, fromage, poisson)"].filter(Boolean);
  return add.length ? `Pour un repas complet, ajoute ${add.join(" et ")} ; un fruit ou un laitage en dessert.` : "Assiette complète : légumes, féculent et protéines ; un fruit ou un laitage en dessert suffit.";
}
