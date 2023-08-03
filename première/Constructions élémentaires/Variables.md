# Variables

## I. Définitions

Une *variable* est un nom qui possède une valeur.

On dit qu'une valeur est affectée à une variable.

## II. Affectations de variable

### a) Affectation simple

On peut affecter n'importe quelle valeur à une variable en Python avec l'opérateur d'affectation ``=`` :

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

- la variable `ma_variable_a` avec la valeur `1`
- la variable `ma_variable_b` avec la valeur `9.99`
- la variable `ma_variable_c` avec la valeur `"hello world"`
- la variable `ma_variable_d` avec la valeur `True`

Puis, vérifier en appelant chacune des variables les valeurs associées.

## III. Type d'une variable

Le type d'une variable est le type de la valeur qu'elle contient.

On peut, comme pour les valeurs, connaître le type des variables en utilisant la fonction ``type()`` :

```python
>>> type(ma_variable)
<class 'int'>
```

##### Application 2

Pour chacune des variables créées à l'application 1, vérifier leur type dans la console python en utilisant la fonction `type()`

## Exercices

### Exercice 1

A l'issue de l'exécution de chacun des programmes suivants, indiquer la valeur affectée à la variable `mystere` :

a) Programme 1

```python
ma_variable = 56.01
mystere = True
```

b) Programme 2

```python
ma_variable = "hello world"
mystere = ma_variable
```

c) Programme 3

```python
ma_variable = 3
mystere = ma_variable * ma_variable
```

d) Programme 4

```python
mystere = 10
mystere = mystere + 1
```

e) Programme 5

```python
ma_variable = 20
mystere = ma_variable + 20
ma_variable = 30
mystere = mystere + ma_variable
```

f) Programme 6

```python
ma_variable = 5
mystere = mystere + ma_variable
```
________

Leçon 4 : [Séquences d'instructions](./Séquences.md)