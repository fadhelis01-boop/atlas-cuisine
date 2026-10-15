import { Icon } from "../components/icons";
import { useEffect, useMemo, useState } from "react";
import { ALLERGENS, INGREDIENTS, RECIPE_BY_ID } from "../lib/data";
import { href } from "../lib/router";
import { useStore } from "../lib/store";
import { norm } from "../lib/text";
import { MONTHS, localMonth, marketOfMonth, zoneOf } from "../lib/season";
import { Grid, Page, RecipeCard, Section, useVisible } from "../components/ui";
import { Credit, Photo, photoOf } from "../components/photo";

// Dictionnaire illustré des ingrédients (Tome 13 §8) : chargé à la demande (import dynamique) pour garder
// l'ouverture de l'application rapide ; ensuite en cache hors connexion comme le reste.
export interface DicoEntry { name: string; section: string; what: string; use: string; season: number[]; aliases: string[]; recipes: string[] }
let cache: Record<string, DicoEntry> | null = null;
let pending: Promise<Record<string, DicoEntry>> | null = null;
export function useDico() {
  const [d, setD] = useState(cache);
  useEffect(() => {
    if (cache) return;
    pending ??= import("../data/dico.json").then((m) => (cache = m.default as unknown as Record<string, DicoEntry>));
    pending.then(setD);
  }, []);
  return d;
}

const SECTION_ICON: [RegExp, string, string][] = [
  [/Viandes/, "steak", "tomato"], [/Porc/, "sausage", "berry"], [/Huiles|sucrants|chocolat/, "honey", "saffron"], [/Poissons/, "fish", "ocean"], [/Œufs|laitiers/, "cheese", "crust"],
  [/Produits du monde/, "globe", "aubergine"], [/Légumes/, "carrot", "herb"], [/Fruits/, "strawberry", "chili"], [/Alcools/, "wine", "berry"], [/Légumineuses|céréales/, "wheat", "crust"],
  [/Farines|pains/, "bread", "saffron"], [/Herbes/, "leaf", "pistachio"], [/Épices/, "chili", "chili"], [/Condiments/, "sauce", "tomato"],
];
export const sectionLook = (s: string) => SECTION_ICON.find(([re]) => re.test(s)) ?? [/./, "plate", "tomato"];
const DISPO: Record<string, string> = { "🟢": "En supermarché", "🟡": "Rayon monde ou bio", "🟠": "Épicerie spécialisée", "🔴": "Difficile à trouver en France" };

function Thumb({ slug, section, big }: { slug: string; section: string; big?: boolean }) {
  const k = `ingredient/${slug}`;
  const [, icon, tone] = sectionLook(section);
  return (
    <div className={`dico-thumb tone-${tone} ${big ? "big" : ""}`}>
      {photoOf(k) ? <Photo k={k} alt="" eager={big} sizes={big ? "(min-width: 760px) 420px, 100vw" : "160px"} /> : <span aria-hidden="true"><Icon name={icon} size={big ? 72 : 48} /></span>}
    </div>
  );
}

export function SeasonStrip({ months }: { months: number[] }) {
  const zone = zoneOf(useStore((s) => s.settings.zone));
  if (!months.length) return null;
  const now = localMonth(zone);
  // hémisphère sud : on affiche les mois réels du lieu (décalés de 6 mois par rapport à la France)
  const real = (m: number) => (zone === "sud" ? ((m + 5) % 12) + 1 : m);
  return (
    <div className="season-strip" role="img" aria-label={`Saison : ${months.map((m) => MONTHS[real(m) - 1]).join(", ")}`}>
      {MONTHS.map((_, i) => {
        const fr = zone === "sud" ? ((i + 6) % 12) + 1 : i + 1; // mois « France » correspondant au mois réel i+1
        return <span key={i} className={`${months.includes(fr) ? "on" : ""} ${fr === now ? "now" : ""}`}>{MONTHS[i].slice(0, 1).toUpperCase()}</span>;
      })}
      {zone === "tropical" && <small> calendrier de France métropolitaine (en zone tropicale, beaucoup de produits importés)</small>}
    </div>
  );
}

export function DictionaryPage({ q0 = "" }: { q0?: string }) {
  const dico = useDico();
  const [q, setQ] = useState(q0);
  const [sec, setSec] = useState<string | null>(null);
  const [seasonOnly, setSeasonOnly] = useState(false);
  const zone = zoneOf(useStore((s) => s.settings.zone));
  const market = useMemo(() => new Set(marketOfMonth(zone)), [zone]);
  if (!dico) return <Page title="Dictionnaire des ingrédients" photo="rubrique/explorer">{<p>Chargement…</p>}</Page>;
  const entries = Object.entries(dico);
  const sections = [...new Set(entries.map(([, e]) => e.section))];
  const nq = norm(q.trim());
  const list = entries.filter(([, e]) => (!sec || e.section === sec) && (!seasonOnly || market.has(e.name))
    && (!nq || norm(e.name + " " + e.aliases.join(" ") + " " + e.what).includes(nq))).sort((a, b) => a[1].name.localeCompare(b[1].name, "fr"));
  const letters = [...new Set(list.map(([, e]) => norm(e.name)[0].toUpperCase()))];
  return (
    <Page title="Dictionnaire des ingrédients" sub={`${entries.length} ingrédients expliqués et illustrés : ce que c'est, comment l'utiliser, la saison, où le trouver, par quoi le remplacer, et les recettes qui l'utilisent.`} back="/explorer">
      <div className="searchbar"><input type="search" value={q} onChange={(e) => setQ(e.target.value)} placeholder="Passata, soumbala, galanga, tahini…" aria-label="Chercher un ingrédient" /></div>
      <div className="chips chips-scroll" role="group" aria-label="Familles">
        <button className={`chip ${seasonOnly ? "on" : ""}`} aria-pressed={seasonOnly} onClick={() => setSeasonOnly(!seasonOnly)}>🌱 De saison ce mois-ci</button>
        <button className={`chip ${!sec ? "on" : ""}`} aria-pressed={!sec} onClick={() => setSec(null)}>Tout</button>
        {sections.map((s) => <button key={s} className={`chip ${sec === s ? "on" : ""}`} aria-pressed={sec === s} onClick={() => setSec(sec === s ? null : s)}><Icon name={sectionLook(s)[1]} size={18} /> {s.split(/,| &| \(/)[0]}</button>)}
      </div>
      <p className="meta" role="status">{list.length} ingrédient{list.length > 1 ? "s" : ""}</p>
      {!q && !sec && !seasonOnly && <nav className="letters" aria-label="Lettres">{letters.map((l) => <a key={l} href={`#lettre-${l}`} onClick={(e) => { e.preventDefault(); document.getElementById(`lettre-${l}`)?.scrollIntoView({ behavior: "smooth" }); }}>{l}</a>)}</nav>}
      {letters.map((l) => (
        <section key={l} className="dico-letter" id={`lettre-${l}`} aria-label={`Lettre ${l}`}>
          <h2 className="dico-l">{l}</h2>
          <div className="dico-grid">
            {list.filter(([, e]) => norm(e.name)[0].toUpperCase() === l).map(([slug, e]) => (
              <a key={slug} href={href(`/ingredient/${slug}`)} className="card dico-card">
                <Thumb slug={slug} section={e.section} />
                <span className="dico-name">{e.name}{market.has(e.name) && <span className="tag-season" title="De saison"> 🌱</span>}</span>
                <span className="dico-what">{e.what}</span>
              </a>
            ))}
          </div>
        </section>
      ))}
    </Page>
  );
}

export function IngredientPage({ slug }: { slug: string }) {
  const dico = useDico();
  const all = useVisible(Object.values(RECIPE_BY_ID));
  if (!dico) return <Page title="Ingrédient" back="/dictionnaire"><p>Chargement…</p></Page>;
  const e = dico[slug];
  if (!e) return <Page title="Ingrédient introuvable" back="/dictionnaire"><p><a href={href("/dictionnaire")}>Retour au dictionnaire</a></p></Page>;
  const ref = INGREDIENTS[e.name];
  const visible = new Set(all.map((r) => r.id));
  const recipes = e.recipes.map((id) => RECIPE_BY_ID[id]).filter((r) => r && visible.has(r.id));
  const pork = ref?.derivs.pork, alcohol = ref?.derivs.alcohol;
  return (
    <main className="page" id="contenu">
      <a className="back" href={href("/dictionnaire")}>← Dictionnaire</a>
      <div className="recipe-head">
        <figure className="hero-fig"><Thumb slug={slug} section={e.section} big /><figcaption><Credit k={`ingredient/${slug}`} note={false} /></figcaption></figure>
        <div>
          <h1>{e.name}</h1>
          <p className="meta"><Icon name={sectionLook(e.section)[1]} size={16} className="ic-inline" /> {e.section}{e.aliases.length ? ` · aussi : ${e.aliases.join(", ")}` : ""}</p>
          <p className="intro">{e.what}</p>
          <div className="card pad"><strong>En cuisine :</strong> {e.use}</div>
          {ref?.note && <div className="card pad zw"><strong>Astuce du référentiel :</strong> {ref.note}</div>}
          <div className="badges">
            {ref && <span className="badge info">🛒 {DISPO[ref.dispo] ?? ref.dispo}</span>}
            {pork && <span className={`badge ${pork === "certain" ? "bad" : "warn"}`}>🐖 {pork === "certain" ? "Contient du porc" : "Porc possible"}</span>}
            {alcohol && <span className={`badge ${alcohol === "certain" ? "bad" : "warn"}`}>🍷 {alcohol === "certain" ? "Alcool" : alcohol === "trace" ? "Traces d'alcool possibles" : "Alcool possible"}</span>}
            {ref?.allergens.length ? <span className="badge neutral">Allergènes : {ref.allergens.map((a) => ALLERGENS[a]).join(", ")}</span> : null}
            {ref && ref.maybe.filter((a) => !ref.allergens.includes(a)).length > 0 && <span className="badge neutral">Possible selon la marque : {ref.maybe.filter((a) => !ref.allergens.includes(a)).map((a) => ALLERGENS[a]).join(", ")}</span>}
          </div>
          {e.season.length > 0 && <Section title="Saison"><SeasonStrip months={e.season} /></Section>}
        </div>
      </div>
      {recipes.length > 0 && <Section title={`Recettes avec cet ingrédient (${recipes.length})`}><Grid>{recipes.slice(0, 24).map((r) => <RecipeCard key={r.id} r={r} />)}</Grid></Section>}
    </main>
  );
}
