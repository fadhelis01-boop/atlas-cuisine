import { useState } from "react";
import { ALLERGENS, RECIPES } from "../lib/data";
import { toTop } from "../lib/router";
import { setState, useProfile } from "../lib/store";
import { Icon } from "../components/icons";
import Household from "../components/Household";

/** Premier lancement en un seul écran (audit UX 2026-10-16, chantier 1) : l'essentiel d'un geste, les allergies
 *  seulement si on en a, et tout le reste (équipement, mode strict, âge des enfants) plus tard dans le profil. */
export default function Onboarding() {
  const p = useProfile();
  const [allergies, setAllergies] = useState(p.allergens.length > 0);
  const toggle = (fn: (s: typeof p) => void) => setState((s) => { fn(s.profile); });
  const done = () => { setState((s) => { s.profile.onboarded = true; }); toTop(); };
  const Choice = ({ on, label, sub, icon, onClick }: { on: boolean; label: string; sub: string; icon: string; onClick: () => void }) => (
    <button type="button" className={`ob-choice ${on ? "on" : ""}`} aria-pressed={on} onClick={onClick}>
      <Icon name={icon} size={28} /><span><strong>{label}</strong><br /><span className="small">{sub}</span></span>
      <span className="ob-check" aria-hidden="true">{on ? <Icon name="check" size={22} /> : null}</span>
    </button>
  );
  return (
    <main className="page onboarding" id="contenu" tabIndex={-1}>
      <img src="./icons/icon.svg" alt="" width="64" height="64" />
      <h1>Bienvenue dans ATLAS</h1>
      <p className="lead">{RECIPES.length} recettes du monde, faites maison. Une seule question pour commencer : <strong>qu'est-ce qu'on évite chez toi ?</strong></p>
      <div className="ob-choices">
        <Choice on={p.noPork} icon="pig" label="Sans porc" sub="ni lardons, ni saindoux, ni gélatine de porc" onClick={() => toggle((x) => { x.noPork = !x.noPork; })} />
        <Choice on={p.alcohol !== "allowed"} icon="wine" label="Sans alcool" sub="versions sans vin, sans bière, sans rhum" onClick={() => toggle((x) => { x.alcohol = x.alcohol === "allowed" ? "standard" : "allowed"; })} />
        <Choice on={p.vegetarian} icon="broccoli" label="Végétarien" sub="ni viande ni poisson" onClick={() => toggle((x) => { x.vegetarian = !x.vegetarian; })} />
        <Choice on={allergies} icon="alert" label="Des allergies" sub="on exclut les recettes concernées" onClick={() => setAllergies(!allergies)} />
      </div>
      {allergies && (
        <div className="chips ob-allergens" role="group" aria-label="Allergies à exclure">
          {Object.entries(ALLERGENS).map(([k, label]) => (
            <button key={k} type="button" className={`chip ${p.allergens.includes(k) ? "on" : ""}`} aria-pressed={p.allergens.includes(k)}
              onClick={() => toggle((x) => { x.allergens = x.allergens.includes(k) ? x.allergens.filter((a) => a !== k) : [...x.allergens, k]; })}>{label}</button>
          ))}
        </div>
      )}
      <h2 className="h3 ob-sub">Pour combien cuisines-tu ?</h2>
      <Household compact />
      <p className="small">Halal : choisis « sans porc » et « sans alcool ». Tout se change ensuite dans <strong>Profil</strong> (équipement, mode strict). Ces informations restent sur ton téléphone.</p>
      <button className="btn big ob-go" onClick={done}>Voir les recettes</button>
    </main>
  );
}
