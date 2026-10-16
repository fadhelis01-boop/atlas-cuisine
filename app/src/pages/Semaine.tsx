import { Icon } from "../components/icons";
import { useEffect, useMemo, useState } from "react";
import { RECIPE_BY_ID, loadLeftovers } from "../lib/data";
import { COST_PER_PART, autoPlan, consolidate, dayName, leftoverLink, prepAhead, weekDays, type Slot, type WeekPlan } from "../lib/planner";
import { householdLabel, householdPortions, weekBalance } from "../lib/famille";
import { href } from "../lib/router";
import { zoneOf } from "../lib/season";
import { setState, uid, useProfile, useStore } from "../lib/store";
import { minutes } from "../lib/text";
import type { Leftover } from "../lib/types";
import { Chip, Cover, Page } from "../components/ui";
import { toast } from "../lib/toast";

const SLOT_LABEL: Record<Slot, string> = { midi: "Midi", soir: "Soir" };
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
  });
  const setPrefs = (p: Partial<typeof prefs>) => setState((s) => { s.weekPrefs = { ...prefs, ...p }; });
  const fill = (base: WeekPlan, onlyDays = days) => {
    if (!left) return;
    save(autoPlan(onlyDays, base, { slots: prefs.slots, weekdayMax: prefs.weekdayMax, zone: zoneOf(zoneSetting), profile, leftovers: left, seed: Date.now() }));
  };
  const clearWeek = () => { const next = { ...plan }; for (const d of days) delete next[d]; return next; };
  const reroll = (day: string, slot: Slot) => {
    const cur = plan[day]?.[slot];
    const next: WeekPlan = { ...plan, [day]: { ...plan[day], [slot]: undefined } };
    if (!left) return;
    const filled = autoPlan(days, next, { slots: prefs.slots.includes(slot) ? prefs.slots : [...prefs.slots, slot], weekdayMax: prefs.weekdayMax, zone: zoneOf(zoneSetting), profile, leftovers: left, seed: Date.now() });
    // ne remplir que la case demandée, et pas avec le même plat
    const pick = filled[day]?.[slot];
    save({ ...plan, [day]: { ...plan[day], [slot]: pick && pick !== cur ? pick : undefined } });
  };
  const remove = (day: string, slot: Slot) => save({ ...plan, [day]: { ...plan[day], [slot]: undefined } });
  const put = (day: string, slot: Slot, id: string) => { save({ ...plan, [day]: { ...plan[day], [slot]: id } }); setMsg(`${RECIPE_BY_ID[id].title.split(" (")[0]} : ajouté le ${dayName(day)} ${SLOT_LABEL[slot].toLowerCase()}.`); };

  const planned = days.flatMap((d) => (["midi", "soir"] as Slot[]).map((s) => plan[d]?.[s]).filter(Boolean) as string[]);
  const shop = () => {
    const lines = consolidate(planned.map((id) => ({ id, factor: prefs.people / (RECIPE_BY_ID[id]?.portions || prefs.people) })));
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
  const prep = useMemo(() => prepAhead(planned), [planned.join()]);
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
          <li key={d} className={`week-day ${i >= 5 ? "weekend" : ""}`}>
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
                          {link && <><br /><span className="small week-left"><Icon name="recycle" size={15} className="ic-inline" /> utilise le reste de {link} de la veille</span></>}</span>
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
          </li>
        ))}
      </ol>
      <p className="small">Pour placer une recette précise : sur sa fiche, touche « Planifier ». Les plats proposés respectent ton profil (porc, alcool, allergies) et la saison de l'endroit où tu es.</p>

      {planned.length > 0 && (
        <>
          <section className="section">
            <h2 className="h3"><Icon name="cart" size={22} className="ic-inline" /> Les courses de la semaine</h2>
            <p className="small">Un seul article par produit, quantités additionnées et calculées pour {prefs.people} part{prefs.people > 1 ? "s" : ""}{profile.household ? ` (${householdLabel(profile)}, un enfant compte pour ⅓ à ½ part selon l'âge)` : ""}. Vérifie ton placard avant de partir.</p>
            <p className="small"><strong>Budget indicatif :</strong> environ {budget} € pour ces {planned.length} repas, hors placard (ordre de grandeur tiré des indicateurs € des fiches, pas un prix de magasin).</p>
            <button className="btn" onClick={shop}>Mettre la semaine dans la liste de courses</button>
            <button className="btn ghost" onClick={() => void shareWeek()}><Icon name="share" size={20} /> Partager la semaine</button>
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
