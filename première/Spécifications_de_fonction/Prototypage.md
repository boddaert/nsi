# Spécification

## I. Définitions

La *spécification* d'une fonction est la raison pour laquelle elle existe. En d'autres termes, la spécification d'une fonction répond aux questions suivantes :

- Que fait cette fonction ?

- Qu'à besoin cette fonction ?

En Python, spécifier une fonction se fait à l'aide d'une documentation spéciale : la *DocString*.

Une *documentation* permet de donner des informations à celui qui lit le code.

## II. Types de documentation

### a) Commentaires

Il est possible de laisser une information n'importe où dans le programme en écrivant un commentaire.

En Python, pour écrire un commentaire, il faut utiliser le caractère spécial : `#` :

```python
# Importation des modules
from math import *
from random import *
```

### b) *DocString*

Lors de l'écriture d'une fonction, il est plus approprié de donner sa spécification à l'aide d'une DocString.

Elle s'écrit toujours juste après la signature d'une fonction et donne les informations suivantes :

- Les paramètres avec leur type.

- Le type de la valeur de renvoi.

- Une phrase en Français expliquant ce que fait la fonction.

- Eventuellement les contraintes d'utilisation.

Par exemple :

```python
def max(l : list)->int:
    """
    :param l: (list) Une liste d'entiers
    :return: (int) Un entier, élément de l
    Renvoie l'entier le plus grand parmi tous les entiers de la liste l
    :CU: La liste l doit contenir au moins un élément
    """
    elt_max = l[0]
    for i in range(1, len(l)):
        if l[i] > elt_max :
            elt_max = l[i]
    return elt_max
```

______________

[Sommaire](./../README.md)