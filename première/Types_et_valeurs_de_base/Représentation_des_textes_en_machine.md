# Représentation des textes en machine

Vu précédemment dans la leçon sur la représentation des nombres en machine (Cf [Représentation des nombres en machine](./../Représentation_des_nombres_en_machine/)), nous savons que l'ordinateur ne comprend que les $0$ (tension basse) et les $1$ (tension haute).

Nous avons vu également que l'ordinateur peut représenter tous les entiers naturels en base deux.

Une première idée serait alors d'associer chacun des caractères à un entier naturel.

Il y a tout de même quelques contraintes :

- Toutes les machines informatiques doivent utiliser le même encodage.

- Tous les caractères doivent être représentés y compris les caractères dits "non imprimables" (comme l'espace).

- L'encodage doit être le plus compact possible pour économiser la mémoire.

## I. Définitions

Un *codage des caractères* est un code qui permet de transmettre informatiquement des textes.

*Encoder* un caractère consiste à transcrire un caractère dans un format selon un codage.

## I. Codage Morse

Le codage Morse permettait de transmettre un texte à l’aide de séries d’impulsions courtes et longues, qu’elles soient produites par des signes, une lumière, un son ou un geste.

![Codage Morse](./img/codage_morse.png)

##### Application 1

A l'aide du Codage Morse Internationnal, encoder, sous forme de point et de trait, le mot `morse`.

## II. Codage ASCII

### a) Table ASCII

L'ANSI ( *American National Standards Institute* ) propose au début des années soixante une norme de codage appelée ASCII ( *American Standard Code for Information Interchange* ).

Cette norme définit un codage de $128$ caractères où chaque caractère est représenté par un octet (avec un bit de contrôle et sept bits codants):

![table ASCII](./img/Table_ASCII.png)

Le codage ASCII peut représenter :

- Toutes les lettres de l'alphabet latin en majuscule et minuscule.
- Les chiffres de $0$ à $9$.
- Quelques signes de ponctuation.
- Des opérateur arithmétiques.
- Des caractères non imprimables (Espace, Retour à la ligne, etc...).

D'après la table ASCII, le caractère `A` correspond à la séquence :

- $1000001_2$.

- $65_{10}$.

- $41_{16}$.

Plus d'informations sur l'encodage ASCII : [Wikipédia ASCII](https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange)

##### Application 1

D'après le codage ASCII, trouver la séquence binaire, décimale et hexadécimale correspondant :

a) Au caractère `Y`.

b) Au caractère `?`.

### b) ASCII en Python

La fonction `ord()` prend en paramètre une chaîne de caractère et renvoie la représentation décimale correspondant à son encodage ASCII :

```python
>>> ord('A')
65
```

La fonction `chr()` prend en paramètre un entier et renvoie le caractère correspondant à son encodage ASCII :

```python
>>> chr(65)
'A'
```

##### Application 2

A l'aide des fonctions `ord()` et `chr()`, trouver :

a) Le caractère correspondant à l'entier décimal $100$ selon l'encodage ASCII.

b) La représentation décimale correpondant au caractère `' '` selon l'encodage ASCII.

## III. Norme ISO 8859

### a) Extension de l'ASCII

Malheureusement, l'encodage ASCII ne permet pas d'imprimer tous les caractères, il manque les caractères accentués, les symboles de monnaies et même les autres alphabets !

Pour remédier à ce problème, l'ISO ( *Organisation Internationale de Normalisation* ) a proposé une extension de l'ASCII qui utilise les huit bits de chaque octet pour représenter les caractères.

Au total, nous pouvons désormais représenter deux-cent cinquante-six caractères, ce qui reste toujours insuffisant pour représenter tous les caractères de tous les alphabets du monde.

### b) Norme ISO 8859

L'ISO propose alors une norme qui définit plusieurs pages de correspondances notées ISO 8859- $n$ où $n$ est le numéro de la page :

| Code ISO           | Zone                          |
| ------------------ | ----------------------------- |
| 8859-1 (latin-1)   | Europe Occidentale            |
| 8859-2 (latin-2)   | Europe Centrale ou de l'Est   |
| 8859-3 (latin-3)   | Europe du Sud                 |
| 8859-4 (latin-4)   | Europe du Nord                |
| 8859-5             | Cyrillique                    |
| 8859-6             | Arabe                         |
| 8859-7             | Grec                          |
| 8859-8             | Hébreu                        |
| 8859-9 (latin-5)   | Turc, Kurde                   |
| 8859-10 (latin-6)  | Nordique                      |
| 8859-11            | Thaï                          |
| 8859-12            | Devanagari (projet abandonné) |
| 8859-13 (latin-7)  | Balte                         |
| 8859-14 (latin-8)  | Celtique                      |
| 8859-15 (latin-9)  | Révision du latin-1 (avec €)  |
| 8859-16 (latin-10) | Europe du Sud-Est             |

Nous, européens occidentaux, utilisons la page ISO 8859-1, reprise de l'ASCII étendu.

Plus d'informations sur la norme ISO 8859 : [Wikipedia 8859](https://fr.wikipedia.org/wiki/ISO/CEI_8859)

## IV. Norme ISO 10646

Bien que les pages ISO 8859- $n$ permettent l'encodage d'un grand nombre de caractères, elles ne conviennent pas par exemple quand nous souhaitons écrire un texte avec un mélange de caractères depuis différents alphabets.

Pour remplacer l'utilisation de ces pages, l'ISO a définit une nouvelle norme donnant dans une seule page un unique jeu universel de caractères (*Universal Character Set*).

La norme ISO 10646 regroupe donc tous les caractères du monde dans une seule page.

Il y a aujourd'hui plus de cent-dix mille caractères recensés dans cette norme, qui est  conçue pour en contenir maximum quatre milliard (Plus précisément, $4 294 967 295$, c'est-à-dire le plus grand entier positif représentable sur trente-deux bits).

Elle associe chaque caractère à un numéro (appelé *point de code*).

Nous utilisons la notation $U+xxxx$ pour désigner les points de code où chaque $x$ est un chiffre hexadécimal.

En pratique, un point de code contient au minimum quatre chiffres et nous en ajoutons un quand cela est nécessaire.

Plus d'informations sur la norme ISO 10646 : [Wikipedia 10646](https://fr.wikipedia.org/wiki/ISO/CEI_10646)

## V. Unicode

### a) UTF

Cependant, avec un tel nombre de point de code, un encodage naïf de la norme ISO 10646 utiliserait donc au minimum quatre octets pour représenter chaque caractère.

Or, dans la majorité des cas, nous n'avons besoin que d'un octet : il y aurait alors trois octets utilisés inutilement. Ce qui représente un énorme gachis !

Unicode a été développée par un consortium du même nom, une organisation privée à but non lucratif où l'objectif a été de représenter les points de code de manière économique.

Unicode développe plusieurs formats de transformation universelle (*Universal Transformation Format*).

UTF-8 est le format le plus utilisé sous Linux et utilise un à quatre octets.

| Plage | Séquence en binaire | Nombre de bits codants |
| :---: | :--- | :---: |
| $U+0000$ à $U+007F$ | $0xxxxxxx$ | $7$ |
| $U+0080$ à $U+07FF$ | $110xxxxx 10xxxxxx$ | $11$ |
| $U+0800$ à $U+FFFF$ | $1110xxxx 10xxxxxx 10xxxxxx$ | $16$ |
| $U+10000$ à $U+10FFFF$ | $11110xxx 10xxxxxx 10xxxxxx 10xxxxxx$ | $21$ |

La première plage correspond à l'encodage ASCII.

Par exemple, le caractère `é` a pour point de code $U+00E9$, ce qui donne en binaire : $1110 1001_2$.

Nous sommes dans la deuxième plage de UTF-8 donc il y aura deux octets.

Encodage UTF-8 du caractère `é` : $11000011 10101001_2$ ou $C3 A9_{16}$.

### b) Unicode en Python

La méthode `encode()` permet d'obtenir l'encodage UTF-8 en hexadécimal à partir d'un caractère ou d'un point de code :

```python
>>> 'é'.encode()
b'\xc3\xa9'
>>> '\u00E9'.encode()
b'\xc3\xa9'
```

La méthode `decode()` permet d'obtenir un caractère à partir de son encodage UTF-8 :

```python
>>> b'\xc3\xa9'.decode()
'é'
```

##### Application 3

Trouver l'encodage UTF-8 des caractères suivants :

a) `'K'`

b) `'Å'`

c) `'જ'`

##### Application 4

Trouver les caractères des encodages UTF-8 suivants :

a) $C3 B9_{16}$

b) $E0 BE BF_{16}$

______________

[Exercices](./Exercices/Exercices_representation_des_textes_en_machine.md)

______________

[Sommaire](./../README.md)


