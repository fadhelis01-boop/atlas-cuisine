import { createRoot } from "react-dom/client";
import App from "./App";
import "./styles/app.css";
import "./styles/skin.css";
import { registerServiceWorker } from "./lib/pwa";
import { installErrorLog } from "./lib/errlog";
import { askPersistence } from "./lib/store";
import { loadDetails } from "./lib/data";
import { cleanOrphans } from "./lib/orphans";

installErrorLog();

createRoot(document.getElementById("root")!).render(<App />);
// le détail des fiches (étapes, conseils…) se lit juste après le premier affichage, sans le retarder (audit dév/UX 2026-10-21)
setTimeout(() => { void loadDetails(); cleanOrphans(); }, 0);
registerServiceWorker();
// Stockage persistant : le navigateur n'efface plus les données d'ATLAS quand l'appareil manque de place (audit famille).
void askPersistence();
// Les voix de synthèse se chargent de façon asynchrone sur certains navigateurs.
if ("speechSynthesis" in window) speechSynthesis.getVoices();
