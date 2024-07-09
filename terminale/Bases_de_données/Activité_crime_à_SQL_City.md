# Activité : Crime à SQL City

Nature : Branchée.

Matériel : Logiciel `DB Browser SQLite`.

Prérequis : [Systèmes de gestion de base de données relationnelles](./Systèmes_de_gestion_de_bases_de_données_relationnelles.md)

À faire : Seul.

## I. Objectif

L'objectif du jeu est de retrouver le criminel en interrogeant la base de données fournie par la police.

Vous savez que :

1. Le meurtre a été commis le quinze janvier 2018 à SQL City.

2. Le club de sport `Get Fit Now!` a un lien avec cette affaire.

## II. Installation

Télécharger le fichier [Crime_a_sql_city.db](./src/crime_a_sql_city.db) et l'ouvrir dans le logiciel `DB Browser SQLite`.

La base de données peut être représentée sous la forme du diagramme suivant :

<img src="./img/diagramme_sql_city.png" width=800>

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

________________

[Sommaire](./../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 