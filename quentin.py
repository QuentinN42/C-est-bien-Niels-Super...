# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def nbadmis(v):
    #renvois le nombres d'admis
    return v.count(True)


def pourcentadmis(v):
    #renvois le pourcentage d'admis entre 0 et 1
    return nbadmis(v)/len(v)

def nbaudessus(xps,pallier):
    nb = 0
    for xp in xps:
        if xp >= pallier:
            nb += 1
    return nb

def pieChart(notes):
    labels = ["UE" + str(1+i) for i in range(len(notes))]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

    plt.pie(notes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)

    plt.axis('equal')
    # plt.savefig('PieChart01.png')
    plt.show()
    plt.close()




if __name__ == "__main__":
    from data import XP as xp
    pieChart([e[1:] for e in xp][2])
