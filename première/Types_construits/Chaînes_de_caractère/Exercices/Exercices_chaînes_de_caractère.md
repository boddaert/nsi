
# Exercices

## Exercice 1

Considérons la chaîne de carcatère ``prenom = 'timoleon'``.

a) Écrire l'instruction permettant d'obtenir la taille de `prenom`.

b) Écrire l'instruction permettant d'obtenir le premier caractère de `prenom`.

c) Écrire l'instruction permettant d'obtenir le dernier caractère de `prenom`.

d) Écrire le programme permettant d'afficher tous les caractères de `prenom` un à un en réalisant un parcours par indice.

e) Écrire le programme permettant d'afficher tous les caractères de `prenom` un à un en réalisant un parcours par élément.

## Exercice 2

Écrire la fonction `contient(mot : str, lettre : str)-> bool` qui prend en paramètres une chaîne de caractère et un caractère et renvoie $True$ si `lettre` est présent dans `mot`.

Cette fonction ne devra pas utiliser l'instruction `in` (sauf éventuellement pour `in range()`).

Écrire deux versions de cette fonction, la première en utilisant la boucle `for` et la seconde en utilisant la boucle `while`.

```python
>>> contient('bonjour', 't')
False
>>> contient('bonjour', 'b')
True
```

## Exercice 3

Considérons la fonction suivante :

```python
1. def mystere(mot : str, lettre : str)->int :
2.   resultat = -1
3.   for i in range(len(mot)) :
4.     if mot[i] == lettre :
5.       resultat = i
6.   return resultat
```

a) Décrire en Français chaque ligne de la fonction.

b) En déduire l'objectif de la fonction.

## Exercice 4

Écrire une fonction `nombre_occurences(mot : str, lettre : str)->int` qui prend en paramètres une chaîne de caractère et un caractère et renvoie comme résultat le nombre de fois qu'apparaît `lettre` dans `mot`.

```python
>>> nombre_occurences('occurence', 'e')
2
```

## Exercice 5

Écrire une fonction `etoiles(mot : str)->str` qui prend en paramètre une chaîne de caractère et renvoie comme résultat une nouvelle chaîne équivalente à celle passée en paramètre mais avec en plus le caractère `*` entre chaque caractère de la chaîne.

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

Écrire une fonction `reduit(mot : str)-> str` qui prend en paramètre une chaîne de caractère et renvoie comme résultat une nouvelle chaîne équivalente à celle passée en paramètre mais sans le premier ni le dernier caractère.

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

Écrire une fonction `maj(mot : str)->str` qui prend en paramètre une chaîne de caractère et renvoie cette même chaîne en majuscule.

```python
>>> maj('nsi')
'NSI'
```

## Exercice 9 (Difficile)

Pour savoir si un caractère est en majuscule ou en minuscule :

```python
>>> lettre = "u"
>>> lettre.isupper()
False
>>> lettre.islower()
True
```

Écrire une fonction `change_casse(mot : str)->str` qui prend en paramètre une chaîne de caractère et renvoie comme résultat cette même chaîne en changeant la casse.

```python
>>> change_casse('Bonjour A Tous')
'bONJOUR a tOUS'
```
______________

[Sommaire](./../../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 