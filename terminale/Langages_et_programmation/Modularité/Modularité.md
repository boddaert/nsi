# Modularité

## I. Définitions

> [!IMPORTANT]
> La *modularité* est le fait d'utiliser des modules existants ou de créer des modules. L'objectif étant de décomposer son code en plusieurs fonctions/fichiers Python afin qu'il soit plus lisible.

> [!IMPORTANT]
> Un *module* (ou *bibliothèque*) est un fichier Python que nous pouvons importer dans notre propre fichier pour pouvoir utiliser son code. (cf [Modules](./../../../première/Langages_et_programmation/Constructions_élémentaires/Modules.md)).

## II. Bonnes pratiques

1. Il est très conseillé de moduler son programme, c'est-à-dire de découper son programme le plus possible en plusieurs fonctions.

L'idéal est : 

- **Une** tâche $\to$ **une** fonction.

- **Une** fonction $\to$ **une** tâche.

2. La modularité de votre programme doit être logique.

> [!NOTE]
> En partant du fait que les modules peuvent être utilisés par d'autres utilisateurs, il est important de donner des noms de fonctions/variables explicites et de documenter le code à l'aide d'une DocString.

#### <ins>Application 1</ins>

a) Créer un fichier `maximum_liste.py` dans lequel vous écrirez une fonction `maxi(liste : list)->int` permettant de récupérer l'entier maximum d'une liste.

b) Puis, dans un second fichier Python `importation_globale.py` situé dans le même répertoire, importer la fonction `maxi()` de manière globale et tester la fonction dans `importation_globale.py`.

c) Enfin, dans un troisième fichier Python `importation_precise.py` situé lui aussi dans le même répertoire, importer la fonction `maxi()` de manière précise et tester la fonction dans `importation_precise.py`.

_______

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 