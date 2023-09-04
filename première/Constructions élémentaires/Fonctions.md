# Fonctions

Voyons le programme suivant :

```python
hauteur_parallelepipede = 2
largeur_parallelepipede = 2
longueur_parallelepipede = 5

aire_rectangle = longueur_parallelepipede * hauteur_parallelepipede
aire_carre = hauteur_parallelepipede * largeur_parallelepipede

aire_parallelepipede = (aire_rectangle * 4) + (aire_carre * 2)
```

Ce programme permet de calculer la somme des aires d'un parallèlépipède de hauteur $2$, de largeur $2$ et de longueur $5$.

Nous constatons que nous avons calculé deux fois une aire : Une première fois pour l'aire d'un rectangle et la seconde pour un carré.

L'opération effectuée est la même (une multiplication) mais les opérandes sont différents.

Afin d'éviter de réécrire plusieurs fois une instruction réalisant la même action, nous utilisons les fonctions.

Ainsi, ici nous aurions pu utiliser une fonction `aire()` qui s'occupe de calculer une aire.

## I. Définition

Une *fonction* est une séquence d'instruction réutilisable. Elle associe une séquence d'instruction à un nom.

Nous la distinguons des variables parce que le nom est suivi de parenthèses.

Elle réalise une tâche précise et peut dépendre de paramètres.

Par exemple, la fonction `type()` que nous avons vu au chapitre sur les types (cf : [Types](./Types.md)) permet d'obtenir le type de la valeur passée en paramètre.

```python
>>> type(5)
<class 'int'>
```

### a) Signature

Soit `somme()` la fonction permettant de faire la somme de deux entiers.

Pour être un peu plus précis sur la définition d'une fonction, nous écrivons sa signature.

La *signature d'une fonction* est composée du nom de la fonction, du nom et du type des paramètres, du type de la valeur du résultat renvoyé par la fonction.

Ainsi, la signature de la fonction `somme()` s'écrirait : `somme(a : int, b : int) -> int`.

- Le nom est : `somme()`.

- Les paramètres sont $`a`$ et $`b`$ et sont tous les deux de type `int`.

- La valeur renvoyée par cette fonction est de type `int`.

La fonction `somme()` permet de faire la somme des entiers $a$ et $b$ passés en paramètres.

##### Application 1

Donner, pour chaque signature, le nom de la fonction, son ou ses paramètres ainsi que leur type et le type de la valeur de résultat :

- ``produit(a : int, b : int) -> int``

- ``est_superieur_a(a : int, b : int) -> bool``

- ``pythagore( a : float, b : float, c : float) -> float``

- ``nombre_caracteres(mot : str ) -> int``

##### Application 2

Ecrire la signature de la fonction ``maximum()``qui prend en paramètres deux entiers $a$ et $b$ et renvoie comme résultat un entier.

##### Application 3

Ecrire la signature de la fonction ``contient()`` qui prend en paramètre une chaîne de caractère $mot$, un caractère $lettre$ et renvoie comme résultat un booléen.

### b) Paramètres

Une fonction peut avoir zéro ou plusieurs paramètres.

Un *paramètre* est le nom d'une variable utilisée à l'intérieur de la fonction.

Lors de l'écriture d'une fonction, ses paramètres désignent alors une valeur qui n'est pas connue et qui pourra être différente à chaque utilisation.

## II. Ecriture de fonction

Une fonction en Python est composé de sa définition, d'un corps et d'un résultat.

### a) Définition d'une fonction en Python

Nous écrivons les fonctions en Python en utilisant le mot-cle : `def` suivi de la signature de la fonction suivi d'un `:`.

```python
def somme(a : int, b : int) -> int :
```

### b) Corps d'une fonction

Le *corps* d'une fonction est la séquence d'instruction située à l'intérieur.

Le corps d'une fonction est *indenté*, c'est-à-dire qu'il est légèrement décalé vers la droite.

```python
def somme(a : int, b : int) -> int :
    resultat = a + b
```

### c) Résultat d'une fonction

Le mot-clé `return` permet de renvoyer un résultat.

Cette instruction est toujours la dernière.

```python
def somme(a : int, b : int) -> int :
    resultat = a + b
    return resultat
```

### e) Procédures

Une *procédure* est une fonction ne renvoyant pas de résultat et donc ne contient pas d'instruction `return`.

##### Application 4

Ecrire, en Python, la fonction ``produit(a : int, b : int) -> int`` qui prend en paramètres deux entiers $a$ et $b$ et renvoie comme résultat $`a * b`$.

##### Application 5

Ecrire, en Python, la fonction `carre(n : int) -> int` qui prend en paramètres un entier $n$ et renvoie comme résultat $`n²`$.

## III. Appels de fonction

Lorsque nous utilisons une fonction pour obtenir un résultat, nous réalisons un *appel* à cette fonction.

Pour appeler une fonction, il suffit d'écrire le nom de la fonction avec, entre parenthèses, des arguments.

### a) Arguments

Paramètres et arguments ne définissent pas la même chose.

Un *argument* est la valeur que prend un paramètre lors d'un appel de fonction.

Ci-dessous, un exemple d'appel à la fonction `somme()` définie plus haut :

```python
>>> somme(5,2)
7
```

Les arguments sont $`5`$ et $`2`$.

Autrement dit, le paramètre $`a`$ a comme valeur $`5`$ et le paramètre $`b`$ a comme valeur $`2`$.

Il est important que le type de l'argument doit être le même que celui du paramètre.

##### Application 6

Vérifier la bonne réponse à l'application 4 en appelant la fonction dans la console Python plusieurs fois avec des arguments différents.

##### Application 7

Vérifier la bonne réponse à l'application 5 en appelant la fonction dans la console Python plusieurs fois avec des arguments différents.

### b) Résultat d'une fonction

Le résultat obtenu suite à l'appel d'une fonction représente une valeur.

Nous pouvons stocker la valeur obtenue dans une variable :

```python
>>> a = somme(5,2)
>>> a
7
```

Ou la réutiliser dans une opération :

```python
>>> 2 * somme(5,2)
14
```

Ou encore l'utiliser en tant qu'argument d'une autre fonction :

```python
>>> type(somme(5,2))
<class 'int'>
```

##### Application 8

Donner le résultat des instructions suivantes :

a) Instruction 1

```python
>>> type(produit(3,4))
```

b) Instruction 2

```python
>>> a = somme(5,2)
>>> b = produit(3,4)
>>> c = a + b
>>> c
```

c) Instruction 3

```python
>>> somme(5, somme(3,2))
```

## IV. Fonctions natives

Les fonctions natives sont des fonctions qui existent déjà. La fonction ``type()`` par exemple est une fonction native.

##### Application 9

Il est possible, avec une fonction native, de changer le type de nos valeurs.

- La fonction ``str()`` renvoie la valeur mise en parenthèses sous le type de chaîne de caractère.

- La fonction ``int()`` renvoie la valeur mise en parenthèses sous le type de nombre entier .

- La fonction ``float()`` renvoie la valeur mise en parenthèses sous le type de nombre flottant.

a) Dans la console Python et à l'aide de la fonction `str()`, convertir les valeurs `42`, `3.14`, `0.0` et `True` en chaîne de caractères.

b) Dans la console Python et à l'aide de la fonction `int()`, convertir les valeurs `3.14`, `True`, `False` et `"42"`.

c) Dans la console Python et à l'aide de la fonction `float()`, convertir les valeurs `42`, `3.14` et `"3000"`.

___________

[Feuille d'exercice](./Exercices/Exercices_fonctions_1.md)
____________

Leçon 6 : [Modules](./Modules.md)
