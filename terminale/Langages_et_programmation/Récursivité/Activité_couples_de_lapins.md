# Activité : Couples de lapins

Nature : Débranchée.

Matériel : Aucun.

Prérequis : [Récusivité](./Récursivité.md).

À faire : Seul.

## I. Objectif

L'objectif de cette activité est d'appliquer la récursivité et le principe de récurrence sur un problème concret.

## II. Travail à faire

a) Dessiner $12$ cases sur une feuille. Chaque case représente un enclos de lapin pour un mois dans l'année.

Nous cherchons à connaître le nombre de couple de lapins au bout du douzième mois en sachant :

- Au début du deuxième mois, les élèveurs placent un couple dans l'enclos.

- Les lapins ne peuvent se reproduire qu'à partir de l'âge de deux mois.

- A chaque début de mois, tout couple susceptible de se reproduire engendre exactement un nouveau couple de lapins.

b) Un couple de lapins est représenté par un point dans l'enclos, remplir les huit premiers mois en respectant les contraintes précédentes.

Il devient fastidieux au delà de compter le nombre de couple de lapins !

c) Pour un mois $m$ donné, quelle est la relation entre $m$, $m-1$ et $m-2$ ?

d) Pour quels mois cette relation ne s'applique t-elle pas ?

e) Soit $f(m)$ une fonction permettant de calculer le nombre de couple de lapins pour un mois $m$ donné.

A l'aide des réponses précédentes, compléter le principe de récurrence suivant :

$$
f(m)=
\begin{cases}
0 & \quad \text{si m = .....}\\ 
..... & \quad \text{si m = 1}\\
f(.....) + f(.....) & \quad \text{sinon}
\end{cases}
$$

f) Sur Thonny, écrire la fonction `f()`.

g) Donner la pile d'appels pour `f(5)`.

h) Donner maintenant le nombre de couple de lapins obtenus au bout d'une année.

_____________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 