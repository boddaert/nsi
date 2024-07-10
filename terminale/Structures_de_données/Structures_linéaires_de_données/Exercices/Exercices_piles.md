# Exercices

## Exercice 1

Écrire une fonction récursive `empiler_n(n : int)->Pile` qui prend en paramètre un entier et renvoie un objet `Pile` contenant les entiers de $1$ à $n$.

```python
>>> empiler_n(5).depile()
5
```

## Exercice 2

Écrire une fonction `transvase(p1 : Pile, p2 : Pile)->None` qui prend en paramètres deux objets `Pile` et transvase tous les éléments de `p1` dans `p2`.

## Exercice 3 

Écrire une fonction `est_present(p : Pile, elt : int)->bool` qui prend en paramètres un objet `Pile` et un entier et renvoie $True$ si `elt` est présent dans `p`, $False$ sinon.

Cette fonction ne doit pas modifier la pile passée en argument.

```python
>>> p = Pile()
>>> p.empile(5)
>>> est_present(p, 5)
True
```

## Exercice 4

Écrire une fonction `sont_egales(p1 : Pile, p2 : Pile)->bool` qui prend en paramètres deux objets `Pile` et renvoie comme résultat $True$ si les deux piles sont égales, $False$ sinon.

## Exercice 5

Écrire une fonction `bien_parenthese(mot : str)->bool` qui prend en paramètre une chaîne de caractère et renvoie $True$ si `mot` est bien parenthésé, $False$ sinon.

```python
>>> bien_parenthese("(())")
True
>>> bien_parenthese(")()")
False
>>> bien_parenthese("())")
False
```
_______________

[Sommaire](./../../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 