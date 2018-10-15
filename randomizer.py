# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 16:31:32 2018

@author: etudiant
"""


import random as rd
P = open('./Prenoms.txt', 'r').read().split("\n")
P1 = P
P2= []


while P != [] :
    i = rd.randint(0,len(P)-1)
    P2.append(P.pop(i))


W = open('./PrenomsRandom.txt', 'w')
for nom in P2:
    W.write(nom + "\n")
