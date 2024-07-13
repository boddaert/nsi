# Gestion des processus et des ressources par un système d'exploitation

## I. Introduction 

Cette leçon décrit le fonctionnement de la gestion du processeur par un système d'exploitation et répond à la question : 

$\to$ *Quel programme exécuter ?*

Rappels sur les missions d'un système d'exploitation : [Systèmes d'exploitation](./../../../première/Architecture_des_machines/Systèmes_d_exploitation/Systèmes_d_exploitation.md).

#### <ins>Application 1</ins>

Lire la leçon [Systèmes d'exploitation](./../../../première/Architecture_des_machines/Systèmes_d_exploitation/Systèmes_d_exploitation.md).

## II. Processus et ressources

### a) Définitions

> [!IMPORTANT]
> Un *programme* est statique: c’est un fichier contenant une suite d’instructions qui lorsqu’elles sont exécutées modifient l’état du processeur et de la mémoire afin de réaliser une tâche donnée.

> [!IMPORTANT]
> Un *processus* est dynamique : Il s'agit d'un programme en cours d'exécution. Il incarne l'état du programme dans le temps.

> [!IMPORTANT]
> Un processus est caractérisé par :
>
> - Un *identifiant* appelé *PID*.
>
> - Un *état* : l'état dans lequel se trouve le processus.
>
> - Un *espace mémoire* : l'espace mémoire alloué necéssaire à l'exécution du processus.
>
> - Une *durée d'exécution* : le temps necéssaire à l'exécution du processus.
>
> - Un *ensemble de ressources* : les ressources dont a besoin le processus.

> [!IMPORTANT]
> Une *ressource* est une entité matérielle ou logicielle dont a besoin un processus pour s'exécuter. Elle est soit libre soit occupée par un processus et possède un certain nombre de point d'accès.

### b) Etats d'un processus

> [!IMPORTANT]
> ```mermaid
> stateDiagram-v2
>     direction TB
>     A : PRET
>     note right of A
>         Un processus dans l'état
>         PRET attend que le
>         processeur le choissise
>         lors de l'élection pour
>         qu'il s'exécute.
>     end note
>     B : ELU
>     note right of B
>         Un processus dans l'état ELU a
>         été choisis et s'exécute.
>
>         Si le processeur décide d'exécuter
>         un processus prioritaire, le 
>         processus dont il avait la charge
>         passe dans l'état PRET.
>
>         Si l'une des ressource dont il
>         a besoin n'est pas disponible,
>         le processus passe dans l'état
>         BLOQUE.
>     end note
>     C : BLOQUE
>     note right of C
>         Un processus dans l'état BLOQUE
>         attend que la ressource dont
>         il a besoin soit disponible.
>
>         Si la ressource est disponible,
>         le processus prend la ressource
>         et passe dans l'état PRET.
>     end note
>     [*] --> A : Création
>     A --> B : Election
>     B --> A : Préemption
>     B --> C : Blocage
>     B --> [*] : Terminaison
>     C --> A : Déblocage
> ```

### c) Visualisation des processus

Les processus actuels sont visibles en exécutant la commande `ps` dans le terminal.

> [!TIP]
> Par exemple :
> ```bash
>     PID TTY          TIME CMD
>   11737 pts/1    00:00:00 bash
>   13000 pts/1    00:00:00 ps
> ```

> [!NOTE]
> Nous remarquons que la commande `ps` est elle-même un programme en cours d'exécution (ainsi que `bash` pour le terminal).

Plusieurs autres informations concernant les processus peuvent être affichées à l'aide de la commande `top` comme :

- `USER` : L’utilisateur qui exécute le processus.

- `%CPU` : L’utilisation en pourcentage du processeur du processus.

- `%MEM` : Le pourcentage de la taille en mémoire utilisée par le processus.

- `STAT` : Le code d’état du processus (`Z` pour Zombie, `S` pour Dormant et `R` pour en cours d’exécution).

Un processus peut créer un autre processus, le *PPID* décrit alors l'identifiant du processus père.

La commande `pstree` permet de visualiser sous forme d'arbre tous les processus engendrés par leur prédécésseur.

Le processus `init` est le premier programme lancé par la machine et a comme PID : $1$.

#### <ins>Application 2</ins>

a) Sur le terminal de votre ordinateur, lancer la commande `ps` et décrire la réponse.

b) Sur le terminal de votre ordinateur, lancer la commande `top` et décrire la réponse.

c) Sur le terminal de votre ordinateur, lancer la commande `pstree` et décrire la réponse.

## III. Politiques d'ordonnancement

> [!IMPORTANT]
> Une *politique d'ordonnancement* est l'ordre, décidé par le processeur, par lequel les processus seront exécutés.

Prenons trois processus :

| PID | Durée d'exécution | Instant d'arrivée | Priorité |
| :---: | :---: | :---: |:---: |
| $1$ | $4$ | $t0$ | $0$ |
| $2$ | $2$ | $t2$ | $1$ |
| $3$ | $3$ | $t4$ | $2$ |

### a) Premier arrivé, premier servi

> [!IMPORTANT]
> La politique du *premier arrivé, premier servi* est comme son nom l'indique un ordre d'exécution des processus selon leur ordre d'arrivée dans la file d'attente.

> [!TIP]
> Par exemple :
> | PID du processus aloué au processeur | Instant |
> | :---: | :---: |
> | $1$ | $t0$ |
> | $1$ | $t1$ |
> | $1$ | $t2$ |
> | $1$ | $t3$ |
> | $2$ | $t4$ |
> | $2$ | $t5$ |
> | $3$ | $t6$ |
> | $3$ | $t7$ |
> | $3$ | $t8$ |

#### <ins>Application 3</ins>

Donner l'ordonnancement des processus suivants selon la politique du premier arrivé, premier servi.

| PID | Durée d'exécution | Instant d'arrivée | Priorité |
| :---: | :---: | :---: |:---: |
| $1$ | $2$ | $t0$ | $1$ |
| $2$ | $5$ | $t1$ | $3$ |
| $3$ | $3$ | $t2$ | $2$ |

### b) Par tourniquet

> [!IMPORTANT]
> La politique *par tourniquet* (*Round-Robin* en anglais) est un ordre d'exécution qui utilise une seconde unité de temps appelée *quantum de temps*.
>
> Cette politique consiste à exécuter les processus dans leur ordre d'arrivée uniquement le temps du quantum. Si le processus ne s'est pas terminé, il rejoint la file d'attente.

> [!TIP]
> Par exemple, avec quantum $= 3$ :
>
> | PID du processus aloué au processeur | Instant |
> | :---: | :---: |
> | $1$ | $t0$ |
> | $1$ | $t1$ |
> | $1$ | $t2$ |
> | $2$ | $t3$ |
> | $2$ | $t4$ |
> | $1$ | $t5$ |
> | $3$ | $t6$ |
> | $3$ | $t7$ |
> | $3$ | $t8$ |

#### <ins>Application 4</ins>

Donner l'ordonnancement des processus suivants selon la politique par tourniquet.

| PID | Durée d'exécution | Instant d'arrivée | Priorité |
| :---: | :---: | :---: |:---: |
| $1$ | $2$ | $t0$ | $1$ |
| $2$ | $5$ | $t1$ | $3$ |
| $3$ | $3$ | $t2$ | $2$ |

### c) Par priorité préemptive

> [!IMPORTANT]
> La politique d'ordonnancement *par priorité préemptive* est un ordre d'exécution des processus en fonction de leur ordre d'arrivé et de leur priorité (plus la priorité d'un processus est grande, plus il est prioritaire).

> [!TIP]
> Par exemple :
> | PID du processus aloué au processeur | Instant |
> | :---: | :---: |
> | $1$ | $t0$ |
> | $1$ | $t1$ |
> | $2$ | $t2$ |
> | $2$ | $t3$ |
> | $3$ | $t4$ |
> | $3$ | $t5$ |
> | $3$ | $t6$ |
> | $1$ | $t7$ |
> | $1$ | $t8$ |

#### <ins>Application 5</ins>

Donner l'ordonnancement des processus suivants selon la politique par priorité préemptive.

| PID | Durée d'exécution | Instant d'arrivée | Priorité |
| :---: | :---: | :---: |:---: |
| $1$ | $2$ | $t0$ | $1$ |
| $2$ | $5$ | $t1$ | $3$ |
| $3$ | $3$ | $t2$ | $2$ |

## IV. Interblocage

L'une des missions du système d'exploitation est le partage des ressources par les processus. Une telle gestion peut engendrer quelques problèmes comme l'exclusion mutuelle ou l'interblocage (*Deadlock* en anglais).

> [!IMPORTANT]
> L'*interblocage*  est un phénomène qui survient lorsque deux processus possèdent une ressource chacun et attendent mutuellement la disponibilité de l'autre pour se terminer.

> [!TIP]
> Par exemple :
> ```mermaid
> flowchart TB
>     A((P1))
>     B((P2))
>     C[/R1\]
>     D[/R2\]
>     A --possède-->C
>     A-. souhaite .-> D
>     B --possède-->D
>     B-. souhaite .->C
> ```

____________

[Exercices](./Exercices/Exercices_gestion_des_processus_et_des_ressources.md)

____________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 