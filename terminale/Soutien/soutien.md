# Soutien

## Exercice 1

a) Programme 1

```python
a = 5
b = 0
while a > b :
    a = a - 1
    b = b + 1
```

b) Programme 2

```python
a = False
b = 1
while not a == True :
    a = True
    b = b + 1
```

c) Programme 3

```python
a = 0
b = 0
while a < 10 or b > -5 :
    a = a + 1
    b = b - 1
```

e) Programme 4

```python
a = 1
b = 5
while a < 10 or b < 10 :
    a = a * 2
    b = b + 1
```

Compléter la trace d'exécution suivante pour chaque programme :

| N° de ligne | Valeur affectée à $a$ | Valeur affectée à $b$ |
| --- | --- | --- |
| 1 | | |

## Exercice 2

a) Programme 1

```python
a = 0
for i in range(0,10) :
    a = a + 2
```

b) Programme 2

```python
a = 0
for i in range(0,10):
    a = a + i
```

c) Programme 3

```python
a = 0
b = 10
for i in range(-5,5):
    a = i**2
    b = b - a
```

Compléter la trace d'exécution suivante pour chaque programme :

| N° de ligne | Valeur affectée à $a$ | Valeur affectée à $b$ | Valeur affectée à $i$ |
| --- | --- | --- | --- |
| 1 | | | |

## Exercice 3

a) Programme 1

```python
l = [9, 7, 5, 3]
for i in range(len(l)) :
    x = l[i]
```

b) Programme 2

```python
l = [7, 9, 3, 1, 10]
x = 0
for i in range(len(l)):
    x = x + l[i]
```

c) Programme 3

```python
l = [56, 89, 23]
x = 0
for elt in l:
    x = x + elt
```

d) Programme 4

```python
l = [-1, 8, -67, 9]
x = []
for elt in l :
    if elt < 0 :
        x.append(elt)
```

Compléter la trace d'exécution suivante pour chaque programme :

| N° de ligne | Valeur affectée à $i$ | Valeur affectée à $l[i]$ | Valeur affectée à $elt$ | Valeur affectée à $x$ |
| --- | --- | --- | --- | --- |
| 1 | | | | |

_________________

[Sommaire](./../README.md)