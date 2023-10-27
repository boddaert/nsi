# Modèle relationnel

## I. Introduction

Dans une bibliothèque, les usagers peuvent venir emprunter le livre qu'ils souhaitent lire ou venir rendre le livre qu'ils ont emprunté.

Lorsqu'un usager emprunte un livre, il faut que celui-ci soit retiré de la liste des livres empruntables. Et lorsqu'un usager rend un livre, il faut qu'il devienne à nouveau disponible.

Il faut donc au bibliothèquaire une solution lui permettant de conserver les informations d'emprunt et de rendu de livre de chacun des utilisateurs en temps réel.

Le bibliothèquaire a besoin d'un *système d'information*, c'est-à-dire d'un système informatique permettant de gérer de l'information.

Les informations à gérer sont les livres, les usagers et les processus d'emprunt et de rendu de livre.

Nous distinguons les livres de par leur ISBN, leur titre, leur auteur, leur année de publication, etc...

Nous distingons les usagers de par leur prénom, leur nom.

Puis nous distingons les processus d'emprunt de part un livre et l'usager qui l'a emprunté.

Cette démarche que nous venons de réaliser s'appelle une *modélisation*.

## II. Définitions

Une *donnée* est une information.

Un *modèle de données* est une représentation mathématique des données et des propriétés sur ces données.

Le *modèle relationnel* est un modèle de données dans lequel les données sont représentées par des entités.

### a) Entités

Une *entité* représente un objet ou une action du monde réel. Il est défini par un tuple de valeurs.

Par exemple, le livre Dune est représenté par l'entité suivante : $('Dune', 'Frank Herbert', '1965', 'Robert Laffont', '2-221-02602-0')$.

Toutes les entités d'un même type sont regroupés dans une relation.

### b) Relation

Une *relation* est un ensemble d'entités.

Par exemple, une relation $Livre$ est :

$$
Livre = \{ \newline('Dune', 'Frank Herbert', 1965, 'Robert Laffont', '2-221-02602-0'),\newline('1984', 'George Orwell', 1949, 'Gallimard', '2-07-036822-X'),\newline('Fondation', 'Isaac Asimov', 1957, 'Hachette', '2-6765-5668543-0') \newline\}
$$

Toutes les entités d'une relation obéissent au schéma relationnel de la relation.

### c) Schéma relationnel

Un *schéma relationnel* est un format dans lequel la relation doit se conformer pour entrer ses entités.

Un schéma relationnel est composé d'attributs.

Un *attribut* est un couple $(nom, domaine)$ où le domaine correspond au type de l'attribut.

Par exemple, les attributs de la relation $Livre$ sont :

| Nom | Domaine | Description |
| :---: | :---: | :---: |
| titre | `str` | Le titre du livre |
| auteur | `str` | L'auteur du livre |
| année | `int` | L'année de publication |
| editeur | `str` | La maison d'édition |
| isbn | `str` | Le numéro d'ISBN du livre |

La notation usuelle d'un schéma relationnel est plutôt : $Livre(titre : str, auteur : str, année : int, editeur : str, isbn : str)$.

## III. Contraintes d'intégrité







