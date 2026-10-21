import { Icon } from "../components/icons";
import { useMemo, useState } from "react";
import { MACROS, RECIPES } from "../lib/data";
import { evaluate } from "../lib/engine";
import { useStore } from "../lib/store";
import { norm, search } from "../lib/text";
import { seasonFit, zoneOf } from "../lib/season";
import { Chip, Empty, Grid, Page, RecipeCard, useVisible } from "../components/ui";
import type { Recipe } from "../lib/types";

// Toutes les recettes, avec les filtres qu'attend un cuisinier amateur (audit UX, Tome 13 §11) :
// quoi (type de plat), combien de temps, quelle difficulté, quel budget, pour quelle occasion, et des tris utiles.
const TYPES: [string, string, (r: Recipe) => boolean][] = [
  ["entree", "Entrées", (r) => r.role === "entree"], ["plat", "Plats", (r) => r.role === "plat"], ["express", "Express 20 min", (r) => r.role === "plat" && r.active + r.rest <= 20],
  ["brunch", "Petit-déj & brunch", (r) => r.cats.includes("brunch")], ["salade", "Salades repas", (r) => r.cats.includes("salade")], ["dessert", "Desserts & goûters", (r) => r.role === "dessert"],
  ["boisson", "Boissons", (r) => r.role === "boisson"], ["sauce", "Sauces & condiments", (r) => r.kind === "Sauce" || r.kind === "Base"],
  ["pain", "Pains & viennoiseries", (r) => r.kind === "Pain"], ["accomp", "Accompagnements", (r) => r.kind === "Accompagnement"],
];
const TIMES: [string, string, number][] = [["15", "≤ 15 min", 15], ["30", "≤ 30 min", 30], ["60", "≤ 1 h", 60], ["120", "≤ 2 h", 120]];
const OCCASIONS = ["Repas de famille", "Apéritif dînatoire", "Anniversaire", "Noël", "Barbecue d'été", "Saint-Valentin", "Ramadan / Aïd", "Pâques", "Nouvel An chinois", "Chandeleur"];
const SORTS: [string, string][] = [["saison", "De saison d'abord"], ["rapide", "Les plus rapides"], ["facile", "Les plus faciles"], ["az", "A à Z"]];

export default function Catalogue({ q0 = "" }: { q0?: string }) {
  const [q, setQ] = useState(q0);
  const [type, setType] = useState<string | null>(null);
  const [time, setTime] = useState<number | null>(null);
  const [level, setLevel] = useState<number | null>(null);
  const [cheap, setCheap] = useState(false);
  const [occ, setOcc] = useState<string | null>(null);
  const [macro, setMacro] = useState<string | null>(null);
  const [veg, setVeg] = useState(false);
  const [video, setVideo] = useState(false);
  const [kids, setKids] = useState(false);
  const [sort, setSort] = useState("saison");
  const [limit, setLimit] = useState(48);
  const zone = zoneOf(useStore((s) => s.settings.zone));
  const visible = useVisible(RECIPES);
  const list = useMemo(() => {
    let l = visible.filter((r) => (!type || TYPES.find((t) => t[0] === type)![2](r)) && (!time || r.active + r.rest <= time) && (!level || r.level <= level)
      && (!cheap || r.cost === "€") && (!occ || r.fetes.includes(occ)) && (!macro || r.macro === macro) && (!veg || evaluate(r).flesh.length === 0)
      && (!video || (r.videoCount ?? r.videos.length) > 0) && (!kids || (r.age !== null && r.age <= 3)));
    if (q.trim()) l = search(l, q, (r) => [r.title, r.origin, r.regionPath.join(" "), r.ingredients.map((i) => i.label).join(" ")], 600);
    else if (sort === "saison") l = l.map((r) => [r, seasonFit(r, zone).score] as const).sort((a, b) => b[1] - a[1]).map(([r]) => r);
    else if (sort === "rapide") l = [...l].sort((a, b) => a.active + a.rest - (b.active + b.rest));
    else if (sort === "facile") l = [...l].sort((a, b) => a.level - b.level || a.ingredients.length - b.ingredients.length);
    else l = [...l].sort((a, b) => norm(a.title).localeCompare(norm(b.title)));
    return l;
  }, [visible, type, time, level, cheap, occ, macro, veg, video, kids, q, sort, zone]);
  const reset = () => { setType(null); setTime(null); setLevel(null); setCheap(false); setOcc(null); setMacro(null); setVeg(false); setVideo(false); setKids(false); setQ(""); };
  return (
    <Page title="Toutes les recettes" sub={`${visible.length} recettes adaptées à ton foyer. Combine les filtres : « plat, 30 min, facile, pas cher » ou « dessert pour Noël ».`} back="/explorer">
      <div className="searchbar"><input type="search" value={q} onChange={(e) => setQ(e.target.value)} placeholder="Nom, ingrédient, région…" aria-label="Chercher dans les recettes" /></div>
      <div className="filters">
        <div className="chips chips-scroll" role="group" aria-label="Type de plat"><Chip on={!type} onClick={() => setType(null)}>Tout</Chip>{TYPES.map(([k, l]) => <Chip key={k} on={type === k} onClick={() => setType(type === k ? null : k)}>{l}</Chip>)}</div>
        <div className="chips chips-scroll" role="group" aria-label="Temps total">{TIMES.map(([k, l, v]) => <Chip key={k} on={time === v} onClick={() => setTime(time === v ? null : v)}><Icon name="timer" size={16} className="ic-inline" /> {l}</Chip>)}
          <Chip on={level === 1} onClick={() => setLevel(level === 1 ? null : 1)}>● Facile</Chip><Chip on={level === 2} onClick={() => setLevel(level === 2 ? null : 2)}>●● Facile ou moyen</Chip>
          <Chip on={cheap} onClick={() => setCheap(!cheap)}>€ Petit budget</Chip></div>
        <div className="chips chips-scroll" role="group" aria-label="Préférences"><Chip on={veg} onClick={() => setVeg(!veg)}><Icon name="broccoli" size={16} className="ic-inline" /> Végétarien</Chip><Chip on={kids} onClick={() => setKids(!kids)}>🧒 Enfants dès 3 ans</Chip><Chip on={video} onClick={() => setVideo(!video)}>▶ Avec vidéo</Chip></div>
        <div className="row">
          <label className="field inline">Occasion <select value={occ ?? ""} onChange={(e) => setOcc(e.target.value || null)}><option value="">Toutes</option>{OCCASIONS.map((o) => <option key={o}>{o}</option>)}</select></label>
          <label className="field inline">Région <select value={macro ?? ""} onChange={(e) => setMacro(e.target.value || null)}><option value="">Toutes</option>{MACROS.filter((m) => m.id !== "fusion").map((m) => <option key={m.id} value={m.id}>{m.name}</option>)}</select></label>
          {!q && <label className="field inline">Trier <select value={sort} onChange={(e) => setSort(e.target.value)}>{SORTS.map(([k, l]) => <option key={k} value={k}>{l}</option>)}</select></label>}
          <button className="btn ghost small" onClick={reset}>Tout effacer</button>
        </div>
      </div>
      <p className="meta" role="status">{list.length} recette{list.length > 1 ? "s" : ""}</p>
      {list.length ? <Grid>{list.slice(0, limit).map((r) => <RecipeCard key={r.id} r={r} />)}</Grid> : <Empty>Aucune recette avec tous ces filtres : retire-en un.</Empty>}
      {list.length > limit && <button className="btn big" onClick={() => setLimit(limit + 48)}>Voir {Math.min(48, list.length - limit)} recettes de plus</button>}
    </Page>
  );
}
