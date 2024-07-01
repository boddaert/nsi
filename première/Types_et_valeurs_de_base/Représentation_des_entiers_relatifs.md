# Représentation des entiers relatifs

## I. Bit de signe

### a) Principe

> [!IMPORTANT]
> Le *bit de signe* est un bit situé tout à gauche de la séquence et qui indique s'il s'agit d'un nombre positif ou négatif.
>
> Si le bit de signe est $0$ alors le nombre est positif, sinon le nombre est négatif.

> [!TIP]
> Par exemple :
> $1101_2 = -5_{10}$.

#### <ins>Application 1</ins>

1. Trouver la représentation décimale de $10101_2$.

2. Trouver la représentation binaire de $-13_{10}$.

### b) Problèmes

Problème n°1 : En utilisant cette méthode, le chiffre $0$ possède deux représentations : $1000_2$ et $0000_2$.

Problème n°2 : Cela complique les opérations arithmétiques.

> [!TIP]
> Par exemple : $1101_2 + 0101_2 = 0010_2$

#### <ins>Application 2</ins>

Expliquer le problème soulevé dans l'exemple. 

## II. Complément à deux

La méthode du complément à deux conserve le bit de signe mais la représentation binaire des entiers négatifs s'obtient en :

1. Inversant la valeur des bits ($0 \to 1$ et $1 \to 0$) de la séquence.

2. Ajoutant $1$.

> [!TIP]
> Par exemple :
> 
> 1. $5_{10}$ donne en représentation binaire : $0101_2$.
>
> 2. $Inverse(0101_2) = 1010_2$.
>
> 3. $1010_2 + 0001_2 = 1011_2$
>
> $-5_{10}$ donne en représentation binaire $1011_2$ en complément à deux.

#### <ins>Application 3</ins>

a) En suivant la méthode du complément à deux, trouver la représentation binaire de $-7$.

b) En suivant la méthode du complément à deux, trouver la représentation binaire de $-2$.

## III. Taille d'un entier

> [!IMPORTANT]
> La *taille* d'un nombre est le nombre de chiffres composant sa séquence.

> [!TIP]
> Par exemple :
> La taille de $5_{10}$ vaut $1$ et la taille de $101_2$ ($= 5$ en base deux) vaut $3$.

#### <ins>Application 4</ins>

a) Donner la taille de $A45_{16}$.

b) Donner la taille de $11110_2$.

## IV. Intervalles de représentation

### a) Taille fixe des entiers

Lorsque nous représentons les entiers en base deux, nous utilisons une taille fixe des séquences.

Ces tailles sont par défaut une puissance de deux, c'est-à-dire que nous représentons les entiers soit dans une représentation binaire de **quatre bits**, de **huit bits**, de **seize bits**, de **trente-deux bits** ou encore de **soixante-quatre bits**.

Nous savons que les seize premiers entiers peuvent être représentés sous quatre bits.

Le dix-septième entier doit donc être représenté avec huit bits.

> [!NOTE]
> Une séquence de huit bits s'appelle un *octet*.

#### <ins>Application 5</ins>

a) Donner le nombre de bits nécessaire de taille fixe pour représenter en base deux le nombre $20_{10}$.

b) Donner le nombre de bits nécessaire de taille fixe pour représenter en base deux le nombre $200_{10}$.

### b) Intervalle de représentation des entiers naturels

> [!IMPORTANT]
> L'*intervalle de représentation* donne l'entier minimum et maximum pouvant être représentés pour une taille donnée.

Pour une séquence de $n$ bits, l'intervalle de représentation des entiers naturels est compris entre $0$ et $2^{n}-1$.

> [!TIP]
> Par exemple :
> L'intervalle de représentation sur quatre bits est compris entre $0$ à $2^4-1$ donc de $0_{10}$ à $15_{10}$.

#### <ins>Application 6</ins>

a) Donner l'intervalle de représentation des entiers naturels sur huit bits.

b) Donner l'intervalle de représentation des entiers naturels sur seize bits.

### c) Intervalle de représentation des entiers relatifs

Comme le premier bit est le bit de signe, l'intervalle de représentation pour les entiers relatifs est réduit.

Pour une séquence de $n$ bits, l'intervalle de représentation des entiers relatifs est compris entre $-2^{n-1}$ et $2^{n-1}-1$.

> [!TIP]
> Par exemple :
> L'intervalle de représentation sur quatre bits est compris entre $-2^3$ à $2^3-1$ donc de $-8_{10}$ à $7_{10}$.

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

#### <ins>Application 7</ins>

a) Donner l'intervalle de représentation des entiers relatifs sur huit bits.

b) Donner l'intervalle de représentation des entiers relatifs sur seize bits.

_______________

[Exercices](./Exercices/Exercices_representation_des_entiers_relatifs.md)

_______________

[Sommaire](./../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 