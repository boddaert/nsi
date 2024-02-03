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

L'invariant de cet algorithme est donc $i_elt == (-1) \lor (indice(elt))$ avec $0 \leq i_elt \leq i$.

Il s'agit bien d'une propriété vraie à l'entrée de la boucle, à chaque itération de boucle et à la sortie de la boucle.

Cet algorithme admet un invariant de boucle donc est correct.

________________

[Sommaire](./../README.md)