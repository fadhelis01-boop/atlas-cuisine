import { Icon } from "../components/icons";
import { useMemo, useState } from "react";
import { RECIPE_BY_ID } from "../lib/data";
import { href } from "../lib/router";
import { verdict } from "../lib/engine";
import { useProfile } from "../lib/store";
import { FILTRES, GAMELLE, PANIERS, RESTES_PN, SAC, SECURITE, ZERO, piqueNique } from "../lib/piquenique";
import { Chip, MoreGrid, Page, Section, useVisible } from "../components/ui";

// Rubrique Pique-nique : paniers tout faits, toutes les recettes qui voyagent (filtrées par le profil du foyer),
// puis la sécurité, le sac, le zéro déchet, les restes et la gamelle.
export default function PiqueNique() {
  const p = useProfile();
  const all = useVisible(piqueNique());
  const [f, setF] = useState("tout");
  const list = useMemo(() => all.filter(FILTRES.find((x) => x.id === f)!.test), [all, f]);
  return (
    <Page photo="rubrique/pique_nique" title="Pique-nique" back="/explorer"
      sub="Ce qui voyage bien et se mange avec les doigts : des classiques, des idées du monde, pour les enfants et pour les grands, sans gaspiller et en sécurité au soleil.">
      <Section title="Paniers tout faits">
        <div className="paniers">
          {PANIERS.map((pn) => {
            const items = pn.ids.map((id) => RECIPE_BY_ID[id]).filter((r) => r && verdict(r, p).availability !== "hidden");
            return (
              <div key={pn.id} className="card pad panier">
                <h3>{pn.title}</h3>
                <p className="small">{pn.for}</p>
                <ul>{items.map((r) => <li key={r.id}><a href={href(`/recette/${r.id}`)}>{r.title.split(" (")[0]}</a></li>)}</ul>
              </div>
            );
          })}
        </div>
      </Section>

      <Section title={`Toutes les recettes à emporter (${list.length})`}>
        <div className="chips" role="group" aria-label="Filtrer">{FILTRES.map((x) => <Chip key={x.id} on={f === x.id} onClick={() => setF(x.id)}>{x.label}</Chip>)}</div>
        <MoreGrid key={f} items={list} />
      </Section>

      <Section title="En sécurité, même au soleil">
        <ul className="pn-list">{SECURITE.map((s) => <li key={s}><Icon name="alert" size={16} className="ic-inline" /> {s}</li>)}</ul>
      </Section>

      <Section title="Préparer le sac">
        <table className="table"><tbody>{SAC.map(([a, b]) => <tr key={a}><th>{a}</th><td>{b}</td></tr>)}</tbody></table>
      </Section>

      <Section title="Zéro déchet sur la nappe">
        <ul className="pn-list">{ZERO.map((s) => <li key={s}><Icon name="recycle" size={16} className="ic-inline" /> {s}</li>)}</ul>
      </Section>

      <Section title="Un pique-nique avec les restes du frigo">
        <table className="table"><tbody>{RESTES_PN.map(([id, a, b]) => <tr key={id}><th><a href={href(`/restes?r=${id}`)}>{a}</a></th><td>{b}</td></tr>)}</tbody></table>
        <p className="small">Toutes les idées, avec les délais de conservation : <a href={href("/restes")}>la cuisine des restes</a>.</p>
      </Section>

      <Section title="Et la gamelle (école, travail) ?">
        <ul className="pn-list">{GAMELLE.map((s) => <li key={s}>{s}</li>)}</ul>
      </Section>
    </Page>
  );
}
