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



def clasmt_thm(l,n):
    # trie un tableau l par raport a la collone n
    # on extrait d'abord la n-ieme colonne
    colonne_trie = []
    for liste in l:
        colonne_trie.append([liste[n]])
    for i in range(len(colonne_trie)):
        colonne_trie[i].append(i)
    colonne_trie.sort()  # <=> sort(reversed = True) pour trier a l'envers
    colonne_trie = colonne_trie[::-1]



    return colonne_trie # return plutot que print()


if __name__ == "__main__":
    # ne s'execute que si on lance ce script seul, pas si on l'importe
    print(clasmt_thm(donnees,0))


import matplotlib.pyplot as plt

labels = 'Allemagne', 'France', 'Belgique', 'Espagne'
sizes = [15, 80, 45, 40]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')

# plt.savefig('PieChart01.png')
plt.show()
