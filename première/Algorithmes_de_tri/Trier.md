# Trier

## I. Définition

*Trier* un ensemble de valeurs (par exemple une liste), c'est obtenir une permutation de cet ensemble en vérifiant plusieurs contraintes.

Prenons par exemple : `l`, une liste Python d'entiers naturels non triée et `l_triee` la permutation de `l` vérifiant les contraintes suivantes :

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

### a) Par comparaison

Un *tri par comparaison* est un type d'algorithme de tri dans lequel le tri s'effectue à l'aide d'une opération de comparaison. 

De manière générale, nous cherchons à trier de simples ensembles d'entiers et l'opérateur `>` ou `<` suffit mais il arrive parfois de vouloir trier par exemple une liste de mots selon leur ordre lexicographique.

Dans cette optique, les informaticiens préfèrent alors utiliser une fonction `compare(a, b)` qui détermine alors lequel des deux éléments doit apparaître en premier.

Ainsi, selon le type des données que l'on souhaite trier, la fonction `compare()` s'adapte au type de données et permet ainsi à ce que l'algorithme de tri ne soit pas modifié.

> Il existe des tris qui n'utilisent pas les comparaisons comme le tri par dénombrement.

##### Application 3

Dire quel est l'outil faisant office de fonction `compare()` lors de l'activité.

### b) En place

Un tri est dit *en place* s'il modifie directement en mémoire la structure de données sur laquelle s'applique le tri.

Un tri en place ne renvoie donc rien.

## III. Applications 

Le tri en informatique est très utilisé dans le pré-traitement des données.

Il permet de réduire les coûts algorithmiques de beaucoup d'autres algorithmes comme par exemple la recherche dichotomique.

____________

[Sommaire](./../README.md)