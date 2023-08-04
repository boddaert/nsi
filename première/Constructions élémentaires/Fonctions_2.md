## II. Renvoyer un résultat

### a) Fonctions et Procédures

Les fonctions renvoient une **valeur** en utilisant le mot-clé ``return``. Le mot-clé ``return`` est situé principalement à la fin de la fonction, lorsque son instruction est réalisée, elle **met fin à l'exécution** de la fonction. Attention à ne pas confondre la fonction ``print`` qui **affiche** un resultat et l'instruction ``return`` qui **renvoie** un resultat.

La valeur renvoyée **possède un type** comme n'importe quelle autre valeur que l'on a pu voir.

Lors de l'écriture de la définition de la fonction, on précise le type de la valeur renvoyée par la notation : `-> type`.

Par exemple, la fonction ``somme`` renvoie un entier.

Une fonction peut ne pas renvoyer de résultat, on appelle cette fonction spéciale : une **procédure**. 

La procédure n'a donc pas d'instruction ``return``, son exécution prend fin lorsque **toutes les instructions** du corps de la fonction ont été exécutées.

Le type de la valeur renvoyée par une procédure est `-> None`.

Objectifs :

- Une fonction a pour objectif de faire un calcul et de renvoyer une valeur.

- Une procédure réalise une action, par exemple un affichage, une écriture dans un fichier, etc...

### b) Expressions

L'appel d'une fonction **représente** une valeur et qui constitue une expression qu'on peut réutiliser dans nos programmes. Par exemple, l'affecter à une variable :

```python
res = somme( 2, 5 )
```

ou l'afficher grâce à la fonction ``print()`` :

```python
print(somme( 2, 5 ))
```

ou encore créer une expression plus complexe en imbriquant mes appels de fonctions :

```python
res = somme(somme( 3, 7 ), somme( 2, 5 ))
```

Ici, j'additionne le résultat de la somme de 3 et 7 avec le résultat de la somme de 2 et 5, ce qui fait 17. 

On peut représenter les appels de fonctions par un schéma :

![](./img/img_fonc/serie_appels.PNG)

Mais cela implique que la valeur renvoyée par ``somme( 2, 5 )`` soit du même type que le paramètre de ma fonction ``somme``. Ce qui est le cas, car ``somme( 2, 5 )`` renvoie un nombre entier et mes paramètres à ma fonction ``somme`` sont de type ``int``.

### c) Décomposer un problème avec des fonctions

Considérons le problème suivant :

On souhaite calculer le carré de la distance d'un point de coordonnées *( x, y )* à l'origine d'un repère orthonormal. Il se calcule $`x^2 + y^2`$.

Pour ce faire, nous pouvons définir une fonction ``carre( n : int)-> int`` permettant de calculer le carré d'un entier passé en paramètre :

```python
def carre( n : int)-> int :
    resultat = n ** 2
    return resultat
```

Puis, une fonction ``carre_distance_origine( x : int, y : int )-> int`` en utilisant la fonction ``somme``et la fonction ``carre`` :

```python
def carre_distance_origine( x : int, y : int )-> int :
    resultat = somme( carre(x), carre(y))
    return resultat
```

## III. Portée des variables

### a) Définition

La **portée** d'une variable désigne la zone de code dans le programme dans laquelle elle est accessible. Toutes nos variables ne sont pas nécessairement accessibles à n'importe quel endroit dans un programme et on ne va donc pas toujours pouvoir les utiliser.

On distingue les variables **globales** et **locales** qui possèdent une portée différente.

### b) Variables globales

Toutes les variables déclarées **hors de toute fonctions** sont les variables globales.

Une fonction peut accéder à une variable globale :

![](./img/img_fonc/var_globale.PNG)

Ici, on a déclarer une variable globale ``v = 42`` et une fonction ``double()-> int`` qui multiplie par 2 notre variable ``v`` déclarée hors de la fonction ``double()``.

On obtient comme résultat 84, ce qui prouve bien que notre fonction ``double()`` a accès à notre variable ``v``.

Lorsqu'une fonction accède à une variable globale, elle accède à sa valeur courante :

![](./img/img_fonc/var_globale2.PNG)

Ici, avant d'appeler ma fonction ``double()``, on a augmenté la valeur de ``v`` de 1 et on obtient donc comme résultat 86.

### c) Variables locales

Le corps d'une fonction peut introduire des variables pour ses calculs intermédiaires, on appelle ces variables : les variables locales et **ne sont accessibles que dans le corps de cette fonction**.

On peut le vérifier en définissant une fonction ``creer_variable()`` qui crée une variable locale, en appellant cette fonction et en vérifiant dans la console si la variable existe :

![](./img/img_fonc/var_locale1.PNG)

On remarque que j'obtiens bien une erreur ``NameError: name 'f' is not defined``lorsque je demande la valeur de ``f`` dans la console, même après avoir appelé la fonction ``creer_variable()``. Ce qui nous prouve que la variable ``f`` existe uniquement dans la fonction et n'est accessible que depuis cette fonction.

La variable locale ``f`` **disparaît après l'exécution de la fonction**.

Si je déclare une variable globale ``f`` avant l'appel à la fonction :

![](./img/img_fonc/var_locale2.PNG)

Pendant l'exécution de ``creer_variable()``, il existe simultanément deux variables qui s'appellent ``f`` : la variable globale et la variable locale. Dans ce cas, seule la variable locale est utilisée, on dit qu'elle *masque* la variable globale.