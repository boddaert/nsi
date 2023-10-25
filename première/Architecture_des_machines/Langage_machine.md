# Langage machine

## I. Introduction

Nous avons lu dans la leçon précédente que les instructions des programmes étaients stockées dans la mémoire sous forme de séquence de bits.

Or, lorsque nous écrivons des programmes, nous le faisons dans un langage de haut niveau et non en binaire.

Il y a donc une traduction de notre programme écrit en Python en langage machine.

## II. Chaîne de production d'un programme

### a) Définitions

Le *langage machine* est l'unique langage compréhensible directement par l'ordinateur. Ce langage de bas niveau est écrit en binaire.

En réalité, il existe un troisième langage appelé *langage d'assemblage* qui joue l'intermédiaire dans la traduction du langage de haut niveau à bas niveau.

La *chaîne de production d'un programme* décrivent les étapes consécutives de la traduction d'un programme écrit dans un langage de haut niveau à bas niveau.

### b) Schéma

```mermaid
flowchart TB
    a["Programme dans un langage de haut niveau (Python) -> `sum(a,b)`"]
    b["Programme dans un langage d'assemblage -> `add e1, e2`"]
    c["Programme dans le langage machine -> `0011 00011010 11100100`"]
    a-- Traduction -->b-- Traduction -->c
```
