# -*- coding: utf-8 -*-
"""Collecte des candidates pour un préfixe de sujets (ex. « recette/ », « ingredient/ ») puis planches denses
(6 sujets × 8 photos) dans planches_v2/<préfixe>_NNN.jpg. Usage : python collect_v2.py recette/ [--sheets-only]"""
import json, os, sys
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageDraw, ImageFont
import fetch_candidates as F
from subjects import ALL

HERE = F.HERE
OUTD = os.path.join(HERE, "planches_v2"); os.makedirs(OUTD, exist_ok=True)
DONE_BEFORE = set(json.load(open(os.path.join(HERE, "selections.json"), encoding="utf-8")))

def collect(prefix):
    db_path = os.path.join(HERE, os.environ.get("ATLAS_DB", "candidats.json"))
    db = json.load(open(db_path, encoding="utf-8")) if os.path.exists(db_path) else {}
    keys = [k for k in ALL if k.startswith(prefix) and k not in DONE_BEFORE]
    todo = [k for k in keys if k not in db]
    def one(k):
        try: return k, F.candidates(k, ALL[k])
        except Exception as e: print("échec", k, e, flush=True); return k, []
    with ThreadPoolExecutor(int(os.environ.get("ATLAS_WORKERS", "1"))) as ex:
        for n, (k, c) in enumerate(ex.map(one, todo), 1):
            db[k] = c; print(f"[{n}/{len(todo)}] {k}: {len(c)}", flush=True)
            if n % 5 == 0: json.dump(db, open(db_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(db, open(db_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    jobs = []
    for k in keys:
        for i, c in enumerate(db.get(k, [])[:8]):
            c["file"] = os.path.join(F.CAND, k.replace("/", "__") + f"__{i}.jpg"); jobs.append((c["file"], c["thumb"]))
    with ThreadPoolExecutor(3) as ex: list(ex.map(lambda j: F.fetch_thumb(*j), jobs))
    json.dump(db, open(db_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return db, keys

def sheets(db, keys, prefix, per=6, tw=200, th=150):
    font = ImageFont.truetype("arial.ttf", 17); small = ImageFont.truetype("arial.ttf", 15)
    tag = prefix.strip("/")
    index = {}
    for s in range(0, len(keys), per):
        group = keys[s:s + per]; name = f"{tag}_{s // per:03d}.jpg"
        W = 8 * (tw + 4) + 8; H = len(group) * (th + 26) + 6
        sheet = Image.new("RGB", (W, H), (245, 240, 230)); d = ImageDraw.Draw(sheet)
        for r, k in enumerate(group):
            y = 4 + r * (th + 26); index[k] = name
            d.text((8, y), f"{r}. {k.split('/', 1)[1]}  —  {' | '.join(ALL[k])[:110]}", fill=(150, 50, 30), font=font)
            for i, c in enumerate(db.get(k, [])[:8]):
                x = 6 + i * (tw + 4)
                try:
                    im = Image.open(c["file"]).convert("RGB"); im.thumbnail((tw, th))
                    sheet.paste(im, (x + (tw - im.width) // 2, y + 22 + (th - im.height) // 2))
                except Exception: pass
                d.rectangle([x, y + 22, x + 20, y + 42], fill=(0, 0, 0)); d.text((x + 5, y + 23), str(i), fill=(255, 255, 255), font=small)
        sheet.save(os.path.join(OUTD, name), quality=80)
    json.dump(index, open(os.path.join(OUTD, f"{tag}_index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("planches :", (len(keys) + per - 1) // per, flush=True)

if __name__ == "__main__":
    prefix = sys.argv[1]
    if "--sheets-only" in sys.argv:
        db = json.load(open(os.path.join(HERE, os.environ.get("ATLAS_DB", "candidats.json")), encoding="utf-8"))
        keys = [k for k in ALL if k.startswith(prefix) and k not in DONE_BEFORE]
        for k in keys:
            for i, c in enumerate(db.get(k, [])[:8]): c["file"] = os.path.join(F.CAND, k.replace("/", "__") + f"__{i}.jpg")
    else:
        db, keys = collect(prefix)
    sheets(db, keys, prefix)
