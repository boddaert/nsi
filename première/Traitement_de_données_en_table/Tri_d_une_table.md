# Tri d'une table

## I. Définitions

*Trier* une table de données, c'est organiser les données pour qu'elles apparaissent dans un certain ordre.

Généralement, les informaticiens trient les tables de données en fonction d'un ou de deux critères. C'est-à-dire en fonction d'un ou de deux attributs.

## II. Fonctions de tri

En Python, il existe les fonctions `sorted()` et `sort()` et permettent toutes les deux de trier une liste d'entiers ou de caractères dans l'ordre lexicographique.

Néanmoins, une différence subsiste, `sort()` est un tri en place, contrairement à `sorted()`.

Un *tri en place* est un tri qui modifie directement la structure en mémoire. Ce tri ne renvoie rien :

```python
>>> l = [5, 8, 2, 0, 7, 9, 2, 1]
>>> l.sort()
>>> l
[0, 1, 2, 2, 5, 7, 8, 9]
```

Alors que la fonction `sorted()` ne modifie pas en mémoire mais renvoie une nouvelle liste triée :

```python
>>> l = [5, 8, 2, 0, 7, 9, 2, 1]
>>> l_triee = sorted(l)
>>> l_triee
[0, 1, 2, 2, 5, 7, 8, 9]
>>> l
[5, 8, 2, 0, 7, 9, 2, 1]
```

## III. Trier une table en fonction d'un attribut

La fonction `sorted()` peut prendre comme second argument une fonction appelée `key`.

Cette fonction renvoie le critère ou l'attribut sur lequel la fonction `sorted()` trie :

```python
def age(personne : dict)->int :
    return personne["Année de naissance"]
```

La fonction `sorted()` peut également prendre un troisème argument indiquant si l'ordre de tri doit être inversé.

Voici donc comment obtenir la liste des personnes du moins âgé au plus âgé :

```python
>>> sorted(personnes, key=age, reverse=True)
[{'Sexe': 'F', 'Prénom': 'Charlotte', 'Année de naissance': 1988}, {'Sexe': 'F', 'Prénom': 'Béatrice', 'Année de naissance': 1964}, {'Sexe': 'M', 'Prénom': 'Alphonse', 'Année de naissance': 1932}]
```

##### Application 1

a) Utiliser la fonction de tri `sorted()` afin de trier les produits du magasin par ordre croissant de prix.

b) Utiliser la fonction de tri `sorted()` afin de trier les produits du magasin par ordre décroissant de quantité.

___________

[Sommaire](./../README.md)