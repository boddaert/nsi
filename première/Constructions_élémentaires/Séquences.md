# Séquences d'instructions

Jusqu'à maintenant, nous avons essentiellement travaillé avec la console Python sur le mode interactif de Thonny.

Ce mode est très utile pour tester nos instructions mais celui-ci n'est pas destiné à écrire des programmes.

## I. Définitions

Un *programme informatique* est un texte composé d'intructions.

Une *instruction* désigne une étape dans un programme. Elle correspond à une action que l'ordinateur réalise lorsqu'il exécute le programme.

Les programmes sont très souvent constitués de plusieurs instructions, cela constitue une *séquence d'instruction*.

Nous associons une ligne de code à une instruction du programme.

## II. Ordre d'exécution

L'ordre d'exécution d'une séquence d'instruction est le même que l'ordre de lecture. 

C'est à dire que l'instruction situé à la ligne $1$ sera exécutée en premier, puis celle située à la ligne $2$ en deuxième, et ainsi de suite ...

Nous pouvons le vérifier très facilement en écrivant un programme comportant une séquence d'instruction dans l'éditeur de texte de Thonny :

```python
a = 10
a = a + 1
```

Puis, après exécution, en vérifiant la valeur affectée à la variable `a` dans la console Python :

```python
>>> a
11
```

##### Application 1

Recopier le programme de l'exemple précédent et vérifier à votre tour la valeur affectée à la variable `a` dans la console Python.

## III. Trace d'exécution

Une trace d'exécution, comme son nom l'indique, permet de garder une trace de l'état du programme à chaque étape de celui-ci.

Nous représentons la trace d'exécution d'un programme dans un tableau :

| Numéro de ligne | Valeur affectée à la variable ...|  Valeur affectée à la variable ... |
| --- | --- | --- |
| | | |

Par exemple, pour le programme suivant :

```python
a = 10
a = a + 1
b = a - 1
```

Nous obtenons la trace d'exécution suivante :

| Numéro de ligne | Valeur affectée à la variable `a` | Valeur affectée à la variable `b` |
| --- | --- | --- |
| 1 | $10$ | / |
| 2 | $11$ | / |
| 3 | $11$ | $10$ |

##### Application 2

Donner la trace d'exécution du programme suivant :

```python
a = 9
b = 1
a = a - b
b = b + 1
a = a - b
```

_______

[Feuille d'exercice](./Exercices/Exercices_sequences.md)
_______

[Sommaire](./../README.md)