import { createRoot } from "react-dom/client";
import App from "./App";
import "./styles/app.css";
import "./styles/skin.css";
import { registerServiceWorker } from "./lib/pwa";
import { installErrorLog } from "./lib/errlog";
import { askPersistence } from "./lib/store";

installErrorLog();

createRoot(document.getElementById("root")!).render(<App />);
registerServiceWorker();
// Stockage persistant : le navigateur n'efface plus les données d'ATLAS quand l'appareil manque de place (audit famille).
void askPersistence();
// Les voix de synthèse se chargent de façon asynchrone sur certains navigateurs.
if ("speechSynthesis" in window) speechSynthesis.getVoices();
