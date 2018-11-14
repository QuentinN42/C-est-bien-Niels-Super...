# -*- coding: utf-8 -*-
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

L = list(csv.reader(open('./donnee.txt', 'r')))
l_test =[5,6,7,2,1,9,8,7,5,2,3,2,8]

l_test.sort(reverse=True)
#print(l_test)




'''modèle graph :
x= [ --- ]
y = [ --- ]

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_xlabel(' ---- ' )
ax.set_ylabel(' ----- ')

plt.plot(x,y, '+r')


plt.show()
plt.close()
'''
#                                               FONCTIONS UTILES

def column(matrix, i):
    return [row[i] for row in matrix]
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

#                 TENTATIVE DE GRAPHS


#nombre d'xp par ue /eleve:

def G_nb_XP(nom,xp,prenoms):
    x = ['t1','t2','t3','t4']
    y = xp[prenoms.index(nom)][1:]
    y_max = dt.XPmaxe[prenoms.index(nom)][1:]
    M1=moy(column(dt.XP1,1))
    M2=moy(column(dt.XP2,1))
    M3=moy(column(dt.XP3,1))
    M4=moy(column(dt.XP4,1))

    fig = plt.figure()
    blue_patch = mpatches.Patch(color='blue', label='legal points')
    black_patch = mpatches.Patch(color='black', label='overkill points')
    ax = fig.add_subplot(111)
    ax.set_xlabel('theme ')
    ax.set_ylabel(' XP ')
    plt.legend(handles=[blue_patch,black_patch])
    plt.bar(x,y,color='k')
    plt.bar(x,y_max,color='b')
    plt.plot(x, [50,100,100,200], 'rv', markersize=10)
    plt.plot(x,[M1,M2,M3,M4], 'r_', markersize=40)



    plt.savefig('./Data/' + str(prenoms.index(nom)) + '/hist.png')
    #plt.show()
    plt.close()

#L'xp par eleves sur chaque ue

def G_alldata(xp):
    y = [i[1:] for i in xp]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    xp_up = np.array(xp)
    Q = np.array(list(map(quartiles, [xp_up[:,1], xp_up[:,2], xp_up[:,3], xp_up[:,4]])))
    print(Q)
    ax.set_xlabel('theme ')
    ax.set_ylabel(' XP ')
    plt.plot(['t1', 't2', 't3', 't4'],Q[:,0], 'b^', markersize=10 )
    plt.plot(['t1', 't2', 't3', 't4'],Q[:,1], 'ro', markersize=10 )  #   ajouter moyene :/
    plt.plot(['t1', 't2', 't3', 't4'],Q[:,2], 'bv', markersize=10)
    for u in range(len(xp)):
        plt.plot(['t1', 't2', 't3', 't4'], y[u], 'k+')
    plt.show()
    plt.close()

#Xp total par élève dans l'ordre croissant

def G_xptot(xpt,prenoms):
    l=sorted(xpt, key=lambda x : x[1])
    print(l)
    x = [str(l[i][0]) for i in range(len(xpt))]
    y = [l[i][1] for i in range(len(xpt))]
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_xlabel('eleve ')
    ax.set_ylabel(' XP ')

    plt.plot(x,y, '+r')
    plt.show()
    plt.close()





if __name__ == "__main__":
    import data as dt
    #G_alldata(dt.XP)
    #G_xptot(dt.XPt,dt.Prenom)
    for i in dt.prenoms:
        G_nb_XP(i, dt.XP, dt.prenoms)



