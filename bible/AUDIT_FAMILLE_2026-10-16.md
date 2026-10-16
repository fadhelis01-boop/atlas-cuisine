# Audit d'ATLAS : un parent de deux enfants, une ingénieure UI/UX, un développeur (16 octobre 2026)

Trois regards sur la version en ligne (912 recettes, 70 contrôles). Le premier est celui d'un parent qui cuisine en amateur pour deux enfants, le soir après le travail. Les deux autres sont ceux d'une ingénieure UI/UX et d'un développeur senior. Méthode : parcours réels sur téléphone (375 × 812, version publiée), 20 semaines de menus simulées pour un foyer avec un enfant de 4 ans, contrôle d'accessibilité automatisé sur cinq pages, lecture du code et mesure du poids de l'application. **Rien n'est corrigé dans ce document** : c'est un état des lieux avec des priorités.

Priorités : **P0** = faux ou risqué, à corriger d'abord ; **P1** = gêne réelle au quotidien d'une famille ; **P2** = amélioration.

## 1. Ce qui marche déjà bien

- **Accessibilité de base solide**, mesurée sur l'accueil, une fiche, la semaine, le frigo et les restes :
  - aucun bouton sans nom, aucune image sans texte alternatif, aucun champ sans étiquette ;
  - un seul titre principal par page, pas de défilement horizontal ;
  - zones tactiles de 44 px partout, sauf le lien d'évitement (visible au clavier seulement) et les liens dans le texte, tolérés par les règles WCAG.
- **Mode cuisine lisible d'une main.** Grosses cases à cocher, sel dosé, boutons Retour / Lire / À la voix / Suivant en bas d'écran, écran maintenu allumé.
- **Profil sérieux.** Sans porc, sans alcool (avec un mode « strict »), 14 allergènes, mode strict en cas de doute, rappel honnête que l'appli signale mais ne certifie pas.
- **Page Enfants utile.** Règles de sécurité justes (miel, sel, étouffement, œuf cru, alcool même cuit) et gestes adaptés à chaque âge pour cuisiner ensemble.
- **Automatisation fiable.** Les dernières exécutions des contrôles et du déploiement sont toutes vertes.

## 2. Le regard du parent

### P0 – La semaine planifiée ignore les enfants
Simulation : 20 semaines, midi et soir, foyer avec un enfant de 4 ans (280 repas).
- **43 repas sur 280 (15 %) sont épicés** : le planificateur ne tient compte ni de l'âge du plus jeune enfant, ni du profil « épicé ».
- **85 recettes épicées sont marquées « dès 1 à 3 ans »**. Beaucoup expliquent comment adapter (dal sans piment), mais d'autres non : poulet kung pao, « ✓ dès 3 ans », sans un mot sur le piment du Sichuan. La recherche « dîner rapide enfants » le propose en huitième position.
- **Le marquage d'âge ne trie plus rien** : 815 recettes sur 912 sont « dès 4 ans ou moins ». Pour un parent, ça ne répond pas à la vraie question : est-ce que mes enfants vont manger ça ?

### P0 – Déséquilibre de la semaine
Le jeu « le reste d'hier sert aujourd'hui » l'emporte sur l'équilibre. Semaine réellement proposée :
- moules-frites, curry japonais, tartiflette, raclette, bacalhau ;
- soit cinq soirs de suite avec de la pomme de terre, dont tartiflette puis raclette ;
- et aucune légumineuse.

Aucun repère de base n'est vérifié : légumes à chaque repas, poisson deux fois par semaine, légumineuses deux fois, fromage fondu au plus une fois.

### P1 – La semaine remplit des jours passés
Un vendredi, « Cette semaine » affiche et remplit lundi à jeudi, alors que la page promet « les repas des 7 prochains jours ». Les plats de ces jours passés finissent même dans la liste de courses.

### P1 – Le foyer n'existe pas vraiment
- **Taille du foyer.** Le profil ne connaît que « l'âge du plus jeune enfant ». La semaine démarre à **2 personnes**. Chaque fiche s'ouvre sur son propre nombre de parts : 400 fiches pour 4 personnes, 250 pour 6, 91 pour 8.
- **Repas des enfants.** Il n'existe aucune notion de portion enfant (une demi-portion adulte jusqu'à 10 ans environ), donc les courses d'une famille de quatre sont surévaluées.
- **Âges des enfants.** Deux enfants d'âges différents ne se déclarent pas. Le plus jeune fixe tout, ce qui est prudent, mais rien n'est prévu pour l'aîné.
- **Allergie d'un seul enfant.** Elle exclut la recette pour toute la famille, sans possibilité de dire « on fait la version sans noix pour lui ».

### P1 – L'accueil n'aide pas le soir de semaine
- **Menu du jour.** Un jeudi soir, il propose un soto ayam, puis un cassoulet en **4 h 40**, puis une compote. Le haut de page s'adapte à l'heure (« L'heure du goûter »), mais le menu du jour ignore le jour et le temps disponible.
- **Bienvenue.** L'écran d'accueil pose la question des restrictions, pas celle du foyer (combien de personnes, âge des enfants). Le réglage existe mais reste caché dans le profil.

### P1 – Les besoins des parents qu'on ne trouve pas
- **Lunchbox.** « lunchbox » ne donne aucun résultat. Seules 6 fiches parlent de pique-nique, de boîte ou de bento, et aucune rubrique « gamelle du midi » ou « goûter à emporter » n'existe.
- **Enfant difficile.** « enfant difficile légumes » ne donne rien, alors que la fiche *pâtes à la sauce aux légumes cachés* existe. La recherche manque de synonymes de parents : légumes cachés, picky, cantine, mercredi, goûter d'école, anniversaire.
- **Cuisine d'avance.** Seules 68 fiches indiquent qu'elles se congèlent. Il n'existe ni « session de cuisine du dimanche », ni repère « se double et se congèle » sur les fiches.
- **Budget de la semaine.** Les fiches portent un indicateur €, €€ ou €€€, mais la semaine ne donne aucune estimation de coût.

### P2 – Les sauces à la mayonnaise crue
La page Enfants dit à juste titre « pas d'œuf cru (mayonnaise…) pour les jeunes enfants ». Les sauces tartare, cocktail et curry sont marquées « dès 3 ans avec la version sans œuf cru ». Cette version n'existe qu'en texte : ce n'est pas une variante qu'on peut choisir, ni que le profil applique tout seul.

## 3. Le regard UI/UX

### P0 – « Pâtisserie & chocolat » affiche des plats salés
Sur l'accueil, la rangée « Pâtisserie & chocolat » montre des tartines de labneh, des muffins aux œufs, un congee et un breakfast burrito. Le code prend « la 3ᵉ envie » de la liste. Quand l'audit UX précédent a ajouté « Express » et « Brunch » en tête, la 3ᵉ est devenue « Brunch » (`Home.tsx`, `CRAVINGS[2]`).

### P1 – Recherche : ordre et rattrapage
- « Rien trouvé » s'affiche **avant** « Compris : pour les enfants · « difficile legumes » » : on lit l'échec avant de voir ce qui a été compris.
- Quand une partie de la phrase n'est pas reconnue, l'appli ne tente pas de garder seulement les intentions comprises (ici, « pour les enfants » donnerait des résultats).

### P1 – Bienvenue et profil
- La bienvenue renvoie au profil « (enfants, équipement…) » sans donner d'accès direct.
- L'équipement ne propose ni **autocuiseur**, ni **micro-ondes**, ni **mijoteuse**, alors que les 23 nouveaux mijotés donnent la cuisson à l'autocuiseur et parfois à la mijoteuse.

### P2 – Détails visibles
- **Chiffre périmé.** La page Profil, section « À propos », annonce « 61 contrôles automatiques » ; il y en a 70.
- **Icônes de remplacement.** Une émoticône subsiste dans l'interface (« 🔊 Tester la voix »). 124 fiches sans photo affichent une icône dessinée, conforme à D19 (pas d'image générée), mais dans une rangée elles se distinguent nettement des photos.
- **Bandeau de mise à jour.** « Une nouvelle version d'ATLAS est prête » est apparu juste après une première visite, cache vidé. C'est sans gravité mais déroutant ; à vérifier.
- **Mode cuisine.** Il s'ouvre sur le nombre de parts de la fiche (6 pour le hachis Parmentier), pas sur celui du foyer.

## 4. Le regard du développeur

### P0 – Risque de perte des données sur iPhone
Tout est dans `localStorage` : favoris, carnet, semaine, frigo, restes, profil.
- **Pas de stockage persistant.** L'appli ne demande pas `navigator.storage.persist()`.
- **Effacement automatique.** Safari efface les données d'un site non installé qui n'a pas été ouvert depuis 7 jours. Un parent qui n'ouvre pas l'appli pendant les vacances peut tout perdre.
- **Échec silencieux.** Quand le stockage est plein, l'erreur est avalée (`store.ts`, ligne 75) sans prévenir l'utilisateur.
- **Sauvegarde à la main.** L'export existe, mais rien n'invite à sauvegarder.

### P1 – Poids au démarrage
- **Avant le premier affichage :** environ **580 Ko compressés**, soit 2,7 Mo de JavaScript à analyser :
  - les données des recettes (2,16 Mo, 418 Ko compressés), préchargées ;
  - le cœur de l'appli (520 Ko, 165 Ko compressés).
- **Effet :** sur un téléphone d'entrée de gamme en 4G moyenne, comptez plusieurs secondes à la première ouverture. Les visites suivantes sont rapides grâce au cache (première peinture mesurée à 120 ms).
- **Piste :** charger les recettes en JSON (plus rapide à lire que du JavaScript) et par région, ou un index léger plus les fiches à la demande.

### P1 – Les tests ne voient pas l'interface
Les 70 contrôles testent la logique (moteur, planificateur, données), jamais l'affichage. Deux défauts réels sont passés à travers :
- la rangée « Pâtisserie » de l'accueil ;
- la page Restes qui bouclait à l'infini (un sélecteur qui renvoyait un nouveau tableau vide à chaque rendu), repérée seulement en ouvrant la page dans le navigateur, le jour même.

Un test de fumée qui ouvre chaque page et vérifie qu'aucune erreur ne remonte aurait attrapé les deux.

### P1 – Code fragile
- **Index en dur.** `CRAVINGS[2]` dépend de l'ordre de la liste : il faut désigner l'envie par son identifiant.
- **Âge des enfants.** Il est écrit à la main sur chaque fiche (« ✓ dès 3 ans »), sans lien avec le profil « épicé » ni avec les ingrédients (piment, œuf cru, fruits à coque entiers). Un contrôle croisé automatique éviterait les incohérences de la section 2.
- **Sauvegarde à chaque modification.** Tout l'état est réécrit dans `localStorage` à chaque changement, y compris les imports de vidéos, qui peuvent être volumineux.

### P2 – Divers
- Les minuteurs ne sonnent pas application fermée sur iPhone : c'est documenté, mais c'est le premier piège d'un parent qui lance une cuisson longue puis s'occupe des enfants.
- Le contrôle de cohérence des données (export de la bible vers l'appli) est en place dans l'automatisation : c'est bien.

## 5. Ordre de travail recommandé

| # | Quoi | Priorité | Effort |
|---|---|---|---|
| 1 | Rangée « Pâtisserie » : viser l'envie par son identifiant | P0 | 10 min |
| 2 | Sécuriser les données : `storage.persist()`, alerte si l'écriture échoue, rappel de sauvegarde mensuel, invitation à installer l'appli sur iPhone | P0 | ½ jour |
| 3 | Semaine famille : partir d'aujourd'hui, nombre de personnes repris du profil, exclusion des plats épicés et des plats non adaptés quand un enfant de moins de 6 ans est déclaré | P0 | 1 jour |
| 4 | Équilibre de la semaine : au plus 2 répétitions d'un même féculent, poisson 2 fois, légumineuses 2 fois, fromage fondu 1 fois ; l'enchaînement des restes passe après | P0 | 1 jour |
| 5 | Contrôle croisé âge ↔ ingrédients (piment, œuf cru, alcool, fruits à coque entiers) et correction des fiches signalées | P0 | 1 jour |
| 6 | Foyer dans la bienvenue (personnes, âges des enfants), portions enfants, ouverture des fiches et du mode cuisine sur la taille du foyer | P1 | 1 jour |
| 7 | Recherche de parents : synonymes (lunchbox, gamelle, goûter, légumes cachés, enfant difficile, mercredi), « Compris » avant « Rien trouvé », repli sur les intentions comprises | P1 | ½ jour |
| 8 | Rubriques famille : « Soir de semaine en 20 min que les enfants aiment », « Lunchbox et goûters à emporter », « Cuisine du dimanche pour la semaine » (repère « se congèle » sur les fiches) | P1 | 2 jours |
| 9 | Menu du jour adapté au jour de la semaine (≤ 45 min en semaine) | P1 | 2 h |
| 10 | Test de fumée de chaque page dans l'automatisation | P1 | ½ jour |
| 11 | Données en JSON par région, chargées à la demande | P1 | 1 à 2 jours |
| 12 | Équipement : autocuiseur, micro-ondes, mijoteuse ; « À propos » à jour ; émoticône restante | P2 | 1 h |
| 13 | Estimation du budget de la semaine à partir des indicateurs € des fiches | P2 | ½ jour |

Les points 1 à 5 corrigent ce qui est faux ou risqué pour une famille. Les points 6 à 9 changent le quotidien d'un parent. Les points 10 et 11 évitent que les prochains ajouts réintroduisent les mêmes défauts.

## 6. Mise en œuvre (16 octobre 2026, même jour)

Les 13 recommandations sont appliquées, toutes vérifiées par des contrôles automatiques (75 contrôles de logique, et 56 rendus de pages).

| # | Recommandation | Ce qui a été fait | Mesure après |
|---|---|---|---|
| 1 | Rangée « Pâtisserie » | Envies désignées par leur identifiant (`cravingById`), la rangée réunit pâtisserie et chocolat | Sucettes en chocolat, cookies, pâte à tartiner, chocolat chaud |
| 2 | Données | `navigator.storage.persist()` au démarrage ; écriture groupée et forcée à la fermeture de la page ; alerte si la mémoire est pleine ; rappel d'export mensuel sur l'accueil (avec le conseil d'installation sur iPhone) | Contrôle 75 |
| 3 | Semaine famille | Les 7 jours à venir (plus de jours passés) ; parts reprises du foyer ; plats filtrés pour le plus jeune enfant (âge de la fiche, piment) | 20 semaines simulées, enfants de 4 et 9 ans : 0 plat épicé, 0 plat d'adulte |
| 4 | Équilibre | Féculents variés, poisson et légumineuses 2 fois, un seul plat très riche ; le reste de la veille pèse moins que l'équilibre ; bilan affiché sous la semaine | Même féculent 3 fois au plus sur 14 repas ; poisson 3,9 et légumineuses 3,6 fois par semaine en moyenne ; 0 plat très riche |
| 5 | Âges ↔ piment | Règle à l'export : piment dans la base (harissa, pâte de curry, gochujang, marinade tandoori…) → « dès 6 ans » ; sinon consigne « piment à part » | 19 fiches passées à 6 ans, 59 précisées ; contrôle 73 à zéro |
| 6 | Foyer | Bienvenue et profil : adultes et âges des enfants, parts calculées (⅓ de part avant 3 ans, ½ de 3 à 10 ans) ; fiches et mode cuisine ouverts sur ces parts (sauf gâteaux et pains) ; allergie d'un seul membre signalée sans exclure | 2 adultes + 4 et 9 ans = 3 parts |
| 7 | Recherche | Synonymes de parents (lunchbox, gamelle, goûter, légumes cachés, enfant difficile, batch cooking, mercredi, cantine) ; « Compris » avant « Rien trouvé » ; repli sur les intentions comprises | « lunchbox » 44 recettes, « enfant difficile légumes » 72, « batch cooking » 68 (0, 0 et 0 avant) |
| 8 | Rubriques famille | Page Enfants : « Soirs de semaine : 30 min, qu'ils aiment », « Cuisine du dimanche : à doubler et congeler », raccourcis ; repère « Se congèle » sur les fiches ; rubrique Pique-nique et gamelle | 77 recettes à emporter, 5 paniers |
| 9 | Menu du jour | En semaine : entrée ≤ 30 min, plat ≤ 1 h, dessert ≤ 45 min actives, adaptés aux enfants du foyer | Un vendredi : guacamole, salade haricots-thon, pouding chômeur |
| 10 | Test de fumée | `tests/smoke.test.tsx` : les 28 pages rendues avec React et un DOM simulé, avec un profil de famille puis un profil vide ; lancé à chaque build et dans l'automatisation | Réintroduire le bug de la page Restes fait échouer le test |
| 11 | Poids au démarrage | Les données étaient déjà lues en JSON ; la liste complète des vidéos (300 Ko) se charge à l'ouverture d'une fiche | 545 Ko compressés au lieu de 580, malgré 22 recettes de plus. Découper par région n'a pas été fait : le moteur a besoin de tous les ingrédients |
| 12 | Équipement et détails | Autocuiseur, mijoteuse, micro-ondes ; l'équipement sert enfin : notes « pas de wok : … », « avec ton autocuiseur : … » sur les fiches ; « À propos » à jour ; émoticônes restantes remplacées par des icônes | Contrôle 74 |
| 13 | Budget | Estimation de la semaine d'après les indicateurs € des fiches (2, 4 ou 7 € la part), présentée comme un ordre de grandeur | Exemple : 65 € pour 7 dîners à 3 parts |

**Rubrique Pique-nique et gamelle** (`/pique-nique`). 22 nouvelles fiches (`bible/recipes_v3_piquenique.py`) s'ajoutent à 55 fiches existantes qui voyagent bien :
- *Classiques* : pain surprise, terrine de légumes, tarte fine courgette-chèvre, salade de pâtes grecque.
- *Originales* : taboulé de chou-fleur cru, courgettes a scapece, œufs marinés au soja.
- *Du monde* : onigirazu, bocadillo de tortilla, muffuletta aux légumes, cornish pasty, scotch eggs en version volaille (D21), brochettes tandoori froides.
- *Pour les enfants* : roulés de tortilla, pizza scrolls, brochettes tomate-mozzarella-melon.
- *Douceurs et boissons anti-gaspi* : flapjacks, boules d'énergie, barres de céréales des fonds de placard, crackers de pain rassis, eau infusée aux épluchures.

La page propose cinq paniers tout faits (enfants, à la française, tour du monde, grands, anti-gaspi) et des filtres. Elle couvre aussi la sécurité au soleil (glacière, 2 h au plus hors du froid, 1 h au-dessus de 32 °C, pas de mayonnaise crue), la préparation du sac, le zéro déchet sur la nappe, les restes qui deviennent un pique-nique et la gamelle (thermos, réchauffage).

Le contrôle 75 a écarté de la liste quatre fiches à la mayonnaise (kimbap, banh mi, coleslaw, arepas).
