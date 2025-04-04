# Projet : Motus

<img src="./img/motus.gif" width=500>

## I. Description

Reprenant les règles du jeu "Motus", le joueur a six essais pour tenter de retrouver le mot Motus.

À chaque fois que le joueur propose un mot, des indices lui sont donnés :

- Les lettres sont coloriées sur fond rouge si elles sont à la bonne place.

- Les lettres sont coloriées sur fond jaune si elles sont dans le mot mais à la mauvaise place.

- Les lettres sont coloriées sur fond bleu si elles ne sont pas dans le mot à trouver.

## II. Cahier des charges

Le programme Python doit respecter les contraintes suivantes :

1. Le mot Motus à retrouver a une taille de six lettres.

2. Si le mot proposé par le joueur ne fais pas six lettres, le programme lui demande de réécrire un mot.

3. Le joueur a droit à six essais. Au delà, le joueur a perdu et le programme s'arrête.

4. Les couleurs du jeu Motus sont respectées. 

5. Le code doit être lisible, les noms de variables/fonctions explicites.

## III. Exemple de rendu

![gif](./img/exemple_motus.gif)

## IV. Changer la couleur de fond d'une chaîne de caractères

Ajouter, dans la fonction `print()`, au début de votre chaîne de caractère :

- `\033[1;37;41m` pour colorier en blanc sur fond rouge le texte qui suit.

- `\033[1;37;44m` pour colorier en blanc sur fond bleu le texte qui suit.

- `\033[1;37;43m` pour colorier en blanc sur fond jaune le texte qui suit.

- `\033[0m` pour revenir aux couleurs par défaut.

## V. Générateur de mots aléatoires

### 1. Via le module `Faker`

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

### 2. Via le module `random`

Si vous n'avez pas les droits pour installer le module `Faker`, créer simplement une liste de mots en Python et choisir un mot aléatoire parmi cette liste via la fonction `choice` du module `random` :

```python
from random import *
liste_mots = ['mot1', 'mot2', 'mot3']
motus = choice(liste_mots)
```

## VI. Aller plus loin

1. Proposer au joueur de recommencer à jouer.

2. Calculer un score en fonction du temps que met le joueur à trouver le mot.

3. Proposer au joueur plusieurs niveaux de longueur de mot.

________

[Sommaire](./../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 