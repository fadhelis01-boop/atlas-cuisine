import { ImportRow, PlayButton } from "../components/video";
import { Photo, photoOf } from "../components/photo";
import { IMPORT_LIBRARY, RECIPES } from "../lib/data";
import { TECH_BY_ID, TECHNIQUES, techniqueFor, youtubeSearch } from "../lib/techniques";
import { href } from "../lib/router";
import { search } from "../lib/text";
import { Grid, Page, RecipeCard, Section } from "../components/ui";

export function TechniquesPage() {
  const families = [...new Set(TECHNIQUES.map((t) => t.family))];
  const tiktok = IMPORT_LIBRARY.filter((i) => i.cat === "techniques");
  return (
    <Page photo="rubrique/techniques" title="Techniques de cuisine" sub="Les gestes de base, pas à pas, avec les erreurs à éviter et une solution sans équipement spécial." back="/explorer">
      {families.map((f) => (
        <Section key={f} title={f}>
          <div className="tech-list">
            {TECHNIQUES.filter((t) => t.family === f).map((t) => (
              <a key={t.id} href={href(`/technique/${t.id}`)} className="card pad tech">
                {photoOf(`technique/${t.id}`) && <div className="thumb43"><Photo k={`technique/${t.id}`} alt="" sizes="(min-width: 900px) 300px, 100vw" /></div>}
                <strong>{t.name}</strong>
                <span className="meta">Niveau {t.level} · {t.why}</span>
              </a>
            ))}
          </div>
        </Section>
      ))}
      {tiktok.length > 0 && (
        <Section title="Astuces et techniques de tes favoris TikTok">
          <ul className="links-list">{tiktok.map((i) => <ImportRow key={i.url} i={i} />)}</ul>
        </Section>
      )}
    </Page>
  );
}

export function TechniquePage({ id }: { id: string }) {
  const t = TECH_BY_ID[id];
  if (!t) return <Page title="Technique introuvable" back="/techniques">{null}</Page>;
  const recipes = RECIPES.filter((r) => r.techniques.some((x) => techniqueFor(x)?.id === t.id));
  const vids = search(IMPORT_LIBRARY, t.keys.slice(0, 2).join(" "), (i) => [i.title], 6);
  return (
    <Page photo={`technique/${t.id}`} title={t.name} sub={t.why} back="/techniques">
      <p className="meta">{t.family} · Niveau {t.level}</p>
      <div className="card pad"><strong>Matériel :</strong> {t.gear}</div>
      <Section title="Pas à pas"><ol className="steps">{t.steps.map((s, i) => <li key={i}>{s}</li>)}</ol></Section>
      <Section title="Erreurs fréquentes"><ul>{t.errors.map((e) => <li key={e}>{e}</li>)}</ul></Section>
      {t.noGear && <Section title="Sans équipement spécial"><p>{t.noGear}</p></Section>}
      <Section title="Voir le geste">
        <p className="small">Démonstrations ATLAS à tourner (Tome 6). En attendant :</p>
        <div className="links">
          <a className="pill" href={youtubeSearch(t.query)} target="_blank" rel="noopener noreferrer">▶ Vidéos YouTube</a>
          {vids.map((x) => <PlayButton key={x.url} v={x} label={x.title.slice(0, 50)} />)}
        </div>
      </Section>
      {recipes.length > 0 && <Section title="Recettes pour pratiquer"><Grid>{recipes.map((r) => <RecipeCard key={r.id} r={r} />)}</Grid></Section>}
    </Page>
  );
}
