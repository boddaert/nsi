# Récursivité

## I. Introduction

Considérons la fonction suivante :

```python
def somme_iter(n : int)->int :
    res = 0
    while n > 0 :
        res += n
        n -= 1
    return res
```

Elle calcule la somme des $n$ premiers entiers ($n + (n-1) + (n-2) + ... + 0$):

```python
>>> somme(4)
10
```

**Question :** Est-il possible d'écrire cet algorithme sans utiliser de boucle ?

## II. Définitions

Une *fonction récursive* est une fonction réalisant au moins un autre appel à elle-même avec des arguments différents.

La *récursivité* est une technique de programmation.

L'implémentation en Python est souvent très proche du principe de récurrence du problème.

### a) Principe de récurrence

Dans un principe de récurrence, nous distinguons :

- Les *cas de base* pour lesquels les calculs sont triviaux.
- Les *cas récursifs* pour lesquels un appel à la définition est réalisé.

En reprenant l'exemple de la somme des $n$ premiers entiers, son principe de récurrence est :

$\begin{equation} somme_rec(n) = \begin{cases} 0 & \text{if $n = 0$}\\ n + somme_rec(n-1) & \text{if $n > 0$} \end{cases} \end{equation}$

### b) Traduction en Python

```python
def somme(n : int)->int :
    if n == 0 :
        return 0
    else :
        return n + somme(n-1)
```

L'instruction `return 0` correspond au cas de base.

L'instruction `return n + somme(n-1)` correspond au cas récursif.

La condition `if n == 0 :` se nomme *condition d'arrêt*.

## III. Pile d'appels

Une *pile d'appels* est la pile représentant tous les appels succéssifs nécessaires à l'exécution de la fonction.

Par exemple, pour l'appel `somme(4)`, cela donne :

![Pile d'appels](./img/pile_d_appels.png)

##


































l'instruction à répéter pour la somme des $n$ premiers entiers est la somme de $n$ avec $n-1$.

Avec $n=4$, cela donne :

- $4 + 4-1$
- $3 + 3-1$
- $2 + 2-1$
- $1 + 1-1$
- $0$

Nous constatons que 

Cette instruction, nous pouvons l'écrire dans fonction `somme_rec(n : int)->int` :

```python
def somme_rec(n : int)->int :
    return n + n-1
```

Et appeler ainsi plusieurs fois la fonction :

```python
>>> somme_rec()
```
Nous remarquons que l'instruction 

