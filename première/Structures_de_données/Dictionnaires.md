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

Écrire l'instruction permettant d'ajouter votre nationnalité, votre date et lieu de naissance au dictionnaire `carte_id`.

### c) Suppression de paire clé/valeur

La suppression de paire clé/valeur d'un dictionnaire s'effectue à l'aide du mot clé  `del` sur la clé :

```python
>>> del dico'55]
>>> dico
{'bonjour': False, 42: [1, 2, 3]}
```

##### Application 6

Finalement, écrire l'instruction permettant de supprimer votre lieu de naissance du dictionnaire `carte_id`.

## IV. Parcours de dictionnaire

Un *parcours de dictionnaire* consiste à visiter tous les éléments du dictionnaire une et une seule fois dans le but de leur appliquer un traitement.

Nous parcourons les dictionnaires en utilisant les boucles.

Comme nous connaissons à l'avance la taille d'un dictionnaire, nous connaissons à l'avance le nombre de tour de boucle nécessaire au parcours : Nous utilisons donc la boucle `for`.

Il existe trois façons de parcourir les dictionnaires :

- Le parcours des clés.

- Le parcours des valeurs.

- Le parcours des paires clé/valeur.

### a) Parcours des clés

Nous pouvons récupérer l'ensemble des clés d'un dictionnaire avec la méthode `keys()` :

```python
>>> dico.keys()
dict_keys(['bonjour', 42])
```

Il suffit alors de parcourir cet ensemble avec un simple parcours de liste par élément :

```python
for cle in dico.keys():
    print(cle)
```

##### Application 7

Écrire le programme permettant d'afficher toute les clés du dictionnaire `carte_id`.

### c) Parcours des valeurs

Nous pouvons récupérer l'ensemble des valeurs d'un dictionnaire avec la méthode `values()` :

```python
>>> dico.values()
dict_values([False, [1, 2, 3]])
```

Il suffit alors de parcourir cet ensemble avec un simple parcours de liste par élément :

```python
for valeur in dico.values():
    print(valeur)
```

##### Application 8

Écrire le programme permettant d'afficher toute les valeurs du dictionnaire `carte_id`.

### d) Parcours des paires clé/valeur

Nous pouvons récupérer l'ensemble des paires clé/valeur (sous forme de tuple) d'un dictionnaire avec la méthode `items()` :

```python
>>> dico.items()
dict_items([('bonjour', False), (42, [1, 2, 3])])
```

Il suffit alors de parcourir cet ensemble avec un simple parcours de liste par élément :

```python
for cle, valeur in dico.items():
    print(cle)
    print(valeur)
```

> *Remarque : Les éléments de la séquence renvoyée par la méthode `items()` étant des tuples, la variable `cle` et la variable `valeur` contiennent respectivement le premier élément et le second élément du tuple (le premier étant la clé et le second la valeur).*

##### Application 9

Écrire le programme permettant d'afficher toute les paires clé/valeur du dictionnaire `carte_id`.

___________________

[Feuille d'exercices](./Exercices/Exercices_dictionnaires.md)

___________________

[Sommaire](./../README.md)