# Représentation des entiers naturels

## I. Définitions

Un *nombre* désigne une quantité.

La *représentation* d'un nombre est le symbole que nous lui associons.

Il existe plusieurs représentations pour un même nombre.

Par exemple le chiffre cinq peut s'écrire : $5$, $cinq$, $V$, ⚄, ...

## II. Les ensembles de nombre

```mermaid
flowchart LR
  subgraph Entiers Naturels
    direction RL
    A[1]
    B[4]
    C[9]
    subgraph Entiers Relatifs
        direction RL
        D[-3]
        E[-7]
        F[-6]
        subgraph Réels
            direction RL
            G[2.2]
            H[7.34]
            I[3.14]
        end
    end
  end
```