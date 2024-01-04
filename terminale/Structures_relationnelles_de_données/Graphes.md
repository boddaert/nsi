# Graphes

## I. Définitions

Une *structure relationnelle de données* est une structure dans laquelle les données sont en relations entre elles.

Un *graphe* est une structure relationnelle de données.

Un *graphe* est un ensemble de noeuds appelés *sommets* reliés entre eux ou non par des liens.

##### Application 1

Donner des exemples informatiques ou de la vie quotidienne de structures pouvant se présenter sous la forme d'un graphe.

## II. Graphes non orientés

### a) Définition

Dans un graphe dit *non-orienté*, les liens fonctionnent dans les deux sens et sont appelés *arêtes*.

### b) Type abstrait

Un graphe non-orienté $G$ est un couple $(V,E)$ où $V$ est un ensemble finis de sommets et $E$ est un ensemble finis de $V\times V$ symétrique d'arêtes.

### c) Représentation sagitalle

Par exemple, le graphe $(\left\{0, 1, 2, 3, 4, 5\right\},\left\{(0,1), (0,2), (0,3), (0,4), (3,4), (2,3), (2,5), (4,1)\right\})$ peut être représenté sagitallement :

$\{ 1+1=2$

```mermaid
    flowchart LR
        0 --- 1
        0 --- 2
        0 --- 3
        0 --- 4
        3 --- 4
        2 --- 3
        2 --- 5
        4 --- 1
```

## III. Graphes orientés

Dans un graphe dit *orienté*, les liens fonctionnent dans un unique sens (et sont alors représentés d'une flèche) et sont appelés *arcs*.

## IV. Graphes pondérés

## V. Propriétés

## VI. Représentations en machine

## VII. Algorithmes