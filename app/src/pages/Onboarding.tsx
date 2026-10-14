import { ProfileForm } from "./Profil";
import { setState } from "../lib/store";

/** Premier lancement : profil du foyer en une page (Tome 1 §3.3, Tome 5 §7.1). Tout est modifiable ensuite. */
export default function Onboarding() {
  return (
    <main className="page onboarding" id="contenu">
      <img src="./icons/icon.svg" alt="" width="72" height="72" />
      <h1>Bienvenue dans ATLAS</h1>
      <p className="lead">Les cuisines du monde, faites maison avec le matériel d'une cuisine française. Dis-nous qui mange à la maison : on adapte les recettes, on propose des substitutions et on ne te montre que ce qui te convient.</p>
      <p className="small">Ces informations restent sur ton appareil. Elles ne sont envoyées nulle part.</p>
      <ProfileForm />
      <button className="btn big" onClick={() => setState((s) => { s.profile.onboarded = true; })}>C'est parti</button>
    </main>
  );
}
