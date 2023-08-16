# Modularité

## I. Définitions

La *modularité* est le fait d'utiliser des modules existants ou de créer des modules.

L'objectif étant de décomposer son code en plusieurs fichiers Python.

Un *module* (ou *bibliothèque*) est un fichier Python contenant du code que nous pouvons utiliser en l'important dans notre propre fichier.

Le module `math` par exemple met à disposition toutes les fonctions mathématiques.

## II. Importation de module

### a) Importer globalement

Importer de manière globale revient à importer tout le code contenu dans le module :

```python
import math
```

Dans ce cas, pour pouvoir utiliser les fonctionnalités du module, nous devons écrire le nom du module suivi d'un point puis du nom de la fonction :

```python
>>> import math
>>> math.sqrt(5)
2.23606797749979
```

### b) Importer précisément

Nous pouvons importer seulement les fonctionnalités qui nous interesse :

```python
from math import sqrt
```

Dans ce cas ci, plus besoin de devoir réécrire le nom du module :

```python
>>> from math import sqrt
>>> sqrt(5)
2.23606797749979
```

## III. Création de module

### a) Bonnes pratiques

En partant du fait que les modules peuvent être utilisés par d'autres utilisateurs, il est important de donner des noms de fonctions et variables explicites.

Il est également très important de bien documenter avec une DocString et une DocTest notamment.

### b) Instruction spéciale

Il existe une instruction permettant de ne pas exécuter celles qui suit lorsque nous importons le module.

Cette instruction spéciale est utilisée principalement pour tester du code qui ne doit pas être importé.

##### Application 1

a) Exécuter le programme suivant dans un fichier `module.py`:

```python
a = 1
if __name__ = 'main' :
    b = 2
```

b) Puis vérifier la valeur affectée aux variables `a` et `b` dans la console.

c) Créer un autre fichier Python qui importe `module.py`.

d) Vérifier une nouvelle fois la valeur affectée aux variables `a` et `b` après avoir exécuté le nouveau fichier. Qu'en déduisez-vous ?

_______

[Feuile d'exercice](./Exercices_modularite.md)

_______

[Sommaire](./../../terminale/)