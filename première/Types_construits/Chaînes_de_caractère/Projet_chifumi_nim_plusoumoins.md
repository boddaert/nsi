# Projet : Jeu ChiFuMi - Nim - Plus ou moins

## I. Description

Vous avez été appelés pour programmer trois mini-jeux Joueur VS Ordinateur : Le jeu du ChiFuMi, le jeu de NIM et le jeu du plus ou moins.

L'utilisateur pourra choisir entre les trois mini-jeux à volonté.

## II. Cahier des charges

Votre programme devra respecter les contraintes suivantes :

### a) Choix des jeux

1. Votre programme devra proposer à l'utilisateur quatre choix :

- Le jeu du ChiFuMi

- Le jeu de NIM

- Le jeu du Plus ou moins

- Quitter

2. Les parties se déroulent entre l'utilisateur et l'ordinateur.

3. A chaque choix de jeu, un très bref rappel des règles est affiché.

### b) Le jeu du ChiFuMi

4. Les règles du jeu doivent être respectées.

5. La partie du ChiFuMi se joue dans un BO5 (pour *Best Of 5*) où le joueur devra gagner au moins trois manches pour remporter la partie.

6. A l'issue de la partie, le programme propose au joueur de rejouer ou de revenir vers l'écran de choix des jeux.

### c) Le jeu de Nim

7. Les règles du jeu doivent être respectées.

8. La partie du jeu du NIM se joue en une manche gagnante.

9. A l'issue de la partie, le programme propose à l'utilisateur de rejouer ou de revenir vers l'écran de choix des jeux.

### d) Le jeu du Plus ou moins

10. Les règles du jeu doivent être respectées.

11. La partie du jeu du Plus ou moins se joue en une manche gagnante.

12. A l'issue de la partie, le programme propose à l'utilisateur de rejouer ou de revenir vers l'écran de choix des jeux.

## III. Règles des jeux

### a) Règles de ChiFuMi

Deux joueurs choisissent entre Chi, Fu et Mi. Le gagnant de la manche est désigné comme étant celui qui a choisis le signe qui "bat" le signe de son adversaire.

En sachant que :

- Chi bat Mi.

- Fu bat Chi.

- Mi bat Fu.

En cas de match nul, aucun gagnant n'est désigné et la manche n'est pas comptabilisée.

### b) Règles de Nim

Onze bâtonnets sont disposés devant les deux joueurs.

A tour de rôle, chaque joueur pourra prendre $1$, $2$ ou $3$ bâtonnets.

Celui qui prend le dernier a perdu.

### c) Règles du Plus ou moins

Le premier joueur choisis un nombre entre zéro et cent que le deuxième joueur tentera de retrouver en sept essais maximum.

Pour cela, le second joueur propose un nombre et le premier lui indique si son nombre est supérieur ou inférieur au nombre proposé.

Si le second joueur trouve le nombre en moins de sept essais, il gagne la partie.

Dans le cadre de ce projet, l'utilisateur est le joueur qui devra chercher le nombre.

## V. Evaluation

Vous serez évalués sur :

- La qualité du code fourni (lisibilité du code, explicité des noms).

- Le respect du cahier des charges.

- La qualité de l'interraction avec l'utilisateur.

_______________

[Sommaire](./../../README.md)


