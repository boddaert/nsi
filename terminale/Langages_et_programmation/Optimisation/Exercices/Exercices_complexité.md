# Exercices

L'objectif des exercices suivants est de tracer une courbe du temps d'exécution des algorithmes de recherche vus en leçon pour les comparer efficacement.

## Exercice 1

a) Écrire la fonction `recherche_1(l : list, elt : int)->int` qui prend en paramètre une liste d'entiers et un entier et renvoie l'indice de cet entier dans `l` s'il y est en appliquant l'algorithme `recherche_1` vu en leçon.

b) Écrire la fonction `recherche_2(l : list, elt : int)->int` qui prend en paramètre une liste d'entiers et un entier et renvoie l'indice de cet entier dans `l` s'il y est en appliquant l'algorithme `recherche_2` vu en leçon.

## Exercice 2

Écrire une fonction `cree_liste_melangee(n : int)->list` qui prend en paramètre un entier et renvoie une liste mélangée de taille $n$ contenant les éléments $0$ jusqu'à $n-1$.

Nous pourrons pour cela utiliser la fonction `shuffle()` du module `random`.

## Exercice 3

a) Écrire une fonction `mesure_temps_recherche_1(l : list)->float` qui prend en paramètre une liste d'entiers et renvoie sous forme de flottant le temps nécessaire à l'exécution de la fonction `recherche_1()`.

b) Écrire une fonction `mesure_temps_recherche_2(l : list)->float` qui prend en paramètre une liste d'entiers et renvoie sous forme de flottant le temps nécessaire à l'exécution de la fonction `recherche_2()`.

## Exercice 4

```python
from math import *
import matplotlib.pyplot as plt

l_temps_recherche_1 = []
l_temps_recherche_2 = []

for i in range(100):
    l = cree_liste_melangee(1000*i)
    l_temps_recherche_1.append(mesure_temps_recherche_1(l))
    l_temps_recherche_2.append(mesure_temps_recherche_2(l))

plt.axis([0, 100, 0, 0.025])

liste_x = [x for x in range(100)]

plt.plot(liste_x, l_temps_recherche_1, 'blue', label="Coût de l'algorithme recherche_1")
plt.plot(liste_x, l_temps_recherche_2,'red', label="Coût de l'algorithme recherche_2")

plt.legend()

plt.show()
```

a) Recopier le code ci-dessus et cliquer sur le bouton d'exécution.

b) D'après l'évolution des courbes, en déduire lequel des deux algorithmes est le plus efficace.

_____________

[Sommaire](./../../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 
