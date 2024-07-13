# Preuve de terminaison

## I. Définitions

> [!IMPORTANT]
> La *preuve de terminaison d'un algorithme* est une preuve cherchant à déterminer si un algorithme se termine.

Faire la preuve de terminaison d'un algorithme est en particulier nécessaire lorsque celui-ci contient des boucles `while`.

## II. Variant de boucle

> [!IMPORTANT]
> Un *variant de boucle* est une suite d'entiers naturels positifs décroissante.

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

#### <ins>Application 1</ins>

Trouver le variant de boucle de l'algorithme suivant `multiplication` afin de prouver qu'il se termine :

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

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 