import random
from atlas_engine import *

I = {i.id: i for i in [
 Ingredient("lardons_porc", {"pork": "certain"}, set(), "A"),
 Ingredient("dinde_fumee", {}, set(), "A"),
 Ingredient("paprika_fume", {}, set(), "A"),
 Ingredient("gelatine", {"pork": "possible"}, set(), "B"),
 Ingredient("agar", {}, set(), "A"),
 Ingredient("vanille_extrait", {"alcohol": "certain"}, set(), "A"),
 Ingredient("vanille_poudre", {}, set(), "A"),
 Ingredient("sauce_soja", {"alcohol": "trace"}, {"SO", "GL"}, "A"),
 Ingredient("oeuf", {}, {"OE"}, "A"),
 Ingredient("huile", {}, set(), "A"), Ingredient("pates", {}, {"GL"}, "A"),
 Ingredient("creme", {}, {"LA"}, "A"), Ingredient("yaourt_grec", {}, {"LA"}, "A"),
 Ingredient("lait_amande", {}, {"FC"}, "A"),
 Ingredient("oignon", {}, set(), "A"), Ingredient("poulet", {}, set(), "A"),
 Ingredient("citron", {}, set(), "A"), Ingredient("riz", {}, set(), "A"),
]}
R = {}
def mk(id_, *lines, **kw):
    R[id_] = Recipe(id_, list(lines), **kw); return R[id_]
L = lambda i, w=2, q=100, opt=False: Line(ing=i, qty=q, weight=w, optional=opt)

rules = [Rule("r1", "lardons_porc", [("dinde_fumee", 1.0), ("paprika_fume", 0.005)], {"pork"}),
         Rule("r2", "gelatine", [("agar", 0.33)], {"pork"}),
         Rule("r3", "vanille_extrait", [("vanille_poudre", 0.1)], {"alcohol"}),
         Rule("r_draft", "sauce_soja", [("oignon", 1.0)], {"alcohol"}, status="draft")]

passed = 0
def check(name, cond):
    global passed
    print(("PASS " if cond else "FAIL ") + name); passed += cond; assert cond, name

# 1 porc certain => violates ; adaptable via règle validée ; recalcul vérifié
carbo = mk("carbonara", L("pates", 3), L("lardons_porc", 3), L("oeuf", 2))
r = evaluate(carbo, I, R)
check("1  lardons => pork=violates", r["pork"] == "violates")
check("2  règle validée => adaptable", availability(r, {"pork"}, False, rules) == "adaptable")
v = apply_substitutions(carbo, rules, I, R, {"pork"}, False)
check("3  variante recalculée sans porc", v["adapted"] and evaluate(v["recipe"], I, R)["pork"] == "ok")
# 4 gélatine = possible => uncertain : standard warning, strict hidden
mousse = mk("mousse", L("creme", 3), L("gelatine", 2))
r = evaluate(mousse, I, R)
check("4  gélatine => uncertain", r["pork"] == "uncertain")
check("5  standard => ok_warning", availability(r, {"pork"}, False, []) == "ok_warning")
check("6  strict sans règle => hidden", availability(r, {"pork"}, True, []) == "hidden")
check("7  strict avec règle agar => adaptable", availability(r, {"pork"}, True, rules) == "adaptable")
# 8 inconnu => jamais ok
mystere = mk("mystere", L("oignon"), L("ingredient_inconnu"))
r = evaluate(mystere, I, R)
check("8  ingrédient inconnu => uncertain + confiance C", r["pork"] == "uncertain" and r["confidence"] == "C")
check("9  inconnu en strict => hidden", availability(r, {"pork", "alcohol"}, True, []) == "hidden")
# 10 alcool : extrait de vanille certain ; traces selon strict
flan = mk("flan", L("creme", 3), L("vanille_extrait", 1))
r = evaluate(flan, I, R)
check("10 vanille liquide => alcohol=violates", r["alcohol"] == "violates")
check("11 règle poudre => adaptable", availability(r, {"alcohol"}, False, rules) == "adaptable")
wok = mk("wok", L("riz", 3), L("sauce_soja", 2))
r = evaluate(wok, I, R)
check("12 soja = trace : standard ok", availability(r, {"alcohol"}, False, rules) == "ok")
check("13 soja = trace : strict, règle draft => hidden", availability(r, {"alcohol"}, True, rules) == "hidden")
# 14 héritage allergènes via sous-recette
mayo = mk("mayo", L("oeuf", 3), L("huile", 3))
salade = mk("salade", Line(sub="mayo"), L("poulet", 3))
check("14 allergène hérité de la sous-recette", "OE" in evaluate(salade, I, R)["allergens"])
# 15 cycles
a = mk("A", Line(sub="B")); b = mk("B", Line(sub="A"))
try: evaluate(a, I, R); ok = False
except ValueError: ok = True
check("15 cycle de sous-recettes détecté", ok)
# 16 optionnel compte pour le régime
opt = mk("opt", L("riz", 3), L("lardons_porc", 0, opt=True))
check("16 lardons « facultatifs » comptent", evaluate(opt, I, R)["pork"] == "violates")
# 17 substitution qui introduit une incertitude => refusée
bad = [Rule("bad", "lardons_porc", [("gelatine", 1.0)], {"pork"})]
check("17 substitut incertain => adaptation refusée (invariant)",
      apply_substitutions(carbo, bad, I, R, {"pork"}, True)["adapted"] is False)
# 18 allergène introduit par un substitut : signalé (lardons -> sauce soja : SO apparaît, GL était déjà là)
soy = [Rule("soy", "lardons_porc", [("sauce_soja", 1.0)], {"pork"})]
out = apply_substitutions(carbo, soy, I, R, {"pork"}, False)
check("18 seul l allergène réellement introduit est signalé (SO ; GL déjà présent via les pâtes)", out["adapted"] and out["new_allergens"] == {"SO"})
# 19 crème -> lait d'amande : LA retiré, FC ajouté (calcul direct)
before = evaluate(Recipe("c", [L("creme", 3), L("poulet", 3)]), I, {})["allergens"]
after = evaluate(Recipe("x", [L("lait_amande", 3), L("poulet", 3)]), I, {})["allergens"]
check("19 LA retiré / FC ajouté", before == {"LA"} and after == {"FC"})
# 19b une règle ne s'applique pas à un ingrédient non fautif
cr = mk("sauce", L("creme", 3), L("poulet", 3))
irrel = [Rule("c", "creme", [("lait_amande", 1.0)], {"pork"})]
out = apply_substitutions(cr, irrel, I, R, {"pork"}, False)
check("19b règle non appliquée à un ingrédient non fautif (crème intacte)", out["adapted"] and any(l.ing == "creme" for l in out["recipe"].lines))
# propriétés aléatoires
rng = random.Random(42); ids = list(I)
def rand_recipe(n):
    return Recipe(f"rnd{n}", [L(rng.choice(ids), rng.randint(1, 3)) for _ in range(rng.randint(1, 8))])
mono = adapted = refused = violations = 0
for n in range(2000):
    rr = rand_recipe(n); base = evaluate(rr, I, {})["allergens"]
    extra = Recipe("e", rr.lines + [L(rng.choice(ids))])
    mono += base <= evaluate(extra, I, {})["allergens"]
    res = evaluate(rr, I, {})
    if availability(res, {"pork"}, True, rules) == "adaptable":
        v = apply_substitutions(rr, rules, I, {}, {"pork"}, True)
        if v["adapted"]:
            adapted += 1
            violations += evaluate(v["recipe"], I, {})["pork"] != "ok"
        else: refused += 1
check("20 propriété : ajouter un ingrédient ne retire jamais un allergène (2000 cas)", mono == 2000)
check(f"21 propriété : {adapted} variantes acceptées, 0 avec porc/incertitude (strict) ; {refused} refusées par le garde-fou", adapted > 20 and violations == 0)
# suggestion
S = [Recipe("riz_poulet", [L("riz", 3), L("poulet", 3), L("oignon", 2), L("citron", 1)]),
     Recipe("riz_oignon", [L("riz", 3), L("oignon", 2), L("citron", 1, opt=True)]),
     Recipe("creme_poulet", [L("creme", 2), L("poulet", 3)]),
     Recipe("carbonara", [L("pates", 3), L("lardons_porc", 3), L("oeuf", 2)])]
res = suggest(S, have={"riz", "poulet", "oignon"}, expiring={"oignon"})
d = {x["id"]: x for x in res}
check("22 « tu as tout » : riz_oignon", d["riz_oignon"]["bucket"] == "all")
check("23 1 manquant secondaire => « almost »", d["riz_poulet"]["bucket"] == "almost" and d["riz_poulet"]["missing"] == ["citron"])
res2 = suggest(S, have={"poulet", "yaourt_grec"}, subs={"creme": {"yaourt_grec"}})
d2 = {x["id"]: x for x in res2}
check("24 substitut compté (crème -> yaourt grec)", d2["creme_poulet"]["substitutes"] == {"creme": ["yaourt_grec"]})
# 25 manquant structurant : bonne couverture mais pénalité => exclue des idées (< 60)
struct = Recipe("struct", [L("viande_rare", 3), L("riz", 2), L("oignon", 2), L("citron", 2), L("poulet", 2)])
d3 = {x["id"]: x for x in suggest([struct], {"riz", "oignon", "citron", "poulet"})}
check("25 manquant structurant => exclue (couverture 72,7 % - 15 < 60)", "struct" not in d3)
# 26 anti-gaspi : à couverture égale, l'ingrédient proche de la DLC fait monter le score
pair = [Recipe("a", [L("riz", 3), L("oignon", 2)]), Recipe("b", [L("riz", 3), L("citron", 2)])]
d4 = {x["id"]: x for x in suggest(pair, {"riz", "oignon", "citron"}, expiring={"oignon"})}
check("26 bonus anti-gaspi (104 > 100)", d4["a"]["score"] == 104.0 and d4["b"]["score"] == 100.0)
# 27 garde-fou : substitut non possédé n'apporte aucun crédit
d5 = {x["id"]: x for x in suggest([Recipe("creme_poulet", [L("creme", 2), L("poulet", 3)])], {"poulet"}, subs={"creme": {"yaourt_grec"}})}
check("27 substitut non possédé => crème reste manquante", d5["creme_poulet"]["missing"] == ["creme"])
print(f"\n{passed} contrôles OK")
