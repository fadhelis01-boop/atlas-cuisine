import { ImportRow } from "../components/video";
import { useState } from "react";
import { useImportLibrary, RECIPES } from "../lib/data";
import { href } from "../lib/router";
import { Grid, Page, RecipeCard, Section, useVisible } from "../components/ui";

/** Calculateur de pâte en pourcentages boulangers (Tome 1 §10.4). Farine = 100 %. */
function DoughCalc() {
  const [flour, setFlour] = useState(500);
  const [hydra, setHydra] = useState(65);
  const [salt, setSalt] = useState(2);
  const [yeastType, setYeastType] = useState<"seche" | "fraiche">("seche");
  const [yeastPct, setYeastPct] = useState(1);
  const [pieces, setPieces] = useState(4);
  const water = Math.round((flour * hydra) / 100);
  const s = Math.round((flour * salt) / 10) / 10;
  const yDry = (flour * yeastPct) / 100;
  const y = yeastType === "seche" ? yDry : yDry * 3; // levure fraîche ≈ 3 × la sèche
  const total = flour + water + s + y;
  const PRESETS: [string, number, number, number][] = [["Pizza", 65, 2, 1], ["Pizza 24 h au froid", 65, 2, 0.4], ["Baguette 24 h", 70, 2, 0.15], ["Pain en cocotte", 76, 2, 0.4], ["Focaccia", 80, 2, 1], ["Naan", 60, 2, 1.2]];
  return (
    <div className="card pad calc">
      <div className="chips">{PRESETS.map(([n, h, sa, ye]) => <button key={n} className="chip" onClick={() => { setHydra(h); setSalt(sa); setYeastPct(ye); }}>{n}</button>)}</div>
      <div className="calc-grid">
        <label className="field">Farine (g)<input type="number" inputMode="numeric" value={flour} min={50} step={50} onChange={(e) => setFlour(Math.max(0, +e.target.value))} /></label>
        <label className="field">Hydratation : {hydra} %<input type="range" min={50} max={90} value={hydra} onChange={(e) => setHydra(+e.target.value)} /></label>
        <label className="field">Sel : {salt.toString().replace(".", ",")} %<input type="range" min={1} max={3} step={0.1} value={salt} onChange={(e) => setSalt(+e.target.value)} /></label>
        <label className="field">Levure (en % de levure sèche) : {yeastPct.toString().replace(".", ",")} %<input type="range" min={0.05} max={2} step={0.05} value={yeastPct} onChange={(e) => setYeastPct(+e.target.value)} /></label>
        <label className="field">Type de levure
          <select value={yeastType} onChange={(e) => setYeastType(e.target.value as "seche" | "fraiche")}><option value="seche">Sèche (sachet)</option><option value="fraiche">Fraîche (cube)</option></select>
        </label>
        <label className="field">Nombre de pâtons<input type="number" inputMode="numeric" min={1} value={pieces} onChange={(e) => setPieces(Math.max(1, +e.target.value))} /></label>
      </div>
      <table className="calc-out">
        <tbody>
          <tr><th>Farine</th><td>{flour} g</td></tr>
          <tr><th>Eau</th><td>{water} g (= ml)</td></tr>
          <tr><th>Sel</th><td>{s.toString().replace(".", ",")} g</td></tr>
          <tr><th>Levure {yeastType === "seche" ? "sèche" : "fraîche"}</th><td>{y < 1 ? `${Math.round(y * 10) / 10} g (une pincée)` : `${Math.round(y * 10) / 10} g`.replace(".", ",")}</td></tr>
          <tr><th>Poids d'un pâton</th><td>{Math.round(total / pieces)} g</td></tr>
        </tbody>
      </table>
      <p className="small">Ne confonds pas levure boulangère (sèche ou fraîche) et levure chimique. Farines : T45 pâtisserie, T55 usage courant et pizza, T65 baguette tradition, T80 et plus : semi-complète et complète.</p>
    </div>
  );
}

export default function Pains() {
  const IMPORT_LIBRARY = useImportLibrary();
  const list = useVisible(RECIPES.filter((r) => r.cats.includes("pains")));
  const tiktok = IMPORT_LIBRARY.filter((i) => i.cat === "pains");
  return (
    <Page photo="rubrique/pains" title="Pains, pâtes & bases" sub="Les recettes les plus simples et les plus réussies, faites avec un four ménager et le matériel d'une cuisine française." back="/explorer">
      <Grid>{list.map((r) => <RecipeCard key={r.id} r={r} />)}</Grid>
      <Section title="Calculateur de pâte"><DoughCalc /></Section>
      <Section title="Les bons réflexes au four ménager">
        <ul>
          <li><strong>Pierre à pizza</strong> → une plaque épaisse retournée, préchauffée 30 min.</li>
          <li><strong>Vapeur</strong> → un plat vide au fond du four, 150 ml d'eau chaude à l'enfournement (<a href={href("/technique/vapeur-four")}>technique</a>).</li>
          <li><strong>Tandoor</strong> → une poêle en fonte très chaude, avec couvercle (<a href={href("/technique/poele-tres-chaude")}>technique</a>).</li>
          <li><strong>Four ventilé</strong> → baisse de 20 °C par rapport à la recette en chaleur statique.</li>
        </ul>
      </Section>
      {tiktok.length > 0 && (
        <Section title={`Tes favoris TikTok : pains, pizzas, brioches (${tiktok.length})`}>
          <ul className="links-list">{tiktok.slice(0, 40).map((i) => <ImportRow key={i.url} i={i} />)}</ul>
          {tiktok.length > 40 && <a href="#/imports?cat=pains">Voir les {tiktok.length}</a>}
        </Section>
      )}
    </Page>
  );
}
