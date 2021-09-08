def affichage_V2(grille):
    affichage_propre1 = "|"
    affichage_propre2 = "|"
    affichage_propre3 = "|"
    affichage_propre4 = "|"
    affichage_propre5 = "|"
    affichage_propre6 = "|"


    for i in grille:
        for j in i:
            if j == '':
                if len(affichage_propre1) < 15:
                    affichage_propre1 += ' '
                    affichage_propre1 += '|'
                elif len(affichage_propre2) < 15:
                    affichage_propre2 += ' '
                    affichage_propre2 += '|'
                elif len(affichage_propre3) < 15:
                    affichage_propre3 += ' '
                    affichage_propre3 += '|'
                elif len(affichage_propre4) < 15:
                    affichage_propre4 += ' '
                    affichage_propre4 += '|'
                elif len(affichage_propre5) < 15:
                    affichage_propre5 += ' '
                    affichage_propre5 += '|'
                elif len(affichage_propre6) < 15:
                    affichage_propre6 += ' '
                    affichage_propre6 += '|'
            else:
                if len(affichage_propre1) < 15:
                    affichage_propre1 += j
                    affichage_propre1 += '|'
                elif len(affichage_propre2) < 15:
                    affichage_propre2 += j
                    affichage_propre2 += '|'
                elif len(affichage_propre3) < 15:
                    affichage_propre3 += j
                    affichage_propre3 += '|'
                elif len(affichage_propre4) < 15:
                    affichage_propre4 += j
                    affichage_propre4 += '|'
                elif len(affichage_propre5) < 15:
                    affichage_propre5 += j
                    affichage_propre5 += '|'
                elif len(affichage_propre6) < 15:
                    affichage_propre6 += j
                    affichage_propre6 += '|'

    print(' 1 2 3 4 5 6 7')
    print(affichage_propre1)
    print(affichage_propre2)
    print(affichage_propre3)
    print(affichage_propre4)
    print(affichage_propre5)
    print(affichage_propre6)
