import { ICON_NAMES, Icon } from "./components/icons";
import { Suspense, lazy, useEffect } from "react";
import { href, useRoute } from "./lib/router";
import { useScreenChange } from "./lib/a11y";
import { PROFILE_MATCH, TABS, tabOf } from "./lib/nav";
import { recordStartup, useUsageCounter } from "./lib/mesures";
import { useStore } from "./lib/store";
import { useDetails, useRecipeDetail } from "./lib/data";
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
import { lazyRetry } from "./lib/chunkRetry";

// pages chargées à la demande (audit dév 🟠 8) : l'accueil, les fiches et la recherche restent dans le fichier principal
// `lazyRetry` (audit dév/UX senior 23/11/2026) : recharge une fois si le chunk a disparu (déploiement entre-temps)
// plutôt que de rester bloqué sur « Chargement… ».
const Frigo = lazy(lazyRetry(() => import("./pages/Frigo")));
const Courses = lazy(lazyRetry(() => import("./pages/Courses")));
const Cook = lazy(lazyRetry(() => import("./pages/Cook")));
const TechniquesPage = lazy(lazyRetry(() => import("./pages/Techniques").then((m) => ({ default: m.TechniquesPage }))));
const TechniquePage = lazy(lazyRetry(() => import("./pages/Techniques").then((m) => ({ default: m.TechniquePage }))));
const Pains = lazy(lazyRetry(() => import("./pages/Pains")));
const Sauces = lazy(lazyRetry(() => import("./pages/Sauces")));
const Fetes = lazy(lazyRetry(() => import("./pages/Fetes")));
const MenuPage = lazy(lazyRetry(() => import("./pages/Menu")));
const ZeroDechet = lazy(lazyRetry(() => import("./pages/ZeroDechet")));
const Restes = lazy(lazyRetry(() => import("./pages/Restes")));
const Marche = lazy(lazyRetry(() => import("./pages/Marche")));
const PiqueNique = lazy(lazyRetry(() => import("./pages/PiqueNique")));
const StreetFood = lazy(lazyRetry(() => import("./pages/StreetFood")));
const Marinades = lazy(lazyRetry(() => import("./pages/Marinades")));
const Enfants = lazy(lazyRetry(() => import("./pages/Enfants")));
const Imports = lazy(lazyRetry(() => import("./pages/Imports")));
const Biblio = lazy(lazyRetry(() => import("./pages/Biblio")));
const Profil = lazy(lazyRetry(() => import("./pages/Profil")));
const Onboarding = lazy(lazyRetry(() => import("./pages/Onboarding")));
const Credits = lazy(lazyRetry(() => import("./pages/Credits")));
const Catalogue = lazy(lazyRetry(() => import("./pages/Catalogue")));
const Apprendre = lazy(lazyRetry(() => import("./pages/Apprendre")));
const Semaine = lazy(lazyRetry(() => import("./pages/Semaine")));
const Partage = lazy(lazyRetry(() => import("./pages/Partage")));

// écrans qui n'ont besoin que de l'index des recettes : ils s'affichent sans attendre le détail (étapes, conseils…)
// Élargi le 21/11/2026 (audit dév senior §1) : ces pages n'affichent que des cartes (titre, région, temps) via
// MoreGrid/RecipeCard, jamais une étape, une astuce ou une conservation — vérifié un par un avant ajout.
const INDEX_ONLY = new Set([
  "",
  "explorer",
  "region",
  "recherche",
  "profil",
  "biblio",
  "imports",
  "credits",
  "apprendre",
  "dictionnaire",
  "ingredient",
  "icones",
  "frigo",
  "courses",
  "partage",
  "recettes",
  "techniques",
  "technique",
  "pains",
  "sauces",
  "fetes",
  "zero-dechet",
  "restes",
  "pique-nique",
  "street-food",
  "marinades",
]);
// écrans qui balaient tout le catalogue (conservation/congélation de chaque fiche) : ils ont besoin des 12 lots de
// détail, pas d'un seul ; tous les autres (une fiche, le mode cuisine) ne chargent que le lot de cette fiche.
const FULL_DETAIL_ROUTES = new Set(["semaine", "menu", "bien-choisir", "enfants"]);

const Loading = () => (
  <main className="page" id="contenu" tabIndex={-1} aria-busy="true">
    <p className="meta">Chargement…</p>
  </main>
);

export default function App() {
  const route = useRoute();
  const onboarded = useStore((s) => s.profile.onboarded);
  const settings = useStore((s) => s.settings);
  const pwa = usePwa();
  useTimerLoop();
  // l'écran change aussi sans changer d'adresse (fin de l'accueil de bienvenue) : l'état d'accueil fait partie de la clé
  useScreenChange(`${onboarded ? 1 : 0}|${route.path.join("/")}?${route.query.toString()}`);
  useUsageCounter(route.path[0]);
  useEffect(() => {
    recordStartup();
  }, []);

  useEffect(() => {
    const root = document.documentElement;
    if (settings.theme === "auto") root.removeAttribute("data-theme");
    else root.setAttribute("data-theme", settings.theme);
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
  const needsAllDetails = FULL_DETAIL_ROUTES.has(p0 ?? "");
  const allDetails = useDetails(needsAllDetails);
  const singleId = p0 === "recette" || p0 === "cuisine" ? p1 : undefined;
  const singleReady = useRecipeDetail(singleId);
  const needsDetails = !INDEX_ONLY.has(p0 ?? "");
  const detailsBlocked = needsAllDetails ? !allDetails : singleId ? !singleReady : false;
  if (p0 === "cuisine" && p1)
    return singleReady ? (
      <Suspense fallback={<Loading />}>
        <Cook id={p1} />
      </Suspense>
    ) : (
      <Loading />
    );
  if (!onboarded && p0 !== "profil")
    return (
      <Suspense fallback={<Loading />}>
        <Onboarding />
      </Suspense>
    );

  let page;
  switch (p0 ?? "") {
    case "":
      page = <Home />;
      break;
    case "explorer":
      page = <Explore />;
      break;
    case "region":
      page = <Region id={p1} />;
      break;
    case "recherche":
      page = <Search q={route.query.get("q") ?? ""} />;
      break;
    case "frigo":
      page = <Frigo key={route.query.get("avec") ?? ""} avec={route.query.get("avec") ?? ""} />;
      break;
    case "courses":
      page = <Courses />;
      break;
    case "recette":
      page = <RecipePage id={p1} q={route.query} />;
      break;
    case "techniques":
      page = <TechniquesPage />;
      break;
    case "technique":
      page = <TechniquePage id={p1} />;
      break;
    case "pains":
      page = <Pains />;
      break;
    case "sauces":
      page = <Sauces />;
      break;
    case "fetes":
      page = <Fetes />;
      break;
    case "menu":
      page = <MenuPage id={p1} />;
      break;
    case "zero-dechet":
      page = <ZeroDechet />;
      break;
    case "restes":
      page = <Restes key={route.query.get("r") ?? ""} preset={route.query.get("r")} />;
      break;
    case "bien-choisir":
      page = <Marche />;
      break;
    case "pique-nique":
      page = <PiqueNique />;
      break;
    case "street-food":
      page = <StreetFood />;
      break;
    case "marinades":
      page = <Marinades />;
      break;
    case "enfants":
      page = <Enfants />;
      break;
    case "imports":
      page = <Imports key={route.query.toString()} q={route.query} />;
      break;
    case "biblio":
      page = <Biblio />;
      break;
    case "profil":
      page = <Profil />;
      break;
    case "credits":
      page = <Credits />;
      break;
    case "apprendre":
      page = <Apprendre />;
      break;
    case "icones":
      if (!import.meta.env.DEV) {
        page = null;
        break;
      }
      page = (
        <main className="page" id="contenu" tabIndex={-1}>
          <h1>Icônes ATLAS</h1>
          <div className="icon-sheet">
            {ICON_NAMES.map((n) => (
              <figure key={n}>
                <Icon name={n} size={40} />
                <figcaption>{n}</figcaption>
              </figure>
            ))}
          </div>
        </main>
      );
      break;
    case "semaine":
      page = <Semaine key={route.query.get("ajout") ?? ""} add={route.query.get("ajout")} />;
      break;
    case "partage":
      page = <Partage key={route.query.get("d") ?? ""} d={route.query.get("d") ?? ""} />;
      break;
    case "recettes":
      page = <Catalogue q0={route.query.get("q") ?? ""} />;
      break;
    case "dictionnaire":
      page = <DictionaryPage q0={route.query.get("q") ?? ""} />;
      break;
    case "ingredient":
      page = <IngredientPage key={p1} slug={p1} />;
      break;
    default:
      page = (
        <main className="page" id="contenu" tabIndex={-1}>
          <h1>Page introuvable</h1>
          <a href={href("/")}>Retour à l'accueil</a>
        </main>
      );
  }
  const active = tabOf(p0); // fiche recette, mode cuisine : aucun onglet
  const onProfile = PROFILE_MATCH.includes(p0 ?? "");

  return (
    <div className="shell">
      <a
        className="skip"
        href="#contenu"
        onClick={(e) => {
          e.preventDefault();
          document.getElementById("contenu")?.focus();
        }}
      >
        Aller au contenu
      </a>
      <nav className="nav" aria-label="Navigation principale">
        <a className="brand" href={href("/")}>
          <img src="./icons/icon.svg" alt="" width="32" height="32" /> <span>ATLAS</span>
        </a>
        {TABS.map((t) => (
          <a key={t.to} href={href(t.to)} className={`tab ${active === t ? "on" : ""}`} aria-current={active === t ? "page" : undefined}>
            <span className="tab-ic" aria-hidden="true">
              <Icon name={t.icon} size={26} />
            </span>
            <span className="tab-lb">{t.label}</span>
          </a>
        ))}
        <a href={href("/profil")} className={`tab tab-profile ${onProfile ? "on" : ""}`} aria-current={onProfile ? "page" : undefined} aria-label="Profil et réglages">
          <span className="tab-ic" aria-hidden="true">
            <Icon name="chef" size={26} />
          </span>
          <span className="tab-lb">Profil</span>
        </a>
      </nav>
      <div className="content">
        {pwa.updateReady && (
          <div className="update" role="status">
            Une nouvelle version d'ATLAS est prête.{" "}
            <button className="btn small" onClick={applyUpdate}>
              Mettre à jour
            </button>
          </div>
        )}
        <ErrorBoundary resetKey={route.path.join("/")}>
          <Suspense fallback={<Loading />}>{needsDetails && detailsBlocked ? <Loading /> : page}</Suspense>
        </ErrorBoundary>
      </div>
      <TimerDock />
      <Toasts />
      <VideoHost />
    </div>
  );
}
