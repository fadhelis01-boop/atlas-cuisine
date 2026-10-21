# Audit d'ATLAS : développement, UI et UX (21 octobre 2026)

> **Regard :** développeur senior et ingénieur UI/UX.
> **Version auditée :** commit da4760a, 954 recettes, 87 contrôles.
> **Méthode :** tout ce qui est chiffré a été mesuré.
> - **Navigateur intégré** sur la version de production, en format téléphone (375 × 812), thème clair puis sombre.
> - **Accessibilité :** axe-core 4.10 (WCAG 2.0 à 2.2 AA et bonnes pratiques).
> - **Écrans :** mesures sur 21 écrans, avec les mêmes critères que l'audit UX du 16/10 pour pouvoir comparer.
> - **Code :** lecture du code, poids réel du build et du dépôt.
>
> **Non mesuré :** les performances sur un vrai téléphone d'entrée de gamme. Les estimations sont signalées comme telles.

---

## Verdict en une phrase

ATLAS est une PWA soignée : hors connexion fiable, contrastes conformes en clair comme en sombre, mode cuisine exemplaire, aucun `innerHTML`. Mais elle a grossi plus vite que son architecture :
- le démarrage pèse **+32 %** depuis le 16/10 ;
- la fiche recette est passée de **5,6 à 9,7 écrans** ;
- la fonction phare, « Ma semaine », est rangée sous l'onglet « Frigo ».

Quatre défauts touchent directement la personne qui cuisine : l'écran qui s'éteint en plein mode cuisine, les portions perdues par le bouton « Cuisiner » sur tablette et ordinateur, des liens importés non filtrés, et une navigation muette pour les lecteurs d'écran.

---

## 0. Ce qui a été mesuré

### Poids et démarrage

| Mesure | 16/10 | 21/10 | Lecture |
|---|---|---|---|
| JavaScript chargé au démarrage (compressé) | 423 Ko | **557 Ko** (index 161 + engine 396) | +32 % ; 2,6 Mo de JavaScript à analyser |
| Recettes embarquées au démarrage | 576 fiches | 954 fiches, **1,9 Mo** sous forme de littéral JavaScript | Le coût croît avec chaque recette ajoutée |
| Analyse des recettes (machine de bureau) | — | 14 ms en littéral JS, 6 ms en `JSON.parse` | Sur un téléphone d'entrée de gamme, estimé 10 à 20 fois plus |
| Fichiers chargés à la demande | — | imports 134 Ko, crédits 79, vidéos 68, dictionnaire 67, restes 62 (compressés) | ✅ Bien découpé |
| Photos dans `app/public/img` | — | **469 Mo** (1 570 photos × 3 tailles × WebP + AVIF) | Publiées telles quelles sur GitHub Pages (limite : 1 Go) |
| Dépôt `.git` | — | **455 Mo** | Chaque photo remplacée s'y ajoute pour toujours |

### Écrans (téléphone, 375 px)

| Écran | Longueur (écrans) | Éléments cliquables | Cibles < 44 px | Textes < 14 px | Nœuds DOM |
|---|---|---|---|---|---|
| Accueil | 6,2 (4,7 le 16/10) | 113 | 1 | 33 | 1 223 |
| **Fiche recette** (blanquette) | **9,7 (5,6 le 16/10)** | 97 | **33** | 33 | 891 |
| Mode cuisine | 1,2 | 7 | 0 | 0 | — |
| Ma semaine | 2,5 | 24 | 1 | 7 | 166 |
| Frigo | 9,0 | 65 | 4 | 3 | 641 |
| Mes recettes | 4,2 | 41 | **28** | 0 | 214 |
| Profil | 6,6 | 79 | 60 (des cases à cocher dans leur libellé, donc faux positif) | 1 | 294 |
| Fêtes | 4,6 | 282 | 29 | **45** | **4 077** |
| Pique-nique | 10,3 | 81 | 34 | 3 | 739 |
| Zéro déchet | 11,0 | 92 | 11 | 3 | 653 |
| Explorer / Recherche « poulet » / Techniques / Dictionnaire | 8,7 / 7,7 / 5,7 / 4,3 | 37 / 68 / 127 / 75 | 2 / 9 / 6 / 1 | 15 / 0 / 3 / 24 | ≤ 600 |

- **Aucun débordement horizontal**, un seul `h1` par page.
- **Contrastes conformes** en thème clair et en thème sombre (axe : 0 défaut sur 7 écrans).
- **Le titre de l'onglet** est « ATLAS Cuisine » sur **toutes** les pages.

### Accessibilité automatisée (axe-core, 10 écrans)

Quatre défauts seulement, ce qui est un très bon score :
- **Mode cuisine :** le lien d'évitement pointe vers une cible absente, et du contenu est hors repère (*landmark*) ;
- **Frigo :** le sélecteur `.seg` a un rôle ARIA dont les enfants ne sont pas autorisés (critique pour un lecteur d'écran) ;
- **Profil :** le journal d'erreurs (`pre`) défile mais n'est pas atteignable au clavier.

### Robustesse

- **Recette disparue.** Une recette disparue (identifiant inconnu), placée dans la semaine, les favoris et le carnet, ne casse aucune page. Elle est ignorée en silence. ✅
- **Filet de sécurité.** Une `ErrorBoundary` et un journal d'erreurs local sont en place. ✅
- **Code sûr.** Pas d'`innerHTML`, pas d'`eval`. Les lecteurs vidéo n'acceptent que YouTube (nocookie) et TikTok. ✅

---

## 1. P0 : ce qui gêne ou expose aujourd'hui

### 1.1 L'écran s'éteint pendant la cuisson
> **Erratum (mise en œuvre, §8) :** constat faux. Le mode cuisine demandait déjà l'écran allumé (`useWakeLock`) ; ma recherche avait été tronquée. Le vrai manque était le cas où le téléphone ne le permet pas : il est traité au §8.
Aucune utilisation de l'API **Screen Wake Lock** dans le code. La personne a les mains dans la farine ; au bout de 30 s à 2 min, selon le téléphone, l'écran s'éteint au milieu d'une étape. C'est le défaut le plus ressenti d'une appli de cuisine, et le plus simple à corriger.

*À faire :* `navigator.wakeLock.request("screen")` à l'ouverture du mode cuisine, à redemander au retour au premier plan (`visibilitychange`), à relâcher en sortant. Repli silencieux si le navigateur ne le prend pas en charge. La fonction est disponible sur Safari iOS 16.4 et plus, ainsi que sur Chrome Android.

### 1.2 Bogue : « Cuisiner pas à pas » perd les portions
- La barre collante du bas ouvre `/cuisine/<id>?portions=N`.
- Le grand bouton du corps de la fiche (`RecipePage.tsx:225`) ouvre `/cuisine/<id>` **sans les portions**.

Sur téléphone, ce bouton est masqué et la barre du bas est correcte. Mais à partir de 900 px de large (tablette en paysage, ordinateur), c'est **le seul** bouton « Cuisiner ». Si on passe à 6 personnes dans les ingrédients puis qu'on lance le mode cuisine, celui-ci affiche les quantités d'origine. On cuisine alors pour 4 en croyant cuisiner pour 6, justement sur la tablette posée sur le plan de travail.

*À faire :* un seul constructeur de lien pour les deux boutons, et un contrôle dans le test de rendu.

### 1.3 Sécurité : liens importés non filtrés
Le lien d'une recette importée (`Imports.tsx`, `doSave`) est enregistré tel que collé. Il est ensuite affiché en `<a href={i.url}>` dans Mes imports, Mes recettes et le lecteur vidéo. La restauration d'une sauvegarde (`importData`) ne vérifie que la présence d'un champ `profile`.

- **Scénario.** Un fichier de sauvegarde transmis par un proche ou trouvé en ligne contient `javascript:…`. Un clic exécute alors du code dans l'origine d'ATLAS.
- **Conséquence.** Ce code peut lire tout l'état local, dont les **allergies et le régime**, des données sensibles (Tome 1 §19.1). React 18 avertit mais n'empêche pas ce type de lien.

*À faire :*
1. Un utilitaire `safeHref()` (http/https seulement) à chaque rendu de lien externe.
2. Le même filtre à l'enregistrement d'un import et d'une vidéo.
3. Une validation de structure à la restauration : types, listes bornées, liens filtrés, avec un aperçu avant d'écraser.
4. Une **Content-Security-Policy** en `<meta>` (GitHub Pages ne permet pas d'en-têtes) : `default-src 'self'`, `frame-src` limité à YouTube nocookie et TikTok, `connect-src` limité aux trois services oEmbed, `img-src 'self' data:`.

### 1.4 Navigation muette pour les lecteurs d'écran
Le routeur par ancre (`router.ts`) remonte en haut de la page. Mais il ne donne **pas de titre** à la page, ne **déplace pas le focus** et **n'annonce rien**. Avec VoiceOver ou TalkBack, toucher un onglet ne dit pas que l'écran a changé. Les onglets du navigateur, l'historique et l'appli installée affichent tous « ATLAS Cuisine ».

*À faire :*
- `document.title = "<titre de la page> · ATLAS"` à chaque écran ;
- focus sur le `h1` (`tabIndex={-1}`) après un changement d'écran, sauf au retour arrière (on garde la position) ;
- une région `aria-live` qui annonce le titre.

---

## 2. P1 : ce qui freine la croissance ou l'usage

### 2.1 Le démarrage grossit avec chaque recette
Les 954 fiches complètes, avec leurs étapes, conseils, variantes et vidéos, sont dans le JavaScript de démarrage. La page d'accueil n'en affiche qu'une dizaine. À ce rythme, 1 500 recettes feraient environ 800 Ko compressés et 4 Mo à analyser. C'est plusieurs secondes de blocage sur un téléphone à 150 €, au premier lancement comme après chaque mise à jour.

*À faire :*
1. Un **index léger** au démarrage : ce qu'il faut pour les cartes, la recherche et le planificateur (titre, région, temps, niveau, badges, ingrédients référencés). C'est environ 25 % du poids actuel.
2. Le **détail d'une fiche** (étapes, conseils, variantes) chargé à la demande, par région, en JSON lu par `JSON.parse` (deux fois plus rapide qu'un littéral). Le service worker continue de tout mettre en cache pour le hors connexion.
3. Un **budget de poids** dans la CI : le build échoue au-delà de 450 Ko compressés au démarrage.

### 2.2 La fiche recette est redevenue trop longue (9,7 écrans)
Ordre actuel, mesuré en écrans depuis le haut :
- **0 à 1,5 :** photo, crédit, titre, vidéo, badges, 5 actions, avertissement « non testée », introduction ;
- **1,5 :** ingrédients ;
- **2,5 à 3,2 :** zéro déchet, 7 encadrés **entre** les ingrédients et les étapes ;
- **3,5 :** étapes ;
- **6,3 :** finition ;
- **6,9 :** six « Si ça rate » ;
- **7,6 :** astuces du chef ;
- **7,9 :** pour recevoir.

Défauts :
- **Astuces mal placées.** Les astuces du chef, le meilleur du contenu, arrivent **après** le dépannage.
- **Coupure entre ingrédients et étapes.** Le zéro déchet sépare les deux ; on fait défiler en cuisinant.
- **Rangée d'actions cassée.** Elle passe sur deux lignes à 375 px : « Partager » reste seul à la ligne.
- **Barre de mise à jour.** Elle pousse tout le contenu vers le bas quand une version est disponible.

*À faire :*
- **Astuces** à la fin des étapes ;
- **zéro déchet et vidéo** repliés en une ligne chacun ;
- **crédit photo** dans une icône (i) sur la photo ;
- **les 5 actions** sur une ligne (icônes de 44 px, libellé court) ;
- **« Si ça rate »** en un seul bloc replié ;
- **la mise à jour** en toast discret.

Cible : ingrédients visibles au premier écran, fiche de 5 à 6 écrans.

### 2.3 Architecture de l'information : la semaine est cachée
- **Ma semaine sous Frigo.** « Ma semaine », la fonction la plus travaillée (planificateur, menus du dimanche, courses, restes), est rangée sous l'onglet **Frigo**. Sur l'écran Ma semaine, c'est l'icône du frigo qui s'allume.
- **Onglet faux ailleurs.** Restes, Pique-nique et Bien choisir n'appartiennent à aucun onglet, donc « Accueil » s'allume à tort.
- **Ratio.** 28 écrans pour 5 onglets.

*À faire :* repenser la barre autour des usages du quotidien.

| Onglet | Contenu |
|---|---|
| **Accueil** | Inchangé |
| **Explorer** | Recherche, rubriques, techniques |
| **Ma semaine** | Planning, courses, restes |
| **Frigo** | Frigo, placard, Bien choisir |
| **Mes recettes** | Favoris, carnet, imports |

Le **Profil** passe en icône dans l'en-tête. Chaque route reçoit un onglet explicite, sans « Accueil » par défaut.

### 2.4 Données locales : quatre fragilités
1. **Pas de version de schéma.** La clé `atlas-state-v1` n'a jamais changé alors que l'état a gagné 8 champs. Tout repose sur des champs facultatifs. Le jour où un champ change de forme (par exemple `week` en tableau), rien ne permet de migrer.
2. **Deux onglets s'écrasent.** Aucune écoute de l'événement `storage`. La liste de courses cochée dans un onglet est écrasée par l'autre.
3. **Restauration sans filet.** Elle remplace tout sans aperçu, et ne fusionne pas.
4. **Copie complète à chaque geste.** Chaque action copie **tout l'état** (`structuredClone`), imports compris. Le coût grandit avec l'usage, et l'écriture complète dans `localStorage` aussi.

*À faire :*
- un champ `version` avec une fonction de migration testée ;
- une synchronisation par l'événement `storage` (ou `BroadcastChannel`) ;
- une restauration en deux temps : aperçu, puis fusion ou remplacement ;
- une copie limitée à la branche modifiée.

### 2.5 Safari peut effacer les données d'un site non installé
Sur iPhone, Safari efface le stockage d'un site **non ajouté à l'écran d'accueil** après 7 jours sans visite (politique ITP). `askPersistence()` n'y change rien. Une personne qui utilise ATLAS dans Safari, sans l'installer, peut perdre favoris, carnet et semaine après des vacances.

*À faire :* sur iOS non installé, proposer l'installation une fois données personnelles présentes, avec le pas à pas (Partager → « Sur l'écran d'accueil »). Garder le rappel de sauvegarde à 30 jours.

### 2.6 Dépôt et publication
- **Publication.** Elle recrée une branche `gh-pages` neuve à chaque fois (`deploy.mjs`) et pousse en force. Les 469 Mo de photos sont probablement renvoyés à chaque publication, faute d'historique commun.
- **Format de photo.** WebP **et** AVIF en trois tailles doublent le volume, alors que tous les navigateurs ciblés lisent l'AVIF.
- **Croissance.** Le dépôt `.git` (455 Mo) grossit à chaque photo remplacée.

*À faire :*
- garder l'historique de `gh-pages` (cloner la branche, copier `dist`, un commit par publication) ;
- ne publier que l'AVIF en 400 et 800, plus le WebP 400 en secours ;
- sortir les originaux et les candidates du dépôt ;
- surveiller la limite de 1 Go de GitHub Pages.

### 2.7 Angle mort produit : la cuisine se fait à deux
La liste de courses et la semaine vivent sur **un seul téléphone**. Dans un foyer, l'un planifie et l'autre fait les courses. Le partage actuel est du texte (WhatsApp), qu'on ne peut ni cocher ni mettre à jour.

*À faire, sans serveur et fidèle au « rien ne quitte le téléphone » :*
- **un lien de partage** qui encode la liste de courses ou la semaine dans l'URL (compressée), à ouvrir et fusionner sur l'autre téléphone ;
- **un export calendrier** (`.ics`) de la semaine.

---

## 3. P2 : finitions

1. **Cache photos jamais vidé.** `atlas-img-v1` ne change pas d'une version à l'autre. Une photo **remplacée** sous le même nom reste l'ancienne chez les utilisateurs. *À faire :* un suffixe de version dans le nom du fichier (`-v2`) quand on remplace une photo.
2. **Journal d'erreurs bruité.** Les échecs de mise à jour du service worker (réseau coupé) y sont enregistrés comme des erreurs et noient les vraies. *À faire :* les filtrer.
3. **Cibles et textes.**
   - Listes de liens de 21 px de haut : « À tester en priorité » dans Mes recettes (28), liens d'ingrédients de la fiche.
   - Crédits des menus de Fêtes : liens de 16 px et textes de 12 px (45 textes < 14 px).
   - Étiquettes zéro déchet et noms du marché de l'accueil en 13 px.
   *À faire :* des lignes de liste de 44 px, et un plancher de 14 px hors mentions légales.
4. **Défauts axe.** Les quatre défauts du §0 : cible du lien d'évitement en mode cuisine, rôle ARIA du sélecteur du Frigo, `pre` du journal sans `tabIndex`.
5. **Impression.** La feuille d'impression ne cache que 5 éléments anciens. La barre collante, les toasts, la bannière de mise à jour, les vidéos et le zéro déchet s'impriment. Il n'y a ni bouton « Imprimer » ni mise en page « fiche » ou « liste de courses ». Beaucoup de familles impriment encore la liste.
6. **Aperçu des liens partagés.** Aucune balise `og:` ni `twitter:`. Un lien ATLAS envoyé sur WhatsApp n'a ni image ni description. Le routage par ancre empêche un aperçu par recette, mais une image et une description générales sont possibles.
7. **Recette disparue en silence.** Un favori ou un plat planifié dont la recette a été renommée disparaît sans un mot. *À faire :* une table de renommage (ancien → nouvel identifiant) à l'export, et un message « 1 recette n'existe plus ».
8. **Animations.** Les photos apparaissent en fondu (250 ms) sur un fond vide. La couleur dominante, déjà calculée pour chaque photo (`images.json`, champ `color`), pourrait servir de fond d'attente et éviter l'effet « trou » au défilement rapide.

---

## 4. Code et outillage

| Constat | Mesure | Recommandation |
|---|---|---|
| TypeScript strict, aucune dépendance d'exécution hors React | ✅ | À garder |
| Lignes de plus de 200 caractères | **632 sur 7 481 (8 %)**, surtout du JSX dense | Formateur (Prettier ou Biome) en vérification CI ; extraire les sous-composants des pages de plus de 250 lignes (RecipePage 385, Home 285, Imports 265) |
| Tests du moteur | 87 contrôles dans **un seul fichier de 474 lignes**, avec des variables globales partagées. Le 21/10, deux contrôles ont déclaré la même variable `plats`, et le build a échoué. | Un fichier par domaine (planificateur, menus, recettes, profils), chacun isolé ; garder le lanceur maison ou passer à Vitest |
| Test de rendu | 28 pages × 2 profils, **sans interaction** | Ajouter 5 parcours bout en bout (Playwright) : bienvenue → recette → portions → cuisiner ; semaine → courses ; frigo → recette ; import d'un lien ; sauvegarde → restauration |
| Dépendance `rolldown: "*"` | Version non épinglée dans `package.json` | Épingler la version (le fichier de verrouillage protège, mais une mise à jour libre pourrait casser le build) |
| Commentaires périmés | Exemple : `weekHistory`, « mémoire de 4 semaines » (8 en réalité), deux commentaires collés sur la même ligne dans `store.ts` | Relecture à chaque changement de règle |
| Données dupliquées | Le filtre d'acidité existe en Python (analyse) **et** en TypeScript (test 85) | Une seule source : l'export écrit le verdict, le test le lit |
| Budget de performance | Absent | Taille du démarrage et nombre de nœuds de la fiche contrôlés en CI |

---

## 5. Angles morts de la demande

1. **L'écran qui s'éteint** (§1.1) : aucun audit ne l'avait vu, parce qu'on teste à la souris sur un ordinateur.
2. **Le foyer à deux** (§2.7) : l'appli est pensée pour une personne, alors que les courses et la semaine se partagent.
3. **La perte de données sur iPhone** (§2.5) : une politique de Safari, invisible en développement.
4. **Le lecteur d'écran** (§1.4) : le score axe est excellent, mais le changement de page n'est jamais annoncé. Les outils automatiques ne testent pas un parcours.
5. **La croissance** (§2.1, §2.6) : chaque recette et chaque photo ajoutée alourdissent le démarrage et le dépôt. Rien ne s'arrête tout seul.
6. **Le partage sortant** (§3.6) : un lien sans aperçu donne peu envie d'être ouvert. C'est pourtant le premier canal pour se faire connaître.
7. **Ce qu'on ne mesure pas** : aucune donnée d'usage, et c'est un choix de confidentialité juste. Mais on ne sait pas quelles rubriques servent. *Proposition :* un compteur **local** des écrans ouverts, joint volontairement à l'export du carnet d'essais.
8. **Les vrais appareils** : rien n'a été mesuré sur un téléphone à 150 € en 4G. À faire une fois, avec Chrome à distance (`chrome://inspect`) : temps jusqu'à l'accueil, fluidité du défilement sur Fêtes (4 077 nœuds).
9. **La tablette et l'ordinateur** : non audités ici. La cuisine sur tablette posée sur le plan de travail est un usage courant ; le mode cuisine en paysage existe, le reste n'a pas été vérifié.

---

## 6. Ce qui est réussi

- **Hors connexion de bout en bout** : service worker versionné, mise à jour proposée, cache photos plafonné et levé si la personne télécharge tout.
- **Mode cuisine** : 7 boutons de 64 × 66 px, texte de 16 px, mise en place cochable, lecture vocale, commandes à la voix, minuteurs nommés avec notification et vibration.
- **Accessibilité de base** : contrastes conformes en clair et en sombre, mouvement réduit respecté, focus visible, taille de texte réglable, police lisible, textes alternatifs, cibles du mode cuisine.
- **Confidentialité réelle** : aucune donnée envoyée, journal d'erreurs local, régime et allergies sur l'appareil.
- **Robustesse** : identifiants orphelins ignorés, écriture groupée, avertissement si la mémoire est pleine, `ErrorBoundary`.
- **Chaîne de données** : la CI vérifie que l'application correspond exactement à la bible. C'est rare et précieux.
- **Ton** : le tutoiement chaleureux et les micro-textes restent constants.

---

## 7. Ordre de travail recommandé

| # | Quoi | Priorité | Effort |
|---|---|---|---|
| 1 | Écran allumé en mode cuisine (Wake Lock) | P0 | 1 h |
| 2 | Portions transmises par les deux boutons « Cuisiner » + test | P0 | 30 min |
| 3 | `safeHref`, filtre à l'import, validation de la restauration, CSP en `<meta>` | P0 | ½ jour |
| 4 | Titre de page, focus et annonce au changement d'écran | P0 | 2 h |
| 5 | Fiche recette resserrée (astuces, zéro déchet replié, actions sur une ligne, mise à jour en toast) | P1 | ½ jour |
| 6 | Barre d'onglets avec « Ma semaine », onglet juste pour chaque écran | P1 | ½ jour |
| 7 | Index léger + détail à la demande + budget de poids en CI | P1 | 1 à 2 jours |
| 8 | État local : version et migration, synchro entre onglets, restauration avec aperçu | P1 | 1 jour |
| 9 | Invitation à installer sur iPhone (risque d'effacement après 7 jours) | P1 | 2 h |
| 10 | Partage de la liste de courses et de la semaine par lien, export `.ics` | P1 | 1 jour |
| 11 | Publication incrémentale, AVIF seul en 2 tailles, originaux hors dépôt | P1 | ½ jour |
| 12 | Finitions P2 (cache photos versionné, journal filtré, cibles et textes, axe, impression, `og:`, table de renommage, fond de couleur des photos) | P2 | 1 jour |
| 13 | Outillage : formateur, tests découpés, 5 parcours Playwright, dépendance épinglée | P2 | 1 jour |
| 14 | Mesure sur un vrai téléphone d'entrée de gamme | P2 | 1 h |

---

## 8. Mise en œuvre (21 octobre 2026)

Les 14 chantiers du §7 et les angles morts du §5 sont traités. Chacun est vérifié par un contrôle automatique : tests 88 à 95, six parcours avec de vrais clics dans le test de rendu, budget de poids et cliquet de lisibilité au build.

### Erratum : trois constats de l'audit étaient faux

1. **Écran qui s'éteint (§1.1).** Le mode cuisine utilisait déjà Screen Wake Lock ; ma recherche avait été coupée trop tôt. Le vrai manque était le cas où le téléphone ne le permet pas (iPhone avant iOS 16.4, certains navigateurs). Le mode cuisine le signale maintenant, avec un conseil.
2. **Couleur d'attente des photos (§3.8).** Elle était déjà posée en fond, mais invisible parce que l'image restait transparente pendant le chargement. C'est corrigé.
3. **Originaux et candidates dans le dépôt (§2.6).** Ils étaient déjà exclus par `.gitignore`. Le poids de `.git` vient de l'historique des photos publiées. Le réécrire serait destructif et n'a pas été fait sans accord.

### Mesures avant / après

| Mesure | Avant | Après |
|---|---|---|
| JavaScript au démarrage (compressé) | 557 Ko | **372 Ko** (−33 %), plafond de 400 Ko contrôlé à chaque build |
| Fiche recette (blanquette, téléphone) | 9,7 écrans, ingrédients à 1,5 écran | **7,1 écrans**, ingrédients à 1,2 écran ; recettes courtes : 4,5 à 5 écrans |
| Défauts axe-core (11 écrans) | 4 | **0** |
| Photos publiées en ligne | 469 Mo (WebP + AVIF, 3 tailles) | **135 Mo** (AVIF 400/800 + WebP 400) ; 350 Mo de moins |
| Publication | Branche neuve poussée en force à chaque fois | Incrémentale : seuls les fichiers modifiés partent |
| Contrôles automatiques | 87 + rendu de 28 pages | **95** + 7 parcours avec clics + rendu de 28 pages × 2 profils |

**Cible non atteinte :** la fiche n'affiche pas encore les ingrédients dans le premier écran (1,2 écran). L'en-tête ne garde que l'utile : titre, temps, badges régime et allergènes, saison, mention « non testée », actions. Le reste est replié.

### Ce qui a été fait

**P0**
- **Mode cuisine.** Si le téléphone ne peut pas garder l'écran allumé, une note le dit et donne un conseil (`useWakeLock` renvoie son état).
- **Portions.** Un seul constructeur de lien (`cookHref`, `lib/nav.ts`) pour les deux boutons « Cuisiner ». Le bouton visible à partir de 900 px perdait les portions ; c'est vérifié par un parcours du test de rendu.
- **Sécurité.**
  - `lib/safe.ts` : `safeUrl` et `safeHref` (http et https seulement) à chaque lien saisi par l'utilisateur, et filtrage à l'enregistrement d'un import.
  - **Restauration en deux temps.** `sanitizeState` vérifie les types, borne les listes, refuse les liens douteux, les dates impossibles et les identifiants suspects, puis compte ce qu'il écarte. Un aperçu montre le contenu du fichier, puis on choisit : **ajouter à mes données** (fusion, le plus récent gagne) ou **tout remplacer**.
  - **Content-Security-Policy** posée à la compilation : scripts de l'origine seulement, pas d'`eval`, `object-src 'none'`, cadres limités à YouTube nocookie et TikTok, connexions aux trois services oEmbed. Vérifié : le lecteur YouTube fonctionne, et un script externe est bien bloqué.
- **Navigation accessible** (`lib/a11y.ts`).
  - Le titre de l'onglet devient « titre de la page · ATLAS ».
  - Le focus va sur le contenu après un changement d'écran (sauf au retour arrière), et l'écran est annoncé par une région `aria-live`.
  - Trouvé en route : le lien « Aller au contenu » ouvrait une page introuvable avec le routeur par ancre. C'est corrigé, et toutes les pages ont une cible focusable.

**P1**
- **Démarrage léger.** L'export écrit un **index** (cartes, recherche, moteur, planificateur) et un **détail** à part (étapes, introductions, vidéos, conseils, matériel, conservation). L'index est lu en `JSON.parse` ; le détail arrive juste après le premier affichage, et les écrans qui en ont besoin l'attendent. Le budget de poids (`scripts/budget.mjs`) fait échouer le build au-delà de 400 Ko.
- **Fiche recette resserrée.**
  - Les astuces du chef suivent les étapes.
  - Repliés : les gestes du métier (« Le geste : Roux »), le zéro déchet, les problèmes fréquents, « Bon à savoir » (conservation, enfants, boissons) et les vidéos.
  - Le crédit photo passe dans un bouton « i » sur la photo, l'introduction est limitée à 3 lignes avec « Lire la suite », et « Pas encore testée » devient un badge relié au carnet.
  - Les 5 actions tiennent sur une ligne, et la mise à jour disponible devient un message flottant.
- **Onglets.**
  - La barre devient Accueil · Explorer · **Ma semaine** (planning, courses, restes) · Frigo (frigo, Bien choisir) · Mes recettes.
  - Le Profil passe en bouton rond en haut à droite sur téléphone, et en bas de la colonne sur grand écran.
  - Chaque écran allume le bon onglet ; le test 93 vérifie toutes les routes.
- **État local.**
  - Version de schéma et migration testée.
  - Table des recettes renommées (`bible/renommages.py` → `renames.json`) suivie dans les favoris, le carnet, la semaine et l'historique.
  - Synchronisation entre onglets (événement `storage`).
  - Copie à la demande : seules les branches touchées sont recopiées ; le test 90 vérifie que les imports ne sont pas recopiés quand on coche un favori.
- **iPhone.** Une invitation à installer ATLAS, avec le pas-à-pas, apparaît dès 3 éléments personnels (au lieu d'attendre 30 jours sans sauvegarde), au plus une fois par mois.
- **Foyer à deux** (`lib/partage.ts`, écran `/partage`).
  - La liste de courses et la semaine voyagent **dans un lien** compressé : l'autre téléphone voit le contenu, puis l'ajoute sans écraser ce qu'il a.
  - La semaine s'exporte dans l'**agenda** (`.ics`).
  - Le lien reçu est vérifié comme une donnée extérieure.
- **Publication.**
  - `deploy.mjs` garde une copie de `gh-pages` avec son historique : seuls les fichiers modifiés partent.
  - `prune-photos.mjs` ne publie que l'AVIF 400/800 et le WebP 400.

**P2**
- **Photos.** Une photo retraitée reçoit un numéro de version dans son adresse, pour ne plus être servie depuis l'ancien cache. La couleur dominante est enfin visible pendant le chargement.
- **Journal d'erreurs** sans le bruit des mises à jour hors ligne.
- **Cibles et textes.** Lignes de liste de 44 px, textes à 14 px au moins hors mentions légales, liens de licence plus faciles à toucher, rôle ARIA du Frigo corrigé, journal d'erreurs atteignable au clavier.
- **Impression** de la fiche et de la liste de courses (liste en deux colonnes, articles cochés masqués), avec un bouton « Imprimer ».
- **Aperçu des liens partagés.** Balises `og:` et image 1200 × 630, composée à partir d'une photo CC0.
- **Recettes disparues.** Elles sont retirées des favoris et de la semaine avec un message ; les notes du carnet sont gardées.

**Outillage**
- **Tests découpés** en cinq suites isolées (`tests/e1` à `e5`) et un socle commun (`tests/helpers.ts`) : deux contrôles ne peuvent plus se télescoper.
- **Sept parcours avec clics** dans le test de rendu :
  - portions transmises au mode cuisine ;
  - titre et focus après un changement d'écran ;
  - lien d'évitement ;
  - semaine envoyée dans la liste de courses ;
  - liste reçue par lien puis ajoutée ;
  - onglet juste.
  - titre de l'onglet à la sortie de l'accueil de bienvenue (défaut trouvé en vérifiant le site publié).
- **Cliquet de lisibilité** (`scripts/lignes.mjs`) : le nombre de lignes de plus de 200 caractères ne peut que baisser (621 aujourd'hui, surtout des textes de techniques et de restes).
- **`rolldown` épinglé**, avec une configuration de tests qui reproduit l'import `?raw` de Vite.

**Angles morts**
- **Rubriques utilisées.** Un compteur local, visible dans le Profil, joint à l'export du carnet seulement si la case est cochée ; rien n'est envoyé.
- **Mesure sur l'appareil.** ATLAS chronomètre sa propre ouverture sur le téléphone de la personne, et le Profil affiche la moyenne. C'est la seule mesure honnête sur un téléphone à 150 €.
- **Tablette et ordinateur vérifiés** : aucun débordement, colonne de navigation avec le Profil en bas, bouton « Cuisiner » avec les portions.

### Reste ouvert
- **Historique Git.** Le dossier `.git` pèse 455 Mo à cause des photos des versions passées. Le réduire suppose de réécrire l'historique (destructif) : à décider par le propriétaire.
- **Mesure sur un vrai téléphone d'entrée de gamme.** L'outil est en place (Profil › Sur cet appareil), il faut ouvrir ATLAS sur un tel appareil.
- **Ingrédients au premier écran** sur téléphone (voir plus haut).

