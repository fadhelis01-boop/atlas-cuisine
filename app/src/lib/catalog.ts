// Aide partagée pour les coins à liste curatoire (audit dév/UX senior 23/11/2026 §2) : `marinadeRecipes`
// (marinades.ts), `sauceRecipes` (sauces.ts) et `painRecipes` (pains.ts) avaient exactement le même corps, écrit
// trois fois à deux jours d'intervalle plutôt que partagé — exactement le rythme qui installe une dette au lieu de
// la prévenir.
import { RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

/** Associe une liste curatoire d'entrées (chacune avec un `id`) à ses fiches, en retirant silencieusement toute
 *  entrée dont l'id ne résout plus dans `RECIPE_BY_ID` (fiche renommée ou supprimée) ; `matches` filtre la liste
 *  avant association (ex. par famille, ou par appartenance à une protéine). */
export function curatedRecipes<E extends { id: string }>(list: readonly E[], matches: (entry: E) => boolean): (Recipe & { entry: E })[] {
  return list
    .filter(matches)
    .map((entry) => (RECIPE_BY_ID[entry.id] ? { ...RECIPE_BY_ID[entry.id], entry } : null))
    .filter((r): r is Recipe & { entry: E } => !!r);
}
