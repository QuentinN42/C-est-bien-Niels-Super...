import csv
import numpy as np
import data as dt
import matplotlib.pyplot as plt

L = list(csv.reader(open('./donnee.txt', 'r')))
l_test =[5,6,7,2,1,9,8,7,5,2,3,2,8]

l_test.sort(reverse=True)
print(l_test)



'''modèle graph : 
x= [ --- ]
y = [ --- ]

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_xlabel(' ---- ' )
ax.set_ylabel(' ----- ')

plt.plot(x,y, '+r')
'''


#                                              STATISTIQUES


def moy(l): #renvoie la moyenne d'une liste
    return sum(l)/len(l)

def ecart_type(l): #renvoie l'écart type d'une liste
    e=0
    m=moy(l)
    # tu peut calculer la moyenne ici tu la calcule une seule fois donc ca vas plus vite :)
    for i in l:
        e+=(i-m)**2
    return np.sqrt(e/len(l))




def quartiles(l): #renvoie un triplet de la forme (1er quartile, médiane, 3ième quartile)
    l.sort()
    i=0
    while len(l[:i+1])/len(l)<=0.25 :
        i+=1
    Q_1 = l[i]
    while len(l[:i + 1]) / len(l) <= 0.5:
        i+=1
    Q_2 = l[i]
    while len(l[:i+1])/len(l)<=0.75 :
        i+=1
    Q_3 = l[i]

    return Q_1, Q_2, Q_3

#                                         TENTATIVE DE GRAPH


#nombre d'xp par ue /eleve:

def G_nb_XP(nom):
    x = ['t1','t2','t3','t4']
    y = dt.XP[dt.prenoms.index(nom)].remove(dt.prenoms.index(nom))
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_xlabel('UE ')
    ax.set_ylabel(' XP ')

    plt.plot(x, y, '+r')




