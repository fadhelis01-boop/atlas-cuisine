import { useMemo, useState } from "react";
import { INGREDIENT_NAMES, INGREDIENTS, RECIPE_BY_ID, RECIPES } from "../lib/data";
import { STAPLES, suggest, verdict } from "../lib/engine";
import { href } from "../lib/router";
import { setState, useProfile, useStore, type FridgeItem } from "../lib/store";
import { norm, search } from "../lib/text";
import { DLC_DDM } from "../lib/content";
import { Chip, Empty, Grid, Page, RecipeCard, Section } from "../components/ui";

/** Raccourcis : les ingrédients les plus courants, à toucher plutôt qu'à taper. */
const COMMON = ["Œuf entier (frais)", "Oignon jaune", "Ail", "Tomate", "Pomme de terre", "Riz long / basmati / thaï", "Pâtes sèches (spaghetti, penne…)",
  "Cuisse / pilon de poulet", "Bœuf haché", "Carotte", "Courgette", "Poivron (rouge/jaune/vert)", "Lait entier / demi-écrémé / écrémé", "Beurre doux / demi-sel",
  "Yaourt nature", "Citron", "Gruyère / comté / emmental / beaufort", "Coulis / passata / tomates pelées", "Pois chiches (secs / bocal)", "Banane", "Pain rassis (réservé)", "Persil plat / frisé"];
const short = (n: string) => n.split(" (")[0].split(" / ")[0];
const daysLeft = (d: string | null) => (d ? Math.ceil((new Date(d).getTime() - Date.now()) / 86400000) : null);

function IngredientPicker({ onPick, exclude }: { onPick: (n: string) => void; exclude: string[] }) {
  const [q, setQ] = useState("");
  // les ingrédients courants passent devant (« riz » → riz long avant riz gluant)
  const hits = q.length >= 2 ? search(INGREDIENT_NAMES.filter((n) => !exclude.includes(n)), q, (n) => [n], 30)
    .sort((a, b) => Number(COMMON.includes(b) || STAPLES.has(b)) - Number(COMMON.includes(a) || STAPLES.has(a))).slice(0, 8) : [];
  return (
    <div className="picker">
      <input type="search" value={q} onChange={(e) => setQ(e.target.value)} placeholder="Ajouter un ingrédient (ex. courgette, lentilles…)" aria-label="Ajouter un ingrédient" />
      {hits.length > 0 && (
        <ul className="picker-list" role="listbox">
          {hits.map((h) => <li key={h}><button onClick={() => { onPick(h); setQ(""); }}>{h}</button></li>)}
        </ul>
      )}
    </div>
  );
}

export default function Frigo() {
  const [tab, setTab] = useState<"cuisiner" | "frigo">("cuisiner");
  return (
    <Page photo="rubrique/frigo" title="Avec ce que j'ai" sub="Choisis tes ingrédients : ATLAS propose les recettes qui les utilisent, en priorité ceux qui arrivent à leur date limite.">
      <div className="seg" role="tablist">
        <button role="tab" aria-selected={tab === "cuisiner"} className={tab === "cuisiner" ? "on" : ""} onClick={() => setTab("cuisiner")}>Que cuisiner ?</button>
        <button role="tab" aria-selected={tab === "frigo"} className={tab === "frigo" ? "on" : ""} onClick={() => setTab("frigo")}>Mon frigo</button>
        <a className="btn small ghost" href={href("/courses")}>🛒 Liste de courses</a>
      </div>
      {tab === "cuisiner" ? <Cuisiner /> : <MonFrigo />}
    </Page>
  );
}

function Cuisiner() {
  const fridge = useStore((s) => s.fridge);
  const p = useProfile();
  const [have, setHave] = useState<string[]>(() => fridge.map((f) => f.ref));
  const [allUse, setAllUse] = useState(false);
  const expiring = useMemo(() => new Set(fridge.filter((f) => { const d = daysLeft(f.dlc); return d !== null && d <= 2; }).map((f) => f.ref)), [fridge]);
  const toggle = (n: string) => setHave((h) => (h.includes(n) ? h.filter((x) => x !== n) : [...h, n]));
  const res = useMemo(() => {
    const ok = RECIPES.filter((r) => verdict(r, p).availability !== "hidden" && r.role !== "boisson");
    let out = suggest(ok, new Set(have), expiring);
    if (allUse) out = out.filter((x) => x.coverage >= 0.6);
    return out;
  }, [have, expiring, p, allUse]);
  const buckets = { all: res.filter((x) => x.bucket === "all"), almost: res.filter((x) => x.bucket === "almost"), ideas: res.filter((x) => x.bucket === "ideas") };

  return (
    <>
      <IngredientPicker onPick={(n) => setHave((h) => [...h, n])} exclude={have} />
      <div className="chips" aria-label="Ingrédients sélectionnés">
        {have.map((h) => <Chip key={h} on onClick={() => toggle(h)}>{short(h)} ✕</Chip>)}
      </div>
      <details className="small"><summary>Raccourcis</summary>
        <div className="chips">{COMMON.filter((c) => !have.includes(c)).map((c) => <Chip key={c} onClick={() => toggle(c)}>+ {short(c)}</Chip>)}</div>
      </details>
      <p className="small">Toujours supposés présents (placard de base) : {[...STAPLES].map(short).join(", ")}.</p>
      <label className="switch"><input type="checkbox" checked={allUse} onChange={(e) => setAllUse(e.target.checked)} /> Je veux utiliser un maximum de ces ingrédients (anti-gaspi)</label>
      {!have.length && <Empty>Ajoute au moins un ingrédient. Astuce : remplis ton frigo une fois, il sera repris automatiquement.</Empty>}
      {have.length > 0 && !res.length && <Empty>Aucune recette pour l'instant avec ces ingrédients. Ajoute-en quelques-uns, ou regarde la <a href={href("/zero-dechet")}>rubrique zéro déchet</a>.</Empty>}
      {(["all", "almost", "ideas"] as const).map((b) => buckets[b].length > 0 && (
        <Section key={b} title={{ all: "✅ Tu as tout", almost: "🟡 Il te manque 1 ou 2 choses", ideas: "🔵 Idées inspirantes" }[b]}>
          <Grid>{buckets[b].map((x) => (
            <RecipeCard key={x.id} r={RECIPE_BY_ID[x.id]} note={<p className="small">
              {x.missing.length > 0 && <>Manque : {x.missing.map(short).join(", ")}. </>}
              {Object.entries(x.substitutes).map(([a, s]) => <span key={a}>{short(a)} → {s.map(short).join(", ")}. </span>)}
              {x.usesExpiring.length > 0 && <strong>♻️ Utilise {x.usesExpiring.map(short).join(", ")} (date proche). </strong>}
            </p>} />
          ))}</Grid>
        </Section>
      ))}
    </>
  );
}

function MonFrigo() {
  const fridge = useStore((s) => s.fridge);
  const [zone, setZone] = useState<FridgeItem["zone"]>("frigo");
  const add = (ref: string) => setState((s) => { s.fridge.push({ ref, dlc: null, zone, added: new Date().toISOString() }); });
  const sorted = [...fridge].sort((a, b) => (daysLeft(a.dlc) ?? 999) - (daysLeft(b.dlc) ?? 999));
  return (
    <>
      <div className="row">
        <label className="field inline">Zone
          <select value={zone} onChange={(e) => setZone(e.target.value as FridgeItem["zone"])}>
            <option value="frigo">Frigo</option><option value="congelateur">Congélateur</option><option value="placard">Placard</option>
          </select>
        </label>
        <IngredientPicker onPick={add} exclude={fridge.map((f) => f.ref)} />
      </div>
      {!fridge.length ? <Empty>Ton frigo virtuel est vide. Ajoute ce que tu as, avec la date limite : ATLAS te dira quoi cuisiner en premier.</Empty> : (
        <ul className="fridge">
          {sorted.map((f) => {
            const d = daysLeft(f.dlc);
            const cls = d === null ? "" : d < 0 ? "bad" : d <= 2 ? "warn" : "ok";
            return (
              <li key={f.ref} className={`card pad fitem ${cls}`}>
                <span className="fname">{short(f.ref)} <span className="meta">· {f.zone}{INGREDIENTS[f.ref] ? ` · ${INGREDIENTS[f.ref].section.split(" (")[0].split(",")[0]}` : ""}</span></span>
                <label className="field inline small">Date limite
                  <input type="date" value={f.dlc ?? ""} onChange={(e) => setState((s) => { const x = s.fridge.find((y) => y.ref === f.ref); if (x) x.dlc = e.target.value || null; })} />
                </label>
                {d !== null && <span className={`badge ${cls === "bad" ? "bad" : cls === "warn" ? "warn" : "ok"}`}>{d < 0 ? "Dépassée" : d === 0 ? "Aujourd'hui" : `J-${d}`}</span>}
                <button className="btn small ghost" onClick={() => setState((s) => { s.fridge = s.fridge.filter((y) => y.ref !== f.ref); })} aria-label={`Retirer ${short(f.ref)}`}>Utilisé ✓</button>
              </li>
            );
          })}
        </ul>
      )}
      <p className="small">{DLC_DDM}</p>
      <p className="small">Une date dépassée sur un produit frais (viande, poisson, laitages) : ne pas consommer. Sur une DDM : regarde, sens, goûte.</p>
      {fridge.some((f) => norm(f.ref).includes("pain")) && <p>♻️ Du pain rassis ? <a href={href("/recette/pain_perdu")}>Pain perdu</a>.</p>}
    </>
  );
}
