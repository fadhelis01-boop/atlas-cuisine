import { createRoot } from "react-dom/client";
import App from "./App";
import "./styles/app.css";
import "./styles/skin.css";
import { registerServiceWorker } from "./lib/pwa";
import { installErrorLog } from "./lib/errlog";
import { askPersistence } from "./lib/store";
import { cleanOrphans } from "./lib/orphans";

installErrorLog();

createRoot(document.getElementById("root")!).render(<App />);
// Depuis le découpage en lots du 21/11/2026 (audit dév senior §1), le détail ne se précharge plus en bloc ici :
// chaque écran demande lui-même son lot (une fiche via useRecipeDetail, un écran qui balaie tout via useDetails),
// pour qu'ouvrir une seule fiche ne télécharge plus les étapes des 1600 autres.
setTimeout(cleanOrphans, 0);
registerServiceWorker();
// Stockage persistant : le navigateur n'efface plus les données d'ATLAS quand l'appareil manque de place (audit famille).
void askPersistence();
// Les voix de synthèse se chargent de façon asynchrone sur certains navigateurs.
if ("speechSynthesis" in window) speechSynthesis.getVoices();
