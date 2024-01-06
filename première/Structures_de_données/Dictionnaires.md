# Dictionnaires

## I. Définition

Les dictionnaires sont des structures de données **non ordonnées**. On n'accède donc pas aux valeurs via leurs indices (ou positions dans la structure).

On accède à une valeur via sa **clé**. Toutes les clés doivent donc être différentes.

Un dictionnaire est un ensemble de paires **clé / valeur**.

Les clés et les valeurs peuvent être de tout type.

## II. Créer, Ajouter, Accéder et Supprimer

### a) Créer

Un dictionnaire s'écrit en Python avec des accolades.

On peut créer un dictionnaire vide :

```python
>>> dico = {}
```

Ou le créer directement avec des clés et des valeurs :

```python
>>> dico = {'triangle' : 3, 'quadrilatère' : 4, 'pentagone' : 5}
>>> dico2 = {3 : 'triangle', 4 : 'quadrilatère', 8 : 'octogone'}
```

*Remarque : Les paires clé / valeur sont séparées par des virgules.*

*Les valeurs sont associées aux clés avec le deux points.*

*Les clés et valeurs peuvent être de n'importe quel type.*

### b) Ajouter

On ajoute dans un dictionnaire une paire clé / valeur avec l'affectation de la valeur à la clé  :

```python
>>> dico['octogone'] = 8
>>> dico2[5] = 'pentagone'
```

### c) Accéder

A partir d'une clé, on peut accéder à sa valeur correspondante :

```python
>>> dico['pentagone']
5
>>> dico2[8]
'octogone' 
```

### d) Supprimer

On supprime une paire clé / valeur d'un dictionnaire avec le mot ``del`` sur la clé :

```python
>>> del dico['triangle']
```

-------------

### Application 1

Sur Thonny, créer un dictionnaire vide `carte_id`.

### Application 2

A partir du dictionnaire vide ``carte_id``, écrire :

- l'instruction permettant d'ajouter au dictionnaire votre nom associé à la clé ``"nom"``.

- l'instruction permettant d'ajouter au dictionnaire votre prénom associé à la clé `"prenom"`.

- l'instruction permettant d'ajouter au dictionnaire votre âge associé à la clé `"age"`.

- l'instruction permettant d'ajouter au dictionnaire votre nationnalité associé à la clé `"nationnalite"`.

- l'instruction permettant d'ajouter au dictionnaire votre genre associé à la clé `"genre"`.

### Application 3

A partir du dictionnaire `carte_id`, écrire :

- l'instruction permettant d'afficher votre nom.

- l'instruction permettant d'afficher votre prénom.

- l'instruction permettant d'afficher votre l'âge.

### Application 4

Finalement, écrire :

- l'instruction permettant de supprimer le genre de ``carte_id``.

-----

## III. Parcourir un dictionnaire

Grâce aux méthode `keys()`, `values()` et `items()`. On peut parcourir un dictionnaire respectivement par ses clés, par ses valeurs ou par ses paires clé / valeur.

### a) Par les clés

Avec la méthode ``keys()``, on peut récupérer sous forme de séquence l'ensemble des clés du dictionnaire :

```python
>>> dico.keys()
dict_keys(['triangle', 'quadrilatère', 'pentagone', 'octogone'])
```

On parcourt simplement les éléments de la séquence renvoyée par la méthode `keys()` :

```python
for cle in dico.keys():
    print(cle)
```

### c) Par les valeurs

Avec la méthode `values()`, on peut récupérer sous forme de séquence l'ensemble des valeurs du dictionnaire :

```python
>>> dico.values()
dict_values([3, 4, 5, 8])
```

On parcourt simplement les éléments de la séquence renvoyée par la méthode `values()` :

```python
for val in dico.values():
    print(val)
```

### d) Par les paires clé / valeur

Avec la méthode ``items()``, on peut récupérer sous forme de séquence l'ensemble des paires clé / valeur (mis en tuple) du dictionnaire :

```python
>>> dico.items()
dict_items([('triangle', 3), ('quadrilatère', 4), ('pentagone', 5), ('octogone', 8)])
```

On parcourt simplement les éléments de la séquence renvoyée par la méthode `items()` :

```python
for cle, val in dico.items():
    print(cle)
    print(val)
```

*Remarque : Les éléments de la séquence renvoyée par la méthode `items()` étant des tuples, la variable `cle` et la variable `val` contiennent respectivement le premier élément et le second élément du tuple (le premier étant la clé et le second la valeur).*

-----------

### Application 5

A l'aide d'un parcours par clés, afficher toutes les clés du dictionnaire ``carte_id``.

### Application 6

A l'aide d'un parcours par valeurs, afficher toutes les valeurs du dictionnaire `carte_id`.

### Application 7

A l'aide d'un parcours par paires clé / valeur, afficher toutes les clés et les valeurs du dictionnaire `carte_id`.

------------------

## IV. Longueur et appartenance

### a) Longueur

La longueur d'un dictionnaire est le nombre de clé présentes dans le dictionnaire et se récupère avec la fonction ``len`` :

```python
>>> len(dico)
4
```

### b) Appartenance

Le test d'appartenance à un dictionnaire s'applique aux clés. Il se réalise avec le mot ``in`` et renvoie un booléen :

```python
>>> 'quadrilatère' in dico
True
```

___________________

[Feuille d'exercices](./Exercices/Exercices_dictionnaires.md)

___________________

[Sommaire](./../README.md)