"""

MaxXP   : tableau 1D    : XP maximum par UE     : [max1,max2,...]
XP      : tableau 2D    : XP par UE par eleve   : [[e1,xp11,xp12,...],[e2,xp21,xp22,...]]



"""
# imports ----------------------------------------------------------------------
import csv


#-------------------------------------------------------------------------------


data = list(csv.reader(open('./donnee.txt', 'r')))

#-------------------------------------------------------------------------------
# supression entete dans les donnees + formatage xp maximum par UE

entete = data.pop(0)
MaxXP = [int(float(entete[i])) for i in range(len(entete)-1)]


#-------------------------------------------------------------------------------
# formatage des donnees en int

data = [list(map(lambda x: int(float(x)),d)) for d in data]

#-------------------------------------------------------------------------------
# creation des xp de chaques etudiants

xp = [[i] + data[i][:-1] for i in range(len(data))]

#-------------------------------------------------------------------------------
# affichage si le prg est executé seul (ne pas en tenir compte)


if __name__ == "__main__":
    print(entete)
    print(xp)
