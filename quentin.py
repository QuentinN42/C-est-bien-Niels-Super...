# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mickael import ecart_type as et,moy
from matthieu import clasmt_thm as trieMult

"""
def map(*arg):
    return list(map(*arg))

"""

def tprint(T):
    for e in T:
        print(e)

def zip(t):
    return [[e[i] for e in t] for i in range(len(t[0]))]

def removefirst(t):
    return [x[1:]for x in t]

def sommeNoteEtValide(v,I):
    O = []
    for i in range(len(I)):
        O.append([v[i]]+I[i])
    return O
        

def f(v,l):
    #prend et formate la liste
    return trieMult(sommeNoteEtValide(v,removefirst(l)),1,False)


def nbadmis(v):
    #renvois le nombres d'admis
    return v.count(True)


def pourcentadmis(v):
    #renvois le pourcentage d'admis entre 0 et 1
    return nbadmis(v)/len(v)


def nbnonadmis(v):
    #renvois le nombres de non admis
    return v.count(False)


def pourcentnonadmis(v):
    #renvois le pourcentage de non admis entre 0 et 1
    return nbnonadmis(v)/len(v)


def nbaudessus(xps,pallier):
    nb = 0
    for xp in xps:
        if xp >= pallier:
            nb += 1
    return nb


def pieChartAdmis(v): # graph des etudiants admis/non admis
    labels = ["Admis","Non admis"]
    colors = ['gold', 'lightskyblue']

    plt.pie([nbadmis(v),nbnonadmis(v)], labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)

    plt.axis('equal')
    # plt.savefig('PieChart01.png')
    plt.show()
    plt.close()


def pieChartNotes(notes): # graph des notes d'un etudiant
    labels = ["UE" + str(1+i) for i in range(len(notes))]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

    plt.pie(notes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)

    plt.axis('equal')
    # plt.savefig('PieChart01.png')
    plt.show()
    plt.close()

def plotColor(v,D,l='XP'):
    valide = []
    nonvalide = []
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5,100.5)
    ax.set_xlabel('N eleve')
    ax.set_ylabel(l)
    for i in range(len(v)):
        if v[i]:
            c = 'g'
            valide.append(D[i])
        else:
            c = 'r'
            nonvalide.append(D[i])
        plt.plot(i,D[i], 'o'+c)
    plt.plot([0,100],[max(nonvalide),max(nonvalide)], '--r')
    plt.plot([0,100],[min(valide),min(valide)], '--g')
    plt.show()
    print(int(max(nonvalide)*100)/100," --- ",int(min(valide)*100)/100," |     Moyenne : ",moy(D))
    plt.close()

def pcz(L,l='XP'):
    plotColor(zip(L)[0],zip(L)[1],l)

def plotEcTColor(v,D,l='Ecart Type'):
    valide = []
    nonvalide = []
    E = list(map(et,D))
    M = list(map(moy,D))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5,len(D)+0.5)
    ax.set_xlabel('N eleve ')
    ax.set_ylabel(l)
    for i in range(len(v)):
        if v[i]:
            c = 'g'
            valide.append(M[i])
        else:
            c = 'r'
            nonvalide.append(M[i])
        plt.plot(i,M[i], 'o'+c)
        plt.plot([i,i],[M[i]-E[i],M[i]+E[i]], '-'+c)
    plt.plot([0,100],[max(nonvalide),max(nonvalide)], '--r')
    plt.plot([0,100],[min(valide),min(valide)], '--g')
    plt.show()
    print(max(nonvalide)," --- ",min(valide))
    plt.close()


if __name__ == "__main__":
    from data import Valide as V,XPt,note,notelog,noteinv,notecarre
    
    XPt = f(V,XPt)
    note = f(V,note)
    notelog = f(V,notelog)
    noteinv = f(V,noteinv)
    notecarre = f(V,notecarre)
    
    pcz(XPt,'XP')
    pcz(note,'Modele Lineaire')
    pcz(notelog,'Modele Log')
    pcz(noteinv,'Modele Inverse')
    pcz(notecarre,'Modele racine carré')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
