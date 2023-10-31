# Exercices

## Exercice 1

Nous souhaitons réaliser le modèle relationnel d'une base de données sur les films.

La base de données comporte une relation $Film$ et une relation $Realisateur$ correspondants respectivement à un film et un réalisateur.

Voici ci-dessous les attributs de la relation $Film$ :

- (id_film, `Integer`)

- (titre, ...)

- (annee, ...)

- (box_office, ...)

- (genre, ...)

- (id_realisateur, ...)

a) Compléter les domaines sur les attributs ci-dessus.

b) Indiquer, en soulignant, quel attribut unique est le plus susceptible d'être la clé primaire.

c) Indiquer, en ajoutant un dièse devant le nom, quel attribut est le plus susceptible d'être la clé étrangère faisant référence à un réalisateur.

d) Donner le schéma relationnel de la relation $Film$.

e) Donner au moins trois entités de la relation $Film$.

## Exercice 2

a) Ecrire le schéma relationnel de la relation $Realisateur$ comprenant un identifiant unique de réalisateur correspondant à la clé primaire, un prénom et un nom.

Voici ci-dessous des entités de la relation $Realisateur$ :

```
Realisateur = {
    (1, 'Sergio', 'Leone'),
    ('2', 'Anderson', 'Wes'),
    (3, 'Villeneuve', 'Denis'),
    (4, 'Scorsese', 'Martin'),
    (4, 'Cameron', 'James'),
    (5, 'Obama', 'Barack')
}
```

a) Indiquer quelles contraintes d'intégrité n'ont pas été respectées par les entités de la relation ci-dessus.

b) Corriger les erreurs afin que les contraintes d'intégrité soient respectées.

c) Expliquer pourquoi le fait d'ajouter l'entité `(36, 'Star Wars V : L'empire contre-attaque', 1979, 140000000, 'Science-fiction', 12)` dans la relation $Film$ viole la contrainte de référence.

## Exercice 3

Donner la modélisation relationnelle d'un bulletin scolaire.

Cette modélisation devra comporter au moins trois relations représentant les élèves, les disciplines et les notes ainsi que les liens entre elles.

Donner pour chaque relation leur schéma en spécifiant les contraintes de domaine, d'entité et de référence.

_________________

[Sommaire](./../../README.md)

