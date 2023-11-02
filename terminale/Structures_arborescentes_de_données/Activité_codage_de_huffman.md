# Activité : Codage de Huffman

Nature : branchée

Matériel : Aucun

Prérequis : Arbres binaires, encodages de textes en machine

## I. Objectif

L'objectif est d'écrire un programme permettant d'encoder un texte selon le codage de Huffman.

Le codage de Huffman est un codage binaire d'un texte qui s'appuie sur la fréquence des lettres.

Plus une lettre est fréquente dans le texte, plus la longueur du mot binaire représentant le caractère est petit.

L'encodage de Huffman est optimal, c'est-à-dire qu'il n'existe pas d'encodages utilisant moins de bits afin de représenter un texte.

Petit rappel sur les encodages de textes [Représentation des textes en machine](./../../première/Chaînes_de_caractère/Représentation_des_textes_en_machine.md).

Plus d'informations : [Wikipédia](https://fr.wikipedia.org/wiki/Codage_de_Huffman)

## II. Algorithme

L'idée est de construire un arbre binaire et de s'en servir pour donner une table de codage des caractères.

Prenons un exemple, le texte : `"aabacbada"` possède cinq lettres `a`, deux lettres `b`, une lettre `c` et une lettre `d`.

A partir de ce texte, voici son arbre de Huffman :

```mermaid
flowchart TB
    A(("(a,5)"))
    B(("(b, 2)"))
    C(("(c, 1))")
    D(("("d", 1)"))
    E(("( , 2)"))
    F(("( , 4)"))
    G(("( , 9)"))
    G --0--> F
    G --1--> A
    E --0--> C
    E --1--> D
    F --0--> B
    F --1--> E
```

