# Exercices 

## Exercice 1

Ecrire une fonction récursive `affiche_liste(l : Liste)->None` qui prend en paramètre un objet `Liste` et affiche dans la console les éléments de `l`.

```python
>>> l = Liste(4,Liste(5,Liste(6,Liste())))
>>> affiche_liste(l)
4
5
6
```

## Exercice 2 

a) Ecrire une fonction récursive `liste_en_str(l : Liste)->str` qui prend en paramètre un objet `Liste` et renvoie les éléments de `l` en chaîne de caractère.

```python
>>> l = Liste(4,Liste(5,Liste(6,Liste())))
>>> liste_en_str(l)
'456'
```

b) Dessiner la pile d'appel de l'instruction ci-dessus.

## Exercice 3

a) Ecrire une fonction récursive `longueur(l : Liste)->int` qui prend en paramètre un objet `Liste` et renvoie comme résultat son nombre d'élément.

```python
>>> l = Liste(4,Liste(5,Liste(6,Liste())))
>>> longueur(l)
3
```

b) Dessiner la pile d'appel de l'instruction ci-dessus.

## Exercice 4

Ecrire une fonction récursive `est_present(l : Liste, elt : int)->bool` qui prend en paramètres un objet `Liste` et un entier et renvoie $True$ si `elt` est présent dans `l`, $False$ sinon.

```python
>>> l = Liste(4,Liste(5,Liste(6,Liste())))
>>> est_present(l, 5)
True
```

## Exercice 5

Ecrire une fonction récursive `occurence(l : Liste, elt : int)->int` qui prend en paramètres un objet `Liste` et un entier et renvoie le nombre de fois qu'apparaît `elt` dans `l`.

```python
>>> l = Liste(4,Liste(5,Liste(5,Liste())))
>>> occurence(l, 5)
2
```

## Exercice 6

a) Ecrire une fonction récursive `ieme(l : Liste, i : int)->int` qui prend en paramètres un objet `Liste` et un entier et renvoie comme résultat l'élément d'indice `i` dans `l`.

La fonction doit traiter le cas où l'élément d'indice `i` n'existe pas. C'est-à-dire, lorsque `i` est supérieur à la longueur de `l`.

```python
>>> l = Liste(4,Liste(5,Liste(6,Liste())))
>>> ieme(l, 1)
5
```

b) Dessiner la pile d'appel de l'instruction ci-dessus.

## Exercice 7

Ecrire une fonction récursive `en_liste(li : list)->Liste` qui prend en paramètre une liste d'entiers et renvoie comme résultat la liste récursive correspondante.

```python
>>> li = [4, 5, 6]
>>> en_liste(li)
<__main__.Liste object at 0x7f53bffa0400>
```

## Exercice 8

Ecrire une fonction récursive `ajoute_en_fin(l : Liste, elt : int)->Liste` qui prend en paramètres un objet `Liste`, un entier et renvoie comme résultat cette même ce même objet `Liste` contenant en plus l'élément `elt` à la fin.

```python
>>> l = Liste(4,Liste(5,Liste(6,Liste())))
>>> liste_en_str(ajoute_en_fin(l, 7))
'4567'
```

## Exercice 9

Ecrire une fonction récursive `concat(l1 : Liste, l2 : Liste)->Liste` qui prend en paramètres deux objets `Liste` et renvoie comme résultat un objet `Liste` dans lequel se trouve tous les éléments de `l1` et de `l2`.