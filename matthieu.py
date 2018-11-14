# -*- coding: utf-8 -*-
import csv
import numpy as np
import data as dt

with open('./donnee.txt', 'r') as f:
    reader = csv.reader(f)
    donnees = list(reader)


donnees = np.array(donnees[1:]).astype(np.float).astype(np.int)
#np.array(donnees).astype(np.float)
LALALA = [[1,2,3,6,5],[25,1,4,3,4],[52,665,32,3,8]]



def clasmt_thm(l,n,r=True):
    # trie un tableau l par raport a la collone n
    # on extrait d'abord la n-ieme colonne
    colonne_trie = []
    for liste in l:
        colonne_trie.append([liste[n]])
    for i in range(len(colonne_trie)):
        colonne_trie[i].append(i)
    colonne_trie.sort(reverse = r)  # <=> sort(reversed = True) pour trier a l'envers
    #colonne_trie = colonne_trie[::-1]
    O = []
    for c in colonne_trie:
        O.append(l[c[1]])

    return O # return plutot que print()


with open('PrenomsRandom.txt', 'r') as f:
    reader = csv.reader(f)
    prenoms = list(reader)



    