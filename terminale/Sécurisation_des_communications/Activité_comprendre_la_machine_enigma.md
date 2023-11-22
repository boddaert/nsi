# Activité : Comprendre la machine Enigma

### Exercice 9 Enigma

Nous allons, dans cet exercice, nous intéresser à la machine Enigma.

Inventée par l'Allemand Athur Scherbius, cette machine électromecanique portable a servi au chiffrement et déchiffrement de l'intégralité des messages échangés par les Allemands nazis pendant la Seconde Guerre mondiale.

a) Pour plus de détails, regarder la vidéo [Enigma Machine - Numberphile](https://www.youtube.com/watch?v=G2_Q9FoD-oQ)

Une clé est constituée :

- des 10 câblages possibles de lettres dans le tableau de connexions.

- de 3 rotors (parmi 5) et de leur position de départ.

- des câblages du réflecteur.

Il y a 158 962 555 217 826 360 000 clés possibles. Et les Allemands avaient une clé différente pour chaque jour. Autrement dit, les Alliés avaient 24h pour espérer trouver la clé permettant de déchiffrer les messages du jour.

Jusqu'à ce qu'Alan Turing créa sa machine.

b) La bibliothèque ``py-enigma`` permet de simuler le fonctionnement d'une machine Enigma en Python.

Pour l'installer :

- Cliquer sur ``Outils`` puis ``Open System shell``

- Ecrire dans la console qui vient de s'afficher la commande ``pip install py-enigma``

c) Télécharger dans votre répertoire commun le fichier [enigma_machine.py](./src/enigma_machine.py)

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

d) Quelle est maintenant la position des rotors ?

e) Quelle est maintenant la lettre chiffrée lorsque j'appuie sur ``'A'`` ?

Le déchiffrement se fait de la manière inverse (il faut que la position des rotors soit la même) :

```python
>>> machine.set_display('PIX')
>>> machine.key_press('I')
'A'
```

f) Ecrire une fonction ``chiffre_enigma(message_clair : str, machine : EnigmaMachine, pos_rotors : str)->str`` qui prend en paramètres un message clair, une machine Enigma configurée et la position des rotors. Cette fonction renvoie le message chiffré.

g) Ecrire une fonction ``dechiffre_enigma(message_chiffre : str, machine : EnigmaMachine, pos_rotors : str)->str`` qui prend en paramètres un message chiffré, une machine Enigma configurée et la position des rotors. Cette fonction renvoie le message clair.