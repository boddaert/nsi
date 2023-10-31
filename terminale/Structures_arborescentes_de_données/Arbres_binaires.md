# Arbres binaires

## I. Définitions

Une *structure arborescente de données* est une structure dans laquelle chaque élément possède un parent (sauf le premier). 

Un *arbre* est une structure de données arborescente dont chaque élément est appelé *noeud*.

Est appelé la *racine*, le noeud qui n'a pas de parent.

Sont appelés *feuilles*, les noeuds qui n'ont pas d'enfants.

Un *arbre binaire* est un arbre dont tous les noeuds possèdent au plus deux enfants.

## II. Type abstrait

### a) Définition d'un arbre binaire

Un arbre binaire est soit :

- Un arbre vide.
- Un triplé constitué :
    + D'un noeud.
    + D'un sous-arbre gauche.
    + D'un sous-arbre droit.

Nous remarquons qu'il s'agit d'une définition récursive : les ous-arbres gauches et droits étant eux aussi des arbres.

### b) Notation

Nous notons les arbres entre parenthèses sous la forme : $(Noeud, SAG, SAD)$.

L'arbre vide se note $\emptyset$.

Ainsi, un arbre consitué que d'une racine $3$ se note : $(3, \emptyset, \emptyset)$.

Et l'arbre constitué d'une racine $3$ et de deux sous-arbres dont la racine du sous-arbre gauche est $5$ et la racine du sous-arbre droit est $8$ se note : $(3, (5, \emptyset, \emptyset), (8, \emptyset, \emptyset))$.

### c) Représentation schématisée

Un arbre binaire est souvent représenté sous la forme d'un schéma :

```mermaid
flowchart TB
    A((3))
    B((5))
    C((8))
    D(())
    E(())
    F(())
    G(())
    A --> B
    B --> D
    B --> E
    A --> C
    C --> F
    C --> G
```

$A$, $B$ et $C$ sont les noeuds de l'arbre.

$A$ est la racine de l'arbre.

