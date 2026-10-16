import { href } from "../lib/router";
import { setState, useStore } from "../lib/store";
import { toast } from "../lib/toast";
import { Empty, Page } from "../components/ui";

/** Liste de courses groupée par rayon (famille du référentiel), partageable (Tome 1 §6.4). */
export default function Courses() {
  const items = useStore((s) => s.shopping);
  const sections = [...new Set(items.map((i) => i.section))].sort();
  const text = sections.map((s) => `${s}\n${items.filter((i) => i.section === s && !i.done).map((i) => `- ${i.label}`).join("\n")}`).join("\n\n");
  const share = async () => {
    try {
      if (navigator.share) await navigator.share({ title: "Liste de courses ATLAS", text });
      else { await navigator.clipboard.writeText(text); alert("Liste copiée : colle-la dans Notes, Rappels ou un message."); }
    } catch { /* partage annulé */ }
  };
  return (
    <Page title="Liste de courses" sub="Ajoutée depuis les recettes et les menus. Coche en faisant les courses." back="/frigo">
      {!items.length ? <Empty>Ta liste est vide. Sur une recette, touche « Courses », ou prépare <a href={href("/semaine")}>ta semaine</a>.</Empty> : (
        <>
          <div className="row">
            <button className="btn" onClick={() => void share()}>Partager ou copier</button>
            <button className="btn ghost" onClick={() => setState((s) => { s.shopping = s.shopping.filter((i) => !i.done); })}>Retirer les articles cochés</button>
            <button className="btn ghost danger" onClick={() => { const before = items; setState((s) => { s.shopping = []; }); toast("Liste vidée", { undo: () => setState((s) => { s.shopping = before; }) }); }}>Tout vider</button>
          </div>
          <p className="small">Depuis « Ma semaine », les produits communs sont déjà regroupés et les quantités additionnées. Depuis une recette seule, les quantités sont celles de la fiche. Achète au plus juste pour ne rien jeter.</p>
          {sections.map((sec) => (
            <section key={sec} className="section">
              <h2 className="h3">{sec.split(" (")[0]}</h2>
              <ul className="shop">
                {items.filter((i) => i.section === sec).map((i) => (
                  <li key={i.id} className={i.done ? "done" : ""}>
                    <label>
                      <input type="checkbox" checked={i.done} onChange={() => setState((s) => { const x = s.shopping.find((y) => y.id === i.id); if (x) x.done = !x.done; })} />
                      <span>{i.label} <span className="meta">· {i.from}</span></span>
                    </label>
                  </li>
                ))}
              </ul>
            </section>
          ))}
        </>
      )}
    </Page>
  );
}
