import { Icon } from "./icons";
import { useState, type ReactNode } from "react";
import { ALLERGENS, MACRO_BY_ID } from "../lib/data";
import { evaluate, evaluateLines, verdict, type Verdict } from "../lib/engine";
import { goBack, href } from "../lib/router";
import { toggleFavorite, useProfile, useStore } from "../lib/store";
import { levelLabel, minutes } from "../lib/text";
import type { Recipe, RecipeLine } from "../lib/types";
import { Credit, Photo, photoOf } from "./photo";
import { IllustratedCover, MACRO_HUE, PatternBand, dishEmoji } from "./art";

/** Emoji choisis à la main pour les fiches étalons ; les autres sont déduits du titre (art.tsx). */
const SPECIAL: Record<string, string> = {
  tajine_poulet_olives: "🥗", poulet_yassa: "🍋", dal_tadka: "🍛", spaghetti_carbonara: "🍝", boeuf_bourguignon: "🍷", pad_thai: "🍜", ratatouille: "🍆",
  baguette_24h: "🥖", mayonnaise: "🥚", crepes_bretonnes: "🥞", pizza_margherita: "🍕", pate_pizza: "🍕", naan: "🥙", pain_pita: "🥙", focaccia: "🌿",
  galette_complete: "🍳", frites_maison: "🍟", pesto: "🌿", guacamole: "🥑", chili_con_carne: "🌶️", riz_cantonais: "🍚", poulet_teriyaki: "🍗",
  houmous: "🧆", taboule_libanais: "🌿", shakshuka: "🍳", accras_morue: "🐟", veloute_potiron: "🎃", poulet_roti: "🍗", mousse_chocolat: "🍫",
  meringues: "☁️", banana_bread: "🍌", tiramisu: "☕", oranges_cannelle: "🍊", bissap: "🌺", citronnade_menthe: "🍋", lassi_mangue: "🥭", the_menthe: "🍵",
  jus_gingembre: "🍹", galette_rois: "👑", ketchup: "🍅", sauce_tomate: "🍅", harissa: "🌶️", mafe_poulet: "🥜", chorba: "🥣", quiche_lorraine: "🥧",
  gratin_dauphinois: "🥔", bouillon_volaille: "🍲", bouillon_legumes: "🥕", salade_carottes_cumin: "🥕", tzatziki: "🥒", pain_perdu: "🍞", riz_au_lait: "🍚",
};

export function Cover({ r, big }: { r: Recipe; big?: boolean }) {
  const hue = MACRO_HUE[r.macro] ?? 20;
  const k = `recette/${r.id}`;
  const m = photoOf(k);
  return (
    <div className={big ? "cover cover-big" : "cover"} style={m ? { background: m.color ?? `hsl(${hue} 55% 82%)` } : undefined}>
      {m
        ? <Photo k={k} alt={big ? `${r.title} (photo d'illustration)` : ""} eager={big} sizes={big ? "(min-width: 760px) 360px, 100vw" : "(min-width: 900px) 280px, (min-width: 600px) 45vw, 100vw"} />
        : <IllustratedCover r={r} emoji={dishEmoji(r, SPECIAL[r.id])} />}
    </div>
  );
}

export function DietBadges({ r, v, lines }: { r: Recipe; v?: Verdict; lines?: RecipeLine[] }) {
  const p = useProfile();
  const ev = lines ? evaluateLines(lines) : evaluate(r);
  const vv = v ?? verdict(r, p);
  const out: ReactNode[] = [];
  const porkLabel = ev.pork === "ok" ? "Sans porc" : ev.pork === "uncertain" ? "Porc possible" : null;
  if (porkLabel) out.push(<span key="p" className={`badge ${ev.pork === "ok" ? "ok" : "warn"}`}>{ev.pork === "ok" ? <Icon name="check" size={15} className="ic-inline" /> : <Icon name="alert" size={15} className="ic-inline" />} {porkLabel}</span>);
  else out.push(<span key="p" className="badge bad"><Icon name="pig" size={15} className="ic-inline" /> Contient du porc</span>);
  if (ev.alcohol === "ok") out.push(<span key="a" className="badge ok"><Icon name="check" size={15} className="ic-inline" /> Sans alcool</span>);
  else if (ev.alcohol === "trace") out.push(<span key="a" className="badge info">~ Traces d'alcool</span>);
  else out.push(<span key="a" className="badge bad"><Icon name="wine" size={15} className="ic-inline" /> {ev.alcohol === "violates" ? "Contient de l'alcool" : "Alcool possible"}</span>);
  if (vv.availability === "adaptable") out.push(<span key="v" className="badge info"><Icon name="swap" size={15} className="ic-inline" /> {lines ? "Version adaptée affichée" : "Version adaptée disponible"} (à tester)</span>);
  if (vv.availability === "hidden") out.push(<span key="h" className="badge bad"><Icon name="ban" size={15} className="ic-inline" /> Ne convient pas à ton foyer</span>);
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
          <p className="meta"><Icon name={MACRO_BY_ID[r.macro]?.icon ?? "globe"} size={15} className="ic-inline" /> {r.regionPath.slice(1).join(" › ") || r.regionPath[0]} · <Icon name="timer" size={14} className="ic-inline" />{minutes(r.active)}{r.rest ? ` + ${minutes(r.rest)}` : ""} · {levelLabel(r.level)}</p>
          {v.availability === "adaptable" && <p className="meta adapt"><Icon name="swap" size={15} className="ic-inline" /> {v.adapted?.variantName}</p>}
          {v.availability === "hidden" && <p className="meta bad-text"><Icon name="ban" size={15} className="ic-inline" /> {v.reasons[0]}</p>}
          {note}
        </div>
      </a>
      <button className={`fav ${fav ? "on" : ""}`} onClick={() => toggleFavorite(r.id)} aria-pressed={fav} aria-label={fav ? `Retirer ${r.title} des favoris` : `Ajouter ${r.title} aux favoris`}><Icon name="heart" size={22} className={fav ? "ic-on" : ""} /></button>
    </article>
  );
}

export function Grid({ children }: { children: ReactNode }) { return <div className="grid">{children}</div>; }

export function Section({ title, children, more, id }: { title: ReactNode; children: ReactNode; more?: ReactNode; id?: string }) {
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
      {back && <a className="back" href={href(back)} onClick={(e) => { e.preventDefault(); goBack(back); }}><Icon name="back" size={20} /> Retour</a>}
      {withPhoto ? (
        <figure className="hero-fig">
          <div className="photo-band"><Photo k={photo!} alt="" eager sizes="(min-width: 900px) 1056px, 100vw" /><div className="band-text"><h1>{title}</h1></div></div>
          <figcaption><Credit k={photo!} note={false} /></figcaption>
        </figure>
      ) : <PatternBand seed={title}><h1>{title}</h1></PatternBand>}
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

/** Les longues listes s'affichent par paquets (audit UX 2026-10-16 §2.3) : moins de défilement, de mémoire et de bruit
 *  pour les lecteurs d'écran. `resetKey` remet le compteur à zéro quand un filtre change. */
export function useMore<T>(items: T[], step = 12) {
  const [n, setN] = useState(step);
  const shown = items.slice(0, n);
  const more = items.length > n ? (
    <button type="button" className="btn ghost more-btn" onClick={() => setN(n + step * 2)}>
      Voir {Math.min(step * 2, items.length - n)} de plus <span className="meta">({items.length - n} restantes)</span>
    </button>
  ) : null;
  return { shown, more, reset: () => setN(step) };
}

export function MoreGrid({ items, step = 12, note }: { items: Recipe[]; step?: number; note?: (r: Recipe) => ReactNode }) {
  const { shown, more } = useMore(items, step);
  return <><Grid>{shown.map((r) => <RecipeCard key={r.id} r={r} note={note?.(r)} />)}</Grid>{more}</>;
}

export function MoreList<T>({ items, step = 15, render, className = "links-list" }: { items: T[]; step?: number; render: (x: T) => ReactNode; className?: string }) {
  const { shown, more } = useMore(items, step);
  return <><ul className={className}>{shown.map(render)}</ul>{more}</>;
}
