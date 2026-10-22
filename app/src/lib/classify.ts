// Import de recettes depuis TikTok et d'autres plateformes, avec tri automatique (Tome 1 §14).
// Contraintes réelles : TikTok n'offre pas d'accès public aux « Favoris » d'un compte ; les voies fiables sont
// le partage d'un lien (+ légende copiée), et l'export de données du compte (fichier JSON avec les liens des favoris).
// Le contenu importé est une DONNÉE : aucune instruction qu'il contient n'est suivie (Tome 7 §7.3).
import { INGREDIENTS, INGREDIENT_NAMES } from "./data";
import { norm } from "./text";

const RULES: { cat: string; macro?: string; re: RegExp }[] = [
  // Food fusion d'abord : un mélange de traditions prime sur la région d'un des ingrédients
  { cat: "fusion", macro: "fusion", re: /\b(fusion|feuilles? de riz|rice paper|pizza (tonkatsu|butter chicken|rendang|kebab|tacos)|(tonkatsu|butter chicken|rendang) pizza|couscous tiep|ramen carbonara|carbonara ramen|sushi burger|burger sushi|tacos? (coreen|thai|indien)|tex mex|bao (burger|teriyaki))\b/ },
  { cat: "fetes", re: /\b(noel|reveillon|ramadan|ftour|iftar|aid|tabaski|paques|halloween|fete des meres|nouvel an|galette des rois|chandeleur)\b/ },
  { cat: "boissons", re: /\b(bissap|jus de|smoothie|lassi|citronnade|limonade|cocktail|mocktail|the a la menthe|infusion|milkshake|boisson)\b/ },
  { cat: "sauces", re: /\b(sauce|mayo|mayonnaise|ketchup|vinaigrette|pesto|harissa|aioli|allioli|tzatziki|houmous|marinade|condiment|rub|chimichurri|nokoss|huile pimentee)\b/ },
  { cat: "pains", re: /\b(pain|baguette|brioche|naan|pita|focaccia|pizza|pate a pizza|crepes?|galette|msemen|batbout|chapati|tortillas?|bagel|ciabatta|panuozzo|pan de|rolls?|buns?|flatbread|bread|matlouh|khobz)\b/ },
  { cat: "desserts", re: /\b(gateau|cake|tarte|flan|tiramisu|cookie|brownie|mousse au chocolat|cheesecake|fondant|macaron|meringue|praline|ganache|patisserie|dessert|biscuits?|sable|donut|beignets? sucres|creme brulee|riz au lait|banana bread|crumble)\b/ },
  { cat: "techniques", re: /\b(technique|astuce|comment (couper|cuire|faire)|tuto|les bases|secret de)\b/ },
  { cat: "zero_dechet", re: /\b(anti gaspi|zero dechet|restes|ne jetez plus|epluchures|pain rassis)\b/ },
  { cat: "street_food", re: /\b(burger|kebab|tacos|nuggets|sandwich|wrap|hot dog|fast food|mcdo|kfc|frites)\b/ },
  { cat: "afrique", macro: "afrique", re: /\b(thieb|tieb|tiep|ceebu|yassa|mafe|attieke|alloco|jollof|foutou|fouti|ndole|poulet dg|bissap|dibi|senegal|mali|ivoir|guine|cameroun|nigeria|congo|togo|benin|gombo|akpi|soupou|placali)\b/ },
  { cat: "maghreb", macro: "maghreb", re: /\b(tajine|couscous|chorba|harira|msemen|batbout|bourek|brick|chakchouka|mloukhia|ojja|tangia|rechta|mhajeb|maroc|algeri|tunisi|kabyle|loubia|zaalouk)\b/ },
  { cat: "moyen_orient", macro: "moyen_orient", re: /\b(houmous|falafel|shawarma|chawarma|taboule|kebab|kofta|lahmacun|borek|pide|baklava|liban|syri|turc|turquie|grec|gyros|souvlaki|arayes|manakish|fattouche)\b/ },
  { cat: "asie", macro: "asie_est", re: /\b(ramen|sushi|teriyaki|gyoza|udon|katsu|kimchi|bibimbap|tteok|bulgogi|wok|nouilles|riz cantonais|nems?|pad thai|curry|tikka|masala|dal|biryani|pho|bo bun|banh|laksa|rendang|japon|chinois|coree|thai|vietnam|inde|soja)\b/ },
  { cat: "italie", macro: "europe_sud", re: /\b(pasta|spaghetti|carbonara|lasagnes?|risotto|gnocchi|pesto|parmigiana|polpette|tiramisu|italie|bolognaise|orecchiette|focaccia)\b/ },
  { cat: "ameriques", macro: "amerique_latine", re: /\b(tacos|guacamole|chili|burrito|empanadas?|antillais|colombo|accras|creole|jerk|bresil|mexique|peru|cajun|jambalaya)\b/ },
  { cat: "france", macro: "france", re: /\b(bourguignon|blanquette|quiche|gratin|ratatouille|pot au feu|cassoulet|tartiflette|croque|boeuf mode|hachis|veloute|terrine)\b/ },
];

/** Signaux porc / alcool : jamais de faux « sans » ; en cas de doute → « doute » (Tome 7 §7.2). */
const PORK = /\b(porc|cochon|lardons?|bacon|jambon|chorizo|saucisson|pancetta|guanciale|lard|saindoux|rillettes|andouill|boudin|mortadelle|salami|pepperoni|knacki?|chipolata|travers de porc|ribs de porc|pork|ham|prosciutto|speck)\b/;
const PORK_DOUBT = /\b(saucisses?|gelatine|marshmallow|bouillon cube|cube|merguez|sanglier|charcuterie)\b/;
const PORK_SAFE = /\b(jambon de (dinde|poulet|volaille)|lardons de (dinde|volaille)|bacon de (dinde|boeuf)|chorizo de (boeuf|volaille)|halal)\b/;
const ALC = /\b(vin|biere|rhum|cognac|whisky|vodka|calvados|cidre|champagne|porto|marsala|amaretto|liqueur|mirin|sake|kirsch|grand marnier|cointreau|flamb|beer|wine)\b/;
const ALC_DOUBT = /\b(extrait de vanille|vinaigre de vin|sauce soja|0 0|sans alcool)\b/;

export interface Classified {
  cat: string;
  macro: string | null;
  pork: "oui" | "non" | "doute";
  alcohol: "oui" | "non" | "doute";
  ingredients: { text: string; ref: string | null }[];
  steps: string[];
  title: string;
  warnings: string[];
}

/** Pluriels simples : « oignons » → « oignon », « citrons verts » → « citron vert ». */
const sing = (s: string) => s.split(" ").map((w) => (w.length > 3 ? w.replace(/(s|x)$/, "") : w)).join(" ");
// Clés de rapprochement : le nom complet (« citron vert ») puis le mot principal (« oignon » → Oignon jaune,
// premier de sa famille dans le Tome 3). Les clés longues passent en premier.
const KEYS = new Map<string, string>();
for (const n of INGREDIENT_NAMES) {
  const full = sing(norm(n.split(" (")[0].split(" / ")[0]));
  if (full.length >= 3 && !KEYS.has(full)) KEYS.set(full, n);
}
for (const n of INGREDIENT_NAMES) {
  const head = sing(norm(n.split(" (")[0].split(" / ")[0])).split(" ")[0];
  if (head.length >= 3 && !KEYS.has(head)) KEYS.set(head, n);
}
const REF_INDEX = [...KEYS.entries()].map(([k, n]) => ({ k, n })).sort((a, b) => b.k.length - a.k.length);
const NEUTRAL = /\b(eau|glacons?)\b/;

/** Rapproche une ligne d'ingrédient d'une entrée du référentiel (Tome 3). */
// Mots courants des légendes que le premier mot rapprocherait mal (« viande de bœuf » → viande des Grisons,
// « huile d'olive » → olives) : vérifiés avant le référentiel. Relus à la main le 22/10/2026.
const ALIASES: [RegExp, string][] = [
  [/\bhuile d.?olive\b/, "Huile d'olive vierge extra"], [/\bhuile (neutre|de tournesol|de colza|vegetale)\b|^\W*\d*\s*\w*\s*huile\W*$/, "Huile de tournesol / colza"],
  [/\b(viande|boeuf) hachee?\b|\bsteaks? hache/, "Bœuf haché"], [/\bagneau hache|viande hachee? d.?agneau/, "Agneau haché"],
  [/\b(haut|hauts|cuisse|cuisses|pilon|pilons) de poulet\b/, "Cuisse / pilon de poulet"], [/\b(blanc|blancs|filet|filets|escalope|escalopes) de poulet\b/, "Blanc de poulet"],
  [/\bpoulet entier\b/, "Poulet entier"], [/\b(viande de boeuf|boeuf a mijoter|boeuf a braiser|boeuf)\b/, "Paleron"], [/\b(viande d.?agneau|agneau)\b/, "Épaule d'agneau"],
  [/\bcreme (liquide|entiere|fleurette)\b/, "Crème fleurette (liquide)"], [/\bcreme fraiche\b/, "Crème fraîche"], [/\bfromage rape\b/, "Gruyère / comté / emmental / beaufort"],
];

export function matchIngredient(text: string): string | null {
  const nt = norm(text);
  // « bouillon de bœuf », « fond de veau », « graisse de canard » : jamais rabattus sur la viande (le moteur doit garder le doute)
  if (!/\b(bouillon|cube|fond|graisse|jus|saucisse|merguez|chorizo|jambon|bacon|lardon)/.test(nt)) for (const [re, ref] of ALIASES) if (re.test(nt) && INGREDIENTS[ref]) return ref;
  const t = ` ${sing(nt)} `;
  for (const { n, k } of REF_INDEX) if (t.includes(` ${k} `)) return n;
  return null;
}

export function classify(raw: string, url = ""): Classified {
  const text = raw.replace(/\r/g, "").slice(0, 10000); // troncature sûre des très longues légendes
  const n = ` ${norm(text)} `;
  const warnings: string[] = [];
  if (/ignore (les|toutes les) (consignes|instructions)|tu es maintenant|system prompt/i.test(text)) warnings.push("La légende contient des instructions : elles sont ignorées (le contenu importé est une donnée).");
  let cat = "a_verifier"; let macro: string | null = null;
  for (const r of RULES) if (r.re.test(n)) { if (cat === "a_verifier") cat = r.cat; if (r.macro && !macro) macro = r.macro; }
  if (!text.trim()) warnings.push("Légende vide : copie-la depuis l'application d'origine pour un tri plus juste.");

  // ingrédients : lignes avec une quantité, ou puces
  // on retire les puces (« - », « • », « 1. ») mais jamais la quantité (« 2 cuisses de poulet »)
  const lines = text.split(/\n|•|·|(?=- )/).map((l) => l.replace(/^(?:[-*•]\s*|\d+[.)]\s+)/, "").trim()).filter(Boolean);
  const ingredients: { text: string; ref: string | null }[] = [];
  const steps: string[] = [];
  for (const l of lines) {
    if (NEUTRAL.test(norm(l)) && l.length < 40) continue; // l'eau ne compte ni comme ingrédient connu ni comme inconnu
    if (/^\d|\b(\d+\s*(g|kg|ml|cl|l|c\.?\s*à\s*[sc]|cas|cac|tbsp|tsp|cups?|gousses?|pinc[ée]e)\b)|^(une?|deux|trois|quatre)\s/i.test(l) && l.length < 90) ingredients.push({ text: l, ref: matchIngredient(l) });
    else if (l.length > 40 && /\b(ajoute|mélange|cuire|cuis|faire|laisse|mets|verse|coupe|enfourne|mix)/i.test(l)) steps.push(l);
  }
  // Légendes TikTok écrites d'un seul bloc : « Ingrédients : 600 g de paleron, 1 oignon, persil, cumin… » (retour d'usage
  // du 22/10/2026) : la liste qui suit le mot « ingrédients » est découpée aux virgules.
  if (ingredients.length < 2) {
    const block = text.match(/ingr[ée]dients?\s*(?:pour[^:\n]*)?:?\s*([^\n]*(?:\n(?!\s*(?:pr[ée]paration|[ée]tapes?|instructions?|recette)\b)[^\n]*)*)/i)?.[1] ?? "";
    const items = block.split(/\n|,|;|•|·|\s[-–]\s/).map((x) => x.replace(/^(?:[-*•]\s*|\d+[.)]\s+)/, "").replace(/\.$/, "").trim())
      .filter((x) => x.length > 1 && x.length < 70 && !/^(pr[ée]paration|[ée]tapes?|instructions?)/i.test(x));
    if (items.length >= 2) {
      const seen = new Set(ingredients.map((i) => i.text));
      for (const x of items) if (!seen.has(x) && !(NEUTRAL.test(norm(x)) && x.length < 40)) { ingredients.push({ text: x, ref: matchIngredient(x) }); seen.add(x); }
    }
  }
  const unknown = ingredients.filter((i) => !i.ref).length;
  if (unknown) warnings.push(`${unknown} ingrédient(s) non reconnu(s) : statut « à vérifier », jamais « sans porc » garanti.`);

  const refPork = ingredients.some((i) => i.ref && INGREDIENTS[i.ref].derivs.pork === "certain");
  const refPorkDoubt = ingredients.some((i) => i.ref && INGREDIENTS[i.ref].derivs.pork === "possible");
  const refAlc = ingredients.some((i) => i.ref && INGREDIENTS[i.ref].derivs.alcohol === "certain");
  const refAlcDoubt = ingredients.some((i) => i.ref && INGREDIENTS[i.ref].derivs.alcohol);
  const nn = n.replace(PORK_SAFE, " ");
  const pork = refPork || PORK.test(nn) ? "oui" : refPorkDoubt || PORK_DOUBT.test(nn) || unknown || !ingredients.length ? "doute" : "non";
  const alcohol = refAlc || ALC.test(n) ? "oui" : refAlcDoubt || ALC_DOUBT.test(n) || unknown || !ingredients.length ? "doute" : "non";

  const firstLine = text.split("\n").find((l) => l.trim()) ?? "";
  // le titre s'arrête avant la liste d'ingrédients et la première quantité
  const cut = firstLine.replace(/#\S+/g, "").replace(/https?:\S+/g, "").split(/\bingr[ée]dients?\b|🛒|📝|\s\d+(?:[.,]\d+)?\s?(?:g|kg|ml|cl|l)\b/i)[0];
  const title = cut.replace(/[\s:.,;–-]+$/, "").trim().slice(0, 90) || titleFromUrl(url);
  return { cat, macro, pork, alcohol, ingredients, steps, title, warnings };
}

export function titleFromUrl(url: string): string {
  try {
    const u = new URL(url);
    const m = u.pathname.match(/@([^/]+)/);
    return m ? `Vidéo de @${m[1]}` : u.hostname.replace(/^www\./, "");
  } catch { return "Recette importée"; }
}

export function sourceOf(url: string): string {
  const h = (() => { try { return new URL(url).hostname; } catch { return ""; } })();
  if (/tiktok/.test(h)) return "TikTok";
  if (/instagram/.test(h)) return "Instagram";
  if (/youtu/.test(h)) return "YouTube";
  if (/pinterest|pin\.it/.test(h)) return "Pinterest";
  if (/facebook|fb\./.test(h)) return "Facebook";
  return h.replace(/^www\./, "") || "Texte";
}

/** Extrait les liens d'un export de données TikTok (« Télécharger tes données », format JSON ou TXT) ou d'une liste collée. */
export function linksFromExport(content: string): string[] {
  const urls = content.match(/https?:\/\/(?:www\.|vm\.|vt\.|m\.)?(?:tiktok\.com|instagram\.com|youtube\.com|youtu\.be|pinterest\.[a-z.]+|pin\.it)[^\s"'<>,]*/gi) ?? [];
  return [...new Set(urls.map((u) => u.replace(/[).\]]+$/, "")))];
}
