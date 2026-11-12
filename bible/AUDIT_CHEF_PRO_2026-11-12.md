# Audit « chef cuisinier professionnel senior » d'ATLAS (12/11/2026)

Regard d'un chef de brigade : ce qu'on vérifie en cuisine professionnelle et que les audits précédents (chef du 16/10,
gourmet du 21/10, chef et famille du 10/11, fin gourmet du 12/11) n'avaient pas mesuré. Les mesures sont faites sur les
1 429 fiches exportées (`app/.tmp/aud/chef.ts`). Tout a été corrigé le jour même. Contrôle automatique : test 124.

## 1. Constats mesurés

| Angle | Mesure | Gravité |
|---|---|---|
| Cuisson à cœur de la volaille | 105 plats sur 179 avec de la volaille cuite vite (poêle, gril, four, friture) sans aucun repère de cuisson à cœur (température, jus clair) | forte (sécurité) |
| Viande hachée, saucisses, porc | 63 sur 79 sans repère | forte (sécurité, enfants) |
| Repos des viandes rouges | 7 pièces saisies ou grillées sans temps de repos avant de trancher | moyenne |
| Convention du four | aucune mention statique / chaleur tournante, alors que l'écart est de 15 à 20 °C | moyenne |
| Mise à l'échelle | changer le nombre de portions adapte les quantités, sans rien dire du moule, de la pièce à rôtir ni des fournées | moyenne |
| Règle du froid | 68 fiches sur 1 429 seulement mentionnent le refroidissement ; rien sur le réchauffage unique à cœur | moyenne (sécurité) |
| Allergènes | les 14 allergènes réglementaires sont couverts, mais l'amidon de blé (ha kao, gâteaux de lune) n'était pas compté comme gluten | forte (ponctuelle) |
| Températures | pizza et flammekueche « au maximum » sans chiffre ; kelewele frit sans température d'huile | faible |
| Pesées | ablo pesé au « bol » (farine, fécule, sucre, riz) | faible |

Points vérifiés et sains :
- ratios des pâtes de base (brisée 2:1) ;
- mise à l'échelle des œufs, pincées et cuillères (arrondis entiers) ;
- dosage du sel calculé par fiche ;
- conservation par famille d'aliment ;
- avertissements sur le cru (œuf, poisson, lait cru) ;
- températures à cœur dans les fiches techniques ;
- sécurité de la friture.

Certaines quantités de viande paraissent basses par part (raviolis, lasagnes). Ce sont des plats où la viande n'est qu'une garniture : rien à corriger.

## 2. Corrigé

- **Cuisson à cœur** (`complements_pro.cuisson_a_coeur`, à l'export) : un repère chiffré est ajouté dans l'étape où la viande cuit.
  - Volaille : 74 °C, jus clair.
  - Viande hachée : 70 °C pour les enfants, les femmes enceintes et les personnes fragiles.
  - Saucisses et porc : 70 °C.
  - 63 fiches de volaille et 33 de viande hachée ou de porc sont concernées.
  - Pas de repère pour :
    - le magret, servi rosé ;
    - le boudin, déjà cuit ;
    - le poulet déjà cuit et les produits fumés ou en bouillon ;
    - les longs mijotages.
- **Repos des viandes** : 7 pièces grillées reçoivent « repos 5 min sous aluminium ».
- **Fiche recette** :
  - convention du four (statique, et l'écart en chaleur tournante) ;
  - conseil de mise à l'échelle quand on change les portions : moule, pièce à rôtir, fournées en pâtisserie ;
  - règle du froid dans « Conservation » : au frais en moins de 2 h, réchauffé une seule fois, fumant à cœur (63 °C).
- **Corrections ponctuelles** :
  - amidon de blé compté comme gluten ;
  - pizza et flammekueche à 250-280 °C ;
  - kelewele frit à 170 °C ;
  - ablo pesé en grammes.

## 3. Reste à faire

- Les recettes ne sont pas testées en cuisine.
- Les temps de cuisson sont donnés pour un four domestique moyen : chaque four doit être apprivoisé, d'où les repères visuels de chaque étape.
- Pas de fiche de production en grande quantité (cuisine collective). Hors du périmètre d'une appli familiale.
