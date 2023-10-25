# Listes

## I. Définition

Une *liste* est une structure de données linéaire mutable.

Elle contient des données appelées *éléments*.

Une *structure de données* est une structure permettant d'organiser ses données dans l'objectif que le traitement de celles-ci soit efficace.

Une *structure de données linéaire* est une structure de données dans laquelle chaque élément possède une place et dont tous les éléments (sauf le dernier) a un successeur.

Une *structure de données linéaire mutable* est une structure de données linéaire dans laquelle les éléments peuvent être ajoutés, retirés ou modifiés.

En Python, le type `list` est encadré par des crochets :

```python
>>> type([1, 2, 3, 4])
<class = 'list'>
```

Une *liste vide* est une liste ne contenant aucun élément :

```python
>>> type([])
<class = 'list'>
```

Une liste peut contenir des éléments de différents types :

```python
>>> type([True, 0, "coucou"])
<class = 'list'>
```

## II. Opérations sur les listes

### a) Taille

La *taille* d'une liste est le nombre d'élément contenu dans celle-ci.

Elle peut être connue avec la fonction `len()` :

```python
>>> len([1, 2, 3, 4])
4
```

##### Application 1

En utilisant la console Python, trouver la taille des listes suivantes :

a) `[5, 8, 9]`

b) `[]`

### b) Accès au *ième* élément

Nous accédons à un élément de la liste selon son indice (ou sa position) dans la liste.

L'*indice d'un élément* dans la liste est le numéro de place de l'élément.

Nous mettons l'indice de l'élément que nous souhaitons obtenir entre crochets :

```python
>>> liste_entiers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> liste_entiers[2]
3
```

Le premier élément est d'indice $0$.

```python
>>> liste_entiers[0]
1
```

##### Application 2

Donner sans utiliser l'ordinateur, le résultat des instructions suivantes :

a)
```python
>>> liste_entiers[5]
...
```

b)
```python
>>> liste_entiers[1]
...
```

c)
```python
>>> liste_entiers[9]
...
```

##### Application 3

Donner l'instruction permettant d'obtenir :

a) L'élément d'indice $7$.

b) Le dernier élément en utilisant la taille de la liste.

### c) Test d'appartenance

Nous pouvons vérifier si un élément est présent dans une liste à l'aide du mot-clé `in`.

```python
>>> 3 in liste_entiers
True
```

Le test d'appartenance renvoie comme résultat un booléen.

##### Application 4

Vérifier, dans la console Python et à l'aide du mot-clé `in`, si :

a) L'élément $2$ est contenu dans `liste_entiers`.

b) L'élément $0$ est contenu dans `liste_entiers`.

### d) Concaténation

La *concaténation* de deux listes consiste à créer une liste contenant les éléments des deux listes.

Nous pouvons concaténer deux listes en utilisant l'opérateur `+` :

```python
>>> liste_pairs = [0, 2, 4, 6, 8]
>>> liste_impairs = [1, 3, 5, 7, 9]
>>> liste_entiers = liste_pairs + liste_impairs
>>> liste_entiers
[0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
```

##### Application 5

Concaténer :

a) La liste `[2, 8]` avec la chaîne `[1, 7]`.

b) La liste `[1]` avec la liste `[2]` puis avec la liste `[3]`.

### e) Découpage ou *slicing* (hors programme)

Le *slicing* permet d'obtenir une sous-liste à partir d'une liste.

Le slicing en Python s'écrit  : ``liste[debut:fin]``  avec ``debut`` l'indice de la première coupe et ``fin`` l'indice de la seconde coupe (exclue) :

```python
>>> liste_entiers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> mot[2:6]
[3, 4, 5, 6]
```

##### Application 6

Donner sans utiliser l'ordinateur, le résultat des instructions suivantes :

a)
```python
>>> liste_entiers[0:2]
...
```

b)
```python
>>> liste_entiers[0:7]
...
```

## III. Mutabilité

Une valeur est dite *mutable* si elle peut être modifiée.

Les listes sont mutables.

### a) Modification d'élément

Nous pouvons modifier les éléments d'une liste :

```python
>>> liste_entiers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> liste_entiers[3] = 999
>>> liste_entiers
[1, 2, 3, 999, 5, 6, 7, 8, 9]
```

##### Application 7

Essayer à votre tour de modifier la valeur d'indice $5$ de la liste `liste_entiers` en $-999$.

### b) Ajouter un élément

L'ajout d'élément s'effectue en fin de liste avec la méthode `append()` :

```python
>>> liste_entiers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> liste_entiers.append(10)
>>> liste_entiers
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

##### Application 8

Ajouter à la liste `liste_entiers` les valeurs $11$ et $12$.

## IV. Parcours de liste

Un *parcours de liste* consiste à visiter un à un tous les éléments de la liste.

Nous parcourons les listes en utilisant les boucles.

Comme nous connaissons à l'avance la taille d'une liste, nous connaissons à l'avance le nombre de tour de boucle nécessaire au parcours : Nous utilisons donc la boucle `for`.

Il existe deux façons d'utiliser la boucle `for` pour parcourir les listes :

- Le parcours par indice.

- Le parcours par élément.

### a) Parcours par indice

Dans le parcours par indice, nous parcourons les éléments indice par indice :

```python
1. liste_entiers = [1, 2, 3, 4]
2. for i in range(len(liste_entiers)) :
3.   entier = liste_entiers[i]
```

Trace d'exécution du programme donné ci-dessus:

| Numéro de ligne | Valeur affectée à $i$ | Valeur affectée à $entier$ |
| :---: | :---: | :---: |
| $1$ | / | / |
| $2$ | $0$ | / |
| $3$ | $0$ | $1$ |
| $2$ | $1$ | $1$ |
| $3$ | $1$ | $2$ |
| ... | ... | ... |

##### Application 8

Compléter la trace d'exécution précédente.

### b) Parcours par élément

Dans le parcours par élément, nous parcourons élément par élément :

```python
1. liste_entiers = [1, 2, 3, 4]
2. for elt in liste_entiers :
3.   entier = elt
```

| Numéro de ligne | Valeur affectée à $elt$ | Valeur affectée à $entier$ |
| :---: | :---: | :---: |
| $1$ | / | / |
| $2$ | $1$ | / |
| $3$ | $1$ | $1$ |
| $2$ | $2$ | $1$ |
| $3$ | $2$ | $2$ |
| ... | ... | ... |


##### Application 9

Compléter la trace d'exécution précédente.
___________

[Feuille d'exercice](./Exercices/Exercices_listes.md)

___________

[Sommaire](./../README.md)