# -*- coding: utf-8 -*-
import csv


Noms  = [x[0] for x in list(csv.reader(open('PrenomsRandom.txt', 'r')))]

print(Noms)

#for i in range(len(Noms))
