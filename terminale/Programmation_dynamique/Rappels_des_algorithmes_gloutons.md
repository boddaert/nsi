# Rappels des algorithmes gloutons 

## I. Généralités

### a) Complexités des algorithmes répondant à un problème d'optimisation combinatoire

Résoudre un problème d'optimisation combinatoire est facile : il suffit de calculer toutes les solutions possibles et de maximiser ou minimiser selon le critère de cet ensemble de solutions.

Malheureusement, en informatique, une contrainte s'impose : la puissance actuelle des ordinateurs.

Prenons un exemple de problème d'optimisation combinatoire : le voyageur de commerce.

Depuis une ville de départ, le voyageur cherche à visiter toutes les villes comprises dans le problème une et une seule fois et finis son tour par la ville de départ.

Il existe plusieurs itinéraires et le voyageur cherche à minimiser la distance de ses solutions.

##### Application 1

a) Démontrer que le problème du voyageur de commerce s'agit bien d'un problème d'optimisation combinatoire.

b) Pour un problème du voyageur de commerce à onze ville, combien le voyageur a t-il de choix quant à la ville de départ ? 

c) Depuis une ville de départ, combien le voyageur a t-il de choix quant à la seconde ville à visiter ?

d) Combien y a t-il d'itinéraires possibles pour ce problème à onze villes ?

e) Combien y a t-il d'itinéraires possibles pour ce problème à $n$ villes ?

f) Est-il possible pour un ordinateur de concevoir une solution en temps raisonnable avec cette stratégie ?

### b) Définitions

Les *algorithmes gloutons* sont des algorithmes répondant à un problème d'optimisation combinatoire.

Les algorithmes gloutons utilisent la stratégie gloutonne.

La *stratégie gloutonne* consiste, par une suite de choix, à sélectionner à chaque étape le choix qui est le meilleur localement.

Cette stratégie ne traite qu'un seul sous-problème local indépendant des autres à la fois :

![image](./../../première/Algorithmes_gloutons/img/strategie_gloutonne.png)

> Cette stratégie ne donner pas forcément pas la meilleure solution. Nous disons de la stratégie gloutonne qu'elle donne une solution satisfaisante.

##### Application 2

a) Donner l'idée de la stratégie gloutonne utilisée pour le problème de rendu de monnaie.

b) Donner l'idée de la stratégie gloutonne utilisée pour le problème du voyageur de commerce.

##### Application 3

Écrire une fonction `rendu_de_monnaie_glouton(l_pieces : list, somme_a_rendre : int)->list` qui prend en paramètre un système monnaitaire sous forme de liste et un entier et renvoie, en utilisant la stratégie gloutonne, une liste des pièces satisfaisante à rendre.

```python
>>> rendu_de_monnaie_glouton([1, 2, 5, 10, 20, 50], 34)
[20, 10, 2, 2]
```

##### Application 4

Écrire une fonction `voyageur_de_commerce_glouton(l_villes : list)->list` qui prend en paramètre une liste de villes, une ville étant représenté par un tuple de coordonnées et renvoie, en utilisant la stratégie gloutonne, sous forme de liste un ordre de visite satisfaisant des villes.

```python
>>> voyageur_de_commerce([(2,3), (4,7), (10,1), (3,8), (1, 0), (10, 9)])
[(4, 7), (3, 8), (2, 3), (1, 0), (10, 1), (10, 9)]
```

_________________

[Sommaire](./../README.md)