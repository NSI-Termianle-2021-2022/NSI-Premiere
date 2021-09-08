
def inttopath(i: int) -> str:
    if i == 1:
        return "pyramides\\p1.txt"
    if i == 2:
        return "pyramides\\p2.txt"
    if i == 3:
        return "pyramides\\p3.txt"
    if i == 4:
        return "pyramides\\p4.txt"
    if i == 5:
        return "pyramides\\p5.txt"

def load(rang: int) -> list:

    L = list()
    path = inttopath(rang)

    fichier = open(path, "r")

    L = fichier.readlines()
    fichier.close()

    for i in range(len(L)):
        L[i] = L[i][:-1]

    return L


