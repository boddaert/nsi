# Exercices

## Exercice 1

a) Dessiner tous les arbres possibles de hauteur $3$.

b) Dessiner tous les arbres possibles de taille $4$.

## Exercice 2

Écrire une fonction itérative `parcours_largeur_d_abord(ab : AB)->None` qui prend en paramètre un arbre binaire et affiche tous les noeuds de l'arbre dans l'ordre du parcours en largeur d'abord.

## Exercice 3

Écrire une fonction itérative `parcours_profondeur_d_abord(ab : AB)->None` qui prend en paramètre un arbre binaire et affiche tous les noeuds de l'arbre dans l'ordre du parcours en profondeur d'abord.

## Exercice 4

a) Écrire une fonction récursive `parcours_prefixe(ab : AB)->None` qui prend en paramètre un arbre binaire et affiche tous les noeuds de l'arbre dans l'ordre du parcours préfixe.

b) Écrire une fonction récursive `parcours_infixe(ab : AB)->None` qui prend en paramètre un arbre binaire et affiche tous les noeuds de l'arbre dans l'ordre du parcours infixe.

c) Écrire une fonction récursive `parcours_suffixe(ab : AB)->None` qui prend en paramètre un arbre binaire et affiche tous les noeuds de l'arbre dans l'ordre du parcours suffixe.

## Exercice 5

Écrire une fonction récursive `taille(ab : AB)->int` qui prend en paramètre un arbre binaire et renvoie la taille de l'arbre.

## Exercice 6

Écrire une fonction récursive `hauteur(ab : AB)->int` qui prend en paramètre un arbre binaire et renvoie la hauteur de l'arbre.

## Exercice 7

Écrire une fonction récursive `est_present(ab : AB, elt : int)->bool` qui prend en paramètre un arbre binaire et renvoie $True$ si l'élément est présent dans l'arbre, $False$ sinon.

## Exercice 8

```python
def mystere(ab : AB)->int:
    if ab.est_vide() :
        return 0
    else :
        return ab.racine() + max(mystere(ab.sag()), mystere(ab.sad()))
```

a) Exécuter à la main l'appel à la fonction `mystere()` avec comme paramètre le second arbre de l'application trois.

b) En déduire sur ce que réalise la fonction `mystere()`.

## Exercice 9

Écrire une fonction récursive `peigne_droit(h : int)->AB` qui prend en paramètre un entier et renvoie un peigne droit de hauteur $h$ dont les éléments sont des entiers aléatoires.

## Exercice 10

Écrire une fonction récursive `est_peigne_droit(ab : AB)->bool` qui prend en paramètre un arbre binaire et renvoie $True$ si l'arbre binaire est un peigne droit, $False$ sinon.

## Exercice 11

Écrire une fonction récursive `ab_complet(h : int)->AB` qui prend en paramètre un entier et renvoie un arbre binaire complet de hauteur $h$ dont les éléments sont des entiers aléatoires.

## Exercice 12 (Difficile)

Écrire une fonction **itérative** `est_complet(ab : AB)->bool` qui prend en paramètre un arbre binaire et renvoie $True$ si l'arbre est complet, $False$ sinon.

________________

[Sommaire](./../../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 