# Algorithmes gloutons

## I. Introduction

Résoudre un problème d'optimisation combinatoire est facile : il suffit de calculer toutes les solutions possibles et de maximiser ou minimiser selon le critère sur cet ensemble de solutions.

Malheureusement, en informatique, une contrainte s'impose : la puissance actuelle des ordinateurs.

Il fau donc trouver une autre stratégie.

##### Application 1

a) Pour un problème du voyageur de commerce à onze villes, combien le voyageur a t-il de choix quant à la ville de départ ? 

b) Depuis une ville de départ, combien le voyageur a t-il de choix quant à la seconde ville à visiter ?

c) Combien y a t-il d'itinéraires possibles pour ce problème à onze villes ?

d) Combien y a t-il d'itinéraires possibles pour ce problème à $n$ villes ?

e) Est-il possible pour un ordinateur de concevoir une solution en temps raisonnable avec cette stratégie ?

## II. Définitions

Les *algorithmes gloutons* sont des algorithmes répondant à un problème d'optimisation combinatoire.

Les algorithmes gloutons utilisent la stratégie gloutonne.

La *stratégie gloutonne* consiste, par une suite de choix, à sélectionner à chaque étape le choix qui est le meilleur localement.

Cette stratégie ne traite qu'un seul sous-problème local et indépendant des autres à la fois :

![image](./img/strategie_gloutonne.png)

> Cette stratégie ne fournit pas forcément la meilleure solution. Nous disons de la stratégie gloutonne qu'elle donne une solution "satisfaisante".

## II. Étude de cas : Le voyageur de commerce

##### Application 2

Proposer l'idée de la stratégie gloutonne pour le problème du voyageur de commerce.

##### Application 3

Voici ci-dessous l'algorithme répondant au problème du voyageur de commerce utilisant la stratégie gloutonne :

```
Algorithme voyageur_de_commerce_glouton
Entrées : l_villes une liste de villes (une ville étant représentée par un tuple de coordonnées) et ville_depart une ville de départ
Sorties : Un itinéraire satisfaisant

itinéraire <- [ville_depart]
TantQue taille(itinéraire) != taille(l_villes), faire :
    i_ville_courante <- dernière ville visitée
    min_distance <- +∞
    Pour i allant de 0 à taille(l_villes), faire :
        Si i n'est pas dans itinéraire, alors :
            distance <- calcul de la distance euclidienne entre l_villes[i_ville_courante] et l_villes[i]
            Si distance < min_distance, alors :
                min_distance <- distance
                prochaine_ville <- i
    Ajouter à itinéraire : l_villes[i]
Ajouter à itinéraire : ville_depart
Renvoyer itinéraire
```

Sans utiliser l'ordinateur, donner le résultat renvoyé par l'algorithme s'il prend comme entrées : `l_villes = [(2,3), (4,7), (10,1), (3,8), (1, 0), (10, 9)]` et `ville_depart = 0`.

##### Application 4

En vous apuyant sur l'algorithme ci-dessus, écrire une fonction `voyageur_de_commerce_glouton(l_villes : list)->list` qui prend en paramètre une liste de villes, une ville étant modélisée par un tuple de coordonnées et une ville de départ et renvoie sous forme de liste, en utilisant la stratégie gloutonne, un ordre de visite satisfaisant des villes.

```python
>>> voyageur_de_commerce([(2,3), (4,7), (10,1), (3,8), (1, 0), (10, 9)],3)
[3, 1, 0, 4, 2, 5, 3]
```

_________________

[Exercices](./Exercices/Exercices_algorithmes_gloutons.md)

_________________

[Sommaire](./../../README.md)