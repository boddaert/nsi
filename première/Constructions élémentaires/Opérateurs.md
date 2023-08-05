# Opérateurs

## I. Définition

Un *opérateur* est un symbole permettant de réaliser une opération.

Comme sur la calculatrice classique, nous disposons les opérateurs entre des opérandes pour réaliser l'opération. Cela constitue une expression.

Les *opérandes* sont des valeurs ou des variables.

Par exemple dans l'exemple suivant, l'opérateur est `+` et les opérandes sont $`3`$ et $`6`$ :

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
|   Modulo (reste de la division entière) |   `%` |
|   Supérieur à |   `>` |
|   Inférieur à |   `<` |
|   Supérieur ou égal à |   `>=` |
|   Inférieur ou égal à |   `<=` |
|   Egal à |   `==` |
|   Différent de    |   `!=` |

Nous remarquons que les six derniers opérateurs du tableau sont des *comparateurs* et renvoient comme résultat un booléen :

```python
>>> 5 > 2
True
```

##### Application 1

Nous considèrons les expressions suivantes :

- `11 + 7`
- `11 * 7`
- `11 / 7`
- `11 // 7`
- `11 ** 7`
- `11 % 7`
- `11 > 7`
- `11 < 7`
- `11 >= 7`
- `11 <= 7`
- `11 == 7`
- `11 != 7`

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

- `(3 + 8) * 2`

- `3 + (8 * 2`$

- `3 + 8 * 2`

- `2 * 8 + 3`

a) Sur chacune d'elle, proposer un résultat sans utiliser l'ordinateur.

b) A l'aide de la console Python, vérifier vos résultats.

__________

[Feuille d'exercice](./Exercices/Exercices_opérateurs.md)
__________

Leçon 3 : [Variables](./Variables.md)