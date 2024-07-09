# Programmation orientée objet

## I. L'objet

### a) Définitions

> [!IMPORTANT]
> La *programmation orientée objet* est une manière différente d'approcher la programmation.

Elle consiste à utiliser des objets.

> [!IMPORTANT]
> Un *objet* est une chose du monde réel. Il possède ses propres caractéristiques et son propre comportement.

### b) Attributs

Les caractéristiques d'un objet sont stockées dans des variables appelés attributs.

> [!IMPORTANT]
> Un *attribut* est une variable propre à l'objet.

> [!TIP]
> Par exemple :
> Un objet `Personnage` peut posséder un nombre de points de vie et un nombre de point d'attaque.

### c) Méthodes

Le comportement des objets est défini dans des méthodes.

> [!IMPORTANT]
> Une *méthode* est une fonction propre à l'objet.

> [!TIP]
> Par exemple :
> Un objet `Personnage` peut avoir comme action celle d'attaquer.

#### <ins>Application 1</ins>

a) Proposer une liste d'attributs pour un objet `Voiture`.

b) Proposer une liste de méthodes pour un objet `Voiture`.

## II. Les classes

### a) Définition

> [!IMPORTANT]
> Une *classe* est un moule permettant de créer un objet. L'objet ainsi créé est appelé *instance de classe*.

> [!NOTE]
> Pour une classe donnée, nous pouvons créer plusieurs objets différents.

En Python, le mot-clé `class` permet d'écrire une classe.

> [!TIP]
> Par exemple :
> ```python
> class Personnage :
> ```

### b) Instanciation de classe

Instancier une classe se fait en appelant la classe.

> [!TIP]
> Par exemple :
> ```python
> >>> perso = Personnage()
> >>> perso
> <__main__.Personnage object at 0x7f1a67b168c0>
> ```

#### <ins>Application 2</ins>

a) Créer la classe `Voiture`.

b) Puis dans une variable `ma_voiture`, instancier la classe `Voiture`.

## III. Constructeur

### a) Définition

Pour donner une valeur par défaut aux attributs de l'objet, nous faisons appel à une méthode : le constructeur.

En Python, le constructeur s'écrit avec le mot-clé `init`.

> [!TIP]
> Par exemple :
> ```python
> class Personnage :
>     def __init__(self):
>         self.__point_de_vie = 50
>         self.__point_d_attaque = 5
> ```

> [!NOTE]
> Les `__` entourant le `init` nous indique qu'il s'agit d'une méthode spéciale.

### b) Paramètre *self*

> [!IMPORTANT]
> Le paramètre `self` (*soi* en français) désigne l'instance de classe auquel nous faisons référence.

> [!WARNING]
> Ce paramètre doit être présent dans chaque méthode créée.

#### <ins>Application 3</ins>

Écrire le constructeur de la classe `Voiture` en reprennant les caractéristiques trouvées à l'application $1$.

### c) Passage des valeurs via paramètres

Il est possible, d'ajouter des valeurs par défaut aux attributs via d'autres paramètres.

> [!TIP]
> Par exemple :
> ```python
> class Personnage :
>     def __init__(self, nom):
>         self.__nom = nom
>         self.__point_de_vie = 50
>         self.__point_d_attaque = 5
> ```

Lors de l'instance de classe, les attributs prennent en valeur les arguments.

> [!TIP]
> Par exemple :
> ```python
> >>> perso = Personnage('Link')
> ```

#### <ins>Application 4</ins>

Ajouter le paramètre `nom` et son attribut au constructeur de la classe `Voiture`.

## IV. Accès aux attributs

### a) Accessibilité des attributs

> [!IMPORTANT]
> Un attribut *privé* est accessible uniquement depuis l'intérieur de la classe. Un attribut privé s'écrit avec `__` devant son nom.

> [!IMPORTANT]
> Un attribut *pubic* est accessible depuis l'extérieur de la classe.

Il est conseillé de toujours mettre ses attributs en privé.

### b) Accesseurs

> [!IMPORTANT]
> Les *accesseurs* sont des méthodes permettant d'accéder aux valeurs des attributs.

Les accesseurs sont usuellement notés `get_<nom_de_l_attribut>`.

> [!TIP]
> Par exemple :
> ```python
> class Personnage :
>     def __init__(self, nom):
>         self.__nom = nom
>         self.__point_de_vie = 50
>         self.__point_d_attaque = 5
>
>     def get_nom(self):
>         return self.__nom
>    
>     def get_point_de_vie(self):
>         return self.__point_de_vie
>
>     def get_point_d_attaque(self):
>         return self.__point_d_attaque
> ```
>
> Résultat dans la console :
>
> ```python
> >>> perso = Personnage('Link')
> >>> perso.get_nom()
> 'Link'
> >>> perso.get_point_de_vie()
> 50
> >>> perso.get_point_d_attaque()
> 5
> ```

#### <ins>Application 5</ins>

a) Une fois après avoir mis les attributs de la classe `Voiture` en privé, écrire un accesseur pour chaque attribut de cette classe.

b) Puis, dans la console, vérifier l'accès à toutes les valeurs des attributs de la classe `Voiture` en utilisant les accesseurs.

##  V. Autres méthodes

Les méthodes peuvent modifier les valeurs des attributs.

> [!TIP]
> Par exemple :
> ```python
> class Personnage :
>     def __init__(self, nom):
>         self.__nom = nom
>         self.__point_de_vie = 50
>         self.__point_d_attaque = 5
>
>     def get_nom(self):
>         return self.__nom
>    
>     def get_point_de_vie(self):
>         return self.__point_de_vie
>
>     def get_point_d_attaque(self):
>         return self.__point_d_attaque
>
>     def se_soigner(self) :
>         self.__point_de_vie = self.__point_de_vie + 10
> ```

#### <ins>Application 6</ins>

Ajouter la méthode `accelere()` dans la classe `Voiture` permettant d'augmenter l'attribut `vitesse` de $20$.

## VI. Principes de la POO

### a) Encapsulation

> [!IMPORTANT]
> Le principe d'*encapsulation* consiste à rassembler les données et le comportement au sein de l'objet. L'encapsulation empêche l'accès aux méthodes depuis l'extérieur de la classe.

> [!TIP]
> Par exemple, la méthode `se_soigner()` n'est pas accessible autrement que par une instanciation de la classe `Personnage` :
>
> ```python
> >>> se_soigner()
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> NameError: name 'se_soigner' is not defined
> ```

#### <ins>Application 7</ins>

Appeler la méthode `accelere()` depuis la console et vérifier que l'instruction renvoie bien une erreur.

### b) Responsabilité

> [!IMPORTANT]
> Le principe de *responsabilité* est le suivant : une classe ne doit s'occuper que de ce pourquoi elle existe.

> [!TIP]
> Il n'est pas responsable, par exemple, d'implémenter une méthode permettant de trouver l'élément maximum d'une liste dans la classe `Personnage`.

__________

[Exercices](./Exercices/Exercices_programmation_orientee_objet.md)

__________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 
