import { Icon } from "./icons";
import { addTime, fmtLeft, removeTimer, useNow, useTimers } from "../lib/timers";

/** Minuteurs en cours, visibles sur tous les écrans. */
export default function TimerDock() {
  const timers = useTimers();
  const now = useNow(500);
  if (!timers.length) return null;
  return (
    <aside className="timers" aria-label="Minuteurs">
      {timers.map((t) => {
        const left = t.endAt - now;
        return (
          <div key={t.id} className={`timer ${t.done ? "done" : ""}`} role={t.done ? "alert" : undefined}>
            <span className="t-label"><Icon name="timer" size={18} className="ic-inline" />{t.label}</span>
            <span className="t-left" aria-live="off">{t.done ? "Terminé !" : fmtLeft(left)}</span>
            <button className="btn small ghost" onClick={() => addTime(t.id, 60)} aria-label={`Ajouter une minute à ${t.label}`}>+1 min</button>
            <button className="btn small ghost" onClick={() => removeTimer(t.id)} aria-label={`Supprimer le minuteur ${t.label}`}><Icon name="close" size={18} /></button>
          </div>
        );
      })}
    </aside>
  );
}
