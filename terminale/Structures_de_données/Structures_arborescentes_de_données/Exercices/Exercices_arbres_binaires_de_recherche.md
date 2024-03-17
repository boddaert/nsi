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

Ecrire une fonction `est_abr(ab : AB)->bool` qui prend en paramètre un arbre binaire et renvoie $True$ s'il s'agit d'un ABR, $False$ sinon.

Nous pourrons nous aider de la définition d'un ABR donné en leçon.

__________________

[Sommaire](./../../README.md)


