# Dictionnaires

## I. Définitions

Un *dictionnaire* est une structure non linéaire mutable de données.

Une *structure de données* est une structure permettant d'organiser ses données dans l'objectif que le traitement de celles-ci soit efficace.

Une *structure non linéaire de données* est une structure de données dans laquelle chaque élément ne possède pas de position.

Une *structure non linéaire mutable de données* est une structure de données non linéaire dans laquelle les éléments peuvent être ajoutés, retirés ou modifiés.

| / | Linéaire | Non linéaire |
| :---: | :---: | :---: |
| **Mutable** | Liste | Dictionnaire |
| **Non mutable** | Tuple | Ensemble (hors programme) |

Étant donné que les éléments n'ont pas de position dans la structure, nous n'accédons donc pas aux éléments via leurs indices.

Un dictionnaire est un ensemble de paires *clé/valeur*.

Nous accédons à une valeur via sa clé. Toutes les clés sont uniques.

En Python, le type `dict` est encadré par des accolades :

```python
>>> type({'a' : 1, 'b': 2})
<class 'dict'>
```

Nous associons les paires clé/valeur par `:`. Ici, la valeur `1` est associée à la clé `'a'`.

Un *dictionnaire vide* est un dictionnaire ne contenant aucune paire clé/valeur :

```python
>>> type({})
<class = 'dict'>
```

Un dictionnaire peut contenir des paires clé/valeur de différents types :

```python
>>> type({'bonjour' : True, 42 : [1, 2, 3]})
<class = 'dict'>
```

##### Application 1

Sur Thonny, créer un dictionnaire appelé : `carte_id` ayant comme élément les paires clé/valeur suivantes :

- Votre nom en chaîne de caractère associé à la clé `nom`.

- Votre prénom en chaîne de caractère associé à la clé `prenom`.

- Votre âge en nombre entier associé à la clé `age`.

## II. Opérations sur les dictionnaires

### a) Taille

La *taille* d'un dictionnaire est le nombre de paire clé/valeur contenu dans celui-ci.

Elle peut être connue en utilisant la fonction `len()` :

```python
>>> len({'bonjour' : True, 42 : [1, 2, 3]})
2
```

##### Application 2

Écrire l'instruction permettant de vérifier que la taille de `carte_id` vaut $3$.

### b) Accès à une valeur

Nous accédons à une valeur du dictionnaire à l'aide de la clé associée.

Nous mettons la clé de la valeur que nous souhaitons obtenir entre crochets :

```python
>>> dico = {'bonjour' : True, 42 : [1, 2, 3]}
>>> dico['bonjour']
True
```

##### Application 3

À partir du dictionnaire `carte_id`, écrire :

- l'instruction permettant d'afficher votre nom.

- l'instruction permettant d'afficher votre prénom.

- l'instruction permettant d'afficher votre âge.

### c) Test d'appartenance

Nous pouvons vérifier si une clé est présente dans un dictionnaire à l'aide du mot-clé `in`.

```python
>>> 'bonjour' in dico
True
```

Le test d'appartenance renvoie comme résultat un booléen.

## III. Mutabilité

Une valeur est dite *mutable* si elle peut être modifiée.

Les dictionnaires sont mutables.

### a) Modification de valeur

Nous pouvons modifier les valeurs d'un dictionnaire :

```python
>>> dico['bonjour'] = False
>>> dico
{'bonjour': False, 42: [1, 2, 3]}
```

##### Application 4

Sur le dictionnaire `carte_id`, écrire l'instruction permettant d'ajouter un an à votre âge.

### b) Ajout de paire clé/valeur

L'ajout de paire clé/valeur s'effectue en associant une valeur à une clé non existante :

```python
>>> dico[55] = (3, 2, 1)
>>> dico
{'bonjour': False, 42: [1, 2, 3], 55: (3, 2, 1)}
```

##### Application 5

Écrire l'instruction permettant d'ajouter votre nationnalité au dictionnaire `carte_id`.

### c) Suppression de paire clé/valeur

La suppression de paire clé/valeur d'un dictionnaire s'effectue à l'aide du mot clé  `del` sur la clé :

```python
>>> del dico'55]
>>> dico
{'bonjour': False, 42: [1, 2, 3]}
```

-------------



### Application 2

A partir du dictionnaire vide ``carte_id``, écrire :

- l'instruction permettant d'ajouter au dictionnaire votre nom associé à la clé ``"nom"``.

- l'instruction permettant d'ajouter au dictionnaire votre prénom associé à la clé `"prenom"`.

- l'instruction permettant d'ajouter au dictionnaire votre âge associé à la clé `"age"`.

- l'instruction permettant d'ajouter au dictionnaire votre nationnalité associé à la clé `"nationnalite"`.

- l'instruction permettant d'ajouter au dictionnaire votre genre associé à la clé `"genre"`.

### Application 3



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