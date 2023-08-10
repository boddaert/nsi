# Programmation orientée objet

## I. Définition

La *programmation orientée objet* se distingue de la programmation impérative (celle avec laquelle nous avons l'habitude d'écrire nos programmes).

Elle consiste à utiliser des *objets*.

Un *objet* est un concept, une idée ou toute entité du monde physique. Il possède une structure de données propre à lui-même et un comportement.

Par exemple, un véhicule ou un personnage de jeu vidéo sont des objets informatiquement parlant.

Nous écrivons alors la structure de données souhaitée selon l'objet en définissant ses caractéristiques appelés *attributs*.

Par exemple, le personnage de jeu possède un nombre de points de vie, d'attaque, de défense.

Puis nous écrivons son comportement en définissant ses actions appelées *méthodes*.

Par exemple, le personnage de jeu a comme action celle de se soigner.

Les attributs et les méthodes sont écrites dans les classes.

## II. Les classes

### a) Définition

Une *classe* est un moule permettant de créer un objet.

Pour une classe donnée, nous pouvons créer plusieurs objets.

En Python, le mot-clé `class` permet d'écrire une classe :

```python
class Personnage :
```

### b) Constructeur

Pour créer un objet à partir d'une classe, nous faisons appel à une méthode : le constructeur.

Une *méthode* est un fonction propre à la classe, il y a les méthodes de comportement et les méthodes spéciales. Elles s'écrivent simplement en Python à l'aide du mot-clé `def`.

Le *constructeur* est une méthode spéciale qui permet de créer les attributs et de mettre une valeur par défaut aux attributs.

En Python, le constructeur s'écrit avec le mot-clé `init` :

```python
class Personnage :
    def __init__(self):
        self.point_de_vie = 50
        self.point_d_attaque = 5
        self.point_de_defense = 2
```

Suite à cet exemple, nous constatons plusieurs choses :

- Premièrement, les attributs `point_de_vie`, `point_d_attaque` et `point_de_defense` agissent comme des variables et ont comme valeurs par défaut $50$, $5$ et $2$ respectivement.

- Deuxièmement, les `__` entourant le `init` nous indique qu'il s'agit d'une méthode spéciale.

- Troisièmement, le paramètre `self` (*soi* en Français) désigne l'objet auquel nous faisons référence. Ce paramètre doit être présent dans chaque méthode créée.

### c) Méthodes de comportement

Les méthodes de comportement désignent les actions que peut effectuer l'objet.

Ajoutons à ma classe de personnage de jeu la compétence de se soigner de dix points de vie :

```python
class Personnage :
    def __init__(self):
        self.point_de_vie = 50
        self.point_d_attaque = 5
        self.point_de_defense = 2

    def se_soigner(self) :
        self.point_de_vie = self.point_de_vie + 10
```

## III. Encapsulation



## IV. Instancier une classe

Nous appelons *instance de classe*, l'objet créé à partir de cette classe.

Nous stockons l'instance de classe dans une variable :

```python
>>> personnage_1 = Personnage()
```