# Audit « cuisinier expert de la street food » d'ATLAS (12/11/2026)

Le regard d'un cuisinier de stand et de marché de nuit. Les mesures portent sur les fiches exportées, avant correction. Les
recettes ajoutées ont été choisies parmi les plats dont les vidéos de recette sont les plus vues sur TikTok. Contrôle
automatique : test 127.

## 1. Constats mesurés (avant)

| Angle | Mesure | Gravité |
|---|---|---|
| Pas de rubrique | La street food n'était qu'une « envie » de l'accueil, calculée sur des mots du titre (taco, burger, nem…). Elle ratait la moitié des plats de rue (suya, dibi, alloco, msemen, takoyaki…). Elle comptait à tort des plats qui n'en sont pas (« crêpes Suzette » pour « crêpe », « pizza » de famille). | forte |
| Classiques absents | 33 plats de rue majeurs manquaient. Mexique : esquites, tlayuda, sopes. États-Unis : hot-dog, cheesesteak. Amérique du Sud : anticuchos, choripán, coxinha, acarajé, salchipapa. Caraïbes : doubles, patties. France : galette-saucisse, panisse. Europe : supplì, piadina, lángos, zapiekanka, trdelník. Proche-Orient et Turquie : sabich, kumpir, tantuni, balık ekmek. Maghreb : bambalouni, mahjouba. Afrique : rolex, akara. Asie : jianbing, eomuk, martabak, roujiamo, egg waffle, dan bing | forte |
| Gestes du métier | Rien ne réunissait les repères des stands. Températures d'huile par usage, double cuisson, préchauffe de la plaque, pain toasté côté mie, mise en place : tout était dispersé dans les fiches. | moyenne |
| Sécurité de la friture | Rien sur l'huile qui prend feu, la durée de vie d'une huile de friture ni le maintien au chaud (63 °C). La règle des 2 h n'était pas rappelée pour un buffet de rue. | forte |
| Soirées | Aucune proposition de « soirée street food » complète : plat, accompagnement, douceur. | moyenne |
| Porc | Plusieurs classiques de rue sont au porc dans leur version d'origine (galette-saucisse, hot-dog, roujiamo, cube de bouillon de la coxinha). | moyenne |

## 2. Corrigé

- **Une vraie rubrique « Street food »** (`/street-food`, tuile dans Explorer, `app/src/lib/streetfood.ts`). Elle compte **134 fiches choisies à la main**, en 6 familles :
  - sandwichs, pains garnis et burgers ;
  - tacos, galettes et crêpes de rue ;
  - fritures, chaussons et beignets salés ;
  - brochettes et grillades ;
  - raviolis, bouchées et bols ;
  - sucré de rue.
  L'envie « Street-food » de l'accueil utilise désormais cette liste.
- **Six soirées toutes faites** : tacos, marché de nuit asiatique, kebab-frites, Afrique de l'Ouest, stand de foire pour enfants, apéro des quais (Marseille, Rome, Istanbul).
- **Les gestes des stands** : température de l'huile selon l'usage, double cuisson, plaque, mise en place, sauces maison, pain toasté. Avec des liens vers les fiches techniques.
- **Friture et sécurité** :
  - feu d'huile (couvercle, jamais d'eau) ;
  - 5 à 6 utilisations d'une huile au plus ;
  - cuisson à cœur des viandes ;
  - 2 h au plus à température ambiante et 63 °C pour garder au chaud ;
  - sauces à l'œuf cru.
- **33 fiches nouvelles** (`recipes_v7_street_food.py`), avec à chaque étape son geste, sa température d'huile et son repère de cuisson. Chacune reçoit la **vidéo de recette la plus aimée** de la recherche TikTok sur son plat (`videos_favoris.EN_PLUS_2026_11_12B`), par exemple Rodrigo Fernandini pour les anticuchos et le choripán, ou Dwight Smith pour les patties. Les birria tacos (Alex Rios, 434 000 j'aime), le smash burger, le kebab maison et le french tacos reçoivent aussi la leur.
- **Sans porc** : saucisses de volaille ou de bœuf. Le roujiamo est au bœuf, la coxinha au bouillon maison. La fiche dit quand l'original est au porc.
- **Doublons évités** : les bretzels et le künefe existaient déjà. Leurs fiches sont gardées et reçoivent la vidéo.
- **Mini-carte d'origine sur chaque vignette de recette** : le pays est en couleur et un point marque la région. Un seul fond de carte est partagé par toutes les vignettes, pour rester léger.
- Fiches techniques reliées : frire, wok, griller, plier les raviolis.

## 3. Reste à faire

- Les vidéos rattachées sont des démonstrations d'autres cuisiniers. Les fiches ATLAS sont écrites à part et ne reprennent pas leurs textes.
- Aucune recette n'est testée en cuisine. Les plus délicates sont à tester d'abord : acarajé et akara (dérober le niébé), lángos, mahjouba (pâte étirée), supplì.
