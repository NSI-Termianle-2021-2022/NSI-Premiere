def tri_longueur(li):
    tri = []
    a = 0
    while True:
        for i in li:
            if len(i) == a:
                tri.append(i)
        if len(li) == len(tri):
            break
        a += 1
    return tri

print(tri_longueur(["aaaa", "bb", "c"]))
assert tri_longueur(["aaaa", "bb", "c"]) == ["c", "bb", "aaaa"]

def minimum(l):
    a = l[0]
    for i in l:
        if i < a:
            a = i
    return (a, position_min(l, a))

def position_min(l, a):
    return l.index(a)

assert minimum([3, 5, -9, 2, 4]) == (-9, 2)