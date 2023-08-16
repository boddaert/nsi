# Exercices

## Exercice 1

Ecrire une fonction `empiler_n(n : int)->Pile` qui prend en paramètre un entier et renvoie un objet `Pile` contenant les entiers de $1$ à $n$.

```python
>>> empiler_n(5).depile()
5
```

## Exercice 2

Ecrire une fonction `transvase(p1 : Pile, p2 : Pile)->None` qui prend en paramètres deux objets `Pile` et transvase tous les éléments de `p1` dans `p2`.

## Exercice 3 

Ecrire une fonction `est_present(p : Pile, elt : int)->bool` qui prend en paramètres un objet `Pile` et un entier et renvoie $True$ si `elt` est présent dans `p`, $False$ sinon.

Cette fonction ne doit pas modifier la pile passée en argument.

```python
>>> p = Pile()
>>> p.empile(5)
>>> est_present(p, 5)
True
```

## Exercice 4

Ecrire une fonction `sont_egales(p1 : Pile, p2 : Pile)->bool` qui prend en paramètres deux objets `Pile` et renvoie comme résultat $True$ si les deux piles sont égales, $False$ sinon.

## Exercice 5

Ecrire une fonction `bien_parenthese(mot : str)->bool` qui prend en paramètre une chaîne de caractère et renvoie $True$ si `mot` est bien parenthésé, $False$ sinon.

```python
>>> bien_parenthese("(())")
True
>>> bien_parenthese(")()")
False
>>> bien_parenthese("())")
False
```