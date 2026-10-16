import { useState } from "react";
import { RECIPES } from "../lib/data";
import { verdict } from "../lib/engine";
import { useProfile } from "../lib/store";
import { PETIT_CHEF, SECURITE_ENFANTS } from "../lib/content";
import { Chip, Empty, MoreGrid, Page, RecipeCard, Section } from "../components/ui";
import { href } from "../lib/router";
import { kidFriendly } from "../lib/famille";
import { Icon } from "../components/icons";

const AGES = [[1, "Dès 1 an"], [3, "3-5 ans"], [6, "6-8 ans"], [9, "9-12 ans"]] as const;

export default function Enfants() {
  const p = useProfile();
  // la tranche d'âge du plus jeune enfant du profil est présélectionnée (audit famille)
  const bracket = (a: number) => (a < 3 ? 1 : a < 6 ? 3 : a < 9 ? 6 : 9);
  const [age, setAge] = useState<number>(p.kidsAge !== null ? bracket(p.kidsAge) : 3);
  const [noPork, setNoPork] = useState(p.noPork);
  const [quick, setQuick] = useState(false);
  const [role, setRole] = useState<string | null>(null);
  // Toujours sans alcool pour les enfants (Tome 1 §7.6) ; sans porc selon le choix.
  const kidProfile = { ...p, alcohol: "standard" as const, noPork };
  const list = RECIPES.filter((r) => r.age !== null && r.age <= age && (!quick || r.active <= 30) && (!role || r.role === role))
    .map((r) => ({ r, v: verdict(r, kidProfile) }))
    .filter((x) => x.v.availability !== "hidden")
    .sort((a, b) => Number(b.r.cats.includes("enfants")) - Number(a.r.cats.includes("enfants"))
      || Number(a.r.profile.includes("epice")) - Number(b.r.profile.includes("epice"))
      || (a.r.active + a.r.rest) - (b.r.active + b.r.rest));
  // rubriques famille (audit famille) : le soir de semaine, la cuisine d'avance
  const fam = RECIPES.filter((r) => r.role === "plat" && kidFriendly(r, { ...p, kidsAge: Math.max(age, p.kidsAge ?? age) }) && verdict(r, kidProfile).availability !== "hidden");
  const soirs = fam.filter((r) => r.active + r.rest <= 30 && !r.profile.includes("epice")).sort((a, b) => Number(b.cats.includes("enfants")) - Number(a.cats.includes("enfants")) || a.active - b.active).slice(0, 10);
  const dimanche = fam.filter((r) => /cong[eé]l/i.test(r.storage)).slice(0, 10);
  return (
    <Page photo="rubrique/enfants" title="Recettes pour enfants" sub="Par âge, toujours sans alcool, avec ou sans porc, et les règles de sécurité qui comptent." back="/explorer">
      <nav className="links fam-links" aria-label="Rubriques famille">
        <a className="pill" href={href("/pique-nique")}><Icon name="leaf" size={16} className="ic-inline" /> Pique-nique et gamelle</a>
        <a className="pill" href={href("/semaine")}><Icon name="calendar" size={16} className="ic-inline" /> La semaine des repas</a>
        <a className="pill" href={href("/restes")}><Icon name="plate" size={16} className="ic-inline" /> Avec les restes</a>
        <a className="pill" href={href("/recherche?q=l%C3%A9gumes%20cach%C3%A9s")}><Icon name="broccoli" size={16} className="ic-inline" /> Légumes bien cachés</a>
      </nav>
      {soirs.length > 0 && <Section title="Soirs de semaine : 30 min, qu'ils aiment"><div className="rail">{soirs.map((r) => <RecipeCard key={r.id} r={r} />)}</div></Section>}
      {dimanche.length > 0 && <Section title="Cuisine du dimanche : à doubler et congeler"><p className="small">Cuisine double le week-end, congèle la moitié en portions : un soir pressé, tu n'as qu'à réchauffer.</p><div className="rail">{dimanche.map((r) => <RecipeCard key={r.id} r={r} />)}</div></Section>}
      <h2 className="h3">Toutes les recettes par âge</h2>
      <div className="chips" role="group" aria-label="Âge">{AGES.map(([a, l]) => <Chip key={a} on={age === a} onClick={() => setAge(a)}>{l}</Chip>)}</div>
      <div className="chips">
        <Chip on={noPork} onClick={() => setNoPork(!noPork)}>Sans porc</Chip>
        <Chip on onClick={() => undefined}>Sans alcool (toujours)</Chip>
        <Chip on={quick} onClick={() => setQuick(!quick)}>30 min maximum</Chip>
      </div>
      <div className="chips chips-scroll" role="group" aria-label="Type de plat">
        {([[null, "Tout"], ["plat", "Plats"], ["entree", "Entrées"], ["dessert", "Desserts & goûters"], ["boisson", "Boissons"]] as const).map(([k, l]) => <Chip key={l} on={role === k} onClick={() => setRole(k)}>{l}</Chip>)}
      </div>
      {list.length ? <MoreGrid key={`${age}|${role}|${quick}|${noPork}`} items={list.map((x) => x.r)} note={(r) => { const v = list.find((x) => x.r === r)!.v; return v.availability === "adaptable" ? <p className="small"><Icon name="swap" size={14} className="ic-inline" /> À faire en {v.adapted?.variantName.toLowerCase()}.</p> : <p className="small"><Icon name="kid" size={14} className="ic-inline" /> {r.kids.replace(/\*\*/g, "")}</p>; }} /> : <Empty>Aucune recette pour ces critères.</Empty>}
      <Section title="Sécurité : ce qu'il faut savoir">
        <ul>{SECURITE_ENFANTS.map((s) => <li key={s}>{s}</li>)}</ul>
      </Section>
      <Section title="Petit chef : cuisiner avec les enfants">
        <table className="table"><tbody>{PETIT_CHEF.map((x) => <tr key={x.age}><th>{x.age}</th><td>{x.tasks}</td></tr>)}</tbody></table>
        <p className="small">Toujours avec un adulte. Les recettes « ✓✓ » sont celles où les enfants peuvent faire le plus de gestes.</p>
      </Section>
    </Page>
  );
}
