# Exercices

## Exercice 1

Ecrire une fonction `double(n : int) -> int` qui prend en paramètre un entier $`n`$ et renvoie comme résultat $`n * 2`$.

```python
>>> double(2)
4
```

## Exercice 2

a) Ecrire une fonction `suivant(n : int) -> int` qui prend en paramètre un entier $`n`$ et renvoie comme résultat $`n+1`$.

b) Que renvoie l'instruction suivante ?

```python
>>> suivant(suivant(2))
```

## Exercice 3

Ecrire une fonction `est_egal_a(a : int, b : int) -> bool` qui prend en paramètre deux entiers $`a`$ et $`b`$ et renvoie comme résultat `True` si $`a`$ et $`b`$ sont égaux et $False$ sinon.

```python
>>> est_egal(5,7)
False
```

## Exercice 4

L'énergie cinétique d'un objet de masse $m$ et de vitesse $v$ est : $`Ec=\frac{1}{2}mv^2`$.

Ecrire une fonction ``energie_cinetique(m : float, v : float) -> float`` qui prend en paramètre une masse $m$ et une vitesse $v$, deux nombres flottants et renvoie la valeur de l'énergie cinétique d'un objet.

Cette fonction devra utiliser les fonctions ``produit()`` et ``carre()`` vus dans le chapitre (cf : [Fonctions](./../Fonctions.md)).

```python
>>> energie_cinetique(6.2, 9.7)
291.679
```

_______________

[Sommaire](./../../README.md)