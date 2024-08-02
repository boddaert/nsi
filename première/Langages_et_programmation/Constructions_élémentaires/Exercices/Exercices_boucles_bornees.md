# Exercices 

## Exercice 1

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

b) Vérifier vos résultats en exécutant les programmes dans Thonny.

## Exercice 2

Écrire une fonction `suite(n : int)->int` qui prend en paramètre un entier $n$ et calcule $1+2+3+ ... +n$ en utilisant la boucle `for`.

```python
>>> suite(6)
21
```

## Exercice 3

Écrire une fonction `puissance_2(n : int)->int` qui prend en paramètre un entier $n$ et renvoie le résultat de $2^n$.

Cette fonction devra utiliser uniquement l'opérateur de multiplication `*` et la boucle `for`.

```python
>>> puissance_2(5)
32
```
_____________

[Sommaire](./../../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 