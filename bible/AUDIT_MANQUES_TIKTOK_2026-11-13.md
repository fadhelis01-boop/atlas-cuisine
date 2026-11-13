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
