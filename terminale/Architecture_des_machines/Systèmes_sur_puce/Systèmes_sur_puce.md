# Systèmes sur puce

## I. Définitions

> [!IMPORTANT]
> Les *systèmes sur puce* (*System on Chip* en anglais) ou *microcontrôleurs* sont des systèmes rassemblant sur une même puce tous les principaux composants d'un ordinateur :

<img src="./img/soc.png" width=300>

Nous y trouvons des microprocesseurs, des zones de mémoire, des périphériques d'entrée/sortie, etc...

Ces systèmes sont utilisés dans toutes les machines informatiques embarquées miniatures comme les téléphones intelligents, les tablettes, les assistants vocaux, montres connectées, etc...

## II. Architecture

À la différence que les programmes ne soient pas situés à l'intérieur de la mémoire, l'architecture des systèmes sur puce est sensiblement la même que celle de John Von Neumann (cf [Modèle de Von Neumann](./../../../première/Architecture_des_machines/Modèle_Von_Neumann/Modèle_Von_Neumann.md)):

<img src="./img/architecture_soc.png" width=800>

Les systèmes sur puce disposent bien sûr d'une unité centrale de calcul (*CPU* pour *Central Processing Unit*).

Ils disposent également de différents niveaux de mémoire (mémoire cache, mémoire *ROM* pour *Read-Only Memory* et mémoire *RAM* pour *Random Acess Memory*) et éventuellement d'un accès rapide à une mémoire externe.

Ils peuvent disposer d'une unité de traitement graphique (*GPU* pour *Graphic Processor Unit*).

Lorsqu'il est présent, le contrôleur *DMA* (pour *Direct Memory Acces*) permet un transfert des données de ou vers un périphérique, sans solliciter le processeur.

## III. Avantages et inconvénients

### a) Avantages

- La taille est réduite.

- La consommation d'énergie est réduite car les distances sont raccourcies.

- Le dispositif chauffe moins, donc les techniques de refroidissement sont simplifiées.

- Les différents éléments s'intègrent mieux les uns avec les autres car ils sont conçus conjointement.

- La sécurité est normalement améliorée car les différents éléments sont conçus conjointement.

### b) Inconvénients

- Si un élément tombe en panne, il faut tout changer.

- La conception est souvent plus complexe.

#### <ins>Application 1</ins>

a) Rechercher sur votre téléphone le nom du système sur puce utilisé.

b) Rechercher sur internet les caractéristiques embarquées de ce système.

____________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 