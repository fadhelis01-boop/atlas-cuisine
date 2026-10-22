/* ATLAS — service worker : fonctionnement hors connexion (recettes, audio système, minuteurs)
   et détection des nouvelles versions. VERSION est remplacée à chaque compilation. */
const VERSION = "2026-10-22T13:31:13.214Z";
const APP_CACHE = "atlas-app-" + VERSION;
const IMG_CACHE = "atlas-img-v1"; // photos : gardées d'une version à l'autre (elles ne changent pas de nom)
const CORE = ["./", "./index.html", "./manifest.webmanifest", "./icons/icon.svg", "./icons/icon-192.png", "./icons/apple-touch-icon.png"];

self.addEventListener("install", (event) => {
  event.waitUntil(
    (async () => {
      const cache = await caches.open(APP_CACHE);
      await cache.addAll(CORE);
      try {
        const html = await (await fetch("./index.html", { cache: "reload" })).text();
        const assets = [...html.matchAll(/(?:src|href)="(\.\/assets\/[^"]+)"/g)].map((m) => m[1]);
        const all = ["./assets/Apprendre-C7AHXYhl.js","./assets/Biblio-B5AHP7GX.js","./assets/Catalogue-Xkx1Vw_8.js","./assets/Cook-DQKCMeZ6.js","./assets/Courses-BQi4ajZA.js","./assets/Credits-BvJpZ6s1.js","./assets/credits-VlhORFne.js","./assets/dico-CqeEF6aH.js","./assets/Enfants-DqW3fBVP.js","./assets/engine-Vx21YhFN.js","./assets/Fetes-BvA8qneF.js","./assets/Frigo-CK5MaIlt.js","./assets/Household-BtyHHhU0.js","./assets/images_more-BUnlqnMg.js","./assets/Imports-BkaLQ4yG.js","./assets/imports-CQUjUdJ7.js","./assets/index-BdgqyQpP.js","./assets/index-BwJtdXN7.css","./assets/leftovers-B4fcddqR.js","./assets/Marche-Bt5GYo1Q.js","./assets/Menu-Gk5rWmUV.js","./assets/Onboarding-GMP8fw59.js","./assets/Pains-7SpFrQBV.js","./assets/Partage-0yVJVrTj.js","./assets/partage-N-Yf7uPk.js","./assets/PiqueNique-DULvFH0Z.js","./assets/planner-DP-Vu0sk.js","./assets/Profil-DHIQQMJj.js","./assets/recipes_detail-Cz6LmUgw.js","./assets/recipe_videos-B6Vt7mKE.js","./assets/Restes-FlB7Wukl.js","./assets/Sauces-C7SGj8Wp.js","./assets/Semaine-SWO9QRJD.js","./assets/sendLink-C0_J6yhK.js","./assets/Techniques-CGbG5x8g.js","./assets/ZeroDechet-CLPWzqEC.js"].filter((a) => a && !a.startsWith("__")); // liste complète écrite à la compilation
        await cache.addAll([...new Set([...assets, ...all])]);
      } catch (e) {
        /* hors ligne pendant l'installation */
      }
    })(),
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    (async () => {
      for (const k of await caches.keys()) if (k.startsWith("atlas-app-") && k !== APP_CACHE) await caches.delete(k);
      await self.clients.claim();
    })(),
  );
});

self.addEventListener("message", (e) => {
  if (e.data === "skip-waiting") self.skipWaiting();
  if (e.data && e.data.type === "img-max") e.waitUntil(caches.open(IMG_CACHE).then((c) => c.put(CAP_KEY, new Response(String(e.data.value)))));
});

async function networkFirst(req, fallbackUrl) {
  const cache = await caches.open(APP_CACHE);
  try {
    const res = await fetch(req);
    if (res.ok) cache.put(fallbackUrl ?? req, res.clone());
    return res;
  } catch (e) {
    return (await cache.match(fallbackUrl ?? req)) || (await caches.match(req)) || Response.error();
  }
}

// plafond du cache photos (audit dév 🟠 8) : environ 400 images, soit 15 à 25 Mo ; les plus anciennes partent d'abord
// quand la personne a choisi « enregistrer toutes les photos », le plafond est levé (sinon on effacerait ce qu'elle vient de télécharger)
let IMG_MAX = 400;
let imgPuts = 0;
const CAP_KEY = "./__atlas-img-max";
async function currentMax(cache) { const r = await cache.match(CAP_KEY); return r ? Number(await r.text()) || IMG_MAX : IMG_MAX; }
async function trimImages(cache) {
  const max = await currentMax(cache);
  const keys = (await cache.keys()).filter((k) => !k.url.endsWith("__atlas-img-max")); // ordre d'insertion
  for (const k of keys.slice(0, Math.max(0, keys.length - max))) await cache.delete(k);
}

async function imgCache(req) {
  const cache = await caches.open(IMG_CACHE);
  const hit = await cache.match(req);
  if (hit) return hit;
  try {
    const res = await fetch(req);
    if (res.ok) { await cache.put(req, res.clone()); if (++imgPuts % 25 === 0) trimImages(cache); }
    return res;
  } catch (e) {
    return Response.error(); // hors ligne et photo jamais vue : l'appli affiche l'illustration de secours
  }
}

async function cacheFirst(req) {
  const hit = await caches.match(req);
  if (hit) return hit;
  const res = await fetch(req);
  if (res.ok) (await caches.open(APP_CACHE)).put(req, res.clone());
  return res;
}

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return; // liens TikTok, YouTube… : jamais mis en cache
  if (req.mode === "navigate") return event.respondWith(networkFirst(req, "./index.html"));
  if (url.pathname.includes("/assets/")) return event.respondWith(cacheFirst(req));
  if (url.pathname.includes("/img/")) return event.respondWith(imgCache(req));
  event.respondWith(networkFirst(req));
});

// Minuteur arrivé à échéance alors que l'application est en arrière-plan : la page demande l'affichage
self.addEventListener("notificationclick", (event) => {
  event.notification.close();
  event.waitUntil(self.clients.matchAll({ type: "window" }).then((cs) => (cs[0] ? cs[0].focus() : self.clients.openWindow("./"))));
});
