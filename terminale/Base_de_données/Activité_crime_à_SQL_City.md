# Activité : Crime à SQL City

Nature : Branchée

Matériel : Logiciel `DB Browser SQLite`

Prérequis : Langage SQL

Sources : [https://mystery.knightlab.com/](https://mystery.knightlab.com/)

## I. Objectif

L'objectif du jeu est de retrouver le criminel en interrogeant la base de données fournie par la police.

Vous savez que :

- Le meurtre a été commis le quinze janvier 2018 à SQL City.

- Le club de sport `Get Fit Now!` a un lien avec cette affaire.

## II. Installation

Télécharger le fichier [Crime_a_sql_city.db](./src/crime_a_sql_city.db) et l'ouvrir dans le logiciel `DB Browser SQLite`.

La base de données peut être représentée sous la forme du diagramme suivant :

![Diagramme_sql_city](./img/diagramme_sql_city.png)

## III. Règles du jeu

Sur `DB Browser`, entrer les requêtes SQL afin d'enquêter et de trouver le coupable du crime.

Une fois l'assassin identifié, entrer la réponse dans la table $solution$ comme ci-dessous :

```sql
INSERT INTO solution VALUES (1, 'nom_du_suspect');
```

Puis pour vérifier le résultat :

```sql
SELECT value FROM solution;
```

## IV. Travail à faire

Vous devez rédiger un rapport d'enquête afin de prouver l'identité du coupable.

Pour cela, vous écrirez toutes les requêtes (ainsi que la ou les réponses permettant de faire les liens entre vos hypothèses) permettant de remonter jusqu'à votre conclusion.
________________

[Sommaire](./../README.md)