# Exercices

## Exercice 1

L'algorithme de recherche par dichotomie est un algorithme utilisant le principe de "Diviser pour régner".

a) Rappeler les étapes de l'algorithme de recherche dichotomique (via un schéma).

b) Décrire les étapes "Diviser", "Régner" et "Combiner" de l'algorithme de recherche dichotomique.

c) Écrire une fonction récursive ``recherche_dichotomique_recursive(l : list, elt : int)->int`` prenant en paramètre une liste triée d'entiers et un entier et renvoit l'élément ``elt`` si celui-ci est dans la liste sinon ``None``.

## Exercice 2 (Difficile)

Dans cet exercice, nous cherchons à écrire une fonction qui effectue la rotation d'une image de $90$ degrés en utilisant le principe "Diviser pour régner" :

<img src="./../img/einstein_rotation.gif" width=600>

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

Sa documentation est disponible [ici](https://pillow.readthedocs.io/en/stable/reference/Image.html).


La couleur du pixel situé aux coordonnées $x$ et $y$ est donnée par ``px[x, y]``. Une couleur est un triplet donnant les composantes rouge, vert et bleu sous la forme d'entiers entre 0 et 255.

Nous pouvons modifier la couleur d'un pixel avec l'affectation :

```python
c = (0, 255, 255)
px[x, y] = c
```

Nous supposons que notre image est carrée. L'idée est de couper l'image en quatre carrés, à effectuer la rotation de $90$ degrés de chacun des quatres carrés, puis à les déplacer vers les positions finales :

<img src="./../img/rotation_carre.PNG" width=500>

a) Exprimer, pour l'algorithme de rotation d'images, la méthode "Diviser pour régner" en décrivant les étapes :
   
   - Diviser :
   
   - Régner :
   
   - Combiner :

b) Afin de pouvoir procéder récursivement, on va définir une fonction ``rotation_aux( px : list, x : int, y :int, t :int)`` qui effectue la rotation de la portion carrée de l'image située aux coordonnées ``x``et ``y`` ( coin supérieur gauche du carré  ) jusqu'aux coordonnées ``x+t`` et ``y+t`` ( coin inférieur droit ). Cette fonction modifie le tableau ``px`` et ne renvoie rien. Ecrire la fonction ``rotation_aux``.

c) Écrire une fonction ``rotation( px : list, taille : int )`` qui effectue une rotation de l'image toute entière, elle prend en paramètre le tableau des pixels et la dimension de celle-ci.
   
Une fois la rotation effectuée, on pourra sauvegarder le résultat dans un autre fichier avec l'instruction :
   
```python
image.save("rotation.png")
```

__________________

[Sommaire](./../../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 