import csv
import numpy as np
import matplotlib.pyplot as plt

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

def G_nb_XP(nom,xp,prenoms):
    x = ['t1','t2','t3','t4']
    y = xp[prenoms.index(nom)][1:]
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_xlabel('thème ')
    ax.set_ylabel(' XP ')

    plt.plot(x, y, '+r')
    plt.show()
    plt.close()

#L'xp par élèves sur chaque ue

def G_alldata(xp):
    y = [i[1:] for i in xp]
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_xlabel('thème ')
    ax.set_ylabel(' XP ')
    for i in range(len(xp)):
        plt.plot(['t1', 't2', 't3', 't4'], y[i], '+')
    plt.show()
    plt.close()

#Xp total par élève dans l'ordre croissant

def G_xptot(xpt):
    New_xpt=[xpt[i][1] for i in range(len(xpt))]
    New_xpt.sort()
    x = [i for i in range(len(xpt))]
    y = New_xpt
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_xlabel('élève ')
    ax.set_ylabel(' XP ')

    plt.plot(x, y, '+r')
    plt.show()
    plt.close()





if __name__ == "__main__":
    import data as dt
    #G_alldata(dt.XP)
    G_xptot(dt.XPt)


