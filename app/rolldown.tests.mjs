// Construction des tests (moteur et rendu) : rolldown seul, sans Vite. Ce petit greffon reproduit l'import « ?raw » de Vite
// (fichier lu comme une chaîne), utilisé pour les recettes, lues en JSON.parse au démarrage (audit dév/UX 2026-10-21).
import { readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";

const raw = {
  name: "raw",
  resolveId(id, importer) {
    if (!id.endsWith("?raw") || !importer) return null;
    return resolve(dirname(importer), id.slice(0, -4)) + "?raw";
  },
  load(id) {
    return id.endsWith("?raw") ? `export default ${JSON.stringify(readFileSync(id.slice(0, -4), "utf8"))};` : null;
  },
};

/** Configuration d'une suite : dossier de sortie et fichier d'entrée. */
export const suite = (name, input) => ({
  input,
  platform: "node",
  external: ["jsdom"],
  logLevel: "warn",
  plugins: [raw],
  output: { format: "esm", dir: `.tmp/${name}`, entryFileNames: "[name].mjs" },
});

export default suite("test", "tests/engine.test.ts");
