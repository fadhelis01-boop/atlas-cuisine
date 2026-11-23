// Coin pains, audit « amateur de pains, brioches et pâtisserie maison » (22/11/2026) : 45 fiches `cats: ["pains"]`
// affichées en une seule grille, sans filtre, mélangeant des familles très différentes (galette minute à la poêle
// et tourage de croissants) — exactement ce que `bible/CONVENTIONS_LISTES_RUBRIQUE.md` range dans « puces de
// filtre » dès que les catégories sont peu nombreuses et se cherchent d'avance.
import { curatedRecipes } from "./catalog";
import type { Recipe } from "./types";

export type PainFamily = "plat" | "leve" | "feuillete" | "brioche" | "crepe" | "base";

export const PAIN_FAMILY_LABEL: Record<PainFamily, string> = {
  plat: "Pains plats & sans levain",
  leve: "Pains levés classiques",
  feuillete: "Viennoiserie feuilletée",
  brioche: "Brioche & pâte enrichie",
  crepe: "Crêpes, gaufres & pâtes à frire",
  base: "Bases, pizza & pâte salée",
};

export interface PainEntry {
  id: string;
  family: PainFamily;
}

export const PAINS: PainEntry[] = [
  // ---- Pains plats & sans levain (à la poêle ou vite faits, le meilleur point de départ pour débuter)
  { id: "naan", family: "plat" },
  { id: "pain_pita", family: "plat" },
  { id: "tortillas_ble", family: "plat" },
  { id: "chapati", family: "plat" },
  { id: "batbout", family: "plat" },
  { id: "msemen", family: "plat" },
  { id: "arepas", family: "plat" },
  { id: "manakish_zaatar", family: "plat" },
  { id: "mhadjeb", family: "plat" },
  { id: "feuilles_brick_maison", family: "plat" },
  { id: "bokit_volaille", family: "plat" },
  { id: "pains_kebab_poele", family: "plat" },
  { id: "injera", family: "plat" },
  { id: "damper", family: "plat" },
  { id: "soda_bread", family: "plat" },
  // ---- Pains levés classiques (pétrissage + pousse, au four)
  { id: "baguette_24h", family: "leve" },
  { id: "pain_cocotte", family: "leve" },
  { id: "pain_de_mie", family: "leve" },
  { id: "pain_campagne_levain", family: "leve" },
  { id: "pain_complet", family: "leve" },
  { id: "fougasse_olives", family: "leve" },
  { id: "bagels", family: "leve" },
  { id: "ciabatta", family: "leve" },
  { id: "pain_sans_gluten", family: "leve" },
  { id: "pain_mais_cornbread", family: "leve" },
  { id: "pain_viennois", family: "leve" },
  { id: "mantou", family: "leve" },
  // ---- Viennoiserie feuilletée (tourage, le plus technique)
  { id: "croissants", family: "feuillete" },
  { id: "pains_chocolat", family: "feuillete" },
  // ---- Brioche & pâte enrichie (beurre et œuf incorporés, sensible à la cuisson)
  { id: "brioche", family: "brioche" },
  { id: "kougelhopf", family: "brioche" },
  { id: "pain_au_lait", family: "brioche" },
  { id: "pains_burger", family: "brioche" },
  // ---- Crêpes, gaufres & pâtes à frire (aucun pétrissage ni pousse)
  { id: "crepes_bretonnes", family: "crepe" },
  { id: "pancakes", family: "crepe" },
  { id: "gaufres", family: "crepe" },
  { id: "spatzle", family: "crepe" },
  { id: "galette_complete", family: "crepe" },
  // ---- Bases, pizza & pâte salée
  { id: "pate_pizza", family: "base" },
  { id: "pizza_margherita", family: "base" },
  { id: "focaccia", family: "base" },
  { id: "pate_brisee", family: "base" },
  { id: "pao_de_queijo", family: "base" },
  { id: "bretzels", family: "base" },
  { id: "pate_a_choux", family: "base" },
];

export const painRecipes = (f?: PainFamily): (Recipe & { entry: PainEntry })[] => curatedRecipes(PAINS, (p) => !f || p.family === f);
