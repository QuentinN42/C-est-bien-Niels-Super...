# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def nbadmis(v):
    #renvois le nombres d'admis
    return v.count(True)


def pourcentadmis(v):
    #renvois le pourcentage d'admis entre 0 et 1
    return nbadmis(v)/len(v)


def nbnonadmis(v):
    #renvois le nombres de non admis
    return v.count(False)


def pourcentnonadmis(v):
    #renvois le pourcentage de non admis entre 0 et 1
    return nbnonadmis(v)/len(v)


def nbaudessus(xps,pallier):
    nb = 0
    for xp in xps:
        if xp >= pallier:
            nb += 1
    return nb


def pieChartAdmis(v): # graph des etudiants admis/non admis
    labels = ["Admis","Non admis"]
    colors = ['gold', 'lightskyblue']

    plt.pie([nbadmis(v),nbnonadmis(v)], labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)

    plt.axis('equal')
    # plt.savefig('PieChart01.png')
    plt.show()
    plt.close()


def pieChartNotes(notes): # graph des notes d'un etudiant
    labels = ["UE" + str(1+i) for i in range(len(notes))]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

    plt.pie(notes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)

    plt.axis('equal')
    # plt.savefig('PieChart01.png')
    plt.show()
    plt.close()




if __name__ == "__main__":
    from data import Valide as V,XP as xp
    pieChartAdmis(V)
    pieChartNotes(xp[2])
