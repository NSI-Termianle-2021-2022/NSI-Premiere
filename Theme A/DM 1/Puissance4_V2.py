from Puissance4_affichage_V2 import affichage_V2
from Puissance4_verif_V2 import verif_V2

grille = [["", "", "", "", "", "", ""],
          ["", "", "", "", "", "", ""],
          ["", "", "", "", "", "", ""],
          ["", "", "", "", "", "", ""],
          ["", "", "", "", "", "", ""],
          ["", "", "", "", "", "", ""]]

affichage_V2(grille)

joueur = 0
symboles = ['X', 'O']

while True:

    rempli = False
    while rempli == False:
        colonne = int(input('Joueur {} : Quelle colonne?'.format(symboles[joueur]))) - 1


        if colonne < 0 or colonne > 7:
            print('Emplacement impossible')
            affichage_V2(grille)
        elif grille[0][colonne] == symboles[0] or grille[0][colonne] == symboles[1]:
            print('Emplacement impossible')
            affichage_V2(grille)
        else:
            for i in reversed(range(len(grille))):
                if rempli == True:
                    a = 0
                elif grille[i][colonne] == "":
                    ligne = i
                    grille[i][colonne] = symboles[joueur]
                    rempli = True
                    affichage_V2(grille)

    victoire = verif_V2(grille, joueur, colonne, symboles, ligne)
    if victoire == True:
        print('Joueur {} gagne!'.format(symboles[joueur]))
        break
    else:
        joueur += 1
        if joueur == 2:
            joueur = 0

    tab_plein = []
    for i in grille[0]:
        if i == symboles[0] or i == symboles[1]:
            tab_plein.append(i)
            if len(tab_plein) == len(grille[0]):
                print('Match nul !')
                break