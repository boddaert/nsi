# Trier

## I. Définition

*Trier* un ensemble de valeurs (par exemple une liste), c'est obtenir une permutation de cet ensemble en vérifiant plusieurs contraintes.

Prenons `l`, une liste Python d'entiers naturels non triée et `l_triee` la permutation de `l` vérifiant :

- La taille de `l` est égale à la taille de `l_triee`.

- Tous les éléments contenus dans `l` sont présents dans `l_triee`.

- Pour chaque élément de `l` et de `l_triee`, le nombre d'occurence des éléments est le même.

- La liste `l_triee` obtenue respecte la relation d'ordre (croissant/décroissant).

##### Application 1

Obtenir `l_triee` la permutation de `l` et en vérifiant que les contraintes précédentes soient respectées avec :

- `l = [4, 99, 0, 34, 7, 3, 2, 78]`.

- `l = [1]`

- `l = []`

##### Application 2

Donner les contraintes qui ne sont pas respectées pour les permutations suivantes :

1) `l = [3, 9, 1, 0, 5, 7, 2, 6]` et `l_triee = [0, 0, 1, 2, 3, 5, 6, 7]`

2) `l = [3, 9, 1, 0, 5, 7, 2, 6]` et `l_triee = [0, 1, 2, 3, 5, 6, 7, 8, 9]`

## II. Spécificités

Un *tri par comparaison* est un tri qui utilise les comparaisons. Il existe des tris qui n'utilisent pas les comparaisons comme le tri par dénombrement.

Un tri est dit *stable* s'il préserve, à l'issue du tri, le même ordre sur des éléments égaux.

Un tri est dit *en place* s'il modifie directement en mémoire la structure de données sur laquelle s'applique le tri.

## III. Applications 

Le tri en informatique permet de réduire les coûts algorithmiques de beaucoup d'algorithmes comme la recherche d'un élément dans une liste ou le calcul de la médiane.

____________

[Sommaire](./../README.md)