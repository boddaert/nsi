import numpy as np
import matplotlib.pyplot as plt
import sys

y1 = [0,0,0,1,3,5,6,8,3,1,0,0]

names = [str(i*20/11)[:4] for i in range(12)]

plt.bar(names, y1)
plt.title("Fréquence de Notes1")
plt.ylabel("Nombre d'élèves")
plt.xlabel("Note obtenue")
plt.savefig("./../diag_barre_notes_1")

