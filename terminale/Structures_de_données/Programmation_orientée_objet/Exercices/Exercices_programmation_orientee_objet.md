# Exercices

## Exercice 1

Dans cet exercice, nous allons travailler avec une classe `Boite`.

Les attributs de cette classe sont `longueur`, `largeur`, `hauteur` trois entiers compris entre 1 et 50 inclus

Les méthodes de cette classe sont `volume()` qui renvoie le volume de la boîte et `infos()` qui renvoie une chaîne de caractères contenant les informations sur la boîte sous la forme $L×l×h$.

a) Ecrire le constructeur de la classe `Boite` qui prend trois entiers en paramètres : la longueur, la largeur et la hauteur.

b) Ecrire tous les accesseurs liés aux attributs `longueur`, `largeur` et `hauteur`. Puis, dans la console, vérifier le fonctionnement de vos méthodes.

c) Ecrire la méthode `volume()` qui ne prend pas de paramètres et renvoie comme résultat le volume de la boîte.

d) Ecrire la méthode `infos()` qui ne prend pas de paramètres et renvoie une chaîne de caractère de la forme $Lxlxh$.

## Exercice 2

Reprendre la classe de l'exercice 1.

a) En dehors de la classe, écrire une fonction `maxi(b1 : Boite, b2 : Boite)->Boite` qui prend deux boîtes en paramètres et renvoie la boite dont le volume est le plus grand.

b) Tester votre fonction dans la console.

## Exercice 3

Reprendre la classe de l'exercice 1.

a) En dehors de la classe, écrire une fonction `creer_liste_boites(n : int)->list` qui prend un nombre entier $n$ en paramètre et renvoie une liste de $n$ boîtes dont les tailles sont aléatoires.

b) En dehors de la classe, écrire une fonction `maxi_liste_boites(liste_boites : list)->Boite` qui prend une liste de boîtes en paramètre et renvoie la boite dont le volume est le plus grand.

c) Tester vos deux fonctions dans la console.

_______________

[Sommaire](./../../../README.md)