import random
import time

def minimum(l):
    a = l[0]
    for i in l:
        if i < a:
            a = i
    return (a, position_min(l, a))

def position_min(l, a):
    return l.index(a)

assert minimum([3, 5, -9, 2, 4]) == (-9, 2)

def exercice_2(a):
    for i in range(len(a)):
        m = i
        for j in range(i+1, len(a)):
            if a[j] < a[i]:
                m = j
            a[i], a[j] = a[j], a[i]
    return a


def exo_3_tri_par_selection(l):
    retour = l
    while True:
        casser = 0
        for i in range(len(l)-1):
            if retour[i] > retour[i+1]:
                retour[i+1], retour[i] = retour[i], retour[i+1]
                casser = 0
            if retour[i] < retour[i+1]:
                casser += 1
        if casser == len(l)-1:
            break
    return retour

assert exo_3_tri_par_selection([15, 2, 56, 48]) == [2, 15, 48, 56]
assert exo_3_tri_par_selection(['kjlhw', 'qsmefjel', 'azejk']) == ['azejk', 'kjlhw', 'qsmefjel']


def minimum(l):
    a = l[0]
    for i in l:
        if i < a:
            a = i
    return (a, position_min(l, a))

def position_min(l, a):
    return l.index(a)

assert minimum([3, 5, -9, 2, 4]) == (-9, 2)

def exo_3_tri_par_selection2(l):
    modifie = l
    retour = []
    for i in range(len(l)):
        min = minimum(modifie)
        retour.append(modifie[min[1]])
        del modifie[min[1]]

    return retour

assert exo_3_tri_par_selection2([15, 2, 56, 48]) == [2, 15, 48, 56]
assert exo_3_tri_par_selection2(['kjlhw', 'qsmefjel', 'azejk']) == ['azejk', 'kjlhw', 'qsmefjel']

def alea(n):
    return [random.randint(0,100) for i in range(n)]

def TempsAlgo(i):
    t = time.time()
    exo_3_tri_par_selection2(alea(i))
    return time.time() -t

print(TempsAlgo(18000))

#Sur mon PC, TempsAlgo() semble dépasser 1s de temps d'exéctution dès 9000 valeurs.
#Sur mon PC, TempsAlgo() semble dépasser 2s de temps d'exéctution dès 12000 valeurs.
#Sur mon PC, TempsAlgo() semble dépasser 5s de temps d'exéctution dès 18000 valeurs.