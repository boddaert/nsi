# Algorithme du tri par sélection

## I. Principe

Nous parcourons la liste de la gauche vers la droite, en maintenant sur la gauche une partie triée :

![image](./img/schema_tri.png)

Il y a donc une partie gauche triée et vide au lancement du programme et une partie droite non triée.

À chaque étape, le plus petit élément de la partie droite non triée est échangé avec le dernier élément de la partie gauche triée.

![animation](./img/animation_tri_selection.gif)

##### Application 1

Écrire une fonction ``minimum(l : list, i : int)->int`` prenant en paramètre une liste d'entiers et un entier et renvoyant l'indice de l'élément le plus petit dans la tranche `l[i:]`.

##### Application 2

Écrire en python une fonction ``tri_selection(l : list)->None`` prenant en paramètre une liste d'entiers et qui trie dans l'ordre croissant les éléments de ``l``.

Le tri par sélection est un tri en place donc la fonction ``tri_selection()`` ne renvoie rien.

## II. Complexité


##### Application 3

Dans cette question, nous souhaitons déterminer la complexité temporelle de cet algorithme en comptant le nombre de comparaisons.

a) Proposer, pour une liste de longueur $n$, une estimation du nombre de fois que la fonction ``tri_selection()`` exécute la fonction ``minimum()``.

Trouver cette estimation en déroulant la fonction à la main sur papier.

b) Modifier la fonction ``minimum()`` pour qu'elle affiche le nombre de comparaisons qu'elle effectue.

c) À partir de l'affichage, comment retrouver le nombre total de comparaisons effectués par la fonction ``tri_selection()`` ?

d) Pour une liste de longueur $n$, estimer le nombre de comparaisons effectuées par la fonction `tri_selection()`.

______________

[Sommaire](./../README.md)