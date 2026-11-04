# Favoris TikTok du 04/11/2026 : recettes intégrées à ATLAS

> Demande du propriétaire : récupérer les nouvelles recettes des favoris, les ajouter avec les liens des vidéos (favoris et autres vidéos des créateurs si disponibles), en couvrant les angles morts.

## Méthode (la même que le 22/10 et le 29/10)

- **Favoris** : relevés dans le navigateur, compte connecté par le propriétaire, jusqu'au premier favori déjà connu. 31 nouveaux : 27 de cuisine, 4 hors cuisine (télétravail, immobilier, animés, un compte sans contenu identifiable), ajoutés à la liste privée `recettes-classees/prive/hors_cuisine.txt` et retirés des données lues.
- **Auteurs** : 20 auteurs jamais explorés. **TikTok a refusé d'afficher leurs listes de vidéos** (« Une erreur est survenue » sur l'onglet Populaire, puis sur l'onglet Récents), même un profil à la fois avec des pauses de 35 s à 7 min. On n'a rien contourné. Seuls 2 profils ont pu être lus (@sosoya06, @zoyacooks7), dans l'onglet Récents. Le tri par nombre d'enregistrements a été fait sur leurs légendes. Les **15 auteurs restants** sont notés dans `recettes-classees/prive/auteurs_a_explorer.txt` pour la prochaine fois.
- **Pages web des auteurs** : aucune page de recettes trouvée, comme les fois précédentes.
- **Doublons** : 11 fiches existantes reçoivent les vidéos en double (`EN_PLUS_2026_11_04`). Exemples : le burrito croustillant et les wraps de @zoyacooks7 vont au « wrap au poulet croquant » ; l'épaule d'agneau de 9 h au gigot de sept heures ; la sauce chien, la mayonnaise, la tartiflette, le poulet frit coréen.
- **Adaptations** : un ramen au porc devient « version sans porc » au bœuf haché. Les guimauves et la vanille liquide sont signalées (alcool). Les jaunes crus sont signalés pour les femmes enceintes et les petits.

## 24 nouvelles fiches (1 202 recettes, 641 plats)

- **Favoris** (16) : kebab de poulet avec pain maison, riz sauté au bœuf, orzo au poulet cajun, widjila (Mali), burger César au poulet croustillant, ramen miso-curry (version sans porc), rougag dajaj (Algérie), tartine sardines-œufs mollets, poulet croustillant à la friteuse sans huile, cheese naan, mayonnaise aux œufs durs (sans œuf cru), sauce verte pour entrecôte, piment camerounais, rillettes de poulet légères, tiramisu crème brûlée, chocolat chaud à l'italienne.
- **Auteurs lus** (3) : burger « hot honey », frites chargées au poulet, carrot cake.
- **Jumeaux végétariens** (5, recettes ATLAS sans vidéo d'origine) : orzo tomates-feta, burger au halloumi, ramen miso au tofu, kebab de chou-fleur, frites chargées aux haricots. Les 11 plats carnés de la semaine n'ont pas fait baisser la part végétarienne (33 %).

Toutes ces fiches sont **non testées en cuisine**.

## Suite le même jour : les 14 autres auteurs, et l'index allégé

- **Index de démarrage allégé d'abord** : les références d'ingrédients de l'index sont des numéros au lieu de leurs noms (400 → 385 Ko compressés, sans rien changer à l'affichage ; contrôle ajouté au test 92). Après cet import : 390 Ko, il reste donc de la place pour environ 60 fiches.
- **Auteurs** : quelques heures plus tard, TikTok a de nouveau affiché les profils. Les 14 auteurs restants ont été lus (onglet « Populaire », 15 vidéos chacun, un profil à la fois avec des pauses), sans aucun refus. Liste privée des auteurs à explorer : vide.
- **30 nouvelles fiches créditées** (1 232 recettes, 661 plats) : pâtes au poulet sauce fromage ail et fines herbes, tenders sauce poivrée, foutou sauce graine, macaronis au bœuf et cheddar, salade de sardines, ramen tom yum (version sans porc), pain chargé camerounais, pepper soup d'agneau, poulet farci épinards-mozzarella, couscous tfaya, pâtes Alfredo au poulet, bœuf Wellington (sans jambon) ; 8 plats végétariens crédités (karantika, omelette aux frites, vermicelles de riz sautés, lo mein, udon ail-champignons, ramen coréen aux champignons, pâtes à la butternut, beignets-haricots-bouillie) ; felfla, bricks poulet-curry, beignets de crevettes, corn dogs coréens (saucisses de volaille) ; gâteau qui pleure, cheesecakes spéculoos, sfenj, beignets de banane ; sauces façon « Giant » et « Big Tasty ».
- **Doublons** : 60 vidéos rejoignent 47 fiches existantes (plov, tajine aux olives, yassa, mafé, thiéboudienne, brioche, fataya, attiéké poisson, couscous, tangia, méchoui, steak frites…). Les vidéos au porc (porc laqué, porc braisé) vont aux fiches « version » sans porc, marquées 🐖 dans la bibliothèque.
- **Vidéos hors recette** de ces comptes de cuisine (piscine, buffet, dégustation au restaurant, conseils santé, « meilleure cuisine de… ») : ajoutées une par une à la liste privée, jamais publiées (le filtre accepte maintenant une vidéo isolée, pas seulement un compte).
- **Bibliothèque du 04/11** : 224 vidéos classées, 32 « À vérifier » (titres trop vagues, recettes sans fiche ATLAS correspondante).
- **Contrôles** : tests 110 (30 fiches créditées, 8 plats végétariens, vidéos d'origine rangées) et 111 (vidéos hors recette absentes) ; la part de plats végétariens reste à 33 % ; la liste des 30 plats à tester en priorité a été régénérée.

## Angles morts

1. **Auteurs non lus** : plus aucun (les 14 restants ont été lus plus tard le même jour).
2. **Filtre hors cuisine** : 4 comptes de plus ; la bibliothèque du 04/11 n'en contient aucun.
3. **Bibliothèque** : 54 vidéos classées, 6 « À vérifier » seulement. Les vidéos d'origine des fiches sont toutes rangées avec leur fiche.
4. **Contrôles** : tests 108 (19 fiches créditées, 5 jumeaux végétariens sans viande ni poisson) et 109 (vidéos d'origine présentes et bien rangées). Les 30 plats « à tester en priorité » ont été régénérés.
5. **Budget de démarrage** : 390 Ko sur 400 après l'allègement et ce second import ; prochaine piste si besoin : sortir de l'index les textes de variantes et d'accords (lus seulement sur la fiche).
