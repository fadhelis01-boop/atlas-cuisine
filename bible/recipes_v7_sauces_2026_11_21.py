# -*- coding: utf-8 -*-
"""Audit amateur indécis du coin Sauces (21/11/2026) : 3 angles morts comblés par de vraies fiches — les sauces de
fast-food américain (quasi absentes, alors que le franco-belge était bien couvert), 2 sauces mères françaises qui
n'existaient qu'en fond de cuisine (Velouté, Espagnole) plus Périgueux et Chasseur jamais autonomes, l'aïoli et la
rémoulade françaises noyées dans d'autres plats, et une poignée de classiques du monde ciblés (tonkatsu, unagi,
ssamjang, zhug, baba ganoush, banana ketchup). NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *
from recipes_v6_tiktok_plats import C

TT = "https://www.tiktok.com/"
def V(author, vid):
    return (f"@{author}", f"{TT}@{author}/video/{vid}")

US = "Amérique du Nord › États-Unis"; FR_BASE = "France › Cuisine de base"; FR_SAUCES = "France › Sauces"
JP = "Asie de l'Est › Japon"; KR = "Asie de l'Est › Corée"; YE = "Moyen-Orient › Yémen"
LB = "Moyen-Orient › Liban"; PH = "Asie du Sud-Est › Philippines"
MOUT_JAUNE = "Moutarde jaune américaine (douce)"; RAIFORT = "Raifort (crème ou râpé)"
CHAMPI = "Champignon de Paris"; VINBLANC = "Vin blanc"; MADERE = "Madère / marsala / xérès"
CORNICHON = "Cornichon"; WORCESTER = "Sauce Worcestershire"; ESTRAGON = "Estragon"; CARDA = "Cardamome"
PLANTAIN = "Plantain (banane à cuire)"; CEB = "Oignon nouveau / cébette"; AUBERGINE = "Aubergine"

# ---------------------------------------------------------------- Fast-food (angle mort n°3)
K("sauce_big_mac", "Sauce Big Mac maison (sauce burger secrète)", "Big Mac special sauce", US, "S", 1, 8, 10, 30, "€",
  "Bol, fouet.",
  "La sauce rosée et acidulée du burger le plus copié au monde : de la mayonnaise, des cornichons hachés très "
  "fin, de la moutarde douce et du paprika. Aucun ingrédient rare, juste les bonnes proportions.",
  ["20 cl|de mayonnaise (fiche Mayonnaise)|SUB:mayonnaise|3", f"2 c. à s.|de cornichons hachés très fin|{CORNICHON}|2",
   f"1 c. à c.|de moutarde jaune américaine|{MOUT_JAUNE}|1", f"1 c. à c.|de vinaigre blanc|Vinaigre blanc|1",
   f"1 c. à c.|de paprika doux|{PAPRIKA}|1", "1 c. à c.|de poudre d'ail et d'oignon mélangées|Poudre d'ail / d'oignon|1",
   f"1/2 c. à c.|de sucre|{SUCRE}|1"],
  ["**Mélanger.** Tous les ingrédients fouettés ensemble jusqu'à une sauce rosée bien homogène.",
   "**Reposer.** Au moins 30 min au frigo avant de servir : les saveurs se mélangent et se rapprochent de "
   "l'originale.",
   "**Servir.** Sur un burger double, en nappage, ou en sauce à tremper pour des nuggets et des frites."],
  tips=["Les cornichons doivent être hachés très fin, presque en purée : c'est ce qui donne la texture lisse de "
        "l'originale, pas des morceaux.", "Se garde une semaine : prépare-la en double, elle disparaît vite."],
  keep="1 semaine au frigo, dans un bocal fermé.", age=2, kids="✓ dès 2 ans.", cats=["sauces"], profil=["acide", "gras"])
K("sauce_chick_fil_a", "Sauce façon Chick-fil-A (miel, moutarde et barbecue)", "Chick-fil-A sauce", US, "S", 1, 8, 5, 0, "€",
  "Bol, fouet.",
  "Le secret de cette sauce culte n'est pas un ingrédient mystère mais un mélange : mayonnaise, moutarde, miel "
  "et sauce barbecue, pour un goût à la fois doux, acidulé et fumé.",
  [f"12 cl|de mayonnaise (fiche Mayonnaise)|SUB:mayonnaise|3", f"3 c. à s.|de miel|{MIEL}|2",
   f"2 c. à s.|de moutarde de Dijon|{DIJON}|1", "3 c. à s.|de sauce barbecue (fiche Sauce barbecue)|SUB:sauce_barbecue|1",
   f"1 c. à c.|de jus de citron|{CIT}|1"],
  ["**Mélanger.** Tous les ingrédients fouettés ensemble jusqu'à une sauce lisse et brillante.",
   "**Goûter et ajuster.** Plus de miel pour plus de douceur, plus de moutarde pour plus de piquant.",
   "**Servir.** Pour tremper des nuggets ou des tenders de poulet pané, ou en sauce de burger au poulet."],
  tips=["Cette sauce est elle-même une combinaison : elle réutilise la fiche maison de la mayonnaise et de la "
        "sauce barbecue plutôt que de repartir de zéro."],
  keep="1 semaine au frigo.", age=2, kids="✓ dès 2 ans.", cats=["sauces"], profil=["sucre"])
K("sauce_alabama_blanche", "Sauce blanche Alabama (barbecue au poivre, pour poulet fumé)", "Alabama white sauce", US, "S", 1, 10, 10, 30, "€",
  "Bol, fouet.",
  "La sauce barbecue blanche du nord de l'Alabama, inventée pour le poulet fumé plutôt que pour les côtes de "
  "porc : mayonnaise, vinaigre, beaucoup de poivre noir et une pointe de raifort, sans aucune tomate.",
  [f"25 cl|de mayonnaise (fiche Mayonnaise)|SUB:mayonnaise|3", f"4 c. à s.|de vinaigre de cidre|{CIDRE}|2",
   f"2 c. à c.|de poivre noir moulu généreusement|{POIVRE}|1", f"1 c. à c.|de raifort|{RAIFORT}|1?",
   f"1 c. à c.|de jus de citron|{CIT}|1", f"1 c. à c.|de sucre|{SUCRE}|1", f"-|sel|{SEL}|1"],
  ["**Mélanger.** Tous les ingrédients fouettés ensemble ; le poivre doit vraiment se voir dans la sauce, pas "
   "juste se deviner.",
   "**Reposer.** Au moins 30 min au frigo, idéalement plusieurs heures : le poivre infuse.",
   "**Servir.** Badigeonnée sur du poulet fumé ou grillé à la sortie du barbecue, jamais pendant la cuisson (elle "
   "brûlerait)."],
  tips=["Sans raifort, la sauce reste très bonne : c'est le poivre généreux qui fait l'essentiel du caractère."],
  keep="1 semaine au frigo.", age=3, kids="✓ dès 3 ans, moins de poivre.", cats=["sauces"], profil=["acide"])
K("sauce_yum_yum", "Sauce yum yum (sauce rose des teppanyaki américains)", "Yum yum sauce", US, "S", 1, 8, 5, 60, "€",
  "Bol, fouet.",
  "La sauce rose sucrée-fumée servie dans les restaurants japonais-américains de grill à la plancha (teppanyaki) "
  "avec le riz et les légumes sautés : mayonnaise, ketchup, beurre fondu et paprika, détendue à l'eau.",
  [f"25 cl|de mayonnaise (fiche Mayonnaise)|SUB:mayonnaise|3", f"3 c. à s.|de ketchup (fiche Ketchup)|SUB:ketchup|2",
   f"2 c. à s.|de beurre fondu|{BEURRE}|1", f"1 c. à c.|de paprika doux|{PAPRIKA}|1",
   "1 c. à c.|de poudre d'ail|Poudre d'ail / d'oignon|1", f"1 c. à c.|de sucre|{SUCRE}|1",
   f"2 à 4 c. à s.|d'eau, pour détendre|{EAU}|1"],
  ["**Mélanger.** Mayonnaise, ketchup, beurre fondu tiède, paprika, poudre d'ail et sucre fouettés ensemble.",
   "**Détendre.** Eau ajoutée cuillère par cuillère jusqu'à une texture nappante, pas liquide.",
   "**Reposer.** Au moins 1 h au frigo (toute une nuit, c'est encore mieux) : le goût se développe nettement."],
  tips=["Le secret des restaurants n'est pas un ingrédient caché : c'est le temps de repos, souvent une nuit "
        "entière, qui change tout."],
  keep="1 semaine au frigo.", age=2, kids="✓ dès 2 ans.", cats=["sauces"], profil=["sucre", "gras"])
K("sauce_douce_acidulee_mcdo", "Sauce douce et acidulée façon McDonald's (sweet and sour)", "Sweet and sour sauce", US, "S", 1, 6, 10, 0, "€",
  "Petite casserole, fouet.",
  "La sauce orange translucide des nuggets, à base de confitures plutôt que de fruits frais : abricot et pêche "
  "donnent la couleur et le fondant, le vinaigre et la moutarde l'équilibrent.",
  ["4 c. à s.|de confiture d'abricot|Confiture / gelée|2", "4 c. à s.|de confiture de pêche|Confiture / gelée|2",
   f"1 c. à s.|de miel|{MIEL}|1", "5 c. à c.|de vinaigre de vin blanc|Vinaigre de vin rouge / blanc|1",
   f"1/2 c. à c.|de sauce soja|{SOJA}|1", f"1/2 c. à c.|de moutarde de Dijon|{DIJON}|1"],
  ["**Chauffer.** Confitures et miel à feu doux 2 min, en remuant : elles fondent en un sirop.",
   "**Mélanger.** Vinaigre, soja et moutarde ajoutés hors du feu, fouettés ensemble.",
   "**Mixer (facultatif).** Un coup de mixeur plongeur si des morceaux de fruit restent, pour une sauce bien "
   "lisse et translucide comme l'originale.",
   "**Refroidir.** Complètement avant de servir : elle épaissit légèrement en refroidissant."],
  keep="2 semaines au frigo.", age=2, kids="✓ dès 2 ans.", cats=["sauces"], profil=["sucre", "acide"],
  credit=C(V("simplylemmons", "7593867958732983583")))

# ---------------------------------------------------------------- Sauces mères et classiques français (angle mort n°4)
K("sauce_veloute", "Velouté (sauce mère au fond blanc)", "Velouté", FR_BASE, "S", 2, 6, 10, 15, "€",
  "Casserole, fouet.",
  "La deuxième des 5 sauces mères françaises, cousine blonde de la béchamel : un roux cuit plus longtemps, "
  "mouillé non pas au lait mais à un fond blanc (volaille, veau ou poisson selon ce qu'elle doit accompagner).",
  [f"40 g|de beurre|{BEURRE}|2", f"40 g|de farine|{F55}|2", "50 cl|de fond blanc de volaille, chaud (fiche Fond blanc de volaille)|SUB:fond_blanc_volaille|3",
   f"-|sel, poivre blanc|{SEL}|1", f"1 c. à s.|de crème, pour une liaison plus riche|{CF}|1?"],
  ["**Roux.** Beurre fondu, farine ajoutée hors du feu puis remise sur feu doux 2 à 3 min en remuant sans cesse : "
   "doit rester blond, à peine coloré (plus long que pour une béchamel).",
   "**Mouiller.** Fond chaud versé en 3 fois en fouettant fort entre chaque ajout, pour éviter les grumeaux.",
   "**Cuire.** 10 min à frémissement doux en remuant souvent : elle épaissit et nappe le dos d'une cuillère.",
   "**Finir.** Sel, poivre blanc, et la crème si utilisée, hors du feu."],
  tips=["Change de fond, change de velouté : fond de volaille pour une blanquette, fond de poisson pour une "
        "sauce de poisson poché (la base de la sauce Nantua ou normande).", "Passée au chinois, elle devient "
        "parfaitement lisse pour les présentations soignées."],
  keep="3 jours au frigo ; se congèle.", age=2, kids="✓ dès 2 ans.", cats=["sauces"], profil=["gras"])
K("sauce_espagnole", "Espagnole (sauce mère brune, base de la demi-glace)", "Sauce espagnole", FR_BASE, "S", 2, 6, 15, 45, "€",
  "Casserole, chinois.",
  "La sauce mère brune, plus longue à faire que ses cousines mais la base de toutes les sauces brunes de "
  "bistrot (bordelaise, chasseur, poivrade, Périgueux) : un roux brun, un fond brun de veau, une mirepoix et un "
  "peu de tomate qui réduisent longuement ensemble.",
  [f"30 g|de beurre|{BEURRE}|2", f"30 g|de farine|{F55}|2", "75 cl|de fond brun de veau (fiche Fond brun de veau)|SUB:fond_brun_veau|3",
   f"1|carotte, en petits dés|{CAROTTE}|1", f"1|oignon, en petits dés|{OIG}|1", f"1 c. à s.|de concentré de tomate|{CONC}|1",
   f"-|sel, poivre|{SEL}|1"],
  ["**Roux brun.** Beurre fondu, farine ajoutée, cuite à feu doux 5 à 8 min en remuant sans arrêt jusqu'à une "
   "couleur noisette (plus foncée qu'un roux blanc : c'est elle qui colore la sauce).",
   "**Mirepoix.** Carotte et oignon ajoutés, 3 min à revenir dans le roux.",
   "**Mouiller.** Fond brun chaud versé peu à peu en fouettant, concentré de tomate ajouté.",
   "**Réduire.** 30 à 45 min à tout petits frémissements, écumée de temps en temps : elle réduit et se "
   "concentre en goût.",
   "**Passer.** Au chinois fin, en pressant les légumes pour en extraire le jus ; sel, poivre."],
  tips=["C'est de cette sauce que partent la plupart des grandes sauces brunes classiques : une fois maîtrisée, "
        "bordelaise, chasseur et Périgueux ne sont plus que quelques ingrédients ajoutés à la fin."],
  keep="3 jours au frigo ; se congèle très bien en portions.", age=3, kids="Pour les grands.", cats=["sauces"],
  profil=["gras"])
K("sauce_perigueux", "Sauce Périgueux (demi-glace, truffe et madère)", "Sauce Périgueux", FR_SAUCES, "S", 2, 6, 10, 15, "€",
  "Petite casserole.",
  "La sauce espagnole réduite encore un peu (une demi-glace) puis parfumée au madère et à la truffe : la grande "
  "sauce des tournedos et des volailles de fête.",
  ["40 cl|de sauce espagnole (fiche Espagnole)|SUB:sauce_espagnole|3", f"5 cl|de madère|{MADERE}|2",
   "1|petite truffe (ou pelures de truffe en bocal)|Truffe (fraîche ou pelures)|1", f"20 g|de beurre froid|{BEURRE}|1"],
  ["**Réduire.** Sauce espagnole portée à petit frémissement 10 min, jusqu'à napper franchement une cuillère "
   "(c'est la demi-glace).",
   "**Parfumer.** Madère ajouté, 2 min pour que l'alcool s'évapore ; truffe en lamelles ou en petits morceaux "
   "ajoutée.",
   "**Lier.** Hors du feu, beurre froid incorporé en fouettant pour une sauce brillante et soyeuse."],
  tips=["Sans alcool : remplace le madère par 5 cl de fond brun réduit avec 1 c. à c. de vinaigre de xérès — le "
        "goût change mais la sauce reste réussie."],
  var=[("Sans alcool", ["alcohol"], {MADERE: [("Bouillon liquide (type fond)", 1.0)]}, "Madère → **fond réduit avec un trait de vinaigre de xérès**. **À tester**.")],
  keep="3 jours au frigo.", age=4, kids="Pour les grands, à cause de l'alcool (sauf version sans alcool).",
  cats=["sauces"], fetes=["Noël et Nouvel An", "Repas de famille"], profil=["gras"])
K("sauce_chasseur", "Sauce chasseur (champignons, échalote, tomate, vin blanc)", "Sauce chasseur", FR_SAUCES, "S", 1, 6, 10, 20, "€",
  "Poêle, casserole.",
  "La sauce brune aux champignons de toutes les escalopes et poulets sautés de bistrot : échalote et "
  "champignons revenus, déglacés au vin blanc, liés à l'espagnole ou à un fond réduit, finis à l'estragon.",
  [f"250 g|de champignons de Paris, émincés|{CHAMPI}|3", f"2|échalotes, hachées|{ECH}|2",
   f"10 cl|de vin blanc sec|{VINBLANC}|2", "30 cl|de sauce espagnole ou de fond brun réduit|SUB:sauce_espagnole|2",
   f"1 c. à s.|de concentré de tomate|{CONC}|1", f"1 c. à c.|d'estragon|{ESTRAGON}|1", f"20 g|de beurre|{BEURRE}|1"],
  ["**Champignons.** Émincés revenus dans le beurre à feu vif 5 min : ils dorent sans rendre trop d'eau.",
   "**Échalote.** Ajoutée, 2 min à peine translucide.",
   "**Déglacer.** Vin blanc versé, porté à ébullition 2 min pour évaporer l'alcool : le fond de poêle se "
   "décolle.",
   "**Lier.** Sauce espagnole et concentré de tomate ajoutés, 5 min à petit frémissement ; estragon à la fin."],
  tips=["Sans alcool : remplace le vin blanc par du fond blanc additionné d'un trait de jus de citron.",
        "Cette sauce accompagne classiquement une escalope ou un poulet sauté : la poêle de cuisson de la "
        "viande sert aussi à faire la sauce, pour récupérer les sucs."],
  var=[("Sans alcool", ["alcohol"], {VINBLANC: [("Bouillon liquide (type fond)", 1.0)]}, "Vin blanc → **fond blanc et jus de citron**. **À tester**.")],
  keep="2 jours au frigo.", age=3, kids="✓ dès 3 ans (version sans alcool).", cats=["sauces"], profil=["acide"])

# ---------------------------------------------------------------- Aïoli et rémoulade (angle mort n°5)
K("aioli", "Aïoli (mayonnaise à l'ail, Provence)", "Aïoli", "France › Provence-Alpes-Côte d'Azur", "S", 1, 6, 15, 0, "€",
  "Mortier ou bol, fouet.",
  "Le vrai aïoli provençal n'est pas une mayonnaise à laquelle on ajoute de l'ail : c'est l'ail lui-même qui est "
  "monté à l'huile, le jaune d'œuf ne servant qu'à stabiliser l'émulsion. Pour accompagner légumes vapeur, "
  "poisson poché ou une soupe de poisson.",
  [f"6 à 8 gousses|d'ail, dégermées|{AIL}|3", f"1|jaune d'œuf très frais|{OEUF}|2",
   f"20 cl|d'huile d'olive, à température ambiante|{HO}|2", f"1 c. à c.|de jus de citron|{CIT}|1", f"-|sel|{SEL}|1"],
  ["**Piler.** Ail dégermé (le germe central donne un goût âcre) pilé au mortier avec une pincée de sel jusqu'à "
   "une pâte lisse ; à défaut, ail écrasé très fin au couteau.",
   "**Monter.** Jaune d'œuf ajouté et mélangé, puis huile versée en tout petit filet continu en fouettant sans "
   "arrêt (comme une mayonnaise) : l'émulsion prend et épaissit.",
   "**Finir.** Jus de citron et sel ajoutés en fouettant ; texture d'une mayonnaise ferme qui tient sur une "
   "cuillère."],
  tips=["Si l'émulsion « tranche » (elle se sépare), recommence avec un nouveau jaune d'œuf dans un bol propre "
        "et verse l'aïoli raté dessus petit à petit, comme pour rattraper une mayonnaise.",
        "Moins d'ail et un peu de pomme de terre vapeur écrasée dedans donnent une version plus douce et plus "
        "nappante, plus proche de certains aïolis commerciaux."],
  keep="3 jours au frigo.", age=4, kids="Pour les grands (œuf cru, goût très prononcé).", cats=["sauces"],
  profil=["gras"])
K("remoulade_francaise", "Sauce rémoulade française (mayonnaise, moutarde, cornichons et câpres)", "Rémoulade", FR_SAUCES, "S", 1, 8, 10, 0, "€",
  "Bol, fouet.",
  "La rémoulade des bistrots français : une mayonnaise bien moutardée, parsemée de cornichons, de câpres et "
  "d'herbes hachées — différente de la sauce tartare, plus simple et plus anglo-saxonne, déjà dans ce coin.",
  [f"20 cl|de mayonnaise (fiche Mayonnaise)|SUB:mayonnaise|3", f"1 c. à s.|de moutarde de Dijon|{DIJON}|1",
   f"2 c. à s.|de cornichons hachés|{CORNICHON}|2", "1 c. à s.|de câpres hachées|Câpres|1",
   f"1 c. à s.|de persil haché|{PERSIL}|1", f"1 c. à c.|d'estragon haché|{ESTRAGON}|1?",
   "2|filets d'anchois, écrasés|Anchois (filets, conserve)|1?"],
  ["**Mélanger.** Mayonnaise et moutarde fouettées ensemble.",
   "**Ajouter.** Cornichons, câpres, persil, estragon et anchois si utilisés, incorporés à la cuillère.",
   "**Servir.** Avec un poisson pané ou froid, des crudités, ou en sauce de céleri rémoulade (remplace alors la "
   "mayonnaise nature de cette fiche)."],
  tips=["Les anchois ne se sentent pas comme un goût de poisson une fois écrasés dans la sauce : ils apportent "
        "surtout du sel et de la profondeur, comme dans une sauce César."],
  keep="4 jours au frigo.", age=2, kids="✓ dès 2 ans, sans anchois.", cats=["sauces"], profil=["acide"])

# ---------------------------------------------------------------- Classiques du monde ciblés (angle mort n°6)
K("sauce_tonkatsu", "Sauce tonkatsu (pour panés japonais)", "Tonkatsu sōsu", JP, "S", 1, 8, 5, 0, "€",
  "Bol.",
  "La sauce brune épaisse et sucrée-salée servie avec les panés japonais (tonkatsu, katsu curry, korokke) : "
  "ketchup et sauce Worcestershire en sont la base, avec un peu de soja et de sucre.",
  [f"4 c. à s.|de ketchup (fiche Ketchup)|SUB:ketchup|2", f"2 c. à s.|de sauce Worcestershire|{WORCESTER}|2",
   f"1 c. à s.|de sauce soja|{SOJA}|1", f"1 c. à c.|de sucre|{SUCRE}|1", f"1/2 c. à c.|de moutarde de Dijon|{DIJON}|1?"],
  ["**Mélanger.** Tous les ingrédients fouettés ensemble jusqu'à une sauce brune homogène.",
   "**Servir.** En filet sur une escalope panée tranchée, ou à part dans un petit bol pour tremper."],
  keep="2 semaines au frigo.", age=2, kids="✓ dès 2 ans.", cats=["sauces"], profil=["sucre", "acide"])
K("sauce_unagi", "Sauce unagi (laque sucrée-salée, anguille et riz)", "Unagi no tare", JP, "S", 1, 8, 5, 10, "€",
  "Petite casserole.",
  "La laque brillante et sucrée qui nappe l'anguille grillée japonaise, aussi utilisée sur du saumon ou du "
  "poulet laqués et sur certains makis : sauce soja, mirin et sucre réduits en sirop.",
  [f"6 c. à s.|de sauce soja|{SOJA}|2", "6 c. à s.|de mirin|Mirin|2", f"3 c. à s.|de sucre|{SUCRE}|2"],
  ["**Réduire.** Les trois ingrédients portés à petit frémissement 8 à 10 min, en remuant de temps en temps : "
   "la sauce épaissit et nappe le dos d'une cuillère.",
   "**Refroidir.** Elle épaissit encore en refroidissant ; détendue avec un peu d'eau si elle devient trop "
   "sirupeuse.",
   "**Servir.** Badigeonnée sur du poisson, du poulet ou du tofu en toute fin de cuisson, pour qu'elle caramélise "
   "sans brûler."],
  tips=["Sans alcool : remplace le mirin par le mélange jus de raisin blanc + vinaigre de riz + sucre (3:1:1) "
        "déjà utilisé ailleurs dans l'appli pour cette substitution."],
  var=[("Sans alcool", ["alcohol"], {"Mirin": [("Vinaigre de riz", 1.0)]}, "Mirin → **jus de raisin blanc + vinaigre de riz + sucre (3:1:1)**. **À tester**.")],
  keep="2 semaines au frigo.", age=2, kids="✓ dès 2 ans (traces d'alcool qui s'évaporent à la cuisson).",
  cats=["sauces"], profil=["sucre"])
K("ssamjang", "Ssamjang (pâte à tremper coréenne, pour viande grillée en feuille de salade)", "Ssamjang", KR, "S", 1, 8, 5, 0, "€",
  "Bol.",
  "La pâte épaisse et salée-piquante posée sur chaque feuille de salade avec la viande grillée coréenne (ssam) : "
  "doenjang (pâte de soja fermentée) et gochujang, ail et huile de sésame.",
  [f"2 c. à s.|de doenjang|Doenjang|2", f"1 c. à s.|de gochujang|Gochujang|2", f"2 gousses|d'ail, écrasées|{AIL}|1",
   f"1 c. à c.|d'huile de sésame|Huile de sésame (grillée)|1", f"1 c. à c.|de sucre|{SUCRE}|1",
   f"1|oignon nouveau, haché fin|{CEB}|1?", "1 c. à c.|de graines de sésame|Sésame (blanc/noir)|1?"],
  ["**Mélanger.** Doenjang, gochujang, ail, huile de sésame et sucre mélangés en une pâte épaisse et homogène.",
   "**Finir.** Oignon nouveau et graines de sésame incorporés.",
   "**Servir.** Une petite cuillerée sur une feuille de salade, avec la viande grillée, de l'ail cru en lamelles "
   "et du riz, le tout roulé et mangé en une bouchée."],
  keep="2 semaines au frigo (c'est une pâte fermentée).", age=4, kids="Pour les grands (très salé et relevé).",
  cats=["sauces"], profil=["epice"])
K("zhug", "Zhug (sauce piquante verte yéménite)", "Skhug", YE, "S", 1, 8, 10, 0, "€",
  "Mixeur ou mortier.",
  "La sauce piquante verte du Yémen, adoptée par toute la cuisine israélienne : piments verts, coriandre, ail "
  "et épices mixés avec de l'huile, pour relever un houmous, une pita ou un œuf au plat.",
  [f"4|piments verts frais, épépinés|{PIMENT}|2", f"1|gros bouquet de coriandre fraîche|{CORI}|3",
   f"4 gousses|d'ail|{AIL}|1", f"1 c. à c.|de cumin|{CUMIN}|1", f"1/2 c. à c.|de cardamome moulue|{CARDA}|1?",
   f"6 c. à s.|d'huile d'olive|{HO}|2", f"-|sel|{SEL}|1"],
  ["**Mixer.** Piments, coriandre, ail, cumin, cardamome et sel mixés avec un peu d'huile jusqu'à une texture "
   "grossière (pas un pesto lisse : on doit voir des petits morceaux).",
   "**Finir.** Reste de l'huile incorporé en mixant par à-coups.",
   "**Reposer.** Au moins 30 min au frigo avant de servir : les saveurs se mélangent et le piquant s'arrondit "
   "un peu."],
  tips=["⚠️ Gants conseillés pour épépiner les piments.", "Une pointe suffit sur un œuf au plat ou un houmous : "
        "c'est une sauce très relevée, pas une garniture généreuse."],
  keep="2 semaines au frigo, une fine couche d'huile sur le dessus la protège.", age=5,
  kids="À partir de 5-6 ans, en toute petite quantité et en goûtant avant.", cats=["sauces"], profil=["epice"])
K("baba_ganoush", "Baba ganoush (caviar d'aubergine au tahini)", "Baba ghanoush", LB, "S", 1, 6, 15, 10, "€",
  "Mixeur ou fourchette.",
  "L'aubergine grillée directement sur la flamme jusqu'à ce que la peau noircisse donne son goût fumé "
  "caractéristique à ce caviar libanais, lié au tahini et au citron comme un houmous d'aubergine.",
  [f"2|grosses aubergines|{AUBERGINE}|3", f"3 c. à s.|de tahini|Tahini (purée de sésame)|2",
   f"2|gousses d'ail|{AIL}|1", f"1|citron (jus)|{CIT}|1", f"2 c. à s.|d'huile d'olive|{HO}|1",
   f"1 c. à s.|de persil haché|{PERSIL}|1?", f"-|sel|{SEL}|1"],
  ["**Griller.** Aubergines entières piquées de quelques coups de fourchette, grillées directement sur une "
   "flamme de gaz ou sous le gril du four en les retournant, jusqu'à ce que la peau soit noire et boursouflée et "
   "la chair très molle, 15 à 20 min.",
   "**Égoutter.** Aubergines fendues en deux encore chaudes, chair raclée à la cuillère dans une passoire 10 min "
   "pour perdre son excès d'eau amère ; peau jetée.",
   "**Écraser.** Chair écrasée à la fourchette (pas au mixeur, qui la rend grise et pâteuse) avec tahini, ail "
   "écrasé, citron, sel.",
   "**Finir.** Filet d'huile d'olive et persil sur le dessus avant de servir, avec du pain pita."],
  tips=["Griller directement sur la flamme (pas seulement au four) est le geste qui donne le vrai goût fumé : au "
        "four seul, le résultat reste bon mais plus doux."],
  keep="3 jours au frigo.", age=2, kids="✓ dès 2 ans.", cats=["sauces", "vegetarien"], profil=["acide"])
K("banana_ketchup", "Banana ketchup (ketchup de banane plantain, Philippines)", "Banana ketchup", PH, "S", 1, 10, 15, 20, "€",
  "Casserole, mixeur.",
  "Le ketchup philippin né d'une pénurie de tomates pendant la Seconde Guerre mondiale : de la banane plantain "
  "bien mûre remplace la tomate, avec les mêmes épices sucrées-vinaigrées — presque personne ne devine "
  "l'ingrédient principal à l'aveugle.",
  [f"3|bananes plantain bien mûres|{PLANTAIN}|3", f"8 cl|de vinaigre blanc|Vinaigre blanc|2",
   f"4 c. à s.|de sucre roux|{SUCRE}|2", f"1/2 c. à c.|de cannelle|{CANN}|1?", f"1 pincée|de piment en poudre|{CAYENNE}|1?",
   f"-|sel|{SEL}|1", "1 pointe|de colorant alimentaire rouge, pour la couleur|-|1?"],
  ["**Cuire.** Plantain pelé en morceaux, cuit 10 min à l'eau bouillante ou à la vapeur : très tendre.",
   "**Mixer.** Plantain, vinaigre, sucre, cannelle, piment et sel mixés en une purée bien lisse.",
   "**Réduire.** Purée chauffée à petit frémissement 10 min en remuant, jusqu'à épaissir comme un ketchup ; "
   "colorant ajouté en fin de cuisson si utilisé.",
   "**Refroidir.** Complètement avant de transférer en bocal : elle épaissit encore en refroidissant."],
  tips=["Sans colorant, la sauce reste brun-doré plutôt que rouge vif : le goût est identique, seule la couleur "
        "change."],
  keep="1 mois au frigo, dans un bocal fermé.", age=2, kids="✓ dès 2 ans.", cats=["sauces"], profil=["sucre", "acide"])
