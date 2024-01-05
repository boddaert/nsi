# Exercices

$G =$

```mermaid
    flowchart LR
        0 --> 2
        0 --> 9
        0 --> 4
        0 --> 6
        0 --> 8
        1 --> 3
        1 --> 5
        1 --> 7
        1 --> 9
        4 --> 0
        4 --> 2
        4 --> 8
        5 --> 1
        5 --> 7
        5 --> 9
        6 --> 8
        6 --> 2
        9 --> 3
        9 --> 8
```

## Exercice 1

Ecrire une fonction `parcours_largeur_d_abord(g : dict, s : int)->None` qui prend en paramètre un graphe `g` représenté par liste d'adjacence et un sommet de départ et affiche les sommets du graphe dans l'ordre de traitement du parcours en largeur d'abord.

## Exercice 2

Ecrire une fonction `parcours_profondeur_d_abord(g : dict, s : int)->None` qui prend en paramètre un graphe `g` représenté par liste d'adjacence et un sommet de départ et affiche les sommets du graphe dans l'ordre de traitement du parcours en profondeur d'abord.

## Exercice 3

Cet exercice répond au problème de connexité d'un graphe et permet de répondre si un graphe est connexe ou non.

Un graphe est dit *connexe* si, à partir de chaque sommet, il existe un chemin le reliant à tous les autres sommets du graphe.

a) Dessiner un graphe non connexe d'ordre $5$.

b) A l'issue d'un parcours sur un graphe non connexe, qu'observe t-on dans la liste `est_visite` ?

c) Ecrire une fonction `est_connexe(g : dict)->bool` qui prend en paramètre un graphe `g` et renvoie $True$ s'il est connexe, $False$ sinon.

## Exercice 4

Cet exercice répond au problème de coloration d'un graphe et permet de connaître le nombre chromatique d'un graphe.

Le *nombre chromatique* d'un graphe est le nombre minimal de couleurs nécessaire à colorier les sommets d'un graphe en respectant la contrainte suivante : chaque sommet ne peut être colorié de la même couleur qu'un sommet voisin.

a) Trouver le nombre chromatique du graphe $G$.

b) Trouver le nombre chromatique du graphe de Peterson :

```mermaid
    flowchart LR
        0 --- 1
        0 --- 5
        0 --- 4
        1 --- 8
        1 --- 2
        2 --- 6
        2 --- 3
        3 --- 9
        3 --- 4
        4 --- 7
        5 --- 6
        5 --- 9
        6 --- 7
        7 --- 8
        8 --- 9
```

## Exercice 5

Cet exercice répond au problème de présence d'un cycle dans un graphe et permet de répondre si un cycle est présent dans un graphe ou non.

La stratégie est de parcourir le graphe avec un parcours en profondeur et en coloriant les sommets.

Tous les sommets non visités sont blancs.

Lorsque nous visitons un sommet, nous le colorons en gris. Si, lors du parcours, nous rencontrons un sommet colorié en gris, nous avons un cycle. S'il n'y a plus de voisins, nous colorons le sommet en noir.

Appliquer l'algorithme de présence d'un cycle sur le graphe $G$.



