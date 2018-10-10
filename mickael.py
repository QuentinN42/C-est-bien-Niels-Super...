import csv

L = list(csv.reader(open('./donnee.txt', 'r')))



print(L)



def moyenne(l):
    return sum(l)/len(l)