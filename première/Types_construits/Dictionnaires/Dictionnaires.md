# Dictionnaires

## I. Définitions

> [!IMPORTANT]
> Un *dictionnaire* est une structure non linéaire mutable de données.
>
> Il est un ensemble de paires clé/valeur.

> [!IMPORTANT]
Une *structure de données* est une structure permettant d'organiser ses données dans l'objectif que le traitement de celles-ci soit efficace.

> [!IMPORTANT]
> Une *structure non linéaire de données* est une structure de données dans laquelle chaque élément ne possède pas de position.

> [!IMPORTANT]
> Une *structure non linéaire mutable de données* est une structure de données non linéaire dans laquelle les éléments peuvent être ajoutés, retirés ou modifiés.

## II. Récapitulatif

> [!IMPORTANT]
> | / | Linéaire | Non linéaire |
> | :---: | :---: | :---: |
> | **Mutable** | Liste | Dictionnaire |
> | **Non mutable** | Tuple | Ensemble (hors programme) |

## III. En Python

### a) Spécificités

Les dictionnaires en Python sont définis entre accolades (`{` `}`).

> [!TIP]
> Par exemple :
> ```python
> {'a' : 1, 'b' : 2}
> ```

Les dictionnaires sont de type `dict`.

> [!TIP]
> Par exemple :
> ```python
> >>> type({'a' : 1, 'b' : 2})
> <class 'dict'>
> ```

> [!IMPORTANT]
> Un *dictionnaire vide* est un dictionnaire ne contenant aucune paire clé/valeur.

> [!TIP]
> Par exemple :
> ```python
> >>> type({})
> <class 'dict'>
> ```

Les clés d'un dictionnaire sont associées à leur valeur avec `:`.

> [!TIP]
> Par exemple :
> ```python
> {'a' : 1, 'b' : 2}
> ```
>
> Les clés sont `'a'` et `'b'`, leur valeur sont respectivement `1` et `2`.

Un dictionnaire peut contenir des valeurs de différents types.

> [!TIP]
> Par exemple :
> ```python
> {'a' : True, 'b' : [1, 2, 3]})
> ```

Un dictionnaire peut contenir des clés de différent type sauf structure de données.

> [!TIP]
> Par exemple :
> ```python
> >>> {[1, 2, 3] : 1, 'b' : 2}
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> TypeError: unhashable type: 'list'
> ```

#### <ins>Application 1</ins>

Sur Thonny, créer un dictionnaire appelé : `carte_id` contenant les paires clé/valeur suivantes :

1. Votre nom en chaîne de caractère associé à la clé `nom`.

2. Votre prénom en chaîne de caractère associé à la clé `prenom`.

3. Votre âge en entier associé à la clé `age`.

### b) Opérations

#### 1. Taille

> [!IMPORTANT]
> La *taille* d'un dictionnaire est le nombre de paire clé/valeur contenu dans celui-ci.

Elle peut être connue en utilisant la fonction `len()` (pour *length* en anglais):

> [!TIP]
> Par exemple :
> ```python
> >>> len({'a' : 1, 'b' : 2})
> 2
> ```

#### <ins>Application 2</ins>

Écrire l'instruction permettant de donner la taille de `carte_id`.

#### 2. Accès à une valeur

Étant donné que les éléments n'ont pas de position dans la structure, nous n'accédons donc pas aux éléments via leurs indices mais via leur clé.

L'accès à une valeur s'effectue en écrivant la clé entre crochets.

> [!TIP]
> Par exemple :
> ```python
> >>> dico = {'a' : 1, 'b' : 2}
> >>> dico['a']
> 1
> ```

#### <ins>Application 3</ins>

À partir du dictionnaire `carte_id`, écrire :

1. L'instruction permettant de renvoyer votre nom.

2. L'instruction permettant de renvoyer votre prénom.

3. L'instruction permettant de renvoyer votre âge.

#### 3. Test d'appartenance

> [!IMPORTANT]
> Le *test d'appartenance* permet de savoir si une valeur est présente dans une autre.

Nous pouvons vérifier si une clé est présente dans un dictionnaire à l'aide du mot-clé `in`.

> [!TIP]
> Par exemple :
> ```python
> >>> 'a' in dico
> True
> >>> 1 in dico
> False
> ```

> Le test d'appartenance renvoie comme résultat un booléen.

### c) Mutabilité

> [!IMPORTANT]
> Une valeur est dite *mutable* si elle peut être modifiée.

Les dictionnaires sont mutables, les éléments peuvent y être modifiés, ajoutés ou supprimés.

#### 1. Modification de valeur

Modifier une valeur dans un dictionnaire s'effectue en réaffectant une valeur à une clé donnée.

> [!TIP]
> Par exemple :
> ```python
> >>> dico['b'] = 0
> >>> dico
> {'a': 1, 'b' : 0}
> ```

#### <ins>Application 4</ins>

Sur le dictionnaire `carte_id`, écrire l'instruction permettant d'ajouter un an à votre âge.

#### 2. Ajout de paire clé/valeur

L'ajout de paire clé/valeur s'effectue en associant une valeur à une clé non existante entre crochets.

> [!TIP]
> Par exemple :
> ```python
> >>> dico['c'] = 3
> >>> dico
> {'a': 1, 'b' : 0, 'c' : 3}
> ```

#### <ins>Application 5</ins>

Écrire l'instruction permettant d'ajouter votre nationnalité, votre date et lieu de naissance au dictionnaire `carte_id`.

#### 3. Suppression de paire clé/valeur

La suppression de paire clé/valeur d'un dictionnaire s'effectue à l'aide du mot clé  `del` sur la clé :

> [!TIP]
> Par exemple :
> ```python
> >>> del dico['c']
> >>> dico
> {'a': 1, 'b' : 0}
> ```

#### <ins>Application 6</ins>

Écrire l'instruction permettant de supprimer votre lieu de naissance du dictionnaire `carte_id`.

### d) Parcours de dictionnaire

> [!IMPORTANT]
> Un *parcours de dictionnaire* consiste à visiter tous les éléments du dictionnaire une et une seule fois dans le but de leur appliquer un traitement.

Nous parcourons les dictionnaires en utilisant les boucles.

> Comme nous connaissons à l'avance la taille d'un dictionnaire, nous connaissons à l'avance le nombre de tour de boucle nécessaire au parcours : Nous utilisons donc la boucle `for`.

Il existe trois façons de parcourir les dictionnaires :

1. Le parcours des clés.

2. Le parcours des valeurs.

3. Le parcours des paires clé/valeur.

#### 1. Parcours des clés

Récupérer l'ensemble des clés d'un dictionnaire s'effectue avec la méthode `keys()`.

> [!TIP]
> Par exemple :
> ```python
> >>> dico.keys()
> dict_keys(['a', 'b'])
> ```

Parcourir les clés d'un dictionnaire revient à faire le parcours par élément de l'ensemble des clés renvoyé par la méthode `keys()`.

> [!TIP]
> Par exemple :
> ```python
> for cle in dico.keys():
>     print(cle)
> ```
>
> Le programme affichera dans la console `'a'` puis `'b'`.

#### <ins>Application 7</ins>

Écrire le programme permettant d'afficher toute les clés du dictionnaire `carte_id`.

#### 2. Parcours des valeurs

Récupérer l'ensemble des valeurs d'un dictionnaire s'effectue avec la méthode `values()`.

> [!TIP]
> Par exemple :
> ```python
> >>> dico.values()
> dict_values([1, 0])
> ```

Parcourir les valeurs d'un dictionnaire revient à faire le parcours par élément de l'ensemble des valeurs renvoyé par la méthode `values()`.

> [!TIP]
> Par exemple :
> ```python
> for valeur in dico.values():
>     print(valeur)
> ```
>
> Le programme affichera `1` puis `0`.

#### <ins>Application 8</ins>

Écrire le programme permettant d'afficher toute les valeurs du dictionnaire `carte_id`.

#### 3. Parcours des paires clé/valeur

Récupérer l'ensemble des paires clé/valeur (sous forme de tuple) d'un dictionnaire s'effectue avec la méthode `items()`.

> [!TIP]
> Par exemple :
> ```python
> >>> dico.items()
> dict_items([('a', 1), ('b', 0)])
> ```

Parcourir les paires clé/valeur d'un dictionnaire revient à faire le parcours par élément de l'ensemble des paires clé/valeur renvoyé par la méthode `items()`.

> [!TIP]
> Par exmple :
> ```python
> for cle, valeur in dico.items():
>     print(cle)
>     print(valeur)
> ```
>
> Le programme affichera `'a'`, `1` puis `'b'` et `0`.

> Les éléments de la séquence renvoyée par la méthode `items()` étant des tuples, la variable `cle` et la variable `valeur` contiennent respectivement le premier élément et le second élément du tuple (le premier étant la clé et le second la valeur).

#### <ins>Application 9</ins>

Écrire le programme permettant d'afficher toute les paires clé/valeur du dictionnaire `carte_id`.

___________________

[Exercices](./Exercices/Exercices_dictionnaires.md)

___________________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 