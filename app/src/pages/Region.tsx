import { ImportRow } from "../components/video";
import { useMemo, useState } from "react";
import { CATALOGUE, IMPORT_CAT_TO_MACRO, useImportLibrary, MACRO_BY_ID, recipesOfMacro } from "../lib/data";
import { useProfile } from "../lib/store";
import { Chip, Empty, MoreGrid, MoreList, Page, Section } from "../components/ui";
import { verdict } from "../lib/engine";
import type { MacroId } from "../lib/types";

const ROLE_LABEL: Record<string, string> = { entree: "Entrées", plat: "Plats", dessert: "Desserts", boisson: "Boissons", autre: "Pains, sauces & bases" };

export default function Region({ id }: { id: string }) {
  const IMPORT_LIBRARY = useImportLibrary();
  const m = MACRO_BY_ID[id as MacroId];
  const p = useProfile();
  const [role, setRole] = useState<string | null>(null);
  const [showHidden, setShowHidden] = useState(false);
  const [sub, setSub] = useState<string | null>(null);
  const all = useMemo(() => recipesOfMacro(id as MacroId), [id]);
  if (!m) return <Page title="Région inconnue">{null}</Page>;
  const subOf = (r: (typeof all)[number]) => r.regionPath[1] ?? r.regionPath[0];
  const subs = [...all.reduce((m2, r) => m2.set(subOf(r), (m2.get(subOf(r)) ?? 0) + 1), new Map<string, number>())].filter(([, n]) => n >= 3).sort((a, b) => b[1] - a[1]);
  const recipes = all.filter((r) => (!role || r.role === role) && (!sub || subOf(r) === sub) && (showHidden || verdict(r, p).availability !== "hidden"));
  const hiddenCount = all.filter((r) => verdict(r, p).availability === "hidden").length;
  const cat = CATALOGUE.filter((c) => c.macro === id);
  const regions = [...new Set(cat.map((c) => c.region))];
  const importCats = Object.entries(IMPORT_CAT_TO_MACRO).filter(([, ms]) => ms.includes(m.id)).map(([k]) => k);
  const imports = IMPORT_LIBRARY.filter((i) => importCats.includes(i.cat)).slice(0, id === "fusion" ? 60 : 12);

  return (
    <Page photo={`region/${m.id}`} title={m.name} sub={m.blurb} back="/explorer">
      <div className="chips" role="group" aria-label="Type de plat">
        <Chip on={!role} onClick={() => setRole(null)}>Tout</Chip>
        {Object.entries(ROLE_LABEL).filter(([k]) => all.some((r) => r.role === k)).map(([k, l]) => <Chip key={k} on={role === k} onClick={() => setRole(k)}>{l}</Chip>)}
      </div>
      {subs.length > 2 && (
        <div className="chips chips-scroll" role="group" aria-label="Pays ou région">
          <Chip on={!sub} onClick={() => setSub(null)}>Partout</Chip>
          {subs.map(([k, n]) => <Chip key={k} on={sub === k} onClick={() => setSub(sub === k ? null : k)}>{k} <span className="meta">{n}</span></Chip>)}
        </div>
      )}
      {id === "fusion" && <div className="card pad"><strong>Qu'est-ce que la food fusion ?</strong> Des plats qui marient plusieurs traditions (pizza au butter chicken, fish & chips en feuille de riz, tex-mex, sauces de snack franco-belges aux saveurs maghrébines…) ou dont l'origine ne se rattache pas à un seul pays. Chaque recette garde aussi sa cuisine principale pour la recherche par région.</div>}
      <Section title={`Recettes (${recipes.length})`}>
        {recipes.length ? <MoreGrid key={`${role}|${sub}|${showHidden}`} items={recipes} /> : <Empty>Aucune recette complète ne correspond encore pour cette région. Regarde le programme ci-dessous.</Empty>}
        {hiddenCount > 0 && <button className="btn small ghost" onClick={() => setShowHidden(!showHidden)}>{showHidden ? "Masquer" : "Afficher"} les {hiddenCount} recette(s) qui ne conviennent pas à ton foyer</button>}
      </Section>
      {imports.length > 0 && (
        <Section title="Dans tes imports" more={<a href={`#/imports?cat=${importCats[0]}`}>Tout voir →</a>}>
          <MoreList items={imports} step={6} render={(i) => <ImportRow key={i.url} i={i} />} />
        </Section>
      )}
      {cat.length > 0 && (
      <details className="section"><summary className="h3">Au programme : {cat.length} plats en préparation</summary>
        <p className="small">Le catalogue du Tome 4 : fiches en cours de rédaction et de test. Les pastilles porc/alcool sont des pré-évaluations ; le moteur recalculera sur la fiche complète.</p>
        {regions.map((rg) => (
          <details key={rg} className="card pad">
            <summary><strong>{rg}</strong> <span className="meta">({cat.filter((c) => c.region === rg).length})</span></summary>
            <ul className="cat-list">
              {cat.filter((c) => c.region === rg).map((c) => (
                <li key={c.title}>
                  <span>{c.title}</span>
                  <span className="meta"> · porc {c.pork} · alcool {c.alcohol} · enfants {c.kids || "—"}{c.notes ? ` · ${c.notes}` : ""}</span>
                </li>
              ))}
            </ul>
          </details>
        ))}
        <p className="small">Légende : ✅ sans · 🔄 adaptable · ❌ indissociable · ~ traces ; enfants ✓✓ très adapté, ✓ adaptable.</p>
      </details>
      )}
    </Page>
  );
}
