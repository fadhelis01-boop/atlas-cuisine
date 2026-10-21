import type { State } from "./store";

/** Faut-il inviter à installer ATLAS ? Sur iPhone, dans Safari, dès qu'il y a quelque chose à perdre (Safari efface le stockage
 *  d'un site non installé et non ouvert depuis 7 jours) ; une fois par mois au plus après « Plus tard » (audit dév/UX 2026-10-21 §2.5). */
export function installDue(s: State, ios: boolean, standalone: boolean, now = Date.now()): boolean {
  if (!ios || standalone) return false;
  const personal = s.favorites.length + Object.keys(s.journal ?? {}).length + s.imports.length + Object.keys(s.week ?? {}).length + s.menus.length;
  if (personal < 3) return false;
  return !s.installNudge || now - Date.parse(s.installNudge) > 30 * 86400000;
}
