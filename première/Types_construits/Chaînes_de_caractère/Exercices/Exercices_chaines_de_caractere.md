
# Exercices

## Exercice 1

Considérons la chaîne de carcatère ``prenom = 'timoleon'``.

a) Ecrire l'instruction permettant d'obtenir la taille de `prenom`.

b) Ecrire l'instruction permettant d'obtenir le premier et le dernier caractère de `prenom`.

c) Ecrire le programme permettant d'affecter dans une variable `lettre` tous les caractères de `prenom`en réalisant un parcours par indice.

d) Ecrire le programme permettant d'affecter dans une variable `lettre` tous les caractères de `prenom`en réalisant un parcours par élément.

## Exercice 2

Ecrire la fonction `contient(mot : str, lettre : str)-> bool` qui prend en paramètres une chaîne de caractère et un caractère et renvoie $True$ si `lettre` est présent dans `mot`.

Cette fonction ne devra pas utiliser l'instruction `in`.

Ecrire deux versions de cette fonction, la première en utilisant la boucle `for` et la seconde en utilisant la boucle `while`.

```python
>>> contient('bonjour', 't')
False
>>> contient('bonjour', 'b')
True
```

## Exercice 3

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

## Exercice 4

Ecrire une fonction `nombre_occurences(mot : str, lettre : str)->int` qui prend en paramètres une chaîne de caractère et un caractère et renvoie comme résultat le nombre de fois qu'apparaît `lettre` dans `mot`.

```python
>>> nombre_occurences('occurence', 'e')
2
```

## Exercice 5

Ecrire une fonction `etoiles(mot : str)->str` qui prend en paramètre une chaîne de caractère et renvoie comme résultat une nouvelle chaîne équivalente à celle passée en paramètre mais avec en plus le caractère `*` entre chaque caractère de la chaîne.

```python
>>> etoiles('La guerre des étoiles')
'L*a* *g*u*e*r*r*e* *d*e*s* *é*t*o*i*l*e*s'
```

## Exercice 6

Expliquer l'erreur suivante :

```python
>>> chaine = "3"
>>> chaine + 2
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

## Exercice 7

Ecrire une fonction `reduit(mot : str)-> str` qui prend en paramètre une chaîne de caractère et renvoie comme résultat une nouvelle chaîne équivalente à celle passée en paramètre mais sans le premier ni le dernier caractère.

```python
>>> reduit('bonjour')
'onjou'
```

## Exercice 8

Il est possible de rendre majuscule une lettre minuscule et vice-versa :

```python
>>> lettre = "u"
>>> lettre.upper()
'U'
>>> lettre.lower()
'u'
```

Ecrire une fonction `maj(mot : str)->str` qui prend en paramètre une chaîne de caractère et renvoie cette même chaîne en majuscule.

```python
>>> maj('nsi')
'NSI'
```

## Exercice 9

Pour savoir si un caractère est en majuscule ou en minuscule :

```python
>>> lettre = "u"
>>> lettre.isupper()
False
>>> lettre.islower()
True
```

Ecrire une fonction `change_casse(mot : str)->str` qui prend en paramètre une chaîne de caractère et renvoie comme résultat cette même chaîne en changeant la casse.

```python
>>> change_casse('Bonjour A Tous')
'bONJOUR a tOUS'
```
______________

[Sommaire](./../../../README.md)