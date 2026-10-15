import { Icon } from "../components/icons";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { RECIPE_BY_ID } from "../lib/data";
import { verdict } from "../lib/engine";
import { go, href, useRoute } from "../lib/router";
import { setState, useProfile } from "../lib/store";
import { durationsIn, gestureLabel, ovenPlan, scaleQty, splitStep } from "../lib/text";
import { listen, speak, stopSpeaking, ttsAvailable, voiceCommandsAvailable } from "../lib/speech";
import { startTimer, useWakeLock } from "../lib/timers";
import { Rich } from "./RecipePage";
import Journal from "../components/Journal";
import { termsIn } from "../lib/glossaire";
import { rescueFor } from "../lib/rescue";
import { cuesIn, saltDose } from "../lib/cues";
import TimerDock from "../components/TimerDock";
import { VideoHost, playVideo } from "../components/video";

/** Mode cuisine (Tome 1 §8.7, Tome 5 §7.7) : une étape à la fois, très grand texte, cibles de 64 px, écran allumé. */
export default function Cook({ id }: { id: string }) {
  const r = RECIPE_BY_ID[id];
  const p = useProfile();
  const route = useRoute();
  const [i, setI] = useState(-1); // -1 = mise en place
  const [auto, setAuto] = useState(false); // lecture automatique de chaque étape
  const [mic, setMic] = useState(false);
  const [micMsg, setMicMsg] = useState("");
  const [heard, setHeard] = useState("");
  const [checked, setChecked] = useState<Set<number>>(new Set());
  const stopListen = useRef<() => void>(() => undefined);
  useWakeLock(true);

  const v = r ? verdict(r, p) : null;
  const lines = r && v?.adapted && route.query.get("adapte") === "1" ? v.adapted.lines : r?.ingredients ?? [];
  const steps = useMemo(() => (r?.steps ?? []).flatMap(splitStep), [r]); // un geste par écran
  const oven = useMemo(() => ovenPlan(steps), [steps]); // préchauffage : prévenir avant d'enfourner

  const say = useCallback((idx: number) => {
    if (!r || !ttsAvailable()) return;
    if (idx < 0) speak(["Mise en place.", ...lines.map((l) => `${l.qty} ${l.label}`)]);
    else speak([`Étape ${idx + 1} sur ${steps.length}.`, steps[idx]]);
  }, [r, lines, steps]);

  const goTo = useCallback((n: number) => {
    const k = Math.max(-1, Math.min(steps.length - 1, n));
    setI(k);
    if (auto) say(k); else stopSpeaking();
  }, [auto, say, steps.length]);

  // clavier et boutons physiques (casque, clavier Bluetooth)
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "ArrowRight" || e.key === " ") { e.preventDefault(); goTo(i + 1); }
      if (e.key === "ArrowLeft") goTo(i - 1);
      if (e.key === "Escape") go(`/recette/${id}`);
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [i, goTo, id]);

  useEffect(() => () => { stopSpeaking(); stopListen.current(); }, []);

  const toggleMic = () => {
    if (mic) { stopListen.current(); setMic(false); return; }
    stopListen.current = listen((c, h) => {
      setHeard(h);
      setI((cur) => {
        if (c === "suivant") { const n = Math.min(steps.length - 1, cur + 1); say(n); return n; }
        if (c === "precedent") { const n = Math.max(-1, cur - 1); say(n); return n; }
        if (c === "repete" || c === "lecture") { say(cur); return cur; }
        if (c === "pause") { stopSpeaking(); return cur; }
        if (typeof c === "object") startTimer(`${r?.title.split(" (")[0]} · minuteur vocal`, c.minutes * 60, id);
        return cur;
      });
    }, (on, err) => { setMic(on); setMicMsg(err ?? ""); });
  };

  if (!r) return <main className="page"><h1>Recette introuvable</h1><a href={href("/")}>Accueil</a></main>;
  const step = i >= 0 ? steps[i] : null;

  return (
    <div className="cook">
      <header className="cook-top">
        <a className="btn ghost" href={href(`/recette/${id}`)} aria-label="Quitter le mode cuisine">✕</a>
        <div className="cook-title">{r.title}</div>
        {r.videos.some((x) => x.embed) && <button className="btn ghost small" onClick={() => playVideo(r.videos.find((x) => x.embed)!)}>▶ Vidéo</button>}
        <div className="cook-progress" aria-hidden="true"><span style={{ width: `${((i + 1) / steps.length) * 100}%` }} /></div>
      </header>

      <main className="cook-body" id="contenu" aria-live="polite">
        {i < 0 ? (
          <>
            <h1 className="cook-step-n">Mise en place</h1>
            <p className="small">Sors et pèse tout avant d'allumer le feu. Coche au fur et à mesure.</p>
            <p className="small"><strong>Matériel :</strong> {r.equipment}</p>
            {saltDose(r) && <p className="small"><strong>Sel :</strong> {saltDose(r)!.text}</p>}
            {oven && oven.at <= 1 && <p className="banner warn"><Icon name="flame" size={20} className="ic-inline" /> Allume le four maintenant à <strong>{oven.temp}</strong> : il lui faut 15 à 20 min pour chauffer.</p>}
            <ul className="mise">
              {lines.map((l, k) => (
                <li key={k}>
                  <label><input type="checkbox" checked={checked.has(k)} onChange={() => setChecked((s) => { const n = new Set(s); if (n.has(k)) n.delete(k); else n.add(k); return n; })} />
                    <span><strong>{scaleQty(l.qty, 1)}</strong> {l.label}{l.optional ? " (facultatif)" : ""}</span></label>
                </li>
              ))}
            </ul>
          </>
        ) : (
          <>
            <p className="cook-step-n">Étape {i + 1} / {steps.length}</p>
            <p className="cook-step"><Rich text={step!} /></p>
            {cuesIn(step!).map((c) => <p key={c} className="cue big"><Icon name="eye" size={20} className="ic-inline" /> {c}</p>)}
            {oven && oven.at > 1 && i === oven.at - 2 && <p className="banner warn"><Icon name="flame" size={20} className="ic-inline" /> Pense à préchauffer le four à <strong>{oven.temp}</strong> maintenant : on enfourne dans 2 étapes.</p>}
            {durationsIn(step!).length > 0 && (
              <div className="timers-inline big">
                {durationsIn(step!).map((d, k) => <button key={k} className="chip big" onClick={() => startTimer(`${r.title.split(" (")[0]} · ${gestureLabel(step!, i + 1)}`, d.seconds, id)}><Icon name="timer" size={22} className="ic-inline" /> Lancer {d.label}</button>)}
              </div>
            )}
            {termsIn(step!).length > 0 && (
              <details className="cook-help"><summary><Icon name="dictionary" size={20} className="ic-inline" /> Je ne comprends pas un mot</summary>
                <dl>{termsIn(step!).map((t) => <div key={t.term}><dt>{t.term}</dt><dd>{t.def}</dd></div>)}</dl>
              </details>
            )}
            <details className="cook-help"><summary><Icon name="lifebuoy" size={20} className="ic-inline" /> Ça ne se passe pas comme prévu</summary>
              <ul>{rescueFor(r, 8).map((x) => <li key={x.problem}><strong>{x.problem} :</strong> {x.fix}</li>)}</ul>
            </details>
          </>
        )}
        {i === steps.length - 1 && (
          <div className="cook-end">
            <p>Bon appétit ! 🍽 Comment c'était ?</p>
            <Journal id={id} compact />
            <button className="btn" onClick={() => { setState((s) => { s.cooked[id] = (s.cooked[id] ?? 0) + 1; }); go(`/recette/${id}`); }}>J'ai terminé</button>
          </div>
        )}
      </main>

      <footer className="cook-bar">
        <button className="cook-btn" onClick={() => goTo(i - 1)} disabled={i < 0} aria-label="Étape précédente">◀</button>
        {ttsAvailable() && <button className="cook-btn" onClick={() => say(i)} aria-label="Lire l'étape">🔊</button>}
        {ttsAvailable() && <button className={`cook-btn ${auto ? "on" : ""}`} onClick={() => { setAuto(!auto); if (!auto) say(i); }} aria-pressed={auto} aria-label="Lecture automatique des étapes">{auto ? "🔁" : "↻"}</button>}
        {voiceCommandsAvailable() && <button className={`cook-btn ${mic ? "on" : ""}`} onClick={toggleMic} aria-pressed={mic} aria-label={mic ? "Arrêter l'écoute" : "Commandes vocales"}>🎙</button>}
        <button className="cook-btn primary" onClick={() => goTo(i + 1)} disabled={i >= steps.length - 1} aria-label="Étape suivante">▶</button>
      </footer>
      {mic && <p className="mic-on" role="status">🎙 Écoute active : dis « suivant », « précédent », « répète », « pause » ou « minuteur 10 minutes ».{heard && ` Entendu : « ${heard} »`}</p>}
      {micMsg && <p className="mic-on warn" role="alert">{micMsg}</p>}
      <TimerDock />
      <VideoHost />
    </div>
  );
}
