# Exercices 

$G =$

```mermaid
    flowchart LR
        0 --> 9
        0 --> 4
        1 --> 3
        1 --> 5
        2 --> 0
        2 --> 1
        3 --> 4
        4 --> 2
        4 --> 8
        5 --> 7
        8 --> 6
        6 --> 2
        7 --> 6
        8 --> 0
        9 --> 3
        9 --> 8
```

## Exercice 1

a) En considérant la représentation sagitalle du graphe $G$ ci-dessus, répondre aux questions suivantes :

1. Le graphe $G$ est-il non orienté, orienté, pondéré ?

2. Donner l'ordre du graphe $G$.

3. Donner les sommets adjacents du sommet $1$, $4$, $9$.

4. Donner le degré entrant et sortant du sommet $4$.

5. Donner un chemin possible du graphe $G$ de longueur $6$.

6. Donner un cycle possible du graphe $G$.

b) Donner sur papier la matrice d'adjacence du graphe $G$ puis l'implémenter en Python en le nommant `G_matrice`.

c) Avec `G_matrice`, écrire l'instruction permettant d'indiquer si le sommet $9$ est adjacent du sommet $5$.

d) Donner sur papier la liste d'adjacence du graphe $G$ puis l'implémenter en Python en le nommant `G_liste`.

e) Avec `G_liste`, écrire l'instruction permettant d'indiquer si le sommet $0$ est adjacent du sommet $6$.

**Pour chacune des fonctions écrites ci-après, tester-les en utilisant `G_matrice` et `G_liste`.**

## Exercice 2

a) Écrire une fonction `ordre_graphe_matrice(g : list)->int` qui prend en paramètre un graphe `g` représenté par matrice d'adjacence et renvoie son ordre.

b) Écrire une fonction `ordre_graphe_liste(g : dict)->int` qui prend en paramètre un graphe `g` représenté par liste d'adjacence et renvoie son ordre.

## Exercice 3

a) Écrire une fonction `est_adjacent_matrice(g : list, i : int, j : int)->bool` qui prend en paramètre un graphe `g` représenté par matrice d'adjacence, deux sommets `i` et `j` et renvoie $True$ si `j` est un sommet adjacent du sommet `i`, $False$ sinon.

b) Écrire une fonction `est_adjacent_liste(g : list, i : int, j : int)->bool` qui prend en paramètre un graphe `g` représenté par liste d'adjacence, deux sommets `i` et `j` et renvoie $True$ si `j` est un sommet adjacent du sommet `i`, $False$ sinon.

## Exercice 4

a) Écrire une fonction `voisins_matrice(g : list, i : int)->list` qui prend en paramètre un graphe `g` représenté par matrice d'adjacence, un sommet et renvoie la liste des sommets adjacents du sommet `i`.

b) Écrire une fonction `voisins_liste(g : dict, i : int)->list` qui prend en paramètre un graphe `g` représenté par liste d'adjacence, un sommet et renvoie la liste des sommets adjacents du sommet `i`.

## Exercice 5

En fonction des programmes donnés en réponse aux exercices trois et quatre, donner les avantages et les inconvénients de représenter son graphe par matrice d'adacence ou par liste d'adjacence.

## Exercice 6

Écrire une fonction `est_chemin(g : dict, chemin : list)->bool` qui prend en paramètre un graphe `g` représenté par une liste d'adjacence et une liste et renvoie $True$ si `chemin` est un chemin de `g`, $False$ sinon.

## Exercice 7

Écrire une fonction `degre_sortant(g : dict, i : int)->int` qui prend en paramètre un graphe `g` représenté par une liste d'adjacence et un sommet et renvoie le degré sortant de `i`.

## Exercice 8 (Difficile)

Un graphe est dit *complet* si chaque sommet du graphe est adjacent de tous les autres sommets.

a) Dessiner un graphe non orienté complet d'ordre 5.

b) Donner le nombre d'arêtes de ce graphe.

c) Donner le nombre d'arêtes d'un graphe non orienté d'ordre $n$.

d) Écrire une fonction `est_complet(g : dict)->bool` qui prend en paramètre un graphe `g` et renvoie $True$ s'il est complet, $False$ sinon.

__________________

[Sommaire](./../../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 