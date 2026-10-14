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

def run(only=""):
    cand = json.load(open(os.path.join(HERE, "candidats.json"), encoding="utf-8"))
    sel = json.load(open(os.path.join(HERE, "selections.json"), encoding="utf-8"))
    man_path = os.path.join(APP, "src", "data", "images.json")
    man = json.load(open(man_path, encoding="utf-8")) if os.path.exists(man_path) else {}
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
        im = Image.open(src_file); im = ImageOps.exif_transpose(im).convert("RGB")
        im = grade(crop43(im, s.get("fx", 0.5), s.get("fy", 0.5), s.get("zoom", 1.0)), s.get("warm", 1.0))
        os.makedirs(os.path.join(OUT, kind), exist_ok=True)
        for w in SIZES:
            if im.width < w * 0.75 and w != SIZES[0]: continue  # pas d'agrandissement artificiel
            im.resize((w, int(w / RATIO)), Image.LANCZOS).save(os.path.join(OUT, kind, f"{ident}-{w}.webp"), "WEBP", quality=78, method=6)
        sizes = [w for w in SIZES if os.path.exists(os.path.join(OUT, kind, f"{ident}-{w}.webp"))]
        avg = im.resize((1, 1), Image.BOX).getpixel((0, 0))
        man[key] = {"path": f"img/{kind}/{ident}", "sizes": sizes, "color": "#%02x%02x%02x" % avg, "author": c["author"] or "Auteur·e inconnu·e",
                    "license": c["license"], "licenseUrl": c["license_url"], "page": c["page"], "source": c["src"], "title": c["title"], "kind": "photo"}
        print("ok", key, sizes, flush=True)
    json.dump(dict(sorted(man.items())), open(man_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    total = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(OUT) for f in fs)
    print(f"{len(man)} images · {total / 1e6:.1f} Mo")

if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else "")
