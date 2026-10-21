import { Icon } from "../components/icons";
import { aTester, PROTOCOLE } from "../lib/aTester";
import { RECIPE_BY_ID } from "../lib/data";
import { href } from "../lib/router";
import { setState, useStore } from "../lib/store";
import { Empty, Grid, Page, RecipeCard, Section } from "../components/ui";

export default function Biblio() {
  const favs = useStore((s) => s.favorites).map((id) => RECIPE_BY_ID[id]).filter(Boolean);
  const menus = useStore((s) => s.menus);
  const imports = useStore((s) => s.imports);
  const cooked = useStore((s) => s.cooked);
  const journal = useStore((s) => s.journal) ?? {};
  const tried = Object.entries(journal).sort((a, b) => b[1].date.localeCompare(a[1].date)).filter(([id]) => RECIPE_BY_ID[id]);
  const exportTests = () => {
    // Protocole de test (audit 🔴 1) : un fichier texte à renvoyer pour corriger les fiches dans la bible
    const lines = ["# Essais en cuisine — carnet ATLAS", `Exporté le ${new Date().toLocaleDateString("fr-FR")} · ${tried.length} recette(s)`, "",
      "| Recette | Identifiant | Note /5 | Fois | Date | Ce qu'il faut changer |", "|---|---|---|---|---|---|",
      ...tried.map(([id, e]) => `| ${RECIPE_BY_ID[id].title} | ${id} | ${e.rating || "-"} | ${cooked[id] ?? 0} | ${new Date(e.date).toLocaleDateString("fr-FR")} | ${e.note.replace(/[|\n]/g, " ") || "-"} |`)];
    const url = URL.createObjectURL(new Blob([lines.join("\n") + "\n"], { type: "text/markdown" }));
    const a = document.createElement("a"); a.href = url; a.download = `atlas-essais-${new Date().toISOString().slice(0, 10)}.md`; a.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  const prio = aTester();
  const cookedList = Object.entries(cooked).sort((a, b) => b[1] - a[1]).map(([id, n]) => ({ r: RECIPE_BY_ID[id], n })).filter((x) => x.r);
  return (
    <Page title="Mes recettes" sub="Favoris, carnet, menus, imports et recettes déjà cuisinées.">
      <Section title={`Favoris (${favs.length})`}>
        {favs.length ? <Grid>{favs.map((r) => <RecipeCard key={r.id} r={r} />)}</Grid> : <Empty>Touche « Garder » sur une recette pour la retrouver ici.</Empty>}
      </Section>
      <p><a className="btn ghost" href={href("/semaine")}><Icon name="calendar" size={20} /> Ma semaine : menus et courses</a></p>
      <Section title={`Mon carnet d'essais (${tried.length})`} more={tried.length ? <button className="btn small ghost" onClick={exportTests}>Exporter</button> : undefined}>
        <p className="small">Les recettes d'ATLAS n'ont pas encore été testées en cuisine. Après chaque essai, note-la sur 5 et écris ce qu'il faut changer
          (sel, temps, quantités, ordre des gestes) : l'export produit un tableau à renvoyer pour corriger les fiches.</p>
        {tried.length ? <ul>{tried.map(([id, e]) => <li key={id}><a href={href(`/recette/${id}`)}>{RECIPE_BY_ID[id].title}</a> <span className="meta">· {e.rating ? "★".repeat(e.rating) : "sans note"} · {new Date(e.date).toLocaleDateString("fr-FR")}</span>{e.note && <><br /><span className="small">{e.note}</span></>}</li>)}</ul>
          : <Empty>Après avoir cuisiné (mode cuisine, dernière étape) ou sur une fiche, remplis « Mon carnet ».</Empty>}
      </Section>
      <Section title={`À tester en priorité (${prio.filter((r) => journal[r.id]).length}/${prio.length})`}>
        <p className="small">Les 30 plats que « Ma semaine » propose le plus souvent. Les essayer d'abord corrige les fiches qui servent le plus.</p>
        <ol className="small">{PROTOCOLE.map((t) => <li key={t}>{t}</li>)}</ol>
        <ul className="links-list">{prio.map((r) => <li key={r.id}><a href={href(`/recette/${r.id}`)}>{r.title}</a>{" "}
          {journal[r.id] ? <span className="ok-text">· essayé{journal[r.id].rating ? ` (${journal[r.id].rating}/5)` : ""}</span> : <span className="meta">· à essayer</span>}</li>)}</ul>
      </Section>
      <Section title={`Menus (${menus.length})`}>
        {menus.length ? menus.map((m) => (
          <div key={m.id} className="card pad">
            <strong>{m.name}</strong> <span className="meta">· {m.guests} convives · {new Date(m.date).toLocaleDateString("fr-FR")}</span>
            <div className="links">{m.recipeIds.map((id) => RECIPE_BY_ID[id] && <a key={id} className="pill" href={href(`/recette/${id}`)}>{RECIPE_BY_ID[id].title}</a>)}</div>
            <p className="small">Boissons : {m.drinks.join(", ")}</p>
            <button className="btn small ghost danger" onClick={() => setState((s) => { s.menus = s.menus.filter((x) => x.id !== m.id); })}>Supprimer</button>
          </div>
        )) : <Empty>Compose un menu depuis une recette (« Pour recevoir » en bas de fiche) ou la rubrique <a href={href("/fetes")}>Fêtes</a>.</Empty>}
      </Section>
      <Section title={`Mes imports (${imports.length})`} more={<a href={href("/imports")}>Gérer →</a>}>
        {imports.length ? <ul className="links-list">{imports.slice(0, 10).map((i) => <li key={i.id}><a href={i.url} target="_blank" rel="noopener noreferrer">{i.title}</a></li>)}</ul> : <Empty>Importe tes recettes TikTok, Instagram ou YouTube depuis <a href={href("/imports")}>Mes imports</a>.</Empty>}
      </Section>
      {cookedList.length > 0 && (
        <Section title="Déjà cuisinées">
          <ul>{cookedList.map(({ r, n }) => <li key={r.id}><a href={href(`/recette/${r.id}`)}>{r.title}</a> <span className="meta">· {n} fois</span></li>)}</ul>
        </Section>
      )}
    </Page>
  );
}
