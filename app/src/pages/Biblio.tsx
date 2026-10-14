import { RECIPE_BY_ID } from "../lib/data";
import { href } from "../lib/router";
import { setState, useStore } from "../lib/store";
import { Empty, Grid, Page, RecipeCard, Section } from "../components/ui";

export default function Biblio() {
  const favs = useStore((s) => s.favorites).map((id) => RECIPE_BY_ID[id]).filter(Boolean);
  const menus = useStore((s) => s.menus);
  const imports = useStore((s) => s.imports);
  const cooked = useStore((s) => s.cooked);
  const cookedList = Object.entries(cooked).sort((a, b) => b[1] - a[1]).map(([id, n]) => ({ r: RECIPE_BY_ID[id], n })).filter((x) => x.r);
  return (
    <Page title="Ma bibliothèque" sub="Favoris, menus, imports et recettes déjà cuisinées.">
      <Section title={`Favoris (${favs.length})`}>
        {favs.length ? <Grid>{favs.map((r) => <RecipeCard key={r.id} r={r} />)}</Grid> : <Empty>Touche ♡ sur une recette pour la retrouver ici.</Empty>}
      </Section>
      <Section title={`Menus (${menus.length})`}>
        {menus.length ? menus.map((m) => (
          <div key={m.id} className="card pad">
            <strong>{m.name}</strong> <span className="meta">· {m.guests} convives · {new Date(m.date).toLocaleDateString("fr-FR")}</span>
            <div className="links">{m.recipeIds.map((id) => RECIPE_BY_ID[id] && <a key={id} className="pill" href={href(`/recette/${id}`)}>{RECIPE_BY_ID[id].title}</a>)}</div>
            <p className="small">Boissons : {m.drinks.join(", ")}</p>
            <button className="btn small ghost danger" onClick={() => setState((s) => { s.menus = s.menus.filter((x) => x.id !== m.id); })}>Supprimer</button>
          </div>
        )) : <Empty>Compose un menu depuis une recette (« 🍽 Compléter le menu ») ou la rubrique <a href={href("/fetes")}>Fêtes</a>.</Empty>}
      </Section>
      <Section title={`Mes imports (${imports.length})`} more={<a href={href("/imports")}>Gérer →</a>}>
        {imports.length ? <ul className="links-list">{imports.slice(0, 10).map((i) => <li key={i.id}><a href={i.url} target="_blank" rel="noopener noreferrer">{i.title}</a></li>)}</ul> : <Empty>Importe tes recettes TikTok, Instagram ou YouTube depuis <a href={href("/imports")}>Mes imports</a>.</Empty>}
      </Section>
      {cookedList.length > 0 && (
        <Section title="Déjà cuisinées">
          <ul>{cookedList.map(({ r, n }) => <li key={r.id}><a href={href(`/recette/${r.id}`)}>{r.title}</a> <span className="meta">· {n} fois</span></li>)}</ul>
        </Section>
      )}
    </Page>
  );
}
