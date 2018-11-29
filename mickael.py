# -*- coding: utf-8 -*-
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matthieu as mat

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
    s=0
    for i in l:
        s+=i
    return s/len(l)


def ecart_type(l): #renvoie l'ecart type d'une liste
    e=0
    m=moy(l)
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



    #plt.savefig('./Data/' + str(prenoms.index(nom)) + '/hist.png')
    #plt.show()
    plt.close()



#                           AVANCEMENT COMPETITIF / RIVAUX

def plotbarlist(x,y,c,nom): #pour faciliter le code plus bas
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel(' The competitive graph ')
    ax.set_ylabel(' XP total ')
    ax.set_ylim(y[0][1]-10, y[4][1]+10)
    blue_patch = mpatches.Patch(color='blue', label='you')
    red_patch = mpatches.Patch(color='red', label='you re not that far')
    green_patch = mpatches.Patch(color='green', label='you ve beaten them !')
    plt.legend(handles=[blue_patch, red_patch,green_patch])
    plt.bar(x[0], y[0][1], color=c[0])
    plt.bar(x[1], y[1][1], color=c[1])
    plt.bar(x[2], y[2][1], color=c[2])
    plt.bar(x[3], y[3][1], color=c[3])
    plt.bar(x[4], y[4][1], color=c[4])
    plt.show()
    plt.savefig('./Data/' + str(dt.prenoms.index(nom)) + '/hist_comp.png')
    plt.close()




def G_position(nom, xp, prenom):

    n=len(prenom)
    numero = prenom.index(nom)
    print(mat.clasmt_thm(xp, 1)[prenom.index(nom)][1])
    if numero == 0 :
        a = mat.clasmt_thm(xp, 1)[prenom.index(nom) + 4]
        b = mat.clasmt_thm(xp, 1)[prenom.index(nom) + 3]
        c = mat.clasmt_thm(xp, 1)[prenom.index(nom) + 2]
        d = mat.clasmt_thm(xp, 1)[prenom.index(nom) + 1]
        e = mat.clasmt_thm(xp, 1)[prenom.index(nom)]
        plotbarlist(['-4', '-3', '-2', '-1', 'ME'], [a, b, c, d, e], ['g', 'g', 'g', 'g', 'b'],nom)
    elif numero == 1 :
        a = mat.clasmt_thm(xp, 1)[prenom.index(nom) + 3]
        b = mat.clasmt_thm(xp, 1)[prenom.index(nom) + 2]
        c = mat.clasmt_thm(xp, 1)[prenom.index(nom) + 1]
        d = mat.clasmt_thm(xp, 1)[prenom.index(nom)]
        e = mat.clasmt_thm(xp, 1)[prenom.index(nom) - 1]
        plotbarlist(['-3', '-2', '-1', 'ME', '+1'], [a, b, c, d, e], ['g', 'g', 'g', 'b', 'r'],nom)
    elif numero == 98 :
        a = mat.clasmt_thm(xp, 1)[prenom.index(nom) + 1 ]
        b = mat.clasmt_thm(xp, 1)[prenom.index(nom)]
        c = mat.clasmt_thm(xp, 1)[prenom.index(nom) - 1 ]
        d = mat.clasmt_thm(xp, 1)[prenom.index(nom) - 2 ]
        e = mat.clasmt_thm(xp, 1)[prenom.index(nom) - 3 ]
        plotbarlist(['-1', 'ME', '+1', '+2', '+3'], [a, b, c, d, e], ['g', 'b', 'r', 'r', 'r'],nom)
    elif numero == 99 :
        a = mat.clasmt_thm(xp, 1)[prenom.index(nom)]
        b = mat.clasmt_thm(xp, 1)[prenom.index(nom) - 1]
        c = mat.clasmt_thm(xp, 1)[prenom.index(nom) - 2]
        d = mat.clasmt_thm(xp, 1)[prenom.index(nom) - 3]
        e = mat.clasmt_thm(xp, 1)[prenom.index(nom) - 4]
        plotbarlist(['ME', '+1', '+2', '+3', '+4'], [a, b, c, d, e], ['b', 'r', 'r', 'r', 'r'],nom)
    else :
        a = mat.clasmt_thm(xp, 1)[prenom.index(nom) + 2]
        b = mat.clasmt_thm(xp, 1)[prenom.index(nom) + 1]
        c = mat.clasmt_thm(xp, 1)[prenom.index(nom)]
        d = mat.clasmt_thm(xp, 1)[prenom.index(nom) - 1]
        e = mat.clasmt_thm(xp, 1)[prenom.index(nom) - 2]
        plotbarlist(['-2', '-1', 'ME', '+1', '+2'], [a, b, c, d, e], ['g', 'g', 'b', 'r', 'r'],nom)









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
    plt.savefig('./Data/Prof/hist_comp.png')
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
    #G_xptot(dt.XPt,dt.prenoms)
    G_position(dt.prenoms[5], dt.XP, dt.prenoms)




