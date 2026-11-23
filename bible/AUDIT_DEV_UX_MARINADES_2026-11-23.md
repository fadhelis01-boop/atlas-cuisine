# Audit « développeur senior + ingénieur UI/UX » : toute l'application et le coin Marinades (23/11/2026)

Relecture code/architecture/UX, à deux échelles : (a) toute l'application, après une semaine (21-22/11) où quatre
audits différents ont ajouté `pains.ts`, `sauces.ts`, étendu `marinades.ts` (champs `cure`/`dry`/`acid`), et deux
scripts de contrôle (`complements_patisserie.py`, `check-regex-collisions.mjs`) ; (b) le coin `/marinades`
spécifiquement, regardé avec un œil dev/UX neuf (pas de chef) car très modifié le 21/11.

**Explicitement hors scope** (déjà audité et corrigé, vérifié en place avant d'écrire ce document, voir §2) :
sharding de `recipes_detail.json`, plafond de poids par chunk, `check-regex-collisions.mjs` intégré au build, les
3 conventions de liste (`CONVENTIONS_LISTES_RUBRIQUE.md`) — `AUDIT_DEV_UX_SENIOR_2026-11-21.md` ; le contenu
culinaire du coin Marinades — `AUDIT_MARINADES_CHEF_2026-11-21.md` ; l'angle métier/amateur — `AUDIT_CHEF_PRO_
SENIOR_2026-11-21.md` et `AUDIT_PATISSERIE_AMATEUR_2026-11-22.md`. Rien n'a été corrigé ici : ce document liste les
angles morts, par ordre de gravité.

## 1. Constats mesurés

| # | Angle | Mesure | Gravité |
|---|---|---|---|
| 1 | **Le budget de démarrage n'a presque plus de marge** | `npm run build` (23/11) : 398 Ko compressés sur un plafond de 400 — 2 Ko de marge. Le chunk partagé `engine` (moteur, lu par `/marinades`, `/sauces`, `/pains` entre autres via `RECIPE_BY_ID`) est à 208,86 Ko compressés sur un plafond par chunk de 220 Ko posé le 21/11 — 11 Ko de marge. Les deux garde-fous existent déjà (c'est le point fort du 21/11), mais les quatre audits de cette semaine les ont déjà presque entièrement consommés : la prochaine fiche ou le prochain champ d'index fera probablement échouer le build. | **forte** |
| 2 | **Trois fonctions quasi identiques, copiées-collées plutôt que partagées** | `marinadeRecipes` (`marinades.ts`), `sauceRecipes` (`sauces.ts`) et `painRecipes` (`pains.ts`) — écrites à 2 jours d'intervalle — ont exactement le même corps (filtrer une liste curatoire par famille optionnelle, associer la fiche de `RECIPE_BY_ID`, retirer les entrées sans fiche). Aucune n'est factorisée dans un helper générique (`src/lib/catalog.ts` par exemple) malgré le même besoin répété 3 fois en une semaine — exactement le rythme qui installe une dette au lieu de la prévenir. | moyenne |
| 3 | **Aucun test ne vérifie que les listes curatoires pointent vers des fiches qui existent encore** | `MARINADES`, `SAUCES` et `PAINS` contiennent 23 + 90 + 45 = 158 ids écrits à la main. Les trois fonctions `*Recipes` filtrent silencieusement (`.filter(Boolean)`) toute entrée dont l'id ne résout plus dans `RECIPE_BY_ID` — un renommage ou une suppression future ferait disparaître une marinade/sauce/pain de sa famille sans qu'aucun test ne le signale. Contraste : le test 25 fait exactement cette vérification pour les références d'ingrédients du Tome 3 (« toutes les références des fiches existent »), mais rien d'équivalent n'a été écrit pour ces 3 listes ajoutées la même semaine. Vérifié : zéro occurrence de `MARINADES`, `SAUCES` ou `PAINS` dans `tests/`. | moyenne |
| 4 | **`check-regex-collisions.mjs` n'a aucun filet de sécurité sur lui-même** | Le script (intégré à `npm run build` le 21/11) affiche « aucune collision » quand il ne trouve rien — mais rien ne distingue ce résultat d'un script cassé (corpus vide par une exception avalée, chemin de fichier mal orthographié dans `FILES`, extraction de regex qui ne matche plus rien) d'un résultat réellement propre. Il n'y a pas de plancher minimal vérifié (ex. « au moins N mots dans le corpus, au moins M regex extraites ») qui ferait échouer le build si le script tournait à vide par accident. | faible |
| 5 | **Les 3 champs `cure`/`dry`/`acid` de `MarinadeEntry` ne sont pas mutuellement exclusifs dans le type** | `cure?: boolean`, `dry?: boolean` et `acid?: boolean` sont 3 booléens indépendants alors qu'ils décrivent 4 gestes mutuellement exclusifs (liquide = aucun des trois, cure, rub sec, ceviche) selon les commentaires du fichier lui-même. Rien n'empêche d'écrire une future entrée avec `cure: true, dry: true` à la fois, un non-sens culinaire que le type ne peut pas repérer (seule la relecture humaine le peut). Vérifié : aucune des 23 entrées actuelles ne combine deux indicateurs — pas un bug aujourd'hui, mais un type qui n'empêche pas l'erreur de demain. | faible |

## 2. Ce qui est déjà solide (vérifié, pas un point à corriger)

- **Les 4 corrections du 21/11 sont bien en place** : `src/lib/data.ts` charge le détail par lots de 12 (`loadShard`/
  `useRecipeDetail`), `scripts/budget.mjs` a bien son plafond par chunk à 220 Ko (ligne `CHUNK_BUDGET`),
  `scripts/check-regex-collisions.mjs` existe et tourne dans `npm run build` juste avant `vite build`,
  `bible/CONVENTIONS_LISTES_RUBRIQUE.md` existe et documente les 3 conventions.
- **Accessibilité des puces de filtre** : le composant `Chip` partagé (`components/ui.tsx`) pose déjà `aria-pressed`
  et un `role="group"`/`aria-label` sur le conteneur — repris à l'identique dans `Marinades.tsx`, `Sauces.tsx` et
  `Pains.tsx`, donc aucune régression d'accessibilité introduite par les 3 réorganisations de cette semaine.
- **Rendu mobile** : vérifié à 375 px sur `/marinades` (9 puces, dont « Tout ») — aucun débordement horizontal,
  `flex-wrap: wrap` fait son travail, aucune puce hors écran.
- **Cohérence visuelle** : `Marinades.tsx`, `Sauces.tsx` et `Pains.tsx` partagent exactement la même structure
  (`Section` titrée avec compteur, puces de filtre, `MoreGrid key={filtre}` pour réinitialiser la pagination) —
  malgré avoir été écrites par 3 audits différents en 2 jours, pas de divergence visuelle entre elles.
- **Smoke test** : `/marinades`, `/sauces` et `/pains` sont bien dans la liste des 29 pages rendues par
  `tests/smoke.test.tsx` — les 3 réorganisations de la semaine sont donc vérifiées « ça ne plante pas » à chaque
  build, juste pas vérifiées plus finement (voir constat n°3).
- **Pas de combinaison contradictoire actuelle** entre `cure`/`dry`/`acid` (constat n°5) : le risque est pour une
  future entrée, pas un bug présent.

## 3. Pourquoi ce sont des angles morts

Le constat n°1 est le plus urgent parce qu'il touche le garde-fou que le 21/11 vient juste d'installer : il existe,
mais il est déjà presque saturé — la marge gagnée par le découpage en lots a été reconsommée en deux jours par les
audits suivants. Les constats n°2 et 3 viennent du même rythme : quatre audits corrigés en deux jours ont chacun
ajouté une petite rubrique avec sa propre liste curatoire et sa propre fonction d'association, sans jamais revenir
factoriser ce qui se répétait ni poser le filet de sécurité qui existe déjà pour un besoin presque identique
(les références d'ingrédients). Aucun de ces points n'est un bug aujourd'hui ; tous les trois rendent le prochain
ajout plus risqué qu'il ne devrait l'être.

## 4. Pistes de correction (non appliquées)

- **#1** : avant d'ajouter la prochaine fiche ou le prochain champ d'index, alléger l'existant (même levier que le
  20/11 : champ omis de l'index quand il vaut une valeur par défaut reconstruite à la lecture) plutôt que
  d'attendre l'échec du build pour s'en soucier.
- **#2** : factoriser `marinadeRecipes`/`sauceRecipes`/`painRecipes` en un helper générique (ex.
  `curatedRecipes<T>(list: {id: string}[], matchFamily: ...)`) dans un nouveau `src/lib/catalog.ts`, réutilisé par
  les 3 fichiers.
- **#3** : ajouter un test (sur le modèle du test 25) qui vérifie `MARINADES.every(m => RECIPE_BY_ID[m.id])`,
  `SAUCES.every(...)` et `PAINS.every(...)` — échec explicite plutôt que disparition silencieuse d'une entrée.
- **#4** : ajouter un plancher vérifié dans `check-regex-collisions.mjs` (ex. échoue si le corpus a moins de 1000
  mots ou si moins de 20 regex ont été extraites des 8 fichiers), pour détecter un script qui tournerait à vide.
- **#5** : soit documenter explicitement (commentaire déjà presque suffisant) que les 3 champs sont mutuellement
  exclusifs et laisser la revue humaine trancher, soit remplacer les 3 booléens par un seul champ
  `geste?: "cure" | "dry" | "acid"` qui rend la combinaison invalide impossible à écrire.

## 5. Corrigé (commit 2026-11-23)

- **Bug signalé par l'utilisateur, en plus des 5 constats** : « problème de chargement de la page sur mobile du
  coin marinade ». Cause trouvée et vérifiée : `deploy.mjs` republie exactement `dist/` à chaque déploiement et
  supprime tout fichier devenu inutile ; un onglet resté ouvert depuis avant un déploiement référence encore
  l'ancien nom de fichier (haché) d'une page chargée à la demande (`React.lazy`) — sur un réseau mobile, cet échec
  traîne parfois au lieu de faire un 404 net, et l'écran reste bloqué sur « Chargement… ». Nouveau `lib/chunkRetry.ts`
  (`lazyRetry`) : recharge la page une seule fois (jamais en boucle, un drapeau `sessionStorage`) si un chunk ne se
  charge pas, ce qui récupère le nom de fichier à jour. Appliqué aux 23 pages `React.lazy` (`App.tsx`) et à tous les
  imports dynamiques de données (`recipes_detail_*.json` par lot, `imports.json`, `recipe_videos.json`,
  `leftovers.json`, `credits.json`, `images_more.json`, `dico.json`, `worldmap.json`) — pas seulement Marinades,
  puisque c'est la même classe de bug partout. **Vérifié avec `vite preview` sur le build réel** : un chunk Marinades
  supprimé du disque déclenche un rechargement automatique puis, le fichier restant absent, une page d'erreur propre
  (jamais de blocage infini) ; le fichier remis en place, le rechargement suivant affiche la page normalement.
- **#1** : pas d'action de poids cette fois — le budget (398/400 Ko démarrage, 208,97/220 Ko sur `engine`) tient
  encore après les correctifs du jour (nouveaux fichiers `catalog.ts`/`chunkRetry.ts`, test 132), mesuré à chaque
  build. La vigilance reste la même : alléger l'index avant toute nouvelle fiche ou tout nouveau champ, pas après un
  échec de build.
- **#2** : nouveau `lib/catalog.ts` (`curatedRecipes`), réutilisé par `marinadeRecipes`, `sauceRecipes` et
  `painRecipes`, qui n'ont plus chacune leur copie du même corps.
- **#3** : nouveau test 132 (`tests/e12-audit-devux-marinades.ts`) : échoue explicitement si un id de `MARINADES`,
  `SAUCES` ou `PAINS` ne résout plus dans `RECIPE_BY_ID`, sur le modèle du test 25.
- **#4** : `scripts/check-regex-collisions.mjs` échoue désormais si le corpus a moins de 1000 mots ou si moins de
  20 regex ont été extraites des 8 fichiers (mesuré au 23/11 : 2992 mots, 157 regex) — un script qui tournerait à
  vide ne peut plus passer pour « aucune collision ».
- **#5** : les 3 booléens `cure`/`dry`/`acid` de `MarinadeEntry` sont remplacés par un seul champ
  `geste?: "cure" | "dry" | "acid"` : écrire deux gestes à la fois pour une même marinade est maintenant une erreur
  de typage, pas seulement une relecture à faire.
