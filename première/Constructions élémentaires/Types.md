# Types

## I. Définitions

En Python, les valeurs ont des types. 

On appelle valeur toute donnée manipulable. Par exemple, `42` et `$` sont des valeurs que l'on peut manipuler dans nos programmes.

Chaque valeur a un type qui la **caractérise**. On peut distinguer, parallèlement aux mathématiques, les nombres entiers et les réels par exemple, qui sont deux types distincts en Python : les entiers et les flottants.

Par exemple, `42` est un entier et `$` un caractère.

Attribuer un type à une valeur nous sert à **classer nos données** et donc à savoir si telle ou telle opération est possible sur la donnée.

Par exemple, nous pouvons effectuer toutes les opérations possibles aux entiers à la valeur `42` puisque `42` est un entier. Mais nous ne pouvons pas additionner `42` et `$` puisque `$` est un caractère.

## II. Les nombres

### a) Les entiers naturels

On peut utiliser la fonction `type()` pour afficher le type d'une valeur mise entre les parenthèses :

```Python
>>> type(5)
<class 'int'>
```

Par exemple, si je demande le type de la valeur 5 en écrivant `type(5)` dans la console Python, j'obtiens comme résultat : `<class 'int'>`.

Pour l'instant, il est inutile de s'attarder sur le mot-clé `class`, concentrons nous sur le mot-clé `int` qui nous indique qu'il s'agit du type `int` ou `integer` qui veut dire **entier naturel**.

##### Application 1

Dans la console Python et à l'aide de la fonction `type()`, vérifier que les valeurs `42`, `3000`, `0` et `-4` sont bien des entiers.

### b) Les réels

Les nombres réels sont des nombres à virgule et possèdent un type différent des entiers naturels en Python :

```Python
>>> type(3.14)
<class 'float'>
```

Le type des réels en Python est le type ``float`` pour **nombres flottants**.

##### Application 2

Dans la console Python et à l'aide de la fonction `type()`, vérifier que les valeurs `5.0`, `0.6578543`, `0.0` et `-6.4` sont bien des flottants.

## III. Les chaînes de caractères

Une chaîne de caractère est une valeur encadrée par des **guillemets** (ou des guillemets simples) : ``"a"``  ou ``'a'``.

Une chaîne de caractère peut contenir plusieurs caractères : ``"acdc"``.

En Python, les chaînes de caractère sont représentés par le type ``str``  :

```Python
>>> type("acdc")
<class 'str'>
```

##### Application 3

Dans la console Python et à l'aide de la fonction `type()`, vérifier que les valeurs `"azerty"`, `"exemple@mail.fr` et `"3.14"` sont bien des chaînes de caractères.

## IV. Les booléens

Les booléens sont un type bien particulier de la programmation, présents dans l'algèbre de Bool inventé par un mathématicien du même nom dans les années 1860.

Dans le type booléen, il y a seulement deux valeurs : **Vrai**, **Faux**.

En Python, ces valeurs sont ``True`` et ``False`` respectivement. 

```Python
>>> type(True)
<class 'bool'>
```

Ces booléens servent notemment dans les tables de vérité et les instructions conditionnelles.

##### Application 4

Dans la console Python et à l'aide de la fonction `type()`, vérifier que les valeurs `True` et `False` sont bien des booléens.

## V. NoneType

Voici un type encore plus particulier : ``NoneType`` 

Une seule valeur possède ce type, c'est ``None`` et comme son nom l'indique, c'est une valeur qui ne représente ... rien !

```Python
>>> type(None)
<class 'NoneType'>
```

## VI. Récapitulatif des types

| En Français | En Python |
|----|----|
|Entier naturel | `int` |
| Flottant | `float` |
| Chaîne de caractères | `str` |
| Booléen | `bool` |
| NoneType | `None` |

## Exercices

### Exercice 1

a) Donner, pour chaque valeur suivante, son type sans utiliser la fonction `type()` :

- 8
- 6.5
- "6.5"
- '6.5'
- False
- "True"
- ""
- 5 + 4
- "5 + 4"
- '"abcd"'
- 5.5 + 0.3
- 5.5 + 0.5
- 5 + 3.14
- 5 + 3.0

b) Vérifier, à l'aide de la fonction `type()` et dans la console vos précédentes réponses. Puis sur chacune d'entre elles, écrire une explication du type obtenu.




#### Application 2
chaine vide

A l'aide de la fonction ``type()``, vérifier dans la console le type du résultat de l'expression ``5 + 3.14`` sur une seule ligne.

# 

__________

Leçon 2 : [Variables](./Variables.md)
