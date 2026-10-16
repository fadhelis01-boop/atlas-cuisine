import { useCredits } from "../components/photo";
import { Page, useMore } from "../components/ui";

/** Crédits des photos (licences CC BY / CC BY-SA / CC0 / domaine public : attribution obligatoire). */
export default function Credits() {
  const credits = useCredits();
  const entries = Object.entries(credits ?? {}).sort(([a], [b]) => a.localeCompare(b, "fr"));
  const { shown, more } = useMore(entries, 50);
  return (
    <Page title="Crédits photos" sub="Les photos d'ATLAS viennent de banques d'images libres (Wikimedia Commons, Flickr via Openverse). Merci à leurs auteur·e·s." back="/profil">
      <p className="small">Les photos ont été recadrées et légèrement étalonnées pour l'application ; ces versions adaptées restent sous la licence de l'original (« partage dans les mêmes conditions » pour les CC BY-SA). Ce sont des photos d'illustration : le plat présenté peut différer de la recette ATLAS. Un·e auteur·e qui souhaite le retrait ou la correction d'un crédit peut le demander via le dépôt du projet.</p>
      {!credits && <p className="meta">Chargement des crédits…</p>}
      <p className="small">{entries.length} photos créditées.</p>
      <table className="table">
        <thead><tr><th>Sujet</th><th>Auteur·e</th><th>Licence</th><th>Source</th></tr></thead>
        <tbody>
          {shown.map(([k, m]) => (
            <tr key={k}>
              <td>{k.split("/")[0]} · {k.split("/")[1].replace(/[_-]/g, " ")}</td>
              <td>{m.author}</td>
              <td>{m.licenseUrl ? <a href={m.licenseUrl} target="_blank" rel="noopener noreferrer">{m.license}</a> : m.license}</td>
              <td><a href={m.page} target="_blank" rel="noopener noreferrer">{m.source}</a></td>
            </tr>
          ))}
        </tbody>
      </table>
      {more}
    </Page>
  );
}
