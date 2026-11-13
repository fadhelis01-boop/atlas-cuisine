# Audit des catégories et plats manquants (13/11/2026)

Mesure sur les 1 527 fiches exportées (`app/src/data/recipes.json`), avant toute nouvelle fiche. Objectif : identifier ce qui
manque pour compléter l'appli avec les recettes les plus vues sur TikTok, catégorie par catégorie et région par région,
avant de les écrire. Rien n'est corrigé dans cet audit — c'est la liste de ce qui reste à faire.

## 1. Déséquilibres mesurés par grande région (`macro`)

| Région | Fiches | Plats | Entrées | Desserts |
|---|---|---|---|---|
| Asie du Sud (Inde, Pakistan…) | 74 | 48 | 5 | **4** |
| Moyen-Orient & Caucase | 73 | 47 | 12 | **2** |
| Amérique latine & Caraïbes | 80 | 50 | 11 | **4** |
| Asie du Sud-Est | 78 | 54 | 12 | **3** |
| Océanie | 26 | 16 | 4 | 5 |

Ces cinq régions ont le dessert comme angle mort le plus net : une cuisine qui pèse 50-80 fiches de plats n'a que 2 à 4
desserts, alors que ce sont souvent les desserts les plus filmés sur TikTok (riz au lait indien, baklava, ube philippin…).

## 2. Pays sous-représentés malgré un poids réel sur TikTok

| Pays | Fiches | Ce qui existe déjà |
|---|---|---|
| **Philippines** | 4 | Pancit, adobo de poulet, sinigang, lumpia — aucun dessert, aucun grillé |
| Colombie | 3 | Sancocho (×2), ajiaco |
| Chili | 1 | — |
| Équateur, Bolivie, République dominicaine, Pays de Galles, Islande | 0 | — |

La Colombie, le Chili et les Philippines ont une présence TikTok largement supérieure à leur présence dans l'appli.

## 3. Classiques mondiaux absents, vérifiés un par un (titre + variantes d'orthographe)

Vérifié par recherche dans les titres (accents neutralisés, plusieurs graphies essayées) pour éviter les faux « manquants ».

### Desserts (le plus gros manque, toutes régions)
- **Asie du Sud** : rasmalai, gajar halwa (halwa de carotte), barfi, ladoo, falooda
- **Moyen-Orient** : maamoul, qatayef (biscuits/crêpes du Ramadan), sutlaç (riz au lait turc)
- **Asie du Sud-Est / Philippines** : halo-halo, leche flan, bibingka, turon
- **Amérique latine** : quindim (Brésil), picarones (Pérou)
- **Occidental, très viral** : red velvet cake, cinnamon rolls, trifle anglais
- **Pâtisserie moderne virale** : chocolat de Dubaï (pistache-kadaïfi), cruffin

### Plats et street food
- **Chine** : xiaolongbao (raviolis soupe), aucun dim sum à la carte
- **Inde** : dosa (crêpe de lentilles/riz)
- **Philippines** : sisig, lechon (porc rôti, toujours avec une version volaille), kare-kare
- **Colombie** : bandeja paisa, patacones/tostones, buñuelos, obleas
- **Grande-Bretagne** : bangers and mash, haggis (avec la réserve d'usage sur les abats)
- **Espagne** : tortilla española / de patatas — étonnant, c'est un classique absolu, absent
- **Argentine** : asado (le rituel, pas juste « churrasco »)
- **États-Unis, très viral TikTok** : smash burger, pulled pork, mac and cheese ✅ déjà présent (vérifié à tort manquant au premier passage)

### Pains
- Challah, pain au chocolat, pide (pizza turque), johnny cake/bakes antillais, hushpuppies

### Tendances TikTok à forte vue (hors classiques régionaux)
- Pâtes feta au four (baked feta pasta)
- Smash burger (doublon avec plus haut, confirme la priorité)
- Nouilles à l'ail façon TikTok (garlic noodles)
- Dalgona coffee
- Butter board (planche à tartiner)
- Corn ribs (travers de maïs)
- Chaffle (gaufre au fromage, low-carb)
- Baked oats (avoine cuite au four, format mug/plat)
- Birria ramen (fusion virale 2023-2025)

## 4. Déjà couverts (vérifié, pas de doublon à créer)
Pad thai, banh mi, pho, bibimbap, tteokbokki, bulgogi, poulet frit coréen, ramen, gyoza, okonomiyaki, takoyaki, shawarma,
falafel, houmous, biryani, butter chicken, tikka masala, samoussa, naan, paneer tikka, idli, jollof rice, suya, injera,
doro wat, bobotie, piri-piri, poutine, chowder, BBQ ribs, buffalo wings, tacos al pastor, ceviche, empanadas, arepas,
feijoada, moqueca, chimichurri, poke bowl, fish and chips, shepherd's pie, paella, churrasco, risotto, osso buco, focaccia,
gnocchi, cannoli, moussaka, souvlaki, baklava, tzatziki, goulash, pierogi, schnitzel, pretzel/bretzel, fondue, raclette,
crumble, scones, umm ali, basbousa, pastel de nata, arroz con leche, mochi, dorayaki, taïyaki, bubble tea, beignets,
pancakes, crêpe Suzette, tiramisu, cheesecake, baozi/bao, birria tacos, esquites, hot honey chicken, matcha latte.

## 5. Priorités proposées pour la prochaine vague de fiches

1. **Desserts d'Asie du Sud, du Moyen-Orient et des Philippines** (angle mort le plus net et le plus mesuré) : rasmalai,
   gajar halwa, barfi, ladoo, falooda, maamoul, qatayef, sutlaç, halo-halo, leche flan, bibingka, turon, quindim, picarones.
2. **Philippines, plats et street food** : sisig, lechon (+ variante volaille), kare-kare — pour sortir d'un pays à 4 fiches.
3. **Classiques « étonnamment absents »** : tortilla española, dosa, xiaolongbao, asado argentin, bangers and mash.
4. **Tendances TikTok virales à forte vue** : smash burger, pâtes feta au four, nouilles à l'ail, dalgona coffee, butter
   board, chaffle, baked oats, birria ramen, chocolat de Dubaï, corn ribs, cronut, cinnamon rolls, red velvet, trifle.
5. **Compléter la Colombie et le Chili** : bandeja paisa, patacones, buñuelos, obleas (Colombie) ; au moins 2-3 classiques
   chiliens (empanada de pino, pastel de choclo, completo italiano).

Chaque fiche créditera la vidéo TikTok la plus vue/aimée trouvée pour ce plat (méthode déjà établie : recherche
`tiktok.com/search/video?q=<plat>`, ou comptes déjà exploités dans ce projet — Le Riz Jaune, Cooking with Morgane, Eryn,
Ryuji, Lynja — et « Ethan Bernat » à identifier). Illustration par photo libre via le pipeline `illustrations/collect_vN.py`
existant. Décision du propriétaire pas encore demandée sur l'ordre de ces 5 priorités.

## 6. Mise en œuvre (13/11/2026, suite)

Les 5 priorités ont été écrites le jour même, dans l'ordre : **42 fiches nouvelles** au total.

- `recipes_v7_desserts_manquants.py` (priorité 1, 14 fiches) : rasmalai, gajar halwa, barfi, ladoo, falooda, maamoul,
  qatayef, sütlaç, halo-halo, leche flan, bibingka, turon, quindim, picarones.
- `recipes_v7_monde_manquants.py` (priorités 2 et 3, 13 fiches) : sisig, lechon kawali, kare-kare (Philippines) ; dosa,
  xiaolongbao, asado argentin, bangers and mash, haggis (façon terrine, sans la panse — décision du propriétaire si une
  version 100 % traditionnelle doit s'y ajouter) ; bandeja paisa, patacones, buñuelos colombiens, obleas, completo
  italiano (Colombie/Chili). **Correction en cours de route** : « tortilla española » était déjà dans l'appli
  (`tortilla_espanola`) — mon audit initial l'avait classée à tort comme manquante (titre français « Tortilla de
  patatas », pas « tortilla española »), retirée de la liste avant d'écrire la fiche.
- `recipes_v7_vege_tiktok.py` (correctif + début priorité 4, 3 fiches) : pâtes feta au four, nouilles à l'ail, saag
  paneer. Les fiches carnées des priorités 2-3 avaient fait tomber la part de plats végétariens sous le seuil mesuré
  (test 63, ≥ 33 %) ; ces 3 fiches, elles-mêmes très vues sur TikTok, l'ont rétablie.
- `recipes_v7_tiktok_viral.py` (fin priorité 4, 12 fiches) : smash burger, dalgona coffee, butter board, chaffle,
  baked oats, birria ramen, chocolat façon Dubaï, cinnamon rolls, red velvet cake, trifle anglais, corn ribs, cronut.

**Chaque plat sans élément acide** (test 85) a reçu un ajout authentique plutôt qu'un acide forcé : sawsawan (vinaigre
et piment) pour le kare-kare, chimichurri relié en sous-recette pour l'asado, moutarde anglaise pour le haggis, citron
vert sur l'avocat pour la bandeja paisa.

**Non fait, à faire dans une passe ultérieure** : aucune fiche n'a de vidéo TikTok créditée sauf le rasmalai (crédité
avant que la recherche TikTok ne tombe en erreur serveur 500, de façon persistante, pendant tout le reste de la session —
retenter plus tard).

## 8. Illustrations (13/11/2026, suite)

`collect_v18.py` (Commons/Openverse, licences libres uniquement) → planches de contact relues une à une →
`choix_v18.txt` → fusion dans `candidats.json`/`selections.json` → `process.py`. **38 fiches sur 42 illustrées**
(1 212 images publiées sur le dépôt ; budget de démarrage inchangé, les photos sont chargées à la demande).

4 fiches sans photo convenable, à reprendre avec d'autres mots-clés :
- `obleas_dulce_de_leche` : aucun résultat libre trouvé pour ce plat précis.
- `chaffle`, `baked_oats` : les résultats montraient des barres de céréales/granola, pas le plat réel (gaufre minute
  au fromage, bol cuit au four individuel) — mots-clés anglais trop génériques.
- `nouilles_a_lail` (garlic noodles) : résultats sans rapport (pâtes tomate, saumon, coquilles Saint-Jacques) —
  « garlic noodles » seul ramène trop de bruit, essayer « buttery garlic noodles » ou un terme plus spécifique.

Budget de démarrage : 398/400 Ko après ces 4 vagues (contre 390/400 avant). La marge restante (2 Ko) est désormais très
faible : toute nouvelle fiche devra d'abord alléger l'index (`app/src/lib/data.ts`) avant d'en ajouter.

## 7. Audit du dico et des techniques (13/11/2026, en tant que cuisinier senior)

Mesuré sur l'ensemble du catalogue (pas seulement les 42 fiches du jour) : chaque mot de jargon culinaire employé dans
une étape doit soit être expliqué dans `glossaire.ts` (le lexique du débutant, détecté automatiquement par régulière
sur le texte), soit renvoyer à une fiche technique existante.

- **Fiche technique manquante repérée** : faire un fromage frais maison (chenna, paneer) — utilisé dans mes deux
  nouvelles fiches indiennes (rasmalai, saag paneer) mais aucune fiche technique ne l'expliquait. Ajoutée
  (`techniques2.ts`, famille « Produits laitiers maison », id `fromage-frais-maison`) et reliée aux deux fiches.
- **6 mots de jargon utilisés dans des dizaines de fiches existantes mais jamais expliqués dans le lexique**, repérés
  par mesure (comparaison mot-utilisé / mot-défini sur tout le corpus) : **fond brun**, **court-bouillon**,
  **déveiner**, **détendre**, **caraméliser**, **pincer** (au sens « pincer les sucs », fond de veau). Ajoutés à
  `glossaire.ts`, reliés à la fiche technique du bouillon ou du caramel quand elle existe.
- **Quenelle** : mot utilisé dans 4 fiches (quenelles de brochet, féroce d'avocat « en quenelles », île flottante,
  dumplings de poulet) dans deux sens différents (la boulette façonnée à la cuillère, et la quenelle lyonnaise
  pochée) ; aucune des deux définie. Ajoutée.
- **Vérifié et déjà couvert** (pour éviter les doublons) : parer, flamber, singer, brider, concasser, zester,
  chiffonnade, effilocher, tempérer, clarifier, beurre clarifié, chemiser — tous déjà dans le lexique malgré une
  première mesure erronée (comparaison sensible à la casse, corrigée).
- **Vérifié, non utilisé dans le catalogue** (pas d'ajout nécessaire) : suprêmes, lever les filets, clouter, canneler,
  désosser.

Reste à faire si on va plus loin : mesurer de la même façon les définitions d'ingrédients rares du dictionnaire
(`dico_*.py`) plutôt que le seul vocabulaire des étapes — non fait dans cette passe.
