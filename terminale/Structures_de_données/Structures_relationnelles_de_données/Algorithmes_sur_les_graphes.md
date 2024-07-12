# Algorithmes sur les graphes

## I. Problèmes algorithmiques

Plusieurs situations quotidiennes sont modélisables par des graphes comme le réseau internet, le réseau routier ou encore les réseaux sociaux. 

Et la théorie des graphes, réunissant la modélisation de graphes et l'ensemble des problèmes s'appliquant sur ceux-ci, a été inventé par le mathématicien Leonhard Euler lors du problème des sept ponts de Königsberg.

<img src="./img/leonhard_euler.jpg" width=500>

La théorie des graphes a été depuis longuement étudiée par les mathématiciens et informaticiens de l'Histoire. 

L'un des problème les plus connus est le problème du chemin de poids minimal où il s'agit de trouver un chemin de poids minimal dans un graphe pondéré reliant un sommet de départ à un sommet de destination. 

Les mathématiciens Richard Bellman et Lester Randolph Ford junior ont publié en 1956 l'algorithme de Bellman-Ford résolvant le problème de chemin de poids minimal.

Suivis de près par l'informaticien néerlandais Edsger Dijkstra qui a publié en 1959 sa propre version.

Ces algorithmes sont utilisés dans les protocoles RIP et OSPF et permettent entre autre de trouver le chemin le plus rapide dans le routage internet entre deux machines.

Beaucoup d'autres problèmes existent en théorie des graphes comme la connexité d'un graphe, la recherche d'un cycle dans un graphe, la résolution automatique de labyrinthes, la coloration d'un graphe et bien d'autres...

La théorie des graphes a permis le développement de la recherche dans énormément de domaines encore aujourd'hui comme l'intelligence artificielle et ses réseaux de neurones.

## II. Parcours de graphes

### a) Définition

Dans chacun de ces algorithmes, il sera nécessaire de parcourir les sommets du graphe.

> [!IMPORTANT]
> Un *parcours de graphe* consiste à visiter tous les sommets du graphe une et une seule fois en respectant les relations d'adjacence dans le but de leur appliquer un traitement.

Il existe deux types de parcours de graphe : le **parcours en largeur d'abord** et le **parcours en profondeur d'abord**.

### b) Parcours en largeur d'abord

> [!IMPORTANT]
> Le *parcours en largeur d'abord* est un parcours de graphe par niveau de voisinage. Il consiste à visiter tous les voisins du sommet de départ, puis tous les voisins des voisins, etc ...

<a name="exemple_larg"></a>
> [!TIP]
> Par exemple sur le graphe suivant :
>
> ```mermaid
>     flowchart LR
>         0 --> 1
>         1 --> 0
>         0 --> 2
>         2 --> 0
>         3 --> 1
>         3 --> 4
>         4 --> 3
>         1 --> 4
>         0 --> 5
>         5 --> 6
>         6 --> 5
> ```
>
> L'ordre de traitement des sommets en partant du sommet $0$ selon le parcours en largeur d'abord est : $0$, $1$, $2$, $5$, $4$, $6$ et $3$.

#### <ins>Application 1</ins>

Donner l'ordre de traitement des sommets en partant de $0$ selon le parcours en largeur d'abord du graphe $G$ donné en [Exercices](./Exercices/Exercices_algorithmes_sur_les_graphes.md).

### b) Algorithme du parcours en largeur d'abord

L'algorithme du parcours en largeur d'abord sur un graphe s'écrit très facilement avec une File (cf : [Files](./../Structures_linéaires_de_données/Files.md)) :

```algo
Algorithme : parcours_largeur_d_abord(g, s):
Entrées : g un graphe représenté par une liste d'adjacence, s un entier
Sorties : Rien

est_visite <- [s]
f <- File()
f.enfile(s)
Tant que f n'est pas vide, faire :
    v <- f.defile()
    Traiter(v)
    Pour w tous les voisins de v, faire :
        Si w n'a pas été visité, alors :
            f.enfile(w)
            est_visite.append(w)
```

#### <ins>Application 2</ins>

Dérouler à la main sur papier et en dessinant les files l'algorithme du parcours en largeur d'abord sur le graphe donné en [exemple](#exemple_larg) afin de vérifier l'ordre de traitement.

### c) Parcours en profondeur d'abord

> [!IMPORTANT]
> Le *parcours en profondeur d'abord* est un parcours de graphe par profondeur de voisinage. Il consiste à visiter en profondeur d'abord le voisin d'un sommet avant de passer aux voisins suivants.

<a name="exemple_prof"></a>
> [!TIP]
> Par exemple sur le graphe suivant :
> ```mermaid
>     flowchart LR
>         0 --> 1
>         1 --> 0
>         0 --> 2
>         2 --> 0
>         3 --> 1
>         3 --> 4
>         4 --> 3
>         1 --> 4
>         0 --> 5
>         5 --> 6
>         6 --> 5
> ```
>
> L'ordre de traitement des sommets en partant du sommet $0$ selon le parcours en largeur d'abord est : $0$, $1$, $4$, $3$, $2$, $5$ et $6$.

#### <ins>Application 3</ins>

Donner l'ordre de traitement des sommets en partant de $0$ selon le parcours en profondeur d'abord du graphe $G$ donné en [Eexercices](./Exercices/Exercices_algorithmes_sur_les_graphes.md).

### d) Algorithme du parcours en profondeur d'abord

L'algorithme du parcours en profondeur d'abord sur un graphe s'écrit très facilement avec une Pile (cf : [Piles](./../Structures_linéaires_de_données/Piles.md)) :

```algo
Algorithme : parcours_largeur_d_abord(g, s):
Entrées : g un graphe représenté par une liste d'adjacence, s un entier
Sorties : Rien

est_visite <- [s]
p <- Pile()
p.empile(s)
Tant que p n'est pas vide, faire :
    v <- p.depile()
    Traiter(v)
    Pour w tous les voisins de v, faire :
        Si w n'a pas été visité, alors :
            p.empile(w)
            est_visite.append(w)
```

#### <ins>Application 4</ins>

Dérouler à la main sur papier et en dessinant les piles l'algorithme du parcours en largeur d'abord sur le graphe donné en [exemple](#exemple_prof) afin de vérifier l'ordre de traitement.

_______________

[Exercices](./Exercices/Exercices_algorithmes_sur_les_graphes.md)

_______________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 