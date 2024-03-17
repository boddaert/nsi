# Exercices

## Exercice 1

a) Pour chacun des scénario ci-dessous, indiquer lequel provoque un interblocage en justifiant.

```
Situation n°1:
P1 acquiert R1
P2 acquiert R2
P3 attend R1
P2 libère R2
P2 attend R1
P1 libère R1
```

```
Situation n°2:
P1 acquiert R1
P2 acquiert R3
P3 acquiert R2
P1 attend R2
P2 libère R3
P3 attend R1
```

```
Situation n°3:
P1 acquiert R1
P2 acquiert R2
P3 attend R2
P1 attend R2
P2 libère R2
P3 acquiert R2
```

b) Modifier la situation pour que l'interblocage ne se produise plus.

c) Pour chacune des situations, indiquer l'état des processus à chaque instant.

## Exercice 2

| PID | Durée d'exécution | Instant d'arrivée | Priorité |
| :---: | :---: | :---: |:---: |
| $1$ | $3$ | $t3$ | $1$ |
| $2$ | $3$ | $t2$ | $2$ |
| $3$ | $4$ | $t0$ | $3$ |

Dans cet exercice, le numéro de priorité est d'autant plus petit que la priorité est grande.

Donner l'ordonnancement des processus selon la prolitique de priorité préemptive.

## Exercice 3

a) Ecrire une classe `Processus` qui a comme attribut un PID, un instant d'arrivée, une durée d'exécution et une priorité.

b) Ecrire, pour chaque attribut, l'accesseur permettant de renvoyer la valeur de l'attribut correspondant.

c) Ecrire une fonction `premier_arrive_premier_servi(liste_processus : Liste)->Liste` qui prend en paramètre une liste d'objets Processus et renvoie une liste indiquant l'ordonnancement des processus selon la politique du premier arrivé, premier servi.

_____________

[Sommaire](./../../../README.md)
