# Séquences d'instructions

Jusqu'à maintenant, nous avons essentiellement travaillé avec la console Python sur le mode interactif de Thonny.

Ce mode est très utile pour tester nos instructions mais celui-ci n'est pas destiné à écrire des programmes.

## I. Définitions

> [!IMPORTANT]
> Un *programme informatique* est un texte composé d'intructions.

> [!IMPORTANT]
> Une *instruction* désigne une étape dans un programme. Elle correspond à une action que l'ordinateur réalise lorsqu'il exécute le programme.

> [!IMPORTANT]
> Les programmes sont très souvent constitués de plusieurs instructions, cela constitue une *séquence d'instruction*.

Nous associons une ligne de code à une instruction du programme.

## II. Ordre d'exécution

L'ordre d'exécution d'une séquence d'instruction est le même que l'ordre de lecture (de haut en bas, de gauche à droite). 

> [!TIP]
> Par exemple :
> 
>```python
>a = 10
>a = a + 1
>```
>
>Puis, après exécution, en vérifiant la valeur affectée à la variable `a` dans la console Python :
>
>```python
>>>> a
>11
>```

#### <ins>Application 1</ins>

Recopier le programme de l'exemple précédent et vérifier à votre tour la valeur affectée à la variable `a` dans la console Python.

## III. Trace d'exécution

Une trace d'exécution, comme son nom l'indique, permet de garder une trace de l'état du programme à chaque étape de celui-ci.

Nous représentons la trace d'exécution d'un programme dans un tableau :

| Numéro de ligne | Valeur affectée à la variable ...|  Valeur affectée à la variable ... |
| --- | --- | --- |
| | | |

> [!TIP]
> Par exemple, pour le programme suivant :
>
>```python
>a = 10
>a = a + 1
>b = a - 1
>```
>
>Nous obtenons la trace d'exécution suivante :
>
>| Numéro de ligne | Valeur affectée à la variable `a` | Valeur affectée à la variable `b` |
>| --- | --- | --- |
>| $1$ | $10$ | / |
>| $2$ | $11$ | / |
>| $3$ | $11$ | $10$ |


#### <ins>Application 2</ins>

Donner la trace d'exécution du programme suivant :

```python
a = 9
b = 1
a = a - b
b = b + 1
a = a - b
```

_______

[Exercices](./Exercices/Exercices_sequences.md)
_______

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 