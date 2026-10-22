import { useMemo, useRef, useState } from "react";
import { INGREDIENT_NAMES, INGREDIENTS, RECIPES } from "../lib/data";
import { STAPLES, verdict } from "../lib/engine";
import { buildMenu, COURSES, pickIdeas, rankFor, type Course, type FridgeIdea, type FridgeMenu } from "../lib/frigo";
import { freshSeed } from "../lib/variete";
import { toast } from "../lib/toast";
import { href } from "../lib/router";
import { setState, uid, useProfile, useStore, type FridgeItem } from "../lib/store";
import { norm, search } from "../lib/text";
import { DLC_DDM } from "../lib/content";
import { Chip, Empty, Grid, Page, RecipeCard, Section } from "../components/ui";
import { Icon } from "../components/icons";

/** Raccourcis : les ingrédients les plus courants, à toucher plutôt qu'à taper. */
const COMMON = ["Œuf entier (frais)", "Oignon jaune", "Ail", "Tomate", "Pomme de terre", "Riz long / basmati / thaï", "Pâtes sèches (spaghetti, penne…)",
  "Cuisse / pilon de poulet", "Bœuf haché", "Carotte", "Courgette", "Poivron (rouge/jaune/vert)", "Lait entier / demi-écrémé / écrémé", "Beurre doux / demi-sel",
  "Yaourt nature", "Citron", "Gruyère / comté / emmental / beaufort", "Coulis / passata / tomates pelées", "Pois chiches (secs / bocal)", "Banane", "Pain rassis (réservé)", "Persil plat / frisé"];
// nom court lisible ; quelques noms du référentiel perdent leur sens une fois coupés (« Cuisse / pilon de poulet »)
const SHORT: Record<string, string> = { "Cuisse / pilon de poulet": "Poulet (cuisses)", "Œuf entier (frais)": "Œufs", "Pain rassis (réservé)": "Pain rassis",
  "Lait entier / demi-écrémé / écrémé": "Lait", "Riz long / basmati / thaï": "Riz", "Pâtes sèches (spaghetti, penne…)": "Pâtes", "Coulis / passata / tomates pelées": "Tomates en boîte" };
const short = (n: string) => SHORT[n] ?? n.split(" (")[0].split(" / ")[0];
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
      <div className="row frigo-head">
        <div className="seg" role="tablist" aria-label="Frigo">
          <button role="tab" aria-selected={tab === "cuisiner"} className={tab === "cuisiner" ? "on" : ""} onClick={() => setTab("cuisiner")}>Que cuisiner ?</button>
          <button role="tab" aria-selected={tab === "frigo"} className={tab === "frigo" ? "on" : ""} onClick={() => setTab("frigo")}>Mon frigo</button>
        </div>
        <a className="btn small ghost" href={href("/courses")}><Icon name="cart" size={18} /> Liste de courses</a>
      </div>
      {tab === "cuisiner" ? <Cuisiner /> : <MonFrigo />}
    </Page>
  );
}

// Placard : ce qu'on suppose toujours présent, en mots simples, modifiable (audit UX 2026-10-16 §2.6)
const PANTRY_LABEL: Record<string, string> = {
  "Sel fin / gros sel / fleur de sel": "sel", "Poivre noir / blanc / vert": "poivre", "Huile de tournesol / colza": "huile neutre",
  "Huile d'olive vierge extra": "huile d'olive", "Sucre blanc / roux / cassonade / vergeoise": "sucre", "Farine de blé T55": "farine",
  "Farine de blé T45": "farine fine (gâteaux)", "Vinaigre de cidre": "vinaigre", "Moutarde de Dijon": "moutarde",
  "Ail": "ail", "Oignon jaune": "oignons", "Concentré de tomate": "concentré de tomate", "Bouillon cube volaille": "bouillon cube",
  "Cumin (graines / moulu)": "cumin", "Paprika doux": "paprika", "Herbes de Provence": "herbes de Provence", "Laurier": "laurier",
  "Thym / romarin": "thym", "Sauce soja claire": "sauce soja", "Levure chimique": "levure chimique", "Fécule de maïs (maïzena)": "maïzena",
  "Curry (mélange)": "curry", "Riz long / basmati / thaï": "riz", "Pâtes sèches (spaghetti, penne…)": "pâtes",
};
const PANTRY_OPTIONS = Object.keys(PANTRY_LABEL);
const IDEAS = 6;
const TIMES = [[0, "Pas de limite"], [20, "20 min"], [30, "30 min"], [45, "45 min"], [60, "1 h"]] as const;

/** Ajoute à la liste de courses ce qui manque ; renvoie le nombre de lignes ajoutées. */
function addMissing(refs: string[], from: string): number {
  let added = 0;
  setState((s) => {
    for (const ref of refs) {
      if (s.shopping.some((x) => x.ref === ref && !x.done)) continue;
      s.shopping.push({ id: uid(), ref, label: short(ref), from, done: false, section: INGREDIENTS[ref]?.section ?? "Autres" }); added++;
    }
  });
  return added;
}

const notifyAdded = (n: number) => toast(n ? `${n} ajouté${n > 1 ? "s" : ""} aux courses` : "Déjà dans ta liste de courses", { link: { label: "Voir", to: "/courses" } });

function IdeaNote({ x }: { x: FridgeIdea }) {
  return (
    <div className="small idea-note">
      <p><strong>Utilise :</strong> {x.used.map(short).join(", ")}.{x.s.usesExpiring.length > 0 && <strong> Dont {x.s.usesExpiring.map(short).join(", ")} (date proche).</strong>}</p>
      {Object.entries(x.s.substitutes).map(([a, sub]) => <p key={a}>{short(a)} → {sub.map(short).join(", ")}.</p>)}
      {x.s.missing.length ? (
        <p>À acheter : {x.s.missing.map(short).join(", ")}.{" "}
          <button type="button" className="linkish" onClick={() => notifyAdded(addMissing(x.s.missing, x.r.title))}>
            Ajouter aux courses</button></p>
      ) : <p className="ok-text">Tu as tout (avec ton placard).</p>}
    </div>
  );
}

interface Launch { course: Course; seed: number; key: string; seen: string[]; menu?: FridgeMenu }

function Cuisiner() {
  const fridge = useStore((s) => s.fridge);
  const pantryList = useStore((s) => s.pantry) ?? [...STAPLES];
  const p = useProfile();
  const [have, setHave] = useState<string[]>(() => fridge.map((f) => f.ref));
  const [allUse, setAllUse] = useState(false);
  const [editPantry, setEditPantry] = useState(false);
  const [allCommon, setAllCommon] = useState(false);
  const [course, setCourse] = useState<Course>("plat");
  const [maxMinutes, setMaxMinutes] = useState(0);
  const [launch, setLaunch] = useState<Launch | null>(null);
  const [showAll, setShowAll] = useState(false);
  const resultsRef = useRef<HTMLDivElement>(null);
  const pantry = useMemo(() => new Set(pantryList), [pantryList.join("|")]); // eslint-disable-line react-hooks/exhaustive-deps
  const expiring = useMemo(() => new Set(fridge.filter((f) => { const d = daysLeft(f.dlc); return d !== null && d <= 2; }).map((f) => f.ref)), [fridge]);
  const toggle = (n: string) => setHave((h) => (h.includes(n) ? h.filter((x) => x !== n) : [...h, n]));
  const allowed = useMemo(() => RECIPES.filter((r) => verdict(r, p).availability !== "hidden"), [p]);
  const opts = { have, pantry, expiring, maxMinutes, useMost: allUse };
  const key = JSON.stringify([have, course, maxMinutes, allUse, pantryList]);
  const stale = !!launch && launch.key !== key;
  const ranked = useMemo(() => (launch && launch.course !== "menu" ? rankFor(allowed, launch.course, opts) : []),
    [launch?.key, launch?.course, allowed]); // eslint-disable-line react-hooks/exhaustive-deps
  const shown = launch && launch.course !== "menu" ? pickIdeas(ranked, IDEAS, launch.seed, new Set(launch.seen)) : [];
  const go = () => {
    const seed = freshSeed();
    setShowAll(false);
    setLaunch({ course, seed, key, seen: [], menu: course === "menu" ? buildMenu(allowed, opts, seed) : undefined });
    requestAnimationFrame(() => resultsRef.current?.scrollIntoView({ behavior: "smooth", block: "start" }));
  };
  const more = () => {
    if (!launch) return;
    const seed = freshSeed();
    if (launch.course === "menu") {
      const m = launch.menu!; const seen = [...launch.seen, ...[m.entree, m.plat, m.dessert].flatMap((x) => (x ? [x.r.id] : []))];
      setLaunch({ ...launch, seed, seen, menu: buildMenu(allowed, opts, seed, new Set(seen)) });
    } else setLaunch({ ...launch, seed, seen: [...launch.seen, ...shown.map((x) => x.r.id)] });
  };
  const swap = (slot: "entree" | "plat" | "dessert") => {
    if (!launch?.menu) return;
    const cur = launch.menu[slot]; const seen = new Set([...launch.seen, ...(cur ? [cur.r.id] : [])]);
    const next = pickIdeas(rankFor(allowed, slot, opts).filter((x) => !seen.has(x.r.id)), 1, freshSeed(), seen)[0];
    if (!next) { toast("Pas d'autre idée avec ces ingrédients : ajoute-en un ou enlève la limite de temps"); return; }
    setLaunch({ ...launch, seen: [...seen], menu: { ...launch.menu, [slot]: next } });
  };
  const commons = COMMON.filter((c) => !have.includes(c));

  return (
    <>
      <IngredientPicker onPick={(n) => setHave((h) => [...h, n])} exclude={have} />
      {have.length > 0 && <div className="chips" aria-label="Ingrédients sélectionnés">
        {have.map((h) => <Chip key={h} on onClick={() => toggle(h)}>{short(h)} <Icon name="close" size={16} /></Chip>)}
      </div>}
      {have.some((h) => !fridge.some((f) => f.ref === h)) && (
        <p className="small"><button type="button" className="linkish" onClick={() => {
          setState((s) => { for (const h of have) if (!s.fridge.some((f) => f.ref === h)) s.fridge.push({ ref: h, dlc: null, zone: "frigo", added: new Date().toISOString() }); });
          toast("Gardé dans Mon frigo : tu retrouveras cette sélection la prochaine fois");
        }}>Garder ces ingrédients dans Mon frigo</button> (sinon la sélection s'efface en quittant l'écran)</p>
      )}
      <p className="small strong-label">Touche ce que tu as :</p>
      <div className="chips">{(allCommon ? commons : commons.slice(0, 12)).map((c) => <Chip key={c} onClick={() => toggle(c)}>+ {short(c)}</Chip>)}
        {!allCommon && commons.length > 12 && <button type="button" className="chip" onClick={() => setAllCommon(true)}>Plus…</button>}</div>
      <p className="small pantry-line">
        <strong>Dans ton placard :</strong> {[...new Set(pantryList.map((x) => PANTRY_LABEL[x] ?? short(x).toLowerCase()))].join(", ")}.{" "}
        <button type="button" className="linkish" onClick={() => setEditPantry(!editPantry)}>{editPantry ? "Fermer" : "Modifier"}</button>
      </p>
      {editPantry && (
        <div className="chips" role="group" aria-label="Mon placard">
          {PANTRY_OPTIONS.map((x) => <Chip key={x} on={pantry.has(x)} onClick={() => setState((s) => { const cur = s.pantry ?? [...STAPLES]; s.pantry = cur.includes(x) ? cur.filter((y) => y !== x) : [...cur, x]; })}>{PANTRY_LABEL[x]}</Chip>)}
        </div>
      )}
      <p className="small strong-label">Ce que tu veux cuisiner :</p>
      <div className="seg seg-wrap" role="radiogroup" aria-label="Ce que tu veux cuisiner">
        {COURSES.map((c) => <button key={c.id} type="button" role="radio" aria-checked={course === c.id} className={course === c.id ? "on" : ""} onClick={() => setCourse(c.id)}>{c.label}</button>)}
      </div>
      <div className="row frigo-options">
        <label className="field inline">Temps
          <select value={maxMinutes} onChange={(e) => setMaxMinutes(Number(e.target.value))}>{TIMES.map(([v, l]) => <option key={v} value={v}>{l}</option>)}</select>
        </label>
        <label className="switch"><input type="checkbox" checked={allUse} onChange={(e) => setAllUse(e.target.checked)} /> Utiliser un maximum de ces ingrédients (anti-gaspi)</label>
      </div>
      <button type="button" className="btn big frigo-go" disabled={!have.length} onClick={go}>
        <Icon name="search" size={20} className="ic-inline" /> {have.length ? (course === "menu" ? "Composer mon menu" : "Trouver des idées") : "Choisis d'abord au moins un ingrédient"}
      </button>
      <div ref={resultsRef} aria-live="polite">
        {stale && <p className="notice">Ta sélection a changé. <button type="button" className="btn small" onClick={go}>Relancer</button></p>}
        {launch?.course === "menu" && launch.menu && <MenuResult m={launch.menu} onSwap={swap} onMore={more} />}
        {launch && launch.course !== "menu" && (shown.length ? (
          <Section title={<>{COURSES.find((c) => c.id === launch.course)!.label} avec ce que tu as <span className="meta">({ranked.length} possibles)</span></>}>
            <Grid>{(showAll ? ranked.slice(0, 48) : shown).map((x) => <RecipeCard key={x.r.id} r={x.r} note={<IdeaNote x={x} />} />)}</Grid>
            <div className="row">
              {!showAll && <button type="button" className="btn" onClick={more}><Icon name="refresh" size={18} className="ic-inline" /> D'autres idées</button>}
              {ranked.length > IDEAS && <button type="button" className="btn ghost" onClick={() => setShowAll(!showAll)}>{showAll ? "Revenir aux idées" : `Tout voir, du plus adapté au moins adapté (${Math.min(ranked.length, 48)})`}</button>}
            </div>
          </Section>
        ) : <NoIdea course={launch.course} maxMinutes={maxMinutes} />)}
      </div>
    </>
  );
}

function NoIdea({ course, maxMinutes }: { course: Course; maxMinutes: number }) {
  return (
    <Empty>
      Pas de {course === "dessert" ? "dessert" : course === "entree" ? "entrée" : "plat"} avec ces ingrédients et ton profil.
      {maxMinutes ? " Enlève la limite de temps, ou" : ""} ajoute un ingrédient, choisis un autre type de recette, ou regarde la <a href={href("/restes")}>cuisine des restes</a>.
    </Empty>
  );
}

function MenuResult({ m, onSwap, onMore }: { m: FridgeMenu; onSwap: (s: "entree" | "plat" | "dessert") => void; onMore: () => void }) {
  const slots = [["entree", "Entrée"], ["plat", "Plat"], ["dessert", "Dessert"]] as const;
  const missing = [...new Set(slots.flatMap(([k]) => m[k]?.s.missing ?? []))];
  return (
    <Section title="Ton menu avec ce que tu as">
      {slots.map(([k, label]) => (
        <div key={k} className="menu-slot">
          <div className="row"><h3 className="h4">{label}</h3>
            <button type="button" className="btn small ghost" onClick={() => onSwap(k)}><Icon name="refresh" size={16} className="ic-inline" /> Changer</button></div>
          {m[k] ? <RecipeCard r={m[k]!.r} note={<IdeaNote x={m[k]!} />} /> : <p className="small">Rien ne va avec tes ingrédients pour ce service : touche « Changer » après avoir ajouté un ingrédient.</p>}
        </div>
      ))}
      {m.leftover.length > 0 && <p className="small">Pas utilisé dans ce menu : {m.leftover.map(short).join(", ")}. Un autre menu les prendra peut-être.</p>}
      <div className="row">
        <button type="button" className="btn" onClick={onMore}><Icon name="refresh" size={18} className="ic-inline" /> Un autre menu</button>
        {missing.length > 0 && <button type="button" className="btn ghost" onClick={() => notifyAdded(addMissing(missing, "Menu du frigo"))}>
          <Icon name="cart" size={18} className="ic-inline" /> Ajouter ce qui manque aux courses ({missing.length})</button>}
      </div>
    </Section>
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
      {fridge.some((f) => norm(f.ref).includes("pain")) && <p><Icon name="recycle" size={16} className="ic-inline" /> Du pain rassis ? <a href={href("/recette/pain_perdu")}>Pain perdu</a>.</p>}
    </>
  );
}
