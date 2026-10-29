# Favoris TikTok du 29/10/2026 : recettes intégrées à ATLAS

> Demande du propriétaire : ajouter les recettes enregistrées depuis la dernière connexion (22/10) et le contenu des auteurs de ces nouvelles recettes, avec la même méthode, en comblant les angles morts.

## Méthode (la même que le 22/10)

- **Favoris** : relevés dans le navigateur, compte connecté par le propriétaire. **16 nouveaux** depuis le 22/10 : 12 de cuisine, 4 hors cuisine (jamais publiés, retirés des données lues).
- **Auteurs** : 10 auteurs derrière les 12 favoris de cuisine. 2 avaient déjà été lus le 22/10 (@on_est_gourmands, @nicolaslepatissier). Les **8 autres ont été lus pour la première fois**, dont @lardoise_porto_vecchio, qui comptait 16 favoris sans avoir jamais été exploré (angle mort du 22/10).
- **Pages web des auteurs** : aucun n'a de site de recettes. Le site de l'école Chefsquare a été lu poliment (robots.txt respecté) et ne publie aucune recette. Les autres auteurs n'ont qu'un livre ou un restaurant. Comme le 22/10, la source « auteurs » est donc l'onglet « Populaire » de leur profil TikTok public, soit 20 à 40 vidéos par auteur.
- **Légendes** : 183 pages publiques lues une à une, à 3–4 s d'intervalle. La collecte a été interrompue une fois puis reprise là où elle s'était arrêtée.
- **« Mieux notées »** : nombre d'enregistrements, comme le 22/10.
- **« Mieux adaptées »** :
  - porc : remplacé par de la dinde ou de la volaille, avec la version d'origine en astuce ; une potée au porc structurant devient « version » (D21) ;
  - alcool : gardé, avec sa variante sans alcool « À tester » ;
  - guimauves sans gélatine de porc signalées ;
  - écartés : liqueurs, limoncello et spritz (rien à adapter sans alcool), filet américain (bœuf cru), vidéos sans plat identifiable.
- **Doublons** : chaque candidate est comparée au catalogue (y compris les orthographes voisines : la carbonade de @chesterfoodies est rattachée à la « Carbonnade flamande » existante). **41 fiches existantes** reçoivent les vidéos en double (`bible/videos_favoris.py`, `EN_PLUS_2026_10_29`).
- **Droit d'auteur** : chaque fiche est réécrite (repères et durées ATLAS) et crédite la vidéo d'origine. Quand la légende ne donne que le nom du plat (sauce gombo, poulet mayo, Dampfnudeln…), la fiche suit la recette de référence du plat et la vidéo est créditée comme source d'idée.

## 39 nouvelles fiches (1 178 recettes, 625 plats)

- **Favoris** (10) : cookies Rocher cœur noisette, muffins double chocolat, lasagnes montagnardes à la raclette, sauce gombo ivoirienne, sandwich merguez à l'orientale, Eiersalat, sauce curry-mangue, sauce bourguignonne pour fondue, sirop de citron, vinaigre d'épluchures de pommes.
- **Plats des auteurs** (13) : ficelle picarde, potée au chou (version), Hackbraten alsacien, salade de bœuf feta-avocat, médaillons de courgette farcis, poulet mayo ivoirien, gésiers sautés, garba, pâtes crémeuses au poulet croustillant, poêlée pommes de terre-viande hachée, gratin pommes de terre-poulet, et 2 plats végétariens tirés des légendes (gâteau invisible de courgettes au chèvre, pâtes au Mont d'Or et aux champignons).
- **Autres plats végétariens** (4), pour garder un tiers de plats sans viande ni poisson : pâtes au pesto de vert de poireau, tatin de carottes, salade westaf, fromage pané et pommes de terre au paprika fumé.
- **Entrées, goûters, bases** (12) : rouleaux de brick reblochon-bœuf, boules de pomme de terre à la mozzarella, soupe froide concombre-zaatar, velouté d'épluchures d'asperges, barres cookie s'mores, moelleux à la poêle, fleurs de pommes, Dampfnudeln, buns fourrés, lait concentré sucré maison, mayonnaise sans œuf, sirop de fraise.

Toutes ces fiches sont **non testées en cuisine**.

## Angles morts comblés

1. **Auteurs jamais explorés** : les 8 profils sont lus, et la collecte relit désormais tous les relevés datés (`prive/favoris_*.txt`, `prive/createurs_*.txt`).
2. **Bibliothèque « À vérifier »** : une vidéo rattachée à une fiche prend la rubrique de la fiche (`classement.section_from_fiche`). Une rubrique « Europe : autres pays » a été ajoutée, ainsi que des mots-clés courants (KFC, foutou, alsacien, brookie…). Résultat : le relevé du 29/10 passe de 98 à 20 vidéos « À vérifier » sur 182, celui du 22/10 de 131 à 82 (dont 20 vidéos hors cuisine retirées). Les vidéos restantes n'ont qu'une légende du type « #cuisine #pourtoi » ; il faut les regarder pour les classer.
3. **Vie privée** : les favoris hors cuisine sont retirés du relevé et des légendes lues, pas seulement écartés de la publication. **Rattrapage** : 29 favoris hors cuisine (finance, IA, emploi, immigration, bricolage…) des relevés du 14/10 et du 22/10 s'étaient glissés dans « À vérifier » et étaient publiés. Ils sont retirés de la bibliothèque et des listes classées. La liste des comptes à exclure reste privée (`recettes-classees/prive/hors_cuisine.txt`), et les relevés comme l'export la filtrent désormais (`recettes-classees/hors_cuisine.py`). Ces titres restent toutefois dans l'historique git du dépôt public. Les numéros WhatsApp que certaines créatrices mettent dans leurs légendes (« pour passer commande… ») sont coupés des titres publiés ; un titre ancien du 14/10 en contenait un, retiré.
4. **Contrôles** : tests 105 (39 fiches créditées, au moins 6 plats végétariens), 106 (les vidéos d'origine sont dans la bibliothèque, aucune dans « À vérifier ») et 107 (aucune coordonnée de créateur dans les titres publiés). Les 30 plats « à tester en priorité » ont été régénérés (garba, poulet mayo et sandwich merguez y entrent).

Liste classée : `recettes-classees/favoris_createurs_2026-10-29_classes.md` (lue par l'export).
