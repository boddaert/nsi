# Langage machine

## I. Introduction

Nous avons lu dans la leçon précédente que les instructions des programmes étaients stockées dans la mémoire sous forme de séquence de bits.

Or, lorsque nous écrivons des programmes, nous le faisons dans un langage de haut niveau et non en binaire.

Il y a donc une traduction de notre programme écrit en Python en langage machine.

## II. Chaîne de production d'un programme

### a) Définitions

> [!IMPORTANT]
> Le *langage machine* est l'unique langage compréhensible directement par l'ordinateur. Ce langage de bas niveau est écrit en binaire.

En réalité, il existe un troisième langage appelé *langage d'assemblage* qui joue l'intermédiaire dans la traduction du langage de haut niveau à bas niveau.

> [!IMPORTANT]
> La *chaîne de production d'un programme* décrivent les étapes consécutives de la traduction d'un programme écrit dans un langage de haut niveau à bas niveau.

### b) Schéma

```mermaid
flowchart TB
    a["Programme dans un langage de haut niveau (Python) -> `sum(a,b)`"]
    b["Programme dans un langage d'assemblage -> `add e1, e2`"]
    c["Programme dans le langage machine -> `0011 00011010 11100100`"]
    a-- Compilateur -->b-- Assembleur -->c
```

______________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p>
