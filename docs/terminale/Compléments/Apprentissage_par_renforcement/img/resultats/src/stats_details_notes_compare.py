import numpy as np
import matplotlib.pyplot as plt
import sys

y1 = [0,0,0,1,3,5,6,8,3,1,0,0]
y2 = [0,0,0,0,0,1,0,1,2,2,12,9]

notes = [str(i*20/11)[:4] for i in range(12)]

barWidth = 0.4

r1 = range(len(y1))
r2 = [x + barWidth for x in r1]

plt.bar(r1, y1, width = barWidth)
plt.bar(r2, y2, width = barWidth, color = 'red')
plt.xticks([r + barWidth / 2 for r in range(len(y1))], notes)

plt.title("Fréquence sur Notes1 et Notes2")
plt.ylabel("Nombre d'élèves")
plt.xlabel("Note obtenue")

plt.savefig("./../diag_barre_notes_compare")