# Exercices 

## Exercice 1

Traduire en Français les programmes suivants :

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

Pour chacun des programmes de l'exercice 1, écrire la trace d'exécution.

## Exercice 4

Ecrire une fonction `puissance_2(n : int)->int` qui prend en paramètre un entier $n$ et renvoie le résultat de $2^n$.

Cette fonction devra utiliser uniquement l'opérateur de multiplication et la boucle `for`.

## Exercice 5

Ecrire une fonction `suite(n : int)->int` qui prend en paramètre un entier $n$ et calcule $1+2+3+ ... +n$ en utilisant la boucle `for`.