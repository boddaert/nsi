# Exercices

## Exercice 1

a) Ecrire une fonction `divise(a : int, b : int) -> float` qui prend en paramètre deux entiers $a$ et $b$ et renvoie le résultat de la division de $a$ par $b$.

Cette fonction devra effectuer la division uniquement si $b$ est différent de $0$.

```python
>>> divise(6,3)
2.0
```

b) Dessiner le schéma de branchement de la fonction `divise()`.

## Exercice 2

Considérons le programme suivant :

```{.python .numberLines}
if n > 2 :
    n = n + 10
    res = (n // 2) + n
else :
    res = n * n
res = res - n
```

a) Remplir la trace d'exécution du programme précédent :

- Une première fois avec $n$ est égal à $1$.

- Une seconde fois avec $n$ est égal à $3$.

b) Dessiner son schéma de branchement.

## Exercice 3

Ecrire une fonction ``test_pythagore( a : int, b : int, c : int )-> bool`` qui prend en paramètre 3 entiers $a$, $b$ et $c$ et renvoie $True$ si $a^2 + b^2 = c^2$, et $False$ sinon.

Cette fonction doit comporter une instruction conditionnelle.

## Exercice 4

a) Ecrire une fonction ``max2( a : int, b : int)-> int`` qui prend en paramètres deux entiers $a$ et $b$ et renvoie l'entier le plus grand.

```python
>>> max2(5,13)
13
```

b) Ecrire une fonction ``max3( a : int, b : int, c : int )-> int`` qui prend en paramètres trois entiers $a$, $b$ et $c$ et renvoie l'entier le plus grand.

```python
>>> max3(5,7,15)
15
```

## Exercice 5

En utilisant la fonction `randint()` du module `random`, écrire une fonction `max_alea(n : int)->bool` qui prend en paramètre un entier $n$ et renvoie $True$ si $n$ est plus grand que l'entier aléatoire créé compris entre $1$ et $10$.

### Exercice 6

Ecrire une fonction ``ordre_croissant( a : int, b : int, c : int )-> str`` qui prend en paramètre trois entiers $a$, $b$ et $c$ et renvoie comme résultat une chaîne de caractère contenant $a$, $b$ et $c$ dans l'ordre croissant.

```python
>>> ordre_croissant(5,13,4)
'4,5,13'
```

## Exercice 7

a) Ecrire une fonction ``test_triangle( a : int, b : int, c : int )-> str`` qui prend en paramètres trois entiers représentant les longueurs d'un triangle et renvoie comme résultat une chaîne de caractères.

La fonction doit renvoyer `isocele` s'il s'agit d'un triangle iscoèle, `equilateral` s'il s'agit d'un triangle équilatéral ou `ce nest pas un triangle` s'il ne s'agit pas d'un triangle.

*Rappel : Dans un triangle, aucune longueur n'est strictement supérieure à la somme des deux autres.*

*Rappel : Un triangle équilatéral possède trois longueurs longueurs égales et un triangle isocèle en possède deux.*

b) Modifier la fonction ``test_triangle()`` en ajoutant le fait qu'il peut s'agir d'un triangle rectangle, on pourra utiliser la fonction ``test_pythagore()`` pour cela.


_______________

[Sommaire](./../../README.md)