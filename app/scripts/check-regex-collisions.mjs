// Collisions de sous-chaîne dans les regex de classification (audit dév senior 21/11/2026 §4) : trois bugs trouvés
// le 21/11/2026 venaient tous d'une regex à alternatives (/mot1|mot2|.../) sans limite de mot (\b), qui matche par
// accident à l'intérieur d'un autre mot (« classique » contient « lassi », « chiche » contient « chich », « menthe »
// contient « the »). Ce script simule chaque regex trouvée dans les fichiers listés contre un corpus de vrais textes
// (titres, étapes, conseils, lexique) et signale toute correspondance qui tombe au milieu d'un mot plutôt qu'à sa
// frontière. Il ne remplace pas la relecture humaine (toute alerte doit être vérifiée : certaines regex normalisent
// le texte avant de le tester, ce que ce script ne reproduit pas toujours), mais attrape la même classe d'erreur
// que celle trouvée à la main cette journée-là, sur n'importe quel fichier, pas seulement ceux déjà corrigés.
import { readFileSync, readdirSync } from "node:fs";

const FILES = [
  "src/lib/planner.ts",
  "src/lib/intents.ts",
  "src/lib/famille.ts",
  "src/lib/text.ts",
  "src/lib/speech.ts",
  "src/lib/season.ts",
  "src/lib/dressage.ts",
  "src/components/art.tsx",
];

function norm(s) {
  return s
    .toLowerCase()
    .replace(/œ/g, "oe")
    .replace(/æ/g, "ae")
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "");
}

// Corpus : titres de fiches et noms d'ingrédients du référentiel — exactement ce que « simuler chaque classification
// sur tous les titres » (constat n°4 de l'audit) veut dire, PAS le texte libre des étapes. Les classifications
// visées (dishEmoji, dressage, famille d'accompagnement, protéine dominante…) reçoivent un titre ou une référence
// d'ingrédient, jamais une phrase d'étape entière ; tester contre les étapes produirait des centaines de « collisions »
// sur des verbes de cuisine (rissoler, démouler, écailler…) qui ne sont jamais l'entrée réelle de ces fonctions.
function buildCorpus() {
  const words = new Set();
  const add = (s) => {
    if (typeof s !== "string") return;
    // mots alphabétiques réels uniquement (longueur ≥ 3) : les identifiants (ids TikTok, hash) et les nombres n'ont
    // jamais été la source d'une collision observée, et noient le signal utile sous des centaines de faux positifs.
    for (const w of norm(s).replace(/[^a-z]+/g, " ").split(" ")) if (w.length > 2) words.add(w);
  };
  const recipes = JSON.parse(readFileSync("src/data/recipes.json", "utf8"));
  for (const r of recipes) add(r.title);
  const ingredients = JSON.parse(readFileSync("src/data/ingredients.json", "utf8"));
  for (const key of Object.keys(ingredients)) add(key);
  try {
    const catalogue = JSON.parse(readFileSync("src/data/catalogue.json", "utf8"));
    for (const c of catalogue) add(c.title ?? c.label ?? c.name);
  } catch {
    /* champ absent : ignoré */
  }
  return [...words];
}

// Extrait les littéraux /…/flags qui contiennent une alternative (|), ligne par ligne (évite les commentaires
// purs et les lignes sans risque). Heuristique volontairement simple : faux négatifs possibles (regex étalées sur
// plusieurs lignes), pas de faux positifs côté compilation (un littéral qui ne compile pas est juste ignoré).
function extractRegexes(src) {
  const out = [];
  const lines = src.split("\n");
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (/^\s*\/\//.test(line)) continue;
    const re = /\/((?:\\.|[^\\/\n])+)\/([a-z]*)/g;
    let m;
    while ((m = re.exec(line))) {
      const [full, body, flags] = m;
      // regex sans alternative, ou qui classe des nombres/durées (\d) plutôt que du vocabulaire : hors du périmètre
      // du bug recherché (un mot-clé contenu dans un autre mot), et source de faux positifs massifs sur un corpus
      // qui contient aussi des identifiants (vidéos, hash) sans rapport avec du texte culinaire.
      if (!body.includes("|") || body.includes("\\d")) continue;
      try {
        out.push({ regex: new RegExp(body, flags || undefined), source: full, line: i + 1 });
      } catch {
        /* pas une regex valide (ex. division, chemin) : ignoré */
      }
    }
  }
  return out;
}

function isWordChar(c) {
  return c !== undefined && /[a-z0-9]/i.test(c);
}

// Un mot du corpus matche "au milieu" quand la correspondance est précédée d'une lettre : le mot-clé n'est pas au
// début du mot testé, donc pas un simple pluriel/suffixe (ex. « poisson » dans « poissons », sans risque), mais
// contenu dans un mot sans rapport (ex. « lassi » dans « classique », « the » dans « menthe ») — exactement la
// classe de bug trouvée le 21/11/2026. Une correspondance qui ne fait que s'étendre après le mot-clé (pluriel,
// terminaison) n'est volontairement pas signalée : elle n'a jamais été la source d'un faux positif observé.
function midWordHit(regex, word) {
  const g = new RegExp(regex.source, regex.flags.includes("g") ? regex.flags : regex.flags + "g");
  let m;
  while ((m = g.exec(word))) {
    if (m[0].length === 0) {
      g.lastIndex++;
      continue;
    }
    if (isWordChar(word[m.index - 1])) return { match: m[0], index: m.index };
  }
  return null;
}

// Collisions passées en revue et gardées volontairement (21/11/2026) : le mot-clé fait vraiment partie du mot
// trouvé (pancake contient cake, cheeseburger contient burger…), ou le même radical désigne la même préparation
// dans deux langues (bao/xiaolongbao, spatzle/kasespatzle, steak/cheesesteak, strudel/apfelstrudel, frit/refrit).
// Toute collision hors de cette liste fait échouer le script : avant d'y ajouter une entrée, vérifier qu'il s'agit
// bien du même plat, pas d'un mot sans rapport.
const ALLOWED = new Set([
  "cake|cheesecake", "cake|cheesecakes", "cake|pancake", "cake|pancakes",
  "burger|cheeseburger", "burger|hamburger",
  "steak|cheesesteak",
  "bao|xiaolongbao",
  "spatzle|kasespatzle",
  "strudel|apfelstrudel",
  "frit|refrit",
]);

const corpus = buildCorpus();
let hits = 0;
for (const file of FILES) {
  let src;
  try {
    src = readFileSync(file, "utf8");
  } catch {
    continue;
  }
  for (const { regex, source, line } of extractRegexes(src)) {
    for (const word of corpus) {
      const hit = midWordHit(regex, word);
      if (hit && !ALLOWED.has(`${hit.match}|${word}`)) {
        console.error(`${file}:${line}  ${source}  →  « ${hit.match} » au milieu de « ${word} »`);
        hits++;
      }
    }
  }
}
if (hits === 0) console.log(`check-regex-collisions : aucune collision au milieu d'un mot (${FILES.length} fichiers, ${corpus.length} mots du corpus)`);
else {
  console.error(`check-regex-collisions : ${hits} collision(s) à vérifier (chaque alerte n'est pas forcément un bug : regex déjà bornée par \\b ailleurs dans la ligne, texte normalisé différemment…)`);
  process.exit(1);
}
