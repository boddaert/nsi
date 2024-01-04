# Diviser pour régner

## I. Introduction

Alice se décide à ranger ses bandes déssinées par ordre alphabétique de titre.

Le travail est fastidieux car elle en possède une bonne centaine. Elle appelle son frère Basile à la rescousse pour aller plus vite.

Ils se partagent les bande déssinées et chacun d'eux trie sa moitié, sous la forme d'une pile de BD. 

Ensuite, Alice et Basile rangent les bandes déssinées dans la bibliothèque en fusionnant les deux piles : c'est-à-dire en prenant à chaques fois celle des deux BD au sommet des deux piles qui vient avant l'autre dans l'ordre alphabétique.

A deux, ils ont été plus rapide qu'Alice toute seule. On imagine alors qu'une troisième personne les aurait aidé à encore diminuer le temps nécessaire à ranger les BD.

*Question : Combien de personnes faudrait-il pour que le temps nécessaire au rangement des BD de la bibliothèque soit le plus petit possible ?*

## II. Définitions

Le principe "diviser pour régner" consiste à :

1. *Diviser* : décomposer un problème en un ou plusieurs sous-problèmes de même nature mais plus petits donc plus faciles à résoudre.

2. *Regner* : résoudre ces sous-problèmes, éventuellement en les décomposant à leur tour récursivement en problèmes plus petits encore jusqu'à obtenir des problèmes triviaux.

3. *Combiner* : déduire, par les solutions des sous-problèmes, la solution du problème initial.

## III. Tri Fusion

### a) Trier une liste 

Le tri fusion, comme le tri par sélection ou insertion est un algorithme de tri. Il permet de trier les éléments d'une liste.

C'est-à-dire, d'obtenir une permutation de la liste vérifiant :

- La taille de la liste d'origine est égale à la taille de la liste obtenue.

- Tous les éléments contenus dans la liste d'origine sont présents dans la liste obtenue.

- Pour chaque élément de la liste d'origine et de la liste obtenue, le nombre d'occurence est le même.

- La liste obtenue respecte la relation d'ordre (croissant/décroissant).

### b) Principe

Le tri fusion est un tri utilisant le principe "Diviser pour régner".

1. Diviser :

Nous séparons les éléments de la liste en deux listes de même taille, à un élément près.

2. Régner/Combiner :

Nous répétons jusqu'à obtenir des listes à au plus $1$ élément.

Une liste à $1$ élément étant implicitement triée.

Puis, nous fusionnons les listes triées en liste triée, ce qui est facile car il suffit d'examiner le premier élément de chaque liste.

### c) Algorithme

```
Algorithme de Tri fusion :

- Si la longueur de la liste est supérieure à 2 :

    + Découper en deux (au milieu) la liste en deux sous-listes.

    + Ré-appliquer l'algorithme du tri fusion sur les deux sous-listes obtenues.

    + Fusionner les deux sous-listes triées en une liste triée.

    + Renvoyer la liste fusionnée.

- Si la liste contient un seul élément :

    + Renvoyer cette liste (car elle est implicitement triée).
```

### d) Complexité temporelle

La complexité temporelle de l'algorithme du tri fusion est $O(n\log_2 n)$.

Ce qui est bien plus performant que les algorithmes de tri vus en Première qui ont une complexité temporelle de $O(n^2)$.

### e) Programme

La fonction ``decoupe()`` représente l'étape "Diviser".

La fonction ``fusion()`` représente l'étape "Régner".

La fonction ``tri_fusion()`` représente l'étape "Combiner".

##### Application 1

La fonction `decoupe()` prend en paramètre une liste et renvoit deux listes. La fonction `decoupe()` sépare une liste en deux listes ayant le même nombre d'éléments, à un près.

a) Quelles sont les deux listes renvoyées par la fonction ``decoupe()`` lorsquenous lui donnons en paramètre la liste ``[5, 1, 3, 4, 2]`` ?

b) Ecrire en Python, la fonction ``decoupe(l : list) -> (list , list)``.

##### Application 2

La fonction `fusion()` prend en paramètre deux listes triées et renvoit une liste triée, fusion des listes passées en paramètre.

a) Quelle liste est renvoyée par la fonction ``fusion()`` lorsque nous lui donnons en paramètres les listes ``[3, 5, 8]`` et ``[2, 4, 9]`` ?

b) Ecrire en Python, la fonction récursive ``fusion(l1 : list, l2 : list) -> list``.

##### Application 3

a) La fonction ``tri_fusion()`` est récursive. Quelle est la condition d'arrêt à cette fonction ?

b) Ecrire en Python, une fonction `tri_fusion(l : list) -> list` prenant en paramètre une liste et renvoyant la liste triée en utilisant le principe du tri fusion.

______________

[Feuille d'exercice](./Exercices/Exercices_diviser_pour_régner.md)

______________

[Sommaire](./../README.md)

