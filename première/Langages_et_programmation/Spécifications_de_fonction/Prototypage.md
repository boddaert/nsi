# Spécification

## I. Définitions

> [!IMPORTANT]
> La *spécification* d'une fonction est la raison pour laquelle elle existe. En d'autres termes, la spécification d'une fonction répond aux questions suivantes :
>
> - Que fait cette fonction ?
>
> - Qu'à besoin cette fonction ?

> [!IMPORTANT]
> Une *documentation* est un texte compréhensible permetant de donner des informations à celui qui lit le code.

En Python, spécifier une fonction se fait à l'aide d'une documentation spéciale : la **DocString**.

## II. Écriture de DocString

La DocString s'écrit toujours après la signature d'une fonction entre triple guillemets (`"""`) et donne les informations suivantes :

- Les paramètres avec leur type.

- Le type de la valeur de renvoi.

- Une phrase en Français expliquant ce que fait la fonction.

- Eventuellement les contraintes d'utilisation.

> [!TIP]
> Par exemple :
>
>```python
> def max(l : list)->int:
>     """
>     :param l: (list) Une liste d'entiers
>     :return: (int) Un entier, élément de l
>     Renvoie l'entier le plus grand parmi tous les entiers de la liste l
>     :CU: La liste l doit contenir au moins un élément
>     """
>     elt_max = l[0]
>     for i in range(1, len(l)):
>         if l[i] > elt_max :
>             elt_max = l[i]
>     return elt_max
> ```

#### <ins>Application 1</ins>

a) Recopier les réponses des exercices $10$, $11$, $12$, $13$ et $14$ des listes (cf [Exercices sur les listes](./../Structures_de_données/Exercices/Exercices_listes.md)) dans un nouveau fichier Python.

b) Écrire la DocString pour chacune d'entre elles.

______________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 