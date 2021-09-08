# Pyramides

import sys

def pyramide(rang: int) -> None:
    etage = 0
    largeur = []
    for i in range(0, rang):
        for j in range(0, i+3):
            etage = etage + 1
            if etage == 1:
                largeur.append(1)
            else:
                assert(0 <= (etage- 2) < len(largeur))
                if j == 0 and i % 2 == 0:
                    largeur.append(largeur[etage - 2] + i + 4)
                elif j ==0 and i % 2 == 1:
                    largeur.append(largeur[etage - 2] + i + 3)
                else:
                    largeur.append(largeur[etage - 2] + 2)

    impr = []
    for i in range(etage):
        assert(0 <= (etage-1) < len(largeur))
        assert(0 <= i < len(largeur))
        indentation = int((largeur[etage-1] - largeur[i])/2)
        impr.append(' ' * indentation + '/' + '*' * largeur[i] + '\\')

    if rang == 2:
        largeur_porte = 3
    elif rang % 2 == 0:
        largeur_porte = rang -1
    else:
        largeur_porte = rang

    if rang == 0:
        largeur_max = 0
    else:
        largeur_max = len(impr[etage - 1])

    for i in range(etage - rang, etage):
        str_porte = largeur_porte * '|'
        position = (largeur_max - largeur_porte) // 2
        impr[i] = impr[i][:position] + str_porte + impr[i][position + largeur_porte:]

    for item in impr:
        print(item)


print("\nProgram name: ", sys.argv[0])
print("Argument List:", str(sys.argv))

if len(sys.argv) < 2:
    n = int(input("Choissisez le rang de la pyramide: "))
    print("\nPyramide {}:".format(n))
    pyramide(n)
else:
    for compteur in range(1, len(sys.argv)):
        rang = int(sys.argv[compteur])
        print("\nPyramide {}:".format(rang))
        pyramide(rang)
