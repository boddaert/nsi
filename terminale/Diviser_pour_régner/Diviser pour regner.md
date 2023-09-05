# Diviser pour régner

## I. Principe

Le principe "diviser pour régner" consiste à :

1. **Diviser** : décomposer un problème en un ou plusieurs sous-problèmes de même nature mais plus petits

2. **Regner** : résoudre ces sous-problèmes, éventuellement en les décomposant à leur tour récursivement en problèmes plus petits encore 

3. **Combiner** : déduire, par les solutions des sous-problèmes, la solution du problème initial

<img src="https://images-schoolmouv-cours.s3.eu-west-1.amazonaws.com/t-fnx-nsi-c18-img01.png" title="" alt="Diviser pour régner : Fiche de cours - Numérique et sciences informatiques  | SchoolMouv" data-align="center">

## 

## II. Exemple

Alice se décide à ranger ses bandes déssinées par ordre alphabétique de titre. Le travail est fastidieux car elle en possède une bonne centaine. Elle appelle son frère Basile à la rescousse. Ils se partagent les bande déssinées ( Etape 1 : **Diviser** ) et chacun d'eux trie sa moitié, sous la forme d'une pile de BD ( Etape 2 : **Régner** ). 

Ensuite, les bandes déssinées sont rangées dans la bibliothèque en fusionnant les deux piles, c'est-à-dire en prenant à chaques fois celle des deux BD au sommet des deux piles qui vient avant l'autre dans l'ordre alphabétique (Etape 3 : **Combiner** )

# 

# Tri Fusion

Le tri fusion, comme le tri par sélection ou insertion est un algorithme de tri. Il permet de trier les éléments d'une liste. 

## I. Principe

Le tri fusion est un tri utilisant le principe "Diviser pour régner".

Il consiste à séparer les éléments de la liste en deux listes de même taille, à un élément près. Répéter jusqu'à obtenir des listes à au plus 1 élément.

Ensuite, on trie chacune des sous-listes obtenues récursivement. Enfin, on fusionne les listes triées, ce qui est facile car il suffit d'examiner le premier élément de chaque liste :

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Merge-sort-example-300px.gif/260px-Merge-sort-example-300px.gif" title="" alt="Merge-sort-example-300px.gif" data-align="center">

## II. Algortihme du Tri Fusion

```
Algortihme de Tri :

Dans le cas où la longueur de la liste est supérieure à 2 :

- Découper la liste en deux sous listes

- Appliquer l'algorithme de tri à chaque sous-liste

- Fusionner les deux sous-listes triées

- Renvoyer la liste fusionnée (qui est maintenant triée)

Dans le cas où la liste a 1 seul élément :

- Renvoyer directement cette liste ( car elle est implicitement triée )
```

## III. Exemple

On peut, pour simplifier, schématiser l'application du tri fusion sur une liste sous forme d'arbre.

Avec la liste ``[23, 12, 4, 56, 35, 32, 42, 57, 3]``, cela donnerait :

# 

![](https://pixees.fr/informatiquelycee/n_site/img/nsi_term_algo_div_1.png)

## IV. Rappel Slicing

Le slicing permet d'obtenir une *sous-liste* depuis une *liste*. Le slicing fonctionne pour les listes comme pour les chaînes de caractères ou encore les tuples.

#### IV.1 Syntaxe :

`liste[debut:fin:pas]` où :

- `debut` est l'indice du premier élément à sélectionner
- `fin` est l'indice du dernier élément ( exclu ) à sélectionner
- `pas` le pas, à 1 par défaut

```python
>>> liste = [0, 1, 2, 3, 4, 5, 6]
>>> liste[2:5]
[2, 3, 4]
```

# Applications

### Application 1

Dessiner l'arbre correspondant à l'application du tri fusion sur la liste : ``l = [8, 2, 4, 9, 3, 1, 5, 7, 6]``

Sur l'arbre, écrire pour chaque étape s'il s'agit d'une étape **Diviser**, **Régner** ou **Combiner**.

# 

Nous allons maintenant essayer de programmer en python le tri fusion. Chacune des étapes **Diviser**, **Régner** et **Combiner** peut être codée par une fonction.

La fonction ``decoupe`` représente l'étape **Diviser**.

La fonction ``fusion`` représente l'étape **Régner**.

La fonction ``tri_fusion`` représente l'étape **Combiner**.

### Application 2 : Fonction Découpe

La fonction `decoupe` prend en paramètre une liste et renvoit deux listes. La fonction `decoupe` sépare une liste en deux listes ayant le même nombre d'éléments, à un près.

1. Quelles sont les deux listes renvoyées par la fonction ``decoupe`` lorsqu'on lui passe en paramètre la liste ``[5, 1, 3, 4, 2]`` ?

2. Ecrire en python, la fonction ``decoupe( l : list ) -> ( list , list )``.

3. Tester sa fonction ``decoupe`` à l'aide de la fonction ``verif_decoupe`` donnée dans le fichier [tester.py](tester.py). ( Lire sa DocString pour comprendre comment elle fonctionne )

### Application 3 : Fonction Fusion

La fonction `fusion` prend en paramètre deux listes triées et renvoit une liste triée, fusion des listes passées en paramètre.

1. Quelle liste est renvoyée par la fonction ``fusion`` lorsqu'on lui passe en paramètres les listes ``[3, 5, 8]`` et ``[2, 4, 9]`` ?

2. Ecrire en python, la fonction ``fusion( l1 : list , l2 : list ) ->  list ``.

       On pourra écrire cette fonction de manière récursive ou à l'aide d'une boucle ``while``.

3. Tester sa fonction ``fusion`` à l'aide de la fonction ``verif_fusion`` donnée dans le fichier [tester.py](tester.py). ( Lire sa DocString pour comprendre comment elle fonctionne )

### Application 4 : Fonction Tri Fusion

1. La fonction ``tri_fusion`` est récursive. Quelle est la condition d'arrêt à cette fonction ?

2. Ecrire en python, une fonction `tri_fusion( l : list ) -> list` prenant en paramètre une liste et renvoyant la liste triée en utilisant le principe du tri fusion.

# 

### Exercice 1 : Recherche dichotomique

L'algorithme de recherche par dichotomie est un algorithme utilisant le principe de "Diviser pour régner".

1. Rappeler les étapes de l'algortihme de recherche par dichotomie ( via un schéma ).

2. Ecrire une fonction ``recherche_dichotomie_recursive( l : list, el : int ) -> int`` prenant en paramètre une liste ``l`` triée et ``el`` un nombre entier et renvoit l'élément ``el`` si celui-ci est dans la liste sinon ``None``. 

        La fonction ``recherche_dichotomie_recursive``devra utiliser la récursivité.

# 

# Pour aller plus loin ..

### Exercice 2 : Rotation d'image

Dans cet exercice, on cherche à écrire une fonction qui effectue la rotation d'une image de 90 degrés en utilisant le principe "Diviser pour régner" :

<img src="./img/einstein_rotation.gif" title="" alt="" data-align="center">

Pour manipuler une image en python, on pourra utiliser le module PIL :

```python
from PIL import Image
image = Image.open("image.png")
largeur, hauteur = image.size
px = image.load()
```

On charge l'image contenue dans le fichier ``image.png``, on obtient ses dimensions dans les variables ``largeur``et ``hauteur``, et la variable ``px`` représente le tableau des pixels constituant l'image. 

La couleur du pixel situé aux coordonnées $x$ et $y$ est donnée par ``px[x, y]``. Une couleur est un triplet donnant les composantes rouge, vert et bleu sous la forme d'entiers entre 0 et 255.

On peut modifier la couleur d'un pixel avec l'affectation :

```python
c = (0, 255, 255)
px[x, y] = c
```

On suppose que notre image est carrée. L'idée est de couper l'image en 4 carrés, à effectuer la rotation de 90 degrés de chacun des quatres carrés, puis à les déplacer vers les positions finales :

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
