# Projet : Combat de Pokémons

![image](./img/combat_de_pokemon.gif)

## I. Description

Nous souhaitons écrire un programme simulant le combat entre deux Pokémons.

Pour ce faire, nous utiliserons la programmation orientée objet.

## II. Règles d'un combat de Pokémons

Deux Pokémons se battent en duel jusqu'à ce que l'un des deux soit mis KO, c'est-à-dire, avec les points de vie inférieur ou égal à zéro.

Au tour par tour, chacun des deux Pokémons vont choisir aléatoirement une action parmi quatre :

- Augmenter ses points d'attaque.

- Augmenter ses points de vie.

- Augmenter ses points de vitesse.

- Attaquer le pokémon adverse.

Le Pokémon le plus rapide, celui qui a le plus de point de vitesse, joue en premier.

Le nombre de dégât reçus est calculé de la manière suivante : 

Nombre de point d'attaque (Pokémon attaquant) - Nombre de point de défense (Pokémon attaqué)

## III. Cahier des charges

a) Classe Pokémon

- Pokémon est une classe dont les attributs sont :

    + Un nom donné en paramètre du constructeur.

    + Un nombre de point de vie initialisé par défaut aléatoirement entre $800$ et $1000$.

    + Un nombre de point d'attaque initialisé par défaut aléatoirement entre $100$ et $200$.

    + Un nombre de point de défense initialisé par défaut aléatoirement entre $100$ et $200$.

    + Un nombre de point de vitesse initialisé par défaut aléatoirement entre $100$ et $200$.

    + Un booléen indiquant si le pokémon est KO ou non. Initialisé par défaut à `False`.

- Et dont les méthodes sont :

    + Tous les accesseurs des attributs précédents.

    + Une méthode `set_point_de_vie(new_point_de_vie : int)` qui prend en paramètre un entier et fixe les points de vie de l'objet à cet entier.

    + Une méthode `set_ko()` mettant à `True` l'attribut `KO` si le pokémon possède des points de vie inférieur ou égal à zéro.

    + Une méthode `affiche_statistiques()` qui affiche toutes les caractérisitiques du pokémon.

- L'objet Pokémon dispose également de quatre actions disponibles pendant son tour de jeu :

    + Une méthode `augmente_attaque(bonus : int)` qui prend en paramètre un entier et ajoute le montant de l'argument aux points d'attaque de l'objet.

    + Une méthode `augmente_point_de_vie(bonus : int)` qui prend en paramètres un entier et ajoute le montant de l'argument aux points de vie de l'objet.

    + Une méthode `augmente_vitesse(bonus : int)` qui prend en paramètre un entier et ajoute le montant de l'argument aux points de vitesse de l'objet.

    + Une méthode `attaque(pokemon_adverse : Pokemon)->int` qui prend en paramètre un second objet Pokémon et renvoie le montant des dégâts que le pokémon passé en paramètre doit recevoir.

b) Programme principal

Le programme principal est découpé en plusieurs fonctions :

- Une fonction `joue_en_premier(pokemon_1 : Pokemon, pokemon_2 : Pokemon)->tuple` qui prend en paramètres deux objets Pokémon et renvoie un tuple de deux objets Pokémon dont le premier élément est le Pokémon le plus rapide.

- Une fonction `choix_action(pokemon_1 : Pokemon, pokemon_2 : Pokemon)->None` qui prend en paramètres deux objets Pokemon et effectue une action aléatoire de `pokemon_1`.

- Une fonction `combat(pokemon_1 : Pokemon, pokemon_2 : Pokemon)->None` qui prend en paramètres deux objets Pokemon et simule un combat entre ces deux Pokémons.

## IV. Affichage

Le programme doit afficher :

- Au début du combat les caractéristiques de chaque Pokémon.
- Les actions utilisées.
- Le gagnant du combat.

Par exemple :

```
Nom : Tiplouf
Points de vie : 825
Attaque : 180
Défense : 117
Vitesse : 188


Nom : Canarticho
Points de vie : 871
Attaque : 117
Défense : 180
Vitesse : 168


Tour numéro n°1
Tiplouf est plus rapide !
Tiplouf augmente sa vitesse à 208.
Canarticho se soigne : PV = 891.


PV de Tiplouf : 825
PV de Canarticho : 891


Tour numéro n°2
Tiplouf est plus rapide !
Tiplouf augmente son attaque à 200.
Canarticho augmente sa vitesse à 188.


PV de Tiplouf : 825
PV de Canarticho : 891

[...]

Tour numéro n°31
Canarticho est plus rapide !
Canarticho augmente son attaque à 237.
Tiplouf attaque Canarticho en faisant 240 dégats.


PV de Canarticho : -49
PV de Tiplouf : 385


Canarticho est KO !
Tiplouf remporte le combat !
```

## V. Evaluation

Vous serez évalués sur :

- La qualité du code fourni (lisibilité du code, explicité des noms).

- Le respect du cahier des charges.

- La propreté de l'affichage.

________

[Sommaire](./../README.md)