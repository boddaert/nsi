# Représentation des entiers relatifs

## I. Bit de signe

### a) Principe

Nous ajoutons un bit supplémentaire appelé bit de signe, situé tout à gauche de la séquence, et qui indique s'il s'agit d'un nombre positif ou négatif.

Si le bit de signe est zéro alors le nombre est positif.

Si le bit de signe est un alors le nombre est négatif.

Ainsi : $1101_2 = -5_{10}$.

##### Application 1

Trouver la représentation décimale de $10101_2$.

Trouver la représentation binaire de $-13_{10}$.

### b) Problèmes

Premier problème : En utilisant cette méthode, le chiffre $0$ possède deux représentations : $1000_2$ et $0000_2$.

Second problème : Cela complique les opérations arithmétiques tel que l'addition par exemple.

Ainsi $-5_{10} + 5_{10}$ en représentation décimale donne comme résultat $0_{10}$.

Alors qu'en représentation binaire avec le bit de signe : $1101_2 + 0101_2 = 0010_2$.

## II. Complément à deux

La méthode du complément à deux conserve le bit de signe mais la représentation binaire des entiers négatifs s'obtient en inversant la valeur des bits ($0 \to 1$ et $1 \to 0$) de la séquence et en ajoutant $1$.

Ainsi, $-5_{10}$ donne en représentation binaire $1011_2$ en utilisant le complément à deux parce que :

1) $5_{10}$ donne en représentation binaire : $0101_2$.

2) $Inverse(0101_2) = 1010_2$.

3) $1010_2 + 0001_2 = 1011_2$

##### Application 2

a) En suivant la méthode du complément à deux, trouver la représentation binaire de $-7$.

b) En suivant la méthode du complément à deux, trouver la représentation binaire de $-2$.

## III. Taille d'un entier

La *taille* d'un nombre est le nombre de symbole composant sa séquence.

Ainsi, la taille de $5_{10}$ vaut $1$ et la taille de $101_2$ ($= 5$ an base deux) vaut $3$.

##### Application 3

a) Donner la taille de $A45_{16}$.

b) Donner la taille de $11110_2$.

## IV. Intervalle de représentation

### a) Taille fixe des entiers

Lorsque nous représentons les entiers en base deux, nous utilisons une taille fixe des séquences.

Ces tailles sont par défaut une puissance de deux, c'est-à-dire que nous représentons les entiers soit dans une représentation binaire de quatre bits, de huit bits, de seize bits, de trente-deux bits ou encore de soixante-quatre bits.

Nous savons que les seize premiers entiers peuvent être représentés sous quatre bits.

Le dix-septième entier est donc représenté avec huit bits :

| Représentation binaire | Représentation décimale | Taille de la représentation binaire |
| ---: | :---: | :---: |
| $0000$ | $0$ | $4$ |
| ... | ... | ... |
| $1111$ | $15$ | $4$ |
| $0001$ $0000$ | $16$ | $8$ |
| ... | ... | ... |
| $1111$ $1111$ | $255$ | $8$ |
| $0000$ $0001$ $0000$ $0000$ | $256$ | $16$ |
| ... | ... | ... |

### b) Intervalle de représentation des entiers naturels

L'intervalle de représentation donne l'entier minimum et maximum pouvant être représentés pour une taille donnée.

Pour une séquence de $n$ bits, l'intervalle de représentation des entiers naturels est compris entre $0$ et $2^{n}-1$.

Ainsi, l'intervalle de représentation sur quatre bits est compris entre $0_{10}$ et $15_{10}$.

##### Application 4

a) Donner l'intervalle de représentation des entiers naturels sur huit bits.

b) Donner l'intervalle de représentation des entiers naturels sur seize bits.

### c) Intervalle de représentation des entiers relatifs

Comme le premier bit est le bit de signe, l'intervalle de représentation pour les entiers relatifs est modifié.

Pour une séquence de $n$ bits, l'intervalle de représentation des entiers relatifs est compris entre $-2^{n-1}$ et $2^{n-1}-1$.

Ainsi, l'intervalle de représentation sur quatre bits est compris entre $-8_{10}$ et $7_{10}$.

Tableau du complément à deux sur quatre bits :

| Représentation binaire en complément à deux | Représentation décimale |
| :---: | :---: |
| $0000$ | $0$ |
| $0001$ | $1$ |
| $0010$ | $2$ |
| $0011$ | $3$ |
| $0100$ | $4$ |
| $0101$ | $5$ |
| $0110$ | $6$ |
| $0111$ | $7$ |
| $1000$ | $-8$ |
| $1001$ | $-7$ |
| $1010$ | $-6$ |
| $1011$ | $-5$ |
| $1100$ | $-4$ |
| $1101$ | $-3$ |
| $1110$ | $-2$ |
| $1111$ | $-1$ |

##### Application 5

a) Donner l'intervalle de représentation des entiers relatifs sur huit bits.

b) Donner l'intervalle de représentation des entiers relatifs sur seize bits.

_______________

[Feuille d'exercices](./Exercices/Exercices_representation_des_entiers_relatifs.md)

_______________

[Sommaire](./../README.md)