# Convention : comment présenter la liste d'une rubrique (21/11/2026, audit dév senior §5)

Trois façons de présenter la liste d'une rubrique de fiches coexistent dans l'application. Ce document fixe quand
utiliser laquelle, pour que la prochaine rubrique créée ou corrigée reparte d'une règle plutôt que d'un choix
arbitraire.

## Puces de filtre par catégorie

Exemple : `Marinades.tsx` (par protéine), `Sauces.tsx` (par famille fast-food / France / monde).

**Quand** : la rubrique a une poignée de catégories (3 à 8) qui se chevauchent peu, et l'utilisateur sait en général
ce qu'il cherche avant d'arriver (« je veux mariner du poulet », « une sauce fast-food »). Une puce reste visible et
cliquable en un geste, sans repli ni défilement caché.

## Accordéon `<details>` par famille

Exemple : `Techniques.tsx` (une famille de gestes par pli : pâtisserie, boulangerie, poissons…).

**Quand** : la rubrique a beaucoup de familles (plus de 8) et chacune contient elle-même plusieurs fiches à
parcourir en profondeur plutôt qu'à filtrer. L'accordéon évite une liste à plat trop longue à l'ouverture, au prix
d'un clic supplémentaire pour déplier ; la première famille reste ouverte par défaut pour montrer le principe.

## Tri chronologique sans filtre

Exemple : `Fetes.tsx` (prochaines fêtes dans l'ordre du calendrier).

**Quand** : il n'y a pas de catégorie pertinente à filtrer — l'ordre naturel (la prochaine fête, la semaine à venir)
est déjà le critère que l'utilisateur veut, et un filtre ajouterait une étape sans réduire vraiment la liste.

## Choisir entre les trois

1. Y a-t-il un ordre naturel (date, étape) plus utile qu'un classement ? → tri chronologique sans filtre.
2. Sinon, les catégories sont-elles peu nombreuses et se cherchent-elles d'avance ? → puces de filtre.
3. Sinon (beaucoup de familles, à parcourir plutôt qu'à filtrer) → accordéon `<details>`.
