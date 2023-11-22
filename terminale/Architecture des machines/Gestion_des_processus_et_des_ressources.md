# Gestion des processus et des ressources par un système d'exploitation

Petit rappel sur la définition d'un système d'exploitation : [Systèmes d'exploitation](./../../première/Architecture_des_machines/Systèmes_d_exploitation.md).

Cette leçon décrit le fonctionnement de la gestion du processeur par un système d'exploitation et répond à la question : Quel programme exécuter ?

## I. Processus et ressources

### a) Définitions

Un *programme* est statique: c’est un fichier contenant une suite d’instructions qui lorsqu’elles sont exécutées modifient l’état du processeur et de la mémoire afin de réaliser une tâche donnée.

Un *processus* est dynamique : Il s'agit d'un programme en cours d'exécution. Il incarne l'état du programme dans le temps.

Nous caractérisons un processus par :

- Un identifiant appelé *PID*.

- Un état : l'état dans lequel se trouve le processus.

- Un espace mémoire : l'espace mémoire alloué necéssaire à l'exécution du programme.

- Une durée d'exécution : le temps necéssaire à l'exécution du programme.

- Un ensemble de ressources : les ressources dont a besoin le processus.

Une *ressource* est une entité matérielle ou logicielle dont a besoin un processus pour s'exécuter.

Une ressource est soit libre soit occupée par un processus, elle possède un certain nombre de point d'accès.

### b) Etats d'un processus

```mermaid
stateDiagram-v2
    direction TB
    A : PRET
    note right of A
        Un processus dans l'état
        PRET attend que le
        processeur le choissise
        lors de l'élection pour
        qu'il s'exécute.
    end note
    B : ELU
    note right of B
        Un processus dans l'état ELU a
        été choisis et s'exécute.

        Si le processeur décide d'exécuter
        un processus prioritaire, le 
        processus dont il avait la charge
        passe dans l'état PRET.

        Si l'une des ressource dont il
        a besoin n'est pas disponible,
        le processus passe dans l'état
        BLOQUE.
    end note
    C : BLOQUE
    note right of C
        Un processus dans l'état BLOQUE
        attend que la ressource dont
        il a besoin soit disponible.

        Si la ressource est disponible,
        le processus prend la ressource
        et passe dans l'état PRET.
    end note
    [*] --> A : Création
    A --> B : Election
    B --> A : Préemption
    B --> C : Blocage
    B --> [*] : Terminaison
    C --> A : Déblocage
```

### c) Visualisation des processus

Nous visualisons facilement les processus actuels en exécutant la commande `ps` dans le terminal :

```bash
    PID TTY          TIME CMD
  11737 pts/1    00:00:00 bash
  13000 pts/1    00:00:00 ps
```

Nous remarquons que la commande `ps` est elle-même un programme en cours d'exécution. (Ainsi que `bash` pour le terminal)

Nous pouvons afficher plus d'informations des processus et en temps réel avec la commande `top` comme :

- `USER` : L’utilisateur qui exécute le processus.

- `%CPU` : L’utilisation en pourcentage du processeur du processus.

- `%MEM` : Le pourcentage de la taille en mémoire utilisée par le processus.

- `STAT` : Le code d’état du processus (`Z` pour Zombie, `S` pour Dormant et `R` pour en cours d’exécution).

Un processus peut créer un autre processus, le *PPID* décrit alors l'identifiant du processus père.

La commande `pstree` permet de visualiser sous forme d'arbre tous les processus engendrés par leur prédécésseur.

Le processus `init` est le premier programme lancé par la machine et a comme PID : $1$.

## II. Politiques d'ordonnancement

Une *politique d'ordonnancement* est l'ordre, décidé par le processeur, par lequel les processus seront exécutés.

Voici, pour illustrer les différentes politiques, un exemple d'ensemble de trois processus :

| PID | Durée d'exécution | Temps d'arrivée | Priorité |
| :---: | :---: | :---: |:---: |
| $1$ | $4$ | $t0$ | $0$ |
| $2$ | $2$ | $t3$ | $1$ |
| $3$ | $3$ | $t4$ | $2$ |

### a) Premier arrivé, premier servi

La politique du premier arrivé, premier servi est comme son nom l'indique un ordre d'exécution des processus selon leur ordre d'arrivée.



| PID du processus aloué au processeur | Temps |
| :---: | :---: |
| $1$ | $t0$ |
| $1$ | $t1$ |
| $1$ | $t2$ |
| $1$ | $t3$ |
| $2$ | $t4$ |
| $2$ | $t5$ |
| $3$ | $t6$ |
| $3$ | $t7$ |
| $3$ | $t8$ |


## III. Problèmes

### Exclusion mutuelle
### Interblocage

#### Coffman