import { RECIPE_BY_ID } from "../lib/data";
import { TECH_BY_ID } from "../lib/techniques";
import { href } from "../lib/router";
import { setState, useStore } from "../lib/store";
import { Grid, Page, RecipeCard, Section } from "../components/ui";
import { PARCOURS } from "../lib/parcours";


const NONE: string[] = [];

export default function Apprendre() {
  const cooked = useStore((s) => s.cooked);
  const learned = useStore((s) => s.learned) ?? NONE;
  const done = (st: (typeof PARCOURS)[number]) => learned.includes(st.id) || st.recipes.some((id) => (cooked[id] ?? 0) > 0);
  const n = PARCOURS.filter(done).length;
  const next = PARCOURS.find((s) => !done(s));
  const toggle = (id: string) => setState((s) => { s.learned = s.learned ?? []; s.learned = s.learned.includes(id) ? s.learned.filter((x) => x !== id) : [...s.learned, id]; });
  return (
    <Page title="J'apprends à cuisiner" sub="Quinze étapes, du couteau à la pâte à choux. À chaque étape : le geste expliqué pas à pas, puis une recette pour le pratiquer. Une étape se valide quand tu cuisines l'une de ses recettes (bouton « Cuisiner »), ou d'un clic." back="/explorer">
      <div className="card pad progress-card">
        <strong>{n} / {PARCOURS.length} étapes</strong>
        <div className="progress" role="progressbar" aria-valuemin={0} aria-valuemax={PARCOURS.length} aria-valuenow={n}><span style={{ width: `${(n / PARCOURS.length) * 100}%` }} /></div>
        {next ? <p className="small">Prochaine étape : <a href={`#etape-${next.id}`}>{next.title}</a></p> : <p className="small">Bravo, parcours terminé : passe aux <a href={href("/fetes")}>menus de fête</a> !</p>}
      </div>
      {PARCOURS.map((st, i) => (
        <Section key={st.id} id={`etape-${st.id}`} title={`${done(st) ? "✅" : `${i + 1}.`} ${st.title}`}>
          <p>{st.why}</p>
          <div className="links">{st.techs.map((t) => TECH_BY_ID[t] && <a key={t} className="pill" href={href(`/technique/${t}`)}>🔪 {TECH_BY_ID[t].name}</a>)}</div>
          <Grid>{st.recipes.map((id) => RECIPE_BY_ID[id] && <RecipeCard key={id} r={RECIPE_BY_ID[id]} />)}</Grid>
          <label className="switch"><input type="checkbox" checked={done(st)} onChange={() => toggle(st.id)} /> J'ai réussi cette étape</label>
        </Section>
      ))}
    </Page>
  );
}
