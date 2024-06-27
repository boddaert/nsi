# Fonctions

## I. Définitions

> [!IMPORTANT]
> Une *fonction* est une séquence d'instruction réutilisable. Elle associe une séquence d'instruction à un nom.

Nous la distinguons des variables parce que le nom est suivi de parenthèses.

Elle réalise une tâche précise et peut dépendre de paramètres.

> [!TIP]
>Par exemple, la fonction `type()` que nous avons vu au chapitre sur les types (cf : [Types](./Types.md)) permet d'obtenir le type de la valeur passée en paramètre.
>
>```python
>>>> type(5)
><class 'int'>
>```

### a) Signature

Pour être un peu plus précis sur la définition d'une fonction, nous écrivons sa **signature**.

> [!IMPORTANT]
>La *signature d'une fonction* est composée du nom de la fonction, du nom et du type des paramètres et du type de la valeur du résultat renvoyé par la fonction.

> [!TIP]
> Par exemple : 
>
> Soit `somme()` la fonction permettant de faire la somme de deux entiers.
>
>La signature de la fonction `somme()` s'écrirait : `somme(a : int, b : int) -> int`.
>
>- Le nom est : `somme()`.
>
>- Les paramètres sont `a` et `b` et sont tous les deux de type `int`.
>
>- La valeur renvoyée par cette fonction est de type `int`.

### b) Paramètres

> [!IMPORTANT]
>Un *paramètre* est une variable qui pourra être utilisée à l'intérieur de la fonction.

> [!WARNING]
> Une fonction peut avoir zéro ou plusieurs paramètres.

#### <ins>Application 1</ins>

Donner, pour chaque signature suivante, le nom de la fonction, son ou ses paramètres ainsi que leur type et le type de la valeur de résultat :

1. ``produit(a : int, b : int) -> int``

2. ``est_superieur_a(a : int, b : int) -> bool``

3. ``pythagore( a : float, b : float, c : float) -> float``

4. ``nombre_caracteres(mot : str ) -> int``

#### <ins>Application 2</ins>

Écrire la signature de la fonction ``maximum()``qui prend en paramètres deux entiers $a$ et $b$ et renvoie comme résultat l'entier maximum parmi les deux.

## II. Écriture de fonction

Une fonction en Python est composé de sa **signature** et d'un **corps**.

### a) Définition d'une fonction en Python

Nous écrivons les fonctions en Python en utilisant le mot-clé `def` suivi de la signature de la fonction suivi d'un `:`.

> [!TIP]
> Par exemple :
> ```python
> def somme(a : int, b : int) -> int :
> ```

### b) Corps d'une fonction

> [!IMPORTANT]
> Le *corps* d'une fonction est la séquence d'instruction située à l'intérieur.

> [!WARNING]
> Le corps d'une fonction est **indenté**, c'est-à-dire qu'il est décalé de trois espaces vers la droite.

> [!TIP]
> Par exemple :
>```python
>def somme(a : int, b : int) -> int :
>    resultat = a + b
>```

### c) Résultat d'une fonction

Le mot-clé `return` permet de **renvoyer** un résultat.

> [!TIP]
> Par exemple :
>```python
>def somme(a : int, b : int) -> int :
>    resultat = a + b
>    return resultat
>```

> [!NOTE]
> Il est toujours préférable que l'instruction `return` soit toujours la dernière afin d'éviter les erreurs.

### e) Procédures

> [!IMPORTANT]
> Une *procédure* est une fonction ne renvoyant pas de résultat et donc ne contient pas d'instruction `return`.

#### <ins>Application 3</ins>

Écrire, en Python, la fonction ``produit(a : int, b : int) -> int`` qui prend en paramètres deux entiers $a$ et $b$ et renvoie comme résultat $a \times b$.

#### <ins>Application 4</ins>

Écrire, en Python, la fonction `carre(n : int) -> int` qui prend en paramètres un entier $n$ et renvoie comme résultat $n²$.

## III. Appels de fonction

### a) Arguments

> [!IMPORTANT]
> Un *appel de fonction* revient à utiliser le code de cette fonction avec des arguments.

> [!IMPORTANT]
> Un *argument* est la valeur que prend un paramètre lors d'un appel de fonction.

> [!WARNING]
> Paramètres et arguments ne définissent pas la même chose.

Pour appeler une fonction, il suffit d'écrire le nom de la fonction avec les arguments souhaités entre parenthèses.

> [!TIP]
>```python
>>>> somme(5,2)
>7
>```
>
>Les arguments sont `5` et `2`.
>
>Autrement dit, le paramètre `a` a comme valeur $5$ et le paramètre `b` a comme valeur $2$.

> [!WARNING]
> Le type de l'argument doit être impérativement le même que celui du paramètre.

#### <ins>Application 5</ins>

a) Vérifier la bonne réponse à l'application $3$ en appelant la fonction dans la console Python plusieurs fois avec des arguments différents.

b) Vérifier la bonne réponse à l'application $4$ en appelant la fonction dans la console Python plusieurs fois avec des arguments différents.

### b) Réutilisation d'un résultat d'une fonction

Le résultat obtenu suite à l'appel d'une fonction représente une valeur.

Nous pouvons stocker la valeur obtenue dans une variable.

> [!TIP]
> Par exemple :
>```python
>>>> a = somme(5,2)
>>>> a
>7
>```

Ou la réutiliser dans une opération.

> [!TIP]
> Par exemple :
>```python
>>>> 2 * somme(5,2)
>14
>```

Ou encore l'utiliser en tant qu'argument d'une autre fonction.

> [!TIP]
> Par exemple :
>```python
>>>> type(somme(5,2))
><class 'int'>
>```

#### <ins>Application 6</ins>

a) Sans utiliser l'ordinateur, proposer un résultat sur chacune des séquence suivante :

1. Instruction 1

```python
>>> type(produit(3,4))
```

2. Instruction 2

```python
>>> a = somme(5,2)
>>> b = produit(3,4)
>>> c = a + b
>>> c
```

3. Instruction 3

```python
>>> somme(5, somme(3,2))
```

b) Vérifier vos réponses en utilisant la console Python.

## IV. Fonctions natives de Python

> [!IMPORTANT]
> Les *fonctions natives* sont des fonctions qui existent déjà.

> [!TIP]
> La fonction ``type()`` par exemple est une fonction native.

#### <ins>Application 7</ins>

Il est possible, avec une fonction native, de changer le type de nos valeurs.

- La fonction ``str()`` renvoie la valeur mise en parenthèses sous le type de chaîne de caractère.

- La fonction ``int()`` renvoie la valeur mise en parenthèses sous le type de nombre entier .

- La fonction ``float()`` renvoie la valeur mise en parenthèses sous le type de nombre flottant.

a) Dans la console Python et à l'aide de la fonction `str()`, convertir les valeurs `42`, `3.14`, `0.0` et `True` en chaîne de caractères.

b) Dans la console Python et à l'aide de la fonction `int()`, convertir les valeurs `3.14`, `True`, `False` et `"42"`.

c) Dans la console Python et à l'aide de la fonction `float()`, convertir les valeurs `42`, `3.14` et `"3000"`.

___________

[Exercices](./Exercices/Exercices_fonctions.md)
____________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 