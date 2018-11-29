    # -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import to_hex
from mickael import ecart_type as et,quartiles as Q,moy
from matthieu import clasmt_thm as trieMult

"""
def map(*arg):
    return list(map(*arg))

"""






#%%

read = lambda x: int(100*x)/100

def tprint(T):
    for e in T:
        print(e)

def zip(t):
    return [[e[i] for e in t] for i in range(len(t[0]))]



def removefirst(t):
    return [x[1:]for x in t]


#%%


def sommeNoteEtValide(v,I):
    O = []
    for i in range(len(I)):
        O.append([v[i]]+I[i])
    return O
        

#%%

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



#%%



def pieChartAdmis(v): # graph des etudiants admis/non admis
    labels = ["Admis","Non admis"]
    colors = ['gold', 'lightskyblue']

    plt.pie([nbadmis(v),nbnonadmis(v)], labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)

    plt.axis('equal')
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




#%%





def someinfo(D,name):
    O = "Moyenne          : " + str(read(moy(D))) + "<br>Ecart type       : " + str(read(et(D))) +  "<br>Min / Max        : " + str(read(min(D))) + " --- " + str(read(max(D))) + "<br>Q1 / M / Q3      : " + str(tuple(map(read,Q(D))))
    print(O)
    with open("./Data/Prof/" + name.replace(" ","_") + ".txt", 'w') as f:
        f.write(O)



def plotColor(v,D,l='XP',text=True):
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
    #plt.plot([0,100],[10,10], '--b')
    plt.show()
    plt.savefig("./Data/Prof/" + l.replace(" ","_") + ".png")
    if text:
        print("Echec / Reussite : ",read(max(nonvalide))," --- ",read(min(valide)))
        someinfo(D,l)


def plotEcTColor(v,D,l='Ecart Type',text=True):
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
    plt.plot([0,100],[10,10], '--b')
    plt.show()
    if text:
        print(max(nonvalide)," --- ",min(valide))


def pcz(L,l='XP',text=True):
    plotColor(zip(L)[0],zip(L)[1],l,text)




#%%




def plot3d(v,l,C):
    fig = plt.figure()
    ax = Axes3D(fig)
    
    x = [e[0] for e in l]
    y = [e[1] for e in l]
    z = [e[2] for e in l]
    
    c = [to_hex((1-(e-min(C))/(max(C)-min(C)),(e-min(C))/(max(C)-min(C)),0)) for e in C]
    
    nrx = [x[i] for i in range(len(l)) if v[i] is not True]
    nry = [y[i] for i in range(len(l)) if v[i] is not True]
    nrz = [z[i] for i in range(len(l)) if v[i] is not True]
    nrC = [C[i] for i in range(len(c)) if v[i] is not True]
    nrc = [to_hex((1-(e-min(nrC))/(max(nrC)-min(nrC)),(e-min(nrC))/(max(nrC)-min(nrC)),0)) for e in nrC]
    
    for i in range(len(v)):
        if v[i]:
            f = 'o'
        else:
            f = '^'
        ax.plot([x[i]], [y[i]], [z[i]], f, color = c[i])
    
    plt.show()
    plt.savefig("./Data/Prof/3D.png")
    
    """
    fig = plt.figure()
    ax = Axes3D(fig)
    
    for i in range(len(nrc)):
        ax.plot([nrx[i]], [nry[i]], [nrz[i]], '^', color = nrc[i])
    plt.show()
    """

#%%





if __name__ == "__main__":
    from data import Valide as V,XPt,note,notelog,noteinv,notecarre,XPmaxe,MaxXP
    
    
    XPt = f(V,XPt)
    note = f(V,note)
    notelog = f(V,notelog)
    noteinv = f(V,noteinv)
    notecarre = f(V,notecarre)
    
    
    print(notelog)
    
    pcz(XPt,'XP',True)
    pcz(note,'Modele Lineaire',True)
    pcz(notelog,'Modele Log',True)
    pcz(noteinv,'Modele Inverse',True)
    
    
    
    #pcz(notecarre,'Modele racine carré')
    
    
    """
    someinfo(zip(note)[1])
    someinfo(zip(notelog)[1])
    someinfo(zip(noteinv)[1])
    someinfo(zip(notecarre)[1])
    """
    print(MaxXP)
    plot3d(V,removefirst(XPmaxe),[e[3] for e in XPmaxe])
    
    