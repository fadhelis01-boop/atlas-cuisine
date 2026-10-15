import { ImportRow } from "../components/video";
import { useState } from "react";
import { useImportLibrary, RECIPES, RECIPE_BY_ID } from "../lib/data";
import { FETES, PAR_CONVIVE } from "../lib/content";
import { go, href } from "../lib/router";
import { Grid, Page, RecipeCard, Section, useVisible } from "../components/ui";
import { Credit, Photo, photoOf } from "../components/photo";

const FETE_PHOTO: Record<string, string> = {
  "Épiphanie": "epiphanie", "Chandeleur": "chandeleur", "Nouvel An chinois": "nouvel-an-chinois", "Saint-Valentin": "saint-valentin",
  "Ramadan, ftour et Aïd el-Fitr": "ramadan", "Aïd el-Kébir (Tabaski)": "aid-kebir", "Pâques": "paques", "Fête des mères et des pères": "fete-meres",
  "Barbecue d'été et 14 juillet": "barbecue", "Halloween": "halloween", "Diwali": "diwali", "Noël et Nouvel An": "noel", "Anniversaire": "anniversaire", "Apéritif dînatoire": "aperitif",
};

export default function Fetes() {
  const IMPORT_LIBRARY = useImportLibrary();
  const [pick, setPick] = useState("");
  const plats = useVisible(RECIPES.filter((r) => r.role === "plat" || r.role === "entree" || r.role === "dessert"));
  const month = new Date().getMonth() + 1;
  const sorted = [...FETES].sort((a, b) => ((a.month ?? 13) - month + 12) % 12 - ((b.month ?? 13) - month + 12) % 12);
  const tiktok = IMPORT_LIBRARY.filter((i) => i.fete);
  return (
    <Page photo="rubrique/fetes" title="Repas de fêtes" sub="Le calendrier des fêtes d'ici et d'ailleurs, et un composeur de menu : choisis un plat, ATLAS complète entrée, plat, dessert et boissons." back="/explorer">
      <Section title="Composer un menu à partir d'un plat">
        <form className="row" onSubmit={(e) => { e.preventDefault(); if (pick) go(`/menu/${pick}`); }}>
          <label className="field grow">Je pars de…
            <select value={pick} onChange={(e) => setPick(e.target.value)} required>
              <option value="">Choisis un plat, une entrée ou un dessert</option>
              {(["plat", "entree", "dessert"] as const).map((role) => (
                <optgroup key={role} label={{ plat: "Plats", entree: "Entrées", dessert: "Desserts" }[role]}>
                  {plats.filter((r) => r.role === role).sort((a, b) => a.title.localeCompare(b.title, "fr")).map((r) => <option key={r.id} value={r.id}>{r.title}</option>)}
                </optgroup>
              ))}
            </select>
          </label>
          <button className="btn" type="submit">Composer</button>
        </form>
      </Section>
      <Section title="Calendrier des fêtes">
        {sorted.map((f) => {
          const recs = f.ideas.map((id) => RECIPE_BY_ID[id]).filter(Boolean);
          const tagged = RECIPES.filter((r) => r.fetes.includes(f.tag) && !f.ideas.includes(r.id));
          return (
            <details key={f.name} className="card pad fete">
              <summary><strong>🎉 {f.name}</strong> <span className="meta">· {f.when}</span></summary>
              {photoOf(`fete/${FETE_PHOTO[f.name]}`) && <figure className="hero-fig"><div className="photo-band"><Photo k={`fete/${FETE_PHOTO[f.name]}`} alt="" sizes="(min-width: 900px) 1000px, 100vw" /></div><figcaption><Credit k={`fete/${FETE_PHOTO[f.name]}`} note={false} /></figcaption></figure>}
              <p>{f.traditions}</p>
              <Grid>{[...recs, ...tagged].slice(0, 8).map((r) => <RecipeCard key={r.id} r={r} />)}</Grid>
            </details>
          );
        })}
      </Section>
      <Section title="Combien prévoir par convive ?">
        <table className="table"><tbody>{PAR_CONVIVE.map(([a, b]) => <tr key={a}><th>{a}</th><td>{b}</td></tr>)}</tbody></table>
        <p className="small">Repères de départ pour acheter juste (zéro déchet). Prévois toujours une option sans porc, sans alcool et végétarienne quand tu ne connais pas tous tes invités.</p>
      </Section>
      {tiktok.length > 0 && <Section title="Idées de fêtes dans tes favoris"><ul className="links-list">{tiktok.map((i) => <ImportRow key={i.url} i={i} />)}</ul></Section>}
      <p className="small">Les fêtes religieuses à date lunaire (Ramadan, Aïd, Nouvel An chinois…) changent chaque année : vérifie la date. <a href={href("/explorer")}>Retour à l'atlas</a></p>
    </Page>
  );
}
