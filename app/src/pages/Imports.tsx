import { Icon } from "../components/icons";
import { ImportRow, PlayButton, embedOf } from "../components/video";
import { useEffect, useMemo, useRef, useState } from "react";
import { IMPORT_CATS, useImportLibrary, INGREDIENTS, loadImports } from "../lib/data";
import { classify, linksFromExport, sourceOf, titleFromUrl, type Classified } from "../lib/classify";
import { canFetchMeta, fetchMeta } from "../lib/oembed";
import { getState, setState, uid, useStore, type MyImport } from "../lib/store";
import { search } from "../lib/text";
import { Chip, Empty, Page, Section } from "../components/ui";
import { safeHref, safeUrl } from "../lib/safe";

type Tab = "importer" | "mes" | "biblio";

// À l'ouverture de « Mes imports » : les liens encore non lus (titre = adresse, catégorie « à vérifier ») sont relus et triés.
let enriching = false;
async function enrichPending() {
  if (enriching || !navigator.onLine) return;
  enriching = true;
  try {
    const todo = getState().imports.filter((i) => i.cat === "a_verifier" && !i.caption && canFetchMeta(i.url)).slice(0, 40);
    for (const it of todo) {
      const m = await fetchMeta(it.url, 8000, 1);
      if (m) {
        const c0 = classify(m.title, it.url);
        const ac = c0.cat === "a_verifier" && m.author ? await creatorCat(m.author) : null;
        setState((s) => { const x = s.imports.find((i) => i.id === it.id); if (x) { x.title = c0.title || m.title; x.caption = m.title; x.cat = ac ?? c0.cat; x.macro = c0.macro; x.pork = c0.pork; x.alcohol = c0.alcohol; x.ingredients = c0.ingredients; x.author = m.author; } });
      }
      await new Promise((r) => setTimeout(r, 300));
    }
  } finally { enriching = false; }
}

export default function Imports({ q }: { q: URLSearchParams }) {
  const IMPORT_LIBRARY = useImportLibrary();
  useEffect(() => { void enrichPending(); }, []);
  const shared = q.get("partage");
  const [tab, setTab] = useState<Tab>(shared ? "importer" : q.get("cat") ? "biblio" : "mes");
  const mine = useStore((s) => s.imports);
  return (
    <Page photo="rubrique/imports" title="Mes imports" sub="Les recettes enregistrées sur TikTok, Instagram, YouTube ou ailleurs, triées automatiquement par catégorie.">
      <div className="seg" role="tablist">
        <button role="tab" aria-selected={tab === "importer"} className={tab === "importer" ? "on" : ""} onClick={() => setTab("importer")}>Importer</button>
        <button role="tab" aria-selected={tab === "mes"} className={tab === "mes" ? "on" : ""} onClick={() => setTab("mes")}>Mes imports ({mine.length})</button>
        <button role="tab" aria-selected={tab === "biblio"} className={tab === "biblio" ? "on" : ""} onClick={() => setTab("biblio")}>Favoris classés ({IMPORT_LIBRARY.length})</button>
      </div>
      {tab === "importer" && <Importer initial={shared ?? ""} onDone={() => setTab("mes")} />}
      {tab === "mes" && <MesImports />}
      {tab === "biblio" && <Bibliotheque cat0={q.get("cat")} />}
    </Page>
  );
}

/** Spécialité d'un créateur déjà classé (catégorie la plus fréquente) : sert quand le titre seul ne suffit pas. */
async function creatorCat(author: string): Promise<string | null> {
  const lib = await loadImports();
  const k = (a: string) => a.toLowerCase().replace(/[^a-z0-9]/g, "");
  const cnt = new Map<string, number>();
  for (const i of lib) if (i.author && i.cat !== "a_verifier" && k(i.author) === k(author)) cnt.set(i.cat, (cnt.get(i.cat) ?? 0) + 1);
  return [...cnt].sort((x, y) => y[1] - x[1])[0]?.[0] ?? null;
}

function Importer({ initial, onDone }: { initial: string; onDone: () => void }) {
  const IMPORT_LIBRARY = useImportLibrary();
  const initUrl = initial.match(/https?:\/\/\S+/)?.[0] ?? "";
  const [url, setUrl] = useState(initUrl);
  const [caption, setCaption] = useState(initial.replace(initUrl, "").trim());
  const [res, setRes] = useState<Classified | null>(null);
  const [title, setTitle] = useState("");
  const [cat, setCat] = useState("a_verifier");
  const [bulk, setBulk] = useState("");
  const [msg, setMsg] = useState("");
  const file = useRef<HTMLInputElement>(null);

  const [author, setAuthor] = useState("");
  const [busy, setBusy] = useState(false);
  const analyse = (cap = caption, u = url) => { const c = classify(cap, u); setRes(c); setTitle(c.title); setCat(c.cat); return c; };
  // Coller (ou partager) un lien suffit : titre, légende et auteur sont lus sur TikTok / YouTube / Vimeo, puis la recette est triée.
  // une lecture lancée avant que la légende change ne doit pas afficher un résultat périmé
  const latest = useRef(0);
  const auto = async (u: string, cap: string, saveAfter = false) => {
    if (!/^https?:\/\//.test(u)) return;
    const token = ++latest.current;
    let text = cap;
    if (canFetchMeta(u)) {
      setBusy(true);
      const m = await fetchMeta(u);
      setBusy(false);
      if (token !== latest.current) return;
      if (m) { setAuthor(m.author); if (!text) { text = m.title; setCaption(m.title); } }
      const c0 = classify(text, u);
      if (c0.cat === "a_verifier" && m?.author) { const ac = await creatorCat(m.author); if (token !== latest.current) return; if (ac) { const c = { ...c0, cat: ac }; setRes(c); setTitle(c.title); setCat(ac); if (saveAfter) doSave(c, u, text, c.title, ac, m.author); return; } }
    }
    const c = analyse(text, u);
    if (saveAfter) doSave(c, u, text, c.title, c.cat);
  };
  const doSave = (r: Classified, u: string, cap: string, t: string, ct: string, au = author) => {
    const safe = safeUrl(u);
    if (!safe) { setMsg("Colle un lien qui commence par https:// (TikTok, Instagram, YouTube, un site de recettes…)."); return; }
    u = safe;
    if (getState().imports.some((i) => i.url === u)) { setMsg("Ce lien est déjà dans tes imports."); return; }
    const item: MyImport = { id: uid(), url: u, title: t || titleFromUrl(u), caption: cap, source: sourceOf(u), cat: ct, macro: r.macro, pork: r.pork, alcohol: r.alcohol, ingredients: r.ingredients, steps: r.steps, added: new Date().toISOString(), notes: "", author: au };
    setState((s) => { s.imports.unshift(item); });
    setUrl(""); setCaption(""); setRes(null); setAuthor(""); setMsg(`Recette importée et classée dans « ${IMPORT_CATS[ct] ?? ct} ».`); onDone();
  };
  const save = () => { if (res) doSave(res, url, caption, title, cat); };
  useEffect(() => { if (initUrl) void auto(initUrl, caption, true); }, []); // partage depuis TikTok, YouTube… : tri et enregistrement immédiats
  const saveLinks = (links: string[]) => {
    const existing = new Set(useStoreSnapshot().map((i) => i.url));
    const fresh = links.map(safeUrl).filter((l): l is string => !!l && !existing.has(l));
    const lib = new Map(IMPORT_LIBRARY.map((i) => [i.url.split("?")[0], i]));
    setState((s) => {
      for (const l of fresh) {
        const known = lib.get(l.split("?")[0]); // déjà classé dans la bibliothèque : on reprend son tri
        s.imports.unshift({ id: uid(), url: l, title: known?.title ?? titleFromUrl(l), caption: "", source: sourceOf(l), cat: known?.cat ?? "a_verifier", macro: null,
          pork: known ? (known.pork ? "oui" : "doute") : "doute", alcohol: known ? (known.alcohol ? "oui" : "doute") : "doute", ingredients: [], steps: [], added: new Date().toISOString(), notes: "" });
      }
    });
    setMsg(`${fresh.length} lien(s) ajouté(s)${links.length - fresh.length ? `, ${links.length - fresh.length} déjà présent(s)` : ""}. Lecture des titres et tri automatique en cours…`);
    void enrich(fresh.filter((l) => !lib.has(l.split("?")[0]) && canFetchMeta(l)));
  };
  // tri automatique des liens importés en masse : un par un, gentiment (300 ms entre deux)
  const enrich = async (links: string[]) => {
    let n = 0;
    for (const l of links) {
      const m = await fetchMeta(l);
      if (m) {
        const c0 = classify(m.title, l);
        const ac = c0.cat === "a_verifier" && m.author ? await creatorCat(m.author) : null;
        const c = ac ? { ...c0, cat: ac } : c0;
        setState((s) => { const it = s.imports.find((i) => i.url === l); if (it) { it.title = c.title || m.title; it.caption = m.title; it.cat = c.cat; it.macro = c.macro; it.pork = c.pork; it.alcohol = c.alcohol; it.ingredients = c.ingredients; it.author = m.author; } });
        n++;
      }
      await new Promise((r) => setTimeout(r, 300));
    }
    setMsg(`${n} lien(s) classé(s) automatiquement à partir de leur titre et de leur légende.`);
  };

  return (
    <>
      <Section title="Une recette">
        <div className="form">
          <label className="field">Lien de la vidéo ou de la page
            <input type="url" inputMode="url" value={url} onChange={(e) => { setUrl(e.target.value); if (/^https?:\/\/\S+$/.test(e.target.value.trim()) && e.target.value.length - url.length > 10) void auto(e.target.value.trim(), caption); }} onBlur={() => { if (url && !res) void auto(url.trim(), caption); }} placeholder="https://www.tiktok.com/@…/video/…" />
          </label>
          {busy && <p className="small" role="status">Lecture du titre et de la légende…</p>}
          {author && <p className="small">Auteur·e : <strong>{author}</strong></p>}
          <label className="field">Légende ou texte de la recette (copie-colle la description de la vidéo)
            <textarea rows={6} value={caption} onChange={(e) => { setCaption(e.target.value); setRes(null); latest.current++; setBusy(false); }} placeholder={"Poulet yassa 🍋\nIngrédients : 4 cuisses de poulet, 6 oignons, 4 citrons…"} />
          </label>
          <button className="btn" onClick={() => void auto(url.trim(), caption)} disabled={(!url && !caption) || busy}>Analyser et trier</button>
          <p className="small">Astuce : colle juste le lien (TikTok, YouTube, Vimeo) : titre, légende et auteur sont lus automatiquement. Sur Android, utilise « Partager › ATLAS » depuis l'application TikTok ou YouTube : la recette est classée et enregistrée d'un geste.</p>
        </div>
        {res && (
          <div className="card pad">
            <label className="field">Titre<input value={title} onChange={(e) => setTitle(e.target.value)} /></label>
            <label className="field">Catégorie (tri automatique, modifiable)
              <select value={cat} onChange={(e) => setCat(e.target.value)}>{Object.entries(IMPORT_CATS).map(([k, l]) => <option key={k} value={k}>{l}</option>)}</select>
            </label>
            <p>
              <span className={`badge ${res.pork === "non" ? "ok" : res.pork === "oui" ? "bad" : "warn"}`}>🐖 Porc : {res.pork}</span>{" "}
              <span className={`badge ${res.alcohol === "non" ? "ok" : res.alcohol === "oui" ? "bad" : "warn"}`}>🍷 Alcool : {res.alcohol}</span>{" "}
              <span className="badge neutral">Non vérifié</span>
            </p>
            {res.ingredients.length > 0 && (
              <>
                <h3>Ingrédients repérés</h3>
                <ul>{res.ingredients.map((i, k) => <li key={k}>{i.text} {i.ref ? <span className="meta">→ {i.ref}{INGREDIENTS[i.ref].derivs.pork ? " 🐖" : ""}{INGREDIENTS[i.ref].derivs.alcohol ? " 🍷" : ""}</span> : <span className="meta">→ non reconnu</span>}</li>)}</ul>
              </>
            )}
            {res.warnings.map((w) => <p key={w} className="warn-text"><Icon name="alert" size={16} className="ic-inline" /> {w}</p>)}
            <p className="small">Une recette importée reste « non vérifiée » : en cas de doute, ATLAS indique « doute », jamais « sans porc ».</p>
            <button className="btn" onClick={save}>Enregistrer dans mes imports</button>
          </div>
        )}
      </Section>
      <Section title="Tous mes favoris TikTok d'un coup">
        <ol className="small">
          <li>Dans TikTok : <strong>Profil › ☰ › Paramètres et confidentialité › Compte › Télécharger tes données</strong>, format <strong>JSON</strong>. TikTok prépare le fichier (quelques heures à quelques jours).</li>
          <li>Télécharge-le, décompresse-le si besoin, puis choisis le fichier ici : ATLAS récupère les liens de tes favoris et de tes vidéos aimées, et reprend le tri déjà fait quand il les connaît.</li>
          <li>Pour une seule vidéo : bouton Partager › Copier le lien, puis colle-le ci-dessus avec la légende. Sur Android, une fois ATLAS installée, choisis directement « ATLAS » dans le menu Partager.</li>
        </ol>
        <div className="row">
          <button className="btn ghost" onClick={() => file.current?.click()}>Choisir le fichier d'export</button>
          <input ref={file} type="file" accept=".json,.txt,application/json,text/plain" hidden onChange={async (e) => {
            const f = e.target.files?.[0]; if (!f) return;
            const links = linksFromExport(await f.text());
            if (!links.length) setMsg("Aucun lien TikTok, Instagram, YouTube ou Pinterest trouvé dans ce fichier."); else saveLinks(links);
          }} />
        </div>
        <label className="field">…ou colle une liste de liens (un par ligne)
          <textarea rows={4} value={bulk} onChange={(e) => setBulk(e.target.value)} />
        </label>
        <button className="btn ghost" disabled={!bulk.trim()} onClick={() => { saveLinks(linksFromExport(bulk)); setBulk(""); }}>Ajouter ces liens</button>
        {msg && <p role="status" className="banner info">{msg}</p>}
        <p className="small">ATLAS ne télécharge jamais les vidéos : il garde le lien, le crédit de l'auteur·e et le texte (Tome 7 §7.5). TikTok ne permet pas à une application de lire directement les favoris d'un compte.</p>
      </Section>
    </>
  );
}

// accès ponctuel à l'état, hors rendu
const useStoreSnapshot = () => getState().imports;

function MesImports() {
  const mine = useStore((s) => s.imports);
  const [cat, setCat] = useState<string | null>(null);
  const cats = [...new Set(mine.map((i) => i.cat))];
  const list = mine.filter((i) => !cat || i.cat === cat);
  if (!mine.length) return <Empty>Aucun import pour l'instant. Onglet « Importer » : colle un lien et sa légende, ou importe tes favoris TikTok d'un coup.</Empty>;
  return (
    <>
      <div className="chips"><Chip on={!cat} onClick={() => setCat(null)}>Tout ({mine.length})</Chip>{cats.map((c) => <Chip key={c} on={cat === c} onClick={() => setCat(c)}>{IMPORT_CATS[c] ?? c} ({mine.filter((i) => i.cat === c).length})</Chip>)}</div>
      <ul className="imports">
        {list.map((i) => (
          <li key={i.id} className="card pad">
            <span className="row"><PlayButton v={{ title: i.title, url: i.url, embed: embedOf(i.url), source: i.source }} /><a href={safeHref(i.url)} target="_blank" rel="noopener noreferrer"><strong>{i.title}</strong></a></span>
            <p className="meta">{i.source}{i.author ? ` · ${i.author}` : ""} · ajouté le {new Date(i.added).toLocaleDateString("fr-FR")} · 🐖 {i.pork} · 🍷 {i.alcohol}</p>
            <div className="row">
              <select aria-label="Catégorie" value={i.cat} onChange={(e) => setState((s) => { const x = s.imports.find((y) => y.id === i.id); if (x) x.cat = e.target.value; })}>
                {Object.entries(IMPORT_CATS).map(([k, l]) => <option key={k} value={k}>{l}</option>)}
              </select>
              <button className="btn small ghost danger" onClick={() => setState((s) => { s.imports = s.imports.filter((y) => y.id !== i.id); })}>Supprimer</button>
            </div>
            {i.ingredients.length > 0 && <details><summary>Ingrédients ({i.ingredients.length})</summary><ul>{i.ingredients.map((x, k) => <li key={k}>{x.text}</li>)}</ul></details>}
          </li>
        ))}
      </ul>
    </>
  );
}

function Bibliotheque({ cat0 }: { cat0: string | null }) {
  const IMPORT_LIBRARY = useImportLibrary();
  const [cat, setCat] = useState<string | null>(cat0);
  const [source, setSource] = useState<string | null>(null);
  const [q, setQ] = useState("");
  const [noPork, setNoPork] = useState(false);
  const [noAlcohol, setNoAlcohol] = useState(false);
  const [channel, setChannel] = useState<string | null>(null);
  const [frOnly, setFrOnly] = useState(false);
  const channels = useMemo(() => [...new Set(IMPORT_LIBRARY.filter((i) => i.source === "YouTube").map((i) => i.author))], [IMPORT_LIBRARY]);
  const counts = useMemo(() => IMPORT_LIBRARY.reduce<Record<string, number>>((a, i) => ((a[i.cat] = (a[i.cat] ?? 0) + 1), a), {}), [IMPORT_LIBRARY]);
  let list = IMPORT_LIBRARY.filter((i) => (!cat || i.cat === cat) && (!source || i.source === source) && (!noPork || !i.pork) && (!noAlcohol || !i.alcohol)
    && (!channel || i.author === channel) && (!frOnly || !i.lang));
  if (q.trim()) list = search(list, q, (i) => [i.title, i.author, i.sub], 300);
  return (
    <>
      <p className="small">{IMPORT_LIBRARY.length} recettes en vidéo classées : tes favoris TikTok, les comptes La cuisine de Marina et NiangCook, le site Cooking with Morgane et 13 chaînes YouTube (Le Riz Jaune, L'Ardoise Porto-Vecchio, Armand Hasanpapaj, CookWithBash, ChesterFoodies, Cook with Nabeela…). Les pastilles 🐖/🍷 viennent du titre ou de la légende : à confirmer.</p>
      <input type="search" value={q} onChange={(e) => setQ(e.target.value)} placeholder="Chercher dans les favoris" aria-label="Chercher dans les favoris classés" />
      <div className="chips">
        <Chip on={!source} onClick={() => setSource(null)}>Toutes sources</Chip>
        {[...new Set(IMPORT_LIBRARY.map((i) => i.source))].map((s) => <Chip key={s} on={source === s} onClick={() => setSource(s)}>{s}</Chip>)}
        <Chip on={noPork} onClick={() => setNoPork(!noPork)}>Sans porc</Chip>
        <Chip on={noAlcohol} onClick={() => setNoAlcohol(!noAlcohol)}>Sans alcool</Chip>
        <Chip on={frOnly} onClick={() => setFrOnly(!frOnly)}>En français seulement</Chip>
      </div>
      {source === "YouTube" && (
        <div className="chips chips-scroll" role="group" aria-label="Chaînes YouTube">
          <Chip on={!channel} onClick={() => setChannel(null)}>Toutes les chaînes</Chip>
          {channels.map((c) => <Chip key={c} on={channel === c} onClick={() => setChannel(channel === c ? null : c)}>▶ {c}</Chip>)}
        </div>
      )}
      <div className="chips">
        <Chip on={!cat} onClick={() => setCat(null)}>Toutes</Chip>
        {Object.entries(IMPORT_CATS).filter(([k]) => counts[k]).map(([k, l]) => <Chip key={k} on={cat === k} onClick={() => setCat(k)}>{l} ({counts[k]})</Chip>)}
      </div>
      <ul className="links-list">
        {list.slice(0, 300).map((i) => <ImportRow key={i.url} i={i} />)}
      </ul>
      {list.length > 300 && <p className="small">300 premiers résultats sur {list.length} : affine avec la recherche.</p>}
    </>
  );
}
