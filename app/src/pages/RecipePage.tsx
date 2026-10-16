import StepPhotos from "../components/StepPhotos";
import { Icon } from "../components/icons";
import { toast } from "../lib/toast";
import { balanceOf, finishFor } from "../lib/dressage";
import { cuesIn, saltDose } from "../lib/cues";
import { rescueFor } from "../lib/rescue";
import Journal from "../components/Journal";
import { termsIn } from "../lib/glossaire";
import { SEASON_LABEL, seasonFit, seasonOf, zoneOf } from "../lib/season";
import { useEffect, useMemo, useState } from "react";
import { ALLERGENS, INGREDIENTS, RECIPE_BY_ID } from "../lib/data";
import { evaluateLines, verdict } from "../lib/engine";
import { href, goBack } from "../lib/router";
import { pushRecent, setState, toggleFavorite, uid, useProfile, useStore, getState } from "../lib/store";
import { durationsIn, gestureLabel, minutes, ovenPlan, plain, scaleQty, scaleStep, costLabel, levelLabel } from "../lib/text";
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
  if (f.inSeason.length && f.score > 0) return <p className="meta season-ok"><Icon name="sprout" size={16} className="ic-inline" /> De saison ({SEASON_LABEL[s]}) : {f.inSeason.slice(0, 4).join(", ").toLowerCase()}</p>;
  if (f.outSeason.length) return <p className="meta season-out"><Icon name="timer" size={16} className="ic-inline" /> Hors saison ici en ce moment : {f.outSeason.slice(0, 3).join(", ").toLowerCase()} (surgelés ou conserves de qualité conviennent souvent).</p>;
  return null;
}

/** Ce qu'un débutant doit savoir avant d'allumer le feu : matériel, préchauffage, ingrédients à sortir à l'avance. */
function BeforeYouStart({ r }: { r: Recipe }) {
  const all = r.steps.join(" ");
  const oven = ovenPlan(r.steps);
  const soft = /pommade|beurre mou|température ambiante|sors .{0,40}avant/i.test(all + " " + r.ingredients.map((l) => l.label).join(" "));
  const longRest = r.rest >= 240;
  return (
    <div className="card pad before">
      <strong>Avant de commencer</strong>
      <ul className="small">
        <li>Lis toute la recette une fois, puis prépare et pèse tous les ingrédients (la « mise en place ») : la cuisson va ensuite plus vite que prévu.</li>
        {r.equipment && <li>Matériel : {plain(r.equipment)}</li>}
        {oven && <li>Préchauffe le four à <strong>{oven.temp}</strong> au moins 15 min avant d'enfourner (chaque four est différent : surveille les premières fois).</li>}
        {soft && <li>Sors le beurre (et les œufs) du frigo 1 h avant.</li>}
        {longRest && <li>Prévois à l'avance : {minutes(r.rest)} de repos, de pousse ou de cuisson.</li>}
      </ul>
    </div>
  );
}

function Lexique({ text }: { text: string }) {
  const terms = termsIn(text);
  if (!terms.length) return null;
  return (
    <details className="card pad lexique">
      <summary><strong><Icon name="dictionary" size={18} className="ic-inline" /> Les mots de cuisine de cette recette ({terms.length})</strong></summary>
      <dl>{terms.map((t) => <div key={t.term}><dt>{t.tech ? <a href={href(`/technique/${t.tech}`)}>{t.term}</a> : t.term}</dt><dd>{t.def}</dd></div>)}</dl>
    </details>
  );
}

const TOC: [string, string][] = [["r-ingredients", "Ingrédients"], ["r-etapes", "Étapes"], ["r-finition", "Finition"], ["r-aide", "Si ça rate"]];
/** Sommaire collant (audit UX 5) : sur téléphone, sauter d'un bloc à l'autre d'une fiche longue. Boutons et non ancres : le routeur utilise le #. */
function RecipeToc() {
  return (
    <nav className="recipe-toc" aria-label="Sommaire de la recette">
      {TOC.map(([id, l]) => <button key={id} type="button" className="chip" onClick={() => document.getElementById(id)?.scrollIntoView({ behavior: "smooth", block: "start" })}>{l}</button>)}
    </nav>
  );
}

function FinishBlock({ r }: { r: Recipe }) {
  const f = finishFor(r);
  return (
    <div className="finish card pad" id="r-finition">
      <h3 className="h4"><Icon name="plate" size={22} className="ic-inline" /> Finition et dressage</h3>
      {f.taste && <p><strong>Goûte et rectifie.</strong> {f.taste}</p>}
      <p>{f.plate}</p>
      {f.green && <p className="small">{f.green}</p>}
      {balanceOf(r) && <p className="small"><Icon name="broccoli" size={16} className="ic-inline" /> {balanceOf(r)}</p>}
      <p className="small"><a href={href("/technique/presenter-une-assiette")}>Les gestes pour présenter une assiette →</a></p>
    </div>
  );
}

function RescueBlock({ r }: { r: Recipe }) {
  const list = rescueFor(r);
  if (!list.length) return null;
  return (
    <Section title={<><Icon name="lifebuoy" size={24} className="ic-inline" /> Si ça ne se passe pas comme prévu</>} id="r-aide">
      <div className="rescue">
        {list.map((x) => (
          <details key={x.problem} className="card pad">
            <summary><strong>{x.problem}</strong></summary>
            <p>{x.fix}</p>
            {x.tech && <p className="small"><a href={href(`/technique/${x.tech}`)}>Voir la technique pas à pas →</a></p>}
          </details>
        ))}
      </div>
    </Section>
  );
}

export default function RecipePage({ id, q }: { id: string; q: URLSearchParams }) {
  const r = RECIPE_BY_ID[id];
  const p = useProfile();
  const fav = useStore((s) => s.favorites.includes(id));
  const cookedN = useStore((s) => s.cooked[id]);
  const journalEntry = useStore((s) => s.journal?.[id]);
  const asked = Number(q.get("portions")) || 0;
  const [portions, setPortions] = useState(asked || r?.portions || 4);
  const [useAdapted, setUseAdapted] = useState(true);
  const [reading, setReading] = useState<number | null>(null);
  const [showAnyway, setShowAnyway] = useState(q.get("voir") === "1");
  useEffect(() => { if (r) { pushRecent(r.id); setPortions(asked || r.portions); } return () => { stopSpeaking(); }; }, [id]); // eslint-disable-line react-hooks/exhaustive-deps
  const v = useMemo(() => (r ? verdict(r, p) : null), [r, p]);
  if (!r || !v) return <Page title="Recette introuvable" back="/explorer">{null}</Page>;

  const adapted = v.availability === "adaptable" && useAdapted ? v.adapted : null;
  const lines: RecipeLine[] = adapted ? adapted.lines : r.ingredients;
  const factor = portions / r.portions;
  const salt = saltDose(r, portions);
  // repères visuels : chacun n'apparaît qu'à sa première étape, pour ne pas répéter
  const cues = (() => { const seen = new Set<string>(); return r.steps.map((st) => cuesIn(st).filter((c) => !seen.has(c) && (seen.add(c), true))); })();
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
    const before = getState().shopping.length;
    setState((s) => {
      for (const l of lines) {
        if (!l.ref || l.ref.startsWith("SUB:")) continue;
        if (s.shopping.some((x) => x.ref === l.ref && !x.done && x.from === r.title)) continue;
        s.shopping.push({ id: uid(), ref: l.ref, label: `${scaleQty(l.qty, factor)} ${l.label}`.trim(), from: r.title, done: false, section: INGREDIENTS[l.ref]?.section ?? "Autres" });
      }
    });
    const added = getState().shopping.length - before;
    toast(added ? `${added} ingrédient${added > 1 ? "s" : ""} ajouté${added > 1 ? "s" : ""} aux courses` : "Déjà dans ta liste de courses",
      { undo: added ? () => setState((s) => { s.shopping = s.shopping.slice(0, before); }) : undefined, link: { label: "Voir", to: "/courses" } });
  };

  const share = async () => {
    const url = `${location.origin}${location.pathname}#/recette/${r.id}`;
    try {
      if (navigator.share) await navigator.share({ title: r.title, text: `${r.title} : une recette ATLAS`, url });
      else { await navigator.clipboard.writeText(url); toast("Lien copié : colle-le dans un message"); }
    } catch { /* partage annulé */ }
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
      <div className="cook-sticky" role="group" aria-label="Cuisiner cette recette">
        <div className="portions mini" role="group" aria-label="Nombre de portions">
          <button type="button" onClick={() => setPortions(Math.max(1, portions - 1))} aria-label="Moins de portions">−</button>
          <span><strong>{portions}</strong> pers.</span>
          <button type="button" onClick={() => setPortions(portions + 1)} aria-label="Plus de portions">+</button>
        </div>
        <a className="btn" href={href(`/cuisine/${r.id}${adapted ? "?adapte=1" : ""}${portions !== r.portions ? `${adapted ? "&" : "?"}portions=${portions}` : ""}`)}><Icon name="play" size={20} /> Cuisiner</a>
      </div>
      <button type="button" className="back" onClick={() => goBack(`/region/${r.macro}`)}><Icon name="back" size={20} /> Retour</button>
      <div className="recipe-head">
        <figure className="hero-fig"><Cover r={r} big /><figcaption><Credit k={`recette/${r.id}`} /></figcaption></figure>
        <div>
          <h1>{r.title}</h1>
          {r.origin && r.origin !== r.title && <p className="origin" lang="und">{r.origin}</p>}
          <p className="meta">{r.regionPath.join(" › ")} · {r.kind}</p>
          {r.fusionNote && <p className="meta"><a href={href("/region/fusion")}><Icon name="fusion" size={16} className="ic-inline" /> Food fusion</a> : {r.fusionNote}</p>}
          {r.videos.some((x) => x.embed) && <button className="btn ghost small" onClick={() => { const x = r.videos.find((y) => y.embed)!; playVideo(x); }}><Icon name="play" size={16} className="ic-inline" /> Voir la vidéo</button>}
          <p className="meta"><Icon name="timer" size={16} className="ic-inline" />{minutes(r.active)} de préparation{r.rest ? ` + ${minutes(r.rest)} (cuisson / repos)` : ""} · {levelLabel(r.level)} · {costLabel(r.cost)}</p>
          <DietBadges r={r} v={v} lines={adapted ? lines : undefined} />
          <SeasonBadge r={r} />
          <a className="btn big cook-cta" href={href(`/cuisine/${r.id}${adapted ? "?adapte=1" : ""}`)}><Icon name="play" size={22} /> Cuisiner pas à pas</a>
          {/* actions secondaires : icônes légendées de même taille (audit UX 2026-10-16 §2.4) */}
          <div className="quick-actions" role="group" aria-label="Actions">
            <button type="button" onClick={() => toggleFavorite(r.id)} aria-pressed={fav}><Icon name="heart" size={24} className={fav ? "ic-on" : ""} /><span>{fav ? "Favori" : "Garder"}</span></button>
            <button type="button" onClick={addToShopping}><Icon name="cart" size={24} /><span>Courses</span></button>
            {r.role === "plat" && <a href={href(`/semaine?ajout=${r.id}`)}><Icon name="calendar" size={24} /><span>Planifier</span></a>}
            {ttsAvailable() && <button type="button" onClick={() => read("tout")} aria-pressed={reading !== null}><Icon name={reading !== null ? "close" : "speaker"} size={24} /><span>{reading !== null ? "Arrêter" : "Écouter"}</span></button>}
            <button type="button" onClick={() => void share()}><Icon name="share" size={24} /><span>Partager</span></button>
          </div>
          <p className="small untested"><Icon name="alert" size={15} className="ic-inline" /> Recette pas encore testée dans la cuisine d'ATLAS : après l'avoir faite, note-la dans <a href={href("/biblio")}>ton carnet</a>, ton avis sert à la corriger.</p>
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
          <p className="small"><Icon name="alert" size={16} className="ic-inline" /> <strong>Substitution à tester</strong> : elle n'a pas encore passé la dégustation à l'aveugle (Tome 7 §3). Elle est vérifiée pour ton régime, pas encore pour le goût.</p>
          {v.adapted.newAllergens.length > 0 && <p className="warn-text"><Icon name="alert" size={16} className="ic-inline" /> Nouvel allergène dans la version adaptée : {v.adapted.newAllergens.map((a) => ALLERGENS[a]).join(", ")}.</p>}
        </div>
      )}
      {v.warnings.length > 0 && <div className="banner warn"><strong>À vérifier :</strong> {v.warnings.join(" · ")}. Lis les étiquettes.</div>}
      {kidsAlert && <div className="banner warn"><Icon name="kid" size={16} className="ic-inline" /> Recette conseillée à partir de {r.age} ans ; ton plus jeune a {p.kidsAge} an(s). {plain(r.kids)}</div>}

      <p className="intro"><Rich text={r.intro} /></p>

      <RecipeToc />
      <div className="two-col">
        <Section title="Ingrédients" id="r-ingredients">
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
            {salt && <li className="salt-line"><span className="qty">Sel</span> {salt.text}{salt.water && <span className="meta"> · Eau de cuisson des pâtes ou des légumes : 10 g de sel par litre (2 c. à c. rases).</span>}</li>}
          </ul>
          {lines.some((l) => /c\. à [sc]\.|pincée/.test(l.qty)) && <p className="small abbr">c. à s. = cuillère à soupe (15 ml) · c. à c. = cuillère à café (5 ml) · pincée = ce qu'on prend entre 2 doigts</p>}
          {ev.allergens.size > 0 && <p className="small"><strong>Allergènes :</strong> {[...ev.allergens].map((a) => ALLERGENS[a]).join(", ")}{ev.maybeAllergens.size > ev.allergens.size ? ` ; possibles selon la marque : ${[...ev.maybeAllergens].filter((a) => !ev.allergens.has(a)).map((a) => ALLERGENS[a]).join(", ")}` : ""}.</p>}
          <Leftovers r={r} />
        </Section>

        <Section title="Étapes" id="r-etapes">
          <BeforeYouStart r={r} />
          <ol className="steps">
            {r.steps.map((s, i) => (
              <li key={i}>
                <Rich text={scaleStep(s, factor)} />
                {cues[i].length > 0 && <p className="cue">{cues[i].map((c) => <span key={c}><Icon name="eye" size={16} className="ic-inline" /> {c} </span>)}</p>}
                {durationsIn(s).length > 0 && (
                  <div className="timers-inline">
                    {durationsIn(s).filter((d, j, a) => a.findIndex((x) => x.label === d.label) === j).map((d, j) => <button key={j} className="chip" onClick={() => startTimer(`${r.title.split(" (")[0]} · ${gestureLabel(s, i + 1)}`, d.seconds, r.id)}><Icon name="timer" size={15} className="ic-inline" />{d.label}</button>)}
                  </div>
                )}
              </li>
            ))}
          </ol>
          <Lexique text={r.steps.join(" ")} />
          <FinishBlock r={r} />
        </Section>
      </div>

      <StepPhotos subject={`recette/${r.id}`} title="Pas à pas en photos" />
      <RescueBlock r={r} />
      {((cookedN ?? 0) > 0 || journalEntry) && <Section title="Mon carnet"><Journal id={r.id} /></Section>}
      {r.tips.length > 0 && <Section title="Astuces du chef"><ul>{r.tips.map((t, i) => <li key={i}><Rich text={t} /></li>)}</ul></Section>}
      <Section title={<><Icon name="plate" size={24} className="ic-inline" /> Pour recevoir</>}>
        <p>Entrée, dessert et boissons qui vont avec, quantités calculées pour tes invités et ce qui se prépare la veille.</p>
        <a className="btn ghost" href={href(`/menu/${r.id}`)}>Compléter le menu autour de ce plat</a>
      </Section>
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
      <p className="small source">Source : bible ATLAS, {r.source}. Fiche <strong>non testée en cuisine</strong> (Tome 7 §2) ; référentiel d'ingrédients niveau C. À valider au test : quantités, temps et rendu (Tome 7 §2).</p>
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
