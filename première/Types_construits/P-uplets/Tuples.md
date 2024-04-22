# Tuples

## I. Définition

Un *tuple* (ou *p-uplet*) est une structure linéaire non mutable de données. (Voir [listes](./Listes.md) pour les définitions)

En Python, le type `tuple` est encadré de parenthèses :

```python
>>> type((1, 3, 5))
<class 'tuple'>
```

Un *tuple vide* est un tuple ne contenant aucun élément :

```python
>>> type(())
<class = 'tuple'>
```

*Attention : Il faut toujours au moins une virgule pour définir un tuple à un élément.*

```python
>>> type((1))
<class = 'int'>
>>> type((1,))
<class = 'tuple'>
```

## II. Opérations sur les tuples

L'ensemble des opérations pouvant être effectuées sur les tuples est équivalent à l'ensemble des opérations pouvant être effectuées sur les listes.

A la différence des opérations de mutabilité.

Les tuples, n'étant pas mutables, nous ne pouvons pas modifier les éléments d'un tuple :

```python
>>> tuple_entiers = (1, 2, 3, 4)
>>> tuple_entiers[2] = 2
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Les tuples sont généralement utilisés pour définir des structures de données où les éléments restent les mêmes.

Par exemple, les coordonnées $x$ et $y$ dans un plan.

## III. Parcours de tuple

Le parcours de tuple est équivalent au parcours de liste.

## IV. Affectation parallèle

Nous pouvons utiliser les tuples pour affecter sur une même ligne plusieurs valeurs à plusieurs variables :

```python
>>> (a, b) = ("coucou", 42)
>>> a
"coucou"
>>> b
42
```
##### Application 1

Compléter le programme ci-dessous pour échanger les valeurs de `a` et `b` sur une seule ligne.

```python
a = 42
b = "coucou"
...
```

## V. Renvoyer plusieurs résultats

Parfois, il est utile de renvoyer plusieurs résultats pour une fonction. Nous pouvons le faire facilement en utilisant les tuples.

Le type de la valeur renvoyée est un tuple :

```python
def fonc()->tuple:
    return (a, b)
```

Puis, en utilisant l'affectation parallèle :

```python
>>> x, y = fonc()
```
_____________

[Exercices](./Exercices/Exercices_tuples.md)

_____________

[Sommaire](./../../README.md)

