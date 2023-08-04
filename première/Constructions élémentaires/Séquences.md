# Séquences d'instructions

Jusqu'à maintenant, nous avons essentiellement travaillé avec la console Python sur le mode interactif de Thonny.

Ce mode est très utile pour tester nos instructions mais celui-ci n'est pas destiné à écrire des programmes.

## I. Définitions

Un *programme informatique* est un texte composé d'intructions et d'opérations.

Une *instruction* désigne une étape dans un programme. Elle correspond à une action que l'ordinateur réalise lorsqu'il l'exécute.

Les programmes sont très souvent constitués de plusieurs instructions, cela constitue une *séquence d'instruction*.

On associe généralement une ligne de code à une instruction du programme.

## II. Ordre d'exécution

Lors de l'exécution d'une séquence d'instruction, l'ordinateur effectue les actions les unes après les autres dans l'ordre de lecture du programme. 

C'est à dire que l'instruction situé à la ligne 1 sera exécutée en premier, puis celle située à la ligne 2 en deuxième, et ainsi de suite ...

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

Une trace d'exécution est représentée par un tableau :

| Numéro de ligne | Nom de variable | Valeur affectée |
| --- | --- | --- |
| | | |

Par exemple, pour le programme suivant :

```python
a = 10
a = a + 1
b = a - 1
```

Nous obtiendrions la trace d'exécution suivante :

| Numéro de ligne | Valeur affectée à `a` | Valeur affectée à `b` |
| --- | --- | --- |
| 1 | 10 | / |
| 2 | 11 | / |
| 3 | 11 | 10 |

##### Application 2

Donner la trace d'exécution du programme suivant :

```python
a = 9
b = 1
a = a - b
b = b + 1
a = a - b
```
 
## Exercices

### Exercice 1

Pour chacun des programmes suivants, donner la trace d'exécution.:

a) Programme 1

```python
a = 3
b = 9
c = a * a
d = b - c
```

b) Programme 2

```python
a = 10
b = a // 2
d = a + b
```

c) Programme 3

```python
a = 2
b = 5 ** a
d = b // 2
```

d) Programme 4

```python
a = 30
b = 50
c = b - a
d = c // 2 + a
```

e) Programme 5

```python
a = 10
b = a + 1
c = b + 1
d = a + b + c
```

### Exercice 2

Pour chacun des programmes de l'exercice 1 :

- Ecrire le programme dans l'éditeur de texte en mode programmation de Thonny.

- Aller dans l'onglet `Affichage` et cocher `Variables`. Une nouvelle fenêtre à droite de l'écran s'ouvre.

- Exécuter ligne par ligne le programme en utilisant l'outil de `Débogueur` (le bouton à droite de celui d'exécution).

_______

Leçon 5 : [Fonctions 1](./Fonctions_1.md)