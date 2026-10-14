import { useEffect } from "react";
import { href, useRoute } from "./lib/router";
import { useStore } from "./lib/store";
import { useTimerLoop } from "./lib/timers";
import { applyUpdate, usePwa } from "./lib/pwa";
import TimerDock from "./components/TimerDock";
import { VideoHost } from "./components/video";
import Home from "./pages/Home";
import Explore from "./pages/Explore";
import Region from "./pages/Region";
import Search from "./pages/Search";
import Frigo from "./pages/Frigo";
import Courses from "./pages/Courses";
import RecipePage from "./pages/RecipePage";
import Cook from "./pages/Cook";
import { TechniquesPage, TechniquePage } from "./pages/Techniques";
import Pains from "./pages/Pains";
import Sauces from "./pages/Sauces";
import Fetes from "./pages/Fetes";
import MenuPage from "./pages/Menu";
import ZeroDechet from "./pages/ZeroDechet";
import Enfants from "./pages/Enfants";
import Imports from "./pages/Imports";
import Biblio from "./pages/Biblio";
import Profil from "./pages/Profil";
import Onboarding from "./pages/Onboarding";
import Credits from "./pages/Credits";

const TABS = [
  { to: "/", label: "Accueil", icon: "🏠", match: [""] },
  { to: "/explorer", label: "Explorer", icon: "🧭", match: ["explorer", "region", "recherche", "techniques", "technique", "pains", "sauces", "fetes", "enfants", "menu", "zero-dechet"] },
  { to: "/frigo", label: "Frigo", icon: "🥕", match: ["frigo", "courses"] },
  { to: "/biblio", label: "Ma biblio", icon: "📚", match: ["biblio", "imports"] },
  { to: "/profil", label: "Profil", icon: "👤", match: ["profil", "credits"] },
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
  if (p0 === "cuisine" && p1) return <Cook id={p1} />;
  if (!onboarded && p0 !== "profil") return <Onboarding />;

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
            <span className="tab-ic" aria-hidden="true">{t.icon}</span><span className="tab-lb">{t.label}</span>
          </a>
        ))}
      </nav>
      <div className="content">
        {pwa.updateReady && (
          <div className="update" role="status">Une nouvelle version d'ATLAS est prête. <button className="btn small" onClick={applyUpdate}>Mettre à jour</button></div>
        )}
        {page}
      </div>
      <TimerDock />
      <VideoHost />
    </div>
  );
}
