# Chaînes de caractères

## I. Définition

Un *caractère* est un symbole écrit lié à un système d'écriture.

En Python, le caractère est encadré par des guillements simples ou doubles et possède le type `str`.

Une *chaîne de caractère* est un ensemble de caractères.

Python ne fait pas la différence entre les caractères "imprimables" et les caractères "non imprimables" :

```python
>>> type(" ")
<class = 'str'>
```

Une *chaîne de caractère vide* est une chaîne de caractère ne contenant aucun caractère.

## II. Opérations sur les chaînes de caractère

### a) Taille

La *taille* d'une chaîne de caractère est le nombre de caractère contenu dans la chaîne.

Elle peut être connue avec la fonction `len()` :

```python
>>> len("hello world")
11
```

##### Application 1

En utilisant la console Python, trouver la taille des chaînes de caractères suivantes :

a) `'Bonjour a tous'`

b) `'Numérique et Sciences Informatique'`

c) `'-\_("_")_/-'`

### b) Accès au *ième* caractère

Nous accédons à un caractère de la chaîne selon son indice (ou sa position) dans la chaîne.

L'*indice d'un caractère* dans la chaîne est le numéro de place du caractère.

Nous mettons l'indice du caractère que nous souhaitons obtenir entre crochets :

```python
>>> mot = "hello world"
>>> mot[2]
'l'
```

Le premier caractère est d'indice $0$.

```python
>>> mot[0]
'h'
```

##### Application 2

Donner sans utiliser l'ordinateur, le résultat des instructions suivantes :

a)
```python
>>> mot[5]
...
```

b)
```python
>>> mot[9]
...
```

c)
```python
>>> mot[1]
...
```

##### Application 3

Donner l'instruction permettant d'obtenir :

a) La lettre d'indice $7$.

b) La dernière lettre en utilisant la taille de la chaîne.

### c) Test d'appartenance

Nous pouvons vérifier si une chaîne de caractère est contenu dans une chaîne à l'aide du mot-clé `in`.

```python
>>> 'lo' in mot
True
```

Le test d'appartenance renvoie comme résultat un booléen.

##### Application 4

Vérifier, dans la console Python et à l'aide du mot-clé `in`, si :

a) La chaîne `rld` est contenue dans `mot`.

b) La chaîne `p` est contenue dans `mot`.

c) La chaîne `hello` est contenue dans `mot`.

### d) Concaténation

La *concaténation* de deux chaînes de caractère consiste à créer une chaîne de caractère contenant les caractères des deux chaînes.

Nous pouvons concaténer deux chaînes de caractères en utilisant l'opérateur `+` :

```python
>>> mot_1 = "hello"
>>> mot_2 = " world"
>>> mot = mot_1 + mot_2
>>> mot
'hello world'
```

##### Application 5

Concaténer :

a) La chaîne `Bonjour a` avec la chaîne `tous`.

b) La chaîne `Numérique` avec la chaîne `Sciences` puis avec la chaîne `Informatiques`.

### e) Découpage ou *slicing* (hors programme)

Le *slicing* permet d'obtenir une sous-chaîne à partir d'une chaîne de caractère.

Le slicing en Python s'écrit  : ``chaine[debut:fin]``  avec ``debut`` l'indice de la première coupe et ``fin`` l'indice de la seconde coupe (exclue) :

```python
>>> mot = "hello world"
>>> mot[2:6]
'llo '
```

##### Application 6

Donner sans utiliser l'ordinateur, le résultat des instructions suivantes :

a)
```python
>>> mot[0:2]
...
```

b)
```python
>>> mot[0:11]
...
```

## III. Mutabilité

Une valeur est dite *mutable* si elle peut être modifiée.

Les chaînes de caractères ne sont pas mutables.

Nous ne pouvons pas modifier les caractères d'une chaîne :

```python
>>> mot = "hello world"
>>> mot[3] = "c"
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

##### Application 7

Essayer à votre tour de modifier la valeur affectée à la variable `mot` en changeant la lettre `w` en `h`.

## IV. Parcours de chaîne

Un *parcours de chaîne* consiste à visiter un à un tous les caractères de la chaîne.

Nous parcourons les chaînes de caractères en utilisant les boucles.

Comme nous connaissons à l'avance la taille d'une chaîne, nous connaissons à l'avance le nombre de tour de boucle nécessaire au parcours : Nous utilisons donc la boucle `for`.

Il existe deux façons d'utiliser la boucle `for` pour parcourir les chaînes de caractères :

- Le parcours par indice.

- Le parcours par élément.

### a) Parcours par indice

Dans le parcours par indice, nous parcourons les caractères indice par indice :

```python
1. mot = "hello"
2. for i in range(len(mot)) :
3.   lettre = mot[i]
```

Trace d'exécution du programme donné ci-dessus:

| Numéro de ligne | Valeur affectée à $i$ | Valeur affectée à $lettre$ |
| :---: | :---: | :---: |
| $1$ | / | / |
| $2$ | $0$ | / |
| $3$ | $0$ | $h$ |
| $2$ | $1$ | $h$ |
| $3$ | $1$ | $e$ |
| ... | ... | ... |

##### Application 8

Compléter la trace d'exécution précédente.

### b) Parcours par élément

Dans le parcours par élément, nous parcourons caractère par caractère :

```python
1. mot = "world"
2. for caractere in mot :
3.   lettre = caractere
```

| Numéro de ligne | Valeur affectée à $caractere$ | Valeur affectée à $lettre$ |
| :---: | :---: | :---: |
| $1$ | / | / |
| $2$ | $w$ | / |
| $3$ | $w$ | $w$ |
| $2$ | $o$ | $w$ |
| $3$ | $o$ | $o$ |
| ... | ... | ... |


##### Application 9

Compléter la trace d'exécution précédente.
___________

[Feuille d'exercice](./Exercices/Exercices_chaines_de_caractere.md)

___________

[Sommaire](./../README.md)