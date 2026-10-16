import { Icon } from "../components/icons";
import { useState } from "react";
import { CATALOGUE, useImportLibrary, MACROS, recipesOfMacro } from "../lib/data";
import { go, href } from "../lib/router";
import { Page, Section } from "../components/ui";
import { Photo, photoOf } from "../components/photo";

const TILE_PHOTO: Record<string, string> = { "/explorer": "rubrique/explorer", "/frigo": "rubrique/frigo", "/enfants": "rubrique/enfants", "/pains": "rubrique/pains",
  "/sauces": "rubrique/sauces", "/techniques": "rubrique/techniques", "/fetes": "rubrique/fetes", "/zero-dechet": "rubrique/zero_dechet", "/imports": "rubrique/imports", "/pique-nique": "rubrique/pique_nique" };

const CATS = [
  { to: "/recettes", icon: "search", label: "Toutes les recettes, avec filtres", sub: "type, temps, niveau, budget, occasion" },
  { to: "/apprendre", icon: "cap", label: "J'apprends à cuisiner", sub: "un parcours pas à pas pour débuter" },
  { to: "/techniques", icon: "knife", label: "Techniques de cuisine", sub: "71 fiches : chef, pâtissier, boulanger, chocolatier" },
  { to: "/dictionnaire", icon: "dictionary", label: "Dictionnaire des ingrédients", sub: "657 fiches illustrées, saisons, substituts, bien choisir" },
  { to: "/pains", icon: "bread", label: "Pains, pâtes & bases", sub: "baguette, pizza, naan, crêpes…" },
  { to: "/sauces", icon: "sauce", label: "Sauces maison", sub: "mayo, algérienne, samouraï, frites…" },
  { to: "/enfants", icon: "kid", label: "Recettes pour enfants", sub: "par âge, avec sécurité" },
  { to: "/fetes", icon: "cake", label: "Repas de fêtes", sub: "calendrier, menus, boissons" },
  { to: "/pique-nique", icon: "leaf", label: "Pique-nique et gamelle", sub: "enfants, grands, du monde, anti-gaspi" },
  { to: "/restes", icon: "plate", label: "Cuisine des restes", sub: "entrée, plat, sandwich, dessert ou menu complet" },
  { to: "/bien-choisir", icon: "cart", label: "Bien choisir, bien rattraper", sub: "maraîcher, boucher, poissonnier ; trop mûr, viande dure" },
  { to: "/zero-dechet", icon: "recycle", label: "Zéro déchet", sub: "épluchures, carcasses, conservation" },
];

export default function Explore() {
  const IMPORT_LIBRARY = useImportLibrary();
  const [q, setQ] = useState("");
  const [list, setList] = useState(false);
  return (
    <Page photo="rubrique/explorer" title="Explorer" sub="Les cuisines du monde classées par région, et les rubriques transversales.">
      <form role="search" className="searchbar" onSubmit={(e) => { e.preventDefault(); go(`/recherche?q=${encodeURIComponent(q)}`); }}>
        <input type="search" value={q} onChange={(e) => setQ(e.target.value)} placeholder="Nom de plat, pays, ingrédient" aria-label="Rechercher" />
        <button className="btn" type="submit">Chercher</button>
      </form>
      <Section title="L'atlas des cuisines" more={<button className="btn small ghost" onClick={() => setList(!list)}>{list ? "Vue cartes" : "Vue liste"}</button>}>
        <div className={list ? "macro-list" : "macros"}>
          {MACROS.map((m) => {
            const n = recipesOfMacro(m.id).length;
            const c = m.id === "fusion" ? IMPORT_LIBRARY.filter((x) => x.cat === "fusion").length : CATALOGUE.filter((x) => x.macro === m.id).length;
            return (
              <a key={m.id} href={href(`/region/${m.id}`)} className="macro card">
                {!list && photoOf(`region/${m.id}`) && <div className="thumb43"><Photo k={`region/${m.id}`} alt="" sizes="(min-width: 900px) 300px, 100vw" /></div>}
                <span className="macro-ic" aria-hidden="true"><Icon name={m.icon} size={30} /></span>
                <span className="macro-name">{m.name}</span>
                {!list && <span className="small">{m.blurb}</span>}
                <span className="meta">{n} recette{n > 1 ? "s" : ""} complète{n > 1 ? "s" : ""} · {c} {m.id === "fusion" ? "dans tes favoris" : "au programme"}</span>
              </a>
            );
          })}
        </div>
      </Section>
      <Section title="Rubriques">
        <nav className="entries">
          {CATS.map((e) => (() => { const pk = TILE_PHOTO[e.to]; const has = pk && photoOf(pk); return (
          <a key={e.to} href={href(e.to)} className={`entry ${has ? "has-photo" : ""}`}>{has && <Photo k={pk} alt="" sizes="(min-width: 700px) 200px, 33vw" />}<span className="entry-ic" aria-hidden="true"><Icon name={e.icon} size={34} /></span><span className="entry-lb">{e.label}</span><span className="entry-sub">{e.sub}</span></a>); })())}
        </nav>
      </Section>
    </Page>
  );
}
