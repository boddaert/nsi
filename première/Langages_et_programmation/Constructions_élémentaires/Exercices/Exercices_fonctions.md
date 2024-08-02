# Exercices

## Exercice 1

Écrire la signature de la fonction ``contient()`` qui prend en paramètre une chaîne de caractère $mot$, un caractère $lettre$ et renvoie comme résultat $True$ si $lettre$ est présent dans $mot$, $False$ sinon.

## Exercice 2

Écrire une fonction `double(n : int)->int` qui prend en paramètre un entier $n$ et renvoie comme résultat $n \times 2$.

```python
>>> double(2)
4
```

## Exercice 3

a) Écrire une fonction `suivant(n : int)->int` qui prend en paramètre un entier $n$ et renvoie comme résultat $n+1$.

b) Que renvoie l'instruction suivante ?

```python
>>> suivant(suivant(2))
```

## Exercice 4

Écrire une fonction `est_egal_a(a : int, b : int)->bool` qui prend en paramètre deux entiers $a$ et $b$ et renvoie comme résultat $True$ si $a$ et $b$ sont égaux et $False$ sinon.

```python
>>> est_egal_a(5,7)
False
```

## Exercice 5

Écrire une fonction `est_superieur_a(a : int, b : int)->bool` qui prend en paramètre deux entiers $a$ et $b$ et renvoie comme résultat $True$ si $a > b$ et $False$ sinon.

```python
>>> est_superieur_a(10, 9)
True
```

## Exercice 6 (Difficile)

Rappel : L'énergie cinétique d'un objet de masse $m$ et de vitesse $v$ est : $`Ec=\frac{1}{2}mv^2`$.

Écrire une fonction ``energie_cinetique(m : float, v : float)->float`` qui prend en paramètre une masse $m$ et une vitesse $v$, deux nombres flottants et renvoie la valeur de l'énergie cinétique d'un objet.

Cette fonction devra utiliser les fonctions ``produit()`` et ``carre()`` vus dans le chapitre (cf : [Fonctions](./../Fonctions.md)).

```python
>>> energie_cinetique(6.2, 9.7)
291.679
```

_______________

[Sommaire](./../../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 