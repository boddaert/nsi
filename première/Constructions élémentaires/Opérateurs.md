# Opérateurs

## I. Définition

Un *opérateur* est un symbole permettant de réaliser une opération.

Comme sur la calculatrice classique, nous disposons les opérateurs entre des opérandes pour réaliser l'opération. Cela constitue une expression.

Les *opérandes* sont des valeurs ou des variables.

Par exemple dans l'exemple suivant, l'opérateur est `+` et les opérandes sont `3` et `6` :

```python
>>> 3 + 6
9
```

## II. Les différents opérateurs

|   En Français    |   En Python   |
| --- | --- |
|   Addition    |`+`|
|   Soustraction | `-`|
|   Multiplication | `*` |
|   Division euclidienne | `/` |
|   Division entière    | `//` |
|   Puissance   |   `**` |
|   Modulo (reste de la divion entière) |   `%` |
|   Supérieur à |   `>` |
|   Inférieur à |   `<` |
|   Supérieur ou égale à |   `>=` |
|   Inférieur ou égale à |   `<=` |
|   Egale à |   `==` |
|   Différent de    |   `!=` |

Nous remarquons que les six derniers opérateurs du tableau renvoient comme résultat un booléen :

```python
>>> 5 > 2
True
```

##### Application 1

Nous considèrons les expressions suivantes :

- 11 + 7
- 11 * 7
- 11 / 7
- 11 // 7
- 11 ** 7
- 11 % 7
- 11 > 7
- 11 < 7
- 11 >= 7
- 11 <= 7
- 11 == 7
- 11 != 7

a) Sur chacune d'elle, proposer un résultat sans utiliser l'ordinateur.

b) A l'aide de la console Python, vérifier vos résultats.

## III. Ordres de priorité

Comme sur la calculatrice classique, les ordres de priorité sont respectés. L'opérateur `*` étant prioritaire par rapport à l'opérateur `+`.

Les parenthèses `()` permettent d'augmenter la priorité de l'expression encadrée :

```python
>>> (3 + 5) * 2
16
```

##### Application 2

Nous considérons les expressions suivantes :

- (3 + 8) * 2

- 3 + (8 * 2)

- 3 + 8 * 2

- 2 * 8 + 3

a) Sur chacune d'elle, proposer un résultat sans utiliser l'ordinateur.

b) A l'aide de la console Python, vérifier vos résultats.

## Exercices 

### Exercice 1

A l'aide de la console, déterminer lequel des deux opérateurs est le plus prioritaire entre :

- `*` et `**`

- `+` et `//`

- `%` et `*`

### Exercice 2

Donner le résultat des expressions suivantes en précisant le type du résultat ou lorsqu'une erreur doit survenir.

- 5 ** 2 - 3

- 5 / 2

- 4 / 2

- 'quatre' / 'deux'

- 4 // 2

- 4 % 2

- ( 3 + ) 5

- 5 % 2

- 7 + 7 % 2

- 3 * 3 ** 2

- '4' // 2


__________

Leçon 3 : [Variables](./Variables.md)