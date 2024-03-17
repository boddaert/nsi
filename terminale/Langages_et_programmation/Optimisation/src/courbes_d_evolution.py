from math import *
import matplotlib.pyplot as plt

# Taille des données
n = 100

# Évolution du coût
liste_constant = [A COMPLETER for i in range(1,n)]
liste_logarithmique = [A COMPLETER for i in range(1,n)]
liste_lineaire = [A COMPLETER for i in range(1,n)]
liste_quadratique = [A COMPLETER for i in range(1,n)]
liste_exponentiel = [A COMPLETER for i in range(1,n)]

# Taille de l'axe des abcisses et de l'axe des ordonnées
plt.axis([0, 100, 0, 100])

# Liste des abcisses des courbes
liste_x = [x for x in range(1,n)]

# Traçage des courbes d'évoluation
plt.plot(liste_x, liste_constant, 'green', label="Coût constant")
plt.plot(liste_x, liste_logarithmique, 'violet', label="Coût logarithmique")
plt.plot(liste_x, liste_lineaire, 'blue', label="Coût linéaire")
plt.plot(liste_x, liste_quadratique, 'yellow', label="Coût quadratique")
plt.plot(liste_x, liste_exponentiel,'red', label="Coût exponentiel")

# Ajout des labels sur les courbes d'évolution
plt.legend()

# Affichage du graphique
plt.show()