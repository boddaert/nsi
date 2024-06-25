# Opérateurs

## I. Définitions

> [!IMPORTANT]
> Un *opérateur* est un symbole permettant de réaliser une opération.

Comme sur la calculatrice classique, nous disposons les opérateurs entre des opérandes pour réaliser l'opération. Cela constitue une **expression**.

Les opérandes sont des valeurs ou des variables.

> [!TIP]
> Par exemple dans l'exemple suivant, l'opérateur est `+` et les opérandes sont $`3`$ et $`6`$ :
> ```python
> >>> 3 + 6
> 9
> ```

## II. Les différents opérateurs

### a) Opérateurs mathématiques

|   En Français    |   En Python   |
| --- | --- |
|   Addition    |`+`|
|   Soustraction | `-`|
|   Multiplication | `*` |
|   Division euclidienne | `/` |
|   Division entière    | `//` |
|   Puissance   |   `**` |
|   Modulo (reste de la division entière) |   `%` |

Les opérateurs mathématiques ont comme opérandes des nombres entiers ou flottants et renvoient comme résultat un nombre entier ou flottant.

> [!TIP]
> ```python
> >>> 12 // 4
> 3
> ```

#### <ins>Application 1</ins>

a) Sans utiliser l'ordinateur, proposer un résultat sur chacune des opérations suivante :

1. `11 + 7`
2. `11 * 7`
3. `11 / 7`
4. `11 // 7`
5. `11 ** 7`
6. `11 % 7`

b) Vérifier vos réponses en utilisant la console Python.

### b) Opérateurs de comparaison

|   En Français    |   En Python   |
| --- | --- |
|   Supérieur à |   `>` |
|   Inférieur à |   `<` |
|   Supérieur ou égal à |   `>=` |
|   Inférieur ou égal à |   `<=` |
|   Egal à |   `==` |
|   Différent de    |   `!=` |

Les opérateurs de comparaison ont comme opérandes des nombres entiers ou flottants et renvoient comme résultat un booléen.

> [!TIP]
>  ```python
> >>> 5 > 2
> True
> ```

#### <ins>Application 2</ins>

a) Sans utiliser l'ordinateur, proposer un résultat sur chacune des opérations suivante :

1. `11 > 7`
2. `11 < 7`
3. `11 >= 7`
4. `11 <= 7`
5. `11 == 7`
6. `11 != 7`

b) Vérifier vos réponses en utilisant la console Python.

### c) Opérateurs booléens

|   En Français    |   En Python   |
| --- | --- |
|   $NON$ |   `not` |
|   $ET$ |   `and` |
|   $OR$ |   `or` |

Les opérateurs booléens ont comme opérandes des booléens et renvoient comme résultat un booléen.

> [!TIP]
> ```python
> >>> True or False
> True
> ```

Nous résumons généralement les résultats des opérateurs booléens dans des **tables de vérité** :

- Table de vérité de $NON$ :

| $A$ | $NON A$ | 
|---|---|
| $False$ | $True$ |
| $True$ | $False$ |

- Table de vérité de $ET$ :

| $A$ | $B$ | $A$ $ET$ $B$ | 
|---|---|---|
| $False$ | $False$ | $False$ | 
| $False$ | $True$ | $False$ | 
| $True$ | $False$ | $False$ | 
| $True$ | $True$ | $True$ | 

- Table de vérité de $OU$ :

| $A$ | $B$ | $A$ $OU$ $B$ | 
|---|---|---|
| $False$ | $False$ | $False$ | 
| $False$ | $True$ | $True$ | 
| $True$ | $False$ | $True$ | 
| $True$ | $True$ | $True$ | 


####  <ins>Application 3</ins>

a) Sans utiliser l'ordinateur, proposer un résultat sur chacune des opérations suivante :

1. `True or False`
2. `True or True`
3. `True and True`
4. `not False`
5. `not False and True`

b) Vérifier vos réponses en utilisant la console Python.

## III. Ordres de priorité

Comme sur la calculatrice classique, les ordres de priorité sont respectés. L'opérateur `*` étant prioritaire par rapport à l'opérateur `+`.

Les parenthèses `()` permettent d'augmenter la priorité de l'expression encadrée.

> [!TIP]
> ```python
> >>> (3 + 5) * 2
> 16
> ```

#### <ins>Application 4</ins>

a) Sans utiliser l'ordinateur, proposer un résultat sur chacune des opérations suivante :

1. `(3 + 8) * 2`

2. `3 + (8 * 2)`

3. `3 + 8 * 2`

4. `2 * 8 + 3`

b) Vérifier vos réponses en utilisant la console Python.

__________

[Exercices](./Exercices/Exercices_opérateurs.md)
__________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 