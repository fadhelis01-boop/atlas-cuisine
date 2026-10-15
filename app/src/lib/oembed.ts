// Métadonnées publiques d'une vidéo à partir de son seul lien (oEmbed officiel : TikTok, YouTube, Vimeo).
// Rien n'est envoyé d'autre que le lien collé par l'utilisateur ; aucune clé, aucun compte. Si le service ne répond pas
// (hors connexion, lien privé), on retombe sur le titre tiré de l'adresse : le tri reste possible, en « à vérifier ».
export interface Meta { title: string; author: string; provider: string }

const ENDPOINTS: [RegExp, (u: string) => string][] = [
  [/tiktok\.com\//, (u) => `https://www.tiktok.com/oembed?url=${encodeURIComponent(u)}`],
  [/(youtube\.com|youtu\.be)\//, (u) => `https://www.youtube.com/oembed?format=json&url=${encodeURIComponent(u)}`],
  [/vimeo\.com\//, (u) => `https://vimeo.com/api/oembed.json?url=${encodeURIComponent(u)}`],
];

export const canFetchMeta = (url: string) => ENDPOINTS.some(([re]) => re.test(url));

export async function fetchMeta(url: string, timeoutMs = 8000, retries = 2): Promise<Meta | null> {
  for (let k = 0; k <= retries; k++) {
    const m = await fetchOnce(url, timeoutMs);
    if (m) return m;
    await new Promise((r) => setTimeout(r, 1200 * (k + 1)));
  }
  return null;
}

async function fetchOnce(url: string, timeoutMs: number): Promise<Meta | null> {
  const ep = ENDPOINTS.find(([re]) => re.test(url));
  if (!ep) return null;
  const ctl = new AbortController();
  const t = setTimeout(() => ctl.abort(), timeoutMs);
  try {
    const r = await fetch(ep[1](url), { signal: ctl.signal, credentials: "omit", referrerPolicy: "no-referrer" });
    if (!r.ok) return null;
    const j = (await r.json()) as { title?: string; author_name?: string; provider_name?: string };
    if (!j.title) return null;
    return { title: j.title.trim(), author: (j.author_name ?? "").trim(), provider: j.provider_name ?? "" };
  } catch {
    return null;
  } finally {
    clearTimeout(t);
  }
}
