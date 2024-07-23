# Arbres binaires de recherche

## I. Définition de l'arbre binaire de recherche

> [!IMPORTANT]
> Un arbre binaire de recherche est soit :
>
> - Un arbre binaire vide.
>
> - Un arbre binaire vérifiant :
>
>     + Son sous-arbre gauche est un arbre binaire de recherche.
>
>     + Son sous-arbre droit est un arbre binaire de recherche.
>
>     + Tous les nœuds du sous-arbre gauche sont inférieurs à la valeur de la racine.
>
>     + Tous les nœuds du sous-arbre droit sont supérieurs à la valeur de la racine.

> [!TIP]
> Par exemple :
> ```mermaid
> flowchart TB
>     A((8))
>     B((5))
>     C((15))
>     D((2))
>     E((7))
>     F((12))
>     G((16))
>
>     H((" "))
>     I((" "))
>     J((" "))
>     K((" "))
>     L((" "))
>     M((" "))
>     N((" "))
>     O((" "))
>
>     A --> B
>     A --> C
>     B --> D
>     B --> E
>     C --> F
>     C --> G
>     D --> H
>     D --> I
>     E --> J
>     E --> K
>     F --> L
>     F --> M
>     G --> N
>     G --> O
> ```
>
> Sur chacun des sous-arbres de l'arbre ci-dessus, tous les nœuds du sous-arbre gauche sont inférieurs à la valeur de la racine et tous les nœuds du sous-arbre droit sont supérieurs à la valeur de la racine.

#### <ins>Application 1</ins>

a) Où se trouve l'élément le plus grand dans un ABR ?

b) Où se trouve l'élément le plus petit dans un ABR ?

## II. Recherche d'élément 

### a) Algorithme

L'algorithme de recherche d'élément consiste à renvoyer $VRAI$ si l'élément est présent, $FAUX$ sinon.

> [!WARNING]
> L'algorithme de recherche d'élément dans un arbre binaire de recherche se voit modifié par rapport à l'algorithme de recherche dans un arbre binaire quelconque.
>
> En effet, si nous considérons les propriétés de l'ABR, nous pouvons accélérer le processus de recherche.


```algo
Algorithme : recherche_abr(abr, elt)
Entrées : arb un arbre binaire de recherche, elt un entier
Sorties : Vrai si elt est présent dans abr, Faux sinon.

Si abr est vide, alors :
    Renvoie Faux
Sinon si la racine de abr est égal à elt, alors :
    Renvoie Vrai
Sinon :
    Si elt < à la racine de abr, alors :
        Renvoie recherche_abr(abr.sag(), elt)
    Sinon :
        Renvoie recherche_abr(abr.sad(), elt)
```

#### <ins>Application 2</ins>

Écrire une fonction `recherche_abr(abr : AB, elt : int)->bool` qui prend en paramètre un arbre binaire de recherche et un entier et renvoie `True` si `elt` est présent, `False` sinon.

### b) Efficacité

*Rappel : [Complexité](./../../../première/Algorithmique/Optimisation/Complexité.md).*

#### Coût algorithmique de la recherche dans un arbre binaire de recherche équilibré

> [!IMPORTANT]
> Un arbre *équilibré* est un arbre qui maintient une profondeur de nœud minimum. Un arbre complet est équilibré, un peigne ou un arbre filiforme ne l'est pas. 

Dans un arbre binaire de recherche équilibré, le coût algorithmique de recherche d'un élément est **logarithmique** $O(\log_2 n)$ avec $n$ le nombre de nœuds, ce qui est bien moins coûteux que la recherche séquentielle.

#### <ins>Application 3</ins>

a) Exécuter à la main l'algorithme de recherche classique sur l'arbre donné en début de leçon pour l'élément $12$ en comptant le nombre de comparaisons effectué.

b) Exécuter à la main l'algorithme de recherche dans un ABR dans le même arbre pour l'élément $12$ en comptant le nombre de comparaisons effectué.

c) Comparer les résultats trouvés aux questions a) et b).

_________________

[Exercices](./Exercices/Exercices_arbres_binaires_de_recherche.md)

_________________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 