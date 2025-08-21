# Systèmes de gestion de bases de données relationnelles

## I. Introduction

Une fois après avoir finis la modélisation des données concernant les emprunts des livres de sa bibliothèque, le bibliothèquaire doit maintenant appliquer son système d'information en temps réel.

Par exemple, si un usager rend un livre, celui-ci doit être de nouveau apparaître comme étant de nouveau disponible dans le système.

De la même façon que si un usager emprunte un livre, celui-ci doit disparaître de la liste des livres empruntables.

Outre le stockage des données, le système d'information doit garantir au bibliothèquaire d'ajouter de nouveaux livres ou de retirer ceux en mauvais état.

Cette fonctionnalité ne doit pas être réalisée par les usagers, il faut alors que le système d'information gère plusieurs niveaux de droits/permissions d'accès aux données.

Enfin, si les données sont consultables depuis plusieurs ordinateurs, les données doivent être les mêmes partout.

Ces fonctionnalités peuvent être mises en pratique à l'aide d'un **système de gestion de base de données**.

## II. Définitions

> [!IMPORTANT]
> Une *base de données* est un conteneur permettant de stocker physiquement les données et de retrouver des données.

> [!IMPORTANT]
> Une *base de données relationnelles* est une base de données qui s'appuie sur le modèle relationnel.

> [!IMPORTANT]
> Un *système de gestion de base de données relationnelles* (ou *SGBDR*) est un logiciel mettant en oeuvre le modèle relationnel.

> [!IMPORTANT]
> Le langage *SQL* (pour *Structured Query Language*) est un langage de requête sur les données.

## III. Bases de données relationnelles

> [!IMPORTANT]
> La base de données relationnelle regroupe ses données sous forme de *tables de données*.

>[!TIP]
> Par exemple, les entités de la relation $Livre$ sont représentées physiquement dans la table suivante :
>
> | id_livre | titre | auteur | annee | editeur |
> | :---: | :---: | :---: | :---: | :---: | 
> | 1 | 'Dune' | 'Frank Herbert' | 1965 | 'Robert Laffont' |
> | 2 | '1984' | 'George Orwell' | 1949 | 'Gallimard' |
> | 3 | 'Fondation' | 'Isaac Asimov' | 1957 | 'Hachette' |
> | 4 | 'Dune' | 'Frank Herbert' | 1965 | 'Robert Laffont' |

> [!NOTE]
> Chaque *colonne* de la table est un attribut et chaque *ligne* est une entité.
>
> Une base de données relationnelles est donc un ensemble de tables de données.

#### <ins>Application 1</ins>

Donner sur feuille, la table de la relation $Usager$.

## IV. Missions d'un SGBDR

### a) Récapitulatif

> [!IMPORTANT]
> Le SGBDR permet de :
>
> - Créer les bases de données.
>
> - Créer les tables en spécifiant leurs schémas et leurs contraintes d'intégrité.
>
> - Ajouter des données.
>
> - Interroger les données.
>
> - Mettre à jour ou supprimer des données.
>
> - Assurer la sûreté et la perennité des données.
>
> - Assurer l'accès concurent aux données.

### b) Présentation du logiciel

Le SGBDR que nous utiliserons cette année est `DB Browser for SQLite`.

Il se présente de la façon suivante :

<img src="./img/DB_Browser_for_SQLite.png" width=800>

Plusieurs outils intéressants s'y trouvent comme `Structure de la base de données`, `Parcourir les données` et `Exécuter le SQL`.

C'est sur ce dernier outil que nous allons écrire nos requêtes.

### c) Mission n°1 : Créer les bases de données

Sur `DB Browser for SQLite`, nous pouvons créer une base de donnée en cliquant sur `Nouvelle base de données`.

> [!NOTE]
> Les fichiers de base de données se terminent par l'extension `.db` pour *Data Base*.

#### <ins>Application 2</ins>

Créer, dans votre répertoire de travail, le fichier de base de données `test_bibliotheque.db`.

### d) Mission n°2 : Créer les tables en spécifiant leurs schémas et leurs contraintes d'intégrité.

En SQL, créer une table se fait selon la syntaxe suivante :

```
CREATE TABLE <nom_table> ( <nom_attribut_1> DOMAINE,
                        <nom_attribut_2> DOMAINE
);
```

Les domaines ou types de données en langage SQL sont :

| Domaine | Représentation |
| :---: | :---: |
| `INT` | Nombres entiers |
| `REAL` | Nombres flottants |
| `VARCHAR(n)` | Chaînes de caractère d'au plus $n$ caractères |
| `DATE` | Date au format `AAAA-MM-JJ` |

La contrainte d'entité (clé primaire) se spécifie avec le mot-clé `PRIMARY KEY` : 
```
<nom_attribut_clé_primaire> DOMAINE PRIMARY KEY
```

La contrainte de référence (clé étrangère faisant référence à une clé primaire d'une autre table) se spécifie avec la syntaxe :
```
<nom_attribut_clé_étrangère> DOMAINE REFERENCES <nom_table>(<nom_attribut_clé_primaire>)
```

Les contraintes utilisateur ne sont pas au programme de Terminale.

> [!TIP]
> Par exemple, la requête SQL permettant de créer la table correspondant à la relation $Livre$ est :
>
> ```sql
> CREATE TABLE Livre (id_livre INT PRIMARY KEY,
>     titre VARCHAR(15),
>     auteur VARCHAR(15),
>     annee INT,
>     editeur VARCHAR(15)
> );
> ```

#### <ins>Application 3</ins>

a) Recopier la requête SQL ci-dessus dans `DB Browser` dans l'onglet `Exécuter le SQL` puis exécuter la requête.

b) Vérifier dans l'onglet `Structure de la base de données` l'apparition de la nouvelle table `Livre` et ses informations.

#### <ins>Application 4</ins>

Écrire les requêtes SQL permettant de créer les tables correspondantes aux relations $Usager$ et $Emprunt$.

### e) Mission n°3 : Ajouter des données

Nous ajoutons des données dans la table selon la syntaxe suivante :

```
INSERT INTO <nom_table> VALUES (<entité_1_valeur_1>, <entité_1_valeur_2>),
    (<entité_2_valeur_1>, <entité_2_valeur_2>);
```

> [!TIP]
> Par exemple, la requête SQL suivante permet d'ajouter à la table `Livre` ses entités :
>
> ```sql
> INSERT INTO Livre VALUES (1, 'Dune', 'Frank Herbert', 1965, 'Robert Laffont'),
>     (2, '1984', 'George Orwell', 1949, 'Gallimard'),
>     (3, 'Fondation', 'Isaac Asimov', 1957, 'Hachette'),
>     (4, 'Dune', 'Frank Herbert', 1965, 'Robert Laffont');
> ```

#### <ins>Application 5</ins>

a) Recopier la requête SQL ci-dessus dans `DB Browser` dans l'onglet `Exécuter le SQL` puis exécuter la requête.

b) Vérifier dans l'onglet `Parcourir les données` les nouvelles données ajoutées suite à la requête.

#### <ins>Application 6</ins>

Ajouter aux tables `Usager` et `Emprunt` au moins trois entités chacune.

### f) Mission n°4 : Interroger les données

L'interrogation de données consiste à l'écriture de requêtes SQL permettant de retrouver les données qui nous interesse.

#### 1. Sélections

> [!IMPORTANT]
> La *sélection* de données consiste à n'obtenir que les données d'une ou plusieurs colonnes (attributs).

Elle s'effectue avec la syntaxe suivante :

```
SELECT <nom_attribut_1>, <nom_attribut_2> FROM <nom_table>;
```

> [!TIP]
> Par exemple, la requête SQL permettant d'obtenir tous les titres et auteurs de livre contenus dans la table `Livre` est :
>
> ```sql
> SELECT titre, auteur from Livre;
> ```

#### <ins>Application 7</ins>

a) Écrire la requête SQL permettant d'obtenir tous les prénoms des usagers.

b) Écrire la requête SQL permettant d'obtenir tous les dates des emprunts.

#### 2. Projections

> [!IMPORTANT]
> La *projection* de données consiste à n'obtenir que les données d'une ou plusieurs lignes (entités).

Elle s'effectue avec la syntaxe suivante :

```
SELECT * FROM <nom_table> WHERE <condition>;
```

> `*` signifie toutes les colonnes.

> [!TIP]
> Par exemple, la requête SQL permettant d' obtenir toutes les lignes dont l'auteur est `Frank Herbert` depuis la table `Livre` est :
>
> ```sql
> SELECT * FROM Livre WHERE auteur = 'Frank Herbert';
> ```

#### <ins>Application 8</ins>

a) Écrire la requête SQL permettant d'obtenir tous les livres dont l'identifiant est égale à $3$.

b) Écrire la requête SQL permettant d'obtenir tous les livres dont l'année de publication est inférieure ou égale à $1960$.

#### 3. Sélection + projection

Il est possible de combiner une sélection avec une projection.

> [!TIP]
> Par exemple, la requête SQL permettant d'obtenir les années de publication des livres dont l'auteur est Isaac Asimov s'écrit :
>
> ```sql
> SELECT annee FROM Livre WHERE auteur = 'Isaac Asimov';
> ```

#### <ins>Application 9</ins>

a) Écrire la requête SQL permettant d'obtenir l'identifiant du livre dont l'auteur est Isaac Asimov.

b) Écrire la requête SQL permettant d'obtenir les éditeurs de livre dont le titre est 1984.

#### 4. Fonctions d'agrégation

> [!IMPORTANT]
> Les *fonctions d'agrégation* sont des fonctions appliquées à l'ensemble des valeurs lors de la sélection.

| Fonction d'agrégation | Description |
| :---: | :---: |
| `COUNT()` | Compte le nombre de lignes. |
| `SUM()` | Réalise la somme des valeurs. |
| `AVG()` | Réalise la moyenne des valeurs. |
| `MIN()` | Renvoie l'élément le plus petit. |
| `MAX()` | Renvoie l'élément le plus grand. |

Les appels aux fonctions d'agrégation obéissent à la syntaxe suivante :

```
SELECT <fonction_agrégation>(<nom_attribut>) FROM <nom_table>;
```

> [!TIP]
> Par exemple, la requête SQL permettant d'obtenir l'année du livre publié en premier depuis la table `Livre` est :
>
> ```sql
> SELECT MIN(annee) AS premiere_annee FROM Livre;
> ```

> `AS` permet de renommer un attribut dans le résultat à la requête.

#### <ins>Application 10</ins>

Écrire la requête SQL permettant d'obtenir le nombre de livres contenus dans la table.

#### 5. Tris

Ajouter `ORDER BY attribut` suivi de `ASC` (par ordre croissant) ou de `DESC` (par ordre décroissant) permet d'afficher les résultats triés selon une relation d'ordre donnée.

> [!TIP]
> Par exemple, la requête ci-dessous affiche tous les titres de livre par ordre croissant de titre :
>
> ```sql
> SELECT titre FROM Livre ORDER BY titre ASC;
> ```

#### <ins>Application 11</ins>

Écrire la requête SQL permettant d'obtenir tous les usagers par ordre décroissant de prénom.

#### 6. Jointures

Dans la table correspondant à la relation $Emprunt$ y figure uniquement les identifiants des livres et des usagers, mais comment obtenir par exemple le titre d'un livre emprunté ?

> [!IMPORTANT]
> La *jointure* entre deux tables dans une requête SQL permet de fusionner les données pour les interroger efficacement.

La jointure s'effectue à l'aide des clés primaires et des clés étrangères.

Sa syntaxe est la suivante :

```
SELECT <nom_attribut> FROM <nom_table_1> JOIN <nom_table_2> ON <clé_table_1> = <clé_table_2>;
```

> [!TIP]
> Par exemple, il nous faut joindre les tables `Livre` et `Emprunt` si nous voulons obtenir les titres des livres qui sont empruntés :
>
> ```sql
> SELECT Livre.titre FROM Livre JOIN Emprunt ON Livre.id_livre = Emprunt.id_livre;
> ```

#### <ins>Application 12</ins>

a) Écrire la requête SQL permettant d'obtenir tous les auteurs dont les livres sont empruntés.

b) Écrire la requête SQL permettant d'obtenir les prénoms et les noms des usagers qui ont empruntés un livre.

### g) Mission n°5 : Mettre à jour ou supprimer des données

#### 1. Mettre à jour

La mise à jour de données s'effectue selon la syntaxe suivante :

```
UPDATE <nom_table> SET <nom_attribut> = <nouvelle_valeur> WHERE <condition>;
```

> [!TIP]
> Par exemple, la requête permettant de mettre à jour la date de publication en 1970 des livres dont l'auteur est Isaac Asimov est :
>
> ```sql
> UPDATE Livre SET annee = 1970 WHERE auteur = 'Isaac Asimov';
> ```

#### <ins>Application 13</ins>

a) Recopier la requête SQL ci-dessus dans `DB Browser` dans l'onglet `Exécuter le SQL` puis exécuter la requête.

b) Vérifier dans l'onglet `Parcourir les données` que la mise à jour a bien été effectuée.

#### 2. Supprimer des données

La suppression de données s'effectue selon la syntaxe suivante :

```
DELETE FROM <nom_table> WHERE <condition>;
```

> [!TIP]
> Par exemple, la requête SQL permettant de supprimer les livres dont l'auteur est Isaac Asimov est :
>
> ```sql
> DELETE FROM Livre WHERE auteur = 'Isaac Asimov';
> ```

> [!WARNING]
> Avant de supprimer une ligne, il est nécessaire de vérifier au préalable si la clé primaire de ce livre n'existe pas dans une autre table. Si c'est le cas, il faut également supprimer cette ligne.

#### <ins>Application 14</ins>

a) Recopier la requête SQL ci-dessus dans `DB Browser` dans l'onglet `Exécuter le SQL` puis exécuter la requête. Si une erreur survient, vérifier si le livre n'existe pas dans une autre table.

b) Vérifier le résultat dans l'onglet `Parcourir les données`.

### h) Mission n°6 : Assurer la sécurité et la perennité des données

En cas de problème matériel, c'est-à-dire lors d'une coupure courant ou la présence d'un défaut sur un disque dur, le SGBDR doit permettre de mettre en sécurité les données pour que celles-ci soient récupérables.

Le SGBDR gère également les accès sécurisés aux données, un utilisateur qui ne possède pas les droits de mise à jour ou de suppression ne doit pas pouvoir effectuer des requêtes de ce type sur les données.

### i) Mission n°7 : Assurer l'accès concurent aux données

Lee SGBDR doit permettre l'accès aux données de plusieurs utilisateurs en même temps. Par conséquent, il doit vérifier que deux requêtes, par exemple de mise à jour ou de suppression, n'interfèrent pas entre elles.

______________

[Exercices](./Exercices/Exercices_systèmes_de_gestion_de_bases_de_données_relationnelles.md)

________________

[Sommaire](./../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 