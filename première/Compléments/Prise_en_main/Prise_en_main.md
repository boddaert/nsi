# Prise en main

## I. L'informatique

En Numérique et Sciences Informatiques, nous allons être amenés à écrire des programmes informatiques.

> [!IMPORTANT]
> Un *programme informatique* est un texte composé d'instructions et d'opérations écrit dans un certain langage de programmation et destiné à être exécuté par un ordinateur.

> [!IMPORTANT]
> L'*informatique* est la science des données, les programmes informatiques que nous écrivons nous permettent de manipuler ces données et d'effectuer des calculs sur celles-ci.

Pour nous aider à écrire des programmes informatiques, les informaticiens utilisent des algorithmes. Un algorithme est une suite d'instructions écrit en Français. Il sert à résoudre un problème.

Un algorithme est comparable à une recette de cuisine, par exemple :

```
Recette Mayonnaise
- Mettre un jaune d'oeuf dans un bol.
- Y ajouter une cuillière de moutarde.
- Tant que la préparation est liquide :
    - Ajouter une cuillière à soupe d'huile.
    - Fouetter la préparation.
```

L'objectif de construire un algorithme est qu'il soit compris par tous et qu'on puisse le traduire dans n'importe quel langage de programmation.

## II. Langage de programmation

> [!IMPORTANT]
> Un *langage de programmation* est un langage dans lequel nous allons écrire notre programme.

Comme nos langues naturelles, un langage de programmation est composé d'un alphabet et de règles.

Nous distinguons une multitude de langages comme le Java, le C++, le HTML, le CSS, le SQL, etc ...

<img src="./img/langages.png" width="60"/>

![](./img/langages.png){width=20}

## III. Le Python

En NSI, nous travaillerons avec le langage Python principalement.

Il a été inventé en 1989 par le néerlandais Guido Van Rossum et est aujourd'hui l'un des lagages les plus utilisés au monde.

![](./img/python_logo.png)

## IV. Environnement de développement

Un *IDE* (ou environnement de développement) est un logiciel permettant d'écrire et de faire exécuter des programmes. Nous utiliserons pour cela le logiciel Thonny :

![](./img/presentation_thonny.png)

Sur Thonny, il y a un **mode programmation** et un **mode interactif**.

### a) Mode programmation

Le mode programmation de Thonny est l'endroit où l'on va écrire nos programmes. C'est ce texte qui sera enregistré sur le fichier.

Par exemple, je crée un fichier vide `test.py` (la terminaison `.py` indique qu'il s'agit bien d'un fichier python), puis j'écris un programme informatique qui réalise la somme de 5 et 5. Enfin, en cliquant sur le bouton d'exécution, j'exécute le programme. Nous devrions, à l'issue de cette manipulation, arriver à un état comme celui-ci :

![](./img/mode_programmation.png)

Nous constatons plusieurs choses :

- Premièrement, le programme a bien été enregistré sur le fichier puisque si je ferme le fichier et le réouvre avec Thonny, je retrouve mon programme.
- Deuxièmement, le code a bien été éxécuté puisque dans la console du mode interactif, l'instruction `run test.py` le prouve.
- Troisièmement, aucun résultat ne s'affiche.

Aucun résultat ne s'est affiché et c'est tout à fait normal, je n'ai pas écris dans mon programme la fonction permettant d'afficher mon résultat. Donc, mon programme a bien effectué la somme de 5 et 5 mais n'a rien effectué de plus.

##### Application 1

- Ouvrir le logiciel Thonny.
- Sur Thonny, créer le fichier `test_mon-nom.py`.
- Ecrire votre premier programme informatique python, qui réalise l'opération suivante : `(5+3)-(4*2)`.

Le programme s'exécute t-il ?

##### Application 2

Remplacer l'opération de l'application 1 par `5 + * 3`

Le programme s'exécute t-il correctement ? 
Qu'est-il écrit sur la console ?

### b) Mode interactif

La console situé en bas de la page se présente comme une calculatrice. Les trois chevrons **>>>** indique que la console attend une instruction.

Par exemple, j'efface mon précédent programme, je réexécute le programme vierge (rien ne se passe) et j'écris dans la console l'opération permettant de faire la somme de 5 et 5, puis en appuyant sur `Entrée`, je me retrouve dans l'état suivant :

![](./img/mode_interactif.png)

Ici aussi, nous constatons plusieurs choses :

- Premièrement, le résultat de l'opération s'affiche et la console attend de nouveau une instruction.
- Deuxièmement, si je ferme et réouvre le fichier, les instructions précédemment écrites dans la console sont perdues. Le mode interactif ne permet pas d'enregistrer sur le fichier des programmes.

On utilise généralement le mode interactif pour tester ses programmes ou ses instructions.

#### Application 3

Répéter les opérations des applications 1 et 2 en utilisant cette fois uniquement le mode interactif de Thonny.

________

[Sommaire](./../README.md)