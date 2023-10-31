# Listes récursives

## I. Définitions

Une *structure de données linéaire* est une structure de données dans laquelle chaque élément possède une place et dont tous les éléments (sauf le dernier) a un successeur.

Il s'agit d'une structure évolutive, nous pouvons y ajouter ou supprimer des éléments.

En Python, nous définissons les listes avec les crochets `[]` ou la fonction `list()`.

Nous parlons dans ce chapitre d'un autre type de liste.

Une *liste récursive* est une structure de données linéaire utilisant la récursivité.

## II. Définition de la liste récursive et ses opérations

### a) Type abstrait

Une liste récursive est soit :

- Vide.
- Soit un couple constitué :
    + D'une *tête* représentant le premier élément de la liste.
    + D'un *reste*, une liste représentant le reste de la liste.

Nous remarquons qu'il s'agit bien là d'une définition récursive puisque le reste est lui-même une liste récursive.

### b) Notation

Nous notons la liste entre parenthèse sous la forme : $(tête, reste)$.

La liste vide se note $\emptyset$.

Ainsi, la liste constituée d'un unique élément $3$ s'écrit : $(3,(\emptyset))$.

Et la liste constituée de l'élément $5$ puis $2$ s'écrit : $(5,(2,(\emptyset)))$.

##### Application 1

Traduire les listes itératives suivantes en listes récursives :

- $(1)$

- $(1,2)$

- $(1,2,3)$

##### Application 2

Traduire les listes récursives suivantes en listes itératives :

- $(4,(5,(\emptyset)))$

- $(6,(7,(8,(9,(\emptyset)))))$

##### Application 3

Donner la tête des listes récursives suivantes :

- $(4,(5,(\emptyset)))$

- $(6,(7,(8,(9,(\emptyset)))))$

##### Application 4

Donner le reste des listes récursives suivantes :

- $(4,(5,(\emptyset)))$

- $(6,(7,(8,(9,(\emptyset)))))$

### c) Opérations primitives

Les *opérations primitives* sont celles qui constituent le strict minimum pour la définition d'une structure de données.

Voici ci-dessous les opérations primitives de la liste récursive.

- Créer une liste vide.
- Créer une liste avec une tête et un reste.
- Vérifier si une liste est vide.
- Récupérer la tête de liste.
- Récupérer le reste d'une liste.

### d) Opérations avancées

Voici ci-dessous une liste non exhaustive d'*opérations avancées* pour la liste récursive :

- Récupérer la longueur de la liste.
- Vérifier si un élément est présent ou non dans la liste.
- Récupérer l'élément d'indice $i$ dans la liste.
- Ajouter un élément à l'indice $i$.
- Supprimer un élément à l'indice $i$.
- Concaténer deux listes.

## III. Implémentation en Python

### a) Classe Liste

Nous implémentons les listes récursives en Python à l'aide de la programmation orientée objet.

Ci-dessous une classe `Liste` contenant les opérations primitives définies plus haut dans le chapitre :

- Le constructeur permettant de soit créer une liste vide soit une liste constituée d'une tête et d'un reste.
- `est_vide()` permettant de vérifier si la liste est vide.
- `tete()` permettant de récupérer la tête de la liste.
- `reste()` permettant de récupérer le reste de la liste.

```python
class Liste:
    def __init__(self, *args):
        if len(args) == 0 :
            self.__tete = None
            self.__reste = None
        elif len(args) == 2 :
            if isinstance(args[1], Liste):
                self.__tete = args[0]
                self.__reste = args[1]

    def est_vide(self):
        pass

    def tete(self):
        pass

    def reste(self):
        pass
```
##### Application 5

Compléter les méthodes `est_vide()`, `tete()` et `reste()` de la classe `Liste`.

### b) Utilisation de la classe

```python
>>> l = Liste()
>>> l.est_vide()
True
>>> l = Liste(5,Liste())
>>> l.est_vide()
False
>>> l.tete()
5
>>> l.reste()
<__main__.Liste object at 0x7f53bffa0400>
```

##### Application 6

En utilisant la classe `Liste`, créer et stocker dans les variables `l1` et `l2` les listes récursives de l'application 2.

##### Application 7

En utilisant les méthodes `tete()` et `reste()`, vérifier vos réponses à l'application 3 et 4.

##### Application 8

a) Sans utiliser l'ordinateur, donner le résultat des instructions suivantes :

```python
>>> l1.reste().tete()
```

```python
>>> l2.reste().reste().tete()
```

b) Vérifier vos résultats à l'aide de la console Python.

##### Application 9

a) Ecrire l'instruction permettant de retirer $4$ de `l1`.

b) Ecrire l'instruction permettant d'ajouter en tête de `l1` l'élément $8$.

## IV. Représentation en mémoire

Les listes peuvent être représentées en mémoire de deux manière différentes selon la définition de la structure.

Elles peuvent être en représentation contiguë ou en représentation chaînée.

### a) Représentation contiguë

Lorsque la liste est représentée contiguëllement, elle est stockée en mémoire sous forme de tableau de $N$ cellules.

Dans cette représentation, les cellules sont placées côte à côte les unes à la suite des autres :

![Représentation contiguë](./img/representation_contigue.drawio.png)

Les éléments sont stockés dans les cellules, l'élément d'indice $i$ se trouve donc à la $i-ème$ cellule.

Avantages : 

- Les cellules possèdent une place $i$, est donc très rapide d'accèder à l'élément d'indice $i$.

Inconvénients : 

- La taille $N$ d'une liste représentée sous forme de tableau doit être donné lors de la création de la liste, ainsi, le nombre d'élément de la liste ne doit pas dépassé le nombre de cellule.

- Lors d'un ajout ou d'une supression d'élément, le décalage des éléments suivants doit être réalisé.

### b) Représentation chaînée

Lorsque la liste est représentée sous forme chaînée, chaque élément est contenu dans une cellule indépendante des autres.

Dans cette représentation, la cellule possède une information supplémentaire : la référence vers la cellule suivante :

![Représentation chaînée](./img/representation_chainee.drawio.png)

La liste est donc définie sur la référence de la première cellule.

La référence de la dernière cellule est `None`.

Avantages :

- L'ajout et la suppression ne nécessite pas de décalage des éléments suivants, il suffit d'ajouter ou supprimer une cellule dans la chaîne et de modifier les références.

- Par conséquent, le nombre de cellule ne doit plus être défini lors de la création de la liste.

Inconvévients :

- L'accès à un élément d'indice $i$ nécessite alors de parcourir toute la liste depuis le début.

_________

[Feuille d'exercice](./Exercices/Exercices_listes_recursives.md)

_______________

[Sommaire](./../README.md)