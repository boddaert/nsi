from math import sqrt
import numpy as np
import scipy.stats as stat
ALPHA = 0.05

# génére deux échantillons indépendants
notes_classe1 = [9.090909091,7.272727273,14.54545455,9.090909091,12.72727273,10.90909091,9.090909091,12.72727273,12.72727273,14.54545455,10.90909091,14.54545455,12.72727273,12.72727273,10.90909091,10.90909091,12.72727273,10.90909091,16.36363636,9.090909091,5.454545455,12.72727273,12.72727273,9.090909091,7.272727273,7.272727273,10.90909091]

notes_classe2 = [20,20,18.18181818,14.54545455,18.18181818,20,18.18181818,20,20,14.54545455,20,16.36363636,12.72727273,18.18181818,18.18181818,20,18.18181818,18.18181818,20,16.36363636,18.18181818,18.18181818,18.18181818,18.18181818,18.18181818,9.090909091,20]

notes = [notes_classe1, notes_classe2]

result = stat.ttest_rel(*notes)
print(f"La statistique observée est de {result.statistic}")
print(f"La probabilité que la va soit <= à {result.statistic} est {result.pvalue}")
print(f"donc, au seuil de risque {ALPHA}", end="")
if result.pvalue < ALPHA:
    print(", on rejette", end="")
else:
    print(", on accepte", end="")
print(" l'hypothèse selon laquelle la moyenne de Notes1 est supérieure à celle de Notes2.")

