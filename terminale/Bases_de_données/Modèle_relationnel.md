# Modèle relationnel

## I. Définitions

> [!IMPORTANT]
> Une *donnée* est une information.

> [!IMPORTANT]
> Un *modèle de données* est une représentation mathématique des données et des propriétés sur ces données.

> [!IMPORTANT]
> Le *modèle relationnel* est un modèle de données dans lequel les données sont représentées par des relations.

### a) Entités

> [!IMPORTANT]
> Une *entité* représente un objet ou une action du monde réel. Il est défini par un tuple de valeurs.

> [!TIP]
> Par exemple :
>
> Un livre possède comme caractéristique un titre, un auteur, une année de publication, etc...
>
> Le livre Dune est représenté par l'entité suivante : 
>
> ```
> ('Dune', 'Frank Herbert', 1965, 'Robert Laffont').
> ```

> [!WARNING]
> Toutes les entités d'un même type sont regroupés dans une relation.

### b) Relation

> [!IMPORTANT]
> Une *relation* est un ensemble d'entités.

> [!TIP]
> Par exemple :
> Une relation $Livre$ est :
>
> ```
> Livre = { 
>     ('Dune', 'Frank Herbert', 1965, 'Robert Laffont'),
>     ('1984', 'George Orwell', 1949, 'Gallimard'),
>     ('Fondation', 'Isaac Asimov', 1957, 'Hachette')
> }
> ```

> [!WARNING]
> Toutes les entités d'une relation obéissent au schéma relationnel de la relation.

### c) Schéma relationnel

> [!IMPORTANT]
> Un *schéma relationnel* est une définition des attributs des entités composant la relation.

> [!IMPORTANT]
> Un *attribut* est un couple $(nom, domaine)$ où le domaine correspond au type de l'attribut.

> [!TIP]
> Par exemple :
>
> Les attributs de la relation $Livre$ sont :
>
> - ($titre$, `VARCHAR`)
>
> - ($auteur$, `VARCHAR`)
> 
> - ($annee$, `INT`)
>
> - ($editeur$, `VARCHAR`)
>
> Le schéma relationnel de la relation $Livre$ est :
>
> $Livre(titre : VARCHAR, auteur : VARCHAR, annee : INT, editeur : VARCHAR)$.

#### <ins>Application 1</ins>

Un usager est une personne empruntant un livre à la bibliothèque.

a) Proposer une liste d'attributs propres à un usager.

b) Donner le schéma relationnel de la relation $Usager$.

c) Donner au moins trois exemples d'entités pour la relation $Usager$.

## II. Contraintes d'intégrité

> [!IMPORTANT]
> Une *contrainte d'intégrité* est une propriété du modèle de données vérifiée à tout instant et qui permet d'assurer la cohérence des données.

Nous distinguons **quatre contraintes d'intégrité** dans le modèle relationnel.

### a) Contrainte de domaine

> [!IMPORTANT]
> La *contrainte de domaine* concerne le type de l'attribut.

En effet, tous les types des valeurs d'une entité doivent correspondre au domaine donné par le schéma de la relation.

#### <ins>Application 2</ins>

Vérifier puis expliquer pourquoi la contrainte de domaine est respectée pour chaque entité de la relation $Livre$.

### b) Contrainte d'entité

> [!IMPORTANT]
> La *contrainte d'entité* permet de s'assurer que chaque entité d'une relation est unique.

> [!TIP]
> Par exemple :
> Il n'est pas impossible qu'il y ait deux fois le même ouvrage dans une bibliothèque ou bien que deux usagers aient les mêmes nom/prénom, pourtant il s'agit bien de deux entités distinctes.

> [!IMPORTANT]
> Une *clé primaire* est un attribut unique pour chaque entité d'une relation.

Les clés primaires sont soulignées dans le modèle relationnel.

> [!TIP]
> Par exemple :
> Livre(<ins>id_livre</ins> : INT, titre : VARCHAR, auteur : VARCHAR, annee : INT, editeur : VARCHAR).

#### <ins>Application 3</ins>

a) Modifier en conséquence les entités de la relation $Livre$.

b) Ajouter dans la relation $Livre$ un second ouvrage de `Dune` mais par conséquent, avec un identifiant différent.

#### <ins>Application 4</ins>

a) Ajouter une clé primaire au schéma relationnel de la relation $Usager$ pour que chaque usager soit unique.

b) Modifier en conséquence les entités de la relation $Usager$.

### c) Contrainte de référence

> [!IMPORTANT]
> La *contrainte de référence* permet de s'assurer qu'une relation mentionne des entités bien existantes dans d'autres relations.

> [!TIP]
> Par exemple :
> Dans une relation $Emprunt$ s'y trouve les usagers qui ont emprunté un livre.
>
> Or, pour éviter que la relation $Emprunt$ mentionne des livres ou des usagers inexistants, nous ajoutons à la relation $Emprunt$ des clés étrangères.

> [!IMPORTANT]
> Une *clé étrangère* est une référence vers une entité unique d'une autre relation.

Pour s'assurer qu'il s'agit d'une référence vers une entité unique, la clé étrangère correspond alors à la clé primaire de l'entité auquel elle fait référence.

Les clés étrangères sont précédées d'un dièse.

> [!TIP]
> Par exemple :
> Le schéma relationnel de la relation $Emprunt$ est :
>
> $Emprunt(\\#id\textunderscore livre : INT, \\#id\textunderscore usager : INT, date : DATE)$

#### <ins>Application 5</ins>

Imaginons qu'une entité de la relation $Usager$ ait emprunté le livre d'identifiant $1$ à la date d'aujourd'hui.

Ajouter en conséquence l'entité dans la relation $Emprunt$.

### d) Contrainte utilisateur

> [!IMPORTANT]
> Les *contraintes utilisateur* sont des contraintes logiques.

> [!TIP]
> Par exemple :
>
> - L'âge d'un usager ne peut pas être supérieur à $150$.
>
> - L'adresse mail d'un usager doit comporter un arobase dans sa chaîne de caractère.

#### <ins>Application 6</ins>

Trouver au moins deux contraintes utilisateur que nous pourrions ajouter à la relation $Emprunt$.

______________

[Exercices](./Exercices/Exercices_modèle_relationnel.md)

______________

[Sommaire](./../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 
