##############################################
# Séance #48 - Préparation DM - 08/04/2021  #
##############################################

# Introduction
###############

# Balade sur le site https://aava.sh...

# Utilisation du module sys pour la lecture de paramètres
##########################################################

"""
Le module sys permet d'accéder aux paramètres que l'on "passe" au programme.

On donne des paramètres au programme en les écrivant à la suite après le nom du
fichier :

> python mon_fichier.py  123   "ab"  2.4

On les récupère ensuite via sys.argv, qui contient la liste des paramètres.

Deux remarques :
  - sys.argv[0] contient le nom du programme lui-même, donc les arguments
    eux-mêmes commencent à l'indice 1
  - tous les paramètres sont des strings, qu'il faudra éventuellement
    convertir !
"""
import sys

if len(sys.argv) > 3:
    print(type(sys.argv))      # => <class 'list'>
    print(len(sys.argv))       # => 4
    print(sys.argv[0])         # => 'cpy_13_modules.py'
    print(int(sys.argv[1]))    # => 123
    print(sys.argv[2])         # => 'ab'
    print(float(sys.argv[3]))  # => 2.4


# Précaution utile en début de programme : ce morceau de code...
if len(sys.argv) > 3:
    print("...")
# ...permet d'éviter d'accéder aux éléments d'une liste qui n'existent pas,
# comme sys.argv[2]!

# L'annotation de type (type hint)
###################################

"""
L'annotation de type ("type hint") consiste à indiquer dans une fonction :
  - le type de valeurs accepté en paramètres
  - le type de valeurs retourné par la fonction

Ceci aide ensuite pour la lecture du programme à savoir comment se comportera
la fonction.

On utilise ":" pour les paramètres, et "->" pour la valeur de retour.

Ainsi, cette fonction indique très clairement qu'elle ne retourne rien :
"""
def print_bidule(parametre) -> None:
    print(parametre)

# Inversement, cette fonction de comparaison retourne toujours un booléen :
def comparer_listes(a, b):
    return len(a) > len(b)

print(comparer_listes([2], [3, 7]))
print(comparer_listes([2, 5, 8], [3, 7]))

"""
Avec le type hinting, on le précise dans sa définition pour plus de clarté.
Cela donnera :
"""
def comparer_listes_th(a: list, b: list) -> bool:
    return len(a) > len(b)

print(comparer_listes_th([2], [3, 7]))
print(comparer_listes_th([2, 5, 8], [3, 7]))


"""
Si les valeurs de la liste sont toutes de même nature, on peut même le dire
dans l'annotation avec la syntaxe list[type]

Ainsi cette fonction est censée ne prendre que des listes d'entiers
"""
def comparer_listes_th_2(a: list[int], b: list[int]) -> bool:
    return len(a) > len(b)

print(comparer_listes_th_2([2], [3, 7]))
print(comparer_listes_th_2([2, 5, 8], [3, 7]))

# On note qu'il n'y aura pas d'erreurs si on lui passe autre chose : il s'agit
# juste d'une indication d'utilisation.
print(comparer_listes_th_2([2.1, 5.42, 8.89], [3.1, 7.9]))


"""
Les types utilisables sont :
   - None (si on ne retourne rien)
   - int
   - float
   - str
   - bool
   - list
   - list[bool] (pour une liste ne contenant que des booléesn)
"""


