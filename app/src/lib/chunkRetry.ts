// Rechargement après un chunk introuvable (audit dév/UX senior 23/11/2026, signalé par un problème de chargement
// sur mobile du coin Marinades) : chaque déploiement republie exactement `dist/` et supprime les fichiers devenus
// inutiles (`deploy.mjs`) ; un onglet resté ouvert depuis avant un déploiement tente encore de charger une page à la
// demande (React.lazy) sous son ancien nom de fichier, qui n'existe plus sur le serveur. Sur un réseau mobile, cet
// échec peut traîner (au lieu d'un 404 net) et laisser l'écran bloqué sur « Chargement… ». Un seul rechargement
// automatique (jamais en boucle) suffit : il récupère la page actuelle avec les noms de fichiers à jour.
const RELOADED_KEY = "atlas-chunk-reload";

export function lazyRetry<T>(loader: () => Promise<T>): () => Promise<T> {
  return () =>
    loader().catch((err) => {
      let already = false;
      try {
        already = sessionStorage.getItem(RELOADED_KEY) === "1";
      } catch {
        /* stockage indisponible (navigation privée…) : pas de rechargement automatique, l'erreur s'affiche normalement */
      }
      if (already) throw err;
      try {
        sessionStorage.setItem(RELOADED_KEY, "1");
      } catch {
        throw err;
      }
      location.reload();
      return new Promise<T>(() => {}); // le rechargement arrive ; cette promesse n'a pas besoin de se résoudre
    });
}
