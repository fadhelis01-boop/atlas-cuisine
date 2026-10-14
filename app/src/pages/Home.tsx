import { useState } from "react";
import { RECIPES, RECIPE_BY_ID } from "../lib/data";
import { FETES } from "../lib/content";
import { go, href } from "../lib/router";
import { useProfile, useStore } from "../lib/store";
import { Grid, RecipeCard, Section, useVisible } from "../components/ui";
import { Photo, photoOf } from "../components/photo";

const ENTRIES = [
  { to: "/explorer", icon: "🌍", label: "Cuisines du monde", sub: "par région" },
  { to: "/frigo", icon: "🥕", label: "Avec ce que j'ai", sub: "par ingrédients" },
  { to: "/enfants", icon: "🧒", label: "Enfants", sub: "âges, sécurité" },
  { to: "/pains", icon: "🥖", label: "Pains & bases", sub: "pizza, naan, crêpes" },
  { to: "/sauces", icon: "🥫", label: "Sauces maison", sub: "sans additifs" },
  { to: "/techniques", icon: "🔪", label: "Techniques", sub: "pas à pas" },
  { to: "/fetes", icon: "🎉", label: "Fêtes & menus", sub: "entrée, plat, dessert" },
  { to: "/zero-dechet", icon: "♻️", label: "Zéro déchet", sub: "tout utiliser" },
  { to: "/imports", icon: "📲", label: "Mes imports", sub: "TikTok & co" },
];

const TILE_PHOTO: Record<string, string> = { "/explorer": "rubrique/explorer", "/frigo": "rubrique/frigo", "/enfants": "rubrique/enfants", "/pains": "rubrique/pains",
  "/sauces": "rubrique/sauces", "/techniques": "rubrique/techniques", "/fetes": "rubrique/fetes", "/zero-dechet": "rubrique/zero_dechet", "/imports": "rubrique/imports" };

export default function Home() {
  const [q, setQ] = useState("");
  const p = useProfile();
  const recent = useStore((s) => s.recent).map((id) => RECIPE_BY_ID[id]).filter(Boolean);
  const month = new Date().getMonth() + 1;
  const nextFetes = FETES.filter((f) => f.month && (f.month === month || f.month === (month % 12) + 1));
  const visible = useVisible(RECIPES);
  // suggestion du jour : stable sur la journée, parmi les plats qui conviennent au foyer
  const day = Math.floor(Date.now() / 86400000);
  const plats = visible.filter((r) => r.role === "plat");
  const today = plats.length ? plats[day % plats.length] : null;
  const kidsPick = p.kidsAge !== null ? visible.filter((r) => r.age !== null && r.age <= Math.max(p.kidsAge ?? 1, 1) && r.role === "plat").slice(0, 4) : [];

  return (
    <main className="page" id="contenu">
      <form className="hero" role="search" onSubmit={(e) => { e.preventDefault(); go(`/recherche?q=${encodeURIComponent(q)}`); }}>
        <h1>Qu'est-ce qu'on cuisine ?</h1>
        <div className="searchbar">
          <input type="search" value={q} onChange={(e) => setQ(e.target.value)} placeholder="Un plat, une région, un ingrédient… (tajine, naan, mafé)" aria-label="Rechercher une recette" />
          <button className="btn" type="submit">Chercher</button>
        </div>
        {(p.noPork || p.alcohol !== "allowed" || p.allergens.length > 0 || p.vegetarian) && (
          <p className="small">Filtres du foyer actifs : {[p.noPork && "sans porc", p.alcohol === "standard" && "sans alcool", p.alcohol === "strict" && "sans alcool strict", p.vegetarian && "végétarien", p.allergens.length && `${p.allergens.length} allergène(s) exclu(s)`].filter(Boolean).join(" · ")} — <a href={href("/profil")}>modifier</a></p>
        )}
      </form>

      <nav className="entries" aria-label="Rubriques">
        {ENTRIES.map((e) => (
(() => { const pk = TILE_PHOTO[e.to]; const has = pk && photoOf(pk); return (
          <a key={e.to} href={href(e.to)} className={`entry ${has ? "has-photo" : ""}`}>{has && <Photo k={pk} alt="" sizes="(min-width: 700px) 200px, 33vw" />}<span className="entry-ic" aria-hidden="true">{e.icon}</span><span className="entry-lb">{e.label}</span><span className="entry-sub">{e.sub}</span></a>); })()
        ))}
      </nav>

      {today && (
        <Section title="La recette du jour">
          <Grid><RecipeCard r={today} /></Grid>
        </Section>
      )}
      {nextFetes.length > 0 && (
        <Section title="Fêtes à venir" more={<a href={href("/fetes")}>Toutes les fêtes →</a>}>
          {nextFetes.map((f) => (
            <div key={f.name} className="card pad">
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
