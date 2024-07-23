# Exercices 

## Exercice 1

Écrire une fonction récursive `affiche_liste(l : ListeR)->None` qui prend en paramètre un objet `ListeR` et affiche dans la console les éléments de `l`.

```python
>>> l = ListeR(4,ListeR(5,ListeR(6,ListeR())))
>>> affiche_liste(l)
4
5
6
```

## Exercice 2 

a) Écrire une fonction récursive `liste_en_str(l : ListeR)->str` qui prend en paramètre un objet `ListeR` et renvoie les éléments de `l` en chaîne de caractère.

```python
>>> l = ListeR(4,ListeR(5,ListeR(6,ListeR())))
>>> liste_en_str(l)
'456'
```

b) Dessiner la pile d'appel de l'instruction ci-dessus.

## Exercice 3

a) Écrire une fonction récursive `longueur(l : ListeR)->int` qui prend en paramètre un objet `ListeR` et renvoie comme résultat son nombre d'élément.

```python
>>> l = ListeR(4,ListeR(5,ListeR(6,ListeR())))
>>> longueur(l)
3
```

b) Dessiner la pile d'appel de l'instruction ci-dessus.

## Exercice 4

Écrire une fonction récursive `est_present(l : ListeR, elt : int)->bool` qui prend en paramètres un objet `ListeR` et un entier et renvoie $True$ si `elt` est présent dans `l`, $False$ sinon.

```python
>>> l = ListeR(4,ListeR(5,ListeR(6,ListeR())))
>>> est_present(l, 5)
True
```

## Exercice 5

Écrire une fonction récursive `occurence(l : ListeR, elt : int)->int` qui prend en paramètres un objet `ListeR` et un entier et renvoie le nombre de fois qu'apparaît `elt` dans `l`.

```python
>>> l = ListeR(4,ListeR(5,ListeR(5,ListeR())))
>>> occurence(l, 5)
2
```

## Exercice 6

Écrire une fonction récursive `ieme(l : ListeR, i : int)->int` qui prend en paramètres un objet `ListeR` et un entier et renvoie comme résultat l'élément d'indice `i` dans `l`.

La fonction doit traiter le cas où l'élément d'indice `i` n'existe pas. C'est-à-dire, lorsque `i` est supérieur à la longueur de `l`.

```python
>>> l = ListeR(4,ListeR(5,ListeR(6,ListeR())))
>>> ieme(l, 1)
5
```

## Exercice 7

Écrire une fonction récursive `en_liste(li : list)->ListeR` qui prend en paramètre une liste d'entiers et renvoie comme résultat la liste récursive correspondante.

```python
>>> li = [4, 5, 6]
>>> en_liste(li)
<__main__.ListeR object at 0x7f53bffa0400>
```

## Exercice 8 (Difficile)

Écrire une fonction récursive `ajoute_en_fin(l : ListeR, elt : int)->ListeR` qui prend en paramètre un objet `ListeR`, un entier et renvoie comme résultat ce même objet `ListeR` contenant en plus l'élément `elt` à la fin.

```python
>>> l = ListeR(4,ListeR(5,ListeR(6,ListeR())))
>>> liste_en_str(ajoute_en_fin(l, 7))
'4567'
```

## Exercice 9 (Difficile)

Écrire une fonction récursive `concat(l1 : ListeR, l2 : ListeR)->ListeR` qui prend en paramètre deux objets `ListeR` et renvoie comme résultat un objet `ListeR` dans lequel se trouve tous les éléments de `l1` et de `l2`.

## Exercice 10 (Difficile)

Écrire une fonction récursive `ajoute(l : ListeR, elt : int, i : int)->ListeR` qui prend en paramètre un objet `ListeR`, deux entiers et renvoie comme résultat `l` dont l'élément `elt` a été ajouté à l'indice `i`.

## Exercice 11 (Difficile)

Écrire une fonction récursive `supprime(l : ListeR, i : int)->ListeR` qui prend en paramètre un objet `ListeR` et un entier et renvoie `l` dont l'élément d'indice `i` a été supprimé.

_______________

[Sommaire](./../../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 