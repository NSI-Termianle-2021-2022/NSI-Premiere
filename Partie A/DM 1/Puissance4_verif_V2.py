def verif_V2(grille, joueur, colonne, symboles, ligne):

    suite_horizontale = 0
    horizontale = []
    for i in grille:
        for j in i:
            horizontale.append(j)
            if j == symboles[joueur]:
                suite_horizontale += 1
                if suite_horizontale > 3:
                    return 4
            else:
                suite_horizontale = 0


    suite_vertical = 0
    for i in range(len(grille)):
        if grille[i][colonne] == symboles[joueur]:
            suite_vertical += 1
            if suite_vertical > 3:
                return True
        else:
            suite_vertical = 0



    x = colonne+1
    y = ligne-1
    diagonale_hd_bg = [symboles[joueur]]
    while y > -1 and x < len(grille[0]):
        diagonale_hd_bg.append(grille[y][x])
        y -= 1
        x += 1

    diagonale_hd_bg.reverse()

    x = colonne-1
    y = ligne+1
    while y < len(grille) and x > -1:
        diagonale_hd_bg.append(grille[y][x])
        y += 1
        x -= 1

    suite_diagonale = 0
    for i in diagonale_hd_bg:
        if i == symboles[joueur]:
            suite_diagonale += 1
            if suite_diagonale > 3:
                return True
        else:
            suite_diagonale = 0


    x = colonne-1
    y = ligne-1
    diagonale_hg_bd = [symboles[joueur]]
    while y > -1 and x > -1:
        diagonale_hg_bd.append(grille[y][x])
        y -= 1
        x -= 1

    diagonale_hg_bd.reverse()
    x = colonne+1
    y = ligne+1
    while y < len(grille) and x < len(grille[0]):
        diagonale_hg_bd.append(grille[y][x])
        y += 1
        x += 1
    suite_diagonale = 0
    for i in diagonale_hg_bd:
        if i == symboles[joueur]:
            suite_diagonale += 1
            if suite_diagonale > 3:
                return True
        else:
            suite_diagonale = 0
