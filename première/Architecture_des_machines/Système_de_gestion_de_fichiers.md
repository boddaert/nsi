# Système de gestion de fichiers

## I. Définitions

Un *système de gestion de fichiers* ou un *gestionnaire de fichiers* est un système répondant à l'un des objectifs du système d'exploitation : la gestion des fichiers.

Un *système de gestion de fichiers* permet de conserver dans la mémoire de l'ordinateur les données du système et de l'utilisateur même lors de la mise hors tension de la machine.

Un *fichier* est un ensemble de données. Il comporte un nom et une extension qui renseigne sur la nature des données contenues dans le fichier et donc des logiciels utilisables pour le manipuler.

Les *métadonnées* d'un fichier sont des informations propres au fichier tel que la date de création, l'auteur, la taille du fichier, etc...

Un *répertoire* ou *dossier* est un fichier spécial pouvant contenir des fichiers ou d'autres répertoires.

##### Application 1

| Extension de fichier | Type de contenu | Logiciel/Application permettant d'ouvrir ce type de fichier |
| --- | :---: | :---: |
| `.txt` | Texte | Bloc-notes |
| `.odt` | | |
| `.mp3` | | |
| `.md`  | | |
| `.png` | | |
| `.jpeg`| | |
| `.pdf` | | |
| `.gif` | | |
| `.py`  | | |
| `.csv` | | |

a) Sur feuille, recopier et compléter le tableau ci-dessus.

b) Dans le système de gestion de fichiers et sur l'un de vos fichiers, repérer la date de sa création, son auteur et sa taille.

## II. Organisation des fichiers

### a) Arborescence

Les répertoires et les fichiers sont organisés en mémoire sous forme de hierarchie arborescente. Par exemple :

- :file_folder: `nsi`
    - :file_folder: `premiere`
        - :file_folder: `Architecture des machines`
            - :page_facing_up: `Systèmes_d_exploitation.md`
            - :page_facing_up: `Activité_terminus.md`
            - :page_facing_up: `Système_de_gestion_de_fichiers.md`
            - :page_facing_up: `Évaluation.pdf`
        - :page_facing_up: `README.md`
        - ...
    - :file_folder: `terminale`
        - ...

Comme dans un arbre généalogique, nous parlons de répertoires ou de fichiers *parents* et de répertoires ou de fichiers *enfants*.

La *racine* est parent de tous les autres répertoires et fichiers du système et est désignée par le caractère `~` (`\`sur Windows).

`.` désigne le *répertoire courant*, c'est-à-dire le répertoire où nous nous trouvons.

`..` désigne le répertoire parent du répertoire courant.

##### Application 2

La commande Linux `tree` affiche l'arborescence du répertoire courant.

Trouver l'équivalent Windows et donner l'arborescence de votre répertoire de travail présent sur votre machine.

### b) Inœuds

Chaque fichier et répertoire est désigné au sein du système par un numéro appelé *inœud de fichier*.

Les inœuds permettent d'obtenir en autre les métadonnées des fichiers.

Un répertoire est en fait un fichier pointant vers d'autres inœuds.

##### Application 3

La commande Linux `ls -i` affiche les inœuds des fichiers du répertoire courant.

Trouver l'équivalent Windows et donner les inœuds des fichiers de votre répertoire de travail présent sur votre machine.

## III. Chemins

### a) Chemin absolu

Un *chemin absolu* vers un fichier est la concaténation de tous les noms de répertoires depuis la racine menant à ce fichier.

Par exemple, le chemin absolu du fichier `Évaluation.pdf` est `~/nsi/premiere/Architecture_des_machines/Évaluation.pdf`.

### b) Chemin relatif

Un *chemin relatif* vers un fichier est la concaténation de tous les noms de répertoires depuis le répertoire courant menant à ce fichier.

Par exemple, le chemin relatif du fichier `Évaluation.pdf` depuis le répertoire `terminale` est `../premiere/Architecture_des_machines/Évaluation.pdf`.

##### Application 4

La commande Linux `pwd` affiche le chemin absolu du répertoire courant.

Trouver l'équivalent Windows et donner le chemin absolu de votre répertoire de travail présent sur votre machine.

## IV. Droits et permissions

Le système de gestion de fichier doit permettre aux utilisateurs de créer, modifier et supprimer un fichier.

Les systèmes POSIX étant multi-utilisateurs, ils doivent permettre à chaque utilisateur de différencier ses fichiers de ceux des autres.

À cette fin, le système d'exploitation accorde des *droits et permissions* aux utilisateurs.

C'est pourquoi il associe à chaque fichier l'UID de son propriétaire (pour *User Identification*) et le GID de son propiétaire (pour *Group Identification*).

La commande `ls -l` donne un affichage des métadonnées dont les droits sur les fichiers du répertoire courant.

En réponse, le système indique quels droits l'utilisateur a sur les fichiers comme ci-dessous :

```
~/nsi/premiere$ ls -l
drwxrwxrwx Architecture_des_machines
-rwx------ README.md
```

- Le premier caractère indique s'il s'agit d'un répertoire (`d`) ou d'un fichier (`-`).

- Pour les neuf caractères suivants, la réponse système indique d'une lettre si le concerné possède les droits (`r` pour les droits de lecture, `w` pour ceux d'écriture et `x` pour ceux d'exécution) et d'un tiret sinon.

    + Les trois premiers caractères conernent le propriétaire (`u`).

    + Les trois suivants caractères concernent le groupe (`g`).

    + Les trois derniers caractères concernent les autres utilisateurs (`o`).

La commande `chmod` suivi d'un nom de fichier modifie les droits de ce fichier. Par exemple, en précisant lequels ajouter et lesquels supprimer :

```
~/nsi/premiere$ chmod u-x, g+rwx, o+r README.md
~/nsi/premiere$ ls -l
drwxrwxrwx Architecture_des_machines
-rw-rwxr-- README.md
```

##### Application 5

```
~/nsi/premiere$ ls -l
drwxrwxrwx Architecture_des_machines
-rw-rwxr-- README.md
~/nsi/premiere$ chmod u-rw, u+x, g-rx, o-rw, o+x README.md
~/nsi/premiere$ ls -l
...
```

a) Qu'affiche l'exécution de la dernière commande ?

b) Quelle commande écrire pour obtenir le résultat ci-dessous ?

```
~/nsi/premiere$ ls -l
drwxrwxrwx Architecture_des_machines
-rwxr-xr-x README.md
```

________________

[Sommaire](./../README.md)
