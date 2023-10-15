# Files

## I. Définitions

Une *structure de données linéaire* est une structure de données dans laquelle chaque élément possède une place et dont tous les éléments (sauf le dernier) a un successeur.

Il s'agit d'une structure évolutive, nous pouvons y ajouter ou supprimer des éléments.

Les *files* sont des structures linéaires de données dans lesquelles les insertions se font d'un côté et les suppressions de l'autre côté de la file.

Nous parlons de structure FIFO (*First In First Out*) pour premier entré, premier sorti en Français.

## II. Type abstrait

### a) Définition de la file

La structure d'une file correspond en partie à la structure d'une liste récursive définie dans la [leçon précédente](Listes_recursives.md).

Par conséquent, le type abstrait d'une file est le même que celui de la liste récursive avec pour seule modification les opérations d'insertions et de suppression.

### b) Opérations primitives

Les opérations primitives de la file sont :

- Créer une file vide.
- Vérifier si une file est vide.
- Enfiler un élément à la fin de la file.
- Défiler le sommet de la file.

## III. Implémentation en Python

### a) Classe File

Nous implémentons les files à l'aide de la classe `Liste`.

Ci-dessous une classe `File` contenant les opérations primitives définies plus haut dans le chapitre :

- Le constructeur permettant de soit créer une file vide.
- `est_vide()` permettant de vérifier si la file est vide.
- `enfile()` qui prend en paramètre un élément et enfile l'élément à la fin de la file.
- `defile()` permettant de défiler l'élément du sommet de la file et renvoie l'élément défilé.

```python
from liste import Liste

class File:
    def __init__(self):
        self.__file = Liste()
    
    def est_vide():
        pass

    def enfile(self, elt : int):
        pass

    def defile(self):
        pass
```

##### Application 1

Compléter les méthodes `est_vide()`, `enfile()` et `defile()` de la classe `File`.

### b) Utilisation de la classe 

```python
>>> f = File()
>>> f.est_vide()
True
>>> f.enfile(2)
>>> f.est_vide()
False
>>> f.enfile(3)
>>> f.defile()
2
```

##### Application 2

Sans utiliser l'ordinateur, dessiner à quoi ressemble la file après chaque instruction suivante :

```python
f = File()
f.enfile(5)
f.enfile(4)
f.defile()
f.enfile(2)
f.defile()
```

## IV. Activité : Tri crêpe

Matériel : Tas de crêpe schématisé par un tas de planche de bois.

Objectif : Ranger par ordre de taille de la plus petite à la plus grande le tas de crêpe. Avec la plus petite au sommet du tas et la plus grande tout en dessous du tas.

Pour cela, vous ne disposez que d'une seule action : placer la spatule entre deux crêpes dans le tas et retourner la partie supérieure.

a) Mettre au point et écrire un algorithme en Français permettant de trier le tas de crêpe.

b) Quelle est la structure de données la plus adaptée pour représenter le tas de crêpe ?

c) Quelle est la structure de données la plus adaptée pour effectuer le retournement du tas supérieur ?

d) Modifier et réécrire l'algorithme en Python et en utilisant les structures de données adaptées.

e) Vérifier le bon fonctionnement de l'algorithme sur Thonny.

_________

[Feuille d'exercice](./Exercices/Exercices_files.md)

_______________

[Sommaire](./../README.md)