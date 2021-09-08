from random import *
from tkinter import *

class Yams:
    def __init__(self, joueur):
        self.n_joueur = joueur
        self.q_joueur = 0
        self.score_list = []
        self.coups_joueur_list = []
        self.score_total = []
        self.coups = ['Total 1', 'Total 2', 'Total 3', 'Total 4', 'Total 5', 'Total 6', 'Brelan', 'Carre', 'Full', 'Petite suite', 'Grande suite', 'Yams', 'Chance']
        for i in range(joueur):
            self.score_list.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            self.coups_joueur_list.append([])
            self.score_total.append(0)
        self.coups_joueur = ""

    def partie(self):
        for i in range(13*self.n_joueur):
            print('Joueur {}:'.format(self.q_joueur+1))
            self.tirage()
            self.modifier()
            self.frepartition()
            self.verif()
            if self.deja_joue == False:
                self.score1()
                self.score2()
                self.score3()
            self.fscore_total()
            self.q_joueur += 1
            if self.q_joueur == self.n_joueur:
                self.q_joueur = 0
        for i in range(self.n_joueur):
            self.q_joueur = i
            self.fscore_total()
            print('Votre score final est: {} points'.format(self.var_score_total))

    def affichage(self):
        """self.fenetre = Tk()
        self.fenetre.title('Jeu du Yams')

        text = Label(self.fenetre, text= 'Vous avez fait:')
        text.place(relx =0.5, rely= 0.4, anchor = 'center')
        des = Label(self.fenetre, text=self.tirage_list)
        des.place(relx = 0.5, rely = 0.5, anchor = 'center')

        self.fenetre.mainloop()"""
        self.tirage_list.sort()
        print(self.tirage_list)

    def tirage(self):
        self.tirage_list = []
        for i in range(5):
            self.tirage_list.append(randint(1, 6))
        self.affichage()

    def modifier(self):
        for tour in range(2):
            fini = False
            while not fini:
                q_des = int(input('Combien de dés voulez-vous lancer?(0-5)'))
                if q_des<6 and q_des>-1:
                    for i in range(q_des):
                        fini_2 = False
                        while not fini_2:
                            m_des = int(input('Quel dé voulez-vous relancer?(1-5)'))
                            if m_des>0  and m_des<6:
                                self.tirage_list[m_des-1] = randint(1, 6)
                                self.affichage()
                                fini_2 = True
                            else:
                                print('Ce nombre de dés est inconnu')
                    fini = True
                else:
                    print('Ce nombre de dés est inconnu')

    def frepartition(self):
        self.repartition = []
        for i in range(1, 7):
            q_nombre = 0
            for j in self.tirage_list:
                if i == j:
                    q_nombre += 1
            self.repartition.append(q_nombre)

    """def figures(self):
        self.possibilites = []
        if self.tirage_list == [1, 2, 3, 4, 5]:
            self.possibilites.append('petite suite')
        if self.tirage_list == [2, 3, 4, 5, 6]:
            self.possibilites.append('grande suite')
        casseur_brelan, casseur_carre, pos_2 = False, False, False
        print(self.repartition)
        for i in self.repartition:
            if i == 5:
                self.possibilites.append('Yams')
            if i == 2:
                pos_2 = True
            if i == 3:
                if pos_2 == True:
                    self.possibilites.append('Full')
                if casseur_brelan == False:
                    self.possibilites.append('Brelan')
                    casseur_brelan = True
            if i == 4:
                if casseur_carre == False:
                    self.possibilites.append('Carre')
                    casseur_carre = True
        print(self.possibilites)"""

    def verif(self):
        print('Vous avez déjà joué: {}'.format(self.coups_joueur_list[self.q_joueur]))
        fini = False
        while not fini:
            print(self.coups)
            bonne_orthographe = False
            self.deja_joue = False
            self.coups_joueur = input('Que voulez-vous jouer?')
            for h in self.coups:
                if h == self.coups_joueur:
                    bonne_orthographe = True
            if bonne_orthographe == False:
                print("Coup inconnu (merci de respecter l'orthographe indiqué):")
            if bonne_orthographe == True:
                for i in self.coups_joueur_list[self.q_joueur]:
                    if self.coups_joueur == i:
                        self.deja_joue = True
                        print('Impossible, déja joué!')
                if self.deja_joue == False:
                    fini = True

    def score1(self):
        self.emplacement = self.coups.index(self.coups_joueur)
        possible = False
        self.full_possible = [False, False]
        if self.coups_joueur == 'Brelan':
            for j in self.repartition:
                if j == 3:
                    self.score_list[self.q_joueur][6] = 3*(self.repartition.index(3)+1)
                    possible = True
            if possible == False:
                    self.score_list[self.q_joueur][6] = 'X'
        elif self.coups_joueur == 'Carre':
            for j in self.repartition:
                if j == 4:
                    self.score_list[self.q_joueur][7] = 4*(self.repartition.index(4)+1)
                    possible = True
                if possible == False:
                    self.score_list[self.q_joueur][7] = 'X'



    def score2(self):
        if self.coups_joueur == 'Full':
            for j in self.repartition:
                if j == 2:
                    tot_full = 2 * (self.repartition.index(2) + 1)
                    self.full_possible[0] = True
                if j == 3:
                    tot_full = 3 * (self.repartition.index(3) + 1)
                    self.full_possible[1] = True
            self.score_list[self.q_joueur][8] = tot_full
            if self.full_possible[0] == False or self.full_possible[1] == False:
                self.score_list[self.q_joueur][8] = 'X'
        elif self.coups_joueur == 'Yams':
            for j in self.repartition:
                if j == 5:
                    self.score_list[self.q_joueur][11] = 5 * (self.repartition.index(5) + 1)
                    possible = True
                if possible == False:
                    self.score_list[self.q_joueur][11] = 'X'
        elif self.coups_joueur == 'Chance':
            for i in self.tirage_list:
                self.score_list[self.q_joueur][12] += i
        elif self.coups_joueur == 'Petite suite':
            if self.tirage_list == [1, 2, 3, 4, 5]:
                self.score_list[self.q_joueur][9] = 15
            else:
                self.score_list[self.q_joueur][9] = 'X'

    def score3(self):
        if self.coups_joueur == 'Grande suite':
            if self.tirage_list == [2, 3, 4, 5, 6]:
                self.score_list[self.q_joueur][10] = 20
            else:
                self.score_list[self.q_joueur][10] = 'X'

        elif self.coups_joueur[-1] == '1' or self.coups_joueur[-1] == '2' or self.coups_joueur[-1] == '3' or self.coups_joueur[-1] == '4' or self.coups_joueur[-1] == '5' or self.coups_joueur[-1] == '6':
                dernier = self.coups_joueur[-1]
                for i in range(1, 7):
                    if str(i) == dernier:
                        multiplicateur = self.repartition[i - 1]
                        self.score_list[self.q_joueur][int(self.coups_joueur[-1]) - 1] = multiplicateur * i
                        if self.score_list[self.q_joueur][int(self.coups_joueur[-1]) - 1] == 0:
                            self.score_list[self.q_joueur][int(self.coups_joueur[-1]) - 1] = 'X'

        self.coups_joueur_list[self.q_joueur].append(self.coups_joueur)

    def fscore_total(self):
        self.var_score_total = 0
        verif_63 = 0
        Bonus = False
        avancement_tab = 0
        for i in self.score_list[self.q_joueur]:
            avancement_tab += 1
            if i == 'X':
                None
            else:
                self.var_score_total += i
                if avancement_tab < 7 and Bonus == False:
                    verif_63 += i
                    if verif_63 > 63:
                        self.var_score_total += 35
                        Bonus = True
        print(self.score_list[self.q_joueur])
        print('Votre score est: {}'.format(self.var_score_total))



jeu = Yams(2)
jeu.partie()

