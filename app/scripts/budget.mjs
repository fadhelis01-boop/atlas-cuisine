// Budget de poids (audit dév/UX 2026-10-21 §2.1) : le JavaScript chargé au démarrage ne doit pas dépasser BUDGET Ko
// compressés. Chaque recette ajoutée alourdit l'index : si le build échoue ici, alléger l'index (export_app_data.py, DETAIL)
// plutôt que relever le plafond.
import { readFileSync, readdirSync } from "node:fs";
import { gzipSync } from "node:zlib";

const BUDGET = 400;
const html = readFileSync("dist/index.html", "utf8");
const start = [...html.matchAll(/(?:src|href)="\.\/(assets\/[^"]+\.(?:js|css))"/g)].map((m) => m[1]);
const kb = (f) => gzipSync(readFileSync(`dist/${f}`)).length / 1024;
const total = start.reduce((s, f) => s + kb(f), 0);
const lazy = readdirSync("dist/assets").filter((f) => !start.includes(`assets/${f}`)).reduce((s, f) => s + kb(`assets/${f}`), 0);
console.log(`budget : démarrage ${total.toFixed(0)} Ko compressés (plafond ${BUDGET}) · à la demande ${lazy.toFixed(0)} Ko`);
if (total > BUDGET) { console.error(`Démarrage trop lourd : ${total.toFixed(0)} Ko > ${BUDGET} Ko`); process.exit(1); }
