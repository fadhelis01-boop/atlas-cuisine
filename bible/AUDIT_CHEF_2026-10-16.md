# Audit du chef : le panel de recettes d'ATLAS (16 octobre 2026)

Regard d'un chef de cuisine française, italienne et du monde sur les recettes de l'application : ce qui manquait, ce qui bloquait un amateur, ce qui a été ajouté. Les choix déjà validés restent la règle : Tome 13 §0 (goût franc, 10 ingrédients au plus, gestes simples, matériel d'une cuisine française, repères par les sens), D21 (plats où le porc est structurant : nom d'origine + « version », variantes sans porc ou sans alcool marquées « À tester »), D17 (food fusion transversale), D19 (aucune image générée par IA), Tome 4 comme programme.

Toutes les fiches ajoutées sont **non testées en cuisine**, comme les précédentes (Tome 7 §2). L'application l'affiche sur chaque fiche.

## 1. Mesures avant et après

| | Avant (713 fiches) | Après (889 fiches) |
|---|---|---|
| Plats du catalogue du Tome 4 couverts | 237 / 380 (62 %) | 378 / 380 (99 %) |
| Part de la France | 42 % | 36 % |
| Fiches italiennes | 42 | 61 |
| Espagne, Portugal, Grèce | 30 | 41 |
| Moyen-Orient | 32 | 50 |
| Asie de l'Est | 39 | 58 |
| Plats végétariens (part des plats) | 35 % (31 % à mi-parcours) | 33 % |
| Fiches de niveau 3 | 13 | 28 |
| Fiches à plus de 10 ingrédients | 24 | 24 (aucune parmi les nouvelles) |
| Ingrédients rares avec un substitut de supermarché | 0 | 99 |
| Contrôles automatiques | 64 | 67 |

Le décompte du catalogue est fait plat par plat. Deux entrées restent volontairement sans fiche : la fabada, que le Tome 4 classe « porc structurant, non adaptable », et les tripes à la mode de Caen (abat absent du Tome 3, huit heures de cuisson, cidre et calvados indissociables). Les ajouter demanderait une décision de ta part, pas une simple rédaction.

## 2. Constats du chef

### Ce qui tenait déjà

La base française est solide : sauces mères, pâtisserie de ménage, plats mijotés, cuisine de région. Les fiches sont courtes, chaque étape donne un repère visuel ou sonore (« l'huile perle », « la lame ressort presque sèche ») et l'enfant a sa place. Pour un amateur, c'est le bon ton.

### Ce qui manquait

- **L'Italie était sous-représentée** pour une cuisine que les Français cuisinent chaque semaine : pas d'amatriciana, pas de risotto alla milanese, pas de vongole, ni de vitello tonnato, de ribollita ou de cannoli. Aucune entrée par région italienne.
- **Les grands classiques du monde** qu'un amateur cherche en premier manquaient par dizaines : couscous royal, pastilla, tajine aux pruneaux, poulet tikka masala, massaman, tom yum, gyudon, tempura, japchae, mole, moqueca, gumbo, canard laqué, apple pie.
- **Des pans entiers de la carte** se résumaient à trois ou quatre fiches : Europe centrale et de l'Est, Iran, Turquie, Corée, Amérique du Sud.
- **Les régions françaises** de Corse, du Centre, des Pays de la Loire et d'Occitanie étaient pauvres.
- **Les ingrédients rares** sans plan B : le scotch bonnet seul apparaissait dans 17 fiches, et rien n'indiquait par quoi le remplacer.

### L'angle mort qu'on ne voit qu'en cuisinant le panel

Les grands classiques du monde sont presque tous carnés. Ajouter les 140 premières fiches a fait tomber la part végétarienne de 35 % à 31 %, sous le seuil validé de 33 %. Le contrôle automatique l'a signalé. La correction n'est pas un détail : 33 plats végétariens « de vraie cuisine » ont été écrits (kuku sabzi, mercimek köftesi, misir wat, red red, matar paneer, pupusas, gemista, lobio, couscous aux sept légumes, quiche aux poireaux…), plutôt que des salades de remplissage.

## 3. Ce qui a été ajouté (176 fiches)

| Fichier | Fiches | Contenu |
|---|---|---|
| `recipes_v3_france.py` | 17 | Soufflé au fromage, bouchées à la reine, moules marinières, sole normande, axoa, bourride, petit salé (version sans porc en variante), soupe corse, tarte au sucre du Nord… |
| `recipes_v3_italie_sud.py` | 27 | Amatriciana (guanciale, variante dinde fumée), risotto milanese, vongole, ribollita, vitello tonnato, cannoli, scaloppine ; Espagne, Portugal, Grèce : pulpo, pastitsio, salmorejo, keftedes… |
| `recipes_v3_nord_ameriques.py` | 33 | Cottage pie, Wiener Schnitzel, Stroganov, pelmeni, sarmale (version bœuf), Sachertorte ; gumbo, tourtière, pâté chinois, dinde farcie ; mole, moqueca, causa, ajiaco, tres leches, jerk |
| `recipes_v3_asie.py` | 29 | Gyudon, yakitori, tempura, chawanmushi, makis (sans poisson cru par défaut), japchae, kimbap, wontons ; paratha, sambar, rajma, korma, gulab jamun ; curry rouge, massaman, tom yum, riz de Hainan |
| `recipes_v3_orient_afrique.py` | 49 | Couscous royal, pastilla, tajine aux pruneaux, rechta, bissara ; mansaf, maqluba, fesenjan, koobideh, plov, dolmas ; egusi, bunny chow, malva ; agneau-kumara, parma ; bloc végétarien |
| `recipes_v3_complements.py` | 21 | Les derniers trous du catalogue : quenelles Nantua, full English et bigos (versions volaille), tikka masala, thali, canard laqué, hot pot, apple pie, tamales, griot (version poulet), méchoui, baba ghanoush… et cinq plats végétariens de semaine |

Répartition des niveaux : 108 fiches de niveau 1, 53 de niveau 2, 15 de niveau 3. Le niveau 3 est réservé aux plats où le geste compte vraiment (tempura, pastilla, Sachertorte, gumbo et son roux brun), et chaque fois le point d'échec est écrit dans l'étape (« s'il noircit ou sent le brûlé : recommence »).

## 4. Accessibilité pour un amateur

- **Plan B pour chaque ingrédient rare.** Nouveau fichier `app/src/lib/substituts.ts`, 99 correspondances écrites en cuisinier : gochujang → concentré de tomate, miel, soja et piment ; galanga → gingembre et zeste de citron ; poivre du Sichuan → poivre noir et baies roses. La fiche recette l'affiche à côté du badge « rare » (« sinon : … »), la page de l'ingrédient dans le dictionnaire aussi.
- **Dix ingrédients au plus** sur toutes les nouvelles fiches. Trois dépassaient (couscous royal, couscous aux sept légumes, gumbo) : l'ingrédient secondaire passe dans l'étape (« et 150 g de gombos si tu en trouves »).
- **Matériel courant.** Aucune nouvelle fiche ne demande de robot. Le thermomètre apparaît là où il évite un raté ou un risque (friture, volaille entière, sirop).
- **Sécurité.** Poisson cru (makis) et viande crue (carpaccio, hot pot) portent l'avertissement : congélation préalable du poisson, baguettes séparées, pas de jeunes enfants ni de femmes enceintes.
- **Alcool et porc.** Seize nouvelles fiches portent une variante sans alcool ou sans porc, toutes marquées « À tester ». Les plats où le porc est structurant suivent D21 : bigos, full English, griot, sarmale, dan dan noodles, tourtière gardent leur nom avec « version ».

## 5. Contrôles automatiques ajoutés

- **65.** Trente grands classiques présents, chacun à 10 ingrédients au plus et 3 étapes au moins.
- **66.** Les versions D21 ne contiennent aucun ingrédient porcin hors option signalée.
- **67.** Seize ingrédients rares ont chacun un substitut, et leur nom existe bien dans le Tome 3.

Le contrôle 63 (variété) a aussi fait son travail en arrêtant la baisse de la part végétarienne. Le seuil reste à 33 %.

## 6. Photos

Audit précédent : sur les 137 fiches ajoutées le 16 octobre, 104 ont maintenant une vraie photo libre de droits (Wikimedia Commons, crédit et licence dans la page Crédits). Pour les 33 autres, aucun candidat ne convenait (mauvais plat, porc visible sur une fiche végétarienne ou sans porc, image hors sujet). Elles gardent leur icône dessinée plutôt qu'une photo trompeuse.

Les 176 fiches du chef passent par la même chaîne : collecte (`illustrations/collect_v4.py`), planches de choix, sélection à la main, conversion AVIF et WebP.

## 7. Ce qui reste et dépend de toi

1. Fabada et tripes : les laisser hors de l'application, ou valider une « version » (haricots et bœuf fumé pour l'une, gras-double de bœuf sans calvados pour l'autre).
2. Tester en cuisine en priorité les 15 fiches de niveau 3 et les 16 variantes « À tester ».
3. Le catalogue du Tome 4 est maintenant presque épuisé. La suite logique serait un Tome 4 bis : desserts du monde (il en manque plus que de plats), cuisine de saison par mois, et fiches « reste du rôti du dimanche ».
