# Décidabilité et calculabilité

## I. Introduction

Le pouvoir de l'algorithmique n'est pas infini.

Nous savons que certains problèmes ne peuvent être résolus parfaitement de manière automatique.

L'étude des possibilités et limites des algorithmes définit le champs de la calculabilité, qui est l'un des piliers de la science informatique.

Ce champs d'étude a été largement travaillé par les mathématiciens et informaticiens de l'époque :

![image](./img/hilbert_godel_church_turing.png)

## II. Historique

### a) Acte 1 : Les problèmes de Hilbert

En 1900, un des plus grands mathématiciens de l'époque, David Hilbert (1862-1943) énonce ce que l'on appellera plus tard le « Programme de Hilbert », à savoir une liste des vingt-trois plus grands problèmes qui, selon lui, restaient à résoudre en mathématiques.

Le programme de Hilbert adopte une démarche formaliste qui postule que toute théorie mathématique est fondée sur des axiomes considérés comme vrais a priori et que toutes les vérités de la théorie, les théorèmes, doivent être démontrés en un nombre fini d'étapes de manière mécaniquement vérifiable (par un algorithme).

### b) Acte 2 : La logique implacable de Gödel

En 1930, un jeune mathématicien autrichien, Kurt Gödel (1906-1978), met fin au rêve formaliste de Hilbert et démontre son premier théorème d'incomplétude qui stipule que dans toute axiomatique des mathématiques contenant au moins les axiomes de l'arithmétique, il existe des propositions vraies mais qui sont indémontrables dans la théorie.

Ce théorème fait l'effet d'un coup de tonnerre dans le petit cercle des mathématiciens mais dépasse rapidement ce cadre et affecte aussi grandement l'informatique naissante, influençant notamment des mathématiciens comme Alonzo Church et Alan Turing.

De manière très schématique, la preuve de Gödel consiste - à travers un codage numérique des propositions et de la véracité mathématique - à construire, au sein de la théorie, une proposition $P$ du style « Je ne suis pas démontrable ».

Cette proposition mène à une conclusion inattendue. En effet, si nous supposons $P$ fausse, alors cela signifierait « Je suis démontrable » et donc $P$ serait vraie ! C'est impossible, donc $P$ est à la fois vraie et indémontrable.

### c) Acte 3 : Le problème de décision et de l'arrêt

David Hilbert formula un nouveau problème en 1928 : le problème de la décision ou *Entscheidungsproblem* en allemand. La question est « Y a-t-il un algorithme qui, étant donné un système formel et une proposition logique dans ce système, pourra décider sans ambiguïté si cette proposition est vraie ou fausse dans le système formel ? »

En 1936, Alonzo Church (1903-1995) et Alan Turing montrent de manière indépendante que la réponse à cette question est négative.

Alan Turing (1912-1954) est un mathématicien anglais. Il présente sa machine en 1936, rebaptisée « machine de Turing » par son directeur de thèse Alonzo Church. Cette machine n'a pas de finalité pratique bien qu'elle ait été réellement fabriquée et que de nombreux simulateurs existent. C'est plutôt une machine conceptuelle qui permet d'expliciter de manière précise ce qu'est un programme et de présenter de manière rigoureuse des algorithmes de tous genres, de trouver des limites à ce qui est calculable et de permettre l'exploration systématique de la complexité algorithmique à travers un modèle simple et non ambigu de calcul.

Turing pose alors le problème suivant : « Existe-t-il un programme qui, prenant en entrée un autre programme et son entrée, determine si ce programme finit par s'arrêter avec cette entrée ou boucle indéfiniment ? »

Il répond par la négative et montre que ce problème de l'arrêt répond aussi au problème de la décision. Church propose une preuve indépendante du même résultat grâce à son formalisme du $\lamda$-calcul.

## III. Définitions

Une fonction $f$ est *calculable* s'il existe une méthode/un algorithme qui, étant donné un argument $x$, calcule $f(x)$ en un nombre finis d'étape.

La fonction `pgcd()` est une fonction calculable puisqu'elle permet de calculer le PGCD de n'importe quel argument $x$ en un nombre finis d'étape.

Les *méthodes de calcul* $\lamda$-calcul et machine de Turing permettent de définir des fonctions calculables.

Alonzo Church a démontré que ces deux méthodes de calculs sont équivalentes.

La méthode de calcul $\lamda$-calcul a donné naissance à la programmation fonctionnelle, se reposant essentiellement sur la récursivité.

La méthode de calcul de la machine de Turing a donné naissance à la programmation itérative.

Ainsi, Alonzo Church a démontré, par conséquent, que chaque fonction récursive avait un équvalent itératif et vice-versa.

Un *problème de décision* est une question mathématique dont la réponse est "oui" ou "non".

Un problème de décision est *décidable* s'il existe un algorithme qui se termine en un nombre fini d'étapes pour chaque instance du problème.

> Cette définition revient à dire que la fonction qui correspond au problème de décision est calculable.

Nous admettrons que les langages de programmation actuels (JavaScript, C, Perl, Java, Fortran, etc...) sont aussi des méthodes de calculs valables.

##### Application 1

"Ce nombre est-il un nombre premier ?"

a) Dire s'il s'agit d'un problème de décision.

b) Indiquer s'il est décidable. Si oui, écrire une fonction `est_premier(x : int)->bool` prenant en paramètre un nombre entier et renvoie $True$ s'il est premier, $False$ sinon.

c) Enfin, dire si la fonction `est_premier()` est calculable.

## IV. Problème de l'arrêt

### a) Programmes en tant que données

Un programme (écrit en Python par exemple) n’est autre qu’une chaîne de caractères : c’est le texte même du programme.

Or les chaines de caractères peuvent être utilisées en paramètre des fonctions d'un programme :

```python
programme = '''
for i in range(3):
    print("Le Python, c'est cool :-)")
'''
exec(programme)
```

### b) Problème de l'arrêt

Compte tenu du fait que les programmes qui ne se terminent pas peuvent avoir des conséquences fâcheuses, est-il possible de concevoir un programme nous permettant de nous indiquer si l'execution d'un programme passé en paramètre peut se terminer ?

Ce problème, que l'on appelle "Problème de l'arrêt" est un problème de décision pour lequel les instances sont les programmes :

"Ce programme se termine t-il ?"

### c) Preuve par l'absurde de l'indécidabilité du problème de l'arrêt

Considérons une fonction `arret(f, e)` qui prend en paramètre une fonction `f` et une entrée `e` et renvoie $True$ si $f(e)$ s'arrête et $False$ sinon.

##### Application 2

```python
def paradoxe(e) :
    if arret(paradoxe, e):
        while True :
            pass
    else :
        return True
```

a) Que penser de la fonction `paradoxe()` ?

b) Démontrer par l'absurde que le problème de l'arrêt n'est pas décidable.

____________

[Sommaire](./../README.md)