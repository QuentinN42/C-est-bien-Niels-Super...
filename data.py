# -*- coding: utf-8 -*-
"""

MaxXP   : tableau 1D    : XP maximum par UE     : [max1,max2,...]
XP      : tableau 2D    : XP par eleve          : [[e1,xp11,xp12,...],[e2,xp21,xp22,...],...]
XPt     : tableau 2D    : XP total par eleve    : [[e1,xp11+xp12+...],[e2,xp21+xp22+...],...]
XPi     : tableau 2D    : XP par UE par eleve   : [[e1,xpi1],[e2,xpi2],...]
Valide  : tableau 1D    : True/False si validé  : [True,True,False,...]
prenoms : tableau 1D    : nom des eleves        : ["pierre","bla","bli",...]
note    : tableau 2D    : note /20 par eleves   : [12/20,10/20,....]

"""
# imports ----------------------------------------------------------------------
import csv

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

XPt = [[i] + [sum(data[i][:-1])] for i in range(len(data))]

XP1 = [[i,data[i][1]] for i in range(len(data))]
XP2 = [[i,data[i][2]] for i in range(len(data))]
XP3 = [[i,data[i][3]] for i in range(len(data))]
XP4 = [[i,data[i][4]] for i in range(len(data))]



#-------------------------------------------------------------------------------
# creation de la note sur 20 de chaques étudiants
note = []

for i in range (len(data)):
    tab = [XP[i][0]]
    for j in range(4):
        if XP[i][j+1] >= MaxXP[j]:
            tab.append(20)
        else:
            tab.append(20*XP[i][j+1]/MaxXP[j])
    note.append(tab)

#-------------------------------------------------------------------------------
# creation des validation de chaques etudiants

Valide = [True if data[i][-1] == 1 else False for i in range(len(data))]


#-------------------------------------------------------------------------------
# affichage si le prg est executé seul (ne pas en tenir compte)

if __name__ == "__main__":
    print(MaxXP)
    for i in range(len(data)):
        print(XP[i],note[i])
        
        

    
    

