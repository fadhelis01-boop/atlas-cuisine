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

// Rubriques : chacune a sa couleur d'étiquette (palette « marché » du Tome 13 §6).
const ENTRIES = [
  { to: "/explorer", icon: "🌍", label: "Cuisines du monde", sub: "par région", tone: "tomato" },
  { to: "/frigo", icon: "🥕", label: "Avec ce que j'ai", sub: "par ingrédients", tone: "saffron" },
  { to: "/enfants", icon: "🧒", label: "Enfants", sub: "âges, sécurité", tone: "pistachio" },
  { to: "/pains", icon: "🥖", label: "Pains & bases", sub: "pizza, naan, crêpes", tone: "crust" },
  { to: "/sauces", icon: "🥫", label: "Sauces maison", sub: "sans additifs", tone: "chili" },
  { to: "/techniques", icon: "🔪", label: "Techniques", sub: "chef, pâtissier, boulanger", tone: "aubergine" },
  { to: "/fetes", icon: "🎉", label: "Fêtes & menus", sub: "entrée, plat, dessert", tone: "berry" },
  { to: "/zero-dechet", icon: "♻️", label: "Zéro déchet", sub: "tout utiliser", tone: "herb" },
  { to: "/imports", icon: "📲", label: "Mes imports", sub: "TikTok & co", tone: "ocean" },
];
const TILE_PHOTO: Record<string, string> = { "/explorer": "rubrique/explorer", "/frigo": "rubrique/frigo", "/enfants": "rubrique/enfants", "/pains": "rubrique/pains",
  "/sauces": "rubrique/sauces", "/techniques": "rubrique/techniques", "/fetes": "rubrique/fetes", "/zero-dechet": "rubrique/zero_dechet", "/imports": "rubrique/imports" };

const PASTRY = /choux|patissiere|sucree|feuilletage|meringue|ganache|temperer|macaron|genoise|caramel|tourage|brioche|praline|chantilly|creme anglaise/;
const has = (r: Recipe, re: RegExp) => re.test(norm(r.title)) || r.ingredients.some((l) => re.test(norm(l.label)));

/** Envies : des filtres d'un geste, affichés en rangée sous le bandeau. */
const CRAVINGS: { id: string; icon: string; label: string; test: (r: Recipe) => boolean }[] = [
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

export default function Home() {
  const [q, setQ] = useState("");
  const [craving, setCraving] = useState<string | null>(null);
  const p = useProfile();
  const recent = useStore((s) => s.recent).map((id) => RECIPE_BY_ID[id]).filter(Boolean);
  const month = new Date().getMonth() + 1;
  const nextFetes = FETES.filter((f) => f.month && (f.month === month || f.month === (month % 12) + 1));
  const visible = useVisible(RECIPES);
  const g = greeting(new Date().getHours());
  const plats = visible.filter((r) => r.role === "plat");
  const today = daily(plats, 1, 0)[0] ?? null;
  const dessert = daily(visible.filter((r) => r.role === "dessert"), 1, 3)[0] ?? null;
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
        <Section title="Le menu du jour">
          <Grid>{today && <RecipeCard r={today} note={<p className="tag-day">Le plat</p>} />}{dessert && <RecipeCard r={dessert} note={<p className="tag-day">Le dessert</p>} />}</Grid>
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
