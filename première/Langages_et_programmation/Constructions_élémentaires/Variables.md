# Variables

## I. Définitions

> [!IMPORTANT]
> Une *variable* est un nom qui possède une valeur.
> Nous disons qu'une valeur est **affectée** à une variable.

## II. Affectations de variable

### a) Affectation simple

Nous pouvons affecter n'importe quelle valeur à une variable en Python avec l'opérateur d'affectation ``=``.

> [!TIP]
> Par exemple :
> ```python
> >>> ma_variable = 42
> ```

Pour connaître la valeur contenue dans une variable, il suffit de **l'appeler** en écrivant son nom.

> [!TIP]
> Par exemple :
> ```python
> >>> ma_variable
> 42
> ```

### b) Ré-affectation

Pour modifier la valeur contenue dans une variable, il suffit d'affecter une nouvelle valeur à la variable.

> [!TIP]
> Par exemple :
>```python
>>>> ma_variable = 42
>>>> ma_variable
>42
>>>> ma_variable = 67
>>>> ma_variable
>67
>```

L'ancienne valeur est alors **écrasée** par la nouvelle valeur.

#### <ins>Application 1</ins>

a) Dans la console python et en utilisant l'opérateur d'affectation, affecter :

1. la variable `variable_a` avec la valeur `1`.
2. la variable `variable_b` avec la valeur `9.99`.
3. la variable `variable_c` avec la valeur `"hello world"`.
4. la variable `variable_d` avec la valeur `True`.

b) Vérifier les valeurs contenues dans chacune de ces variables en les appelant dans la console Python.

## III. Type d'une variable

Le type d'une variable est le type de la valeur qu'elle contient.

Nous pouvons, comme pour les valeurs, connaître le type des variables en utilisant la fonction ``type()``.

> [!TIP]
> Par exemple :
>```python
>>>> type(ma_variable)
><class 'int'>
>```

#### <ins>Application 2</ins>

Pour chacune des variables créées à l'application $1$, vérifier leur type dans la console python en utilisant la fonction `type()`.

________

[Exercices](./Exercices/Exercices_variables.md)
________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 