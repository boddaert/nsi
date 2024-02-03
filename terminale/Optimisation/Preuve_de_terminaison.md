# Preuve de terminaison

## I. Définitions

La *preuve de terminaison d'un algorithme* est une preuve cherchant à déterminer si un algorithme se termine.

Faire la preuve de terminaison d'un algorithme est en particulier nécessaire lorsque celui-ci contient des boucles.

## II. Variant de boucle

Un *variant de boucle* est une suite d'entiers naturels positifs décroissante.

Cette suite est nécessairement finie puisqu'une fois arrivée à zéro, il n'y a plus d'entiers naturels possible.

Ainsi, pour prouver qu'un algorithme se termine, il faut trouver son variant.

### III. Mise en situation

L'algorithme `recherche_1` se termine t-il ?

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

Nous remarquons que la valeur de `i` augmente à chaque itération de la boucle `TantQue` jusqu'à arriver à la taille de `l` puis s'arrête.

Le variant de cet algorithme est donc $taille(l)-i$.

Il s'agit bien d'une suite d'entiers naturels positifs décroissante.

Cet algorithme admet un variant de boucle donc se termine.

________________

[Sommaire](./../README.md)