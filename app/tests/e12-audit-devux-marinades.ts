// Audit dév/UX senior du 23/11/2026 (bible/AUDIT_DEV_UX_MARINADES_2026-11-23.md §3) : les listes curatoires des
// coins Marinades/Sauces/Pains filtrent silencieusement toute entrée dont l'id ne résout plus dans RECIPE_BY_ID —
// sur le modèle du test 25 pour les références d'ingrédients, mais rien d'équivalent n'existait pour ces 3 listes.
import { MARINADES } from "../src/lib/marinades";
import { SAUCES } from "../src/lib/sauces";
import { PAINS } from "../src/lib/pains";
import { RECIPE_BY_ID } from "../src/lib/data";
import { check } from "./helpers";

check(
  "132 listes curatoires : chaque id de MARINADES, SAUCES et PAINS résout vers une fiche existante",
  MARINADES.every((m) => !!RECIPE_BY_ID[m.id]) && SAUCES.every((s) => !!RECIPE_BY_ID[s.id]) && PAINS.every((p) => !!RECIPE_BY_ID[p.id]),
);
