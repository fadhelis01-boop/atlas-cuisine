# Audit UI/UX senior d'ATLAS (12/11/2026)

Cet audit fait suite à l'audit développement et UX du 21/10 (`AUDIT_DEV_UX_2026-10-21.md`). Les points corrigés ce jour-là
n'ont pas été refaits. Mesures sur 22 écrans, au format téléphone (375 × 812), en thème clair et sombre, puis à 1 280 px.
L'accessibilité est vérifiée avec axe-core 4.10 (WCAG 2.0 à 2.2 AA et bonnes pratiques). Contrôle automatique : test 128.

## 1. Ce qui est sain

- Aucun défilement horizontal et un seul `h1` par écran.
- Contrastes conformes en clair et en sombre.
- Focus visible, lien d'évitement, changement d'écran annoncé aux lecteurs d'écran, animations coupées si le système le demande.
- Mode cuisine clair : grandes cibles, lecture à voix haute, avertissement quand l'écran risque de s'éteindre.
- Sur ordinateur : navigation latérale et colonne de lecture bornée.
- Cibles tactiles : toutes atteignent le minimum WCAG 2.2 AA (24 px). Les liens de crédit photo font 28 px.

## 2. Angles morts mesurés (avant)

| Angle | Mesure | Gravité |
|---|---|---|
| Recouvrement | Le bouton Profil, fixe en haut à droite, recouvre le 4e onglet du sommaire collant de la fiche (« Si ça rate ») | forte |
| Recherche sans issue | Une recherche sans résultat ne proposait qu'un lien vers « Avec ce que j'ai » | moyenne |
| Rubriques introuvables | Chercher « street food », « pique-nique » ou « zéro déchet » affichait des vidéos, jamais la rubrique | moyenne |
| Pages longues sans sommaire | Zéro déchet 11,2 écrans, Pique-nique 10,2, Enfants 9,9, Street food 8,8 : aucun moyen d'aller à une section | moyenne |
| Poids d'une page | Fêtes : 5 209 éléments, dont 3 756 dans le calendrier, alors que toutes ses fêtes sont repliées | moyenne (téléphones modestes) |
| Titre d'onglet | L'accueil s'intitulait « Une pâtisserie, un chocolat chaud, des crêpes ? · ATLAS » : historique et lecteurs d'écran perdus | faible |
| Clavier du téléphone | Aucun champ de recherche n'affichait la touche « Rechercher » ; le texte d'aide de l'accueil était coupé | faible |
| Mains mouillées | « Le geste » (9 par fiche) et le badge « Pas encore testée » faisaient 32 px de haut ; les liens des tableaux du pique-nique, 20 px | faible |
| Place à l'écran | Barre « Cuisiner » et barre d'onglets : 138 px en bas de la fiche, soit 17 % de l'écran | faible |
| Ordre des titres | Catalogue et Sauces : cartes en `h3` directement sous le `h1` (axe, heading-order) | faible |

## 3. Corrigé

- **Sommaire de la fiche** : il garde 56 px de marge à droite sur téléphone, plus rien n'est recouvert.
- **Recherche sans impasse** :
  - sans résultat, 8 recherches suggérées, toutes vérifiées avec des résultats, plus les liens « Avec ce que j'ai » et « toutes les recettes » ;
  - le nom d'une rubrique (street food, pique-nique, zéro déchet, fêtes, enfants, sauces, pains, techniques, restes) affiche un raccourci vers elle en tête des résultats.
- **Sommaire « Sur cette page »** automatique dès 4 sections titrées (`PageToc` dans `Page`) : Zéro déchet, Pique-nique, Enfants, Street food, Fêtes…
- **Fêtes** : le contenu d'une fête n'est construit qu'à sa première ouverture (`LazyDetails`). La page passe de 5 209 à 1 628 éléments.
- **Accueil** : l'onglet s'appelle « Accueil · ATLAS » (`data-title`), et le texte d'aide de la recherche est court et lisible en entier.
- **Clavier** : la touche « Rechercher » s'affiche sur les 5 champs de recherche.
- **Cibles de 44 px** : « Le geste », le badge « Pas encore testée » et les liens des tableaux.
- **Barre « Cuisiner »** : 73 px au lieu de 81.
- **Ordre des titres** : un titre `h2` réservé aux lecteurs d'écran avant les grilles du catalogue et des sauces. axe ne trouve plus aucun défaut sur les écrans mesurés.

## 4. Reste à faire (proposé)

- ~~Masquer la barre d'onglets en défilant vers le bas sur la fiche~~ : fait le 12/11 (`hideNavOnScroll`). Sur téléphone, elle sort de l'écran quand on descend, et la barre « Cuisiner » prend sa place. Elle revient dès qu'on remonte, près du haut de la page, ou quand le focus clavier y arrive. Le comportement reste à essayer sur un vrai téléphone.
- Pages encore longues : Zéro déchet (11,5 écrans) et Pique-nique (10,2). Le sommaire aide ; il faudrait aussi replier les listes secondaires.
- Il reste peu de marge sur le budget de démarrage (389 Ko pour 400) : toute nouvelle fonction de l'accueil doit être chargée à la demande.
- Rien ne remplace un test avec de vraies personnes : 5 foyers, 3 tâches (trouver un plat ce soir, préparer la semaine, cuisiner une fiche).
