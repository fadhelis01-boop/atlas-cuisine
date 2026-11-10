# Audit d'ATLAS par un chef de cuisine et un parent de deux enfants (10 novembre 2026)

Deux regards, une seule question : est-ce qu'on peut faire confiance à ATLAS pour nourrir une famille de quatre, soir après soir, et est-ce qu'un professionnel signerait les fiches ?

Les audits du 16 et du 21 octobre ont réglé beaucoup de choses : la semaine qui tournait en boucle, les enfants oubliés du planificateur, l'acidité, les protéines, le vocabulaire. Ils ne sont pas refaits ici. Cet audit porte sur ce qu'ils n'ont pas regardé : la sécurité des aliments, les allergènes cachés, le temps réel d'un soir de semaine, la liste de courses vue par celui qui la tient au supermarché, la congélation et les 199 fiches ajoutées depuis (dont 169 tirées de TikTok).

**Méthode.** Mesures sur les 1 232 fiches (scripts sur les données publiées). Huit semaines de « Ma semaine » simulées pour 2 adultes et 2 enfants de 4 et 8 ans, en novembre-décembre, zone nord. Puis l'appli en ligne, sur un écran de téléphone, comme un parent qui l'ouvre un mardi à 18 h 30 : profil famille, « Propose-moi », une fiche, la semaine, les courses. L'état du navigateur a été remis comme avant.

## Verdict

Le fond est bon. Les quantités tiennent (150 g de viande ou de poisson par part en médiane). La semaine est équilibrée : 3 à 4 repas de poisson, 2 à 5 de légumineuses, 1 à 4 de viande rouge sur 14 repas. Les fiches sont faciles (niveau 1 ou 2 pour 112 repas sur 112), et le profil famille est pris en compte partout.

Mais trois choses empêchent un parent de s'y fier les yeux fermés :

1. **Des règles de sécurité qui se contredisent d'une fiche à l'autre** : le riz cuit est « 24 h au plus » sur une fiche, « 3 jours » sur 49 autres ; la mayonnaise maison à l'œuf cru se garde 3 jours, et les sauces qui l'utilisent 4 jours, « dès 1 an ».
2. **Un temps affiché qui ne dit pas tout** : l'appli m'a proposé des falafels pour ce soir. Les pois chiches doivent tremper 24 heures.
3. **Des allergènes qui passent à travers** quand une ligne regroupe deux ingrédients : la blanquette et la moussaka n'affichent pas le gluten.

Rien de tout ça n'est difficile à corriger. Tout se règle dans les données et dans deux ou trois règles du moteur.

## 1. Ce qui marche (et qu'il ne faut pas casser)

- **Le profil famille.** Deux enfants de 4 et 8 ans se déclarent dès la première page ; ensuite les fiches s'ouvrent pour 3 parts, la semaine écarte les plats d'adultes et le piment sans adaptation.
- **L'équilibre de la semaine.** Sur 8 semaines : 97 plats différents sur 112 repas, aucune protéine identique deux repas de suite, 0 à 2 fritures ou panés par semaine, 9 à 10 cuisines différentes.
- **Les portions.** Médiane de 150 g de viande ou de poisson cru par part, 75 g de féculent sec. Les fiches qui dépassent 260 g par part sont des moules, du poulpe, des morceaux avec os : c'est normal.
- **Les desserts restent raisonnables** : 12 g de sucre ajouté par part en médiane. Seules 3 fiches dépassent 50 g, des gourmandises assumées (cookies fourrés, baba, poires Belle-Hélène).
- **La fiche** : mise en place, matériel, repères visuels, minuteurs, « si ça rate », variantes sans porc ou sans alcool. Un amateur s'y retrouve.
- **La préparation à l'avance et les restes du dimanche**, qui sont l'idée la plus utile pour une famille.

## 2. Sécurité des aliments

### P0 · La conservation par défaut est fausse pour les aliments fragiles

638 fiches portent le texte par défaut : « 3 jours au frigo, dans une boîte fermée ». Il a été posé partout, y compris là où il ne faut pas :

| Fiches au texte par défaut | Nombre | Ce qu'un chef écrirait |
|---|---|---|
| Plats de poisson et fruits de mer | 80 | 1 à 2 jours, crustacés et coquillages 1 jour |
| Plats au riz cuit | 49 | 1 jour, refroidi vite (la fiche du riz cantonais le dit elle-même : « pas plus de 24 h, bactérie Bacillus cereus ») |
| Plats à la mayonnaise maison | 15 | 24 h, au froid |
| Œufs mollets, pochés, coulants | 34 | à manger tout de suite |

L'appli se contredit donc d'une fiche à l'autre. C'est le premier point à corriger : une règle de conservation par famille d'aliment, calculée à partir des ingrédients, qui remplace le texte par défaut.

### P0 · La mayonnaise maison : durée et âge incohérents

- La fiche mayonnaise (jaune d'œuf cru) dit « 3 jours ». Les recommandations sanitaires disent 24 h, 48 h au plus, au frigo.
- Les sauces qui l'utilisent annoncent **plus** que leur base : « façon Giant » et « façon Big Tasty » 4 jours (ajoutées le 04/11, mon erreur).
- **44 fiches qui utilisent la mayonnaise maison sont notées pour des enfants** (dès 1 an pour 5 d'entre elles, dès 3 ans au plus pour 41), alors que la mayonnaise elle-même est marquée « en version sans œuf ou avec œuf pasteurisé ». Le filtre « enfants » du planificateur ne regarde que l'âge de la fiche, pas celui de ses sous-recettes : un plat noté dès 1 an peut contenir de l'œuf cru.

À faire : l'âge d'une fiche = le plus élevé de ses sous-recettes (calculé, pas saisi) ; une vraie variante « mayonnaise sans œuf cru » (œuf pasteurisé, ou base yaourt/aquafaba) que le profil enfant applique tout seul ; durées alignées.

### P1 · Autres incohérences d'âge héritées

Le même calcul révèle d'autres écarts : quiches et tartes « dès 1 an » sur une pâte brisée notée 4 ans (c'est l'âge de la pâte brisée qui est probablement faux), effiloché de poulet dès 1 an avec une sauce barbecue dès 3 ans, tropézienne dès 1 an sur une brioche à 4 ans. 61 couples fiche/sous-recette au total.

### P1 · La friture sans consigne de sécurité

37 fiches font frire dans un bain d'huile (accras, nems, churros, tenders, sfenj, beignets…) sans un mot de sécurité. Dans une cuisine avec un enfant de 4 ans, il faut au minimum : casserole à l'arrière, queue tournée, ne jamais quitter l'huile chaude, couvercle à portée en cas de flamme, jamais d'eau. Une ligne automatique dans « Avant de commencer » suffit.

### P1 · Le café et l'alcool dans des desserts « pour les petits »

Le gâteau d'anniversaire au chocolat (dès 1 an) se mouille au café chaud, avec l'eau en simple alternative. La sauce au poivre (dès 3 ans) se flambe au cognac, les cannelés et la galette des rois (dès 3-4 ans) prennent du rhum. L'alcool cuit ne s'évapore pas entièrement. Pour un profil avec enfants de moins de 6 ans, la variante sans café ni alcool devrait s'appliquer d'office.

### P2 · Petits points

- Fromages au lait cru (tartiflette, flamiche au maroilles, rouleaux au reblochon, pâtes au mont-d'or) : pas de mention pour les femmes enceintes.
- Huile pimentée : « 1 mois au frigo » sans précaution sur l'ail ou les aromates frais s'il y en a (risque botulique).
- Les quantités divisées pour 3 parts donnent « ¾ pincée de sel », « 2 ¼ c. à s. d'huile » : arrondir les pincées et les cuillères à la demie.

## 3. Allergènes

### P0 · 28 fiches affichent une liste d'allergènes incomplète

Le moteur lit l'allergène de l'ingrédient de référence de chaque ligne. Quand une ligne en contient deux, le second disparaît. Mesuré ligne par ligne, en vérifiant qu'aucune autre ligne de la fiche ne le couvre :

- **Gluten** absent : blanquette de poulet, blanquette de veau, moussaka (« 40 g de beurre + 40 g de farine », rattaché au beurre).
- **Arachide** absente : bao au poulet (« coriandre et cacahuètes »), rouleaux de printemps (beurre de cacahuète dans la sauce), ají de gallina et moambe (en alternative).
- **Sésame** absent : poulet du Général Tao, ramen au tofu (le mien), canard laqué.
- **Céleri** absent : lasagnes bolognaise, pot-au-feu, bouillon de légumes.
- **Moutarde** absente : 3 fiches dont la vinaigrette « moutarde » est dans le libellé.
- **Fruits à coque** absents : mansaf (« amandes et pignons »), maqluba, pommes au four (« raisins secs ou noix »), energy balls.
- **Lait** absent : beignets de crevettes (« œufs et 5 cl de lait », le mien), choucroute (« graisse de canard ou beurre »).

Pour une famille avec une allergie, c'est le point le plus grave de l'audit. À faire : scinder ces lignes et ajouter un contrôle automatique « mot d'allergène dans le libellé, absent de la fiche ». Les ingrédients en alternative (« ou cacahuètes ») doivent compter comme « peut contenir ».

## 4. Le soir de semaine, en vrai

### P0 · Ce qui se prépare la veille n'apparaît nulle part

Mardi 10 novembre, 18 h 30, « Ma semaine » propose pour ce soir des **falafels**. La fiche demande des pois chiches secs trempés 24 heures, et sa première étape dit « 1 h au frais » pour 15 minutes de repos annoncées. Même chose avec « Propose-moi, 20 min » : en tête, le **riz cantonais**, qui demande du riz cuit la veille.

Mesures :

- **14 plats et entrées annoncés en 45 minutes ou moins** demandent quelque chose la veille ou une nuit avant : riz cantonais, arroz chaufa, riz sauté au bœuf, falafels, ta'ameya, shawarma, chich taouk, poulet tandoori, buttermilk fried chicken, tenders, poulet croustillant à l'air chaud, bocadillo de tortilla, gallo pinto, pyttipanna.
- **31 plats ont des étapes qui durent nettement plus que le temps annoncé**, presque toujours à cause d'une marinade ou d'un trempage : brandade (dessalage de la morue, 24 h), tajine de poulet aux olives, poulet yassa, fabada, chich taouk (35 min annoncées, 4 h de marinade), pizza margherita (20 min annoncées, la pâte lève 1 h).
- Le poulpe surgelé (proposé un samedi) doit décongeler une nuit : ce n'est pas dit.

À faire : un champ « à lancer la veille » (trempage, marinade, décongélation, riz cuit, pâte à lever), calculé depuis les étapes ; un badge sur la fiche (« ⏰ à lancer la veille ») ; « Propose-moi » et la semaine ne proposent pas pour ce soir un plat qui demandait quelque chose hier, et rappellent la veille au soir ce qu'il faut lancer.

### P1 · « 45 minutes au plus » ne veut pas dire « à table à 19 h 15 »

La règle des soirs de semaine accepte un plat de 25 minutes actives et jusqu'à 60 minutes de cuisson sans surveillance. Sur 8 semaines simulées, 2 à 4 dîners par semaine dépassent 45 minutes au total (thiou au poulet 75 min, tajine au citron 85 min, bourguignon aux champignons 85 min). Pour un parent qui rentre à 18 h 30 avec des enfants qui dînent à 19 h 15, c'est trop tard. À faire : un réglage « à table à … », et l'heure de début affichée (« commence à 17 h 50 »).

### P2 · L'accueil d'un soir de semaine

Le « menu du jour, soir de semaine » proposait des boulettes de poisson danoises et une **apple pie de 1 h 40**. La rangée « Pour les enfants » montrait une bouillabaisse (1 h 25) et un ragù bolognais (2 h 30). Le soir, l'accueil devrait trier par temps total.

## 5. La semaine et les courses, vues du supermarché

### P1 · Le panier part dans trop de directions

Une semaine simulée demande, pour un seul repas chacun : du dashi, de la farofa, du queso fresco, des tortillas de maïs, de la viande des Grisons, des haricots noirs. Quatre semaines sur huit ont au moins 3 produits introuvables dans un supermarché ordinaire. Avec 9 à 10 cuisines par semaine, la famille fait deux magasins ou gaspille des fonds de paquet. Un chef de famille ancre la semaine sur 3 ou 4 bases connues des enfants et garde 1 ou 2 découvertes. À faire : un plafond de produits « épicerie du monde » par semaine (réglable), et un bonus aux plats qui réutilisent un ingrédient déjà acheté.

### P1 · Le même produit deux jours de suite

Dans la première semaine simulée : moules-frites mardi midi, moules marinières mercredi midi, soit 3,75 kg de moules en deux jours. La règle « pas deux fois la même protéine de suite » compare des familles (« poisson ») et pas le produit principal. À faire : pas deux fois le même ingrédient principal dans la semaine.

### P1 · La liste de courses ne s'additionne pas toujours

Extraits réels de la liste de la semaine 1 :

- « Ail : 2 gousses d'ail + 1 ½ gousses d'ail + 1 gousses d'ail + 1 ½ gousses d'ail… »
- « Persil : 1 c. à s. + ¾ bouquet de persil + ¾ bouquet de persil »
- « Oignon jaune : 8 + 800 g » ; « Pomme de terre : 2,9 kg + 2 » ; « Saumon : 3 » (trois quoi ?)
- « Haricots blancs : 1 bocaux (800 g) »

69 lignes pour 14 repas. À faire : convertir en une unité d'achat par produit (gousses → têtes d'ail, bouquets entiers, pièces → kg approximatif), arrondir à ce qu'on achète vraiment (1 bouquet, 1 tête, 1 filet de 3 citrons).

### P1 · Le calendrier des saisons a des erreurs

Le référentiel marque hors saison des produits qui sont en pleine saison :

- **Épinard** : de saison seulement de mars à mai. En réalité de septembre à mai.
- **Citron, orange** : hors saison en novembre. Les agrumes arrivent à ce moment-là (et le citron est un produit de placard toute l'année).
- **Cresson** : mars à mai seulement (en réalité de septembre à mai).

À l'inverse, chaque semaine de novembre-décembre propose des tomates, des courgettes, des poivrons, des haricots verts ou des petits pois frais. Le planificateur tient compte de la saison, mais pas assez. À faire : corriger le calendrier, et en hiver remplacer automatiquement la tomate fraîche par des tomates pelées dans les plats cuisinés.

### P2 · Préparer à l'avance : deux conseils de chef à revoir

- « Lave et coupe d'un coup : tomate, poivron, pomme de terre… 3 jours au plus » : une pomme de terre coupée noircit (à garder dans l'eau, 24 h au plus) et une tomate coupée rend son eau. Seuls les légumes fermes se coupent trois jours à l'avance.
- Pour les falafels, la tâche « à préparer à l'avance » retenue est « Frire 4 min à 175 °C ». C'est le contraire : on fait tremper la veille, et on frit au dernier moment.

### P2 · Détails

- « Utilise le reste de citron de la veille » revient 4 soirs sur 7 : un demi-citron n'est pas un reste qui mérite une mention.
- « La boisson maison de la semaine : chocolat chaud, en carafe pour les repas » : du chocolat chaud à chaque dîner des enfants, ce n'est pas l'idée.
- Les parts : un enfant de 8 ans compte pour une demi-part, la famille cuisine pour 3. Il ne reste rien pour la gamelle du lendemain midi. À faire : une case « cuisiner aussi pour les gamelles ».

## 6. Ce qui manque à une famille

- **La congélation.** 81 plats sur 661 disent s'ils se congèlent ; 88 mijotés d'une heure ou plus n'en disent rien. Pour une famille, le bourguignon du dimanche fait trois repas, dont deux au congélateur. À faire : une mention « se congèle 3 mois » sur tous les plats qui le permettent, un bouton « doubler et congeler la moitié » et un rayon « mon congélateur » dans le frigo.
- **Les enfants en cuisine.** 2 fiches sur 1 232 disent ce qu'un enfant peut faire (casser les œufs, mélanger, façonner les boulettes). Pour un enfant de 4 ou 8 ans, c'est ce qui lui fait goûter le plat.
- **Les desserts de tous les jours.** 8 desserts sur 190 sont marqués légers. Un soir de semaine, un fruit, un yaourt, une compote suffisent, et l'appli ne les propose pas.
- **Les bébés.** Aucune fiche avant 1 an (la diversification, purées et morceaux fondants). Pour une famille avec un petit dernier, c'est une rubrique à part entière.
- **Le mangeur difficile.** Le carnet « les enfants n'ont pas aimé » existe, mais rien pour présenter un légume refusé autrement (en purée, en galette, caché dans une sauce). Le sujet est en partie traité (pâtes aux légumes cachés), sans rubrique.

## 7. Les 169 fiches tirées de TikTok

Rédigées plus longuement que le reste du catalogue (4,1 étapes et 90 mots en médiane, contre 3,4 et 52 pour les autres plats), elles sont plutôt meilleures sur le papier. Trois réserves :

- **Aucune n'a de photo** (169 sur 169). Le catalogue entier en compte 418 sans photo sur 1 232. Une fiche sans photo se choisit beaucoup moins, surtout par un enfant. Certaines prennent un emoji trompeur (la karantika, un plat salé, porte l'icône du flan sucré).
- **155 sur 169 ont un texte enfants générique** (« ✓ dès 3 ans ») sans adaptation (moins de piment, comment couper pour un petit).
- Elles ont été écrites vite, à partir de légendes souvent vides. Elles sont les premières à tester en cuisine, avant les fiches anciennes.

## 8. Angles morts de la demande

- **Personne n'a encore cuisiné une seule fiche.** Tout ce qui précède est mesuré sur le papier. Le protocole d'essai existe (« 30 plats à tester en priorité »). Une semaine réelle, cuisinée par la famille avec le carnet, apprendra plus que dix audits.
- **Le coût réel.** Le budget affiché (75 € pour 7 dîners) vient des indicateurs €, €€, €€€, pas des prix. Une semaine avec du poulpe et des crevettes coûte nettement plus.
- **Les jours sans courses.** Rien pour le soir où le frigo est presque vide et où personne ne veut ressortir : une liste « placard de secours » (pâtes, œufs, conserves) et ses 15 recettes.
- **L'accessibilité.** Les quatre boutons de la première page (sans porc, sans alcool, végétarien, allergies) n'ont pas de nom pour un lecteur d'écran.

## 9. Ordre de travail recommandé

| Priorité | Chantier | Effort |
|---|---|---|
| P0 | Allergènes : scinder les 28 lignes composées, contrôle automatique libellé ↔ allergènes, alternatives en « peut contenir » | ½ journée |
| P0 | Conservation calculée par famille d'aliment (poisson, riz, mayonnaise, œufs coulants) à la place du texte par défaut | ½ journée |
| P0 | Âge hérité des sous-recettes ; vraie variante mayonnaise sans œuf cru appliquée au profil enfant | ½ journée |
| P0 | « À lancer la veille » : champ calculé, badge sur la fiche, exclu de « ce soir », rappel la veille | 1 journée |
| P1 | Consigne friture ; café et alcool écartés d'office pour les moins de 6 ans | 2 h |
| P1 | Semaine : même ingrédient principal une fois, plafond d'épicerie du monde, heure « à table à » | 1 journée |
| P1 | Courses : unités d'achat et arrondis | ½ journée |
| P1 | Calendrier des saisons corrigé, tomates pelées en hiver | 2 h |
| P1 | Congélation : mention sur les plats concernés, « doubler et congeler » | ½ journée |
| P2 | Rôle des enfants en cuisine, desserts légers du quotidien, placard de secours, photos des fiches TikTok, arrondis des pincées, boutons nommés | au fil de l'eau |

Toutes les fiches restent **non testées en cuisine** ; la première semaine réellement cuisinée devrait passer avant les nouveaux ajouts.

## 10. Mise en œuvre (10 novembre 2026, même jour)

Les règles sont calculées à l'export (`bible/securite_famille.py`), pour que les fiches anciennes et futures y passent toutes. Contrôles ajoutés : tests 112 à 118 (`app/tests/e11-audit-chef-famille.ts`).

**Points urgents**
- **Allergènes** : 65 lignes composées séparées en vraies lignes (« 40 g de beurre » et « 40 g de farine »), et les allergènes nommés dans un libellé s'ajoutent à la fiche (« ou de cacahuètes » compte comme « peut contenir »). Blanquette et moussaka affichent le gluten, le bao l'arachide. Test 112 : plus aucun mot d'allergène sans son allergène.
- **Conservation** : poisson 2 jours, fruits de mer, riz cuit, œuf cru et œufs coulants 24 h (178 fiches ajustées) ; jamais plus long que les sous-recettes. La mayonnaise maison passe à 24 h.
- **Âge** : une sous-recette qu'on ne mange pas avant N ans relève l'âge du plat (l'âge « pour aider », comme sabler une pâte brisée, ne compte pas). Les 44 fiches à mayonnaise maison disent : « moins de 6 ans, femme enceinte : mayonnaise du commerce ». Encadré « œuf cru » sur 53 fiches.
- **À lancer la veille** : 67 fiches repérées (trempage, marinade longue, riz ou tortilla de la veille, dessalage, décongélation), 54 avec un temps à prévoir avant (marinade d'une heure, repos au frais). Badge en tête de fiche ; jamais proposé pour ce soir (« Propose-moi », Express, recherche, frigo, accueil, rubrique Enfants) ; « Ma semaine » ne le met pas le jour même et rappelle la veille au soir ce qu'il faut lancer.
- **Soirs de semaine** : avec des enfants de moins de 11 ans, le temps compté est le temps total. Sur 8 semaines simulées : plus aucun dîner de semaine au-delà de 45 minutes.

**Points importants et détails**
- Même produit principal une seule fois par semaine ; au plus 3 produits d'épicerie du monde par semaine.
- Liste de courses : gousses et têtes d'ail, bouquets et bottes, pavés, boîtes additionnés ; pièces et grammes de légumes en un seul poids ; « 1/2 » compris ; en hiver, note « tomates pelées » sur la tomate fraîche.
- Saisons : épinard et cresson de septembre à mai, orange de novembre à avril, citron au placard toute l'année.
- Moins de 6 ans : café et alcool peu cuit (moins de 45 min) écartés ; un vin mijoté 2 h reste permis. Le gâteau d'anniversaire se mouille à l'eau (le café devient l'option des grands).
- Consigne de sécurité friture sur chaque fiche qui fait frire.
- Congélation dite sur 207 plats (148 ajoutés), bouton « doubler pour en congeler la moitié ».
- « + gamelles » dans Ma semaine : les dîners du lundi au jeudi cuisinent aussi le déjeuner du lendemain (courses et portions).
- 419 fiches disent ce que les enfants peuvent faire, avec l'âge (dans le détail de la fiche, pour garder le démarrage léger).
- Lait cru signalé aux femmes enceintes (9 fiches).
- Rubrique Enfants : desserts de tous les jours, « un légume refusé ? », repères avant 1 an (avec le lien officiel mangerbouger.fr).
- « Placard de secours » dans Avec ce que j'ai.
- Accueil du soir : plat en 45 min au total, dessert léger ou de 20 min, rangée enfants faisable ce soir.
- Pincées entières et cuillères à la demie quand on change le nombre de parts.
- Préparation à l'avance : ce qui doit se faire la veille en premier, jamais une friture, une cuisson minute ou une marinade de poisson ; pommes de terre, tomates et avocats ne se coupent plus trois jours avant.
- Menus de fête : desserts variés d'un menu à l'autre, un vrai dessert hors menu léger ; le pizza scroll salé n'est plus classé en dessert.
- Icônes : jamais d'icône sucrée sur un plat salé ; boutons de la première page nommés pour les lecteurs d'écran ; « reste de citron » n'est plus signalé ; la boisson de la semaine n'est plus un chocolat chaud.
- Budget de démarrage : 393 Ko sur 400.

**Pas fait**
- Photos des 169 fiches TikTok : il faut chercher des photos sous licence libre fiche par fiche, sans images générées ; à faire en lot séparé.
- Prix réels : le budget reste un ordre de grandeur tiré des €.
- Recettes avant 1 an : seulement des repères, pas de fiches (contenu à valider par un professionnel de santé).
- La semaine réellement cuisinée en famille, qui reste le meilleur test.
