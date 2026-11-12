# Audit « fin gourmet » de la cuisine française d'ATLAS (12/11/2026)

Regard d'un amateur exigeant de cuisine française : ce qu'un gourmet cherche dans l'appli et ne trouvait pas. Tout est
mesuré sur les données exportées (`app/src/data/recipes.json`), puis corrigé le jour même. Contrôle automatique : test 123.

## 1. Constats mesurés (avant)

| Angle | Mesure | Gravité |
|---|---|---|
| Classiques absents | ~65 sur une liste de référence de 170 (bistrot, poissons, sauces, abats, gibier, entrées, pâtisserie, viennoiserie, confiserie) | forte |
| Socle technique | aucun fond brun, fond blanc, fumet ni court-bouillon ; pas de pâte à choux en fiche de base ; sauces dérivées manquantes (Mornay, bordelaise, Choron, ravigote, Soubise, poivrade, morilles) | forte |
| Abats et gibier | aucun ris de veau, rognons, foie de veau, tête de veau, civet, pigeon, pintade | forte |
| Grande pâtisserie | pas de Saint-Honoré, religieuse, opéra, bavarois, pêche Melba, vacherin, dacquoise, merveilleux, puits d'amour | forte |
| Classiques régionaux bâclés | 82 plats français en moins de 4 étapes, dont moules marinières, sole normande, bouchées à la reine, blanquette, baeckeoffe, pissaladière, quenelles Nantua, croque-monsieur, Saint-Jacques | forte |
| Accords mets-vins | 19 plats français sur 160 avec un accord vin, 24 avec un accord sans alcool ; aucun accord régional | moyenne |
| Régions | « Bourgogne », « Franche-Comté » et « Bourgogne-Franche-Comté » coexistaient ; 35 fiches de base sans région | faible |
| Lexique | gestes classiques absents : monter au beurre, chinoiser, réduire à glace, brider, escaloper, monter les blancs, beurre clarifié, fumet, fond, meunière, crème anglaise à 83 °C, luter, dessécher, quadriller | moyenne |
| Astuces | 182 fiches françaises sans aucune astuce | moyenne |

## 2. Corrigé

- **63 fiches nouvelles** (`recipes_v7_france_bistrot.py`, `recipes_v7_france_mer_sauces.py`, `recipes_v7_france_patisserie.py`, `recipes_v7_france_complements.py`) :
  - bistrot et terroir : steak au poivre, canard à l'orange (gastrique), tête de veau gribiche, pâté en croûte (version volaille), foie gras mi-cuit (50 °C à cœur), waterzoï, andouillette, boudin aux pommes, pommes dauphine, Anna, boulangère ;
  - entrées : vichyssoise, artichauts vinaigrette, grenouilles en persillade, cervelle de canut ;
  - abats et gibier : ris de veau aux morilles, rognons à la moutarde, foie de veau, civet de chevreuil, civet de lièvre, daube de sanglier, faisan en cocotte, pintade au chou, pigeon aux petits pois ;
  - fonds et sauces : fond brun, fond blanc, fumet, court-bouillon, Mornay, bordelaise, Choron, ravigote, Soubise, morilles, poivrade, diable, charcutière ;
  - mer : raie au beurre noisette, truite aux amandes, maquereaux au vin blanc, thon basquaise, langoustines, homard grillé, tourteau, encornets, bulots ;
  - pâtisserie et boulangerie : pâte à choux, religieuse, Saint-Honoré, opéra, bavarois, pêche Melba, vacherin, succès praliné, merveilleux, puits d'amour, pithiviers, nonnettes, calissons, pâtes de fruits, pains aux raisins, pain viennois, pralines roses.
- Le porc et l'alcool restent dans la recette d'origine, avec leur version adaptée quand elle existe (pâté en croûte, pintade, gélatine). L'andouillette et le boudin n'ont pas de version : un foyer sans porc ne les voit pas.
- **18 classiques régionaux réécrits** au niveau étalon (`complements_fin_gourmet.ETAPES`, mêmes ingrédients) : chaque étape a son geste, son temps et son repère, et chaque plat une astuce.
- **Accords mets-vins régionaux** (`complements_fin_gourmet.accords`) : un vin du terroir et un accord sans alcool du terroir pour chacun des 111 plats de terroir et de bistrot, ainsi que pour les entrées et desserts français. Exemples : un bourgogne pour la Bourgogne, un riesling pour l'Alsace, un cidre pour la Bretagne, un muscadet pour les poissons de Loire. Rien pour la cuisine des enfants ni les plats express. La mention Evin est affichée par l'appli.
- **Régions unifiées** : Bourgogne-Franche-Comté ; les bases sans région vont en « Cuisine de base ».
- **Lexique** : 15 gestes ajoutés.

## 3. Suite du 12/11 (deuxième passe)

- **Les 64 plats français du quotidien** encore en 2 ou 3 étapes réécrits au niveau étalon (`complements_etapes_fr.py`, `complements_etapes_fr2.py`, mêmes ingrédients) : plus aucun plat français sous 4 étapes.
- **Une astuce de cuisinier pour chaque fiche française** qui n'en avait aucune (226 fiches, `complements_astuces_fr.py`) : plus aucune fiche française sans astuce.
- **Lièvre à la royale** (version accessible en deux jours, roulé farci au foie gras) et **plateau de fruits de mer** en fiches.
- **Photos** : seconde recherche (`collect_v12.py`) ; artichauts, lièvre à la royale et plateau illustrés. 1 260 fiches illustrées.
- Test 123 renforcé : tous les plats français en ≥ 4 étapes, une astuce sur chaque fiche française.

## 4. Reste à faire

- 15 classiques sans photo juste (les banques libres n'en ont pas) : pommes Anna, pigeon, fond brun, court-bouillon, Choron, poivrade, raie, maquereaux au vin blanc, bulots, bavarois, vacherin, puits d'amour, faisan, sauces diable et charcutière. À photographier soi-même lors des tests.
- ~~65 entrées et desserts français en moins de 4 étapes~~ : réécrits le 12/11 (`complements_etapes_fr3.py`, `complements_etapes_fr4.py`, mêmes ingrédients) ; test 123 étendu aux entrées et desserts.
- Toutes ces fiches restent à tester en cuisine.
