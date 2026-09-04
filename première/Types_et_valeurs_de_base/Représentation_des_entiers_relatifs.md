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

a) Trouver la représentation décimale de $10101_2$.

b) Trouver la représentation binaire de $-13_{10}$.

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
> 1. $5_{10}$ donne en représentation binaire : $0101_2$ sur quatre bits.
>
> 2. $Inverse(0101_2) = 1010_2$.
>
> 3. $1010_2 + 0001_2 = 1011_2$
>
> $-5_{10}$ donne en représentation binaire $1011_2$ en complément à deux.

> [!WARNING]
> Afin d'éviter certains problèmes de taille de données en utilisant la méthode du complément à deux, il est nécessaire de donner la taille de la séquence de bits sur laquelle nous travaillons. Cette taille doit être une puissance de deux : 4, 8, 16, 32, etc ... Elle sera généralement donnée en énoncé.

#### <ins>Application 3</ins>

a) En suivant la méthode du complément à deux, trouver la représentation binaire de $-7$ sur quatre bits.

b) En suivant la méthode du complément à deux, trouver la représentation binaire de $-2$ sur quatre bits.

_______________

[Exercices](./Exercices/Exercices_representation_des_entiers_relatifs.md)

_______________

[Sommaire](./../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 