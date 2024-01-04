# Exercices

## Exercice 1

L'algorithme de recherche par dichotomie est un algorithme utilisant le principe de "Diviser pour régner".

a) Rappeler les étapes de l'algorithme de recherche dichotomique (via un schéma).

b) Décrire les étapes "Diviser", "Régner" et "Combiner" de l'algorithme de recherche dichotomique.

c) Ecrire une fonction récursive ``recherche_dichotomique_recursive(l : list, el : int)->int`` prenant en paramètre une liste triée et un nombre entier et renvoit l'élément ``el`` si celui-ci est dans la liste sinon ``None``. 

## Exercice 2 (Difficile)

Dans cet exercice, nous cherchons à écrire une fonction qui effectue la rotation d'une image de $90$ degrés en utilisant le principe "Diviser pour régner" :

![Image einstein](./../img/einstein_rotation.gif)

Pour manipuler une image en python, nous utiliserons le module PIL :

```python
from PIL import Image

# Nous chargeons l'image contenue dans le fichier image.png
image = Image.open("image.png")

# La méthode size permet d'obtenir les dimensions de l'image
largeur, hauteur = image.size

# La variable px représente le tableau des pixels de l'image
px = image.load()
```

Sa documentation est disponible [ici](https://pillow.readthedocs.io/en/stable/reference/Image.html)


La couleur du pixel situé aux coordonnées $x$ et $y$ est donnée par ``px[x, y]``. Une couleur est un triplet donnant les composantes rouge, vert et bleu sous la forme d'entiers entre 0 et 255.

Nous pouvons modifier la couleur d'un pixel avec l'affectation :

```python
c = (0, 255, 255)
px[x, y] = c
```

Nous supposons que notre image est carrée (téléchargeable [ici]()). L'idée est de couper l'image en 4 carrés, à effectuer la rotation de 90 degrés de chacun des quatres carrés, puis à les déplacer vers les positions finales :

![](./img/rotation_carre.PNG)

1. Exprimer, pour l'algorithme de rotation d'images, la méthode "Diviser pour régner" en décrivant les étapes :
   
   - Diviser :
   
   - Régner :
   
   - Combiner :

2. Afin de pouvoir procéder récursivement, on va définir une fonction ``rotation_aux( px : list, x : int, y :int, t :int)`` qui effectue la rotation de la portion carrée de l'image située aux coordonnées ``x``et ``y`` ( coin supérieur gauche du carré  ) jusqu'aux coordonnées ``x+t`` et ``y+t`` ( coin inférieur droit ). Cette fonction modifie le tableau ``px`` et ne renvoie rien. Ecrire la fonction ``rotation_aux``.

3. Ecrire une fonction ``rotation( px : list, taille : int )`` qui effectue une rotation de l'image toute entière, elle prend en paramètre le tableau des pixels et la dimension de celle-ci.
   
Une fois la rotation effectuée, on pourra sauvegarder le résultat dans un autre fichier avec l'instruction :
   
```python
image.save("rotation.png")
```

__________________

[Sommaire](./../../README.md)