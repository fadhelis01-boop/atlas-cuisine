import { createRoot } from "react-dom/client";
import App from "./App";
import "./styles/app.css";
import "./styles/skin.css";
import { registerServiceWorker } from "./lib/pwa";

createRoot(document.getElementById("root")!).render(<App />);
registerServiceWorker();
// Les voix de synthèse se chargent de façon asynchrone sur certains navigateurs.
if ("speechSynthesis" in window) speechSynthesis.getVoices();
