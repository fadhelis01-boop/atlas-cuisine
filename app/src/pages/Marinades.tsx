import { Icon } from "../components/icons";
import { useMemo, useState } from "react";
import { href } from "../lib/router";
import { minutes } from "../lib/text";
import { MARINADES, PROTEIN_LABEL, REPERES_MARINADE, marinadeRecipes, type Protein } from "../lib/marinades";
import { Chip, MoreGrid, Page, Section } from "../components/ui";

// Rubrique Marinades (audit UI/UX senior, 20/11/2026) : réunit les marinades jusque-là dispersées dans les sauces et
// condiments, classées par type de viande/poisson puis par pays, temps de repos visible sur chaque fiche.
const PROTEINS: Protein[] = ["boeuf", "agneau", "porc", "volaille", "poisson", "crevettes", "vegetal"];

export default function Marinades() {
  const [p, setP] = useState<Protein | "tout">("tout");
  const list = useMemo(() => marinadeRecipes(p === "tout" ? undefined : p), [p]);
  return (
    <Page
      photo="rubrique/sauces"
      title="Marinades"
      back="/explorer"
      sub="Les marinades du monde entier, classées par viande ou poisson : pays d'origine, temps de repos, et le geste du cure à sec (gravlax) à côté de la marinade liquide classique."
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
                <Icon name="timer" size={14} className="ic-inline" /> {m.entry.cure ? "Cure à sec : " : "Repos : "}
                {minutes(r.rest)} · {(r.regionPath ?? []).slice(-1)[0] ?? r.macro}
              </p>
            );
          }}
        />
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
