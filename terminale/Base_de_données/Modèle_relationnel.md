# Modèle relationnel

## I. Introduction

Dans une bibliothèque, les usagers peuvent venir emprunter le livre qu'ils souhaitent lire ou venir rendre le livre qu'ils ont emprunté.

Un livre emprunté par un usager n'est plus disponible.

Les livres vont et viennent et le bibliothèquaire souhaite savoir quels sont les livres disponibles et quel usager emprunte quel livre.

Le bibliothèquaire souhaite enregistrer toutes ces informations informatiquement.

Il va utiliser pour cela : un *système d'information*.

Pour l'exploiter, le bibliothèquaire doit nécessairement modéliser ses données.

Les informations à gérer sont :

- Les livres.

- Les usagers.

- Les processus d'emprunt de livre.

Un livre possède comme caractéristique un ISBN, un titre, un auteur, une année de publication, etc...

Un usager possède comme caractéristique un prénom, un nom.

Un processus d'emprunt se définit par le livre emprunté, l'usager qui l'a emprunté et la date de l'emprunt.

La démarche que nous venons de réaliser s'appelle une *modélisation*.

## II. Définitions

Une *donnée* est une information.

Un *modèle de données* est une représentation mathématique des données et des propriétés sur ces données.

Le *modèle relationnel* est un modèle de données dans lequel les données sont représentées par des entités.

### a) Entités

Une *entité* représente un objet ou une action du monde réel. Il est défini par un tuple de valeurs.

Par exemple, le livre Dune est représenté par l'entité suivante : 

```
('Dune', 'Frank Herbert', 1965, 'Robert Laffont').
```

Toutes les entités d'un même type sont regroupés dans une relation.

### b) Relation

Une *relation* est un ensemble d'entités.

Par exemple, une relation $Livre$ est :

```
Livre = { 
    ('Dune', 'Frank Herbert', 1965, 'Robert Laffont'),
    ('1984', 'George Orwell', 1949, 'Gallimard'),
    ('Fondation', 'Isaac Asimov', 1957, 'Hachette')
}
```

Toutes les entités d'une relation obéissent au schéma relationnel de la relation.

### c) Schéma relationnel

Un *schéma relationnel* est un format dans lequel la relation doit se conformer pour entrer ses entités.

Un schéma relationnel est composé d'attributs.

Un *attribut* est un couple $(nom, domaine)$ où le domaine correspond au type de l'attribut.

Par exemple, les attributs de la relation $Livre$ sont :

- (titre, `VARCHAR`)

- (auteur, `VARCHAR`)

- (annee, `INT`)

- (editeur, `VARCHAR`)

Le schéma relationnel de la relation $Livre$ est :

$Livre(titre : VARCHAR, auteur : VARCHAR, annee : INT, editeur : VARCHAR, isbn : VARCHAR)$.

##### Application 1

Donner les attributs que l'on pourrait avoir dans la relation $Usager$.

##### Application 2

Donner le schéma relationnel de la relation $Usager$ en supposant qu'un usager possède uniquement un prénom et un nom.

##### Application 3

En respectant le schéma relationnel donné à la question précédente, donner au moins trois entités à la relation $Usager$.

## III. Contraintes d'intégrité

Une *contrainte d'intégrité* est une propriété du modèle de données vérifiée à tout instant et qui permet d'assurer la cohérence des données.

Nous distinguons quatre contraintes d'intégrité dans le modèle relationnel.

### a) Contrainte de domaine

La *contrainte de domaine* concerne le type de l'attribut.

En effet, tous les types des valeurs d'une entité doivent correspondre au domaine donné par le schéma de la relation.

##### Application 4

Vérifier puis expliquer pourquoi la contrainte de domaine est respectée (ou pas) pour chaque entité dans la relation $Livre$.

### b) Contrainte d'entité

La *contrainte d'entité* permet de s'assurer que chaque entité d'une relation est unique.

Il n'est pas impossible qu'il y ait deux fois le même ouvrage dans une bibliothèque, pourtant il s'agit bien de deux entités distinctes.

Pour les différencier, nous ajoutons au schéma relationnel un nouvel attribut appelé *clé primaire* :

$Livre(\underline{id\textunderscore livre} : INT, titre : VARCHAR, auteur : VARCHAR, annee : INT, editeur : VARCHAR)$.

Nous notons usuellement la clé primaire en souligné dans le schéma relationnel.

Ici, l'attribut $\underline{id\textunderscore livre}$ est un entier qui sera unique pour chaque entité.

Ainsi, même s'il s'agit de la même oeuvre, le livre est unique dans la bibliothèque parce que leur identifiant est différent.

##### Application 5

a) Modifier en conséquence le contenu de la relation $Livre$.

b) Ajouter dans la relation $Livre$ un second ouvrage de `Dune` mais par conséquent, avec un identifiant différent.

##### Application 6

a) Ajouter une clé primaire au schéma relationnel de la relation $Usager$ pour que chaque usager soit unique.

b) Modifier en conséquence les entités de la relation $Usager$.

### c) Contrainte de référence

La *contrainte de référence* permet de s'assurer qu'une relation mentionne des entités existantes dans d'autres relations.

Par exemple, la relation $Emprunt$ mentionne une entité de la relation $Livre$ et une entité de la relation $Usager$. 

Or, pour éviter que la relation $Emprunt$ mentionne des livres ou des usagers inexistants, nous ajoutons à la relation $Emprunt$ les clés étrangères adéquates.

Une *clé étrangère* est une référence vers une entité unique d'une autre relation.

Pour s'assurer qu'il s'agit d'une référence vers une entité unique, la clé étrangère correspond alors à la clé primaire de l'entité auquel elle fait référence.

Ansi, le schéma relationnel de la relation $Emprunt$ est :

$Emprunt(\\#id\textunderscore livre : VARCHAR, \\#id\textunderscore usager : INT, date : DATE)$

Nous notons usuellement les clé étrangères précédées d'un dièse.

##### Application 7

A quelle clé primaire la clé étrangère $\\#id\textunderscore livre$ de la relation $Emprunt$ fait-elle référence ?

##### Application 8

Imaginons qu'une entité de la relation $Usager$ ait emprunté le livre d'identifiant $1$ à la date d'aujourd'hui.

Ajouter en conséquence l'entité dans la relation $Emprunt$.

### d) Contrainte utilisateur

Les *contraintes utilisateur* sont toutes les contraintes qui ne concernent pas les trois précédentes contraintes d'intégrité.

Un exemple de contrainte utilisateur est que l'âge d'un usager ne peut pas être $200$ ou que l'adresse mail d'un usager doit comporter un arobase dans sa chaîne de caractère.

##### Application 9

Trouver une contrainte utilisateur que nous pourrions ajouter à la relation $Emprunt$.
______________

[Feuille d'exercice](./Exercices/Exercices_modèle_relationnel.md)

______________

[Sommaire](./../README.md)
