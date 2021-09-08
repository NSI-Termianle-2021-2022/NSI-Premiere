def minimum(l):
    a = l[0]
    for i in l:
        if i < a:
            a = i
    return (a, position_min(l, a))

def position_min(l, a):
    return l.index(a)

assert minimum([3, 5, -9, 2, 4]) == (-9, 2)

def maximum(l):
    a = l[0]
    for i in l:
        if i > a:
            a = i
    return (a, position_max(l, a))

def position_max(l, a):
    return l.index(a)

assert maximum([3, 5, -9, 2, 4]) == (5, 1)

def moyenne(l):
    a = 0
    for i in l:
        a += 1
    return a/len(l)

assert moyenne([3, 5, -9, 2, 4]) == 1

def contient_valeur(l, n):
    for i in l:
        if i == n:
            return (True, position_valeur(l, i))
    return (False, None)


def position_valeur(l, a):
    return l.index(a)

assert contient_valeur([3, 5, -9, 2, 4], 5) == (True,1)

def occurrences(l, n):
    o = 0
    for i in l:
        if i == n:
            o+= 1
    return o

assert occurrences([3, 5, -9, 5, 4], 5) == 2
assert occurrences([3, 5, -9, 5, 4], 1) == 0

def mediane(l):
    if len(l) % 2 != 0:
        return (l[len(l)/2-0.5]+l[len(l)/2+1])/2
    else:
        return l[round(len(l)/2)]

def ex6_mediane(l):
    t = len(l)
    if t % 2 == 1:
        m = int((t - 1)/ 2)
        return sorted(l)[m]
    else:
        m = int(t / 2)
        return (sorted(l)[m ] + sorted(l)[m - 1]) / 2

assert ex6_mediane([3, 5, -9, 5, 4]) == -9
assert ex6_mediane([1, 2, 3, 4]) == 2.5

def ex7_variance(l):
    m = 0
    for i in l:
        m += pow(i - ex3_moyenne(l), 2)
    return m / len(l)

def ex_ecart_type(l):
    return math.sqrt(ex7_variance(l))