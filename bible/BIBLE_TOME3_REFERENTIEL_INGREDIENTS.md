# 📗 BIBLE ATLAS : TOME 3 : Référentiel d'ingrédients V1

> Complète le Tome 1 (§7 filtres, §13 zéro déchet, §15.2 disponibilité) et le Tome 2 (schéma SQL §5, tests dorés §4).
> **Statut : V1 « brouillon éditorial ».** Aucune ligne n'est « vérifiée » (niveau A) tant qu'un(e) diététicien(ne) et un chef ne l'ont pas relue et signée (§1.5). Les marqueurs de risque (porc, alcool, allergène) sont volontairement **prudents** : en cas de doute, on signale.

---

## 1. Règles du référentiel

### 1.1 Légende des colonnes

| Colonne | Codes |
|---|---|
| **Allerg.** (14 allergènes UE) | `GL` gluten · `CR` crustacés · `OE` œufs · `PO` poissons · `AR` arachide · `SO` soja · `LA` lait · `FC` fruits à coque · `CE` céleri · `MO` moutarde · `SE` sésame · `SU` sulfites · `LU` lupin · `MM` mollusques. Suffixe `?` = **selon la marque / la recette**, à lire sur l'étiquette. |
| **Dérivés** | `PORC` porc certain · `PORC?` porc possible (origine à vérifier) · `ALC` alcool certain · `ALC~` traces / alcool de fermentation · `ANIM` dérivé animal (non végétarien/vegan) · `ANIM?` selon fabrication (ex. présure) · `—` rien à signaler |
| **Dispo** | 🟢 supermarché standard · 🟡 rayon monde / bio / grande surface · 🟠 épicerie spécialisée / marché · 🔴 difficile ou en ligne → voir substituts (§16) |
| **Notes / zéro déchet** | Parties utilisables (→ valorisation), alertes, ambiguïtés |

### 1.2 Convention d'identifiant
`id = "ing_" + slug(nom)` (minuscules, sans accents, tirets bas). Exemple : « Crème fleurette » → `ing_creme_fleurette`. Les **variantes** partagent une famille (`ing_vinaigre_*`). Les doublons (alias) sont gérés dans `aliases[]` (ex. « zucchini » → courgette).

### 1.3 Règles de calcul (rappel opérationnel)
1. Allergènes et dérivés **s'héritent** : recette ← ingrédients ← sous-recettes.
2. Un ingrédient **industriel composé** (bouillon cube, sauce, pâte de curry, chocolat, charcuterie) porte toujours le suffixe `?` pour les allergènes et un `PORC?` / `ALC~` si la composition varie. Il est **remplaçable par une version maison** (cf. Tome 1 §11).
3. **« Origine à vérifier »** : tout produit carné non précisé (« saucisse », « jambon », « chorizo ») est `PORC?` **par défaut**, sauf mention explicite (dinde, bœuf, agneau).
4. **Halal / casher** : le référentiel ne **certifie pas** ; il signale. L'abattage et la certification se vérifient à l'achat.
5. **Alcool** : trois états seulement : `ALC` (ajouté / ingrédient alcoolisé), `ALC~` (traces de fermentation ou support d'arôme), `—`. La cuisson **ne remet pas à zéro** un `ALC`.
6. **Miel** : `ANIM` + alerte « interdit avant 12 mois ».
7. **Recoupement croisé (hors UE 14)** : champ `watch[]` pour allergies fréquentes non réglementaires (pignon, sarrasin, kiwi, coco, argan…).

### 1.4 Cibles de volume V1

| Famille | Cible | Famille | Cible |
|---|---|---|---|
| Viandes & volailles | 35 | Herbes & aromates | 28 |
| Porc & charcuterie (+ alternatives) | 45 | Épices & mélanges | 55 |
| Poissons & fruits de mer | 35 | Condiments, sauces, bases | 60 |
| Œufs & produits laitiers | 55 | Huiles, graisses, sucrants, chocolat | 40 |
| Légumes & champignons | 85 | Alcools, arômes, dérivés | 40 |
| Fruits | 50 | Fruits à coque & graines | 25 |
| Légumineuses & céréales | 45 | Produits du monde (4 zones) | 70 |
| Farines, pains, pâtes | 50 | Pâtisserie, gélifiants, boissons | 30 |
| **Total** | **≈ 750 entrées planifiées** | **Livré dans ce tome** | **713 lignes (voir §18)** |

### 1.5 Processus de vérification (niveaux)
`Brouillon (C)` → relu par un rédacteur culinaire → `Calculé (B)` → relu par **diététicien(ne) + chef** (double signature) → `Vérifié (A)`. Chaque ligne conserve `verified_by`, `verified_at`, `source` (Ciqual/Anses, étiquettes, fournisseurs). Une modification d'un ingrédient `A` **repasse** toutes les recettes dépendantes en revue (cf. vue `recipe_diet`, Tome 2 §5).

---

## 2. Viandes & volailles (hors porc)

> Rappel : la viande n'est **jamais** « halal garanti » dans l'app ; c'est un choix d'achat. Origine animale uniquement signalée.

| Nom | Allerg. | Dérivés | Dispo | Notes / zéro déchet |
|---|---|---|---|---|
| Bœuf haché | — | — | 🟢 | Vérifier « pur bœuf » (parfois mélange) |
| Steak / bifteck | — | — | 🟢 | Parures → bouillon, haché |
| Entrecôte | — | — | 🟢 | Gras → à fondre pour cuisson |
| Rumsteck | — | — | 🟢 | |
| Bavette | — | — | 🟢 | |
| Onglet | — | — | 🟢 | |
| Côte de bœuf | — | — | 🟢 | Os → bouillon, fond |
| Rôti de bœuf | — | — | 🟢 | Restes → sandwichs, salade |
| Paleron | — | — | 🟢 | Braisage |
| Joue de bœuf | — | — | 🟡 | Mijotage long |
| Jarret de bœuf | — | — | 🟢 | Os à moelle → bouillon |
| Macreuse / gîte | — | — | 🟢 | Pot-au-feu |
| Queue de bœuf | — | — | 🟡 | |
| Os à moelle | — | — | 🟡 | Moelle → tartines, beurre |
| Langue de bœuf | — | — | 🟡 | |
| Escalope de veau | — | — | 🟢 | |
| Jarret de veau | — | — | 🟢 | Osso buco, os → fond de veau |
| Épaule / tendron de veau | — | — | 🟢 | Blanquette |
| Rôti de veau | — | — | 🟢 | |
| Foie de veau | — | — | 🟡 | |
| Gigot d'agneau | — | — | 🟢 | Os → bouillon, restes → samoussas |
| Épaule d'agneau | — | — | 🟢 | |
| Collier d'agneau | — | — | 🟡 | |
| Côtelettes d'agneau | — | — | 🟢 | |
| Agneau haché | — | — | 🟡 | Kefta |
| Poulet entier | — | — | 🟢 | Carcasse → bouillon ; peau → croustillants ; graisse → cuisson |
| Blanc de poulet | — | — | 🟢 | |
| Cuisse / pilon de poulet | — | — | 🟢 | |
| Ailes de poulet | — | — | 🟢 | Bouts d'ailes → bouillon |
| Foies / gésiers de volaille | — | — | 🟡 | |
| Dinde (escalope, cuisse, filet) | — | — | 🟢 | |
| Canard : magret, cuisse | — | — | 🟢 | Graisse → pommes de terre, confit |
| Canard entier / carcasse | — | — | 🟡 | |
| Pintade | — | — | 🟡 | |
| Caille | — | — | 🟡 | |
| Lapin | — | — | 🟡 | |
| Cerf / biche / chevreuil | — | — | 🟠 | Gibier, saisonnier |
| **Sanglier** | — | **PORC?** (suidé) | 🟠 | ⚠️ **Assimilé porc** pour les régimes sans porc |
| Chèvre / cabri | — | — | 🟠 | Fêtes maghrébines |

---

## 3. Porc, charcuterie et alternatives sans porc

> **Règle** : la ligne « Dérivés = PORC » exclut l'ingrédient pour tout profil « sans porc ». Les lignes **✅ alt.** sont les substituts recommandés (cf. Tome 1 §7.5).

### 3.1 Porc et charcuteries à base de porc

| Nom | Allerg. | Dérivés | Dispo | Notes |
|---|---|---|---|---|
| Poitrine de porc (fraîche) | — | PORC | 🟢 | |
| Échine / palette de porc | — | PORC | 🟢 | |
| Filet mignon de porc | — | PORC | 🟢 | ⚠️ « Filet mignon » existe aussi en **veau** : nommer l'animal |
| Côte / rôti de porc | — | PORC | 🟢 | |
| Jarret de porc | — | PORC | 🟢 | ⚠️ « jarret » existe aussi en bœuf/veau |
| Travers de porc (ribs) | — | PORC | 🟢 | |
| Pied de porc, queue, oreille | — | PORC | 🟠 | |
| Couenne | — | PORC | 🟠 | |
| Lardons | — | PORC | 🟢 | Existent aussi en dinde/bœuf (voir ✅) |
| Poitrine fumée / lard fumé | — | PORC | 🟢 | |
| Bacon | — | PORC | 🟢 | |
| Lard gras / lardo | — | PORC | 🟡 | |
| Jambon blanc | — | PORC | 🟢 | |
| Jambon cru (Bayonne, Parme, serrano) | — | PORC | 🟢 | |
| Jambon de pays / à l'os | — | PORC | 🟢 | |
| Jambonneau | — | PORC | 🟡 | |
| Coppa / capocollo | — | PORC | 🟡 | |
| Pancetta | — | PORC | 🟡 | |
| Guanciale | — | PORC | 🟠 | |
| Speck | — | PORC | 🟡 | |
| Mortadelle | FC? | PORC | 🟡 | Pistaches (FC) possibles |
| Salami / saucisson sec | — | PORC | 🟢 | Alcool possible (vin, eau-de-vie) : **ALC~?** |
| Rosette, jésus | — | PORC | 🟢 | |
| Chorizo (sec/frais) | — | PORC | 🟢 | Origine porc par défaut |
| Pepperoni | — | PORC? | 🟢 | Peut contenir du bœuf |
| Saucisse de Toulouse | — | PORC | 🟢 | |
| Chipolatas | — | PORC | 🟢 | |
| Saucisse de Strasbourg / Francfort | — | PORC? | 🟢 | Souvent porc, parfois volaille |
| Knack / saucisse cocktail | GL?, LA? | PORC? | 🟢 | |
| Andouille / andouillette | — | PORC | 🟡 | |
| Boudin noir | — | PORC | 🟡 | Sang de porc |
| Boudin blanc | LA, GL?, OE? | PORC? | 🟡 | |
| Pâté de campagne / terrine | GL?, SU?, ALC~? | PORC | 🟢 | Alcool fréquent (cognac, porto) |
| Rillettes de porc | — | PORC | 🟢 | |
| Fromage de tête | — | PORC | 🟠 | |
| Saucisse sèche / cervelas | — | PORC? | 🟢 | |
| Saindoux | — | PORC | 🟡 | |
| Gélatine alimentaire | — | **PORC?**, ANIM | 🟢 | Origine à préciser (bœuf, porc, poisson) |
| Os / couenne de jambon (bouillon) | — | PORC | 🟡 | |
| Graisse de porc ibérique | — | PORC | 🟠 | |

### 3.2 ✅ Alternatives sans porc

| Nom | Allerg. | Dérivés | Dispo | Remplace / notes |
|---|---|---|---|---|
| ✅ Lardons de dinde / de volaille fumés | — | — | 🟢 | Lardons de porc |
| ✅ Poitrine de dinde fumée | — | — | 🟢 | Lard, bacon, pancetta |
| ✅ Bacon de dinde / de bœuf | — | — | 🟡 | Bacon |
| ✅ Jambon de dinde / de poulet | — | — | 🟢 | Jambon blanc |
| ✅ Viande des Grisons / bresaola | — | — | 🟡 | Jambon cru (vérifier ingrédients) |
| ✅ Magret de canard séché / fumé | — | — | 🟡 | Guanciale, jambon cru |
| ✅ Merguez (agneau/bœuf) | — | PORC? vérifier | 🟢 | Saucisses grillées. Certaines marques mélangent |
| ✅ Saucisse de bœuf / de veau / de volaille | — | — | 🟢 | Saucisse, chipolata |
| ✅ Chorizo de bœuf ou de volaille | — | — | 🟡 | Chorizo |
| ✅ Pastrami / bœuf fumé | — | — | 🟡 | Charcuterie sandwich |
| ✅ Rillettes de poulet / thon / saumon | PO? | — | 🟢 | Rillettes de porc |
| ✅ Terrine de volaille / gibier | GL?, ALC~? | — | 🟡 | Pâté de campagne |
| ✅ Pâté de foie de volaille | ALC~? | — | 🟡 | |
| ✅ Gélatine de bœuf / poisson, agar-agar, pectine | — | ANIM (gél.) / — | 🟡 | Gélatine porcine |
| ✅ Graisse de canard / beurre clarifié | LA (ghee: traces) | ANIM | 🟢 | Saindoux |
| ✅ Paprika fumé + huile | — | — | 🟢 | Rend le goût fumé |
| ✅ Champignons fumés / tempeh fumé | SO | — | 🟡 | Version végétarienne des lardons |

---

## 4. Poissons, crustacés & fruits de mer

| Nom | Allerg. | Dérivés | Dispo | Notes / zéro déchet |
|---|---|---|---|---|
| Saumon (frais, pavé) | PO | — | 🟢 | Arêtes/peau → bouillon, chips |
| Saumon fumé | PO, SU? | ALC~? | 🟢 | |
| Cabillaud / morue fraîche | PO | — | 🟢 | |
| Morue salée (dessalage 24-48 h) | PO | — | 🟡 | |
| Colin, lieu noir, merlu | PO | — | 🟢 | |
| Haddock fumé | PO | — | 🟢 | |
| Églefin | PO | — | 🟡 | |
| Thon (frais) | PO | — | 🟡 | |
| Thon en conserve | PO | — | 🟢 | |
| Sardine (fraîche / conserve) | PO | — | 🟢 | |
| Maquereau | PO | — | 🟢 | |
| Hareng | PO | — | 🟢 | |
| Anchois (filets, conserve) | PO | — | 🟢 | Huile → vinaigrette |
| Truite | PO | — | 🟢 | |
| Bar / loup | PO | — | 🟡 | |
| Dorade | PO | — | 🟡 | |
| Sole, limande | PO | — | 🟡 | |
| Raie | PO | — | 🟠 | |
| Lotte | PO | — | 🟡 | Os → fumet |
| Tarama / œufs de poisson | PO | — | 🟢 | Peut contenir GL? |
| Œufs de truite / saumon | PO | — | 🟡 | |
| Surimi | PO, CR?, GL, OE? | — | 🟢 | Additifs fréquents (à éviter dans notre charte) |
| Crevettes (cuites/crues) | CR | — | 🟢 | Carapaces → bisque/huile |
| Gambas / bouquet | CR | — | 🟡 | |
| Langoustines | CR | — | 🟡 | |
| Homard | CR | — | 🟠 | |
| Crabe / tourteau | CR | — | 🟡 | |
| Écrevisses | CR | — | 🟠 | |
| Moules | MM | — | 🟢 | Vin blanc fréquent → substitution (Tome 1 §7.5) |
| Huîtres | MM | — | 🟡 | |
| Coquilles Saint-Jacques | MM | — | 🟡 | Corail |
| Palourdes / coques | MM | — | 🟡 | |
| Bulots / bigorneaux | MM | — | 🟡 | |
| Calamar / encornet | MM | — | 🟡 | |
| Poulpe / seiche | MM | — | 🟡 | |
| Escargots | MM | — | 🟡 | |
| Fumet / bouillon de poisson | PO, CE? | — | 🟡 | À faire avec arêtes (zéro déchet) |

---

## 5. Œufs & produits laitiers (et alternatives)

| Nom | Allerg. | Dérivés | Dispo | Notes / zéro déchet |
|---|---|---|---|---|
| Œuf entier (frais) | OE | ANIM | 🟢 | Coquilles → jardin ; calibre M ≈ 53-63 g |
| Jaune d'œuf | OE | ANIM | 🟢 | Mayo, crèmes |
| Blanc d'œuf | OE | ANIM | 🟢 | Meringues, financiers |
| Œuf pasteurisé (liquide) | OE | ANIM | 🟡 | Sauces sans risque cru |
| Lait entier / demi-écrémé / écrémé | LA | ANIM | 🟢 | Lait tourné → pancakes |
| Lait en poudre | LA | ANIM | 🟢 | |
| Lait ribot / lait fermenté | LA | ANIM | 🟡 | |
| Babeurre | LA | ANIM | 🟡 | Substitut : lait + citron |
| Lait concentré sucré / non sucré | LA | ANIM | 🟢 | |
| Crème fleurette (liquide) | LA | ANIM | 🟢 | 30-35 % MG |
| Crème épaisse | LA | ANIM | 🟢 | |
| Crème fraîche | LA | ANIM | 🟢 | |
| Beurre doux / demi-sel | LA | ANIM | 🟢 | |
| Beurre clarifié / ghee | LA (traces) | ANIM | 🟡 | |
| Yaourt nature | LA | ANIM | 🟢 | |
| Yaourt grec | LA | ANIM | 🟢 | |
| Skyr | LA | ANIM | 🟡 | |
| Fromage blanc / faisselle | LA | ANIM? | 🟢 | |
| Petit-suisse | LA | ANIM? | 🟢 | |
| Mascarpone | LA | ANIM | 🟢 | |
| Ricotta | LA | ANIM? | 🟢 | |
| Mozzarella / burrata | LA | ANIM? | 🟢 | |
| Parmesan / Parmigiano | LA | ANIM (présure) | 🟢 | Croûte → bouillons |
| Pecorino | LA | ANIM (présure) | 🟡 | |
| Gruyère / comté / emmental / beaufort | LA | ANIM? (présure) | 🟢 | |
| Cheddar | LA | ANIM? | 🟢 | |
| Feta | LA | ANIM? | 🟢 | |
| Halloumi | LA | ANIM? | 🟡 | |
| Chèvre (frais, bûche) | LA | ANIM? | 🟢 | |
| Camembert / brie | LA | ANIM? | 🟢 | Croûte comestible |
| Roquefort / bleu | LA | ANIM? | 🟢 | |
| Reblochon / raclette / mont-d'or | LA | ANIM? | 🟢 | |
| Cantal / saint-nectaire / tomme | LA | ANIM? | 🟢 | |
| Fromage à tartiner / fondu | LA | ANIM? | 🟢 | Additifs fréquents |
| Cottage cheese | LA | ANIM? | 🟡 | |
| Paneer | LA | ANIM? | 🟠 | Recette maison simple |
| Labneh | LA | ANIM? | 🟠 | Yaourt égoutté |
| Kéfir de lait | LA | ALC~ | 🟡 | Fermentation |
| Lait de coco / crème de coco | — | — | 🟢 | `watch: noix de coco` |
| Lait d'avoine | GL | — | 🟢 | |
| Lait d'amande | FC | — | 🟢 | |
| Lait de soja | SO | — | 🟢 | |
| Lait de riz | — | — | 🟢 | |
| Lait de noisette | FC | — | 🟡 | |
| Aquafaba (eau de pois chiches) | — | — | 🟢 | Remplace le blanc d'œuf — **zéro déchet** |
| Crème de soja / avoine | SO / GL | — | 🟢 | |
| Œuf végétal (prêt à l'emploi) | variable | — | 🟡 | À lire sur étiquette |

> **Présure** : `ANIM?` signale que la présure peut être animale (veau, voire porc dans de rares cas) ou microbienne. Mode **Végétarien / Halal / Casher** : exiger mention « présure microbienne/végétale » ou classer « à vérifier ».

---

## 6. Légumes, champignons & algues

| Nom | Allerg. | Dérivés | Dispo | Notes / zéro déchet |
|---|---|---|---|---|
| Oignon jaune | — | — | 🟢 | Pelures → bouillon |
| Oignon rouge | — | — | 🟢 | |
| Échalote | — | — | 🟢 | |
| Ail | — | — | 🟢 | Germes enlevés ; peaux → bouillon |
| Oignon nouveau / cébette | — | — | 🟢 | Vert → ciboulette |
| Poireau | — | — | 🟢 | Vert → bouillon/soupe/chips |
| Carotte | — | — | 🟢 | Fanes → pesto |
| Navet / navet boule d'or | — | — | 🟢 | Fanes comestibles |
| Radis rose | — | — | 🟢 | Fanes → soupe/pesto |
| Radis noir / daikon | — | — | 🟡 | |
| Betterave (crue/cuite) | — | — | 🟢 | Fanes → comme épinard |
| Céleri-rave | CE | — | 🟢 | Épluchures → bouillon |
| Céleri-branche | CE | — | 🟢 | Feuilles → herbes |
| Fenouil | — | — | 🟢 | Fanes → aromates |
| Panais / rutabaga | — | — | 🟢 | |
| Topinambour | — | — | 🟡 | |
| Pomme de terre | — | — | 🟢 | Épluchures → chips au four |
| Patate douce | — | — | 🟢 | |
| Manioc / yuca | — | — | 🟠 | ⚠️ ne jamais consommer cru ; cuisson obligatoire |
| Igname | — | — | 🟠 | |
| Taro / madère | — | — | 🟠 | |
| Plantain (banane à cuire) | — | — | 🟡 | |
| Butternut / courge musquée | — | — | 🟢 | Graines → grillées |
| Potimarron | — | — | 🟢 | Peau comestible |
| Potiron / citrouille | — | — | 🟢 | |
| Courgette | — | — | 🟢 | |
| Aubergine | — | — | 🟢 | |
| Poivron (rouge/jaune/vert) | — | — | 🟢 | |
| Piment frais (divers) | — | — | 🟢 | Gants conseillés |
| Piment antillais / scotch bonnet | — | — | 🟠 | Très fort |
| Tomate | — | — | 🟢 | Peaux → poudre de tomate |
| Tomate cerise | — | — | 🟢 | `watch: étouffement <4 ans` |
| Concombre | — | — | 🟢 | |
| Cornichon | MO?, SU? | ALC~? | 🟢 | Vinaigre de vin parfois |
| Champignon de Paris | — | — | 🟢 | Pieds → bouillon |
| Shiitake | — | — | 🟡 | Pieds → bouillon umami |
| Pleurote | — | — | 🟡 | |
| Cèpe / girolle / morille | — | — | 🟠 | ⚠️ morille crue toxique ; cueillette = pharmacien/mycologue |
| Champignon noir séché | — | — | 🟠 | |
| Chou blanc / rouge | — | — | 🟢 | Trognon → bouillon, râpé |
| Chou vert / frisé / kale | — | — | 🟢 | |
| Chou de Bruxelles | — | — | 🟢 | |
| Chou-fleur | — | — | 🟢 | Tiges et feuilles comestibles |
| Brocoli | — | — | 🟢 | Tiges → râpées/soupe |
| Chou chinois / pak-choï | — | — | 🟡 | |
| Épinard | — | — | 🟢 | |
| Blette / bette | — | — | 🟢 | Côtes → gratin |
| Salade (laitue, batavia) | — | — | 🟢 | |
| Roquette / mâche | — | — | 🟢 | |
| Endive | — | — | 🟢 | |
| Chicorée / frisée | — | — | 🟢 | |
| Cresson | — | — | 🟢 | |
| Oseille | — | — | 🟡 | |
| Artichaut | — | — | 🟢 | Feuilles/fonds ; tiges |
| Asperge | — | — | 🟢 | Talons → bouillon |
| Haricots verts | — | — | 🟢 | |
| Petits pois / pois gourmands | — | — | 🟢 | Cosses → bouillon |
| Fèves fraîches | — | — | 🟡 | Cosses → soupe |
| Maïs doux | — | — | 🟢 | Rafles → bouillon |
| Gombo (okra) | — | — | 🟠 | |
| Avocat | — | — | 🟢 | `watch: latex-fruit` |
| Olives (vertes / noires) | — | — | 🟢 | Saumure → déglaçage ; `SU?` selon marque |
| Câpres | — | — | 🟢 | |
| Salsifis / cardon | — | — | 🟠 | |
| Pousses de bambou | — | — | 🟠 | Conserve |
| Germes de soja | SO | — | 🟡 | |
| Edamame | SO | — | 🟡 | |
| Gingembre frais | — | — | 🟢 | Peau → tisane |
| Curcuma frais | — | — | 🟡 | |
| Galanga | — | — | 🟠 | |
| Citronnelle | — | — | 🟡 | |
| Chayotte / christophine | — | — | 🟠 | |
| Tomatille / nopal | — | — | 🔴 | → substituts §16 |
| Algue nori | — | — | 🟡 | |
| Algue wakame / kombu | — | — | 🟠 | Dashi |
| Laitue de mer, dulse | — | — | 🟠 | |

---

## 7. Fruits (frais, secs, agrumes)

| Nom | Allerg. | Dérivés | Dispo | Notes / zéro déchet |
|---|---|---|---|---|
| Pomme | — | — | 🟢 | Épluchures → infusion/gelée |
| Poire | — | — | 🟢 | |
| Coing | — | — | 🟡 | Pâte de coing |
| Citron | — | — | 🟢 | Zeste, peau → confite, vinaigre ménager |
| Citron vert | — | — | 🟢 | |
| Orange | — | — | 🟢 | Zeste → sucre aromatisé |
| Pamplemousse | — | — | 🟢 | |
| Mandarine / clémentine | — | — | 🟢 | |
| Yuzu | — | — | 🔴 | → substitut : citron + mandarine |
| Fraise | — | — | 🟢 | Queues → infusion |
| Framboise / mûre / myrtille | — | — | 🟢 | |
| Cassis / groseille | — | — | 🟡 | |
| Cerise / griotte | — | — | 🟢 | Noyaux → bouillottes, infusion |
| Abricot | — | — | 🟢 | Amande du noyau : **toxique en excès** → ne pas utiliser |
| Pêche / nectarine | — | — | 🟢 | |
| Prune / mirabelle / reine-claude | — | — | 🟢 | |
| Figue (fraîche) | — | — | 🟢 | |
| Raisin | — | — | 🟢 | `watch: étouffement <4 ans` |
| Melon / pastèque | — | — | 🟢 | Écorce de pastèque → pickles |
| Banane | — | — | 🟢 | Peau → pickles asiatiques, engrais |
| Ananas | — | — | 🟢 | Peau/cœur → boisson, infusion |
| Mangue | — | — | 🟢 | `watch: latex` |
| Papaye | — | — | 🟡 | |
| Fruit de la passion | — | — | 🟡 | |
| Goyave / litchi | — | — | 🟡 | |
| Grenade | — | — | 🟡 | Peau séchée → infusion |
| Kiwi | — | — | 🟢 | `watch: allergie fréquente` |
| Datte (medjool, deglet) | SU? | — | 🟡 | |
| Rhubarbe | — | — | 🟢 | ⚠️ **feuilles toxiques** |
| Noix de coco fraîche | — | — | 🟡 | `watch: coco` |
| Tamarin (pulpe) | — | — | 🟠 | |
| Kaki | — | — | 🟡 | |
| Physalis | — | — | 🟡 | |
| Abricots secs | SU | — | 🟢 | Sulfités en général |
| Raisins secs | SU? | — | 🟢 | Sultanines/corinthe |
| Pruneaux | — | — | 🟢 | |
| Figues sèches | SU? | — | 🟢 | |
| Canneberges séchées | SU? | — | 🟡 | |
| Bananes séchées | — | — | 🟡 | |
| Fruits confits | SU? | — | 🟢 | |
| Compote sans sucre ajouté | — | — | 🟢 | |
| Jus de pomme / raisin / orange (pur jus) | SU? | — | 🟢 | Jus de raisin = base sans alcool pour substitutions |
| Verjus | SU? | — | 🟠 | Substitut du vin blanc |


---

## 8. Légumineuses, céréales & féculents

| Nom | Allerg. | Dérivés | Dispo | Notes |
|---|---|---|---|---|
| Lentilles vertes / brunes | — | — | 🟢 | Eau de cuisson → soupe |
| Lentilles corail | — | — | 🟢 | |
| Lentilles noires (beluga) | — | — | 🟡 | |
| Pois chiches (secs / bocal) | — | — | 🟢 | Eau → **aquafaba** |
| Haricots blancs / lingots | — | — | 🟢 | ⚠️ Haricots rouges crus = toxiques : cuisson longue obligatoire |
| Haricots rouges / noirs | — | — | 🟢 | |
| Flageolets | — | — | 🟢 | |
| Pois cassés | — | — | 🟢 | |
| Fèves sèches | — | — | 🟡 | |
| Haricots mungo / azuki | — | — | 🟠 | |
| Graines de lupin (saumure) | LU | — | 🟠 | |
| Soja jaune (graines) | SO | — | 🟠 | |
| Riz long / basmati / thaï | — | — | 🟢 | `watch: arsenic` (rincer, varier) |
| Riz rond / sushi | — | — | 🟢 | |
| Riz à risotto (arborio, carnaroli) | — | — | 🟢 | |
| Riz complet | — | — | 🟢 | |
| Riz gluant | — | — | 🟡 | |
| Riz sauvage | — | — | 🟡 | |
| Quinoa | — | — | 🟢 | Rincer (saponines) |
| Boulgour | GL | — | 🟢 | |
| Semoule de blé (fine/moyenne) | GL | — | 🟢 | Couscous |
| Couscous perlé (moghrabieh) | GL | — | 🟠 | |
| Freekeh | GL | — | 🟠 | |
| Épeautre | GL | — | 🟢 | |
| Orge perlé | GL | — | 🟢 | |
| Avoine (flocons) | GL | — | 🟢 | Gluten **inclus** dans la liste UE |
| Sarrasin (grain, farine) | — | — | 🟢 | `watch: allergie sarrasin` ; contamination GL possible |
| Millet / sorgho | — | — | 🟡 | |
| Fonio | — | — | 🟠 | |
| Teff | — | — | 🟠 | |
| Amarante | — | — | 🟡 | |
| Polenta / semoule de maïs | — | — | 🟢 | |
| Maïs à popcorn | — | — | 🟢 | `watch: étouffement <4 ans` |
| Tapioca (perles) | — | — | 🟡 | |
| Seitan | GL | — | 🟡 | |
| Tofu (ferme / soyeux) | SO | — | 🟢 | |
| Tempeh | SO | — | 🟡 | |
| Protéines de soja texturées | SO | — | 🟡 | |
| Flocons d'avoine (porridge) | GL | — | 🟢 | |
| Pain rassis (réservé) | GL?, LA?, OE? | — | — | **Zéro déchet** : chapelure, croûtons, pain perdu |

---

## 9. Farines, pains, pâtes & pâtes de base

### 9.1 Farines et agents de levée

| Nom | Allerg. | Dérivés | Dispo | Notes |
|---|---|---|---|---|
| Farine de blé T45 | GL | — | 🟢 | Pâtisserie, crêpes |
| Farine de blé T55 | GL | — | 🟢 | Usage courant, pizza |
| Farine de blé T65 (tradition) | GL | — | 🟢 | Baguette |
| Farine de blé T80 (semi-complète) | GL | — | 🟡 | |
| Farine T110 / T150 (complète) | GL | — | 🟡 | |
| Farine de seigle | GL | — | 🟡 | |
| Farine d'épeautre | GL | — | 🟡 | |
| Farine de sarrasin | — | — | 🟢 | Galettes bretonnes |
| Farine de maïs | — | — | 🟡 | |
| Farine de riz / riz gluant | — | — | 🟡 | |
| Farine de pois chiche (besan) | — | — | 🟡 | Socca, pakora |
| Farine de châtaigne | — | — | 🟡 | |
| Farine de coco | — | — | 🟡 | `watch: coco` |
| Farine d'amande / poudre d'amande | FC | — | 🟢 | |
| Farine de manioc | — | — | 🟠 | |
| Farine atta (chapati) | GL | — | 🟠 | |
| Masa harina | — | — | 🔴 | → substitut §16 |
| Gluten vital | GL | — | 🟡 | |
| Fécule de maïs (maïzena) | — | — | 🟢 | |
| Fécule de pomme de terre | — | — | 🟢 | |
| Arrow-root / agar-agar | — | — | 🟡 | Agar : végétal |
| Levure boulangère sèche | — | — | 🟢 | **Fraîche ≈ 3× la sèche** |
| Levure boulangère fraîche | — | — | 🟢 | |
| Levure chimique | GL? | — | 🟢 | Amidon de blé possible |
| Bicarbonate de soude | — | — | 🟢 | |
| Levain (maison) | GL | — | — | |
| Malt d'orge (poudre) | GL | — | 🟠 | |
| Améliorants (ascorbique…) | — | — | — | **Hors charte** |

### 9.2 Pains et pâtes de base

| Nom | Allerg. | Dérivés | Dispo | Notes |
|---|---|---|---|---|
| Baguette tradition | GL | — | 🟢 | Rassie → chapelure |
| Pain de campagne / complet | GL | — | 🟢 | |
| Pain de mie | GL, LA?, OE? | — | 🟢 | Additifs fréquents |
| Brioche | GL, LA, OE | — | 🟢 | |
| Pain pita / libanais | GL | — | 🟢 | |
| Naan | GL, LA?, OE? | — | 🟡 | |
| Tortillas de blé | GL | — | 🟢 | |
| Tortillas de maïs | — | — | 🟡 | |
| Lavash / pain azyme | GL | — | 🟠 | |
| Pâte feuilletée (prête) | GL, LA? | ANIM? (graisse) | 🟢 | Margarine/palme parfois ; **pur beurre** à privilégier |
| Pâte brisée / sablée (prête) | GL, LA? | — | 🟢 | |
| Pâte filo / feuilles de brick | GL | — | 🟡 | |
| Pâte à pizza (prête) | GL | — | 🟢 | |
| Galettes de riz (rice paper) | — | — | 🟡 | |
| Chapelure | GL | — | 🟢 | |
| Panko | GL | — | 🟡 | |
| Biscottes | GL | — | 🟢 | |
| Biscuits (spéculoos, sablés) | GL, LA?, OE?, FC? | — | 🟢 | |
| Boudoirs / biscuits cuillère | GL, OE | — | 🟢 | |
| Pâtes sèches (spaghetti, penne…) | GL | — | 🟢 | Eau de cuisson amidonnée → sauce |
| Pâtes fraîches aux œufs | GL, OE | — | 🟢 | |
| Gnocchi | GL, OE?, LA? | — | 🟢 | |
| Lasagnes | GL, OE? | — | 🟢 | |
| Pâtes sans gluten | — | — | 🟡 | Riz/maïs/légumineuses |
| Nouilles de riz / vermicelles | — | — | 🟡 | |
| Vermicelles de haricots mungo | — | — | 🟠 | |
| Nouilles udon | GL | — | 🟡 | |
| Nouilles soba | GL?, — | — | 🟡 | Vérifier % de sarrasin |
| Nouilles ramen | GL, OE? | — | 🟡 | |
| Nouilles chinoises aux œufs | GL, OE | — | 🟡 | |
| Pâte à gyoza / wonton | GL | — | 🟠 | |

---

## 10. Herbes & aromates

| Nom | Allerg. | Dérivés | Dispo | Notes / zéro déchet |
|---|---|---|---|---|
| Persil plat / frisé | — | — | 🟢 | Tiges → bouillons, pesto |
| Coriandre fraîche | — | — | 🟢 | Racines → pâtes thaïes |
| Menthe | — | — | 🟢 | Tiges → infusion |
| Basilic | — | — | 🟢 | |
| Thym / romarin | — | — | 🟢 | Tiges → grillades |
| Laurier | — | — | 🟢 | |
| Sarriette / marjolaine | — | — | 🟡 | |
| Origan frais / sec | — | — | 🟢 | |
| Sauge | — | — | 🟢 | |
| Estragon | — | — | 🟢 | |
| Cerfeuil | — | — | 🟡 | |
| Ciboulette | — | — | 🟢 | |
| Aneth | — | — | 🟢 | |
| Livèche | CE | — | 🟠 | |
| Basilic thaï | — | — | 🟠 | |
| Feuille de curry | — | — | 🟠 | |
| Feuille de combava (kaffir) | — | — | 🟠 | |
| Shiso | — | — | 🔴 | → basilic + menthe |
| Feuille de bananier | — | — | 🟠 | Papillote |
| Feuilles de vigne (bocal) | SU? | — | 🟡 | |
| Verveine / mélisse | — | — | 🟡 | Infusions |
| Fleurs comestibles (capucine…) | — | — | 🟠 | |

---

## 11. Épices, sels & mélanges

> Les mélanges du commerce portent `?` (anti-agglomérants, sel, céleri, moutarde, gluten). **Recettes maison** privilégiées : charte « sans additifs » (Tome 1 §11.1).

| Nom | Allerg. | Dérivés | Dispo | Notes |
|---|---|---|---|---|
| Poivre noir / blanc / vert | — | — | 🟢 | Moulu à la minute |
| Poivre du Sichuan | — | — | 🟡 | |
| Baies roses | — | — | 🟡 | `watch: cousine de l'anacarde` |
| Piment d'Espelette | — | — | 🟢 | |
| Cayenne / piment en poudre | — | — | 🟢 | |
| Flocons de piment | — | — | 🟢 | |
| Paprika doux | — | — | 🟢 | |
| Paprika fumé (pimentón) | — | — | 🟢 | Remplace le goût charcutier |
| Cumin (graines / moulu) | — | — | 🟢 | |
| Coriandre (graines) | — | — | 🟢 | |
| Carvi / fenouil / anis vert (graines) | — | — | 🟡 | |
| Anis étoilé (badiane) | — | — | 🟡 | |
| Cannelle (bâton / poudre) | — | — | 🟢 | |
| Cardamome | — | — | 🟡 | |
| Clou de girofle | — | — | 🟢 | |
| Noix de muscade | — | — | 🟢 | ⚠️ toxique à forte dose |
| Macis | — | — | 🟠 | |
| Curcuma (poudre) | — | — | 🟢 | |
| Gingembre (poudre) | — | — | 🟢 | |
| Safran (pistils) | — | — | 🟡 | |
| Vanille (gousse) | — | — | 🟡 | Gousse vide → sucre vanillé |
| Poudre de vanille | — | — | 🟡 | **Substitut de l'extrait alcoolisé** |
| Fenugrec | — | — | 🟡 | |
| Nigelle | — | — | 🟠 | |
| Sésame (blanc/noir) | SE | — | 🟢 | |
| Pavot | — | — | 🟡 | |
| Graines de moutarde | MO | — | 🟡 | |
| Curry (mélange) | MO?, CE?, GL? | — | 🟢 | |
| Garam masala | — | — | 🟡 | |
| Ras el-hanout | — | — | 🟡 | Dosages variables |
| Baharat / tabil | — | — | 🟠 | |
| Zaatar | SE | — | 🟡 | Souvent aussi sumac |
| Sumac | — | — | 🟡 | |
| Dukkah | FC, SE | — | 🟠 | |
| Berbéré | — | — | 🟠 | |
| Cinq-épices chinois | — | — | 🟡 | |
| Shichimi togarashi | SE | — | 🟠 | |
| Mélange cajun | — | — | 🟡 | |
| Mélange tex-mex / fajitas | GL? | — | 🟢 | |
| Herbes de Provence | — | — | 🟢 | |
| Quatre-épices | — | — | 🟢 | |
| Mélange tandoori / tikka | — | — | 🟡 | |
| Piments ancho / chipotle / guajillo / pasilla | — | — | 🟠 | |
| Piment doux (poudre de poivron) | — | — | 🟢 | |
| Amchur (mangue) | — | — | 🔴 | → citron + pincée de sucre |
| Asafoetida | GL? | — | 🟠 | Souvent coupée à la farine |
| Poudre d'ail / d'oignon | — | — | 🟢 | |
| Sel fin / gros sel / fleur de sel | — | — | 🟢 | |
| Sel de céleri | CE | — | 🟡 | |
| Sel fumé | — | — | 🟡 | |
| Sel nitrité (charcuterie maison) | — | — | 🟠 | ⚠️ usage professionnel : **hors périmètre** |
| Baies de genièvre | — | — | 🟡 | Épice, pas alcool |

---

## 12. Condiments, sauces du commerce, bouillons & bases

> Tous ces produits ont un équivalent maison dans le Tome 1 §11. Colonne « Alerte » = risque de **porc / alcool / allergène** selon la marque.

| Nom | Allerg. | Dérivés | Dispo | Notes |
|---|---|---|---|---|
| Moutarde de Dijon | MO, SU? | ALC~? (vin blanc/verjus) | 🟢 | Vérifier vin blanc |
| Moutarde à l'ancienne | MO, SU? | ALC~? | 🟢 | |
| Ketchup | CE?, SU? | — | 🟢 | Additifs fréquents |
| Mayonnaise industrielle | OE, MO, SU? | — | 🟢 | |
| Sauce soja claire | SO, GL | ALC~ | 🟢 | Fermentation |
| Tamari | SO, GL? | ALC~ | 🟡 | |
| Kecap manis | SO, GL? | — | 🟠 | |
| Sauce d'huître | MM, SO?, GL? | — | 🟡 | |
| Sauce de poisson (nuoc-mâm, nam pla) | PO | — | 🟡 | |
| Sauce Worcestershire | PO, GL?, SU? | — | 🟢 | Anchois |
| Tabasco / sauce piquante | — | ALC~? | 🟢 | |
| Sriracha | — | — | 🟡 | |
| Sambal oelek | CR? | — | 🟠 | |
| Harissa (tube/pâte) | — | — | 🟡 | Souvent additifs |
| Pâte de piment | — | — | 🟡 | |
| Gochujang | SO, GL | ALC~ | 🟠 | |
| Doenjang | SO | ALC~ | 🟠 | |
| Miso | SO, GL? | ALC~ | 🟡 | |
| Pâte de curry rouge/verte/jaune | CR?, PO? | — | 🟡 | Pâte de crevettes fréquente |
| Pâte de crevettes | CR | — | 🟠 | |
| Sauce hoisin | SO, SE?, GL? | — | 🟡 | |
| Sauce XO | CR, PO | PORC? (jambon) | 🟠 | Souvent jambon de Jinhua |
| Pâte de haricots noirs fermentés | SO | ALC~ | 🟠 | |
| Sauce ponzu | SO, GL, PO? | ALC~ | 🟠 | |
| Sauce teriyaki | SO, GL | ALC~ (mirin) | 🟡 | |
| Pâte de tamarin | — | — | 🟠 | |
| Concentré de tomate | — | — | 🟢 | |
| Coulis / passata / tomates pelées | — | — | 🟢 | |
| Sauce tomate (bocal) | CE?, SU? | — | 🟢 | |
| Pesto (bocal) | LA, FC (pignons/cajou) | ANIM? (parmesan) | 🟢 | `watch: pignon` |
| Tapenade | PO? (anchois) | — | 🟢 | |
| Houmous | SE | — | 🟢 | |
| Tahini (purée de sésame) | SE | — | 🟡 | |
| Baba ghanoush / caviar d'aubergine | SE? | — | 🟡 | |
| Tzatziki | LA | ANIM? | 🟢 | |
| Guacamole du commerce | — | — | 🟢 | Additifs |
| Salsa du commerce | SU? | ALC~? | 🟢 | |
| Vinaigre blanc | — | — | 🟢 | |
| Vinaigre de cidre | — | — | 🟢 | Sans alcool (acide acétique) |
| Vinaigre de vin rouge / blanc | SU | ALC~ | 🟢 | |
| Vinaigre balsamique | SU | ALC~ | 🟢 | |
| Vinaigre de xérès | SU | ALC~ | 🟡 | |
| Vinaigre de riz | — | ALC~ | 🟡 | |
| Vinaigre de malt | GL | — | 🟡 | |
| Vinaigre noir chinois (Chinkiang) | GL | ALC~ | 🟠 | |
| Jus de citron (bouteille) | SU? | — | 🟢 | Frais à privilégier |
| Miel | — | ANIM | 🟢 | ⚠️ **interdit < 12 mois** |
| Sirop d'agave / d'érable | — | — | 🟢 | Végétal |
| Confiture / gelée | SU? | — | 🟢 | |
| Chutney (commerce) | MO?, SU?, CE? | ALC~? | 🟡 | |
| Cornichons, oignons au vinaigre | MO?, SU? | ALC~? | 🟢 | |
| Bouillon cube volaille | CE, GL?, OE?, SO? | PORC?, ANIM | 🟢 | Graisse parfois porcine ; **à remplacer par maison** |
| Bouillon cube bœuf | CE, GL? | PORC? | 🟢 | |
| Bouillon cube légumes | CE | — | 🟢 | Exhausteurs fréquents |
| Bouillon liquide (type fond) | CE, GL, SO | PORC? | 🟢 | |
| Fond de veau / de volaille (poudre) | CE, GL? | PORC? | 🟢 | |
| Dashi (instantané) | PO, SO?, GL? | ALC~? | 🟠 | Katsuobushi = poisson |
| Dashi maison (kombu + katsuobushi) | PO | — | 🟠 | |
| Bouillon d'os maison (bœuf/volaille) | CE? | — | — | **Zéro déchet** |
| Fumet de poisson maison | PO | — | — | Arêtes |
| Fumée liquide | — | — | 🟡 | Additif : hors charte |


---

## 13. Huiles, graisses, sucrants, chocolat, fruits à coque & graines

### 13.1 Huiles et graisses

| Nom | Allerg. | Dérivés | Dispo | Notes |
|---|---|---|---|---|
| Huile d'olive vierge extra | — | — | 🟢 | |
| Huile de tournesol / colza | — | — | 🟢 | Friture : filtrer, réutiliser |
| Huile d'arachide | AR | — | 🟢 | Raffinée : risque faible mais **à signaler** |
| Huile de sésame (grillée) | SE | — | 🟡 | |
| Huile de noix / de noisette | FC | — | 🟡 | |
| Huile de coco | — | — | 🟢 | `watch: coco` |
| Huile de pépins de raisin / maïs | — | — | 🟢 | |
| Huile de palme rouge | — | — | 🟠 | Cuisine africaine ; enjeu environnemental |
| Huile d'argan alimentaire | FC? | — | 🟠 | `watch: argan` |
| Huile pimentée maison | — | — | — | Conservation courte (botulisme) |
| Beurre de cacahuète | AR | — | 🟢 | |
| Beurre d'amande / noisette | FC | — | 🟡 | |
| Graisse de canard | — | ANIM | 🟢 | Substitut du saindoux |
| Graisse de bœuf / suif | — | ANIM | 🟠 | |
| Saindoux | — | PORC | 🟡 | cf. §3 |
| Margarine | LA? | — | 🟢 | Additifs possibles |
| Smen (beurre fermenté) | LA | ANIM | 🟠 | Substitut : beurre clarifié + pincée de fromage fort |

### 13.2 Sucrants, chocolat, bases sucrées

| Nom | Allerg. | Dérivés | Dispo | Notes |
|---|---|---|---|---|
| Sucre blanc / roux / cassonade / vergeoise | — | — | 🟢 | |
| Sucre glace | — | — | 🟢 | Amidon (maïs) parfois |
| Sucre muscovado | — | — | 🟡 | |
| Sucre de coco | — | — | 🟡 | |
| Sucre vanillé | — | — | 🟢 | Alternative maison : gousse + sucre |
| Mélasse / sirop de canne | SU? | — | 🟡 | |
| Mélasse de grenade | — | — | 🟠 | |
| Sirop de datte | — | — | 🟡 | |
| Jaggery | — | — | 🟠 | |
| Sirop de glucose | — | — | 🟡 | |
| Chocolat noir | SO?, LA? | — | 🟢 | Lécithine de soja ; traces de lait |
| Chocolat au lait | LA, SO? | — | 🟢 | |
| Chocolat blanc | LA, SO? | — | 🟢 | |
| Cacao en poudre non sucré | — | — | 🟢 | |
| Pépites de chocolat | LA?, SO? | — | 🟢 | |
| Pâte à tartiner chocolat-noisette | FC, LA | — | 🟢 | |
| Praliné / pâte de noisette | FC | — | 🟡 | |
| Pâte d'amande / massepain | FC | — | 🟢 | |
| Nougat | FC, OE? | — | 🟢 | |
| Dulce de leche | LA | — | 🟡 | |
| Fève tonka | — | — | 🟠 | ⚠️ coumarine : usage limité |
| Caramel (sucre + eau) | — | — | — | Maison, **sans E150** |

### 13.3 Fruits à coque, graines

> **Pignon de pin** : non listé parmi les 14 allergènes UE mais allergène réel (`watch`). **Châtaigne** et **noix de coco** : non listées UE (`watch`).

| Nom | Allerg. | Dérivés | Dispo | Notes |
|---|---|---|---|---|
| Amande (entière, effilée, poudre) | FC | — | 🟢 | |
| Noisette | FC | — | 🟢 | |
| Noix | FC | — | 🟢 | Coques → allume-feu / compost |
| Noix de cajou | FC | — | 🟢 | |
| Pistache | FC | — | 🟡 | |
| Noix de pécan | FC | — | 🟡 | |
| Noix de macadamia | FC | — | 🟡 | |
| Noix du Brésil | FC | — | 🟡 | |
| Pignons de pin | — | — | 🟢 | `watch: pignon` |
| Châtaigne (fraîche, crème, purée) | — | — | 🟢 | `watch: châtaigne` |
| Cacahuète / arachide | AR | — | 🟢 | Légumineuse ; allergène majeur |
| Graines de tournesol / courge | — | — | 🟢 | |
| Graines de lin / chia / chanvre | — | — | 🟡 | Lin : gel liant (substitut œuf) |
| Noix de coco râpée | — | — | 🟢 | `watch: coco` |
| Cacao nibs | — | — | 🟡 | |

---

## 14. Alcools, arômes & dérivés alcoolisés (cuisine)

> **Rappel** : tout profil « sans alcool » exclut `ALC`. `ALC~` est exclu en **mode Strict**. Chaque ligne indique le **substitut sans alcool** (testé : cf. Tome 1 §7.5 — statut « testé » à confirmer au cas par cas).

| Nom | Allerg. | Dérivés | Dispo | Substitut sans alcool |
|---|---|---|---|---|
| Vin rouge | SU | **ALC** | 🟢 | Jus de raisin rouge + vinaigre de vin (ou balsamique) |
| Vin blanc | SU | **ALC** | 🟢 | Bouillon + jus de citron ; verjus |
| Vin rosé | SU | **ALC** | 🟢 | Jus de raisin + citron |
| Vin moelleux / liquoreux | SU | **ALC** | 🟡 | Jus de raisin blanc réduit + miel |
| Champagne / crémant / mousseux | SU | **ALC** | 🟢 | Jus de pomme pétillant / eau gazeuse citronnée |
| Porto | SU | **ALC** | 🟡 | Jus de raisin réduit + balsamique |
| Madère / marsala / xérès | SU | **ALC** | 🟡 | Jus de raisin réduit + balsamique |
| Vermouth | SU | **ALC** | 🟡 | Bouillon + citron + herbes |
| Bière (blonde, brune, blanche) | GL | **ALC** | 🟢 | Bouillon + balsamique ; bière 0,0 % (ALC~) |
| Cidre | — | **ALC** | 🟢 | Jus de pomme + trait de vinaigre de cidre |
| Poiré | — | **ALC** | 🟡 | Jus de poire |
| Calvados | — | **ALC** | 🟢 | Jus de pomme réduit + vinaigre de cidre |
| Cognac / armagnac / brandy | — | **ALC** | 🟢 | Jus de pomme/raisin réduit + vanille |
| Rhum ambré / blanc | — | **ALC** | 🟢 | Sirop + zeste d'orange + vanille ; thé fumé |
| Whisky / bourbon | GL? | **ALC** | 🟢 | Thé fumé + sirop d'érable |
| Vodka | — | **ALC** | 🟢 | Eau + citron (pâtes, sauces) |
| Gin / genièvre | — | **ALC** | 🟢 | Eau de genièvre / infusion de baies |
| Tequila | — | **ALC** | 🟡 | Jus de citron vert + eau |
| Kirsch / eaux-de-vie de fruits | — | **ALC** | 🟢 | Jus de cerise réduit |
| Grand Marnier / Cointreau / triple sec | — | **ALC** | 🟢 | Jus d'orange réduit + zestes |
| Amaretto | FC? | **ALC** | 🟡 | Sirop + arôme d'amande sans alcool |
| Limoncello | — | **ALC** | 🟡 | Jus de citron + zeste + sirop |
| Liqueur de café | — | **ALC** | 🟡 | Café fort + sirop |
| Crème de whisky / liqueur crémeuse | LA | **ALC** | 🟡 | Crème + café/caramel |
| Pastis / anisés | — | **ALC** | 🟢 | Infusion d'anis étoilé + eau |
| Mirin | — | **ALC** | 🟡 | Jus de raisin blanc + vinaigre de riz + sucre |
| Saké / saké de cuisine | — | **ALC** | 🟡 | Dashi léger + vinaigre de riz |
| Vin Shaoxing | GL | **ALC** | 🟠 | Bouillon + vinaigre de riz + pincée de sucre |
| Extrait de vanille liquide | — | **ALC** | 🟢 | Poudre/gousse/pâte de vanille |
| Arôme amande amère / rhum / « arômes » | — | **ALC** (support) | 🟢 | Version sans alcool ou poudre naturelle |
| Eau de fleur d'oranger / de rose | — | ALC~? | 🟡 | Vérifier : certaines sans alcool ; sinon zeste + sirop |
| Kombucha | — | ALC~ | 🟡 | Jus pétillant + thé |
| Kéfir de fruits / de lait | LA? | ALC~ | 🟡 | |
| Bière 0,0 % / vin désalcoolisé | GL?, SU? | ALC~ | 🟢 | Résidu ≤ 0,5 % : **exclu en Strict** |
| Cerises / fruits « à l'eau-de-vie » | — | **ALC** | 🟡 | Fruits au sirop |
| Rhum-raisins, marrons à l'alcool | — | **ALC** | 🟡 | Version sirop |
| Crèmes glacées / sorbets « arrosés » | LA? | **ALC** | 🟢 | Version sans alcool |
| Jus de raisin / pomme (pur jus) | SU? | — | 🟢 | Base de substitution (**vérifier jus non fermenté**) |
| Verjus | SU? | — | 🟠 | |
| Thé noir fumé (lapsang) | — | — | 🟡 | Remplace notes de whisky/rhum |

---

## 15. Produits du monde (par zone)

> Table dédiée à ce qui fait la **valeur d'ATLAS** : les cuisines du monde. Chaque ligne a son substitut en cas de 🔴 (cf. §16).

### 15.1 Asie

| Nom | Allerg. | Dérivés | Dispo | Notes |
|---|---|---|---|---|
| Bonite séchée (katsuobushi) | PO | — | 🟠 | |
| Kombu / wakame | — | — | 🟠 | |
| Nori | — | — | 🟡 | |
| Umeboshi | — | ALC~? | 🟠 | |
| Gingembre mariné (gari) | — | — | 🟡 | |
| Wasabi (pâte) | — | — | 🟡 | Souvent raifort + colorant |
| Panko | GL | — | 🟡 | |
| Tofu soyeux / ferme / frit | SO | — | 🟡 | |
| Yuba | SO | — | 🟠 | |
| Kimchi | PO, CR? | — | 🟡 | Sauce de poisson, crevettes |
| Gochugaru | — | — | 🟠 | |
| Kecap manis | SO | — | 🟠 | |
| Lait de coco | — | — | 🟢 | |
| Galanga / citronnelle / combava | — | — | 🟠 | |
| Pâte de curry thaï (rouge, verte) | CR?, PO? | — | 🟡 | |
| Tamarin | — | — | 🟠 | |
| Ghee | LA | ANIM | 🟡 | |
| Paneer | LA | ANIM? | 🟠 | |
| Besan | — | — | 🟡 | |
| Atta | GL | — | 🟠 | |
| Lentilles corail (masoor) | — | — | 🟢 | |
| Curry leaves | — | — | 🟠 | |
| Asafoetida (hing) | GL? | — | 🟠 | |
| Jaggery | — | — | 🟠 | |
| Huile de moutarde | MO | — | 🟠 | |
| Eau de rose | — | ALC~? | 🟡 | |
| Vinaigre noir de Chine | GL | ALC~ | 🟠 | |
| Poivre du Sichuan | — | — | 🟡 | |
| Huile pimentée chinoise | SO?, SE? | — | 🟡 | |
| Sauce hoisin | SO, SE?, GL? | — | 🟡 | |
| Pâte de haricots jaunes/noirs | SO | ALC~ | 🟠 | |

### 15.2 Maghreb & Moyen-Orient

| Nom | Allerg. | Dérivés | Dispo | Notes |
|---|---|---|---|---|
| Semoule de couscous | GL | — | 🟢 | |
| Citron confit | — | — | 🟠 | Express : citron + sel + jus, 48 h |
| Harissa | — | — | 🟡 | Maison conseillée |
| Ras el-hanout / chermoula | — | — | 🟡 | |
| Smen | LA | ANIM | 🟠 | |
| Olives (violettes, cassées) | — | — | 🟡 | |
| Eau de fleur d'oranger | — | ALC~? | 🟡 | Vérifier |
| Pâte de brick / ouarka | GL | — | 🟡 | |
| Merguez | — | PORC? | 🟢 | Vérifier |
| Tahini / houmous | SE | — | 🟡 | |
| Labneh | LA | ANIM? | 🟠 | |
| Zaatar / sumac | SE? | — | 🟡 | |
| Mélasse de grenade | — | — | 🟠 | |
| Boulgour fin | GL | — | 🟢 | |
| Freekeh | GL | — | 🟠 | |
| Feuilles de vigne | SU? | — | 🟡 | |
| Halloumi | LA | ANIM? | 🟡 | |
| Ful medames (fèves) | — | — | 🟠 | |
| Dattes medjool | SU? | — | 🟡 | |
| Pâte de dattes | — | — | 🟠 | |
| Mastic / mahleb | — | — | 🔴 | → vanille + pincée de poivre blanc |
| Pistaches vertes | FC | — | 🟡 | |
| Baklava (pâte filo + noix) | GL, FC, LA | — | 🟡 | |

### 15.3 Afrique subsaharienne

| Nom | Allerg. | Dérivés | Dispo | Notes |
|---|---|---|---|---|
| Manioc / attiéké / garri | — | — | 🟠 | |
| Plantain | — | — | 🟡 | |
| Gombo | — | — | 🟠 | |
| Huile de palme rouge | — | — | 🟠 | |
| Piment scotch bonnet | — | — | 🟠 | |
| Pâte d'arachide | AR | — | 🟡 | Mafé, tigadèguè |
| Poisson fumé / séché | PO | — | 🟠 | |
| Crevettes séchées | CR | — | 🟠 | |
| Soumbala / netetou | — | — | 🔴 | → miso léger + moutarde (à tester) |
| Feuilles de manioc / de patate douce | — | — | 🔴 | → épinard + chou kale |
| Teff / injera | — | — | 🟠 | |
| Berbéré | — | — | 🟠 | |
| Niter kibbeh | LA | ANIM | 🔴 | → ghee + cardamome + fenugrec + gingembre |
| Fonio | — | — | 🟠 | |
| Hibiscus séché (bissap) | — | — | 🟠 | |
| Tamarin / baobab (poudre) | — | — | 🟠 | |
| Igname / taro | — | — | 🟠 | |

### 15.4 Amériques & Caraïbes

| Nom | Allerg. | Dérivés | Dispo | Notes |
|---|---|---|---|---|
| Masa harina | — | — | 🔴 | → farine de maïs précuite + pincée de chaux (ou polenta fine) |
| Tortillas de maïs | — | — | 🟡 | |
| Haricots noirs | — | — | 🟢 | |
| Piments chipotle / ancho / guajillo | — | — | 🟠 | |
| Tomatille | — | — | 🔴 | → tomate verte + citron vert |
| Nopal | — | — | 🔴 | → haricots verts + citron vert |
| Epazote | — | — | 🔴 | → coriandre + origan |
| Aji amarillo | — | — | 🔴 | → poivron jaune + piment jaune |
| Achiote / rocou | — | — | 🟠 | → paprika + curcuma |
| Chorizo mexicain | — | PORC | 🟠 | → chorizo de bœuf/volaille |
| Queso fresco / cotija | LA | ANIM? | 🟠 | → feta émiettée |
| Dulce de leche | LA | — | 🟡 | |
| Sauce chipotle en adobo | — | ALC~? | 🟠 | |
| Mole (pâte) | FC?, SE?, AR?, GL? | — | 🟠 | |
| Farofa / farine de manioc torréfiée | — | — | 🟠 | |
| Cachaça / pisco | — | **ALC** | 🟡 | |
| Colombo (mélange antillais) | MO? | — | 🟠 | |
| Christophine, giraumon | — | — | 🟠 | |
| Fruit à pain | — | — | 🟠 | |
| Morue salée | PO | — | 🟡 | |
| Lime / citron vert | — | — | 🟢 | |
| Avocat | — | — | 🟢 | |

---

## 16. Substituts pour ingrédients 🟠 / 🔴 (disponibilité France)

> Statut des substituts : **à tester** tant qu'une fiche de test goût n'a pas validé la règle (Tome 1 §7.5).

| Ingrédient difficile | Substitut proposé | Ajustement | Écart goût attendu |
|---|---|---|---|
| Yuzu | Citron + mandarine (1:1) | + zeste | Moyen |
| Shiso | Basilic + menthe | | Moyen |
| Mirin | Jus de raisin blanc + vinaigre de riz + sucre | 3:1:1 | Faible |
| Kansui (nouilles ramen) | Bicarbonate **cuit au four 1 h à 120 °C** | 1 c. à c. par 300 g de farine | Faible |
| Gochujang | Purée de piment + miso + miel | 2:1:1 | Moyen |
| Tamarin | Jus de citron vert + sucre roux | 2:1 | Moyen |
| Pâte de crevettes | Anchois + pâte de piment | | Moyen |
| Nuoc-mâm | Sauce soja + citron vert + sucre | ⚠️ perd l'umami « poisson » | Moyen |
| Mastic / mahleb | Vanille + poivre blanc | | Moyen |
| Masa harina | Farine de maïs précuite (ou polenta fine) | Ajouter eau chaude ; + pincée de chaux alimentaire optionnelle | Moyen |
| Tomatille | Tomate verte + citron vert | | Moyen |
| Nopal | Haricots verts + citron vert | | Moyen |
| Epazote | Coriandre + origan | | Moyen |
| Aji amarillo | Poivron jaune + piment jaune | | Moyen |
| Amchur | Citron + pincée de sucre | | Moyen |
| Niter kibbeh | Ghee + cardamome + fenugrec + gingembre | Infuser 10 min | Faible |
| Soumbala / netetou | Miso léger + moutarde | | Fort |
| Citron confit | Citron + sel, 48 h au réfrigérateur | | Faible |
| Smen | Beurre clarifié + pincée de fromage fort | | Moyen |
| Guanciale | Magret fumé / bœuf fumé | | Moyen |
| Lardons | Dinde fumée + paprika fumé | | Faible |
| Babeurre | Lait + 1 c. à s. de citron par 250 ml (10 min) | | Faible |
| Crème fraîche | Yaourt grec + un peu de crème | | Faible |
| Œuf (liant) | Lin moulu (1 c. à s. + 3 c. à s. d'eau) / aquafaba (3 c. à s.) | Pâtisserie : selon recette | Moyen |
| Gélatine | Agar-agar (≈ 1/3 de dose, bouillir 1-2 min) | Texture plus ferme | Moyen |
| Vin (rouge/blanc) | cf. §14 | | |
| Pierre à pizza | Plaque épaisse retournée préchauffée | | Faible |
| Tandoor (naan) | Poêle en fonte couverte | | Moyen |

---

## 17. Annexes

### 17.1 Additifs et ingrédients **hors charte** (à signaler « Évité » quand présents dans un produit du commerce)
Conservateurs (sorbates E200-203, benzoates E210-213, sulfites E220-228 hors usage naturel) · exhausteurs (glutamate E620-625, inosinates E630-635) · colorants (E100-E199 industriels, caramel E150) · épaississants/stabilisants industriels (E400-E499 sauf **agar E406, pectine E440** en usage maison), amidons modifiés (E14xx) · édulcorants intenses (E950-969) · arômes artificiels · acide citrique industriel (hors recettes maison). **Règle** : une recette « maison sans additif » ne contient **aucun** ingrédient du commerce portant ces codes ; le référentiel porte `additive_flags[]` par produit composé.

### 17.2 Durées de conservation de référence (repères prudents)
> Ce sont des **ordres de grandeur éditoriaux** ; la **DLC/DDM de l'emballage prime** ; pour les produits maison, appliquer la règle prudente.

| Famille | Frigo (≤ 4 °C) | Congélateur (−18 °C) |
|---|---|---|
| Viande hachée crue | 1 jour | 3-4 mois |
| Viande/volaille crue | 1-2 jours | 6-12 mois |
| Poisson cru | 1 jour | 3-6 mois |
| Plats cuisinés | 3 jours | 2-3 mois |
| Riz cuit | 1 jour (refroidir vite) | 1 mois |
| Mayonnaise maison (œuf cru) | **3 jours** | ❌ |
| Sauces sans œuf (yaourt, tomate) | 3-5 jours | selon base |
| Pesto maison | 5-7 jours | 3 mois (portions) |
| Œufs durs | 5-7 jours | ❌ |
| Fromages à pâte dure | 3-4 semaines | possible, texture altérée |
| Légumes feuilles | 3-5 jours | ❌ (blanchis : oui pour épinards, etc.) |
| Pain maison | 2-3 jours (température ambiante) | 3 mois |
| Pâte à pizza (levée au froid) | 2-3 jours | 2-3 mois |

### 17.3 Densités de conversion (g par 100 ml ≈, à valider par pesée)
Farine T55 ≈ 55 g · Sucre ≈ 85 g · Sucre glace ≈ 55 g · Beurre ≈ 95 g · Huile ≈ 92 g · Eau/lait ≈ 100 g · Miel ≈ 140 g · Riz cru ≈ 80 g · Semoule ≈ 70 g · Cacao ≈ 40 g.
*Les ratios « 1 verre = X g » sont **bannis** de la base (trop variables).*

### 17.4 Anatomie zéro déchet : table de relations (extrait)

| Ingrédient | Partie | Valorisation (id recette) |
|---|---|---|
| Poireau | vert | `rcp_bouillon_legumes`, `rcp_chips_poireau` |
| Carotte / radis / betterave | fanes | `rcp_pesto_fanes`, `rcp_soupe_fanes` |
| Pain | rassis | `rcp_pain_perdu`, `rcp_chapelure_maison`, `rcp_panzanella` |
| Œuf | blanc | `rcp_meringue`, `rcp_financiers`, `rcp_mousse_chocolat` |
| Œuf | jaune | `rcp_mayo`, `rcp_creme_anglaise`, `rcp_sabayon` |
| Poulet | carcasse | `rcp_bouillon_volaille` |
| Agrumes | zeste / peau | `rcp_sucre_agrumes`, `rcp_ecorces_confites` |
| Parmesan | croûte | `rcp_risotto`, `rcp_bouillon_parmesan` |
| Champignons | pieds | `rcp_bouillon_umami`, `rcp_duxelles` |
| Pommes de terre | peaux | `rcp_chips_epluchures` |
| Brocoli / chou-fleur | tiges, feuilles | `rcp_soupe_tiges`, `rcp_chou_fleur_roti_entier` |
| Pois chiches | eau de cuisson | `rcp_aquafaba_meringue` |
| Café | marc | `rcp_marinade_cafe` |
| Poisson | arêtes | `rcp_fumet_poisson` |

### 17.5 Champs du fichier d'import CSV (pour l'équipe contenu)

```
id, name_fr, aliases, family, allergens, derivatives_pork, derivatives_alcohol, derivatives_animal,
availability, watch, additive_flags, parts, shelf_fridge_days, shelf_freezer_months,
density_g_per_100ml, halal_notes, source, verified_level, verified_by, verified_at
```

---

## 18. Bilan de livraison V1 et prochaines étapes

Comptage réel des lignes du fichier (hors en-têtes) :

| Section | Lignes |
|---|---|
| §2 Viandes & volailles | 39 |
| §3 Porc, charcuterie, alternatives sans porc | 57 |
| §4 Poissons & fruits de mer | 37 |
| §5 Œufs, laitiers & alternatives | 47 |
| §6 Légumes, champignons, algues | 76 |
| §7 Fruits | 43 |
| §8 Légumineuses, céréales, féculents | 39 |
| §9 Farines, pains, pâtes | 57 |
| §10 Herbes & aromates | 22 |
| §11 Épices & mélanges | 52 |
| §12 Condiments, sauces, bouillons | 59 |
| §13 Huiles, sucrants, coques | 52 |
| §14 Alcools & dérivés | 40 |
| §15 Produits du monde | 93 |
| **Total (avec indice de disponibilité)** | **713 lignes** |

À cela s'ajoutent quelques lignes « maison » sans disponibilité (bouillons, levain, etc.) et les 27 substituts du §16.

> ⚠️ **Lecture honnête du volume** : 713 lignes dépassent l'objectif de 500, mais plusieurs lignes sont des **groupes** (ex. « Gruyère / comté / emmental », « Cèpe / girolle / morille ») et certains ingrédients apparaissent dans **deux sections** (ex. saindoux §3 et §13, miel, tahini). Après éclatement des groupes et dédoublonnage, compter **≈ 650 à 750 ingrédients canoniques**. Les valeurs d'allergènes et de dérivés sont **prudentes mais non vérifiées** (niveau C/B, voir §1.5).

### Prochaines étapes (ordre recommandé)
1. **Éclater les groupes** en entrées canoniques et générer les `id`.
2. **Compléter** `aliases` (FR/EN/AR/translittérations) et `density_g_per_100ml`.
3. **Relecture croisée** diététicien(ne) + chef sur les familles à risque : §3, §5 (présure), §12 (bouillons), §14, §15.
4. **Rapprochement Ciqual / Open Food Facts** (licences : Ciqual, ODbL à respecter).
5. **Brancher** le référentiel sur les **30 tests dorés** (Tome 2 §4) et sur la vue `recipe_diet`.
6. **Tests goût à l'aveugle** des substitutions du §16 (Tome 7).
