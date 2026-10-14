"""ATLAS : implémentation de référence (moteur diététique, substitutions, suggestion).
Objectif : valider la logique décrite dans les Tomes 1-3-8. Ce n'est PAS le code de production."""
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple

@dataclass
class Ingredient:
    id: str
    derivs: Dict[str, str] = field(default_factory=dict)   # kind -> 'certain' | 'possible' | 'trace'
    allergens: Set[str] = field(default_factory=set)
    verified: str = "C"                                    # A | B | C

@dataclass
class Line:
    ing: Optional[str] = None      # ingrédient canonique
    sub: Optional[str] = None      # sous-recette
    qty: float = 0.0
    weight: int = 2                # 0 optionnel/assaisonnement … 3 structurant
    optional: bool = False

@dataclass
class Recipe:
    id: str
    lines: List[Line]
    imported: bool = False

@dataclass
class Rule:                        # règle de substitution (extrait du schéma Tome 2 §5)
    id: str
    replaces: str
    items: List[Tuple[str, float]] # (ingrédient, ratio sur la quantité d'origine)
    satisfies: Set[str]            # {'pork','alcohol'}
    status: str = "validated"      # draft | testing | validated | retired

ORDER = {"ok": 0, "trace": 1, "uncertain": 2, "violates": 3}

def _walk(r: Recipe, recipes: Dict[str, Recipe], stack=()):
    """Aplatit les ingrédients (sous-recettes incluses). Détecte les cycles."""
    if r.id in stack:
        raise ValueError(f"cycle de sous-recettes : {' -> '.join(stack + (r.id,))}")
    for ln in r.lines:
        if ln.sub:
            yield from _walk(recipes[ln.sub], recipes, stack + (r.id,))
        else:
            yield ln

def evaluate(r: Recipe, ings: Dict[str, Ingredient], recipes: Dict[str, Recipe]):
    res = {"pork": "ok", "alcohol": "ok", "allergens": set(), "uncertain_allergens": False,
           "unknown": [], "offenders": {"pork": [], "alcohol": []}, "confidence": "A"}
    def bump(kind, st, ing_id):
        if ORDER[st] > ORDER[res[kind]]:
            res[kind] = st
        if st in ("violates", "uncertain", "trace"):
            res["offenders"][kind].append(ing_id)
    for ln in _walk(r, recipes):
        ing = ings.get(ln.ing)
        if ing is None:                                   # inconnu => JAMAIS « ok »
            res["unknown"].append(ln.ing)
            bump("pork", "uncertain", ln.ing); bump("alcohol", "uncertain", ln.ing)
            res["uncertain_allergens"] = True
            res["confidence"] = "C"
            continue
        for kind, key in (("pork", "pork"), ("alcohol", "alcohol")):
            lvl = ing.derivs.get(key)
            if lvl == "certain": bump(kind, "violates", ing.id)
            elif lvl == "possible": bump(kind, "uncertain", ing.id)
            elif lvl == "trace": bump(kind, "trace", ing.id)
        res["allergens"] |= ing.allergens                  # les « optionnels » comptent aussi
        if ing.verified == "C": res["confidence"] = "C"
        elif ing.verified == "B" and res["confidence"] == "A": res["confidence"] = "B"
    if r.imported: res["confidence"] = "C"
    return res

def availability(res, constraints: Set[str], strict: bool, rules: List[Rule]):
    """ok | ok_warning | adaptable | hidden  (Tome 1 §7.1 et §7.5)"""
    worst = "ok"
    need_sub = set(); warn = False
    for c in constraints:
        st = res[c]
        if st == "trace": st = "violates" if strict else "ok"
        if st == "uncertain":
            if strict: st = "violates"
            else: warn = True; continue
        if st == "violates":
            need_sub |= set(res["offenders"][c])
    if need_sub:
        covered = {ru.replaces for ru in rules if ru.status == "validated" and ru.satisfies & constraints}
        return "adaptable" if need_sub <= covered else "hidden"
    return "ok_warning" if warn else "ok"

def apply_substitutions(r: Recipe, rules: List[Rule], ings, recipes, constraints: Set[str], strict: bool):
    """Réécrit la recette en ne remplaçant QUE les ingrédients fautifs, puis REVÉRIFIE
    le résultat (invariant : jamais d'adaptation « présumée »)."""
    before = evaluate(r, ings, recipes)
    offenders = set()
    for c in constraints:
        st = before[c]
        if st == "trace" and not strict: continue
        if st == "uncertain" and not strict: continue
        offenders |= set(before["offenders"][c])
    by = {ru.replaces: ru for ru in rules
          if ru.status == "validated" and ru.satisfies & constraints and ru.replaces in offenders}
    new_lines = []
    for ln in r.lines:
        if ln.ing in by:
            for ing_id, ratio in by[ln.ing].items:
                new_lines.append(Line(ing=ing_id, qty=ln.qty * ratio, weight=ln.weight, optional=ln.optional))
        else:
            new_lines.append(ln)
    r2 = Recipe(r.id + "#variant", new_lines, r.imported)
    after = evaluate(r2, ings, {**recipes, r2.id: r2})
    ok = availability(after, constraints, strict, []) in ("ok", "ok_warning")
    return {"recipe": r2 if ok else None, "adapted": ok,
            "new_allergens": after["allergens"] - before["allergens"]}

# ---------------------------------------------------------------- suggestion (Tome 1 §6.3)
STAPLES = {"sel", "poivre", "eau", "huile", "sucre", "farine", "vinaigre", "moutarde"}

def suggest(recipes: List[Recipe], have: Set[str], expiring: Set[str] = frozenset(),
            subs: Dict[str, Set[str]] = None, staples=STAPLES, sub_credit=0.8):
    subs = subs or {}
    out = []
    for r in recipes:
        req = [l for l in r.lines if l.weight > 0 and not l.optional and l.ing]
        if not req: continue
        tot = sum(l.weight for l in req); got = 0.0; missing = []; used_sub = {}
        for l in req:
            if l.ing in have or l.ing in staples: got += l.weight
            elif subs.get(l.ing, set()) & have:
                got += l.weight * sub_credit; used_sub[l.ing] = sorted(subs[l.ing] & have)
            else: missing.append(l)
        score = 100 * got / tot
        score -= 15 * sum(1 for l in missing if l.weight == 3)          # manquant structurant
        score += 4 * len({l.ing for l in req} & set(expiring))          # bonus anti-gaspi
        bucket = "all" if not missing else ("almost" if len(missing) <= 2 and
                 not any(l.weight == 3 for l in missing) else ("ideas" if score >= 60 else None))
        if bucket: out.append({"id": r.id, "score": round(score, 1), "bucket": bucket,
                               "missing": [l.ing for l in missing], "substitutes": used_sub})
    return sorted(out, key=lambda x: (-x["score"], x["id"]))
