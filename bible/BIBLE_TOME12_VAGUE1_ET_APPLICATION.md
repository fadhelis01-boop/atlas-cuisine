# 📘 BIBLE ATLAS : TOME 12 : Vague 1 (59 fiches), corpus importé et application v1

> Ce tome **intègre à la bible** trois livraisons du 14/10/2026 :
> 1. **59 nouvelles fiches** (vague 1) au format du Tome 11 : pains et bases, sauces maison, plats et entrées du monde, desserts, fêtes, anti-gaspi, boissons sans alcool. Avec les 11 fiches étalons, le catalogue rédigé compte **70 recettes complètes** ;
> 2. le **corpus d'imports classés** : 585 recettes des favoris TikTok du compte et 339 recettes du site Cooking with Morgane, triées dans les catégories de la bible ;
> 3. **l'application ATLAS v1** (PWA iPhone, iPad, Mac, Android, PC), construite à partir des Tomes 1 à 11 et de ce tome.
>
> **Statut des fiches : « Brouillon rédactionnel prêt pour le Test 1 »**, comme au Tome 11. **Aucune n'a été testée en cuisine** ; quantités et temps = pratiques usuelles, à confirmer par le Tome 7 §2. Badges **calculés** par le moteur de référence (`atlas_engine.py`) sur le référentiel du Tome 3 (**confiance C**). Variantes et règles génériques : **à tester** (Tome 7 §3).

---

## 1. Tableau récapitulatif de la vague 1 (calculé)

| # | Recette | Région | Rubriques | Allergènes (sûrs) | Porc | Alcool | Sans porc Std / Strict | Sans alcool Std / Strict | Enfants dès |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Pain en cocotte sans pétrissage | France | pains | GL | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 4 |
| 2 | Pâte à pizza maison (express ou 24 h) | Campanie | pains | GL | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 3 |
| 3 | Pizza margherita | Campanie | pains, enfants | GL, LA | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 3 |
| 4 | Naan à la poêle (nature, ail ou fromage) | Inde | pains, enfants | GL, LA | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 3 |
| 5 | Pain pita (four ou poêle) | Liban | pains | GL | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 4 |
| 6 | Focaccia moelleuse au romarin | Ligurie | pains, fetes | GL | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 3 |
| 7 | Msemen (crêpes feuilletées) | Maroc | pains, fetes | GL, LA | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 6 |
| 8 | Batbout (pain marocain à la poêle) | Maroc | pains, enfants | GL | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 4 |
| 9 | Galette de sarrasin complète | Bretagne | pains, enfants | LA, OE | 🐖 | ✅ | 🔄 / 🔄 | ✅ / ✅ | 3 |
| 10 | Pancakes moelleux | États-Unis | pains, enfants | GL, LA, OE | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 3 |
| 11 | Pain de mie maison | France | pains, enfants | GL, LA | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 4 |
| 12 | Brioche maison | Normandie | pains, fetes | GL, LA, OE | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 4 |
| 13 | Pâte brisée maison | France | pains | GL, LA | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 4 |
| 14 | Chapati (galettes de blé complet) | Inde | pains | GL, LA | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 3 |
| 15 | Tortillas de blé | Mexique | pains, enfants | GL | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 3 |
| 16 | Ketchup maison | États-Unis | sauces, enfants | – | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 2 |
| 17 | Sauce samouraï maison | France | sauces, fusion | MO, OE | ✅ | 🟡 traces | ✅ / ✅ | ✅ / 🔄 | – |
| 18 | Sauce blanche (kebab, grillades) | France | sauces, enfants | LA | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 2 |
| 19 | Sauce burger maison | États-Unis | sauces, enfants | MO, OE | ✅ | 🟡 traces | ✅ / ✅ | ✅ / 🔄 | 3 |
| 20 | Sauce barbecue maison | États-Unis | sauces | MO, PO | ✅ | 🟡 traces | ✅ / ✅ | ✅ / 🔄 | 3 |
| 21 | Sauce andalouse maison | Belgique | sauces, enfants | MO, OE | ✅ | 🟡 traces | ✅ / ✅ | ✅ / 🔄 | 3 |
| 22 | Harissa maison | Tunisie | sauces | – | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | – |
| 23 | Pesto au basilic (ou aux fanes) | Ligurie | sauces, zero_dechet, enfants | LA | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 3 |
| 24 | Sauce tomate maison | Italie | sauces, enfants, zero_dechet | – | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 1 |
| 25 | Béchamel | France | sauces, enfants | GL, LA | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 1 |
| 26 | Vinaigrette de base (et variantes) | France | sauces, enfants, zero_dechet | MO | ✅ | 🟡 traces | ✅ / ✅ | ✅ / 🔄 | 2 |
| 27 | Tzatziki | Grèce | sauces, enfants | LA | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 2 |
| 28 | Frites maison (double cuisson, four ou airfryer) | Belgique | sauces, enfants, techniques | – | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 3 |
| 29 | Bouillon de volaille avec la carcasse | France | zero_dechet, sauces | CE | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 1 |
| 30 | Bouillon d'épluchures de légumes | France | zero_dechet | – | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 1 |
| 31 | Mafé de poulet | Mali / Sénégal | enfants | AR | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 2 |
| 32 | Chorba frik (soupe du Ramadan) | Algérie | fetes, enfants | CE, GL | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 1 |
| 33 | Salade de carottes au cumin et à l'orange | Maroc | enfants | – | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 1 |
| 34 | Houmous | Liban | enfants, fetes, zero_dechet | SE | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 1 |
| 35 | Taboulé libanais (au persil) | Liban | enfants | GL | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 3 |
| 36 | Chakchouka (œufs pochés à la tomate et aux poivrons) | Tunisie | enfants, zero_dechet | OE | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 1 |
| 37 | Riz cantonais | Canton | enfants, zero_dechet | GL, OE, SO | 🐖 | 🟡 traces | 🔄 / 🔄 | ✅ / 🔄 | 2 |
| 38 | Poulet teriyaki | Japon | enfants | GL, SE, SO | ✅ | 🍷 | ✅ / ✅ | 🔄 / 🔄 | 2 |
| 39 | Chili con carne | Texas | enfants, fetes, fusion | – | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 2 |
| 40 | Guacamole | Mexique | enfants, fetes | – | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 1 |
| 41 | Accras de morue | Antilles | fetes | GL, PO | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 3 |
| 42 | Quiche lorraine | Lorraine | enfants, zero_dechet | GL, LA, OE | 🐖 | ✅ | 🔄 / 🔄 | ✅ / ✅ | 1 |
| 43 | Gratin dauphinois | Dauphiné | enfants, fetes | LA | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 1 |
| 44 | Velouté de potiron (et graines grillées) | France | enfants, zero_dechet, fetes | LA | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 1 |
| 45 | Poulet rôti du dimanche (plat-mère) | France | enfants, zero_dechet, fetes | LA | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 1 |
| 46 | Mousse au chocolat | France | fetes | LA, OE | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 5 |
| 47 | Meringues (avec les blancs restants) | France | zero_dechet, enfants | OE | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 3 |
| 48 | Pain perdu | France | zero_dechet, enfants | LA, OE | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 1 |
| 49 | Banana bread | États-Unis | zero_dechet, enfants | FC, GL, LA, OE | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 1 |
| 50 | Tiramisu | Vénétie | fetes | GL, LA, OE | ✅ | 🍷 | ✅ / ✅ | 🔄 / 🔄 | – |
| 51 | Gâteau au yaourt | France | enfants | GL, LA, OE | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 3 |
| 52 | Oranges à la cannelle | Maroc | enfants, fetes | – | ✅ | 🟡 traces | ✅ / ✅ | ✅ / 🔄 | 1 |
| 53 | Riz au lait vanille | France | enfants, zero_dechet | LA | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 1 |
| 54 | Galette des rois à la frangipane | Île-de-France | fetes | FC, GL, LA, OE | ✅ | 🍷 | ✅ / ✅ | 🔄 / 🔄 | 4 |
| 55 | Bissap (jus d'hibiscus) | Sénégal | boissons, enfants, fetes | – | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 3 |
| 56 | Citronnade à la menthe | Maghreb | boissons, enfants | – | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 3 |
| 57 | Lassi à la mangue | Inde | boissons, enfants, zero_dechet | LA | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 1 |
| 58 | Thé à la menthe | Maroc | boissons, fetes | – | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | – |
| 59 | Jus de gingembre | Côte d'Ivoire | boissons, fetes | – | ✅ | ✅ | ✅ / ✅ | ✅ / ✅ | 6 |

**Légende** : identique au Tome 11 §1. **🔄** = version adaptée par une variante de la fiche ou une règle générique (§4), **à tester**. **Enfants dès** : âge minimal conseillé (Tome 1 §7.6).

**Couverture des rubriques demandées** (vague 0 + vague 1) : pains : 17 · sauces : 16 · enfants : 45 · fetes : 22 · zero_dechet : 17 · boissons : 5 · techniques : 1.

---

## 2. Fiches de la vague 1

### 2.1 Pain en cocotte sans pétrissage

*No-knead bread · France · Pain*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 8 | 15 min | 13 h 00 | **13 h 15** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten
- 👶 **Enfants** : ✓✓ dès 4 ans : mélanger, façonner. La cocotte chaude reste pour les adultes.

**Équipement** : Cocotte en fonte avec couvercle (24 cm environ), saladier, papier cuisson, four.

Le pain le plus simple qui soit : on mélange, on attend une nuit, on cuit en cocotte. La cocotte fermée garde la vapeur et donne une croûte de boulanger.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 500 g | de farine de blé T65 (ou T55) | Farine de blé T65 (tradition) | 🟢 |
| 380 g | d'eau tiède (76 % d'hydratation) | *implicite* | 🟢 |
| 10 g | de sel fin | Sel fin / gros sel / fleur de sel | 🟢 |
| 2 g | de levure boulangère sèche (½ c. à c.) | Levure boulangère sèche | 🟢 |

**Étapes**

1. **Mélange.** Dans un saladier, mélange farine, sel et levure. Ajoute l'eau et remue avec une cuillère jusqu'à ce qu'il n'y ait plus de farine sèche. La pâte est collante : c'est normal.
2. **Pousse longue.** Couvre et laisse reposer 12 à 18 h à température ambiante (20 °C). La pâte doit avoir doublé et être couverte de bulles.
3. **Façonnage.** Renverse la pâte sur un plan fariné. Rabats les bords vers le centre pour former une boule. Pose-la, soudure dessous, sur du papier cuisson.
4. **Apprêt.** Couvre d'un torchon et laisse lever 1 h. Pendant ce temps, mets la cocotte vide avec son couvercle dans le four et préchauffe à 240 °C (th. 8) pendant 45 min.
5. **Cuisson couverte.** ⚠️ La cocotte est brûlante : gants épais. Dépose le pain avec son papier dans la cocotte, couvre et enfourne 30 min.
6. **Cuisson à découvert.** Retire le couvercle et cuis encore 15 à 20 min, jusqu'à une croûte brun foncé. Le pain sonne creux quand on tape dessous.
7. **Refroidissement.** Laisse refroidir 1 h sur une grille avant de couper.

**Astuces et sécurité**

- Pas de cocotte ? Un plat en fonte ou en terre allant au four, couvert de papier aluminium, fonctionne aussi.
- Ajoute 100 g de graines (tournesol, courge, lin) à l'étape 1 pour un pain aux graines.
- Remplace 100 g de farine blanche par de la farine complète ou de seigle pour plus de goût.

**Conservation** : 3 jours dans un torchon. Congélation : 3 mois, en tranches.

**Zéro déchet** : **Pain rassis** → pain perdu (recette liée), chapelure, croûtons. **Croûtons de fin de pain** → soupe, panzanella.

**Techniques** : Pointage, Façonner une boule, Cuire en cocotte · **À valider au test** : Durée de pousse selon la saison ; cocotte 22 vs 26 cm ; four statique vs ventilé.

---

### 2.2 Pâte à pizza maison (express ou 24 h)

*Impasto per pizza · Europe du Sud › Italie › Campanie · Pain*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 4 | 20 min | 2 h 00 | **2 h 20** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten
- 👶 **Enfants** : ✓✓ dès 3 ans : étaler et garnir.

**Équipement** : Saladier, four ménager (le plus chaud possible), plaque à pâtisserie ou plaque épaisse.

Une pâte souple et alvéolée pour 4 pizzas. En version express, elle est prête en 2 h ; en version longue, 24 h au frigo, elle gagne en goût et en légèreté.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 500 g | de farine de blé T55 (ou T45) | Farine de blé T55 | 🟢 |
| 325 g | d'eau tiède (65 %) | *implicite* | 🟢 |
| 10 g | de sel fin | Sel fin / gros sel / fleur de sel | 🟢 |
| 5 g | de levure boulangère sèche (2 g pour la version 24 h) | Levure boulangère sèche | 🟢 |
| 2 c. à s. | d'huile d'olive | Huile d'olive vierge extra | 🟢 |

**Étapes**

1. **Pâte.** Délaie la levure dans l'eau tiède. Dans un saladier, mélange farine et sel, verse l'eau et l'huile.
2. **Pétrissage.** Pétris 8 à 10 min à la main, jusqu'à une pâte lisse et souple qui ne colle plus aux doigts.
3. **Pousse.** Version express : couvre et laisse lever 1 h 30 près d'une source de chaleur douce (25 °C), jusqu'à doubler. Version 24 h : 2 g de levure seulement, pousse au frigo, couvert, 24 h.
4. **Pâtons.** Divise en 4 boules de 210 g. Couvre et laisse reposer 30 min (1 h pour la pâte sortie du frigo).
5. **Étalage.** Préchauffe le four au maximum (250 à 275 °C, th. 9) avec la plaque à l'intérieur. Étale chaque boule à la main en partant du centre, en gardant un bord plus épais. Évite le rouleau : il chasse les bulles.
6. **Cuisson.** Garnis puis glisse sur la plaque chaude. Cuis 7 à 10 min, jusqu'à un bord gonflé et doré.

**Astuces et sécurité**

- Une plaque épaisse retournée, préchauffée 30 min, remplace la pierre à pizza.
- Les pâtons se congèlent : décongèle-les une nuit au frigo.

**Conservation** : Pâtons crus : 3 jours au frigo, 2 mois au congélateur.

**Zéro déchet** : **Reste de pâte** → gressins ou pain plat à la poêle. **Pizza du lendemain** → réchauffée à la poêle couverte, 5 min.

**Techniques** : Pétrir, Pointage, Étaler une pâte à pizza à la main · **À valider au test** : Four domestique 250 vs 275 °C ; T45 vs T55 ; 24 h au froid vs express.

---

### 2.3 Pizza margherita

*Pizza Margherita · Europe du Sud › Italie › Campanie · Plat*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 4 | 20 min | 0 min | **20 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten, lait
- 👶 **Enfants** : ✓✓ dès 3 ans.

**Équipement** : Four, plaque épaisse.

Tomate, mozzarella, basilic : la pizza la plus simple et souvent la meilleure. Sur la pâte maison, avec la sauce tomate maison.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 4 | pâtons de pâte à pizza (recette liée) | *sous-recette : Pâte à pizza maison (express ou 24 h)* | – |
| 300 g | de sauce tomate maison (recette liée) | *sous-recette : Sauce tomate maison* | – |
| 250 g | de mozzarella, égouttée et déchirée | Mozzarella / burrata | 🟢 |
| 1 bouquet | de basilic frais | Basilic | 🟢 |
| 2 c. à s. | d'huile d'olive | Huile d'olive vierge extra | 🟢 |

**Étapes**

1. **Mozzarella.** Déchire-la et laisse-la égoutter 20 min dans une passoire : sinon la pizza sera détrempée.
2. **Four.** Préchauffe au maximum (th. 9) avec la plaque dedans, 30 min.
3. **Garniture.** Étale la pâte, puis 3 c. à s. de sauce tomate en laissant 2 cm de bord. Répartis la mozzarella.
4. **Cuisson.** Cuis 7 à 10 min, jusqu'à ce que le fromage bouillonne et que le bord soit doré.
5. **Finition.** À la sortie du four, ajoute les feuilles de basilic et un filet d'huile d'olive.

**Astuces et sécurité**

- Moins de garniture = pizza plus croustillante.
- Pour une pizza « reine » sans porc : jambon de dinde et champignons.

**Conservation** : Se mange aussitôt. Restes : 2 jours au frigo.

**Zéro déchet** : **Petit-lait de la mozzarella** → dans la pâte à pain à la place de l'eau. **Tiges de basilic** → dans la sauce tomate.

**Boissons** : *sans alcool* : Citronnade à la menthe (recette liée) ; Eau pétillante · *avec alcool (adultes)* : Vin rouge léger italien (adultes)

**Techniques** : Étaler une pâte à pizza à la main · **À valider au test** : Égouttage de la mozzarella ; temps de cuisson par type de four.

---

### 2.4 Naan à la poêle (nature, ail ou fromage)

*नान · naan · Asie du Sud › Inde · Pain*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 25 min | 1 h 30 | **1 h 55** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten, lait
- 👶 **Enfants** : ✓✓ dès 3 ans (étaler, badigeonner après cuisson).

**Équipement** : Saladier, poêle en fonte ou antiadhésive avec couvercle, rouleau à pâtisserie.

Pas besoin de four tandoor : une poêle très chaude et un couvercle suffisent pour des naans moelleux et boursouflés. Le yaourt donne la souplesse.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 400 g | de farine de blé T55 | Farine de blé T55 | 🟢 |
| 125 g | de yaourt nature | Yaourt nature | 🟢 |
| 150 ml | d'eau tiède | *implicite* | 🟢 |
| 5 g | de levure boulangère sèche | Levure boulangère sèche | 🟢 |
| 1 c. à c. | de sucre | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 1 c. à c. | de sel | Sel fin / gros sel / fleur de sel | 🟢 |
| 2 c. à s. | d'huile neutre | Huile de tournesol / colza | 🟢 |
| 40 g | de beurre fondu ou de ghee (pour badigeonner) | Beurre clarifié / ghee | 🟡 |
| 2 gousses | d'ail hachées (facultatif) *(facultatif)* | Ail | 🟢 |
| 100 g | de fromage fondu ou de cheddar (facultatif, cheese naan) *(facultatif)* | Fromage à tartiner / fondu | 🟢 |

**Étapes**

1. **Levure.** Mélange l'eau tiède, le sucre et la levure. Attends 5 min qu'une mousse se forme.
2. **Pâte.** Ajoute la farine, le sel, le yaourt et l'huile. Pétris 5 min jusqu'à une pâte souple et légèrement collante.
3. **Pousse.** Couvre et laisse lever 1 h 30, jusqu'à doubler.
4. **Boules.** Divise en 6. Pour un cheese naan : aplatis une boule, mets 1 c. à s. de fromage au centre, referme et aplatis à nouveau.
5. **Étalage.** Étale chaque boule en goutte de 5 mm d'épaisseur.
6. **Cuisson.** Chauffe la poêle à feu vif, sans matière grasse. Cuis 1 à 2 min jusqu'à ce que des bulles se forment, retourne, couvre et cuis 1 min.
7. **Finition.** Badigeonne aussitôt de beurre fondu (mélangé à l'ail si tu veux). Garde les naans sous un torchon.

**Astuces et sécurité**

- La poêle doit être très chaude : c'est le choc de chaleur qui fait gonfler le naan.
- Version sans yaourt : remplace-le par 100 ml de lait + 1 c. à s. de jus de citron.

**Conservation** : 2 jours dans un sac. Congélation : 2 mois ; réchauffe à la poêle.

**Zéro déchet** : **Naan rassi** → chips de naan au four avec huile et épices. **Fond de pot de yaourt** → marinade de poulet.

**Boissons** : *sans alcool* : Lassi à la mangue (recette liée)

**Techniques** : Pétrir, Cuire à la poêle très chaude · **À valider au test** : Fonte vs antiadhésive ; induction vs gaz ; fromage fondu vs cheddar.

---

### 2.5 Pain pita (four ou poêle)

*خبز عربي · khubz arabi · Moyen-Orient & Caucase › Levant › Liban · Pain*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 8 | 25 min | 1 h 15 | **1 h 40** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten
- 👶 **Enfants** : ✓✓ dès 4 ans.

**Équipement** : Saladier, rouleau, plaque épaisse ou poêle avec couvercle, four.

Un pain plat qui gonfle comme un ballon et forme une poche. Parfait pour les falafels, le shawarma ou avec un houmous.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 500 g | de farine de blé T55 | Farine de blé T55 | 🟢 |
| 300 ml | d'eau tiède | *implicite* | 🟢 |
| 7 g | de levure boulangère sèche | Levure boulangère sèche | 🟢 |
| 1 c. à c. | de sucre | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 10 g | de sel | Sel fin / gros sel / fleur de sel | 🟢 |
| 2 c. à s. | d'huile d'olive | Huile d'olive vierge extra | 🟢 |

**Étapes**

1. **Pâte.** Mélange tous les ingrédients et pétris 8 min jusqu'à une pâte lisse.
2. **Pousse.** Couvre et laisse lever 1 h, jusqu'à doubler.
3. **Disques.** Divise en 8 boules, laisse reposer 10 min, puis étale des disques de 15 cm et 4 mm d'épaisseur.
4. **Four.** Préchauffe le four à 250 °C (th. 8-9) avec une plaque épaisse. Cuis 2 ou 3 pitas à la fois, 4 à 5 min : elles gonflent sans dorer.
5. **Poêle (sans four).** Poêle très chaude, 1 min par face, puis retourne encore : la pita gonfle.
6. **Souplesse.** Enferme les pitas dans un torchon dès la sortie : elles restent souples.

**Astuces et sécurité**

- Une pita qui ne gonfle pas : pâte étalée trop finement ou plaque pas assez chaude.

**Conservation** : 2 jours dans un sac. Congélation : 3 mois.

**Zéro déchet** : **Pitas rassies** → chips de pita (fattouche), croûtons.

**Techniques** : Pétrir, Cuire à la poêle très chaude · **À valider au test** : Taux de gonflement four vs poêle ; épaisseur idéale.

---

### 2.6 Focaccia moelleuse au romarin

*Focaccia genovese · Europe du Sud › Italie › Ligurie · Pain* · Fêtes : Apéritif dînatoire, Anniversaire

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 8 | 20 min | 4 h 00 | **4 h 20** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten
- 👶 **Enfants** : ✓✓ dès 3 ans : creuser les alvéoles.

**Équipement** : Saladier, plat à four de 30 × 20 cm, four.

Une pâte très hydratée, presque sans pétrissage, beaucoup d'huile d'olive et des alvéoles qu'on creuse avec les doigts. Idéale à l'apéritif.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 500 g | de farine de blé T55 | Farine de blé T55 | 🟢 |
| 400 g | d'eau tiède | *implicite* | 🟢 |
| 5 g | de levure boulangère sèche | Levure boulangère sèche | 🟢 |
| 10 g | de sel fin | Sel fin / gros sel / fleur de sel | 🟢 |
| 80 ml | d'huile d'olive | Huile d'olive vierge extra | 🟢 |
| 2 branches | de romarin | Thym / romarin | 🟢 |
| 1 c. à c. | de fleur de sel | Sel fin / gros sel / fleur de sel | 🟢 |
| 150 g | de tomates cerises (facultatif) *(facultatif)* | Tomate cerise | 🟢 |

**Étapes**

1. **Mélange.** Mélange farine, levure, sel et eau à la cuillère. Couvre 30 min.
2. **Rabats.** Fais 4 séries de rabats toutes les 30 min : mains mouillées, étire un bord de la pâte et replie-le sur le centre, 4 fois en tournant le saladier.
3. **Plat.** Verse 4 c. à s. d'huile dans le plat. Dépose la pâte, retourne-la pour l'huiler, puis étire-la doucement vers les coins.
4. **Pousse.** Couvre et laisse lever 1 h 30, jusqu'à ce que la pâte soit gonflée et bullée.
5. **Alvéoles.** Préchauffe à 220 °C (th. 7-8). Arrose du reste d'huile, enfonce les doigts jusqu'au fond partout, ajoute romarin, tomates et fleur de sel.
6. **Cuisson.** Cuis 25 min, jusqu'à ce que le dessus soit bien doré. Laisse tiédir 10 min hors du plat.

**Astuces et sécurité**

- Ne lésine pas sur l'huile : elle fait la croûte croustillante dessous.

**Conservation** : 2 jours, réchauffée au four. Congélation : 2 mois.

**Zéro déchet** : **Focaccia rassie** → croûtons à l'huile d'olive, panzanella.

**Boissons** : *sans alcool* : Citronnade à la menthe (recette liée)

**Techniques** : Rabats (pâte hydratée) · **À valider au test** : Hydratation 80 % avec farine T55 française.

---

### 2.7 Msemen (crêpes feuilletées)

*مسمن · msemen · Afrique du Nord › Maghreb › Maroc · Pain* · Fêtes : Ramadan / Aïd

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐⭐ | 10 | 45 min | 20 min | **1 h 05** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten, lait
- 👶 **Enfants** : ✓ dès 6 ans pour le pliage.

**Équipement** : Saladier, grand plan de travail huilé, poêle.

Des carrés feuilletés, croustillants dehors et fondants dedans, qu'on mange au petit-déjeuner ou au ftour avec du miel et du beurre.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 300 g | de farine de blé T55 | Farine de blé T55 | 🟢 |
| 200 g | de semoule de blé fine | Semoule de blé (fine/moyenne) | 🟢 |
| 1 c. à c. | de sel | Sel fin / gros sel / fleur de sel | 🟢 |
| 1 c. à c. | de sucre | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 300 ml | d'eau tiède | *implicite* | 🟢 |
| 100 ml | d'huile neutre (pour le façonnage) | Huile de tournesol / colza | 🟢 |
| 60 g | de beurre mou | Beurre doux / demi-sel | 🟢 |
| 4 c. à s. | de semoule fine (pour saupoudrer) | Semoule de blé (fine/moyenne) | 🟢 |

**Étapes**

1. **Pâte.** Mélange farine, 200 g de semoule, sel et sucre. Ajoute l'eau peu à peu et pétris 10 min : la pâte doit être très souple et élastique.
2. **Boules.** Huile tes mains et forme 10 boules de la taille d'une mandarine. Pose-les sur un plat huilé, couvre et laisse reposer 15 min.
3. **Étirement.** Sur le plan huilé, étale une boule avec les doigts en un voile très fin (on doit presque voir à travers).
4. **Pliage.** Badigeonne d'un peu de beurre, saupoudre de semoule. Plie en trois dans un sens, puis en trois dans l'autre : tu obtiens un carré de 8 cm.
5. **Cuisson.** Aplatis légèrement le carré. Cuis dans une poêle à feu moyen, 3 min par face, jusqu'à ce qu'il soit doré et croustillant.

**Astuces et sécurité**

- La pâte qui se déchire n'a pas assez reposé ou manque d'eau.
- Version farcie : avant le pliage, ajoute une cuillère d'oignon, poivron et viande hachée revenus.

**Conservation** : 2 jours sous un torchon ; 3 mois au congélateur (papier cuisson entre chaque). Réchauffe à la poêle.

**Zéro déchet** : **Huile du façonnage** → réutilise-la pour la cuisson.

**Boissons** : *sans alcool* : Thé à la menthe (recette liée)

**Techniques** : Pétrir, Étirer une pâte en voile, Feuilletage plié · **À valider au test** : Ratio farine/semoule ; temps de repos ; induction vs gaz.

---

### 2.8 Batbout (pain marocain à la poêle)

*بطبوط · batbout · Afrique du Nord › Maghreb › Maroc · Pain*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 12 | 30 min | 1 h 15 | **1 h 45** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten
- 👶 **Enfants** : ✓✓ dès 4 ans (découper les disques).

**Équipement** : Saladier, rouleau, emporte-pièce ou verre, poêle.

Des petits pains moelleux qui gonflent à la poêle et s'ouvrent comme une pita. Sans four.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 300 g | de farine de blé T55 | Farine de blé T55 | 🟢 |
| 200 g | de semoule de blé fine | Semoule de blé (fine/moyenne) | 🟢 |
| 7 g | de levure boulangère sèche | Levure boulangère sèche | 🟢 |
| 1 c. à c. | de sucre | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 1 c. à c. | de sel | Sel fin / gros sel / fleur de sel | 🟢 |
| 320 ml | d'eau tiède | *implicite* | 🟢 |

**Étapes**

1. **Pâte.** Mélange tout et pétris 10 min : la pâte doit être souple et un peu collante.
2. **Pousse.** Couvre et laisse lever 1 h.
3. **Découpe.** Étale sur 5 mm d'épaisseur sur un plan semoulé. Découpe des disques de 10 cm. Laisse lever 15 min sous un torchon.
4. **Cuisson.** Poêle à feu moyen, sans matière grasse. Cuis 2 à 3 min par face en retournant plusieurs fois : le batbout gonfle.

**Astuces et sécurité**

- Retourne souvent : c'est ce qui le fait gonfler régulièrement.

**Conservation** : 2 jours dans un sac ; 3 mois au congélateur.

**Zéro déchet** : **Chutes de pâte** → pétris-les à nouveau et fais un dernier batbout.

**Boissons** : *sans alcool* : Thé à la menthe (recette liée)

**Techniques** : Pétrir, Cuire à la poêle · **À valider au test** : Épaisseur idéale pour la poche.

---

### 2.9 Galette de sarrasin complète

*Krampouezh gwinizh du · France › Bretagne · Plat*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐⭐ | 4 | 40 min | 2 h 00 | **2 h 40** | € |

- 🐖 **Contient du porc** : Jambon blanc
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : lait, œufs
- 👶 **Enfants** : ✓✓ dès 3 ans (œuf bien cuit).

**Équipement** : Saladier, fouet, grande poêle (28 cm) ou crêpière, spatule.

La galette bretonne au sarrasin, garnie jambon, œuf, fromage. Naturellement sans blé : vérifie la farine si tu cuisines sans gluten.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 250 g | de farine de sarrasin | Farine de sarrasin | 🟢 |
| 1 | œuf (pour la pâte, facultatif) *(facultatif)* | Œuf entier (frais) | 🟢 |
| 550 ml | d'eau froide | *implicite* | 🟢 |
| 1 c. à c. | de gros sel | Sel fin / gros sel / fleur de sel | 🟢 |
| 30 g | de beurre demi-sel (cuisson) | Beurre doux / demi-sel | 🟢 |
| 4 tranches | de jambon blanc | Jambon blanc | 🟢 |
| 4 | œufs (garniture) | Œuf entier (frais) | 🟢 |
| 120 g | d'emmental râpé | Gruyère / comté / emmental / beaufort | 🟢 |

**Étapes**

1. **Pâte.** Mélange farine et sel. Ajoute l'eau petit à petit en fouettant énergiquement 5 min (et l'œuf si tu veux une pâte plus facile).
2. **Repos.** Couvre et laisse reposer 2 h au frigo (ou une nuit).
3. **Cuisson.** Poêle très chaude, beurrée. Verse 1 louche et étale vite. Cuis 2 min, jusqu'à ce que les bords se décollent.
4. **Garniture.** Sans retourner, baisse le feu. Mets le fromage, le jambon, puis casse l'œuf au centre. Couvre 2 min, jusqu'à ce que le blanc soit pris.
5. **Pliage.** Replie les 4 bords en carré en laissant le jaune visible. Ajoute un peu de beurre sur les bords et sers aussitôt.

**Astuces et sécurité**

- Pâte trop épaisse : ajoute un peu d'eau. Les galettes se déchirent : pâte pas assez reposée.

**Variantes (à tester)**

- **Sans porc** : Remplace le jambon blanc par du **jambon de dinde ou de poulet**, ou par des champignons poêlés. Substitution **à tester**. *Calcul* : porc **ok**, alcool **ok**.

**Conservation** : Galettes nature : 3 jours au frigo, 2 mois au congélateur.

**Zéro déchet** : **Reste de pâte** → galettes-saucisse (de volaille) ou chips de galette au four. **Galettes nature en trop** → roulées au chèvre-épinards le lendemain.

**Boissons** : *sans alcool* : Jus de pomme pétillant ; Lait ribot · *avec alcool (adultes)* : Cidre brut (adultes)

**Techniques** : Faire une pâte sans grumeaux, Cuire une crêpe · **À valider au test** : Avec/sans œuf dans la pâte ; poêle antiadhésive vs crêpière.

---

### 2.10 Pancakes moelleux

*Pancakes · Amérique du Nord › États-Unis · Goûter / dessert*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 4 | 25 min | 15 min | **40 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten, lait, œufs
- 👶 **Enfants** : ✓✓ dès 3 ans : mélanger, verser (adulte à la poêle).

**Équipement** : Saladier, fouet, poêle antiadhésive, louche.

Des pancakes épais et légers pour le petit-déjeuner. Le secret : ne pas trop mélanger.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 250 g | de farine de blé T45 | Farine de blé T45 | 🟢 |
| 1 sachet | de levure chimique (11 g) | Levure chimique | 🟢 |
| 2 c. à s. | de sucre | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 1 pincée | de sel | Sel fin / gros sel / fleur de sel | 🟢 |
| 2 | œufs | Œuf entier (frais) | 🟢 |
| 300 ml | de lait | Lait entier / demi-écrémé / écrémé | 🟢 |
| 40 g | de beurre fondu | Beurre doux / demi-sel | 🟢 |

**Étapes**

1. **Sec.** Mélange farine, levure, sucre et sel.
2. **Liquide.** Fouette les œufs, le lait et le beurre fondu.
3. **Mélange.** Verse le liquide sur le sec et mélange juste assez pour qu'il n'y ait plus de farine sèche : quelques grumeaux, c'est bien.
4. **Repos.** Laisse reposer 15 min.
5. **Cuisson.** Poêle à feu moyen, à peine graissée. Verse ½ louche. Retourne quand des bulles crèvent en surface (2 min), puis 1 min de l'autre côté.

**Astuces et sécurité**

- Feu trop fort = dessus brûlé et cœur cru.
- Babeurre ou lait ribot à la place du lait : encore plus moelleux.

**Conservation** : 2 jours au frigo ; 2 mois au congélateur ; réchauffe au grille-pain.

**Zéro déchet** : **Banane trop mûre** → écrasée dans la pâte. **Fond de lait ribot** → à la place du lait.

**Boissons** : *sans alcool* : Chocolat chaud ; Jus d'orange pressé

**Techniques** : Mélanger sans trop travailler · **À valider au test** : Levure 11 g vs 8 g ; repos 0 vs 15 min.

---

### 2.11 Pain de mie maison

*Pain de mie · France · Pain*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐⭐ | 12 | 30 min | 2 h 30 | **3 h 00** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten, lait
- 👶 **Enfants** : ✓✓ dès 4 ans.

**Équipement** : Moule à cake ou à pain de mie (25 cm), saladier ou robot, four.

Une mie blanche et filante, parfaite pour les croque-monsieur, les sandwichs et le pain perdu.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 500 g | de farine de blé T45 | Farine de blé T45 | 🟢 |
| 280 ml | de lait tiède | Lait entier / demi-écrémé / écrémé | 🟢 |
| 50 g | de beurre mou | Beurre doux / demi-sel | 🟢 |
| 25 g | de sucre | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 9 g | de sel | Sel fin / gros sel / fleur de sel | 🟢 |
| 7 g | de levure boulangère sèche | Levure boulangère sèche | 🟢 |

**Étapes**

1. **Pétrissage.** Mélange farine, sucre, sel, levure et lait. Pétris 10 min, ajoute le beurre en morceaux et pétris encore 5 min jusqu'à une pâte lisse et élastique.
2. **Pousse.** Couvre et laisse lever 1 h 30, jusqu'à doubler.
3. **Façonnage.** Dégaze, divise en 3 boules et place-les côte à côte dans le moule beurré.
4. **Apprêt.** Laisse lever 1 h, jusqu'à ce que la pâte dépasse le bord du moule.
5. **Cuisson.** Four préchauffé à 180 °C (th. 6), 30 à 35 min. Démoule aussitôt et laisse refroidir sur une grille.

**Astuces et sécurité**

- Pour des tranches carrées : couvre le moule d'une plaque pendant la cuisson.

**Conservation** : 4 jours dans un sac ; 3 mois au congélateur, tranché.

**Zéro déchet** : **Croûtes** → chapelure. **Pain de mie rassis** → pain perdu (recette liée).

**Techniques** : Pétrir, Façonner en boules · **À valider au test** : Moule métal vs verre ; temps de cuisson.

---

### 2.12 Brioche maison

*Brioche · France › Normandie · Goûter / dessert* · Fêtes : Pâques, Anniversaire

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐⭐ | 10 | 35 min | 10 h 00 | **10 h 35** | €€ |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten, lait, œufs
- 👶 **Enfants** : ✓✓ dès 4 ans (façonner).

**Équipement** : Robot pétrisseur conseillé (ou pétrissage à la main, 20 min), moule à cake, four.

Une brioche filante au beurre. La nuit au frigo rend la pâte facile à façonner et développe le goût.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 500 g | de farine de blé T45 | Farine de blé T45 | 🟢 |
| 5 | œufs | Œuf entier (frais) | 🟢 |
| 200 g | de beurre mou | Beurre doux / demi-sel | 🟢 |
| 60 g | de sucre | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 10 g | de sel | Sel fin / gros sel / fleur de sel | 🟢 |
| 7 g | de levure boulangère sèche | Levure boulangère sèche | 🟢 |
| 50 ml | de lait (+ 1 jaune pour dorer) | Lait entier / demi-écrémé / écrémé | 🟢 |

**Étapes**

1. **Pâte.** Pétris farine, sucre, sel, levure, œufs et lait 10 min à vitesse lente, jusqu'à ce que la pâte se décolle des parois.
2. **Beurre.** Ajoute le beurre en 4 fois et pétris encore 10 min : la pâte doit être lisse et brillante.
3. **Nuit au froid.** Couvre et mets au frigo 8 à 12 h.
4. **Façonnage.** Divise en 6 boules et range-les dans le moule beurré. Laisse lever 2 h à 25 °C.
5. **Cuisson.** Dore au jaune d'œuf battu avec 1 c. à s. de lait. Cuis 30 min à 170 °C (th. 5-6).

**Astuces et sécurité**

- Pâte trop collante au façonnage : elle est trop chaude, remets-la 30 min au frigo.

**Conservation** : 3 jours dans un sac ; 2 mois au congélateur.

**Zéro déchet** : **Blanc d'œuf restant** → meringues (recette liée). **Brioche rassie** → pain perdu.

**Boissons** : *sans alcool* : Chocolat chaud

**Techniques** : Pétrir une pâte riche, Dorer · **À valider au test** : Pétrissage à la main (temps réel) ; pousse 2 h en hiver.

---

### 2.13 Pâte brisée maison

*Pâte brisée · France · Base*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 15 min | 30 min | **45 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten, lait
- 👶 **Enfants** : ✓✓ dès 4 ans : sabler.

**Équipement** : Saladier, rouleau, moule à tarte de 26 cm.

Trois ingrédients et cinq minutes : la base de toutes les quiches et tartes salées. Moins on la travaille, plus elle est friable.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 250 g | de farine de blé T55 | Farine de blé T55 | 🟢 |
| 125 g | de beurre froid en dés | Beurre doux / demi-sel | 🟢 |
| ½ c. à c. | de sel | Sel fin / gros sel / fleur de sel | 🟢 |
| 60 ml | d'eau froide | *implicite* | 🟢 |

**Étapes**

1. **Sablage.** Frotte la farine, le sel et le beurre entre tes doigts jusqu'à obtenir un sable grossier.
2. **Eau.** Ajoute l'eau froide d'un coup et rassemble la pâte en boule sans la pétrir.
3. **Repos.** Aplatis en disque, filme et mets 30 min au frigo.
4. **Fonçage.** Étale sur 3 mm et garnis le moule. Pique le fond à la fourchette.

**Astuces et sécurité**

- Pour une cuisson « à blanc » : papier cuisson + légumes secs, 15 min à 180 °C (th. 6).

**Conservation** : 3 jours au frigo ; 3 mois au congélateur.

**Zéro déchet** : **Chutes de pâte** → sablés salés au fromage ou petits chaussons.

**Techniques** : Sabler, Foncer un moule · **À valider au test** : Beurre doux vs demi-sel ; repos 30 min vs 2 h.

---

### 2.14 Chapati (galettes de blé complet)

*चपाती · chapati · Asie du Sud › Inde · Pain*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 8 | 30 min | 20 min | **50 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten, lait
- 👶 **Enfants** : ✓✓ dès 3 ans.

**Équipement** : Saladier, rouleau, poêle.

Le pain de tous les jours en Inde et en Afrique de l'Est : farine complète, eau, sel. Sans levure, cuit en quelques minutes.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 300 g | de farine atta (ou farine T110 complète) | Farine atta (chapati) | 🟠 |
| 200 ml | d'eau tiède | *implicite* | 🟢 |
| ½ c. à c. | de sel | Sel fin / gros sel / fleur de sel | 🟢 |
| 1 c. à s. | d'huile ou de ghee | Beurre clarifié / ghee | 🟡 |

**Étapes**

1. **Pâte.** Mélange farine et sel, ajoute l'eau peu à peu et pétris 5 min jusqu'à une pâte souple. Ajoute l'huile et pétris 1 min.
2. **Repos.** Couvre 20 min.
3. **Étalage.** Divise en 8 boules et étale des disques fins de 18 cm.
4. **Cuisson.** Poêle chaude à sec : 30 s, retourne, 1 min, retourne encore en appuyant avec un torchon plié : le chapati gonfle.
5. **Service.** Badigeonne de ghee et empile sous un torchon.

**Astuces et sécurité**

- Sans farine atta : moitié T110 complète, moitié T55.

**Conservation** : 2 jours ; 2 mois au congélateur.

**Zéro déchet** : **Chapatis rassis** → coupés en lanières et sautés aux œufs et légumes (chapati sauté).

**Techniques** : Cuire à la poêle très chaude · **À valider au test** : Farine atta vs mélange T110/T55.

---

### 2.15 Tortillas de blé

*Tortillas de harina · Amérique latine & Caraïbes › Mexique · Pain*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 8 | 30 min | 30 min | **1 h 00** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten
- 👶 **Enfants** : ✓✓ dès 3 ans.

**Équipement** : Saladier, rouleau, poêle.

Des tortillas souples pour les wraps, fajitas et quesadillas, bien meilleures que celles du commerce et sans conservateurs.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 300 g | de farine de blé T55 | Farine de blé T55 | 🟢 |
| 1 c. à c. | de levure chimique | Levure chimique | 🟢 |
| 1 c. à c. | de sel | Sel fin / gros sel / fleur de sel | 🟢 |
| 50 ml | d'huile neutre | Huile de tournesol / colza | 🟢 |
| 170 ml | d'eau chaude (pas bouillante) | *implicite* | 🟢 |

**Étapes**

1. **Pâte.** Mélange farine, levure et sel. Ajoute l'huile puis l'eau chaude et pétris 3 min jusqu'à une pâte souple.
2. **Repos.** Couvre 30 min : la pâte devient facile à étaler.
3. **Étalage.** Divise en 8 boules et étale très finement (2 mm, 20 cm).
4. **Cuisson.** Poêle chaude à sec, 30 à 45 s par face : des taches dorées apparaissent.
5. **Souplesse.** Empile-les aussitôt dans un torchon pour qu'elles restent souples.

**Astuces et sécurité**

- Utilisée chez les Mexicains du nord, la graisse traditionnelle est parfois du saindoux : ici, huile neutre.

**Conservation** : 3 jours dans un sac ; 2 mois au congélateur.

**Zéro déchet** : **Tortillas rassies** → chips de tortillas au four.

**Techniques** : Cuire à la poêle très chaude · **À valider au test** : Épaisseur ; souplesse après 24 h.

---

### 2.16 Ketchup maison

*Ketchup · Amérique du Nord › États-Unis · Sauce*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 12 | 15 min | 40 min | **55 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : aucun déclaré
- 👶 **Enfants** : ✓✓ dès 2 ans.

**Équipement** : Casserole, mixeur plongeur, bocal propre.

Tomate, oignon, vinaigre, sucre et épices : un ketchup qui a vraiment le goût de la tomate, sans épaississant ni conservateur.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 800 g | de tomates pelées (ou passata) | Coulis / passata / tomates pelées | 🟢 |
| 1 | oignon jaune, haché | Oignon jaune | 🟢 |
| 1 gousse | d'ail | Ail | 🟢 |
| 70 g | de sucre roux | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 80 ml | de vinaigre de cidre | Vinaigre de cidre | 🟢 |
| 2 c. à s. | de concentré de tomate | Concentré de tomate | 🟢 |
| ½ c. à c. | de paprika doux | Paprika doux | 🟢 |
| 1 pincée | de clou de girofle moulu et de cannelle | Clou de girofle | 🟢 |
| 1 c. à c. | de sel | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Cuisson.** Mets tous les ingrédients dans une casserole. Porte à ébullition puis laisse mijoter 30 à 40 min à feu doux, en remuant souvent.
2. **Mixage.** Mixe très finement. Pour un ketchup lisse, passe-le au tamis.
3. **Réduction.** Remets sur le feu si nécessaire jusqu'à ce qu'une cuillère tracée au fond de la casserole laisse un sillon qui ne se referme pas.
4. **Bocal.** Verse chaud dans un bocal ébouillanté, ferme, laisse refroidir puis mets au frigo.

**Astuces et sécurité**

- Le vinaigre de cidre ne contient pas de traces d'alcool de vin : il convient au profil « sans alcool strict ».

**Conservation** : 3 semaines au frigo, bocal fermé (acidité + sucre). Congélation : 6 mois en petites portions.

**Zéro déchet** : **Fond de bocal** → déglace-le avec un peu d'eau dans une sauce bolognaise.

**Techniques** : Réduire une sauce · **À valider au test** : Temps de réduction ; tenue au frigo (observation).

---

### 2.17 Sauce samouraï maison

*Sauce samouraï · France · Sauce*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 5 min | 15 min | **20 min** | € |

- ✅ Sans porc (calculé)
- 🟡 **Traces d'alcool possibles** : Moutarde de Dijon
- ⚠️ **Allergènes** : moutarde, œufs ; **possibles selon marque** : sulfites
- 👶 **Enfants** : Trop piquante pour les petits ; version sans harissa = sauce cocktail.

**Équipement** : Bol, cuillère.

La sauce piquante des snacks : mayonnaise, ketchup et harissa. Prête en 5 minutes.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 150 g | de mayonnaise maison (recette liée) | *sous-recette : Mayonnaise maison* | – |
| 2 c. à s. | de ketchup maison (recette liée) | *sous-recette : Ketchup maison* | – |
| 1 à 2 c. à c. | de harissa maison (recette liée) | *sous-recette : Harissa maison* | – |
| ½ c. à c. | de jus de citron | Citron | 🟢 |

**Étapes**

1. **Mélange.** Mélange la mayonnaise, le ketchup et la harissa.
2. **Réglage.** Goûte : ajoute la harissa par petites quantités, elle se renforce au repos.
3. **Repos.** 15 min au frigo avant de servir.

**Astuces et sécurité**

- Plus douce : remplace la moitié de la mayonnaise par du yaourt grec.

**Conservation** : 3 jours au frigo (mayonnaise à l'œuf cru).

**Zéro déchet** : **Restes** → dans un wrap ou une marinade de poulet.

**Techniques** : Assaisonner une sauce · **À valider au test** : Dosage de harissa.

---

### 2.18 Sauce blanche (kebab, grillades)

*Sauce blanche · France · Sauce*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 5 min | 30 min | **35 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : lait
- 👶 **Enfants** : ✓✓ dès 2 ans (peu d'ail).

**Équipement** : Bol, cuillère.

La sauce du kebab, sans œuf cru : yaourt, ail, citron et herbes. Légère et fraîche.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 250 g | de yaourt grec | Yaourt grec | 🟢 |
| 1 gousse | d'ail pressée | Ail | 🟢 |
| 1 c. à s. | de jus de citron | Citron | 🟢 |
| 1 c. à s. | d'huile d'olive | Huile d'olive vierge extra | 🟢 |
| 1 c. à s. | de ciboulette ou de persil ciselé | Ciboulette | 🟢 |
| ½ c. à c. | de menthe séchée (facultatif) *(facultatif)* | Menthe | 🟢 |
| 1 pincée | de sel et de poivre | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Mélange.** Mélange tous les ingrédients.
2. **Repos.** 30 min au frigo : l'ail se diffuse.

**Astuces et sécurité**

- Plus onctueuse : ajoute 1 c. à s. de mayonnaise maison.
- Sans lactose : remplace le yaourt par du tahini dilué au citron et à l'eau.

**Conservation** : 4 jours au frigo.

**Zéro déchet** : **Tiges d'herbes** → hache-les finement dans la sauce.

**Techniques** : Ciseler les herbes · **À valider au test** : Yaourt grec vs fromage blanc.

---

### 2.19 Sauce burger maison

*Burger sauce · Amérique du Nord › États-Unis · Sauce*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 5 min | 15 min | **20 min** | € |

- ✅ Sans porc (calculé)
- 🟡 **Traces d'alcool possibles** : Moutarde de Dijon, Moutarde de Dijon, Cornichon
- ⚠️ **Allergènes** : moutarde, œufs ; **possibles selon marque** : sulfites
- 👶 **Enfants** : ✓ dès 3 ans (mayonnaise pasteurisée ou sans œuf).

**Équipement** : Bol, couteau.

La sauce des burgers de fast-food, à la maison : mayonnaise, ketchup, moutarde et cornichons.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 120 g | de mayonnaise maison (recette liée) | *sous-recette : Mayonnaise maison* | – |
| 1 c. à s. | de ketchup maison (recette liée) | *sous-recette : Ketchup maison* | – |
| 1 c. à c. | de moutarde | Moutarde de Dijon | 🟢 |
| 2 | cornichons hachés finement | Cornichon | 🟢 |
| 1 c. à s. | d'oignon haché très fin | Oignon jaune | 🟢 |
| ½ c. à c. | de paprika doux | Paprika doux | 🟢 |

**Étapes**

1. **Hachage.** Hache très finement les cornichons et l'oignon.
2. **Mélange.** Mélange avec le reste.
3. **Repos.** 15 min au frigo.

**Astuces et sécurité**

- Profil sans alcool strict : les cornichons et la moutarde au vinaigre de vin portent des traces ; utilise des cornichons au vinaigre de cidre ou du concombre + vinaigre de cidre.

**Variantes (à tester)**

- **Sans traces d'alcool (profil Strict)** : Cornichons → **concombre en petits dés + 1 c. à c. de vinaigre de cidre** ; moutarde → **graines de moutarde écrasées + vinaigre de cidre**. **À tester**. *Calcul* : porc **ok**, alcool **trace**.

**Conservation** : 3 jours au frigo.

**Zéro déchet** : **Jus de cornichons** → vinaigrette ou marinade.

**Techniques** : Hacher finement · **À valider au test** : Proportion cornichon/oignon.

---

### 2.20 Sauce barbecue maison

*Barbecue sauce · Amérique du Nord › États-Unis · Sauce*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 10 | 10 min | 20 min | **30 min** | € |

- ✅ Sans porc (calculé)
- 🟡 **Traces d'alcool possibles** : Moutarde de Dijon
- ⚠️ **Allergènes** : moutarde, poissons ; **possibles selon marque** : gluten, sulfites
- 👶 **Enfants** : ✓ dès 3 ans (miel : jamais avant 1 an).

**Équipement** : Casserole, fouet, bocal.

Sucrée, fumée, acidulée : pour les grillades, les ribs de bœuf et les burgers.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 200 g | de ketchup maison (recette liée) | *sous-recette : Ketchup maison* | – |
| 50 g | de sucre muscovado (ou cassonade) | Sucre muscovado | 🟡 |
| 3 c. à s. | de vinaigre de cidre | Vinaigre de cidre | 🟢 |
| 1 c. à s. | de miel | Miel | 🟢 |
| 2 c. à c. | de paprika fumé | Paprika fumé (pimentón) | 🟢 |
| 1 c. à c. | de moutarde | Moutarde de Dijon | 🟢 |
| 1 c. à c. | de poudre d'ail | Poudre d'ail / d'oignon | 🟢 |
| 1 c. à c. | de sauce Worcestershire (facultatif) *(facultatif)* | Sauce Worcestershire | 🟢 |
| 50 ml | d'eau | *implicite* | 🟢 |

**Étapes**

1. **Mélange.** Mets tout dans une casserole et fouette.
2. **Cuisson.** Laisse frémir 15 à 20 min à feu doux, en remuant, jusqu'à ce que la sauce nappe la cuillère.
3. **Bocal.** Verse dans un bocal propre. Elle épaissit en refroidissant.

**Astuces et sécurité**

- Pas de fumée liquide : le paprika fumé donne le goût de feu de bois.
- La Worcestershire contient de l'anchois (poisson) : retire-la pour une sauce sans poisson.

**Conservation** : 2 semaines au frigo.

**Zéro déchet** : **Fond de bocal** → marinade de poulet.

**Techniques** : Réduire une sauce · **À valider au test** : Muscovado vs cassonade ; tenue au frigo.

---

### 2.21 Sauce andalouse maison

*Sauce andalouse · Europe du Nord & Centrale › Belgique · Sauce*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 10 min | 15 min | **25 min** | € |

- ✅ Sans porc (calculé)
- 🟡 **Traces d'alcool possibles** : Moutarde de Dijon
- ⚠️ **Allergènes** : moutarde, œufs ; **possibles selon marque** : sulfites
- 👶 **Enfants** : ✓ dès 3 ans (mayonnaise pasteurisée ou sans œuf).

**Équipement** : Bol, mixeur plongeur.

La sauce des friteries belges : mayonnaise, tomate et poivron grillé. Douce et parfumée.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 150 g | de mayonnaise maison (recette liée) | *sous-recette : Mayonnaise maison* | – |
| 1 c. à s. | de concentré de tomate | Concentré de tomate | 🟢 |
| ½ | poivron rouge grillé et pelé | Poivron (rouge/jaune/vert) | 🟢 |
| 1 c. à c. | de jus de citron | Citron | 🟢 |
| 1 pincée | de piment d'Espelette | Piment d'Espelette | 🟢 |

**Étapes**

1. **Poivron.** Grille le demi-poivron sous le gril du four 15 min, jusqu'à ce que la peau noircisse. Enferme-le 10 min dans un bol couvert, puis pèle-le.
2. **Mixage.** Mixe le poivron avec le concentré et le citron.
3. **Mélange.** Incorpore à la mayonnaise. 15 min au frigo.

**Astuces et sécurité**

- Grille un poivron entier et garde le reste dans l'huile pour une salade.

**Conservation** : 3 jours au frigo.

**Zéro déchet** : **Reste de poivron grillé** → salade, pizza, houmous au poivron.

**Techniques** : Griller et peler un poivron · **À valider au test** : Poivron grillé maison vs bocal.

---

### 2.22 Harissa maison

*هريسة · harissa · Afrique du Nord › Maghreb › Tunisie · Sauce*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 12 | 20 min | 30 min | **50 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : aucun déclaré
- 👶 **Enfants** : Trop piquante pour les enfants.

**Équipement** : Bol, mixeur ou mortier, poêle, petit bocal.

La pâte de piments tunisienne : piments séchés, ail, carvi, coriandre et huile d'olive. Rien d'autre.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 40 g | de piments rouges séchés (type guajillo, ou piments forts) | Piments ancho / chipotle / guajillo / pasilla | 🟠 |
| 3 gousses | d'ail | Ail | 🟢 |
| 1 c. à c. | de graines de carvi | Carvi / fenouil / anis vert (graines) | 🟡 |
| 1 c. à c. | de graines de coriandre | Coriandre (graines) | 🟢 |
| ½ c. à c. | de cumin | Cumin (graines / moulu) | 🟢 |
| 1 c. à c. | de sel | Sel fin / gros sel / fleur de sel | 🟢 |
| 1 c. à s. | de jus de citron | Citron | 🟢 |
| 4 c. à s. | d'huile d'olive (+ pour couvrir) | Huile d'olive vierge extra | 🟢 |

**Étapes**

1. **Réhydratation.** Retire les queues et les graines des piments (gants conseillés). Couvre d'eau chaude 30 min.
2. **Épices.** Fais griller à sec carvi, coriandre et cumin 1 min, puis moud-les.
3. **Mixage.** Égoutte les piments et mixe-les avec l'ail, les épices, le sel, le citron et l'huile jusqu'à une pâte.
4. **Bocal.** Mets en bocal propre et couvre d'une fine couche d'huile.

**Astuces et sécurité**

- ⚠️ Ne te touche pas les yeux après avoir manipulé les piments ; lave-toi les mains.
- Plus douce : mélange piments forts et piments doux.

**Conservation** : 3 semaines au frigo, toujours recouverte d'huile.

**Zéro déchet** : **Eau de trempage des piments** → dans une soupe ou un bouillon (elle est piquante).

**Techniques** : Torréfier les épices, Moudre · **À valider au test** : Variétés de piments disponibles en France ; piquant selon le lot.

---

### 2.23 Pesto au basilic (ou aux fanes)

*Pesto alla genovese · Europe du Sud › Italie › Ligurie · Sauce*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 10 min | 0 min | **10 min** | €€ |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : lait
- 👶 **Enfants** : ✓✓ dès 3 ans (fruits à coque mixés).

**Équipement** : Mixeur ou mortier.

Basilic, pignons, parmesan, ail et huile d'olive. La version aux fanes de carottes ou de radis évite de les jeter.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 50 g | de feuilles de basilic (ou de fanes) | Basilic | 🟢 |
| 30 g | de pignons de pin | Pignons de pin | 🟢 |
| 50 g | de parmesan râpé | Parmesan / Parmigiano | 🟢 |
| 1 gousse | d'ail | Ail | 🟢 |
| 100 ml | d'huile d'olive | Huile d'olive vierge extra | 🟢 |
| 1 pincée | de sel | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Pignons.** Fais-les dorer à sec 2 min dans une poêle.
2. **Mixage.** Mixe basilic, pignons, ail et sel par à-coups, en ajoutant l'huile en filet.
3. **Fromage.** Ajoute le parmesan et mélange à la cuillère.
4. **Conservation.** Mets en bocal et couvre d'huile.

**Astuces et sécurité**

- Mixer par à-coups évite de chauffer le basilic (il noircit).
- Pignons trop chers : noix de cajou ou graines de tournesol.
- Le parmesan est fait avec de la présure animale (veau) : non végétarien strict.

**Conservation** : 5 jours au frigo sous une couche d'huile ; 3 mois au congélateur en bacs à glaçons.

**Zéro déchet** : **Fanes de carottes ou de radis**, **tiges de basilic** → dans le pesto. **Croûte du parmesan** → dans une soupe.

**Techniques** : Torréfier, Émulsionner au mixeur · **À valider au test** : Pesto de fanes : amertume selon les fanes.

---

### 2.24 Sauce tomate maison

*Salsa di pomodoro · Europe du Sud › Italie · Sauce*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 10 min | 30 min | **40 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : aucun déclaré
- 👶 **Enfants** : ✓✓ dès 1 an (sans sel ajouté avant 1 an).

**Équipement** : Sauteuse ou casserole.

La sauce de base des pâtes, des pizzas et des boulettes. Une boîte de tomates pelées de bonne qualité suffit.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 800 g | de tomates pelées | Coulis / passata / tomates pelées | 🟢 |
| 3 c. à s. | d'huile d'olive | Huile d'olive vierge extra | 🟢 |
| 1 | oignon jaune, haché | Oignon jaune | 🟢 |
| 2 gousses | d'ail, émincées | Ail | 🟢 |
| quelques feuilles | de basilic | Basilic | 🟢 |
| 1 pincée | de sucre (si les tomates sont acides) *(facultatif)* | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 1 c. à c. | de sel | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Oignon.** Fais fondre l'oignon dans l'huile 8 min à feu doux, sans coloration. Ajoute l'ail 1 min.
2. **Tomates.** Ajoute les tomates écrasées, le sel et les tiges de basilic.
3. **Mijotage.** Laisse mijoter 25 à 30 min à feu doux, à demi-couvert.
4. **Finition.** Retire les tiges, ajoute les feuilles de basilic, ajuste le sel.

**Astuces et sécurité**

- Mixée, elle sert de base à pizza ; avec des légumes rôtis, elle fait une sauce de pâtes complète.

**Conservation** : 5 jours au frigo ; 6 mois au congélateur.

**Zéro déchet** : **Tomates trop mûres** → à la place des pelées. **Croûte de parmesan** → à faire mijoter dans la sauce.

**Techniques** : Faire suer, Mijoter · **À valider au test** : Tomates pelées de marques différentes.

---

### 2.25 Béchamel

*Sauce béchamel · France · Sauce*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 15 min | 0 min | **15 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten, lait
- 👶 **Enfants** : ✓✓ dès 1 an.

**Équipement** : Casserole, fouet.

Beurre, farine, lait : la base des gratins, lasagnes, croque-monsieur et de la sauce fromagère pour frites.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 40 g | de beurre | Beurre doux / demi-sel | 🟢 |
| 40 g | de farine de blé T55 | Farine de blé T55 | 🟢 |
| 500 ml | de lait | Lait entier / demi-écrémé / écrémé | 🟢 |
| 1 pincée | de noix de muscade | Noix de muscade | 🟢 |
| 1 pincée | de sel et poivre | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Roux.** Fais fondre le beurre, ajoute la farine et remue 2 min à feu moyen, sans coloration.
2. **Lait.** Hors du feu, verse le lait froid d'un coup et fouette.
3. **Cuisson.** Remets sur feu moyen et fouette sans arrêt jusqu'à l'ébullition, puis 2 min de plus.
4. **Assaisonnement.** Sel, poivre, muscade.

**Astuces et sécurité**

- Roux chaud + lait froid (ou l'inverse) = pas de grumeaux.
- **Sauce fromagère** : ajoute 80 g de cheddar ou d'emmental râpé hors du feu.

**Conservation** : 3 jours au frigo, film au contact.

**Zéro déchet** : **Fromages secs** → râpés dans la sauce fromagère.

**Techniques** : Faire un roux, Lier une sauce · **À valider au test** : Lait entier vs demi-écrémé.

---

### 2.26 Vinaigrette de base (et variantes)

*Vinaigrette · France · Sauce*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 5 min | 0 min | **5 min** | € |

- ✅ Sans porc (calculé)
- 🟡 **Traces d'alcool possibles** : Moutarde de Dijon
- ⚠️ **Allergènes** : moutarde ; **possibles selon marque** : sulfites
- 👶 **Enfants** : ✓✓ dès 2 ans.

**Équipement** : Bocal à couvercle.

Une part d'acide, trois parts d'huile, un peu de moutarde : la règle à retenir pour toutes les salades.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 1 c. à s. | de vinaigre de cidre (ou jus de citron) | Vinaigre de cidre | 🟢 |
| 1 c. à c. | de moutarde | Moutarde de Dijon | 🟢 |
| 3 c. à s. | d'huile (olive, colza, noix) | Huile de tournesol / colza | 🟢 |
| 1 pincée | de sel et poivre | Sel fin / gros sel / fleur de sel | 🟢 |
| 1 | échalote ciselée (facultatif) *(facultatif)* | Échalote | 🟢 |

**Étapes**

1. **Sel.** Dans le bocal, dissous le sel dans le vinaigre (le sel ne fond pas dans l'huile).
2. **Moutarde.** Ajoute la moutarde et le poivre.
3. **Huile.** Ajoute l'huile, ferme et secoue 10 s.

**Astuces et sécurité**

- Miel-citron : citron + 1 c. à c. de miel. Yaourt-herbes : 2 c. à s. de yaourt + ciboulette. Tahini-citron : tahini + citron + eau.

**Conservation** : 1 semaine au frigo (sans échalote) ; 2 jours avec échalote.

**Zéro déchet** : **Fond de pot de moutarde** → fais la vinaigrette directement dedans.

**Techniques** : Émulsionner · **À valider au test** : Ratio 1:3 selon les huiles.

---

### 2.27 Tzatziki

*Τζατζίκι · tzatzíki · Europe du Sud › Grèce · Sauce*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 15 min | 30 min | **45 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : lait
- 👶 **Enfants** : ✓✓ dès 2 ans (peu d'ail).

**Équipement** : Râpe, torchon propre ou passoire fine, bol.

Yaourt grec, concombre râpé bien essoré, ail et aneth. À l'apéritif ou avec des grillades.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 400 g | de yaourt grec | Yaourt grec | 🟢 |
| 1 | concombre | Concombre | 🟢 |
| 1 gousse | d'ail pressée | Ail | 🟢 |
| 1 c. à s. | d'aneth ou de menthe ciselée | Aneth | 🟢 |
| 1 c. à s. | d'huile d'olive | Huile d'olive vierge extra | 🟢 |
| 1 c. à c. | de jus de citron | Citron | 🟢 |
| 1 pincée | de sel | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Concombre.** Râpe-le avec la peau, sale-le et laisse dégorger 10 min. Essore-le fort dans un torchon.
2. **Mélange.** Mélange avec le yaourt, l'ail, l'herbe, l'huile et le citron.
3. **Repos.** 30 min au frigo.

**Astuces et sécurité**

- Si tu n'essores pas le concombre, le tzatziki devient liquide.

**Conservation** : 3 jours au frigo.

**Zéro déchet** : **Jus du concombre** → dans une citronnade ou un smoothie.

**Techniques** : Dégorger un légume · **À valider au test** : Temps de dégorgement.

---

### 2.28 Frites maison (double cuisson, four ou airfryer)

*Frites · Europe du Nord & Centrale › Belgique · Accompagnement*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐⭐ | 4 | 30 min | 30 min | **1 h 00** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : aucun déclaré
- 👶 **Enfants** : ✓ dès 3 ans en version four ; la friture reste pour les adultes.

**Équipement** : Casserole profonde ou friteuse avec thermomètre, OU four, OU airfryer ; écumoire ; papier absorbant.

Croustillantes dehors, fondantes dedans : le trempage et la double cuisson font tout. Version four ou airfryer pour moins d'huile.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 1 kg | de pommes de terre (Bintje ou Agria) | Pomme de terre | 🟢 |
| 1,5 L | d'huile de tournesol ou d'arachide (friture) — ou 2 c. à s. pour le four | Huile de tournesol / colza | 🟢 |
| 1 c. à c. | de sel fin | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Taille.** Épluche et coupe en bâtonnets de 1 cm.
2. **Trempage.** Rince et laisse tremper 30 min dans l'eau froide (retire l'amidon). Sèche-les très bien dans un torchon.
3. **1re cuisson.** ⚠️ Huile à 150 °C, jamais plus de 2/3 de la casserole, couvercle à portée de main, enfants éloignés. Cuis par petites quantités 6 à 7 min : les frites sont cuites mais pâles. Égoutte.
4. **2e cuisson.** Monte l'huile à 180 °C. Replonge 2 à 3 min jusqu'à ce qu'elles soient dorées.
5. **Sel.** Égoutte sur papier absorbant et sale aussitôt.
6. **Version four.** Après trempage et séchage : 2 c. à s. d'huile, une seule couche sur la plaque, 220 °C (th. 7-8), 35 à 40 min en retournant à mi-cuisson.
7. **Version airfryer.** 1 c. à s. d'huile, 200 °C, 20 à 25 min en secouant 3 fois.

**Astuces et sécurité**

- ⚠️ **Feu d'huile** : jamais d'eau. Coupe le feu et couvre avec le couvercle ou un linge humide.
- Bintje = la plus belge ; Agria = plus dorée.

**Conservation** : À manger aussitôt. Frites précuites (1re cuisson) : 2 mois au congélateur.

**Zéro déchet** : **Épluchures** → chips au four (huile, sel, 200 °C, 15 min). **Huile de friture** → filtre-la une fois refroidie ; réutilisable 5 à 6 fois si elle reste claire. Ne jamais la jeter à l'évier (déchetterie).

**Techniques** : Frire en sécurité, Double cuisson · **À valider au test** : Bintje vs Agria ; four statique vs ventilé ; airfryer de 3 marques.

---

### 2.29 Bouillon de volaille avec la carcasse

*Bouillon de volaille · France · Base*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 8 | 15 min | 2 h 30 | **2 h 45** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : céleri
- 👶 **Enfants** : ✓✓ dès 1 an (sans sel).

**Équipement** : Grande casserole ou cocotte, passoire fine.

La carcasse du poulet rôti, les épluchures de légumes et de l'eau : un bouillon maison qui remplace les cubes industriels (souvent à base de graisse de porc ou d'exhausteurs).

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 1 | carcasse de poulet rôti (et les os) | Poulet entier | 🟢 |
| 2 L | d'eau froide | *implicite* | 🟢 |
| 1 | oignon coupé en deux (avec la peau) | Oignon jaune | 🟢 |
| 1 | carotte (ou ses épluchures) | Carotte | 🟢 |
| 1 | vert de poireau | Poireau | 🟢 |
| 1 branche | de céleri ou ses feuilles | Céleri-branche | 🟢 |
| 1 | bouquet garni (thym, laurier, tiges de persil) | Laurier | 🟢 |
| 5 | grains de poivre | Poivre noir / blanc / vert | 🟢 |

**Étapes**

1. **Départ à froid.** Mets la carcasse cassée en morceaux dans la casserole et couvre d'eau froide.
2. **Écume.** Porte à frémissement et retire l'écume grise qui monte, pendant 10 min.
3. **Légumes.** Ajoute les légumes, le bouquet garni et le poivre. Pas de sel : tu saleras le plat final.
4. **Frémissement.** Laisse frémir 2 h, sans bouillir fort (un bouillon qui bout devient trouble).
5. **Filtrage.** Filtre à la passoire fine. Laisse refroidir, mets au frigo : le gras figé se retire à la cuillère.

**Astuces et sécurité**

- La peau de l'oignon colore le bouillon en doré.
- Garde un sac de congélation pour les épluchures propres de la semaine : il servira au prochain bouillon.

**Conservation** : 4 jours au frigo ; 6 mois au congélateur (en bacs à glaçons pour les petites quantités).

**Zéro déchet** : **Carcasse, épluchures, verts de poireau, tiges d'herbes** → c'est tout l'objet de cette recette. **Gras retiré** → pour faire revenir des pommes de terre.

**Techniques** : Écumer, Faire un bouillon · **À valider au test** : Durée 2 h vs 3 h ; rendement en litres.

---

### 2.30 Bouillon d'épluchures de légumes

*Bouillon de légumes · France · Base*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 10 min | 45 min | **55 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : aucun déclaré
- 👶 **Enfants** : ✓✓ dès 1 an.

**Équipement** : Casserole, passoire.

Les épluchures propres, les fanes, les tiges et les fonds de légumes de la semaine deviennent un bouillon parfumé, gratuit.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 500 g | d'épluchures et parures de légumes propres (carotte, poireau, oignon, céleri, champignons…) | Carotte | 🟢 |
| 1,5 L | d'eau | *implicite* | 🟢 |
| 1 | feuille de laurier | Laurier | 🟢 |
| 1 branche | de thym | Thym / romarin | 🟢 |
| 5 | grains de poivre | Poivre noir / blanc / vert | 🟢 |

**Étapes**

1. **Lavage.** Utilise des épluchures de légumes bien lavés avant épluchage (bio de préférence).
2. **Cuisson.** Couvre d'eau froide, ajoute les aromates et porte à frémissement 45 min.
3. **Filtrage.** Filtre et presse les légumes pour récupérer tout le jus.

**Astuces et sécurité**

- À éviter : épluchures de pommes de terre (amer, trouble), chou en grande quantité (odeur forte).

**Conservation** : 4 jours au frigo ; 6 mois au congélateur.

**Zéro déchet** : **Légumes cuits filtrés** → compost.

**Techniques** : Faire un bouillon · **À valider au test** : Ratio épluchures/eau ; amertume selon les légumes.

---

### 2.31 Mafé de poulet

*Maafe · tigadèguèna · Afrique subsaharienne › Afrique de l'Ouest › Mali / Sénégal · Plat* · Fêtes : Repas de famille

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐⭐ | 6 | 30 min | 1 h 00 | **1 h 30** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : arachide
- 👶 **Enfants** : ✓✓ dès 2 ans sans le piment (arachide : vérifier les allergies).

**Équipement** : Cocotte ou faitout avec couvercle, casserole pour le riz.

Le ragoût d'Afrique de l'Ouest à la pâte d'arachide : une sauce épaisse et douce, des légumes fondants, du poulet. Servi avec du riz blanc.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 1,2 kg | de cuisses de poulet en morceaux | Cuisse / pilon de poulet | 🟢 |
| 150 g | de pâte d'arachide (ou beurre de cacahuète sans sucre) | Pâte d'arachide | 🟡 |
| 2 | oignons jaunes, émincés | Oignon jaune | 🟢 |
| 3 c. à s. | de concentré de tomate | Concentré de tomate | 🟢 |
| 400 g | de tomates pelées | Coulis / passata / tomates pelées | 🟢 |
| 3 | carottes en tronçons | Carotte | 🟢 |
| 1 | patate douce en cubes | Patate douce | 🟢 |
| ¼ | de chou blanc en quartiers (facultatif) *(facultatif)* | Chou blanc / rouge | 🟢 |
| 3 gousses | d'ail | Ail | 🟢 |
| 1 morceau | de gingembre frais (3 cm) | Gingembre frais | 🟢 |
| 1 | piment antillais entier (facultatif, ne pas le percer) *(facultatif)* | Piment antillais / scotch bonnet | 🟠 |
| 3 c. à s. | d'huile d'arachide | Huile d'arachide | 🟢 |
| 1 L | d'eau | *implicite* | 🟢 |
| 1 c. à c. | de sel | Sel fin / gros sel / fleur de sel | 🟢 |
| 400 g | de riz long | Riz long / basmati / thaï | 🟢 |

**Étapes**

1. **Saisie.** Dans la cocotte, fais dorer le poulet salé dans l'huile 8 min. Réserve.
2. **Base.** Fais revenir les oignons 5 min. Ajoute l'ail et le gingembre écrasés, puis le concentré de tomate : remue 3 min pour enlever son acidité.
3. **Sauce.** Ajoute les tomates pelées et l'eau. Délaye la pâte d'arachide dans une louche de ce bouillon chaud, puis verse-la dans la cocotte.
4. **Mijotage.** Remets le poulet, ajoute carottes, patate douce, chou et piment entier. Couvre et laisse mijoter 50 à 60 min à feu doux, en remuant souvent (la pâte d'arachide accroche).
5. **Huile.** La sauce est prête quand une fine couche d'huile remonte en surface et que les légumes sont fondants.
6. **Riz.** Pendant ce temps, cuis le riz. Sers le mafé sur le riz.

**Astuces et sécurité**

- ⚠️ Arachide : allergène majeur, préviens tes invités.
- Une sauce trop épaisse : un peu d'eau. Trop liquide : 10 min à découvert.

**Conservation** : 3 jours au frigo ; 3 mois au congélateur. Encore meilleur le lendemain.

**Zéro déchet** : **Épluchures de carottes** → bouillon d'épluchures (recette liée). **Reste de sauce** → avec des pâtes ou des œufs durs.

**Boissons** : *sans alcool* : Bissap (recette liée) ; Jus de gingembre (recette liée) · *avec alcool (adultes)* : Bière blonde légère (adultes)

**Techniques** : Saisir, Mijoter · **À valider au test** : Pâte d'arachide vs beurre de cacahuète ; temps d'apparition de l'huile.

---

### 2.32 Chorba frik (soupe du Ramadan)

*شربة فريك · chorba frik · Afrique du Nord › Maghreb › Algérie · Entrée* · Fêtes : Ramadan / Aïd

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐⭐ | 6 | 30 min | 1 h 15 | **1 h 45** | €€ |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : céleri, gluten
- 👶 **Enfants** : ✓✓ dès 1 an (mixée).

**Équipement** : Faitout ou cocotte.

La soupe qui rompt le jeûne en Algérie : agneau, tomate, herbes fraîches et blé vert concassé (frik). Avec du vermicelle si tu n'as pas de frik.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 400 g | d'épaule d'agneau en petits cubes | Épaule d'agneau | 🟢 |
| 1 | oignon jaune, râpé | Oignon jaune | 🟢 |
| 2 c. à s. | de concentré de tomate | Concentré de tomate | 🟢 |
| 2 | tomates râpées | Tomate | 🟢 |
| 1 branche | de céleri, émincée | Céleri-branche | 🟢 |
| 100 g | de pois chiches trempés la veille (ou en bocal) | Pois chiches (secs / bocal) | 🟢 |
| 80 g | de frik (blé vert concassé) ou de vermicelles | Freekeh | 🟠 |
| 1 bouquet | de coriandre ciselée | Coriandre fraîche | 🟢 |
| 1 c. à s. | de menthe séchée | Menthe | 🟢 |
| 1 c. à c. | de paprika doux | Paprika doux | 🟢 |
| ½ c. à c. | de cannelle | Cannelle (bâton / poudre) | 🟢 |
| 3 c. à s. | d'huile d'olive | Huile d'olive vierge extra | 🟢 |
| 2 L | d'eau | *implicite* | 🟢 |
| 1 c. à c. | de sel, poivre | Sel fin / gros sel / fleur de sel | 🟢 |
| 1 | citron (pour servir) | Citron | 🟢 |

**Étapes**

1. **Viande.** Fais revenir l'agneau, l'oignon et l'huile 5 min avec le sel, le poivre, le paprika et la cannelle.
2. **Tomate.** Ajoute le concentré, les tomates râpées et le céleri, 3 min.
3. **Bouillon.** Verse l'eau, ajoute les pois chiches et la moitié de la coriandre. Laisse mijoter 50 min à couvert.
4. **Frik.** Ajoute le frik rincé (ou les vermicelles) et cuis 20 min de plus (10 min pour les vermicelles), en remuant.
5. **Finition.** Ajoute la menthe et le reste de coriandre. Sers avec un quartier de citron.

**Astuces et sécurité**

- Le frik se trouve en épicerie orientale ; le boulgour fin est un bon remplaçant.

**Conservation** : 3 jours au frigo ; 3 mois au congélateur (sans le frik, à ajouter au réchauffage).

**Zéro déchet** : **Tiges de coriandre** → dans le bouillon dès le début. **Eau de cuisson des pois chiches** → aquafaba (mayonnaise sans œuf).

**Boissons** : *sans alcool* : Lben ou lait ribot ; Thé à la menthe (recette liée)

**Techniques** : Mijoter · **À valider au test** : Frik vs vermicelles vs boulgour ; temps de cuisson du frik.

---

### 2.33 Salade de carottes au cumin et à l'orange

*سلاطة خيزو · slata khizou · Afrique du Nord › Maghreb › Maroc · Entrée*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 4 | 15 min | 30 min | **45 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : aucun déclaré
- 👶 **Enfants** : ✓✓ dès 1 an.

**Équipement** : Casserole, saladier.

Une entrée marocaine fraîche et parfumée : carottes juste cuites, cumin, orange, persil.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 600 g | de carottes | Carotte | 🟢 |
| 1 | orange (jus et zeste) | Orange | 🟢 |
| 1 c. à c. | de cumin moulu | Cumin (graines / moulu) | 🟢 |
| 1 gousse | d'ail | Ail | 🟢 |
| 3 c. à s. | d'huile d'olive | Huile d'olive vierge extra | 🟢 |
| 1 c. à s. | de jus de citron | Citron | 🟢 |
| ½ bouquet | de persil plat | Persil plat / frisé | 🟢 |
| 1 pincée | de sel | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Cuisson.** Cuis les carottes en rondelles 8 min à l'eau salée avec la gousse d'ail : elles doivent rester un peu fermes.
2. **Assaisonnement.** Égoutte, écrase l'ail cuit et mélange-le avec le cumin, l'huile, le jus d'orange, le zeste et le citron.
3. **Repos.** Verse sur les carottes tièdes et laisse reposer 30 min. Ajoute le persil au moment de servir.

**Astuces et sécurité**

- Version crue : carottes râpées, même assaisonnement.

**Conservation** : 3 jours au frigo.

**Zéro déchet** : **Fanes de carottes** → pesto (recette liée). **Peau d'orange** → zestes séchés ou écorces confites.

**Boissons** : *sans alcool* : Thé à la menthe (recette liée)

**Techniques** : Cuire à l'anglaise · **À valider au test** : Cuisson 8 min vs 10 min.

---

### 2.34 Houmous

*حمص بطحينة · hummus bi tahina · Moyen-Orient & Caucase › Levant › Liban · Entrée* · Fêtes : Apéritif dînatoire

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 15 min | 0 min | **15 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : sésame
- 👶 **Enfants** : ✓✓ dès 1 an (sésame : vérifier les allergies).

**Équipement** : Mixeur.

Pois chiches, tahini, citron, ail : la crème la plus célèbre du Levant. Le secret du houmous très lisse : des pois chiches bien cuits, encore tièdes.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 400 g | de pois chiches cuits (1 bocal égoutté) | Pois chiches (secs / bocal) | 🟢 |
| 80 g | de tahini (purée de sésame) | Tahini (purée de sésame) | 🟡 |
| 1 | citron (jus) | Citron | 🟢 |
| 1 gousse | d'ail | Ail | 🟢 |
| ½ c. à c. | de cumin | Cumin (graines / moulu) | 🟢 |
| 3 à 5 c. à s. | d'eau glacée | *implicite* | 🟢 |
| 2 c. à s. | d'huile d'olive (pour servir) | Huile d'olive vierge extra | 🟢 |
| 1 pincée | de paprika | Paprika doux | 🟢 |
| ½ c. à c. | de sel | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Pois chiches.** Réchauffe les pois chiches 5 min dans leur eau (ils se mixent mieux tièdes).
2. **Tahini.** Mixe d'abord le tahini, le citron, l'ail et le sel 1 min : ça devient pâle et épais.
3. **Mixage.** Ajoute les pois chiches égouttés et le cumin. Mixe 3 min en ajoutant l'eau glacée cuillère par cuillère jusqu'à une crème lisse.
4. **Service.** Étale dans une assiette creuse, creuse un sillon, verse l'huile et saupoudre de paprika.

**Astuces et sécurité**

- Pour encore plus lisse : retire les peaux des pois chiches en les frottant dans un torchon.
- ⚠️ Sésame : allergène.

**Conservation** : 4 jours au frigo.

**Zéro déchet** : **Jus du bocal (aquafaba)** → mayonnaise sans œuf, meringues véganes.

**Boissons** : *sans alcool* : Citronnade à la menthe (recette liée)

**Techniques** : Mixer une crème lisse · **À valider au test** : Bocal vs pois chiches secs cuits ; tahini de 2 marques.

---

### 2.35 Taboulé libanais (au persil)

*تبولة · tabbouleh · Moyen-Orient & Caucase › Levant › Liban · Entrée*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 4 | 25 min | 15 min | **40 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten
- 👶 **Enfants** : ✓ dès 3 ans.

**Équipement** : Bon couteau, planche, saladier.

Le vrai taboulé est une salade de persil avec un peu de boulgour, pas l'inverse. Frais, acidulé, très vert.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 3 bouquets | de persil plat | Persil plat / frisé | 🟢 |
| 1 bouquet | de menthe | Menthe | 🟢 |
| 50 g | de boulgour fin | Boulgour | 🟢 |
| 3 | tomates fermes | Tomate | 🟢 |
| 3 | oignons nouveaux | Oignon nouveau / cébette | 🟢 |
| 2 | citrons (jus) | Citron | 🟢 |
| 5 c. à s. | d'huile d'olive | Huile d'olive vierge extra | 🟢 |
| 1 c. à c. | de sel, poivre | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Boulgour.** Rince-le et laisse-le gonfler 15 min dans le jus de citron.
2. **Herbes.** Lave et sèche très bien persil et menthe. Cisèle-les finement au couteau (le mixeur les écrase).
3. **Tomates.** Coupe les tomates en petits dés, émince les oignons nouveaux.
4. **Assemblage.** Mélange tout avec l'huile, le sel et le poivre juste avant de servir.

**Astuces et sécurité**

- Des herbes mouillées font un taboulé détrempé : sèche-les à l'essoreuse.

**Conservation** : 1 jour au frigo (les herbes noircissent).

**Zéro déchet** : **Tiges de persil et de menthe** → bouillon ou thé à la menthe.

**Boissons** : *sans alcool* : Citronnade à la menthe (recette liée)

**Techniques** : Ciseler les herbes · **À valider au test** : Temps de trempage du boulgour.

---

### 2.36 Chakchouka (œufs pochés à la tomate et aux poivrons)

*شكشوكة · chakchouka · Afrique du Nord › Maghreb › Tunisie · Plat*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 4 | 15 min | 25 min | **40 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : œufs
- 👶 **Enfants** : ✓✓ dès 1 an (jaune cuit, sans harissa).

**Équipement** : Grande poêle ou sauteuse avec couvercle.

Des œufs cuits doucement dans une sauce de poivrons et tomates épicée. Un plat complet en une poêle, à saucer avec du pain.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 6 | œufs | Œuf entier (frais) | 🟢 |
| 2 | poivrons (rouge et vert), en lanières | Poivron (rouge/jaune/vert) | 🟢 |
| 1 | oignon jaune, émincé | Oignon jaune | 🟢 |
| 400 g | de tomates pelées | Coulis / passata / tomates pelées | 🟢 |
| 2 gousses | d'ail | Ail | 🟢 |
| 1 c. à c. | de cumin | Cumin (graines / moulu) | 🟢 |
| 1 c. à c. | de paprika | Paprika doux | 🟢 |
| 1 c. à c. | de harissa (facultatif) *(facultatif)* | *sous-recette : Harissa maison* | – |
| 3 c. à s. | d'huile d'olive | Huile d'olive vierge extra | 🟢 |
| quelques brins | de coriandre ou de persil | Coriandre fraîche | 🟢 |
| 1 pincée | de sel | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Poivrons.** Fais revenir oignon et poivrons dans l'huile 10 min, jusqu'à ce qu'ils soient tendres.
2. **Sauce.** Ajoute l'ail, le cumin, le paprika (et la harissa), puis les tomates écrasées et le sel. Laisse mijoter 10 min.
3. **Œufs.** Creuse 6 puits avec une cuillère et casse un œuf dans chacun. Couvre et cuis 5 à 8 min à feu doux, jusqu'à ce que les blancs soient pris.
4. **Service.** Parsème d'herbes et sers dans la poêle, avec du pain.

**Astuces et sécurité**

- Pour les enfants et les femmes enceintes : cuis jusqu'à ce que les jaunes soient pris (10 min).

**Conservation** : La sauce sans œufs : 3 jours au frigo.

**Zéro déchet** : **Poivrons fripés, tomates trop mûres** → parfaits ici. **Pain rassi** → pour saucer, grillé.

**Boissons** : *sans alcool* : Thé à la menthe (recette liée)

**Techniques** : Pocher des œufs dans une sauce · **À valider au test** : Temps de cuisson des œufs selon couvercle.

---

### 2.37 Riz cantonais

*扬州炒饭 · Yángzhōu chǎofàn · Asie de l'Est › Chine › Canton · Plat*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 4 | 20 min | 0 min | **20 min** | € |

- 🐖 **Contient du porc** : Jambon blanc
- 🟡 **Traces d'alcool possibles** : Sauce soja claire
- ⚠️ **Allergènes** : gluten, œufs, soja
- 👶 **Enfants** : ✓✓ dès 2 ans.

**Équipement** : Wok ou grande poêle.

Le plat des restes par excellence : du riz cuit la veille, des œufs, des petits pois, du jambon. Le riz froid est indispensable pour qu'il ne colle pas.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 600 g | de riz long cuit la veille (200 g cru) | Riz long / basmati / thaï | 🟢 |
| 3 | œufs | Œuf entier (frais) | 🟢 |
| 150 g | de jambon blanc en dés | Jambon blanc | 🟢 |
| 150 g | de petits pois (surgelés) | Petits pois / pois gourmands | 🟢 |
| 3 | oignons nouveaux | Oignon nouveau / cébette | 🟢 |
| 2 c. à s. | de sauce soja claire | Sauce soja claire | 🟢 |
| 3 c. à s. | d'huile neutre | Huile de tournesol / colza | 🟢 |
| 1 pincée | de sel, poivre blanc | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Mise en place.** Égraine le riz froid à la main. Coupe tout avant d'allumer le feu : la cuisson va très vite.
2. **Œufs.** Wok très chaud, 1 c. à s. d'huile : brouille les œufs 30 s, réserve.
3. **Garniture.** 1 c. à s. d'huile : saute les petits pois et le jambon 2 min.
4. **Riz.** Ajoute le reste d'huile et le riz. Saute 3 min à feu vif en remuant sans cesse, jusqu'à ce que chaque grain soit chaud et sec.
5. **Finition.** Remets les œufs, ajoute la sauce soja et les oignons nouveaux, saute 1 min.

**Astuces et sécurité**

- ⚠️ Riz cuit : refroidis-le vite et garde-le au frigo, pas plus de 24 h (bactérie Bacillus cereus).

**Variantes (à tester)**

- **Sans porc** : Remplace le jambon par du **jambon de dinde ou de poulet**, ou des crevettes. Substitution **à tester**. *Calcul* : porc **ok**, alcool **trace**.
- **Sans porc et sans traces d'alcool (Strict)** : Jambon → **dinde** ; sauce soja (fermentée) → **sauce d'huître + 1 pincée de sel**. Mollusques : allergène. **À tester**. *Calcul* : porc **ok**, alcool **ok**.

**Conservation** : 2 jours au frigo ; réchauffe à la poêle, jamais deux fois.

**Zéro déchet** : **Riz de la veille** → c'est la base. **Fonds de légumes** → carotte, poivron, chou en petits dés.

**Boissons** : *sans alcool* : Thé au jasmin ; Eau pétillante au citron · *avec alcool (adultes)* : Bière légère (adultes)

**Techniques** : Sauter au wok · **À valider au test** : Riz de la veille vs riz du jour ; poêle vs wok sur induction.

---

### 2.38 Poulet teriyaki

*照り焼きチキン · teriyaki chikin · Asie de l'Est › Japon · Plat*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 4 | 20 min | 0 min | **20 min** | €€ |

- ✅ Sans porc (calculé)
- 🍷 **Contient de l'alcool** : Sauce soja claire, Mirin, Saké / saké de cuisine
- ⚠️ **Allergènes** : gluten, sésame, soja
- 👶 **Enfants** : ✓✓ dès 2 ans en version sans alcool.

**Équipement** : Grande poêle.

Des cuisses de poulet à la peau croustillante, laquées d'une sauce sucrée-salée brillante. La version classique utilise saké et mirin.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 4 | hauts de cuisse de poulet désossés, avec la peau | Cuisse / pilon de poulet | 🟢 |
| 4 c. à s. | de sauce soja | Sauce soja claire | 🟢 |
| 3 c. à s. | de mirin | Mirin | 🟡 |
| 2 c. à s. | de saké (de cuisine) | Saké / saké de cuisine | 🟡 |
| 1 c. à s. | de sucre | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 1 c. à c. | de gingembre frais râpé | Gingembre frais | 🟢 |
| 1 c. à c. | d'huile neutre | Huile de tournesol / colza | 🟢 |
| 1 c. à s. | de graines de sésame *(facultatif)* | Sésame (blanc/noir) | 🟢 |
| 300 g | de riz rond | Riz rond / sushi | 🟢 |

**Étapes**

1. **Sauce.** Mélange soja, mirin, saké, sucre et gingembre.
2. **Peau.** Pique la peau du poulet. Pose-le côté peau dans la poêle froide légèrement huilée, puis allume à feu moyen. Cuis 8 à 10 min sans bouger, jusqu'à une peau dorée et croustillante.
3. **Retourner.** Retourne et cuis 5 min. Retire le gras de la poêle avec du papier absorbant.
4. **Laquage.** Verse la sauce et laisse bouillonner 2 à 3 min en arrosant le poulet, jusqu'à ce qu'elle devienne sirupeuse. ⚠️ Le poulet doit atteindre 74 °C à cœur.
5. **Service.** Tranche, nappe de sauce, parsème de sésame. Avec du riz.

**Astuces et sécurité**

- Le mirin et le saké contiennent de l'alcool ; il en reste une partie après cuisson (Tome 1 §7.4).

**Variantes (à tester)**

- **Sans alcool (Standard et Strict)** : Mirin → **3 c. à s. de jus de raisin blanc + 1 c. à c. de vinaigre de cidre + 1 c. à c. de sucre** ; saké → **bouillon de volaille** ; profil Strict : soja → **sauce d'huître + sel**. **À tester**. *Calcul* : porc **ok**, alcool **ok**.

**Conservation** : 2 jours au frigo.

**Zéro déchet** : **Gras de cuisson du poulet** → pour sauter des légumes. **Reste de poulet** → onigiri ou riz sauté.

**Boissons** : *sans alcool* : Thé vert froid ; Eau pétillante au yuzu ou au citron · *avec alcool (adultes)* : Bière légère (adultes)

**Techniques** : Cuire côté peau, Laquer · **À valider au test** : Goût de la version sans alcool à l'aveugle (Tome 7 §3) ; cuisson peau en poêle inox vs antiadhésive.

---

### 2.39 Chili con carne

*Chili con carne · Amérique du Nord › États-Unis › Texas · Plat* · Fêtes : Repas de famille, Anniversaire

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 25 min | 1 h 00 | **1 h 25** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : aucun déclaré ; **possibles selon marque** : lait, soja
- 👶 **Enfants** : ✓✓ dès 2 ans avec peu de piment.

**Équipement** : Cocotte.

Bœuf haché, haricots rouges, tomate et épices : un plat de partage qui se prépare la veille et nourrit une tablée.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 600 g | de bœuf haché | Bœuf haché | 🟢 |
| 500 g | de haricots rouges cuits (bocal égoutté) | Haricots rouges / noirs | 🟢 |
| 800 g | de tomates pelées | Coulis / passata / tomates pelées | 🟢 |
| 2 | oignons | Oignon jaune | 🟢 |
| 1 | poivron rouge | Poivron (rouge/jaune/vert) | 🟢 |
| 3 gousses | d'ail | Ail | 🟢 |
| 2 c. à c. | de cumin | Cumin (graines / moulu) | 🟢 |
| 2 c. à c. | de paprika fumé | Paprika fumé (pimentón) | 🟢 |
| ½ à 1 c. à c. | de piment en poudre | Cayenne / piment en poudre | 🟢 |
| 1 c. à c. | d'origan séché | Origan frais / sec | 🟢 |
| 2 c. à s. | de concentré de tomate | Concentré de tomate | 🟢 |
| 10 g | de chocolat noir (facultatif) *(facultatif)* | Chocolat noir | 🟢 |
| 2 c. à s. | d'huile | Huile de tournesol / colza | 🟢 |
| 1 c. à c. | de sel | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Légumes.** Fais revenir oignons et poivron 8 min dans l'huile, ajoute l'ail.
2. **Viande.** Ajoute le bœuf et fais-le dorer 5 min à feu vif en l'émiettant.
3. **Épices.** Ajoute les épices et le concentré, remue 1 min pour les torréfier.
4. **Mijotage.** Ajoute les tomates, le sel, couvre et laisse mijoter 45 min.
5. **Haricots.** Ajoute les haricots (et le chocolat) et cuis 15 min de plus. Sers avec du riz, des tortillas ou du pain.

**Astuces et sécurité**

- Le carré de chocolat noir arrondit l'acidité sans donner de goût sucré.

**Conservation** : 4 jours au frigo ; 3 mois au congélateur.

**Zéro déchet** : **Reste de chili** → garniture de burritos, de pommes de terre au four ou de nachos.

**Boissons** : *sans alcool* : Citronnade à la menthe (recette liée) ; Lassi (recette liée) · *avec alcool (adultes)* : Bière ambrée (adultes)

**Techniques** : Torréfier les épices, Mijoter · **À valider au test** : Dosage de piment ; haricots secs vs bocal.

---

### 2.40 Guacamole

*Guacamole · Amérique latine & Caraïbes › Mexique · Entrée* · Fêtes : Apéritif dînatoire

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 4 | 10 min | 0 min | **10 min** | €€ |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : aucun déclaré
- 👶 **Enfants** : ✓✓ dès 1 an (sans piment ni sel).

**Équipement** : Bol, fourchette ou mortier.

Des avocats mûrs écrasés grossièrement, du citron vert, de l'oignon, de la coriandre et du piment.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 3 | avocats mûrs | Avocat | 🟢 |
| 1 | citron vert (jus) | Citron vert | 🟢 |
| ½ | oignon rouge haché fin | Oignon rouge | 🟢 |
| 1 | tomate épépinée en dés | Tomate | 🟢 |
| ½ bouquet | de coriandre | Coriandre fraîche | 🟢 |
| ½ | piment frais (facultatif) *(facultatif)* | Piment frais (divers) | 🟢 |
| ½ c. à c. | de sel | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Base.** Écrase l'oignon, le piment et le sel avec la moitié de la coriandre.
2. **Avocats.** Ajoute la chair des avocats et le citron vert, écrase grossièrement : garde des morceaux.
3. **Finition.** Ajoute la tomate et le reste de coriandre. Sers aussitôt.

**Astuces et sécurité**

- Pose le noyau dans le bol et un film au contact pour limiter le noircissement.

**Conservation** : Quelques heures au frigo, film au contact.

**Zéro déchet** : **Avocats trop mûrs** → idéal ici. **Tiges de coriandre** → hachées dans le guacamole.

**Boissons** : *sans alcool* : Citronnade (recette liée) ; Agua de jamaica (bissap)

**Techniques** : Ciseler les herbes · **À valider au test** : Noircissement au frigo.

---

### 2.41 Accras de morue

*Akra lanmori · France › Outre-mer › Antilles · Entrée* · Fêtes : Noël, Apéritif dînatoire

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐⭐ | 30 | 40 min | 1 h 00 | **1 h 40** | €€ |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten, poissons
- 👶 **Enfants** : ✓ dès 3 ans, sans piment ; friture réservée aux adultes.

**Équipement** : Saladier, casserole profonde ou friteuse avec thermomètre, écumoire, 2 cuillères.

Les beignets antillais de morue, aux herbes et au piment, croustillants et aériens. Indispensables à l'apéritif des fêtes.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 250 g | de morue salée (dessalée 24 h) | Morue salée (dessalage 24-48 h) | 🟡 |
| 200 g | de farine de blé T55 | Farine de blé T55 | 🟢 |
| 1 c. à c. | de levure chimique | Levure chimique | 🟢 |
| 200 ml | d'eau froide (ou d'eau gazeuse) | *implicite* | 🟢 |
| 3 | cives ou oignons nouveaux | Oignon nouveau / cébette | 🟢 |
| 3 gousses | d'ail | Ail | 🟢 |
| ½ bouquet | de persil | Persil plat / frisé | 🟢 |
| 2 branches | de thym | Thym / romarin | 🟢 |
| ½ | piment antillais (selon le goût) | Piment antillais / scotch bonnet | 🟠 |
| 1 L | d'huile de friture | Huile de tournesol / colza | 🟢 |

**Étapes**

1. **Dessalage.** La veille, fais tremper la morue 24 h au frais en changeant l'eau 3 à 4 fois.
2. **Morue.** Poche-la 10 min dans l'eau frémissante, égoutte, retire peau et arêtes, effiloche.
3. **Hachis.** Hache finement cives, ail, persil, thym et piment (gants pour le piment).
4. **Pâte.** Mélange farine et levure, ajoute l'eau en fouettant, puis la morue et le hachis. La pâte doit être épaisse. Laisse reposer 1 h.
5. **Friture.** ⚠️ Huile à 175 °C (jamais plus de 2/3 de la casserole). Forme des boulettes avec 2 cuillères et fais frire 3 à 4 min en les retournant, jusqu'à ce qu'elles soient dorées.
6. **Égouttage.** Sur papier absorbant. Sers chaud.

**Astuces et sécurité**

- Goûte la morue avant de saler : elle reste souvent salée.
- Eau gazeuse très froide = accras plus légers.

**Conservation** : Pâte : 24 h au frigo. Accras cuits : réchauffés 5 min au four à 200 °C.

**Zéro déchet** : **Eau de pochage de la morue** → base d'un court-bouillon. **Huile de friture** → filtrée et réutilisée.

**Boissons** : *sans alcool* : Jus de gingembre (recette liée) ; Planteur sans alcool (jus de fruits exotiques) · *avec alcool (adultes)* : Ti-punch (adultes, avec modération)

**Techniques** : Dessaler, Frire en sécurité · **À valider au test** : Durée de dessalage selon la morue ; légèreté avec eau gazeuse.

---

### 2.42 Quiche lorraine

*Quiche lorraine · France › Grand Est › Lorraine · Plat*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 20 min | 40 min | **1 h 00** | € |

- 🐖 **Contient du porc** : Lardons
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten, lait, œufs
- 👶 **Enfants** : ✓✓ dès 1 an (bien cuite).

**Équipement** : Moule à tarte de 26 cm, poêle, saladier, four.

Pâte brisée, lardons, œufs et crème : la vraie quiche lorraine n'a pas de fromage. Ici avec sa version sans porc.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 1 | pâte brisée maison (recette liée) | *sous-recette : Pâte brisée maison* | – |
| 200 g | de lardons fumés | Lardons | 🟢 |
| 3 | œufs | Œuf entier (frais) | 🟢 |
| 200 ml | de crème fraîche épaisse | Crème fraîche | 🟢 |
| 200 ml | de lait | Lait entier / demi-écrémé / écrémé | 🟢 |
| 1 pincée | de noix de muscade, poivre | Noix de muscade | 🟢 |

**Étapes**

1. **Four.** Préchauffe à 200 °C (th. 6-7). Fonce le moule et cuis la pâte à blanc 10 min.
2. **Lardons.** Fais-les revenir 5 min à sec, égoutte-les.
3. **Appareil.** Fouette œufs, crème, lait, muscade et poivre (peu de sel : les lardons sont salés).
4. **Cuisson.** Répartis les lardons sur la pâte, verse l'appareil. Cuis 30 min à 180 °C (th. 6), jusqu'à ce que la quiche soit dorée et prise au centre.

**Astuces et sécurité**

- Le centre doit à peine trembler à la sortie : il finit de cuire en tiédissant.

**Variantes (à tester)**

- **Sans porc** : **Lardons de dinde fumés** + **1 pincée de paprika fumé** pour le fumé ; ou poireaux fondus et saumon pour une quiche différente. **À tester**. *Calcul* : porc **ok**, alcool **ok**.

**Conservation** : 3 jours au frigo ; 2 mois au congélateur.

**Zéro déchet** : **Fin de crème, de lait, de fromage** → dans l'appareil. **Restes de légumes cuits** → quiche du vide-frigo.

**Boissons** : *sans alcool* : Jus de pomme pétillant · *avec alcool (adultes)* : Vin blanc d'Alsace (adultes)

**Techniques** : Cuire à blanc, Faire un appareil à quiche · **À valider au test** : Version dinde à l'aveugle (Tome 7 §3) ; cuisson à blanc 10 vs 15 min.

---

### 2.43 Gratin dauphinois

*Gratin dauphinois · France › Auvergne-Rhône-Alpes › Dauphiné · Accompagnement* · Fêtes : Noël, Repas de famille

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 20 min | 1 h 15 | **1 h 35** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : lait
- 👶 **Enfants** : ✓✓ dès 1 an.

**Équipement** : Plat à gratin, casserole, mandoline (avec protège-doigts) ou couteau, four.

Des pommes de terre fines cuites lentement dans le lait et la crème à l'ail. Sans fromage dans la version d'origine.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 1,2 kg | de pommes de terre à chair ferme | Pomme de terre | 🟢 |
| 500 ml | de lait | Lait entier / demi-écrémé / écrémé | 🟢 |
| 250 ml | de crème liquide | Crème fleurette (liquide) | 🟢 |
| 2 gousses | d'ail | Ail | 🟢 |
| 20 g | de beurre | Beurre doux / demi-sel | 🟢 |
| 1 pincée | de noix de muscade | Noix de muscade | 🟢 |
| 1 c. à c. | de sel, poivre | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Pommes de terre.** Épluche et tranche en rondelles de 3 mm. ⚠️ Mandoline : toujours avec le protège-doigts. Ne les rince pas : l'amidon lie la sauce.
2. **Précuisson.** Dans une casserole, porte lait, crème, ail écrasé, sel, poivre et muscade à frémissement. Ajoute les pommes de terre et cuis 10 min en remuant doucement.
3. **Gratin.** Frotte le plat avec l'ail et beurre-le. Verse le tout, égalise.
4. **Cuisson.** 1 h à 160 °C (th. 5-6), jusqu'à ce que la pointe d'un couteau entre sans résistance et que le dessus soit doré.

**Astuces et sécurité**

- La précuisson dans le lait évite le gratin qui tranche.

**Conservation** : 3 jours au frigo.

**Zéro déchet** : **Épluchures** → chips au four.

**Techniques** : Trancher à la mandoline en sécurité, Gratiner · **À valider au test** : Variétés de pommes de terre ; temps à 160 vs 180 °C.

---

### 2.44 Velouté de potiron (et graines grillées)

*Velouté de potiron · France · Entrée* · Fêtes : Halloween, Noël

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 20 min | 30 min | **50 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : lait
- 👶 **Enfants** : ✓✓ dès 6 mois (sans sel ni graines).

**Équipement** : Faitout, mixeur plongeur, plaque de four.

Un velouté doux et orangé, et ses graines grillées en garniture : rien ne se jette.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 1,2 kg | de potiron ou de potimarron | Potiron / citrouille | 🟢 |
| 1 | oignon | Oignon jaune | 🟢 |
| 1 | pomme de terre | Pomme de terre | 🟢 |
| 1 L | de bouillon de légumes maison (recette liée) ou d'eau | *sous-recette : Bouillon d'épluchures de légumes* | – |
| 100 ml | de crème ou de lait de coco (facultatif) *(facultatif)* | Crème fleurette (liquide) | 🟢 |
| 20 g | de beurre | Beurre doux / demi-sel | 🟢 |
| 1 pincée | de noix de muscade | Noix de muscade | 🟢 |
| 1 c. à c. | de sel | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Graines.** Retire les graines, rince-les, sèche-les. Mélange-les avec 1 c. à c. d'huile et du sel et grille 12 min à 180 °C.
2. **Légumes.** Fais fondre l'oignon dans le beurre 5 min. Ajoute le potiron et la pomme de terre en cubes (le potimarron se cuisine avec sa peau).
3. **Cuisson.** Couvre de bouillon, sale, cuis 25 min.
4. **Mixage.** Mixe finement, ajoute la crème et la muscade. Sers avec les graines.

**Astuces et sécurité**

- Une cuillère de curry ou de gingembre change tout le velouté.

**Conservation** : 4 jours au frigo ; 3 mois au congélateur.

**Zéro déchet** : **Graines** → grillées en garniture. **Peau du potimarron** → mixée avec le velouté.

**Boissons** : *sans alcool* : Jus de pomme chaud à la cannelle

**Techniques** : Mixer un velouté · **À valider au test** : Potiron vs potimarron vs butternut.

---

### 2.45 Poulet rôti du dimanche (plat-mère)

*Poulet rôti · France · Plat* · Fêtes : Repas de famille

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 4 | 20 min | 1 h 30 | **1 h 50** | €€ |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : lait
- 👶 **Enfants** : ✓✓ dès 1 an.

**Équipement** : Plat à rôtir, four, thermomètre de cuisson conseillé.

Le plat qui en fait trois : le poulet le dimanche, la carcasse en bouillon le lundi, les restes en salade ou en riz sauté le mardi.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 1 | poulet fermier de 1,6 kg | Poulet entier | 🟢 |
| 40 g | de beurre mou | Beurre doux / demi-sel | 🟢 |
| 1 | citron | Citron | 🟢 |
| 1 tête | d'ail | Ail | 🟢 |
| 4 branches | de thym | Thym / romarin | 🟢 |
| 800 g | de pommes de terre grenaille | Pomme de terre | 🟢 |
| 2 | oignons | Oignon jaune | 🟢 |
| 1 c. à c. | de sel, poivre | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Avant.** Sors le poulet 1 h avant. Sèche-le, sale l'intérieur et l'extérieur.
2. **Garniture.** Glisse dans le poulet le citron coupé en deux, 3 gousses d'ail et le thym. Masse la peau avec le beurre.
3. **Plat.** Mets pommes de terre, oignons en quartiers et gousses d'ail autour.
4. **Cuisson.** 1 h 15 à 200 °C (th. 6-7) en arrosant toutes les 20 min. ⚠️ Cuisson OK : 74 °C dans la cuisse, ou jus clair quand on pique.
5. **Repos.** Laisse reposer 10 min sous aluminium avant de découper.

**Astuces et sécurité**

- Pose le poulet sur le côté 20 min, puis l'autre côté, puis sur le dos : cuisson plus régulière.

**Conservation** : Restes : 3 jours au frigo.

**Zéro déchet** : **Carcasse** → bouillon de volaille (recette liée). **Restes de chair** → riz cantonais, salade, sandwich. **Jus et gras du plat** → sauce ou pommes de terre sautées. **Citron cuit** → pressé dans le jus.

**Boissons** : *sans alcool* : Jus de pomme pétillant ; Eau infusée au citron et au thym · *avec alcool (adultes)* : Vin blanc sec ou rouge léger (adultes)

**Techniques** : Rôtir une volaille, Laisser reposer une viande · **À valider au test** : Four statique vs ventilé ; poulet 1,6 vs 2 kg.

---

### 2.46 Mousse au chocolat

*Mousse au chocolat · France · Dessert* · Fêtes : Noël, Saint-Valentin, Anniversaire

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 20 min | 4 h 00 | **4 h 20** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : lait, œufs ; **possibles selon marque** : soja
- 👶 **Enfants** : Œufs crus : pas avant 5 ans selon les recommandations françaises ; préférer le gâteau au yaourt.

**Équipement** : Bain-marie (casserole + bol), 2 saladiers, fouet électrique.

Du chocolat noir et des œufs, presque rien d'autre. Les jaunes donnent le fondant, les blancs l'air.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 200 g | de chocolat noir (55-70 %) | Chocolat noir | 🟢 |
| 6 | œufs très frais (blancs et jaunes séparés) | Œuf entier (frais) | 🟢 |
| 30 g | de sucre | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 20 g | de beurre | Beurre doux / demi-sel | 🟢 |
| 1 pincée | de sel | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Chocolat.** Fais fondre chocolat et beurre au bain-marie. Laisse tiédir 5 min.
2. **Jaunes.** Incorpore les jaunes un à un au chocolat tiède.
3. **Blancs.** Monte les blancs avec le sel en neige souple, ajoute le sucre et fouette jusqu'à ce qu'ils soient brillants et fermes.
4. **Mélange.** Mélange un tiers des blancs au chocolat pour le détendre, puis incorpore le reste délicatement à la spatule, en soulevant.
5. **Repos.** Verse en verrines et laisse prendre 4 h au frigo.

**Astuces et sécurité**

- ⚠️ **Œufs crus** : déconseillé aux femmes enceintes, aux jeunes enfants et aux personnes fragiles.
- Chocolat trop chaud = mousse qui retombe.

**Conservation** : 2 jours au frigo.

**Zéro déchet** : **Fond de chocolat** → copeaux en décor. **Coquilles** → compost.

**Boissons** : *sans alcool* : Café ou chocolat chaud ; Jus de cerise · *avec alcool (adultes)* : Vin doux naturel (adultes)

**Techniques** : Fondre au bain-marie, Monter des blancs en neige, Incorporer délicatement · **À valider au test** : Chocolat 55 vs 70 % ; tenue après 24 h.

---

### 2.47 Meringues (avec les blancs restants)

*Meringue française · France · Dessert*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 20 | 15 min | 1 h 30 | **1 h 45** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : œufs
- 👶 **Enfants** : ✓✓ dès 3 ans : dresser les meringues.

**Équipement** : Saladier propre, fouet électrique, plaque, papier cuisson, poche à douille ou 2 cuillères.

La recette anti-gaspi des blancs d'œufs laissés par une mayonnaise, une crème ou une carbonara. Règle simple : deux fois plus de sucre que de blancs (en poids).

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 4 | blancs d'œufs (environ 120 g) | Blanc d'œuf | 🟢 |
| 240 g | de sucre (moitié sucre glace, moitié sucre fin) | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| quelques gouttes | de jus de citron | Citron | 🟢 |

**Étapes**

1. **Blancs.** Dans un saladier propre et sec, fouette les blancs avec le citron jusqu'à une mousse.
2. **Sucre fin.** Ajoute le sucre fin en 3 fois en fouettant à vitesse maximale jusqu'à ce que la meringue soit lisse, brillante et forme un bec.
3. **Sucre glace.** Incorpore le sucre glace tamisé à la spatule.
4. **Dressage.** Forme des petits tas sur la plaque.
5. **Séchage.** 1 h 30 à 100 °C (th. 3-4), puis laisse refroidir dans le four éteint, porte entrouverte.

**Astuces et sécurité**

- Une trace de jaune ou de gras empêche les blancs de monter.
- Les blancs se congèlent : garde-les jusqu'à en avoir assez.

**Conservation** : 2 semaines dans une boîte hermétique, au sec.

**Zéro déchet** : **Blancs d'œufs** → c'est tout l'objet de cette recette. **Meringues cassées** → vacherin, pavlova ou Eton mess avec des fruits.

**Boissons** : *sans alcool* : Thé ; Café

**Techniques** : Monter des blancs en neige, Sécher au four · **À valider au test** : Four ventilé vs statique ; tenue à l'humidité.

---

### 2.48 Pain perdu

*Pain perdu · France · Goûter / dessert*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 4 | 15 min | 0 min | **15 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : lait, œufs ; **possibles selon marque** : gluten
- 👶 **Enfants** : ✓✓ dès 1 an.

**Équipement** : Assiette creuse, poêle.

Le pain rassis trempé dans le lait et l'œuf, doré au beurre : le plus vieux dessert anti-gaspi.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 8 tranches | de pain rassis (baguette, pain de mie, brioche) | Pain rassis (réservé) | — |
| 2 | œufs | Œuf entier (frais) | 🟢 |
| 250 ml | de lait | Lait entier / demi-écrémé / écrémé | 🟢 |
| 2 c. à s. | de sucre | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| ½ c. à c. | de cannelle | Cannelle (bâton / poudre) | 🟢 |
| 30 g | de beurre | Beurre doux / demi-sel | 🟢 |

**Étapes**

1. **Appareil.** Fouette œufs, lait, sucre et cannelle dans une assiette creuse.
2. **Trempage.** Trempe chaque tranche 10 à 30 s selon sa dureté : elle doit être imbibée sans se défaire.
3. **Cuisson.** Fais dorer dans le beurre à feu moyen, 2 à 3 min par face.
4. **Service.** Saupoudre de sucre. Avec des fruits ou de la compote.

**Astuces et sécurité**

- Version salée : sans sucre, avec du fromage râpé et des herbes.

**Conservation** : À manger chaud.

**Zéro déchet** : **Pain rassis** → c'est la base. **Fond d'appareil** → omelette sucrée.

**Boissons** : *sans alcool* : Chocolat chaud ; Jus de pomme

**Techniques** : Dorer à la poêle · **À valider au test** : Durée de trempage selon le pain.

---

### 2.49 Banana bread

*Banana bread · Amérique du Nord › États-Unis · Goûter / dessert*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 10 | 15 min | 55 min | **1 h 10** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : fruits à coque, gluten, lait, œufs
- 👶 **Enfants** : ✓✓ dès 1 an (sans noix entières avant 4 ans).

**Équipement** : Saladier, fourchette, moule à cake, four.

Le gâteau des bananes noircies qu'on ne mange plus : plus elles sont mûres, meilleur il est.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 3 | bananes très mûres | Banane | 🟢 |
| 200 g | de farine de blé T55 | Farine de blé T55 | 🟢 |
| 100 g | de sucre roux | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 80 g | de beurre fondu | Beurre doux / demi-sel | 🟢 |
| 2 | œufs | Œuf entier (frais) | 🟢 |
| 1 c. à c. | de bicarbonate (ou 1 sachet de levure chimique) | Bicarbonate de soude | 🟢 |
| 1 c. à c. | de cannelle | Cannelle (bâton / poudre) | 🟢 |
| 60 g | de noix ou pépites de chocolat (facultatif) *(facultatif)* | Noix | 🟢 |

**Étapes**

1. **Bananes.** Écrase-les à la fourchette en purée.
2. **Liquide.** Ajoute le beurre fondu, le sucre et les œufs, mélange.
3. **Sec.** Ajoute farine, bicarbonate, cannelle et 1 pincée de sel ; mélange juste assez. Ajoute les noix.
4. **Cuisson.** Verse dans le moule beurré. 50 à 55 min à 175 °C (th. 6). La lame d'un couteau doit ressortir sèche.

**Astuces et sécurité**

- Bananes noires au congélateur : décongèle-les, elles sont parfaites pour ce gâteau.

**Conservation** : 4 jours emballé ; 3 mois au congélateur, en tranches.

**Zéro déchet** : **Bananes trop mûres** → c'est la base. **Peaux** → compost.

**Boissons** : *sans alcool* : Lait ; Café

**Techniques** : Mélanger sans trop travailler · **À valider au test** : Bicarbonate vs levure chimique.

---

### 2.50 Tiramisu

*Tiramisù · Europe du Sud › Italie › Vénétie · Dessert* · Fêtes : Noël, Anniversaire, Saint-Valentin

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 8 | 25 min | 6 h 00 | **6 h 25** | €€ |

- ✅ Sans porc (calculé)
- 🍷 **Contient de l'alcool** : Amaretto
- ⚠️ **Allergènes** : gluten, lait, œufs ; **possibles selon marque** : fruits à coque
- 👶 **Enfants** : Contient du café et des œufs crus : pour les adultes et grands enfants.

**Équipement** : 2 saladiers, fouet électrique, plat de 20 × 25 cm.

Biscuits imbibés de café, crème au mascarpone, cacao. La recette d'origine n'a pas d'alcool ; beaucoup en ajoutent (marsala, amaretto) : il est ici facultatif.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 250 g | de mascarpone | Mascarpone | 🟢 |
| 3 | œufs très frais | Œuf entier (frais) | 🟢 |
| 80 g | de sucre | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 200 g | de biscuits à la cuillère | Boudoirs / biscuits cuillère | 🟢 |
| 300 ml | de café fort refroidi | *implicite* | 🟢 |
| 2 c. à s. | de cacao non sucré | Cacao en poudre non sucré | 🟢 |
| 2 c. à s. | d'amaretto (facultatif) *(facultatif)* | Amaretto | 🟡 |

**Étapes**

1. **Jaunes.** Fouette les jaunes et le sucre jusqu'à ce que le mélange blanchisse. Ajoute le mascarpone et fouette jusqu'à ce que ce soit lisse.
2. **Blancs.** Monte les blancs en neige ferme et incorpore-les délicatement.
3. **Montage.** Trempe rapidement les biscuits dans le café (1 s par face). Alterne biscuits et crème, 2 couches.
4. **Repos.** Au moins 6 h au frigo (idéalement une nuit). Saupoudre de cacao au moment de servir.

**Astuces et sécurité**

- ⚠️ **Œufs crus** : publics fragiles exclus ; version à la crème fouettée sans œufs possible (250 ml de crème liquide montée).

**Variantes (à tester)**

- **Sans alcool** : Supprime l'amaretto ; pour le goût d'amande, infuse **1 c. à s. de poudre d'amande** dans le café chaud puis filtre. Pas d'arôme d'amande amère (souvent alcoolisé). **À tester**. *Calcul* : porc **ok**, alcool **ok**.

**Conservation** : 2 jours au frigo.

**Zéro déchet** : **Café du matin** → refroidi pour le tiramisu. **Biscuits cassés** → au fond des verrines.

**Boissons** : *sans alcool* : Café ; Chocolat chaud · *avec alcool (adultes)* : Vin doux (adultes)

**Techniques** : Monter des blancs en neige, Incorporer délicatement · **À valider au test** : Version sans œufs (crème fouettée).

---

### 2.51 Gâteau au yaourt

*Gâteau au yaourt · France · Goûter / dessert*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 8 | 10 min | 35 min | **45 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : gluten, lait, œufs
- 👶 **Enfants** : ✓✓ dès 3 ans : toute la recette avec un adulte (four).

**Équipement** : Pot de yaourt vide (pour mesurer), saladier, moule à manqué, four.

Le premier gâteau qu'on fait avec les enfants : tout se mesure avec le pot de yaourt.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 1 pot | de yaourt nature (125 g) | Yaourt nature | 🟢 |
| 3 pots | de farine de blé T55 | Farine de blé T55 | 🟢 |
| 2 pots | de sucre | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| ½ pot | d'huile neutre | Huile de tournesol / colza | 🟢 |
| 3 | œufs | Œuf entier (frais) | 🟢 |
| 1 sachet | de levure chimique | Levure chimique | 🟢 |
| 1 | citron (zeste, facultatif) *(facultatif)* | Citron | 🟢 |

**Étapes**

1. **Mélange.** Verse le yaourt dans le saladier, garde le pot. Ajoute œufs, sucre et zeste, mélange.
2. **Farine.** Ajoute farine et levure, puis l'huile. Mélange jusqu'à une pâte lisse.
3. **Cuisson.** Moule huilé. 35 min à 180 °C (th. 6). La lame d'un couteau ressort sèche.

**Astuces et sécurité**

- Le citron se remplace par de la poudre de vanille (pas d'extrait liquide si tu cuisines sans alcool).

**Conservation** : 4 jours emballé.

**Zéro déchet** : **Pot de yaourt** → il sert de mesure. **Citron zesté** → jus pour une citronnade.

**Boissons** : *sans alcool* : Lait ; Chocolat chaud

**Techniques** : Mesurer au pot · **À valider au test** : Moule silicone vs métal.

---

### 2.52 Oranges à la cannelle

*Salade d'oranges marocaine · Afrique du Nord › Maghreb › Maroc · Dessert* · Fêtes : Ramadan / Aïd

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 4 | 10 min | 30 min | **40 min** | € |

- ✅ Sans porc (calculé)
- 🟡 **Traces d'alcool possibles** : Eau de fleur d'oranger / de rose
- ⚠️ **Allergènes** : aucun déclaré
- 👶 **Enfants** : ✓✓ dès 1 an.

**Équipement** : Couteau, plat.

Le dessert léger qui termine un tajine ou un couscous : oranges en rondelles, cannelle, menthe.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 4 | oranges | Orange | 🟢 |
| 1 c. à c. | de cannelle | Cannelle (bâton / poudre) | 🟢 |
| 1 c. à s. | de sucre glace | Sucre glace | 🟢 |
| 1 c. à s. | d'eau de fleur d'oranger (facultatif) *(facultatif)* | Eau de fleur d'oranger / de rose | 🟡 |
| quelques feuilles | de menthe | Menthe | 🟢 |

**Étapes**

1. **Oranges.** Pèle les oranges à vif (sans la peau blanche) et coupe-les en rondelles.
2. **Dressage.** Dispose-les sur un plat, arrose de fleur d'oranger.
3. **Finition.** Saupoudre de cannelle et de sucre glace, ajoute la menthe. 30 min au frais.

**Astuces et sécurité**

- Certaines eaux de fleur d'oranger contiennent de l'alcool : lis l'étiquette (profil Strict).

**Variantes (à tester)**

- **Sans traces d'alcool (Strict)** : Remplace la fleur d'oranger par **le zeste fin d'une orange** et un peu de son jus. **À tester**. *Calcul* : porc **ok**, alcool **ok**.

**Conservation** : 1 jour au frigo.

**Zéro déchet** : **Peaux d'orange** → écorces confites ou zestes séchés pour le thé.

**Boissons** : *sans alcool* : Thé à la menthe (recette liée)

**Techniques** : Peler à vif · **À valider au test** : Variétés d'oranges.

---

### 2.53 Riz au lait vanille

*Riz au lait · France · Dessert*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 10 min | 45 min | **55 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : lait
- 👶 **Enfants** : ✓✓ dès 1 an.

**Équipement** : Casserole à fond épais.

Riz rond, lait, sucre, vanille, et beaucoup de patience à feu doux.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 120 g | de riz rond | Riz rond / sushi | 🟢 |
| 1 L | de lait entier | Lait entier / demi-écrémé / écrémé | 🟢 |
| 80 g | de sucre | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 1 | gousse de vanille | Vanille (gousse) | 🟡 |
| 1 pincée | de sel | Sel fin / gros sel / fleur de sel | 🟢 |

**Étapes**

1. **Blanchiment.** Cuis le riz 2 min dans l'eau bouillante, égoutte.
2. **Lait.** Porte le lait à frémissement avec la vanille fendue et grattée et le sel.
3. **Cuisson.** Ajoute le riz et cuis 40 à 45 min à feu très doux, en remuant souvent, jusqu'à ce qu'il soit crémeux.
4. **Sucre.** Ajoute le sucre en fin de cuisson (il durcit le riz s'il est mis trop tôt).

**Astuces et sécurité**

- Gousse de vanille utilisée → rince-la, sèche-la et mets-la dans le sucre pour du sucre vanillé.

**Conservation** : 3 jours au frigo.

**Zéro déchet** : **Gousse de vanille** → sucre vanillé maison. **Lait proche de la date** → parfait ici.

**Techniques** : Cuire à feu très doux · **À valider au test** : Riz rond de 2 marques.

---

### 2.54 Galette des rois à la frangipane

*Galette des rois · France › Île-de-France · Dessert* · Fêtes : Épiphanie

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐⭐ | 8 | 30 min | 1 h 00 | **1 h 30** | €€ |

- ✅ Sans porc (calculé)
- 🍷 **Contient de l'alcool** : Rhum ambré / blanc
- ⚠️ **Allergènes** : fruits à coque, gluten, lait, œufs
- 👶 **Enfants** : ✓ dès 4 ans (fève).

**Équipement** : Saladier, pinceau, couteau, plaque, four.

Deux disques de pâte feuilletée et une crème d'amande (frangipane). Avec une pâte feuilletée pur beurre du commerce, c'est simple.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 2 | rouleaux de pâte feuilletée pur beurre | Pâte feuilletée (prête) | 🟢 |
| 125 g | de poudre d'amande | Amande (entière, effilée, poudre) | 🟢 |
| 100 g | de beurre mou | Beurre doux / demi-sel | 🟢 |
| 100 g | de sucre | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 2 | œufs (+ 1 jaune pour dorer) | Œuf entier (frais) | 🟢 |
| 1 c. à s. | de rhum (facultatif) *(facultatif)* | Rhum ambré / blanc | 🟢 |

**Étapes**

1. **Frangipane.** Fouette beurre mou et sucre, ajoute les œufs un à un, puis la poudre d'amande (et le rhum).
2. **Montage.** Étale la frangipane sur un disque en laissant 2 cm de bord. Glisse la fève. Mouille le bord et pose le second disque, soude en appuyant.
3. **Repos.** 30 min au frigo.
4. **Décor.** Dore au jaune, trace des arcs au couteau sans percer, fais 3 petits trous.
5. **Cuisson.** 35 min à 190 °C (th. 6-7).

**Astuces et sécurité**

- ⚠️ Fève : préviens les enfants, risque d'étouffement avant 4 ans.

**Variantes (à tester)**

- **Sans alcool** : Supprime le rhum ou remplace-le par **1 pincée de poudre de vanille**. **À tester**. *Calcul* : porc **ok**, alcool **ok**.

**Conservation** : 2 jours à température ambiante.

**Zéro déchet** : **Chutes de pâte feuilletée** → palmiers ou allumettes au fromage. **Blanc d'œuf** → meringues.

**Boissons** : *sans alcool* : Cidre doux sans alcool (jus de pomme pétillant) ; Chocolat chaud · *avec alcool (adultes)* : Cidre (adultes)

**Techniques** : Souder une pâte feuilletée, Dorer · **À valider au test** : Pâte du commerce de 2 marques ; cuisson 35 vs 40 min.

---

### 2.55 Bissap (jus d'hibiscus)

*Bissap · wonjo · Afrique subsaharienne › Afrique de l'Ouest › Sénégal · Boisson* · Fêtes : Ramadan / Aïd, Anniversaire

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 8 | 10 min | 1 h 00 | **1 h 10** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : aucun déclaré
- 👶 **Enfants** : ✓✓ dès 3 ans (sucre modéré).

**Équipement** : Casserole, passoire fine, carafe.

Le jus rouge rubis d'Afrique de l'Ouest : fleurs d'hibiscus infusées, menthe, sucre. Servi très frais.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 60 g | de fleurs d'hibiscus séchées | Hibiscus séché (bissap) | 🟠 |
| 1,5 L | d'eau | *implicite* | 🟢 |
| 150 g | de sucre (à ajuster) | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 1 bouquet | de menthe | Menthe | 🟢 |
| 1 | gousse de vanille (ou 1 pincée de poudre) *(facultatif)* | Vanille (gousse) | 🟡 |

**Étapes**

1. **Rinçage.** Rince les fleurs à l'eau froide.
2. **Infusion.** Porte l'eau à ébullition, ajoute fleurs et menthe, coupe le feu. Infuse 15 min (pas plus : amertume).
3. **Filtrage.** Filtre, ajoute le sucre et la vanille, mélange.
4. **Froid.** Au moins 1 h au frigo.

**Astuces et sécurité**

- Pas d'eau de fleur d'oranger si tu veux une boisson 100 % sans traces d'alcool.

**Conservation** : 4 jours au frigo.

**Zéro déchet** : **Fleurs infusées** → une 2e infusion plus légère, ou confiture d'hibiscus.

**Techniques** : Infuser · **À valider au test** : Temps d'infusion 10 vs 20 min.

---

### 2.56 Citronnade à la menthe

*Citronnade · Afrique du Nord › Maghreb · Boisson*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 10 min | 30 min | **40 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : aucun déclaré
- 👶 **Enfants** : ✓✓ dès 3 ans.

**Équipement** : Carafe, presse-agrumes, mixeur (facultatif).

Citrons pressés, menthe fraîche, sucre, eau glacée. Avec les zestes, rien ne se perd.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 4 | citrons | Citron | 🟢 |
| 1 bouquet | de menthe | Menthe | 🟢 |
| 100 g | de sucre | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 1,2 L | d'eau très froide | *implicite* | 🟢 |

**Étapes**

1. **Sirop.** Mixe ou pile le zeste d'un citron et la menthe avec le sucre et 200 ml d'eau.
2. **Jus.** Ajoute le jus des citrons et le reste d'eau.
3. **Filtrage.** Filtre et sers très frais avec des glaçons.

**Astuces et sécurité**

- Version pétillante : la moitié en eau gazeuse.

**Conservation** : 2 jours au frigo.

**Zéro déchet** : **Citrons pressés** → nettoyant naturel (vinaigre aux agrumes). **Tiges de menthe** → infusion.

**Techniques** : Zester · **À valider au test** : Dosage de sucre.

---

### 2.57 Lassi à la mangue

*आम लस्सी · aam lassi · Asie du Sud › Inde · Boisson*

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 4 | 5 min | 0 min | **5 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : lait
- 👶 **Enfants** : ✓✓ dès 1 an (sans miel avant 1 an).

**Équipement** : Mixeur.

Yaourt, mangue, une pointe de cardamome : la boisson qui calme le piquant d'un curry.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 1 | mangue bien mûre (ou 300 g de pulpe) | Mangue | 🟢 |
| 400 g | de yaourt nature | Yaourt nature | 🟢 |
| 150 ml | de lait froid | Lait entier / demi-écrémé / écrémé | 🟢 |
| 1 à 2 c. à s. | de sucre ou de miel | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 1 pincée | de cardamome moulue | Cardamome | 🟡 |

**Étapes**

1. **Mixage.** Mixe tout jusqu'à ce que ce soit lisse et mousseux.
2. **Service.** Sers aussitôt, très frais.

**Astuces et sécurité**

- Mangue trop mûre ou abîmée : parfaite ici.

**Conservation** : 1 jour au frigo.

**Zéro déchet** : **Noyau de mangue** → racle la chair restante dans le mixeur.

**Techniques** : Mixer · **À valider au test** : Mangue fraîche vs surgelée.

---

### 2.58 Thé à la menthe

*أتاي · atay · Afrique du Nord › Maghreb › Maroc · Boisson* · Fêtes : Ramadan / Aïd

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 6 | 10 min | 5 min | **15 min** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : aucun déclaré
- 👶 **Enfants** : Contient de la théine : pour les grands enfants, léger.

**Équipement** : Théière en métal (ou casserole), verres.

Thé vert gunpowder, menthe fraîche, sucre. On le verse de haut pour l'aérer et faire la mousse.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 2 c. à s. | de thé vert gunpowder | *implicite* | 🟢 |
| 1 gros bouquet | de menthe fraîche | Menthe | 🟢 |
| 60 à 100 g | de sucre | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| 1 L | d'eau bouillante | *implicite* | 🟢 |

**Étapes**

1. **Rinçage.** Mets le thé dans la théière, verse un verre d'eau bouillante, remue et jette cette eau (elle retire l'amertume).
2. **Infusion.** Ajoute la menthe, le sucre et le reste d'eau bouillante. Laisse infuser 4 à 5 min.
3. **Mélange.** Verse un verre et reverse-le dans la théière, 2 ou 3 fois.
4. **Service.** Sers de haut pour faire mousser.

**Astuces et sécurité**

- ⚠️ Théière brûlante : la poignée en métal chauffe.

**Conservation** : À boire chaud.

**Zéro déchet** : **Feuilles de thé infusées** → compost. **Tiges de menthe** → elles infusent aussi.

**Techniques** : Infuser · **À valider au test** : Durée d'infusion ; dosage de sucre.

---

### 2.59 Jus de gingembre

*Gnamakoudji · Afrique subsaharienne › Afrique de l'Ouest › Côte d'Ivoire · Boisson* · Fêtes : Noël, Anniversaire

| Niveau | Portions | Temps actif | Repos / cuisson | Total | Coût |
|---|---|---|---|---|---|
| ⭐ | 8 | 15 min | 1 h 00 | **1 h 15** | € |

- ✅ Sans porc (calculé)
- ✅ Sans alcool (calculé)
- ⚠️ **Allergènes** : aucun déclaré
- 👶 **Enfants** : Piquant : à diluer pour les enfants dès 6 ans.

**Équipement** : Mixeur, passoire fine ou torchon, carafe.

Un jus piquant et rafraîchissant : gingembre frais, citron, menthe, sucre.

**Ingrédients**

| Quantité | Ingrédient | Réf. Tome 3 | Dispo |
|---|---|---|---|
| 200 g | de gingembre frais | Gingembre frais | 🟢 |
| 2 | citrons (jus) | Citron | 🟢 |
| 150 g | de sucre | Sucre blanc / roux / cassonade / vergeoise | 🟢 |
| quelques feuilles | de menthe | Menthe | 🟢 |
| 200 ml | de jus d'ananas (facultatif) *(facultatif)* | Ananas | 🟢 |
| 1,5 L | d'eau | *implicite* | 🟢 |

**Étapes**

1. **Gingembre.** Lave-le (pas besoin de l'éplucher s'il est bio), coupe-le en morceaux et mixe-le avec 500 ml d'eau.
2. **Filtrage.** Filtre en pressant fort dans un torchon.
3. **Assemblage.** Ajoute le reste d'eau, le citron, le sucre, la menthe (et l'ananas).
4. **Repos.** 1 h au frigo.

**Astuces et sécurité**

- Très piquant ? Allonge avec de l'eau ou du jus d'ananas.

**Conservation** : 4 jours au frigo.

**Zéro déchet** : **Pulpe de gingembre filtrée** → séchée pour une tisane ou dans une marinade.

**Techniques** : Mixer et filtrer · **À valider au test** : Piquant selon le gingembre.

---

## 3. Corpus importé et classé (TikTok, Cooking with Morgane)

### 3.1 Sources et méthode

| Source | Relevé | Recettes retenues | Méthode de tri | Fichier |
|---|---|---|---|---|
| Favoris TikTok du compte (onglet Favoris) | 14/10/2026 : 672 favoris, dont 87 hors cuisine écartés | 649 | **Manuel**, d'après la légende de chaque vidéo | `recettes-classees/tiktok_favoris_classes.md` |
| Site Cooking with Morgane (index `/fr/liste.aspx`) | 14/10/2026 | 339 | **Automatique**, mots-clés du titre (pays deviné ; 208 en « Chine ou à préciser ») | `recettes-classees/cookingwithmorgane_classees.md` |

- **Ce qui est conservé** : titre, lien, auteur·e, catégorie, pastilles porc/alcool **repérées dans la légende** (pré-évaluation). **Aucune vidéo ni aucun texte de recette n'est copié** (Tome 7 §7.5, Tome 1 §19.7) : ces recettes appartiennent à leurs auteur·e·s ; l'application les présente comme **liens crédités**.
- 43 favoris TikTok ont une légende vide ou insuffisante : catégorie « À vérifier » (il faut regarder la vidéo).
- Les pastilles 🐖/🍷 ne valent pas badge : une recette importée reste en confiance C ; le moteur ne la déclare jamais « sans porc » sans liste d'ingrédients reconnue (Tome 7 §7.2).

### 3.2 Répartition par catégorie de la bible

| Catégorie | Recettes |
|---|---|
| asie | 323 |
| afrique | 111 |
| desserts | 108 |
| pains | 104 |
| a_verifier | 52 |
| france | 44 |
| italie | 40 |
| sauces | 36 |
| street_food | 34 |
| ameriques | 26 |
| fusion | 21 |
| maghreb | 21 |
| moyen_orient | 17 |
| europe | 13 |
| techniques | 13 |
| boissons | 12 |
| fait_maison | 10 |
| fetes | 2 |
| zero_dechet | 1 |

### 3.3 Usage dans la bible et l'application

- **Atlas** : chaque région affiche « Dans tes imports ». **Pains**, **Sauces**, **Techniques**, **Zéro déchet**, **Fêtes** listent les favoris de leur catégorie.
- **Vivier éditorial** : les plats récurrents des favoris (thieb, yassa, mafé, msemen, naan, focaccia, flan, sauces de snack…) confirment les priorités du Tome 4 ; la vague 1 en couvre déjà une partie. Les recettes de créateur·rice·s ne sont **pas** recopiées : elles peuvent inspirer un brief (Tome 4 §2) rédigé et testé par l'équipe.
- **Import continu** : l'application importe un lien + sa légende (tri automatique), une liste de liens, ou l'**export de données TikTok** (fichier JSON du compte : liens des favoris), voie officielle à défaut d'API (Tome 1 §14.1).

### 3.4 Food fusion (catégorie ajoutée le 14/10/2026)

Pour les recettes **dont l'origine ne se rattache pas à un seul pays** ou qui **marient plusieurs traditions**, une entrée « **🌐 Food fusion** » s'ajoute aux 12 macro-régions de l'atlas. Elle **complète** la règle du Tome 1 §5.2 (classement par plat structurant) : une fiche garde sa cuisine principale pour la recherche par région, et porte en plus la rubrique `fusion` avec une phrase qui explique le mélange.

| Fiche | Mélange |
|---|---|
| Chili con carne | Tex-Mex : cuisine texane née de traditions mexicaines |
| Sauce algérienne maison | sauce de snack franco-belge aux saveurs maghrébines |
| Sauce samouraï maison | sauce de snack franco-belge (mayonnaise, ketchup, harissa) |

**Corpus importé : 21 recettes reclassées en food fusion** (motifs relus à la main : pizzas au butter chicken, tonkatsu ou rendang ; feuilles de riz détournées ; couscous-tiep ; carbonara-ramen ; big mac « piadizza » ; poulets de séries et de mangas ; bao teriyaki…). Exemples :

- Le couscous tiep 🤣 voici la recette les gas . N’oublie pas de t’abonner 😑 merci 🤭. *(TikTok, rangée avant dans « afrique »)*
- J’ai tenté une version express du börek… avec des feuilles de riz 🤤🇹🇷 Je trempe chaque feu *(TikTok, rangée avant dans « moyen_orient »)*
- 20-Min Sausage Carbonara Ramen 🌭🍜 Detailed recipe in bio 🔗 *(TikTok, rangée avant dans « asie »)*
- Rice Paper Fried Chicken! I often get comments asking me to “share the recipe,” so here’s  *(TikTok, rangée avant dans « asie »)*
- 12/10 FLATBREAD WITH BUTTER CHICKEN😋 Wollt ihr ein Rezept dazu ? *(TikTok, rangée avant dans « asie »)*
- Ever Had Avocado Pasta Before? 🥑🍝 Avocado Carbonara Pasta, Asanebo Style! 👍 *(TikTok, rangée avant dans « italie »)*
- FISH & CHIPS CROUSTILLANT À LA FEUILLE DE RIZ 🎣🍟🍋 Dernier épisode de ma mini série autour  *(TikTok, rangée avant dans « europe »)*
- Loco moco à ma façon Un bon steak haché maison, du riz, une sauce bien corsée aux oignons  *(TikTok, rangée avant dans « ameriques »)*
- Le big mac maison façon Piadizza J'AI CASSE LES PRIX : 1,90€ (vs 6,40€ McDo) Recette moins *(TikTok, rangée avant dans « street_food »)*
- NEW🔥NEW🔥NEW🔥NEW🔥NEW🔥 LA RECETTE DU JOUR by BIG.T 🔥 Aujourd’hui : kebab de poulet au BBQ et *(TikTok, rangée avant dans « street_food »)*
- Recette de burger healthy 4 feuilles de riz 2 steack haché 110g 4 tranche de fromage 2 Cas *(TikTok, rangée avant dans « street_food »)*
- 🍗 Le fameux poulet frit de " Los Pollos Hermanos " 🌶️🔥 Une recette inspirée ( grâce à quel *(TikTok, rangée avant dans « street_food »)*

À l'import, le tri automatique de l'application teste la food fusion **avant** les régions : un mélange de traditions prime sur la région d'un des ingrédients.

### 3.5 Vidéos des recettes, lues dans l'application

- **48 fiches sur 70** sont reliées à **106 vidéos existantes** (favoris TikTok, vidéos YouTube de Cooking with Morgane), choisies par mots-clés relus à la main pour chaque fiche (`VIDEO_KEYS` dans `export_app_data.py`), les versions sans porc ni alcool d'abord.
- **920 des 988 recettes importées** se lisent **dans l'application** : TikTok par l'intégration officielle (`tiktok.com/embed/v2/<id>`), YouTube par `youtube-nocookie.com` ; les 339 identifiants YouTube ont été relevés sur les pages du site (`recettes-classees/cookingwithmorgane_videos.json`). Les carrousels photo TikTok s'ouvrent dans TikTok.
- La lecture se lance **dans une fenêtre de l'application** (fiche recette, mode cuisine, listes de favoris) ; **rien n'est chargé chez TikTok ou YouTube avant d'appuyer sur ▶** (RGPD). Chaque fiche permet aussi d'**ajouter son propre lien vidéo**.
- Ce sont les vidéos de leurs auteur·e·s : crédit et lien vers l'original sous chaque lecture ; aucune vidéo n'est copiée (D15). Une vidéo supprimée ou rendue privée par son auteur·e ne se lit plus.

### 3.6 Comptes « La cuisine de Marina » et « NiangCook » (ajoutés le 15/10/2026)

- **58 vidéos de @lacuisinedemarina** (cuisine camerounaise : ndolé, eru, okok, koki, placali, macabo, safou…) et **22 de @niangcook** (cuisine sénégalaise : yassa, thieb, thiakry, bissap blanc, jus de bouye…), favoris et comptes réunis sans doublon.
- Relevé : toutes les vidéos que TikTok affiche sur le web (67 et 18) ; au-delà, TikTok ne renvoie plus rien à un navigateur automatisé et **sa protection anti-robot n'a pas été contournée**. Pour le catalogue complet, importer les liens depuis l'application (onglet Importer).
- 16 vidéos écartées (annonces, vente d'épices, livre, restaurant, rappels de notification). Tri manuel : `recettes-classees/build_createurs.py`.

---

## 4. Règles de substitution génériques (moteur de l'application)

Quand une fiche n'a pas de variante pour le régime du foyer, l'application applique ces règles **par fonction** (Tome 1 §7.5, Tome 3 §3.2, §14, §16) aux **seuls ingrédients fautifs**, puis **revérifie** la recette obtenue (invariant du Tome 8). Toutes au statut **`draft`** : l'interface affiche « **Substitution à tester** » (Tome 7 §3.2) et jamais « goût préservé ».

| Remplace | Par (ratio sur la quantité d'origine) | Régime | Indication |
|---|---|---|---|
| Lardons | Lardons de dinde / de volaille fumés (×1) + Paprika fumé (pimentón) (×0.005) | sans porc | Lardons de dinde fumés + 1 pincée de paprika fumé et un trait d'huile. |
| Poitrine fumée / lard fumé | Poitrine de dinde fumée (×1) + Paprika fumé (pimentón) (×0.005) | sans porc | Poitrine de dinde fumée + paprika fumé. |
| Bacon | Bacon de dinde / de bœuf (×1) | sans porc | Bacon de dinde ou de bœuf. |
| Jambon blanc | Jambon de dinde / de poulet (×1) | sans porc | Jambon de dinde ou de poulet. |
| Jambon cru (Bayonne, Parme, serrano) | Viande des Grisons / bresaola (×1) | sans porc | Viande des Grisons, bresaola ou magret séché, tranchés très finement. |
| Guanciale | Magret de canard séché / fumé (×1) + Huile d'olive vierge extra (×0.03) | sans porc | Magret fumé en dés + 1 c. à s. d'huile d'olive. |
| Pancetta | Magret de canard séché / fumé (×1) + Huile d'olive vierge extra (×0.03) | sans porc | Magret fumé ou bœuf fumé + un peu d'huile. |
| Chorizo (sec/frais) | Chorizo de bœuf ou de volaille (×1) | sans porc | Chorizo de bœuf ou de volaille (paprika fumé + ail). |
| Saucisse de Toulouse | Saucisse de bœuf / de veau / de volaille (×1) | sans porc | Saucisse de bœuf, de veau ou de volaille. |
| Chipolatas | Saucisse de bœuf / de veau / de volaille (×1) | sans porc | Saucisses de volaille. |
| Saucisse de Strasbourg / Francfort | Saucisse de bœuf / de veau / de volaille (×1) | sans porc | Saucisses de volaille ou de bœuf. |
| Knack / saucisse cocktail | Saucisse de bœuf / de veau / de volaille (×1) | sans porc | Saucisses de volaille. |
| Rillettes de porc | Rillettes de poulet / thon / saumon (×1) | sans porc | Rillettes de poulet, de thon ou de saumon. |
| Saindoux | Graisse de canard / beurre clarifié (×1) | sans porc | Graisse de canard ou beurre clarifié, même quantité. |
| Gélatine alimentaire | Gélatine de bœuf / poisson, agar-agar, pectine (×0.33) | sans porc | Agar-agar : environ 1/3 de la dose, à faire bouillir 1-2 min (texture plus ferme). |
| Merguez (agneau/bœuf) | Saucisse de bœuf / de veau / de volaille (×1) | sans porc | Merguez à l'origine vérifiée (100 % bœuf/agneau, boyau de mouton) ou saucisse de bœuf. |
| Bouillon cube volaille | Bouillon d'os maison (bœuf/volaille) (×1) | sans porc | Bouillon maison (recette liée) : sans graisse de porc ni exhausteur. |
| Bouillon cube bœuf | Bouillon d'os maison (bœuf/volaille) (×1) | sans porc | Bouillon maison. |
| Vin rouge | Jus de raisin / pomme (pur jus) (×0.67) + Vinaigre de cidre (×0.06) + Bouillon d'os maison (bœuf/volaille) (×0.33) | sans alcool | Jus de raisin rouge pur jus + bouillon + vinaigre de cidre ; réduire en fin de cuisson. |
| Vin blanc | Bouillon d'os maison (bœuf/volaille) (×1) + Citron (×0.05) | sans alcool | Bouillon + 1 c. à c. de jus de citron par 100 ml (ou verjus). |
| Bière (blonde, brune, blanche) | Bouillon d'os maison (bœuf/volaille) (×1) + Vinaigre de cidre (×0.02) | sans alcool | Mijotés : bouillon + trait de vinaigre ; pâte à beignets : eau gazeuse très froide. |
| Cidre | Jus de raisin / pomme (pur jus) (×1) + Vinaigre de cidre (×0.03) | sans alcool | Jus de pomme + trait de vinaigre de cidre. |
| Calvados | Jus de raisin / pomme (pur jus) (×2) + Vinaigre de cidre (×0.05) | sans alcool | Jus de pomme réduit de moitié + une goutte de vinaigre de cidre. |
| Cognac / armagnac / brandy | Jus de raisin / pomme (pur jus) (×2) + Poudre de vanille (×0.05) | sans alcool | Jus de pomme ou de raisin réduit + vanille. |
| Rhum ambré / blanc | Poudre de vanille (×0.1) | sans alcool | Poudre de vanille (ou sirop + zeste d'orange). |
| Amaretto | Farine d'amande / poudre d'amande (×0.5) | sans alcool | Poudre d'amande infusée dans le liquide chaud, puis filtrée. |
| Mirin | Jus de raisin / pomme (pur jus) (×1) + Vinaigre de cidre (×0.15) + Sucre blanc / roux / cassonade / vergeoise (×0.2) | sans alcool | Jus de raisin blanc + vinaigre de cidre + sucre (3:1:1). |
| Saké / saké de cuisine | Bouillon d'os maison (bœuf/volaille) (×1) | sans alcool | Bouillon léger (ou dashi maison) + trait de vinaigre de cidre. |
| Madère / marsala / xérès | Jus de raisin / pomme (pur jus) (×1.5) | sans alcool | Jus de raisin réduit. |
| Porto | Jus de raisin / pomme (pur jus) (×1.5) | sans alcool | Jus de raisin réduit. |
| Extrait de vanille liquide | Poudre de vanille (×0.1) | sans alcool | Gousse, poudre ou pâte de vanille sans alcool. |
| Kirsch / eaux-de-vie de fruits | Jus de raisin / pomme (pur jus) (×2) | sans alcool | Jus de cerise réduit. |
| Grand Marnier / Cointreau / triple sec | Orange (×0.5) | sans alcool | Jus d'orange réduit + zestes. |
| Eau de fleur d'oranger / de rose | Orange (×0.2) | sans alcool | Zeste fin d'orange (ou eau florale certifiée sans alcool). |
| Sauce soja claire | Sauce d'huître (×0.7) + Sel fin / gros sel / fleur de sel (×0.1) | sans alcool | Profil Strict : sauce d'huître + pincée de sel (mollusques : allergène). |
| Moutarde de Dijon | Graines de moutarde (×0.3) + Vinaigre de cidre (×0.3) | sans alcool | Profil Strict : graines de moutarde écrasées + vinaigre de cidre. |
| Moutarde à l'ancienne | Graines de moutarde (×0.5) + Vinaigre de cidre (×0.3) | sans alcool | Profil Strict : graines de moutarde + vinaigre de cidre. |
| Vinaigre de vin rouge / blanc | Vinaigre de cidre (×1) | sans alcool | Vinaigre de cidre. |
| Vinaigre balsamique | Vinaigre de cidre (×0.7) + Sucre blanc / roux / cassonade / vergeoise (×0.2) | sans alcool | Vinaigre de cidre + un peu de sucre. |
| Vinaigre de riz | Vinaigre de cidre (×1) | sans alcool | Vinaigre de cidre. |
| Cornichon | Concombre (×1) + Vinaigre de cidre (×0.2) | sans alcool | Concombre en dés + vinaigre de cidre. |

**Décision prise pour l'application (à valider, D13)** : le moteur de référence n'utilise que les règles `validated` ; l'application affiche **aussi** les versions adaptées par des règles `draft`, **clairement étiquetées « à tester »**, parce que la demande initiale exige des substitutions dès le départ et que le Tome 7 §3.2 autorise ce libellé pour `draft` et `testing`. Le contrôle de régime, lui, n'est jamais assoupli : une version adaptée qui ne passe pas la revérification est refusée.

---

## 5. Application ATLAS v1

### 5.1 Choix techniques (écart assumé avec D2)

| Sujet | Bible (T1 §17, D2) | v1 livrée | Pourquoi |
|---|---|---|---|
| Plateformes | Flutter + modules natifs | **PWA** (React + TypeScript, Vite) installable sur iPhone, iPad, Mac (Safari › Ajouter au Dock), Android, Windows | Un seul code, testable tout de suite, hors connexion ; la version native reste l'objectif (Live Activities, Watch, minuteur écran éteint) |
| Données | API + base | Données de la bible **embarquées** (export JSON) ; état du foyer sur l'appareil (localStorage) ; export/import de sauvegarde | Pas de serveur ni de compte : aucune donnée de santé ou de religion ne quitte l'appareil (T1 §19.1) |
| Moteur diététique | `atlas_engine.py` (référence) | Portage TypeScript fidèle + 36 tests automatiques (les 28 du Tome 8 adaptés, propriétés aléatoires, 70 fiches réelles, import) | Mêmes invariants ; vérifié contre le moteur Python (§5.4) |
| Audio | Voix neuronales pré-générées | Synthèse vocale **du système** (AVSpeechSynthesizer via Safari, voix Google/Microsoft), normalisation du texte (fractions, c. à s., °C, thermostat) et lexique de prononciation | Hors ligne et gratuit ; les voix premium restent une évolution |
| Vidéos / photos | Tournage (Tome 6) | Couvertures générées ; liens « Tutos YouTube » + favoris importés liés à chaque recette et technique | Les médias ATLAS ne sont pas tournés ; aucun média tiers n'est copié |

### 5.2 Couverture des 10 modules du Tome 1 §4.1

| Module | Livré en v1 | Reste à faire |
|---|---|---|
| 1. Atlas du monde | 12 macro-régions + **Food fusion**, fiches complètes + 381 titres « au programme » (Tome 4) + imports liés ; vue cartes et vue liste accessible | Carte interactive, fiches culturelles par région |
| 2. Recherche | Par **nom** (accents, ligatures, translittérations, synonymes, fautes), par **région**, par **ingrédients** (moteur de suggestion du Tome 1 §6.3 : « tu as tout », « il manque 1-2 choses », « idées », bonus anti-gaspi, familles de substitution, mode « tout utiliser ») | Scan de code-barres, dictée, photo du frigo |
| 3. Enfants | Filtre par âge, toujours sans alcool, sans porc au choix, 30 min max ; règles de sécurité (miel < 1 an, étouffement, œuf cru…) ; « Petit chef » | Mode enfant verrouillé par code parent |
| 4. Mes imports | Lien + légende → **tri automatique** (catégorie, région, porc/alcool, ingrédients rapprochés du Tome 3) ; liste de liens ; **export de données TikTok** ; partage direct depuis TikTok/Instagram sur Android (Web Share Target) ; bibliothèque des 924 recettes classées | Extraction depuis la vidéo (transcription), API officielles |
| Vidéos | Lecteur intégré (TikTok, YouTube) sur les fiches, en mode cuisine et dans les listes ; vidéos existantes liées aux fiches ; ajout de ses propres liens | Vidéos ATLAS à tourner (Tome 6) |
| 5. Techniques | 30 fiches P0 au format T1 §9.3 (pourquoi, matériel, pas à pas, erreurs, sans équipement), reliées aux recettes et aux vidéos | Vidéos ATLAS, parcours d'apprentissage |
| 6. Pains & bases | 16 recettes (baguette, cocotte, pizza, focaccia, naan, pita, chapati, tortillas, msemen, batbout, crêpes, galettes, pancakes, pain de mie, brioche, pâte brisée) + **calculateur de pâte** (pourcentages boulangers, levure sèche ↔ fraîche) | Version « express / pointage long » pour chaque pain |
| 7. Sauces maison | 16 recettes (mayo, algérienne, samouraï, blanche, burger, barbecue, andalouse, ketchup, harissa, pesto, tomate, béchamel, vinaigrette, tzatziki) + **frites maison** + **Sauce Builder** (base → profil → aromates, conservation et alertes calculées) | Fiches rouille, tartare, sauce fromagère dédiée |
| 8. Fêtes & menus | Calendrier de 14 fêtes d'ici et d'ailleurs ; **composeur de menu** à partir d'un plat (Classique / Léger / Audacieux) : régime du foyer, cohérence régionale, équilibre, sous-produits réutilisés, ingrédients partagés, temps cumulé ; **boissons** sans alcool toujours proposées, avec alcool seulement pour un adulte déclaré, message loi Evin ; quantités par convive ; rétro-planning type | Rétro-planning daté, profils d'invités |
| 9. Zéro déchet | Anatomie des ingrédients liée aux recettes ; « ce qu'il te restera » sur chaque fiche ; frigo virtuel (zones, DLC, J-x, tri par urgence) ; DLC/DDM ; conservation ; plat-mère poulet rôti → bouillon → riz cantonais | Bilan matière d'une semaine, score zéro déchet |
| 10. Mode cuisine | Une étape à la fois en très grand texte, cibles de 64 px, **écran toujours allumé**, mise en place à cocher, **lecture audio** (continue, résumé, pas à pas automatique), **commandes vocales** (« suivant », « répète », « minuteur 10 minutes ») là où le navigateur les permet, **minuteurs multiples** nommés lancés depuis le texte des étapes, qui survivent au rechargement (son, vibration, notification) | Live Activity / Dynamic Island, Apple Watch (version native) |

**Transversal** : profil de foyer (sans porc, sans alcool standard ou strict, mode strict sur le doute, végétarien, 14 allergènes, âge des enfants, majorité, équipement) ; version adaptée **A/B** sur chaque fiche avec ce qui a été remplacé et les quantités recalculées ; portions ; liste de courses par rayon partageable ; favoris, menus, recettes cuisinées ; thème clair/sombre (palette corrigée du Tome 5), taille du texte, police lisible ; mises à jour détectées.

### 5.3 Limites connues de la v1

- **iPhone (application web)** : un minuteur ne sonne pas quand l'application est fermée (notification si autorisée) ; la commande vocale dépend de Safari ; pas de Live Activity ni d'Apple Watch. → version native (D2).
- **Données** : référentiel en confiance C ; aucune recette testée en cuisine ; substitutions à tester ; pas de nutrition ni de coût réel.
- **Quantités** : mise à l'échelle simple (les quantités non numériques restent telles quelles) ; liste de courses sans addition des doublons.
- **Imports** : le tri automatique repose sur des mots-clés ; un import sans légende reste « À vérifier ».

### 5.4 Vérifications faites

- `export_app_data.py` : **toutes** les références d'ingrédients des 70 fiches et de leurs variantes existent dans le Tome 3 (sinon l'export s'arrête) ; 29 lignes « implicites » (eau, café, thé vert : à ajouter au Tome 3).
- `npm test` (application) : **36 contrôles** (invariants du moteur, 2 000 recettes aléatoires × 4 profils, les 70 fiches en profil le plus strict, suggestion, import et cas piégés du Tome 7 §7.3).
- Ce tome : badges recalculés par `atlas_engine.py` ; fiches présentes des deux côtés : 70/70.
- Parcours de tous les écrans dans le navigateur (mobile et grand écran, clair et sombre) sans erreur ; version de production installable, **service worker actif, fonctionnement hors connexion** vérifié.

### 5.5 Faire évoluer

```
cd bible && python export_app_data.py      # bible -> données de l'application (vérifie les références)
python build_tome12.py                      # régénère ce tome
cd ../app && npm run dev                    # développement (port 5196)
npm run build                               # tests + typage + version de production (dist/)
npm run deploy                              # publication GitHub Pages (dépôt git à créer)
```
Ajouter une recette = l'écrire dans un fichier `recipes_v1_*.py` au format du Tome 11, relancer l'export : elle apparaît dans l'application avec ses badges, ses substitutions, sa place dans les menus, les rubriques et la recherche par ingrédients.

---

## 6. Zéro déchet ingrédient par ingrédient

Chaque fiche liste automatiquement **les ingrédients qu'elle n'utilise pas en entier** et ce qu'on peut faire de chaque reste. Couverture : **188 ingrédients entamés dans 65 fiches sur 70** ; les autres n'utilisent que des produits du placard en entier.

**Comment c'est calculé** : `zero_dechet_data.py` décrit, pour chaque ingrédient du Tome 3 souvent entamé, comment il s'achète (botte, pot, tube, boîte…), quand une ligne de recette signale un usage partiel (« ½ bouquet », « jus de citron », « 2 c. à s. de concentré »…), ce qui reste (tiges, zeste, blancs d'œufs, carcasse, eau de cuisson…), **comment le garder sans risque**, et **quatre familles d'idées** dans cet ordre : 🍽 *dans le repas en cours* (entrée, accompagnement), 🍲 *un autre plat* (lié à une fiche ATLAS), 🧊 *conserver*, 🌱 *hors cuisine* (compost, jardin, ménage). L'export vérifie chaque ingrédient et chaque recette liée ; l'application masque une recette liée qui ne convient pas au foyer et propose d'**ajouter le reste au frigo virtuel** (il remonte alors dans « Avec ce que j'ai »).

**Angles morts traités** : sécurité sanitaire (riz cuit 24 h maximum, huiles aromatisées à l'ail 4 jours au froid, jaunes 24 h, blancs 2 jours ou congelés) ; achat juste (format de vente rappelé) ; régimes (une idée liée à une recette non adaptée est signalée) ; restes non alimentaires (huile de friture en déchetterie, jamais à l'évier) ; aucune recette ne se propose elle-même.

| Ingrédient | Format d'achat | Reste | Conservation | Idées |
|---|---|---|---|---|
| Jaune d'œuf | œufs à l'unité | blancs d'œufs | 2 jours au frigo dans un bocal fermé ; 3 mois au congélateur (noter le nombre) | Un dessert léger pour finir le repas : meringues (→ Meringues (avec les blancs restants)) ; Mousse au chocolat (avec les jaunes d'une autre recette) (→ Mousse au chocolat) ; Omelette blanche aux herbes, ou dans une pâte à crêpes ; Congelés en bac à glaçons : 1 cube = 1 blanc |
| Jaune d'œuf | œufs à l'unité | coquilles | — | Compost, ou broyées au pied des plantes (calcium) |
| Blanc d'œuf | œufs à l'unité | jaunes d'œufs | 24 h au frigo, couverts d'un filet d'eau ; ne se congèlent pas bien seuls | Une mayonnaise maison pour accompagner (→ Mayonnaise maison) ; Crème dessert, riz au lait plus riche, ou dorure des pâtes (→ Riz au lait vanille) ; Carbonara (version cuite pour les enfants) (→ Spaghetti alla carbonara) |
| Œuf entier (frais) | boîte de 6 ou 12 | coquilles | — | Compost, ou broyées au jardin |
| Citron | à l'unité ou en filet | zeste et peau (citron pressé) | Zeste : 3 mois au congélateur ; écorces : séchées en bocal | Zeste râpé sur le plat ou dans la sauce, juste avant de servir ; Gâteau au yaourt au citron (→ Gâteau au yaourt) ; Citronnade (zeste infusé) (→ Citronnade à la menthe) ; Zestes séchés ou sucre aromatisé (zestes + sucre en bocal) ; Vinaigre ménager aux agrumes : écorces + vinaigre blanc, 2 semaines, filtrer |
| Citron vert | à l'unité | zeste et peau | Zeste : 3 mois au congélateur | Zeste sur le guacamole ou le riz (→ Guacamole) ; Dans un jus de gingembre ou un bissap (→ Jus de gingembre) ; Vinaigre ménager aux agrumes |
| Orange | à l'unité ou en filet | peau et zeste | Zeste : 3 mois au congélateur | Salade de carottes à l'orange en entrée (→ Salade de carottes au cumin et à l'orange) ; Oranges à la cannelle (→ Oranges à la cannelle) ; Écorces confites ou séchées pour le thé ; Écorces séchées : allume-feu naturel ; compost en petites quantités |
| Persil plat / frisé | 1 botte / 1 bouquet | reste de la botte et tiges | Dans un verre d'eau au frigo, couvert d'un sac : 5 à 7 jours | Une sauce verte minute : herbes hachées, huile d'olive, citron, ail, sel ; Taboulé ou salade d'herbes (→ Taboulé libanais (au persil)) ; Pesto (tiges comprises) (→ Pesto au basilic (ou aux fanes)) ; Sauce blanche aux herbes (→ Sauce blanche (kebab, grillades)) ; Tiges dans un bouillon (→ Bouillon d'épluchures de légumes) ; Hachées dans un bac à glaçons, couvertes d'huile d'olive : 3 mois au congélateur ; Compost |
| Coriandre fraîche | 1 botte / 1 bouquet | reste de la botte et tiges | Dans un verre d'eau au frigo, couvert d'un sac : 5 à 7 jours | Une sauce verte minute : herbes hachées, huile d'olive, citron, ail, sel ; Taboulé ou salade d'herbes (→ Taboulé libanais (au persil)) ; Pesto (tiges comprises) (→ Pesto au basilic (ou aux fanes)) ; Sauce blanche aux herbes (→ Sauce blanche (kebab, grillades)) ; Tiges dans un bouillon (→ Bouillon d'épluchures de légumes) ; Hachées dans un bac à glaçons, couvertes d'huile d'olive : 3 mois au congélateur ; Compost |
| Menthe | 1 botte / 1 bouquet | reste de la botte et tiges | Dans un verre d'eau au frigo : 5 jours | Thé à la menthe pour finir le repas (→ Thé à la menthe) ; Citronnade à la menthe (→ Citronnade à la menthe) ; Taboulé (→ Taboulé libanais (au persil)) ; Séchée à l'air, en bocal : 6 mois ; Compost |
| Basilic | 1 botte / 1 bouquet | reste du pot ou de la botte | Le pot sur le rebord de la fenêtre, arrosé ; feuilles coupées : 3 jours | Pesto (→ Pesto au basilic (ou aux fanes)) ; Sauce tomate (les tiges aussi) (→ Sauce tomate maison) ; Pizza margherita (→ Pizza margherita) ; Pesto congelé en bac à glaçons |
| Ciboulette | 1 botte / 1 bouquet | reste de la botte et tiges | Dans un verre d'eau au frigo, couvert d'un sac : 5 à 7 jours | Une sauce verte minute : herbes hachées, huile d'olive, citron, ail, sel ; Taboulé ou salade d'herbes (→ Taboulé libanais (au persil)) ; Pesto (tiges comprises) (→ Pesto au basilic (ou aux fanes)) ; Sauce blanche aux herbes (→ Sauce blanche (kebab, grillades)) ; Tiges dans un bouillon (→ Bouillon d'épluchures de légumes) ; Hachées dans un bac à glaçons, couvertes d'huile d'olive : 3 mois au congélateur ; Compost |
| Aneth | 1 botte / 1 bouquet | reste de la botte et tiges | Dans un verre d'eau au frigo, couvert d'un sac : 5 à 7 jours | Une sauce verte minute : herbes hachées, huile d'olive, citron, ail, sel ; Taboulé ou salade d'herbes (→ Taboulé libanais (au persil)) ; Pesto (tiges comprises) (→ Pesto au basilic (ou aux fanes)) ; Sauce blanche aux herbes (→ Sauce blanche (kebab, grillades)) ; Tiges dans un bouillon (→ Bouillon d'épluchures de légumes) ; Hachées dans un bac à glaçons, couvertes d'huile d'olive : 3 mois au congélateur ; Compost |
| Thym / romarin | 1 botte / 1 bouquet | branches restantes | Séchées à l'air : 1 an en bocal | Focaccia au romarin (→ Focaccia moelleuse au romarin) ; Bouquet garni d'un bouillon (→ Bouillon d'épluchures de légumes) ; Huile aromatisée : au frigo, 4 jours maximum (botulisme) |
| Oignon nouveau / cébette | 1 botte | reste de la botte et verts | Frigo, bac à légumes : 5 jours | Ciselés sur le plat au service ; Riz cantonais (→ Riz cantonais) ; Accras (→ Accras de morue) ; Bulbes replantés dans un verre d'eau : les verts repoussent |
| Poivron (rouge/jaune/vert) | à l'unité ou en lot de 3 | demi-poivron et pédoncule | Frigo, filmé : 4 jours ; en lanières au congélateur : 6 mois | Lanières crues en bâtonnets à l'apéritif avec un houmous (→ Houmous) ; Chakchouka (→ Chakchouka (œufs pochés à la tomate et aux poivrons)) ; Sauce andalouse (poivron grillé) (→ Sauce andalouse maison) ; Pédoncule et graines : compost |
| Chou blanc / rouge | entier | reste du chou | Frigo, filmé : 1 semaine | Salade de chou cru râpé, vinaigrette (→ Vinaigrette de base (et variantes)) ; Dans un mafé ou une soupe (→ Mafé de poulet) ; Riz sauté au chou (→ Riz cantonais) ; Lacto-fermenté (choucroute maison, technique Tome 1 §9) |
| Céleri-branche | pied entier | branches et feuilles restantes | Frigo, enveloppé d'un torchon humide : 1 semaine | Chorba (→ Chorba frik (soupe du Ramadan)) ; Bouillon (feuilles comprises) (→ Bouillon de volaille avec la carcasse) ; Bâtonnets à croquer avec une sauce (→ Tzatziki) |
| Carotte | au kilo ou en botte avec fanes | épluchures et fanes | Épluchures propres : sac au congélateur jusqu'au prochain bouillon | Pesto de fanes (→ Pesto au basilic (ou aux fanes)) ; Bouillon d'épluchures (→ Bouillon d'épluchures de légumes) ; Compost |
| Poireau | à l'unité ou en botte | vert de poireau | Frigo : 5 jours ; congelé émincé : 6 mois | Bouillon (→ Bouillon de volaille avec la carcasse) ; Émincé et fondu au beurre en accompagnement ; Dans une quiche (→ Quiche lorraine) |
| Pomme de terre | filet de 1 à 5 kg | épluchures | À cuisiner le jour même (elles noircissent) | Chips d'épluchures au four : huile, sel, 200 °C, 15 min, à l'apéritif (→ Frites maison (double cuisson, four ou airfryer)) ; Compost |
| Potiron / citrouille | entier ou en tranche | graines et reste de chair | Chair crue en cubes : 3 mois au congélateur | Graines grillées (huile, sel, 180 °C, 12 min) sur le plat ou à l'apéritif (→ Velouté de potiron (et graines grillées)) ; Velouté (→ Velouté de potiron (et graines grillées)) |
| Concombre | à l'unité | demi-concombre | Frigo, filmé : 3 jours | Tzatziki en entrée (→ Tzatziki) ; Eau infusée au concombre et à la menthe |
| Tomate | au kilo ou en grappe | tomates trop mûres | Frigo : 2 jours | Sauce tomate (→ Sauce tomate maison) ; Chakchouka (→ Chakchouka (œufs pochés à la tomate et aux poivrons)) ; Ketchup (→ Ketchup maison) |
| Champignon de Paris | barquette de 250 à 500 g | pieds | Frigo : 2 jours ; congelés : 3 mois | Bouillon (pieds et parures) (→ Bouillon d'épluchures de légumes) ; Duxelles : pieds hachés revenus avec une échalote, sur des toasts |
| Gingembre frais | racine au poids | reste de la racine | Au congélateur entier : se râpe sans décongeler, 6 mois | Jus de gingembre (→ Jus de gingembre) ; Mafé ou teriyaki (→ Poulet teriyaki) ; Infusion gingembre-citron |
| Ail | tête entière | reste de la tête | Au sec, à l'air : 1 mois | Houmous, harissa, tzatziki (→ Houmous) ; Gousses épluchées dans l'huile : au frigo, 4 jours maximum (botulisme) ; Peaux : compost |
| Oignon jaune | filet de 1 à 2 kg | peaux et extrémités | Sac au congélateur avec les épluchures | Bouillon (la peau colore en doré) (→ Bouillon de volaille avec la carcasse) ; Compost ; teinture naturelle (œufs de Pâques) |
| Avocat | à l'unité | demi-avocat | Avec le noyau, citron et film au contact : 1 jour au frigo | Guacamole à l'apéritif (→ Guacamole) |
| Mangue | à l'unité | chair autour du noyau et peau | Chair : 3 mois au congélateur | Lassi (la chair raclée autour du noyau) (→ Lassi à la mangue) ; Peau et noyau : compost |
| Banane | régime | bananes trop mûres | Épluchées, au congélateur : 3 mois | Banana bread (→ Banana bread) ; Pancakes à la banane (→ Pancakes moelleux) ; Peaux : compost |
| Concentré de tomate | tube, boîte de 70 ou 140 g | reste de la boîte | Boîte ouverte : à transvaser, 5 jours au frigo ; ou cuillères congelées sur papier cuisson : 6 mois | Sauce algérienne, ketchup, chili (→ Ketchup maison) ; Congelé par cuillerées |
| Coulis / passata / tomates pelées | boîte de 400 g ou brique de 500 g | reste de la boîte | Transvasé en boîte hermétique : 4 jours au frigo ; 6 mois au congélateur | Sauce tomate pour des pâtes le lendemain (→ Sauce tomate maison) ; Chakchouka (→ Chakchouka (œufs pochés à la tomate et aux poivrons)) |
| Crème fleurette (liquide) | brique de 20 cl ou 50 cl | fond de brique | 3 jours au frigo après ouverture | Quiche (fond de crème + lait) (→ Quiche lorraine) ; Gratin dauphinois (→ Gratin dauphinois) ; Congelée en bac à glaçons pour les sauces : 3 mois |
| Crème fraîche | pot de 20 ou 40 cl | fond du pot | 5 jours au frigo après ouverture | Quiche (→ Quiche lorraine) ; Une cuillère dans le velouté (→ Velouté de potiron (et graines grillées)) |
| Yaourt nature | pot de 125 g ou de 500 g | reste du pot | Date du pot, frigo | Sauce blanche (→ Sauce blanche (kebab, grillades)) ; Lassi (→ Lassi à la mangue) ; Gâteau au yaourt (→ Gâteau au yaourt) ; Naan (→ Naan à la poêle (nature, ail ou fromage)) |
| Yaourt grec | pot de 150 à 500 g | reste du pot | Date du pot, frigo | Tzatziki ou sauce blanche (→ Tzatziki) ; Lassi (→ Lassi à la mangue) |
| Lait entier / demi-écrémé / écrémé | bouteille d'1 L | reste de la bouteille | 3 jours au frigo après ouverture | Riz au lait (→ Riz au lait vanille) ; Pain perdu (→ Pain perdu) ; Béchamel (→ Béchamel) ; Pancakes (→ Pancakes moelleux) |
| Pois chiches (secs / bocal) | bocal ou boîte de 400 g | jus du bocal (aquafaba) | 3 jours au frigo ; 3 mois au congélateur | Mayonnaise sans œuf (→ Mayonnaise maison) ; Meringues véganes (→ Meringues (avec les blancs restants)) |
| Parmesan / Parmigiano | morceau ou sachet râpé | croûte | Au congélateur dans un sac : 6 mois | Croûte dans la sauce tomate, une soupe ou un bouillon (retirer avant de servir) (→ Sauce tomate maison) |
| Mozzarella / burrata | boule de 125 g | petit-lait | Le jour même | Petit-lait à la place de l'eau dans la pâte à pizza ou à pain (→ Pâte à pizza maison (express ou 24 h)) |
| Pâte feuilletée (prête) | rouleau | chutes de pâte | Frigo, filmées : 2 jours ; congelées : 2 mois | Allumettes au fromage ou palmiers à l'apéritif |
| Pain rassis (réservé) | — | croûtes et miettes | Au sec en sac papier ; chapelure en bocal : 1 mois | Chapelure maison (pain sec mixé) ; Croûtons pour le velouté (→ Velouté de potiron (et graines grillées)) |
| Riz long / basmati / thaï | paquet de 500 g à 1 kg | riz cuit en trop | ⚠️ Refroidi en moins de 2 h, frigo, 24 h maximum ; réchauffé une seule fois | Riz cantonais le lendemain (→ Riz cantonais) ; Riz au lait (avec du riz rond, de préférence) (→ Riz au lait vanille) |
| Pâtes sèches (spaghetti, penne…) | paquet de 500 g | eau de cuisson | À utiliser chaude, tout de suite | Une louche pour lier la sauce (amidon) ; Refroidie, sans sel : arrosage des plantes ; eau de vaisselle |
| Huile de tournesol / colza | bouteille d'1 L | huile de friture | Filtrée, à l'abri de la lumière : 5 à 6 fritures si elle reste claire | Filtrer refroidie au filtre à café ; Jamais à l'évier : déchetterie (point de collecte des huiles) |
| Poulet entier | entier | carcasse, peau, gras | Carcasse : 2 jours au frigo ou 3 mois au congélateur | Bouillon de volaille (→ Bouillon de volaille avec la carcasse) ; Restes de chair : riz cantonais (→ Riz cantonais) ; Gras du plat pour rôtir des pommes de terre |
| Cuisse / pilon de poulet | barquette | os et peaux (si désossées) | Congelés en sac : 3 mois | Bouillon de volaille (→ Bouillon de volaille avec la carcasse) |
| Paleron | morceau | parures | Frigo : 24 h ; congelées : 3 mois | Bouillon de bœuf ou farce (→ Bouillon de volaille avec la carcasse) |
| Crevettes (cuites/crues) | barquette | têtes et carapaces | Congelées : 3 mois | Fumet ou bisque : revenues, mouillées d'eau, 20 min, filtrées ; Compost (en petite quantité, enterrées) |
| Vin rouge | bouteille de 75 cl | reste de la bouteille | Bouchée, au frigo : 3 à 5 jours pour la cuisine ; en glaçons : 3 mois | Glaçons de vin pour les sauces (adultes) ; Vinaigre maison avec une mère de vinaigre |
| Levure boulangère sèche | sachets de 5,5 g ou boîte de 100 g | reste du sachet | Sachet replié et pincé, au frigo : 1 mois ; boîte : date indiquée, au frigo après ouverture | Une seconde fournée : pâte à pizza, naan, batbout (→ Pâte à pizza maison (express ou 24 h)) ; Noter la date d'ouverture sur le sachet |
| Levure chimique | sachets de 11 g | reste du sachet | Sachet fermé, au sec : 6 mois | Pancakes ou gâteau au yaourt (→ Pancakes moelleux) |
| Hibiscus séché (bissap) | sachet de 100 à 250 g | fleurs déjà infusées | Frigo : 2 jours | Seconde infusion, plus légère (→ Bissap (jus d'hibiscus)) ; Confiture ou chutney d'hibiscus (fleurs mixées, sucre, citron) ; Compost |
| Vanille (gousse) | tube de 1 à 3 gousses | gousse grattée | Rincée et séchée : 1 an | Sucre vanillé maison : la gousse dans un bocal de sucre ; Infusée dans le lait d'un riz au lait ou d'une crème (→ Riz au lait vanille) |

> Durées de conservation **prudentes** (Tome 3 §17.2) : à faire valider par le·la diététicien·ne et un·e référent·e hygiène (D20).

---

## 7. Illustrations : photos sous licence libre

**133 photos** illustrent l'application : 12 fetes, 69 recettes, 12 regions, 9 rubriques, 31 techniques.

**Méthode (illustrations/)** : `fetch_candidates.py` rassemble 10 candidates par sujet sur Wikimedia Commons et Openverse (Flickr), **uniquement sous CC0, domaine public, CC BY ou CC BY-SA** (usage commercial et modification permis ; NC, ND et GFDL seule refusées) ; planches contact relues **une à une** ; choix dans `selections.json` ; `process.py` recadre en 4:3 (point d'intérêt réglable), applique un étalonnage commun discret (contraste, chaleur, saturation, piqué), produit du WebP 400/800/1200 px et la couleur dominante (fond pendant le chargement), et écrit les crédits (`app/src/data/images.json`).

**Règles de choix** : le plat doit être reconnaissable et appétissant, en lumière naturelle ; pas de marque visible (flacons, emballages), pas de bouteille ni de verre d'alcool mis en avant, pas de porc quand le sujet ne l'impose pas (plateau de jambon écarté pour Pâques), **pas de scène d'abattage** (Aïd), **pas de visage d'enfant** (droit à l'image des mineurs), **pas d'image générée par IA** présentée comme une photo (images de robots écartées), pas d'homonymes (la « vinegret » russe pour la vinaigrette).

**Affichage** : crédit sous chaque photo (auteur·e, licence, source) et page « Crédits photos » ; mention « photo d'illustration : le plat peut différer de la recette ATLAS » ; les versions recadrées restent sous la licence d'origine ; chargement différé et taille adaptée à l'écran ; photos gardées hors connexion après affichage, ou toutes d'un coup depuis le Profil ; titre sur photo avec voile ≥ 55 % (Tome 5 §2.5).

**Manques et suite** : *pain de mie* sans photo acceptable (illustration de secours conservée) ; quelques photos correctes sans plus (baguette, sauce samouraï, jus de gingembre). Le pipeline local (ComfyUI / AUTOMATIC1111) n'a qu'un modèle de style manga (Animagine XL), inadapté à la photo culinaire : générer les manques demanderait un modèle photoréaliste (≈ 7 Go) et un étiquetage « image générée » (D19). L'objectif reste les photos ATLAS du Tome 6.

---

## 8. Décisions ouvertes ajoutées au registre

| # | Décision | Recommandation | Échéance |
|---|---|---|---|
| D13 | Afficher les versions adaptées par des règles `draft` (étiquetées « à tester ») | Oui jusqu'au lancement public ; au Go/No-Go, seules les règles `validated` disent « goût préservé » (T7 §14) | Avant bêta |
| D14 | PWA d'abord, native ensuite | PWA pour la bêta fermée ; prototype natif (D2) pour minuteur écran éteint, Live Activities, Watch | Sprint 0 |
| D15 | Corpus TikTok et sites : usage | Liens crédités et inspiration de briefs uniquement ; jamais de recopie de texte ou de média | Phase 0 |
| D16 | Végétarien : fromages à présure animale | Avertissement (pas d'exclusion) en v1 ; à arbitrer avec le·la diététicien·ne | Avant bêta |
| D17 | Catégorie « Food fusion » | Entrée d'atlas transversale ; la fiche garde sa cuisine principale (T1 §5.2) et porte une phrase d'explication | Fait (v1) |
| D18 | Lecture de vidéos tierces dans l'application | Intégrations officielles TikTok et YouTube sans cookie, chargées au clic, crédit + lien ; à revoir si une plateforme le restreint | Avant bêta |
| D19 | Images manquantes : génération IA ? | Non par défaut ; si oui, modèle photoréaliste local, étiquette « image générée », jamais pour un plat présenté comme la recette | Avant bêta |
| D20 | Durées de conservation des restes | Valider les durées prudentes de `zero_dechet_data.py` (diététicien·ne + hygiène) | Avant bêta |

> **Fin du Tome 12.**