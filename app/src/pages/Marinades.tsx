import { Icon } from "../components/icons";
import { useMemo, useState } from "react";
import { href } from "../lib/router";
import { safeHref } from "../lib/safe";
import { minutes } from "../lib/text";
import {
  MARINADES,
  PROTEIN_LABEL,
  QUICK_MARINADES,
  QUICK_MARINADES_CREDIT,
  REPERES_MARINADE,
  SPICE_MIXES,
  marinadeRecipes,
  type Protein,
} from "../lib/marinades";
import { Chip, MoreGrid, MoreList, Page, Section } from "../components/ui";

// Rubrique Marinades (audit UI/UX senior, 20/11/2026) : réunit les marinades jusque-là dispersées dans les sauces et
// condiments, classées par type de viande/poisson puis par pays, temps de repos visible sur chaque fiche.
const PROTEINS: Protein[] = ["boeuf", "agneau", "porc", "volaille", "poisson", "crevettes", "vegetal"];

export default function Marinades() {
  const [p, setP] = useState<Protein | "tout">("tout");
  const list = useMemo(() => marinadeRecipes(p === "tout" ? undefined : p), [p]);
  return (
    <Page
      photo="recette/mojo_cubain_porc"
      title="Marinades"
      back="/explorer"
      sub={
        "Les marinades du monde entier, classées par viande ou poisson : pays d'origine, temps de repos, et les trois " +
        "gestes — marinade liquide, cure à sec (gravlax) et rub sec (BBQ) — distingués sur chaque fiche."
      }
    >
      <Section title={`${p === "tout" ? "Toutes les marinades" : PROTEIN_LABEL[p]} (${list.length})`}>
        <div className="chips" role="group" aria-label="Viande ou poisson">
          <Chip on={p === "tout"} onClick={() => setP("tout")}>
            Tout ({MARINADES.length})
          </Chip>
          {PROTEINS.map((x) => {
            const n = marinadeRecipes(x).length;
            return n ? (
              <Chip key={x} on={p === x} onClick={() => setP(x)}>
                {PROTEIN_LABEL[x]} ({n})
              </Chip>
            ) : null;
          })}
        </div>
        <MoreGrid
          key={p}
          items={list}
          note={(r) => {
            const m = list.find((x) => x.id === r.id)!;
            return (
              <p className="small">
                <Icon name="timer" size={14} className="ic-inline" /> {m.entry.cure ? "Cure à sec : " : m.entry.dry ? "Rub sec, repos : " : "Repos : "}
                {minutes(r.rest)} · {(r.regionPath ?? []).slice(-1)[0] ?? r.macro}
              </p>
            );
          }}
        />
      </Section>

      <Section title={`Marinades expresses (30 min à 2 h, ${QUICK_MARINADES.length})`}>
        <p className="small">Des combinaisons rapides, à la louche plutôt qu'en fiche détaillée : proportions pour environ 500 g de viande, volaille, poisson ou légumes.</p>
        <MoreList
          items={QUICK_MARINADES}
          step={6}
          className="rescue nolist"
          render={(m) => (
            <li className="card pad" key={m.id}>
              <strong>{m.name}</strong>
              <ul className="small">
                {m.ingredients.map((i) => (
                  <li key={i}>{i}</li>
                ))}
              </ul>
            </li>
          )}
        />
        <p className="small">
          Mélanger puis laisser mariner au frais 30 min à 2 h selon l'aliment (crevettes et poisson : vers 30 min, viande rouge : jusqu'à 2 h) ; cuire à cœur. D'après{" "}
          <a href={safeHref(QUICK_MARINADES_CREDIT.url)} target="_blank" rel="noopener noreferrer">
            {QUICK_MARINADES_CREDIT.author}
          </a>
          .
        </p>
      </Section>

      <Section title="Mélanges d'épices secs, par aliment">
        <p className="small">
          Pas de liquide, pas de repos obligatoire : à saupoudrer ou masser juste avant la cuisson. Pour un vrai rub qui croûte à la cuisson longue, voir le BBQ rub américain
          ci-dessus.
        </p>
        <div className="rescue">
          {SPICE_MIXES.map((m) => (
            <div className="card pad" key={m.id}>
              <strong>{m.name}</strong>
              <ul className="small">
                {m.ingredients.map((i) => (
                  <li key={i}>{i}</li>
                ))}
              </ul>
              <p className="small">{m.use}</p>
            </div>
          ))}
        </div>
      </Section>

      <Section title="Les repères du cuisinier, pour n'importe quelle marinade">
        <table className="table">
          <tbody>
            {REPERES_MARINADE.map(([a, b]) => (
              <tr key={a}>
                <th>{a}</th>
                <td>{b}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <p className="small">
          Pour aller plus loin : <a href={href("/technique/attendrir-viande")}>mariner et attendrir</a>, <a href={href("/technique/griller-barbecue")}>griller</a>,{" "}
          <a href={href("/sauces")}>les sauces maison</a>.
        </p>
      </Section>
    </Page>
  );
}
