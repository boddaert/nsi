# Tri d'une table

## I. Définitions

> [!IMPORTANT]
> *Trier* une table de données, c'est organiser les données pour qu'elles apparaissent dans un certain ordre.

Généralement, les informaticiens trient les tables de données en fonction d'un ou de deux critères. C'est-à-dire en fonction d'un ou de deux attributs.

## II. Fonctions de tri

En Python, il existe les fonctions `sorted()` et `sort()` et permettent toutes les deux de trier une liste d'entiers ou de caractères dans l'ordre lexicographique.

Néanmoins, une différence subsiste, `sort()` est un tri en place, contrairement à `sorted()`.

> Un *tri en place* est un tri qui modifie directement la structure en mémoire.

> [!TIP]
> Par exemple :
> ```python
> >>> l = [5, 8, 2, 0, 7, 9, 2, 1]
> >>> l.sort()
> >>> l
> [0, 1, 2, 2, 5, 7, 8, 9]
> ```
>
>
> ```python
> >>> l = [5, 8, 2, 0, 7, 9, 2, 1]
> >>> l_triee = sorted(l)
> >>> l_triee
> [0, 1, 2, 2, 5, 7, 8, 9]
> >>> l
> [5, 8, 2, 0, 7, 9, 2, 1]
> ```

## III. Trier une table en fonction d'un attribut

La fonction `sorted()` peut prendre comme second argument une fonction appelée `key`.

Cette fonction renvoie le critère ou l'attribut sur lequel la fonction `sorted()` trie.

> [!TIP]
> Par exemple :
> L'argument `key` peut prendre la fonction `age()` qui renvoie l'année de naissance :
>
> ```python
> def age(personne : dict)->int :
>     return personne["Année de naissance"]
> ```

La fonction `sorted()` peut également prendre un troisème argument indiquant si l'ordre de tri doit être inversé.

> [!TIP]
> Par exemple :
> ```python
> >>> sorted(personnes, key=age, reverse=True)
> [{'Sexe': 'F', 'Prénom': 'Charlotte', 'Année de naissance': 1988}, {'Sexe': 'F', 'Prénom': 'Béatrice', 'Année de naissance': 1964}, {'Sexe': 'M', 'Prénom': 'Alphonse', 'Année de naissance': 1932}]
> ```

#### <ins>Application 1</ins>

a) Utiliser la fonction de tri `sorted()` afin de trier les produits du magasin par ordre croissant de prix.

b) Utiliser la fonction de tri `sorted()` afin de trier les produits du magasin par ordre décroissant de quantité.

___________

[Sommaire](./../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 