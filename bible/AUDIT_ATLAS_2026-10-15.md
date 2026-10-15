# 🔍 Audit ATLAS du 15/10/2026 : débutant, chef, UX/UI, développement

> Audit à quatre regards demandé par la propriétaire du projet. Les constats s'appuient sur des **mesures faites sur les 576 fiches et le code** (script d'audit, contrôles automatiques, essais dans le navigateur), pas sur des impressions. Chaque partie dit ce qui a été **corrigé le jour même** et ce qui **reste à faire**, par priorité.

## Chiffres clés (mesurés)

| Mesure | Valeur |
|---|---|
| Recettes rédigées | 576 (422 niveau facile, 142 moyen, 12 difficile) ; 199 plats, 118 desserts, 77 entrées, 26 boissons, 156 bases, sauces, pains |
| Étapes par recette | **3,0 en moyenne** (chaque étape regroupe plusieurs gestes) ; 3,5 gestes après découpage automatique |
| Ingrédients par recette | 6,9 en moyenne |
| Étapes avec un repère sensoriel (« jusqu'à doré », « nappe », « bec d'oiseau »…) | 30 % |
| Étapes avec une durée | 54 % |
| Fiches qui disaient quoi faire si ça rate | **16 sur 576** avant correction ; toutes aujourd'hui |
| Fiches avec un mot technique non relié à une explication | 123 avant correction ; 0 aujourd'hui (lexique automatique) |
| Recettes au four sans température | 2 (corrigées) |
| Fiches avec une vraie photo | 69 (12 %) ; collecte en cours pour les 506 autres |
| Fiches avec au moins une vidéo | 291 (51 %) |
| Plats en 45 min ou moins | 84 ; recettes en 30 min ou moins (tous types) : 168 |
| Testées en cuisine | **0** (toutes « brouillon prêt pour le Test 1 ») |

---

## 1. Le regard du débutant gourmand (« j'adore manger, je ne sais pas cuisiner »)

**Ce qui marche.** Les fiches sont courtes, les ingrédients ont une quantité, les étapes commencent par un titre en gras (« **Sauce.** »), les durées deviennent des minuteurs d'un geste, le mode cuisine garde l'écran allumé, lit à voix haute et obéit à la voix. Les profils (sans porc, sans alcool, allergies, enfants) évitent les mauvaises surprises, et les fiches techniques expliquent les gestes avec leurs erreurs fréquentes.

**Ce qui bloquait un débutant.**
1. **Pas de filet de sécurité** : 97 % des fiches ne disaient pas quoi faire quand la mayonnaise tranche, quand la sauce est trop liquide, quand la viande reste dure. Un débutant abandonne au premier accroc.
2. **Le vocabulaire** : « nacrer », « monter au beurre », « foncer », « dessécher », « à la nappe » apparaissaient sans explication dans 123 fiches.
3. **Des étapes trop denses** : 3 étapes par recette en moyenne, chacune avec 3 ou 4 actions séparées par des virgules. Les mains dans la pâte, on perd le fil.
4. **Le « quand » et le « combien »** : 70 % des étapes n'ont pas de repère visuel ; « sel, poivre » sans dose ; le préchauffage du four arrive dans l'étape de cuisson, trop tard.
5. **Pas de progression** : rien ne guide de la première omelette à la pâte à choux.

**Corrigé aujourd'hui.**
- **« Avant de commencer »** en tête des étapes : lire la recette, mise en place, matériel, **préchauffage avec la température**, beurre et œufs à sortir 1 h avant, repos longs à anticiper.
- **« Les mots de cuisine de cette recette »** : 48 termes détectés automatiquement dans les étapes, définis en une phrase, reliés à leur fiche technique.
- **« Si ça ne se passe pas comme prévu »** : 30 situations (trop salé, fade, trop piquant, sauce trop liquide ou trop épaisse, émulsion tranchée, grumeaux, crème tournée, viande dure, viande qui bout au lieu de dorer, volaille cuite ou pas, poisson qui colle, pâte qui ne lève pas, choux retombés, gâteau cru au centre ou sec, fond de tarte détrempé, blancs qui ne montent pas, caramel cristallisé, chocolat figé, chantilly ratée, riz collant, pâtes collées, friture molle, œufs trop cuits, légumes aqueux, oignons brûlés, four qui brûle le dessus, coquillages fermés, fromage huileux, légumes mal cuits), **choisies selon la recette** et classées du plus spécifique au plus général, plus l'erreur type de chaque technique liée.
- **Mode cuisine** : un geste par écran (découpage automatique), et à chaque étape « 📖 Je ne comprends pas un mot » et « 🆘 Ça ne se passe pas comme prévu ».
- **Parcours « J'apprends à cuisiner »** : 15 étapes progressives (couteau, œufs, pâtes et riz, faire revenir, soupes, émulsions, saisir et déglacer, rôtir, mijoter, poisson, béchamel, pain, pâtisserie de base, tarte et crème pâtissière, pâte à choux), chacune avec ses fiches techniques et deux recettes ; progression enregistrée.
- **Mon carnet** : après avoir cuisiné, une note sur 5 et « ce que je changerai la prochaine fois », retrouvés sur la fiche.

**Reste à faire (débutant).**
- 🔴 **Réécrire à la main les étapes des 100 recettes les plus utiles** en gestes unitaires avec repère visuel à chacun (le découpage automatique ne peut pas couper « oignon, ail, épices, 2 min » proprement).
- 🔴 **Doser le sel** (« 1 c. à c. rase pour 1 L d'eau ») plutôt que « sel, poivre ».
- 🟠 **Photos ou vidéos d'étape** pour les gestes décisifs (texture de la pâte, couleur du caramel, nappe) : c'est ce qui manque le plus pour « savoir quand ».
- 🟠 Des **minuteurs nommés par geste** (« retourner le poisson ») et une alerte « préchauffe le four maintenant » calculée à rebours.

---

## 2. Le regard du chef étoilé sur les recettes

**Forces.** Une base saine et honnête : techniques justes (températures à cœur, émulsions, cuissons du sucre, tempérage), sécurité alimentaire présente (œuf cru, poisson cru, miel avant 1 an, haché à 70 °C, botulisme des conserves), variété mondiale réelle, recettes familiales gourmandes et réalistes en cuisine domestique, alternatives sans porc et sans alcool pensées pour le goût (fumé, acidité, umami) et non par simple suppression. Les classiques sont respectés (dauphinois sans fromage, lorraine sans fromage, niçoise sans pommes de terre) et l'origine est dite.

**Faiblesses.**
1. **Aucune recette n'est testée** : c'est le point qui sépare une bonne base d'un livre de cuisine fiable. Les quantités de pâtisserie (macarons, choux, croissants, fraisier) doivent être validées en premier : elles tolèrent mal l'à-peu-près.
2. **Rédaction trop télégraphique** pour certains plats de fête (bûche, fraisier, Paris-Brest, bouillabaisse) : il manque le **rétroplanning** (J-2, J-1, jour J) et ce qui se prépare à l'avance.
3. **Le dressage est absent** : pas une ligne sur la présentation, les assiettes chaudes, la finition (huile, herbes, zeste, fleur de sel au dernier moment), qui font « appétissant ».
4. **L'assaisonnement final** (goûter, rectifier, l'acidité qui réveille) n'est pas un réflexe écrit dans les fiches ; il l'est désormais dans les rattrapages, il devrait l'être dans les étapes.
5. **Quelques simplifications** à assumer clairement : cassoulet, potjevleesch, feijoada sans porc (versions « inspirées » à nommer comme telles, décision D21) ; baba et cannelés sans rhum (à tester).
6. **Grands nombres** : rien pour cuisiner pour 12-20 personnes (multiplication non linéaire des cuissons, matériel).

**Ce qui manque pour une application complète (quotidien et grandes occasions).**
- 🔴 **Planificateur de la semaine** : choisir 5 dîners, obtenir une liste de courses regroupée par rayon, avec les restes réutilisés d'un jour à l'autre (le moteur zéro déchet le permet déjà).
- 🔴 **Menus de fête clés en main** avec rétroplanning, quantités pour N invités, ce qui se congèle, ce qui se fait la veille.
- 🟠 **Cuisine en lot (batch cooking)** : 2 h le dimanche pour 4 repas de semaine.
- 🟠 **Fiches « dressage »** et photos de présentation.
- 🟠 **Repères nutritionnels simples** (équilibre de l'assiette, portions), sans culpabiliser.
- 🟢 Conversions (tasses américaines, onces) pour les recettes des chaînes anglophones.

---

## 3. Le regard de l'ingénieur UX/UI senior

**Organisation actuelle.** 5 onglets (Accueil, Explorer, Frigo, Ma biblio, Profil) ; accueil illustré avec envies, rubriques, menu du jour de saison, marché du mois, nouveautés, pâtisserie ; fiches longues mais structurées ; mode cuisine plein écran ; thème clair et sombre, cibles tactiles de 44 px, contraste vérifié.

**Problèmes constatés.**
1. **Trouver une recette précise était difficile** : pas de filtres (temps, niveau, budget, occasion), une région comme la France affichait plus de 150 cartes d'un bloc. → **Corrigé** : page « Toutes les recettes » avec filtres combinables et tris (de saison, rapide, facile, A-Z), lien « Filtrer ces recettes » depuis la recherche.
2. **S'inspirer** : les envies et le menu de saison répondent bien ; il manque un « je n'ai pas d'idée, propose-moi » en un geste (3 suggestions selon l'heure, la saison, le temps disponible et le frigo).
3. **Trois portes concurrentes** (Explorer, Recherche, Toutes les recettes) : à terme, une seule recherche avec filtres repliables, et Explorer réservé à la découverte par région et rubrique.
4. **Vocabulaire de navigation** : « Ma biblio », « Imports », « Favoris classés » désignent des choses proches ; renommer en « Mes recettes » (favoris, carnet, imports) et « Vidéos » (bibliothèque).
5. **Fiche recette longue** : l'ordre conseillé est Ingrédients → Étapes → Si ça rate → Zéro déchet → reste ; un sommaire collant (Ingrédients · Étapes · Aide · Vidéo) aiderait sur téléphone.
6. **Robustesse** : une erreur dans une page effaçait toute l'application (écran blanc). → **Corrigé** : chaque page est protégée, avec message clair et retour.
7. **Accueil chargé** sur petit écran (9 tuiles + 3 rails) : envisager de personnaliser l'ordre selon l'usage (un débutant voit d'abord le parcours).

---

## 4. Le regard du développeur senior

**Architecture.** PWA React + TypeScript + Vite, données générées depuis la bible (une seule source de vérité, références d'ingrédients vérifiées à chaque export), moteur porc/alcool/allergènes testé, 53 contrôles automatiques, hors connexion par service worker, publication GitHub Pages. Solide pour un projet de cette taille.

**Images.** WebP en 400/800/1200 px avec `srcset`, `sizes`, chargement paresseux, couleur dominante en attente, crédits de licence, cache séparé qui survit aux mises à jour. Manques : 🟠 **AVIF** (30 % plus léger) ; 🟠 aperçu flou intégré (LQIP) au lieu d'un aplat ; 🟠 **plafond du cache photos** (il grossit sans limite) ; 🔴 **88 % des fiches sans vraie photo** (collecte en cours).

**Vidéos.** Rien n'est hébergé : lecteurs officiels (youtube-nocookie, TikTok embed/v2) chargés au clic seulement (pas de pistage avant le clic), Shorts en vertical. C'est le bon choix (droits, poids, vie privée). Manques : 🟠 miniatures (elles viendraient des serveurs de YouTube et TikTok : à proposer en option) ; 🟢 lecture à un horodatage précis pour un geste.

**Poids et performance.** Avant aujourd'hui : 583 Ko compressés (3,2 Mo de JavaScript à analyser) au démarrage, car toutes les données étaient dans le fichier principal. → **Corrigé** : dictionnaire, bibliothèque de 3 061 vidéos et restes zéro déchet chargés à la demande ; **417 Ko** au démarrage. Reste : 🟠 découper les pages (chargement par page) ; 🟠 découper les recettes par région ; 🟢 budget de performance contrôlé à chaque compilation.

**Classement automatique sans recoder (demande).** → **Fait** :
- **Dans l'application** : coller un lien TikTok, YouTube ou Vimeo suffit, ou « Partager › ATLAS » sur Android. Titre, légende et auteur sont lus automatiquement (oEmbed officiel), la recette est classée (règles + spécialité connue du créateur si le titre ne suffit pas), le porc et l'alcool sont repérés, et elle est enregistrée. Les liens importés en masse ou sans légende sont relus et classés à l'ouverture de « Mes imports ». Testé sur TikTok (Afrique), YouTube français (Asie), anglais (Italie) et Short (Fait maison).
- **Dans la bibliothèque partagée** : coller des liens dans `recettes-classees/a_ajouter.md` puis lancer `python ajout_auto.py` (ou, une fois l'automatisation activée, simplement enregistrer le fichier sur GitHub) : chaque lien est lu, classé, ajouté à `ajouts_classes.md`, l'application est reconstruite et publiée. Les autres sites de recettes sont lus par le titre de leur page.
- **Activation de l'automatisation GitHub** : elle demande une autorisation que seule la propriétaire du compte peut donner (droit `workflow`). Le fichier est prêt dans `outils/ajout-recettes.yml`.

**Qualité et fiabilité.** Manques : 🟠 tests d'interface de bout en bout (parcours d'import, mode cuisine) ; 🟠 contrôles automatiques à chaque envoi sur GitHub (même autorisation `workflow`) ; 🟢 journal d'erreurs local consultable dans le profil ; 🟢 sauvegarde et restauration du carnet entre appareils (aujourd'hui par fichier d'export).

---

## 5. Feuille de route proposée

| Priorité | Chantier | Pour qui |
|---|---|---|
| 🔴 1 | Tester en cuisine les 30 recettes les plus demandées (pâtisserie d'abord) et corriger | Tous |
| 🔴 2 | Réécrire en gestes unitaires, avec repère visuel et sel dosé, les 100 recettes du quotidien | Débutant |
| 🔴 3 | Photos de toutes les fiches (en cours) puis photos d'étapes décisives | Débutant, UX |
| 🔴 4 | Planificateur de la semaine + liste de courses consolidée + restes réutilisés | Quotidien |
| 🟠 5 | Menus de fête avec rétroplanning et quantités pour N invités | Grandes occasions |
| 🟠 6 | Recherche unique avec filtres repliables ; « propose-moi » en un geste | UX |
| 🟠 7 | Dressage : une ligne de finition par fiche, fiches techniques « présenter une assiette » | Chef |
| 🟠 8 | AVIF, aperçus flous, plafond du cache photos, pages chargées à la demande | Dév |
| 🟢 9 | Batch cooking, repères nutritionnels, conversions d'unités | Quotidien |

---

## 6. Mise en œuvre des recommandations (15/10/2026, deuxième passe)

Tout ce qui suit est en ligne et vérifié par **61 contrôles automatiques**, rejoués par GitHub à chaque envoi (automatisation « Contrôles »). Les recettes elles-mêmes restent **non testées en cuisine**.

| Recommandation | Ce qui a été fait | État |
|---|---|---|
| 🔴 1 Tester en cuisine | « Mes recettes › Mon carnet d'essais » : note sur 5 et corrections après chaque essai, **export en tableau** (fichier `.md`) à renvoyer pour corriger les fiches. Les tests eux-mêmes demandent une vraie cuisine. | Outil prêt, tests à faire |
| 🔴 2 Gestes unitaires, repères, sel dosé | Découpage d'un geste par écran (déjà fait) ; **repères visuels automatiques** sous les étapes (oignon translucide, frémissement, sauce qui nappe, pousse, blancs fermes, caramel, friture…) sur 289 fiches ; **sel dosé calculé** pour les 231 plats et entrées qui n'en indiquaient pas (≈ 1,2 g par portion, moitié moins avec des ingrédients salés, eau de cuisson à 10 g/L) ; **minuteurs nommés par geste** ; **rappel « préchauffe le four maintenant »** en mode cuisine. La réécriture à la main reste souhaitable pour les fiches à étapes très denses. | Fait (automatique) ; relecture humaine à prévoir |
| 🔴 3 Photos | Photos choisies une à une sur planches contact : **{PHOTOS_R}** ; dictionnaire : **{PHOTOS_I}**. Photos d'étapes : inventaire de Wikimedia Commons (`illustrations/etapes_scan.py`) : les séries d'une même recette sont rares (frites, thiéboudienne…) ; les gestes des fiches techniques sont illustrés à la place (« Le geste en photos »). | Fait pour les plats et ingrédients |
| 🔴 4 Planificateur | Page **« Ma semaine »** : 7 jours midi et/ou soir, plats de saison, rapides en semaine (temps réglable), protéines variées, **restes d'un plat réutilisés le lendemain** (signalés ♻️), « 📅 Planifier » sur chaque plat, **courses regroupées** (un article par produit, quantités additionnées et arrondies à l'achat, épices « vérifie ton placard »), **préparation à l'avance** (tâches de la veille, légumes à couper d'un coup). | Fait |
| 🟠 5 Menus de fête | Quantités **calculées pour N convives** et regroupées dans les courses ; pour chaque menu : ce qui se fait **la veille** et ce qui **se congèle** ; conseils de **grande tablée** à partir de 10 personnes ; rétroplanning J-2/J-1/J. | Fait |
| 🟠 6 Recherche, « propose-moi » | **« 🎲 Pas d'idée ? Propose-moi »** sur l'accueil : 3 idées de 3 cuisines différentes selon l'heure, la saison du lieu, le temps disponible et le frigo ; **filtres repliables** dans la recherche (type, 30 min, facile) ; « Ma biblio » renommée **« Mes recettes »** ; **sommaire collant** sur les fiches ; parcours débutant en tête d'accueil tant qu'on a peu cuisiné. | Fait |
| 🟠 7 Dressage | Bloc **« Finition et dressage »** sur chaque fiche (règles par famille de plats, salé et sucré distingués), **« goûte et rectifie »** pour le salé, touche verte si la fiche n'a pas d'herbes ; fiche technique **« Présenter une assiette »**. | Fait |
| 🟠 8 Performance | **Pages chargées à la demande** (démarrage 427 → 395 Ko compressés avant les photos) ; **manifeste photos allégé**, crédits chargés à l'affichage ; **cache photos plafonné** (400 images) ; vignettes d'ingrédients en 400/800 px seulement. **AVIF** : Pillow 12.3 installé dans `illustrations/.venv` ; chaque photo existe en AVIF (≈ 30 % plus léger) avec repli WebP, le navigateur choisit. Découper les recettes par région : non fait (gain modeste, risque élevé). | Fait |
| 🟢 9 Quotidien | Cuisine en lot dans « Ma semaine » ; **repère d'équilibre** de l'assiette sur chaque plat (sans culpabiliser) ; fiche **« Convertir les mesures »** (tasses, onces, °F) pour les chaînes anglophones. | Fait |
| Dév | **Automatisation GitHub activée** : « Ajouter des recettes » (coller des liens dans `recettes-classees/a_ajouter.md` sur github.com → classement, contrôles et publication automatiques) et « Contrôles » à chaque envoi ; **journal d'erreurs local** dans le profil. Tests d'interface de bout en bout : non faits. | Fait |

### Deuxième demande du 15/10 : AVIF, photos d'étapes, icônes

- **Icônes** : 69 icônes SVG maison (`app/src/components/icons.tsx`, planche de contrôle sur `#/icones` en développement) remplacent les émoticônes de l'interface : onglets, tuiles, envies, régions, familles d'ingrédients, boutons, badges, minuteurs. Même trait (1,8 px arrondi), aplat teinté à 18 %, couleur héritée ; lisibles en clair et en sombre ; plus de carrés vides sous Windows 10. Les couvertures illustrées des quelques fiches sans photo gardent leur pictogramme de plat.
- **AVIF** : voir le tableau ci-dessus.
- **Photos d'étapes** : voir le tableau ; choix relus un à un sur planches contact (`etapes_sheets.py`).
