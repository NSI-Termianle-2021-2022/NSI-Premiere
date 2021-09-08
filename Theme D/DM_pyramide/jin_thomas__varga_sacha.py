import sys
from math import *


def verification(valeur : str) -> bool: #verifit si la valeur entrée par l'utilisateur est valide
    try:
        int(float(valeur))
    except ValueError :
        print("la valeur entrée est incorrecte")
        return False
    if int(float(valeur)) <= 0:
        print("")
        return False
    if float(valeur)%1 != 0:
        print("la valeur entrée est incorrecte")
        return False
    return True
verification(sys.argv[1])

def last_floor(n : int) -> str: # Recupere le dernier etage de la pyramide pour pouvoir definir le nombre d'espace
    additional_floor = 0
    stars_increase = 1
    last_floor = ""
    for i in range(1, n+1):
        for k in range(0, 3+additional_floor):
            last_floor = ("/") + ("*"*stars_increase) + ("\\") + ("\n")
            stars_increase += 2
        additional_floor += 1
        if i < 3 :
            stars_increase += 4
        else :
            stars_increase += 6
    return last_floor

def spaces(n : int) -> int: # definit le nombre d'espace pour aligner la pyramide
    string_last_floor = str(last_floor(n))
    last_floor_length = len(string_last_floor)
    space = int(round(last_floor_length / 2, 0))
    return space

def pyramide(n : int) -> str: # Trace la pyramide
    space = spaces(n) - 2
    space_decrease = 0
    additional_floor = 0
    stars_increase = 1
    pyramid = ""
    for i in range(1, n):
        for k in range(0, 3+additional_floor):
            pyramid += (" "*(space-space_decrease)) + ("/") + ("*"*stars_increase) + ("\\") + ("\n")
            space_decrease += 1
            stars_increase += 2
        additional_floor += 1
        if i < 3 :
            stars_increase += 4
        else :
            space_decrease += 1
            stars_increase += 6
        space_decrease += 2
    if n == 2:
        for w in range(2):
            pyramid += (" " * (space - space_decrease)) + ("/") + ("*" * stars_increase) + ("\\") + ("\n")
            space_decrease += 1
            stars_increase += 2
        for i in range(n):
            n = 3
            calc = int(stars_increase - n)
            mid = int(calc / 2)
            pyramid += (" " * (space - space_decrease)) + ("/") + ("*" * mid) + ("|" * int(n)) + ("*" * mid) + ("\\") + (
                "\n")
            space_decrease += 1
            stars_increase += 2
    else:
        for w in range(2):
            pyramid += (" " * (space - space_decrease)) + ("/") + ("*" * stars_increase) + ("\\") + ("\n")
            space_decrease += 1
            stars_increase += 2
        for i in range(n):
            if n % 2 == 0:
                n = n-1
            calc = int(stars_increase - n)
            mid = int(calc/2)
            if n >= 5:
                if i == floor(n/2):
                    pyramid += (" " * (space - space_decrease)) + ("/") + ("*" * mid) + ("|" * int(n - 2)) + ("$") + ("|") + ("*" * mid) + ("\\") + ("\n")
                    space_decrease += 1
                    stars_increase += 2
                else:
                    pyramid += (" " * (space - space_decrease)) + ("/") + ("*" * mid) + ("|" * int(n)) + ("*" * mid) + ("\\") + ("\n")
                    space_decrease += 1
                    stars_increase += 2
            else:
                pyramid += (" " * (space - space_decrease)) + ("/") + ("*" * mid) + ("|" * int(n)) + ("*" * mid) + ("\\") + ("\n")
                space_decrease += 1
                stars_increase += 2
    return pyramid

print(pyramide(int(sys.argv[1])))

def tests():
    assert spaces(1) == 4
print(tests())

if len(sys.argv) == 1:
    print("Aucune valeur n'a été entrée")
else:
    pyramide(int(sys.argv[1]))


