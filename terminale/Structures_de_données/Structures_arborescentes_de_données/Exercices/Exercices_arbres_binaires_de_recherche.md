# Exercices

## Exercice 1

Écrire une fonction récursive `max_abr(abr : AB)->int` qui prend en paramètre un arbre binaire de recherche et renvoie l'élément le plus grand.

## Exercice 2

Écrire une fonction récursive `min_abr(abr : AB)->int` qui prend en paramètre un arbre binaire de recherche et renvoie l'élément le plus petit.

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

Écrire une fonction `est_abr(ab : AB)->bool` qui prend en paramètre un arbre binaire et renvoie $True$ s'il s'agit d'un ABR, $False$ sinon.

Nous pourrons nous aider de la définition d'un ABR donné en leçon.

__________________

[Sommaire](./../../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 


