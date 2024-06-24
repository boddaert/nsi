# Problèmes d'optimisation combinatoire

## I. Définitions

Un *problème d'optimisation combinatoire* consiste à trouver dans un ensemble de solutions la meilleure solution selon un critère donné. 

Généralement, la meilleure solution est une *maximisation* ou une *minimisation* du critère.

Le *critère* est la quantité que nous cherchons à optimiser.

## II. Exemple du rendu de monnaie

Le problème de rendu de monnaie est un problème d'optimisation combinatoire.

L'intitulé de ce problème est le suivant : Après avoir effectué une vente, il faut rendre la monnaie au client si celui-ci donne une somme supérieure au prix d'achat.

Par exemple, si le client donne un billet de $50$ euros pour un article coûtant $25$, il faudra lui rendre $25$.

Plusieurs solutions existent : 

- Vingt-cinq pièces de $1$.

- Vingt-trois pièces de $1$ et une pièce de $2$.

- Vingt-et-une pièces de $1$ et deux pièces de $2$.

- Vingt pièces de $1$ et un billet de $5$.

- etc ...

Dans ce problème, nous cherchons à rendre un nombre minimal de pièces et de billets.

Donc, parmi l'ensemble des solutions existantes, ce problème cherche une minimisation du critère qui est le nombre de pièces.

##### Application 1

Démontrer que le problème du voyageur de commerce est un problème d'optimisation combinatoire.

## III. Formalisation (hors programme)

Un problème d'optimisation combinatoire $P$ est un quadruplet $(I, r, f, g)$ où :

- $I$ désigne un ensemble d'instances du problème (données sur lesquelles se pose le problème).

- $r$ est une fonction qui, à chaque instance $i$ de $I$, associe un ensemble fini de solutions possibles.

- $f$ est une fonction qui, avec $i$ une instance de problème et $s$ l'une de ses solutions, renvoie le critère sur lequel optimiser.

- $g$ est une fonction qui maximise ou minimise le critère.

_________________

[Sommaire](./../../README.md)