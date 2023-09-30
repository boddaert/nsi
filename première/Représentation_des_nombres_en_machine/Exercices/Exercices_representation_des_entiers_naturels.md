# Exercices

## Exercice 1

1) Trouver la représentation hexadécimale de $111010000_2$.

2) Trouver la représentation binaire de $8967_{10}$.

3) Trouver la représentation décimale de $100001101_2$.

4) Trouver la représentation binaire de $FF78_{16}$.

5) Trouver la représentation décimale de $BF4E_{16}$.

6) Trouver la représentation hexadécimale de $9017_{10}$.

7) Trouver la représentation binaire de $56CF167_{16}$.

9) Trouver la représentation décimale de $901A_{16}$.

10) Trouver la représentation hexadécimale de $19877_{10}$.

## Exercice 2

La fonction `bin(n : int)->str` prend en paramètre un entier et renvoie cet entier sous forme de chaîne de caractère dans sa représentation binaire :

```python
>>> bin(10)
'0b1010'
```

`'Ob'` indiquant qu'il s'agit bien d'une représentation binaire.

a) A l'aide de la fonction `bin()`, vérifier votre résultat à la question 2).

## Exercice 3 

La fonction `hex(n : int)->str` prend en paramètre un entier et renvoie cet entier sous forme de chaîne de caractère dans sa représentation hexadécimale :

```python
>>> hex(10)
'0xa'
```

`'Ox'` indiquant qu'il s'agit bien d'une représentation hexadécimale.

b) A l'aide de la fonction `hex()`, vérifier vos résultats aux questions 6) et 10).

## Exercice 4

La fonction `int(seq : str, base : int)->int` prend en paramètre une séquence sous forme de chaîne de caractère et une base et renvoie l'entier dans sa représentation décimale :

```python
>>> int('0b1010' , 2)
10
>>> int('0xa', 16)
10
```

c) A l'aide des fonctions `bin()`, `hex()` et `int()`, vérifier vos résultats aux questions 1), 3), 4), 5), 7), 8) et 9).

______________

[Sommaire](./../../README.md)