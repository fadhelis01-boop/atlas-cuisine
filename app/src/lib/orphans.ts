// Recettes disparues (audit dév/UX 2026-10-21 §3.7) : après les renommages (renames.json, appliqués par le store), un favori
// ou un repas planifié qui ne correspond plus à aucune fiche est retiré AVEC un message, au lieu de disparaître en silence.
// Les notes du carnet sont gardées : elles peuvent servir à corriger la bible.
import { RECIPE_BY_ID } from "./data";
import { type State, getState, setState } from "./store";
import { toast } from "./toast";

export function findOrphans(s: State, exists: (id: string) => boolean = (id) => !!RECIPE_BY_ID[id]): string[] {
  const ids = new Set<string>(s.favorites);
  for (const d of Object.values(s.week ?? {})) for (const id of Object.values(d)) if (id) ids.add(id);
  return [...ids].filter((id) => !exists(id));
}

export function cleanOrphans() {
  const gone = findOrphans(getState());
  if (!gone.length) return;
  const g = new Set(gone);
  setState((s) => {
    s.favorites = s.favorites.filter((id) => !g.has(id));
    for (const d of Object.values(s.week ?? {})) for (const f of ["midi", "soir", "entree", "dessert"] as const) if (d[f] && g.has(d[f]!)) delete d[f];
  });
  const n = gone.length;
  toast(`${n} recette${n > 1 ? "s" : ""} n'exist${n > 1 ? "ent" : "e"} plus dans ATLAS : retirée${n > 1 ? "s" : ""} de tes favoris et de ta semaine. Tes notes du carnet sont gardées.`, { ms: 9000 });
}
