# Exercices

## Exercice 1

a) Télécharger le fichier [mini_internet.fls](./../src/mini_internet.fls) et ouvrir le fichier.

b) Récupérer les adresses IP de M9 et M14, puis faire la commande ``ping`` afin de vérifier qu'elles sont bien connectées.

c) Exécuter la commande ``traceroute`` de M9 vers M14. Quels sont les routeurs traversés ?

d) Supprimer le câble reliant les routeurs E et F afin de simuler une panne. Puis réexécuter la commande ``traceroute`` de M9 vers M14. Que se passe t-il ?

e) Existe t-il encore un autre chemin ?

f) Remettre le câble reliant les routeurs E et F.

## Exercice 2

En utilisant le protocole RIP, faire la table de routage :

1. Du routeur H.

2. Du routeur F.

3. Du routeur D.

## Exercice 3

| Liaison | Type de liaison |
| :---: | :---: |
| Routeur A - Routeur H | Fast-Ethernet |
| Routeur A - Routeur B | Fast-Ethernet |
| Routeur B - Routeur D | Ethernet |
| Routeur D - Routeur C | Fibre | 
| Routeur D - Routeur E | Fibre |
| Routeur C - Routeur H | Fast-Ethernet |
| Routeur E - Routeur F | Ethernet |
| Routeur H - Routeur F | Ethernet |
| Routeur F - Routeur G | Fibre |

D'après les types de liaisons donées dans le tableau ci-dessus et en utilisant le protocole OSPF, faire la table de routage :

1. Du routeur H.

2. Du routeur F.

3. Du routeur D.

_______________

[Sommaire](./../../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 