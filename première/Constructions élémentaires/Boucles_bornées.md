# Boucles bornées

## I. Définition

Une *boucle* est une construction élémentaire qui permet de répéter une séquence d'instruction.

Nous appelons le *corps de boucle* la séquence d'instruction qui sera répétée.

Il s'agit d'une *boucle bornée* lorsque nous connaissons à l'avance combien de fois le corps de boucle sera exécuté.

En Python, les boucles bornées s'écrivent en utilisant le mot-clé `for` (*Pour* en Français) suivi d'un itérable.

## II. Les itérables

### a) Définition

Un *itérable* est une valeur sur laquelle nous pouvons parcourir un à un les éléments qui le compose.

Un itérable est un *ensemble fini*, c'est-à-dire qu'il comporte un début et une fin.

Lorsque nous avons besoin d'un itérable, nous utilisons la fonction `range()`.

### b) La fonction range

La fonction `range()` renvoie un itérable. Elle prend deux paramètres représentant une borne de début et une borne de fin :

```python
>>> range(2,5)
[2, 3, 4]
```

La borne de fin est exclue.

##### Application 1

Donner, sans utiliser l'ordinateur, le résultat des instructions suivantes :

```python
>>> range(0,10)
```

```python
>>> range(5,10)
```

```python
>>> range(-5,-1)
```

## III. Répéter à l'aide d'un itérable

### a) Syntaxe

En Python, nous pouvons répéter un corps de boucle en parcourant un itérable :

```python
a = 0
for i in range(2,5) :
    a = a + 1
```

A l'issue de l'exécution du programme précédent, la valeur affectée à la variable `a` est $3$.

En Français,cela se traduirait par :

- Pour `i` allant de $2$ à $5$, j'ajoute $1$ à `a`.

##### Application 2

Traduire en Français les programmes suivants :

a) Programme 1

```python
for i in range(0,10):
    a = a - 1
```

b) Programme 2

```python
for ind in range(3,6):
    a = a + 5
```

c) Programme 3

```python
for i in range(-5,3):
    a = a + 2
```

##### Application 3

Ecrire les programmes Python correspondant aux phrases suivantes :

a) Phrase 1

- Pour `i` allant de $0$ à $10$, je retire $5$ à `a`.

b) Phrase 2

- Pour `j` allant de $-1$ à 20, j'ajoute $2$ à `a`.

c) Phrase 3

- Pour `i` allant de $10$ à $20$, je retire $4$ à `a`.

### b) Indice de boucle

La variable `i` est un *indice de boucle*. 

Il indique la valeur de l'élément sur lequel nous itérons et est accessible dans le corps de boucle.

Avec l'exemple précédent, la valeur affectée à la variable `i` :

- Vaut $2$ au premier tour de boucle.
- Vaut $3$ au deuxième tour de boucle.
- Vaut $4$ au troisième tour de boucle.

##### Application 4

Pour chaque programme de l'application 2, donner la valeur de l'indice de boucle pour chaque tour de boucle.
________

[Feuille d'exercice](./Exercices/Exercices_boucles_bornees.md)

________

[Sommaire](./../../première/)