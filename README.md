# ATLAS : cuisines du monde, faites maison

**Application en ligne : https://fadhelis01-boop.github.io/atlas-cuisine/** · **Installer sur iPhone, Android, PC, Mac : [INSTALLER.md](INSTALLER.md)**

**889 recettes** du monde classées par région (+ food fusion), dont pâtisserie française, chocolats d'occasion, condiments et marinades maison (bouillon cube, nokoss…), sauces à frites, recherche par nom ou avec les ingrédients qu'on a, profils sans porc / sans alcool / allergies / végétarien avec versions adaptées, recettes pour enfants, lecture audio et mode cuisine (minuteurs, commandes vocales), **71 fiches techniques (40 avec les gestes en photos)** (gestes du chef, du pâtissier, du boulanger et du chocolatier, cuissons des viandes, poissons et œufs avec tableaux de températures), pains et pâtes, sauces maison sans additifs, fêtes et composeur de menu avec boissons, **zéro déchet ingrédient par ingrédient**, import de recettes TikTok et autres avec tri automatique, **plus de 3 000 recettes en vidéo classées** (favoris TikTok, 13 chaînes YouTube dont Le Riz Jaune, CookWithBash, Cook with Nabeela…) lisibles dans l'application, **dictionnaire illustré de 655 ingrédients**, **menu du jour de saison selon le lieu**, **planificateur de la semaine** (menus de saison, restes réutilisés le lendemain, courses regroupées, préparation à l'avance), « Propose-moi » en un geste, finition et dressage, sel dosé et repères visuels pour chaque fiche, carnet d'essais exportable, photos sous licence libre. Fonctionne hors connexion.

| Dossier | Contenu |
|---|---|
| `bible/` | La bible du projet (index + Tomes 1 à 8, 11, 12, 13), le moteur de référence Python, les fiches recettes (`recipes_data.py`, `recipes_v1_*.py`, vague 2 : `recipes_v2_*.py` au format compact de `recipes_v2_base.py`), la table zéro déchet (`zero_dechet_data.py`) et les générateurs (`export_app_data.py`, `build_tome12.py`, `build_tome13.py`). |
| `app/` | L'application ATLAS (PWA React + TypeScript + Vite). |
| `recettes-classees/` | Recettes TikTok (favoris, @lacuisinedemarina, @niangcook), chaînes YouTube (`build_youtube.py`) et site Cooking with Morgane, classées dans les catégories de la bible (liens crédités, aucune vidéo copiée). |
| `illustrations/` | Chaîne des photos : collecte sous licence libre, choix relus un à un (`selections.json`), recadrage, étalonnage, WebP. |

## Développement

```bash
cd app && npm install
npm run dev        # http://localhost:5196
npm run build      # 67 contrôles (moteur, planificateur, dressage…) + typage + version de production (dist/)
npm run deploy     # publication sur GitHub Pages (branche gh-pages)
```

Ajouter une recette : l'écrire dans `bible/recipes_v1_*.py` (format du Tome 11 ; chaque ingrédient = nom exact du Tome 3), puis `cd bible && python export_app_data.py` (vérifie les références et régénère les données), puis `python build_tome12.py` et `python build_tome13.py`. Vague 2 : une ligne `K(...)` dans un fichier `bible/recipes_v2_*.py` (voir l'en-tête de `recipes_v2_base.py`).

Ajouter une recette vue sur TikTok, YouTube ou un site, **sans coder** : coller le lien (une ligne par lien) dans `recettes-classees/a_ajouter.md`, directement sur github.com ou dans l'appli GitHub, et enregistrer. L'automatisation « Ajouter des recettes » (`.github/workflows/ajout-recettes.yml`) lit chaque lien, le classe, régénère les données, rejoue les contrôles et republie l'application (environ 2 minutes). Chaque envoi déclenche aussi « Contrôles » (`.github/workflows/controles.yml`) : tests, typage et construction.

Ajouter ou changer une photo : `illustrations/` → `fetch_candidates.py` (planches contact), choix dans `selections.json`, `process.py` (avec le Python du venv AUTOMATIC1111, qui a Pillow).

## État et limites

Recettes rédigées mais **non testées en cuisine** ; substitutions **à tester** ; référentiel d'ingrédients en confiance C ; durées de conservation des restes à valider. Photos d'illustration sous licence libre (crédits dans l'application, page « Crédits photos ») ; le plat présenté peut différer de la recette. Détails : `bible/00_INDEX_BIBLE_ATLAS.md` et Tome 12.

## Crédits

Photos : auteur·e·s de Wikimedia Commons et Flickr, licences CC0, domaine public, CC BY, CC BY-SA (voir l'application). Vidéos : leurs auteur·e·s sur TikTok et YouTube, lues par les intégrations officielles.
