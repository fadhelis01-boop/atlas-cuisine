# Audit « cuisinier amateur » d'ATLAS (21/11/2026)

Le regard de quelqu'un qui ne connaît pas la cuisine professionnelle, qui déclare un régime (végétarien, sans porc,
allergies) et fait confiance à l'application pour le tenir. Parcours réel de l'appli en local (onboarding, accueil,
recherche, fiches, filtres, frigo, profil, enfants, Ma semaine) avec vérification systématique sur les données
exportées (`recipes.json`, `recipes_detail.json`, `catalogue.json`) pour chiffrer chaque constat. Rien n'a été corrigé :
ce document liste les angles morts trouvés, par ordre de gravité.

## 1. Constats mesurés

| # | Angle | Mesure | Gravité |
|---|---|---|---|
| 1 | **Le filtre « Végétarien » (et par ricochet « sans porc », allergies) ne voit pas certains abats et gibiers** | 9 fiches ont leur ingrédient principal non référencé au Tome 3 (`ref: null`) : tête de veau, foie gras de canard, cuisses de grenouilles, ris de veau, rognons de veau, pigeon, lièvre (2 fiches), faisan. Le moteur de filtrage (`isFlesh`) ne peut rien dire d'un ingrédient sans référence : ces 9 plats passent le filtre « Végétarien » sans déclencher d'alerte. Vérifié de bout en bout : profil Végétarien activé → fiche « Tête de veau, sauce gribiche » ouverte → aucun bandeau, aucune alerte, la fiche affiche même « c'est léger pour un plat » sur les protéines (car l'ingrédient non référencé n'est pas compté non plus). | **forte** |
| 2 | **Une fiche a son ingrédient référencé sous la mauvaise espèce** | « Jambon de dinde maison » utilise en interne la référence « Blanc de **poulet** » au lieu de « Dinde (escalope, cuisse, filet) », qui existe pourtant au Tome 3. Conséquence concrète : dans « Avec ce que j'ai », la fiche s'affiche comme utilisant du poulet déjà au frigo, et l'estimation protéines/allergènes se base sur du poulet plutôt que de la dinde. | moyenne |
| 3 | **L'icône du plat (emoji) se trompe sur au moins 113 fiches**, par collision de sous-chaîne dans les règles de `art.tsx` (pas de limite de mot dans les regex) : <br>• « pois **chiche**(s) » et « chicharrón » → icône poulet 🍗 sur des plats 100 % végétariens (curry de pois chiches, houmous, chana masala, karantika, panisses, falafels-like…) ; <br>• « **coque**/coquillette » → icône poulet 🍗 (œuf à la coque, coquillettes au bœuf) ; <br>• « **mai**son » → icône maïs 🌽 sur presque toutes les fiches « … maison » (mayonnaise, pâte brisée, granola, yaourts, ghee, lait concentré…) ; <br>• « **courge**tte » → icône citrouille 🎃 au lieu d'une courgette ; <br>• « **the** » dans « men**the** » → icône tasse de thé 🍵 sur des plats à la menthe, pas du thé ; <br>• « gyu**don**/katsu**don** » → icône nouilles 🍜 (ce sont des bols de riz, pas des udon) ; <br>• « sol**eil** » → icône poisson 🐟 (« Terrine de légumes du soleil ») ; <br>• « muff**ul**etta » → icône légumineuses 🥣. <br>Repéré en premier sur l'accueil : « Karantika (flan de pois chiche) », un plat végétarien, affichait une cuisse de poulet en guise de photo de secours. | moyenne (visible dès la page d'accueil, mais cosmétique) |
| 4 | **La liste « Au programme (fiches à venir) » est à moitié obsolète** | 185 des 381 entrées de `catalogue.json` correspondent déjà à une fiche publiée du même nom (ex. Poulet yassa, Tartiflette, Ratatouille, Quiche lorraine, Choucroute garnie…). La recherche les affiche pourtant dans « Au programme », juste en dessous des mêmes plats déjà trouvés dans les résultats : l'utilisateur voit le même nom listé deux fois, une fois comme fiche existante, une fois comme « pas encore écrite ». `Search.tsx` interroge `CATALOGUE` sans jamais le croiser avec `RECIPES`. | forte (confiance : l'appli se contredit elle-même dans le même écran) |

## 2. Repéré mais écarté (faux positifs vérifiés)

- « Gratin de céleri-rave… », « Atakilt wat » → icône frites 🍟 : voulu (toute fiche avec « pommes de terre » prend cette icône, choix assumé de granularité grossière, pas un bug).
- « Choucroute garnie (version bœuf et volaille) » → icône poulet 🍗 : correct, la fiche contient bien de la volaille.
- « Coq au vin », « Samgyetang (coquelet…) » → icône poulet 🍗 : correct, ce sont de vraies volailles.
- « Jambon de dinde maison » (sel nitrité, cuisson à cœur) : la fiche elle-même est exemplaire sur la sécurité alimentaire (dosage du sel nitrité répété deux fois, sonde présentée comme obligatoire, pas en option) — seul le problème n°2 ci-dessus la concerne.
- Page Enfants, diversification, sécurité (miel, étouffement, œuf cru) : toujours à jour et complète, rien à ajouter.

## 3. Pourquoi c'est un angle mort pour un cuisinier amateur

Un débutant qui déclare « Végétarien » ou une allergie fait une confiance totale au badge affiché sur la fiche : il ne
va pas relire la liste d'ingrédients en expert pour vérifier. Les 9 fiches du constat n°1 sont justement les plus
piégeuses pour un amateur (abats, gibier) : impossible de deviner au titre seul qu'il y a un trou dans le filtre. Le
constat n°4 touche la confiance différemment : voir le même plat listé comme « déjà là » et « à venir » dans le même
écran fait douter de la fiabilité de tout le reste.

## 4. Pistes de correction (non appliquées)

- **#1** : référencer les 9 ingrédients manquants au Tome 3 (tête de veau, foie gras, cuisses de grenouilles, ris et
  rognons de veau, pigeon, lièvre, faisan) — ou, à défaut, ajouter une règle de secours dans `isFlesh`/l'export qui
  traite tout ingrédient `ref: null` de poids ≥ 2 comme suspect et le fait remonter dans le rapport d'export (comme les
  « écarts » déjà listés pour les cuissons non chiffrées).
- **#2** : changer la référence de « Jambon de dinde maison » vers « Dinde (escalope, cuisse, filet) ».
- **#3** : entourer les motifs à risque de limites de mot (`\bchich\b`, `\bcoq\b`, `\bmais\b`, `\bthe\b`…) dans
  `BY_WORD` plutôt que des sous-chaînes libres ; un script de contrôle comme celui utilisé pour cet audit (simuler
  `dishEmoji` sur les 1601 titres et repérer les correspondances à cheval sur une lettre) pourrait devenir un test
  automatique.
- **#4** : à l'export, retirer de `catalogue.json` toute entrée dont le titre normalisé existe déjà dans `recipes.json`
  (le mécanisme de renommages existe déjà pour les doublons de recettes, le même genre de croisement s'applique ici).
