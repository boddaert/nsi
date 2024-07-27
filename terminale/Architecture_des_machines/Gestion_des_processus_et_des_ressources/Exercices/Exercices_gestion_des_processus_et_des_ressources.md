# Exercices

## Exercice 1

[Activité : Problème du boulanger](./../Activité_problème_du_boulanger.md)

## Exercice 2

1. Situation n°1 :
```
P1 acquiert R1
P2 acquiert R2
P3 attend R1
P2 libère R2
P2 attend R1
P1 libère R1
```

2. Situation n°2 :
```
P1 acquiert R1
P2 acquiert R3
P3 acquiert R2
P1 attend R2
P2 libère R3
P3 attend R1
```

3. Situation n°3 :
```
P1 acquiert R1
P2 acquiert R2
P3 attend R2
P1 attend R2
P2 libère R2
P3 acquiert R2
```

4. Situation n°4 :
```
P2 acquiert R3
P3 attend R3
P1 attend R3
P1 acquiert R1
P3 attend R1
P2 attend R1
```

a) Pour chacune des situations ci-dessus, indiquer lequel provoque un interblocage en justifiant.

b) Modifier la ou les situations pour que l'interblocage ne se produise plus.

## Exercice 3

| PID | Durée d'exécution | Instant d'arrivée | Priorité |
| :---: | :---: | :---: |:---: |
| $1$ | $3$ | $t3$ | $1$ |
| $2$ | $3$ | $t2$ | $2$ |
| $3$ | $4$ | $t0$ | $3$ |

Dans cet exercice, le numéro de priorité est d'autant plus petit que la priorité est grande.

Donner l'ordonnancement des processus selon la prolitique de priorité préemptive.

## Exercice 4

a) Écrire une classe `Processus` qui a comme attribut un PID, un instant d'arrivée, une durée d'exécution et une priorité.

b) Écrire, pour chaque attribut, l'accesseur permettant de renvoyer la valeur de l'attribut correspondant.

c) Écrire une fonction `premier_arrive_premier_servi(liste_processus : Liste)->Liste` qui prend en paramètre une liste d'objets Processus et renvoie une liste indiquant l'ordonnancement des processus selon la politique du premier arrivé, premier servi.

_____________

[Sommaire](./../../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 
