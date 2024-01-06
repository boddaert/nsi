# Préconditions

## I. Définitions

La spécification d'une fonction est complétée par les préconditions et les postconditions.

Les *préconditions* sont les conditions sur les paramètres et les conditions d'utilisation de la fonction avant son exécution.

Les préconditions doivent être vérifiées pour que la spécification d'une fonction soit vraie.

Par exemple, pour la fonction `max(l : list)->int` définie dans [Spécifications](./Specification.md) dont la spécification est **Renvoie l'entier le plus grand parmi tous les entiers de la liste l**, les préconditions sont :

- Le paramètre `l` est bien de type `list`.

- Le paramètre `l` ne contient que des éléments de type `int`.

- Le paramètre `l` doit contenir au moins un élément.

Nous pouvons vérifier les préconditions d'une fonction en utilisant des assertions.

## II. Assertions

### a) Définition

Une *assertion* est une fonction qui arrête le programme en renvoyant une erreur de type `AssertionError` si son argument ne vaut pas $True$.

### b) Syntaxe

Une assertion s'écrit à l'aide de l'instruction `assert` en Python, elle prend une expression et un message qui est renvoyé si la condition vaut $False$.

Les assertions sont généralement les premières instructions d'un programme :

```python
def max(l : list)->int:
    """
    :param l: (list) Une liste d'entiers
    :return: (int) Un entier, élément de l
    Renvoie l'entier le plus grand parmi tous les entiers de la liste l
    :CU: La liste l doit contenir au moins un élément
    """
    assert type(l) == list, "Le paramètre entré n'est pas de type list"
    assert all([type(l[i]) == int for i in range(len(l))]), "Les éléments ne sont pas tous de type int"
    assert len(l) > 0, "La liste entrée en paramètre ne contient aucun élément"

    elt_max = l[0]
    for i in range(1, len(l)):
        if l[i] > elt_max :
            elt_max = l[i]
    return elt_max
```

### c) Visualisation des assertions

```python
>>> max('123')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "./test.py", line 8, in maxi
    assert type(l) == list, "Le paramètre entré n'est pas de type list"
AssertionError: Le paramètre entré n'est pas de type list

>>> max([1, 2, '3'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "./test.py", line 9, in maxi
    assert all([type(l[i]) == int for i in range(len(l))]), "Les éléments ne sont pas tous de type int"
AssertionError: Les éléments ne sont pas tous de type int

>>> max([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "./test.py", line 11, in maxi
    assert len(l) > 0, "La liste entrée en paramètre ne contient aucun élément"
AssertionError: La liste entrée en paramètre ne contient aucun élément
```

##### Application 1

Ecrire, à l'aide d'assertions, et visualiser les préconditions de toute les fonctions données en réponses aux questions de la feuille d'exercice sur les listes (cf [Feuille d'exercices sur les listes](./../Structures_de_données/Exercices/Exercices_listes.md))

___________________

[Sommaire](./../README.md)