# -*- coding: utf-8 -*-
"""Ajout de recettes SANS CODER : colle des liens (TikTok, YouTube, Instagram, Vimeo, sites de recettes…) dans
a_ajouter.md, un par ligne (un commentaire après le lien est permis), puis :
  - soit tu enregistres le fichier sur GitHub (l'automatisation .github/workflows/ajout-recettes.yml fait tout),
  - soit tu lances, sur ton PC : python ajout_auto.py   (puis l'export et la publication habituels).
Pour chaque lien : titre, légende et auteur·e sont lus (oEmbed officiel pour TikTok, YouTube, Vimeo ; titre de la page
pour les autres sites), la recette est triée avec les règles de classement.py (et la spécialité connue du créateur
si le titre ne suffit pas), le porc et l'alcool repérés dans le titre sont signalés, puis elle rejoint ajouts.json et
ajouts_classes.md (lu par bible/export_app_data.py). Les liens traités sont retirés de a_ajouter.md."""
import html, json, os, re, ssl, sys, time, urllib.parse, urllib.request
from collections import Counter, OrderedDict
from classement import section_of, flags_of, nrm, clean, LABELS

HERE = os.path.dirname(os.path.abspath(__file__))
INBOX, STORE, OUT = (os.path.join(HERE, f) for f in ("a_ajouter.md", "ajouts.json", "ajouts_classes.md"))
CA = r"C:\IA\tools\combined_cacert.pem"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()
UA = {"User-Agent": "ATLAS-cuisine/1.0 (https://github.com/fadhelis01-boop/atlas-cuisine)", "Accept-Language": "fr,en;q=0.8"}
HEADER = """# 📥 Recettes à ajouter

Colle un lien par ligne ci-dessous (TikTok, YouTube, Instagram, Vimeo ou page d'un site de recettes). Tu peux écrire un
commentaire après le lien. À l'enregistrement, chaque lien est lu, classé et publié dans ATLAS, puis retiré de cette liste.

<!-- liens sous cette ligne -->
"""

def get(url, raw=False):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), context=CTX, timeout=20) as r:
        b = r.read(600_000)
        return b if raw else json.loads(b)

def meta(url):
    eps = [(r"tiktok\.com/", "https://www.tiktok.com/oembed?url="), (r"(youtube\.com|youtu\.be)/", "https://www.youtube.com/oembed?format=json&url="),
           (r"vimeo\.com/", "https://vimeo.com/api/oembed.json?url=")]
    for rx, ep in eps:
        if re.search(rx, url):
            try:
                j = get(ep + urllib.parse.quote(url, safe=""))
                return j.get("title", "").strip(), j.get("author_name", "").strip(), j.get("provider_name", "")
            except Exception as e:
                print("  oEmbed indisponible :", str(e)[:80]); return "", "", ""
    try:  # autre site : titre de la page (og:title ou <title>)
        page = get(url, raw=True).decode("utf-8", "ignore")
        m = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)', page) or re.search(r"<title[^>]*>(.*?)</title>", page, re.S)
        site = re.search(r'<meta[^>]+property=["\']og:site_name["\'][^>]+content=["\']([^"\']+)', page)
        return (html.unescape(m.group(1)).strip() if m else ""), (html.unescape(site.group(1)).strip() if site else urllib.parse.urlparse(url).netloc), "site"
    except Exception as e:
        print("  page illisible :", str(e)[:80]); return "", urllib.parse.urlparse(url).netloc, "site"

def creator_sections():
    """Spécialité de chaque créateur déjà classé (rubrique la plus fréquente dans les fichiers classés)."""
    cnt = {}
    for f in ("createurs_youtube_classes.md", "createurs_tiktok_classes.md", "ajouts_classes.md"):
        p = os.path.join(HERE, f)
        if not os.path.exists(p): continue
        sec = None
        for line in open(p, encoding="utf-8"):
            if line.startswith("## "): sec = line[3:].split(" (")[0].strip(); continue
            m = re.search(r"· (?:▶ |@)([^·\n]+)", line)
            if m and sec and not sec.startswith("❓"): cnt.setdefault(re.sub(r"[^a-z0-9]", "", nrm(m.group(1))), Counter())[sec] += 1
    return {k: c.most_common(1)[0][0] for k, c in cnt.items()}

def source_of(url):
    for rx, s in ((r"tiktok\.com", "TikTok"), (r"youtu", "YouTube"), (r"instagram\.com", "Instagram"), (r"vimeo\.com", "Vimeo"), (r"pinterest\.", "Pinterest")):
        if re.search(rx, url): return s
    return "Site"

def main():
    store = json.load(open(STORE, encoding="utf-8")) if os.path.exists(STORE) else []
    known = {x["url"] for x in store}
    lines = open(INBOX, encoding="utf-8").read().split("\n") if os.path.exists(INBOX) else []
    todo = []
    for l in lines:
        m = re.search(r"https?://\S+", l)
        if m and not l.lstrip().startswith(("<!--", "#")): todo.append((m.group(0).rstrip(").,>"), l.replace(m.group(0), "").strip(" -–:·")))
    spec = creator_sections()
    added = 0
    for url, note in todo:
        url = re.sub(r"[?&](is_from_webapp|sender_device|utm_[a-z]+|si|feature)=[^&]*", "", url).rstrip("?&")
        if url in known: print("déjà ajouté :", url); continue
        print("lecture :", url)
        title, author, prov = meta(url)
        title = title or note or urllib.parse.unquote(url.rstrip("/").rsplit("/", 1)[-1]).replace("-", " ")
        default = spec.get(re.sub(r"[^a-z0-9]", "", nrm(author)), None)
        sec = section_of(title + (" " + note if note else ""), "a_verifier")
        if sec in (None,) : print("  hors recette, ignoré :", title[:60]); continue
        if sec == LABELS["a_verifier"] and default: sec = default
        store.append({"url": url, "title": clean(title) or title, "author": author, "source": source_of(url), "section": sec, "flags": flags_of(title), "note": note,
                      "date": time.strftime("%Y-%m-%d")})
        known.add(url); added += 1
        print(f"  → {sec} · {title[:70]}")
        time.sleep(0.5)
    json.dump(store, open(STORE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    groups = OrderedDict()
    for x in store:
        a = f" · ▶ {x['author']}" if x["author"] else ""
        groups.setdefault(x["section"], []).append(f"- [{x['title'][:110].replace('[', '(').replace(']', ')')}]({x['url']}){a} · {x['source']}{x['flags']}")
    o = ["# 📥 Recettes ajoutées par lien (classement automatique)\n", f"> {len(store)} recettes ajoutées via a_ajouter.md, triées par ajout_auto.py. Liens crédités seulement.\n"]
    for k, v in groups.items(): o.append(f"\n## {k} ({len(v)})\n"); o += v
    open(OUT, "w", encoding="utf-8").write("\n".join(o) + "\n")
    open(INBOX, "w", encoding="utf-8").write(HEADER)
    print(f"{added} recette(s) ajoutée(s) ; total {len(store)}.")
    return added

if __name__ == "__main__":
    sys.exit(0 if main() >= 0 else 1)
