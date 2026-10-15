import { useState } from "react";
import { setState, useStore } from "../lib/store";

/** Mon carnet : après avoir cuisiné, une note sur 5 et ce que je changerai la prochaine fois (gardé sur l'appareil). */
export default function Journal({ id, compact, onSaved }: { id: string; compact?: boolean; onSaved?: () => void }) {
  const entry = useStore((s) => s.journal?.[id]);
  const [rating, setRating] = useState(entry?.rating ?? 0);
  const [note, setNote] = useState(entry?.note ?? "");
  const [ok, setOk] = useState(false);
  const save = () => {
    setState((s) => { s.journal = s.journal ?? {}; s.journal[id] = { rating, note: note.trim(), date: new Date().toISOString() }; });
    setOk(true); onSaved?.();
  };
  return (
    <div className={`card pad journal ${compact ? "compact" : ""}`}>
      <strong>📝 Mon carnet</strong>
      <div className="stars" role="radiogroup" aria-label="Ma note">
        {[1, 2, 3, 4, 5].map((n) => <button key={n} type="button" role="radio" aria-checked={rating === n} aria-label={`${n} sur 5`} className={n <= rating ? "on" : ""} onClick={() => setRating(n)}>★</button>)}
      </div>
      <label className="field">Ce que je changerai la prochaine fois (sel, cuisson, quantités…)
        <textarea rows={3} value={note} onChange={(e) => { setNote(e.target.value); setOk(false); }} placeholder="Ex. : 5 min de moins au four, un peu plus de citron" />
      </label>
      <button className="btn small" onClick={save} disabled={!rating && !note.trim()}>Enregistrer dans mon carnet</button>
      {ok && <span className="small" role="status"> Enregistré.</span>}
      {entry && !compact && <p className="small">Dernière fois : {new Date(entry.date).toLocaleDateString("fr-FR")}{entry.rating ? ` · ${"★".repeat(entry.rating)}` : ""}</p>}
    </div>
  );
}
