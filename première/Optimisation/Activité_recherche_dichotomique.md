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

e) Afin de transformer le donjon en une liste d'entiers, ajoutons mentalement dans chaque case du jeu un numéro correspondant à leur indice $i$. Avec la première case d'indice $i=1$.

Refaire le jeu en donnant les numéros de case bloquées.

f) Pour une liste `l` d'entiers quelquonque, quelle est la condition nécessaire pour que la recherche dichotomique fonctionne ?

g) Soit `l_triee` la liste d'entiers `l` dont les éléments sont triés de manière croissante :

`l_triee = [0, 1, 2, 3, 4, 5, 7, 8, 10, 14]`

Utiliser la recherche dichotomique afin de retrouver $1$ en comptant le nombre de comparaisons effectuées puis comparer avec celles trouvées à la leçon précédente.

h) Dire si la complexité temporelle de la recherche dichotomique est plus efficace ou non que les deux autres algorithmes de recherche dans une liste d'entiers triée.

La complexité de la recherche dichotomique a un coût logarithmique : il est proportionnel à $O(\log_2 n)$.

Voici ci-dessous, l'algorithme de recherche dichotomique :

```
Algorithme recherche_dichotomique(l_triee, elt) :
Entrées : l_triee une liste d'entiers triée et elt un entier
Sortie : Un entier, indice de elt dans l_triee, -1 sinon

i_elt <- -1
trouve <- Faux
i_debut <- 0
i_fin <- taille(l_triee)-1
TantQue i_debut <= i_fin and trouve = Faux, faire:
    i_milieu <- (i_fin + i_debut)//2
    Si l_triee[i_milieu] = elt, alors :
        trouve <- Vrai
        i_elt <- i_milieu
    Sinon :
        Si l_triee[i_milieu] > elt, alors :
            i_fin <- i_milieu - 1
        Sinon :
            i_debut <- i_milieu + 1
Renvoyer i_elt
```

i) À l'aide de l'algorithme de recherche dichotomique, écrire une fonction `recherche_dichotomique(l_triee : list, elt : int)->int` qui prend en paramètre une liste d'entiers triée et un entier et renvoie l'indice de `elt` s'il est dans `l`, $-1$ sinon.

j) Avec `l_triee = [0, 1, 2, 3, 4, 5, 7, 8, 10, 14]` et `elt = 1`, compléter la trace d'exécution ci-dessous :

| Avant le tour de boucle n° | Valeur de `trouve` | Valeur de `i_milieu` | Valeur de `i_debut` | Valeur de `i_fin` |
| :---: | :---: | :---: | :---: | :---: |
| $0$ | $False$ | / | $0$ | $9 |
| $1$ | ... | ... | ... | ... |

k) En utilisant les *sclices* (les coupes propres à Python), écrire une fonction `recherche_dichotomique_simplifiee(l_triee : list, elt : int)->bool` qui prend en paramètre une liste d'entiers triée et un entier et renvoie l'indice de `elt` s'il est dans `l`, $-1$ sinon.

___________________

[Sommaire](./../README.md)












