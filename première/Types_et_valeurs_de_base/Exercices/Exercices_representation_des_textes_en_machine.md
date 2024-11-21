# Exercices

## Exercice 1

Sur feuille, donner le texte à partir de la séquence hexadécimale ci-dessous à l'aide de la table ASCII :

$43$ $65$ $63$ $69$ $20$ $65$ $73$ $74$ $20$ $75$ $6E$ $20$ $74$ $65$ $78$ $74$ $65$ $21_{16}$ 

## Exercice 2

Sur feuille, donner la séquence hexadécimale du texte ci-dessous à l'aide de la table ASCII :

`Trop bien la NSI`

## Exercice 3

À l'aide des fonctions `ord()`, `chr()`, `bin()`, `hex()` et `int()`, répondre aux questions suivantes :

a) Trouver la représentation binaire du caractère `A`.

b) Trouver la représentation hexadécimale du caractère `x`.

c) Trouver le caractère correspondant à la représentation binaire $01010101$.

d) Trouver le caractère correspondant à la représentation hexadécimale $7A_{16}$.

## Exercice 4

Écrire une fonction ``str_to_ASCII(mot : str)->str`` qui prend en paramètre une chaîne de caractère et renvoie le code ASCII correspondant sous forme de chaîne de caractère.

```python
>>> str_to_ASCII('coucou')
'99 111 117 99 111 117 '
```

## Exercice 5

L'algorithme **rot13** est un algorithme de chiffrement qui consiste à décaler de treize caractères chaque lettres d'un texte.

Par exemple, le mot ``python`` est transformé en ``}\x86\x81u|{`` en utilisant la table ASCII.

Cet algorithme ne décale pas les caractères "non imprimables" donc ne code pas les espaces.

Écrire une fonction ``rot13(mot : str)->str`` qui prend en paramètre une chaîne de caractère et renvoie sous forme de chaîne de caractère le mot chiffré selon l'algorithme de rot13 :

```python
>>> rot13('python')
'}\x86\x81u|{'
```

## Exercice 6

Sans utiliser les méthodes `upper()` et `lower()`, écrire une fonction ``change_casse(caractere : str)->str`` qui prend en paramètre un caractère et renvoie ce même caractère dans l'autre casse.

```python
>>> change_casse('A')
'a'
>>> change_casse('z')
'Z'
```

## Exercice 7

a) Sur Notepad++, écrire dans un fichier texte encodé en UTF-8 le caractère `é`.

b) Convertir le fichier en encodage ANSI (ASCII).

c) Expliquer pourquoi le caractère `é` s'est tranformé en `xE9`.

__________________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 