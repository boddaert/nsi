# Exercices

## Exercice 1

Traduire en Français les programmes suivants :

a) Programme 1

```python
a = 5
b = 0
while a > b :
    a = a - 1
    b = b + 1
```

b) Programme 2

```python
a = False
b = 1
while not a == True :
    a = True
    b = b + 1
```

c) Programme 3

```python
a = 0
b = 0
while a < 10 or b > -5 :
    a = a + 1
    b = b - 1
```

d) Programme 4

```python
a = 0
b = 0
while a < 10 and b > -5 :
    a = a + 1
    b = b - 1
```

e) Programme 5

```python
a = 1
b = 5
while a < 10 or b < 10 :
    a = a * 2
    b = b + 1
```
## Exercice 2

Pour chacun des programmes de l'exercice 1, dessiner le schéma de branchement.

## Exercice 3

Pour chacun des programmes de l'exercice 1, écrire la trace d'exécution.

## Exercice 4

Ecrire une fonction `puissance_2(n : int)->int` qui prend en paramètre un entier $n$ et renvoie le résultat de $2^n$.

Cette fonction devra utiliser uniquement l'opérateur de multiplication et la boucle `while`.

## Exercice 5

Ecrire une fonction `suite(n : int)->int` qui prend en paramètre un entier $n$ et calcule $1+2+3+ ... +n$ en utilisant la boucle `while`.

## Exercice 6

Ecrire une fonction `nb_etape(n : int)->int` qui prend en paramètre un entier $n$.

Tant que cet entier n'est pas égal à $1$, nous le divisons par $2$ s'il est pair ou nous le multiplions par $3$ et nous ajoutons $1$ s'il est impair.

La fonction renvoie comme résultat le nombre d'étapes nécessaire pour arriver à $1$.

Un entier est pair si le reste de la division entière par $2$ vaut $0$.