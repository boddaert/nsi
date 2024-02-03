# Activité Tri Fusion

Nature : Débranchée

Matériel : Une feuille, un crayon et une paire de ciseaux

Prérequis : Aucun

Groupe : Par deux

## I. Objectif

L'objectif de cette activité est de trier une liste récursivement en appliquant la méthode "Diviser pour régner".

## II. Algorithme du Tri Fusion

L'algorithme du tri fusion est le suivant :

- Si la longueur de la liste est supérieure à $2$ :

    + Découper en deux (au milieu) la liste en deux sous-listes.

    + Ré-appliquer l'algorithme du tri fusion sur les deux sous-listes obtenues.

    + Fusionner les deux sous-listes triées en une liste triée.

    + Renvoyer la liste fusionnée.

- Si la liste contient un seul élément :

    + Renvoyer cette liste (car elle est implicitement triée).

## III. Travail à faire

a) En vous munissant d'un ciseau et d'un crayon, dérouler à la main l'algorithme du tri fusion sur la liste ci-dessous et dessiner sur papier l'état des listes et des sous-listes obtenues à chaque étape de l'algoriithme :

![Image](./img/liste_activite_tri_fusion.png)

b) À l'aide de votre dessin, compter le nombre de comparaisons effectuées.

c) Comparer ce nombre avec le nombre de comparaisons qu'effectuerait le tri par sélection/insertion sur cette même liste.

d) Le coût algorithmique du tri fusion (en complexité temporelle) est-il meilleur que celui du tri par sélection/insertion ?

____________

[Sommaire](./../README.md)