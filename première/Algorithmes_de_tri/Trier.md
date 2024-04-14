# Trier

## I. Définition

*Trier* un ensemble de valeurs (par exemple une liste), c'est obtenir une permutation de cet ensemble en vérifiant plusieurs contraintes.

Prenons par exemple : `l`, une liste Python d'entiers non triée et `l_triee` la permutation de `l` vérifiant les contraintes suivantes :

- La taille de `l` est égale à la taille de `l_triee`.

- Tous les éléments contenus dans `l` sont présents dans `l_triee`.

- Pour chaque élément de `l` et de `l_triee`, le nombre d'occurence des éléments est le même.

- La liste `l_triee` obtenue respecte la relation d'ordre (croissant/décroissant).

##### Application 1

Obtenir les permutations des listes suivantes  :

a) `l = [4, 99, 0, 34, 7, 3, 2, 78]`.

b) `l = [1]`

c) `l = []`

##### Application 2

Donner les contraintes qui ne sont pas respectées pour les permutations suivantes :

a) `l = [3, 9, 1, 0, 5, 7, 2, 6]` et `l_triee = [0, 0, 1, 2, 3, 5, 6, 7]`

b) `l = [3, 9, 1, 0, 5, 7, 2, 6]` et `l_triee = [0, 1, 2, 3, 5, 6, 7, 8, 9]`

##### Application 3

Écrire une fonction `est_bonne_taille(l : list, l_triee : list)->bool` qui prend en paramètre deux listes et renvoie $True$ si elles sont de la même taille, $False$ sinon.

Cette fonction permet de vérifier la première contrainte.

##### Application 4

Écrire une fonction `sont_presents(l : list, l_triee : list)->bool` qui prend en paramètre deux listes et renvoie $True$ si tous les éléments de `l` sont présents dans `l_triee`, $False$ sinon.

Cette fonction permet de vérifier la deuxième contrainte.

##### Application 5

Écrire une fonction `bonnes_occurences(l : list, l_triee : list)->bool` qui prend en paramètre deux listes et renvoie $True$ si pour chacun des éléments de `l` et `l_triee`, leur nombre d'occurence est le même, $False$ sinon.

Cette fonction permet de vérifier la troisième contrainte.

##### Application 6
Écrire une fonction `est_ordonnee(l_triee : list)->bool` qui prend en paramètre une liste et renvoie $True$ si elle est ordonnée en ordre croissant de ses éléments, $False$ sinon.

Cette fonction permet de vérifier la quatrième contrainte.

##### Application 7

Écrire une fonction `est_triee(l : list, l_triee : list)->bool` qui prend en paramètre deux listes et renvoie $True$ si `l_triee` est une permutation de `l` vérifiant les contraintes de tri.

## II. Tri...

### a) ...par comparaison

Un *tri par comparaison* est un type d'algorithme de tri dans lequel le tri s'effectue à l'aide d'une opération de comparaison. 

De manière générale, nous cherchons à trier de simples ensembles d'entiers et l'opérateur `>` ou `<` suffit mais il arrive parfois de vouloir trier par exemple une liste de mots selon leur ordre lexicographique.

Dans cette optique, les informaticiens préfèrent alors utiliser une fonction `compare(a, b)` qui détermine alors lequel des deux éléments doit apparaître en premier.

Ainsi, selon le type des données que l'on souhaite trier, la fonction `compare()` s'adapte au type de données et permet ainsi à ce que l'algorithme de tri ne soit pas modifié.

> Il existe des tris qui n'utilisent pas les comparaisons comme le tri par dénombrement.

##### Application 8

a) Dire quel est l'outil faisant office de fonction `compare()` lors de l'activité.

b) Écrire une fonction `compare(a : int, b : int)->bool` qui prend en paramètre deux entiers et renvoie $True$ si $a \geq b$.

### b) ...en place

Un tri est dit *en place* s'il modifie directement en mémoire la structure de données sur laquelle s'applique le tri.

Un tri en place ne renvoie donc rien.

## III. Applications 

Le tri en informatique est très utilisé dans le pré-traitement des données.

C'est-à-dire, lorsque les données ont besoin d'être triées pour que le traitement sur celles-ci soit plus efficace, moins coûteuse.

##### Application 9

Expliquer pourquoi le tri peut permettre de réduire le coût algorithmique du problème de recherche d'un élément dans une liste.

____________

[Sommaire](./../README.md)