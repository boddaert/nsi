# Remise à niveau

## Exercice 1

a) Sans utiliser l'ordinateur, proposer le type des valeurs suivantes :

1. `8`
2. `6.5`
3. `"6.5"`
4. `'6.5'`
5. `False`
6. `"True"`
7. `""`
8. `True`
9. `true`
10. `5 + 4`
11. `"5 + 4"`
12. `'"abcd"'`
13. `5.5 + 0.3`
14. `5.5 + 0.5`
15. `5 + 3.14`
16. `5 + 3.0`
17. `5 / 2`

b) À l'aide de la fonction `type()`, vérifier vos réponses en utilisant la console Python.

## Exercice 2

Expliquer l'erreur de l'instruction suivante :

```python
>>> "3" + 2
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'str' and 'int'
```

## Exercice 3

Sans utiliser l'ordinateur, indiquer la valeur affectée à la variable `mystere` à l'issue de l'exécution de chacun des programmes suivants :

1. Programme 1

```python
ma_variable = 56.01
mystere = True
```

2. Programme 2

```python
ma_variable = "hello world"
mystere = ma_variable
```

3. Programme 3

```python
ma_variable = 3
mystere = ma_variable * ma_variable
```

4. Programme 4

```python
mystere = 10
mystere = mystere + 1
```

5. Programme 5

```python
ma_variable = 20
mystere = ma_variable + 20
ma_variable = 30
mystere = mystere + ma_variable
```

## Exercice 4

```python
a = 5
b = 3
tmp = a
a = b
b = tmp
```

a) Sans utiliser l'ordinateur, donner les valeurs contenues dans les variables `a` et `b` à l'issue de l'exécution du programme précédent.

b) Vérifier votre résultat en utilisant l'outil de déboguage de Thonny et en affichant l'état des variables.

> [!NOTE]
> Pour afficher l'état des variables, cliquer sur l'onglet **Affichage** puis cocher **Variables**.

c) Finalement, expliquer ce que fait ce programme.

## Exercice 5

Sans utiliser l'ordinateur et pour chacun des programmes suivants, indiquer les valeurs contenues dans les variables `a` et `b` à l'issue de leur exécution :

1. Programme 1

```python
a = 3
a = 4
a = a + 2
b = a - 2
```

2. Programme 2

```python
a = 2
b = a * a
b = a * b
b = b * b
```

3. Programme 3

```python
a = 1
b = 5
b = b + a
a = a + a
b = b - a
```

4. Programme 4

```python
a = 3
b = 4
a = b
b = a
```

## Exercice 6

a) Sans utiliser l'ordinateur, proposer un résultat sur chacune des opérations suivante :

1. `5 ** 2 - 3`

2. `10 < 9`

3. `10 <= 10`

4. `5 / 2`

5. `4 / 2`

6. `False and False`

7. `4 // 2`

8. `4 % 2`

9. `4 != 2`

10. `5 % 2`

11. `True or True`

12. `7 + 7 % 2`

13. `3 * 3 ** 2`

14. `'4' // 2`

b) Vérifier vos réponses en utilisant la console Python.

## Exercice 7

Rappel : L'énergie cinétique d'un objet de masse $m$ et de vitesse $v$ est : $`Ec=\frac{1}{2}mv^2`$.

Écrire une fonction ``energie_cinetique(m : float, v : float)->float`` qui prend en paramètre une masse $m$ et une vitesse $v$, deux nombres flottants et renvoie la valeur de l'énergie cinétique d'un objet.

Cette fonction devra utiliser les fonctions ``produit()`` et ``carre()`` vus dans le chapitre (cf : [Fonctions](./../Fonctions.md)).

```python
>>> energie_cinetique(6.2, 9.7)
291.679
```

## Exercice 8

Ecrire une fonction ``max2( a : int, b : int)-> int`` qui prend en paramètres deux entiers $a$ et $b$ et renvoie l'entier le plus grand.

```python
>>> max2(5,13)
13
```

## Exercice 9

Écrire une fonction ``max3(a : int, b : int, c : int)->int`` qui prend en paramètres trois entiers $a$, $b$ et $c$ et renvoie l'entier le plus grand.

```python
>>> max3(5,7,15)
15
```

## Exercice 10

a) Sans utiliser l'ordinateur, donner la valeur de `a` et `b` à l'issue de l'exécution de chacun des programmes suivants.

1. Programme 1

```python
a = 5
b = 0
while a > b :
    a = a - 1
    b = b + 1
```

2. Programme 2

```python
a = False
b = 1
while not a == True :
    a = True
    b = b + 1
```

3. Programme 3

```python
a = 1
b = 5
while a < 10 or b < 10 :
    a = a * 2
    b = b + 1
```

b) Vérifier vos résultats en exécutant les programmes dans Thonny.

## Exercice 11

Ecrire une fonction `puissance_2(n : int)->int` qui prend en paramètre un entier $n$ et renvoie le résultat de $2^n$.

Cette fonction devra utiliser uniquement l'opérateur de multiplication et la boucle `while`.

```python
>>> puissance_2(5)
32
```

## Exercice 12

a) Sans utiliser l'ordinateur, donner la valeur de `a` et `b` à l'issue de l'exécution de chacun des programmes suivants.

1. Programme 1

```python
a = 0
for i in range(0,10) :
    a = a + 2
```

2. Programme 2

```python
a = 0
for i in range(0,10):
    a = a + i
```

3. Programme 3

```python
a = 0
b = 10
for i in range(-5,5):
    a = i**2
    b = b - a
```

## Exercice 13

Ecrire une fonction `puissance_2(n : int)->int` qui prend en paramètre un entier $n$ et renvoie le résultat de $2^n$.

Cette fonction devra utiliser uniquement l'opérateur de multiplication et la boucle `for`.

```python
>>> puissance_2(5)
32
```

## Exercice 14

Ecrire une fonction `nombre_chiffre(n : int)->int` qui prend en paramètre un entier et renvoie le nombre de chiffres de cet entier.

```python
>>> nombre_chiffre(34567)
5
```

## Exercice 15

Écrire la fonction `contient(mot : str, lettre : str)-> bool` qui prend en paramètres une chaîne de caractère et un caractère et renvoie $True$ si `lettre` est présent dans `mot`.

Cette fonction ne devra pas utiliser l'instruction `in`.

Écrire deux versions de cette fonction, la première en utilisant la boucle `for` et la seconde en utilisant la boucle `while`.

```python
>>> contient('bonjour', 't')
False
>>> contient('bonjour', 'b')
True
```

## Exercice 16

Écrire une fonction `nombre_occurences(mot : str, lettre : str)->int` qui prend en paramètres une chaîne de caractère et un caractère et renvoie comme résultat le nombre de fois qu'apparaît `lettre` dans `mot`.

```python
>>> nombre_occurences('occurence', 'e')
2
```

## Exercice 17

Écrire une fonction `maximum_liste(l : list)->int` qui prend en paramètre une liste `l` et renvoie comme résultat l'entier maximum de `l` :

```python
>>> maximum_liste([4,7,3,9,2])
9
```

## Exercice 18

Écrire une fonction `est_triee(l : list)->bool` qui prend en paramètre une liste d'entiers et renvoie $True$ si $l$ est triée par ordre croissant, $False$ sinon.

## Exercice 19

Écrire une fonction `table_de_multiplication(n : int)->list` qui prend en paramètre un entier et renvoie comme résultat la table de multiplication de $n$ sous forme de liste.

```python
>>> table_de_multiplication(2)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

## Exercice 20

Écrire une fonction `impairs(n : int)->list` qui prend en paramètre un entier et renvoie comme résultat une liste comprenant tous les entiers impairs de $0$ jusqu'à $n$.

```python
>>> impairs(15)
[1, 3, 5, 7, 9, 11, 13, 15]
```

## Exercice 21

Considérons la liste suivante :

```python
li = [["a", "b", "c", "d"],
      [1, 2, 3, 4],
      ["I", "II", "III", "IV"]]
```

1. Que renvoie l'instruction : `>>> li[0]` ?

2. Que renvoie l'instruction : `>>> li[1]` ?

3. Que renvoie l'instruction : `>>> li[0][1]` ?

4. Que renvoie l'instruction : `>>> li[1][0]` ?

## Exercice 22

Écrire une fonction `somme_liste(l : list)->int` qui prend en paramètre une liste de listes d'entiers et renvoie la somme des éléments de $l$.

```python
>>> somme_liste([[1, 2], [3, 4], [5, 6]])
21
```

## Exercice 23

Écrire une fonction `affiche_labyrinthe(labyrinthe : list)->None` qui prend en paramètre un labyrinthe sous forme de liste de listes et l'affiche proprement dans la console à l'aide des caractères '█' et ' '.

```python
>>> labyrinthe = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 1, 1, 0, 1, 1, 1, 0, 1],
              [1, 0, 0, 0, 1, 0, 0, 0, 1],
              [1, 0, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 1, 1]]
>>> affiche_labyrinthe(labyrinthe)
██████████████████
                ██
██████  ██████  ██
██      ██      ██
██  ██████████████
██                
██████████████████
```

## Exercice 24

Écrire une fonction `occurences_par_lettre(mot : str)->dict` qui prend en paramètre une chaîne de caractère et renvoie un dictionnaire dont les clés sont des caractères de la chaîne et les valeurs le nombre de fois qu'apparaissent ces caractères :

```python
>>> occurences_par_lettre('bienvenue')
{'b' : 1, 'i' : 1, 'e' : 3, 'n' : 2, 'v' : 1, 'u' : 1}
```

## Exercice 25

Écrire une fonction ``inversion(dico : dict)->dict`` qui prend en paramètre un dictionnaire et renvoie un dictionnaire dont les clés sont devenus les valeurs et les valeurs, les clés.

```python
>>> inversion({'a' : 1, 'b' : 2, 'c' : 3})
{1 : 'a', 2 : 'b', 3 : 'c'}
```
_______________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 