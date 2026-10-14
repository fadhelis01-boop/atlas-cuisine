# 📔 BIBLE ATLAS : TOME 8 : Décisions d'architecture (ADR) et spécification des moteurs

> Complète le Tome 1 §17-18, le Tome 2 §3-5 et le Tome 3. Objectif : passer de la bible à l'implémentation.
> **Statut de vérification de ce tome** (lire avant d'utiliser) :
> - ✅ **Testé** : moteur diététique, substitutions, suggestion par ingrédients → **implémentation de référence en Python exécutée** (annexe A), **28 contrôles passés** (annexe B).
> - 🟡 **Spécifié, non exécuté** : composeur de menu, planificateur anti-gaspi, pipeline d'import, synchronisation, pipeline audio, recalcul événementiel. Ce sont des **spécifications** et du pseudo-code : à prototyper et mesurer.
> - Les **paramètres numériques** (poids, pénalités, seuils) sont des **valeurs de départ à calibrer** sur des données réelles.

---

## 1. Registre des décisions d'architecture (ADR)

Format : **Contexte → Décision → Alternatives → Conséquences → Statut → Date de revue**. Tous les ADR sont **« Proposé »** tant que le prototype technique du sprint 0 n'a pas confirmé.

### 1.1 Vue d'ensemble

| ADR | Décision | Alternative principale | Statut |
|---|---|---|---|
| 001 | **Flutter** (UI multi-plateforme) + modules natifs Swift/Kotlin | Natif pur ×3 | Proposé |
| 002 | **Monolithe modulaire** côté backend | Microservices d'emblée | Proposé |
| 003 | **PostgreSQL + pgvector** comme base principale | Document DB | Proposé |
| 004 | **Meilisearch ou Typesense** pour la recherche | Postgres FTS seul | Proposé |
| 005 | **Local-first** (SQLite) + synchronisation | Client « mince » en ligne seulement | Proposé |
| 006 | **Régimes calculés** depuis un graphe d'ingrédients, jamais saisis à la main | Tags manuels | Proposé (**fort**) |
| 007 | **Logique à états multiples** (`ok / trace / uncertain / violates`), l'inconnu n'est jamais « ok » | Booléens | Proposé (**fort**) |
| 008 | **Recettes versionnées et immuables** (une publication = une version) | Mise à jour en place | Proposé |
| 009 | **Audio pré-généré** + TTS système en repli | TTS à la volée | Proposé |
| 010 | **Aucune vidéo tierce stockée** à l'import | Copie des vidéos | Proposé (**fort**) |
| 011 | **LLM d'extraction non fiable** : sortie validée par schéma, régimes **recalculés** par le moteur | Confiance au LLM | Proposé (**fort**) |
| 012 | **Interrupteur à distance** (kill switch) pour masquer une recette | Correctif via nouvelle version | Proposé (**fort**) |
| 013 | **Événements + outbox** pour recalculs asynchrones | Recalcul synchrone | Proposé |
| 014 | **Analytics sans PII**, aucune donnée de régime/allergie vers des tiers | Analytics standard | Proposé |
| 015 | **Hébergement UE** pour toutes les données | Multi-régions mondiales | Proposé |
| 016 | **Passkeys + Sign in with Apple/Google** | Mot de passe seul | Proposé |
| 017 | **Feature flags** + déploiements progressifs | Déploiement unique | Proposé |

### 1.2 ADR détaillés (les « décisions fortes »)

#### ADR-006 : Régimes et allergènes calculés depuis un graphe d'ingrédients
- **Contexte** : une erreur sur « sans porc » ou un allergène est un défaut de confiance majeur (Tome 7 §12, Sev 0). Les tags saisis à la main dérivent et ne détectent pas les dérivés cachés (gélatine, bouillons, extraits alcoolisés).
- **Décision** : le régime d'une recette est **toujours calculé** : `recette → lignes → ingrédients canoniques (+ sous-recettes) → dérivés/allergènes`. Les recettes importées n'obtiennent **jamais** de régime déclaré par une source externe.
- **Alternatives** : tags éditoriaux ; calcul + tags manuels (rejeté : deux sources de vérité).
- **Conséquences** : (+) cohérence, traçabilité, recalcul automatique ; (−) le référentiel (Tome 3) devient **critique** et son coût de relecture est élevé ; tout ingrédient inconnu rend la recette « non vérifiée ».
- **Garde-fou** : les 28 contrôles de l'annexe B + tests dorés Tome 2 §4 **bloquent la CI**.

#### ADR-007 : Logique à états multiples, l'inconnu n'est jamais « ok »
- **Décision** : par contrainte, 4 états : `ok`, `trace`, `uncertain`, `violates`. Un ingrédient **absent du référentiel** produit `uncertain`. Les sous-recettes sont aplaties (détection de **cycles**). Les ingrédients « facultatifs » **comptent**.
- **Table de décision de visibilité** (testée) :

| État calculé | Profil **Standard** | Profil **Strict** |
|---|---|---|
| `ok` | visible | visible |
| `trace` (alcool de fermentation…) | visible (note) | traité comme `violates` |
| `uncertain` | visible **avec avertissement** « régime non vérifié » | traité comme `violates` |
| `violates` | **adaptable** si **toutes** les causes ont une règle **validée**, sinon **masquée** | idem |

- **Conséquences** : le mode Strict **réduit** le catalogue visible tant que le référentiel n'est pas vérifié ; c'est voulu et mesuré (Tome 3 §1.5).

#### ADR-010 : Aucune vidéo tierce stockée
- **Contexte** : CGU des plateformes et droit d'auteur (Tome 1 §14, §19.5).
- **Décision** : on stocke **le texte structuré dérivé**, le **lien**, le **crédit**, une **vignette fournie par l'API officielle (oEmbed) quand autorisé**. Pas de téléchargement de la vidéo source.
- **Conséquences** : (+) risque juridique réduit, coûts de stockage faibles ; (−) la transcription automatique ne peut porter que sur du contenu **fourni par l'utilisateur** (fichier, capture) ou sur la **légende**.

#### ADR-011 : Le LLM d'extraction est non fiable
- **Décision** : (1) le modèle n'a **aucun outil** ni accès réseau ; (2) la sortie doit **valider un schéma JSON strict** ; (3) **provenance** : tout nombre de la sortie doit exister dans la source (ou résulter d'une conversion tracée) ; sinon `null` ; (4) **régimes recalculés** par le moteur (ADR-006), jamais lus dans la sortie du LLM ; (5) le contenu importé est **délimité** et traité comme **donnée**.
- **Conséquences** : surcoût de validation ; réduction forte des risques d'injection et d'invention de quantités.

#### ADR-012 : Interrupteur à distance (kill switch)
- **Décision** : liste signée `masked_recipe_ids[]` + `masked_rule_ids[]` publiée par le backend ; l'app la récupère **au lancement et toutes les 6 h**, et reçoit une **notification silencieuse** en cas de Sev 0.
- **Limite honnête** : un appareil **hors-ligne** ne reçoit pas le masquage tant qu'il n'est pas reconnecté. L'app affiche donc, sur toute recette téléchargée, **la version du référentiel** ayant servi au calcul et un avertissement si la dernière synchronisation date de **plus de 30 jours**.

#### ADR-001 : Flutter + modules natifs
- **Décision** : UI Flutter pour iOS, iPadOS, Android, macOS, Windows ; **Swift** pour Share Extension, App Intents, Widgets, Live Activities, Watch ; **Kotlin** pour widgets, Wear OS, partage ; **Next.js** pour le web public (SEO).
- **Critère de remise en cause** (prototype sprint 0, 2 semaines) : lecture vidéo HLS en boucle + audio en arrière-plan + minuteur persistant + Live Activity. **Si un seul échoue de façon non contournable** → bascule vers natif pour la couche concernée.

---

## 2. Moteur diététique (✅ testé)

### 2.1 Entrées / sorties
- **Entrées** : recette (lignes → ingrédients ou sous-recettes), référentiel d'ingrédients (dérivés avec niveau, allergènes, niveau de vérification), contraintes du profil, mode (Standard/Strict), règles de substitution.
- **Sorties** : par recette, `pork`, `alcohol` ∈ {ok, trace, uncertain, violates} ; allergènes ; liste des **ingrédients fautifs** ; **confiance A/B/C** ; **disponibilité** ∈ {ok, ok_warning, adaptable, hidden}.

### 2.2 Invariants (vérifiés par les tests)
| # | Invariant |
|---|---|
| I1 | Un ingrédient **inconnu** ne produit jamais `ok`. |
| I2 | Un ingrédient « facultatif » **compte** pour le régime. |
| I3 | Les allergènes se **propagent** via les sous-recettes ; **ajouter** un ingrédient ne **retire jamais** un allergène (propriété sur 2 000 cas aléatoires). |
| I4 | Une **adaptation** n'est acceptée que si le **recalcul** de la variante est `ok` (jamais présumée) ; sinon elle est **refusée**. |
| I5 | Une règle `draft/testing/retired` **n'adapte jamais** une recette. |
| I6 | Une règle ne s'applique **qu'aux ingrédients fautifs**. |
| I7 | Les **allergènes introduits** par un substitut sont **signalés** (différence avant/après). |
| I8 | Les **cycles** de sous-recettes sont détectés (erreur, pas de boucle infinie). |

### 2.3 Complexité et mise à l'échelle
Calcul **linéaire** en nombre de lignes (incluant sous-recettes). Pour 600 recettes × ~12 lignes, un recalcul complet est de l'ordre de **millisecondes à centaines de ms** (**à mesurer**, non mesuré ici). Le résultat est **matérialisé** (`recipe_diet`, Tome 2 §5) et recalculé sur événement (§9).

### 2.4 Limites de l'implémentation de référence
Voir annexe C (pas de gestion des unités, des quantités seuil comme les sulfites ≥ 10 mg/kg, des synonymes, ni de la persistance).

---

## 3. Moteur de substitution (✅ testé)

### 3.1 Algorithme
```
substituer(recette, règles, contraintes, strict):
  avant  = évaluer(recette)
  fautifs = ingrédients fautifs selon contraintes (trace/uncertain inclus si strict)
  règles_applicables = { r | r.statut = validated ∧ r.satisfait ∩ contraintes ≠ ∅ ∧ r.remplace ∈ fautifs }
  variante = remplacer chaque ligne fautive par les items de sa règle (quantité × ratio)
  après  = évaluer(variante)
  si disponibilité(après) ∉ {ok, ok_warning} : refuser (adaptation = null)
  sinon : retourner variante + allergènes_introduits = après.allergènes − avant.allergènes
```
### 3.2 Points d'attention
- **Règles spécifiques à la recette** prioritaires sur les règles génériques (Tome 1 §7.5) ; non implémentées dans la référence : à ajouter (clé `(recipe_id, ingredient_id)` d'abord).
- **Ajustements d'étapes** (temps de cuisson, assaisonnement) : texte lié à la règle ; **affichés** avec la variante.
- **Mise à l'échelle** : `qty_per_100g` du schéma (Tome 2 §5) à gérer ; la référence applique un **ratio simple**.
- **Chaînes de substitution** (un substitut qui devient fautif pour une autre contrainte) : **interdit** ; le recalcul (I4) le détecte.

---

## 4. Moteur de suggestion par ingrédients (✅ testé)

### 4.1 Formule (Tome 1 §6.3, telle qu'implémentée)
```
requis    = lignes avec poids > 0 et non facultatives
couverture = Σ poids(possédé ou placard) + 0,8 × Σ poids(substituable possédé)   /   Σ poids(requis)
score     = 100 × couverture
          − 15 × (nombre de manquants de poids 3)
          + 4  × (nombre d'ingrédients requis proches de la DLC)
seau      = "all"    si aucun manquant
          = "almost" si ≤ 2 manquants et aucun de poids 3
          = "ideas"  si score ≥ 60
          = exclu    sinon
```
Les **bonus de saison, d'équipement** et la **pénalité de temps** du Tome 1 §6.3 ne sont **pas** dans la référence (à ajouter, mêmes principes).

### 4.2 Mise en œuvre à l'échelle
- **Index inversé** `ingrédient → recettes` (+ **bitsets** par recette) : on ne score que les recettes qui partagent ≥ 1 ingrédient **structurant** avec la liste (réduction massive avant calcul).
- **Filtrage préalable** par régime/allergènes du foyer (§2) : on ne **score pas** les recettes masquées.
- **Substituts** : table `ingrédient → {substituts validés}` précalculée.
- **Cible** : < 150 ms p95 pour 10 000 recettes (**à mesurer**).

### 4.3 Calibration (à faire)
Constituer un **jeu d'évaluation** : 100 listes d'ingrédients réalistes × jugement d'un·e chef·fe sur les 5 meilleures recettes ; mesurer **NDCG@5** ; ajuster les poids (0,8 ; −15 ; +4 ; seuil 60). **Aucune valeur n'est définitive.**

---

## 5. Composeur de menu (🟡 spécification)

### 5.1 Données d'entrée par recette
`course` (E/P/D), `richness` (1-5), `temperature` (chaud/froid/ambiant), `texture_tags`, `color_tags`, `dominant_ingredients` (poids 3, hors placard), `cuisine/région`, `oven` (°C, minutes, simultanéité), `active_min`, `cost_band`, `season`, `diet` (calculé).

### 5.2 Contraintes **dures** (éliminatoires)
1. **Régimes et allergènes de tous les convives** (union) : candidats **masqués** par le moteur §2 (ou **adaptés** si règle validée).
2. **Même ingrédient dominant** dans deux plats : interdit (sauf liste d'exceptions éditoriales).
3. **Four** : deux plats à températures différentes **sans fenêtre de cuisson compatible** : interdit (planification §5.4).
4. **Temps actif total** ≤ limite choisie (défaut 2 h 30 pour un menu de fête).
5. **Saison** : exclure hors saison si l'option « de saison » est active.

### 5.3 Score (valeurs de départ à calibrer)
```
score = 0,30 × équilibre + 0,20 × cohérence + 0,15 × diversité
      + 0,15 × zéro_déchet + 0,10 × temps + 0,10 × budget
équilibre   = 1 − |richesse(E) − cible_E| /4 − |richesse(P) − cible_P|/4 − |richesse(D) − cible_D|/4  (borné [0,1])
              cibles « classique » : E=2, P=4, D=3 ; « léger » : E=1, P=3, D=2 ; « audacieux » : libre
cohérence   = 1 si même région ; 0,6 si région voisine/famille ; 0,3 sinon (menu « fusion » assumé)
diversité   = 1 − chevauchement(textures, couleurs, techniques)
zéro_déchet = part des sous-produits d'un plat réutilisés par un autre (blancs ↔ meringue…)
temps       = 1 − (temps_actif_total / limite)
budget      = 1 si ≤ budget cible, décroissant sinon
```
### 5.4 Algorithme
```
composer(pivot, convives, contraintes, style):
  cours_manquants = {E,P,D} − cours(pivot)
  pour chaque cours : candidats = top K=30 du catalogue (filtres durs + compatibilité avec le pivot)
  si 2 cours manquants : énumérer toutes les paires (≤ 900) ; évaluer contraintes dures + score
  trier par score ; tie-break déterministe : (score desc, id recette asc)
  retourner 3 menus : Classique (cohérence maximale), Léger (cibles « léger »), Audacieux (diversité maximale)
  pour chaque : afficher le score ET ses composantes (explicabilité)
planning_four(menu) : trier les plats par température ; intervalle de cuisson ; signaler conflit
```
**Complexité** : ≤ K² évaluations (≤ 900) → négligeable ; l'essentiel du coût est la **qualité des métadonnées** (richesse, textures), donc éditoriale (Tome 6).

### 5.5 Boissons
Règles par **profil dominant** du plat (acidité, gras, piquant, sucre, umami) (Tome 1 §12.4) ; **colonne sans alcool toujours présente** ; colonne avec alcool **masquée** sans vérification d'âge ni si le profil exclut l'alcool.

### 5.6 Tests à écrire (non exécutés ici)
Menu sans porc pour 6 convives dont 1 allergique aux fruits à coque ; deux plats au four à 220 °C et 160 °C ; pivot = dessert ; pivot sans voisins culturels ; catalogue vide pour un régime (message, pas d'erreur).

---

## 6. Planificateur anti-gaspi et bilan matière (🟡 spécification)

### 6.1 Bilan matière d'un menu / d'une semaine
```
pour chaque ingrédient i :
  acheté(i)   = Σ formats du commerce nécessaires pour couvrir Σ quantités(i) des recettes
  utilisé(i)  = Σ quantités(i)
  reste(i)    = acheté(i) − utilisé(i) − stock_frigo(i)
score_zéro_déchet = 1 − Σ reste_pondéré / Σ acheté_pondéré      (pondération : prix ou fraîcheur)
```
### 6.2 Valorisation des restes
`reste(i)` → parties (Tome 3 §17.4) → recettes de valorisation **compatibles** avec les régimes du foyer ; **classement** par : consommation du reste (↑), achats supplémentaires (↓), temps (↓), DLC (urgence ↑).

### 6.3 Optimisation de la semaine (heuristique gloutonne)
```
planifier(semaine, recettes_choisies, frigo):
  répéter jusqu'à convergence :
    pour chaque reste significatif (> seuil, périssable) :
      chercher une recette dans les jours suivants qui l'utilise avec ≤ 1 achat supplémentaire
      si trouvée et score global ↑ : l'insérer ; sinon proposer en « idée »
  garantie : chaque ingrédient périssable acheté est utilisé ≥ 2 fois si possible
```
**Limites** : heuristique, pas optimale ; à comparer à un solveur (programmation linéaire) si le gain le justifie.

---

## 7. Pipeline d'import (🟡 spécification)

### 7.1 Machine à états
```
RECEIVED → FETCHING → EXTRACTING → NORMALIZING → CLASSIFYING → DEDUP → NEEDS_REVIEW → CONFIRMED
              ↘ (erreur) ↘ FAILED (reprise manuelle)    ↘ REJECTED (non culinaire / inapproprié)
```
- **Idempotence** : clé = `hash(user_id + URL canonique)` ; un même lien partagé 2 fois = **1 job**.
- **Reprises** : jusqu'à 3 avec **attente exponentielle** ; **file morte** (dead-letter) ensuite ; **délai maximal** par étape.
- **Quotas** : par utilisateur (gratuit : 3/mois ; Tome 1 §21) ; **limitation de débit** globale par plateforme.
- **Observabilité** : durée par étape, taux d'échec par plateforme, **taux de champs corrigés** par l'utilisateur.

### 7.2 Extrait du schéma de sortie (validé strictement)
```json
{
  "title": "string(<=120)",
  "servings": "integer|null",
  "time": { "active_min": "integer|null", "total_min": "integer|null" },
  "ingredients": [
    { "raw": "string", "qty": "number|null", "unit": "string|null", "canonical_id": "string|null",
      "confidence": "number[0..1]", "provenance": "caption|transcript|ocr|web" }
  ],
  "steps": [ { "n": "integer", "text": "string(<=400)", "duration_s": "integer|null" } ],
  "cuisine_guess": { "id": "string|null", "confidence": "number[0..1]" },
  "missing": ["string"]
}
```
Le schéma **ne contient pas** de champ « sans porc / sans alcool / allergènes » : ils sont **calculés** par le moteur (ADR-006/011).

### 7.3 Contrôles de sécurité et de qualité
| Contrôle | Règle |
|---|---|
| **Délimitation** | Contenu importé encadré par des balises et marqué « donnée » ; instructions internes **hors** du contenu |
| **Aucun outil** | Le modèle d'extraction n'a **aucun accès** réseau/fichiers |
| **Provenance numérique** | Tout nombre de sortie doit se retrouver dans la source (ou conversion tracée) ; sinon `null` + `missing` |
| **Longueurs bornées** | Troncature sûre des entrées très longues |
| **Allowlist URL** | Seules les plateformes prises en charge sont consultées ; pas de suivi de redirections vers des hôtes inconnus |
| **Recalcul des régimes** | Par le moteur ; inconnus → `uncertain` ; recettes importées en **confiance C** |
| **Revue obligatoire** | Si un champ obligatoire a une confiance < seuil → écran de revue avant enregistrement |

### 7.4 Dédoublonnage
Similarité = `0,6 × Jaccard(ingrédients canoniques) + 0,4 × cosinus(embeddings du titre + étapes)` ; seuil **0,85 → proposer la fusion** (jamais fusion automatique) ; seuils **à calibrer** sur le jeu d'évaluation (Tome 7 §7).

### 7.5 Taxonomie des erreurs
`SOURCE_UNAVAILABLE` (lien mort/privé) · `UNSUPPORTED_SOURCE` · `NOT_A_RECIPE` · `EXTRACTION_INVALID_SCHEMA` · `LOW_CONFIDENCE` (→ revue) · `QUOTA_EXCEEDED` · `CONTENT_REJECTED` · `TIMEOUT`. Chacune a un **message utilisateur humain** (Tome 5 §11) et une **action** (réessayer, éditer, abandonner).

---

## 8. Synchronisation local-first (🟡 spécification)

### 8.1 Entités et stratégies
| Entité | Stratégie de fusion | Remarques |
|---|---|---|
| Profil, réglages | **Dernier écrit gagne** par champ (horloge hybride) | |
| Favoris, collections | **Ensemble « ajout gagnant »** (OR-Set) + tombstones | Une suppression n'écrase pas un ajout concurrent plus récent |
| **Liste de courses (partagée)** | OR-Set pour les lignes ; **cochage** : dernier écrit gagne | Cas multi-appareils/multi-membres |
| Frigo (quantités) | Dernier écrit gagne **par ligne** | Évite la fusion arithmétique ambiguë |
| Planning | Dernier écrit gagne par case | |
| Imports | Serveur = source de vérité ; client = file d'attente | |
| Recettes officielles | Lecture seule ; **version** immuable (ADR-008) | |

### 8.2 Protocole
- `POST /sync/push` : liste de `{entité, id, champ, valeur, hlc}` ; **idempotent** (clé de lot).
- `GET /sync/pull?since=<curseur>` : changements **depuis** le curseur ; **pagination**.
- **Horloge hybride logique (HLC)** pour l'ordre ; **tombstones** conservés **30 jours** puis purgés.
- **Version de schéma** dans chaque requête ; migrations **ascendantes** ; le client trop ancien est **invité à mettre à jour**.
- **File hors-ligne** persistante ; **reprise** au retour réseau ; **conflits visibles** seulement si une **perte de donnée utile** est possible (sinon silencieux).

### 8.3 Tests clés
Deux appareils modifient la même liste hors-ligne puis se synchronisent (aucun ajout perdu) ; suppression concurrente d'un élément ré-ajouté ; appareil absent 45 jours (tombstones purgés → resync complète) ; schéma client plus ancien que serveur.

---

## 9. Recalcul événementiel et masquage (🟡 spécification)

```
Modification d'un ingrédient / d'une règle / d'un dérivé
   └─► écriture + événement « referential_changed » dans l'outbox (même transaction)
        └─► worker : récupérer les recettes dépendantes (index inversé ingredient → recettes)
             └─► recalculer recipe_diet ; comparer à l'ancien
                  ├─ inchangé : rien
                  ├─ passage ok → uncertain/violates : MASQUER auto + alerte Sev 0 (Tome 7 §13)
                  └─ autre changement : publier une nouvelle version de la recette (ADR-008)
        └─► incrémenter catalog_version ; liste de masquage mise à jour ; push silencieux aux clients
```
- **Délai cible** : recalcul complet < 5 minutes après modification (**à mesurer**).
- **Journal d'audit** : qui a changé quoi, quand, version du référentiel (Tome 7 §15.4).
- **Garantie d'ordre** : un seul recalcul **en cours** par ingrédient (verrou) ; **idempotence** par `(ingrédient, version)`.

---

## 10. Pipeline audio (🟡 spécification)

```
étape (texte) → normalisation (table Tome 6 §8.2) → SSML (lexique Tome 6 §8.3, version lex_v)
   → TTS (fournisseur sous licence commerciale) → normalisation sonore (−16 LUFS, crête ≤ −1 dBTP)
   → stockage + CDN ; clé de cache = sha256(texte_normalisé + voix + lex_v + vitesse)
   → manifeste par recette { step_n: audio_url, durée, texte_lu }
Client : télécharge les pistes pour le hors-ligne ; si piste absente → TTS système (même texte normalisé)
```
- **Mise à jour du lexique** → **ne régénérer que** les étapes **affectées** (comparaison de clé de cache).
- **Contrôle qualité** : écoute d'échantillon + rapport des erreurs de prononciation (Tome 7 §6).
- **Coût** : proportionnel au nombre d'étapes **modifiées**, pas au catalogue.

---

## 11. Observabilité, SLO et alertes

| SLI | SLO | Alerte |
|---|---|---|
| Disponibilité API | 99,9 % mensuel | Erreurs 5xx > 1 % sur 5 min |
| Recherche p95 | < 150 ms | > 300 ms sur 10 min |
| Recalcul diététique (lag) | < 5 min | > 15 min |
| **Recettes ok→violates automatiques** | 0 non traitées | **Toute occurrence** → alerte immédiate |
| Imports réussis (hors quota) | ≥ 90 % | < 80 % sur 1 h |
| Délai de traitement d'import p95 | < 60 s | > 120 s |
| Crash-free sessions | ≥ 99,7 % | < 99,5 % sur 24 h |
| Synchronisation : échecs | < 0,5 % | > 2 % |

**Journalisation** sans PII ni données de régime/allergie ; **traçage** distribué sur l'import et le recalcul ; **tableaux de bord** : qualité du catalogue (% niveau A), file d'imports, lag de recalcul.

---

## ANNEXE A : Implémentation de référence (code exécuté)

> Fichier `atlas_engine.py` : **moteur diététique + substitutions + suggestion**. Code **de démonstration** : pas de persistance, pas d'unités, pas de seuils par quantité (cf. annexe C).

```python
"""ATLAS : implémentation de référence (moteur diététique, substitutions, suggestion).
Objectif : valider la logique décrite dans les Tomes 1-3-8. Ce n'est PAS le code de production."""
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple

@dataclass
class Ingredient:
    id: str
    derivs: Dict[str, str] = field(default_factory=dict)   # kind -> 'certain' | 'possible' | 'trace'
    allergens: Set[str] = field(default_factory=set)
    verified: str = "C"                                    # A | B | C

@dataclass
class Line:
    ing: Optional[str] = None      # ingrédient canonique
    sub: Optional[str] = None      # sous-recette
    qty: float = 0.0
    weight: int = 2                # 0 optionnel/assaisonnement … 3 structurant
    optional: bool = False

@dataclass
class Recipe:
    id: str
    lines: List[Line]
    imported: bool = False

@dataclass
class Rule:                        # règle de substitution (extrait du schéma Tome 2 §5)
    id: str
    replaces: str
    items: List[Tuple[str, float]] # (ingrédient, ratio sur la quantité d'origine)
    satisfies: Set[str]            # {'pork','alcohol'}
    status: str = "validated"      # draft | testing | validated | retired

ORDER = {"ok": 0, "trace": 1, "uncertain": 2, "violates": 3}

def _walk(r: Recipe, recipes: Dict[str, Recipe], stack=()):
    """Aplatit les ingrédients (sous-recettes incluses). Détecte les cycles."""
    if r.id in stack:
        raise ValueError(f"cycle de sous-recettes : {' -> '.join(stack + (r.id,))}")
    for ln in r.lines:
        if ln.sub:
            yield from _walk(recipes[ln.sub], recipes, stack + (r.id,))
        else:
            yield ln

def evaluate(r: Recipe, ings: Dict[str, Ingredient], recipes: Dict[str, Recipe]):
    res = {"pork": "ok", "alcohol": "ok", "allergens": set(), "uncertain_allergens": False,
           "unknown": [], "offenders": {"pork": [], "alcohol": []}, "confidence": "A"}
    def bump(kind, st, ing_id):
        if ORDER[st] > ORDER[res[kind]]:
            res[kind] = st
        if st in ("violates", "uncertain", "trace"):
            res["offenders"][kind].append(ing_id)
    for ln in _walk(r, recipes):
        ing = ings.get(ln.ing)
        if ing is None:                                   # inconnu => JAMAIS « ok »
            res["unknown"].append(ln.ing)
            bump("pork", "uncertain", ln.ing); bump("alcohol", "uncertain", ln.ing)
            res["uncertain_allergens"] = True
            res["confidence"] = "C"
            continue
        for kind, key in (("pork", "pork"), ("alcohol", "alcohol")):
            lvl = ing.derivs.get(key)
            if lvl == "certain": bump(kind, "violates", ing.id)
            elif lvl == "possible": bump(kind, "uncertain", ing.id)
            elif lvl == "trace": bump(kind, "trace", ing.id)
        res["allergens"] |= ing.allergens                  # les « optionnels » comptent aussi
        if ing.verified == "C": res["confidence"] = "C"
        elif ing.verified == "B" and res["confidence"] == "A": res["confidence"] = "B"
    if r.imported: res["confidence"] = "C"
    return res

def availability(res, constraints: Set[str], strict: bool, rules: List[Rule]):
    """ok | ok_warning | adaptable | hidden  (Tome 1 §7.1 et §7.5)"""
    worst = "ok"
    need_sub = set(); warn = False
    for c in constraints:
        st = res[c]
        if st == "trace": st = "violates" if strict else "ok"
        if st == "uncertain":
            if strict: st = "violates"
            else: warn = True; continue
        if st == "violates":
            need_sub |= set(res["offenders"][c])
    if need_sub:
        covered = {ru.replaces for ru in rules if ru.status == "validated" and ru.satisfies & constraints}
        return "adaptable" if need_sub <= covered else "hidden"
    return "ok_warning" if warn else "ok"

def apply_substitutions(r: Recipe, rules: List[Rule], ings, recipes, constraints: Set[str], strict: bool):
    """Réécrit la recette en ne remplaçant QUE les ingrédients fautifs, puis REVÉRIFIE
    le résultat (invariant : jamais d'adaptation « présumée »)."""
    before = evaluate(r, ings, recipes)
    offenders = set()
    for c in constraints:
        st = before[c]
        if st == "trace" and not strict: continue
        if st == "uncertain" and not strict: continue
        offenders |= set(before["offenders"][c])
    by = {ru.replaces: ru for ru in rules
          if ru.status == "validated" and ru.satisfies & constraints and ru.replaces in offenders}
    new_lines = []
    for ln in r.lines:
        if ln.ing in by:
            for ing_id, ratio in by[ln.ing].items:
                new_lines.append(Line(ing=ing_id, qty=ln.qty * ratio, weight=ln.weight, optional=ln.optional))
        else:
            new_lines.append(ln)
    r2 = Recipe(r.id + "#variant", new_lines, r.imported)
    after = evaluate(r2, ings, {**recipes, r2.id: r2})
    ok = availability(after, constraints, strict, []) in ("ok", "ok_warning")
    return {"recipe": r2 if ok else None, "adapted": ok,
            "new_allergens": after["allergens"] - before["allergens"]}

# ---------------------------------------------------------------- suggestion (Tome 1 §6.3)
STAPLES = {"sel", "poivre", "eau", "huile", "sucre", "farine", "vinaigre", "moutarde"}

def suggest(recipes: List[Recipe], have: Set[str], expiring: Set[str] = frozenset(),
            subs: Dict[str, Set[str]] = None, staples=STAPLES, sub_credit=0.8):
    subs = subs or {}
    out = []
    for r in recipes:
        req = [l for l in r.lines if l.weight > 0 and not l.optional and l.ing]
        if not req: continue
        tot = sum(l.weight for l in req); got = 0.0; missing = []; used_sub = {}
        for l in req:
            if l.ing in have or l.ing in staples: got += l.weight
            elif subs.get(l.ing, set()) & have:
                got += l.weight * sub_credit; used_sub[l.ing] = sorted(subs[l.ing] & have)
            else: missing.append(l)
        score = 100 * got / tot
        score -= 15 * sum(1 for l in missing if l.weight == 3)          # manquant structurant
        score += 4 * len({l.ing for l in req} & set(expiring))          # bonus anti-gaspi
        bucket = "all" if not missing else ("almost" if len(missing) <= 2 and
                 not any(l.weight == 3 for l in missing) else ("ideas" if score >= 60 else None))
        if bucket: out.append({"id": r.id, "score": round(score, 1), "bucket": bucket,
                               "missing": [l.ing for l in missing], "substitutes": used_sub})
    return sorted(out, key=lambda x: (-x["score"], x["id"]))
```

## ANNEXE B : Tests exécutés et résultat

Fichier `test_engine.py` (28 contrôles, dont 2 **propriétés** sur 2 000 recettes aléatoires). Sortie réelle de l'exécution :

```text
PASS 1  lardons => pork=violates
PASS 2  règle validée => adaptable
PASS 3  variante recalculée sans porc
PASS 4  gélatine => uncertain
PASS 5  standard => ok_warning
PASS 6  strict sans règle => hidden
PASS 7  strict avec règle agar => adaptable
PASS 8  ingrédient inconnu => uncertain + confiance C
PASS 9  inconnu en strict => hidden
PASS 10 vanille liquide => alcohol=violates
PASS 11 règle poudre => adaptable
PASS 12 soja = trace : standard ok
PASS 13 soja = trace : strict, règle draft => hidden
PASS 14 allergène hérité de la sous-recette
PASS 15 cycle de sous-recettes détecté
PASS 16 lardons « facultatifs » comptent
PASS 17 substitut incertain => adaptation refusée (invariant)
PASS 18 seul l allergène réellement introduit est signalé (SO ; GL déjà présent via les pâtes)
PASS 19 LA retiré / FC ajouté
PASS 19b règle non appliquée à un ingrédient non fautif (crème intacte)
PASS 20 propriété : ajouter un ingrédient ne retire jamais un allergène (2000 cas)
PASS 21 propriété : 805 variantes acceptées, 0 avec porc/incertitude (strict) ; 0 refusées par le garde-fou
PASS 22 « tu as tout » : riz_oignon
PASS 23 1 manquant secondaire => « almost »
PASS 24 substitut compté (crème -> yaourt grec)
PASS 25 manquant structurant => exclue (couverture 72,7 % - 15 < 60)
PASS 26 bonus anti-gaspi (104 > 100)
PASS 27 substitut non possédé => crème reste manquante

28 contrôles OK
```

## ANNEXE C : Limites connues de l'implémentation de référence

| Limite | Conséquence | À faire |
|---|---|---|
| Pas de **quantités seuils** (sulfites ≥ 10 mg/kg, traces) | Allergènes binaires | Modéliser les seuils réglementaires (avis expert) |
| Pas de **synonymes / normalisation de noms** | Dépend du mapping canonique | Couche de normalisation (Tome 3 §1.2) |
| Pas de **règles spécifiques par recette** | Seules les règles génériques | Clé `(recipe_id, ingredient_id)` prioritaire |
| **Unités et mise à l'échelle** simplifiées | Ratio simple | Gérer `qty_per_100g`, unités, arrondis |
| Pas de **bonus saison / équipement / pénalité temps** | Suggestion simplifiée | Ajouter selon Tome 1 §6.3 |
| **Poids et pénalités** arbitraires | Classement non calibré | Calibrer (NDCG@5, §4.3) |
| **Performance** non mesurée | Cibles non confirmées | Benchmark sur 10 000 recettes |
| `trace` traité comme `violates` en Strict | Peut **sur-exclure** | Réglage utilisateur par ingrédient (P1) |
| Cas **aléatoires** construits sur un **petit référentiel** de test | Couverture limitée | Rejouer sur le référentiel réel (Tome 3) |
| Les tests prouvent la **logique**, pas la **justesse des données** | Un référentiel faux donne des résultats faux | Relecture humaine (Tome 3 §1.5, Tome 7 §4) |

> **Principe** : *le moteur garantit la cohérence du calcul ; seuls la vérification humaine et les audits (Tome 7) garantissent la justesse des données.*
