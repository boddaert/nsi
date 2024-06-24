# Tri par insertion

## I. <a name="algorithme"></a>Algorithme

L'algorithme du tri par insertion est un algorithme de tri par comparaison.

Dans cet algorithme, nous parcourons la liste de la gauche vers la droite, en maintenant sur la gauche une partie triée :

![image](./img/schema_tri.png)

Il y a donc une partie gauche triée et vide au lancement du programme et une partie droite non triée.

Le principe du tri par insertion est le suivant :

- Insérer le premier élément de la partie droite non triée à sa bonne place dans la partie gauche triée.

- Continuer de cette façon jusqu'à ce que la taille de la partie gauche triée soit égale à la taille de la liste.

Voici, par exemple, une animation décrivant le principe du tri par insertion :

Nous parcourons la liste de la gauche vers la droite, en maintenant sur la gauche une partie triée :

![animation](./img/animation_tri_insertion.gif)

##### Application 1

Voici ci-dessous l'algorithme de la fonction ``inserer(l : list, i : int)->None`` permettant d'insérer l'élément d'indice ``i`` dans la partie gauche triée :

```
Algorithme : insérer(l,i)
Entrées : l une liste d'entiers et i un indice
Sorties : Rien

elt <- l[i]
j <- i
Tant que j > 0 et l[j-1] >=  elt, faire :
    l[j] <- l[j-1]
    j <- j - 1
l[j] <- elt
```

Réécrire, en python, la fonction `inserer( l : list , i : int)->None`.

> Cette fonction devra remplacer la seconde comparaison par la fonction `compare()`.

##### Application 2

Écrire en python une fonction `tri_insertion(l : list)->None` qui en paramètre une liste ``l`` et trie dans l'ordre croissant les éléments de `l`.

> Le tri par insertion est un tri en place donc la fonction `tri_insertion()` ne renvoie rien.

## II. Complexité

L'objectif est de déterminer le coût algorithmique en temps de l'algorithme du tri par insertion.

Pour cela, nous allons compter le nombre d'opérations coûteuses (les comparaisons).

La fonction `tri_insertion()` exécute un appel à la fonction `inserer()`, il faut donc compter préalablement le nombre de comparaisons effectuées par la fonction `inserer()`.

### a) Étude de la fonction `inserer()`

La fonction `inserer()` effectue des appels à la fonction `compare()`.

La fonction `compare()` comptabilise **une** comparaison : calculons alors le nombre d'appels effectués à la fonction `compare()`.

##### Application 3

a) Modifier la fonction ``inserer()`` pour qu'elle affiche le nombre d'appels effectué à la fonction `compare()`.

b) Qu'est-il affiché lorsque j'exécute la fonction `inserer()` avec comme arguments : `l = [1, 2, 3, 4, 0, 9, 8, 6, 7]` et `i = 4` ?

c) Qu'est-il affiché lorsque j'exécute la fonction `inserer()` avec comme arguments : `l = [1, 2, 3, 4, 5, 9, 8, 6, 7]` et `i = 4` ?

d) En déduire de la question b), pour une liste de longueur $n$ et avec $i = n - 1$, le nombre maximal de comparaisons pouvant être effectuées.

Il s'agit du scénario le plus défavorable : le pire des cas.

e) En déduire de la question c) le nombre minimal de comparaisons pouvant être effectuées.

Il s'agit du scénario le plus favorable : le meilleur des cas.

### b) Étude de la fonction `tri_insertion()`

La fonction `tri_insertion()` effectue des appels à la fonction `inserer()`.

Le nombre total de comparaison de la fonction `tri_insertion()` est la somme des appels à la fonction `compare()`.

> Rappel : $somme\quad des\quad termes\quad d'une\quad suite\quad arithmétique\quad =\quad nombre\quad de\quad termes \times \dfrac{(premier\quad terme\quad +\quad dernier\quad terme)}{2}$

##### Application 4

a) Qu'est-il affiché lorsque j'exécute la fonction `tri_insertion()` pour une liste triée décroissante de longueur $5$ ? $10$ ? $20$ ?

b) Qu'est-il affiché lorsque j'exécute la fonction `tri_insertion()` pour une liste déjà triée croissante de longueur $5$ ? $10$ ? $20$ ?

### c) Généralisation du coût algorithmique 

Pour une liste de taille $n$ donnée, le coût algorithmique temporel est égale à $\dfrac{n(n-1)}{2}$ pour le pire des cas et à $(n-1)$ dans le meilleur des cas.

Ce qui est de l'ordre de $O(n²)$ donc le tri par insertion possède un coût quadratique (voir courbes : [complexité](./../Optimisation/Complexité.md)).

##### Application 5

Exprimer en une phrase si l'algoritme du tri par insertion est préférable à utiliser que l'algorithme du tri par sélection.

## III. Terminaison

Prouver qu'un algorithme se termine, c'est trouver son variant de boucle (voir [Preuve de terminaison](./../Optimisation/Preuve_de_terminaison.md)).

Étant donné que l'algorithme de tri par insertion utilise l'algorithme `inserer` et que celui-ci est doté d'une boucle `while`, affirmer que l'algorithme `tri_insertion` nécessite de vérifier que l'algorithme `inserer` se termine.

##### Application 6

En relisant [I. Algorithme](#algorithme) de cette leçon, repérer un variant de boucle dans l'algorithme `inserer` afin d'affirmer qu'il se termine bien.

##### Application 7

Expliquer pourquoi la preuve de terminaison de l'algorithme `inserer` suffit à dire que l'algorithme `tri_insertion` se termine.

## IV. Correction

Prouver qu'un algorithme est correct, c'est trouver son invariant de boucle (voir [Preuve de correction](./../Optimisation/Preuve_de_correction.md)).

L'invariant de boucle de l'algorithme du tri par insertion est : "Chaque élément $e$ au moment de l'insertion dans la partie gauche triée à l'indice $i$ indique que l'élement à l'indice $i-1$ est inférieur à $e$ et que l'élément d'indice $i+1$ est supérieur à $e$".

Il s'agit bien d'une propriété vraie à l'entrée de la boucle, à chaque itération de boucle et à la sortie de la boucle.

L'algorithme du tri par insertion admet un invariant de boucle et est donc correct.

_________________

[Sommaire](./../../README.md)