# Opérateurs

## I. Définitions

Un *opérateur* est un symbole permettant de réaliser une opération.

Comme sur la calculatrice classique, nous disposons les opérateurs entre des opérandes pour réaliser l'opération. Cela constitue une expression.

Les *opérandes* sont des valeurs ou des variables.

Par exemple dans l'exemple suivant, l'opérateur est `+` et les opérandes sont $`3`$ et $`6`$ :

```python
>>> 3 + 6
9
```

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

Les opérateurs mathématiques ont comme opérandes des nombres entiers ou flottants et renvoient comme résultat un nombre entier ou flottant :

```python
>>> 12 // 4
3
```

##### Application 1

Nous considèrons les expressions suivantes :

- `11 + 7`
- `11 * 7`
- `11 / 7`
- `11 // 7`
- `11 ** 7`
- `11 % 7`

a) Sur chacune d'elle et à l'aide de la console Python, donner la réponse aux opérations.

### b) Opérateurs de comparaison

|   En Français    |   En Python   |
| --- | --- |
|   Supérieur à |   `>` |
|   Inférieur à |   `<` |
|   Supérieur ou égal à |   `>=` |
|   Inférieur ou égal à |   `<=` |
|   Egal à |   `==` |
|   Différent de    |   `!=` |

Les opérateurs de comparaison ont comme opérandes des nombres entiers ou flottants et renvoient comme résultat un booléen :

```python
>>> 5 > 2
True
```
##### Application 2

Nous considèrons les expressions suivantes :

- `11 > 7`
- `11 < 7`
- `11 >= 7`
- `11 <= 7`
- `11 == 7`
- `11 != 7`

a) Sur chacune d'elle, proposer un résultat sans utiliser l'ordinateur.

b) A l'aide de la console Python, vérifier vos résultats.

### c) Opérateurs booléens

|   En Français    |   En Python   |
| --- | --- |
|   $NON$ |   `not` |
|   $ET$ |   `and` |
|   $OR$ |   `or` |

Les opérateurs booléens ont comme opérandes des booléens et renvoient comme résultat un booléen :

```python
>>> True or False
True
```

Nous résumons généralement les résultats des opérateurs booléens dans des *tables de vérité* :

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


##### Application 3

Nous considèrons les expressions suivantes :

- `True or False`
- `True or True`
- `True and True`
- `not False`
- `not False and True`
- `not False or not True`

a) Sur chacune d'elle, proposer un résultat sans utiliser l'ordinateur.

b) A l'aide de la console Python, vérifier vos résultats.

## III. Ordres de priorité

Comme sur la calculatrice classique, les ordres de priorité sont respectés. L'opérateur `*` étant prioritaire par rapport à l'opérateur `+`.

Les parenthèses `()` permettent d'augmenter la priorité de l'expression encadrée :

```python
>>> (3 + 5) * 2
16
```

##### Application 4

Nous considérons les expressions suivantes :

- `(3 + 8) * 2`

- `3 + (8 * 2)`

- `3 + 8 * 2`

- `2 * 8 + 3`

a) Sur chacune d'elle, proposer un résultat sans utiliser l'ordinateur.

b) A l'aide de la console Python, vérifier vos résultats.

__________

[Exercices](./Exercices/Exercices_opérateurs.md)
__________

[Sommaire](./../../README.md)