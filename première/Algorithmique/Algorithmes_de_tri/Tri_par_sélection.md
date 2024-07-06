# Tri par sélection

## I. <a name="algorithme"></a>Algorithme

L'algorithme du tri par sélection est un algorithme de tri par comparaison.

Dans cet algorithme, nous parcourons la liste de la gauche vers la droite, en maintenant sur la gauche une partie triée :

<img src="./img/schema_tri.png" width=800>

Il y a donc une partie gauche triée et vide au lancement du programme et une partie droite non triée.

Le principe du tri par sélection est le suivant :

- Rechercher le plus petit élément de la partie droite non triée, et l'échanger avec le premier élément de la partie droite non triée.

- Le premier élément de la partie droite non triée est maintenant trié, nous l'incluons dans la partie gauche triée.

- Continuer de cette façon jusqu'à ce que la taille de la partie gauche triée soit égale à la taille de la liste.

Voici, par exemple, une animation décrivant le principe du tri par sélection :

<img src="./img/animation_tri_selection.gif" width=100>

#### <ins>Application 1</ins>

Écrire une fonction `minimum(l : list, i : int)->int` qui prend en paramètre une liste d'entiers et un indice $i$ et renvoie l'indice de l'élément le plus petit dans la tranche `l[i:]`.

> Cette fonction devra utiliser la fonction `compare()`.

#### <ins>Application 2</ins>

Écrire en python une fonction `tri_selection(l : list)->None` qui prend en paramètre une liste d'entiers et trie dans l'ordre croissant les éléments de `l`.

> Le tri par sélection est un tri en place donc la fonction ``tri_selection()`` ne renvoie rien.

## II. Complexité

L'objectif est de déterminer le coût algorithmique en temps de l'algorithme du tri par sélection.

Pour cela, nous allons compter le nombre d'opérations coûteuses (les comparaisons).

La fonction `tri_selection()` exécute un appel à la fonction `minimum()`, il faut donc compter préalablement le nombre de comparaison effectuées par la fonction `minimum()`.

### a) Étude de la fonction `minimum()`

La fonction `minimum()` effectue des appels à la fonction `compare()`.

La fonction `compare()` comptabilise **une** comparaison : calculons alors le nombre d'appels effectués à la fonction `compare()`.

#### <ins>Application 3</ins>

a) Modifier la fonction ``minimum()`` pour qu'elle affiche le nombre d'appels effectué à la fonction `compare()`.

b) Qu'est-il affiché lorsque j'exécute la fonction `minimum()` pour une liste de longueur $5$ ? $10$ ? $20$ ?

c) En déduire, pour une liste de longueur $n$, une estimation du nombre de fois que la fonction `minimum()` exécute la fonction `compare()`.

### b) Étude de la fonction `tri_selection()`

La fonction `tri_selection()` effectue des appels à la fonction `minimum()`.

Le nombre total de comparaison de la fonction `tri_selection()` est la somme des appels à la fonction `compare()`.

> Rappel : $somme\quad des\quad termes\quad d'une\quad suite\quad arithmétique\quad =\quad nombre\quad de\quad termes \times \dfrac{(premier\quad terme\quad +\quad dernier\quad terme)}{2}$

#### Application 4

a) Qu'est-il affiché lorsque j'exécute la fonction `tri_selection()` pour une liste de longueur $5$ ? $10$ ? $20$ ?

b) À l'aide de la formule mathématique, donner le nombre exact de comparaisons effectuées par la fonction `tri_selection()` pour une liste de taille $5$, $10$ et $20$.

### c) Généralisation du coût algorithmique 

Pour une liste de taille $n$ donnée, le coût algorithmique temporel est égal à $\dfrac{n(n-1)}{2}$.

Ce qui est de l'ordre de $O(n²)$ donc le tri par sélection possède un coût quadratique (voir courbes : [complexité](./../Optimisation/Complexité.md)).

## III. Terminaison

Prouver qu'un algorithme se termine, c'est trouver son variant de boucle (voir [Preuve de terminaison](./../Optimisation/Preuve_de_terminaison.md)).

Étant donné que l'algorithme de tri par sélection est doté de deux boucles `for`, nous pouvons affirmer qu'il se termine.

#### <ins>Application 5</ins>

En relisant [I. Algorithme](#algorithme) de cette leçon, repérer un variant de boucle afin d'affirmer, avec plus de rigueur, que l'algorithme du tri par sélection se termine bien.

## IV. Correction

Prouver qu'un algorithme est correct, c'est trouver son invariant de boucle (voir [Preuve de correction](./../Optimisation/Preuve_de_correction.md)).

L'invariant de boucle de l'algorithme du tri par sélection est : "Chaque élément de la partie droite non triée est supérieur au dernier élément de la partie gauche triée".

Il s'agit bien d'une propriété vraie à l'entrée de la boucle, à chaque itération de boucle et à la sortie de la boucle.

L'algorithme du tri par sélection admet un invariant de boucle et est donc correct.

______________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 