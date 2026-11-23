# Audit « développeur expert + ingénieur UI/UX senior » : découvrabilité du coin Marinades (24/11/2026)

Signalé par l'utilisateur, en tant que cuisinier amateur : « le coin marinade est difficile d'accès à retrouver
dans l'application ». Vérifié, mesuré, et corrigé le jour même.

## 1. Constat mesuré

Avant ce correctif, `/marinades` n'avait que **deux chemins** depuis l'accueil :
- Accueil → onglet **Explorer** → faire défiler toute la grille des régions du monde (`L'atlas des cuisines`) →
  section « Rubriques » → **7ᵉ tuile sur 14**, entre Sauces et Enfants, sans mise en avant particulière.
- Taper le mot « marinade » dans la recherche (fonctionne déjà bien : `lib/search.tsx` reconnaît `/marinad|\bmariner\b/`
  et affiche un lien direct vers la rubrique).

Aucun chemin direct depuis l'écran d'accueil lui-même : ni dans les 6 tuiles « Rubriques » (`Home.tsx`, `ENTRIES` :
Cuisines du monde, Avec ce que j'ai, Ma semaine, Techniques, Fêtes & menus, Enfants), ni dans les 12 puces
« Envies du moment » (`CRAVINGS`). Pour un amateur qui a de la viande ou du poisson à faire mariner — un besoin
fréquent et ponctuel, pas une envie de plat précis — la rubrique n'existait nulle part à l'endroit où il regarde en
premier.

## 2. Pourquoi c'est un angle mort

`Home.tsx` distingue déjà deux rangées avec des rôles différents : les **tuiles de rubrique** (des coins organisés
par technique ou par usage : Techniques, Fêtes, Enfants…) et les **puces d'envie** (des filtres de plat à manger
maintenant : brunch, végétarien, chocolat…). Marinades est un coin-technique comme Techniques, pas une envie de
plat — la ranger dans les envies aurait été le même type d'incohérence que mélanger les deux rangées. Le vrai
manque était simplement l'absence de tuile dans la rangée qui lui correspond déjà.

## 3. Solution appliquée

- **`Home.tsx`** : nouvelle tuile « Marinades » dans `ENTRIES` (7ᵉ tuile, entre Techniques et Fêtes & menus),
  teinte `chili` (distincte des 6 autres), photo de couverture déjà existante (`recette/mojo_cubain_porc`, réutilisée
  depuis `Explore.tsx`). Aucune donnée supplémentaire chargée au démarrage : contrairement à une première version de
  ce correctif qui important `lib/marinades.ts` pour une puce d'envie (et faisait dépasser le budget de démarrage de
  398 à 401 Ko), la tuile est un lien statique, comme les 6 autres.
- Vérifié en mobile (375 px) : la grille à 3 colonnes gère déjà l'orphelin de fin de ligne
  (`.entries > :last-child:nth-child(3n+1) { grid-column: 1 / -1 }`) — passer de 6 à 7 tuiles n'a rien cassé, la
  dernière tuile (Enfants) prend toute la largeur comme prévu par la règle existante.
- **Non touché, volontairement** : la position de Marinades dans `Explore.tsx` (déjà logique, groupée avec
  Techniques/Pains/Sauces) ; les rubriques Pains et Sauces, qui ont le même statut qu'avant (accessibles seulement
  depuis Explorer) — l'utilisateur a signalé Marinades spécifiquement, étendre le correctif à des rubriques non
  signalées aurait été une extension non demandée de la page d'accueil.

## 4. Vérifié

`npm run build` : 132 contrôles OK, smoke 58/58, `check-regex-collisions` propre, budget 398/400 Ko (inchangé).
Testé en navigateur (desktop et mobile 375 px) : la tuile s'affiche, se clique, mène à `/marinades` sans erreur.
