# Activité : Le problème du crêpier psychorigide

Nature : Débranchée.

Matériel : Jeu de cinq planches de bois de taille différente, un crayon et une feuille de brouillon.

Prérequis : [Piles](./Piles.md), [Files](./Files.md).

À faire : Par deux.

## I. Objectif

L'objectif est d'élaborer un algorithme jouant sur les structures linéaires de données *LIFO* et *FIFO* afin de répondre au problème du crêpier psychorigide.

## II. Installation

Placez les crêpes les unes au dessus des autres dans l'ordre que vous voulez.

Il s'agit du tas de crêpes :

<img src="./img/tas_de_crepes.png" width=500>

## IV. Règles du jeu

Le crêpier psychorigide est, comme son nom l'indique, psychorigide.

Il souhaite que son tas de crêpe soit présentée de manière pyramidale. C'est-à-dire, d'ordre de taille de crêpe croissant comme ci-dessous :

<img src="./img/tas_de_crepes_ordonne.png" width=500>

Pour l'aider, vous n'avez qu'une seule opération possible : 

- Placer la spatule entre deux crêpes dans le tas et retourner toutes celles situées au-dessus de la spatule.

## V. Travail à faire

Par groupe de deux, répondre aux questions suivantes :

a) Trouver en manipulant, et écrire un algorithme en Français permettant de trier le tas de crêpe d'ordre de taille croissant en utilisant uniquement l'opération de la spatule.

b) Par quelle structure linéaire de données pourrait-on représenter le tas de crêpes ?

c) Par quelle structure de données linéaire pourrait-on représenter efficacement le retournement de crêpes situées sur la spatule ?

d) Écrire en Python, une fonction prenant en paramètre un tas de crêpes et renvoie comme un résultat un tas de crêpes ordonné.

Une crêpe étant modélisée par un entier représentant sa taille.

_______________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 