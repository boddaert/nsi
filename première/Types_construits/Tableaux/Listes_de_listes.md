# Listes de listes

## I. Définitions 

> [!IMPORTANT]
> Une *liste de listes* est une liste dans lequel chacun de ses éléments est une liste.

Par conséquent, toute les notions vues précédemment dans la leçon sur les listes (cf [Leçon 1 : Listes](./Listes.md)) sont appliquables ici.

## II. En Python

### a) Spécificités

Les données représentables sur deux dimensions comme les tableaux sont facilement modélisées en Python à l'aide des listes de listes.

> [!TIP]
> Par exemple :
>
> Le tableau $t = $
>
> | 0 | 1 | 2 |
> | :---: | :---: | :---: |
> | **3** | **4** | **5** |
> 
> Est modélisé en Python par la liste de listes suivante :
> 
> ```python
> t = [[0, 1, 2], [3, 4, 5]]
> ```

En Python, une liste de listes reste de type `list`.

> [!TIP]
> Par exemple :
> ```python
> >>> type(t)
> <class 'list'>
> ```

#### <ins>Application 1</ins>

En Python, affecter à la variable `table_de_multiplication` la liste de listes correspondant au tableau suivant :

| $0$ | $0$ | $0$ | $0$ | $0$ |
| :---: | :---: | :---: | :---: | :---: |
| $0$ | $1$ | $2$ | $3$ | $4$ |
| $0$ | $2$ | $4$ | $6$ | $8$ |
| $0$ | $3$ | $6$ | $9$ | $12$ |
| $0$ | $4$ | $8$ | $12$ | $16$ |


### b) Opérations

#### 1. Taille

> [!IMPORTANT]
> La *taille* d'une liste de listes est le nombre de sous-listes contenues dans celle-ci.

> [!TIP]
> Par exemple :
> ```python
> >>> len(t)
> 2
> ```

#### 2. Accès au *i-ème* élément

> [!IMPORTANT]
> L'*indice d'un élément* dans la liste est le numéro de position de l'élément.

L'accès à une liste d'indice $i$ s'effectue en l'écrivant entre crochets.

> [!TIP]
> Par exemple :
> ```python
> >>> t[0]
> [0, 1, 2]
> ```

L'accès à un élément d'indice $j$ d'une sous-liste s'effectue en l'écrivant dans de nouveaux crochets.

> [!TIP]
> Par exemple :
> ```python
> >>> t[0][1]
> 1
> ```

#### <ins>Application 2</ins>

a) Écrire l'instruction permettant de connaître la taille de `table_de_multiplication`.

b) Écrire l'instruction permettant de connaître la taille la seconde ligne de `table_de_multiplication`.

c) Donner, sans utiliser l'ordinateur, le résultat des instructions suivantes :

1. Instruction 1
```python
>>> table_de_multiplication[1]
...
```
2. Instruction 2
```python
>>> table_de_multiplication[2][3]
...
```
3. Instruction 3
```python
>>> table_de_multiplication[4][1]
```

d) Écrire l'instruction permettant d'obtenir le nombre $16$ en utilisant uniquement l'opération de taille.

### c) Autres opérations

Les opérations de test d'appartenance, de concaténation, de découpage, de mutabilité sont appliquables aux listes de listes (cf [Listes](./Listes.md)).

### d) Parcours de listes de listes

> [!IMPORTANT]
> Un *parcours de liste de listes* consiste à visiter tous les éléments de la liste de listes une et une seule fois dans le but de leur appliquer un traitement.

Nous parcourons les listes de listes en utilisant deux boucles imbriquées l'une dans l'autre.

#### 1. Parcours par indice

Dans le parcours par indice, nous parcourons les sous-listes puis les éléments des sous-listes indice par indice.

> [!TIP]
> Par exemple :
> ```python
> 1. t = [[0, 1, 2], [3, 4, 5]]
> 2. for i in range(len(t)) :
> 3.   for j in range(len(t[i])):
> 4.      entier = t[i][j]
> ```
>
> Trace d'exécution du programme donné ci-dessus :
> 
> | Numéro de ligne | Valeur affectée à $i$ | Valeur affectée à $j$ | Valeur affectée à $entier$ |
> | :---: | :---: | :---: | :---: |
> | $1$ | / | / | / |
> | $2$ | $0$ | / | / |
> | $3$ | $0$ | $0$ | / |
> | $4$ | $0$ | $0$ | `0` |
> | $3$ | $0$ | $1$ | `0` |
> | $4$ | $0$ | $1$ | `1` |
> | $3$ | $0$ | $2$ | `1` |
> | $4$ | $0$ | $2$ | `2` |
> | $2$ | $1$ | $2$ | `2` |
> | $3$ | $1$ | $0$ | `2` |
> | $4$ | $1$ | $0$ | `3` |
> | ... | ... | ... | ... |

#### <ins>Application 3</ins>

Compléter la trace d'exécution précédente.

#### 2. Parcours par élément

Dans le parcours par élément, nous parcourons les sous-listes puis les éléments des sous-listes élément par élément.

> [!TIP]
> Par exemple :
> ```python
> 1. t = [[0, 1, 2], [3, 4, 5]]
> 2. for sousliste in t :
> 3.   for elt in sousliste:
> 4.      entier = elt
> ```

#### <ins>Application 4</ins>

Écrire un programme permettant d'afficher un par un chacun des nombres présents dans `table_de_multiplication`.

1. Une première fois en effectuant le parcours par indice.

2. Une seconde fois en effectuant le parcours par élément.

__________________

[Exercices](./Exercices/Exercices_listes_de_listes.md)

__________________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 