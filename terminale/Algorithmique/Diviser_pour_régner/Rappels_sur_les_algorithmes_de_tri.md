# Rappels sur les algorithmes de tri

## I. Généralités

### a) Définitions

> [!IMPORTANT]
> *Trier* un ensemble de valeurs (par exemple une liste), c'est obtenir une permutation de cet ensemble en vérifiant plusieurs contraintes.

> [!TIP]
> Par exemple : 
>
> `l`, une liste Python d'entiers non triée et `l_triee` la permutation de `l` triée vérifie les contraintes suivantes :
>
> 1. La taille de `l` est égale à la taille de `l_triee`.
>
> 2. Tous les éléments contenus dans `l` sont présents dans `l_triee`.
>
> 3. Pour chaque élément de `l` et de `l_triee`, le nombre d'occurence des éléments est le même.
>
> 4. La liste `l_triee` obtenue respecte la relation d'ordre (croissant/décroissant).

### b) Spécificités

> [!IMPORTANT]
> - Un tri est dit *stable* s'il préserve, à l'issue du tri, le même ordre sur des éléments égaux.

> [!IMPORTANT]
> - Un tri est dit *en place* s'il modifie directement en mémoire la structure de données sur laquelle s'applique le tri.

### c) Applications

Le tri en informatique permet de réduire les coûts algorithmiques de beaucoup d'algorithmes comme la recherche d'un élément dans une liste ou le calcul de la médiane.

## II. Tri par sélection

### a) Principe

L'algorithme du tri par sélection est un algorithme de tri par comparaison.

Dans cet algorithme, la liste est parcourue de la gauche vers la droite, en maintenant sur la gauche une partie triée :

<img src="./img/schema_tri.png" width=800>

Il y a donc une partie gauche triée et vide au lancement du programme et une partie droite non triée.

Le principe du tri par sélection est le suivant :

- Rechercher le plus petit élément de la partie droite non triée, et l'échanger avec le premier élément de la partie droite non triée.

- Le premier élément de la partie droite non triée est maintenant trié, nous l'incluons dans la partie gauche triée.

- Continuer de cette façon jusqu'à ce que la taille de la partie gauche triée soit égale à la taille de la liste.

> [!TIP]
> Par exemple :
>
> <img src="./img/animation_tri_selection.gif" width=100>

#### <ins>Application 1</ins>

Écrire une fonction ``minimum(l : list, i : int)->int`` prenant en paramètre une liste d'entiers et un entier et renvoyant l'indice de l'élément le plus petit dans la tranche `l[i:]`.

#### <ins>Application 2</ins>

Écrire en python une fonction ``tri_selection(l : list)->None`` prenant en paramètre une liste d'entiers et qui trie dans l'ordre croissant les éléments de ``l``.

Le tri par sélection est un tri en place donc la fonction ``tri_selection()`` ne renvoie rien.

#### <ins>Application 3</ins>

Dans cette question, nous souhaitons déterminer la complexité temporelle de cet algorithme en comptant le nombre de comparaisons.

a) Proposer, pour une liste de longueur $n$, une estimation du nombre de fois que la fonction ``tri_selection()`` exécute la fonction ``minimum()``.

Trouver cette estimation en déroulant la fonction à la main sur papier.

b) Modifier la fonction ``minimum()`` pour qu'elle affiche le nombre de comparaisons qu'elle effectue.

c) À partir de l'affichage, comment retrouver le nombre total de comparaisons effectués par la fonction ``tri_selection()`` ?

d) Pour une liste de longueur $n$, estimer le nombre de comparaisons effectuées par la fonction `tri_selection()`.

## III. Tri par insertion

### a) Principe

L'algorithme du tri par insertion est un algorithme de tri par comparaison.

Dans cet algorithme, la liste est parcourue de la gauche vers la droite, en maintenant sur la gauche une partie triée :

<img src="./img/schema_tri.png" width=800>

Il y a donc une partie gauche triée et vide au lancement du programme et une partie droite non triée.

Le principe du tri par insertion est le suivant :

- Insérer le premier élément de la partie droite non triée à sa bonne place dans la partie gauche triée.

- Continuer de cette façon jusqu'à ce que la taille de la partie gauche triée soit égale à la taille de la liste.

> [!TIP]
> Par exemple :
> <img src="./img/animation_tri_insertion.gif" width=300>

#### <ins>Application 4</ins>

Voici ci-dessous l'algorithme de la fonction ``inserer(l : list, i : int)->None`` permettant d'insérer l'élément d'indice ``i`` dans la partie gauche triée :

```
Algorithme : insérer(l,i)
Entrées : l une liste d'entiers et i un indice
Sorties : Rien

elt <- l[i]
j <- i
Tant que j > 0 et elt <=  l[j-1], faire :
    l[j] <- l[j-1]
    j <- j - 1
l[j] <- elt
```

Réécrire, en python, la fonction ``inserer( l : list , i : int)->None`` 

#### <ins>Application 5</ins>

Écrire en python une fonction ``tri_insertion(l : list)->None`` prenant en paramètre une liste ``l`` et trie dans l'ordre croissant les éléments de ``l``.

Le tri par insertion est un tri en place donc la fonction ``tri_insertion()``ne renvoie rien.

#### <ins>Application 6</ins>

Dans cette question, nous souhaitons déterminer la complexité de cet algorithme.

a) Donner, pour la liste `l = [5, 6, 2, 1, 3, 4]`, le nombre de fois que la fonction ``tri_insertion()`` exécute la fonction `inserer()`. 

Trouver cette estimation en executant le code à la main sur papier.

b) Pour une liste déjà triée croissante, par exemple :``[1, 2, 3, 4, 5, 6, 7, 8]``, estimer le nombre de comparaisons effectuées par la fonction `tri_insertion()`.

c) Pour une liste strictement décroissante, par exemple : ``[8, 7, 6, 5, 4, 3, 2, 1]``, estimer le nombre de comparaisons effectuées par la fonction `tri_insertion()`.

d) Modifier la fonction `inserer()` pour qu'elle affiche le nombre de comparaisons qu'elle effectue.

e) À partir de l'affichage, donner le nombre de comparaisons total effectués par la fonction ``tri_insertion()`` pour les listes `[ 1, 2, 3, 4, 5, 6, 7, 8]` et `[ 8, 7, 6, 5, 4, 3, 2, 1]`.

f) Peut-il y avoir une meilleure complexité de l'algorithme du tri par insertion que celle sur une liste déjà triée ?

g) Comparer la complexité du tri par sélection avec la complexité du tri par insertion.

__________________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 
