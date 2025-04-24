# Activité : Recherche dichotomique

Nature : Débranchée/Branchée.

Matériel : Aucun.

Prérequis : [Complexité](./Complexité.md).

À faire : Seul.

## I. Objectif

L'objectif de cette activité est de concevoir un algorithme de recherche plus efficace en terme de complexité temporelle que les algorithmes de recherche séquentielle et de recherche séquentielle améliorée.

## II. Travail à faire

### 1. Partie débranchée

a) Mettez-vous un par un en rang par ordre alphabétique.

b) Quelle(s) sont les méthodes à ma disposition pour retrouver le plus rapidement possible un élève dont je connais uniquement le nom de famille et en ne pouvant demander qu'à une seule personne à la fois ?

### 2. Partie branchée

c) Sur Thonny, écrire une fonction `recherche_séquentielle(l : list, elt : int)->int` qui prend en paramètre une liste d'entiers et un entier et renvoie l'indice de `elt` s'il est dans `l`, $-1$ sinon.

Cette fonction se repose sur l'algorithme `recherche_1` vue dans la leçon précédente [Complexité](./Complexité.md).

d) Sur Thonny, écrire une fonction `recherche_séquentielle_amelioree(l : list, elt : int)->int` qui prend en paramètre une liste d'entiers et un entier et renvoie l'indice de `elt` s'il est dans `l`, $-1$ sinon.

Cette fonction se repose sur l'algorithme `recherche_2` vue dans la leçon précédente [Complexité](./Complexité.md).

e) Aller sur [Attrapper le monstre](https://castor-informatique.fr/questions/2014/2014-FR-03-monster/) et trouver la stratégie permettant d'obtenir le score maximal.

f) En vous aidant de la solution, expliquer en quelques lignes en quoi consiste la recherche dichotomique.

Nous souhaitons désormais appliquer cette stratégie de recherche pour une liste `l` d'entiers.

g) Afin de transformer le donjon en une liste d'entiers, ajoutons mentalement dans chaque case du jeu un numéro correspondant à leur indice $i$. Avec la première case d'indice $i=1$.

Refaire le jeu en donnant les numéros de case bloquées.

h) Pour une liste `l` d'entiers quelquonque, quelle est la condition nécessaire pour que la recherche dichotomique fonctionne ?

i) Soit `l_triee` la liste d'entiers `l` dont les éléments sont triés de manière croissante :

`l_triee = [0, 1, 2, 3, 4, 5, 7, 8, 10, 14]`

Utiliser la recherche dichotomique afin de retrouver $1$ en comptant le nombre de comparaisons effectuées puis comparer avec celles trouvées à la leçon précédente.

j) Dire si la complexité temporelle de la recherche dichotomique est plus efficace ou non que les deux autres algorithmes de recherche dans une liste d'entiers triée.

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

k) À l'aide de l'algorithme de recherche dichotomique, écrire une fonction `recherche_dichotomique(l_triee : list, elt : int)->int` qui prend en paramètre une liste d'entiers triée et un entier et renvoie l'indice de `elt` s'il est dans `l`, $-1$ sinon.

l) Avec `l_triee = [0, 1, 2, 3, 4, 5, 7, 8, 10, 14]` et `elt = 1`, compléter la trace d'exécution ci-dessous :

| Avant le tour de boucle n° | Valeur de `trouve` | Valeur de `i_milieu` | Valeur de `i_debut` | Valeur de `i_fin` |
| :---: | :---: | :---: | :---: | :---: |
| $0$ | $False$ | / | $0$ | $9$ |
| $1$ | ... | ... | ... | ... |

___________________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 












