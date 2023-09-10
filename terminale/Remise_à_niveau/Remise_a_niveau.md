# Remise à niveau

## I. Définitions, Python, Thonny

Lire : [Première - Prise en main](./../../première/Prise_en_main/Prise_en_main.md)

## II. Entraînement

### a) Types

#### Exercice 1

a) Sans utiliser l'ordinateur, donner le type des valeurs suivantes :

- `8`
- `6.5`
- `"6.5"`
- `'6.5'`
- `False`
- `"True"`
- `""`
- `True`
- `true`
- `5 + 4`
- `"5 + 4"`
- `'"abcd"'`
- `5.5 + 0.3`
- `5.5 + 0.5`
- `5 + 3.14`
- `5 + 3.0`
- `5 / 2`

b) Vérifier, à l'aide de la fonction `type()` et dans la console vos précédentes réponses.

c) Expliquer le type obtenu pour chaque réponse.

#### Exercice 2

a) Sans utiliser l'ordinateur, donner le résultat des expressions suivantes en précisant le type du résultat ou lorsqu'une erreur doit survenir.

- `5 ** 2 - 3`
- `10 < 9`
- `10 <= 10`
- `5 / 2`
- `4 / 2`
- `False and False`
- `4 / 0`
- `4 // 2`
- `4 // 0`
- `4 % 2`
- `4 != 2`
- `5 % 2`
- `True or True`
- `7 + 7 % 2`
- `3 * 3 ** 2`
- `'4' // 2`

b) Vérifier vos résultats dans la console.

### b) Séquences d'instructions

#### Exercice 1

```python
a = 5
b = 3
tmp = a
a = b
b = tmp
```

a) Que vaut les variables $a$ et $b$ à l'issue de l'exécution du programme précédent ?

b) Vérifier votre résultat en utilisant l'outil de déboguage de Thonny et en affichant l'état des variables.

*Rappel : Pour afficher l'état des variables, cliquer sur l'onglet `Affichage` puis cocher `Variables`.*

c) Finalement, expliquer ce que fait ce programme.

### c) Instructions conditionnelles

#### Exercice 1

Ecrire une fonction ``max2( a : int, b : int)-> int`` qui prend en paramètres deux entiers $a$ et $b$ et renvoie l'entier le plus grand.

```python
>>> max2(5,13)
13
```

#### Exercice 2

Ecrire une fonction ``max3( a : int, b : int, c : int )-> int`` qui prend en paramètres trois entiers $a$, $b$ et $c$ et renvoie l'entier le plus grand.

```python
>>> max3(5,7,15)
15
```

### d) Boucles

#### Exercice 1

Ecrire une fonction `puissance_2(n : int)->int` qui prend en paramètre un entier $n$ et renvoie le résultat de $2^n$.

Cette fonction devra utiliser uniquement l'opérateur de multiplication et la boucle `for`.

```python
>>> puissance_2(5)
32
```

#### Exercice 2

Ecrire une fonction `puissance_2(n : int)->int` qui prend en paramètre un entier $n$ et renvoie le résultat de $2^n$.

Cette fonction devra utiliser uniquement l'opérateur de multiplication et la boucle `while`.

```python
>>> puissance_2(5)
32
```

#### Exercice 3

Ecrire une fonction `nombre_chiffre(n : int)->int` qui prend en paramètre un entier et renvoie le nombre de chiffres de cet entier.

```python
>>> nombre_chiffre(34567)
5
```

### e) Chaînes de caractères

#### Exercice 1

Ecrire une fonction `nombre_occurences(mot : str, lettre : str)->int` qui prend en paramètres une chaîne de caractère et un caractère et renvoie comme résultat le nombre de fois qu'apparaît `lettre` dans `mot`.

```python
>>> nombre_occurences('occurence', 'e')
2
```

#### Exercice 2

Considérons la fonction suivante :

```python
def mystere(mot : str, lettre : str)->int :
  resultat = -1
  for i in range(len(mot)) :
    if mot[i] == lettre :
      resultat = i
  return resultat
```
a) Décrire en Français chaque ligne de la fonction.

b) En déduire l'objectif de la fonction.

c) Ecrire la trace d'exécution lorsque nous appelons la fonction avec `coucou` et `o` comme arguments.

### f) Listes

#### Exercice 1

Ecrire une fonction `maximum_liste(l : list)->int` qui prend en paramètre une liste `l` et renvoie comme résultat l'entier maximum de `l` :

```python
>>> maximum_liste([4,7,3,9,2])
9
```

#### Exercice 2

Ecrire une fonction `table_de_multiplication(n : int)->list` qui prend en paramètre un entier et renvoie comme résultat la table de multiplication de $n$ sous forme de liste.

```python
>>> table_de_multiplication(2)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

#### Exercice 3

Ecrire une fonction `impairs(n : int)->list` qui prend en paramètre un entier et renvoie comme résultat une liste comprenant tous les entiers impairs de $0$ jusqu'à $n$.

```python
>>> impairs(15)
[1, 3, 5, 7, 9, 11, 13, 15]
```

#### Exercice 4

Considérons la liste suivante :

```python
li = [["a", "b", "c", "d"],
      [1, 2, 3, 4],
      ["I", "II", "III", "IV"]]
```

1. Que renvoie l'instruction : `>>> li[0]` ?

2. Que renvoie l'instruction : `>>> li[1]` ?

3. Que renvoie l'instruction : `>>> li[0][1]` ?

4. Que renvoie l'instruction : `>>> li[1][0]` ?

#### Exercice 5

Ecrire une fonction `affiche_labyrinthe(labyrinthe : list)->None` qui prend en paramètre un labyrinthe sous forme de liste de listes et l'affiche proprement dans la console à l'aide des caractères '█' et ' '.

```python
>>> labyrinthe = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 1, 1, 0, 1, 1, 1, 0, 1],
              [1, 0, 0, 0, 1, 0, 0, 0, 1],
              [1, 0, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 1, 1]]
>>> affiche_labyrinthe(labyrinthe)
██████████████████
                ██
██████  ██████  ██
██      ██      ██
██  ██████████████
██                
██████████████████
```

### g) Dictionnaires

Ecrire une fonction `occurences_par_lettre(mot : str)->dict` qui prend en paramètre une chaîne de caractère et renvoie un dictionnaire dont les clés sont des caractères de la chaîne et les valeurs le nombre de fois qu'apparaissent ces caractères :

```python
>>> mot = 'bienvenue'
>>> occurences_par_lettre(mot)
{'b' : 1, 'i' : 1, 'e' : 3, 'n' : 2, 'v' : 1, 'u' : 1}
```

_______________

[Sommaire](./../README.md)