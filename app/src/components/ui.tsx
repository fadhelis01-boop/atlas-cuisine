import type { ReactNode } from "react";
import { ALLERGENS, MACRO_BY_ID } from "../lib/data";
import { evaluate, evaluateLines, verdict, type Verdict } from "../lib/engine";
import { href } from "../lib/router";
import { toggleFavorite, useProfile, useStore } from "../lib/store";
import { minutes } from "../lib/text";
import type { Recipe, RecipeLine } from "../lib/types";
import { Credit, Photo, photoOf } from "./photo";

/** Visuel de couverture généré (en attendant les photos du tournage, Tome 6). */
const KIND_EMOJI: Record<string, string> = { Pain: "🥖", Sauce: "🥫", Boisson: "🥤", Dessert: "🍰", "Goûter / dessert": "🥞", Entrée: "🥗", Base: "🫕", Accompagnement: "🍟", Plat: "🍲" };
const SPECIAL: Record<string, string> = {
  tajine_poulet_olives: "🫒", poulet_yassa: "🍋", dal_tadka: "🍛", spaghetti_carbonara: "🍝", boeuf_bourguignon: "🍷", pad_thai: "🍜", ratatouille: "🍆",
  baguette_24h: "🥖", mayonnaise: "🥚", crepes_bretonnes: "🥞", pizza_margherita: "🍕", pate_pizza: "🍕", naan: "🫓", pain_pita: "🫓", focaccia: "🌿",
  galette_complete: "🍳", frites_maison: "🍟", pesto: "🌿", guacamole: "🥑", chili_con_carne: "🌶️", riz_cantonais: "🍚", poulet_teriyaki: "🍗",
  houmous: "🧆", taboule_libanais: "🌿", shakshuka: "🍳", accras_morue: "🐟", veloute_potiron: "🎃", poulet_roti: "🍗", mousse_chocolat: "🍫",
  meringues: "☁️", banana_bread: "🍌", tiramisu: "☕", oranges_cannelle: "🍊", bissap: "🌺", citronnade_menthe: "🍋", lassi_mangue: "🥭", the_menthe: "🫖",
  jus_gingembre: "🫚", galette_rois: "👑", ketchup: "🍅", sauce_tomate: "🍅", harissa: "🌶️", mafe_poulet: "🥜", chorba: "🥣", quiche_lorraine: "🥧",
  gratin_dauphinois: "🥔", bouillon_volaille: "🍲", bouillon_legumes: "🥕", salade_carottes_cumin: "🥕", tzatziki: "🥒", pain_perdu: "🍞", riz_au_lait: "🍚",
};
const MACRO_HUE: Record<string, number> = { france: 12, europe_sud: 28, europe_nord: 200, maghreb: 38, afrique: 20, moyen_orient: 45, asie_sud: 32, asie_est: 0, asie_sud_est: 150, amerique_nord: 8, amerique_latine: 90, oceanie: 180 };

export function Cover({ r, big }: { r: Recipe; big?: boolean }) {
  const hue = MACRO_HUE[r.macro] ?? 20;
  const k = `recette/${r.id}`;
  return (
    <div className={big ? "cover cover-big" : "cover"} style={{ background: photoOf(k)?.color ?? `linear-gradient(135deg, hsl(${hue} 55% 82%), hsl(${(hue + 30) % 360} 45% 68%))` }}>
      {photoOf(k)
        ? <Photo k={k} alt={big ? `${r.title} (photo d'illustration)` : ""} eager={big} sizes={big ? "(min-width: 760px) 360px, 100vw" : "(min-width: 900px) 280px, (min-width: 600px) 45vw, 100vw"} />
        : <span aria-hidden="true">{SPECIAL[r.id] ?? KIND_EMOJI[r.kind] ?? "🍽️"}</span>}
    </div>
  );
}

export function DietBadges({ r, v, lines }: { r: Recipe; v?: Verdict; lines?: RecipeLine[] }) {
  const p = useProfile();
  const ev = lines ? evaluateLines(lines) : evaluate(r);
  const vv = v ?? verdict(r, p);
  const out: ReactNode[] = [];
  const porkLabel = ev.pork === "ok" ? "Sans porc" : ev.pork === "uncertain" ? "Porc possible" : null;
  if (porkLabel) out.push(<span key="p" className={`badge ${ev.pork === "ok" ? "ok" : "warn"}`}>{ev.pork === "ok" ? "✓" : "?"} {porkLabel}</span>);
  else out.push(<span key="p" className="badge bad">🐖 Contient du porc</span>);
  if (ev.alcohol === "ok") out.push(<span key="a" className="badge ok">✓ Sans alcool</span>);
  else if (ev.alcohol === "trace") out.push(<span key="a" className="badge info">~ Traces d'alcool</span>);
  else out.push(<span key="a" className="badge bad">🍷 {ev.alcohol === "violates" ? "Contient de l'alcool" : "Alcool possible"}</span>);
  if (vv.availability === "adaptable") out.push(<span key="v" className="badge info">🔄 {lines ? "Version adaptée affichée" : "Version adaptée disponible"} (à tester)</span>);
  if (vv.availability === "hidden") out.push(<span key="h" className="badge bad">⛔ Ne convient pas à ton foyer</span>);
  if (ev.allergens.size) out.push(<span key="al" className="badge neutral">Allergènes : {[...ev.allergens].map((a) => ALLERGENS[a]).join(", ")}</span>);
  return <div className="badges">{out}</div>;
}

export function RecipeCard({ r, note }: { r: Recipe; note?: ReactNode }) {
  const p = useProfile();
  const fav = useStore((s) => s.favorites.includes(r.id));
  const v = verdict(r, p);
  return (
    <article className={`card rcard ${v.availability === "hidden" ? "dim" : ""}`}>
      <a href={href(`/recette/${r.id}`)} className="rcard-link">
        <Cover r={r} />
        <div className="rcard-body">
          <h3>{r.title}</h3>
          <p className="meta">{MACRO_BY_ID[r.macro]?.emoji} {r.regionPath.slice(1).join(" › ") || r.regionPath[0]} · ⏱ {minutes(r.active)}{r.rest ? ` + ${minutes(r.rest)}` : ""} · {"●".repeat(r.level)}{"○".repeat(3 - Math.min(3, r.level))}</p>
          {v.availability === "adaptable" && <p className="meta adapt">🔄 {v.adapted?.variantName}</p>}
          {v.availability === "hidden" && <p className="meta bad-text">⛔ {v.reasons[0]}</p>}
          {note}
        </div>
      </a>
      <button className={`fav ${fav ? "on" : ""}`} onClick={() => toggleFavorite(r.id)} aria-pressed={fav} aria-label={fav ? `Retirer ${r.title} des favoris` : `Ajouter ${r.title} aux favoris`}>{fav ? "♥" : "♡"}</button>
    </article>
  );
}

export function Grid({ children }: { children: ReactNode }) { return <div className="grid">{children}</div>; }

export function Section({ title, children, more, id }: { title: string; children: ReactNode; more?: ReactNode; id?: string }) {
  return (
    <section className="section" id={id}>
      <div className="section-head"><h2>{title}</h2>{more}</div>
      {children}
    </section>
  );
}

export function Empty({ children }: { children: ReactNode }) { return <div className="empty">{children}</div>; }

export function Page({ title, sub, children, back, photo }: { title: string; sub?: ReactNode; children: ReactNode; back?: string; photo?: string }) {
  const withPhoto = photo && photoOf(photo);
  return (
    <main className="page" id="contenu">
      {back && <a className="back" href={href(back)}>← Retour</a>}
      {withPhoto ? (
        <figure className="hero-fig">
          <div className="photo-band"><Photo k={photo!} alt="" eager sizes="(min-width: 900px) 1056px, 100vw" /><div className="band-text"><h1>{title}</h1></div></div>
          <figcaption><Credit k={photo!} note={false} /></figcaption>
        </figure>
      ) : <h1>{title}</h1>}
      {sub && <p className="lead">{sub}</p>}
      {children}
    </main>
  );
}

/** Filtre les recettes selon le profil : masque celles qui ne conviennent pas (sauf si demandé). */
export function useVisible(list: Recipe[], showHidden = false) {
  const p = useProfile();
  return list.filter((r) => showHidden || verdict(r, p).availability !== "hidden");
}

export function Chip({ on, children, onClick }: { on?: boolean; children: ReactNode; onClick: () => void }) {
  return <button className={`chip ${on ? "on" : ""}`} aria-pressed={!!on} onClick={onClick}>{children}</button>;
}
