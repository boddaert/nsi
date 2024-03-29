# Tri par sélection

## I. Algorithme

L'algorithme du tri par sélection est un algorithme de tri par comparaison.

Dans cet algorithme, nous parcourons la liste de la gauche vers la droite, en maintenant sur la gauche une partie triée :

![image](./img/schema_tri.png)

Il y a donc une partie gauche triée et vide au lancement du programme et une partie droite non triée.

Le principe du tri par sélection est le suivant :

- Rechercher le plus petit élément de la partie droite non triée, et l'échanger avec le premier élément de la partie droite non triée.

- Le premier élément de la partie droite non triée est maintenant trié, nous l'incluons dans la partie gauche triée.

- Continuer de cette façon jusqu'à ce que la taille de la partie gauche triée soit égale à la taille de la liste.

Voici, par exemple, une animation décrivant le principe du tri par sélection :

![animation](./img/animation_tri_selection.gif)

##### Application 1

Écrire une fonction `compare(a : int, b : int)->bool` qui prend en paramètre deux entiers et renvoie $True$ si $a > b$.

##### Application 2

Écrire une fonction `minimum(l : list, i : int)->int` qui prend en paramètre une liste d'entiers et un indice $i$ et renvoie l'indice de l'élément le plus petit dans la tranche `l[i:]`.

> Cette fonction devra utiliser la fonction `compare()`.

##### Application 3

Écrire en python une fonction `tri_selection(l : list)->None` qui prend en paramètre une liste d'entiers et trie dans l'ordre croissant les éléments de `l`.

> Le tri par sélection est un tri en place donc la fonction ``tri_selection()`` ne renvoie rien.

## II. Complexité

L'objectif est de déterminer le coût algorithmique en temps de l'algorithme du tri par sélection.

Pour cela, nous allons compter le nombre d'opérations coûteuses (les comparaisons).

La fonction `tri_selection()` exécute un appel à la fonction `minimum()`, il faut donc compter préalablement le nombre de comparaison effectuées par la fonction `minimum()`.

### a) Étude de la fonction `minimum()`

La fonction `minimum()` effectue des appels à la fonction `compare()`.

La fonction `compare()` comptabilise **une** comparaison : calculons alors le nombre d'appels effectués à la fonction `compare()`.

##### Application 4

a) Modifier la fonction ``minimum()`` pour qu'elle affiche le nombre d'appels effectué à la fonction `compare()`.

b) Qu'est-il affiché lorsque j'exécute la fonction `minimum()` pour une liste de longueur $5$ ? $10$ ? $20$ ?

c) En déduire, pour une liste de longueur $n$, une estimation du nombre de fois que la fonction `minimum()` exécute la fonction `compare()`.

### b) Étude de la fonction `tri_selection()`

La fonction `tri_selection()` effectue des appels à la fonction `minimum()`.

Le nombre total de comparaison de la fonction `tri_selection()` est la somme des appels à la fonction `compare()`.

> Rappel : $somme\quad des\quad termes\quad d'une\quad suite\quad arithmétique = nombre\quad de\quad termes \times \dfrac{(premier\quad terme + dernier\quad terme)}{2}$

##### Application 5

a) Qu'est-il affiché lorsque j'exécute la fonction `tri_selection()` pour une liste de longueur $5$ ? $10$ ? $20$ ?

b) À l'aide de la formule mathématique, donner le nombre exact de comparaison effectuées par la fonction `tri_selection()` pour une liste de taille $5$, $10$ et $20$.

### c) Généralisation du coût algorithmique 

Pour une liste de taille $n$ donnée, le coût algorithmique temporel est égale à $\dfrac{n(n-1)}{2}$.

Ce qui est de l'ordre de $O(n²)$ donc le tri par sélection possède un coût quadratique (voir courbes : [complexité](./../Optimisation/Complexité.md)).

## III. Terminaison

Prouver qu'un algorithme se termine, c'est trouver son variant de boucle (voir [Preuve de terminaison](./../Optimisation/Preuve_de_terminaison.md)).

Étant donné que l'algorithme de tri par sélection est doté de deux boucles `for`, nous pouvons affirmer qu'il se termine.

##### Application 6

En relisant le grand I de cette leçon, repérer un variant de boucle afin d'affirmer, avec plus de rigueur, que l'algorithme du tri par sélection se termine bien.

## IV. Correction

Nous parcourons la liste de la gauche vers la droite, en maintenant sur la gauche une partie triée :

![image](./img/schema_tri.png)

Il y a donc une partie gauche triée et vide au lancement du programme et une partie droite non triée.

À chaque étape, le plus petit élément de la partie droite non triée est échangé avec le dernier élément de la partie gauche triée.
______________

[Sommaire](./../README.md)