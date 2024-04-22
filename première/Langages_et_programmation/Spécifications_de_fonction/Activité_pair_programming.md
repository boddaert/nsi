# Activité : Pair Programming

Nature : Branchée

Matériel : Aucun

Prérequis : Spécifications de fonctions

À faire : Par deux

## I. Objectif

L'objectif de cette activité est de découvrir la méthode de travail utilisée dans beaucoup d'entreprises de développement : le pair programming.

## II. Principe

Le pair programming consiste à travailler par groupe de deux. L'équipe se décompose par celui qui écrit le programme et le second qui écrit la documentation et les tests.

Ils travaillent séparémment sur deux ordinateurs sans communication entre eux deux.

Le but du programmeur est d'écrire un programme qui remplit tous les tests qu'écrit le testeur.

Le but du testeur est d'écrire tous les tests (et assertions) possibles et imaginables afin de faire échouer le programme écrit par le programmeur toujours en respectant la spécification donnée.

En répétant le procédé, l'objectif final étant de réussir à écrire un programme pouvant parer à toutes les éventualités.

## III. Travail à faire

a) Par groupe de deux, décider qui sera le programmeur et qui sera le testeur.

b) En utilisant la méthode de pair programming, écrire le jeu de tests, les assertions necéssaires et le programme de la fonction `paires(l : list)->int` dont la spécification est :


```python
def paires(l : list)->int:
    """
    :param l: (list) une liste d'entiers 
    :return: (int)  le nombre de paires d'entiers dans l
    """
```

__________________

[Sommaire](./../../README.md)