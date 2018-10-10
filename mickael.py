import csv
import numpy as np

L = list(csv.reader(open('./donnee.txt', 'r')))




print(L)



def moy(l):
    return sum(l)/len(l)

def ecart_type(l):
