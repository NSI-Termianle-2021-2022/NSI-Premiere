import sys


def taille_pyramide (nb_etage :int) -> int :

    taille = 3*nb_etage + nb_etage*(nb_etage-1) / 2

    return taille

def test_taille_pyramide():
    assert taille_pyramide(5) == 25
    assert taille_pyramide(0) == 0


def espace(nb_etage :int, ligne: int, etage : int, taille : int) -> str :

    res = ""

    nb_espace = taille-ligne+ 2*(nb_etage-etage-1)

    for i in range(0,int(nb_espace)-1) :

        res+= " "

    return res



def print_ligne(etoile : int, etage:int,nb_etage:int,ligne:int ) -> list:

    taille = taille_pyramide(nb_etage)

    res = espace(nb_etage,ligne,etage,taille)

    res+="/"

    for k in range(0,etoile):

        res += '*'

    res += '\ \n'

    ligne += 1

    etoile += 2

    print(res, end='')

    return [etoile,ligne]



def print_dernieres_lignes(etoile : int, etage:int,nb_etage:int,ligne:int ) -> list:

    if etoile % 2 == 1 :

        borneInf = (etoile/2) - 1.5

        borneSup = borneInf + 2

    else :

        borneInf = (etoile/2) - 1

        borneSup = borneInf + 2



    taille = taille_pyramide(nb_etage)

    res = espace(nb_etage,ligne,etage,taille)

    res+="/"

    for k in range(0,etoile):

        if (k >= borneInf and k <= borneSup) :

            res += '|'

        else :

            res+= '*'

    res += '\ \n'

    ligne += 1

    etoile += 2

    print(res, end='')

    return [etoile,ligne]



def print_etages(etoile : int, etage:int,nb_etage:int,ligne:int )->list:

    for j in range(0,3+etage):

        [etoile,ligne] = print_ligne(etoile,etage,nb_etage,ligne)

    etoile += 4

    return [etoile,ligne]





def print_dernier_etage(etoile : int, etage:int,nb_etage:int,ligne:int )->list:

    for j in range(0,3+etage):

        if j <= 1 :

            [etoile,ligne] = print_ligne(etoile,etage,nb_etage,ligne)

        else :

            [etoile,ligne] = print_dernieres_lignes(etoile,etage,nb_etage,ligne)

    return [etoile,ligne]



def pyramide() -> None :

    nb_etage = int(sys.argv[1])

    etoile = 1

    ligne = 0
    for etage in range(0,nb_etage):
        #Si on est au dernier étage avec porte
        if (etage == nb_etage-1) :
            [etoile,ligne] = print_dernier_etage(etoile,etage,nb_etage,ligne)
        #Sinon etage normal sans porte
        else :
            [etoile,ligne] = print_etages(etoile,etage,nb_etage,ligne)






pyramide()
