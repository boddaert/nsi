# Exercices

## Exercice 1

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

## Exercice 2

Écrire une fonction `suite(n : int)->int` qui prend en paramètre un entier $n$ et calcule $1+2+3+ ... +n$ en utilisant la boucle `while`.

```python
>>> suite(5)
15
```

## Exercice 3

Écrire une fonction `puissance_2(n : int)->int` qui prend en paramètre un entier $n$ et renvoie le résultat de $2^n$.

Cette fonction devra utiliser uniquement l'opérateur de multiplication `*` et la boucle `while`.

```python
>>> puissance_2(4)
16
```

## Exercice 4 (Difficile)

Rappel : Un entier est pair si le reste de la division entière par $2$ vaut $0$.

Écrire une fonction `nb_etape(n : int)->int` qui prend en paramètre un entier $n$.

Tant que cet entier n'est pas égal à $1$, nous le divisons par $2$ s'il est pair ou nous le multiplions par $3$ et nous ajoutons $1$ s'il est impair.

La fonction renvoie comme résultat le nombre d'étapes nécessaire pour arriver à $1$.

```python
>>> nb_etape(734)
46
```

_______________

[Sommaire](./../../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 