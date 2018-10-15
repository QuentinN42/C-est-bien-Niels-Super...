import csv
import numpy as np
from data import xp,entete

L = list(csv.reader(open('./donnee.txt', 'r')))




print(L)
print(entete)


def moy(l):
    return sum(l)/len(l)

def ecart_type(l):
    e=0
    for i in l:
        e+=(i-moy(l))**2
    return np.sqrt(e/len(l))

print(ecart_type([5,6,7,2,1,9,8,7,5,2,3,2,8]))


