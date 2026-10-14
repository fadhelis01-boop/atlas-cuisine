# 📕 BIBLE ATLAS : TOME 5 : Design system détaillé

> Complète le Tome 1 §16 (UX/UI). Ce tome **corrige** la palette du Tome 1 après calcul des contrastes (§2) et fournit les tokens, composants, écrans et règles de passation (handoff).
> Les ratios de contraste de ce document sont **calculés** (formule WCAG 2.x). À re-vérifier dans l'outil de design à chaque évolution de couleur.

---

## 1. Principes et stratégie multi-plateforme

| Principe | Traduction concrète |
|---|---|
| **Cuisine = environnement hostile** | Cibles ≥ 44 pt (iOS) / 48 dp (Android) ; **≥ 64** en mode cuisine ; texte étape ≥ 24 pt ; tolérance aux doigts mouillés |
| **Contenu d'abord** | Photo/vidéo en pleine largeur ; chrome d'interface discret |
| **Natif par plateforme, identique par jeton** | Mêmes **tokens** partout ; composants **adaptatifs** (Cupertino/iOS, Material 3/Android, web responsive) |
| **Confiance visible** | Badges de vérification A/B/C, bandeaux de substitution explicites |
| **Accessibilité par défaut** | WCAG 2.2 AA minimum ; Dynamic Type jusqu'à 200 % ; VoiceOver/TalkBack complets |
| **Sobriété** | Peu d'animations, vidéos adaptatives, pas d'effets gratuits |

### 1.1 Règle « adaptatif »
| Élément | iOS / iPadOS / macOS | Android / ChromeOS | Web |
|---|---|---|---|
| Navigation principale | Barre d'onglets ; **barre latérale** sur iPad/Mac | Barre de navigation M3 ; rail sur tablette | Barre latérale ≥ 1024 px, onglets en bas < 768 px |
| Feuilles modales | Sheets avec « detents » | Bottom sheets M3 | Panneau latéral ou modale |
| Interrupteurs, sélecteurs | Contrôles natifs iOS | Contrôles M3 | Contrôles natifs HTML stylés |
| Retour | Geste de bord + bouton | Retour système | Navigateur |
| Icônes | **SF Symbols** + icônes ATLAS sur-mesure | Material Symbols + icônes ATLAS | SVG ATLAS |
| Typographie | Police titre ATLAS + **SF Pro** (corps) | Police titre ATLAS + Roboto/Inter | Police titre ATLAS + Inter/système |

---

## 2. Palette : corrections après calcul des contrastes

### 2.1 ⚠️ Constat sur la palette du Tome 1
Le Tome 1 (§16.2) proposait Terracotta `#C8553D`, Olive `#6B7A3A`, Safran `#E8A33D` sur Crème `#FBF6EC`. Les calculs donnent :

| Couple (texte sur fond) | Ratio | Verdict AA texte normal (4,5) |
|---|---|---|
| Charbon `#1F1B16` / Crème | **15,89** | ✅ |
| Terracotta `#C8553D` / Crème | **4,04** | ❌ (utilisable en **grand texte ≥ 24 px** ou **graphique non textuel ≥ 3:1**) |
| Olive `#6B7A3A` / Crème | **4,36** | ❌ de peu (grand texte / icônes) |
| Safran `#E8A33D` / Crème | **2,00** | ❌ **décoratif uniquement** |
| Ardoise `#3D5A6C` / Crème | 6,78 | ✅ |
| Blanc / Terracotta `#C8553D` | 4,35 | ❌ pour du texte de bouton normal |

### 2.2 Palette corrigée (mode clair)

| Rôle | Jeton | Valeur | Usage | Contraste |
|---|---|---|---|---|
| Fond | `color.bg.base` | `#FBF6EC` | Fond d'écran | : |
| Surface | `color.bg.surface` | `#FFFFFF` | Cartes | : |
| Surface alt. | `color.bg.alt` | `#F3EBDD` | Zones de regroupement | : |
| Texte principal | `color.text.primary` | `#1F1B16` | Corps, titres | 15,89 sur base |
| Texte secondaire | `color.text.secondary` | `#5A5348` | Métadonnées | 7,05 sur base ; 6,41 sur alt. |
| **Action primaire (fond)** | `color.action.primary` | **`#A8412C`** | Boutons principaux | **6,07** avec texte blanc |
| Action primaire (texte/lien) | `color.action.link` | `#A8412C` | Liens | 5,64 sur base ; 5,13 sur alt. |
| Terracotta décor | `color.brand.terracotta` | `#C8553D` | Illustrations, grands titres ≥ 24 px, icônes (≥ 3:1) | 4,04 |
| **Olive (texte)** | `color.accent.olive.text` | **`#4F5C28`** | Textes verts, badges | 6,74 sur base ; 6,13 sur alt. |
| Olive décor | `color.brand.olive` | `#6B7A3A` | Icônes, fonds, graphiques | 4,36 |
| Safran | `color.brand.saffron` | `#E8A33D` | **Fonds** (texte charbon dessus : 7,94) ; jamais texte sur crème | 2,00 |
| Ardoise | `color.accent.slate` | `#3D5A6C` | Focus, info | 6,78 |
| Bordure UI | `color.border.default` | `#8C8478` | Champs, séparateurs interactifs | 3,43 sur base ; 3,69 sur blanc (≥ 3:1) ✅ |
| Succès | `color.status.success` | `#2E7D4F` | Texte/icône | 4,68 |
| Alerte | `color.status.danger` | `#B3261E` | Erreurs, allergènes | 6,07 |
| Avertissement | `color.status.warning` | `#8A5A00` | Alertes douces | 5,50 |

### 2.3 Palette mode sombre

| Rôle | Jeton | Valeur | Contraste |
|---|---|---|---|
| Fond | `color.bg.base` | `#17140F` | : |
| Surface | `color.bg.surface` | `#221E18` | : |
| Texte principal | `color.text.primary` | `#F3EBDD` | 15,51 sur fond ; 14,00 sur surface |
| Texte secondaire | `color.text.secondary` | `#B5AC9D` | 8,18 |
| Action primaire (fond) | `color.action.primary` | `#E58A73` + texte `#17140F` | 7,18 |
| Lien | `color.action.link` | `#E58A73` | 7,18 |
| Olive clair | `color.accent.olive.text` | `#A9BA6A` | 8,67 |
| Safran | `color.brand.saffron` | `#E8A33D` | 8,52 (texte possible en sombre) |
| Bordure UI | `color.border.default` | `#7A7266` | 3,87 sur fond ; 3,49 sur surface ✅ |
| Focus | `color.focus.ring` | `#8FB4CC` | 8,37 |
| Succès / Alerte / Avert. | | `#6FCF97` / `#F2B8B5` / `#E8B84A` | 9,66 / 10,76 / 9,96 |

### 2.4 Badges de régime et de confiance (fond + texte)

| Badge | Clair (texte sur fond) | Ratio | Sombre (texte sur fond) | Ratio |
|---|---|---|---|---|
| ✅ Vérifié / OK | `#1F5A38` / `#E3F1E7` | 6,98 | `#A7E3BF` / `#1E3A2A` | 8,49 |
| 🟡 Avertissement | `#6B4600` / `#FFF1CC` | 7,48 | `#F5D58A` / `#4A3600` | 8,12 |
| ❗ Allergène / contient | `#8C1D18` / `#FBE4E2` | 7,51 | `#F6C1BD` / `#5A1A16` | 8,33 |
| ℹ️ Info / calculé | `#2C4A5C` / `#E1ECF3` | 7,81 | `#BCD7E8` / `#22394A` | 8,00 |
| Neutre / non vérifié | `#3F3A32` / `#EDE5D6` | 9,01 | : | : |

> **Règle d'or** : un badge a **toujours** une icône **et** un libellé ; la couleur ne porte **jamais** seule le sens (daltonisme).

### 2.5 Texte sur image
Utiliser un **voile (scrim) noir ≥ 55 %** sous le texte blanc posé sur une photo : même sur fond blanc pur, le ratio obtenu est ≈ 4,7:1. Préférer un dégradé progressif et **tester sur 5 photos types** (claire, sombre, saturée).

---

## 3. Jetons (tokens)

### 3.1 Typographie

| Jeton | Taille / interligne (mobile) | Graisse | Police | Usage |
|---|---|---|---|---|
| `type.display` | 32 / 38 | 600 | Fraunces (serif) | Titre de recette plein écran |
| `type.h1` | 28 / 34 | 600 | Fraunces | Titres d'écran |
| `type.h2` | 22 / 28 | 600 | Fraunces | Sections |
| `type.h3` | 18 / 24 | 600 | Inter | Sous-sections |
| `type.body` | 16 / 24 | 400 | Inter | Texte courant |
| `type.body.strong` | 16 / 24 | 600 | Inter | Ingrédients, quantités |
| `type.label` | 14 / 20 | 500 | Inter | Boutons, onglets |
| `type.caption` | 13 / 18 | 400 | Inter | Métadonnées |
| `type.cook.step` | **28 / 38** | 500 | Inter | **Texte d'étape en mode cuisine** |
| `type.cook.timer` | **48 / 52** | 600 tabular | Inter | Compte à rebours |

- **Polices** : Fraunces et Inter sont sous licence libre (SIL OFL) 🔎 vérifier la version à embarquer. Alternative **dyslexie** : OpenDyslexic ou Atkinson Hyperlegible (libres) activable dans Réglages.
- **Chiffres tabulaires** pour minuteurs et quantités (pas de « saut » visuel).
- **Échelle tablette/desktop** : +2 pt sur body, display 40/46 ; mode cuisine tablette : step 32/44.
- **Dynamic Type / taille de police Android** : tous les styles suivent l'échelle système jusqu'à 200 % ; au-delà de 150 %, passage en **mise en page empilée** (pas de colonnes de 2 chiffres/unités).
- **Largeur de ligne** : 45-75 caractères en texte long.

### 3.2 Espacement, rayon, élévation

| Jeton | Valeurs |
|---|---|
| `space` (grille 4) | 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 |
| `radius` | 8 (chips) · 12 (boutons, champs) · 16 (cartes) · 24 (sheets) · 999 (pilules) |
| `elevation` (clair) | 0 : plat ; 1 : ombre blur 8, y 2, 8 % charbon (cartes) ; 2 : blur 24, y 8, 12 % (sheets) |
| `elevation` (sombre) | Pas d'ombre : **surface plus claire** (`bg.surface` → +4 % de luminosité) |
| `stroke` | 1 px bordures, **2 px focus**, 1,75 px icônes |
| `touch.min` | 44 pt (iOS) / 48 dp (Android) ; `touch.cook` = **64** |
| `touch.gap` | ≥ 8 entre cibles |

### 3.3 Mouvement (motion)

| Jeton | Valeur |
|---|---|
| `motion.micro` | 100-150 ms (états de bouton) |
| `motion.standard` | 200-250 ms (transitions d'écran, sheets) |
| `motion.emphasis` | 300-400 ms (changement de recette, bascule A/B) |
| `motion.ease.standard` | `cubic-bezier(0.2, 0, 0, 1)` |
| `motion.ease.decelerate` | `cubic-bezier(0, 0, 0, 1)` |
| **Mouvement réduit** | Remplacer glissements par **fondu ≤ 100 ms** ; clips vidéo : **image fixe + bouton lecture** ; pas de parallaxe ni de rebond |

### 3.4 Extrait de fichier de tokens (format Style Dictionary / Tokens Studio)

```json
{
  "color": {
    "bg":   { "base": { "light": "#FBF6EC", "dark": "#17140F" },
              "surface": { "light": "#FFFFFF", "dark": "#221E18" },
              "alt": { "light": "#F3EBDD", "dark": "#2A251D" } },
    "text": { "primary": { "light": "#1F1B16", "dark": "#F3EBDD" },
              "secondary": { "light": "#5A5348", "dark": "#B5AC9D" } },
    "action": { "primary": { "light": "#A8412C", "dark": "#E58A73" },
                "onPrimary": { "light": "#FFFFFF", "dark": "#17140F" } },
    "border": { "default": { "light": "#8C8478", "dark": "#7A7266" } },
    "focus":  { "ring": { "light": "#3D5A6C", "dark": "#8FB4CC" } },
    "status": { "success": { "light": "#2E7D4F", "dark": "#6FCF97" },
                "danger":  { "light": "#B3261E", "dark": "#F2B8B5" },
                "warning": { "light": "#8A5A00", "dark": "#E8B84A" } }
  },
  "space":  { "1": 4, "2": 8, "3": 12, "4": 16, "6": 24, "8": 32, "12": 48, "16": 64 },
  "radius": { "chip": 8, "control": 12, "card": 16, "sheet": 24, "pill": 999 },
  "touch":  { "min": 48, "cook": 64, "gap": 8 },
  "motion": { "micro": 120, "standard": 220, "emphasis": 350 }
}
```
**Pipeline** : Figma Variables → Tokens Studio → **Style Dictionary** → `atlas_tokens.dart` (Flutter), `AtlasTokens.swift` (extensions Apple), `AtlasTokens.kt` (Android natif/widgets), `tokens.css` (web). **Un seul source de vérité.**

---

## 4. Iconographie & pictogrammes

| Famille | Contenu | Règle |
|---|---|---|
| **Régimes** | Sans porc, sans alcool, végétarien, vegan, sans gluten, sans lactose, halal-compatible | Icône + libellé ; **jamais** de symbole religieux comme icône générique |
| **Allergènes (14)** | Pictogrammes harmonisés UE (gluten, crustacés, œufs, poisson, arachide, soja, lait, fruits à coque, céleri, moutarde, sésame, sulfites, lupin, mollusques) | Taille ≥ 24 px, libellé en infobulle **et** lisible par lecteur d'écran |
| **Niveaux de confiance** | A ✅ Vérifié · B 🟡 Calculé · C ⚪ Non vérifié | Forme distincte (coche, engrenage, point d'interrogation) |
| **Difficulté** | 1 à 3 toques de chef | Pas de couleur seule |
| **Équipement** | Four, plaques, cocotte, robot, Airfryer… | Set cohérent trait 1,75 px |
| **Zéro déchet** | Feuille/cercle « boucle » | Ton positif, jamais culpabilisant |
| **Régions** | Illustrations d'ingrédients emblématiques (pas de drapeaux comme icônes de cuisine) | Évite l'assimilation cuisine = État ; sensibilité culturelle (Tome 6 §6) |

---

## 5. Catalogue de composants

> Pour chaque composant : **anatomie**, **états** (default · pressed · focus · disabled · loading · error), **accessibilité**.

### 5.1 Boutons
| Variante | Spécification |
|---|---|
| **Primaire** | Fond `action.primary`, texte `onPrimary`, hauteur 48 (cuisine : 64), rayon 12, libellé 14/20 medium |
| **Secondaire** | Contour 1,5 px `action.primary`, fond transparent |
| **Tertiaire (texte)** | Texte `action.link`, cible 48 mini |
| **Danger** | Fond `status.danger` (clair) ; confirmation requise |
| **Icône seule** | Cible 48 ; **label d'accessibilité obligatoire** |
- Focus : anneau 2 px `focus.ring`, offset 2 ; **visible** au clavier et au Switch Control.
- Loading : spinner + libellé « En cours… » (annoncé par le lecteur d'écran).

### 5.2 Carte recette
```
┌───────────────────────────────┐
│ [photo 4:5 ou 16:9]        ♡  │  ← favori (cible 48)
│                               │
├───────────────────────────────┤
│ Tajine de poulet aux olives   │  type.h3
│ Maroc · Fès                   │  type.caption
│ ⏱ 85 min · ⭐ Facile · €€     │
│ [✅ Sans porc][✅ Sans alcool]│  badges
└───────────────────────────────┘
```
- Variantes : **compacte** (liste), **large** (carrousel), **horizontale** (tablette).
- États : normal · **hors-ligne téléchargé** (icône) · **version adaptée** (badge « Version sans porc ») · **non adaptable** (voilée + raison).
- A11y : le libellé lu = « Tajine de poulet aux olives, Maroc, 85 minutes, facile, sans porc vérifié ».

### 5.3 Bandeau de substitution (A/B)
```
┌──────────────────────────────────────────────┐
│ 🐖 Cette recette contient du porc (lardons).  │
│ [ Version d'origine ]  [● Version sans porc ] │  ← contrôle segmenté
│ ✅ Règle validée · goût préservé (4,2/5)       │
│ Remplacé : lardons → dinde fumée + paprika     │
└──────────────────────────────────────────────┘
```
- États : **règle validée** (vert) · **à tester** (jaune, **pas** de mention « goût préservé ») · **non adaptable** (rouge, alternatives proposées).
- Le changement **réécrit** les listes d'ingrédients/étapes avec une **transition douce** (`motion.emphasis`) ; focus conservé.
- A11y : annonce « Version sans porc activée, 3 ingrédients modifiés ».

### 5.4 Badge de régime / confiance
Pilule 28 px de haut, icône 16 px + libellé 13/18 ; **tap = explication** (feuille d'info : « Calculé automatiquement. Vérifie les étiquettes. »).

### 5.5 Sélecteur de portions et d'unités
Stepper `− 4 +` (cibles 48) + **segmenté** Métrique | Cups ; changement des quantités avec **mise à l'échelle non linéaire** (Tome 1 §15.3) ; texte « sel, levure, temps ajustés » affiché quand pertinent.

### 5.5b Liste d'ingrédients
Ligne = case à cocher (48) + quantité (strong) + nom + préparation ; **dérivés/allergènes** signalés par pastille ; swipe → **substituer** ; appui long → **fiche ingrédient** (anatomie zéro déchet, Tome 3).

### 5.6 Étape de recette
`[n°]` + texte (body ; en cuisine : `type.cook.step`) + **clip en boucle** (5-15 s) + **minuteur inline** (durée soulignée, cible 48) + **bouton « critique »** (⚠️ pour étapes sensibles).
- Les **durées** et **températures** sont des **liens actionnables** : « 4 min » → lance un minuteur ; « 180 °C (th. 6) » → rappel préchauffage.

### 5.7 Minuteur
Cartes empilées : nom, compte à rebours `type.cook.timer`, **− 1 min / + 1 min**, pause, stop. **Couleur + icône + texte + vibration** à l'échéance. Max 6 minuteurs visibles ; au-delà : liste.

### 5.8 Lecteur audio
Barre persistante : play/pause (64), précédent/suivant étape (56), vitesse (0,75 / 1 / 1,25 / 1,5), **mode** (continu / pas à pas / résumé), minuteur de sommeil non requis. Écran verrouillé : métadonnées « Étape 3/8 : Faire revenir l'oignon ».

### 5.9 Lecteur vidéo
- **Clip d'étape** : boucle muette par défaut, **sous-titres actifs**, poster en cas de mouvement réduit.
- **Vidéo complète** : chapitres = étapes (appui sur une étape → saut), contrôle de vitesse, **plein écran**, **AirPlay/Cast**, sous-titres FR, **audio-description** (P1).
- **Mode économie de données** : qualité plafonnée ; autoplay désactivé en cellulaire.

### 5.10 Champ de recherche & chips d'ingrédients
Champ 48, loupe, micro 🎤, scan ▦ ; suggestions groupées (plats · ingrédients · régions · techniques) ; **chips** supprimables (cible 44) ; **hypothèse de placard** repliable.

### 5.11 Carte de région & carte du monde
Carte (SVG vectoriel) + **liste équivalente** ; zones tactiles ≥ 44 pt (agrandies pour petits pays) ; zoom pincement + boutons ± ; **contraste des contours** ≥ 3:1 ; sélection = bordure 2 px + libellé.

### 5.12 Cartes d'import
`[plateforme] @auteur · statut` (File d'attente · Analyse · À vérifier · Prête) ; champs incertains **surlignés** avec icône « ? » ; bouton **Valider** disponible seulement quand aucun champ obligatoire n'est vide.

### 5.13 Feuilles (bottom sheets) & dialogues
- **Verrou d'âge alcool** : dialogue obligatoire, **pas de pré-sélection**, texte clair, bouton secondaire « Plutôt sans alcool ».
- **Données sensibles** (régimes/allergies) : feuille de consentement **séparée**, explication courte, **révocable**.
- **Suppression** : double confirmation, rappel de l'export des données.

### 5.14 États vides, chargement, erreur, hors-ligne

| État | Règle |
|---|---|
| **Chargement** | **Skeleton** aux dimensions finales (pas de spinner plein écran) ; vidéo : poster net, pas de flash |
| **Vide** | Illustration légère + **une action claire** (« Importer ma première recette ») |
| **Erreur réseau** | Message humain + **réessayer** ; contenu en cache **toujours** affiché |
| **Hors-ligne** | Bandeau discret « Hors-ligne » ; fonctions disponibles listées ; recettes non téléchargées grisées avec « Télécharger au prochain Wi-Fi » |
| **Erreur de données diététiques** | **Ne jamais** afficher un badge si le calcul a échoué : afficher « Régime non vérifié » |

### 5.15 Toasts & notifications
Toast 4 s (8 s s'il y a une action) ; **ne jamais** déplacer le focus ; notifications de minuteur : **priorité haute**, son discret, action « +1 min » / « Arrêter ».

---

## 6. Grilles, points de rupture et mises en page

| Classe | Largeur | Colonnes | Marges | Navigation | Mise en page type |
|---|---|---|---|---|---|
| **Compact** | < 600 | 4 | 16 | Barre d'onglets | 1 volet |
| **Medium** | 600-839 | 8 | 24 | Rail latéral | 1 ou 2 volets |
| **Expanded** | 840-1199 | 12 | 24 | Barre latérale | **2 volets** (liste + détail) |
| **Large** | ≥ 1200 | 12 | 32 (max 1440) | Barre latérale | **3 volets** (navigation + liste + détail) |

- **iPad** : Split View, Slide Over et Stage Manager supportés ; **aucun** verrouillage d'orientation sauf mode cuisine (au choix).
- **Mode cuisine tablette (paysage)** : 2 volets : **clip vidéo / photo (55 %)** + **étape et ingrédients (45 %)**.
- **Zones de sécurité** : respecter *safe areas* (encoche, Dynamic Island, barre d'accueil), **marge latérale** supplémentaire en paysage.

---

## 7. Spécifications des écrans (P0)

> Pour chaque écran : **objectif**, **composants**, **états**, **notes d'accessibilité**.

### 7.1 Onboarding & profil de foyer
- **Objectif** : paramétrer foyer, équipement, régimes sans friction ; **passable**.
- **Étapes** : (1) Bienvenue (valeur en 1 phrase) → (2) Qui mange ? (membres, âges) → (3) Régimes & allergies (consentement distinct) → (4) Équipement → (5) Niveau & temps → (6) Notifications (anti-gaspi) en contexte, **jamais** à froid.
- **États** : reprise possible (« Continuer plus tard ») ; **modifiable** depuis Profil.
- **A11y** : un champ = une question par écran, progression annoncée « Étape 2 sur 5 ».

### 7.2 Accueil
- Blocs : **Reprendre** (recette/menu en cours) · **À consommer d'abord** (frigo) · **De saison** · **Fêtes à venir** (compte à rebours) · **Idées du jour** (selon profil) · **Techniques à apprendre**.
- **Pas de contenu qui contredit le profil** (aucune suggestion avec porc pour un foyer sans porc).

### 7.3 Explorer : Atlas
- Vue carte / liste ; **fil d'Ariane** (Monde › Maghreb › Maroc › Fès) ; fiche culturelle repliable ; **Menu découverte** ; **Épicerie de la région**.
- États : région sans contenu → « Bientôt » + **alerte** (abonnement newsletter / notifications).

### 7.4 Recherche & résultats
- **Trois onglets** : Nom · Région · Ingrédients ; **filtres** en feuille (régime du foyer pré-appliqué, temps, difficulté, équipement, enfants, budget).
- **Tri** : pertinence · temps · difficulté · anti-gaspi · saison.
- **Résultat vide** : « Aucune recette avec tous ces ingrédients. Il manque 1 ingrédient pour 7 recettes. » + action.

### 7.5 Recherche par ingrédients (wireframe : Tome 1 §16.4)
- Saisie (texte, voix, scan) ; chips ; **hypothèse de placard** ; trois sections (✅ Tu as tout · 🟡 Il manque 1-2 · 🔵 Idées) ; **bascule « Je veux tout utiliser »**.
- Chaque carte affiche **ce qui manque** et **le substitut** éventuel ; **ajout direct à la liste de courses**.

### 7.6 Fiche recette (wireframe : Tome 1 §8.1)
- **Ordre de lecture** (VoiceOver) : titre → badges (régimes, allergènes, confiance) → actions → équipement → ingrédients → étapes → variantes → zéro déchet → accords.
- **Bandeau de substitution** (5.3) affiché **au-dessus** des ingrédients si un filtre est actif.
- **Sticky bar** (bas) : **Cuisiner ▶** · **Écouter 🔊** · **Courses 🛒**.

### 7.7 Mode cuisine
```
┌──────────────────────────────────────────────┐
│ ✕  Tajine de poulet          Étape 3/8   🔊 │
├──────────────────────────────────────────────┤
│          [ clip vidéo en boucle ]            │
├──────────────────────────────────────────────┤
│ Ajoute l'oignon émincé et fais revenir       │
│ 4 minutes jusqu'à ce qu'il soit translucide. │
│ [ ⏱ 4:00  Lancer ]                           │
├──────────────────────────────────────────────┤
│ ◀ Précédent               Suivant ▶          │  ← 64 de haut
│ 🧅 Ingrédients  ⇄ Substituer  ⏱ 2 minuteurs  │
└──────────────────────────────────────────────┘
```
- **Écran allumé** ; **verrou tactile** temporaire (nettoyage).
- **Commandes vocales** : « suivant », « répète », « précédent », « minuteur 4 minutes », « combien de farine ? ».
- **Sortie** : confirmation si minuteurs actifs ; **bilan** (« Ça a marché ? » 👍/👎 + motif).
- **A11y** : **toutes** les infos de l'étape disponibles par audio ; **gestes alternatifs** aux swipes.

### 7.8 Substitution rapide (feuille)
Liste des ingrédients de l'étape avec **« Remplacer »** : propose les **substituts validés** (ratio, ajustement) ; mention « à tester » si besoin.

### 7.9 Lecteur audio plein écran
Visuel : titre, étape courante (texte grand), **barre de progression par étapes**, commandes 64, **vitesse**, **mode**. Fonctionne **écran éteint**.

### 7.10 Frigo virtuel
- Zones (frigo/congélateur/placard) en onglets ; lignes avec **code couleur + icône + texte** (« J-1 », « Périmé »).
- Actions : **Ajouter** (voix, scan, saisie), **Cuisiner avec ça**, **Congeler**, **Jeter** (compte pour le bilan sans culpabiliser).
- **Alerte** : « 3 produits à consommer d'ici demain ».

### 7.11 Liste de courses & planning
- Regroupement par **rayon** ; **fusion** de doublons ; quantités **optimisées** au format du commerce ; partage famille ; export Rappels/Notes.
- Planning : semaine en cartes, **glisser-déposer** (+ alternative par menu contextuel), **score zéro déchet** de la semaine.

### 7.12 Composeur de menu (à partir d'un plat)
```
┌──────────────────────────────────────────────┐
│ Menu autour de : Tajine de poulet 🍽         │
│ Convives : 6   Régimes : sans porc ✓         │
├──────────────────────────────────────────────┤
│ [ Classique ] [ Léger ] [ Audacieux ]        │
│ ENTRÉE   Zaalouk & pain maison     [↻]       │
│ PLAT     Tajine de poulet…         (pivot)   │
│ DESSERT  Oranges à la cannelle     [↻]       │
│ BOISSONS  Sans alcool: thé menthe · jus…     │
│          (Avec alcool : après vérif. d'âge)  │
├──────────────────────────────────────────────┤
│ Score : Équilibre 8/10 · Zéro déchet 7/10    │
│ Temps actif total : 1 h 20                   │
│ [ Adopter ce menu → planning + courses ]     │
└──────────────────────────────────────────────┘
```
- **↻** remplace un plat en conservant les contraintes ; **explication du score** en un tap.
- **A11y** : chaque ligne = bouton avec nom et action (« Changer l'entrée »).

### 7.13 Mes imports (file + revue)
- Liste par statut ; **revue** : champs surlignés, **éditer en ligne**, **voir la source**, **valider**.
- États : **hors-ligne** (en attente) · **quota atteint** (message clair + offre).
- **Crédit** auteur toujours visible.

### 7.14 Sauce Builder (P1)
Étapes : base → profil → aromates → **résultat** (ingrédients, proportions, conservation, **alertes œuf cru**) ; curseurs avec **alternative à saisie numérique** (accessibilité).

### 7.15 Techniques
Liste par famille + **recherche** ; fiche : vidéo 30-120 s, pas à pas, **erreurs courantes**, recettes liées ; **parcours** (P1).

### 7.16 Mode enfant
Navigation simplifiée (grands boutons, icônes + mots), **aucune pub**, aucun lien externe, **sortie par code parent** ; consignes de supervision visibles ; palette plus chaude, **mêmes** contraintes d'accessibilité.

### 7.17 Profil & réglages
Foyer · Régimes (niveau **Standard/Strict**) · Équipement · Unités · **Voix et audio** · Vidéo & données · Notifications · Langue · Accessibilité (police dyslexie, contrastes) · Compte · **Export / suppression des données** · À propos (version du référentiel).

---

## 8. Mouvement et haptique

| Événement | Mouvement | Haptique |
|---|---|---|
| Changement d'étape | Glissement 220 ms ; fondu si mouvement réduit | iOS : impact léger ; Android : `CLOCK_TICK` |
| Minuteur terminé | Pulsation + changement d'icône | **Notification success** (iOS) ; vibration longue (Android) |
| Bascule version sans porc | Fondu enchaîné 350 ms des lignes modifiées (surlignage 1 s) | Impact léger |
| Ajout au frigo / courses | Micro-animation 150 ms | Aucune |
| Erreur | Secousse **désactivée** si mouvement réduit | Notification error |

---

## 9. Accessibilité : annotations par composant

| Composant | Libellé lu (exemple) | Ordre / focus | Remarques |
|---|---|---|---|
| Carte recette | « Tajine de poulet aux olives, Maroc, 85 minutes, facile, sans porc vérifié. Bouton ajouter aux favoris » | Carte → favori | Un seul arrêt si possible ; action secondaire via actions personnalisées |
| Badge de régime | « Sans porc, vérifié par l'équipe » | Dans l'ordre visuel | Tap = explication |
| Étape | « Étape 3 sur 8. Ajoute l'oignon… Minuteur de 4 minutes, bouton » | Texte → minuteur → vidéo | La vidéo a une **description** |
| Minuteur | « Minuteur pâtes, 8 minutes 30 restantes, en cours » | : | Annonce à intervalles discrets (**pas chaque seconde**) |
| Substitution | « Version sans porc activée, 3 ingrédients modifiés » | Focus reste sur le contrôle | Région `aria-live` / annonce |
| Carte du monde | « Carte des régions, 12 macro-régions. Bascule vers liste » | : | **Liste équivalente** |

**Checklist transverse** :
- [ ] Contrastes ≥ 4,5:1 (texte), ≥ 3:1 (composants/graphismes)
- [ ] Cibles ≥ 44/48 (64 en cuisine), espacement ≥ 8
- [ ] **Dynamic Type 200 %** sans perte d'information
- [ ] VoiceOver/TalkBack : tous les contrôles ont nom, rôle, état
- [ ] Clavier / Switch Control : **ordre logique**, **focus visible**, pas de piège
- [ ] **Mouvement réduit** respecté ; pas de clignotement > 3 Hz
- [ ] **Sous-titres** sur toutes les vidéos ; transcription disponible
- [ ] **Aucune info par la couleur seule**
- [ ] Gestes complexes **avec alternative**
- [ ] Erreurs **décrites** (pas seulement colorées) et **corrigibles**

---

## 10. Surfaces Apple et Android spécifiques

### 10.1 Live Activity / Dynamic Island (minuteur)
- **Compact** : icône casserole + temps restant (à droite).
- **Étendu** : nom du minuteur · compte à rebours · boutons « +1 min » / « Arrêter » · nom de la recette.
- **Écran verrouillé** : même contenu en bandeau.
- 🔎 Limites de durée et de mise à jour imposées par l'OS : à vérifier et à documenter (repli : notification locale).

### 10.2 Widgets
| Taille | Contenu |
|---|---|
| Petit | Prochain minuteur **ou** « À consommer d'abord » (3 produits) |
| Moyen | Recette du jour (photo, titre, temps) ou liste de courses (5 lignes) |
| Grand (iPad/Android) | Planning de la semaine |
| Écran verrouillé | Minuteur ; nombre de produits à consommer |

### 10.3 Apple Watch / Wear OS
1. **Minuteurs** (liste + grand compte à rebours) · 2. **Étape courante** (texte court, 2 lignes max, suivant/précédent) · 3. **Liste de courses** (cochable) · haptique à l'échéance. **Aucune** vidéo.

### 10.4 macOS / web
Menu « Recette » (raccourcis : ⌘F recherche, ⌘P imprimer, ⌘+/− taille texte) ; **feuille imprimée** propre (ingrédients + étapes, sans navigation, **QR** vers la version vidéo).

### 10.5 Siri / Raccourcis (App Intents)
« Lance un minuteur de 8 minutes » · « Ouvre la recette en cours » · « Ajoute des œufs à ma liste de courses » · « Qu'est-ce qui périme demain ? » (lecture vocale du frigo).

---

## 11. Microcopie (extraits FR)

| Clé | Texte |
|---|---|
| `diet.pork.contains` | « Cette recette contient du porc. Voir la version sans porc ? » |
| `diet.substitute.validated` | « Règle validée : le goût est préservé (note moyenne 4,2/5). » |
| `diet.substitute.draft` | « Substitution à tester : le goût peut différer. » |
| `diet.not_adaptable` | « Cette recette ne peut pas être adaptée sans la dénaturer. Voici 3 idées proches. » |
| `diet.unverified` | « Régime non vérifié : lis les étiquettes de tes produits. » |
| `alcohol.cooking_note` | « La cuisson ne fait pas disparaître tout l'alcool. » |
| `alcohol.age_gate` | « Pour voir les accords avec alcool, confirme que tu as 18 ans ou plus. L'abus d'alcool est dangereux pour la santé. » |
| `egg.raw_warning` | « Cette sauce contient de l'œuf cru. Version sans œuf disponible. » |
| `kids.honey` | « Pas de miel avant 12 mois. » |
| `import.review` | « Vérifie les champs en jaune avant d'enregistrer. » |
| `import.credit` | « Recette importée de @{auteur}. La vidéo reste chez son créateur. » |
| `empty.fridge` | « Ton frigo est vide ici. Ajoute ce que tu as, je te propose des idées. » |
| `offline` | « Hors-ligne : tes recettes téléchargées restent disponibles. » |
| `zero_waste.leftover` | « Il te reste 3 blancs d'œufs : meringues ou financiers ? » |

**Ton** : chaleureux, direct, jamais moralisateur ; **verbes d'action** ; **pas d'humour** sur religions/régimes ; **pas de jargon** sans explication.

---

## 12. Passation (handoff) et qualité du design system

### 12.1 Structure Figma
`00 Cover · 01 Foundations (couleurs, type, espace, icônes) · 02 Components (avec variantes/états) · 03 Patterns (recherche, substitution, import) · 04 Screens (mobile/tablette/desktop) · 05 Prototypes · 06 Accessibility annotations · 07 Archive`.
- **Variables Figma** : modes **Light / Dark** et densité **Normal / Cuisine**.
- **Nommage** : `Component/Variant/State` ; jetons `color.text.primary`.

### 12.2 Documentation vivante
**Widgetbook** (Flutter) et **Storybook** (web) alimentés par les **mêmes jetons** ; chaque composant documente : usage, interdits, états, accessibilité, exemples de contenu **réel** (pas de lorem ipsum : titres longs, noms arabes/chinois, allergènes multiples).

### 12.3 Tests visuels
- **Tests golden** Flutter (clair/sombre ; échelle de texte 100 %, 150 %, 200 % ; paysage).
- **Régression visuelle** web (captures par point de rupture).
- **Jeu de contenus stress** : titre de 80 caractères, 25 ingrédients, nom en arabe (RTL), quantité 1/2, 12 badges.

### 12.4 Définition de « Done » design
- [ ] Composant avec **tous les états** + **clair/sombre** + **Dynamic Type 200 %**
- [ ] Annotation d'accessibilité complète
- [ ] Contraste **vérifié** (outil + calcul)
- [ ] Jetons exclusivement (aucune valeur brute)
- [ ] **RTL** testé
- [ ] Contenu **réel** testé
- [ ] Validé par un(e) **utilisateur(trice) malvoyant(e)** pour les parcours critiques

### 12.5 Gouvernance
Un(e) **propriétaire du design system** ; revue **bimensuelle** ; versionnage sémantique des jetons ; **changelog** ; **aucune** couleur ajoutée sans calcul de contraste.
