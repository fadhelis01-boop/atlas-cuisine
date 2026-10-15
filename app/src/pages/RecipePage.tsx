import { SEASON_LABEL, seasonFit, seasonOf, zoneOf } from "../lib/season";
import { useEffect, useMemo, useState } from "react";
import { ALLERGENS, INGREDIENTS, MACRO_BY_ID, RECIPE_BY_ID } from "../lib/data";
import { evaluateLines, verdict } from "../lib/engine";
import { href } from "../lib/router";
import { pushRecent, setState, toggleFavorite, uid, useProfile, useStore } from "../lib/store";
import { durationsIn, minutes, plain, scaleQty } from "../lib/text";
import { speak, stopSpeaking, ttsAvailable } from "../lib/speech";
import { startTimer } from "../lib/timers";
import { techniqueFor, youtubeSearch } from "../lib/techniques";
import { PlayButton, embedOf, playVideo } from "../components/video";
import { Credit } from "../components/photo";
import Leftovers from "../components/Leftovers";
import type { Recipe } from "../lib/types";
import { ACCORDS, EVIN, SECURITE_ENFANTS } from "../lib/content";
import { Cover, DietBadges, Page, Section } from "../components/ui";
import type { RecipeLine } from "../lib/types";

export function Rich({ text }: { text: string }) {
  // **gras** → <strong>
  const parts = text.split(/(\*\*[^*]+\*\*)/g);
  return <>{parts.map((p, i) => (p.startsWith("**") ? <strong key={i}>{p.slice(2, -2)}</strong> : <span key={i}>{p}</span>))}</>;
}

function SeasonBadge({ r }: { r: Recipe }) {
  const zone = zoneOf(useStore((st) => st.settings.zone));
  const f = seasonFit(r, zone);
  const s = seasonOf(zone);
  if (f.inSeason.length && f.score > 0) return <p className="meta season-ok">🌱 De saison ({SEASON_LABEL[s]}) : {f.inSeason.slice(0, 4).join(", ").toLowerCase()}</p>;
  if (f.outSeason.length) return <p className="meta season-out">🕰️ Hors saison ici en ce moment : {f.outSeason.slice(0, 3).join(", ").toLowerCase()} (surgelés ou conserves de qualité conviennent souvent).</p>;
  return null;
}

export default function RecipePage({ id, q }: { id: string; q: URLSearchParams }) {
  const r = RECIPE_BY_ID[id];
  const p = useProfile();
  const fav = useStore((s) => s.favorites.includes(id));
  const [portions, setPortions] = useState(r?.portions ?? 4);
  const [useAdapted, setUseAdapted] = useState(true);
  const [reading, setReading] = useState<number | null>(null);
  const [showAnyway, setShowAnyway] = useState(q.get("voir") === "1");
  const [msg, setMsg] = useState("");
  useEffect(() => { if (r) { pushRecent(r.id); setPortions(r.portions); } return () => { stopSpeaking(); }; }, [id]); // eslint-disable-line react-hooks/exhaustive-deps
  const v = useMemo(() => (r ? verdict(r, p) : null), [r, p]);
  if (!r || !v) return <Page title="Recette introuvable" back="/explorer">{null}</Page>;

  const adapted = v.availability === "adaptable" && useAdapted ? v.adapted : null;
  const lines: RecipeLine[] = adapted ? adapted.lines : r.ingredients;
  const factor = portions / r.portions;
  const ev = evaluateLines(lines);
  const kidsAlert = p.kidsAge !== null && r.age !== null && p.kidsAge < r.age;
  const showAlcoholDrinks = p.adult && p.alcohol === "allowed";
  const prof = r.profile.find((x) => ACCORDS[x]);

  const read = (mode: "tout" | "resume") => {
    if (reading !== null) { stopSpeaking(); setReading(null); return; }
    const parts = mode === "resume"
      ? [`${r.title}. ${plain(r.intro)}`, `Pour ${portions} personnes, ${minutes(r.active)} de préparation${r.rest ? ` et ${minutes(r.rest)} de cuisson ou de repos` : ""}.`, `Matériel : ${r.equipment}`]
      : [r.title, plain(r.intro), `Ingrédients pour ${portions} personnes.`, ...lines.map((l) => `${scaleQty(l.qty, factor)} ${l.label}`), "Étapes.", ...r.steps.map((s, i) => `Étape ${i + 1}. ${s}`)];
    setReading(0);
    speak(parts, { onIndex: (i) => setReading(i), onEnd: () => setReading(null) });
  };

  const addToShopping = () => {
    setState((s) => {
      for (const l of lines) {
        if (!l.ref || l.ref.startsWith("SUB:")) continue;
        if (s.shopping.some((x) => x.ref === l.ref && !x.done && x.from === r.title)) continue;
        s.shopping.push({ id: uid(), ref: l.ref, label: `${scaleQty(l.qty, factor)} ${l.label}`.trim(), from: r.title, done: false, section: INGREDIENTS[l.ref]?.section ?? "Autres" });
      }
    });
    setMsg("Ingrédients ajoutés à la liste de courses.");
  };

  if (v.availability === "hidden" && !showAnyway) {
    return (
      <Page title={r.title} back="/explorer">
        <div className="banner bad" role="alert">
          <strong>Cette recette ne convient pas à ton foyer</strong> : {v.reasons.join(", ")}. Aucune substitution fiable n'existe encore pour cette fiche.
        </div>
        <button className="btn ghost" onClick={() => setShowAnyway(true)}>Voir la recette quand même</button>
        <a className="btn" href={href(`/region/${r.macro}`)}>Voir des plats proches de la même région</a>
      </Page>
    );
  }

  return (
    <main className="page recipe" id="contenu">
      <a className="back" href={href(`/region/${r.macro}`)}>← {MACRO_BY_ID[r.macro]?.name}</a>
      <div className="recipe-head">
        <figure className="hero-fig"><Cover r={r} big /><figcaption><Credit k={`recette/${r.id}`} /></figcaption></figure>
        <div>
          <h1>{r.title}</h1>
          {r.origin && r.origin !== r.title && <p className="origin" lang="und">{r.origin}</p>}
          <p className="meta">{r.regionPath.join(" › ")} · {r.kind}</p>
          {r.fusionNote && <p className="meta"><a href={href("/region/fusion")}>🌐 Food fusion</a> : {r.fusionNote}</p>}
          {r.videos.some((x) => x.embed) && <button className="btn ghost small" onClick={() => { const x = r.videos.find((y) => y.embed)!; playVideo(x); }}>▶ Voir la vidéo</button>}
          <p className="meta">⏱ {minutes(r.active)} de préparation{r.rest ? ` + ${minutes(r.rest)} (cuisson / repos)` : ""} · Niveau {r.level} · {r.cost}</p>
          <DietBadges r={r} v={v} lines={adapted ? lines : undefined} />
          <SeasonBadge r={r} />
          <div className="row actions">
            <a className="btn" href={href(`/cuisine/${r.id}${adapted ? "?adapte=1" : ""}`)}>▶ Cuisiner</a>
            {ttsAvailable() && <button className="btn ghost" onClick={() => read("tout")} aria-pressed={reading !== null}>{reading !== null ? "⏹ Arrêter" : "🔊 Écouter"}</button>}
            {ttsAvailable() && reading === null && <button className="btn ghost" onClick={() => read("resume")}>🔊 Résumé</button>}
            <button className="btn ghost" onClick={addToShopping}>🛒 Courses</button>
            <a className="btn ghost" href={href(`/menu/${r.id}`)}>🍽 Compléter le menu</a>
            <button className={`btn ghost ${fav ? "on" : ""}`} onClick={() => toggleFavorite(r.id)} aria-pressed={fav}>{fav ? "♥ Favori" : "♡ Favori"}</button>
          </div>
          {msg && <p role="status" className="small">{msg} <a href={href("/courses")}>Voir la liste</a></p>}
        </div>
      </div>

      {v.availability === "adaptable" && v.adapted && (
        <div className="banner info" role="region" aria-label="Version adaptée">
          <p><strong>La recette d'origine {v.reasons.join(", ")}.</strong> {useAdapted ? `Tu vois la version adaptée : ${v.adapted.variantName.toLowerCase()}.` : "Tu vois la recette d'origine."}</p>
          <div className="seg" role="group" aria-label="Choisir la version">
            <button className={useAdapted ? "on" : ""} aria-pressed={useAdapted} onClick={() => setUseAdapted(true)}>Version adaptée</button>
            <button className={!useAdapted ? "on" : ""} aria-pressed={!useAdapted} onClick={() => setUseAdapted(false)}>Recette d'origine</button>
          </div>
          {useAdapted && <ul>{v.adapted.notes.map((n, i) => <li key={i}><Rich text={n} /></li>)}</ul>}
          <p className="small">🧪 <strong>Substitution à tester</strong> : elle n'a pas encore passé la dégustation à l'aveugle (Tome 7 §3). Elle est vérifiée pour ton régime, pas encore pour le goût.</p>
          {v.adapted.newAllergens.length > 0 && <p className="warn-text">⚠️ Nouvel allergène dans la version adaptée : {v.adapted.newAllergens.map((a) => ALLERGENS[a]).join(", ")}.</p>}
        </div>
      )}
      {v.warnings.length > 0 && <div className="banner warn"><strong>À vérifier :</strong> {v.warnings.join(" · ")}. Lis les étiquettes.</div>}
      {kidsAlert && <div className="banner warn">👶 Recette conseillée à partir de {r.age} ans ; ton plus jeune a {p.kidsAge} an(s). {plain(r.kids)}</div>}

      <p className="intro"><Rich text={r.intro} /></p>
      <p className="small"><strong>Matériel :</strong> {r.equipment}</p>

      <div className="two-col">
        <Section title="Ingrédients">
          <div className="portions" role="group" aria-label="Nombre de portions">
            <button className="btn small ghost" onClick={() => setPortions(Math.max(1, portions - 1))} aria-label="Moins de portions">−</button>
            <span><strong>{portions}</strong> {r.role === "boisson" || r.kind === "Sauce" ? "portions" : "personnes"}</span>
            <button className="btn small ghost" onClick={() => setPortions(portions + 1)} aria-label="Plus de portions">+</button>
          </div>
          <ul className="ingredients">
            {lines.map((l, i) => (
              <li key={i} className={l.optional ? "opt" : ""}>
                <span className="qty">{scaleQty(l.qty, factor)}</span>{" "}
                {l.ref?.startsWith("SUB:") ? <a href={href(`/recette/${l.ref.slice(4)}`)}>{l.label}</a> : l.ref && INGREDIENTS[l.ref]?.slug ? <a className="ing-link" href={href(`/ingredient/${INGREDIENTS[l.ref].slug}`)} title={`${l.ref} : voir le dictionnaire`}>{l.label}</a> : l.label}
                {l.optional && <span className="meta"> (facultatif)</span>}
                {l.replaces && <span className="meta repl"> · remplace {l.replaces}</span>}
                {l.ref && INGREDIENTS[l.ref] && "🟠🔴".includes(INGREDIENTS[l.ref].dispo) && <span className="meta" title="Disponibilité en France"> · {INGREDIENTS[l.ref].dispo === "🟠" ? "épicerie spécialisée" : "difficile à trouver"}</span>}
              </li>
            ))}
          </ul>
          {ev.allergens.size > 0 && <p className="small"><strong>Allergènes :</strong> {[...ev.allergens].map((a) => ALLERGENS[a]).join(", ")}{ev.maybeAllergens.size > ev.allergens.size ? ` ; possibles selon la marque : ${[...ev.maybeAllergens].filter((a) => !ev.allergens.has(a)).map((a) => ALLERGENS[a]).join(", ")}` : ""}.</p>}
          <Leftovers r={r} />
        </Section>

        <Section title="Étapes">
          <ol className="steps">
            {r.steps.map((s, i) => (
              <li key={i}>
                <Rich text={s} />
                {durationsIn(s).length > 0 && (
                  <div className="timers-inline">
                    {durationsIn(s).filter((d, j, a) => a.findIndex((x) => x.label === d.label) === j).map((d, j) => <button key={j} className="chip" onClick={() => startTimer(`${r.title.split(" (")[0]} · étape ${i + 1}`, d.seconds, r.id)}>⏱ {d.label}</button>)}
                  </div>
                )}
              </li>
            ))}
          </ol>
        </Section>
      </div>

      {r.tips.length > 0 && <Section title="Astuces du chef"><ul>{r.tips.map((t, i) => <li key={i}><Rich text={t} /></li>)}</ul></Section>}
      {r.variants.length > 0 && (
        <Section title="Variantes et substitutions">
          {r.variants.map((x) => <div key={x.name} className="card pad"><h3>{x.name} {!x.tested && <span className="badge info">à tester</span>}</h3><p><Rich text={x.note} /></p></div>)}
        </Section>
      )}
      <Section title="Conservation"><p>{plain(r.storage)}</p></Section>
      <Section title="Enfants">
        <p>{plain(r.kids)}</p>
        {p.kidsAge !== null && p.kidsAge < 4 && <ul className="small">{SECURITE_ENFANTS.slice(0, 4).map((x) => <li key={x}>{x}</li>)}</ul>}
      </Section>
      <Section title="Boissons d'accompagnement">
        <div className="two-col">
          <div className="card pad"><h3>Sans alcool</h3><ul>{[...new Set([...r.drinksNoAlcohol, ...(prof ? ACCORDS[prof].sa : [])])].slice(0, 5).map((d) => <li key={d}>{d}</li>)}</ul></div>
          {showAlcoholDrinks && (r.drinksAlcohol.length > 0 || prof) && <div className="card pad"><h3>Avec alcool</h3><ul>{[...new Set([...r.drinksAlcohol, ...(prof ? ACCORDS[prof].a : [])])].slice(0, 3).map((d) => <li key={d}>{d}</li>)}</ul><p className="small">{EVIN}</p></div>}
        </div>
        {prof && <p className="small">{ACCORDS[prof].why}</p>}
      </Section>
      {r.techniques.length > 0 && (
        <Section title="Techniques utilisées">
          <div className="links">{r.techniques.map((t) => { const tf = techniqueFor(t); return tf ? <a key={t} className="pill" href={href(`/technique/${tf.id}`)}>🔪 {t}</a> : <span key={t} className="pill">{t}</span>; })}</div>
        </Section>
      )}
      <RecipeVideos r={r} />
      <p className="small source">Source : bible ATLAS, {r.source}. Fiche <strong>non testée en cuisine</strong> (Tome 7 §2) ; référentiel d'ingrédients niveau C. À tester : {r.tests}</p>
    </main>
  );
}

const NONE: string[] = [];

/** Vidéos liées à la fiche : favoris importés et vidéos des sites, lisibles dans l'appli ; + les liens ajoutés par l'utilisateur. */
function RecipeVideos({ r }: { r: Recipe }) {
  const mine = useStore((s) => s.recipeVideos[r.id]) ?? NONE; // jamais un nouveau tableau dans le sélecteur
  const [link, setLink] = useState("");
  const [err, setErr] = useState("");
  const add = () => {
    const u = link.trim();
    if (!/^https?:\/\//.test(u)) { setErr("Colle un lien qui commence par https://"); return; }
    setState((s) => { s.recipeVideos[r.id] = [...new Set([...(s.recipeVideos[r.id] ?? []), u])]; });
    setLink(""); setErr("");
  };
  return (
    <Section title="En vidéo">
      {r.videos.length > 0 ? (
        <ul className="links-list">
          {r.videos.map((x) => (
            <li key={x.url} className="import-row">
              <PlayButton v={x} />
              <span><a href={x.url} target="_blank" rel="noopener noreferrer">{x.title.slice(0, 90)}</a> <span className="meta">· {x.source === "TikTok" ? `@${x.author}` : x.source}{x.pork ? " · 🐖 version avec porc" : ""}{x.alcohol ? " · 🍷" : ""}</span></span>
            </li>
          ))}
        </ul>
      ) : <p className="small">Pas encore de vidéo liée à cette fiche dans tes favoris.</p>}
      {mine.length > 0 && (
        <ul className="links-list">
          {mine.map((u) => (
            <li key={u} className="import-row">
              <PlayButton v={{ title: "Ma vidéo", url: u, embed: embedOf(u), source: "Mon lien" }} />
              <span><a href={u} target="_blank" rel="noopener noreferrer">{u.replace(/^https?:\/\/(www\.)?/, "").slice(0, 60)}</a> <button className="btn small ghost danger" onClick={() => setState((s) => { s.recipeVideos[r.id] = (s.recipeVideos[r.id] ?? []).filter((x) => x !== u); })}>Retirer</button></span>
            </li>
          ))}
        </ul>
      )}
      <div className="row">
        <input type="url" inputMode="url" value={link} onChange={(e) => setLink(e.target.value)} placeholder="Ajouter une vidéo (lien TikTok, YouTube…)" aria-label="Lien d'une vidéo pour cette recette" />
        <button className="btn ghost" onClick={add}>Ajouter</button>
      </div>
      {err && <p className="warn-text">{err}</p>}
      <p className="small">Les vidéos sont celles de leurs auteur·e·s, lues depuis TikTok ou YouTube. Les vidéos ATLAS ne sont pas encore tournées. <a href={youtubeSearch(`${r.title.split(" (")[0]} recette`)} target="_blank" rel="noopener noreferrer">Chercher d'autres tutos sur YouTube</a>.</p>
    </Section>
  );
}
