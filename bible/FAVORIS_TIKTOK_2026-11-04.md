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

## Angles morts

1. **Auteurs non lus** : 15 profils restent à explorer, liste privée tenue à jour.
2. **Filtre hors cuisine** : 4 comptes de plus ; la bibliothèque du 04/11 n'en contient aucun.
3. **Bibliothèque** : 54 vidéos classées, 6 « À vérifier » seulement. Les vidéos d'origine des fiches sont toutes rangées avec leur fiche.
4. **Contrôles** : tests 108 (19 fiches créditées, 5 jumeaux végétariens sans viande ni poisson) et 109 (vidéos d'origine présentes et bien rangées). Les 30 plats « à tester en priorité » ont été régénérés.
5. **Budget de démarrage** : l'index atteint 400 Ko compressés, soit le plafond. Avant le prochain ajout de recettes, il faudra alléger l'index (par exemple sortir les textes courts du démarrage), sinon la construction refusera.
