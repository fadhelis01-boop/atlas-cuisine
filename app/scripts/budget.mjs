// Budget de poids (audit dév/UX 2026-10-21 §2.1) : le JavaScript chargé au démarrage ne doit pas dépasser BUDGET Ko
// compressés. Chaque recette ajoutée alourdit l'index : si le build échoue ici, alléger l'index (export_app_data.py, DETAIL)
// plutôt que relever le plafond.
// Plafond par chunk à la demande (audit dév senior 21/11/2026 §3) : avant le découpage en lots, rien ne bornait un
// fichier chargé à la demande pris isolément — recipes_detail.json a pu grossir jusqu'à 559 Ko compressés (2,1 Mo
// bruts) sans jamais faire échouer la moindre vérification. Seuil choisi au-dessus du plus gros chunk légitime
// actuel (le moteur partagé, ~209 Ko) : si un chunk dépasse CHUNK_BUDGET, le découper (comme recipes_detail) plutôt
// que relever ce plafond.
import { readFileSync, readdirSync } from "node:fs";
import { gzipSync } from "node:zlib";

const BUDGET = 400;
const CHUNK_BUDGET = 220;
const html = readFileSync("dist/index.html", "utf8");
const start = [...html.matchAll(/(?:src|href)="\.\/(assets\/[^"]+\.(?:js|css))"/g)].map((m) => m[1]);
const kb = (f) => gzipSync(readFileSync(`dist/${f}`)).length / 1024;
const total = start.reduce((s, f) => s + kb(f), 0);
const lazyFiles = readdirSync("dist/assets").filter((f) => !start.includes(`assets/${f}`));
const lazy = lazyFiles.reduce((s, f) => s + kb(`assets/${f}`), 0);
console.log(`budget : démarrage ${total.toFixed(0)} Ko compressés (plafond ${BUDGET}) · à la demande ${lazy.toFixed(0)} Ko`);
if (total > BUDGET) { console.error(`Démarrage trop lourd : ${total.toFixed(0)} Ko > ${BUDGET} Ko`); process.exit(1); }
for (const f of lazyFiles) {
  const w = kb(`assets/${f}`);
  if (w > CHUNK_BUDGET) { console.error(`Chunk à la demande trop lourd : ${f} = ${w.toFixed(0)} Ko > ${CHUNK_BUDGET} Ko`); process.exit(1); }
}
