# Projet : Ice Walker

## I. Description

Le jeu du Ice Walker est un jeu à énigme sur une grille à deux dimensions vu du dessus.

En déplaçant un personnage via les quatres directions possibles (Nord, Est, Ouest et Sud), l'objectif du jeu est de faire parvenir le personnage jusqu'à une case finale.

Cependant, les autres cases du jeu sont faites de mur ou de glace qui ne facilitent pas la résolution de l'énigme. 

Le personnage ne peut évidemment pas traverser les murs.

Et le personnage, une fois lancé sur la glace, ne peut s'arrêter. A moins, bien sûr, d'arriver jusqu'à un mur.

Ce type de jeu a été repris plusieurs fois par la licence Pokémon. Voici ci-dessous un exemple de jeu Ice Walker avec sa résolution :

![image](./img/pokemon_ice_walker.gif)

## II. Cahier des charges

Le programme Python doit respecter les contraintes suivantes :

1. La grille de jeu est modélisée par une liste de listes.

2. Les mécaniques de jeu de sol glacé et de l'infranchissabilité des murs doivent être implémentées.

3. À chaque tour de jeu, le joueur entre une direction (Nord, Est, Ouest ou Sud) et fais déplacer le personnage dans la direction donnée.

4. À l'issue de chaque action du joueur, la grille doit être affichée.

6. Le score final de la partie est calculé en fonction du nombre de déplacement effectués pour atteindre la case finale.

7. Chaque fonction écrite doit être documentée par une *DocString* complète.

8. Le code doit être lisible, les noms de variables/fonctions explicites.

## III. Exemple de rendu

![gif](./img/exemple_ice_walker.gif)

_______________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 



