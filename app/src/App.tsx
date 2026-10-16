import { ICON_NAMES, Icon } from "./components/icons";
import { Suspense, lazy, useEffect } from "react";
import { href, useRoute } from "./lib/router";
import { useStore } from "./lib/store";
import { useTimerLoop } from "./lib/timers";
import { applyUpdate, usePwa } from "./lib/pwa";
import TimerDock from "./components/TimerDock";
import Toasts from "./components/Toasts";
import { VideoHost } from "./components/video";
import Home from "./pages/Home";
import Explore from "./pages/Explore";
import Region from "./pages/Region";
import Search from "./pages/Search";
import RecipePage from "./pages/RecipePage";
import { DictionaryPage, IngredientPage } from "./pages/Dictionnaire";
import ErrorBoundary from "./components/ErrorBoundary";

// pages chargées à la demande (audit dév 🟠 8) : l'accueil, les fiches et la recherche restent dans le fichier principal
const Frigo = lazy(() => import("./pages/Frigo"));
const Courses = lazy(() => import("./pages/Courses"));
const Cook = lazy(() => import("./pages/Cook"));
const TechniquesPage = lazy(() => import("./pages/Techniques").then((m) => ({ default: m.TechniquesPage })));
const TechniquePage = lazy(() => import("./pages/Techniques").then((m) => ({ default: m.TechniquePage })));
const Pains = lazy(() => import("./pages/Pains"));
const Sauces = lazy(() => import("./pages/Sauces"));
const Fetes = lazy(() => import("./pages/Fetes"));
const MenuPage = lazy(() => import("./pages/Menu"));
const ZeroDechet = lazy(() => import("./pages/ZeroDechet"));
const Enfants = lazy(() => import("./pages/Enfants"));
const Imports = lazy(() => import("./pages/Imports"));
const Biblio = lazy(() => import("./pages/Biblio"));
const Profil = lazy(() => import("./pages/Profil"));
const Onboarding = lazy(() => import("./pages/Onboarding"));
const Credits = lazy(() => import("./pages/Credits"));
const Catalogue = lazy(() => import("./pages/Catalogue"));
const Apprendre = lazy(() => import("./pages/Apprendre"));
const Semaine = lazy(() => import("./pages/Semaine"));

const Loading = () => <main className="page" aria-busy="true"><p className="meta">Chargement…</p></main>;

const TABS = [
  { to: "/", label: "Accueil", icon: "home", match: [""] },
  { to: "/explorer", label: "Explorer", icon: "compass", match: ["explorer", "region", "recherche", "techniques", "technique", "pains", "sauces", "fetes", "enfants", "menu", "zero-dechet", "dictionnaire", "ingredient", "recettes", "apprendre"] },
  { to: "/frigo", label: "Frigo", icon: "fridge", match: ["frigo", "courses", "semaine"] },
  { to: "/biblio", label: "Mes recettes", icon: "book", match: ["biblio", "imports"] },
  { to: "/profil", label: "Profil", icon: "chef", match: ["profil", "credits"] },
];

export default function App() {
  const route = useRoute();
  const onboarded = useStore((s) => s.profile.onboarded);
  const settings = useStore((s) => s.settings);
  const pwa = usePwa();
  useTimerLoop();

  useEffect(() => {
    const root = document.documentElement;
    if (settings.theme === "auto") root.removeAttribute("data-theme"); else root.setAttribute("data-theme", settings.theme);
    root.style.setProperty("--scale", String(settings.textScale));
    root.classList.toggle("readable", settings.readableFont);
    root.classList.toggle("big-text", settings.textScale >= 1.4);
  }, [settings]);

  // Partage depuis TikTok / Instagram (Android, application installée) : ?share_url=…
  useEffect(() => {
    const q = new URLSearchParams(location.search);
    const u = q.get("share_url") || q.get("share_text") || q.get("share_title");
    if (u) {
      const payload = encodeURIComponent([q.get("share_title"), q.get("share_text"), q.get("share_url")].filter(Boolean).join("\n"));
      history.replaceState(null, "", location.pathname);
      location.hash = `#/imports?partage=${payload}`;
    }
  }, []);

  const [p0, p1] = route.path;
  if (p0 === "cuisine" && p1) return <Suspense fallback={<Loading />}><Cook id={p1} /></Suspense>;
  if (!onboarded && p0 !== "profil") return <Suspense fallback={<Loading />}><Onboarding /></Suspense>;

  let page;
  switch (p0 ?? "") {
    case "": page = <Home />; break;
    case "explorer": page = <Explore />; break;
    case "region": page = <Region id={p1} />; break;
    case "recherche": page = <Search q={route.query.get("q") ?? ""} />; break;
    case "frigo": page = <Frigo />; break;
    case "courses": page = <Courses />; break;
    case "recette": page = <RecipePage id={p1} q={route.query} />; break;
    case "techniques": page = <TechniquesPage />; break;
    case "technique": page = <TechniquePage id={p1} />; break;
    case "pains": page = <Pains />; break;
    case "sauces": page = <Sauces />; break;
    case "fetes": page = <Fetes />; break;
    case "menu": page = <MenuPage id={p1} />; break;
    case "zero-dechet": page = <ZeroDechet />; break;
    case "enfants": page = <Enfants />; break;
    case "imports": page = <Imports key={route.query.toString()} q={route.query} />; break;
    case "biblio": page = <Biblio />; break;
    case "profil": page = <Profil />; break;
    case "credits": page = <Credits />; break;
    case "apprendre": page = <Apprendre />; break;
    case "icones": if (!import.meta.env.DEV) { page = null; break; } page = <main className="page"><h1>Icônes ATLAS</h1><div className="icon-sheet">{ICON_NAMES.map((n) => <figure key={n}><Icon name={n} size={40} /><figcaption>{n}</figcaption></figure>)}</div></main>; break;
    case "semaine": page = <Semaine key={route.query.get("ajout") ?? ""} add={route.query.get("ajout")} />; break;
    case "recettes": page = <Catalogue q0={route.query.get("q") ?? ""} />; break;
    case "dictionnaire": page = <DictionaryPage q0={route.query.get("q") ?? ""} />; break;
    case "ingredient": page = <IngredientPage key={p1} slug={p1} />; break;
    default: page = <main className="page"><h1>Page introuvable</h1><a href={href("/")}>Retour à l'accueil</a></main>;
  }
  const active = TABS.find((t) => t.match.includes(p0 ?? "")) ?? (p0 === "recette" ? null : TABS[0]);

  return (
    <div className="shell">
      <a className="skip" href="#contenu">Aller au contenu</a>
      <nav className="nav" aria-label="Navigation principale">
        <a className="brand" href={href("/")}><img src="./icons/icon.svg" alt="" width="32" height="32" /> <span>ATLAS</span></a>
        {TABS.map((t) => (
          <a key={t.to} href={href(t.to)} className={`tab ${active === t ? "on" : ""}`} aria-current={active === t ? "page" : undefined}>
            <span className="tab-ic" aria-hidden="true"><Icon name={t.icon} size={26} /></span><span className="tab-lb">{t.label}</span>
          </a>
        ))}
      </nav>
      <div className="content">
        {pwa.updateReady && (
          <div className="update" role="status">Une nouvelle version d'ATLAS est prête. <button className="btn small" onClick={applyUpdate}>Mettre à jour</button></div>
        )}
        <ErrorBoundary resetKey={route.path.join("/")}><Suspense fallback={<Loading />}>{page}</Suspense></ErrorBoundary>
      </div>
      <TimerDock />
      <Toasts />
      <VideoHost />
    </div>
  );
}
