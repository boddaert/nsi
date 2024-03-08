# Fichiers CSV

## I. Définitions

Un *fichier CSV* (*Coma-Seperated Values*) est un fichier texte représentant des données tabulaires sous forme de valeurs séparées par des virgules (ou des point-virgules).

Chaque ligne du texte correspond à une ligne du tableau et les virgules correspondent aux séparations entre les colonnes.

Par exemple, le fichier [personnes.csv](./src/personnes.csv) contenant :

```csv
Sexe,Prénom,Année de naissance
M,Alphonse,1932
F,Béatrice,1964
F,Charlotte,1988
```

Peut être représenté sous forme de tableau appelée *table* :

| Sexe | Prénom | Année de naissance |
| :---: | :---: | :---: |
| M | Alphonse | 1932 |
| F | Béatrice | 1964 |
| F | Charlotte | 1988 |

Le titre de chaque colonne est un *attribut*.

Chaque ligne suivante est un *enregistrement*.

Chaque case contient une *valeur*, une valeur est une donnée.

Une *donnée* est une information.

##### Application 1

a) Télécharger le fichier [personnes.csv](./src/personnes.csv).

b) Ouvrir le fichier de deux façons :

    - Une première fois avec le logiciel Bloc-notes.

    - Une seconde avec LibreOffice Tableur.

## II. Chargement des données

Le module CSV de Python permet d'importer les données depuis un fichier CSV. Sa documentation est disponible [ici](https://docs.python.org/3/library/csv.html).

### a) Importer les données sous forme de liste de listes

```python
import csv

personnes = []
with open('personnes.csv', 'r', encoding='utf-8') as csvfile:
    lecteur_liste = csv.reader(csvfile, delimiter=',')
    for ligne in lecteur_liste:
        personnes.append(ligne)
```

L'importation de données s'effectue avec la fonction `open()`, celle-ci prend en paramètre le nom du fichier CSV à ouvrir, le mode d'ouverture (en lecture ou en écriture) et l'encodage.

Ces données regroupées au sein d'un objet `csvfile` sont ensuite lues par un lecteur représenté par la fonction `reader` qui prend en paramètre le séparateur entre les données.

Puis, par une simple boucle, les lignes sont ajoutées dans une liste préalablement créee :

```python
>>> personnes
[['Sexe', 'Prénom', 'Année de naissance'], ['M', 'Alphonse', '1932'], ['F', 'Béatrice', '1964'], ['F', 'Charlotte', '1988']]
```

##### Application 2

a) Recopier le code ci-dessus dans le même répertoire que le fichier [personnes.csv](./src/personnes.csv) et exécuter le.

b) Vérifier dans la console que le contenu de la variable `personnes`.

### b) Importer les données sous forme de dictionnaire

```python
import csv

personnes = []
with open('personnes.csv', 'r', encoding='utf-8') as csvfile:
    lecteur_dict = csv.DictReader(csvfile, delimiter=',')
    for ligne in lecteur_dict :
        personnes.append(ligne)
```

À la différence de la première méthode, il s'agit ici d'une liste de dictionnaire :

```python
>>> personnes
[{'Sexe': 'M', 'Prénom': 'Alphonse', 'Année de naissance': '1932'}, {'Sexe': 'F', 'Prénom': 'Béatrice', 'Année de naissance': '1964'}, {'Sexe': 'F', 'Prénom': 'Charlotte', 'Année de naissance': '1988'}]
```

##### Application 3

a) Recopier le code ci-dessus dans le même répertoire que le fichier [personnes.csv](./src/personnes.csv) et exécuter le.

b) Vérifier dans la console que le contenu de la variable `personnes`.

## III. Validation des données

Après avoir chargé les données à l'intérieur du script Python, il serait intéressant de vérifier et de valider les données.

La *vérification* et la *validation* des données chargées consiste à convertir ou à refuser des données non valides.

Lors du chargement de données, la fonction `DictReader()` ne se préoccupe pas de l'état des valeurs en entrée, elle importe tout ce qui s'y trouve dans le fichier et sous forme de chaîne de caractères.

Or, les années de naissance sont plutôt de type `int`.

Et les seules valeurs possibles de l'attribut `sexe` sont `"F"` et `"M"`.

La validation de données est propre à chaque fichier CSV, c'est pourquoi il n'existe pas de fonction native permettant de le faire à notre place.

##### Application 4

a) Écrire une fonction `valide_personnes(personnes : list)->list` qui prend en paramètre une liste de personnes et renvoie cette même liste en convertissant les années de naissance en entier et/ou renvoie un message d'erreur si une valeur autre que `"F"` ou `"M"` est présente dans la colonne `sexe`.

b) Modifier votre fichier CSV afin de vérifier le bon fonctionnement de votre fonction `valide_personnes()`.

____________

[Feuille d'exercices](./Exercices/Exercices_fichiers_csv.md)

____________

[Sommaire](./../README.md)