import { Icon } from "../components/icons";
import { useMemo, useState } from "react";
import { RECIPE_BY_ID } from "../lib/data";
import { href } from "../lib/router";
import { verdict } from "../lib/engine";
import { useProfile } from "../lib/store";
import { FAMILLES, GESTES, SECURITE_STREET, SOIREES, streetRecipes } from "../lib/streetfood";
import { Chip, MoreGrid, Page, Section, useVisible } from "../components/ui";

// Rubrique Street food (12/11/2026) : les familles de la cuisine de rue du monde, des soirées toutes faites, les gestes
// des stands adaptés à la maison et la sécurité de la friture. Filtrée par le profil du foyer, comme le reste de l'atlas.
export default function StreetFood() {
  const p = useProfile();
  const [f, setF] = useState("tout");
  const famille = FAMILLES.find((x) => x.id === f);
  const all = useMemo(() => [...new Map(FAMILLES.flatMap(streetRecipes).map((r) => [r.id, r])).values()], []);
  const list = useVisible(famille ? streetRecipes(famille) : all);
  return (
    <Page photo="recette/tacos_al_pastor" title="Street food" back="/explorer"
      sub="La cuisine des stands, des marchés de nuit et des camions du monde entier, refaite à la maison : sandwichs, galettes, fritures, brochettes, bouchées et douceurs.">
      <Section title="Soirées street food toutes faites">
        <div className="paniers">
          {SOIREES.map((s) => {
            const items = s.ids.map((id) => RECIPE_BY_ID[id]).filter((r) => r && verdict(r, p).availability !== "hidden");
            return (
              <div key={s.title} className="card pad panier">
                <h3>{s.title}</h3>
                <p className="small">{s.for}</p>
                <ul>{items.map((r) => <li key={r.id}><a href={href(`/recette/${r.id}`)}>{r.title.split(" (")[0]}</a></li>)}</ul>
              </div>
            );
          })}
        </div>
      </Section>

      <Section title={`${famille ? famille.label : "Toute la street food"} (${list.length})`}>
        <div className="chips" role="group" aria-label="Familles">
          <Chip on={f === "tout"} onClick={() => setF("tout")}>Tout</Chip>
          {FAMILLES.map((x) => <Chip key={x.id} on={f === x.id} onClick={() => setF(x.id)}><Icon name={x.icon} size={16} className="ic-inline" /> {x.label}</Chip>)}
        </div>
        {famille && <p className="small">{famille.sub}</p>}
        <MoreGrid key={f} items={list} />
      </Section>

      <Section title="Les gestes des stands, à la maison">
        <table className="table"><tbody>{GESTES.map(([a, b]) => <tr key={a}><th>{a}</th><td>{b}</td></tr>)}</tbody></table>
        <p className="small">Pour aller plus loin : <a href={href("/technique/frire-tempura")}>frire et paner</a>, <a href={href("/technique/wok")}>sauter au wok</a>,{" "}
          <a href={href("/technique/griller-barbecue")}>griller</a>, <a href={href("/technique/plier-raviolis")}>plier les raviolis</a>, <a href={href("/sauces")}>les sauces maison</a>.</p>
      </Section>

      <Section title="Friture et sécurité">
        <ul className="pn-list">{SECURITE_STREET.map((s) => <li key={s}><Icon name="alert" size={16} className="ic-inline" /> {s}</li>)}</ul>
      </Section>
    </Page>
  );
}
