# Audit « chef cuisinier professionnel senior » de toute l'application (21/11/2026)

Relecture de métier à l'échelle de toute l'application (pas une seule rubrique), après les audits chef du 12/11
(cuisson à cœur, repos, four, échelle, froid), fin gourmet du 12/11 (classiques régionaux, accords), chef+famille du
10/11 (sécurité familiale) et les deux coins corrigés aujourd'hui (Marinades, Sauces). Le vocabulaire technique
classique (découpe, liaison, pâtisserie, filetage du poisson, points de cuisson) s'est révélé **déjà très
complet** — voir §2 — donc cet audit porte sur ce qui reste vraiment non couvert : discipline d'hygiène, mise en
place/coordination, et deux tests de cuisson manquants. Rien n'a été corrigé : ce document liste les angles morts,
par ordre de gravité.

## 1. Constats mesurés

| # | Angle | Mesure | Gravité |
|---|---|---|---|
| 1 | **Aucune mention de l'hygiène croisée viande crue / élément prêt à manger, dans toute l'application** | Recherche sur tout `src/lib/` : zéro occurrence de « planche séparée », « lave-mains » ou « contamination ». 314 fiches utilisent de la volaille crue comme ingrédient ; 36 d'entre elles manipulent en plus une herbe fraîche ajoutée crue en fin de recette (persil, coriandre, ciboulette…) dans la même préparation — exactement le scénario où une planche ou des mains contaminées par le poulet cru touchent ensuite un élément qui ne sera plus cuit. | **forte** |
| 2 | **La coordination de plusieurs éléments d'un même plat n'est presque jamais explicite** | 990 fiches ont 4 étapes ou plus (plat avec accompagnement, sauce à part, etc.). Seules 6 disent explicitement de mener deux choses en parallèle (« pendant que… », « en même temps »). Un cuisinier qui suit les étapes dans l'ordre écrit, sans réflexe de métier, cuit son riz et sa sauce l'un après l'autre plutôt qu'en parallèle, et sert un plat avec un élément froid. | moyenne |
| 3 | **Le repère « goûte et rectifie » couvre le sel, l'acide et le sucre, jamais le gras** | Le texte affiché sur toute fiche salée (`dressage.ts`, fonction `finishFor`) propose 4 corrections : sel (manque de relief), acide (lourd ou plat), sucre (trop acide), eau/crème/pomme de terre (trop salé) — mais rien pour un plat qui a cuit à sec ou dont la sauce a réduit trop fort : la correction professionnelle (« un filet d'huile, une noix de beurre, une cuillère de crème ») n'existe pas, alors que c'est l'un des 4 grands leviers de goût enseignés avec le sel/sucre/acide. | moyenne |
| 4 | **Les braisés et mijotés n'ont presque jamais de test de cuisson textural, seulement une durée** | 54 plats repérés comme braisés/mijotés (titre ou nature du plat) ; seuls 11 décrivent un signal de cuisson indépendant du minuteur (la fourchette s'enfonce sans résistance, la viande s'effiloche). Les 43 autres ne donnent qu'un temps fixe — risqué pour un mijoté, dont la cuisson réelle varie avec la pièce, la cocotte et le feu, à l'inverse d'une grillade où le test au doigt existe déjà (`techniques2.ts`). | moyenne |

## 2. Ce qui est déjà solide (vérifié, pas un point à corriger)

Avant d'écrire ce document, le vocabulaire et les techniques suivants ont été recherchés dans `glossaire.ts`
(111 termes) et `techniques.ts`/`techniques2.ts`/`techniques3.ts` (1 270 lignes) pour éviter de signaler comme
manquant ce qui existe déjà :
- **Découpe** : julienne, brunoise/mirepoix, chiffonnade, émincer, ciseler, escaloper, parer — tous présents et
  reliés aux étapes qui les emploient.
- **Liaison et sauces** : roux, singer, beurre manié, monter au beurre, réduire, émulsionner, nappe, liaison —
  tous présents.
- **Pâtisserie** : pétrir, pointage/pousse, tourage, sablage, tempérer (chocolat), mantecare — tous présents.
- **Poisson** : deux fiches techniques dédiées (« Écailler, vider et lever les filets d'un poisson rond » et
  « lever les filets d'un poisson plat »), avec matériel, gestes et erreurs fréquentes.
- **Points de cuisson de la viande** : température à cœur ET test au doigt pour bleu/saignant/à point/bien cuit
  (bœuf, agneau, veau, magret), déjà détaillés par espèce dans `techniques2.ts`.
- **Cohérence niveau/technique** : les 1 100 fiches de niveau « facile » ne font appel à aucune technique classée
  avancée (filetage, tourage, mantecare) — vérifié, aucune incohérence.

## 3. Pourquoi ce sont des angles morts

Le constat n°1 est le plus sérieux parce qu'il touche un réflexe de sécurité enseigné en premier dans n'importe
quelle cuisine professionnelle (et dans tout cours d'hygiène alimentaire grand public), alors que l'application a
déjà un volet sécurité développé pour la cuisson à cœur, le froid et les allergènes — ce volet s'arrête net avant la
contamination croisée, qui n'a pourtant rien à voir avec la température. Les constats n°2 à 4 touchent la même
chose sous un angle différent : l'application explique très bien *comment faire un geste* (pétrir, lever un filet,
déglacer) mais beaucoup moins bien *quand l'enchaîner avec un autre* ou *comment savoir que c'est prêt sans
minuteur* — deux réflexes qui distinguent un cuisinier formé d'une personne qui suit une recette à la lettre.

## 4. Pistes de correction (non appliquées)

- **#1** : ajouter un repère de sécurité générique (type `REPERES_MARINADE` du coin Marinades, ou une entrée dans
  « Conservation »/« Sécurité ») : une planche et un couteau dédiés à la volaille/viande crue, les mains lavées
  avant de toucher un élément qui ne cuira plus (herbe de finition, salade, pain). L'afficher sur les fiches qui
  combinent une protéine crue et un élément cru de finition (au moins les 36 repérées) plutôt que partout.
- **#2** : repérer dans les étapes existantes les cas à deux éléments qui doivent arriver à la même minute (riz +
  sauce, viande + légumes grillés) et ajouter une phrase de coordination (« pendant que la viande repose, finis la
  sauce ») plutôt que réécrire l'ordre des étapes.
- **#3** : ajouter une 5ᵉ branche au texte de `finishFor` : « Sec ou la sauce a trop réduit ? un filet d'huile, une
  noix de beurre ou une cuillère de crème. »
- **#4** : sur les 43 fiches de braisé/mijoté sans test textural, ajouter le repère générique « la pointe d'un
  couteau (ou une fourchette) s'enfonce sans résistance » à l'étape de cuisson, comme déjà fait pour le test au
  doigt des grillades.

## 5. Corrigé (commit 2026-11-22)

- **#1** : `dressage.ts` — nouveau champ `Finish.hygiene`, calculé dans `finishFor` : volaille crue (liste exacte de
  10 références « Viandes & volailles (hors porc) » réellement crues, sans compter fumé/séché/charcuterie) +
  herbe de finition (même détection `HERBS` que le repère vert existant) → « Planche et couteau à part pour la
  volaille crue ; lave-toi les mains avant de toucher l'herbe de finition ou tout élément qui ne cuira plus. »,
  affiché sous « Finition et dressage » (`RecipePage.tsx`) uniquement sur les fiches concernées, pas partout.
- **#2** : plutôt que réécrire 990 fiches une par une (risque de phrases mal à propos), une ligne générique ajoutée
  à « Avant de commencer » (déjà affichée sur toute fiche) dès que la fiche a 4 étapes ou plus : « Repère les
  éléments à faire arriver en même temps (féculent, sauce, légumes, viande qui repose) : rien ne doit attendre froid
  dans l'assiette. » Couvre les 990 fiches visées sans risque de contresens recette par recette.
- **#3** : 5ᵉ branche ajoutée au texte « Goûte et rectifie » de `finishFor` : « Sec, ou la sauce a trop réduit ? un
  filet d'huile, une noix de beurre ou une cuillère de crème. »
- **#4** : `bible/complements_pro.py`, nouvelle fonction `test_textural()` (même schéma que `cuisson_a_coeur`/
  `repos_viande` déjà en place) : sur les plats dont le titre correspond à la même liste de braisés/mijotés que le
  repère de dressage (tajine, curry, daube, blanquette, bourguignon, ragoût, navarin, osso buco, cassoulet,
  pot-au-feu…) et dont les étapes n'ont **aucun** repère textural (s'effiloche, se défait, à la fourchette, pointe
  du couteau), ajoute « La pointe d'un couteau (ou une fourchette) s'enfonce sans résistance : c'est prêt. » à la
  dernière étape de cuisson longue. 71 fiches complétées à l'export (liste plus large que l'estimation initiale
  de 43, car la détection par titre couvre aussi des currys et tajines non comptés dans le relevé manuel).
