import { ImportRow } from "../components/video";
import { useState } from "react";
import { CATALOGUE, useImportLibrary, INGREDIENTS, INGREDIENT_NAMES, MACROS, RECIPES } from "../lib/data";
import { TECHNIQUES } from "../lib/techniques";
import { go, href } from "../lib/router";
import { search } from "../lib/text";
import { Empty, Grid, Page, RecipeCard, Section } from "../components/ui";
import { useStore } from "../lib/store";

export default function Search({ q }: { q: string }) {
  const IMPORT_LIBRARY = useImportLibrary();
  const [v, setV] = useState(q);
  const mine = useStore((s) => s.imports);
  const recipes = search(RECIPES, q, (r) => [r.title, r.origin, r.regionPath.join(" "), r.ingredients.map((i) => i.label).join(" "), r.cats.join(" "), r.fetes.join(" ")]);
  const macros = search(MACROS, q, (m) => [m.name, m.blurb]);
  const ings = search(INGREDIENT_NAMES.filter((n, i, a) => a.findIndex((m) => INGREDIENTS[m].slug === INGREDIENTS[n].slug) === i), q, (n) => [n], 10);
  const techs = search(TECHNIQUES, q, (t) => [t.name, t.family, t.keys.join(" ")], 8);
  const cat = search(CATALOGUE, q, (c) => [c.title, c.region], 20);
  const imps = search(IMPORT_LIBRARY, q, (i) => [i.title, i.author], 20);
  const myImps = search(mine, q, (i) => [i.title, i.caption], 10);
  const total = ings.length + recipes.length + macros.length + techs.length + cat.length + imps.length + myImps.length;
  return (
    <Page title="Recherche" sub="Insensible aux accents et aux petites fautes : « tagine », « boeuf », « pad thai » marchent aussi.">
      <form role="search" className="searchbar" onSubmit={(e) => { e.preventDefault(); go(`/recherche?q=${encodeURIComponent(v)}`); }}>
        <input type="search" value={v} onChange={(e) => setV(e.target.value)} autoFocus aria-label="Rechercher" placeholder="tajine, naan, sauce blanche, crêpes…" />
        <button className="btn" type="submit">Chercher</button>
      </form>
      {q && !total && <Empty>Rien trouvé pour « {q} ». Essaie un ingrédient dans <a href={href("/frigo")}>Avec ce que j'ai</a>.</Empty>}
      {macros.length > 0 && <Section title="Régions"><div className="links">{macros.map((m) => <a key={m.id} className="pill" href={href(`/region/${m.id}`)}>{m.emoji} {m.name}</a>)}</div></Section>}
      {recipes.length > 0 && <Section title={`Recettes (${recipes.length})`}><Grid>{recipes.map((r) => <RecipeCard key={r.id} r={r} />)}</Grid></Section>}
      {ings.length > 0 && <Section title="Dictionnaire des ingrédients"><div className="links">{ings.map((n) => <a key={n} className="pill" href={href(`/ingredient/${INGREDIENTS[n].slug}`)}>📖 {n}</a>)}</div></Section>}
      {techs.length > 0 && <Section title="Techniques"><div className="links">{techs.map((t) => <a key={t.id} className="pill" href={href(`/technique/${t.id}`)}>🔪 {t.name}</a>)}</div></Section>}
      {myImps.length > 0 && <Section title="Mes imports"><ul className="links-list">{myImps.map((i) => <li key={i.id}><a href={i.url || "#/imports"} target="_blank" rel="noopener noreferrer">{i.title}</a></li>)}</ul></Section>}
      {imps.length > 0 && <Section title="Favoris TikTok et sites classés"><ul className="links-list">{imps.map((i) => <ImportRow key={i.url} i={i} />)}</ul></Section>}
      {cat.length > 0 && <Section title="Au programme (fiches à venir)"><ul className="cat-list">{cat.map((c) => <li key={c.title + c.region}>{c.title} <span className="meta">· {c.region}</span></li>)}</ul></Section>}
    </Page>
  );
}
