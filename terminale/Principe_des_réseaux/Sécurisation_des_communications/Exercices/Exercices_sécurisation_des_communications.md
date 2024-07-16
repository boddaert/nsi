# Exercices

Pour la totalité des exercices, nous utiliserons comme alphabet la constante :

```python
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
```

## Exercice 1

Écrire une fonction ``chiffre_cesar(message_clair : str, cle : int)->str`` qui prend en paramètres un message clair et une clé de chiffrement et renvoie le message chiffré selon la méthode du Chiffre de César :

```python
>>> chiffre_cesar("ATTAQUEZLECHATEAU", 2)
'CVVCSWGBNGEJCVGCW'
```

## Exercice 2

Écrire une fonction ``dechiffre_cesar(message_chiffre : str, cle : int)->str`` qui prend en paramètres un message chiffré et une clé de déchiffrement et renvoie le message clair :

```python
>>> dechiffre_cesar('CVVCSWGBNGEJCVGCW', 2)
'ATTAQUEZLECHATEAU'
```

## Exercice 3

Écrire une fonction ``chiffre_vigenere(message_clair : str, cle : tuple)->str`` qui prend en paramètres un message clair et un tuple de clé de chiffrement et renvoie le message chiffré selon la méthode du chiffrement de Vigenère :

```python
>>> chiffre_vigenere("ATTAQUEZLECHATEAU", (2,4,1))
'CXUCUVGDMGGICXFCY'
```

## Exercice 4

Écrire une fonction ``dechiffre_vigenere(message_chiffre : str, cles : tuple)->str`` qui prend en paramètres un message chiffré et un tuple de clés de déchiffrement et renvoie le message clair :

```python
>>> dechiffre_vigenere('CXUCUVGDMGGICXFCY', (2,4,1))
'ATTAQUEZLECHATEAU'
```

## Exercice 5

Le chiffrement XOR (ou *Ou Exclusif*) est un chiffrement symétrique qui repose sur l'opération logique du XOR.

> *Rappel sur la table de vérité du Ou exclusif :*
> 
> | a XOR b | 0   | 1   |
> | :-------: | :---: | :---: |
> | 0       | 0   | 1   |
> | 1       | 1   | 0   |
> 
> En Python, nous utilisons l'opérateur ``^``:
> 
> ```python
> >>> 0 ^ 1
> 1
> ```

Le principe de ce chiffrement est le suivant :

1. Encoder sous forme binaire le message clair et la clé.

2. Réaliser un Ou Exclusif bit à bit sur chacun des bits du message avec la clé.

Par exemple, si mon message est `0101` et si ma clé est `1001` alors le message chiffré sera `1100` :

| Message clair   | ``0101`` |
| --------------- | -------- |
| Clé             | ``1001`` |
| Message chiffré | ``1100`` |

De plus, comme il s'agit d'un système de chiffrement symétrique, en réeffectuant l'opération Ou Exclusif entre la clé et le message chiffré, je retrouve bien mon message d'origine ``0101``.

Par la suite, nous utiliserons les positions des lettres dans la variable ``alphabet`` pour obtenir la représentation binaire d'une lettre : 

- La lettre ``A`` d'indice $0$ a pour représentation binaire ``00000``

- La lettre ``B`` d'indice $1$ a pour représentation binaire ``00001``

a) En se servant de la fonction ``bin()``, écrire une fonction ``repr_bin(mot : str)->list`` qui prend en paramètre une chaîne de caractères et renvoie une liste dont les éléments sont les représentations binaires des lettres du mot (attention à ce que les représentations binaires aient la même taille) :

```python
>>> bin(3)
'ob11'
>>> bin(3)[:2]
'11'
>>> repr_bin('ATTAQUEZ')
['00000', '10011', '10011', '00000', '10000', '10100', '00100', '11001']
>>> repr_bin('NSI')
['01101', '10010', '01000']
```

b) Écrire une fonction ``xor(x : str, y : str)->str`` qui prend en paramètres deux représentations binaires et renvoie le résultat de l'opération du Ou Exclusif :

```python
>>> xor('0101', '1001')
'1100'
```

c) Écrire une fonction ``chiffre_xor(message_clair : list, cle : list)->list`` qui prend en paramètres la représentation binaire du message clair et la représentation binaire de la clé et renvoie une liste dont les éléments sont les représentations binaire du message chiffré selon la méthode du chiffrement XOR :

```python
>>> chiffre_xor(repr_bin("ATTAQUEZ"), repr_bin("NSI"))
['01101', '00001', '11011', '01101', '00010', '11100', '01001', '01011']
```

d) Le chiffrement XOR étant un chiffrement symétrique, nous devrions retrouver la représentation binaire du message clair à partir de la clé et de la représentation binaire du message chiffré :

```python
>>> chiffre_xor(['01101', '00001', '11011', '01101', '00010', '11100', '01001', '01011'], repr_bin('NSI'))
['00000', '10011', '10011', '00000', '10000', '10100', '00100', '11001']
```

## Exercice 6

L'objectif de cet exercice est de découvrir une méthode permettant de décrypter le Chiffre de César.

##### Méthode : Analyse de fréquence

Supposons que le message chiffré envoyé est écrit en langue française et que la lettre qui apparaît le plus souvent dans ce message est `E`.

L'idée est de calculer les occurences de chaques lettres chiffrées et de repérer celle qui en a le plus.

Puis, de retrouver le nombre $n$ de décalages nécessaire pour chiffrer cette lettre en `E`, $n$ est alors la clé.

a) Écrire une fonction `occ(message_chiffre : str)->dict` qui prend en paramètre le message chiffré et renvoie un dictionnaire dans lequel la clé est la lettre et la valeur, son nombre d'occurences :

```python
>>> occ('EQODQF')
{'E' : 1, 'Q' : 2, 'O' : 1, 'D' : 1, 'F' :1}
```

b) Écrire une fonction `max_occ(occ : dict)->str` qui prend en paramètres le dictionnaire des occurences et renvoie la lettre la plus fréquente :

```python
>>> max_occ(occ('EQODQF'))
'Q'
```

c) Écrire une fonction `trouve_cle(lettre : str)->int` qui prend en paramètre une lettre et renvoie le nombre de décalages jusqu'à `E` :

```python
>>> trouve_cle('Q')
12
```

d) Écrire une fonction `decrypter_cesar_analyse_freq(message_chiffre : str)->str` qui prend en paramètre le message chiffré et renvoie le message clair en réutilisant les fonctions précédentes :

```python
>>> decrypter_cesar_analyse_freq('EQODQF')
'SECRET' 
```

e) Dans quel cas l'analyse de fréquence ne fonctionne pas ?

## Exercice 7

Pour cet exercice, télécharger et ouvrir le fichier [merkle.py](./src/merkle.py).

Pour cet exercice, ajouter dans la variable ``alphabet`` les entiers de zéro à neuf et l'espace.

Le puzzle de Merkle est une méthode permettant de s'échanger une clé de chiffrement de manière (un peu) sécurisée. Voici son principe :

1. Alice génère une grande quantité de messages de la forme ``identifiant:i cle:k`` avec $i$ un entier unique et $k$ un entier aléatoire.

2. Alice chiffre chacun de ces messages (Chiffre de César) en utilisant une clé de chiffrement différente.

3. Alice envoie l'intégralité de ces messages à Bob.

4. Bob choisis aléatoirement un message parmi tous et le décrypte.

5. Bob trouve alors un identifiant et une clé et envoie à Alice l'identifiant qu'il a trouvé.

6. Alice repère la clé associée à cet identifiant.

7. Alice et Bob possèdent tous les deux une clé de chiffrement.

##### Etape 1 Alice

a) Écrire une fonction ``genere_messages(n : int)->list`` qui prend en paramètre un entier $n$ et renvoie une liste de $n$ messages de la forme ``identifiant:i cle:k`` où $k$ est un entier aléatoire :

```python
>>> messages = genere_messages(10)
>>> messages
['identifiant:0 cle:6799100', 'identifiant:1 cle:689143', 'identifiant:2 cle:66654', 'identifiant:3 cle:633728', 'identifiant:4 cle:656285', 'identifiant:5 cle:267157', 'identifiant:6 cle:96664', 'identifiant:7 cle:319894', 'identifiant:8 cle:23433', 'identifiant:9 cle:702382']
```

b) Écrire une fonction ``chiffrer_messages(messages : list)->list`` qui prend en paramètres une liste de messages clairs et renvoie une liste de messages chiffrés selon le système du Chiffre de César avec pour chaque message une clé différente :

```python
>>> messages_chiffres = chiffrer_messages(messages)
>>> messages_chiffres
['hcdmsheh:ms9 zbkd956880  ', 'nijsynknfsye64hqjeacd698', '2yz7c2 2v7cumjx5zuqqqpo', '834ci8580ci tp2a4 wttxsy', '2yz7c2 2v7cuojx5zuqpqmsp', 'topy3tqtly3kf:nwpkcghbfh', '723bh747 bhzvo1:3zyvvvt', '834ci8580ci xp2a4 trzyzu', ' vw4: x s4:rpgu2wrjklkk', '723bh747 bhzyo1:3zwprsxr']
```

##### Etape 2 Bob

c) Écrire une fonction ``choisir_message(messages_chiffres : list)->str`` qui prend en paramètre une liste de messages chiffrés et renvoie un message choisis aléatoirement :

```python
>>> message_choisis = choisir_message(messages_chiffres)
>>> message_choisis
'2yz7c2 2v7cuojx5zuqpqmsp'
```

d) Écrire une fonction ``decrypter(message_choisis : str)->str`` qui prend en paramètre le message choisis chiffré et renvoie le message en clair (sachant que Bob connaît la forme du message) :

```python
>>> decrypter(message_choisis)
'identifiant:4 cle:656285'
```

##### Etape 3 Simulation

e) Compléter la fonction ``simulation`` afin de correspondre au principe du puzzle de Merkle.

## Exercice 8

a) Installer la bibliothèque ``py-enigma`` permettant de simuler le fonctionnement d'une machine Enigma en Python.

Pour l'installer :

1. Cliquer sur ``Outils`` puis ``Open System shell``

2. Écrire dans la console qui vient de s'afficher la commande ``pip install py-enigma``

b) Télécharger dans votre répertoire commun le fichier [enigma_machine.py](./src/enigma_machine.py)

Pour configurer la position des rotors :

```python
>>> machine.set_display('PIX')
```

Pour afficher la position des rotors :

```python
>>> machine.get_display()
'PIX'
```

Pour chiffrer une lettre :

```python
>>> machine.key_press('A')
'I'
```

a) Quelle est maintenant la position des rotors ?

b) Quelle est maintenant la lettre chiffrée lorsque j'appuie sur ``'A'`` ?

Le déchiffrement se fait de la manière inverse (il faut que la position des rotors soit la même) :

```python
>>> machine.set_display('PIX')
>>> machine.key_press('I')
'A'
```

c) Écrire une fonction ``chiffre_enigma(message_clair : str, machine : EnigmaMachine, pos_rotors : str)->str`` qui prend en paramètres un message clair, une machine Enigma configurée et la position des rotors. Cette fonction renvoie le message chiffré.


_______________

[Sommaire](./../../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 