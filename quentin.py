


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

if __name__ == "__main__":
    from data import XPt as xp
    print(nbaudessus([e[1] for e in xp],250))
