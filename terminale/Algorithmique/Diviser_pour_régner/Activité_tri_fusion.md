# Activité Tri Fusion

Nature : Débranchée.

Matériel : Une feuille de brouillon, un crayon et une paire de ciseaux.

Prérequis : [Algorithmes de tri](./Rappels_sur_les_algorithmes_de_tri.md).

À faire : Par deux.

## I. Objectif

L'objectif de cette activité est de trier une liste récursivement en appliquant la méthode "Diviser pour régner".

## II. Algorithme du Tri Fusion

L'algorithme du tri fusion est le suivant :

```
Algorithme : tri_fusion(liste)
Entrées : liste une liste
Sorties : Une liste

Si la longueur de la liste est supérieure ou égal à deux, alors :
    Découper en deux (au milieu) la liste en deux sous-listes
    Ré-applquer l'algorithme du Tri Fusion sur chacune des deux sous-listes obtenues
    Fusionner les deux sous-listes triées en une liste triée
    Renvoyer la liste fusionnée
Sinon :
    Renvoyer cette liste (puisqu'elle est implicitement triée)
```

## III. Travail à faire

a) En vous munissant d'une paire de ciseaux et d'un crayon, dérouler à la main l'algorithme du tri fusion sur la liste ci-dessous et dessiner sur papier l'état des listes et des sous-listes obtenues à chaque étape de l'algorithme.

<img src="./img/liste_activite_tri_fusion.png" width=800>

b) À l'aide de votre dessin, compter le nombre de comparaisons effectuées.

c) Comparer ce nombre avec le nombre de comparaisons qu'effectuerait le tri par sélection/insertion sur cette même liste.

d) Le coût algorithmique du tri fusion (en complexité temporelle) est-il meilleur que celui du tri par sélection/insertion ?

____________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 