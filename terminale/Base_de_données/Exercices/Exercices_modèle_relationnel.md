# Exercices

## Exercice 1

Nous souhaitons réaliser le modèle relationnel d'une base de données sur les films.

Voici ci-dessous les attributs de la relation $Film$ :

| Nom | Domaine | Description |
| :---: | :---: | :---: |
| id_film | `Integer` | Identifiant unique du film |
| titre | ... | ... |
| annee | ... | ... |
| ... | ... | Le nombre d'entrée en salle de cinéma. |
| ... | ... | Le genre du film |
| id_realisateur | ... | ... |

a) Compléter les informations manquantes du tableau des attributs.

b) Indiquer, en soulignant, quel attribut est le plus adéquat pour être la clé primaire.

c) Indiquer, en ajoutant un dièse devant le nom, quels attributs peuvent être des clés étrangères.

d) Donner le schéma relationnel de la relation $Film$.

e) Ecrire la relation $Film$ en donnant au moins cinq entités.

## Exercice 2

a) Ecrire le schéma relationnel de la relation $Realisateur$ comprenant un identifiant unique de réalisateur correspondant à la clé primaire, un prénom et un nom.

Voici ci-dessous la relation $Realisateur$ :

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

c) Expliquer pourquoi le fait d'ajouter l'entité `(36, 'Star Wars V : L'empire contre-attaque', 1979, 140000000, 'Science-fiction', 12)` viole la contrainte de référence.

## Exercice 3

Donner la modélisation relationnelle d'un bulletin scolaire.

Cette modélisation devra comporter au moins quatre relations représentant les élèves, les professeurs, les spécialités et les notes ainsi que les liens entre elles.

_________________

[Sommaire](./../../README.md)

