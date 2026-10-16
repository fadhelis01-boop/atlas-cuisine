import { Icon } from "./icons";
import { useState } from "react";
import { RECIPE_BY_ID, useLeftovers } from "../lib/data";
import { verdict } from "../lib/engine";
import { href } from "../lib/router";
import { getState, setState, useProfile } from "../lib/store";
import type { Recipe } from "../lib/types";

// Zéro déchet ingrédient par ingrédient (Tome 12 §6) : pour chaque ingrédient entamé de la recette,
// ce qui reste, comment le garder sans risque, et quoi en faire (repas en cours, autre plat, hors cuisine).
const KIND: Record<string, { icon: string; label: string }> = {
  repas: { icon: "plate", label: "Dans ce repas" }, plat: { icon: "pot", label: "Un autre plat" },
  conserver: { icon: "snowflake", label: "Conserver" }, hors: { icon: "sprout", label: "Hors cuisine" },
};
const ORDER = ["repas", "plat", "conserver", "hors"];
const short = (n: string) => n.split(" (")[0].split(" / ")[0];

export default function Leftovers({ r }: { r: Recipe }) {
  const leftovers = useLeftovers(r.id);
  const p = useProfile();
  const [added, setAdded] = useState<string[]>([]);
  const toFridge = (ref: string, part: string) => {
    // date limite prudente : 3 jours (frigo) ; l'utilisateur peut la corriger dans « Mon frigo »
    const dlc = new Date(Date.now() + 3 * 86400000).toISOString().slice(0, 10);
    if (!getState().fridge.some((f) => f.ref === ref)) setState((s) => { s.fridge.push({ ref, dlc, zone: "frigo", added: new Date().toISOString() }); });
    setAdded((a) => [...a, `${ref}|${part}`]);
  };
  return (
    <div className="zw card pad">
      <h3><Icon name="recycle" size={20} className="ic-inline" /> Zéro déchet : ce qu'il te restera, et quoi en faire</h3>
      {r.zeroWaste.length > 0 && <ul className="zw-chef">{r.zeroWaste.map((z, i) => <li key={i}>{z.replace(/\*\*/g, "")}</li>)}</ul>}
      {leftovers === null && <p className="small">Chargement des idées zéro déchet…</p>}
      {leftovers?.length === 0 && <p className="small">Cette recette utilise ses ingrédients en entier ou des produits du placard qui se gardent : rien à jeter.</p>}
      {(leftovers ?? []).map((lo) => (
        <details key={lo.ref} className="zw-item">
          <summary><strong>{short(lo.ref)}</strong> <span className="meta">· tu achètes : {lo.sold} · la recette en utilise : {lo.line}</span></summary>
          {lo.parts.map((pt) => (
            <div key={pt.part} className="zw-part">
              <p><strong>Il reste : {pt.part}.</strong> <span className="small">Conservation : {pt.keep}</span></p>
              <ul className="zw-ideas">
                {ORDER.flatMap((k) => pt.ideas.filter((i) => i.kind === k)).map((i, n) => {
                  const rec = i.recipe ? RECIPE_BY_ID[i.recipe] : null;
                  const hidden = rec && verdict(rec, p).availability === "hidden";
                  return (
                    <li key={n} className={hidden ? "dim" : ""}>
                      <span className="zw-kind" title={KIND[i.kind].label}><Icon name={KIND[i.kind].icon} size={16} className="ic-inline" /> {KIND[i.kind].label}</span>{" "}
                      {i.text}{rec && !hidden && <> · <a href={href(`/recette/${rec.id}`)}>{rec.title.split(" (")[0]}</a></>}
                      {hidden && <span className="meta"> (recette liée non adaptée à ton foyer)</span>}
                    </li>
                  );
                })}
              </ul>
              {!pt.part.match(/coquille|peau|carapace|eau de cuisson|huile|graines|chutes/) && (
                added.includes(`${lo.ref}|${pt.part}`)
                  ? <p className="small"><Icon name="check" size={16} className="ic-inline" /> Ajouté à ton frigo (date limite à 3 jours, modifiable) : il sera proposé en priorité dans « Avec ce que j'ai ».</p>
                  : <button className="btn small ghost" onClick={() => toFridge(lo.ref, pt.part)}>Ajouter le reste à mon frigo</button>
              )}
            </div>
          ))}
        </details>
      ))}
    </div>
  );
}
