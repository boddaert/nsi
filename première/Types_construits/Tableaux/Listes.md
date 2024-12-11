# Listes

## I. Définitions

> [!IMPORTANT]
> Une *liste* est une structure linéaire mutable de données.
>
> Elle contient des données appelées *éléments*.

> [!IMPORTANT]
> Une *structure de données* est une structure permettant d'organiser ses données dans l'objectif que le traitement de celles-ci soit efficace.

> [!IMPORTANT]
> Une *structure linéaire de données* est une structure de données dans laquelle chaque élément possède une place et dont tous les éléments (sauf le dernier) a un successeur.

> [!IMPORTANT]
> Une *structure linéaire mutable de données* est une structure de données linéaire dans laquelle les éléments peuvent être ajoutés, retirés ou modifiés.

## II. En Python

### a) Spécificités

En Python, les listes sont définies entre crochets (`[` `]`).

> [!TIP]
> Par exemple :
> ```python
> [1, 2, 3, 4]
> ```

Les listes sont de type `list`.

> [!TIP]
> Par exemple :
> ```python
> >>> type([1, 2, 3, 4])
> <class 'list'>
> ```

> [!IMPORTANT]
> Une *liste vide* est une liste ne contenant aucun élément.

> [!TIP]
> Par exemple :
> ```python
> >>> type([])
> <class 'list'>
> ```

Une liste peut contenir des éléments de différents types.

> [!TIP]
> Par exemple :
> ```python
> [True, 0, "coucou"])
> ```

### b) Opérations

#### 1. Taille

> [!IMPORTANT]
> La *taille* d'une liste est le nombre d'élément contenu dans celle-ci.

Elle peut être connue avec la fonction `len()` (pour *length* en anglais).

> [!TIP]
> Par exemple :
> ```python
> >>> len([1, 2, 3, 4])
> 4
> ```

#### <ins>Application 1</ins>

En utilisant la console Python, trouver la taille des listes suivantes :

1. `[5, 8, 9]`

2. `[]`

#### 2. Accès au *ième* élément

Les éléments d'une liste sont indicés, c'est-à-dire qu'ils possèdent chacun un numéro de position dans la liste.

> [!IMPORTANT]
> L'*indice d'un élément* dans la liste est le numéro de position de l'élément.

L'accès à un élément d'indice $i$ s'effectue en l'écrivant entre crochets.

> [!TIP]
> Par exemple :
> ```python
> >>> entiers = [1, 2, 3, 4]
> >>> entiers[2]
> 3
> ```

> [!WARNING]
> Le premier élément est d'indice $0$.

> [!TIP]
> Par exemple :
> ```python
> >>> entiers[0]
> 1
> ```

#### <ins>Application 2</ins>

Donner sans utiliser l'ordinateur, le résultat des instructions suivantes :

1. Instruction 1
```python
>>> entiers[3]
...
```

2. Instruction 2
```python
>>> entiers[1]
...
```

#### <ins>Application 3</ins>

Expliquer l'erreur suivante :

```python
>>> entiers = [1, 2, 3, 4]
>>> entiers[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

#### <ins>Application 4</ins>

Donner l'instruction permettant d'obtenir :

1. L'élément d'indice $2$.

2. Le dernier élément en utilisant la taille de la liste.

#### 3. Test d'appartenance

> [!IMPORTANT]
> Le *test d'appartenance* permet de savoir si une valeur est présente dans une autre.

Nous pouvons vérifier si un élément est présent dans une liste à l'aide du mot-clé `in`.

> [!TIP]
> Par exemple :
> ```python
> >>> 3 in entiers
> True
> ```

> Le test d'appartenance renvoie comme résultat un booléen.

#### <ins>Application 5</ins>

Vérifier, dans la console Python et à l'aide du mot-clé `in`, si :

1. L'élément $2$ est contenu dans `entiers`.

2. L'élément $5$ est contenu dans `entiers`.

#### 4. Concaténation

> [!IMPORTANT]
> La *concaténation* de deux listes consiste à assembler l'une après l'autre les listes pour n'en former qu'une.

La concaténation de deux listes en Python s'effectue à l'aide de l'opérateur `+`.

> [!TIP]
> Par exemple :
> ```python
> >>> pairs = [0, 2, 4, 6, 8]
> >>> impairs = [1, 3, 5, 7, 9]
> >>> entiers = pairs + impairs
> >>> entiers
> [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
> ```

#### <ins>Application 6</ins>

Concaténer :

1. La liste `[2, 8]` avec la chaîne `[1, 7]`.

2. La liste `[1]` avec la liste `[2]` puis avec la liste `[3]`.

#### 5. Découpage ou *slicing* (hors programme)

> [!IMPORTANT]
> Le *slicing* permet d'obtenir une sous-liste à partir d'une liste.

Le slicing en Python s'écrit  : ``chaine[debut:fin]``  avec ``debut`` l'indice de la première coupe et ``fin`` l'indice de la seconde coupe (exclue).

> [!TIP]
> Par exemple :
> ```python
> >>> entiers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
> >>> entiers[2:6]
> [3, 4, 5, 6]
> ```

#### <ins>Application 7</ins>

Donner sans utiliser l'ordinateur, le résultat des instructions suivantes :

1. Instruction 1
```python
>>> entiers[0:2]
...
```

2. Instruction 2
```python
>>> entiers[0:7]
...
```

### c) Mutabilité

> [!IMPORTANT]
> Une valeur est dite *mutable* si elle peut être modifiée.

Les listes sont mutables, les éléments peuvent y être modifiés, ajoutés ou supprimés.

#### 1. Modification d'élément

Modifier un élément dans une liste s'effectue en réaffectant une valeur à une position $i$ donnée.

> [!TIP]
> Par exemple :
> ```python
> >>> entiers = [1, 2, 3, 4]
> >>> entiers[3] = 999
> >>> entiers
> [1, 2, 3, 999]
> ```

#### <ins>Application 8</ins>

Modifier dans la liste `entiers` la valeur d'indice $1$ en $-999$.

#### 2. Ajout d'élément

L'ajout d'un élément $p$ s'effectue en fin de liste avec la méthode `append()`.

> [!TIP]
> Par exemple :
> ```python
> >>> entiers = [1, 2, 3, 4]
> >>> entiers.append(5)
> >>> entiers
> [1, 2, 3, 4, 5]
> ```

#### <ins>Application 9</ins>

Ajouter à la liste `entiers` les valeurs $6$ et $7$.

#### 3. Suppression d'élément via son indice

La suppression d'élément d'indice $i$ s'effectue avec la méthode `pop()` :

> [!TIP]
> Par exemple :
> ```python
> >>> entiers = [1, 2, 3, 4]
> >>> entiers.pop(2)
> >>> entiers
> [1, 2, 4]
> ```

#### <ins>Application 10</ins>

Supprimer dans la liste `entiers` l'élément d'indice $0$.

### d) Parcours de liste

> [!IMPORTANT]
> Un *parcours de liste* consiste à visiter tous les éléments de la liste une et une seule fois dans le but de leur appliquer un traitement.

Nous parcourons les listes en utilisant les boucles.

> Comme nous connaissons à l'avance la taille d'une liste, nous connaissons à l'avance le nombre de tour de boucle nécessaire au parcours : Nous utilisons donc la boucle `for`.

Il existe deux façons d'utiliser la boucle `for` pour parcourir les listes :

1. Le parcours par **indice**.

2. Le parcours par **élément**.

#### 1. Parcours par indice

Dans le parcours par indice, nous parcourons les éléments indice par indice.

> [!TIP]
> Par exemple
> ```python
> 1. entiers = [1, 2, 3, 4]
> 2. for i in range(len(entiers)) :
> 3.   entier = entiers[i]
> ```
>
> Trace d'exécution du programme donné ci-dessus :
>
> | Numéro de ligne | Valeur affectée à $i$ | Valeur affectée à $entier$ |
> | :---: | :---: | :---: |
> | $1$ | / | / |
> | $2$ | $0$ | / |
> | $3$ | $0$ | $1$ |
> | $2$ | $1$ | $1$ |
> | $3$ | $1$ | $2$ |
> | ... | ... | ... |

#### <ins>Application 11</ins>

Recopier et compléter la trace d'exécution de l'exemple précédent.

#### 2. Parcours par élément

Dans le parcours par élément, nous parcourons élément par élément.

> [!TIP]
> Par exemple :
> ```python
> 1. entiers = [1, 2, 3, 4]
> 2. for elt in entiers :
> 3.   entier = elt
> ```
> Trace d'exécution du programme donné ci-dessus:
>
> | Numéro de ligne | Valeur affectée à $elt$ | Valeur affectée à $entier$ |
> | :---: | :---: | :---: |
> | $1$ | / | / |
> | $2$ | $1$ | / |
> | $3$ | $1$ | $1$ |
> | $2$ | $2$ | $1$ |
> | $3$ | $2$ | $2$ |
> | ... | ... | ... |

#### <ins>Application 12</ins>

Recopier et compléter la trace d'exécution de l'exemple précédent.

### e) Construction de liste en compréhension

#### 1. Principe

Imaginons que nous voulons créer une liste de taille dix dont les éléments sont tous des zéros.

Il est facile d'écrire un programme le permettant :

```python
zeros = []
for i in range(10) :
    zeros.append(0)
```

Or, il est possible en Python d'économiser des lignes de code en utilisant la construction de liste en compréhension :

```python
zeros = [0 for i in range(10)]
```

> Il s'agit d'utiliser la boucle `for` sur une unique ligne.

#### 2. Syntaxe

Syntaxe de construction de liste classique :

```python
liste = []
for <indice> in <itérable> :
    liste.append(<élément>)
```

Syntaxe de construction de liste en compréhension :

```python
liste = [<élément> for <indice> in <itérable>]
```

#### <ins>Application 13</ins>

a) Écrire, en compréhension, le programme permettant de construire une liste `[2, 2, 2, 2, 2]`.

b) Écrire en compréhension, le programme permettant de construire une liste `[0, 1, 2, 3]`.

#### 3. Condition (hors programme)

Syntaxe de construction de liste classique avec condition :

```python
liste = []
for <indice> in <itérable> :
    if <condition> :
        liste.append(<élément>)
```

Syntaxe de construction de liste en compréhension avec condition :

```python
liste = [<élément> for <indice> in <itérable> if <condition>]
```

___________

[Exercices](./Exercices/Exercices_listes.md)

___________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 