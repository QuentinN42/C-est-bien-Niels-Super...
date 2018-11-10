# -*- coding: utf-8 -*-

import data as dt

for i in range (100):
    with open('Data/'+str(i)+'/prenom.txt', 'w') as f:
        f.write(dt.prenoms[i])





#-------------------------------------------------------------------------------
# ecriture des notes / xps
for i in range (100):
    ln = "Data/" + str(i) + "/note"
    
    llin =   ln + ".txt"
    llog =   ln + "l.txt"
    linv =   ln + "i.txt"
    lcarre = ln + "c.txt"
    
    
    
    with open(llin, 'w') as f:
        w = str(dt.note[i][1])
        f.write(w)
    
    with open(llog, 'w') as f:
        w = str(dt.notelog[i][1])
        f.write(w)
    
    with open(linv, 'w') as f:
        w = str(dt.noteinv[i][1])
        f.write(w)
    
    with open(lcarre, 'w') as f:
        w = str(dt.notecarre[i][1])
        f.write(w)
    
    
    # XP
    for j in [1,2,3,4]:
        lxp= "Data/" + str(i) + "/xp"   + str(j) + ".txt"
        with open(lxp, 'w') as f:
            w = str(dt.XPmaxe[i][j])
            f.write(w)



