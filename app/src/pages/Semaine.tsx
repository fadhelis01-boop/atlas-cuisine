import { useEffect, useMemo, useState } from "react";
import { RECIPE_BY_ID, loadLeftovers } from "../lib/data";
import { DAY_NAMES, autoPlan, consolidate, leftoverLink, prepAhead, weekDays, type Slot, type WeekPlan } from "../lib/planner";
import { href } from "../lib/router";
import { zoneOf } from "../lib/season";
import { setState, uid, useProfile, useStore } from "../lib/store";
import { minutes } from "../lib/text";
import type { Leftover } from "../lib/types";
import { Chip, Cover, Page } from "../components/ui";

const SLOT_LABEL: Record<Slot, string> = { midi: "Midi", soir: "Soir" };
const DEFAULT_PREFS = { people: 2, slots: ["soir"] as Slot[], weekdayMax: 45 };
const shortDate = (iso: string) => new Date(iso + "T12:00:00").toLocaleDateString("fr-FR", { day: "numeric", month: "short" });

/** Planificateur de la semaine (audit 🔴 4) : 7 jours remplis selon la saison et le temps disponible,
 *  restes d'un plat réutilisés le lendemain, une seule liste de courses, et ce qui se prépare à l'avance. */
export default function Semaine({ add }: { add: string | null }) {
  const profile = useProfile();
  const zoneSetting = useStore((s) => s.settings.zone);
  const plan = useStore((s) => s.week) ?? {};
  const prefs = useStore((s) => s.weekPrefs) ?? DEFAULT_PREFS;
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
  const put = (day: string, slot: Slot, id: string) => { save({ ...plan, [day]: { ...plan[day], [slot]: id } }); setMsg(`${RECIPE_BY_ID[id].title.split(" (")[0]} : ajouté le ${DAY_NAMES[days.indexOf(day)]} ${SLOT_LABEL[slot].toLowerCase()}.`); };

  const planned = days.flatMap((d) => (["midi", "soir"] as Slot[]).map((s) => plan[d]?.[s]).filter(Boolean) as string[]);
  const shop = () => {
    const lines = consolidate(planned.map((id) => ({ id, factor: prefs.people / (RECIPE_BY_ID[id]?.portions || prefs.people) })));
    setState((s) => {
      s.shopping = s.shopping.filter((i) => i.from !== "Ma semaine");
      for (const l of lines) s.shopping.push({ id: uid(), ref: l.ref, label: l.label, from: "Ma semaine", done: false, section: l.section });
    });
    setMsg(`${lines.length} articles dans la liste de courses, quantités additionnées pour ${prefs.people} personne${prefs.people > 1 ? "s" : ""}.`);
  };
  const prep = useMemo(() => prepAhead(planned), [planned.join()]);
  const slotsShown: Slot[] = (["midi", "soir"] as Slot[]).filter((s) => prefs.slots.includes(s) || days.some((d) => plan[d]?.[s]));

  return (
    <Page title="Ma semaine" sub="Les repas des 7 prochains jours : de saison, rapides en semaine, variés, et les restes d'un jour servent le lendemain." back="/">
      {adding && (
        <div className="banner info week-add" role="group" aria-label="Choisir le jour">
          <p>Où placer <strong>{adding.title.split(" (")[0]}</strong> ?</p>
          <div className="week-add-grid">
            {days.map((d, i) => (
              <span key={d} className="week-add-day">
                <span className="meta">{DAY_NAMES[i].slice(0, 3)} {shortDate(d)}</span>
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
        <button className="btn ghost small" disabled={offset === 0} onClick={() => setOffset(0)}>Cette semaine</button>
        <button className="btn ghost small" disabled={offset === 1} onClick={() => setOffset(1)}>Semaine prochaine</button>
        <span className="grow" />
        <button className="btn" disabled={!left} onClick={() => fill(plan)}>✨ Compléter les cases vides</button>
        <button className="btn ghost" disabled={!left} onClick={() => { if (!planned.length || confirm("Remplacer tous les plats de cette semaine ?")) fill(clearWeek()); }}>Tout reproposer</button>
      </div>
      {msg && <p role="status" className="banner info">{msg} <a href={href("/courses")}>Voir les courses</a></p>}

      <ol className="week">
        {days.map((d, i) => (
          <li key={d} className={`week-day ${i >= 5 ? "weekend" : ""}`}>
            <h2 className="h3">{DAY_NAMES[i]} <span className="meta">{shortDate(d)}</span></h2>
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
                          {link && <><br /><span className="small week-left">♻️ utilise le reste de {link} de la veille</span></>}</span>
                      </a>
                      <span className="week-acts">
                        <button className="btn ghost small" title="Proposer un autre plat" aria-label={`Autre plat pour ${DAY_NAMES[i]} ${s}`} onClick={() => reroll(d, s)}>↻</button>
                        <button className="btn ghost small" title="Retirer" aria-label={`Retirer le plat de ${DAY_NAMES[i]} ${s}`} onClick={() => remove(d, s)}>✕</button>
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
      <p className="small">Pour placer une recette précise : sur sa fiche, touche « 📅 Planifier ». Les plats proposés respectent ton profil (porc, alcool, allergies) et la saison de l'endroit où tu es.</p>

      {planned.length > 0 && (
        <>
          <section className="section">
            <h2 className="h3">🛒 Les courses de la semaine</h2>
            <p className="small">Un seul article par produit, quantités additionnées et calculées pour {prefs.people} personne{prefs.people > 1 ? "s" : ""}. Vérifie ton placard avant de partir.</p>
            <button className="btn" onClick={shop}>Mettre la semaine dans la liste de courses</button>
          </section>
          {(prep.tasks.length > 0 || prep.veg.length > 0) && (
            <section className="section">
              <h2 className="h3">🧺 À préparer à l'avance (le dimanche ou la veille)</h2>
              {prep.veg.length > 0 && <p>Lave et coupe d'un coup : {prep.veg.join(", ").toLowerCase()}. Range-les dans des boîtes fermées au frigo (3 jours au plus).</p>}
              <ul>{prep.tasks.map((t, k) => <li key={k}><strong>{t.recipe} :</strong> {t.task}</li>)}</ul>
            </section>
          )}
        </>
      )}
    </Page>
  );
}
