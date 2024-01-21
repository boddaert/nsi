# Listes de listes

## I. Définitions 

Une *liste de listes* est une liste dans lequel chacun de ses éléments est une liste.

Par conséquent, toute les notions vues précédemment dans la leçon sur les listes (cf [Leçon 1 : Listes](./Listes.md)) sont appliquables ici.

Nous utilisons les listes de listes pour modéliser les données représentables sur deux dimensions comme les tableaux.

$t = $

| 00 | 01 | 02 |
| :---: | :---: | :---: |
| **10** | **11** | **12** |

Par exemple, le tableau précédent est modélisé en Python par la liste suivante :

```python
t = [['00', '01', '02'], ['10', '11', '12']]
```

En Python, une liste de listes reste de type `list` :

```python
>>> type(t)
<class 'list'>
```

##### Application 1

En Python, affecter à la variable `table_de_multiplication` la liste de listes correspondant au tableau suivant :

| $0$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
| $0$ | $2$ | $4$ | $6$ | $8$ | $10$ |
| $0$ | $3$ | $6$ | $9$ | $12$ | $15$ |
| $0$ | $4$ | $8$ | $12$ | $16$ | $20$ |
| $0$ | $5$ | $10$ | $15$ | $20$ | $25$ |

## II. Opérations sur les listes de listes

### a) Taille

La *taille* d'une liste de listes indique le nombre de sous-listes qui la constitue :

```python
>>> len(t)
2
```

Et la taille de la première sous-liste :

```python
>>> len(t[0])
3
```

### b) Accès au *i-ème* élément

Nous mettons l'indice de la sous-liste que nous souhaitons obtenir entre crochets :

```python
>>> t[0]
['00', '01', '02']
```

L'élément `'01'` est récupérable en ajoutant de nouveaux crochets encadrés de son indice dans la sous-liste :

```python
>>> t[0][1]
'01'
```

##### Application 2

a) Écrire l'instruction permettant de connaître la taille de `table_de_multiplication`.

b) Écrire l'instruction permettant de connaître la taille la seconde ligne de `table_de_multiplication`.

c) Donner, sans utiliser l'ordinateur, le résultat des instructions suivantes :

```python
>>> table_de_multiplication[1]
...
```

```python
>>> table_de_multiplication[2][3]
...
```

d) Écrire l'instruction permettant d'obtenir le nombre $25$ en utilisant uniquement la taille de liste.

## III. Parcours de listes de listes

Un *parcours de liste de listes* consiste à visiter tous les éléments de la liste de listes une et une seule fois dans le but de leur appliquer un traitement.

Nous parcourons les listes de listes en utilisant deux boucles imbriquées l'une dans l'autre.

### a) Parcours par indice

Dans le parcours par indice, nous parcourons les éléments indice par indice :

```python
1. t = [['00', '01', '02'], ['10', '11', '12']]
2. for i in range(len(t)) :
3.   for j in range(len(t[i])):
4.      entier = t[i][j]
```

Trace d'exécution du programme donné ci-dessus:

| Numéro de ligne | Valeur affectée à $i$ | Valeur affectée à $j$ | Valeur affectée à $entier$ |
| :---: | :---: | :---: | :---: |
| $1$ | / | / | / |
| $2$ | $0$ | / | / |
| $3$ | $0$ | $0$ | / |
| $4$ | $0$ | $0$ | `'00'` |
| $3$ | $0$ | $1$ | `'00'` |
| $4$ | $0$ | $1$ | `'01'` |
| $3$ | $0$ | $2$ | `'01'` |
| $4$ | $0$ | $2$ | `'02'` |
| $2$ | $1$ | $2$ | `'02'` |
| $3$ | $1$ | $0$ | `'02'` |
| $4$ | $1$ | $0$ | `'10'` |
| ... | ... | ... | ... |

##### Application 3

Compléter la trace d'exécution précédente.

### b) Parcours par élément

Dans le parcours par élément, nous parcourons élément par élément :

```python
1. t = [['00', '01', '02'], ['10', '11', '12']]
2. for sousliste in t :
3.   for elt in sousliste:
4.      entier = elt
```

##### Application 4

Écrire un programme permettant d'afficher un par un chacun des nombres présents dans `table_de_multiplication`.

__________________

[Feuille d'exercices](./Exercices/Exercices_listes_de_listes.md)

__________________

[Sommaire](./../README.md)
