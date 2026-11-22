# Audit « amateur de pains, brioches et pâtisserie maison » (22/11/2026)

Je fais mon pain, ma brioche, mes viennoiseries et mes gâteaux à la maison depuis quelques années : j'ai déjà raté
des pâtes qui ne lèvent pas, des brioches sèches au démoulage, un tourage où le beurre a fondu. Cet audit regarde
l'application du point de vue de cet amateur — pas le vocabulaire technique (déjà vérifié complet le 21/11 dans
`AUDIT_CHEF_PRO_SENIOR_2026-11-21.md` : pétrir, pointage, tourage, sablage, tempérer le chocolat existent bien), mais
ce qui aide concrètement à réussir chez soi sans y être déjà passé dix fois. Rien n'a été corrigé : ce document liste
les angles morts, par ordre de gravité.

## 1. Constats mesurés

| # | Angle | Mesure | Gravité |
|---|---|---|---|
| 1 | **La pousse n'a presque jamais de repère visuel, seulement une durée** | Sur 45 fiches de la rubrique `/pains`, 26 ont une étape de pousse/apprêt. **15 d'entre elles ne donnent qu'une durée fixe** (« Laisse lever 2 h à 25 °C », « Pousse. 1 h 30, couvert. ») sans aucun repère visuel (« double de volume », « la pâte tremble »), alors que la pousse réelle dépend fortement de la température de la cuisine — un amateur en cuisine froide en hiver qui s'en tient au chrono sort une pâte qui n'a pas assez levé. Parmi les fiches sans repère : `brioche`, `kougelhopf`, `pains_chocolat`, `bagels`, `fougasse_olives`, `pain_au_lait`, `pain_complet`. Les 11 autres (dont `croissants` : « ils doublent et tremblent ») montrent que ce repère existe déjà ailleurs dans l'appli — il manque juste sur plus de la moitié des fiches. | **forte** |
| 2 | **Aucun dépannage pour une brioche sèche au démoulage, le problème le plus classique de ce type de pâte** | `lib/rescue.ts` a déjà une carte « Le gâteau est sec » très complète (sirop, crème anglaise, baisser le four), mais sa regex (`gateau\|cake\|genoise\|muffin\|biscuit\|quatre.quarts\|madeleine`) ne couvre pas le mot « brioche » : vérifié sur les 6 fiches de pâte briochée (`brioche`, `kougelhopf`, `kanelbullar`, `cinnamon_rolls`, `brioches_roulees_pate_tartiner`, `pain_au_lait`), aucune ne déclenche cette carte ni aucune autre carte « c'est sec ». Une brioche trop cuite ou trop farinée — l'erreur la plus fréquente d'un amateur qui débute — n'a donc aucun rattrapage proposé sur sa propre fiche. | **forte** |
| 3 | **45 fiches dans `/pains`, zéro classement, alors que la rubrique mélange des familles très différentes** | Mesuré par technique dominante : pains du quotidien sans levain (naan, pita, tortillas, chapati, batbout, msemen, arepas, manakish — 9), pains levés classiques (baguette, cocotte, mie, complet, fougasse, bagels, ciabatta, levain, etc. — 15), viennoiserie feuilletée levée (croissants, pains au chocolat — 2), pâte briochée sucrée (brioche, kougelhopf, kanelbullar, cinnamon rolls, brioches roulées, cronut — 6), pâtes à crêpes/gaufres (crêpes, pancakes, gaufres, spätzle — 4), bases/pizza (pâte à pizza, margherita, pâte brisée, bretzels, pão de queijo — 5). `Pains.tsx` affiche tout en une seule grille (`MoreGrid`), sans puce de filtre ni accordéon — exactement le cas que `bible/CONVENTIONS_LISTES_RUBRIQUE.md` (audit dév senior du 21/11) range dans « plus de 8 familles → accordéon », déjà appliqué à `Techniques.tsx` mais pas ici. Un amateur qui débute (naan à la poêle) et un qui vise un tourage de croissants n'ont aucun moyen de filtrer par niveau ou par famille. | moyenne |
| 4 | **Le calculateur de pâte ne couvre que la conversion sèche ↔ fraîche, jamais la levure chimique ni le levain** | `Pains.tsx` (`DoughCalc`) convertit très bien levure sèche en levure fraîche (× 3) et rappelle de ne pas confondre levure boulangère et levure chimique — mais ne donne aucune équivalence quand une fiche (gâteaux, certains pains rapides) demande de la levure chimique en grammes/sachets, ni de repère pour transformer une recette au levain en recette à la levure boulangère (ou l'inverse) pour quelqu'un qui n'a pas encore de levain actif. | faible |

## 2. Ce qui est déjà solide (vérifié, pas un point à corriger)

- **Dépannage boulangerie-pâtisserie déjà très complet dans `lib/rescue.ts`** : pâte qui ne lève pas (« pièce trop froide ou levure inactive »), pâte collante, choux retombés, fond de tarte rétréci/détrempé, blancs qui ne montent pas, chantilly qui ne monte pas ou tourne en beurre, caramel cristallisé ou brûlé, chocolat figé/tempérage raté, gâteau cru ou sec (pour les gâteaux au sens strict) — vérifié avant d'écrire ce document pour ne pas re-signaler ce qui existe déjà.
- **Tourage et feuilletage** : la fiche technique « Pâte levée feuilletée (croissants) » (`techniques2.ts`) liste précisément les deux pannes classiques (« beurre qui coule à la cuisson », « couches soudées ») ; les fiches `croissants` et `pains_chocolat` sont bien reliées à la technique « Tourage », donc ce rattrapage apparaît réellement dans leur « Si ça ne se passe pas comme prévu ».
- **Levain** : une technique dédiée « Levain maison » existe (`techniques2.ts`), et `pain_campagne_levain` y est bien relié (`techniques: ["Levain", ...]`) — un amateur qui n'a pas de levain actif trouve l'explication depuis la fiche, pas seulement l'ingrédient supposé acquis.
- **Pesée en grammes** : vérifié sur les 45 fiches de `/pains`, aucune ligne de farine n'est donnée en tasses/cup/verre — toutes en grammes, ce qui compte pour une pâte sensible au ratio eau/farine.
- **Équivalences levure sèche/fraîche et farines par type (T45 à T80+)** données clairement dans le calculateur de pâte.

## 3. Pourquoi ce sont des angles morts

Les constats n°1 et 2 touchent exactement le moment où un amateur abandonne : une pâte qui semble ne pas avoir levé
après le temps annoncé (alors qu'elle a juste besoin de plus de temps dans une cuisine froide) ou une brioche sèche
qu'on ne sait pas rattraper donnent l'impression d'avoir raté la recette, alors que ce sont des pannes connues et
rattrapables — l'application sait déjà le dire pour un gâteau ou un pain classique, mais pas pour une pâte briochée,
qui est justement la plus technique de ce corpus (beurre incorporé, hydratation précise, sensible à la température).
Le constat n°3 est le même problème que les coins Marinades et Sauces avant leur réorganisation du 21/11 : une
rubrique qui mélange tout sans classement renvoie un amateur débutant vers une recette trop technique par hasard,
faute de repère.

## 4. Pistes de correction (non appliquées)

- **#1** : ajouter un repère visuel (« la pâte a doublé de volume », « elle rebondit lentement au doigt ») à la fin
  des 15 étapes de pousse qui n'en ont aucun, en plus de la durée déjà donnée — comme déjà fait pour les 11 autres
  fiches et pour l'apprêt des croissants.
- **#2** : élargir la regex de la carte « Le gâteau est sec » (`rescue.ts`) pour inclure les mots « brioche »,
  « kougelhopf », « pain au lait », « cannelle » (kanelbullar, cinnamon rolls) — ou créer une carte dédiée « La
  brioche est sèche » si la cause/le rattrapage diffère assez d'un gâteau (farinage excessif au façonnage, four trop
  chaud pour une pâte enrichie qui dore vite).
- **#3** : ajouter des puces de filtre par famille sur `/pains` (pains du quotidien / pains levés / viennoiserie
  feuilletée / brioche sucrée / crêpes et pâtes à frire / bases et pizza), sur le modèle de `Marinades.tsx` et
  `Sauces.tsx`.
- **#4** : ajouter au calculateur de pâte une note d'équivalence levure chimique (en grammes selon le poids de
  farine) et un repère pour adapter une recette au levain vers la levure boulangère (quantité approximative) pour
  qui n'a pas encore de levain actif.

## 5. Corrigé (commit 2026-11-22)

- **#1** : `bible/complements_patisserie.py` (nouveau, même schéma que `complements_pro.py`) — toute étape de pousse
  (« pousse », « apprêt », « lève »/« laisse lever ») qui n'avait encore aucun repère visuel reçoit « Repère plus
  fiable que l'heure : la pâte a doublé de volume et rebondit lentement quand tu l'enfonces du doigt. », en plus de
  la durée déjà donnée (jamais à la place). 57 étapes complétées à l'export (plus que les 15 fiches `/pains`
  estimées à la main, car la détection s'applique à toute pâte levée de l'appli, pas seulement cette rubrique).
- **#2** : `lib/rescue.ts` — nouvelle carte dédiée « La brioche est sèche au démoulage » (`brioche|kougelhopf|pain au
  lait|kanelbullar|cinnamon roll|cannelle`), avec une cause et un rattrapage propres à la pâte enrichie (farinage
  excessif au façonnage, four trop chaud qui dore et dessèche plus vite) plutôt que d'élargir la carte « gâteau sec »
  dont le rattrapage (sirop, crème anglaise) ne convient pas à une brioche.
- **#3** : nouveau `lib/pains.ts` (même schéma que `sauces.ts`/`marinades.ts`) classant les 45 fiches en 6 familles
  (pains plats & sans levain 15, pains levés classiques 12, viennoiserie feuilletée 2, brioche & pâte enrichie 4,
  crêpes/gaufres/pâtes à frire 5, bases/pizza/pâte salée 7) ; `Pains.tsx` affiche des puces de filtre par famille,
  sur le modèle de `Marinades.tsx`/`Sauces.tsx`.
- **#4** : `DoughCalc` (`Pains.tsx`) — note ajoutée sur l'équivalence levure chimique (≈ 1 sachet/11 g pour 500 g de
  farine, mélangée à sec) et sur le remplacement d'un levain pas encore actif par de la levure boulangère (≈ 1 % du
  poids de farine en sèche, pousse 3 à 4 fois plus courte).
