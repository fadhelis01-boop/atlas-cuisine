import { ImportRow } from "../components/video";
import { IMPORT_LIBRARY, RECIPES, RECIPE_BY_ID } from "../lib/data";
import { ANATOMIE, CONSERVATION, DLC_DDM } from "../lib/content";
import { href } from "../lib/router";
import { Grid, Page, RecipeCard, Section, useVisible } from "../components/ui";

export default function ZeroDechet() {
  const list = useVisible(RECIPES.filter((r) => r.cats.includes("zero_dechet")));
  const tiktok = IMPORT_LIBRARY.filter((i) => i.cat === "zero_dechet" || i.cat === "fait_maison");
  return (
    <Page photo="rubrique/zero_dechet" title="Zéro déchet" sub="Chaque ingrédient a plusieurs vies : carcasse, épluchures, fanes, pain rassis, blancs d'œufs… Voici comment tout utiliser." back="/explorer">
      <Section title="L'anatomie des ingrédients">
        <div className="table-wrap">
          <table className="table">
            <thead><tr><th>Ingrédient</th><th>Parties</th><th>Que faire</th><th>Recettes</th></tr></thead>
            <tbody>{ANATOMIE.map((a) => (
              <tr key={a.ing}><th>{a.ing}</th><td>{a.parts}</td><td>{a.uses}</td>
                <td>{a.recipes.filter((id) => RECIPE_BY_ID[id]).map((id) => <a key={id} className="pill" href={href(`/recette/${id}`)}>{RECIPE_BY_ID[id].title.split(" (")[0]}</a>)}</td></tr>
            ))}</tbody>
          </table>
        </div>
      </Section>
      <Section title="Recettes anti-gaspi"><Grid>{list.map((r) => <RecipeCard key={r.id} r={r} />)}</Grid></Section>
      <Section title="Cuisiner une fois, manger trois fois">
        <ol>
          <li><a href={href("/recette/poulet_roti")}>Poulet rôti</a> le dimanche ;</li>
          <li><a href={href("/recette/bouillon_volaille")}>bouillon avec la carcasse</a> le lundi (et un velouté) ;</li>
          <li><a href={href("/recette/riz_cantonais")}>riz cantonais</a> avec les restes de chair et le riz de la veille.</li>
        </ol>
      </Section>
      <Section title="Conserver sans risque">
        <table className="table"><tbody>{CONSERVATION.map(([a, b]) => <tr key={a}><th>{a}</th><td>{b}</td></tr>)}</tbody></table>
        <p className="small">{DLC_DDM}</p>
        <p>Ton <a href={href("/frigo")}>frigo virtuel</a> classe tes produits par date et propose d'abord les recettes qui utilisent ce qui arrive à échéance.</p>
      </Section>
      {tiktok.length > 0 && <Section title="Fait maison et anti-gaspi dans tes favoris"><ul className="links-list">{tiktok.map((i) => <ImportRow key={i.url} i={i} />)}</ul></Section>}
    </Page>
  );
}
