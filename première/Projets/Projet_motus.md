# Projet : Motus

## I. Description

Reprenant les règles du jeu "Motus", le joueur a six essais pour tenter de retrouver le mot Motus.

À chaque fois que le joueur propose un mot, des indices lui sont donnés :

- Les lettres sont coloriées en vert si elles sont à la bonne place.

- Les lettres sont coloriées en jaune si elles sont dans le mot mais à la mauvaise place.

- Les lettres sont coloriées en rouge si elles ne sont pas dans le mot à trouver.

## II. Cahier des charges

Le programme Python doit respecter les contraintes suivantes :

1. Le mot Motus à retrouver a une taille de six lettres.

2. Si le mot proposé par le joueur ne fais pas six lettres, le programme lui demande de réécrire un mot.

3. Le joueur a droit à six essais. Au delà, le joueur a perdu et le programme s'arrête.

4. Les couleurs du jeu Motus sont respectées. 

5. Le code doit être lisible, les noms de variables/fonctions explicites.

## III. Exemple de rendu

Exemple de rendu :

![gif](./img/exemple_motus.gif)

## IV. Module générateur

Le module générateur `Faker` permet de générer un mot français aléatoire.

> [!TIP]
> Par exemple :
> ```python
> >>> from faker import Faker
> >>> fake = Faker(locale="fr_FR")
> >>> fake.word()
> 'soir'
> ```

Sa documentation est disponible [ici](https://faker.readthedocs.io/en/master/).
________

[Sommaire](./../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 