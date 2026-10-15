# 📚 BIBLE ATLAS : Index général et guide de lecture

> Application de cuisine du monde (iOS, iPadOS, macOS, watchOS, Android, Web) : recettes par région, vidéos/photos, audio, filtres enfants / sans porc / sans alcool avec substitutions, import TikTok & co, techniques, pains & bases, sauces maison, fêtes & menus, zéro déchet.
> **10 documents (tomes 1 à 8, 11 et 12) · ≈ 9 470 lignes** · Markdown, en français · + code de référence testé (`atlas_engine.py`, `test_engine.py`) + générateurs (`load_ref.py`, `recipes_data.py`, `recipes_v1_*.py`, `build_tome11.py`, `build_tome12.py`, `export_app_data.py`).
> **Application ATLAS v1** (dossier `../app`) : PWA iPhone, iPad, Mac, Android, PC, construite sur cette bible (Tome 12 §5).
> **Recettes classées** (dossier `../recettes-classees`) : favoris TikTok et site Cooking with Morgane (Tome 12 §3).

---

## 1. Les tomes livrés

| Tome | Fichier | Contenu | Lignes |
|---|---|---|---|
| **1** | `BIBLE_APPLICATION_CUISINE.md` | Vision, personas, architecture de l'information, atlas des régions, recherche (nom / région / ingrédients), filtres porc-alcool-allergènes et **moteur de substitution**, fiche recette, **mode cuisine & audio**, techniques, pains & bases, sauces, fêtes & menus & boissons, **zéro déchet**, **import social**, équipement France, UX/UI, **architecture technique & Apple**, modèle de données, légal, production, business, roadmap, risques | 1 203 |
| **2** | `BIBLE_TOME2_BACKLOG_ET_SPECS.md` | Backlog MVP (8 épopées, critères d'acceptation), sprints 1-6, **API REST**, **30 tests dorés** du moteur diététique, **schéma SQL**, plan analytics, « Done » technique | 394 |
| **3** | `BIBLE_TOME3_REFERENTIEL_INGREDIENTS.md` | **713 lignes d'ingrédients** : allergènes, dérivés porc/alcool/animal, disponibilité en France, zéro déchet ; 17 alternatives sans porc ; 43 alcools avec substituts ; 94 produits du monde ; 27 substituts ; annexes (additifs, conservation, densités) | 1 055 |
| **4** | `BIBLE_TOME4_CATALOGUE_EDITORIAL.md` | **381 titres de recettes** classés par région avec statut porc/alcool/enfants, **fiche de brief**, grille de sélection, blocs transversaux (pains, sauces, enfants, fêtes, zéro déchet, boissons), décisions éditoriales, planning de production | 637 |
| **5** | `BIBLE_TOME5_DESIGN_SYSTEM.md` | **Palette corrigée (contrastes calculés)**, tokens, typographie, composants et états, écrans P0, mouvement, accessibilité, Live Activities / widgets / Watch, microcopie, passation | 518 |
| **6** | `BIBLE_TOME6_STYLE_EDITORIAL_ET_TOURNAGE.md` | Voix et ton, règles d'écriture des recettes, noms de plats, sensibilité culturelle, **écriture audio-first + lexique de prononciation**, **charte de tournage et de photo**, specs vidéo/son, modèles | 450 |
| **7** | `BIBLE_TOME7_PROTOCOLES_DE_TEST.md` | Test de recette domestique, **protocole de test de goût à l'aveugle (seuils statistiques calculés)**, QA diététique / accessibilité / audio / imports / technique / RGPD, UAT, **plan de bêta**, checklists stores, incident Sev 0, Go/No-Go | 552 |
| **8** | `BIBLE_TOME8_ADR_ET_MOTEURS.md` | **17 décisions d'architecture (ADR)**, spécification des moteurs (diététique, substitution, suggestion ✅ **testés** ; menu, anti-gaspi, import, synchronisation, audio, recalcul 🟡 spécifiés), SLO ; **code de référence Python + 28 contrôles passés** | 544 |
| **11** | `BIBLE_TOME11_VAGUE0_RECETTES_ETALONS.md` | **11 fiches étalons** (tajine, yassa, dal, carbonara, bourguignon, pad thaï, ratatouille, baguette, mayonnaise, sauce algérienne, crêpes) au format du Tome 6, reliées ligne à ligne au référentiel (Tome 3), **badges calculés par le moteur (Tome 8)**, variantes sans porc / sans alcool / sans œuf **à tester**, démonstration de suggestion, **rapport d'écarts du référentiel** ; **non testées en cuisine** | 917 |
| **12** | `BIBLE_TOME12_VAGUE1_ET_APPLICATION.md` | **59 fiches de la vague 1** (pains et bases, sauces maison et frites, plats et entrées du monde, desserts, fêtes, anti-gaspi, boissons sans alcool), badges calculés par le moteur ; **corpus importé** (585 favoris TikTok + 339 recettes Cooking with Morgane classés), catégorie **Food fusion**, **vidéos liées aux fiches et lues dans l'application** ; **41 règles de substitution génériques** ; **application v1** : choix techniques, couverture des 10 modules, limites, vérifications (41 tests), **comptes La cuisine de Marina et NiangCook**, **zéro déchet ingrédient par ingrédient** (§6), **138 photos sous licence libre** (§7), mode d'emploi ; décisions D13-D20 ; **non testées en cuisine** | 3333 |
| **13** | `BIBLE_TOME13_VAGUE2.md` | **506 fiches de la vague 2** : France région par région, Europe, Maghreb, Afrique, Moyen-Orient, Asie, Amériques, Océanie, food fusion, **pâtisserie française**, **chocolats d'occasion**, **condiments et marinades maison** (bouillon cube, nokoss…), sauces à frites, boulangerie, enfants, quotidien, anti-gaspi, boissons sans alcool, cahier du chef ; **39 nouvelles techniques** (pâtisserie, chocolat, boulangerie, poissons, viandes, cuissons, œufs, condiments) avec tableaux de températures ; **habillage graphique** ; décisions D21-D25 ; **non testées en cuisine** | 13666 |
| **Audit** | `AUDIT_ATLAS_2026-10-15.md` | Audit à quatre regards (débutant, chef étoilé, UX/UI, développeur) mesuré sur les 576 fiches et le code ; corrections du jour (aide au débutant, filtres, classement automatique des liens, poids) ; feuille de route priorisée | 150 |

---

## 2. Ordre de lecture selon le métier

| Rôle | Lire dans cet ordre |
|---|---|
| **Direction / Product Owner** | T1 §1-4 → T1 §21-22 → **T12 §5-8** → T2 §1-2 → T4 §1, §16-17 → T7 §14 |
| **Chef·fe exécutif·ve / éditorial** | T1 §5, §7, §9-13 → **T3** → **T4** → **T6** → **T11** → **T12 §1-3** → T7 §2-3 |
| **Diététicien·ne** | T1 §7 → **T3 §1, §3, §5, §12, §14** → T2 §4 → T7 §3-4, §13 |
| **Développeur·se (mobile/web)** | T1 §17-18 → **T2** → **T8** → **T12 §4-5** (application v1) → T5 §3-7 → T7 §8 |
| **Backend / data / IA** | T1 §14, §17-18 → T2 §3-6 → **T8** → T3 §17.5 → T7 §4, §7 |
| **Designer UI/UX** | T1 §16 → **T5** → T6 §4, §14 → T7 §5 |
| **Vidéaste / photographe** | T1 §8.4 → **T6 §9-16** |
| **QA / test** | **T7** → T2 §4, §7 → T5 §9 |
| **Juridique / DPO** | T1 §19 → T7 §8.5, §11 → T6 §6, §15 |

---

## 3. Dépendances entre tomes

```
T1 Vision & produit ─┬─► T2 Backlog & specs ─────────────┐
                     ├─► T3 Référentiel ingrédients ──┬──┼─► moteur diététique & substitutions
                     ├─► T4 Catalogue éditorial ◄─────┘  │
                     ├─► T5 Design system ───────────────┤
                     └─► T6 Style & tournage ────────────┤
                                                         ▼
            T8 ADR & moteurs (code de référence testé)  ─►  T7 Tests, qualité, bêta, Go/No-Go

T3 + T6 + T8 ─► T11 / T12 fiches ─► export_app_data.py ─► application v1 (../app)
```
- **T3 est le socle de la promesse « sans porc / sans alcool »** : sans référentiel vérifié, le moteur (T2) et le catalogue (T4) ne tiennent pas.
- **T7 conditionne le lancement** : aucune règle de substitution n'est présentée comme « goût préservé » avant validation (T7 §3.6).

---

## 4. ⚠️ Points d'attention transverses (à lire avant de s'engager)

| # | Point | Où |
|---|---|---|
| 1 | **Palette corrigée** : trois couleurs de marque du Tome 1 échouent au contraste AA pour du texte. **Le Tome 5 fait foi** (une note de correction a été ajoutée dans le Tome 1). | T5 §2 |
| 2 | **Référentiel non vérifié** : les 713 lignes sont au niveau « brouillon ». Les allergènes/dérivés sont prudents mais exigent une **double relecture diététicien·ne + chef·fe**. | T3 §1.5, §18 |
| 3 | **Statuts porc/alcool du catalogue = pré-évaluations** : le moteur recalcule, **le moteur prime**. | T4 §1.4 |
| 4 | **Substitutions « à tester »** : aucune n'est validée au goût. | T3 §16, T7 §3 |
| 5 | **Seuils de validation du goût** : critères internes simples ; à faire valider par un·e spécialiste de l'analyse sensorielle avant toute communication publique. | T7 §3.6 |
| 6 | **Spécifications vidéo/audio/débits** : points de départ à confirmer par des tests d'encodage et sur appareils réels. | T6 §12, T7 §8 |
| 7 | **Juridique** : cadrage opérationnel, **pas un avis juridique**. Faire valider RGPD (données de santé/religion), loi Evin, DSA, accessibilité, droit d'auteur des imports. | T1 §19 |
| 8 | **Politiques des plateformes et API sociales** : évoluent vite (accès aux « favoris » TikTok/Instagram, règles App Store/Play, limites Live Activities). Marqués 🔎. | T1 §14, §17.4, T7 §11 |
| 9 | **Volumes** : 713 ingrédients (avec doublons de sections), 381 titres de recettes. Les **600 recettes** du MVP incluent les blocs transversaux ; ≈ 12 titres d'atlas restent à commander. | T3 §18, T4 §1 |
| 10 | **Plats à porc indissociable** (cassoulet, choucroute, fabada, feijoada) : traités comme « non adaptables », avec recette d'origine étiquetée et version « inspirée » nommée comme telle. | T4 §16 |
| 11 | **Moteurs** : seuls diététique, substitution et suggestion sont **exécutés** (28 contrôles) ; menu, import, synchronisation, audio sont **spécifiés mais non prototypés** ; paramètres à calibrer. | T8 en-tête, annexe C |
| 12 | **Tomes 11 et 12 : recettes non testées.** Quantités et temps = pratiques usuelles, **à confirmer** par les Tests 1 et 2 (Tome 7 §2). Badges calculés avec un référentiel de **confiance C**. Le rapport d'écarts (T11 §14) liste ce qui manque au référentiel (eau, relation œuf → jaune, moutarde sans vin). | T11 en-tête, §14 ; T12 en-tête |
| 13 | **Application v1 = PWA** (écart avec D2) : sur iPhone, pas de minuteur qui sonne application fermée, pas de Live Activity ni de Watch ; les versions adaptées par des règles `draft` sont affichées **« à tester »** (D13). | T12 §4, §5.3 |
| 14 | **Corpus TikTok et sites** : liens crédités uniquement, aucune recopie de texte ni de média (droit d'auteur). Tri TikTok manuel, tri du site automatique. Les vidéos se lisent dans l'application par les intégrations officielles (rien n'est copié) ; une vidéo retirée par son auteur·e ne se lit plus. | T12 §3 |

---

## 5. Registre consolidé des décisions ouvertes

| # | Décision | Source | Recommandation actuelle | Échéance |
|---|---|---|---|---|
| D1 | Nom définitif et identité de marque | T1 §23.5 | Vérifier INPI / stores | Phase 0 |
| D2 | Flutter vs natif | T1 §17.1, §23.5 | **Flutter + modules Swift/Kotlin** après prototype de 2 semaines | Sprint 0 |
| D3 | Fournisseurs vidéo / TTS / recherche | T1 §23.5 | Benchmark coût, qualité, hébergement UE | Sprint 0-1 |
| D4 | Périmètre MVP (5 ou 8 macro-régions) | T1 §23.5 | 5 régions solides plutôt que 12 faibles | Phase 0 |
| D5 | Politique halal / casher | T1 §7.2, §23.5 | Halal-compatible en V1 (signal, pas certification) ; casher en V2 | Phase 0 |
| D6 | Stratégie d'import TikTok au lancement | T1 §14 | Partage + lien + export de données ; API officielle selon accès | Sprint 3 |
| D7 | Modèle de tarification | T1 §21 | Freemium + abonnement famille ; tests de prix | Avant bêta |
| D8 | Foie gras / gibier / cheval | T4 §16 | Foie gras et cheval hors MVP ; gibier saisonnier oui | Vague 0 |
| D9 | Tutoiement / vouvoiement | T6 §1 | Tutoiement par défaut | Phase 0 |
| D10 | Polices (Fraunces/Inter) et licences | T5 §3.1 | Valider la version OFL à embarquer | Sprint 1 |
| D11 | Consultants culturels par région | T6 §6 | Un·e par macro-région avant la vague 1 | Vague 0 |
| D12 | Panel de dégustation (recrutement, lieu, budget) | T7 §3 | 36 personnes minimum par règle validée | Avant vague 1 |
| D13 | Afficher les versions adaptées par des règles `draft` | T12 §4 | Oui, étiquetées « à tester » ; « goût préservé » réservé aux règles validées | Avant bêta |
| D14 | PWA d'abord, native ensuite | T12 §5.1 | PWA pour la bêta fermée ; prototype natif pour minuteur, Live Activities, Watch | Sprint 0 |
| D15 | Usage du corpus TikTok / sites | T12 §3 | Liens crédités et inspiration de briefs ; jamais de recopie | Phase 0 |
| D16 | Végétarien et fromages à présure animale | T12 §8 | Avertissement en v1 ; arbitrage diététicien·ne | Avant bêta |
| D17 | Catégorie « Food fusion » | T12 §3.4 | Entrée d'atlas transversale ; la fiche garde sa cuisine principale (T1 §5.2) | Fait (v1) |
| D18 | Lecture de vidéos tierces dans l'application | T12 §3.5 | Intégrations officielles TikTok / YouTube sans cookie, chargées au clic, crédit + lien | Avant bêta |
| D19 | Images manquantes : génération IA ? | T12 §7 | Non par défaut ; sinon modèle photoréaliste local et étiquette « image générée » | Avant bêta |
| D20 | Durées de conservation des restes | T12 §6 | Validation diététicien·ne + hygiène | Avant bêta |

---

## 6. Plan des 30 premiers jours (proposition)

| Semaine | Actions |
|---|---|
| **S1** | Constituer le noyau (PO, chef·fe exécutif·ve, diététicien·ne, lead dev, lead design) ; trancher D1, D4, D5, D9 ; lancer le **recrutement des consultants culturels** (D11) |
| **S2** | **Prototype technique** (vidéo + audio + minuteur en arrière-plan) pour D2/D3 ; démarrer la **relecture du référentiel** (familles à risque : T3 §3, §5, §12, §14, §15) |
| **S3** | **Figma** : fondations + 10 composants du T5 ; **brief des 30 recettes étalons** (T4 §17, vague 0) ; avis juridique initial (RGPD, Evin) |
| **S4** | **Setup** CI/CD + **30 tests dorés** (T2 §4) ; premier tournage d'essai (T6) ; recrutement du **panel de testeurs domestiques** (T7 §2.5) ; **revue de jalon** et décisions D6-D8 |

---

## 7. Tomes complémentaires possibles

| Tome | Sujet | Utilité |
|---|---|---|
| ~~8~~ | ~~ADR techniques + moteurs~~ | ✅ **Livré** : `BIBLE_TOME8_ADR_ET_MOTEURS.md` |
| **9** | **Pack juridique** : trames CGU / politique de confidentialité / DPIA / registre des traitements / charte de modération (à valider par un avocat) | Sécuriser le lancement |
| **10** | **Go-to-market** : positionnement, ASO, SEO des pages recettes, partenariats, plan de lancement, métriques d'acquisition | Faire connaître le produit |
| **11** | **Catalogue complet des 600 recettes** : fiches de brief remplies vague par vague | **Vague 0 (11 fiches, T11) et vague 1 (59 fiches, T12) livrées** ; reste ≈ 530 fiches |
| ~~12~~ | ~~Vague 1 + application~~ | ✅ **Livré** : `BIBLE_TOME12_VAGUE1_ET_APPLICATION.md` |
| ~~13~~ | ~~Vague 2 + techniques de chef~~ | ✅ **Livré** : `BIBLE_TOME13_VAGUE2.md` |
| **13** | **Plan de formation / onboarding** des chefs, testeurs, modérateurs | Industrialiser la qualité |

---

## 8. Conventions communes à tous les tomes

- **Pastilles** : 🍳 chef · 💻 dev · 🎨 UX/UI · ⚠️ angle mort comblé · 🔎 à vérifier à l'implémentation.
- **Priorités** : **P0** (MVP), **P1** (V1.x), **P2** (V2+).
- **Renvois** : « T1 §7.5 » = Tome 1, section 7.5. Tous les renvois entre tomes ont été **vérifiés** (existence des sections cibles).
- **Niveaux de confiance des données** : A (vérifié) · B (calculé) · C (non vérifié).
- **Principe cardinal** : *en cas de doute sur un régime ou un allergène, on signale ; on ne devine jamais.*
