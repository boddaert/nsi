# Exercices 

## Exercice 1

a) Ecrire une fonction `affiche_liste_parcours_indice(l : list)->None` qui prend en paramètre une liste et affiche un par un tous les éléments de $l$ en effectuant le parcours par indice.

b) Ecrire une fonction `affiche_liste_parcours_element(l : list)->None` qui prend en paramètre une liste et affiche un par un tous les éléments de $l$ en effectuant le parcours par élément.

## Exercice 2

Soit le programme suivant :

```python
1. l = [2, 4, 2, 2]
2. res = 0
3. for i in range(len(l)):
4.    if l[i] == 2 :
5.       res = res + 1
```

a) Compléter la trace d'exécution suivante du programme précédent :

| Numéro de ligne | Valeur affectée à $i$ | Valeur affectée à $res$ |
| :---: | :---: | :---: |
| ... | ... | ... |

b) Décrire en Français ce que réalise le programme précédent.

c) Transformer le programme précédent afin qu'il effectue un parcours par élément.

## Exercice 3

a) Ecrire une fonction `construit_liste_aleatoire_classique(n : int, i : int, j : int)->list` qui prend en paramètre trois entiers et renvoie une liste de taille $n$ dont les éléments sont des entiers aléatoires compris entre $i$ et $j$ en utilisant la construction classique.

b) Ecrire une fonction `construit_liste_aleatoire_comprehension(n : int, i : int, j : int)->list` qui prend en paramètre trois entiers et renvoie une liste de taille $n$ dont les éléments sont des entiers aléatoires compris entre $i$ et $j$ en utilisant la construction en compréhension.

## Exercice 4

Ecrire une fonction `recherche_sequentielle(l : list, x : int)->bool` qui prend en paramètre une liste d'entiers et un entier et renvoie comme résultat $True$ si $x$ est présent dans $l$, $False$ sinon.

## Exercice 5

Ecrire une fonction `somme_liste(l : list)->int` qui prend en paramètre une liste d'entiers et renvoie la somme des éléments de $l$.

## Exercice 6

Ecrire une fonction `produit_liste(l : list)->int` qui prend en parmètre une liste d'entiers et renvoie le produit des éléments de $l$.

## Exercice 7

Ecrire une fonction `moyenne_liste(l : list)->float` qui prend en paramètre une liste d'entiers et renvoie la moyenne des éléments de $l$.

## Exercice 8

Ecrire une fonction `somme_pairs_liste(l : list)->int` qui prend en paramètre une liste d'entiers et renvoie la somme des éléments pairs de $l$.

## Exercice 9

Ecrire la ligne de code permettant de construire en compréhension une liste contenant tous les éléments pairs compris entre $0$ et $n$.

## Exercice 10

Ecrire une fonction `maximum_liste(l : list)->int` qui prend en paramètre une liste d'entiers et renvoie son élément le plus grand.

## Exercice 11

Ecrire une fonction `minimum_liste(l : list)->int` qui prend en paramètre une liste d'entiers et renvoie son élément le plus petit.

## Exercice 12

Ecrire une fonction `est_triee(l : list)->bool` qui prend en paramètre une liste d'entiers et renvoie $True$ si $l$ est triée par ordre croissant, $False$ sinon.

## Exercice 13

Ecrire une fonction `listes_egales(l1 : list, l2 : list)->bool` qui prend en paramètre deux listes de taille égale et renvoie $True$ si elles sont égales, $False$ sinon.

Cette fonction devra necéssairement utiliser le parcours par indice.

## Exercice 14

Ecrire une fonction `concatene(l1 : list, l2 : list)->list` qui prend en paramètre deux listes et renvoie une liste contenant tous les éléments de $l1$ et tous les éléments de $l2$.

Cette fonction ne pourra pas utiliser l'opérateur de concaténation `+`.

## Exercice 15

Ecrire une fonction `echange(l : list, i : int, j : int)->None` qui prend en paramètre une liste et deux entiers et échange de place les éléments d'indice $i$ et $j$.

## Exercice 16

Ecrire une fonction `miroir(l : list)->list` qui prend en paramètre une liste et renvoie son miroir.

C'est-à-dire que le premier élément est échangé avec le dernier, le second est échangé avec l'avant-dernier, etc... Nous pourrons utiliser pour cela la fonction `echange()` écrite dans l'exercice précédent.

## Exercice 17

Ecrire une fonction `melange_liste(l : list)->list` qui prend en paramètre une liste et renvoie une liste mélangée aléatoirement.

Nous pourrons pour cela choisir deux indices aléatoirement et échanger les éléments des indices choisis.

## Exercice 18

Ecrire une fonction `fibonacci(n : int)->list` qui prend en paramètre un entier et renvoie une liste contenant les $n$ premiers termes de la suite de fibonacci.

Les deux premiers termes de la suite de fibonacci sont $0$ et $1$ puis, tous les suivants correspondent à la sommes des deux termes précédents :

```python
>>> fibonacci(7)
[0, 1, 1, 2, 3, 5, 8]
```

## Exercice 19

Ecrire une fonction `distance_hamming(l1 : list, l2 : list)->int` qui prend en paramètre deux listes et renvoie de combien d'éléments $l1$ et $l2$ sont différents :

```python
>>> distance_hamming([2, 5, 8, 1], [2, 3, 8, 1])
1
```

## Exercice 20 (Difficile)

Ecrire une fonction `tri_denombrement(l : list)->list` qui prend en paramètre une liste et renvoie une liste triée en utilisant le dénombrement.

Le tri par dénombrement consiste à :

- Premièrement, créer une liste intermédiaire où pour chaque élément d'indice $i$ de cette liste correspond au nombre de rencontres de la valeur $i$ dans $l$.

- Deuxièmement, de créer une nouvelle liste triée en parcourant la liste intermédiaire où les éléments de la liste intermédiaire indique le nombre d'éléments qu'il y a de valeur $i$.

Par exemple,

```python
l = [1, 2, 1, 0, 0, 4, 1, 10]
l_intermédiaire = [2, 3, 1, 0, 1, 0, 0, 0, 0, 0, 1]
l_triee = [0, 0, 1, 1, 1, 2, 4, 10]
```

_____________

[Sommaire](./../../README.md)