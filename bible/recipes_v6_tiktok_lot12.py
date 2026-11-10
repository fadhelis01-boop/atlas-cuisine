# -*- coding: utf-8 -*-
"""Vague 9 (suite) · Favoris TikTok ajoutés entre le 04/11 et le 10/11/2026 (compte connecté par le propriétaire). Fiches
réécrites (repères et durées ATLAS) et créditées ; rien n'est recopié des légendes. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *
from recipes_v6_tiktok_plats import C

TT = "https://www.tiktok.com/"
def V(author, vid):
    return (f"@{author}", f"{TT}@{author}/video/{vid}")

K("sauce_cesar", "Sauce César maison (anchois, parmesan, ail, citron)", "Caesar dressing", "Amérique du Nord › États-Unis", "S", 2, 8, 10, 0, "€", "Mixeur plongeur, bocal étroit.",
  "La vraie sauce des salades César : un jaune d'œuf, de la moutarde, de l'ail, des anchois, du citron et de la sauce Worcestershire, montés à l'huile comme une mayonnaise, puis beaucoup de parmesan et un peu d'eau pour la rendre nappante.",
  [f"1|jaune d'œuf très frais|Jaune d'œuf|2", f"1 c. à s.|de moutarde|{DIJON}|1", f"2|gousses d'ail|{AIL}|1", "5|filets d'anchois|Anchois (filets, conserve)|2", f"1/2|citron (jus)|{CIT}|1",
   "1 c. à c.|de sauce Worcestershire (ou de soja)|Sauce Worcestershire|1", f"80 g|de parmesan râpé|{PARM}|2", f"25 cl|d'huile neutre|{HN}|3", "10 cl|d'eau froide|-|0"],
  ["**Base.** Dans le bocal : jaune, moutarde, ail, anchois, jus de citron, Worcestershire.",
   "**Monter.** Huile versée par-dessus, mixeur au fond, 20 s sans bouger puis remonté lentement : sauce épaisse et brillante.",
   "**Finir.** Parmesan, puis l'eau froide cuillère par cuillère en mixant : nappante, elle coule de la cuillère en ruban.",
   "**Goûter.** Poivre ; un trait de citron s'il manque de peps (les anchois et le parmesan salent déjà)."],
  tips=["⚠️ Œuf cru : pas pour les moins de 6 ans, les femmes enceintes ni les personnes âgées ; une mayonnaise du commerce (œufs pasteurisés) peut servir de base."],
  keep="24 h au frigo, au froid.", age=None, kids="Œuf cru et anchois : pour les adultes et les grands enfants.", cats=["sauces"], profil=["gras", "acide"],
  credit=C(V("amscooking", "7693277240691363104")))
K("ballotine_poulet_camembert", "Ballottines de poulet au camembert, sauce crème à la moutarde", "Ballottine poulet-camembert", "France › Normandie", "P", 2, 4, 25, 30, "€€", "Film alimentaire résistant à la chaleur ou papier aluminium, grande casserole, poêle.",
  "Des blancs de poulet aplatis, roulés serrés autour d'un morceau de camembert, pochés dans leur film puis dorés à la poêle : coupés en tranches, ils coulent. Une sauce crème à la moutarde avec le jus de cuisson.",
  [f"4|blancs de poulet|{BLANC_P}|3", "1/2|camembert (125 g)|Camembert / brie|2", f"20 cl|de crème liquide|{CL}|2", f"1 c. à s.|de moutarde à l'ancienne|Moutarde à l'ancienne|1", f"1|échalote|{ECH}|1",
   f"20 g|de beurre|{BEURRE}|1", "2|branches de thym|Thym / romarin|1", f"1/2|citron|{CIT}|1", "1|salade verte|Salade (laitue, batavia)|1"],
  ["**Aplatir.** Chaque blanc ouvert en portefeuille, entre deux films, tapé au rouleau à 1 cm d'épaisseur ; sel, poivre, thym effeuillé.",
   "**Rouler.** Un bâtonnet de camembert au bord, roulé serré, extrémités rentrées ; enveloppé dans le film, serré en papillote, bouts noués.",
   "**Pocher.** Eau frémissante (pas bouillante), 18 min : ferme au toucher, 74 °C à cœur ; 5 min de repos, film retiré.",
   "**Dorer.** Beurre mousseux, ballottines 4 min en les roulant : dorées partout ; réservées.",
   "**Sauce.** Échalote ciselée dans la poêle, 2 min ; crème, moutarde, 3 min : nappante ; trait de citron ; ballottines en tranches épaisses, nappées, salade à côté."],
  tips=["Le film doit résister à la chaleur (indiqué « cuisson » sur la boîte) ; à défaut, papier aluminium bien serré.", "Femme enceinte : un camembert au lait pasteurisé."],
  keep="2 jours au frigo ; se réchauffe dans la sauce.", age=3, cats=["enfants"], profil=["gras"],
  credit=C(V("lardoise_porto_vecchio", "7706553977965481248")))
K("poisson_braise_camerounais", "Poisson braisé à la camerounaise (marinade gingembre, ail, piment, herbes), plantain frit", "Poisson braisé", "Afrique subsaharienne › Cameroun", "P", 2, 4, 25, 30, "€€", "Barbecue, plancha ou four en position grill, mixeur.",
  "Le poisson des braiseuses de Douala : entier, entaillé, enduit d'une marinade verte mixée (gingembre, ail, oignon, céleri, persil, basilic, piment), grillé jusqu'à une peau croustillante. Avec du plantain frit ou du bâton de manioc et un piment à part.",
  ["4|bars, dorades ou maquereaux vidés (ou 2 gros)|Bar / loup|3", f"5 cm|de gingembre|{GING}|1", f"4|gousses d'ail|{AIL}|1", f"1|oignon|{OIG}|1", "1|branche de céleri|Céleri-branche|1",
   "1|bouquet de persil et de basilic|Persil plat / frisé|1", "1|piment antillais (facultatif)|Piment antillais / scotch bonnet|1?", "1|cube de bouillon|Bouillon cube volaille|1", f"4 c. à s.|d'huile|{HN}|1",
   f"2|citrons verts|{CITV}|2", "2|bananes plantain mûres|Plantain (banane à cuire)|2"],
  ["**Marinade.** Gingembre, ail, oignon, céleri, herbes, cube émietté, 2 c. à s. d'huile, sel ; mixés en pâte verte.",
   "**Mariner.** Poissons entaillés tous les 3 cm des deux côtés, frottés de citron vert ; marinade dans les entailles et le ventre : 30 min au frais.",
   "**Griller.** Grill bien chaud, poissons huilés, 8 à 10 min par face selon la taille : peau dorée et croustillante, chair qui se détache de l'arête au couteau.",
   "**Plantain.** En biseaux, 3 min par face dans l'huile chaude : doré ; salé.",
   "**Servir.** Poisson, plantain, quartiers de citron vert ; le piment mixé à part pour les grands."],
  tips=["Retourner le poisson une seule fois, avec une large spatule : la peau colle et se déchire si on le bouge trop tôt."],
  keep="Le jour même (poisson cuit : 24 h au plus).", age=3, kids="✓ dès 3 ans, sans le piment, arêtes retirées par un adulte.", cats=["enfants"], profil=["epice", "poisson", "acide"],
  credit=C(V("tiaghohilson", "7705772636214807841"), V("tiaghohilson", "7680593591164521760")))
