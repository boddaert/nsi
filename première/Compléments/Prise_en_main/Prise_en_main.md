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

Nous distinguons une multitude de langages comme le **Java**, le **C++**, le **HTML**, le **CSS**, le **SQL**, etc ...

<img src="./img/langages.png" width="800"/>

## III. Le Python

En NSI, nous travaillerons avec le langage Python principalement.

Il a été inventé en 1989 par le néerlandais Guido Van Rossum et est aujourd'hui l'un des lagages les plus utilisés au monde.

<img src="./img/python_logo.png" width="600"/>

## IV. Environnement de développement
> [!IMPORTANT]
> Un *IDE* (ou environnement de développement) est un logiciel permettant d'écrire et de faire exécuter des programmes. 

Nous utiliserons pour cela le logiciel Thonny :

<img src="./img/presentation_thonny.png" width="1000"/>

Sur Thonny, il y a un **mode programmation** et un **mode interactif**.

### a) Mode programmation

Le mode programmation de Thonny est l'endroit où l'on va écrire nos programmes. C'est ce texte qui sera enregistré sur le fichier.

Par exemple :

- Je crée un fichier vide `test.py` (la terminaison `.py` indique qu'il s'agit bien d'un fichier python).

- J'écris un programme informatique qui réalise la somme de cinq et cinq.

- Enfin, en cliquant sur le bouton d'exécution, j'exécute le programme.

Nous devrions, à l'issue de cette manipulation, arriver à un état comme celui-ci :

<img src="./img/mode_programmation.png" width="1000"/>

Nous constatons plusieurs choses :

- Premièrement, le programme a bien été enregistré sur le fichier puisque si je ferme le fichier et le réouvre avec Thonny, je retrouve mon programme.

- Deuxièmement, le code a bien été éxécuté puisque dans la console du mode interactif : l'instruction `run test.py` le prouve.

- Troisièmement, aucun résultat ne s'affiche.

> [!WARNING]
> Aucun résultat ne s'est affiché et c'est tout à fait normal, je n'ai pas écris dans mon programme la fonction permettant d'afficher mon résultat. Donc, mon programme a bien effectué la somme de cinq et cinq mais n'a rien effectué de plus.

#### <ins>Application 1</ins>

a) Effectuer les étapes suivantes :

1. Ouvrir le logiciel Thonny.
2. Sur Thonny, créer le fichier `test_mon-nom.py`.
3. Écrire votre premier programme informatique python, qui réalise l'opération suivante : `(5+3)-(4*2)`.

b) Le programme s'exécute t-il ?

#### <ins>Application 2</ins>

a) Remplacer l'opération de l'application 1 par `5 + * 3`

b) Le programme s'exécute t-il correctement ?

c) Qu'est-il écrit sur la console ?

### b) Mode interactif

La console situé en bas de la page se présente comme une calculatrice. Les trois chevrons `>>>` indique que la console attend une instruction.

Par exemple :

- J'efface mon précédent programme.

- Je réexécute le programme vierge (rien ne se passe).

- J'écris dans la console l'opération permettant de faire la somme de cinq et cinq, puis j'appuie sur `Entrée`, je me retrouve dans l'état suivant :

<img src="./img/mode_interactif.png" width="1000"/>

Ici aussi, nous constatons plusieurs choses :

- Premièrement, le résultat de l'opération s'affiche et la console attend de nouveau une instruction.
- Deuxièmement, si je ferme et réouvre le fichier, les instructions précédemment écrites dans la console sont perdues. Le mode interactif ne permet pas d'enregistrer sur le fichier des programmes.

> [!NOTE]
> Nous utilisons généralement le mode interactif pour tester les programmes ou les instructions.

#### <ins>Application 3</ins>

Répéter les opérations des applications $1$ et $2$ en utilisant cette fois uniquement le mode interactif de Thonny.

________

[Sommaire](./../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 