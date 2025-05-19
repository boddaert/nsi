# Fichiers CSV

## I. Définitions

> [!IMPORTANT]
> Un *fichier CSV* (*Coma-Seperated Values*) est un fichier texte représentant des données tabulaires sous forme de valeurs séparées par des virgules (ou des point-virgules).

Chaque ligne du texte correspond à une ligne du tableau et les virgules correspondent aux séparations entre les colonnes.

> [!TIP]
> Par exemple :
>
> Le fichier [personnes.csv](./src/personnes.csv) contenant :
>
> ```csv
> Sexe,Prénom,Année de naissance
> M,Alphonse,1932
> F,Béatrice,1964
> F,Charlotte,1988
> ```
>
> Peut être représenté sous forme de tableau appelée *table* :
>
> | Sexe | Prénom | Année de naissance |
> | :---: | :---: | :---: |
> | M | Alphonse | 1932 |
> | F | Béatrice | 1964 |
> | F | Charlotte | 1988 |

> [!IMPORTANT]
> Le titre de chaque colonne est un *attribut*.

> [!IMPORTANT]
> Chaque ligne suivante est un *enregistrement*.

> [!IMPORTANT]
> Chaque case contient une *valeur*, une valeur est une donnée.

> [!IMPORTANT]
> Une *donnée* est une information.

#### <ins>Application 1</ins>

a) Télécharger le fichier [personnes.csv](./src/personnes.csv).

b) Ouvrir le fichier de deux façons :

1. Une première fois avec le logiciel Bloc-notes.

2. Une seconde avec LibreOffice Tableur.

## II. Chargement des données

Le module CSV de Python permet d'importer les données depuis un fichier CSV. Sa documentation est disponible [ici](https://docs.python.org/3/library/csv.html).

L'importation de données s'effectue avec la fonction `open()`, celle-ci prend en paramètre le nom du fichier CSV à ouvrir, le mode d'ouverture (en lecture ou en écriture) et l'encodage.

> [!TIP]
> Par exemple :
> ```python
> import csv
>
> personnes = []
> with open('personnes.csv', 'r', encoding='utf-8') as csvfile:
>     lecteur = csv.DictReader(csvfile, delimiter=',')
>     for ligne in lecteur:
>         personnes.append(ligne)
> ```

Ces données regroupées au sein d'un objet `csvfile` sont ensuite lues par un lecteur représenté par la fonction `DictReader` qui prend en paramètre le séparateur entre les données.

> [!TIP]
> Par exemple :
> ```python
> lecteur = csv.DictReader(csvfile, delimiter=',')
> ```

À l'aide d'une boucle, les lignes lues par le lecteur sont ajoutées dans une liste.

> [!TIP]
> Par exemple :
> ```python
> >>> personnes
> [{'Sexe': 'M', 'Prénom': 'Alphonse', 'Année de naissance': '1932'}, {'Sexe': 'F', 'Prénom': 'Béatrice', 'Année de naissance': '1964'}, {'Sexe': 'F', 'Prénom': 'Charlotte', 'Année de naissance': '1988'}]
> ```

#### <ins>Application 2</ins>

a) Recopier le code ci-dessus dans le même répertoire que le fichier [personnes.csv](./src/personnes.csv) et exécuter le code.

b) Écrire l'instruction permettant d'obtenir les informations de la première personne.

c) Écrire l'instruction permettant d'obtenir uniquement le prénom de la première personne.

## III. Validation des données

Après avoir chargé les données à l'intérieur du script Python, il serait intéressant de vérifier et de valider les données.

La *vérification* et la *validation* des données chargées consiste à convertir ou à refuser des données non valides.

Lors du chargement de données, la fonction `DictReader()` ne se préoccupe pas de l'état des valeurs en entrée, elle importe tout ce qui s'y trouve dans le fichier et sous forme de chaîne de caractères.

Or, les années de naissance sont plutôt de type `int`.

Et les seules valeurs possibles de l'attribut `sexe` sont `"F"` et `"M"`.

La validation de données est propre à chaque fichier CSV, c'est pourquoi il n'existe pas de fonction native permettant de le faire à notre place.

____________

[Exercices](./Exercices/Exercices_fichiers_csv.md)

____________

[Sommaire](./../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 