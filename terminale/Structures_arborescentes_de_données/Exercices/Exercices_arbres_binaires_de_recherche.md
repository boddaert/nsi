# Exercices

## Exercice 1

Ecrire une fonction récursive `max_abr(abr : AB)->int` qui prend en paramètre un arbre binaire de recherche et renvoie l'élément le plus grand.

## Exercice 2

Ecrire une fonction récursive `min_abr(abr : AB)->int` qui prend en paramètre un arbre binaire de recherche et renvoie l'élément le plus petit.

## Exercice 3

```python
def mystere(abr : AB, elt : int)->AB :
    if abr.est_vide() :
        return AB(elt, AB(), AB())
    else :
        if elt < abr.racine() :
            return AB(abr.racine(), mystere(abr.sag(), elt), abr.sad())
        else :
            return AB(abr.racine(), abr.sag(), mystere(abr.sad(), elt))
```

a) Exécuter à la main la fonction précédente avec l'ABR donné en exemple en leçon et l'élément $13$.

b) En déduire sur ce que réalise la fonction `mystere()`.

## Exercice 4

L'objectif de cet exercice est d'afficher la différence de coût algorithmique de l'algorithme de recherche séquentielle et l'algorithme de recherche amélioré dans un ABR.

a) A l'aide du module `random`, écrire une fonction `creer_liste_alea(n : int)->list` qui prend en paramètre un entier et renvoie une liste mélangée de taille `n` comprenant les éléments $0$ à $n-1$.

b) Ecrire une fonction `list_to_abr(l : list)->AB` qui prend en paramètre une liste d'entiers et renvoie un ABR contenant les éléments de `l`.

c) A l'aide du module `time` et sa méthode `time()` renvoyant l'heure quand elle est appelée, écrire une fonction `recherche_temps_d_execution_recherche_abr(abr : AB)->float` qui prend en paramètre un ABR et renvoie le temps d'exécution de la fonction recherche améliorée dans un ABR.

Nous prendrons le soin de rechercher un élément qui existe forcément comme $0$.

d) A l'aide du module `time` et sa méthode `time()` renvoyant l'heure quand elle est appelée, écrire une fonction `recherche_temps_d_execution_recherche_classique(abr : AB)->float` qui prend en paramètre un ABR et renvoie le temps d'exécution de la fonction recherche classique.

Nous prendrons le soin de rechercher un élément qui existe forcément comme $0$.


e) Dans le programme principal :

- Créer cent listes aléatoires avec une taille croissante allant de $10$ à $110$.

- A partir de ces listes, créer une liste de cent ABR.

- A partir de ces ABR, calculer les temps d'exécution de l'algorithme de recherche classique et mettre les résultats dans une liste.

- A partir de ces ABR, calculer les temps d'exécution de l'algorithme de recherche améliorée et mettre les résultats dans une liste.

- A l'aide du module `matplotlib`, afficher dans un graphique deux courbes : l'une représentant le temps d'exécution de la première méthode et la deuxième courbe représentant le temps d'exécution de la seconde méthode.

[Documentation de Time](https://docs.python.org/3/library/time.html)

[Documentation de Matplotlib](https://matplotlib.org/stable/users/explain/quick_start.html)

## Exercice 5 (Difficile)

Ecrire une fonction `est_abr(ab : AB)->bool` qui prend en paramètre un arbre binaire et renvoie $True$ s'il s'agit d'un ABR, $False$ sinon.

Nous pourrons nous aider de la définition d'un ABR donné en leçon.

__________________

[Sommaire](./../../README.md)


