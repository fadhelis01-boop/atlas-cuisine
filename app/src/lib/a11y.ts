// Changement d'écran annoncé (audit dév/UX 2026-10-21 §1.4) : le routeur par ancre ne recharge pas la page, donc
// un lecteur d'écran ne sait pas que l'écran a changé. À chaque écran : titre de l'onglet = titre de la page,
// focus sur le contenu (sauf retour arrière, où l'on garde sa place), annonce dans une région « polite ».
import { useEffect } from "react";
import { wasBackNav } from "./router";

const SITE = "ATLAS";
let announcer: HTMLElement | null = null;
function announce(text: string) {
  if (!announcer) {
    announcer = document.createElement("div");
    announcer.className = "sr"; announcer.setAttribute("role", "status"); announcer.setAttribute("aria-live", "polite");
    document.body.appendChild(announcer);
  }
  announcer.textContent = ""; // vider puis écrire : certains lecteurs n'annoncent pas un texte identique
  setTimeout(() => { if (announcer) announcer.textContent = text; }, 60);
}

/** Titre lisible d'un écran : son h1, sans les mentions secondaires (« · pour 4 personnes »). */
export function screenTitle(root: ParentNode = document): string | null {
  const h = root.querySelector("main h1");
  if (!h) return null;
  const c = h.cloneNode(true) as HTMLElement;
  c.querySelectorAll(".meta, .sr").forEach((x) => x.remove());
  const t = c.textContent?.replace(/\s+/g, " ").trim();
  return t || null;
}

let firstScreen = true;
export function useScreenChange(key: string) {
  useEffect(() => {
    let tries = 0, done = false;
    const apply = () => {
      if (done) return;
      const t = screenTitle();
      const busy = document.querySelector("main[aria-busy='true']");
      if ((!t || busy) && tries++ < 40) { setTimeout(apply, 50); return; } // page chargée à la demande : on attend son titre
      done = true;
      document.title = t ? `${t} · ${SITE}` : SITE;
      if (firstScreen) { firstScreen = false; return; } // premier affichage : le navigateur annonce déjà la page
      announce(t ?? SITE);
      if (!wasBackNav()) (document.getElementById("contenu") as HTMLElement | null)?.focus({ preventScroll: true });
    };
    requestAnimationFrame(apply);
    return () => { done = true; };
  }, [key]);
}
