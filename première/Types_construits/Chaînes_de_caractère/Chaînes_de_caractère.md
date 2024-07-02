# Chaînes de caractères

## I. Définitions

> [!IMPORTANT]
> Un *caractère* est un symbole écrit lié à un système d'écriture.

> [!IMPORTANT]
> Une *chaîne de caractère* est un ensemble de caractères.

## II. Spécificités en Python

### a) Syntaxe

En Python, le caractère est encadré par des guillements simples (`'`) ou doubles (`"`).

> [!TIP]
> Par exemple :
> ```python
> "coucou"
> ```

Les chaînes de caractères sont de type `str`.

> [!TIP]
> Par exemple :
> ```python
> >>> type("coucou")
> <class 'str'>
> ```

Python ne fait pas la différence entre les caractères dit "imprimables" et les caractères "non imprimables".

> [!TIP]
> Par exemple :
> ```python
> >>> type(" ")
> <class 'str'>
> ```

> [!IMPORTANT]
> Une *chaîne de caractère vide* est une chaîne de caractère ne contenant aucun caractère.

> [!TIP]
> Par exemple :
> ```python
> >>> type("")
> <class 'str'>
> ```

### b) Opérations

#### 1. Taille

> [!IMPORTANT]
> La *taille* d'une chaîne de caractère est le nombre de caractère contenu dans la chaîne.

Elle peut être connue avec la fonction `len()` (pour *length* en anglais).

> [!TIP]
> Par exemple :
> ```python
> >>> len("coucou")
> 6
> ```

#### <ins>Application 1</ins>

En utilisant la console Python, trouver la taille des chaînes de caractères suivantes :

1. `"hello world"`

2. `""`

#### 2. Accès au *ième* caractère

Les caractères d'une chaîne sont indicés, c'est-à-dire qu'ils possèdent chacun un numéro de position dans la chaîne.

> [!IMPORTANT]
> L'*indice d'un caractère* dans la chaîne est le numéro de position du caractère.

L'accès à un caractère d'indice $i$ s'effectue en l'écrivant entre crochets.

> [!TIP]
> Par exemple :
> ```python
> >>> mot = "coucou"
> >>> mot[2]
> 'u'
> ```

> [!WARNING]
> Le premier caractère est d'indice $0$.

> [!TIP]
> Par exemple :
> ```python
> >>> mot[0]
> 'c'
> ```

#### <ins>Application 2</ins>

Donner sans utiliser l'ordinateur, le résultat des instructions suivantes :

1. Instruction 1
```python
>>> mot[5]
...
```

2. Instruction 2
```python
>>> mot[1]
...
```

#### <ins>Application 3</ins>

Expliquer l'erreur suivante :

```python
>>> mot = "coucou"
>>> mot[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

#### <ins>Application 4</ins>

Donner l'instruction permettant d'obtenir :

a) La lettre d'indice $4$.

b) La dernière lettre en utilisant la taille de la chaîne.

#### 3. Test d'appartenance

> [!IMPORTANT]
> Le *test d'appartenance* permet de savoir si une valeur est présente dans une autre.

Nous pouvons vérifier si une chaîne de caractère est contenue dans une chaîne à l'aide du mot-clé `in`.

> [!TIP]
> Par exemple :
> ```python
> >>> 'u' in mot
> True
> ```

> Le test d'appartenance renvoie comme résultat un booléen.

#### <ins>Application 5</ins>

Vérifier, dans la console Python et à l'aide du mot-clé `in`, si :

a) La chaîne `"cou"` est contenue dans `mot`.

b) La chaîne `""` est contenue dans `mot`.

#### 4. Concaténation

> [!IMPORTANT]
> La *concaténation* de deux chaînes de caractère consiste à assembler l'une après l'autre les chaînes pour n'en former qu'une.

La concaténation de deux chaînes de caractères en Python s'effectue à l'aide de l'opérateur `+`.

> [!TIP]
> Par exemple :
> ```python
> >>> mot_1 = "couc"
> >>> mot_2 = "ou"
> >>> mot = mot_1 + mot_2
> >>> mot
> 'coucou'
> ```

#### <ins>Application 6</ins>

Concaténer :

a) La chaîne `Bonjour a` avec la chaîne `tous`.

b) La chaîne `Numérique` avec la chaîne `Sciences` puis avec la chaîne `Informatiques`.

#### 5. Découpage ou *slicing* (hors programme)

> [!IMPORTANT]
> Le *slicing* permet d'obtenir une sous-chaîne à partir d'une chaîne de caractère.

Le slicing en Python s'écrit  : ``chaine[debut:fin]``  avec ``debut`` l'indice de la première coupe et ``fin`` l'indice de la seconde coupe (exclue).

> [!TIP]
> Par exemple :
> ```python
> >>> mot = "coucou"
> >>> mot[1:4]
> 'ouc'
> ```

#### <ins>Application 7</ins>

Donner sans utiliser l'ordinateur, le résultat des instructions suivantes :

1. Instruction 1
```python
>>> mot[1:2]
...
```

2. Instruction 2
```python
>>> mot[0:6]
...
```

## III. Mutabilité

> [!IMPORTANT]
> Une valeur est dite *mutable* si elle peut être modifiée.

Les chaînes de caractères ne sont pas mutables. C'est-à-dire que nous ne pouvons pas modifier les caractères d'une chaîne.

> [!TIP]
> Par exemple :
> ```python
> >>> mot = "coucou"
> >>> mot[0] = "A"
> Traceback (most recent call last):
>   File "<pyshell>", line 1, in <module>
> TypeError: 'str' object does not support item assignment
> ```

#### <ins>Application 8</ins>

Essayer à votre tour de modifier la valeur affectée à la variable `mot` en changeant la troisième lettre en `h`.

## IV. Parcours de chaîne

> [!IMPORTANT]
> Un *parcours de chaîne* consiste à visiter un à un tous les caractères de la chaîne.

Nous parcourons les chaînes de caractères en utilisant les boucles.

> Comme nous connaissons à l'avance la taille d'une chaîne, nous connaissons à l'avance le nombre de tour de boucle nécessaire au parcours : Nous utilisons donc la boucle `for`.

Il existe deux façons d'utiliser la boucle `for` pour parcourir les chaînes de caractères :

1. Le parcours par **indice**.

2. Le parcours par **élément**.

### a) Parcours par indice

Dans le parcours par indice, nous parcourons les caractères indice par indice.

> [!TIP]
> Par exemple :
> ```python
> 1. mot = "coucou"
> 2. for i in range(len(mot)) :
> 3.   lettre = mot[i]
> ```
>
> Trace d'exécution du programme donné ci-dessus:
> 
> | Numéro de ligne | Valeur affectée à $i$ | Valeur affectée à $lettre$ |
> | :---: | :---: | :---: |
> | $1$ | / | / |
> | $2$ | $0$ | / |
> | $3$ | $0$ | $c$ |
> | $2$ | $1$ | $o$ |
> | $3$ | $1$ | $u$ |
> | ... | ... | ... |

#### <ins>Application 9</ins>

Compléter la trace d'exécution de l'exemple précédent.

### b) Parcours par élément

Dans le parcours par élément, nous parcourons caractère par caractère.

> [!TIP]
> Par exemple :
> ```python
> 1. mot = "coucou"
> 2. for caractere in mot :
> 3.   lettre = caractere
> ```
> Trace d'exécution du programme donné ci-dessus:
>
>| Numéro de ligne | Valeur affectée à $caractere$ | Valeur affectée à $lettre$ |
>| :---: | :---: | :---: |
>| $1$ | / | / |
>| $2$ | $w$ | / |
>| $3$ | $w$ | $c$ |
>| $2$ | $o$ | $o$ |
>| $3$ | $o$ | $u$ |
>| ... | ... | ... |


#### <ins>Application 10</ins>

Compléter la trace d'exécution de l'exemple précédent.
___________

[Exercices](./Exercices/Exercices_chaines_de_caractere.md)

___________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 