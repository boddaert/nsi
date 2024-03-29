# Algorithme du tri par insertion

### a) Principe

Nous parcourons la liste de la gauche vers la droite, en maintenant sur la gauche une partie triée :

![image](./img/schema_tri.png)

Plutôt que de chercher la plus petite valeur, à chaque étapes, le tri par insertion va insérer le premier élément de la partie non triée dans la partie triée à sa bonne place.

Pour insérer l'élément à sa bonne place, tous les éléments déjà triés qui sont plus grands que l'élément à insérer seront décalés d'un cran vers la droite. Puis insérer l'élément à la place ainsi libérée.

![animation](./img/animation_tri_insertion.gif)

##### Application 4

Voici ci-dessous l'algorithme de la fonction ``inserer(l : list, i : int)->None`` permettant d'insérer l'élément d'indice ``i`` dans la partie gauche triée :

```
Algorithme : insérer(l,i)
Entrées : l une liste d'entiers et i un indice
Sorties : Rien

elt <- l[i]
j <- i
Tant que j > 0 et elt <=  l[j-1], faire :
    l[j] <- l[j-1]
    j <- j - 1
l[j] <- elt
```

Réécrire, en python, la fonction ``inserer( l : list , i : int)->None`` 

##### Application 5

Écrire en python une fonction ``tri_insertion(l : list)->None`` prenant en paramètre une liste ``l`` et trie dans l'ordre croissant les éléments de ``l``.

Le tri par insertion est un tri en place donc la fonction ``tri_insertion()``ne renvoie rien.

##### Application 6

Dans cette question, nous souhaitons déterminer la complexité de cet algorithme.

a) Donner, pour la liste `l = [5, 6, 2, 1, 3, 4]`, le nombre de fois que la fonction ``tri_insertion()`` exécute la fonction `inserer()`. 

Trouver cette estimation en executant le code à la main sur papier.

b) Pour une liste déjà triée croissante, par exemple :``[1, 2, 3, 4, 5, 6, 7, 8]``, estimer le nombre de comparaisons effectuées par la fonction `tri_insertion()`.

c) Pour une liste strictement décroissante, par exemple : ``[8, 7, 6, 5, 4, 3, 2, 1]``, estimer le nombre de comparaisons effectuées par la fonction `tri_insertion()`.

d) Modifier la fonction `inserer()` pour qu'elle affiche le nombre de comparaisons qu'elle effectue.

e) À partir de l'affichage, donner le nombre de comparaisons total effectués par la fonction ``tri_insertion()`` pour les listes `[ 1, 2, 3, 4, 5, 6, 7, 8]` et `[ 8, 7, 6, 5, 4, 3, 2, 1]`.

f) Peut-il y avoir une meilleure complexité de l'algorithme du tri par insertion que celle sur une liste déjà triée ?

g) Comparer la complexité du tri par sélection avec la complexité du tri par insertion.