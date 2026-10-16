import { Icon } from "../components/icons";
import { INGREDIENTS, RECIPE_BY_ID } from "../lib/data";
import { href } from "../lib/router";
import { LABELS, MALIN, PHRASES, RATTRAPAGES, RAYONS, type Choix } from "../lib/marche";
import { Page, Section } from "../components/ui";

// Guide « Bien choisir, bien rattraper » : l'œil du maraîcher, du boucher et du poissonnier, puis les rattrapages
// (et les cas où l'on jette, sans discussion).
function ChoixCard({ c }: { c: Choix }) {
  const linked = c.refs.filter((r) => INGREDIENTS[r]);
  return (
    <details className="card pad choix">
      <summary><strong>{c.name}</strong></summary>
      <p><Icon name="check" size={16} className="ic-inline" /> <strong>Je prends :</strong> {c.good}</p>
      <p><Icon name="ban" size={16} className="ic-inline" /> <strong>J'évite :</strong> {c.avoid}</p>
      {c.tip && <p className="small"><strong>Astuce de pro :</strong> {c.tip}</p>}
      {linked.length > 0 && <p className="small">Au dictionnaire : {linked.map((r) => <a key={r} className="pill" href={href(`/ingredient/${INGREDIENTS[r].slug}`)}>{r.split(" (")[0]}</a>)}</p>}
    </details>
  );
}

export default function Marche() {
  return (
    <Page photo="rubrique/frigo" title="Bien choisir, bien rattraper" back="/explorer"
      sub="Ce que regardent le maraîcher, le boucher et le poissonnier ; que faire d'un fruit trop mûr, d'une viande dure ou d'un poisson moins frais, et quand il faut jeter.">
      <nav className="chips toc" aria-label="Sommaire">
        {RAYONS.map((r) => <a key={r.id} className="chip" href={`#${r.id}`} onClick={(e) => { e.preventDefault(); document.getElementById(r.id)?.scrollIntoView({ behavior: "smooth" }); }}><Icon name={r.icon} size={16} className="ic-inline" /> {r.title}</a>)}
        <a className="chip" href="#rattraper" onClick={(e) => { e.preventDefault(); document.getElementById("rattraper")?.scrollIntoView({ behavior: "smooth" }); }}><Icon name="lifebuoy" size={16} className="ic-inline" /> Rattraper</a>
      </nav>

      {RAYONS.map((r) => (
        <Section key={r.id} id={r.id} title={`${r.title} : l'œil ${r.who.startsWith("le ") ? "du " + r.who.slice(3) : "de " + r.who}`}>
          <p>{r.intro}</p>
          <div className="choix-list">{r.items.map((c) => <ChoixCard key={c.name} c={c} />)}</div>
        </Section>
      ))}

      <Section id="rattraper" title="Rattraper… ou jeter">
        <div className="choix-list">
          {RATTRAPAGES.map((x) => (
            <details key={x.id} className="card pad choix" open={x.id === "poisson-moins-frais"}>
              <summary><strong>{x.title}</strong></summary>
              <p>{x.ok}</p>
              <ul>{x.how.map((h) => <li key={h}>{h}</li>)}</ul>
              {x.jeter && <p className="jeter"><Icon name="alert" size={16} className="ic-inline" /> <strong>On jette si :</strong> {x.jeter}</p>}
              {x.recipes && <p className="small">{x.recipes.filter((id) => RECIPE_BY_ID[id]).map((id) => <a key={id} className="pill" href={href(`/recette/${id}`)}>{RECIPE_BY_ID[id].title.split(" (")[0]}</a>)}</p>}
            </details>
          ))}
        </div>
        <p className="small">Des restes déjà cuits ? <a href={href("/restes")}>La cuisine des restes</a> propose entrée, plat, sandwich, dessert ou menu complet.</p>
      </Section>

      <Section title="Ce que disent les étiquettes">
        <table className="table"><tbody>{LABELS.map(([a, b]) => <tr key={a}><th>{a}</th><td>{b}</td></tr>)}</tbody></table>
      </Section>

      <Section title="Oser demander">
        <p>Les artisans aiment conseiller : dis ce que tu cuisines et pour combien, ils choisissent le morceau et font la découpe.</p>
        <table className="table"><tbody>{PHRASES.map(([a, b]) => <tr key={a}><th>{a}</th><td>{b}</td></tr>)}</tbody></table>
      </Section>

      <Section title="Acheter malin">
        <ul>{MALIN.map((m) => <li key={m}>{m}</li>)}</ul>
        <p className="small">Repères de professionnels, pas encore vérifiés dans la cuisine d'ATLAS : en cas de doute sur la fraîcheur d'un produit animal, on ne prend pas de risque.</p>
      </Section>
    </Page>
  );
}
