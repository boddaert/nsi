# Variables

## I. Définitions

Une *variable* est un nom qui possède une valeur.

On dit qu'une valeur est affectée à une variable.

## II. Affectations de variable

### a) Affectation simple

Nous pouvons affecter n'importe quelle valeur à une variable en Python avec l'opérateur d'affectation ``=`` :

```python
>>> ma_variable = 42
```

Pour connaître la valeur contenue dans une variable, il suffit de l'appeler :

```python
>>> ma_variable
42
```

### b) Ré-affectation

Pour modifier la valeur contenue dans une variable, j'affecte une nouvelle valeur à ma variable :

```python
>>> ma_variable = 42
>>> ma_variable
42
>>> ma_variable = 67
>>> ma_variable
67
```

L'ancienne valeur est alors écrasée par la nouvelle valeur.

##### Application 1

Dans la console python et en utilisant l'affectation, affecter :

- la variable `ma_variable_a` avec la valeur $`1`$
- la variable `ma_variable_b` avec la valeur $`9.99`$
- la variable `ma_variable_c` avec la valeur $`"hello world"`$
- la variable `ma_variable_d` avec la valeur $`True`$

Puis, vérifier en appelant chacune des variables les valeurs associées.

## III. Type d'une variable

Le type d'une variable est le type de la valeur qu'elle contient.

On peut, comme pour les valeurs, connaître le type des variables en utilisant la fonction ``type()`` :

```python
>>> type(ma_variable)
<class 'int'>
```

##### Application 2

Pour chacune des variables créées à l'application 1, vérifier leur type dans la console python en utilisant la fonction `type()`.

________

[Feuille d'exercice](./Exercices/Exercices_variables.md)
________

Leçon 4 : [Séquences d'instructions](./Séquences.md)