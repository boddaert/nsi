# Problèmes d'optimisation combinatoire

## I. Définitions

> [!IMPORTANT]
> Un *problème d'optimisation combinatoire* consiste à trouver dans un ensemble de solutions la meilleure solution selon un critère donné. 
>
> Généralement, la meilleure solution est une *maximisation* ou une *minimisation* du critère.

> [!IMPORTANT]
> Le *critère* est la quantité que nous cherchons à optimiser.

## II. Exemple du rendu de monnaie

Le problème de rendu de monnaie est un problème d'optimisation combinatoire.

L'intitulé de ce problème est le suivant : Après avoir effectué une vente, il faut rendre la monnaie au client si celui-ci donne une somme supérieure au prix d'achat.

> [!TIP]
> Par exemple :
> Si le client donne un billet de $50$ euros pour un article coûtant $25$, il faudra lui rendre $25$.
>
> Plusieurs solutions existent : 
> 
> 1. Vingt-cinq pièces de $1$.
>
> 2. Vingt-trois pièces de $1$ et une pièce de $2$.
>
> 3. Vingt-et-une pièces de $1$ et deux pièces de $2$.
>
> 4. Vingt pièces de $1$ et un billet de $5$.
>
> - etc ...

Dans ce problème, nous cherchons à rendre un nombre minimal de pièces et de billets.

Donc, parmi l'ensemble des solutions existantes, ce problème cherche une minimisation du critère qui est le nombre de pièces.

#### <ins>Application 1</ins>

a) Donner au moins deux autres exemples de problème d'optimisation combinatoire

b) Justifier en quoi ils sont des problèmes d'optimisation combinatoire.

## III. Formalisation (hors programme)

Un problème d'optimisation combinatoire $P$ est un quadruplet $(I, r, f, g)$ où :

- $I$ désigne un ensemble d'instances du problème (données sur lesquelles se pose le problème).

- $r$ est une fonction qui, à chaque instance $i$ de $I$, associe un ensemble fini de solutions possibles.

- $f$ est une fonction qui, avec $i$ une instance de problème et $s$ l'une de ses solutions, renvoie le critère sur lequel optimiser.

- $g$ est une fonction qui maximise ou minimise le critère.

#### <ins>Application 2</ins>

Formaliser le problème du rendu de monnaie en un problème d'optimisation combinatoire $P$ en précisant à quoi correspond chacun des éléments de $P$.

_________________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 