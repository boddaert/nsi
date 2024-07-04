# Tuples

## I. Définitions

> [!IMPORTANT]
> Un *tuple* (ou *p-uplet*) est une structure linéaire non mutable de données. (Voir [listes](./Listes.md) pour les définitions)

> [!IMPORTANT]
> Une *structure linéaire non mutable de données* est une structure de données linéaire dans laquelle les éléments ne peuvent pas être ajoutés, retirés ou modifiés.

## II. En Python

### a) Spécificités

En Python, les tuples sont définis entre parenthèses (`(` `)`).

> [!TIP]
> Par exemple :
> ```python
> (1, 2, 3)
> ```

Les tuples sont de type `tuple`.

> [!TIP]
> Par exemple :
>```python
> >>> type((1, 2, 3))
> <class 'tuple'>
> ```

> [!IMPORTANT]
> Un *tuple vide* est un tuple ne contenant aucun élément :

> [!TIP]
> Par exemple :
> ```python
> >>> type(())
> <class = 'tuple'>
> ```

Une liste peut contenir des éléments de différents types.

> [!TIP]
> Par exemple :
> ```python
> (True, 0, "coucou"))
> ```

> [!WARNING]
> Il faut toujours au moins une virgule pour définir un tuple.

> [!TIP]
> Par exemple :
> ```python
> >>> type((1))
> <class 'int'>
> >>> type((1,))
> <class 'tuple'>
> ```

### b) Opérations

> L'ensemble des opérations pouvant être effectuées sur les tuples est équivalent à l'ensemble des opérations pouvant être effectuées sur les listes. (Voir [Listes](./../Tableaux/Listes.md)).

Les tuples, n'étant pas mutables, les éléments d'un tuple ne sont pas modifiables.

> [!TIP]
> Par exemple :
> ```python
> >>> tuple_entiers = (1, 2, 3)
> >>> tuple_entiers[2] = 2
> Traceback (most recent call last):
>   File "<pyshell>", line 1, in <module>
> TypeError: 'tuple' object does not support item assignment
> ```

### c) Affectation parallèle

Les tuples permettent d'affecter des valeurs sur une seule ligne à plusieurs variables.

> [!TIP]
> Par exemple :
> ```python
> >>> (a, b) = ("coucou", 42)
> >>> a
> "coucou"
> >>> b
> 42
> ```

#### <ins>Application 1</ins>

Compléter le programme ci-dessous pour échanger les valeurs de `a` et `b` sur une seule ligne.

```python
a = 42
b = "coucou"
...
```

### d) Renvoyer plusieurs résultats

Les tuples permettent de renvoyer plusieurs valeurs dans une fonction.

> [!TIP]
> Par exemple :
> ```python
> def fonc()->tuple:
>     return (a, b)
> ```

> [!WARNING]
> Le type de la valeur renvoyée est un tuple.

#### <ins>Application 2</ins>

Écrire une fonction `nom_prenom()->tuple` ne prenant aucun paramètre, demande à l'utilisateur quel est son nom et son prénom et les renvoie sous forme de tuple.

### e) Parcours de tuple

Le parcours de tuple est équivalent au parcours de liste.
_____________

[Exercices](./Exercices/Exercices_tuples.md)

_____________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 

