#####################################################
# Séance #53 - Algorithmes gloutons I - 11/05/2021  #
#####################################################

"""
Cette séance aborde le problème bien connu du rendu de monnaie : comment rendre
la monnaie en utilisant le moins de pièces/billets possibles ?

On suppose que :
    - il y a une infinité de pièces de monnaie de chaque catégorie dans le
      tiroir-caisse,
    - il est équivalent de rendre une pièce ou un billet,
    - le tuple des pièces/billets est trié en ordre croissant,
    - l'unité utilisée partout est le centime (ce qui évite de travailler avec
      des floats).

Note : on passera un tuple de pièces (et non une liste) pour s'assurer que la
variable "pieces" passée en argument ne sera pas modifiée.
"""


def trouve_piece(pieces: tuple[int], montant: int) -> int:
    longueur = len(pieces)
    for i in range(longueur):
        if montant >= pieces[i] and (i == longueur - 1 or montant < pieces[i + 1]):
            return pieces[i]
    return 0 # aucune pièce n'a été trouvée


def rendu_monnaie(montant: int, apport: int, pieces: tuple[int]) -> list[int]:
    if apport < montant:
        return [-1]

    a_rendre = apport - montant
    rendu = []

    while sum(rendu) < a_rendre:
        piece = trouve_piece(pieces, a_rendre - sum(rendu))
        if piece == 0:
            return [-1]  # ceci évite les boucles infinies !
        rendu.append(piece)

    return rendu


"""
1. L'algorithme vous semble-t-il optimal avec les pièces standard de l'euro ?

2. Trouvez une situation pour lequel cet algorithme n'est pas optimal. Vous
pouvez utiliser le jeu de pièces n'est pas optimal.
"""

#############################################
#          TESTS RENDU DE MONNAIE           #
#############################################

# On teste d'abord les erreurs...
assert rendu_monnaie(5, 2, (1,)) == [-1]  # Il n'y a pas assez d'argent
assert rendu_monnaie(2, 7, (6,)) == [-1]  # Aucune combinaison ne fonctionne

# Que des pièces d'1 ct
assert len(rendu_monnaie(2632, 5000, (1,))) == 2368
# Que des pièces d'1 ou 2 cts
assert len(rendu_monnaie(2632, 5000, (1, 2))) == 1184
# Que des pièces d'1, 2 ou 5 cts. Etc.
assert len(rendu_monnaie(2632, 5000, (1, 2, 5))) == 475
assert len(rendu_monnaie(2632, 5000, (1, 2, 5, 10))) == 239
assert len(rendu_monnaie(2632, 5000, (1, 2, 5, 10, 20))) == 121
assert len(rendu_monnaie(2632, 5000, (1, 2, 5, 10, 20, 50))) == 51
assert len(rendu_monnaie(2632, 5000, (1, 2, 5, 10, 20, 50, 100))) == 28

assert rendu_monnaie(187, 200, (1, 2)) == [2, 2, 2, 2, 2, 2, 1]
assert rendu_monnaie(2632, 3000, (1, 2, 5, 10, 20, 50, 100, 200)) == [200, 100, 50, 10, 5, 2, 1]
assert rendu_monnaie(2632, 3000, (1, 2, 5, 10, 20, 50, 100)) == [100, 100, 100, 50, 10, 5, 2, 1]
assert rendu_monnaie(2632, 3000, (1, 2, 5, 10, 20, 50)) == [50, 50, 50, 50, 50, 50, 50, 10, 5, 2, 1]
assert rendu_monnaie(2632, 3000, (1, 2, 5, 10, 20)) == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 5, 2, 1]

assert rendu_monnaie(63, 100, (1, 2, 5, 10, 20, 50, 100, 200)) == [20, 10, 5, 2]

"""
1. L'algo semble optimal avec le découpage classique des pièces utilisé pour
l'Euro : la meilleure solution est donc bien : TOUJOURS RENDRE LA PLUS GRANDE
PIÈCE POSSIBLE.

2. En revanche, avec un jeu de pièces étrange, cette solution n'est pas
optimale. Ainsi, avec 1, 3 et 4 cents :
"""
assert rendu_monnaie(4, 10, (1, 3, 4)) == [4, 1, 1]  # solution plus longue que [3, 3] !


# Problème du sac à dos
########################

# Pour cette partie, voir https://pixees.fr/informatiquelycee/n_site/nsi_prem_glouton_algo.html
