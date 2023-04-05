# Chaînes de caractères

Une chaîne de caractère en python s'écrit sous la forme ``'.....'`` ou ``"....."`` 

Les chaînes de caractères présentent une certaine ressemblance avec les listes en python. On peut en effet connaître la taille d'une chaîne avec la fonction ``len(chaine)`` ou accéder au *i-ème* caractere de la chaîne  grâce à l'instruction ``chaine[i]`` . Il faut néanmoins noter quelques différences.

## I. Typage et Parcours

#### I.1 Typage

En python, les listes sont des objets de type ``list`` , ce sont des structures de données linéaires. 
Les chaînes de caractères sont des objets de type ``str`` :

```python
>>> type("bonjour")
<class 'str'>
```

#### I.2 Mutabilité

En revanche, contrairement aux listes, les chaînes de caractères ne sont pas mutables, c'est-à-dire qu'on ne peut pas les modifier :

```python
>>> chaine = "bonjour"
>>> chaine[3] = "c"
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

#### I.3 Accès au *i-ème* caractère

La syntaxe permettant d'accéder au *i-ème* caractère fonctionne exactement de la même façon qu'avec les listes :

```python
>>> chaine = "bonjour"
>>> chaine[5]
'u'
```

#### I.4 Parcours de chaîne de caractère

Les parcours de chaînes de caractères, de même que l'accès au *i-ème* élément, s'écrivent de la même manière que les parcours de listes. Nous pouvons donc parcourir tous les caractères d'une chaîne avec une boucle ``for`` ou ``while``. 
Exemple de parcours par valeur avec ``for`` :

```python
chaine = "bonjour"
for caractere in chaine:
    print(caractere)

b
o
n
j
o
u
r
```

#### I.5 Applications

**Application 1**

Considérons la chaîne de carcatère ``chaine = 'timoleon'``:

Ecrire les instructions en python permettant d'afficher :

- La longueur de ``chaine``
- Le premier et le dernier caractère de ``chaine``
- Tous les caractères de cette chaîne, ligne par ligne, en effectuant un parcours par valeur 
- Tous les caractères de cette chaîne, ligne par ligne, en effectuant un parcours par indice

Quel est l'avantage de réaliser un parcours par indice ?

**Application 2**

Ecrire un script permettant d'obtenir la liste des indices où se situe une lettre donnée dans la chaîne. 
Par exemple :

```python
chaine = "N'allez pas dans les hautes herbes !"
lettre = 'e'
```

Après exécution, la console doit afficher :

```python
[5, 18, 25, 29, 32]
```

**Application 3**

Ecrire un script permettant d'afficher le nombre de fois qu'apparaît une lettre donnée dans la chaîne. Par exemple :

```python
chaine = "j'adore la nsi"
lettre = 'a'
```

Après exécution, la console doit afficher :

```python
2
```

## II. Concaténation

**Syntaxe**

Pour concaténer deux chaînes de caractères, c'est-à-dire relier les chaînes entre elles, nous utilisons l'opérateur ``+`` :

```python
>>> chaine1 = "Salut a tous, "
>>> chaine2 = "c est Fanta !"
>>> chaine1 + chaine2
'Salut a tous, c est Fanta !'
```

**Application 4**

Ecrire un script permettant d'ajouter entre chaque caractère d'une chaîne donnée une étoile ``*`` . Par exemple :

```python
chaine = "La guerre des etoiles"
```

Après exécution, la console doit afficher :

```python
L*a* *g*u*e*r*r*e* *d*e*s* *e*t*o*i*l*e*s*
```

**Application 5**

```python
>>> chaine = "ca ne marche pas"
>>> chaine + 2
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

- Expliquez pourquoi la console affiche cette erreur.
- Comment faire pour que la concaténation fonctionne ? 

## III. Slicing (hors programme)

Le slicing permet d'obtenir une *sous-liste* depuis une *liste*. Le slicing fonctionne pour les listes comme pour les chaînes de caractères.

#### III.1 Syntaxe :

``liste[debut:fin:pas]``  où :

- ``debut`` est l'indice du premier élément à sélectionner 
- ``fin`` est l'indice du dernier élément ( exclu ) à sélectionner
- ``pas`` le pas, à 1 par défaut

```python
>>> chaine = "j'adore la nsi"
>>> chaine[4:8]
'ore '
```

**Application 6**

Ecrire un script qui, à partir d'une chaîne, affiche cette chaîne en la réduisant, ligne après ligne, d'un carcatère à gauche et d'un caractère à droite.
Par exemple :

```python
chaine = "Vous savez, moi je ne crois pas qu il y ait de bonne ou de mauvaise situation."
```

Après exécution, la console m'affiche :

```python
ous savez, moi je ne crois pas qu il y ait de bonne ou de mauvaise situation
us savez, moi je ne crois pas qu il y ait de bonne ou de mauvaise situatio
s savez, moi je ne crois pas qu il y ait de bonne ou de mauvaise situati
 savez, moi je ne crois pas qu il y ait de bonne ou de mauvaise situat
savez, moi je ne crois pas qu il y ait de bonne ou de mauvaise situa
avez, moi je ne crois pas qu il y ait de bonne ou de mauvaise situ
vez, moi je ne crois pas qu il y ait de bonne ou de mauvaise sit
ez, moi je ne crois pas qu il y ait de bonne ou de mauvaise si
z, moi je ne crois pas qu il y ait de bonne ou de mauvaise s
, moi je ne crois pas qu il y ait de bonne ou de mauvaise 
 moi je ne crois pas qu il y ait de bonne ou de mauvaise
moi je ne crois pas qu il y ait de bonne ou de mauvais
oi je ne crois pas qu il y ait de bonne ou de mauvai
i je ne crois pas qu il y ait de bonne ou de mauva
 je ne crois pas qu il y ait de bonne ou de mauv
je ne crois pas qu il y ait de bonne ou de mau
e ne crois pas qu il y ait de bonne ou de ma
 ne crois pas qu il y ait de bonne ou de m
ne crois pas qu il y ait de bonne ou de 
e crois pas qu il y ait de bonne ou de
 crois pas qu il y ait de bonne ou d
crois pas qu il y ait de bonne ou 
rois pas qu il y ait de bonne ou
ois pas qu il y ait de bonne o
is pas qu il y ait de bonne 
s pas qu il y ait de bonne
 pas qu il y ait de bonn
pas qu il y ait de bon
as qu il y ait de bo
s qu il y ait de b
 qu il y ait de 
qu il y ait de
u il y ait d
 il y ait 
il y ait
l y ai
 y a
y 
```

#### III.2 Test d'appartenance

Le test d'appartenance permet de savoir si une sous-chaîne est comprise dans une chaîne. Par exemple, la sous-chaîne ``'ors on at'`` est comprise dans la chaîne ``'Et alors on attend pas patrick ?'``. En python, nous utilisons le mot-clé ``in`` :

```python
>>> chaine = "Et alors on attend pas patrick ?"
>>> chaine_test = "ors on at"
>>> chaine_test in chaine
True
```

On remarque que l'instruction du test d'appartenance grâce au mot-clé ``in`` donne comme résultat un booléen.

**Application 7**

Ecrire un script permettant de vérifier si un mot de passe entré par l'utilisateur contient le caractère ``*``.

```python
mot de passe = "abcd*efg"
```

Après l'exécution, la console doit afficher :

```python
True
```

## IV. Majuscules et Minuscules

Il est possible de mettre en majuscule un caractère minuscule et de mettre en minuscule un caractère majuscule :

```python
>>> lettre_minuscule = "u"
>>> lettre_minuscule.upper()
'U'
>>> lettre_majuscule = "U"
>>> lettre_majuscule.lower()
'u'
```

Pour savoir si le caractère en question est majuscule ou minuscule, nous pouvons nous aider des méthodes ``islower()`` et ``isupper()``. Ces méthodes renvoient des booléens :

```python
>>> lettre_minuscule = "u"
>>> lettre_minuscule.isupper()
False
>>> lettre_minuscule.islower()
True
```

**Application 8**

Ecrire un script permettant de mettre tous les caractères d'une chaîne en majuscule. Par exemple :

```python
chaine = "ce texte est en minuscule"
```

Après exécution, la console doit afficher :

```python
'CE TEXTE EST EN MINUSCULE'
```

**Application 9**

Ecrire un script prenant une chaîne de caractère permettant de changer la casse. Ce script doit mettre les minuscules en majuscules et les majuscules en minuscules :

```python
chaine = "Que Ce Jour Reste A Grave Dans Vos Memoires Comme Celui Ou Vous Avez Failli Capturer Le Capitaine Jack Sparrow"
```

Après exécution, la console doit afficher :

```python
'qUE cE jOUR rESTE a gRAVE dANS vOS mEMOIRES cOMME cELUI oU vOUS aVEZ fAILLI cAPTURER lE cAPITAINE jACK sPARROW'
```

### Exercice : Joyeux Noël !

Ecrire un  script python permettant d'afficher un sapin de Noël avec des décorations aléatoires.

Les caractères utilisés pour les décorations seront stockés dans une liste créée en début de script.

Par exemple, la console doit afficher :

```python
           *            
          X**           
         *****          
        *******         
       *******II        
      I**@*******       
     ********I****     
    *******I*******    
   *****************   
  **@*****I****@**@**  
 ***********X*I*****I* 
**I****X***X***@******@
          ***          
          ***          
          ***          
```

ou 

```python
           *            
          ***           
         **X*I          
        *******         
       *****@*@*        
      **X****@***       
     *************     
    ****X*I********    
   ***********X*****   
  ***@***I*I*****X***  
 ********X****@****X** 
***@**I****I**X**I*****
          ***          
          ***          
          ***          
```
