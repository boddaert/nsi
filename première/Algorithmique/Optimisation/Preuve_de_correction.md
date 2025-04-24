# Preuve de correction

## I. Définitions

> [!IMPORTANT]
> La *preuve de correction d'un algorithme* est une preuve cherchant à déterminer si un algorithme est correct. C'est-à-dire, s'il fait correctement la chose qu'il est censé faire.

Faire la preuve de correction d'un algorithme est en particulier nécessaire lorsque celui-ci contient des boucles.

## II. Invariant de boucle

> [!IMPORTANT]
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

Nous remarquons que la valeur de `i_elt` contient l'indice de l'élément (s'il est présent) dans l'intervalle $[l[0],l[i]]$.

L'invariant de cet algorithme est donc : "La variable `i_elt` contient `-1` ou l'indice de `elt` avec $0 \leq i_{elt} \leq i$".

Il s'agit bien d'une propriété vraie à l'entrée de la boucle, à chaque itération de boucle et à la sortie de la boucle.

Cet algorithme admet un invariant de boucle et est donc correct.

#### <ins>Application 1</ins>

Trouver l'invariant de boucle de l'algorithme suivant `multiplication` afin de prouver qu'il est correct :

```
Algorithme : multiplication(n, m)

produit = 0
TantQue m != 0, faire :
    produit = produit + n
    m = m - 1
Renvoyer produit
```

________________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 