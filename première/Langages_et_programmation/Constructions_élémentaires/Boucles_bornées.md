# Boucles bornées

## I. Définitions

> [!IMPORTANT]
> Une *boucle* est une construction élémentaire qui permet de répéter une séquence d'instruction.
>
>Nous appelons le *corps de boucle* la séquence d'instruction qui sera répétée.

> [!IMPORTANT]
>Une *boucle bornée* permet de répéter l'exécution du corps de boucle un nombre fixe de fois.

>[!NOTE]
>Nous utilisons les boucles bornées lorsque nous connaissons à l'avance combien de fois le corps de boucle sera exécuté.

## II. Les itérables

### a) Définition

En Python, les boucles bornées s'écrivent en utilisant le mot-clé `for` (*Pour* en français) suivi d'un itérable.

> [!IMPORTANT]
>Un *itérable* est un ensemble fini de valeurs sur laquelle nous pouvons itérer.
>
>*Itérer* revient à parcourir **un à un** les éléments de l'itérable.

Lorsque nous avons besoin d'un itérable, nous utilisons la fonction `range()`.

### b) La fonction range

La fonction `range()` renvoie un itérable.

Elle prend deux paramètres représentant une **borne de début** et une **borne de fin** :

```python
>>> range(2,5)
[2, 3, 4]
```
>[!WARNING]
>La borne de fin est exclue.

#### <ins>Application 1</ins>

Donner, sans utiliser l'ordinateur, le résultat des instructions suivantes :

1. Instruction 1
```python
>>> range(0,10)
```

2. Instruction 2
```python
>>> range(5,10)
```

3. Instruction 3
```python
>>> range(-5,-1)
```

## III. Répéter à l'aide d'un itérable

### a) Syntaxe

En Python, nous pouvons répéter un corps de boucle en parcourant un itérable à l'aide du mot-clé `for`.

>[!TIP]
>Par exemple :
>```python
>a = 0
>for i in range(2,5) :
>    a = a + 1
>```
>
>Cela se traduit en français :
>```
>a est égal à 0
>Pour i allant de 2 à 5, faire :
>   a est égal à a+1
>```
>
>À l'issue de l'exécution du programme précédent, la valeur affectée à la variable `a` est $3$.

#### <ins>Application 2</ins>

Traduire en Français les programmes suivants :

1. Programme 1

```python
for i in range(0,10):
    a = a - 1
```

2. Programme 2

```python
for ind in range(3,6):
    a = a + 5
```

3. Programme 3

```python
for i in range(-5,3):
    a = a + 2
```

#### <ins>Application 3</ins>

Écrire les programmes Python correspondant aux algorithmes suivants :

1. Algorithme 1
```
a est égal à 0
Pour i allant de 0 à 10, faire :
    a est égal à a-5
```

2. Algorithme 2
```
a est égal à 0
Pour j allant de -1 à 20, faire :
    a est égal à a+2
```

3. Algorithme 3
```
a est égal à 0
Pour i allant de 10 à 20, faire :
    a est égal à a-4
```

### b) Indice de boucle

>[!IMPORTANT]
>La variable `i` est un *indice de boucle*. 
>
>Il indique la valeur de l'élément sur lequel nous itérons et est accessible dans le corps de boucle.

>[!TIP]
>Par exemple :
>```python
>a = 0
>for i in range(2,5) :
>    a = a + 1
>```
>
>Dans le programme ci-dessus, la valeur affectée à la variable `i` est égal à :
>
>- $2$ au premier tour de boucle.
>- $3$ au deuxième tour de boucle.
>- $4$ au troisième tour de boucle.

#### <ins>Application 4</ins>

Pour chaque programme de l'application $2$, faire la trace d'exécution en indiquant en plus la valeur de l'indice de boucle.

________

[Exercices](./Exercices/Exercices_boucles_bornees.md)

________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 