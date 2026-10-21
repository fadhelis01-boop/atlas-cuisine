import { Icon } from "../components/icons";
import { useEffect, useMemo, useState } from "react";
import { RECIPE_BY_ID, loadLeftovers } from "../lib/data";
import { COST_PER_PART, autoPlan, consolidate, dayName, leftoverLink, prepAhead, weekDays, type Slot, type WeekPlan } from "../lib/planner";
import { householdLabel, householdPortions, weekBalance } from "../lib/famille";
import { restesOfRecipe } from "../lib/restes";
import { RECIPES } from "../lib/data";
import { verdict } from "../lib/engine";
import { seasonFit } from "../lib/season";
import { href } from "../lib/router";
import { zoneOf } from "../lib/season";
import { setState, uid, useProfile, useStore } from "../lib/store";
import { minutes } from "../lib/text";
import type { Leftover } from "../lib/types";
import { Chip, Cover, Page } from "../components/ui";
import { toast } from "../lib/toast";
import { encodeShare, shareUrl, weekToIcs } from "../lib/partage";
import { downloadText, sendLink } from "../lib/sendLink";

const SLOT_LABEL: Record<Slot, string> = { midi: "Midi", soir: "Soir" };
/** Libellé d'un accompagnement : fiche reliée ou produit à acheter. */
export const sideLabel = (side: string) => side.startsWith("achat:") ? side.slice(6).split(" (")[0].split(" / ")[0].toLowerCase() : (RECIPE_BY_ID[side]?.title.split(" (")[0].toLowerCase() ?? side);
const DEFAULT_PREFS = { people: 2, slots: ["soir"] as Slot[], weekdayMax: 45 };
const shortDate = (iso: string) => new Date(iso + "T12:00:00").toLocaleDateString("fr-FR", { day: "numeric", month: "short" });

/** Planificateur de la semaine (audit 🔴 4) : 7 jours remplis selon la saison et le temps disponible,
 *  restes d'un plat réutilisés le lendemain, une seule liste de courses, et ce qui se prépare à l'avance. */
export default function Semaine({ add }: { add: string | null }) {
  const profile = useProfile();
  const zoneSetting = useStore((s) => s.settings.zone);
  const plan = useStore((s) => s.week) ?? {};
  const prefs = useStore((s) => s.weekPrefs) ?? { ...DEFAULT_PREFS, people: householdPortions(profile) ?? DEFAULT_PREFS.people };
  const [offset, setOffset] = useState(0);
  const [msg, setMsg] = useState("");
  const [left, setLeft] = useState<Record<string, Leftover[]> | null>(null);
  useEffect(() => { void loadLeftovers().then(setLeft); }, []);
  const days = useMemo(() => weekDays(offset), [offset]);
  const adding = add ? RECIPE_BY_ID[add] : undefined;

  const save = (next: WeekPlan) => setState((s) => {
    // on ne garde que les semaines en cours et à venir : le planning ne grossit pas indéfiniment
    const from = weekDays(0)[0];
    s.week = Object.fromEntries(Object.entries(next).filter(([d, v]) => d >= from && (v.midi || v.soir)));
    // mémoire du planificateur (audit gourmet) : la dernière date de chaque plat, gardée 8 semaines
    const h = { ...(s.weekHistory ?? {}) };
    for (const [d, v] of Object.entries(s.week)) for (const id of [v.midi, v.soir]) if (id && (!h[id] || h[id] < d)) h[id] = d;
    const limit = new Date(Date.now() - 70 * 86400000).toISOString().slice(0, 10);
    s.weekHistory = Object.fromEntries(Object.entries(h).filter(([, d]) => d >= limit));
  });
  const history = useStore((s) => s.weekHistory);
  const journal = useStore((s) => s.journal);
  const kidsVerdict = useMemo(() => Object.fromEntries(Object.entries(journal ?? {}).filter(([, e]) => e.kids).map(([id, e]) => [id, e.kids!])), [journal]);
  // plats vus dans les 8 semaines qui précèdent les jours affichés (hors ces jours-là)
  const recent = useMemo(() => {
    const first = new Date(`${days[0]}T12:00:00`).getTime();
    return new Set(Object.entries(history ?? {}).filter(([, d]) => !days.includes(d) && Math.abs(new Date(`${d}T12:00:00`).getTime() - first) < 56 * 86400000).map(([id]) => id));
  }, [history, days]);
  const setPrefs = (p: Partial<typeof prefs>) => setState((s) => { s.weekPrefs = { ...prefs, ...p }; });
  const fill = (base: WeekPlan, onlyDays = days) => {
    if (!left) return;
    save(autoPlan(onlyDays, base, { slots: prefs.slots, weekdayMax: prefs.weekdayMax, zone: zoneOf(zoneSetting), profile, leftovers: left, seed: Date.now(), recent, sundayMenu: prefs.slots.includes("midi"), kidsVerdict }));
  };
  const clearWeek = () => { const next = { ...plan }; for (const d of days) delete next[d]; return next; };
  const reroll = (day: string, slot: Slot) => {
    const cur = plan[day]?.[slot];
    const next: WeekPlan = { ...plan, [day]: { ...plan[day], [slot]: undefined } };
    if (!left) return;
    const filled = autoPlan(days, next, { slots: prefs.slots.includes(slot) ? prefs.slots : [...prefs.slots, slot], weekdayMax: prefs.weekdayMax, zone: zoneOf(zoneSetting), profile, leftovers: left, seed: Date.now(), recent: new Set([...recent, ...(cur ? [cur] : [])]) });
    // ne remplir que la case demandée, et pas avec le même plat
    const pick = filled[day]?.[slot];
    save({ ...plan, [day]: { ...plan[day], [slot]: pick && pick !== cur ? pick : undefined } });
  };
  const remove = (day: string, slot: Slot) => save({ ...plan, [day]: { ...plan[day], [slot]: undefined } });
  const put = (day: string, slot: Slot, id: string) => { save({ ...plan, [day]: { ...plan[day], [slot]: id } }); setMsg(`${RECIPE_BY_ID[id].title.split(" (")[0]} : ajouté le ${dayName(day)} ${SLOT_LABEL[slot].toLowerCase()}.`); };

  const planned = days.flatMap((d) => (["midi", "soir"] as Slot[]).map((s) => plan[d]?.[s]).filter(Boolean) as string[]);
  const extras = days.flatMap((d) => [plan[d]?.entree, plan[d]?.dessert]).filter(Boolean) as string[];
  const shop = () => {
    const lines = consolidate([...planned, ...extras].map((id) => ({ id, factor: prefs.people / (RECIPE_BY_ID[id]?.portions || prefs.people) })));
    setState((s) => {
      s.shopping = s.shopping.filter((i) => i.from !== "Ma semaine");
      for (const l of lines) s.shopping.push({ id: uid(), ref: l.ref, label: l.label, from: "Ma semaine", done: false, section: l.section });
    });
    setMsg(`${lines.length} articles dans la liste de courses, quantités additionnées pour ${prefs.people} personne${prefs.people > 1 ? "s" : ""}.`);
  };
  // pour la personne qui fait les courses ou qui cuisine aussi : le planning en texte, à envoyer
  const shareWeek = async () => {
    const text = ["Ma semaine ATLAS", ...days.map((d) => { const m = (["midi", "soir"] as Slot[]).map((sl) => plan[d]?.[sl] && `${SLOT_LABEL[sl].toLowerCase()} : ${RECIPE_BY_ID[plan[d]![sl]!]?.title.split(" (")[0]}`).filter(Boolean); return m.length ? `${dayName(d)} ${shortDate(d)} · ${m.join(" · ")}` : null; }).filter(Boolean)].join("\n");
    try { if (navigator.share) await navigator.share({ title: "Ma semaine ATLAS", text }); else { await navigator.clipboard.writeText(text); toast("Planning copié : colle-le dans un message"); } } catch { /* annulé */ }
  };
  // la semaine dans un lien (l'autre téléphone l'ajoute à la sienne) ou dans l'agenda (audit dév/UX 2026-10-21 §2.7)
  const sendWeek = async () => {
    const week = Object.fromEntries(days.filter((d) => plan[d]).map((d) => [d, plan[d]!]));
    await sendLink("Ma semaine ATLAS", "Ma semaine ATLAS : ouvre le lien pour l'ajouter à ta semaine.", shareUrl(await encodeShare({ v: 1, kind: "semaine", week })));
  };
  const exportIcs = () => {
    const week = Object.fromEntries(days.filter((d) => plan[d]).map((d) => [d, plan[d]!]));
    downloadText(`atlas-semaine-${days[0]}.ics`, weekToIcs(week, (id) => RECIPE_BY_ID[id]?.title.split(" (")[0], (id) => `${location.origin}${location.pathname}#/recette/${id}`), "text/calendar");
    toast("Agenda téléchargé : ouvre le fichier pour ajouter les repas à ton calendrier");
  };
  const prep = useMemo(() => prepAhead(planned), [planned.join()]);
  // boisson maison de la semaine (audit gourmet) : sans alcool, de saison, change chaque semaine
  const drink = useMemo(() => {
    const zone = zoneOf(zoneSetting);
    const list = RECIPES.filter((r) => r.role === "boisson" && verdict(r, { ...profile, alcohol: "standard" }).availability === "ok" && r.active <= 20).sort((a, b) => seasonFit(b, zone).score - seasonFit(a, zone).score).slice(0, 12);
    return list.length ? list[Math.floor(new Date(`${days[0]}T12:00:00`).getTime() / (7 * 86400000)) % list.length] : null;
  }, [days, zoneSetting, profile]);
  const balance = useMemo(() => weekBalance(planned.map((id) => RECIPE_BY_ID[id]).filter(Boolean)), [planned.join()]);
  const budget = Math.round(planned.reduce((a, id) => a + (COST_PER_PART[RECIPE_BY_ID[id]?.cost ?? "€€"] ?? 4), 0) * prefs.people / 5) * 5;
  const slotsShown: Slot[] = (["midi", "soir"] as Slot[]).filter((s) => prefs.slots.includes(s) || days.some((d) => plan[d]?.[s]));

  return (
    <Page title="Ma semaine" sub="Les repas des 7 prochains jours : de saison, rapides en semaine, variés, et les restes d'un jour servent le lendemain." back="/">
      {adding && (
        <div className="banner info week-add" role="group" aria-label="Choisir le jour">
          <p>Où placer <strong>{adding.title.split(" (")[0]}</strong> ?</p>
          <div className="week-add-grid">
            {days.map((d) => (
              <span key={d} className="week-add-day">
                <span className="meta">{dayName(d).slice(0, 3)} {shortDate(d)}</span>
                {(["midi", "soir"] as Slot[]).map((s) => (
                  <button key={s} className={`btn small ${plan[d]?.[s] === adding.id ? "" : "ghost"}`} onClick={() => put(d, s, adding.id)}>{SLOT_LABEL[s]}</button>
                ))}
              </span>
            ))}
          </div>
        </div>
      )}

      <div className="week-prefs card pad">
        <label className="field inline">Personnes <input type="number" min={1} max={20} value={prefs.people} onChange={(e) => setPrefs({ people: Math.max(1, +e.target.value || 1) })} /></label>
        <span className="chips" role="group" aria-label="Repas à prévoir">
          {(["midi", "soir"] as Slot[]).map((s) => (
            <Chip key={s} on={prefs.slots.includes(s)} onClick={() => { const n = prefs.slots.includes(s) ? prefs.slots.filter((x) => x !== s) : [...prefs.slots, s]; if (n.length) setPrefs({ slots: (["midi", "soir"] as Slot[]).filter((x) => n.includes(x)) }); }}>{SLOT_LABEL[s]}</Chip>
          ))}
        </span>
        <label className="field inline">En semaine, au plus
          <select value={prefs.weekdayMax} onChange={(e) => setPrefs({ weekdayMax: +e.target.value })}>
            {[20, 30, 45, 60, 90].map((m) => <option key={m} value={m}>{minutes(m)}</option>)}
          </select>
        </label>
      </div>

      <div className="row week-nav">
        <button className="btn ghost small" disabled={offset === 0} onClick={() => setOffset(0)}>Les 7 prochains jours</button>
        <button className="btn ghost small" disabled={offset === 1} onClick={() => setOffset(1)}>Les 7 suivants</button>
        <span className="grow" />
        <button className="btn" disabled={!left} onClick={() => fill(plan)}><Icon name="calendar" size={20} /> Compléter les cases vides</button>
        <button className="btn ghost" disabled={!left} onClick={() => { const before = structuredClone(plan); fill(clearWeek()); if (planned.length) toast("Nouvelle semaine proposée", { undo: () => save(before) }); }}>Tout reproposer</button>
      </div>
      {msg && <p role="status" className="banner info">{msg} <a href={href("/courses")}>Voir les courses</a></p>}

      <ol className="week">
        {days.map((d, i) => (
          <li key={d} className={`week-day ${[0, 6].includes(new Date(`${d}T12:00:00`).getDay()) ? "weekend" : ""}`}>
            <h2 className="h3">{dayName(d)} <span className="meta">{shortDate(d)}</span></h2>
            {slotsShown.map((s) => {
              const id = plan[d]?.[s]; const r = id ? RECIPE_BY_ID[id] : undefined;
              const prevId = s === "soir" ? plan[d]?.midi ?? plan[days[i - 1]]?.soir : plan[days[i - 1]]?.soir ?? plan[days[i - 1]]?.midi;
              const link = leftoverLink(prevId, id, left);
              return (
                <div key={s} className="week-slot">
                  <span className="week-slot-lb">{SLOT_LABEL[s]}</span>
                  {r ? (
                    <>
                      <a className="week-meal" href={href(`/recette/${r.id}?portions=${prefs.people}`)}>
                        <Cover r={r} />
                        <span><strong>{r.title.split(" (")[0]}</strong><br /><span className="meta">{minutes(r.active)}{r.rest > 0 ? ` + ${minutes(r.rest)} sans rien faire` : ""}</span>
                          {link && <><br /><span className="small week-left"><Icon name="recycle" size={15} className="ic-inline" /> utilise le reste de {link} de la veille</span></>}
                          {r.side && <><br /><span className="small">avec {sideLabel(r.side)}</span></>}</span>
                      </a>
                      <span className="week-acts">
                        <button className="btn ghost small" title="Proposer un autre plat" aria-label={`Autre plat pour ${dayName(d)} ${s}`} onClick={() => reroll(d, s)}><Icon name="refresh" size={18} /></button>
                        <button className="btn ghost small" title="Retirer" aria-label={`Retirer le plat de ${dayName(d)} ${s}`} onClick={() => remove(d, s)}><Icon name="close" size={18} /></button>
                      </span>
                    </>
                  ) : (
                    <button className="btn ghost small week-empty" disabled={!left} onClick={() => reroll(d, s)}>+ Proposer un plat</button>
                  )}
                </div>
              );
            })}
            {(plan[d]?.entree || plan[d]?.dessert) && (
              <p className="small week-sunday"><Icon name="plate" size={15} className="ic-inline" /> Menu du dimanche :{" "}
                {plan[d]?.entree && RECIPE_BY_ID[plan[d]!.entree!] && <>en entrée <a href={href(`/recette/${plan[d]!.entree}`)}>{RECIPE_BY_ID[plan[d]!.entree!].title.split(" (")[0]}</a></>}
                {plan[d]?.dessert && RECIPE_BY_ID[plan[d]!.dessert!] && <>, en dessert <a href={href(`/recette/${plan[d]!.dessert}`)}>{RECIPE_BY_ID[plan[d]!.dessert!].title.split(" (")[0]}</a></>}
                {" "}<button className="btn ghost small" onClick={() => save({ ...plan, [d]: { ...plan[d], entree: undefined, dessert: undefined } })}>Retirer</button></p>
            )}
            {new Date(`${d}T12:00:00`).getDay() === 1 && i > 0 && (() => {
              const sun = plan[days[i - 1]]?.midi ?? plan[days[i - 1]]?.soir; const sr = sun ? RECIPE_BY_ID[sun] : null; const rs = sr ? restesOfRecipe(sr) : [];
              return rs.length ? <p className="small week-left"><Icon name="recycle" size={15} className="ic-inline" /> Restes du dimanche : <a href={href(`/restes?r=${rs.map((x) => x.id).join(",")}`)}>idées pour ce soir</a></p> : null;
            })()}
          </li>
        ))}
      </ol>
      {drink && <p className="small"><Icon name="cup" size={15} className="ic-inline" /> La boisson maison de la semaine : <a href={href(`/recette/${drink.id}`)}>{drink.title.split(" (")[0]}</a>, à préparer en carafe pour les repas.</p>}
      <p className="small">Pour placer une recette précise : sur sa fiche, touche « Planifier ». Les plats proposés respectent ton profil (porc, alcool, allergies) et la saison de l'endroit où tu es.</p>

      {planned.length > 0 && (
        <>
          <section className="section">
            <h2 className="h3"><Icon name="cart" size={22} className="ic-inline" /> Les courses de la semaine</h2>
            <p className="small">Un seul article par produit, quantités additionnées et calculées pour {prefs.people} part{prefs.people > 1 ? "s" : ""}{profile.household ? ` (${householdLabel(profile)}, un enfant compte pour ⅓ à ½ part selon l'âge)` : ""}. Vérifie ton placard avant de partir.</p>
            <p className="small"><strong>Budget indicatif :</strong> environ {budget} € pour ces {planned.length} repas, hors placard (ordre de grandeur tiré des indicateurs € des fiches, pas un prix de magasin).</p>
            <button className="btn" onClick={shop}>Mettre la semaine dans la liste de courses</button>
            <div className="row">
              <button className="btn ghost" onClick={() => void sendWeek()}><Icon name="share" size={20} /> Envoyer la semaine</button>
              <button className="btn ghost" onClick={exportIcs}><Icon name="calendar" size={20} /> Dans mon agenda</button>
              <button className="btn ghost" onClick={() => void shareWeek()}>Copier en texte</button>
            </div>
          </section>
          <section className="section week-balance">
            <h2 className="h3"><Icon name="leaf" size={22} className="ic-inline" /> L'équilibre de la semaine</h2>
            <p>{balance.fish} repas de poisson · {balance.legumes} de légumineuses · {balance.vege} végétarien{balance.vege > 1 ? "s" : ""}{balance.rich ? ` · ${balance.rich} plat${balance.rich > 1 ? "s" : ""} très riche${balance.rich > 1 ? "s" : ""}` : ""}.</p>
            {balance.tips.length ? <ul>{balance.tips.map((t) => <li key={t}>{t}</li>)}</ul> : balance.meals >= 5 && <p className="small">Semaine équilibrée selon les repères simples du PNNS. Ajoute des légumes ou un fruit à chaque repas.</p>}
          </section>
          {(prep.tasks.length > 0 || prep.veg.length > 0) && (
            <section className="section">
              <h2 className="h3"><Icon name="knife" size={22} className="ic-inline" /> À préparer à l'avance (le dimanche ou la veille)</h2>
              {prep.veg.length > 0 && <p>Lave et coupe d'un coup : {prep.veg.join(", ").toLowerCase()}. Range-les dans des boîtes fermées au frigo (3 jours au plus).</p>}
              <ul>{prep.tasks.map((t, k) => <li key={k}><strong>{t.recipe} :</strong> {t.task}</li>)}</ul>
            </section>
          )}
        </>
      )}
    </Page>
  );
}
