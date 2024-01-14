# Activité : Comprendre la machine Enigma

Nature : Branchée

Matériel : Module `py-enigma`

Prérequis : Sécurisation des communications

## I. Objectif

L'objectif de cette activité est de comprendre comment la machine Enigma chiffrer les messages.

## II. Contexte

Nous sommes en 1938 et sous la montée du nazisme en Allemagne, Alan Turing, jeune mathématicien britannique est convoqué à la *Government Code and Sypher School* de Betchley Park afin de travailler sur une curieuse machine.

Inventée par l'Allemand Athur Scherbius, la machine Enigma électromecanique portable a servi au chiffrement et déchiffrement de l'intégralité des messages échangés par les Allemands nazis pendant la Seconde Guerre mondiale.

Cette machine pouvait concevoir une clé de chiffrement aléatoire à l'aide :

- De dix câblages possibles de lettres dans le tableau de connexions.

- De trois rotors (parmi cinq) et d'une position de départ.

- De câblages du réflecteur.

Le nombre de clés possibles s'élevant à $158 962 555 217 826 360 000$.

Et les Allemands concevaient une clé différente pour tous les jours.

Autrement dit, les Alliés avaient 24h pour espérer trouver la clé permettant de déchiffrer les messages envoyés le jour même.

Jusqu'à ce qu'Alan Turing créa une machine permettant de décrypter n'importe quel message en quelques minutes.

Vidéo Youtube (10 min) : [Enigma Machine  - Numberphile](https://www.youtube.com/watch?v=G2_Q9FoD-oQ)

## III. Installation

a) Installer la bibliothèque ``py-enigma`` permettant de simuler le fonctionnement d'une machine Enigma en Python.

Pour l'installer :

- Cliquer sur ``Outils`` puis ``Open System shell``

- Ecrire dans la console qui vient de s'afficher la commande ``pip install py-enigma``

b) Télécharger dans votre répertoire commun le fichier [enigma_machine.py](./src/enigma_machine.py)

## IV. Travail à faire

Pour configurer la position des rotors :

```python
>>> machine.set_display('PIX')
```

Pour afficher la position des rotors :

```python
>>> machine.get_display()
'PIX'
```

Pour chiffrer une lettre :

```python
>>> machine.key_press('A')
'I'
```

a) Quelle est maintenant la position des rotors ?

b) Quelle est maintenant la lettre chiffrée lorsque j'appuie sur ``'A'`` ?

Le déchiffrement se fait de la manière inverse (il faut que la position des rotors soit la même) :

```python
>>> machine.set_display('PIX')
>>> machine.key_press('I')
'A'
```

c) Ecrire une fonction ``chiffre_enigma(message_clair : str, machine : EnigmaMachine, pos_rotors : str)->str`` qui prend en paramètres un message clair, une machine Enigma configurée et la position des rotors. Cette fonction renvoie le message chiffré.

_______________

[Sommaire](./../README.md)