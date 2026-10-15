# ATLAS : cuisines du monde, faites maison

**Application en ligne : https://fadhelis01-boop.github.io/atlas-cuisine/** · **Installer sur iPhone, Android, PC, Mac : [INSTALLER.md](INSTALLER.md)**

**576 recettes** du monde classées par région (+ food fusion), dont pâtisserie française, chocolats d'occasion, condiments et marinades maison (bouillon cube, nokoss…), sauces à frites, recherche par nom ou avec les ingrédients qu'on a, profils sans porc / sans alcool / allergies / végétarien avec versions adaptées, recettes pour enfants, lecture audio et mode cuisine (minuteurs, commandes vocales), **69 fiches techniques** (gestes du chef, du pâtissier, du boulanger et du chocolatier, cuissons des viandes, poissons et œufs avec tableaux de températures), pains et pâtes, sauces maison sans additifs, fêtes et composeur de menu avec boissons, **zéro déchet ingrédient par ingrédient**, import de recettes TikTok et autres avec tri automatique, vidéos lisibles dans l'application, photos sous licence libre. Fonctionne hors connexion.

| Dossier | Contenu |
|---|---|
| `bible/` | La bible du projet (index + Tomes 1 à 8, 11, 12, 13), le moteur de référence Python, les fiches recettes (`recipes_data.py`, `recipes_v1_*.py`, vague 2 : `recipes_v2_*.py` au format compact de `recipes_v2_base.py`), la table zéro déchet (`zero_dechet_data.py`) et les générateurs (`export_app_data.py`, `build_tome12.py`, `build_tome13.py`). |
| `app/` | L'application ATLAS (PWA React + TypeScript + Vite). |
| `recettes-classees/` | Recettes TikTok (favoris, @lacuisinedemarina, @niangcook) et du site Cooking with Morgane, classées dans les catégories de la bible (liens crédités, aucune vidéo copiée). |
| `illustrations/` | Chaîne des photos : collecte sous licence libre, choix relus un à un (`selections.json`), recadrage, étalonnage, WebP. |

## Développement

```bash
cd app && npm install
npm run dev        # http://localhost:5196
npm run build      # 41 tests du moteur + typage + version de production (dist/)
npm run deploy     # publication sur GitHub Pages (branche gh-pages)
```

Ajouter une recette : l'écrire dans `bible/recipes_v1_*.py` (format du Tome 11 ; chaque ingrédient = nom exact du Tome 3), puis `cd bible && python export_app_data.py` (vérifie les références et régénère les données), puis `python build_tome12.py` et `python build_tome13.py`. Vague 2 : une ligne `K(...)` dans un fichier `bible/recipes_v2_*.py` (voir l'en-tête de `recipes_v2_base.py`).

Ajouter ou changer une photo : `illustrations/` → `fetch_candidates.py` (planches contact), choix dans `selections.json`, `process.py` (avec le Python du venv AUTOMATIC1111, qui a Pillow).

## État et limites

Recettes rédigées mais **non testées en cuisine** ; substitutions **à tester** ; référentiel d'ingrédients en confiance C ; durées de conservation des restes à valider. Photos d'illustration sous licence libre (crédits dans l'application, page « Crédits photos ») ; le plat présenté peut différer de la recette. Détails : `bible/00_INDEX_BIBLE_ATLAS.md` et Tome 12.

## Crédits

Photos : auteur·e·s de Wikimedia Commons et Flickr, licences CC0, domaine public, CC BY, CC BY-SA (voir l'application). Vidéos : leurs auteur·e·s sur TikTok et YouTube, lues par les intégrations officielles.
