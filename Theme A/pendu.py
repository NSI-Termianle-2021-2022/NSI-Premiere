from random import *

mode = input('Mode 2 joueurs? (o/n): ')
value = []
value_l = []

if mode == "n":
    print('mode 1 joueur')
    bank = ["rouge", "vert", "manger", "destruction", "deforestation", "sphynx"]
    mot = randint(0, len(bank)-1)
    mot = bank[mot]

elif mode == "o":
    print("mode 2 joueurs")
    mot = input('Quel mot? ')
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")





visu = []
for i in range(len(mot)):
    visu.append('_')





n_lettre = len(mot)
print("Ce mot contient {} de lettres".format(n_lettre))
erreur = 1
faux_1 = str("""
 +---+
     |
     |
     |
    ===
""")

faux_2 = str("""
 +---+
 O   |
     |
     |
    ===
""")

faux_3 = str("""
 +---+
 O   |
 |   |
     |
    ===
""")

faux_4 = str("""
 +---+
 O   |
-|   |
     |
    ===
""")

faux_5 = str("""
 +---+
 O   |
-|-  |
     |
    ===
""")

faux_6 = str("""
 +---+
 O   |
-|-  |
/    |
    ===
""")

faux_7 = str("""
 +---+
 O   |
-|-  |
/ }  |
    ===
""")

while erreur < 8:
    affiche = ""
    for i in visu:
        affiche += i
    print(affiche)
    prop = input('proposition:')

    if len(prop) > 1:
        for i in value:
            if i == prop:
                print('Deja proposé!')
            else:
                value.append(prop)
                if mot == prop:
                    print("C'est gagné !")
                    break
                else:
                    print('faux')
                    if erreur == 1:
                        print(faux_1)
                        print('plus que {} essais'.format(7 - erreur))
                        erreur += 1
                    elif erreur == 2:
                        print(faux_2)
                        print('plus que {} essais'.format(7 - erreur))
                        erreur += 1
                    elif erreur == 3:
                        print(faux_3)
                        print('plus que {} essais'.format(7 - erreur))
                        erreur += 1
                    elif erreur == 4:
                        print(faux_4)
                        print('plus que {} essais'.format(7 - erreur))
                        erreur += 1
                    elif erreur == 5:
                        print(faux_5)
                        print('plus que {} essais'.format(7 - erreur))
                        erreur += 1
                    elif erreur == 6:
                        print(faux_6)
                        print('plus que {} essais'.format(7 - erreur))
                        erreur += 1
                    elif erreur == 7:
                        print(faux_7)
                        print('Perdu')
                        break
    if len(prop) == 1:
        position = []
        n_fois = 0
        list_mot = []
        for i in mot:
            list_mot.append(i)
            if i == prop:
                position.append(len(list_mot)-1)
                n_fois += 1
        if n_fois == 0:
            print('faux')
            if erreur == 1:
                print(faux_1)
                print('plus que {} essais'.format(7 - erreur))
                erreur += 1
            elif erreur == 2:
                print(faux_2)
                print('plus que {} essais'.format(7 - erreur))
                erreur += 1
            elif erreur == 3:
                print(faux_3)
                print('plus que {} essais'.format(7 - erreur))
                erreur += 1
            elif erreur == 4:
                print(faux_4)
                print('plus que {} essais'.format(7 - erreur))
                erreur += 1
            elif erreur == 5:
                print(faux_5)
                print('plus que {} essais'.format(7 - erreur))
                erreur += 1
            elif erreur == 6:
                print(faux_6)
                print('plus que {} essais'.format(7 - erreur))
                erreur += 1
            elif erreur == 7:
                print(faux_7)
                print('Perdu')
                break
        if n_fois > 0:
            print('Ce mot comprend {} lettres'.format(n_lettre))
            print('Il y a {} fois la lettre {} en position {}'.format(n_fois, prop, position))
            for i in position:
                visu[i] = prop
