import csv
import numpy as np
with open('./donnee.txt', 'r') as f:
    reader = csv.reader(f)
    donnees = list(reader)

np.array(donnees).astype(np.float)