# Préconditions

## I. Définitions

La spécification d'une fonction est complétée par les **préconditions** et les **postconditions**.

> [!IMPORTANT]
> Les *préconditions* sont les conditions sur les paramètres et les conditions d'utilisation de la fonction avant son exécution.

> [!TIP]
> Par exemple, pour la fonction `max(l : list)->int` définie dans [Prototypage](./Prototypage.md) dont la spécification est **Renvoie l'entier le plus grand parmi tous les entiers de la liste l**, les préconditions sont :
>
> - Le paramètre `l` est bien de type `list`.
>
> - Le paramètre `l` ne contient que des éléments de type `int`.
>
> - Le paramètre `l` doit contenir au moins un élément.

> Les préconditions doivent être vérifiées pour que la spécification d'une fonction soit vraie.

Nous pouvons vérifier les préconditions d'une fonction en utilisant des assertions.

> [!IMPORTANT]
> Une *assertion* est une fonction qui arrête le programme en renvoyant une erreur de type `AssertionError` si son argument ne vaut pas `True`.

## II. Assertions

### a) Syntaxe

Une assertion s'écrit à l'aide de l'instruction `assert` en Python, elle prend une expression et un message qui est renvoyé si la condition vaut `False`.

> [!TIP]
> Par exemple :
> ```python
> def max(l : list)->int:
>     """
>     :param l: (list) Une liste d'entiers
>     :return: (int) Un entier, élément de l
>     Renvoie l'entier le plus grand parmi tous les entiers de la liste l
>     :CU: La liste l doit contenir au moins un élément
>     """
>     assert type(l) == list, "Le paramètre entré n'est pas de type list"
>     assert all([type(l[i]) == int for i in range(len(l))]), "Les éléments ne sont pas tous de type int"
>     assert len(l) > 0, "La liste entrée en paramètre ne contient aucun élément"
>
>     elt_max = l[0]
>     for i in range(1, len(l)):
>         if l[i] > elt_max :
>             elt_max = l[i]
>     return elt_max
> ```

### c) Visualisation des assertions

En cas de non respect des assertions, le programme s'arrête et renvoie une erreur de type `AssertionError`.

> [!TIP]
> Par exemple :
> ```python
> >>> max([1, 2, '3'])
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
>   File "./test.py", line 9, in maxi
>     assert all([type(l[i]) == int for i in range(len(l))]), "Les éléments ne sont pas tous de type int"
> AssertionError: Les éléments ne sont pas tous de type int
> ```

#### <ins>Application 1</ins>

a) Proposer, sur papier, des contraintes de préconditions pour les exercices $11$, $12$, $13$ et $14$ des listes (cf [Exercices sur les listes](./../../Types_construits/Tableaux/Exercices/Exercices_listes.md)).

b) Écrire les assertions correspondantes aux préconditions proposées à la question précédente dans chacune des fonctions.

___________________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 