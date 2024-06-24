# Exercices

## Exercice 1

Ecrire une fonction `enfiler_n(n : int)->File` qui prend en paramètre un entier et renvoie un objet `File` contenant les entiers de $1$ à $n$.

```python
>>> enfiler_n(5).defile()
1
```

## Exercice 2

Ecrire une fonction `est_present(f : File, elt : int)->bool` qui prend en paramètres un objet `File` et un entier et renvoie $True$ si `elt` est présent dans `f`, $False$ sinon.

Cette fonction ne doit pas modifier la file passée en argument.

```python
>>> f = File()
>>> f.enfile(5)
>>> est_present(f, 5)
True
```

## Exercice 3

Ecrire une fonction `sont_egales(f1 : File, f2 : File)->bool` qui prend en paramètres deux objets `File` et renvoie comme résultat $True$ si les deux files sont égales, $False$ sinon.

## Exercice 4

Ecrire une fonction `max(f : File)->int` qui prend en paramètre un objet `File` et renvoie comme résultat l'élément le plus grand de `f`.

Cette fonction ne doit pas modifier la file passée en argument.

_________________

[Sommaire](./../../../README.md)