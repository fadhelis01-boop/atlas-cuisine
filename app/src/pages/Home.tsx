import { useMemo, useState } from "react";
import { RECIPES, RECIPE_BY_ID } from "../lib/data";
import { FETES } from "../lib/content";
import { evaluate } from "../lib/engine";
import { go, href } from "../lib/router";
import { useProfile, useStore } from "../lib/store";
import { norm } from "../lib/text";
import type { Recipe } from "../lib/types";
import { Grid, RecipeCard, Section, useVisible } from "../components/ui";
import { Photo, photoOf } from "../components/photo";
import { HeroArt } from "../components/art";
import { MONTHS_FULL, SEASON_LABEL, type Zone, marketOfMonth, seasonFit, seasonOf, zoneOf } from "../lib/season";
import { INGREDIENTS } from "../lib/data";
import { sectionLook } from "./Dictionnaire";
import { momentOf, propose } from "../lib/propose";
import { PARCOURS } from "../lib/parcours";

// Rubriques : chacune a sa couleur d'étiquette (palette « marché » du Tome 13 §6).
const ENTRIES = [
  { to: "/explorer", icon: "🌍", label: "Cuisines du monde", sub: "par région", tone: "tomato" },
  { to: "/frigo", icon: "🥕", label: "Avec ce que j'ai", sub: "par ingrédients", tone: "saffron" },
  { to: "/semaine", icon: "📅", label: "Ma semaine", sub: "menus + courses", tone: "herb" },
  { to: "/enfants", icon: "🧒", label: "Enfants", sub: "âges, sécurité", tone: "pistachio" },
  { to: "/pains", icon: "🥖", label: "Pains & bases", sub: "pizza, naan, crêpes", tone: "crust" },
  { to: "/sauces", icon: "🥫", label: "Sauces maison", sub: "sans additifs", tone: "chili" },
  { to: "/techniques", icon: "🔪", label: "Techniques", sub: "chef, pâtissier, boulanger", tone: "aubergine" },
  { to: "/fetes", icon: "🎉", label: "Fêtes & menus", sub: "entrée, plat, dessert", tone: "berry" },
  { to: "/zero-dechet", icon: "♻️", label: "Zéro déchet", sub: "tout utiliser", tone: "herb" },
  { to: "/dictionnaire", icon: "📖", label: "Dictionnaire", sub: "ingrédients illustrés", tone: "ocean" },
  { to: "/imports", icon: "📲", label: "Mes imports", sub: "TikTok & co", tone: "crust" },
];
const TILE_PHOTO: Record<string, string> = { "/explorer": "rubrique/explorer", "/frigo": "rubrique/frigo", "/enfants": "rubrique/enfants", "/pains": "rubrique/pains",
  "/sauces": "rubrique/sauces", "/techniques": "rubrique/techniques", "/fetes": "rubrique/fetes", "/zero-dechet": "rubrique/zero_dechet", "/imports": "rubrique/imports" };

const PASTRY = /choux|patissiere|sucree|feuilletage|meringue|ganache|temperer|macaron|genoise|caramel|tourage|brioche|praline|chantilly|creme anglaise/;
const has = (r: Recipe, re: RegExp) => re.test(norm(r.title)) || r.ingredients.some((l) => re.test(norm(l.label)));

/** Envies : des filtres d'un geste, affichés en rangée sous le bandeau. */
let ZONE: Zone = "nord"; // zone courante, fixée au rendu (les tests d'envies en ont besoin)
const CRAVINGS: { id: string; icon: string; label: string; test: (r: Recipe) => boolean }[] = [
  { id: "saison", icon: "🌱", label: "De saison", test: (r) => r.role !== "autre" && seasonFit(r, ZONE).score >= 2 },
  { id: "rapide", icon: "⏱️", label: "Prêt en 30 min", test: (r) => r.role === "plat" && r.active + r.rest <= 30 },
  { id: "chocolat", icon: "🍫", label: "Chocolat", test: (r) => (r.role === "dessert" || r.role === "boisson" || r.kind === "Base") && has(r, /chocolat|cacao|praline/) },
  { id: "patisserie", icon: "🧁", label: "Pâtisserie", test: (r) => (r.role === "dessert" || r.kind === "Pain" || r.kind === "Base") && (r.techniques.some((t) => PASTRY.test(norm(t))) || r.regionPath.includes("Chocolaterie")) },
  { id: "street", icon: "🌯", label: "Street-food", test: (r) => /taco|burger|kebab|bao|banh|bokit|fataya|empanada|samoussa|falafel|souvlaki|suya|arepa|lahmacun|pan bagnat|bourek|briouat|nem|gyoza|frites|churros|elote|pizza|croque|poutine/.test(norm(r.title)) },
  { id: "vege", icon: "🥦", label: "Végétarien", test: (r) => r.role === "plat" && evaluate(r).flesh.length === 0 },
  { id: "mer", icon: "🐟", label: "Poissons & mer", test: (r) => r.role !== "dessert" && r.profile.includes("poisson") },
  { id: "epice", icon: "🌶️", label: "Ça pique", test: (r) => r.profile.includes("epice") && r.role === "plat" },
  { id: "fusion", icon: "🌐", label: "Food fusion", test: (r) => r.cats.includes("fusion") },
  { id: "boissons", icon: "🍹", label: "Boissons", test: (r) => r.role === "boisson" },
];

function greeting(h: number) {
  if (h >= 5 && h < 11) return { hi: "Bonjour !", line: "Un petit-déjeuner gourmand ou le menu du jour ?" };
  if (h >= 11 && h < 14) return { hi: "Bon appétit !", line: "Qu'est-ce qu'on cuisine pour midi ?" };
  if (h >= 14 && h < 18) return { hi: "L'heure du goûter", line: "Une pâtisserie, un chocolat chaud, des crêpes ?" };
  if (h >= 18 && h < 23) return { hi: "Bonsoir !", line: "Qu'est-ce qu'on mange ce soir ?" };
  return { hi: "Une envie de nuit ?", line: "Quelque chose de rapide et réconfortant." };
}

/** Choix stable sur la journée (même liste toute la journée, nouvelle le lendemain). */
function daily<T>(list: T[], n: number, salt: number) {
  const day = Math.floor(Date.now() / 86400000) + salt;
  if (list.length <= n) return list;
  const out: T[] = []; const step = 7919 % list.length || 1;
  for (let i = 0, k = (day * 31) % list.length; out.length < n; i++, k = (k + step) % list.length) if (!out.includes(list[k])) out.push(list[k]);
  return out;
}

function SeasonNote({ r, zone, label }: { r: Recipe; zone: Zone; label: string }) {
  const f = seasonFit(r, zone);
  return <p className="tag-wrap"><span className="tag-day">{label}</span>{f.inSeason.length > 0 && <span className="meta"> 🌱 {f.inSeason.slice(0, 3).map((x) => x.split(/ \/ | \(/)[0].toLowerCase()).join(", ")}</span>}{!f.inSeason.length && f.mood && <span className="meta"> {f.mood === "chaud" ? "🔥 plat réconfortant" : "❄️ plat frais"}</span>}</p>;
}

const TIMES: [number, string][] = [[20, "20 min"], [45, "45 min"], [999, "J'ai le temps"]];

/** « Pas d'idée ? » : trois suggestions en un geste (heure, saison, temps disponible, frigo). */
function ProposeMoi({ visible, zone }: { visible: Recipe[]; zone: Zone }) {
  const fridge = useStore((s) => s.fridge);
  const [time, setTime] = useState(45);
  const [seed, setSeed] = useState(0);
  const hour = new Date().getHours();
  const props = useMemo(() => (seed ? propose(visible, { hour, zone, maxMinutes: time, fridge: fridge.map((f) => f.ref), seed }) : []), [seed, time, visible, zone, fridge, hour]);
  return (
    <section className="section propose card pad" aria-label="Propose-moi">
      <div className="propose-head">
        <h2 className="h3">🎲 Pas d'idée ? <span className="meta">{momentOf(hour).label}</span></h2>
        <span className="chips" role="group" aria-label="Temps disponible">
          {TIMES.map(([m, l]) => <button key={m} type="button" className={`chip ${time === m ? "on" : ""}`} aria-pressed={time === m} onClick={() => { setTime(m); if (seed) setSeed(seed + 1); }}>{l}</button>)}
        </span>
        <button type="button" className="btn" onClick={() => setSeed(Date.now())}>{seed ? "Autres idées" : "Propose-moi"}</button>
      </div>
      {seed > 0 && (props.length
        ? <Grid>{props.map((x) => <RecipeCard key={x.r.id} r={x.r} note={<span className="meta">{x.why.join(" · ")}</span>} />)}</Grid>
        : <p className="small">Rien dans ce temps-là avec les réglages de ton foyer : essaie « J'ai le temps ».</p>)}
      {seed > 0 && !fridge.length && <p className="small">Astuce : renseigne <a href={href("/frigo")}>ton frigo</a> et les idées utiliseront d'abord ce que tu as.</p>}
    </section>
  );
}

/** Accueil personnalisé (audit UX 7) : tant qu'on a très peu cuisiné, le parcours débutant passe en premier. */
function Beginner() {
  const cooked = useStore((s) => Object.values(s.cooked).reduce((a, n) => a + n, 0));
  const learned = useStore((s) => s.learned?.length ?? 0);
  if (cooked >= 3 || learned >= PARCOURS.length) return null;
  const next = PARCOURS[learned];
  return (
    <a className="card pad beginner" href={href("/apprendre")}>
      <span className="beginner-ic" aria-hidden="true">🎓</span>
      <span><strong>{learned ? `J'apprends à cuisiner : étape ${learned + 1} sur ${PARCOURS.length}` : "Tu débutes ? Apprends pas à pas"}</strong><br />
        <span className="small">{learned ? `Prochaine étape : ${next.title}.` : "15 étapes courtes, du couteau aux sauces, avec une recette facile à chaque fois."}</span></span>
    </a>
  );
}

export default function Home() {
  const [q, setQ] = useState("");
  const [craving, setCraving] = useState<string | null>(null);
  const p = useProfile();
  const recent = useStore((s) => s.recent).map((id) => RECIPE_BY_ID[id]).filter(Boolean);
  const month = new Date().getMonth() + 1;
  const nextFetes = FETES.filter((f) => f.month && (f.month === month || f.month === (month % 12) + 1));
  const visible = useVisible(RECIPES);
  const g = greeting(new Date().getHours());
  const zone = zoneOf(useStore((st) => st.settings.zone));
  ZONE = zone;
  const season = seasonOf(zone);
  // Menu du jour : parmi les recettes les mieux accordées à la saison du lieu (produits de saison, plat chaud ou frais selon le climat)
  const seasonal = (role: string, salt: number) => {
    const ranked = visible.filter((r) => r.role === role).map((r) => [r, seasonFit(r, zone).score] as const).sort((a, b) => b[1] - a[1]);
    const top = ranked.slice(0, Math.max(12, Math.round(ranked.length * 0.3))).map(([r]) => r);
    return daily(top, 1, salt)[0] ?? null;
  };
  const entree = seasonal("entree", 7);
  const today = seasonal("plat", 0);
  const dessert = seasonal("dessert", 3);
  const market = useMemo(() => marketOfMonth(zone).filter((n) => INGREDIENTS[n]?.slug), [zone]);
  const monthName = MONTHS_FULL[new Date().getMonth()];
  const news = useMemo(() => daily(visible.filter((r) => r.source.includes("vague 2") && r.role !== "autre"), 8, 1), [visible]);
  const pastry = useMemo(() => daily(visible.filter(CRAVINGS[2].test), 8, 2), [visible]);
  const picked = craving ? CRAVINGS.find((c) => c.id === craving) : null;
  const cravingList = useMemo(() => (picked ? daily(visible.filter(picked.test), 12, 5) : []), [picked, visible]);
  const kidsPick = p.kidsAge !== null ? visible.filter((r) => r.age !== null && r.age <= Math.max(p.kidsAge ?? 1, 1) && r.role === "plat").slice(0, 4) : [];

  return (
    <main className="page home" id="contenu">
      <form className="hero hero-skin" role="search" onSubmit={(e) => { e.preventDefault(); go(`/recherche?q=${encodeURIComponent(q)}`); }}>
        <div className="hero-copy">
          <p className="hero-hi">{g.hi}</p>
          <h1>{g.line}</h1>
          <p className="hero-sub">{RECIPES.length} recettes du monde, faites maison : de la sauce frites au fraisier, du thiéboudienne au ramen.</p>
          <div className="searchbar">
            <input type="search" value={q} onChange={(e) => setQ(e.target.value)} placeholder="Un plat, une région, un ingrédient… (tajine, éclair, mafé)" aria-label="Rechercher une recette" />
            <button className="btn" type="submit">Chercher</button>
          </div>
          {(p.noPork || p.alcohol !== "allowed" || p.allergens.length > 0 || p.vegetarian) && (
            <p className="hero-filters">Filtres du foyer : {[p.noPork && "sans porc", p.alcohol === "standard" && "sans alcool", p.alcohol === "strict" && "sans alcool strict", p.vegetarian && "végétarien", p.allergens.length && `${p.allergens.length} allergène(s) exclu(s)`].filter(Boolean).join(" · ")} · <a href={href("/profil")}>modifier</a></p>
          )}
        </div>
        <HeroArt />
      </form>

      <div className="cravings" role="group" aria-label="Envies du moment">
        {CRAVINGS.map((c) => (
          <button key={c.id} type="button" className={`craving ${craving === c.id ? "on" : ""}`} aria-pressed={craving === c.id} onClick={() => setCraving(craving === c.id ? null : c.id)}>
            <span aria-hidden="true">{c.icon}</span> {c.label}
          </button>
        ))}
      </div>
      {picked && (
        <Section title={`${picked.icon} ${picked.label}`} more={<button type="button" className="btn ghost small" onClick={() => setCraving(null)}>Fermer</button>}>
          {cravingList.length ? <div className="rail">{cravingList.map((r) => <RecipeCard key={r.id} r={r} />)}</div> : <p className="small">Rien pour ce filtre avec les réglages de ton foyer.</p>}
        </Section>
      )}

      <Beginner />
      <ProposeMoi visible={visible} zone={zone} />

      <nav className="entries" aria-label="Rubriques">
        {ENTRIES.map((e) => {
          const pk = TILE_PHOTO[e.to]; const ph = pk && photoOf(pk);
          return (
            <a key={e.to} href={href(e.to)} className={`entry tone-${e.tone} ${ph ? "has-photo" : ""}`}>
              {ph && <Photo k={pk} alt="" sizes="(min-width: 700px) 200px, 33vw" />}
              <span className="entry-ic" aria-hidden="true">{e.icon}</span><span className="entry-lb">{e.label}</span><span className="entry-sub">{e.sub}</span>
            </a>
          );
        })}
      </nav>

      {(today || dessert) && (
        <Section title={`Le menu du jour · ${SEASON_LABEL[season]}`} more={<a href={href("/profil")}>Ma zone de saisons →</a>}>
          <Grid>
            {entree && <RecipeCard r={entree} note={<SeasonNote r={entree} zone={zone} label="L'entrée" />} />}
            {today && <RecipeCard r={today} note={<SeasonNote r={today} zone={zone} label="Le plat" />} />}
            {dessert && <RecipeCard r={dessert} note={<SeasonNote r={dessert} zone={zone} label="Le dessert" />} />}
          </Grid>
        </Section>
      )}
      {market.length > 0 && (
        <Section title={zone === "tropical" ? "Le marché des tropiques" : `Le marché ${/^[aeiou]/.test(monthName) ? "d'" : "de "}${monthName}`} more={<a href={href("/dictionnaire")}>Dictionnaire →</a>}>
          <div className="market">
            {market.slice(0, 24).map((n) => {
              const ing = INGREDIENTS[n]; const k = `ingredient/${ing.slug}`; const [, icon, tone] = sectionLook(ing.section);
              return (
                <a key={n} href={href(`/ingredient/${ing.slug}`)} className="market-item">
                  <span className={`dico-thumb round tone-${tone}`}>{photoOf(k) ? <Photo k={k} alt="" sizes="96px" /> : <span aria-hidden="true">{icon}</span>}</span>
                  <span className="market-name">{n.split(/ \/ | \(/)[0]}</span>
                </a>
              );
            })}
          </div>
        </Section>
      )}
      {news.length > 0 && (
        <Section title="Nouveautés gourmandes" more={<a href={href("/explorer")}>Tout l'atlas →</a>}>
          <div className="rail">{news.map((r) => <RecipeCard key={r.id} r={r} />)}</div>
        </Section>
      )}
      {pastry.length > 0 && (
        <Section title="Pâtisserie & chocolat" more={<a href={href("/techniques")}>Les gestes du pâtissier →</a>}>
          <div className="rail">{pastry.map((r) => <RecipeCard key={r.id} r={r} />)}</div>
        </Section>
      )}
      {nextFetes.length > 0 && (
        <Section title="Fêtes à venir" more={<a href={href("/fetes")}>Toutes les fêtes →</a>}>
          {nextFetes.map((f) => (
            <div key={f.name} className="card pad fete-card">
              <h3>🎉 {f.name} <span className="meta">· {f.when}</span></h3>
              <p>{f.traditions}</p>
              <div className="links">{f.ideas.map((id) => RECIPE_BY_ID[id] && <a key={id} className="pill" href={href(`/recette/${id}`)}>{RECIPE_BY_ID[id].title}</a>)}</div>
            </div>
          ))}
        </Section>
      )}
      {kidsPick.length > 0 && (
        <Section title={`Pour les enfants (dès ${p.kidsAge} an${(p.kidsAge ?? 0) > 1 ? "s" : ""})`} more={<a href={href("/enfants")}>Rubrique enfants →</a>}>
          <Grid>{kidsPick.map((r) => <RecipeCard key={r.id} r={r} />)}</Grid>
        </Section>
      )}
      {recent.length > 0 && (
        <Section title="Reprendre">
          <Grid>{recent.slice(0, 4).map((r) => <RecipeCard key={r.id} r={r} />)}</Grid>
        </Section>
      )}
    </main>
  );
}
