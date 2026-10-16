import Household from "../components/Household";
import { EQUIPEMENTS } from "../lib/equipement";
import { Icon } from "../components/icons";
import { ZONE_LABEL, detectZone } from "../lib/season";
import { useEffect, useRef, useState } from "react";
import { ALLERGENS, RECIPES } from "../lib/data";
import { Page, Section } from "../components/ui";
import { IMAGES, loadMoreImages, supportsAvif } from "../components/photo";
import { href } from "../lib/router";
import { exportData, importData, resetAll, setState, useStore } from "../lib/store";
import { frenchVoices, speak, ttsAvailable, voiceCommandsAvailable } from "../lib/speech";
import { checkForAppUpdate, isIos, isStandalone, promptInstall, usePwa } from "../lib/pwa";
import type { Profile } from "../lib/types";
import { clearErrors, readErrors } from "../lib/errlog";

/** Journal d'erreurs local : à copier pour signaler un problème (rien n'est envoyé automatiquement). */
function ErrorLog() {
  const [list, setList] = useState(readErrors);
  const [copied, setCopied] = useState(false);
  if (!list.length) return <p className="small">Aucune erreur enregistrée sur cet appareil.</p>;
  const text = list.map((e) => `${e.at} · ${e.where} · ${e.msg}`).join("\n");
  return (
    <>
      <p className="small">{list.length} erreur(s) récente(s), gardées seulement sur cet appareil. Copie-les pour signaler un problème.</p>
      <pre className="errlog">{text}</pre>
      <div className="row">
        <button className="btn small ghost" onClick={() => { void navigator.clipboard?.writeText(text).then(() => setCopied(true)); }}>{copied ? "Copié" : "Copier"}</button>
        <button className="btn small ghost" onClick={() => { clearErrors(); setList([]); }}>Effacer le journal</button>
      </div>
    </>
  );
}

const EQUIP = EQUIPEMENTS;

export function ProfileForm() {
  const p = useStore((s) => s.profile);
  const set = (fn: (p: Profile) => void) => setState((s) => { fn(s.profile); });
  return (
    <div className="form">
      <fieldset>
        <legend>Régimes et convictions</legend>
        <label className="switch"><input type="checkbox" checked={p.noPork} onChange={(e) => set((x) => { x.noPork = e.target.checked; })} /> Sans porc (et ses dérivés : saindoux, gélatine porcine, certains bouillons…)</label>
        <div className="radio-row" role="radiogroup" aria-label="Alcool">
          <span>Alcool :</span>
          {([["allowed", "Autorisé"], ["standard", "Sans alcool"], ["strict", "Sans alcool strict (ni traces : sauce soja, vinaigre de vin, extrait de vanille…)"]] as const).map(([v, l]) => (
            <label key={v} className="radio"><input type="radio" name="alc" checked={p.alcohol === v} onChange={() => set((x) => { x.alcohol = v; })} /> {l}</label>
          ))}
        </div>
        <label className="switch"><input type="checkbox" checked={p.strict} onChange={(e) => set((x) => { x.strict = e.target.checked; })} /> Mode strict : en cas de doute (ingrédient « possible »), exclure la recette</label>
        <label className="switch"><input type="checkbox" checked={p.vegetarian} onChange={(e) => set((x) => { x.vegetarian = e.target.checked; })} /> Végétarien (ni viande ni poisson)</label>
        <p className="small">Halal : active « sans porc » et « sans alcool ». L'application signale ; elle ne certifie pas (l'origine de la viande dépend de ton achat).</p>
      </fieldset>
      <fieldset>
        <legend>Allergies à exclure (14 allergènes réglementaires)</legend>
        <div className="chips">
          {Object.entries(ALLERGENS).map(([k, l]) => (
            <label key={k} className={`chip ${p.allergens.includes(k) ? "on" : ""}`}>
              <input type="checkbox" className="sr" checked={p.allergens.includes(k)} onChange={() => set((x) => { x.allergens = x.allergens.includes(k) ? x.allergens.filter((a) => a !== k) : [...x.allergens, k]; })} /> {l}
            </label>
          ))}
        </div>
        <p className="small">Vérifie toujours les étiquettes des produits que tu achètes : les recettes sont calculées avec un référentiel d'ingrédients encore au niveau « brouillon » (non relu par un·e diététicien·ne).</p>
      </fieldset>
      <fieldset>
        <legend>Foyer</legend>
        <Household />
        <p className="small">Une allergie qui ne concerne qu'une personne ? Choisis-la ici plutôt que dans « Allergies à exclure » : les recettes restent proposées, avec une alerte pour lui préparer une part à part.</p>
        <div className="chips" role="group" aria-label="Allergies d'une seule personne">
          {Object.entries(ALLERGENS).map(([k, l]) => (
            <label key={k} className={`chip ${(p.allergensWarn ?? []).includes(k) ? "on" : ""}`}>
              <input type="checkbox" className="sr" checked={(p.allergensWarn ?? []).includes(k)} onChange={() => set((x) => { const w = x.allergensWarn ?? []; x.allergensWarn = w.includes(k) ? w.filter((a) => a !== k) : [...w, k]; })} /> {l}
            </label>
          ))}
        </div>
        <label className="switch"><input type="checkbox" checked={p.adult} onChange={(e) => set((x) => { x.adult = e.target.checked; })} /> J'ai 18 ans ou plus (affiche aussi les accords avec alcool, si l'alcool est autorisé)</label>
      </fieldset>
      <fieldset>
        <legend>Mon équipement</legend>
        <div className="chips">
          {EQUIP.map(([k, l]) => (
            <label key={k} className={`chip ${p.equipment.includes(k) ? "on" : ""}`}>
              <input type="checkbox" className="sr" checked={p.equipment.includes(k)} onChange={() => set((x) => { x.equipment = x.equipment.includes(k) ? x.equipment.filter((a) => a !== k) : [...x.equipment, k]; })} /> {l}
            </label>
          ))}
        </div>
      </fieldset>
    </div>
  );
}

function OfflinePhotos() {
  const [state, setStateLocal] = useState<string>("");
  const favs = useStore((st) => st.favorites);
  const week = useStore((st) => st.week);
  const mine = new Set([...favs, ...Object.values(week ?? {}).flatMap((d) => [d.midi, d.soir])].filter(Boolean).map((id) => `recette/${id}`));
  const run = async (only: "tout" | "mes") => {
    await loadMoreImages();
    const everything = Object.entries(IMAGES);
    const list = only === "tout" ? everything : everything.filter(([k]) => mine.has(k));
    // lève le plafond du cache photos (sinon les plus anciennes seraient effacées pendant le téléchargement)
    navigator.serviceWorker?.controller?.postMessage({ type: "img-max", value: only === "tout" ? 6000 : 400 + list.length * 2 });
    let done = 0;
    const avif = await supportsAvif();
    for (const [, m] of list) {
      for (const w of m.sizes.filter((x) => x <= 800)) { try { await fetch(`./${m.path}-${w}.${m.avif && avif ? "avif" : "webp"}`); } catch { /* hors ligne */ } }
      done++; if (done % 10 === 0 || done === list.length) setStateLocal(`${done} / ${list.length} photos enregistrées`);
    }
  };
  return (
    <>
      <p className="small">Les photos se gardent sur l'appareil au fur et à mesure que tu les vois (les 400 dernières). Pour cuisiner sans réseau, enregistre-les d'avance, de préférence en Wi-Fi :</p>
      <div className="row">
        <button className="btn ghost" disabled={!mine.size} onClick={() => void run("mes")}>Mes favoris et ma semaine ({mine.size} photos)</button>
        <button className="btn ghost" onClick={() => void run("tout")}>Toutes les photos (≈ 70 Mo)</button>
      </div>
      {state && <p role="status" className="small">{state}</p>}
      <p className="small"><a href={href("/credits")}>Crédits photos</a></p>
    </>
  );
}

export default function Profil() {
  const settings = useStore((s) => s.settings);
  const pwa = usePwa();
  const [voices, setVoices] = useState<SpeechSynthesisVoice[]>([]);
  const [msg, setMsg] = useState("");
  const file = useRef<HTMLInputElement>(null);
  useEffect(() => {
    const load = () => setVoices(frenchVoices());
    load();
    if (ttsAvailable()) speechSynthesis.addEventListener("voiceschanged", load);
    return () => { if (ttsAvailable()) speechSynthesis.removeEventListener("voiceschanged", load); };
  }, []);
  const setS = (fn: (s: typeof settings) => void) => setState((st) => { fn(st.settings); });

  const download = () => {
    const a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([exportData()], { type: "application/json" }));
    a.download = `atlas-sauvegarde-${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
  };

  return (
    <Page title="Profil du foyer" sub="Régimes, allergies, équipement, lecture audio, affichage.">
      <ProfileForm />
      <Section title="Lecture audio">
        {!ttsAvailable() ? <p>La synthèse vocale n'est pas disponible sur ce navigateur.</p> : (
          <div className="form">
            <label className="field">Voix
              <select value={settings.voiceURI ?? ""} onChange={(e) => setS((s) => { s.voiceURI = e.target.value || null; })}>
                <option value="">Automatique (meilleure voix française)</option>
                {voices.map((v) => <option key={v.voiceURI} value={v.voiceURI}>{v.name} ({v.lang})</option>)}
              </select>
            </label>
            <label className="field">Vitesse : {settings.rate.toFixed(2).replace(".", ",")}×
              <input type="range" min={0.75} max={1.5} step={0.05} value={settings.rate} onChange={(e) => setS((s) => { s.rate = +e.target.value; })} />
            </label>
            <button className="btn ghost" onClick={() => speak(["Préchauffe le four à 180 °C (th. 6). Ajoute 1 c. à s. d'huile et ½ c. à c. de sel, puis cuis 1 h 30."])}><Icon name="speaker" size={18} className="ic-inline" /> Tester la voix</button>
            <p className="small">Sur iPhone et iPad, les voix « améliorées » se téléchargent dans Réglages › Accessibilité › Contenu énoncé › Voix › Français. Commandes vocales en mode cuisine : {voiceCommandsAvailable() ? "disponibles sur ce navigateur" : "non disponibles sur ce navigateur (utilise les gros boutons)"}.</p>
          </div>
        )}
      </Section>
      <Section title="Affichage">
        <div className="form">
          <div className="radio-row" role="radiogroup" aria-label="Thème">
            <span>Thème :</span>
            {([["auto", "Automatique"], ["light", "Clair"], ["dark", "Sombre"]] as const).map(([v, l]) => (
              <label key={v} className="radio"><input type="radio" name="theme" checked={settings.theme === v} onChange={() => setS((s) => { s.theme = v; })} /> {l}</label>
            ))}
          </div>
          <label className="field">Taille du texte : {Math.round(settings.textScale * 100)} %
            <input type="range" min={0.9} max={1.6} step={0.1} value={settings.textScale} onChange={(e) => setS((s) => { s.textScale = +e.target.value; })} />
          </label>
          <label className="switch"><input type="checkbox" checked={settings.readableFont} onChange={(e) => setS((s) => { s.readableFont = e.target.checked; })} /> Police plus lisible (dyslexie)</label>
        </div>
      </Section>
      <Section title="Saisons de ton lieu" id="saisons">
        <div className="form">
          <p className="small">Le menu du jour, le « marché du mois » et la pastille « de saison » suivent les saisons de l'endroit où tu cuisines. ATLAS ne te localise pas : la zone est déduite du fuseau horaire de ton appareil (détecté : <strong>{ZONE_LABEL[detectZone()].split(" (")[0]}</strong>), et tu peux la choisir ici.</p>
          <div className="radio-row" role="radiogroup" aria-label="Zone de saisons">
            {(["auto", "nord", "sud", "tropical"] as const).map((v) => (
              <label key={v} className="radio"><input type="radio" name="zone" checked={settings.zone === v} onChange={() => setS((s) => { s.zone = v; })} /> {v === "auto" ? "Automatique (fuseau horaire)" : ZONE_LABEL[v]}</label>
            ))}
          </div>
        </div>
      </Section>
      <Section title="Installer ATLAS sur tes appareils">
        {isStandalone() ? <p><Icon name="check" size={16} className="ic-inline" /> ATLAS est installée sur cet appareil.</p> : isIos() ? (
          <p><strong>iPhone, iPad :</strong> dans Safari, touche le bouton Partager <span aria-hidden="true">⎋</span> puis « Sur l'écran d'accueil ». <strong>Mac :</strong> Safari › Fichier › « Ajouter au Dock ».</p>
        ) : pwa.canInstall ? <button className="btn" onClick={() => void promptInstall()}>Installer l'application</button> : (
          <p>Android et ordinateur : menu du navigateur › « Installer l'application » (ou « Ajouter à l'écran d'accueil »).</p>
        )}
        <p className="small">Une fois installée, ATLAS fonctionne hors connexion : recettes, audio, minuteurs, frigo et courses. Sur Android, l'application installée apparaît dans le menu « Partager » de TikTok et Instagram.</p>
        <button className="btn ghost" onClick={async () => setMsg((await checkForAppUpdate()) ? "Mise à jour trouvée : un bandeau va apparaître." : "Tu as la dernière version.")}>Vérifier les mises à jour</button>
      </Section>
      <Section title="Photos hors connexion">
        <OfflinePhotos />
      </Section>
      <Section title="Mes données">
        <p className="small">Tout est enregistré sur cet appareil. Sauvegarde le fichier pour le transférer sur un autre appareil.</p>
        <div className="row">
          <button className="btn ghost" onClick={download}>Exporter mes données</button>
          <button className="btn ghost" onClick={() => file.current?.click()}>Importer une sauvegarde</button>
          <input ref={file} type="file" accept="application/json" hidden onChange={async (e) => {
            const f = e.target.files?.[0]; if (!f) return;
            try { importData(await f.text()); setMsg("Sauvegarde restaurée."); } catch (err) { setMsg(`Impossible de lire ce fichier : ${(err as Error).message}`); }
          }} />
          <button className="btn danger" onClick={() => { if (confirm("Effacer toutes tes données ATLAS sur cet appareil ?")) resetAll(); }}>Tout effacer</button>
        </div>
        {msg && <p role="status">{msg}</p>}
      </Section>
      <Section title="Journal des erreurs">
        <ErrorLog />
      </Section>
      <Section title="À propos">
        <p className="small">ATLAS · {RECIPES.length} recettes (Tomes 11 à 13 de la bible) · moteur diététique et planificateur vérifiés par plus de 70 contrôles automatiques à chaque publication. Les recettes n'ont pas encore passé les tests en cuisine du Tome 7 ; les substitutions sont « à tester » : note tes essais dans « Mes recettes › Mon carnet d'essais ». Les photos viennent de Wikimedia Commons et d'Openverse (licences libres, voir les crédits) ; les vidéos sont celles des créatrices et créateurs, lues avec leurs lecteurs officiels.</p>
        <p className="small">Limites des applications web sur iPhone : un minuteur ne peut pas sonner quand l'application est fermée (une notification s'affiche si tu l'as autorisée) ; la commande vocale dépend de Safari. Ces points seront levés par la version native (Tome 1 §17).</p>
      </Section>
    </Page>
  );
}
