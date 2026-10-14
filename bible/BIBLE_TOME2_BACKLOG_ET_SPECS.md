# 📘 BIBLE ATLAS : TOME 2 : Backlog, spécifications techniques et tests

> Complément du **Tome 1** (`BIBLE_APPLICATION_CUISINE.md`). Les renvois « §x » pointent vers le Tome 1.
> Objectif : donner à l'équipe de quoi **démarrer le sprint 1** sans ambiguïté.

---

## 1. Backlog MVP (P0) : épopées et user stories

Format : **En tant que** [persona], **je veux** [action], **afin de** [bénéfice]. Chaque story a des **critères d'acceptation (CA)** testables.

### EPIC A : Onboarding & profil de foyer (§3.3)

**A1.** En tant que parent, je veux créer des profils pour chaque membre du foyer afin que les filtres s'appliquent automatiquement.
- CA1 : je peux ajouter ≥ 8 membres avec prénom, tranche d'âge, régimes, allergies (14 allergènes UE), aversions.
- CA2 : l'onboarding est **passable** ; les données restent modifiables dans Profil.
- CA3 : les allergies/régimes (données sensibles) exigent un **consentement explicite** séparé, révocable.
- CA4 : fonctionne hors-ligne ; synchronisation au retour du réseau.

**A2.** En tant qu'utilisateur, je veux déclarer mon équipement afin de ne voir que des recettes réalisables.
- CA1 : liste à cocher (four, plaques gaz/induction, cocotte, robot, Airfryer…).
- CA2 : une recette exigeant un équipement absent affiche « Équipement manquant » + alternative si elle existe.

**A3.** En tant que parent d'un foyer « sans porc / sans alcool », je veux choisir **Standard** ou **Strict** afin d'adapter le niveau d'exigence (§7.2).
- CA1 : le mode Strict exclut tout dérivé potentiel non vérifié (niveaux B/C, §7.1).
- CA2 : le niveau est affiché en permanence dans l'en-tête des résultats.

### EPIC B : Atlas & recherche (§5, §6)

**B1.** Naviguer par région (carte + liste équivalente).
- CA1 : 4 niveaux (macro-région → région → pays → terroir).
- CA2 : la **liste** offre exactement les mêmes accès que la carte (accessibilité).
- CA3 : chaque région affiche sa fiche culturelle et son « Menu découverte ».

**B2.** Rechercher par nom avec tolérance (accents, fautes, translittérations).
- CA1 : « tagine », « tajin », « tajine » → même résultat.
- CA2 : autocomplétion < 150 ms (p95) sur 10 000 entrées.
- CA3 : la recherche vocale (dictée système) fonctionne.

**B3.** Rechercher par liste d'ingrédients (§6.3).
- CA1 : saisie texte, chips et dictée ; hypothèse « placard de base » modifiable.
- CA2 : trois sections (« Tu as tout », « Il manque 1-2 trucs », « Idées »).
- CA3 : un ingrédient substituable (règle **validée**) compte comme possédé et affiche le substitut.
- CA4 : le mode « anti-gaspi » n'affiche que les recettes consommant ≥ X % des ingrédients saisis (X réglable).
- CA5 : les filtres du foyer sont appliqués par défaut.

**B4.** Filtrer par catégorie : enfants, techniques, pains/bases, sauces, fêtes.

### EPIC C : Filtres alimentaires & substitutions (§7)

**C1.** Filtres porc / alcool / allergènes **calculés** depuis les ingrédients et leurs dérivés.
- CA1 : un ingrédient avec dérivé non résolu rend la recette « non garantie » dans les profils stricts.
- CA2 : badge de confiance A/B/C visible sur chaque fiche.
- CA3 : test CI bloquant (cf. §4 de ce tome).

**C2.** « Voir la version sans porc / sans alcool ».
- CA1 : bascule A/B en 1 tap ; ingrédients, quantités et ajustements d'étapes réécrits.
- CA2 : seules les règles « validées » sont présentées comme « goût préservé » ; les autres sont étiquetées « à tester ».
- CA3 : si aucune règle fiable, message « non adaptable » + 3 recettes proches.

**C3.** Message explicite : « La cuisson ne fait pas disparaître tout l'alcool. »

### EPIC D : Fiche recette, mode cuisine, audio (§8)

**D1.** Fiche recette complète (champs §8.2).
- CA1 : °C **et** thermostat toujours affichés ensemble.
- CA2 : mise à l'échelle des portions avec règles non linéaires (sel, levure, temps).
- CA3 : bascule métrique / cups.

**D2.** Mode cuisine : écran allumé, grande typographie, swipe + boutons, clip d'étape en boucle.
- CA1 : zones tactiles ≥ 64 dp ; texte ≥ 24 pt par défaut.
- CA2 : fonctionne **hors-ligne** si la recette est téléchargée.
- CA3 : l'écran se réactive normalement à la sortie (pas de fuite de wake lock).

**D3.** Minuteurs multiples nommés.
- CA1 : un tap sur une durée dans le texte crée le minuteur.
- CA2 : persiste en arrière-plan et après redémarrage ; notification locale à l'échéance.

**D4.** Lecture audio (§8.6).
- CA1 : 3 modes (continu, pas à pas, résumé).
- CA2 : normalisation « 1/2 → un demi », « c. à s. → cuillère à soupe », « 180 °C (th. 6) » lus correctement.
- CA3 : commandes de l'écran verrouillé et du casque (lecture/pause/suivant).
- CA4 : pause automatique sur appel entrant ; reprise.
- CA5 : TTS système en repli pour toute recette sans audio premium.

**D5.** Commandes vocales : « suivant », « répète », « précédent », « minuteur X minutes ».
- CA1 : reconnaissance FR ≥ 90 % sur un jeu de 200 énoncés (bruit de cuisine simulé).

### EPIC E : Imports (§14)

**E1.** Partager vers ATLAS depuis TikTok / Instagram / YouTube / Safari (Share Extension iOS, Intent Android).
- CA1 : le lien arrive dans la file d'imports en < 2 s, même si l'app est fermée.

**E2.** Coller un lien.

**E3.** Extraction et revue.
- CA1 : champs à faible confiance (< seuil) surlignés ; édition en 1 écran.
- CA2 : aucune vidéo tierce stockée ; lien + crédit conservés.
- CA3 : « quantité non précisée » signalée plutôt qu'inventée.

**E4.** Tri automatique : cuisine/région, type de plat, régime, difficulté, temps, enfants.
- CA1 : correction manuelle mémorisée pour les imports suivants.
- CA2 : doublon détecté avec proposition de fusion.

**E5.** Quota gratuit (3 imports/mois) et message clair avant dépassement.

### EPIC F : Frigo, courses, planning (§6.4, §13)

**F1.** Frigo virtuel avec dates limites et alertes « à consommer d'abord ».
**F2.** Liste de courses fusionnée par rayon, partageable, export vers Rappels/Notes.
**F3.** Planning hebdomadaire (glisser-déposer).
**F4.** Bloc « Ce qu'il vous reste » sur chaque recette (§13.2).

### EPIC G : Contenu P0 (§9, §10, §11, §12)

**G1.** 30 techniques, 20 recettes pains/bases, 20 sauces, 5 fêtes avec menus types.
**G2.** Composeur de menu **minimal** : à partir d'un plat, 1 proposition entrée/dessert (le moteur complet est P1).
**G3.** Accords boissons **sans alcool** pour les plats principaux (alcool P1 avec vérification d'âge).

### EPIC H : Compte, abonnement, conformité

**H1.** Sign in with Apple, Google, e-mail/passkey.
**H2.** Suppression de compte **dans l'app** ; export des données (JSON + PDF).
**H3.** Abonnement ATLAS+ (StoreKit 2 / Google Play Billing), restauration d'achats, résiliation expliquée.
**H4.** Signalement d'un contenu (recette importée partagée, commentaire).
**H5.** Mode enfant protégé par code parent : sans pub, sans lien externe, sans achat.

---

## 2. Priorisation du sprint 1 → 6 (proposition)

| Sprint | Objectif | Livrables |
|---|---|---|
| **S1** | Socle | Design system, CI/CD, auth, modèle de données, CMS minimal, référentiel ingrédients (500 premiers) |
| **S2** | Catalogue | Fiche recette, atlas liste, recherche par nom (Meilisearch), 50 recettes saisies |
| **S3** | Diététique | Moteur porc/alcool/allergènes + dérivés, tests dorés CI, badges de confiance |
| **S4** | Cuisiner | Mode cuisine, minuteurs, wake lock, hors-ligne basique |
| **S5** | Voix | Pipeline TTS + normalisation, lecteur audio, commandes vocales |
| **S6** | Ingrédients | Recherche par ingrédients + frigo + courses ; **jalon : bêta fermée TestFlight** |

---

## 3. Spécification API (REST, extrait v1)

Base : `https://api.atlas.example/v1` · Auth : OAuth2/OIDC (Bearer) · Format : JSON · Pagination : curseur.

| Méthode | Route | Description |
|---|---|---|
| GET | `/regions` · `/regions/{id}` | Arbre et fiche de région |
| GET | `/recipes?region=&q=&diet=&exclude_allergens=&max_time=&kids=&equipment=` | Liste filtrée (le profil du foyer est appliqué côté serveur si `household_id` fourni) |
| GET | `/recipes/{id}?variant=no_pork,no_alcohol&servings=6` | Fiche recette, éventuellement **réécrite** selon les substitutions |
| POST | `/recipes/suggest` | Corps : `{ingredients[], pantry_assumption[], household_id, anti_waste: bool}` → recettes scorées (§6.3) |
| GET | `/techniques` · `/techniques/{id}` | Techniques |
| GET | `/sauces/formulas` · POST `/sauces/build` | Sauce Builder (ratios) |
| POST | `/menus/compose` | `{anchor_recipe_id, guests[], constraints}` → 3 menus (§12.3) |
| GET | `/pairings?recipe_id=&alcohol=false` | Accords boissons |
| GET/POST/PATCH/DELETE | `/pantry/items` | Frigo virtuel |
| GET/POST | `/shopping-lists` · `/{id}/items` | Courses (fusion automatique) |
| GET/PUT | `/meal-plans/{week}` | Planning |
| POST | `/imports` | `{url}` ou fichier d'export → crée un `ImportJob` |
| GET | `/imports/{id}` | Statut + brouillon + confiances par champ |
| POST | `/imports/{id}/confirm` | Valide après revue |
| GET | `/audio/recipes/{id}` | Manifeste audio (pistes par étape, SSML normalisé) |
| GET/PUT | `/households/{id}` | Profil foyer (données sensibles, consentement requis) |
| POST | `/reports` | Signalement |
| DELETE | `/me` · GET `/me/export` | Suppression / export RGPD |

**Erreurs** : format RFC 7807 (`application/problem+json`). **Idempotence** : en-tête `Idempotency-Key` sur POST d'imports et d'achats. **Versionnage** : préfixe `/v1`, dépréciation annoncée 6 mois.

---

## 4. Tests dorés du moteur diététique (jeu de départ)

Ces cas deviennent des **tests automatisés bloquants** (CI). Chaque ligne = un test.

### 4.1 Porc

| # | Entrée (ingrédient) | Attendu (Standard) | Attendu (Strict) |
|---|---|---|---|
| 1 | lardons de porc | `pork = true` (A) | `pork = true` |
| 2 | gélatine alimentaire (origine non précisée) | `pork = possible` (B) | **exclu** |
| 3 | gélatine de bœuf (origine précisée) | `pork = false` | `false` |
| 4 | bouillon cube (liste non vérifiée) | `pork = possible` (B) | **exclu** |
| 5 | bouillon maison de volaille | `false` (A) | `false` |
| 6 | saindoux | `true` | `true` |
| 7 | merguez (agneau/bœuf, origine vérifiée) | `false` | `false` |
| 8 | chorizo (origine non précisée) | `pork = true` par défaut | `true` |
| 9 | présure (fromage) | `false` pour porc ; **flag « présure »** pour Halal/Végé | idem |
| 10 | recette importée (confiance C) sans ingrédients détaillés | `unknown` | **exclu** |

### 4.2 Alcool

| # | Entrée | Standard | Strict |
|---|---|---|---|
| 11 | vin rouge (déglaçage) | `alcohol = true` | `true` |
| 12 | extrait de vanille liquide | `true` (alcool résiduel) | `true` → proposer poudre/gousse |
| 13 | gousse de vanille | `false` | `false` |
| 14 | sauce soja | `trace` | `exclu` (selon réglage) |
| 15 | mirin | `true` | `true` |
| 16 | vinaigre de cidre | `false` | `false` |
| 17 | vinaigre de vin | `trace` (signalé) | selon réglage |
| 18 | bière 0,0 % | `trace` (≤ 0,5 %) | `exclu` |
| 19 | rhum (flambé) | `true` | `true` ; message « l'alcool ne disparaît pas totalement » |

### 4.3 Allergènes & héritage

| # | Cas | Attendu |
|---|---|---|
| 20 | pâte brisée (farine de blé, beurre, œuf) | gluten, lait, œufs |
| 21 | sauce algérienne (mayo à l'œuf, moutarde) | œufs, moutarde |
| 22 | tahini | sésame |
| 23 | vinaigrette avec vin blanc | sulfites (si ≥ seuil) + alcool trace |
| 24 | recette A contient « sauce B » | allergènes de B **hérités** par A |
| 25 | substitution (crème → yaourt grec) | recalcul : lait toujours présent ; badge « sans lait » **interdit** |

### 4.4 Substitutions

| # | Cas | Attendu |
|---|---|---|
| 26 | « Version sans porc » d'une carbonara | lardons → bœuf/magret fumé + paprika ; **aucun** dérivé porcin ; badge A conservé uniquement si règle `validated` |
| 27 | « Version sans alcool » d'un bœuf bourguignon | vin → jus de raisin + vinaigre ; temps de réduction ajusté |
| 28 | Règle `draft` | **jamais** libellée « goût préservé » |
| 29 | Aucune règle disponible | message « non adaptable » + alternatives |
| 30 | Profil Strict + recette importée (C) | recette masquée ou bandeau d'avertissement bloquant |

### 4.5 Propriétés (property-based testing)
- **Invariant 1** : toute recette marquée `pork=false` (A) ne contient aucun ingrédient dont `derivatives` inclut `pork` non résolu.
- **Invariant 2** : après substitution, `pork(recipe') = false` si la contrainte « sans porc » était demandée, sinon la recette est `non adaptable`.
- **Invariant 3** : l'ajout d'un ingrédient ne peut **jamais** retirer un allergène du calcul.

---

## 5. Schéma SQL de base (PostgreSQL, extrait)

```sql
-- Référentiel
CREATE TABLE ingredient (
  id TEXT PRIMARY KEY,                 -- ing_poulet_cuisses
  name_fr TEXT NOT NULL,
  aliases TEXT[] DEFAULT '{}',
  category TEXT,                       -- viande, légume, épice…
  availability TEXT CHECK (availability IN ('green','yellow','orange','red')),
  density_g_per_ml NUMERIC,
  shelf_life_fridge_days INT,
  shelf_life_freezer_months INT
);

CREATE TABLE ingredient_derivative (
  ingredient_id TEXT REFERENCES ingredient(id),
  kind TEXT CHECK (kind IN ('pork','alcohol','animal','gluten','lactose','other')),
  level TEXT CHECK (level IN ('certain','possible','trace')),
  note TEXT,
  verified_by TEXT, verified_at DATE,
  PRIMARY KEY (ingredient_id, kind)
);

CREATE TABLE ingredient_allergen (
  ingredient_id TEXT REFERENCES ingredient(id),
  allergen TEXT CHECK (allergen IN ('gluten','crustaces','oeufs','poissons','arachides','soja','lait','fruits_a_coque','celeri','moutarde','sesame','sulfites','lupin','mollusques')),
  PRIMARY KEY (ingredient_id, allergen)
);

CREATE TABLE ingredient_part (
  id TEXT PRIMARY KEY,
  ingredient_id TEXT REFERENCES ingredient(id),
  part_name TEXT,                      -- fanes, zeste, carcasse…
  edible BOOLEAN DEFAULT TRUE
);

CREATE TABLE valorisation (
  part_id TEXT REFERENCES ingredient_part(id),
  recipe_id TEXT,                      -- recette de valorisation
  PRIMARY KEY (part_id, recipe_id)
);

-- Recettes
CREATE TABLE recipe (
  id TEXT PRIMARY KEY,
  title_fr TEXT NOT NULL,
  title_original TEXT, translit TEXT,
  cuisine_id TEXT, region_id TEXT,
  servings INT, active_min INT, passive_min INT,
  difficulty SMALLINT, cost_band SMALLINT,
  verification_level CHAR(1) CHECK (verification_level IN ('A','B','C')),
  source_type TEXT CHECK (source_type IN ('editorial','import','community')),
  source_url TEXT, source_credit TEXT,
  published_at TIMESTAMPTZ
);

CREATE TABLE recipe_ingredient (
  recipe_id TEXT REFERENCES recipe(id),
  position SMALLINT,
  ingredient_id TEXT REFERENCES ingredient(id),
  qty NUMERIC, unit TEXT,
  weight SMALLINT CHECK (weight BETWEEN 0 AND 3),
  prep TEXT, optional BOOLEAN DEFAULT FALSE,
  PRIMARY KEY (recipe_id, position)
);

CREATE TABLE step (
  recipe_id TEXT REFERENCES recipe(id),
  n SMALLINT, text_fr TEXT, duration_s INT, is_critical BOOLEAN DEFAULT FALSE,
  clip_id TEXT, photo_id TEXT,
  PRIMARY KEY (recipe_id, n)
);

-- Substitutions
CREATE TABLE substitution (
  id TEXT PRIMARY KEY,
  replaces_ingredient_id TEXT REFERENCES ingredient(id),
  recipe_id TEXT NULL,                 -- NULL = règle générique
  constraint_satisfied TEXT[],         -- {'no_pork','no_alcohol'}
  functions TEXT[],
  status TEXT CHECK (status IN ('draft','testing','validated','retired')),
  taste_delta_mean NUMERIC, n_testers INT,
  step_adjustments TEXT[]
);

CREATE TABLE substitution_item (
  substitution_id TEXT REFERENCES substitution(id),
  ingredient_id TEXT REFERENCES ingredient(id),
  ratio NUMERIC, qty_per_100g NUMERIC, unit TEXT, note TEXT
);

-- Utilisateurs
CREATE TABLE household (id UUID PRIMARY KEY, owner_id UUID, strictness TEXT CHECK (strictness IN ('standard','strict')));
CREATE TABLE household_member (
  id UUID PRIMARY KEY, household_id UUID REFERENCES household(id),
  display_name TEXT, age_band TEXT,
  diets TEXT[], allergens TEXT[], dislikes TEXT[],
  consent_sensitive_at TIMESTAMPTZ     -- consentement art. 9 RGPD
);
CREATE TABLE pantry_item (
  id UUID PRIMARY KEY, household_id UUID, ingredient_id TEXT,
  qty NUMERIC, unit TEXT, zone TEXT, best_before DATE, use_by DATE
);

-- Imports
CREATE TABLE import_job (
  id UUID PRIMARY KEY, user_id UUID, source_url TEXT, platform TEXT,
  status TEXT, confidence JSONB, draft JSONB, created_at TIMESTAMPTZ DEFAULT now()
);
```

**Index utiles** : GIN sur `aliases`, index composite `(recipe_id, ingredient_id)`, `pgvector` sur l'embedding de recette (similarité/dédoublonnage), partition des événements analytics par mois.

**Vue calculée** : `recipe_diet` (matérialisée) recalculée à chaque modification d'ingrédient ou de dérivé.

---

## 6. Plan d'événements analytics (sans PII)

| Événement | Propriétés |
|---|---|
| `onboarding_completed` | `members_count`, `skipped_steps[]` |
| `search_performed` | `mode` (name/region/ingredients), `results_count`, `filters[]` |
| `ingredient_search_result_opened` | `bucket` (all/almost/ideas), `score_band` |
| `recipe_viewed` | `recipe_id`, `source` |
| `diet_variant_toggled` | `variant` (no_pork/no_alcohol), `rule_status` |
| `cooking_started` / `cooking_completed` | `recipe_id`, `duration_vs_estimate`, `used_audio`, `used_voice` |
| `timer_started` | `from_text` (bool) |
| `audio_played` | `mode`, `voice_type` (premium/system), `speed` |
| `import_started` / `import_confirmed` | `platform`, `confidence_avg`, `fields_edited` |
| `menu_composed` / `menu_adopted` | `anchor_course`, `zero_waste_score` |
| `pantry_alert_actioned` | `items_count` |
| `recipe_feedback` | `worked` (bool), `issue_tag` |
| `paywall_viewed` / `subscribed` | `trigger`, `plan` |

Règles : **pas de contenu saisi libre**, **pas d'identifiants publicitaires**, **identifiant pseudonyme rotatif**, données de régime/allergie **jamais** envoyées aux outils analytics tiers.

---

## 7. Définition du « Done » technique (extrait)

- [ ] Tests unitaires du moteur ≥ 90 % de couverture sur les modules diététique/substitution.
- [ ] Les 30 tests dorés passent en CI.
- [ ] Audit d'accessibilité (VoiceOver + TalkBack + clavier) sans bloquant.
- [ ] Performances : démarrage à froid < 2 s (iPhone milieu de gamme), recherche < 150 ms p95.
- [ ] Mode avion : mode cuisine, minuteurs, audio téléchargé, courses et frigo fonctionnent.
- [ ] Revue sécurité (OWASP MASVS L1) ; pas de secret dans le dépôt.
- [ ] Checklist App Store (§17.4 du Tome 1) validée, notes de revue rédigées.
- [ ] Mentions légales, CGU, politique de confidentialité, déclaration d'accessibilité publiées.

---

## 8. Prochains volumes possibles

| Tome | Contenu |
|---|---|
| **Tome 3** | **Référentiel ingrédients V1** (500 entrées : dérivés, allergènes, parties, disponibilité France) |
| **Tome 4** | **Catalogue éditorial** : 600 recettes P0 classées par région avec fiches de brief |
| **Tome 5** | **Design system détaillé** : composants, états, tokens, maquettes écran par écran |
| **Tome 6** | **Style guide éditorial & charte de tournage** (rédaction, voix off, cadrages, lumière) |
| **Tome 7** | **Fiches de test** (protocoles de tests goût à l'aveugle, QA accessibilité, recette de bêta) |
