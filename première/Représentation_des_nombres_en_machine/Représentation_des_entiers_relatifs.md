# Représentation des entiers relatifs

## I. Bit de signe

### a) Principe

Nous ajoutons un bit supplémentaire appelé bit de signe, situé tout à gauche de la séquence, et qui indique s'il s'agit d'un nombre positif ou négatif.

Si le bit de signe est zéro alors le nombre est positif.

Si le bit de signe est un alors le nombre est négatif.

Ainsi : $1101_2 = -5_{10}$.

##### Application 1

Trouver la représentation décimale de $11101_2$.

Trouver la représentation binaire de $-13_{10}$.

### b) Problèmes

Premier problème : En utilisant cette méthode, le chiffre $O$ possède deux représentations : $1000_2$ et $0000_2$.

Second problème : Cela complique les opérations arithmétiques tel que l'addition par exemple.

Ainsi $-5_{10} + 5_{10}$ en représentation décimale donne comme résultat $0_{10}$.

Alors qu'en représentation binaire : $1101_2 + 0101_2 = 0010_2$.

## II. Complément à deux

### a) Principe

La méthode du complément à deux conserve le bit de signe mais la représentation binaire des entiers négatifs s'obtient en inversant la valeur des bits ($0 \to 1$, $1 \to 0$) de la séquence et en ajoutant $1$.

Ainsi, $-5_{10}$ donne $1011_2$ en utilisant le complément à deux parce que :

1) $5_{10}$ donne $0101_2$.

2) $Inverse(0101_2) = 1010_2$.

3) $1010_2 + 0001_2 = 1011_2$

##### Application 2

En suivant la méthode du complément à deux, trouver la représentation binaire de $-9$.

En suivant la méthode du complément à deux, trouver la représentation binaire de $-2$.
_______________

[Feuille d'exercices](./Exercices/Exercices_representation_des_entiers_relatifs.md)

_______________

[Sommaire](./../README.md)