import { useMemo, useState } from "react";
import { INGREDIENTS, RECIPE_BY_ID } from "../lib/data";
import { composeMenus } from "../lib/menu";
import { flatten } from "../lib/engine";
import { href } from "../lib/router";
import { setState, uid, useProfile } from "../lib/store";
import { minutes } from "../lib/text";
import { EVIN } from "../lib/content";
import { Cover, Page } from "../components/ui";

const ROLE: Record<string, string> = { entree: "Entrée", plat: "Plat", dessert: "Dessert" };

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
      for (const c of m.courses) {
        for (const l of flatten(c.recipe.ingredients)) {
          if (!l.ref) continue;
          s.shopping.push({ id: uid(), ref: l.ref, label: `${l.qty} ${l.label} (pour ${c.recipe.portions}, à adapter à ${guests})`, from: c.recipe.title, done: false, section: INGREDIENTS[l.ref]?.section ?? "Autres" });
        }
      }
    });
    setMsg("Menu enregistré dans Ma biblio ; les ingrédients sont dans la liste de courses.");
  };

  return (
    <Page title="Compléter le menu" sub={<>À partir de <a href={href(`/recette/${id}`)}>{anchor.title}</a> : trois propositions, adaptées à ton foyer, qui partagent leurs ingrédients pour ne rien gaspiller.</>} back={`/recette/${id}`}>
      <label className="field inline">Convives <input type="number" min={1} max={40} value={guests} onChange={(e) => setGuests(Math.max(1, +e.target.value))} /></label>
      {msg && <p role="status" className="banner info">{msg} <a href={href("/courses")}>Courses</a> · <a href={href("/biblio")}>Ma biblio</a></p>}
      <div className="menus">
        {menus.map((m, i) => (
          <article key={m.name} className="card pad menu">
            <h2>{m.name}</h2>
            <ol className="courses">
              {m.courses.map((c) => (
                <li key={c.role}>
                  <a href={href(`/recette/${c.recipe.id}`)} className="course">
                    <Cover r={c.recipe} />
                    <span><span className="meta">{ROLE[c.role]}</span><br /><strong>{c.recipe.title}</strong>{c.adapted && <span className="meta"> · 🔄 version adaptée</span>}</span>
                  </a>
                </li>
              ))}
            </ol>
            <p className="meta">Temps de préparation cumulé : {minutes(m.activeTotal)}</p>
            {m.zeroWaste.length > 0 && <p className="small">♻️ {m.zeroWaste.join(" ; ")}.</p>}
            {m.reasons.length > 0 && <p className="small">Pourquoi : {m.reasons.join(", ")}.</p>}
            <div className="drinks">
              <p><strong>🥤 Boissons sans alcool :</strong> {m.drinks.sa.join(", ")}.</p>
              {alcoholOk && m.drinks.a.length > 0 && <p><strong>🍷 Avec alcool (adultes) :</strong> {m.drinks.a.join(", ")}. <span className="small">{EVIN}</span></p>}
              <p className="small">{m.drinks.why}</p>
            </div>
            <button className="btn" onClick={() => adopt(i)}>Adopter ce menu</button>
          </article>
        ))}
      </div>
      <h2 className="h3">Rétro-planning conseillé</h2>
      <ul>
        <li><strong>J-2 :</strong> courses ; prépare les sauces, les pâtes à pain et les bases qui se gardent (bouillon, pâte brisée).</li>
        <li><strong>J-1 :</strong> les plats mijotés (meilleurs réchauffés), les desserts qui prennent au froid (mousse, tiramisu), les entrées froides.</li>
        <li><strong>Jour J :</strong> les cuissons minute ; un seul plat à très haute température au four à la fois.</li>
      </ul>
    </Page>
  );
}
