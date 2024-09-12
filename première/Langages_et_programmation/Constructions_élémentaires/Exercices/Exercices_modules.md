# Exercices

## Exercice 1

Écrire une fonction `racine(n : int)->float` qui prend en paramètre un entier $n$ et renvoie comme résultat la racine carrée de $n$.

Cette fonction devra utiliser le module `math` qui aura été importé de manière précise.

```python
>>> racine(3)
1.732050808
```

## Exercice 2

*Rappel : Le calcul de l'hypoténuse du segment* $c$ *est :* $c = sqrt{(a^2 + b^2)}$

Écrire une fonction `hypotenuse(a : int, b : int)->float` qui prend en paramètre deux entiers et renvoie comme résultat la valeur de l'hypoténuse d'un triangle rectangle dont les deux autres côtés ont comme longueurs celles des paramètres.

Cette fonction doit utiliser la fonction `racine()` définie précédemment.

```python
>>> hypotenuse(5,3)
5.84
```

## Exercice 3

Écrire une fonction `des()->int` qui ne prend aucun paramètre et renvoie comme résultat un chiffre aléatoire parmi $1$, $2$, $3$, $4$, $5$ et $6$.

Cette fonction devra utiliser le module `random` qui aura été importé de manière globale.

```python
>>> des()
5
>>> des()
2
```
_______________

[Sommaire](./../../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 