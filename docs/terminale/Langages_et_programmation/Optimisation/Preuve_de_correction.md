# Preuve de correction

## I. Définitions

La *preuve de correction d'un algorithme* est une preuve cherchant à déterminer si un algorithme est correct.

Faire la preuve de correction d'un algorithme est en particulier nécessaire lorsque celui-ci contient des boucles.

## II. Invariant de boucle

Un *invariant de boucle* est une propriété qui doit être vraie à l'entrée de la boucle, à chaque itération de boucle et à la sortie de la boucle.

Ainsi, pour prouver qu'un algorithme est correct, il faut trouver son invariant.

### III. Mise en situation

L'algorithme `recherche_1` est-il correct ?

```
Algorithme : recherche_1(l, elt)

i = 0
i_elt = -1
TantQue i < taille(l), faire :
    Si l[i] == elt, alors :
        i_elt = i
    i = i + 1
Renvoyer i_elt
```

Nous remarquons que la valeur de `i_elt` contient l'indice de l'élément (s'il est présent) dans l'intervalle `l[0]` et `l[i]`.

L'invariant de cet algorithme est donc $i\textunderscore elt == (-1) \lor i\textundercsore elt ==(indice(elt))$ avec $0 \leq i_{elt} \leq i$.

En français : la variable `i_elt` contient `-1` ou l'indice de `elt` avec $0 \leq i_{elt} \leq i$.

Il s'agit bien d'une propriété vraie à l'entrée de la boucle, à chaque itération de boucle et à la sortie de la boucle.

Cet algorithme admet un invariant de boucle donc est correct.

##### Application 1

Trouver l'invariant de boucle de l'algorithme suivant `multiplication` afin de prouver qu'il est correct :

```
Algorithme : multiplication(n, m)

produit = 0
TantQue m != 0, faire :
    produit = produit + n
    m = m - 1
Renvoyer n
```

________________

[Sommaire](./../../README.md)