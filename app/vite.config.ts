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

// Politique de sécurité du contenu (audit dév/UX 2026-10-21 §1.3) : GitHub Pages ne permet pas d'en-têtes HTTP, on la pose
// en <meta> à la compilation seulement (le serveur de développement injecte un script en ligne). Seules origines externes :
// les fiches oEmbed (titre d'un lien importé) et les lecteurs vidéo YouTube (sans cookies) et TikTok.
export const CSP = [
  "default-src 'self'", "script-src 'self'", "style-src 'self' 'unsafe-inline'", "img-src 'self' data: blob:", "media-src 'self'", "font-src 'self'",
  "connect-src 'self' https://www.tiktok.com https://www.youtube.com https://vimeo.com",
  "frame-src https://www.youtube-nocookie.com https://www.tiktok.com", "worker-src 'self'", "manifest-src 'self'",
  "object-src 'none'", "base-uri 'self'", "form-action 'self'",
].join("; ");
function contentSecurityPolicy(): Plugin {
  return { name: "csp", apply: "build", transformIndexHtml: (html) => html.replace('<meta charset="UTF-8" />', `<meta charset="UTF-8" />\n    <meta http-equiv="Content-Security-Policy" content="${CSP}" />`) };
}

// base "./" : fonctionne à la racine d'un domaine comme dans un sous-dossier (GitHub Pages, NAS…).
export default defineConfig({
  base: "./",
  plugins: [react(), stampServiceWorker(), contentSecurityPolicy()],
  build: { target: "es2020", chunkSizeWarningLimit: 1200 },
  server: { port: 5196 },
  preview: { port: 5197 },
});
