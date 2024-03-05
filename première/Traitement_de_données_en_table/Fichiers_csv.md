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

Chaque case contient une donnée, une *donnée* est une information.

##### Application 1

a) Télécharger le fichier [personnes.csv](./src/personnes.csv).

b) Ouvrir le fichier de deux façons :

    - Une première fois avec le logiciel Bloc-notes.

    - Une seconde avec LibreOffice Tableur.

## II. Module CSV

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

____________

[Sommaire](./../README.md)