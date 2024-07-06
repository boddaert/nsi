# Recherche dans une table

## I. Définitions

Une fois les données chargées et validées, il devient possible d'exploiter ces données afin de vérifier la présence de certaine donnée, d'extraire des données cibles ou encore d'en faire des statistiques.

Ces opérations sont appelées *requêtes*.

> [!IMPORTANT]
> La *requête de projection* est une requête qui consiste à récupérer, sur chaque enregistrement, toutes les valeurs d'un attribut donné.

> [!TIP]
> Par exemple :
>
> | Sexe | Prénom | Année de naissance |
> | :---: | :---: | :---: |
> | M | Alphonse | 1932 |
> | F | Béatrice | 1964 |
> | F | Charlotte | 1988 |
>
> Avec la table `personnes` ci-dessus, la projection des valeurs de l'attribut `"Année de naissance"` est :
>
> | Année de naissance |
> | :---: |
> | 1932 |
> | 1964 |
> | 1988 |

> [!IMPORTANT]
> La *requête de sélection* est une requête qui consiste à récupérer tous les enregistrements contenant une valeur donnée.

> [!TIP]
> Par exemple :
> Par exemple :
> Avec la table `personnes` ci-dessus, la sélection des enregistrements en fonction de la valeur `"F"` pour l'attribut `Sexe` est :
>
> | Sexe | Prénom | Année de naissance |
> | :---: | :---: | :---: |
> | F | Béatrice | 1964 |
> | F | Charlotte | 1988 |


> [!IMPORTANT]
> Une *requête de recherche* est la combinaison d'une requête de projection et de sélection.

> [!TIP]
> Par exemple :
> Avec la table `personnes` ci-dessus, la requête de recherche des années de naissances pour les femmes est :
>
> | Année de naissance |
> | :---: |
> | 1964 |
> | 1988 |

## II. Algorithmes de requête de recherche

### a) Algorithme de requête de projection

```
Algorithme : projection(table_de_données, attribut)
Entrées : table_de_données une liste de dictionnaires et attribut le nom de l'attribut
Sortie : Une nouvelle table de données

table_de_résultats <- ∅
Pour chaque enregistrement de table_de_données, faire :
    Ajouter à table_de_resultats : enregistrement[attribut]
Renvoyer table_de_résultats
```

#### <ins>Application 1</ins>

a) Écrire une fonction `projection(table_de_données : list, attribut : str)->list` correspondant à l'algorithme de projection ci-dessus.

b) Exécuter la fonction `projection()` avec les bons arguments afin d'obtenir les années de naissance des personnes présentes dans le fichier `personnes.csv`.

### b) Algorithme de requête de sélection

```
Algorithme : sélection(table_de_données, attribut, valeur)
Entrées : table_de_données une liste de dictionnaires, attribut le nom de l'attribut et valeur la valeur
Sortie : Une nouvelle table de données

table_de_résultats <- ∅
Pour chaque enregistrement de table_de_données, faire :
    Si enregistrement[attribut] = valeur, alors
        Ajouter à table_de_resultats : enregistrement
Renvoyer table_de_résultats
```

#### <ins>Application 2</ins>

a) Écrire une fonction `selection(table_de_données : list, attribut : str, valeur : str)->list` correspondant à l'algorithme de sélection ci-dessus.

b) Exécuter la fonction `selection()` avec les bons arguments afin d'obtenir les enregistrements des personnes de sexe féminin présentes dans le fichier `personnes.csv`.

### c) Algorithme de requête de recherche

```
Algorithme : recherche(table_de_données, attribut_projection, attribut_sélection, valeur_sélection)
Entrées : table_de_données une liste de dictionnaires, attribut_projection le nom de l'attribut de la projection, attribut_sélection le nom de l'attribut de sélection et valeur la valeur
Sortie : Une nouvelle table de données

Renvoyer projection(sélection(table_de_données, attribut_sélection, valeur_sélection), attribut_projection)
```

#### <ins>Application 3</ins>

a) Écrire une fonction `recherche(table_de_données : list, attribut_projection : str, attribut_selection : str, valeur : str)->list` correspondant à l'algorithme de recherche ci-dessus.

b) Exécuter la fonction `recherche()` avec les bons arguments afin d'obtenir les années de naissance des personnes de sexe féminin présentes dans le fichier `personnes.csv`.

## III. Fonctions d'agrégation

> [!IMPORTANT]
> Les fonctions d'*agrégation* est une opération supplémentaire afin d'obtenir des informations précises comme le nombre d'occurences de la recherche ou la moyenne des résultats.

### a) Algorithme d'occurences

La fonction d'agrégation d'occurences permet d'obtenir le nombre de lignes d'une sélection.

```
Algorithme : occurences(table_de_données, attribut, valeur)
Entrées : table_de_données une liste de dictionnaires, attribut le nom de l'attribut et valeur la valeur
Sortie : Un entier

Renvoyer taille(sélection(table_de_données, attribut, valeur))
```

#### <ins>Application 4</ins>

a) Écrire une fonction `occurences(table_de_données : list, attribut : str, valeur : str)->list` correspondant à l'algorithme d'occurences ci-dessus.

b) Exécuter la fonction `occurences()` avec les bons arguments afin d'obtenir le nombre de personnes de sexe féminin présentes dans le fichier `personnes.csv`.

### b) Algorithme de moyenne

La fonction de moyenne permet d'obtenir la moyenne des valeurs suite à une projection sur un attribut.

```
Algorithme : moyenne(table_de_données, attribut)
Entrées : table_de_données une liste de dictionnaires, attribut le nom de l'attribut et valeur la valeur
Sortie : Un flottant

table_de_résultats = projection(table_de_données, attribut)
Renvoyer somme(table_de_résultats)/taille(table_de_résultats)
```

#### <ins>Application 5</ins>

a) Écrire une fonction `moyenne(table_de_données : list, attribut : str)->list` correspondant à l'algorithme de moyenne ci-dessus.

b) Exécuter la fonction `moyenne()` avec les bons arguments afin d'obtenir la moyenne des années de naissance des personnes présentes dans le fichier `personnes.csv`.

__________

[Exercices](./Exercices/Exercices_recherche_dans_une_table.md)

__________

[Sommaire](./../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 