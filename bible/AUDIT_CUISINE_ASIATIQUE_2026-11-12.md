# Audit « cuisinier senior, cuisines d'Asie » d'ATLAS (12/11/2026)

Le regard d'un cuisinier qui a travaillé les cuisines chinoise, japonaise, coréenne, thaïe, vietnamienne et indienne. Il
cherche ce qu'un professionnel de ces cuisines remarquerait tout de suite dans l'appli. Les mesures portent sur les fiches
exportées (`app/.tmp/aud/asie.ts`), avant correction. Tout a été corrigé le jour même. Contrôle automatique : test 125.

## 1. Constats mesurés (avant)

| Angle | Mesure | Gravité |
|---|---|---|
| Faux végétariens | 4 fiches étiquetées végétariennes portaient du poisson caché : kai jeow (sauce de poisson), kimchi jjigae et tteokbokki (dashi instantané, à la bonite), curry vert au tofu (pâte de curry, souvent à la crevette) | forte (confiance, régimes) |
| Riz | 10 plats sur du riz rond ou gluant sans rinçage ; le mango sticky rice sans trempage, alors que le riz gluant non trempé reste dur | forte (résultat raté) |
| Wok | 24 sautés sans repère de wok fumant ni de petites fournées : à la maison, c'est la première cause d'un sauté qui bout au lieu de sauter | moyenne |
| Fiches techniques | rien sur le dashi, le lavage et la cuisson des riz d'Asie, le pliage des raviolis, la tadka, la pâte de curry, la cuisson des nouilles, la lacto-fermentation | forte |
| Classiques absents | Chine : xiao long bao, hong shao rou, agneau au cumin, mantou, dan tat. Japon : takoyaki, sukiyaki, yakisoba, dorayaki, agedashi. Corée : samgyetang, jajangmyeon, doenjang jjigae, hotteok. Thaïlande : panang, gai yang. Vietnam : bún bò Huế, cơm tấm, chả cá. Inde : vindaloo, khichdi, poha, idli, vada pav, pani puri, rasam, kulfi, jalebi. Malaisie et Singapour : char kway teow, kaya toast | forte |
| Pays absents | Népal, Bangladesh, Birmanie, Mongolie, Asie centrale : aucune fiche (le plov était rangé en « Asie du Sud ») | forte |
| Boissons | 5 boissons d'Asie seulement ; aucun thé de table conseillé avec les plats | moyenne |
| Accords | la plupart des plats d'Asie n'avaient ni boisson sans alcool ni accord | moyenne |
| Régions | « Chine (Sichuan) », « Inde (Goa) », « Inde (Cachemire) », « Inde (Tamil Nadu) », « Asie de l'Est » seul, Ouzbékistan en « Asie du Sud » | faible |
| Fiches techniques mal reliées | une technique « Riz à sushi » aurait été rattachée à la fiche générale du riz (premier mot trouvé) | faible |

Points vérifiés et sains :
- variantes sans alcool sur toutes les fiches au mirin, au saké ou au Shaoxing ;
- piment à part pour les enfants ;
- part végétarienne des plats d'Asie supérieure à celle du catalogue.

## 2. Corrigé

- **42 fiches nouvelles** (`recipes_v7_asie_est.py`, `recipes_v7_asie_sud.py`). Toutes ont au moins 4 étapes, avec à chaque étape son geste, son temps et son repère.
  - Chine : xiao long bao (gelée de bouillon, 18 plis), hong shao rou, agneau au cumin du Xinjiang, mantou, dan tat.
  - Japon : takoyaki, sukiyaki, yakisoba, dorayaki, agedashi tofu au kombu, nasu dengaku.
  - Corée : samgyetang, jajangmyeon, doenjang jjigae au kombu, hotteok, boricha.
  - Mongolie : buuz.
  - Inde : vindaloo de Goa, khichdi, poha, rava idli, vada pav, pani puri, rasam, kulfi, jalebi.
  - Népal : dal bhat tarkari, momos aux légumes et au paneer, thukpa.
  - Bangladesh : shorshe maach.
  - Birmanie : mohinga.
  - Ouzbékistan : lagman aux nouilles tirées.
  - Thaïlande : panang, gai yang et sauce jaew, cha yen.
  - Vietnam : cơm tấm, bún bò Huế (sans porc), chả cá Lã Vọng, cà phê sữa đá.
  - Malaisie et Singapour : char kway teow, kaya toast, teh tarik.
- **Porc et alcool** : ils restent dans la recette d'origine (hong shao rou, xiao long bao, vindaloo, jajangmyeon), avec une version sans porc et une version sans alcool. Le yakisoba et le cơm tấm sont présentés en version poulet, avec la version au porc d'origine en variante.
- **Faux végétariens corrigés** (`complements_asie.FAUX_VEG`) :
  - kai jeow au soja ;
  - kimchi jjigae et tteokbokki au kombu ;
  - curry vert : « pâte sans crevettes, lis l'étiquette ».
  - La fiche technique du dashi rappelle que le dashi instantané contient de la bonite.
- **Riz** (`complements_asie.riz`) :
  - 12 fiches reçoivent le lavage jusqu'à eau presque claire, l'égouttage et la bonne quantité d'eau ;
  - le riz gluant du mango sticky rice est trempé 4 h.
- **Wok** (`complements_asie.wok`) : 20 sautés reçoivent le repère « wok fumant, feu vif, fournées de 300 g au plus ». La fiche technique du wok décrit maintenant la préchauffe à sec et le goût grillé (wok hei).
- **7 fiches techniques d'Asie** (`app/src/lib/techniques3.ts`, famille « Cuisines d'Asie ») : dashi, riz japonais / à sushi / gluant (avec la règle du riz cuit et de *Bacillus cereus*), pliage des raviolis, tadka, pâte de curry, nouilles, lacto-fermentation. Une technique est désormais rattachée d'abord à la fiche dont le nom correspond exactement.
- **Boissons et accords** (`complements_asie.accords`) : chaque plat d'Asie a la boisson de son pays (oolong, sencha, boricha, thé glacé thaï, trà đá, lassi, thé masala, teh tarik, kok choy…). Il a aussi un accord vin ou bière, choisi selon le piment, le poisson ou la viande rouge.
- **Régions** : « Chine › Sichuan », « Inde › Goa »… ; une macro-région « Asie centrale » pour l'Ouzbékistan (plov, lagman), regroupée avec l'Asie du Sud dans les filtres.
- **Acidité** : agneau au cumin, agedashi et samgyetang reçoivent l'acidité que leur cuisine leur donne (vinaigre, citron, radis vinaigré).

## 3. Reste à faire

- ~~Les 42 nouvelles fiches n'ont pas encore de photo~~ : toutes illustrées le 12/11 (`collect_v13`, licences libres).
- Le sel noir (kala namak), le poha, le chunjang et les puris s'achètent en épicerie asiatique ou indienne. Les fiches le disent.
- Aucune recette n'est testée en cuisine. Les plus délicates sont à tester d'abord : xiao long bao, lagman (nouilles tirées), jalebi, takoyaki.

## 4. Suite du 12/11 : TikTok, photos, carte d'origine

- **Recettes asiatiques les plus vues sur TikTok** :
  - **Cooking with Morgane** (@cooking.with.morgane, autrice du livre *Cuisines d'Asie*). Ses 235 vidéos ont été relevées et triées par nombre de vues. 11 fiches nouvelles (`recipes_v7_tiktok_asie.py`) suivent les ingrédients de ses légendes, avec des étapes réécrites et la vidéo créditée :
    - poulet caramélisé (3,3 M de vues) ;
    - raviolis grillés sans pliage (1,8 M) ;
    - bœuf sauté à l'œuf ;
    - beignets de poulet sel et poivre ;
    - goong ob woon sen ;
    - galettes feuilletées au bœuf ;
    - aehobak jeon ;
    - bánh cuốn ;
    - œufs aux crevettes ;
    - mayonnaise japonaise ;
    - poulet au caramel croustillant.
    Le loc lac existait déjà (lok_lak) : sa vidéo y est rattachée.
  - **Ryuji** (@ryuji_tiktok_, cuisine de maison japonaise) : 3 fiches (tenshindon, niku daikon, poivrons farcis).
  - **Lynja** (@cookingwithlynja) : 1 fiche (tanghulu, 47,9 M de vues).
  - 41 fiches existantes reçoivent leurs vidéos (Général Tao, nems, riz cantonais, gyoza, pad thaï, karaage, kulfi…).
- **Porc** : comme toutes les fiches TikTok (test 100), elles sont faites à la volaille. Quand l'original est au porc, la fiche le signale.
- **Photos** :
  - les 42 fiches de l'audit et 12 des 15 fiches TikTok sont illustrées ;
  - une troisième recherche sur toutes les fiches encore sans photo (nom d'origine, titre, parenthèses) en ajoute 5.
  - Total : 1 316 fiches illustrées sur 1 486. Les 170 restantes n'ont aucune photo libre fidèle (homonymes : animaux, lieux, personnes).
- **Pictogramme « carte du monde »** sur chaque fiche :
  - le pays d'origine est en couleur, avec un point pour la région ou le petit territoire (Bretagne, Sichuan, Singapour, Réunion…) ;
  - une fiche sans pays (fusion, bases) montre sa grande région en safran ;
  - un toucher agrandit la carte avec son nom.
  - Données : Natural Earth 1:110m (domaine public), générées par `app/scripts/worldmap.mjs`, 40 Ko compressés chargés à l'ouverture d'une fiche seulement.
  - Correspondances : `app/src/lib/origine.ts`.
  - Toutes les régions « Pays (Région) » deviennent « Pays › Région ».
- Test 126.
