# Modules

## I. Définitions

Un *module* (ou *bibliothèque*) est un fichier Python contenant du code que nous pouvons utiliser en l'important dans notre propre fichier.

Le module `math` par exemple met à disposition toutes les fonctions mathématiques.

## II. Importation de module

### a) Importer globalement

Importer de manière globale revient à importer tout le code contenu dans le module :

```python
import math
```

Dans ce cas, pour pouvoir utiliser les fonctionnalités du module, nous devrons écrire le nom du module suivi d'un point suivi de la fonctionnalité :

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

## III. Modules standards

### a) Module mathématique

Le module `math` possède toutes les fonctions mathématiques.

| Nom  du module : | `math` |
|---|---|
| Racine carrée de $n$ | `sqrt(n)` |
| Trigonométrie | `sin()`, `cos()` |
| Pi | `pi` |

Voir plus : [https://docs.python.org/fr/3.5/library/math.html](https://docs.python.org/fr/3.5/library/math.html)

### b) Module d'aléatoire

Le module `random` met à disposition plusieurs fonctions permettant d'obtenir de l'aléatoire.

| Nom du module : | `random` |
|---|---|
| Entier aléatoire compris entre $x$ et $y$ | `randint(x : int, y : int)` |
| Nombre aléatoire compris entre $0$ et $1$ | `random()` |

Voir plus : [https://docs.python.org/fr/3/library/random.html](https://docs.python.org/fr/3/library/random.html)

##### Application 1

a) Dans un fichier `nom_prenom_importation_globale.py`, importer de manière globale le module `math` puis, dans la console, afficher la valeur de Pi.

b) Dans un second fichier `nom_prenom_importation_precise.py`, importer de manière précise le module `math` puis, dans la console, afficher la valeur de Pi.

________

[Exercices](./Exercices/Exercices_modules.md)

________

[Sommaire](./../../README.md)