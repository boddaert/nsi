# Exercices

## Exercice 1

a) Écrire une fonction `affiche_liste_de_listes_parcours_indice(l : list)->None` qui prend en paramètre une liste de listes et affiche un par un tous les éléments de $l$ en effectuant le parcours par indice.

b) Écrire une fonction `affiche_liste_de_listes_parcours_element(l : list)->None` qui prend en paramètre une liste de listes et affiche un par un tous les éléments de $l$ en effectuant le parcours par élément.

## Exercice 2

Écrire une fonction `somme_liste(l : list)->int` qui prend en paramètre une liste de listes d'entiers et renvoie la somme des éléments de $l$.

## Exercice 3

Écrire une fonction `recherche_sequentielle(l : list, x : int)->bool` qui prend en paramètre une liste de listes d'entiers et un entier et renvoie comme résultat $True$ si $x$ est présent dans $l$, $False$ sinon.

## Exercice 4

Écrire une fonction `cree_table_de_multiplication(n : int)->list` qui prend en paramètre un entier et renvoie comme résultat une liste de listes représentant une table de multiplication de taille $n \times n$.

## Exercice 5

Nous pouvons observer un clavier d'ordinateur comme un tableau à deux dimensions dans lequel chaque case contient un caractère :

| **a** | **z** | **e** | **r** | **t** | **y** | **u** | **i** | **o** | **p** |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **q** | **s** | **d** | **f** | **g** | **h** | **j** | **k** | **l** | **m** |
| **<** | **w** | **x** | **c** | **v** | **b** | **n** | **,** | **;** | **:** |

En Python, nous modélisons ce tableau sous forme de liste de listes :

```python
>>> liste_clavier = [['a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
      ['q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm'],
      ['<', 'w', 'x', 'c', 'v', 'b', 'n', ',', ';', ':']]
```

L'objectif de cet exercice est de réaliser une fonction permettant de calculer la distance entre deux touches du clavier.

a) Écrire une fonction ``coord_clavier(liste_clavier : list)->dict`` qui prend en paramètre une liste de listes correspondant à un clavier et renvoie un dictionnaire dont les clés sont les caractères du clavier et les valeurs sont les coordonnées de la touche.

```python
>>> dico_clavier = coord_clavier(liste_clavier)
>>> dico_clavier
{'a': (0, 0), 'z': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4), 'y': (0, 5), 'u': (0, 6), 'i': (0, 7), 'o': (0, 8), 'p': (0, 9), 'q': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4), 'h': (1, 5), 'j': (1, 6), 'k': (1, 7), 'l': (1, 8), 'm': (1, 9), '<': (2, 0), 'w': (2, 1), 'x': (2, 2), 'c': (2, 3), 'v': (2, 4), 'b': (2, 5), 'n': (2, 6), ',': (2, 7), ';': (2, 8), ':': (2, 9)}
```

b) Écrire une fonction ``distance_touches(dico_clavier : dict, caractere_1 : str, caractere_2)->int`` qui prend en paramètres le dictionnaire et deux caractères et renvoie la distance qui les sépare sur le clavier.

> Rappel : La distance entre deux points $A(x_1, y_1)$ et $B(x_2, y_2)$ se calcule : $\sqrt[]{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.

```python
>>> distance_touches(dico_clavier, 'a', 'n')
6.324555320336759
>>> distance_touches(dico_clavier, 'a', 'b')
5.385164807134504
```

## Exercice 6 (Difficile)

Un carré magique d'ordre $n$ est un tableau de taille $n \times n$ dans lequel la somme des nombres de chaque ligne, chaque colonne et chaque diagonale est égale.

Par exemple :

<img src="./../img/carre_magique.png" width=400>


Écrire une fonction `est_carre_magique(carre : list, test_somme : int)->bool` qui prend en paramètre une liste de listes et un entier et renvoie $True$ s'il s'agit d'un carré magique, $False$ sinon.

```python
>>> est_carre_magique([[2, 7, 6],
                      [9, 5, 1],
                      [4, 3, 8]], 15)
True
```

## Exercice 7 (Difficile)

L'objectif de cet exercice est de programmer le jeu du Tic-tac-toe aussi appelé Morpion.

Les règles du jeu du Tic-tac-toe sont disponibles [ici](https://fr.wikipedia.org/wiki/Tic-tac-toe).

Vous choisirez de programmer la version du jeu à deux joueurs ou la version du jeu à un joueur contre l'ordinateur.

a) Écrire une fonction `init_grille()->list` qui ne prend pas de paramètre et renvoie une liste de listes composée uniquement de zéros correspondant à la grille de jeu du Tic-tac-toe vide.

Un $0$ indique qu'aucun joueur n'a mis de pion, un $1$ représente `X` et $2$ représente `O`.

```python
>>> init_grille()
[[0,0,0],[0,0,0],[0,0,0]]
```

b) Écrire une fonction `affiche_grille(grille : list)->None` qui prend en paramètre une liste de listes et l'affiche proprement dans la console :

```python
>>> affiche_grille(init_grille())
|     |     |     |
|     |     |     |
|     |     |     |
```

c) Écrire une fonction `placer_jeton(grille : list, pion : str, i : int, j : int)->list` qui prend en paramètre une liste de listes, un caractère correspondant au pion choisis et deux entiers correspondant aux indices de la position choisie et renvoie le nouvel état de jeu :

```python
>>> affiche_grille(placer_jeton(init_grille(), 1, 1, 1))
|     |     |     |
|     |  X  |     |
|     |     |     |
```

d) Écrire une fonction `test_victoire(grille : list)->bool` qui prend en paramètre une liste de listes et renvoie $True$ s'il s'agit d'un état de victoire, $False$ sinon.

e) Écrire une fonction `tic_tac_toe()->None` permettant à deux joueurs de jouer au jeu du Tic-tac-toe.

_______________

[Sommaire](./../../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 