# Exercices

## Exercice 1

Dans cet exercice, nous allons manipuler l'interface en ligne de commande. Pour cela, il faut ouvrir l'application Windows **Invite de commandes**.

Exécuter la commande ``ipconfig`` et répondre aux questions suivantes :

a) Donner l'adresse MAC de votre machine.

b) Donner l'adresse IP (IPv4) de votre machine.

c) Donner le masque de sous-réseau et vérifier qu'il s'agit d'un masque valide.

d) Donner l'adresse réseau du lycée.

e) Combien de machines ce réseau peut-il contenir ?

f) Quelle est sa plage d'adresse possible ? (Première adresse à dernière adresse IP)

---------

Pour la suite des exercices, nous utiliserons le logiciel libre et gratuit : Filius.

Filius permet de construire et simuler un réseau. Une fois lancé, nous disposons de plusieurs modes :

- *Mode construction* : permet d'ajouter des composants réseaux, de les paramétrer et de les relier entre eux.

- *Mode simulation* : permet de lancer une simulation et de voir les paquets circuler dans le réseau.

En mode construction, nous pouvons sélectionner un composant réseau et le faire glisser dans la zone de dessin.

Pour relier deux éléments , nous cliquons sur l'icône du câble, puis sur chacun des deux éléments à relier.

## Exercice 2

<img src="./../img/exo2.PNG" width=500>

a) En mode construction, reproduire le réseau de la figure ci-dessus dans un fichier nommé ``reseau_ex2.fls``.

b) Avec un masque de sous-réseau de ``255.255.0.0`` et en supposant l'adresse réseau ``192.168.0.0``. Écrire deux adresses IP valides appartenenant à ce réseau.

c) En cliquant sur ``configurer``, attribuer les adresses IP données à la question précédente aux deux ordinateurs du réseau. (Attention à modifier également le masque de sous-réseau.)

La commande ``ping`` permet d’envoyer un paquet IP "vide" vers une adresse IP. Si la
machine de destinatation reçoit ce paquet, elle répond avec un autre paquet IP comme accusé de réception. Cette commande permet de vérifier si deux machines peuvent communiquer entre-elles.

e) Passer en mode simulation. Cliquer sur l'un des deux ordinateurs, puis sur **Installation de logiciels** et installer le logiciel **Ligne de commande**.

Sur ce logiciel, exécuter la commande ``ping`` suivie de l'adresse IP du second ordinateur. Les deux machines sont-elles connectées ?

f) A quoi correspond le temps affiché à côté de chaque accusé de réception ?

## Exercice 3

<img src="./../img/exo3.PNG" width=700>

a) En mode construction, reproduire le réseau de la figure ci-dessus dans un fichier nommé `reseau_ex3.fls`.

Les machines M1 et M2 ont respectivement les adresses IP ``192.168.10.1`` et ``192.168.30.5``.

Le serveur possède l'adresse IP ``8.8.8.1``.

b) Donner l'adresse réseau du réseau A et B.

c) Il faut désormais relier ces deux réseaux, pour cela configurer le routeur :

- L'adresse IP du routeur du port relié au réseau A est ``192.168.0.1``.

- L'adresse IP du routeur du port relié au réseau B est ``8.8.8.254``.

Attention à également modifier le masque de sous-réseau si cela est nécessaire.

d) Depuis M1, lancer un ``ping`` vers le serveur. Que se passe t-il ? Les machines sont-elles connectées ?

L'erreur survient du fait qu'il manque une information à M1, il ne sait pas où envoyer le paquet. La passerelle est l'interface qui permet aux paquets de sortir du réseau.

e) Dans la configuration de M1, ajouter dans Passerelle l'adresse IP du routeur relié au réseau A.

f) Dans la configuration du serveur, ajouter dans Passerelle l'adresse IP du routeur relié au réseau B.

g) Refaire la commande ``ping`` vers le serveur depuis M1. Les machines sont-elles connectées ?

La commande `traceroute`permet de visualiser quels équipements le paquet traverse.

h) Depuis M1, effectuer la commande ``traceroute`` suivie de l'adresse IP du serveur. A quoi correspondent les adresses affichées ?

On décide de faire héberger sur le serveur une page Web.

i) Pour cela, installer sur le serveur le logiciel **Serveur web** et sur M1 le logiciel **Navigateur web**.

S'assurer que le serveur web est bien démarré, puis faire clic droit sur M1 et choisir **Afficher les échanges de données**.

Enfin, sur M1, ouvrir le navigateur et à la suite de ``https://`` : écrire l'adresse IP du serveur.

j) En visualisant les échanges effectués entre le navigateur et le serveur web, donner en précisant les couches, les protocoles utilisés.

________________

[Sommaire](./../../README.md)

___________

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/boddaert/nsi">Cours NSI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/boddaert">Théo Boddaert</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="">  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></p> 
