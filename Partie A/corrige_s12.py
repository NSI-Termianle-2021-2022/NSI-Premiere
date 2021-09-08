###########################################
# Séance #12 - Le pendu - 13/10/2020      #
###########################################

# Ex0 : écrire une fonction my_pop qui :
#    - prend un dictionnaire en paramètre
#    - reproduit exactement le comportement de la méthode .pop() du dictionnaire.

# Vous devrez vous créer un jeu de tests pour vous assurer que les deux fonctionnent de la même façon.

# Indice :
#    - Vous devez créer des erreurs de la même façon que la méthode .pop()
#      du dictionnaire !
#raise IndexError("Crée une erreur et affiche ce texte")  # => IndexError: Crée une erreur et affiche ce texte

# Ex1 : faire un jeu du pendu avec les strings suivantes :

print("""
 +---+
     |
     |
     |
    ===
""")

"""
 +---+
 O   |
     |
     |
    ===
"""

"""
 +---+
 O   |
 |   |
     |
    ===
"""

"""
 +---+
 O   |
-|   |
     |
    ===
"""


"""
 +---+
 O   |
-|-  |
     |
    ===
"""

"""
 +---+
 O   |
-|-  |
/    |
    ===
"""

"""
 +---+
 O   |
-|-  |
/ }  |
    ===
"""
