import { Icon } from "../components/icons";
import { useMemo, useState } from "react";
import { RECIPE_BY_ID } from "../lib/data";
import { href } from "../lib/router";
import { setState, useProfile, useStore } from "../lib/store";
import { toast } from "../lib/toast";
import { COURSES, RESTES, RESTE_BY_ID, buildMenu, ideasFor, resteStatus, type Course, type IdeeReste, type Reste } from "../lib/restes";
import { Chip, Page, Section } from "../components/ui";

// Cuisine des restes : je coche ce qu'il me reste (cuit ou entamé), ATLAS propose entrée, plat, sandwich, dessert,
// ou compose un menu complet qui les réunit. Les restes enregistrés affichent leur délai de conservation.
const GROUPS: [Reste["group"], string][] = [["viande", "Viandes"], ["poisson", "Poisson"], ["feculent", "Riz, pâtes, pommes de terre, légumineuses"],
  ["legume", "Légumes"], ["pain", "Pains"], ["oeuf", "Œufs"], ["laitier", "Fromages et laitages"], ["fruit", "Fruits"], ["sucre", "Sucré"], ["base", "Bouillons et sauces"]];

const NONE: { id: string; cooked: string }[] = [];

function IdeaRow({ i }: { i: IdeeReste }) {
  const rec = i.recipe ? RECIPE_BY_ID[i.recipe] : null;
  return (
    <li className="reste-idea">
      <strong>{i.title}</strong> <span className="meta">· {i.minutes} min</span>
      <p>{i.how}</p>
      {rec ? <a className="pill" href={href(`/recette/${rec.id}`)}>Voir la fiche : {rec.title.split(" (")[0]}</a>
        : <span className="small">Idée de cuisinier, pas encore testée dans la cuisine d'ATLAS.</span>}
    </li>
  );
}

export default function Restes({ preset }: { preset: string | null }) {
  const p = useProfile();
  const saved = useStore((s) => s.restes) ?? NONE;
  const [sel, setSel] = useState<string[]>(() => (preset ?? "").split(",").filter((id) => RESTE_BY_ID[id]));
  const [course, setCourse] = useState<Course | "menu" | "tout">(sel.length > 1 ? "menu" : "tout");
  const visible = RESTES.filter((r) => !(p.vegetarian && r.flesh));
  const toggle = (id: string) => setSel((s) => (s.includes(id) ? s.filter((x) => x !== id) : [...s, id]));
  const menu = useMemo(() => (course === "menu" && sel.length ? buildMenu(sel, p) : null), [course, sel, p]);
  const keep = (id: string) => {
    setState((s) => { s.restes = [...(s.restes ?? []).filter((x) => x.id !== id), { id, cooked: new Date().toISOString().slice(0, 10) }]; });
    toast(`${RESTE_BY_ID[id].name.split(" (")[0]} : noté, cuit aujourd'hui.`);
  };
  const drop = (id: string) => setState((s) => { s.restes = (s.restes ?? []).filter((x) => x.id !== id); });

  return (
    <Page photo="rubrique/zero_dechet" title="Cuisine des restes" back="/zero-dechet"
      sub="Coche ce qu'il te reste, cuit ou entamé : ATLAS propose une entrée, un plat, un sandwich, un dessert, ou compose un menu complet avec.">
      {saved.length > 0 && (
        <Section title="Mes restes au frigo">
          <ul className="restes-saved">
            {saved.map((x) => {
              const r = RESTE_BY_ID[x.id]; if (!r) return null;
              const st = resteStatus(x.id, x.cooked);
              return (
                <li key={x.id} className={`reste-saved ${st.level}`}>
                  <button className="link" onClick={() => setSel((s) => (s.includes(x.id) ? s : [...s, x.id]))}>{r.name}</button>
                  <span className="meta"> · {st.age === 0 ? "cuit aujourd'hui" : st.age === 1 ? "cuit hier" : `cuit il y a ${st.age} jours`} · </span>
                  {st.level === "jeter" ? <strong className="warn"><Icon name="alert" size={16} className="ic-inline" /> Dépassé : à jeter</strong>
                    : st.level === "bientot" ? <strong>À manger aujourd'hui</strong>
                    : <span>encore {st.left} jour{st.left > 1 ? "s" : ""}</span>}
                  <button className="btn small ghost" onClick={() => drop(x.id)} aria-label={`Retirer ${r.name}`}>Fini</button>
                </li>
              );
            })}
          </ul>
        </Section>
      )}

      <Section title="Qu'est-ce qu'il te reste ?">
        {GROUPS.map(([g, label]) => {
          const list = visible.filter((r) => r.group === g);
          if (!list.length) return null;
          return (
            <div key={g} className="reste-group">
              <h3 className="small">{label}</h3>
              <div className="chips">{list.map((r) => <Chip key={r.id} on={sel.includes(r.id)} onClick={() => toggle(r.id)}>{r.name}</Chip>)}</div>
            </div>
          );
        })}
      </Section>

      {sel.length > 0 && (
        <>
          <div className="chips" role="group" aria-label="Que veux-tu préparer ?">
            <Chip on={course === "tout"} onClick={() => setCourse("tout")}>Toutes les idées</Chip>
            {COURSES.map((c) => <Chip key={c.id} on={course === c.id} onClick={() => setCourse(c.id)}><Icon name={c.icon} size={16} className="ic-inline" /> {c.label}</Chip>)}
            <Chip on={course === "menu"} onClick={() => setCourse("menu")}><Icon name="plate" size={16} className="ic-inline" /> Menu complet</Chip>
          </div>

          {menu && (
            <Section title="Ton menu avec les restes">
              {(["entree", "plat", "dessert"] as const).map((k) => {
                const m = menu[k];
                const label = COURSES.find((c) => c.id === k)!.label;
                if (m) return <div key={k} className="card pad menu-course"><h3>{label} <span className="meta">· avec : {m.reste.name.split(" (")[0].toLowerCase()}</span></h3><ul className="reste-ideas"><IdeaRow i={m.idea} /></ul></div>;
                if (k === "dessert" && menu.fallback) return <div key={k} className="card pad menu-course"><h3>{label} <span className="meta">· sans reste sucré, un dessert minute du placard</span></h3><a className="pill" href={href(`/recette/${menu.fallback.id}`)}>{menu.fallback.title}</a></div>;
                return <div key={k} className="card pad menu-course"><h3>{label}</h3><p className="small">Aucun de tes restes ne s'y prête : coche-en un autre, ou garde ce service simple (crudités, fruit, yaourt).</p></div>;
              })}
              <p className="small">Le menu met un reste différent dans chaque service quand c'est possible, et préfère les idées qui en utilisent plusieurs à la fois.</p>
            </Section>
          )}

          {course !== "menu" && sel.map((id) => {
            const r = RESTE_BY_ID[id];
            const ideas = ideasFor(r, p, course === "tout" ? undefined : course);
            return (
              <Section key={id} title={r.name}>
                <div className="card pad reste-keep">
                  <p><Icon name="snowflake" size={16} className="ic-inline" /> <strong>Conservation :</strong> {r.keep}</p>
                  {r.safety && <p><Icon name="alert" size={16} className="ic-inline" /> <strong>Sécurité :</strong> {r.safety}</p>}
                  {!saved.some((x) => x.id === id) && <button className="btn small ghost" onClick={() => keep(id)}>Je le garde : cuit aujourd'hui</button>}
                </div>
                {ideas.length ? <ul className="reste-ideas">{ideas.map((i) => <IdeaRow key={i.title} i={i} />)}</ul>
                  : <p className="small">Pas d'idée {course !== "tout" ? `en ${COURSES.find((c) => c.id === course)?.label.toLowerCase()} ` : ""}adaptée à ton foyer pour ce reste{course !== "tout" ? " : essaie un autre service" : ""}.</p>}
              </Section>
            );
          })}
        </>
      )}

      <Section title="Pour aller plus loin">
        <p>Choisir des produits qui durent, rattraper un fruit trop mûr ou une viande dure : <a href={href("/bien-choisir")}>le guide Bien choisir, bien rattraper</a>. Épluchures, fanes, carcasses : <a href={href("/zero-dechet")}>Zéro déchet</a>.</p>
      </Section>
    </Page>
  );
}
