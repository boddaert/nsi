# Recherche textuelle

## I. Introduction

Une application de la recherche textuelle est le séquençage des génomes.

Le séquençage du génome a conduit à une collaboration fructueuse entre généticiens et informaticiens et au développement de nouveaux algorithmes.

En effet, le génome est codé sur quatre lettres : `A`, `C`, `T` et `G` qui sont les initiales de quatre bases nucléiques : adénine, cytosine, thymine et guanine.

Voici, par exemple, un extrait d'un gène d'arabica et d'un motif à retrouver :

- `AAGGTCCCTTATGATGCTGGCTTCTCTATTGATGATGATTACCAAGGAAGATCCCATTCCCCAGTATCCTGCGATGAACA`

- `AAGA`

Nous souhaitons dans cette partie écrire un algorithme efficace permettant de rechercher un motif dans un texte.

## II. Définitions

La *recherche textuelle* est un problème algorithmique de recherche qui consiste à retrouver une chaîne de caractère dans une autre chaîne de caractère et de renvoyer leur position.

Le *motif* est le nom donné à la chaîne de caractère que nous souhaitons retrouver.

Le *texte* est le nom donné à la chaîne de caractère sur laquelle la recherche s'effectue.

##### Application 1

Dans le texte `abracadabra`, rechercher et donner les positions du motif `bra`.

## III. Problème de recherche textuelle

### a) Notations

Notons $m$ le motif et $M$ la longueur de $m$.

Notons $t$ le texte et $T$ la longueur de $t$.

### b) Premières observations

- Remarquons qu'il ne peut y avoir une occurence de $m$ dans $t$ si $M > T$.

- Il y a $T + 1$ occurences si $m$ est une chaîne vide ($M = 0$).

### c) Formalisation du problème

![image](./img/formalisation_recherche_textuelle.png)

Au dessus, le texte $t$ allant de l'indice $0$ à $T-1$.

En dessous, le motif $m$ allant de l'indice $0$ à $M-1$.

Si une occurence du motif existe à la position $i$, alors les caractères `t[i]`, `t[i+1]`, ... , `t[i+(M-1)]` coïncident avec les caractères `m[0]`, `m[1]`, ... , `m[M-1]`.

## IV. Algorithme naïf

L'idée de l'algorithme naïf est de tester à chaque position la présence du motif :

```
Algorithme recherche_textuelle_naïve
Entrées : m le motif, une chaîne de caractère et t le texte, une chaîne de caractères
Sorties : La liste des positions de motif dans texte

positions <- []
Pour i allant de 0 à taille(texte)-taille(motif)+1, faire :
    Si t[i] est égal à m[0], alors :
        trouvé <- Vrai
        Pour j allant de 0 à taille(m), faire :
            Si t[i+j] est différent de m[j], alors :
                trouvé <- Faux
        Si trouvé est égal à Vrai, alors :
            Ajouter i à positions
Renvoyer positions
```

##### Application 2

a) Réécrire l'algorithme de recherche textuelle naïve en Python.

b) Vérifier le résultat suivant :

```python
>>> recherche_textuelle_naive("bra", "abracadabra")
[1, 8]
```

## V. Algorithme de Boyer-Moore

Les faibles performances de la recherche naïve lorsque la taille du texte augmente a poussé de nombreux informaticiens à proposer des solutions pour améliorer le coût algorithmique de ce type de recherche.

L'algorithme de Boyer et Moore est un algorithme de recherche textuelle très efficace developpé en 1977.

Bien trop complexe pour le programme de terminale, nous étudierons sa version simplifiée dévelopée en 1980 par Nigel Horspool.

## VI. Algorithme de Horspool

### a) Idées d'améliorations

Afin de réduire le coût algorithmique de la recherche textuelle naïve, Boyer et Moore imaginent deux concepts :

**1) Comparer de droite à gauche**

La première idée est de parcourir, non plus de gauche à droite, mais de droite à gauche le motif lors des comparaisons.

Ainsi, pour une position $i$ donnée, nous allons comparer les caractères de $m$ et $t$ de la droite vers la gauche, c'est-à-dire en comparant d'abord `m[M-1]` avec `t[i+(M-1)]` :

![image](./img/comparer_de_droite_a_gauche_1.png)

Puis, `m[-2]` avec `t[i+(M-2)]` si les caractères coïncident :

![image](./img/comparer_de_droite_a_gauche_2.png)

Etc ...

Le changement peut paraître anecdotique mais permet d'effectuer moins de comparaisons si nous la combinons avec l'idée suivante :

**2) Sauter des rangs**

La seconde idée est de pré-traiter le texte dans le but de construire un tableau des décalages.

Ce tableau des décalages permet de savoir de nombre de rang que $i$ effectuera en cas de non correspondance des lettres.

Par exemple, dans la configuration suivante, il est inutile de réaliser la comparaison à $i+1$ et $i+2$ puisque nous savons que la lettre `B` ne figure pas parmi les trois dernières lettres de $m$.

![image](./img/sauter_des_rangs.png)

### b) 

____________

[Sommaire](./../../README.md)
