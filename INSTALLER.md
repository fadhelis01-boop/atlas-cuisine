# Installer ATLAS sur ton téléphone, ta tablette ou ton ordinateur

ATLAS est une **application web installable** : on l'installe depuis le navigateur, sans passer par l'App Store ni le Play Store. Une fois installée, elle a son icône, s'ouvre en plein écran et **fonctionne sans connexion** (recettes, audio, minuteurs, frigo, courses ; photos après le premier affichage ou après « Enregistrer toutes les photos » dans le Profil).

**Adresse de l'application : https://fadhelis01-boop.github.io/atlas-cuisine/**

---

## 📱 iPhone et iPad

1. Ouvre **Safari** (pas Chrome : sur iPhone, l'installation passe par Safari).
2. Va à l'adresse ci-dessus.
3. Touche le bouton **Partager** (le carré avec une flèche vers le haut, en bas de l'écran sur iPhone, en haut à droite sur iPad).
4. Fais défiler et touche **« Sur l'écran d'accueil »**.
5. Laisse le nom « ATLAS » et touche **Ajouter** (en haut à droite).
6. L'icône ATLAS (un bol fumant) apparaît sur l'écran d'accueil : ouvre-la depuis là.

Conseils iPhone :
- **Voix plus naturelle** pour la lecture des recettes : Réglages › Accessibilité › Contenu énoncé › Voix › Français › télécharge une voix « améliorée » ou « premium ».
- **Minuteurs** : autorise les notifications quand ATLAS les demande (au premier minuteur). Limite d'iOS : une application web ne peut pas sonner quand elle est complètement fermée ; garde ATLAS ouverte pendant la cuisson (l'écran reste allumé en mode cuisine).
- **Commandes vocales** (« suivant », « répète », « minuteur 10 minutes ») : elles dépendent de Safari ; si elles ne marchent pas, utilise les gros boutons du mode cuisine.

## 🤖 Téléphone ou tablette Android

1. Ouvre **Chrome**.
2. Va à l'adresse ci-dessus.
3. Un bandeau **« Installer l'application »** peut apparaître : touche-le. Sinon, menu **⋮** (en haut à droite) › **« Installer l'application »** (ou « Ajouter à l'écran d'accueil »).
4. Confirme avec **Installer**.
5. ATLAS apparaît dans tes applications.

Bonus Android : une fois ATLAS installée, dans **TikTok** ou **Instagram**, bouton **Partager** › **ATLAS** : la recette arrive directement dans « Mes imports », triée automatiquement.

Samsung Internet : menu ☰ › **Ajouter la page à** › **Écran d'accueil**.

## 💻 Ordinateur Windows (ou Linux, ChromeOS)

1. Ouvre **Chrome** ou **Microsoft Edge**.
2. Va à l'adresse ci-dessus.
3. Clique sur l'icône **Installer** à droite de la barre d'adresse (un écran avec une flèche), ou menu **⋮** › **« Installer ATLAS »** (Edge : menu **…** › **Applications** › **Installer ce site en tant qu'application**).
4. ATLAS s'ouvre dans sa propre fenêtre ; un raccourci est créé dans le menu Démarrer (épingle-le à la barre des tâches si tu veux).

## 🍎 Mac

- **Safari** (macOS Sonoma ou plus récent) : va à l'adresse, menu **Fichier** › **« Ajouter au Dock »**.
- **Chrome** ou **Edge** : même méthode que sur Windows (icône Installer dans la barre d'adresse).

---

## Mettre à jour

Rien à faire : à chaque ouverture, ATLAS vérifie s'il existe une nouvelle version et affiche un bandeau **« Mettre à jour »**. Tu peux aussi vérifier dans **Profil › Vérifier les mises à jour**.

## Garder ses données en changeant d'appareil

Tes favoris, ton frigo, ta liste de courses, tes menus et tes imports sont enregistrés **sur l'appareil** (rien n'est envoyé sur Internet). Pour les transférer : **Profil › Exporter mes données** sur l'ancien appareil, puis **Profil › Importer une sauvegarde** sur le nouveau.

## Désinstaller

- iPhone/iPad : appui long sur l'icône › Supprimer l'app.
- Android : appui long › Désinstaller.
- Windows/Mac (Chrome, Edge) : ouvre ATLAS › menu **⋮** › **Désinstaller ATLAS**.

## En cas de souci

- **L'option « Installer » n'apparaît pas** : vérifie que tu es bien sur l'adresse en `https://` ; sur iPhone, utilise Safari.
- **Une page ne s'affiche pas hors connexion** : ouvre-la une première fois avec du réseau.
- **Les photos manquent hors connexion** : Profil › **Enregistrer toutes les photos** (≈ 10 Mo, en Wi-Fi).
- **Les vidéos TikTok ou YouTube ne se lancent pas** : elles demandent une connexion ; une vidéo supprimée ou rendue privée par son auteur·e ne se lit plus.

---

## Pour les développeurs : lancer le projet en local

```bash
git clone https://github.com/fadhelis01-boop/atlas-cuisine.git
cd atlas-cuisine/app
npm install
npm run dev        # http://localhost:5196
npm run build      # 41 tests + typage + version de production
npm run deploy     # publie dist/ sur la branche gh-pages
```
Les données viennent de la bible : `cd bible && python export_app_data.py`. Voir `README.md`.
