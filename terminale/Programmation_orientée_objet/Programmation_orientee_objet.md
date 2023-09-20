# Programmation orientée objet

## I. L'objet

### a) Définition

La *programmation orientée objet* est une manière différente d'approcher la programmation.

Elle consiste à utiliser des *objets*.

Un *objet* est une chose du monde réel.

Il possède ses propres données et son propre comportement.

### b) Attributs

Les données sont stockées dans des variables que nous appelons attributs.

Un *attribut* est une variable propre à l'objet.

Par exemple, l'objet `Personnage` peut posséder un nombre de points de vie et un nombre de point d'attaque.

### c) Méthodes

Le comportement des objets est défini dans des méthodes.

Une *méthode* est une fonction propre à l'objet.

Par exemple, l'objet `Personnage` peut avoir comme action celle de se soigner et d'attaquer.

##### Application 1

Trouver et noter des exemples d'attributs et de méthodes pour l'objet `Voiture`.

## II. Les classes

### a) Définition

Une *classe* est un moule permettant de créer un objet.

L'objet ainsi créé est appelé *instance de classe*.

Pour une classe donnée, nous pouvons créer plusieurs objets différents.

En Python, le mot-clé `class` permet d'écrire une classe :

```python
class Personnage :
```

### b) Instanciation de classe

Instancier une classe se fait en appelant la classe :

```python
>>> perso = Personnage()
```

La variable `perso` est une instance de la classe `Personnage` :

```python
>>> perso
<__main__.Personnage object at 0x7f1a67b168c0>
```

##### Application 2

a) Ouvrir Thonny et créer la classe `Voiture`.

b) Puis, à l'aide de la console, vérifier qu'il s'agit bien d'un objet.

## III. Constructeur

### a) Définition

Pour donner une valeur aux attributs de l'objet, nous faisons appel à une méthode : le constructeur.

En Python, le constructeur s'écrit avec le mot-clé `init` :

```python
class Personnage :
    def __init__(self):
        self.__point_de_vie = 50
        self.__point_d_attaque = 5
```

Les `__` entourant le `init` nous indique qu'il s'agit d'une méthode spéciale.

### b) Paramètre *self*

Le paramètre `self` (*soi* en Français) désigne l'instance de classe auquel nous faisons référence.

Ce paramètre doit être présent dans chaque méthode créée.

### c) Autres paramètres

Il est possible, d'ajouter des paramètres au constructeur pour donner une valeur à un attribut :

```python
class Personnage :
    def __init__(self, nom):
        self.__nom = nom
        self.__point_de_vie = 50
        self.__point_d_attaque = 5
```

Ainsi, lorsque nous instancions la classe, nous donnons une valeur à l'attribut `nom` :

```python
>>> perso = Personnage('Link')
```
##### Application 3

a) Ecrire le constructeur de la classe `Voiture` en reprennant les caractéristiques trouvées à l'application 1.

b) Ajouter un paramètre au constructeur de `Voiture`.

## IV. Accès aux attributs

### a) Accessibilité des attributs

Un attribut *privé* est accessible uniquement depuis l'intérieur de la classe. Un attribut privé s'écrit avec `__` devant son nom.

Un attribut *pubic* est accessible depuis l'extérieur de la classe.

Il est conseillé de toujours mettre ses attributs en privé.

### b) Accesseurs

Les *accesseurs* sont des méthodes permettant d'accéder aux valeurs des attributs :

```python
class Personnage :
    def __init__(self, nom):
        self.__nom = nom
        self.__point_de_vie = 50
        self.__point_d_attaque = 5

    def get_nom(self):
        return self.__nom
    
    def get_point_de_vie(self):
        return self.__point_de_vie

    def get_point_d_attaque(self):
        return self.__point_d_attaque
```

Résultat dans la console :

```python
>>> perso = Personnage('Link')
>>> perso.get_nom()
'Link'
>>> perso.get_point_de_vie()
50
>>> perso.get_point_d_attaque()
5
```

##### Application 4

a) Une fois après avoir mis les attributs de la classe `Voiture` en privé, écrire un accesseur pour chaque attribut de cette classe.

b) Puis, dans la console, vérifier l'accès à toutes les valeurs des attributs de la classe `Voiture` en utilisant les accesseurs.

##  V. Autres méthodes

Ajoutons à ma classe de personnage de jeu la compétence de se soigner de dix points de vie :

```python
class Personnage :
    def __init__(self, nom):
        self.__nom = nom
        self.__point_de_vie = 50
        self.__point_d_attaque = 5

    def get_nom(self):
        return self.__nom
    
    def get_point_de_vie(self):
        return self.__point_de_vie

    def get_point_d_attaque(self):
        return self.__point_d_attaque

    def se_soigner(self) :
        self.__point_de_vie = self.__point_de_vie + 10
```

##### Application 5

Ajouter la méthode `accelere()` dans la classe `Voiture` permettant d'augmenter l'attribut `vitesse` de $20$.

## VI. Principes de la POO

### a) Encapsulation

Le principe d'*encapsulation* consiste à rassembler les données et le comportement au sein de l'objet.

L'encapsulation empêche l'accès aux méthodes depuis l'extérieur de la classe.

Par exemple, la méthode `se_soigner()` n'est pas accessible autrement que par une instanciation de la classe `Personnage` :

```python
>>> se_soigner()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'se_soigner' is not defined
```

##### Application 6

Appeler la méthode `accelere()` depuis la console et vérifier que l'instruction renvoie bien une erreur.

### b) Responsabilité

Le principe de *responsabilité* est le suivant : une classe ne doit s'occuper que de ce pourquoi elle existe.

Il n'est pas responsable, par exemple, d'implémenter une méthode permettant de trouver l'élément maximum d'une liste dans la classe `Personnage`.

__________

[Feuille d'exercice](./Exercices_programmation_orientee_objet.md)

__________

[Sommaire](./../README.md)
