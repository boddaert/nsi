# Postconditions

## I. Définitions

La spécification d'une fonction est complétée par les préconditions et les postconditions.

Les *postconditions* sont les conditions sur le résultat de la fonction à l'issue de son exécution.

Les postconditions doivent être vérifiées pour que la spécification d'une fonction soit vraie.

Par exemple, pour la fonction `max(l : list)->int` définie dans [Spécifications](./Specification.md) dont la spécification est `Renvoie l'entier le plus grand parmi tous les entiers de la liste l`, les postconditions sont :

- Le résultat renvoyé par la fonction est bien de type `int`.

- Le résultat correspond bien à un élément présent dans `l`.

- Le résultat renvoyé par la fonction est bien un élément supérieur à tous les autres de la liste.

Nous pouvons vérifier les postconditions d'une fonction en utilisant des jeux de test.

## II. Jeu de test

### a) Définitions

Un *jeu de test* est un ensemble de test réalisé afin de vérifier les postconditions d'une fonction.

Un *test* est une simulation d'exécution de la fonction avec des arguments bien choisis.

Un bon jeu de test considère notamment les cas particuliers d'arguments, quand la liste est vide par exemple.

Le succès d'un jeu de test ne garantit pas pour autant la correction de la fonction.

### b) DocTest

En Python, nous pouvons écrire un jeu de test à l'aide du module `Doctest` :

```python
import doctest
```

Les tests s'écrivent dans la DocString, après la spécification :

```python
def max(l : list)->int:
    """
    :param l: (list) Une liste d'entiers
    :return: (int) Un entier, élément de l
    Renvoie l'entier le plus grand parmi tous les entiers de la liste l
    :CU: La liste l doit contenir au moins un élément

    Exemples :
    >>> max([1, 2, 3])
    3
    >>> max([3, 2, 1])
    3
    """
    elt_max = l[0]
    for i in range(1, len(l)):
        if l[i] > elt_max :
            elt_max = l[i]
    return elt_max
```

### c) Visualisation des tests

Depuis la console, l'instruction suivante permet de savoir si les tests ont réussis ou échoués :

```python
>>> doctest.testmod(verbose=True)
Trying:
    max([1, 2, 3])
Expecting:
    3
ok
Trying:
    max([3, 2, 1])
Expecting:
    3
ok
1 items had no tests:
    __main__
1 items passed all tests:
   2 tests in __main__.max
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
TestResults(failed=0, attempted=2)
```

______________

[Sommaire](./../README.md)