# Piles

## I. Définitions

Une *structure de données linéaire* est une structure de données dans laquelle chaque élément possède une place et dont tous les éléments (sauf le dernier) a un successeur.

Il s'agit d'une structure évolutive, nous pouvons y ajouter ou supprimer des éléments.

Les *piles* sont des structures linéaires de données dans lesquelles les insertions et les suppressions ne se font qu'au sommet de la pile.

Nous parlons de structure LIFO (*Last In First Out*) pour dernier entré, premier sorti en Français.

## II. Type abstrait

### a) Définition de la pile

La structure d'une pile correspond à la structure d'une liste récursive définie dans la [leçon précédente](Listes_recursives.md).

Par conséquent, le type abstrait d'une pile est le même que celui de la liste récursive.

### b) Opérations primitives

Les opérations primitives de la pile sont :

- Créer une pile vide.
- Vérifier si une pile est vide.
- Empiler un élément au sommet de la pile.
- Dépiler le sommet de la pile.

## III. Implémentation en Python

### a) Classe Pile

Nous implémentons les piles à l'aide de la classe `Liste`.

Ci-dessous une classe `Pile` contenant les opérations primitives définies plus haut dans le chapitre :

- Le constructeur permettant de soit créer une pile vide.
- `est_vide()` permettant de vérifier si la pile est vide.
- `empiler()` qui prend en paramètre un élément et empile l'élément au sommet de la pile.
- `depiler()` permettant de dépiler la pile et renvoie l'élément dépilé.

```python
from liste import Liste

class Pile:
    def __init__(self):
        self.pile = Liste()
    
    def est_vide():
        pass

    def empiler(self, elt : int):
        pass

    def depiler(self):
        pass
```

### b) Utilisation de la classe 

