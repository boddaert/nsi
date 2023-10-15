# Modularité

## I. Définitions

La *modularité* est le fait d'utiliser des modules existants ou de créer des modules.

L'objectif étant de décomposer son code en plusieurs fonctions/fichiers Python afin d'y voir plus clairement.

Un *module* (ou *bibliothèque*) est un fichier Python que nous pouvons importer dans notre propre fichier pour pouvoir utiliser son code.

Le module `math` par exemple est un fichier Python mettant à disposition toutes les fonctions mathématiques.

## II. Importation de module

### a) Importer globalement

Importer de manière globale revient à importer tout le code contenu dans le module :

```python
import math
```

Dans ce cas, pour pouvoir utiliser les fonctions du module, nous devons écrire le nom du module suivi d'un point puis du nom de la fonction que l'on souhaite utiliser :

```python
>>> import math
>>> math.sqrt(5)
2.23606797749979
```

### b) Importer précisément

Importer de manière précise revient à importer seulement les fonctions qui nous interesse :

```python
from math import sqrt
```

Dans ce cas ci, plus besoin de devoir réécrire le nom du module :

```python
>>> from math import sqrt
>>> sqrt(5)
2.23606797749979
```

## III. Bonnes pratiques

1. Il est très conseillé de moduler son programme, c'est-à-dire de découper son programme le plus possible en plusieurs fonctions.

L'idéal est : Une tâche -> Une fonction.

2. En partant du fait que les modules peuvent être utilisés par d'autres utilisateurs, il est important de donner des noms de fonctions explicites et des noms de variables explicites.

3. Il est également très important de documenter et tester chaque fonction.

##### Application 1

a) Créer un fichier `maximum_liste.py` dans lequel vous écrirez une fonction `maxi(liste : list)->int` permettant de récupérer l'entier maximum d'une liste.

b) Puis, dans un second fichier Python `importation_globale.py` situé dans le même répertoire, importer la fonction `maxi()` de manière globale et tester la fonction dans `importation_globale.py`.

c) Enfin, dans un troisième fichier Python `importation_precise.py` situé lui aussi dans le même répertoire, importer la fonction `maxi()` de manière précise et tester la fonction dans `importation_precise.py`.

_______

[Feuile d'exercice](./Exercices/Exercices_modularite.md)

_______

[Sommaire](./../README.md)