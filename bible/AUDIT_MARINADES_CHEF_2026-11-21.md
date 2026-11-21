# Audit « chef cuisinier senior » du coin Marinades (21/11/2026)

Relecture de métier de la rubrique `/marinades` (`app/src/lib/marinades.ts`, `app/src/pages/Marinades.tsx`) et de ses
17 fiches, croisée avec les 1605 fiches de la bible pour mesurer ce qui existe déjà ailleurs sans être rattaché au
coin. Les 8 constats ont tous été corrigés le jour même (commit `76e7a7e`) : voir « 5. Corrigé » à la fin de ce
document.

## 1. Constats mesurés

| # | Angle | Mesure | Gravité |
|---|---|---|---|
| 1 | **La marinade au vin rouge (technique française classique) est absente du coin** | Au moins 4 fiches de la bible marinent une viande toute une nuit dans du vin rouge avec mirepoix et bouquet garni — `coq_au_vin` (17 h), `daube_provencale` (16 h), `civet_lievre`, `lievre_royale` (24 h) — un geste qu'on enseigne en premier en cuisine française. Le coin Marinades couvre yassa, tandoori, jerk, bulgogi, teriyaki, mojo, chermoula, shawarma… mais pas celle-là. | **forte** |
| 2 | **Architecture incohérente : 5 fiches ne sont plus des marinades réutilisables mais des mini-recettes figées** | `harissa_marinade_agneau`, `mojo_cubain_porc`, `porc_citronnelle_vietnamien`, `shawarma_marinade` et `crevettes_citron_vert_marinade` intègrent la pièce de viande/poisson **comme ingrédient structurant** (poids 3 : gigot d'agneau, filet mignon de porc, cuisse de poulet, gambas) et vont jusqu'à la cuisson et au dressage dans leurs étapes — exactement ce que l'en-tête du fichier dit vouloir éviter (« chacune réutilisable sur n'importe quelle pièce… pas liée à un seul plat fini »). À l'inverse, `chermoula`, `marinade_teriyaki_sauce`, `marinade_rouge_africaine` restent de vraies marinades génériques (la viande n'apparaît que dans le texte des étapes, jamais dans la liste d'ingrédients). | **forte** |
| 3 | **Ces 5 fiches tombent dans un angle mort structurel du reste de l'appli** | Leur `role` est `"autre"` (kind `Base`), comme toutes les marinades — donc elles ne sortent jamais dans « Avec ce que j'ai » en tapant « plat » même si l'utilisateur a justement un gigot ou des gambas au frigo. Elles ne sont ni une marinade réutilisable, ni un plat proposé : un vrai cul-de-sac. | moyenne |
| 4 | **119 fiches du catalogue commencent par une étape « mariner » sans aucun lien, dans aucun des deux sens, avec le coin Marinades** | Recherche sur les 1605 fiches : 119 recettes ont « mariner » dans leurs deux premières étapes et ne sont pas dans `MARINADES`. Le coin ne renvoie vers aucune d'elles, et ces 119 fiches ne renvoient jamais vers `/marinades`. Plusieurs familles entières de marinade n'existent nulle part dans le coin alors qu'elles sont déjà écrites : babeurre (`buttermilk_fried_chicken`), achiote-agrumes (`pollo_pibil`, `tacos_al_pastor`), vinaigre-soja-laurier à la philippine (`adobo_poulet`), glaçage hoisin chinois (`char_siu_poulet`), sauce d'huître cambodgienne (`lok_lak`). | forte |
| 5 | **Le ceviche / poisson « cuit » à l'acide n'est présenté nulle part comme un geste à part entière** | `ajitama` (œufs marinés au soja, 6 h), `poisson_cru_fidji`/`poisson_cru_coco`/`poisson_cru_tahitienne` (citron vert, 15 min, le poisson devient opaque) existent dans la bible. Le coin distingue déjà marinade liquide / cure à sec (gravlax) / rub sec (BBQ) comme trois gestes différents — le ceviche en est un quatrième, et le repère n°1 des « repères du cuisinier » met en garde contre « un fruit de mer qui cuit » par l'acide sans jamais dire que ce geste a un nom, des fiches dédiées et des usages volontaires. | moyenne |
| 6 | **Aucune catégorie pour les œufs marinés** | `ajitama` existe (6 h dans le soja-mirin, classique du ramen) mais le type `Protein` du coin (`boeuf \| agneau \| porc \| volaille \| poisson \| crevettes \| vegetal`) n'a pas de valeur « œuf » : structurellement impossible à y rattacher sans élargir le type. | faible |
| 7 | **Incohérence de repos affichée sur une fiche déjà dans le coin** | Le BBQ rub américain affiche « Rub sec, repos : 0 min » sur sa vignette (`rest: 0` dans les données), alors que sa propre fiche dit noir sur blanc : « laissé reposer à température ambiante 30 min à 1 h avant de cuire, ou toute une nuit au frigo pour une pièce épaisse ». Le badge contredit le texte juste en dessous. | moyenne |
| 8 | **Déséquilibre des protéines, deux semaines après les derniers ajouts** | « Tofu & légumes » n'a qu'1 fiche (le tofu) : aucune marinade dédiée à un légume à griller (aubergine façon nasu dengaku au miso, halloumi, portobello). « Crevettes & fruits de mer » n'a que 2 fiches : rien sur moules, calamars ou noix de Saint-Jacques, pourtant déjà présents ailleurs dans la bible (`calamars_romaine`, etc., non vérifié un par un ici). | faible |

## 2. Repéré mais écarté (vérifié, pas un bug)

- Les marinades qui citent la viande uniquement **dans le texte des étapes** (`marinade_bulgogi` : « 600 g de bœuf… » ; `marinade_yassa` : « avec la viande… ») restent de vraies marinades réutilisables : rien dans leur liste d'ingrédients ni leur `role` ne change selon la pièce choisie. Seules les 5 fiches du constat n°2 structurent la viande en ingrédient.
- Le calcul « Protéines : X g par part » n'est **pas** faussé par les fiches du constat n°2 : toutes les marinades (bundlées ou non) ont `role: "autre"`, et ce champ n'est calculé qu'au export pour `role === "plat"` — il est donc simplement absent partout, de façon cohérente.
- `coq_au_vin` (role plat, repos 17 h) et `daube_provencale` (16 h) ont bien une vraie étape de marinade au vin complète et détaillée dans leur propre fiche : rien à leur reprocher en soi, seulement leur absence de rattachement au coin Marinades (constat n°1 et 4).

## 3. Pourquoi c'est un angle mort pour un chef

Le coin Marinades se présente comme la référence centrale pour « quelle marinade pour ma viande » — mais un chef qui
connaît la cuisine française cherchera d'abord la marinade au vin, la plus ancienne et la plus enseignée, et ne la
trouvera pas. Les 119 fiches orphelines montrent que la rubrique n'a capté qu'une fraction des marinades déjà
écrites dans la bible : elle fait figure de florilège plutôt que de référentiel, ce qui est trompeur pour qui s'y fie
pour « tout ce qu'il faut savoir sur les marinades ». Le constat n°2 est le plus gênant en interne : une rubrique
censée séparer « la marinade » de « la recette finie » contient elle-même cinq recettes finies déguisées en
marinades, ce qui brouille la promesse éditoriale du coin pour les 12 autres fiches qui, elles, la tiennent.

## 4. Pistes de correction (non appliquées)

- **#1** : ajouter une fiche « marinade au vin rouge » générique (mirepoix, bouquet garni, vin, 12 à 24 h), réutilisable
  pour un futur braisé ou civet, et noter dans son texte qu'elle est déjà utilisée telle quelle par `coq_au_vin`,
  `daube_provencale`, `civet_lievre` et `lievre_royale`.
- **#2 et #3** : soit réécrire les 5 fiches bundlées pour qu'elles redeviennent de vraies marinades génériques (la
  pièce de viande sort de la liste d'ingrédients vers le texte des étapes, comme `marinade_bulgogi`), soit les sortir
  du coin Marinades et les laisser vivre comme plats à part entière (`role: "plat"`) avec un lien « Fait avec notre
  marinade [X] » vers une fiche marinade générique correspondante.
- **#4** : à défaut d'ajouter toutes les familles manquantes au coin, relier dans les deux sens : un bloc « Cette
  recette commence par une marinade » sur les 119 fiches concernées, pointant vers la rubrique, et une section
  « D'autres marinades, utilisées dans des recettes complètes » sur `/marinades` qui liste quelques-unes de ces 119
  fiches sans les dupliquer.
- **#5 et #6** : ajouter une section « Ceviche et poisson cru mariné » (ou élargir `REPERES_MARINADE`) qui nomme le
  geste et renvoie vers `poisson_cru_fidji`/`poisson_cru_coco`/`poisson_cru_tahitienne` ; envisager d'élargir `Protein`
  avec une valeur `oeuf` pour rattacher `ajitama`, ou a minima le citer en texte dans les repères.
- **#7** : remettre `rest` à une valeur cohérente (30 à 60 min, ou champ dédié pour le cas « toute une nuit en
  option ») sur `bbq_rub_americain`, ou changer le libellé affiché pour ne pas promettre « 0 min » quand la fiche dit
  l'inverse.
- **#8** : au moins une marinade pour légumes à griller (type miso-mirin pour aubergine, nasu dengaku) et une pour
  fruits de mer autres que la crevette.

## 5. Corrigé (21/11/2026, commit `76e7a7e`)

- **#1** : `marinade_vin_rouge` ajoutée (vin rouge, carottes, oignon, ail, bouquet garni, 12 à 24 h), réutilisable pour
  un futur braisé ou civet ; son texte cite `coq_au_vin`, `daube_provencale`, `civet_lievre` et `lievre_royale` comme
  l'utilisant déjà telle quelle.
- **#2 et #3** : les 5 fiches bundlées (`harissa_marinade_agneau`, `mojo_cubain_porc`, `porc_citronnelle_vietnamien`,
  `shawarma_marinade`, `crevettes_citron_vert_marinade`) réécrites en vraies marinades génériques : la pièce de viande
  est sortie de la liste d'ingrédients vers le texte des étapes, comme `marinade_bulgogi`. Vérifié sur la fiche
  shawarma : l'ingrédient « poulet » a disparu de la liste, le texte dit « poulet (ou agneau, même proportions) ».
- **#4** : section « D'autres marinades, dans des recettes complètes » ajoutée sur `/marinades`, avec 6 liens vers des
  familles entières (babeurre, achiote-agrumes mexicaine ×2, adobo philippin, glaçage hoisin chinois, sauce d'huître
  cambodgienne) sans dupliquer de contenu. Le lien inverse (bloc sur les 119 fiches concernées) n'a pas été fait : trop
  de fiches pour cette session, resterait à faire.
- **#5 et #6** : le ceviche devient un 4e geste nommé dans `REPERES_MARINADE`, avec un flag `acid` sur `MarinadeEntry` ;
  `poisson_cru_fidji` (kokoda) et `poisson_cru_tahitienne` rattachés. `Protein` élargi avec `oeuf`, `ajitama` (œufs
  marinés au soja) rattaché avec sa propre catégorie dans les puces de filtre.
- **#7** : `bbq_rub_americain` passé de `repos: 0` à `repos: 30` (min), cohérent avec le texte de sa fiche.
- **#8** : `marinade_miso_aubergine` (nasu dengaku, sourcée sur TikTok @chey__nese, 30,2K j'aime, ingrédients exacts
  dans la légende) et `marinade_calamars_citron_persillade` (sourcée sur TikTok @poesiadefogon, 67,1K j'aime — une
  sauce-marinade ail/citron/persil espagnole à la fois badigeonnée avant cuisson et servie en nappage) ajoutées.
  Tofu & légumes passe de 1 à 3 fiches, Crevettes & fruits de mer de 2 à 3.

**Bug trouvé en vérifiant en local** (pas dans la liste d'origine) : le titre « marinade_vin_rouge_classique » (id
d'origine) contenait « classique », qui contient lui-même la sous-chaîne « lassi » — collision avec le motif
`/lassi/` de `src/lib/dressage.ts` (choix de la « finition et dressage » affichée sur la fiche), qui affichait à tort
un conseil de présentation de boisson (« verres passés au congélateur ») sur une marinade. Même défaut de limite de
mot que l'audit cuisinier amateur avait trouvé dans `art.tsx` la veille. Corrigé par un renommage de l'id
(`marinade_vin_rouge`) et l'ajout d'une limite de mot (`\blassi\b`) au motif de `dressage.ts`.
