import { setState, useProfile } from "../lib/store";
import { householdPortions } from "../lib/famille";

// Le foyer en deux gestes (audit famille) : adultes et âges des enfants. Il règle les parts par défaut des fiches,
// de la semaine et du mode cuisine, et le filtre « enfants » (le plus jeune décide : piment, plats d'adultes).
export default function Household({ compact }: { compact?: boolean }) {
  const p = useProfile();
  const h = p.household ?? { adults: 2, kids: p.kidsAge !== null ? [p.kidsAge] : [] };
  const save = (next: { adults: number; kids: number[] }) => setState((s) => {
    s.profile.household = next;
    s.profile.kidsAge = next.kids.length ? Math.min(...next.kids) : null;
  });
  const parts = householdPortions({ ...p, household: h });
  return (
    <div className={`household ${compact ? "compact" : ""}`}>
      <div className="household-row">
        <span>Adultes</span>
        <button type="button" className="btn small ghost" aria-label="Un adulte de moins" disabled={h.adults <= 1} onClick={() => save({ ...h, adults: h.adults - 1 })}>−</button>
        <strong aria-live="polite">{h.adults}</strong>
        <button type="button" className="btn small ghost" aria-label="Un adulte de plus" disabled={h.adults >= 12} onClick={() => save({ ...h, adults: h.adults + 1 })}>+</button>
      </div>
      <div className="household-row">
        <span>Enfants</span>
        {h.kids.map((age, i) => (
          <label key={i} className="household-kid">
            <span className="sr">Âge de l'enfant {i + 1}</span>
            <input type="number" min={0} max={17} inputMode="numeric" value={age} aria-label={`Âge de l'enfant ${i + 1}`}
              onChange={(e) => save({ ...h, kids: h.kids.map((a, j) => (j === i ? Math.max(0, Math.min(17, +e.target.value || 0)) : a)) })} /> ans
            <button type="button" className="btn small ghost" aria-label={`Retirer l'enfant ${i + 1}`} onClick={() => save({ ...h, kids: h.kids.filter((_, j) => j !== i) })}>×</button>
          </label>
        ))}
        {h.kids.length < 8 && <button type="button" className="btn small ghost" onClick={() => save({ ...h, kids: [...h.kids, 6] })}>+ un enfant</button>}
      </div>
      {p.household && <p className="small">ATLAS cuisinera pour <strong>{parts} part{(parts ?? 0) > 1 ? "s" : ""}</strong> (un enfant de moins de 3 ans compte pour ⅓ de part, de 3 à 10 ans pour ½){h.kids.length ? " et évitera piment et plats d'adultes pour le plus jeune" : ""}.</p>}
    </div>
  );
}
