# Exercices

## Exercice 1

Écrire une fonction `enfiler_n(n : int)->File` qui prend en paramètre un entier et renvoie un objet `File` contenant les entiers de $1$ à $n$.

```python
>>> enfiler_n(5).defile()
1
```

## Exercice 2

Écrire une fonction `est_present(f : File, elt : int)->bool` qui prend en paramètres un objet `File` et un entier et renvoie $True$ si `elt` est présent dans `f`, $False$ sinon.

Cette fonction ne doit pas modifier la file passée en argument.

```python
>>> f = File()
>>> f.enfile(5)
>>> est_present(f, 5)
True
```

## Exercice 3

Écrire une fonction `sont_egales(f1 : File, f2 : File)->bool` qui prend en paramètres deux objets `File` et renvoie comme résultat $True$ si les deux files sont égales, $False$ sinon.

## Exercice 4

Écrire une fonction `max(f : File)->int` qui prend en paramètre un objet `File` et renvoie comme résultat l'élément le plus grand de `f`.

Cette fonction ne doit pas modifier la file passée en argument.

## Exercice 5 (Difficile)

Réécrire la classe `File` mais cette fois en utilisant deux piles : l'une pour défiler et l'autre pour enfiler.

_________________

[Sommaire](./../../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 