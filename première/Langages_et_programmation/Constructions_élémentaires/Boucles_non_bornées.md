# Boucle non bornées

## I. Définitions

> [!IMPORTANT]
> Une *boucle* est une construction élémentaire qui permet de répéter une séquence d'instruction.
>
>Nous appelons le *corps de boucle* la séquence d'instruction qui sera répétée.

> [!IMPORTANT]
>La *boucle non bornée* permet de répéter l'exécution du corps de boucle tant que la condition est remplie.

La condition est remplie si elle vaut $VRAI$.

> [!NOTE]
>Nous utilisons les boucles non bornées lorsque nous ne connaissons pas à l'avance combien de fois le corps de boucle sera exécuté.

## II. Répéter à l'aide d'une condition

### a) Syntaxe

En Python, les boucles non bornées s'écrivent en utilisant le mot-clé `while` (*Tant que* en français) suivi d'une condition.

> [!TIP]
>Par exemple :
>```python
>a = 0
>while a < 3 :
>    a = a + 1
>b = a
>```
>
>Cela se traduit en français :
>
>```
>a est égal à 0
>Tant que a est inférieur à 3, faire :
>    a est égal à a+1
>b est égal à a
>```
>
>Et son schéma de branchement est :
>
>```mermaid
>  graph TB;
>      A{Si a est inférieur à 3, faire :};
>      A--VRAI-->B[a est égal à a+1];
>      B-->A;
>      A--FAUX-->C[b est égal à a];
>```
>À l'issue de l'exécution du programme précédent, la valeur affectée à la variable `a` est $3$.

#### <ins>Application 1</ins>

Traduire en Français les programmes suivants :

1. Programme 1

```python
a = 0
while a < 6 :
    a = a + 1
```

2. Programme 2

```python
a = 10
while a > 0 :
    a = a - 1
```

3. Programme 3

```python
a = 0
while a <= 10 :
    a = a + 2
```

#### <ins>Application 2</ins>

Dessiner le schéma de branchement pour chacun des programmes de l'application $1$.

#### <ins>Application 3</ins>

Écrire les programmes Python correspondant aux algorithmes en français suivants :

1. Algorithme 1

```
a est égal à 0
Tant que a est inférieur à 12, faire :
    a est égal à a+1
```

2. Algorithme 2

```
a est égal à 0
Tant que a est inférieur à 12, faire :
    a est égal à a+5
```

3. Algorithme 3

```
a est égal à -2
Tant que a est supérieur à -7, faire :
    a est égal à a-1
```

#### <ins>Application 4</ins>

Faire la trace d'exécution pour chacun des programmes de l'application $3$.
_______

[Exercices](./Exercices/Exercices_boucles_non_bornees.md)

_______

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 