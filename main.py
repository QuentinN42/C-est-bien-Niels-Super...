# -*- coding: utf-8 -*-

import data as dt

for i in range (100):
    with open('Data/'+str(i)+'/prenom.txt', 'w') as f:
        f.write(dt.prenoms[i])
        
        
#-------------------------------------------------------------------------------
# ecriture des notes / 20
for i in range (100):
    with open('Data/'+str(i)+'/notes.txt', 'w') as f:
        for e in dt.note[i][1:]:
            f.write(str(e)+"\n")
        
        
        
#-------------------------------------------------------------------------------
# ecriture des notes xp
for i in range (100):
    with open('Data/'+str(i)+'/xps.txt', 'w') as f:
        for e in dt.XP[i][1:]:
            f.write(str(e)+"\n")