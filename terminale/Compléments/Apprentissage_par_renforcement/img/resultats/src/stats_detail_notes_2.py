import numpy as np
import matplotlib.pyplot as plt
import sys

y1 = [0,0,0,0,0,1,0,1,2,2,12,9]

names = [str(i*20/11)[:4] for i in range(12)]

plt.bar(names, y1, color = 'red')
plt.title("Fréquence de Notes2")
plt.ylabel("Nombre d'élèves")
plt.xlabel("Note obtenue")
plt.savefig("./../diag_barre_notes_2")