# Audit « cuisinier de 20 ans et chef de famille de 4 enfants » (13/11/2026)

J'ai regardé ATLAS comme quelqu'un qui cuisine tous les jours pour 6 : 2 adultes et 4 enfants, de la maternelle au collège.
Les mesures portent sur les 1 519 fiches exportées et sur le planificateur de semaine. Les audits famille précédents
(16/10, 10/11) ne sont pas refaits. Contrôle automatique : test 130.

## 1. Ce qui est déjà solide pour une famille nombreuse

- **Classiques du quotidien** : 83 sur 88 présents, par exemple :
  - plats : hachis, gratin dauphinois, lasagnes, bolognaise, poulet rôti, blanquette, pot-au-feu, chili, croque, quiche, pizza, crêpes ;
  - desserts et goûters : gâteau au yaourt, riz au lait, clafoutis, crumble, cookies, madeleines.
- **Foyer détaillé** : adultes et âges des enfants. Les portions s'en déduisent (un enfant de moins de 11 ans compte pour une demi-part), sur les fiches comme dans Ma semaine.
- **Volume** : 694 plats adaptés dès 3 ans, 220 plats prêts en 30 minutes au plus, 432 plats économiques (€).
- **Ma semaine** :
  - semaine remplie avec des repères d'équilibre (poisson et légumineuses 2 fois, un seul plat riche) ;
  - dimanche midi en menu complet, restes réutilisés le lendemain ;
  - gamelles du lendemain, liste de courses unique, budget, préparation à l'avance.
- **Rubriques famille** : Enfants (par âge, diversification, légume refusé, petit chef), Pique-nique et gamelle, Restes, Zéro déchet, anniversaire dans les Fêtes.

## 2. Angles morts mesurés (avant)

| Angle | Mesure | Gravité |
|---|---|---|
| Cantine | Le planificateur ignorait que les enfants mangent à la cantine le midi. Sur 12 semaines simulées, 7 dîners de soir d'école reprenaient de la viande, déjà servie à midi. | forte |
| Goûters | La semaine ne prévoyait que les midis et les soirs. Rien pour les 4 goûters quotidiens, alors que 80 goûters de l'appli tiennent plusieurs jours ou se congèlent. | forte |
| Classiques absents | Poisson pané maison (le premier poisson des enfants), semoule au lait, œuf à la coque et mouillettes, rôti du dimanche, gratin de poisson | moyenne |
| Fait maison du quotidien | Yaourts maison, biscuit roulé (gâteau d'anniversaire des petits), frites de légumes (porte d'entrée des légumes racines) | moyenne |

## 3. Corrigé

- **Mode cantine** dans Ma semaine (case « Cantine le midi : soirs plus légers »). Les lundis, mardis, jeudis et vendredis soir, le planificateur favorise légumes, légumineuses, œufs et poisson, et écarte viande et volaille. Le mercredi et le week-end ne changent pas. Sur 12 semaines simulées, les dîners avec viande les soirs d'école passent de 7 à 0, sans casser les autres équilibres.
- **Les goûters de la semaine** : chaque semaine, 3 goûters faciles et économiques à préparer le dimanche, qui tiennent plusieurs jours en boîte ou se congèlent. Ils sont pris parmi 17 recettes (gâteau au yaourt, banana bread, crêpes, sablés, barres de céréales…) et rappellent le goûter complet : avec un fruit et un laitage.
- **8 fiches nouvelles** (`recipes_v7_famille.py`), avec les gestes que les enfants peuvent faire et la congélation :
  - poisson pané maison au four ;
  - semoule au lait ;
  - œuf à la coque et mouillettes (œuf mollet pour les plus petits) ;
  - rôti du dimanche moutarde-miel, en version dinde ou veau ;
  - gratin de poisson aux épinards ;
  - yaourts maison sans yaourtière ;
  - biscuit roulé à la confiture ;
  - frites de légumes au four.

## 4. Reste à faire (proposé)

- Une vraie séance de « cuisine du dimanche » : 3 ou 4 plats préparés en 2 heures, dans le bon ordre (four d'abord, puis plaques), avec une seule liste. La semaine donne déjà « à préparer à l'avance » et « lave et coupe d'un coup ».
- Indiquer dans la semaine ce que la cantine a servi (menu du jour saisi ou importé), pour ajuster finement le dîner.
- Aucune recette n'est testée en cuisine.
