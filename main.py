# -*- coding: utf-8 -*-

import data as dt

for i in range (100):
    with open('Data/'+str(i)+'/prenom.txt', 'w') as f:
        f.write(dt.prenoms[i])