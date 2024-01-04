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

Répondre aux questions suivantes :

a) Définir "trier une liste".

b) Rappeler la méthode des algorithmes des tris par insertion et par sélection vus en Première.

c) Rappeler la complexité algorithmique en temps des algorithmes du tri par insertion et par sélection.

d) Dérouler à la main l'algorithme du tri fusion sur la liste ci-dessous et dessiner l'état des listes et des sous-listes obtenues à chaque étape :

![Image](./img/liste_activite_tri_fusion.png)

____________

[Sommaire](./../README.md)