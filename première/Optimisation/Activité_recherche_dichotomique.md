# Activité : Recherche dichotomique

Nature : Branchée

Matériel : Aucun

Prérequis : Recherche séquentielle, recherche séquentielle améliorée

Groupe : Seul

## I. Objectif

L'objectif de cette activité est de concevoir un algorithme de recherche plus efficace en terme de complexité temporelle que les algorithmes de recherche séquentielle et de recherche séquentielle améliorée.

## II. Travail à faire

a) Sur Thonny, écrire une fonction `recherche_séquentielle(l : list, elt : int)->int` qui prend en paramètre une liste d'entiers et un entier et renvoie l'indice de `elt` s'il est dans `l`, $-1$ sinon.

Cette fonction se repose sur l'algorithme `recherche_1` vue dans la leçon précédente [Complexité](./Complexité.md).

b) Sur Thonny, écrire une fonction `recherche_séquentielle_amelioree(l : list, elt : int)->int` qui prend en paramètre une liste d'entiers et un entier et renvoie l'indice de `elt` s'il est dans `l`, $-1$ sinon.

Cette fonction se repose sur l'algorithme `recherche_2` vue dans la leçon précédente [Complexité](./Complexité.md).

c) Aller sur [Attrapper le monstre](https://castor-informatique.fr/questions/2014/2014-FR-03-monster/) et trouver la stratégie permettant d'obtenir le score maximal.

d) En vous aidant de la solution, expliquer en quelques lignes en quoi consiste la recherche dichotomique.

Nous souhaitons désormais appliquer cette stratégie de recherche pour une liste `l` d'entiers.

e) Afin de transformer le donjon en une liste d'entiers, ajoutons mentalement dans chaque case du jeu un numéro correspondant à leur indice $i$. Avec la première case d'indice $i=0$.

Refaire le jeu en donnant les numéros de case bloquées.

f) Pour une liste `l` d'entiers quelquonque, quelle est la condition nécessaire pour que la recherche dichotomique fonctionne ?

g) Soit `l_triee` la liste d'entiers `l` dont les éléments sont triés de manière croissante :

`l_triee = [0, 1, 2, 3, 4, 5, 7, 8, 10, 14]`

Utiliser la recherche dichotomique afin de retrouver $1$ en comptant le nombre de comparaisons effectuées puis comparer avec celles trouvées à la leçon précédente.

h) Dire si la complexité temporelle de la recherche dichotomique est plus efficace ou non que les deux autres algorithmes de recherche dans une liste d'entiers triée.

La complexité de la recherche dichotomique a un coût logarithmique : il est proportionnel à $O(\log_2 n)$.

i) Écrire une fonction `recherche_dichotomique(l_triee : list, elt : int)->int` qui prend en paramètre une liste d'entiers triée et un entier et renvoie l'indice de `elt` s'il est dans `l`, $-1$ sinon.

___________________

[Sommaire](./../README.md)












