import { Icon } from "../components/icons";
import { ImportRow } from "../components/video";
import { useState } from "react";
import { CATALOGUE, useImportLibrary, INGREDIENTS, INGREDIENT_NAMES, MACROS, RECIPES } from "../lib/data";
import { TECHNIQUES } from "../lib/techniques";
import { go, href } from "../lib/router";
import { search } from "../lib/text";
import { Chip, Empty, MoreGrid, MoreList, Page, Section, useVisible } from "../components/ui";
import { fuzzyRecipes, parseIntents } from "../lib/intents";

import type { Recipe } from "../lib/types";

// filtres repliables (audit UX 3) : une seule recherche, sans changer de page
const KINDS: [string, (r: Recipe) => boolean][] = [["Entrées", (r) => r.role === "entree"], ["Plats", (r) => r.role === "plat"], ["Desserts", (r) => r.role === "dessert"], ["Boissons", (r) => r.role === "boisson"], ["Sauces & bases", (r) => r.kind === "Sauce" || r.kind === "Base"]];
import { useStore } from "../lib/store";

export default function Search({ q }: { q: string }) {
  const IMPORT_LIBRARY = useImportLibrary();
  const [v, setV] = useState(q);
  const mine = useStore((s) => s.imports);
  const [kind, setKind] = useState<string | null>(null);
  const [fast, setFast] = useState(false);
  const [easy, setEasy] = useState(false);
  const visible = useVisible(RECIPES);
  const { intents, rest } = parseIntents(q);
  const base = intents.length ? visible.filter((r) => intents.every((it) => it.test(r))) : visible;
  const fieldsOf = (r: Recipe) => [r.title, r.origin, r.regionPath.join(" "), r.ingredients.map((i) => i.label).join(" "), r.cats.join(" "), r.fetes.join(" ")];
  let recipesAll = rest ? search(base, rest, fieldsOf, 600) : intents.length ? base : [];
  if (!recipesAll.length && rest) recipesAll = fuzzyRecipes(base, rest); // fautes plus lourdes (« creppe »)
  const tq = rest || q;
  const recipes = recipesAll.filter((r) => (!kind || KINDS.find((k) => k[0] === kind)![1](r)) && (!fast || r.active + r.rest <= 30) && (!easy || r.level === 1));
  const nFilters = +!!kind + +fast + +easy;
  const macros = search(MACROS, tq, (m) => [m.name, m.blurb]);
  const ings = search(INGREDIENT_NAMES.filter((n, i, a) => a.findIndex((m) => INGREDIENTS[m].slug === INGREDIENTS[n].slug) === i), tq, (n) => [n], 10);
  const techs = search(TECHNIQUES, tq, (t) => [t.name, t.family, t.keys.join(" ")], 8);
  const cat = search(CATALOGUE, tq, (c) => [c.title, c.region], 20);
  const imps = search(IMPORT_LIBRARY, tq, (i) => [i.title, i.author], 20);
  const myImps = search(mine, tq, (i) => [i.title, i.caption], 10);
  const total = ings.length + recipes.length + macros.length + techs.length + cat.length + imps.length + myImps.length;
  return (
    <Page title="Recherche" sub="Insensible aux accents et aux petites fautes : « tagine », « boeuf », « pad thai » marchent aussi.">
      <form role="search" className="searchbar" onSubmit={(e) => { e.preventDefault(); go(`/recherche?q=${encodeURIComponent(v)}`); }}>
        <input type="search" value={v} onChange={(e) => setV(e.target.value)} autoFocus aria-label="Rechercher" placeholder="tajine, naan, sauce blanche, crêpes…" />
        <button className="btn" type="submit">Chercher</button>
      </form>
      {q && !total && <Empty>Rien trouvé pour « {q} ». Essaie un ingrédient dans <a href={href("/frigo")}>Avec ce que j'ai</a>.</Empty>}
      {macros.length > 0 && <Section title="Régions"><div className="links">{macros.map((m) => <a key={m.id} className="pill" href={href(`/region/${m.id}`)}><Icon name={m.icon} size={18} className="ic-inline" /> {m.name}</a>)}</div></Section>}
      {intents.length > 0 && <p className="small understood"><Icon name="check" size={16} className="ic-inline" /> Compris : {intents.map((it) => it.label).join(" · ")}{rest ? ` · « ${rest} »` : ""}</p>}
      {recipesAll.length > 0 && (
        <details className="search-filters" open={nFilters > 0}>
          <summary>Filtrer les recettes{nFilters ? ` (${nFilters})` : ""}</summary>
          <div className="chips">
            {KINDS.map(([k]) => <Chip key={k} on={kind === k} onClick={() => setKind(kind === k ? null : k)}>{k}</Chip>)}
            <Chip on={fast} onClick={() => setFast(!fast)}><Icon name="timer" size={16} className="ic-inline" /> ≤ 30 min</Chip>
            <Chip on={easy} onClick={() => setEasy(!easy)}>Facile</Chip>
          </div>
        </details>
      )}
      {recipesAll.length > 0 && !recipes.length && <p className="small">Aucune recette avec ces filtres : retire-en un.</p>}
      {recipes.length > 0 && <Section title={`Recettes (${recipes.length})`} more={<a href={href(`/recettes?q=${encodeURIComponent(q)}`)}>Plus de filtres →</a>}><MoreGrid key={`${q}|${kind}|${fast}|${easy}`} items={recipes} /></Section>}
      {ings.length > 0 && <Section title="Dictionnaire des ingrédients"><div className="links">{ings.map((n) => <a key={n} className="pill" href={href(`/ingredient/${INGREDIENTS[n].slug}`)}><Icon name="dictionary" size={18} className="ic-inline" /> {n}</a>)}</div></Section>}
      {techs.length > 0 && <Section title="Techniques"><div className="links">{techs.map((t) => <a key={t.id} className="pill" href={href(`/technique/${t.id}`)}><Icon name="knife" size={18} className="ic-inline" /> {t.name}</a>)}</div></Section>}
      {myImps.length > 0 && <Section title="Mes imports"><ul className="links-list">{myImps.map((i) => <li key={i.id}><a href={i.url || "#/imports"} target="_blank" rel="noopener noreferrer">{i.title}</a></li>)}</ul></Section>}
      {imps.length > 0 && <Section title="Favoris TikTok et sites classés"><MoreList items={imps} step={8} render={(i) => <ImportRow key={i.url} i={i} />} /></Section>}
      {cat.length > 0 && <Section title="Au programme (fiches à venir)"><ul className="cat-list">{cat.map((c) => <li key={c.title + c.region}>{c.title} <span className="meta">· {c.region}</span></li>)}</ul></Section>}
    </Page>
  );
}
