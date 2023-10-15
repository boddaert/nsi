# Chaînes de caractères

## I. Définition

Une chaîne de caractère est une valeur encadrée par des *guillemets doubles* (ou des guillemets simples) : $`"a"`$  ou $`'a'`$.

Une chaîne de caractère peut contenir plusieurs caractères : $`"acdc"`$.

En Python, les chaînes de caractère sont représentés par le type ``str``  :

```python
>>> type("acdc")
<class 'str'>
```

## II. Opérations sur les chaînes de caractère

### a) Taille

La *taille* d'une chaîne de caractère est son nombre de caractère.

Elle peut être connue avec la fonction `len()` :

```python
>>> len("hello world")
11
```

##### Application 1

En utilisant la console Python, trouver la taille des chaînes de caractères suivantes :

- `'Bonjour a tous'`

- `'Numérique et Sciences Informatique'`

- `'-\_("_")_/-'`

### b) Accès au *ième* caractère

Nous pouvons *accèder* à un caractère de la chaîne d'après sa position.

La position d'un caractère dans la chaîne est équivalent à son *indice*.

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

a) La lettre `o`.

b) La lettre d'indice $7$.

c) La dernière lettre en utilisant la taille de la chaîne.

### c) Test d'appartenance

Nous pouvons vérifier si une chaîne de caractère est présent dans une chaîne à l'aide du mot-clé `in`.

```python
>>> 'lo' in mot
True
```

Le test d'appartenance renvoie comme résultat un booléen.

##### Application 4

Vérifier à l'aide du mot-clé `in`, dans la console Python, si :

a) La chaîne `rld` est contenue dans `mot`.

b) La chaîne ` rld` est contenue dans `mot`.

c) La chaîne `hello` est contenue dans `mot`.

### d) Concaténation

La *concaténation* de deux chaînes revient à les coller l'une après l'autre pour n'en former qu'une.

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

Le *slicing* permet d'obtenir une sous-chaîne.

Le slicing en Python s'écrit  : ``chaine[debut:fin]``  avec ``debut`` l'indice de la première coupe et ``fin`` l'indice de la seconde coupe (exclue) :

```python
>>> mot = "hello world"
>>> mot[2:6]
'llo '
```

##### Application 6

Donner sans utiliser l'ordinateur, le résultat des instructions suivantes :

```python
>>> mot[0:2]
...
```

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

Un *parcours de chaîne* revient à visiter un à un tous les caractères de la chaîne.

Nous parcourons les chaînes de caractères en utilisant les boucles.

Comme nous connaissons à l'avance la taille d'une chaîne, nous connaissons à l'avance le nombre de tour de boucle nécessaire au parcours.

Nous utilisons donc la boucle `for`.

Il existe deux façons d'utiliser la boucle `for` pour parcourir les chaînes de caractères :

- Le parcours par indice.

- Le parcours par élément.

### a) Parcours par indice

Dans le parcours par indice, nous allons parcourir les caractères selon leur indice :

```python
mot = "hello world"
for i in range(len(mot)) :
  lettre = mot[i]
```

L'indice de boucle `i` aura comme valeur :

- $0$ au premier tour de boucle.
- $1$ au deuxième tour de boucle.
- ...
- $10$ au dernier tour de boucle.

Donc la valeur de `mot[i]` sera respectivement :

- `h` au premier tour de boucle.
- `e` au deuxième tour de boucle.
- ...
- `d` au dernier tour de boucle.

##### Application 8

Donner la trace d'exécution du programme suivant :

```python
mot = "hello world"
for i in range(len(mot)) :
  lettre = mot[i]
```

### b) Parcours par élément

Dans le parcours par élément, nous parcourons simplement tous les caractères de la chaîne :

```python
mot = "hello world"
for caractere in mot :
  lettre = caractere
```

Il n'y a pas d'indice de boucle dans ce parcours mais la valeur affectée à la variable `caractere` sera :

- `h` au premier tour de boucle.
- `e` au deuxième tour de boucle.
- ...
- `d` au dernier tour de boucle.

##### Application 9

Donner la trace d'exécution du programme suivant :

```python
mot = "hello world"
for caractere in mot :
  lettre = caractere
```
___________

[Feuille d'exercice](./Exercices/Exercices_chaines_de_caractere.md)

___________

[Sommaire](./../README.md)