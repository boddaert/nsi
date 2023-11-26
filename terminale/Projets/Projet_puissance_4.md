# Projet : Puissance 4

## I. Description

L'objectif de ce projet est de programmer un jeu de Puissance 4 en Python.

Règles du jeu : [Wikipedia - Puissance 4](https://fr.wikipedia.org/wiki/Puissance_4).

## II. Cahier des charges

1. Les règles du jeu du Puissance 4 doivent être respectées.

2. La programmation de ce projet se fera exclusivement en itératif sans utiliser d'objets.

3. Le programme doit être modulaire : chaque fonction réalisant une unique tâche.

Pour vous aider à commencer, voici plusieurs idées de fonctions à réaliser :

- Une fonction `init_grille()->list` qui ne prend pas de paramètre et renvoie une liste de listes correspondant à la grille de jeu.

- Une fonction `affiche_grille(grille : list)->None` qui prend en paramètre une liste de listes et affiche dans la console l'état de la grille de jeu.

- Une fonction `placer_jeton(grille : list, num_colonne : int, num_joueur : int)->None` qui prend en paramètre une liste de listes et deux entiers et place un jeton dans la grille à la colonne `num_colonne`.

- Une fonction `test_victoire(grille : list, num_joueur : int)->bool` qui prend en paramètre une liste de listes et un entier et renvoie $True$ si le joueur numéro `num_joueur` a gagné la partie.

4. Chaque fonction écrite doit être munie d'une documentation complète et d'un jeu de test complet. Toute les préconditions et postconditions de chaque spécification devant être vérfiées.

Rappel de Première NSI :

- [Prototypage d'une fonction](./../../première/Spécifications_de_fonction/Prototypage.md)

- [Préconditions d'une fonction](./../../première/Spécifications_de_fonction/Préconditions.md)

- [Postconditions d'une fonction](./../../première/Spécifications_de_fonction/Postconditions.md)

## III. Exemple d'affichage dans la console 

```python
Début du match

|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |

Tour n°1
Joueur n°0
Colonne :2
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   | * |   |   |   |

Joueur n°1
Colonne :1
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   | o | * |   |   |   |

Tour n°2
Joueur n°0
Colonne :5
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   | o | * |   |   | * |

Joueur n°1
Colonne :2
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   | o |   |   |   |
|   | o | * |   |   | * |

Tour n°3
Joueur n°0
Colonne :4
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   | o |   |   |   |
|   | o | * |   | * | * |

Joueur n°1
Colonne :2
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   | o |   |   |   |
|   |   | o |   |   |   |
|   | o | * |   | * | * |

Tour n°4
Joueur n°0
Colonne :3
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   | o |   |   |   |
|   |   | o |   |   |   |
|   | o | * | * | * | * |
Le joueur n°0 a gagné !
```

## IV. Evaluation

Vous serez évalués sur :

- La qualité du code fourni (lisibilité du code, modularité, explicité des noms).

- Le respect du cahier des charges.

- La qualité de la *DocString*.

- La qualité de la *DocTest*.

____________

[Sommaire](./../README.md)