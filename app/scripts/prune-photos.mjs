// Photos publiées (audit dév/UX 2026-10-21 §2.6) : tous les navigateurs ciblés lisent l'AVIF. On ne met en ligne que l'AVIF
// en 400 et 800 px et le WebP 400 en secours ; le 1200 px et les WebP 800/1200 restent dans le dépôt (retraitement possible).
// Le site publié passe ainsi d'environ 470 Mo à moins de 150 Mo (limite GitHub Pages : 1 Go).
import { readdirSync, rmSync, statSync } from "node:fs";
import { join } from "node:path";

let removed = 0, kept = 0, bytes = 0;
const walk = (d) => {
  for (const n of readdirSync(d)) {
    const p = join(d, n);
    if (statSync(p).isDirectory()) { walk(p); continue; }
    if (/-1200\.(webp|avif)$|-800\.webp$/.test(n)) { bytes += statSync(p).size; rmSync(p); removed++; } else kept++;
  }
};
walk("dist/img");
console.log(`photos publiées : ${kept} fichiers gardés, ${removed} retirés (${(bytes / 1e6).toFixed(0)} Mo de moins en ligne)`);
