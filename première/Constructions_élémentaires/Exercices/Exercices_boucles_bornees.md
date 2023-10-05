# Exercices 

## Exercice 1

Pour chacun des programmes suivants, écrire la trace d'exécution.

a) Programme 1

```python
a = 0
for i in range(0,10) :
    a = a + 2
```

b) Programme 2

```python
a = 0
for i in range(0,10):
    a = a + i
```

c) Programme 3

```python
a = 0
b = 10
for i in range(-5,5):
    a = i**2
    b = b - a
```

## Exercice 2

Ecrire une fonction `puissance_2(n : int)->int` qui prend en paramètre un entier $n$ et renvoie le résultat de $2^n$.

Cette fonction devra utiliser uniquement l'opérateur de multiplication et la boucle `for`.

```python
>>> puissance_2(5)
32
```

## Exercice 3

Ecrire une fonction `suite(n : int)->int` qui prend en paramètre un entier $n$ et calcule $1+2+3+ ... +n$ en utilisant la boucle `for`.

```python
>>> suite(6)
21
```
_____________

[Sommaire](./../../README.md)