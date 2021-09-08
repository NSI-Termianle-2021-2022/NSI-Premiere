import sys

def entree_valide(entree):
    try:
        int(entree)
    except ValueError:
        return False
    if int(entree) <= 0:
        return False
    return True


def rang_porte(nombre_lignes):
    c = 0
    li_nbr_entier_naturels = [3]
    li_rang = [3]
    for i in range(nombre_lignes):
        ligne_rang = 0
        for j in li_nbr_entier_naturels:
            ligne_rang += j
        ligne_rang += li_nbr_entier_naturels[i] + 1
        li_nbr_entier_naturels.insert(i + 1, li_nbr_entier_naturels[i] + 1)
        li_rang.append(ligne_rang)
        i += 1
    while nombre_lignes >= li_rang[c]:
        c += 1
    return li_rang[c - 1]


def nbr_total_de_rang(nombre_lignes):
    c = 0
    li_nbr_entier_naturels = [3]
    li_rang = [3]
    for i in range(nombre_lignes):
        ligne_rang = 0
        for j in li_nbr_entier_naturels:
            ligne_rang += j
        ligne_rang += li_nbr_entier_naturels[i] + 1
        li_nbr_entier_naturels.insert(i + 1, li_nbr_entier_naturels[i] + 1)
        li_rang.append(ligne_rang)
        i += 1
    while nombre_lignes >= li_rang[c]:
        c += 1
    return li_nbr_entier_naturels[c - 1] - 2


def rang_vers_ligne(rang):
    if entree_valide(rang) == False:
        return None
    else:
        rang = int(rang)
    li_nbr_entier_naturels = [3]
    li_rang = [3]
    for i in range(rang):
        ligne_rang = 0
        for j in li_nbr_entier_naturels:
            ligne_rang += j
        ligne_rang += li_nbr_entier_naturels[i] + 1
        li_nbr_entier_naturels.insert(i + 1, li_nbr_entier_naturels[i] + 1)
        li_rang.append(ligne_rang)
        i += 1
    return li_rang[rang - 1]




def arbre(nombre_lignes):
    if nombre_lignes == None:
        return None
    p = 0
    surplus_etoiles = 0
    li = [3]
    li_niv = [3]
    k = 0
    pyramide = ""

    for i in range(1, nombre_lignes+1):
        pyramide += (nombre_lignes-i - int(surplus_etoiles/2)+int(nombre_lignes/2)) * " "
        pyramide += "/"
        if i > nombre_lignes - nbr_total_de_rang(nombre_lignes):
            if rang_porte(nombre_lignes) <= 3:
                pyramide += (i + int(surplus_etoiles / 2) - 1) * "*"
                pyramide += "|"
                pyramide += (p + int(surplus_etoiles / 2) - 0) * "*"

            if rang_porte(nombre_lignes) > 3 and rang_porte(nombre_lignes) < 25:
                pyramide += (i + int(surplus_etoiles / 2) - 2) * "*"
                pyramide += "|||"
                pyramide += (p + int(surplus_etoiles / 2) - 1) * "*"

            if rang_porte(nombre_lignes) >= 25:
                pyramide += (i + int(surplus_etoiles / 2) - nbr_total_de_rang(p) + int(round(nbr_total_de_rang(nombre_lignes) - 2)/2 - 0.1)) * "*"

                if round(nombre_lignes - nbr_total_de_rang(nombre_lignes) + nbr_total_de_rang(nombre_lignes)/2 + 0.1) == i:
                    pyramide += (nbr_total_de_rang(nombre_lignes) - 2) * "|"
                    pyramide += "$|"

                else:
                    pyramide += (nbr_total_de_rang(nombre_lignes))*"|"

                pyramide += (p + int(surplus_etoiles / 2) - 1 - int(round(nbr_total_de_rang(nombre_lignes) - 2)/2 - 0.1)) * "*"

        else:
            pyramide += (i + int(surplus_etoiles / 2)) * "*"
            pyramide += (p + int(surplus_etoiles / 2)) * "*"

        #pyramide += (p + int(surplus_etoiles/2)) * "*"y
        pyramide += "\\"
        pyramide += "\n"
        p += 1

        if i == li_niv[k]:
            #print(li)
            surplus_etoiles += li[k]+1
            m = 0
            for j in li:
                m += j
            m += li[k] + 1
            #print(m)
            li.insert(k+1, li[k]+1)
            li_niv.append(m)
            k += 1

    return pyramide

def main():
    print(arbre(rang_vers_ligne(sys.argv[1])))
    if arbre(rang_vers_ligne(sys.argv[1])) == None:
        print("Mauvaise entree, veuillez entrez un entier naturel different de zéro")

main()