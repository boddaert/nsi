# Récursivité

## I. Introduction

$\to$ Est-il possible de répéter une séquence d'instruction sans utiliser de boucle ?

### a) Première idée

La première idée serait d'appeler plusieurs fois la fonction :

```python
fonc()
fonc()
fonc()
```

Problème : Le nombre de répétition est limité au nombre de ligne.

### b) Deuxième idée

La seconde idée serait d'appeler la fonction dans son propre bloc d'instruction :

```python
def fonc():
    fonc()
```

Problème : Le nombre de répétition est infini.

### c) Troisième idée

La troisième idée serait d'utiliser la fonction de la deuxième idée mais en y ajoutant une condition qui arrêterait les appels à elle-même.

```python
def fonc():
    if arrêt :
        return resultat
    else :
        fonc()
```

> La variable `arrêt` est une valeur booléenne : elle vaut donc `True` ou `False`.

Problème : `arrêt` n'est pas définie.

### d) Quatrième idée

Passons `arrêt` en paramètre de la fonction.

```python
def fonc(arrêt) :
    if arrêt :
        return resultat
    else :
        fonc(arrêt)
```

#### <ins>Application 1</ins>

Soit la fonction suivante :

```python
def fonction_recursive(n : int)->str :
    if n == 3 :
        return 'fini'
    else :
        return fonction_recursive(n + 1)
```

Dérouler à la main l'exécution de la fonction précédente avec $n = 0$.

## II. Définitions

> [!IMPORTANT]
> La *récursivité* est une technique de programmation.

> [!IMPORTANT]
> Une *fonction récursive* est une fonction réalisant au moins un autre appel à elle-même avec des arguments différents.

La récursivité permet de ne pas modifier l'état des variables en mémoire.

L'implémentation en Python est souvent très proche du principe de récurrence du problème.

### a) Mise en situation

Considérons une fonction itérative (non récursive).

> [!TIP]
> Par exemple :
>
> La fonction `somme()` :
>
> ```python
> def somme(n : int)->int :
>     res = 0
>     while n > 0 :
>         res = res + n
>         n = n - 1
>     return res
> ```
>
> Elle calcule la somme des $n$ premiers entiers ($n + (n-1) + (n-2) + ... + 0$):
>
> ```python
> >>> somme(4)
> 10
> ```

### b) Principe de récurrence

> [!IMPORTANT]
> Dans un principe de récurrence, nous distinguons :
>
> - Les *cas de base* pour lesquels les calculs sont triviaux.
>
> - Les *cas récursifs* pour lesquels un appel à la définition est réalisé.

> [!TIP]
> Par exemple :
> En reprenant l'exemple de la somme des $n$ premiers entiers, son principe de récurrence est :
>
> $$
> somme(n)=
> \begin{cases}
> 0 & \quad \text{si n = 0}\\ 
> n + somme(n-1) & \quad \text{si n > 0}
> \end{cases}
> $$
>
> Ainsi, les valeurs de $somme(n)$, pour $n$ valant $0$, $1$, $2$ puis $3$ sont :
>
> $somme(0) = 0$
>
> $somme(1) = 1 + somme(0)$
>
> $somme(2) = 2 + somme(1)$
>
> $somme(3) = 3 + somme(2)$

> [!NOTE]
> Nous constatons que pour calculer la valeur de $somme(n)$, nous avons besoin de connaître la valeur de $somme(n-1)$.

Il s'agit bien d'une définition récursive du problème, nous avons bien une fonction nécessitant un appel à elle-même avec un argument différent.

#### <ins>Application 2</ins>

Donner le principe de récurrence de la fonction de l'application $1$.

### c) Traduction en Python

Le principe de récurrence est directement traduisible en programme Python.

> [!TIP]
> Par exemple :
> ```python
> def somme(n : int)->int :
>     if n == 0 :
>         return 0
>     else :
>         return n + somme(n-1)
> ```
>
> L'instruction `return 0` correspond au cas de base.
> 
> L'instruction `return n + somme(n-1)` correspond au cas récursif.
>
> La condition `if n == 0 :` se nomme *condition d'arrêt*.

#### <ins>Application 3</ins>

Indiquer sur la fonction `fonction_recursive()` de l'application $1$ où se situe le cas de base, le cas récursif et la condition d'arrêt.

## III. Pile d'appels

> [!IMPORTANT]
> Une *pile d'appels* est la pile représentant tous les appels successifs nécessaires à l'exécution de la fonction.

> [!TIP]
> Par exemple :
> Pour l'appel `somme(4)`, cela donne :
>
> <img src="./img/pile_d_appels.png" width=500>

#### <ins>Application 4</ins>

Dessiner la pile d'appels de la fonction `fonction_recursive()` de l'application 1 avec $n = 0$.

#### <ins>Application 5</ins>

a) Recopier le code de la fonction `fonction_recursive()` dans Thonny.

b) Avec l'outil `Debogueur` de Thonny, exécuter pas à pas l'instruction `fonction_recursive(0)`.

## IV. Méthodologie

> [!NOTE]
> Avant de se lancer dans l'écriture d'une fonction récursive, il est conseillé de suivre la méthodologie suivante :
>
> 1. Repérer le problème qui se répète et les relations entre les différents résultats.
>
> 2. Trouver la ou les conditions d'arrêt.
>
> 3. Ecrire le principe de récurrence.
>
> 4. Traduire le principe précédent en fonction récursive Python.
>
> 5. Vérifier le bon fonctionnement de la fonction récursive à l'aide du debogueur.

_________

[Exercices](./Exercices/Exercices_recursivité.md)

_________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 