// Barre d'onglets autour des usages du quotidien (audit dév/UX 2026-10-21 §2.3) : la semaine a son onglet, chaque écran
// allume le bon onglet (jamais « Accueil » par défaut), le profil passe en bouton rond en haut à droite sur téléphone.
export const TABS = [
  { to: "/", label: "Accueil", icon: "home", match: [""] },
  { to: "/explorer", label: "Explorer", icon: "compass", match: ["explorer", "region", "recherche", "techniques", "technique", "pains", "sauces", "fetes", "enfants", "menu", "zero-dechet", "dictionnaire", "ingredient", "recettes", "apprendre", "pique-nique"] },
  { to: "/semaine", label: "Ma semaine", icon: "calendar", match: ["semaine", "courses", "restes", "partage"] },
  { to: "/frigo", label: "Frigo", icon: "fridge", match: ["frigo", "bien-choisir"] },
  { to: "/biblio", label: "Mes recettes", icon: "book", match: ["biblio", "imports"] },
];
export const PROFILE_MATCH = ["profil", "credits"];
/** Écrans sans onglet allumé, volontairement : la fiche recette et le mode cuisine (on y arrive de partout). */
export const NO_TAB = ["recette", "cuisine", "icones"];
/** Onglet d'un écran (null = aucun). */
export const tabOf = (p0: string | undefined) => TABS.find((t) => t.match.includes(p0 ?? "")) ?? null;
/** Lien du mode cuisine : toujours avec les portions choisies (audit dév/UX 2026-10-21 : un des deux boutons les perdait). */
export const cookHref = (id: string, portions: number, adapted: boolean) => `/cuisine/${id}?portions=${portions}${adapted ? "&adapte=1" : ""}`;
