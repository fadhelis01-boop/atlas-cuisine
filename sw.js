/* ATLAS — service worker : fonctionnement hors connexion (recettes, audio système, minuteurs)
   et détection des nouvelles versions. VERSION est remplacée à chaque compilation. */
const VERSION = "2026-11-23T23:11:57.032Z";
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
        const all = ["./assets/Apprendre-DzZKPb6P.js","./assets/Biblio-LyBY4npq.js","./assets/catalog-BgxRFi46.js","./assets/Catalogue-B3IZlTON.js","./assets/Cook-C1WuALj0.js","./assets/Courses-D3h-BUkd.js","./assets/credits-liSHl3w2.js","./assets/Credits-LwrN0-tV.js","./assets/dico-Cyy-v9rg.js","./assets/Enfants-i2UpsUoA.js","./assets/engine-BM7zDUtL.js","./assets/Fetes-BOXSbVC1.js","./assets/Frigo-BGXs7jFa.js","./assets/Household-BH6aF7vc.js","./assets/images_more-BXL_arQc.js","./assets/Imports-BwL9wiIy.js","./assets/imports-CQAEcQIo.js","./assets/index-BZobv3dF.css","./assets/index-CJq0BzT8.js","./assets/leftovers-rguCuhue.js","./assets/Marche-BAeENHHr.js","./assets/Marinades-Ck6pvisF.js","./assets/Menu-BDqanniK.js","./assets/Onboarding-DUHQ6WN9.js","./assets/Pains-YPx6YvS4.js","./assets/Partage-CmdU4VmO.js","./assets/partage-XrRf9Tro.js","./assets/PiqueNique-Cj-p9RWV.js","./assets/planner-jzJQ5ie3.js","./assets/Profil-DyD0Iian.js","./assets/recipes_detail_0-DGMUHvDj.js","./assets/recipes_detail_1-GG0vGz91.js","./assets/recipes_detail_10-uRoYvjuE.js","./assets/recipes_detail_11-D55f7-BQ.js","./assets/recipes_detail_2-CfS-36XP.js","./assets/recipes_detail_3-CCmYj2UW.js","./assets/recipes_detail_4-kusrLXA8.js","./assets/recipes_detail_5-CIxH4M4C.js","./assets/recipes_detail_6-Db_MqIu1.js","./assets/recipes_detail_7-CPuG-4uo.js","./assets/recipes_detail_8-DUCAxT_c.js","./assets/recipes_detail_9-BnQYuaYy.js","./assets/recipe_videos-C5nMBVMf.js","./assets/Restes-B-hHuhLd.js","./assets/Sauces-Bmgm7iVY.js","./assets/Semaine-BhGgF8m9.js","./assets/sendLink-wBNuR-8W.js","./assets/StreetFood-Bg8hR1LI.js","./assets/Techniques-BiB-1yzd.js","./assets/worldmap-BN1ZwdeE.js","./assets/ZeroDechet-4yutq4Ei.js"].filter((a) => a && !a.startsWith("__")); // liste complète écrite à la compilation
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
