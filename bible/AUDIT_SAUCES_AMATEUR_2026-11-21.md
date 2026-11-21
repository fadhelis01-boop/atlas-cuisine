# Audit « amateur indécis » du coin Sauces maison (21/11/2026)

Le regard de quelqu'un qui veut faire une sauce mais ne sait pas laquelle : peut-être recréer un classique de
fast-food vu sur TikTok, peut-être une sauce française qu'il a mangée au restaurant, peut-être découvrir une sauce
du monde. Parcours de `/sauces` (`app/src/pages/Sauces.tsx`) et des 113 fiches `cats: ["sauces"]`. Les 7 constats ont
tous été corrigés le jour même (commit `cc1b7e8`) : voir « 5. Corrigé » à la fin de ce document.

## 1. Constats mesurés

| # | Angle | Mesure | Gravité |
|---|---|---|---|
| 1 | **Plus d'un tiers de la liste n'est pas des sauces** | Sur les 113 fiches affichées dans la grille de `/sauces`, 38 (34 %) sont en réalité des marinades (18, dont `bbq_rub_americain` qui n'a même pas de liquide), des mélanges d'épices secs (`ras_el_hanout_maison`, `garam_masala_maison`, `zaatar_maison`, `berbere_maison`, `dukkah`, `yaji`, `curry_poudre_maison`), des bouillons et fonds (`bouillon_volaille`, `fond_brun_veau`, `fond_blanc_volaille`, `fumet_poisson`, `court_bouillon`), et une poignée d'intrus isolés : `frites_maison` (des frites, pas une sauce), `kimchi_maison`, `citrons_confits_maison`, `ghee_maison`, `pickles_oignons_rouges`, `beurre_cacahuete_maison`, `confiture_peaux_bananes`. Un amateur qui veut « une sauce pour ses frites » doit trier lui-même le fond de veau et le ghee du reste. | **forte** |
| 2 | **Aucun classement par origine ni par usage, contrairement au coin Marinades** | La grille est une simple liste dans l'ordre d'écriture de la bible (ni alphabétique, ni par pays, ni par occasion) : « Mayonnaise, Sauce algérienne, Ketchup, Sauce samouraï, Sauce blanche… ». Pas de puces de filtre comme celles du coin Marinades (protéine, pays). Rien ne répond à « je veux une sauce de fast-food », « je veux un classique français » ou « je veux une sauce du monde » — exactement la question posée par l'amateur de cet audit. | **forte** |
| 3 | **Les sauces de fast-food américaines, très demandées, sont quasi absentes** | Seules des versions franco-belges existent : `sauce_facon_giant` (Quick), `sauce_facon_big_tasty` (McDonald's France), `sauce_andalouse`/`sauce_americaine_belge`/`sauce_brazil` (friteries belges). Aucune fiche pour les classiques américains copiés en masse sur TikTok : sauce Big Mac, sauce Chick-fil-A, sauce Chipotle, spread In-N-Out, sauces Taco Bell, Wendy's, Raising Cane's, Zaxby's, KFC, Popeyes, la sauce Yum Yum des teppanyaki, la sauce blanche Alabama pour barbecue. | forte |
| 4 | **2 des 5 sauces mères françaises manquent comme sauce autonome** | Le Velouté (roux + fond blanc) n'existe que comme fond ou comme potage, jamais comme sauce liée finie. L'Espagnole/demi-glace (fond brun lié) n'existe pas du tout : `fond_brun_veau` est un fond, pas une sauce. Pas de Périgueux (truffe) ni de Chasseur en fiche autonome (la sauce chasseur n'existe que dans `pollo_cacciatora`, un plat). | moyenne |
| 5 | **L'aïoli et la rémoulade françaises n'existent pas comme fiches à part** | L'aïoli (ail, huile, œuf) n'apparaît que noyé dans « Le grand aïoli », « Bourride à l'aïoli » et « Bulots, aïoli » : jamais une fiche qu'on peut faire et garder au frigo pour l'utiliser ailleurs. Idem pour la rémoulade française (mayonnaise, moutarde, cornichons, câpres, herbes — différente de la `sauce_tartare` déjà présente, plus proche de l'anglo-saxonne) : seule « Céleri rémoulade » l'utilise, jamais en fiche. | moyenne |
| 6 | **Angles morts ciblés en Asie et au Moyen-Orient** | Pas de tonkatsu (panés japonais), pas d'unagi (anguille/riz), pas de ssamjang coréen (pâte à accompagner le barbecue), pas de zhug/skhug yéménite, pas de baba ganoush, pas de banana ketchup philippin — alors que l'Asie de l'Est et le Moyen-Orient sont par ailleurs bien couverts ailleurs dans la bible (curry, teriyaki, toum, muhammara, ajvar existent déjà). | faible |
| 7 | **Le « Sauce Builder » sert à construire, pas à découvrir** | Les 3 étapes (base, profil, aromates) aident à inventer une sauce sur mesure, mais ne répondent à aucune des vraies questions d'un amateur indécis (« quelle sauce pour des frites ? », « une sauce qui pique ? », « sans cuisson ? », « pour accompagner du poisson ? ») : aucune recherche par intention équivalente à celle déjà utilisée ailleurs dans l'appli (`lib/intents.ts`) n'existe pour les sauces. | moyenne |

## 2. Repéré mais écarté (pas un bug)

- `frites_maison` dans la liste des sauces est au moins annoncé dans le sous-titre de la page (« … et les frites qui vont avec ») : un choix éditorial assumé, pas un oubli — mais rien ne le distingue visuellement du reste de la grille, ce qui reste trompeur au premier coup d'œil (voir constat n°1).
- `sauce_teriyaki_sauce` et les autres marinades-sauces hybrides (déjà couvertes par l'audit du coin Marinades du même jour) sont à la fois des marinades ET utilisables en nappage ; leur présence dans `cats: ["sauces"]` n'est donc pas totalement injustifiée, seulement mal signalée.
- La charte des sauces ATLAS (8 ingrédients maximum, pas de conservateur, version sans œuf) est appliquée de façon cohérente sur les fiches vérifiées : rien à redire sur la qualité des fiches existantes elles-mêmes.

## 3. Pourquoi c'est un angle mort pour un amateur indécis

La question posée (« je veux faire une sauce mais je ne sais pas laquelle ») suppose justement de pouvoir parcourir,
comparer, filtrer — or la page actuelle n'offre qu'une liste plate polluée à plus d'un tiers par des éléments qui ne
sont pas des sauces. Les deux familles explicitement citées par l'amateur (fast-food américain, classiques français)
sont précisément les deux familles les plus trouées : la première est quasiment absente, la seconde a deux sauces
mères et deux grands classiques manquants. Le Sauce Builder, mis en avant dans la page, répond à une question que
l'amateur indécis ne pose pas (« comment inventer ma propre sauce ») plutôt qu'à la sienne (« laquelle existe déjà et
me convient »).

## 4. Pistes de correction (non appliquées)

- **#1** : séparer `cats: ["sauces"]` en sous-catégories distinctes à l'export ou dans la logique d'affichage (ex. un
  nouveau tag `cats: ["sauces_mariandes"]` déjà en partie fait pour les marinades propres, à étendre aux épices,
  bouillons et intrus isolés) pour que `/sauces` n'affiche plus que de vraies sauces de table ou de cuisson.
- **#2 et #3** : ajouter des puces de filtre par origine (France classique / fast-food / monde) sur le modèle de
  `marinades.ts`, et écrire les sauces de fast-food américaines manquantes (Big Mac, Chick-fil-A, Chipotle, In-N-Out,
  Taco Bell, Alabama white, Yum Yum…), probablement les contenus les plus demandés sur TikTok pour cette rubrique.
- **#4 et #5** : ajouter les sauces mères et classiques manquants comme fiches autonomes (Velouté, Espagnole/demi-glace,
  Périgueux, Chasseur, Aïoli, Rémoulade française), chacune réutilisable indépendamment du plat où elle apparaît
  aujourd'hui.
- **#6** : combler les trous ciblés identifiés (tonkatsu, unagi, ssamjang, zhug/skhug, baba ganoush, banana ketchup).
- **#7** : une recherche par intention dédiée aux sauces (« pour des frites », « piquant », « sans cuisson », « pour du
  poisson »), à côté du Sauce Builder plutôt qu'à sa place.

## 5. Corrigé (21/11/2026, commit `cc1b7e8`)

- **#1** : nouveau `app/src/lib/sauces.ts`, liste organisée à la main de 90 vraies sauces (sur les 130 fiches
  `cats: ["sauces"]`, marinades et nouvelles fiches comprises) — exclut les 38 marinades, mélanges d'épices secs,
  bouillons/fonds et intrus isolés repérés au constat n°1, sans toucher aux `cats` des fiches elles-mêmes (moins
  risqué qu'une refonte de l'export, et cohérent avec la façon dont `marinades.ts` gère déjà sa propre liste à part).
- **#2** : puces de filtre par famille sur `/sauces`, sur le modèle du coin Marinades : Fast-food & snack (19),
  Classiques de France (37), Sauces du monde (34). Vérifié en local et en ligne : le filtre fonctionne, les
  compteurs sont justes.
- **#3** : 5 sauces de fast-food écrites — Big Mac, façon Chick-fil-A, blanche Alabama, yum yum (teppanyaki), et la
  sauce douce et acidulée de McDonald's, **sourcée et créditée sur TikTok** (@simplylemmons, ingrédients exacts
  donnés dans sa légende : confiture d'abricot et de pêche, miel, vinaigre de vin blanc, soja, moutarde). Les autres
  (Big Mac, Chick-fil-A, Alabama, yum yum) sont des recettes copiées des dizaines de fois, très proches d'une vidéo
  à l'autre : écrites à partir de cette connaissance culinaire publique plutôt que d'une seule vidéo précise, comme
  pour le gravlax ou la marinade au vin rouge plus tôt dans cet audit.
- **#4 et #5** : `sauce_veloute`, `sauce_espagnole`, `sauce_perigueux`, `sauce_chasseur`, `aioli` et
  `remoulade_francaise` ajoutées comme fiches autonomes, réutilisables indépendamment du plat où elles apparaissaient
  jusqu'ici.
- **#6** : `sauce_tonkatsu`, `sauce_unagi`, `ssamjang`, `zhug`, `baba_ganoush`, `banana_ketchup` ajoutées.
- **#7** : les trois familles de filtre répondent directement à la question de découverte (« je veux une sauce de
  fast-food / un classique français / une sauce du monde ») ; le Sauce Builder reste à côté pour qui veut inventer la
  sienne, avec un texte d'intro qui le présente comme un second choix plutôt que la porte d'entrée de la page.

**Ingrédients manquants ajoutés au Tome 3** pour rendre ces fiches réalisables : « Moutarde jaune américaine
(douce) » et « Raifort (crème ou râpé) » (sauces américaines), « Truffe (fraîche ou pelures) » (Périgueux) —
référencés dans `BIBLE_TOME3_REFERENTIEL_INGREDIENTS.md` et dans les dictionnaires illustrés (`dico_2.py`,
`dico_4.py`).
