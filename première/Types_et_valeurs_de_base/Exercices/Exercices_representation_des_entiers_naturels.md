# Exercices

## Exercice 1

1. Trouver la représentation binaire de $89_{10}$.

2. Trouver la représentation binaire de $55_{10}$.

3. Trouver la représentation binaire de $100_{10}$.

## Exercice 2

1. Trouver la représentation décimale de $100001101_2$.

2. Trouver la représentation décimale de $11111_2$.

3. Trouver la représentation décimale de $10101010101_2$.

## Exercice 3

1. Trouver la représentation hexadécimale de $111010000_2$.

2. Trouver la représentation hexadécimale de $111111111_2$.

3. Trouver la représentation binaire de $FF78_{16}$.

4. Trouver la représentation binaire de $56CF167_{16}$.

## Exercice 4

1. Trouver la représentation décimale de $BF4_{16}$.

2. Trouver la représentation hexadécimale de $91_{10}$.

3. Trouver la représentation décimale de $91A_{16}$.

## Exercice 5

La fonction `bin(n : int)->str` prend en paramètre un entier en base dix et renvoie cet entier sous forme de chaîne de caractère dans sa représentation binaire :

```python
>>> bin(10)
'0b1010'
```

`'Ob'` indiquant qu'il s'agit bien d'une représentation binaire.

a) À l'aide de la fonction `bin()`, vérifier vos résultats à l'exercice $1$.

## Exercice 6 (Difficile)

La fonction `hex(n : int)->str` prend en paramètre un entier en base dix et renvoie cet entier sous forme de chaîne de caractère dans sa représentation hexadécimale :

```python
>>> hex(10)
'0xa'
```

`'Ox'` indiquant qu'il s'agit bien d'une représentation hexadécimale.

La fonction `int(seq : str, base : int)->int` prend en paramètre une séquence sous forme de chaîne de caractère et la base dans laquelle est représentée la séquence et renvoie l'entier dans sa représentation décimale :

```python
>>> int('0b1010' , 2)
10
>>> int('0xa', 16)
10
```

a) À l'aide des fonctions `bin()`, `hex()` et `int()`, vérifier vos résultats aux exercices $2$, $3$ et $4$.

______________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 