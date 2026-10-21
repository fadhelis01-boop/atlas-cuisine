import { useEffect, useState } from "react";
import { RECIPE_BY_ID } from "../lib/data";
import { decodeShare, mergeShopping, mergeWeek, type SharePayload } from "../lib/partage";
import { go, href } from "../lib/router";
import { getState, setState, uid } from "../lib/store";
import { toast } from "../lib/toast";
import { Page } from "../components/ui";
import { dayName } from "../lib/planner";

/** Réception d'une liste de courses ou d'une semaine envoyée par un proche : on montre, puis on ajoute sur demande. */
export default function Partage({ d }: { d: string }) {
  const [p, setP] = useState<SharePayload | null | undefined>(undefined);
  useEffect(() => { void decodeShare(d).then(setP); }, [d]);
  if (p === undefined) return <Page title="Partage reçu">{<p className="meta">Lecture du lien…</p>}</Page>;
  if (!p) return <Page title="Lien illisible"><p>Ce lien de partage est incomplet ou abîmé. Demande à la personne de te le renvoyer.</p><a className="btn" href={href("/")}>Accueil</a></Page>;
  if (p.kind === "courses") {
    const items = p.shopping ?? [];
    const add = () => {
      const { list, added } = mergeShopping(getState().shopping, items, uid);
      setState((s) => { s.shopping = list; });
      toast(added ? `${added} article${added > 1 ? "s" : ""} ajouté${added > 1 ? "s" : ""} à ta liste` : "Tout était déjà dans ta liste");
      go("/courses");
    };
    return (
      <Page title="Liste de courses reçue" sub={`${items.length} article${items.length > 1 ? "s" : ""}. Rien n'est ajouté tant que tu ne le demandes pas.`}>
        <ul className="shop">{items.slice(0, 80).map((i, n) => <li key={n}>{i.label} <span className="meta">· {i.section.split(" (")[0]}</span></li>)}</ul>
        <div className="row"><button className="btn" onClick={add}>Ajouter à ma liste</button><a className="btn ghost" href={href("/")}>Ignorer</a></div>
      </Page>
    );
  }
  const days = Object.entries(p.week ?? {}).sort(([a], [b]) => a.localeCompare(b));
  const known = (id?: string) => (id && RECIPE_BY_ID[id] ? RECIPE_BY_ID[id].title.split(" (")[0] : null);
  const add = () => {
    const { week, added } = mergeWeek(getState().week ?? {}, Object.fromEntries(days.map(([k, v]) => [k, Object.fromEntries(Object.entries(v).filter(([, id]) => RECIPE_BY_ID[id]))])));
    setState((s) => { s.week = week; });
    toast(added ? `${added} repas ajouté${added > 1 ? "s" : ""} à ta semaine (les cases déjà remplies n'ont pas bougé)` : "Ta semaine était déjà remplie ces jours-là");
    go("/semaine");
  };
  return (
    <Page title="Semaine reçue" sub="Les repas prévus par un proche. Les cases que tu as déjà remplies ne bougeront pas.">
      <ul>{days.map(([day, v]) => <li key={day}><strong>{dayName(day)}</strong> · {[known(v.midi) && `midi : ${known(v.midi)}`, known(v.soir) && `soir : ${known(v.soir)}`].filter(Boolean).join(" · ") || <span className="meta">rien de prévu</span>}</li>)}</ul>
      <div className="row"><button className="btn" onClick={add}>Ajouter à ma semaine</button><a className="btn ghost" href={href("/")}>Ignorer</a></div>
    </Page>
  );
}
