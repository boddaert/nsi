# Fusion de tables

## I. Définitions

La *fusion* de deux tables est la réunion des données de ces deux tables pour n'en former plus qu'une.

Selon la forme ce ces tables, la fusion peut être semblable à une simple concaténation des données ou à la jointure en fonction d'un attribut unique de ces deux tables.

Fusionner deux tables n'a de sens que si les données contenues dans ces tables sont liées.

## II. Concaténation de deux tables

### a) Principe

La *concaténation de deux tables* consiste à concaténer les données de deux tables. Elle n'est possible que si les deux tables ont exactement les mêmes attributs.

Par exemple, la concaténation de la table suivante :

| Sexe | Prénom | Année de naissance |
| :---: | :---: | :---: |
| M | Alphonse | 1932 |
| F | Béatrice | 1964 |
| F | Charlotte | 1988 |

Avec celle-ci :

| Sexe | Prénom | Année de naissance |
| :---: | :---: | :---: |
| M | David | 1955 |
| M | Emanuel | 1992 |
| F | Florentine | 1973 |

Donne :

| Sexe | Prénom | Année de naissance |
| :---: | :---: | :---: |
| M | Alphonse | 1932 |
| F | Béatrice | 1964 |
| F | Charlotte | 1988 |
| M | David | 1932 |
| M | Emanuel | 1992 |
| F | Florentine | 1973 |

### b) Algorithme de concaténation

L'algorithme de concanténation de deux listes s'effectue très facilement avec l'opérateur `+`.

Il serait néanmoins judicieux de vérifier au préalable si les tables de données possèdent les mêmes attributs :

```
Algorithme : concaténation(table_1, table_2)
Entrées : table_1 une liste de dictionnaires et tabl_2 une liste de dictionnaires.
Sortie : Une liste correspondant à la concaténation de table_1 et table_2

table_fusionnée <- ∅
liste_clés_table_1 <- ∅
liste_clés_table_2 <- ∅
mêmes_clés <- Vrai

Pour chaque clé de table_1[0], faire :
    Ajouter clé à liste_clés_table_1
Pour chaque clé de table_2[0], faire :
    Ajouter clé à liste_clés_table_2

Pour chaque clé de liste_clés_table_1, faire :
    Si clé n'est pas présent dans liste_clés_table_2, alors :
        mêmes_clés <- Faux

Si taille(liste_clés_table_1) = taille(liste_clés_table_2) et si mêmes_clés = Vrai, alors :
    table_fusionée <- table_1 + table_2

Renvoyer table_fusionée
```

##### Application 1

a) Écrire la fonction `concaténation()` correspondant à l'algorithme de concaténation ci-dessus.

b) Vérifier votre fonction en fusionnant les deux tables données en exemple.

## III. Opération de jointure

### a) Principe

L'*opération de jointure entre deux tables* consiste à réaliser le produit cartésien des données pésentes dans ces deux tables.

Elle n'est possible que si les deux tables ont des valeurs communes pour un même attribut unique.

Par exemple, l'opération de jointure de la table suivante :

| Sexe | Prénom | Année de naissance |
| :---: | :---: | :---: |
| M | Alphonse | 1932 |
| F | Béatrice | 1964 |
| F | Charlotte | 1988 |

Avec celle-ci sur l'attribut `Prénom` :

| Prénom | Lieu d'habitation |
| :---: | :---: |
| Alphonse | Paris |
| Béatrice | Lille |
| David | Lyon |
| Florentine | Strasbourg |

Donne :

| Sexe | Prénom | Année de naissance | Lieu d'habitation |
| :---: | :---: | :---: | :---: |
| M | Alphonse | 1932 | Paris |
| F | Béatrice | 1964 | Lille |

### b) Algorithme de jointure

L'algorithme de jointure s'écrit en utilisant une double boucle. Nous considérerons que toutes les valeurs de l'attribut sur lequel la jointure s'effectue sont uniques.

```
Algorithme : jointure(table_1, table_2, attribut)
Entrées : table_1 une liste de dictionnaires, table_2 une liste de dictionnaires et attribut un attribut
Sortie : Une liste de dictionnaires correspondant à la jointure de table_1 et table_2

table_fusionnée <- ∅
Pour chaque enregistrement_1 de table_1, faire :
    Pour chaque enregistrement_2 de table_2, faire :
        Si enregistrement_1[attribut] = enregistrement_2[attribut], alors :
            nouvel_enregistrement <- ∅
            Pour chaque clé de enregistrement_1, faire :
                Ajouter à nouvel_enregistrement enregistrement_1[clé]
            Pour chaque clé de enregistrement_2, faire :
                Ajouter à nouvel_enregistrement enregistrement_2[clé]
            Ajouter à table_fusionnée nouvel_enregistrement
Renvoyer table_fusionnée
```

##### Application 2

a) Écrire la fonction `jointure()` correspondant à l'algorithme de jointure ci-dessus.

b) Vérifier votre fonction en fusionnant les deux tables données en exemple.

____________

[Sommaire](./../README.md)
