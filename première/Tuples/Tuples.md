# Les Tuples

## I. Définition

Les tuples (ou *p-uplet*) sont des structures linéaires de données **ordonnées** et **non mutables**.

Ils s'écrivent en Python avec des parenthèses et des virgules entre les éléments :

```python
>>> tpl = (1, 3, 5)
>>> type(tpl)
<class 'tuple'>
```

*Remarque : Il faut toujours au moins une virgule pour définir un tuple. Par exemple un tuple avec un seul élément s'écrit : ``tpl_a_un_element = (1, )``*.

- **Ordonnées** comme les listes : nous pouvons accèder aux éléments via leur indice (leur position dans la structure) :

```python
>>> tpl[0]
1
>>> tpl[2]
5
```

- **Non mutables**, contrairement aux listes : nous ne pouvons pas modifier les valeurs d'un tuple :

```python
>>> tpl[1] = 2
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

C'est la grande différence avec les listes. Les tuples sont généralement utilisés pour définir des structures de données dont les éléments restent les mêmes.

Par exemple, les coordonnées $x$ et $y$ dans un plan.

## II. Parcours d'un tuple

Comme les listes, nous pouvons parcourir les éléments d'un tuple avec le parcours par indices et le parcours des valeurs.

### a) Par indices

```python
for i in range(len(tpl)):
    print(tpl[i])
```

La fonction ``len`` renvoie la taille du tuple passé en paramètre.

### b) Des valeurs

```python
for elt in tpl:
    print(elt)
```

## III. Appartenance d'un élément à un tuple

Avec le mot ``in``, nous pouvons savoir si un élément est dans un tuple :

```python
>>> 2 in tpl
False
>>> 3 in tpl
True
```

Le test d'appartenance renvoie un booléen.

## IV. Affectation parallèle

Nous pouvons utiliser les tuples pour affecter sur une ligne plusieurs valeurs à plusieurs variables :

```python
>>> (a, b) = ("cc", 42)
>>> a
"cc"
>>> b
42
```

Ici, les parenthèses sont facultatives, nous ne sommes pas obligés d'en mettre :

```python
>>> a, b = "cc", 42
>>> a
"cc"
>>> b
42
```

*Remarque : Nous n'avons pas écrit de parenthèses mais il s'agit bien de tuples.*

Nous pouvons, grâce à l'affectation parallèle, échanger les valeurs de deux variables :

```python
>>> a, b = b, a
>>> a
42
>>> b
"cc"
```

## V. Renvoyer plusieurs valeurs

Parfois, nous voulons renvoyer plusieurs résultats dans une seule fonction.

Nous pouvons utiliser les tuples pour cela :

```python
def moitie_et_double(nb : int)->tuple:
    return (nb//2 , nb*2)

(a, b) = moitie_et_double(10) 
#La variable a prend la valeur 5
#La variable b prend la valeur 20
```

*Remarque : Le type de la valeur de renvoi de la fonction est bien un tuple.*

---------------

## Applications

### Application 1

Pourquoi le code suivant me renvoie t-il une erreur ?

```python
tpl = ("bonjour", "goodbye", "guten tag")
tpl[1] = "hello"
```

### Application 2

Ecrire une seule instruction permettant d'affecter à la variable $x$ la valeur $3$ et à la variable $y$ la valeur $9$.

Vérifier le contenu de ces variables.

Echanger, sur une seule ligne, les valeurs de $x$ et $y$.

### Application 3

Ecrire une fonction ``suivant_et_suivant(x : int)->tuple``qui prend en paramètre $x$  : un entier et renvoie sous forme de tuple les valeurs  $x+1$et $x+2$.

----------------

## Exercices

### Exercice 1 Parcours

On dispose d'un tuple `fruits = ("banane", "raisin", "orange", ananas")` dont on souhaite afficher les éléments.

a) Ecrire une fonction `fruits_par_indice(fruits : tuple)`en python permettant d'afficher, en utilisant le parcours par indices, chaque fruit.

b) Ecrire une fonction `fruits_par_valeurs(fruits : tuple)`en python permettant d'afficher, en utilisant le parcours des valeurs, chaque fruit.

### Exercice 2 Min, Max et Moyenne

Ecrire une fonction ``min_max_moy(notes : tuple)->tuple`` qui prend en paramètres un tuple de notes et renvoie un tuple de 3 éléments constitué de la note la plus basse, la note la plus élevée et la moyenne des notes.

```python
>>> notes = (20, 15, 10, 16, 9)
>>> minimum_maximum_et_moyenne = min_max_moy(notes)
>>> minimum_maximum_et_moyenne
(9, 20, 14)
```

### Exercice 3 Distance entre deux points

Dans un plan orthonormé, un point est défini par ses coordonnées $x$ et $y$.

La distance entre deux points $A(x_1, y_1)$ et $B(x_2, y_2)$ se calcule : $\sqrt[]{(x_2 - x_1)^2 + (y_2 - y_1)^2}$

<img title="" src="./img/plan.PNG" alt="" width="556">

Par exemple, la distance entre le point A et B dans le plan ci-dessus est 5,4.

Ecrire une fonction `distance(point_a : tuple, point_b : tuple)->float` qui prend en paramètres deux points de coordonnées $(x, y)$ et renvoie la distance entre ces deux points.

*Rappel : Pour utiliser la racine carrée en Python : ``from math import sqrt``*

### Exercice 4 Négatif d'une image

Le négatif d'une image est une image dont les couleurs RGB des pixels sont les couleurs complémentaires des pixels originaux :

![](./img/negatif.PNG)

Pour le faire automatiquement, nous allons nous servir d'un programme utilisant le module PIL.

a) Télécharger l'image [logo_python.png](./img/logo_python.png) et le programme [negatif_img.py](./src/negatif_img.py) dans le répertoire courant.

b) Remplacer les 'A COMPLETER' dans le programme donné pour obtenir le négatif de l'image.

### Exercice 5 Swap

Nous avons vu, précédemment, que l'on pouvait échanger deux éléments d'une liste avec la fonction suivante :

```python
def swap(liste : list, i1 : int, i2 : int):
    tmp = liste[i1]
    liste[i1] = liste[i2]
    liste[i2] = tmp
```

Ecrire une fonction ``swap2(liste : list, i1 : int, i2 : int)`` qui prend en paramètre une liste et deux indices et échange les valeurs situés à ces deux indices.

Le corps de la fonction devra s'écrire sur une seule ligne et utiliser les tuples.

### Exercice 6 Emploi du temps

On dispose de la variable ``semaine`` qui est une liste dont les éléments sont des tuples constitués du jour de la semaine et du nombre d'heures de cours.

Par exemple : ``semaine = [("lundi" , 5), ("mardi", 2), ("mercredi", 8), ("jeudi", 6), ("vendredi", 3)]``

a) Ecrire une fonction `total_heures(semaine : list)->int` qui prend en paramètre la liste `semaine` et renvoie le nombre total d'heures de cours :

```python
>>> total = total_heures(semaine)
>>> total
24
```

b) Ecrire une fonction ``journees_heures_inferieur_a_4(semaine : list)->list`` qui prend en paramètre la liste ``semaine`` et renvoie une liste de tuple constitué des jours de la semaine où le nombre d'heures de cours est inférieur à 4 :

```python
>>> liste_journees = journee_heures_inferieur_a_4(semaine)
>>> liste_journees
[('mardi', 2), ('vendredi', 3)]
```
