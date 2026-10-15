# -*- coding: utf-8 -*-
"""Traite les photos choisies (selections.json) : téléchargement en 1280 px, recadrage 4:3 (point d'intérêt réglable),
étalonnage commun « lumière naturelle, chaleureux, appétissant », WebP en 3 tailles, couleur dominante, crédits.
selections.json : { "recette/naan": 3, "recette/pesto": {"i": 1, "fx": 0.5, "fy": 0.4, "zoom": 1.1} }
  i = numéro sur la planche ; fx, fy = point d'intérêt (0-1) ; zoom = recadrage plus serré.
Sortie : ../app/public/img/<type>/<id>-<400|800|1200>.webp et ../app/src/data/images.json"""
import io, json, os, sys
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
from fetch_candidates import get

HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(HERE, "..", "app")
OUT = os.path.join(APP, "public", "img")
SIZES = (400, 800, 1200)
try:  # AVIF : Pillow 11.3+ (environnement illustrations/.venv) ; sinon WebP seul
    from PIL import features as _f
    AVIF = bool(_f.check("avif"))
except Exception:
    AVIF = False
RATIO = 4 / 3

def full_url(c):
    # Commons : vignette 1600 px plutôt que l'original (souvent 10-20 Mo)
    t = c.get("thumb") or ""
    if "wikimedia.org" in t and "/thumb/" in t and "px-" in t:  # upload. ou thumb.wikimedia.org
        import re
        # Wikimedia n'accepte que des largeurs standard (https://w.wiki/GHai) : 1280 px, ou l'original s'il est plus petit
        return re.sub(r"/\d+px-", "/1280px-", t) if c.get("w", 0) > 1280 else c["full"]
    return c["full"]

def grade(im: Image.Image, warm=1.0) -> Image.Image:
    """Étalonnage commun : un peu de contraste, de chaleur et de saturation, piqué léger. Volontairement discret."""
    im = ImageOps.autocontrast(im, cutoff=0.5, preserve_tone=True)
    r, g, b = im.split()
    r = r.point(lambda v: min(255, int(v * (1.0 + 0.03 * warm))))
    b = b.point(lambda v: int(v * (1.0 - 0.03 * warm)))
    im = Image.merge("RGB", (r, g, b))
    im = ImageEnhance.Contrast(im).enhance(1.05)
    im = ImageEnhance.Color(im).enhance(1.10)
    return im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=45, threshold=3))

def crop43(im, fx=0.5, fy=0.5, zoom=1.0):
    w, h = im.size
    cw, ch = (w, w / RATIO) if w / h < RATIO else (h * RATIO, h)
    cw, ch = cw / zoom, ch / zoom
    x0 = min(max(0, fx * w - cw / 2), w - cw); y0 = min(max(0, fy * h - ch / 2), h - ch)
    return im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch)))

def write_manifests(man, full_path, man_path):
    """Trois fichiers : le complet (ici), l'essentiel pour l'appli (chargé au démarrage : chemin, tailles, couleur)
    et les crédits (chargés seulement quand on les affiche), pour ne pas alourdir le démarrage de l'application."""
    json.dump(man, open(full_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    lite = {k: {"path": v["path"], "sizes": v["sizes"], "color": v["color"], **({"kind": "ia"} if v.get("kind") == "ia" else {}), **({"avif": 1} if v.get("avif") else {})} for k, v in man.items()}
    json.dump(lite, open(man_path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    cred = {k: {f: v.get(f, "") for f in ("author", "license", "licenseUrl", "page", "source", "title")} for k, v in man.items()}
    json.dump(cred, open(os.path.join(os.path.dirname(man_path), "credits.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

def run(only=""):
    cand = json.load(open(os.path.join(HERE, "candidats.json"), encoding="utf-8"))
    sel = json.load(open(os.path.join(HERE, "selections.json"), encoding="utf-8"))
    man_path = os.path.join(APP, "src", "data", "images.json")
    full_path = os.path.join(HERE, "images_full.json")  # manifeste complet (source de vérité, crédits compris)
    src = full_path if os.path.exists(full_path) else man_path
    man = json.load(open(src, encoding="utf-8")) if os.path.exists(src) else {}
    cache = os.path.join(HERE, "originaux"); os.makedirs(cache, exist_ok=True)
    for key, s in sel.items():
        if only and only not in key: continue
        s = s if isinstance(s, dict) else {"i": s}
        c = cand[s.get("from", key)][s["i"]]  # « from » : candidate prise dans un autre sujet
        kind, ident = key.split("/", 1)
        src_file = os.path.join(cache, key.replace("/", "__") + ".jpg")
        if not os.path.exists(src_file) or s.get("refresh"):
            import time; time.sleep(2.5)  # politesse envers upload.wikimedia.org
            try:
                b = get(full_url(c), raw=True, tries=3)
            except Exception as e:  # refus temporaire : on passe, une prochaine exécution reprendra
                print("plus tard", key, str(e)[:60], flush=True); continue
            open(src_file, "wb").write(b)
        done = [w for w in SIZES if os.path.exists(os.path.join(OUT, kind, f"{ident}-{w}.webp"))]
        if done and not s.get("refresh") and key in man and (not AVIF or all(os.path.exists(os.path.join(OUT, kind, f"{ident}-{w}.avif")) for w in done)):
            man[key]["avif"] = AVIF or man[key].get("avif", False); continue
        im = Image.open(src_file); im = ImageOps.exif_transpose(im).convert("RGB")
        im = grade(crop43(im, s.get("fx", 0.5), s.get("fy", 0.5), s.get("zoom", 1.0)), s.get("warm", 1.0))
        os.makedirs(os.path.join(OUT, kind), exist_ok=True)
        for w in (SIZES[:2] if kind == "ingredient" else SIZES):  # vignettes du dictionnaire : 1200 px inutile
            if im.width < w * 0.75 and w != SIZES[0]: continue  # pas d'agrandissement artificiel
            small = im.resize((w, int(w / RATIO)), Image.LANCZOS)
            webp = os.path.join(OUT, kind, f"{ident}-{w}.webp"); avif = os.path.join(OUT, kind, f"{ident}-{w}.avif")
            # on ne réécrit pas un fichier existant (sauf « refresh ») : Git ne revoit pas 1 000 photos identiques
            if s.get("refresh") or not os.path.exists(webp): small.save(webp, "WEBP", quality=78, method=6)
            if AVIF and (s.get("refresh") or not os.path.exists(avif)): small.save(avif, "AVIF", quality=52, speed=6)  # ~30 % plus léger
        sizes = [w for w in SIZES if os.path.exists(os.path.join(OUT, kind, f"{ident}-{w}.webp"))]
        avif = all(os.path.exists(os.path.join(OUT, kind, f"{ident}-{w}.avif")) for w in sizes)
        avg = im.resize((1, 1), Image.BOX).getpixel((0, 0))
        man[key] = {"path": f"img/{kind}/{ident}", "sizes": sizes, "color": "#%02x%02x%02x" % avg, "author": c["author"] or "Auteur·e inconnu·e",
                    "license": c["license"], "licenseUrl": c["license_url"], "page": c["page"], "source": c["src"], "title": c["title"], "kind": "photo", "avif": avif}
        print("ok", key, sizes, flush=True)
    write_manifests(dict(sorted(man.items())), full_path, man_path)
    total = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(OUT) for f in fs)
    print(f"{len(man)} images · {total / 1e6:.1f} Mo")

if __name__ == "__main__":
    if sys.argv[1:] == ["--manifestes"]:  # régénère seulement les manifestes de l'appli à partir du complet
        full = os.path.join(HERE, "images_full.json")
        mp = os.path.join(APP, "src", "data", "images.json")
        write_manifests(json.load(open(full if os.path.exists(full) else mp, encoding="utf-8")), full, mp)
    else:
        run(sys.argv[1] if len(sys.argv) > 1 else "")
