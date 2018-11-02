# -*- coding: utf-8 -*-
"""

MaxXP     : tableau 1D    : XP maximum par UE                  : [max1,max2,...]
XP        : tableau 2D    : XP par eleve                       : [[e1,xp11,xp12,...],[e2,xp21,xp22,...],...]
XPmaxe    : tableau 2D    : XP par eleve maxé                  : [[e1,xp11,xp12,...],[e2,xp21,xp22,...],...]
XPt       : tableau 2D    : XP total par eleve (maxé)          : [[e1,xp11+xp12+...],[e2,xp21+xp22+...],...]
XPi       : tableau 2D    : XP par UE par eleve                : [[e1,xpi1],[e2,xpi2],...]
Valide    : tableau 1D    : True/False si validé               : [True,True,False,...]
prenoms   : tableau 1D    : nom des eleves                     : ["pierre","bla","bli",...]
note      : tableau 2D    : note /20 par eleves modele lin     : [[e1,12],[e2,15]...]
notelog   : tableau 2D    : note /20 par eleves modele log     : [[e1,12],[e2,15]...]
noteinv   : tableau 2D    : note /20 par eleves modele inverse : [[e1,12],[e2,15]...]
notecarre : tableau 2D    : note /20 par eleves modele sqrt    : [[e1,12],[e2,15]...]

"""
# imports ----------------------------------------------------------------------
import csv
from math import log,sqrt



with open('PrenomsRandom.txt', 'r') as f:
    reader = csv.reader(f)
    prenoms = [x[0] for x in list(reader)]


#-------------------------------------------------------------------------------

data = list(csv.reader(open('./donnee.txt', 'r')))
#prenoms = open('./Prenoms.txt', 'r').read().split("\n")

#-------------------------------------------------------------------------------
# supression entete dans les donnees + formatage xp maximum par UE

entete = data.pop(0)
MaxXP = [int(float(entete[i])) for i in range(len(entete)-1)]


#-------------------------------------------------------------------------------
# formatage des donnees en int

data = [list(map(lambda x: int(float(x)),d)) for d in data]

#-------------------------------------------------------------------------------
# creation des xp de chaques etudiants

XP = [[i] + data[i][:-1] for i in range(len(data))]

XP1 = [[i,data[i][1]] for i in range(len(data))]
XP2 = [[i,data[i][2]] for i in range(len(data))]
XP3 = [[i,data[i][3]] for i in range(len(data))]
XP4 = [[i,data[i][4]] for i in range(len(data))]

#-------------------------------------------------------------------------------
# maxing des etudiants

XPmaxe = []

for i in range(len(XP)):
    t = [i]
    for j in range(len(XP[i])-1):
        if XP[i][j+1]> MaxXP[j]:
            t.append(MaxXP[j])
        else:
            t.append(XP[i][j+1])
    XPmaxe.append(t)

XPt = [[i]+[sum(XPmaxe[i][1:])] for i in range(len(data))]

#-------------------------------------------------------------------------------
# creation de la note sur 20 de chaques étudiants
note = []
notelog = []
noteinv = []
notecarre = []


for i in range (len(XP)):
    tablin = [XP[i][0]]
    tablog = [XP[i][0]]
    tabinv = [XP[i][0]]
    tabcarre = [XP[i][0]]
    
    #modele lineaire
    tablin.append(20*XPt[i][1]/sum(MaxXP))
    #modele log
    tablog.append(10*log(XPt[i][1],20))
    #modele 1/x
    tabinv.append(116.36*XPt[i][1]/(1000+4*XPt[i][1]))
    #modele carre
    tabcarre.append(20/sqrt(550)*sqrt(XPt[i][1]))
    
    
    
    note.append(tablin)
    notelog.append(tablog)
    noteinv.append(tabinv)
    notecarre.append(tabcarre)



#-------------------------------------------------------------------------------
# creation des validation de chaques etudiants

Valide = [True if data[i][-1] == 1 else False for i in range(len(data))]


#-------------------------------------------------------------------------------
# affichage si le prg est executé seul (ne pas en tenir compte)

if __name__ == "__main__":
    print(MaxXP)
    for i in range(len(data)):
        print(XPmaxe[i])
        
        

    
    

