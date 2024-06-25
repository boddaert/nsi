# Types

## I. Définitions

En Python, les valeurs ont des types. 

> [!IMPORTANT]
> Une *valeur* est donnée manipulable.

Par exemple, `42` et `ù` sont des valeurs que nous pouvons manipuler dans nos programmes.

> [!IMPORTANT]
> Chaque valeur possède un *type* qui la **caractérise**.

Nous pouvons distinguer, parallèlement aux mathématiques, les nombres entiers et les réels par exemple, qui sont deux types distincts en Python : les entiers et les flottants.

> [!TIP]
> `42` est une valeur de type entier et `ù` est une valeur de type caractère.

Attribuer un type à une valeur nous sert à **classer nos données** et donc à savoir si telle ou telle opération est possible sur telle donnée.

> [!TIP]
> Nous ne pouvons pas additionner `42` et `ù` puisque `42` est un entier et `ù` un caractère.

## II. Les nombres

### a) Les entiers naturels

La fonction `type()` affiche le type d'une valeur mise entre les parenthèses :

> [!TIP]
> ```python
> >>> type(5)
> <class 'int'>
> ```

> [!NOTE]
> Pour l'instant, il est inutile de s'attarder sur le mot-clé `class`, concentrons nous sur le mot-clé `int` qui nous indique qu'il s'agit du type `int` ou `integer` qui veut dire **entier**.

#### <ins>Application 1</ins>

Dans la console Python et à l'aide de la fonction `type()`, vérifier que les valeurs `3000`, `0` et `-4` sont bien des entiers.

### b) Les réels

Les nombres réels sont les nombres décimaux et possèdent un type différent des entiers en Python :

> [!TIP]
> ```python
> >>> type(3.14)
> <class 'float'>
> ```

Le type des réels en Python est le type ``float`` pour **nombres flottants**.

> [!WARNING]
> Les nombres flottants s'écrivent avec des points et non des virgules.

#### <ins>Application 2</ins>

Dans la console Python et à l'aide de la fonction `type()`, vérifier que les valeurs $`0.6578543`$, $`0.0`$ et $`-6.4`$ sont bien des nombres flottants.

## III. Les chaînes de caractères

Une chaîne de caractère est une valeur encadrée par des **guillemets** (ou des guillemets simples) : `"a"`  ou `'a'`.

Une chaîne de caractère peut contenir plusieurs caractères : `"acdc"`.

En Python, les chaînes de caractère sont représentés par le type ``str``.

> [!TIP]
> ```python
> >>> type("a")
> <class 'str'>
> ```

#### <ins>Application 3</ins>

Dans la console Python et à l'aide de la fonction `type()`, vérifier que les valeurs $`"azerty"`$, $`"exemple@mail.fr"`$ et $`"3.14"`$ sont bien des chaînes de caractères.

## IV. Les booléens

Les booléens sont un type bien particulier de la programmation, présents dans l'algèbre de Bool inventé par un mathématicien du même nom dans les années 1860.

Dans le type booléen, il y a seulement deux valeurs : **Vrai**, **Faux** respectivement `True` et `False` en Python.

> [!TIP]
> ```python
> >>> type(True)
> <class 'bool'>
> ```

####  <ins>Application 4</ins>

Dans la console Python et à l'aide de la fonction `type()`, vérifier que les valeurs `True` et `False` sont bien des booléens.

## V. Récapitulatif des types

| En Français | En Python |
|----|----|
|Entier naturel | `int` |
| Flottant | `float` |
| Chaîne de caractères | `str` |
| Booléen | `bool` |

_________

[Exercices](./Exercices/Exercices_types.md)
_________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 