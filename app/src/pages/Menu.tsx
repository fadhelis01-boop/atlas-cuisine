import { Icon } from "../components/icons";
import { useMemo, useState } from "react";
import { RECIPE_BY_ID } from "../lib/data";
import { composeMenus } from "../lib/menu";
import { consolidate, prepAhead } from "../lib/planner";
import { norm } from "../lib/text";
import { href } from "../lib/router";
import { setState, uid, useProfile } from "../lib/store";
import { minutes } from "../lib/text";
import { EVIN } from "../lib/content";
import { Cover, Page } from "../components/ui";

const ROLE: Record<string, string> = { entree: "Entrée", plat: "Plat", autre: "Fromage", dessert: "Dessert" };

const FREEZE = /congel/;
/** Ce qui se prépare la veille ou se congèle, pour un menu donné (audit 🟠 5). */
function Ahead({ ids }: { ids: string[] }) {
  const { tasks } = prepAhead(ids);
  const frozen = ids.map((id) => RECIPE_BY_ID[id]).filter((r) => FREEZE.test(norm(r.storage)) && !/ne se congele pas|pas de congel/.test(norm(r.storage)));
  if (!tasks.length && !frozen.length) return null;
  return (
    <div className="small ahead">
      {tasks.length > 0 && <p><strong><Icon name="calendar" size={15} className="ic-inline" /> La veille :</strong> {tasks.map((t) => `${t.recipe} (${t.task.split(/[.;:]/)[0].toLowerCase()})`).join(" ; ")}.</p>}
      {frozen.length > 0 && <p><strong><Icon name="snowflake" size={15} className="ic-inline" /> Se congèle (à faire jusqu'à 1 mois avant) :</strong> {frozen.map((r) => r.title.split(" (")[0]).join(", ")}.</p>}
    </div>
  );
}

export default function MenuPage({ id }: { id: string }) {
  const p = useProfile();
  const anchor = RECIPE_BY_ID[id];
  const menus = useMemo(() => (anchor ? composeMenus(id, p) : []), [id, p, anchor]);
  const [guests, setGuests] = useState(anchor?.portions ?? 4);
  const [msg, setMsg] = useState("");
  if (!anchor) return <Page title="Plat introuvable" back="/fetes">{null}</Page>;
  const alcoholOk = p.adult && p.alcohol === "allowed";

  const adopt = (i: number) => {
    const m = menus[i];
    setState((s) => {
      s.menus.unshift({ id: uid(), name: `Menu ${m.name.toLowerCase()} autour de : ${anchor.title}`, recipeIds: m.courses.map((c) => c.recipe.id), drinks: m.drinks.sa, date: new Date().toISOString(), guests });
      const from = `Menu : ${anchor.title.split(" (")[0]}`;
      s.shopping = s.shopping.filter((i) => i.from !== from);
      for (const l of consolidate(m.courses.map((c) => ({ id: c.recipe.id, factor: guests / c.recipe.portions })))) {
        s.shopping.push({ id: uid(), ref: l.ref, label: l.label, from, done: false, section: l.section });
      }
    });
    setMsg(`Menu enregistré dans Mes recettes ; les courses sont calculées pour ${guests} convives, produits communs regroupés.`);
  };

  return (
    <Page title="Compléter le menu" sub={<>À partir de <a href={href(`/recette/${id}`)}>{anchor.title}</a> : trois propositions, adaptées à ton foyer, qui partagent leurs ingrédients pour ne rien gaspiller.</>} back={`/recette/${id}`}>
      <label className="field inline">Convives <input type="number" min={1} max={40} value={guests} onChange={(e) => setGuests(Math.max(1, +e.target.value))} /></label>
      {msg && <p role="status" className="banner info">{msg} <a href={href("/courses")}>Courses</a> · <a href={href("/biblio")}>Mes recettes</a></p>}
      <div className="menus">
        {menus.map((m, i) => (
          <article key={m.name} className="card pad menu">
            <h2>{m.name}</h2>
            <ol className="courses">
              {m.courses.map((c) => (
                <li key={c.role}>
                  <a href={href(`/recette/${c.recipe.id}`)} className="course">
                    <Cover r={c.recipe} />
                    <span><span className="meta">{ROLE[c.role]}</span><br /><strong>{c.recipe.title}</strong>{c.adapted && <span className="meta"> · version adaptée</span>}</span>
                  </a>
                </li>
              ))}
            </ol>
            <p className="meta">Temps de préparation cumulé : {minutes(m.activeTotal)}</p>
            {m.zeroWaste.length > 0 && <p className="small"><Icon name="recycle" size={16} className="ic-inline" /> {m.zeroWaste.join(" ; ")}.</p>}
            {m.reasons.length > 0 && <p className="small">Pourquoi : {m.reasons.join(", ")}.</p>}
            <div className="drinks">
              <p><strong><Icon name="drink" size={16} className="ic-inline" /> Boissons sans alcool :</strong> {m.drinks.sa.join(", ")}.</p>
              {alcoholOk && m.drinks.a.length > 0 && <p><strong><Icon name="wine" size={16} className="ic-inline" /> Avec alcool (adultes) :</strong> {m.drinks.a.join(", ")}. <span className="small">{EVIN}</span></p>}
              <p className="small">{m.drinks.why}</p>
            </div>
            <Ahead ids={m.courses.map((c) => c.recipe.id)} />
            <button className="btn" onClick={() => adopt(i)}>Adopter ce menu (courses pour {guests})</button>
          </article>
        ))}
      </div>
      {guests >= 10 && (
        <p className="banner warn small"><strong>Grande tablée ({guests} personnes).</strong> Les quantités se multiplient, pas les temps de cuisson ni la taille des casseroles :
          au-delà de 2 fois la recette, cuis en plusieurs fois ou en plusieurs cocottes ; une grosse pièce (rôti, gigot) se cuit au thermomètre, pas à la montre ;
          les épices et le sel s'ajustent à la fin, en goûtant (ils ne se multiplient pas tout à fait). Compte 1 grande assiette par personne et prévois la place au frigo la veille.</p>
      )}
      <h2 className="h3">Rétro-planning conseillé</h2>
      <ul>
        <li><strong>J-2 :</strong> courses ; prépare les sauces, les pâtes à pain et les bases qui se gardent (bouillon, pâte brisée).</li>
        <li><strong>J-1 :</strong> les plats mijotés (meilleurs réchauffés), les desserts qui prennent au froid (mousse, tiramisu), les entrées froides.</li>
        <li><strong>Jour J :</strong> les cuissons minute ; un seul plat à très haute température au four à la fois.</li>
      </ul>
    </Page>
  );
}
