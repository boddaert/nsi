# Modules

## I. Définitions

> [!IMPORTANT]
> Un *module* (ou *bibliothèque*) est un fichier Python contenant du code que nous pouvons utiliser en l'important dans notre propre fichier.

Le module `math` par exemple met à disposition toutes les fonctions mathématiques.

## II. Importation de module

### a) Importer globalement

Importer de **manière globale** revient à importer tout le code contenu dans le module et s'effectue avec le mot-clé `import`.


> [!TIP]
> Par exemple
> ```python
> import math
> ```

Dans ce cas, pour pouvoir utiliser les fonctions du module, nous devrons écrire le nom du module suivi d'un point suivi du nom de la fonction que nous souhaitons utiliser.

> [!TIP]
> Par exemple :
> ```python
> >>> import math
> >>> math.sqrt(5)
> 2.23606797749979
> ```

### b) Importer précisément

Importer de **manière précise** revient à importer uniquement la fonction qui nous interesse du module et s'effectue avec les mot-clés `from` et `import`.

> [!TIP]
> Par exemple :
> ```python
> from math import sqrt
> ```

Dans ce cas ci, il n'y a plus besoin de devoir réécrire le nom du module.

> [!TIP]
> Par exemple :
> ```python
> >>> from math import sqrt
> >>> sqrt(5)
> 2.23606797749979
> ```

## III. Modules standards

### a) Module de mathématiques

Le module `math` possède toutes les fonctions mathématiques.

| Nom  du module : | `math` |
|---|---|
| Racine carrée de $n$ | `sqrt(n)` |
| Trigonométrie | `sin()`, `cos()` |
| Pi | `pi` |

Voir plus : [https://docs.python.org/fr/3.5/library/math.html](https://docs.python.org/fr/3.5/library/math.html)

### b) Module d'aléatoire

Le module `random` met à disposition plusieurs fonctions permettant de jouer avec l'aléatoire.

| Nom du module : | `random` |
|---|---|
| Entier aléatoire compris entre $x$ et $y$ | `randint(x : int, y : int)` |
| Nombre aléatoire compris entre $0$ et $1$ | `random()` |

Voir plus : [https://docs.python.org/fr/3/library/random.html](https://docs.python.org/fr/3/library/random.html)

#### <ins>Application 1</ins>

a) Dans un fichier `nom_prenom_importation_globale.py`, importer de manière globale le module `math` puis, dans la console, afficher la valeur de $\pi$.

b) Dans un second fichier `nom_prenom_importation_precise.py`, importer de manière précise le module `math` puis, dans la console, afficher la valeur de $\pi$.

________

[Exercices](./Exercices/Exercices_modules.md)

________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 