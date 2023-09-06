# Remise à niveau

## I. Définitions, Langages de programmation, Thonny

Lire [Prise en main - Première](./../../première/Prise_en_main/Prise_en_main.md)

## II. Exercices de remise à niveau

### a) Exercice 1

a) Sans utiliser l'ordinateur, donner le type des valeurs suivantes :

- `8`
- `6.5`
- `"6.5"`
- `'6.5'`
- `False`
- `"True"`
- `""`
- `True`
- `true`
- `5 + 4`
- `"5 + 4"`
- `'"abcd"'`
- `5.5 + 0.3`
- `5.5 + 0.5`
- `5 + 3.14`
- `5 + 3.0`
- `5 / 2`

b) Vérifier, à l'aide de la fonction `type()` et dans la console vos précédentes réponses.

c) Expliquer le type obtenu pour chaque réponse.

### b) Exercice 2

a) Sans utiliser l'ordinateur, donner le résultat des expressions suivantes :

- `5 ** 2 - 3`
- `10 < 9`
- `10 <= 10`
- `5 / 2`
- `4 / 2`
- `False and False`
- `4 / 0`
- `4 // 2`
- `4 // 0`
- `4 % 2`
- `4 != 2`
- `5 % 2`
- `True or True`
- `7 + 7 % 2`
- `3 * 3 ** 2`
- `'4' // 2`

b) Vérifier vos résultats dans la console.

### c) Exercice 3

- $3$

```python
a = 5
b = 3
tmp = a
a = b
b = tmp
```

Expliquer ce que fait le programme précédent.

### d) Exercice 4

a) Ecrire une fonction ``max2( a : int, b : int)-> int`` qui prend en paramètres deux entiers $a$ et $3$ et renvoie l'entier le plus grand.



```python
>>> max2(5,13)
13
```

b) Ecrire une fonction ``max3( a : int, b : int, c : int )-> int`` qui prend en paramètres trois entiers $a$, $b$ et $c$ et renvoie l'entier le plus grand.

```python
>>> max3(5,7,15)
15
```

### e) Exercice 5

Ecrire une fonction `puissance_2(n : int)->int` qui prend en paramètre un entier $n$ et renvoie le résultat de $2^n$.

Cette fonction devra utiliser uniquement l'opérateur de multiplication et la boucle `for`.

```python
>>> puissance_2(5)
32
```

### f) Exercice 6

Ecrire une fonction `puissance_2(n : int)->int` qui prend en paramètre un entier $n$ et renvoie le résultat de $2^n$.

Cette fonction devra utiliser uniquement l'opérateur de multiplication et la boucle `while`.

```python
>>> puissance_2(4)
16
```

### g) Exercice 7

Ecrire une fonction `nombre_occurences(mot : str, lettre : str)->int` qui prend en paramètres une chaîne de caractère et un caractère et renvoie comme résultat le nombre de fois qu'apparaît `lettre` dans `mot`.

```python
>>> nombre_occurences('occurence', 'e')
2
```
______________

[Sommaire](./../../terminale/)