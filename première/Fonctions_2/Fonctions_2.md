# Fonctions 2

## I. Spécification d'une fonction

### a) Préconditions

-> assertions

### b) Postconditions

-> doctests

## III. Portée des variables

### a) Définition

La *portée* d'une variable désigne la zone de code dans le programme dans laquelle elle est accessible. Toutes nos variables ne sont pas nécessairement accessibles à n'importe quel endroit dans un programme et on ne va donc pas toujours pouvoir les utiliser.

On distingue les variables **globales** et **locales** qui possèdent une portée différente.

### b) Variables globales

Toutes les variables déclarées **hors de toute fonctions** sont les variables globales.

Une fonction peut accéder à une variable globale :

![](./img/img_fonc/var_globale.PNG)

Ici, on a déclarer une variable globale ``v = 42`` et une fonction ``double()-> int`` qui multiplie par 2 notre variable ``v`` déclarée hors de la fonction ``double()``.

On obtient comme résultat 84, ce qui prouve bien que notre fonction ``double()`` a accès à notre variable ``v``.

Lorsqu'une fonction accède à une variable globale, elle accède à sa valeur courante :

![](./img/img_fonc/var_globale2.PNG)

Ici, avant d'appeler ma fonction ``double()``, on a augmenté la valeur de ``v`` de 1 et on obtient donc comme résultat 86.

### c) Variables locales

Le corps d'une fonction peut introduire des variables pour ses calculs intermédiaires, on appelle ces variables : les variables locales et **ne sont accessibles que dans le corps de cette fonction**.

On peut le vérifier en définissant une fonction ``creer_variable()`` qui crée une variable locale, en appellant cette fonction et en vérifiant dans la console si la variable existe :

![](./img/img_fonc/var_locale1.PNG)

On remarque que j'obtiens bien une erreur ``NameError: name 'f' is not defined``lorsque je demande la valeur de ``f`` dans la console, même après avoir appelé la fonction ``creer_variable()``. Ce qui nous prouve que la variable ``f`` existe uniquement dans la fonction et n'est accessible que depuis cette fonction.

La variable locale ``f`` **disparaît après l'exécution de la fonction**.

Si je déclare une variable globale ``f`` avant l'appel à la fonction :

![](./img/img_fonc/var_locale2.PNG)

Pendant l'exécution de ``creer_variable()``, il existe simultanément deux variables qui s'appellent ``f`` : la variable globale et la variable locale. Dans ce cas, seule la variable locale est utilisée, on dit qu'elle *masque* la variable globale.


#### Exercice

- Ecrire une fonction ``incremente`` prenant en paramètre un entier *n* et renvoie $`n+1`$.

- Déterminer le résultat de l'appel suivant :

```python
incremente( incremente ( incremente ( -3 )))
```

- Déssiner le schéma représentant les appels succéssifs de l'instruction précédente.

#### Application 10

Réécrire les fonctions ``double`` et ``creer_variable`` et refaire les situations vues dans le cours.

#### Application 11

Voici une procédure ``suivant`` prenant en paramètre un entier *n* et ajoute 1 à n mais ne renvoie rien :

```python
def suivant(x : int)-> None:
    x = x + 1
```

Puis une suite d'instructions dans la console :

![](./img/img_fonc/app11.PNG)

Expliquer pourquoi *x* vaut toujours 1 après l'appel à ``suivant``.

### Exercice 1

*Dans cet exercice, on utilisera la division entière notée ``//``*

Dans cet exercice, on souhaite faire la somme de tous les entiers multiples de 3 et 5 inférieurs à 1000.

Commençons avec la somme des entiers des multiples de 3, c'est-à-dire :

$`3+6+9+12+...+999`$

On peut mettre 3 en facteur :

$`3 * (1+2+3+4+...+333)`$

Par chance, on sait que la somme des entiers de $`1`$ à $`n`$ est égale à $`n*(n+1)/2`$.

Donc $`1+2+3+4+...+333= 333 * \frac{(333+1)}{2}`$

- Ecrire une fonction ``somme_entier`` prenant en paramètre un entier *n* et renvoie la somme des entiers de 1 à *n* 

La somme des entiers multiples de 3 est donc ``3 * somme_entier(333)``.

On peut également l'écrire comme ``3 * somme_entier(999 // 3)``, ce qui nous permet d'écrire une fonction ``multiples`` permettant  d'obtenir la somme des entiers multiples de n'importe quel entier puisqu'il suffira de remplacer 3 par l'entier que l'on veut.

- Ecrire une fonction ``multiples`` prenant en paramètre un entier *i* et renvoie la somme des entiers multiples de *i*

La somme de tous les entiers multiples de 3 et 5 inférieurs à 1000 sera donc 

```python
multiples(3) + multiples(5)