# Audit « développeur senior et ingénieur UI/UX » d'ATLAS (21/11/2026)

Relecture technique et d'expérience de l'application entière (pas une rubrique précise cette fois), après une
journée où plusieurs audits ciblés (cuisinier amateur, coin Marinades, coin Sauces) ont déjà corrigé une dizaine
d'angles morts éditoriaux. Celui-ci regarde le code et l'architecture : performance de chargement, dette de test,
cohérence d'interaction. Mesuré sur le build de production (`npm run build`, commit `3faf1c7`). Rien n'a été
corrigé : ce document liste les angles morts, par ordre de gravité.

## 1. Constats mesurés

| # | Angle | Mesure | Gravité |
|---|---|---|---|
| 1 | **Le détail de toutes les recettes se télécharge en un seul bloc, et bloque l'affichage** | `recipes_detail.json` (étapes, intro, astuces, crédits de 1609 fiches) est chargé par **un seul** `import()` dynamique (`src/lib/data.ts:105`), jamais découpé. Mesuré sur le build : **559 Ko compressés / 2,1 Mo bruts**. `App.tsx` bloque l'affichage (`<Loading/>`) sur **toute** route hors d'une courte liste blanche (`INDEX_ONLY` : accueil, explorer, profil, frigo, courses…) tant que ce fichier entier n'est pas téléchargé — vérifié en vidant le cache et en ouvrant `/semaine` : la requête réseau du fichier entier se déclenche avant que la page ne s'affiche. Pour un premier visiteur (ou après un nettoyage de cache), ouvrir **une seule** fiche recette revient à télécharger les étapes des 1609 autres. | **forte** |
| 2 | **Même défaut, deux fois de plus, à des degrés différents** | `recipe_videos.json` (158,7 Ko compressés) et `credits.json` (114 Ko compressés) suivent le même schéma : un seul fichier pour toutes les fiches, jamais segmenté. `credits.json` est particulièrement large de conséquence : `useCredits()` (`components/photo.tsx`) déclenche son téléchargement dès qu'un composant `<Photo>`/`<Credit>` s'affiche — c'est-à-dire sur la quasi-totalité des écrans (presque chaque page a une photo d'en-tête) — pas seulement quand quelqu'un consulte les crédits. | moyenne |
| 3 | **Aucun garde-fou de taille sur ces fichiers « à la demande »** | `scripts/budget.mjs` ne plafonne que le total du bundle de démarrage (≤ 400 Ko). Rien ne borne la taille d'un chunk chargé à la demande pris isolément : `recipes_detail.json` a pu grossir jusqu'à 2,1 Mo bruts sans jamais faire échouer la moindre vérification automatique, et grossira du même pas à chaque nouvelle fiche ajoutée (plusieurs dizaines l'ont été dans cette seule journée). | forte |
| 4 | **Angle mort méthodologique : les collisions de sous-chaîne ne sont détectées qu'à la main** | Trois bugs trouvés *dans cette seule session* venaient de la même cause : une regex à alternatives (`/mot1\|mot2\|mot3/`) sans limite de mot (`\b`), qui matche par accident à l'intérieur d'un autre mot — l'icône de plat (`components/art.tsx`, 113 fiches touchées), le texte de « finition et dressage » (`lib/dressage.ts`, « classique » → « lassi » → conseil de présentation de cocktail affiché sur une marinade). Les deux ont été trouvés par un script de simulation écrit à la volée pour l'occasion, pas par une vérification qui existe dans `npm run build`. Au moins 10 autres fichiers de `src/lib/` ont une densité de regex comparable (`planner.ts` 21 occurrences, `intents.ts` 14, `famille.ts` et `text.ts` 9, `speech.ts` 7, `season.ts` 5) et n'ont jamais été vérifiés pour la même faiblesse. | moyenne |
| 5 | **Trois conventions d'interaction coexistent entre les rubriques de fiches, sans règle écrite** | Les coins Marinades et Sauces (réorganisés aujourd'hui) utilisent des puces de filtre par catégorie ; `Techniques.tsx` utilise un accordéon `<details>` par famille ; `Fetes.tsx` trie par mois à venir sans aucun filtre. Chaque choix est défendable pour son contenu, mais rien ne documente quand utiliser lequel — le prochain coin ajouté (ou corrigé) repartira d'un choix arbitraire plutôt que d'une convention. | faible |

## 2. Ce qui est déjà solide (vérifié, pas un point à corriger)

- **Robustesse** : un vrai `ErrorBoundary` (`components/ErrorBoundary.tsx`) isole les pannes par page (retour, accueil, rechargement, détail technique dépliable) — une erreur dans une fiche n'efface pas toute l'application.
- **Mise à jour PWA** : le flux `updatefound` / `controllerchange` (`lib/pwa.ts`) existe déjà pour prévenir d'une nouvelle version sans rester bloqué sur un cache périmé.
- **Sécurité** : CSP stricte posée en meta au build (`script-src 'self'`, pas d'`unsafe-eval`, `object-src 'none'`), aucun `dangerouslySetInnerHTML` dans tout `src/`, aucun `: any` explicite — discipline de typage réelle sur 18 300 lignes de TypeScript.
- **Accessibilité et recherche** : le Dictionnaire (657 fiches) a déjà recherche + filtre par section + navigation alphabétique ; un audit axe-core dédié avait déjà eu lieu le 12/11 (voir mémoire du projet).
- **Tests** : 168 contrôles automatiques à chaque `npm run build`, dont plusieurs exactement du type qui aurait pu attraper les bugs du constat n°4 si on avait pensé à les écrire pour ce cas précis — l'enjeu n'est pas le manque de rigueur de test en général (la couverture est déjà large), mais ce cas précis d'angle mort.
- **Zéro `TODO`/`FIXME`** laissé dans `src/` : rien de connu-mais-pas-traité qui traîne silencieusement.

## 3. Pourquoi ce sont des angles morts

Le projet a une charte affichée (application légère, utilisable hors connexion, pensée pour un téléphone) que les
constats n°1 à 3 contredisent directement : l'app elle-même grossit plus vite que son propre garde-fou ne le
permet de détecter, parce que ce garde-fou ne regarde qu'une partie du problème (le démarrage) et pas l'autre (le
contenu chargé ensuite). Le constat n°4 est plus subtil mais plus coûteux à terme : la même erreur humaine (oublier
`\b`) s'est reproduite deux fois dans la même journée malgré la première correction, précisément parce que rien
n'empêche une troisième occurrence dans un fichier qui n'a pas encore été regardé.

## 4. Pistes de correction (non appliquées)

- **#1 et #2** : découper `recipes_detail.json`/`recipe_videos.json`/`credits.json` par macro-région ou par lot
  (chargés à la demande selon la fiche consultée, pas la bible entière), ou a minima par lettre/tranche d'ids ; sur
  `credits.json`, ne déclencher le téléchargement que lorsque le crédit est effectivement affiché (ex. au clic sur
  « Photo : … ») plutôt qu'au montage du composant.
- **#3** : ajouter à `scripts/budget.mjs` un plafond par chunk individuel (pas seulement sur le total « à la
  demande »), qui échoue si un seul fichier dépasse un seuil raisonnable (ex. 150 à 200 Ko compressés).
- **#4** : écrire un script de contrôle réutilisable (sur le modèle de celui fait à la volée pour `art.tsx` cette
  session : simuler chaque classification sur tous les titres, repérer les correspondances à cheval sur une lettre)
  et l'intégrer à `npm run build`, puis l'exécuter une fois sur les fichiers à forte densité de regex listés au
  constat n°4 pour vérifier qu'aucune autre collision ne s'y cache déjà.
- **#5** : documenter (dans ce dépôt ou dans un prochain Tome) les trois conventions existantes et le critère de
  choix entre elles pour la prochaine rubrique.

## 5. Corrigé

- **#1** : `recipes_detail.json` (559 Ko compressés, 1609 fiches) est découpé en 12 lots déterministes (`export_app_data.py`,
  fonction `shardOf` répliquée à l'identique en Python et en TypeScript, `src/lib/data.ts`). Une fiche ouverte
  (`/recette/:id`, mode cuisine) ne charge plus que son propre lot (`useRecipeDetail`) ; seuls les écrans qui balaient
  tout le catalogue (Ma semaine, menus, Bien choisir, Enfants) chargent les 12 (`useDetails`). `App.tsx` ne bloque
  plus l'affichage que sur ces quatre routes et sur une fiche seule — 12 routes supplémentaires (recherche,
  catalogue, techniques, pains, sauces, fêtes, zéro déchet, restes, pique-nique, street-food, marinades) rejoignent
  `INDEX_ONLY` après vérification une par une qu'elles n'utilisent aucun champ de détail. Le chargement en tâche de
  fond posé le 21/10/2026 (tout précharger juste après le premier affichage) est retiré : il aurait annulé le
  bénéfice en re-téléchargeant les 12 lots à chaque visite, même pour une seule fiche. Vérifié en vidant le cache et
  en ouvrant `/recette/blanquette_veau` : une seule requête réseau (`recipes_detail_9.json`) au lieu de 12 ; `/marinades`
  (`INDEX_ONLY`) : zéro requête de détail ; `/semaine` (`FULL_DETAIL_ROUTES`) : les 12 lots, comme attendu.
  `import.meta.glob` (propre à Vite, qui faisait planter les tests et le smoke test sous rolldown) est abandonné au
  profit de 12 imports statiques explicites, qui marchent sous les deux empaqueteurs sans artifice.
- **#2** : non traité séparément — `credits.json` et `recipe_videos.json` restent des fichiers uniques (114 et
  158,7 Ko compressés), sous le nouveau plafond par chunk posé au n°3 ; un découpage par lot comme `recipes_detail.json`
  reste à faire si ces fichiers continuent de grossir.
- **#3** : `scripts/budget.mjs` plafonne désormais chaque chunk chargé à la demande pris isolément à 220 Ko
  compressés (au-dessus du plus gros chunk légitime actuel, le moteur partagé à ~209 Ko), en plus du plafond déjà
  existant sur le total de démarrage. Un futur fichier qui regrossirait comme l'ancien `recipes_detail.json` (2,1 Mo)
  ferait à nouveau échouer le build, cette fois dès son premier dépassement plutôt que jamais.
- **#4** : `scripts/check-regex-collisions.mjs` simule chaque regex à alternatives des fichiers à forte densité
  (`planner.ts`, `intents.ts`, `famille.ts`, `text.ts`, `speech.ts`, `season.ts`, plus `art.tsx` et `dressage.ts` déjà
  corrigés une fois) contre les titres de fiches et les noms d'ingrédients du référentiel — le corpus que ces
  classifications reçoivent réellement. Exécuté une première fois, il a trouvé et fait corriger une trentaine de
  collisions non détectées jusqu'ici, dont plusieurs à fort impact : `pie` (plat américain) matchait à l'intérieur de
  « éthiopien », « papier », « récipient » (mots très courants) ; `glace` à l'intérieur de « déglacer » (geste de
  cuisson salé) ; `lassi` à l'intérieur de « classique » dans `art.tsx` (le même bug déjà corrigé dans `dressage.ts`
  le même jour, mais pas ici) ; `veau` dans « nouveau » ; `marin` dans « romarin » et « tamarin » ; `riz` dans
  « chorizo » ; `moule`/`sole`/`lotte`/`lieu` dans « semoule », « cassolette », « charlotte », « milieu » ; `dal` dans
  « andalou » et « bourdaloue » ; `udon` dans « gyudon »/« katsudon » ; `boulette` dans « ciboulette » ; `mousse` dans
  « pamplemousse » ; `rouille` dans « citrouille ». Chaque correction borne le mot-clé par `\b` (en début seulement
  quand un pluriel ou une terminaison légitime doit encore matcher, en début et fin sinon) ; les correspondances
  volontaires entre langues (bao/xiaolongbao, cake/pancake, burger/hamburger, steak/cheesesteak, strudel/apfelstrudel,
  spatzle/kasespatzle, frit/refrit) sont listées explicitement dans le script plutôt qu'ignorées en silence. Le
  script est intégré à `npm run build` (avant `vite build`) : toute nouvelle collision de ce type fera désormais
  échouer le build au lieu d'attendre une relecture manuelle.
- **#5** : voir `bible/CONVENTIONS_LISTES_RUBRIQUE.md` — les trois conventions (puces de filtre, accordéon, tri
  chronologique) et le critère de choix entre elles pour la prochaine rubrique.
