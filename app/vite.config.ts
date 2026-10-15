import { defineConfig, type Plugin } from "vite";
import react from "@vitejs/plugin-react";
import { readFileSync, writeFileSync, existsSync, readdirSync } from "node:fs";

// Estampille le service worker à chaque compilation : les appareils
// détectent ainsi la nouvelle version et proposent la mise à jour.
function stampServiceWorker(): Plugin {
  return {
    name: "stamp-sw",
    apply: "build",
    closeBundle() {
      const f = "dist/sw.js";
      // tous les fichiers compilés (y compris les morceaux chargés à la demande, comme le dictionnaire) sont mis en cache à l'installation
      const assets = existsSync("dist/assets") ? readdirSync("dist/assets").map((n) => `./assets/${n}`) : [];
      if (existsSync(f)) writeFileSync(f, readFileSync(f, "utf8").replaceAll("__BUILD__", new Date().toISOString()).replace('"__ASSETS__"', JSON.stringify(assets).slice(1, -1) || '""'));
    },
  };
}

// base "./" : fonctionne à la racine d'un domaine comme dans un sous-dossier (GitHub Pages, NAS…).
export default defineConfig({
  base: "./",
  plugins: [react(), stampServiceWorker()],
  build: { target: "es2020", chunkSizeWarningLimit: 1200 },
  server: { port: 5196 },
  preview: { port: 5197 },
});
