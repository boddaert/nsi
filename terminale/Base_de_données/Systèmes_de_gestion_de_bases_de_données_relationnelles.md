# Systèmes de gestion de bases de données relationnelles

## I. Introduction

Notre bibliothèquaire, une fois après avoir finis la modélisation des données concernant les emprunts des livres de sa bibliothèque doit maintenant appliquer son système d'information en temps réel.

Par exemple, si un usager rend un livre, celui-ci doit être de nouveau apparaître comme étant disponible dans le système.

De la même façon que si un usager emprunte un livre, celui-ci doit disparaître de la liste des livres empruntables.

Outre le stockage des données, le système d'information doit garantir au bibliothèquaire d'ajouter de nouveaux livres ou de retirer ceux en mauvais état.

Cette fonctionnalité ne peut pas être réalisée par les usagers, il faut alors que le système d'information gère plusieurs niveaux d'accès aux données.

Enfin, si les données sont consultables depuis plusieurs ordinateurs, les données doivent être les mêmes partout.

Ces fonctionnalités peuvent être mises en pratique à l'aide d'un système de gestion de base de données.

## II. Définitions

Une *base de données* est un conteneur permettant de stocker physiquement les données et de retrouver des données.

Une *base de données relationnelles* est une base de données qui s'appuie sur le modèle relationnel.

Un *système de gestion de base de données relationnelles* (ou *SGBDR*) est un logiciel mettant en oeuvre le modèle relationnel.

Le langage *SQL* (pour *Select Query Language*) est un langage de requête sur les données.

## III. Bases de données relationnelles

La base de données relationnelle regroupe ses données sous forme de *tables de données*.

Par exemple, les entités de la relation $Livre$ sont représentées physiquement dans la table suivante :

| id_livre | titre | auteur | annee | editeur |
| :---: | :---: | :---: | :---: | :---: | 
| 1 | 'Dune' | 'Frank Herbert' | 1965 | 'Robert Laffont' |
| 2 | '1984' | 'George Orwell' | 1949 | 'Gallimard' |
| 3 | 'Fondation' | 'Isaac Asimov' | 1957 | 'Hachette' |
| 4 | 'Dune' | 'Frank Herbert' | 1965 | 'Robert Laffont' |

Nous remarquons que chaque *colonne* de la table est un attribut et chaque *ligne* est une entité.

Une base de données relationnelles est donc un ensemble de tables de données.

##### Application 1

Donner sur feuille, la table de la relation $Usager$.

## IV. Missions d'un SGBDR

### a) Récapitulatif

Le SGBDR permet de :

- Créer les bases de données.

- Créer les tables en spécifiant leurs schémas et leurs contraintes d'intégrité.

- Ajouter des données.

- Interroger les données.

- Mettre à jour ou supprimer des données.

- Assurer la sûreté et la perennité des données.

- Aassurer l'accès concurent aux données.

### b) Présentation du logiciel

Le SGBDR que nous utiliserons cette année est `DB Browser for SQLite`.

Il se présente de la façon suivante :

![Accueil](./img/DB_Browser_for_SQLite.png)

Plusieurs outils intéressants se présentent comme `Structure de la base de données`, `Parcourir les données` et `Exécuter le SQL`.

C'est sur ce dernier outil que nous allons écrire nos requêtes.

### c) Mission n°1 : Créer les bases de données

Sur `DB Browser for SQLite`, nous pouvons créer une base de donnée en cliquant sur `Nouvelle base de données`.

Les fichiers de base de données se terminent par l'extension `.db` pour *Data Base*.

##### Application 2

Créer, dans votre répertoire de travail, le fichier de base de données `bibliotheque.db`.

### d) Mission n°2 : Créer les tables en spécifiant leurs schémas et leurs contraintes d'intégrité.

En SQL, créer une table se fait selon la syntaxe suivante :

```sql
CREATE TABLE nom_table ( nom_attribut_1 DOMAINE CONTRAINTE,
                        nom_attribut_2 DOMAINE CONTRAINTE
);
```

Les domaines ou types de données en langage SQL sont :

| Domaine | Représentation |
| :---: | :---: |
| `INT` | Nombres entiers |
| `REAL` | Nombres flottants |
| `VARCHAR(n)` | Chaînes de caractère d'au plus $n$ caractères |
| `DATE` | Date au format `AAAA-MM-JJ` |

Si l'attribut ne possède pas de contrainte, il n'y a alors de spécification de contrainte.

La contrainte d'entité (clé primaire) se spécifie avec le mot-clé : `PRIMARY KEY`.

La contrainte de référence (clé étrangère) se spécifie avec la syntaxe `nom_attribut DOMAINE REFERENCES nom_table(clé_primaire)`.

Les contraintes utilisateur ne sont pas au programme de Terminale.

Par exemple, la requête SQL permettant de créer la table correspondant à la relation $Livre$ est :

```sql
CREATE TABLE Livre (id_livre INT PRIMARY KEY,
    titre VARCHAR(15),
    auteur VARCHAR(15),
    annee INT,
    editeur VARCHAR(15)
);
```

##### Application 3 

a) Recopier la requête SQL ci-dessus dans `DB Browser` dans l'onglet `Exécuter le SQL` puis sur `Exécuter la requête`.

b) Remarquer dans l'onglet `Structure de la base de données`, une nouvelle table est apparue puis vérifier dans les détails de la table si elle est correcte.

##### Application 4

Ecrire les requêtes SQL permettant de créer les tables correspondantes aux relations $Usager$ et $Emprunt$.

### e) Mission n°3 : Ajouter des données

Nous ajoutons des données dans la table selon la syntaxe suivante :

```sql
INSERT INTO nom_table VALUES (entité_1_valeur_1, entité_1_valeur_2),
    (entité_2_valeur_1, entité_2_valeur_2);
```

Par exemple, la requête SQL suivante permet d'ajouter à la table correspondant à la relation $Livre$ ses entités :

```sql
INSERT INTO Livre VALUES (1, 'Dune', 'Frank Herbert', 1965, 'Robert Laffont'),
    (2, '1984', 'George Orwell', 1949, 'Gallimard'),
    (3, 'Fondation', 'Isaac Asimov', 1957, 'Hachette'),
    (4, 'Dune', 'Frank Herbert', 1965, 'Robert Laffont')
```

##### Application 5

a) Recopier la requête SQL ci-dessus dans `DB Browser` dans l'onglet `Exécuter le SQL` puis sur `Exécuter la requête`.

b) Remarquer dans l'onglet `Parcourir les données`, les nouvelles données ajoutées suite à la requête.

##### Application 6

Ajouter aux tables `Usager` et `Emprunt` les entités trouvées à la leçon précédente.

### f) Mission n°4 : Interroger les données

L'interrogation de données consiste à l'écriture de requêtes SQL permettant de retrouver les données qui nous interesse.

#### 1. Sélections

La sélection de données consiste à n'obtenir que les données d'une ou plusieurs colonnes (attributs).

Elle s'effectue avec la syntaxe suivante :

```sql
SELECT attribut_1, attribut_2 FROM nom_table;
```

Par exemple, la requête SQL permettant d'obtenir tous les titres de livre contenus dans la table correspondant à la relation $Livre$ est :

```sql
SELECT titre from Livre;
```

##### Application 7

a) Ecrire la requête SQL permettant d'obtenir tous les prénoms des usagers.

b) Ecrire la requête SQL permettant d'obtenir tous les titres et les auteurs des livres.

#### 2. Projections

La projection de données consiste à n'obtenir que les données d'une ou plusieurs lignes (entités).

Elle s'effectue avec la syntaxe suivante :

```sql
SELECT * FROM nom_table WHERE attribut = valeur;
```

`*` signifie toutes les colonnes.

Par exemple, la requête SQL permettant d' obtenir toutes les lignes dont l'auteur est `Frank Herbert` depuis la table correspondant à la relation $Livre$ est :

```sql
SELECT * FROM Livre WHERE auteur = 'Frank Herbert';
```

##### Application 8

a) Ecrire la requête SQL permettant d'obtenir tous les livres dont le code est égale à $3$.

b) Ecrire la requête SQL permettant d'obtenir tous les livres dont l'année de publication est inférieure ou égale à $1960$.

#### 3. Sélection + projection

Il est possible de combiner une sélection avec une projection.

Par exemple, la requête SQL permettant d'obtenir les années de publication des livres dont l'auteur est Isaac Asimov s'écrit :

```sql
SELECT annee FROM Livre WHERE auteur = 'Isaac Asimov';
```

##### Application 9

a) Ecrire la requête SQL permettant d'obtenir l'identifiant du livre dont l'auteur est Isaac Asimov.

b) Ecrire la requête SQL permettant d'obtenir les éditeurs de livre dont le titre est 1984.

#### 4. Fonctions d'agrégation

Les *fonctions d'agrégation* sont des fonctions appliquées à l'ensemble des valeurs lors de la sélection.

| Fonction d'agrégation | Description |
| :---: | :---: |
| `COUNT()` | Compte le nombre de lignes. |
| `SUM()` | Réalise la somme des valeurs. |
| `AVG()` | Réalise la moyenne des valeurs. |
| `MIN()` | Renvoie l'élément le plus petit. |
| `MAX()` | Renvoie l'élément le plus grand. |

Les appels aux fonctions d'agrégation obéissent à la syntaxe suivante :

```sql
SELECT fonction_agrégation(attribut) FROM nom_table;
```

Par exemple, la requête SQL permettant d'obtenir l'année du livre publié en premier depuis la table correspondant à la relation $Livre$ est :

```sql
SELECT MIN(annee) FROM Livre;
```

##### Application 10

Ecrire la requête SQL permettant d'obtenir le nombre de livres contenus dans la table.

#### 5. Tris

#### 6. Jointures

### g) Mission n°5 : Mettre à jour ou supprimer des données

#### 1. Mettre à jour

La mise à jour de données s'effectue selon la syntaxe suivante :

```sql
UPDATE nom_table SET attribut_à_modifier = nouvelle_valeur WHERE condition
```
______________

[Feuille d'exercice](./Exercices/Exercices_systèmes_de_gestion_de_bases_de_données_relationnelles.md)