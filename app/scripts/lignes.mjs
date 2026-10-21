// Lisibilité du code (audit dév/UX 2026-10-21 §4) : reformater 7 500 lignes d'un coup rendrait l'historique illisible.
// Cliquet : le nombre de lignes de plus de 200 caractères dans src/ ne peut que baisser. Après un nettoyage, abaisser PLAFOND.
import { readFileSync, readdirSync, statSync } from "node:fs";
import { join } from "node:path";

const PLAFOND = Number(process.argv[2] ?? NaN) || 619;
const files = [];
const walk = (d) => { for (const n of readdirSync(d)) { const p = join(d, n); if (statSync(p).isDirectory()) { if (n !== "data") walk(p); } else if (/\.(ts|tsx)$/.test(n)) files.push(p); } };
walk("src");
let long = 0, total = 0;
const worst = [];
for (const f of files) {
  const ls = readFileSync(f, "utf8").split("\n");
  total += ls.length;
  const n = ls.filter((l) => l.length > 200).length;
  long += n;
  if (n) worst.push([n, f]);
}
worst.sort((a, b) => b[0] - a[0]);
console.log(`lignes de plus de 200 caractères : ${long} sur ${total} (plafond ${PLAFOND}) · à reprendre d'abord : ${worst.slice(0, 3).map(([n, f]) => `${f} (${n})`).join(", ")}`);
if (long > PLAFOND) { console.error(`Trop de lignes très longues : ${long} > ${PLAFOND}. Découpe les nouvelles lignes avant de publier.`); process.exit(1); }
