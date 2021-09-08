####################################################
## 7. Structures de contrôle : if, for, while
####################################################

# Exemple : on crée une simple variable
some_var = 5

# Voici une condition "si" (if). Attention, l'indentation est
# significative en Python!
if some_var > 10:
  print("some_var is totally bigger than 10.")
elif some_var < 10:    # La clause elif ("sinon si") est optionelle
  print("some_var is smaller than 10.")
else:                  # La clause else ("sinon") l'est aussi.
  print("some_var is indeed 10.")
# Affiche: "some_var is smaller than 10"


"""
Les boucles "for" itèrent sur une liste (= elles parcourent chaque
élément de la liste)
Par exemple, ce programme affichera :
  chien est un mammifère
  chat est un mammifère
  souris est un mammifère
"""
for animal in ["chien", "chat", "souris"]:
  print("{} est un mammifère".format(animal))

"""
"range(nombre)" retourne un itérable qui va de 0 au nombre donné
Par exemple, ce programme affichera :
  0
  1
  2
  3
"""
for i in range(4):
  print(i)

# Souvent on va itérer sur un range() :
age = int(input("Quel est ton âge ?"))
for i in range(age):
print("Joyeux anniversaire, tu as {} ans".format(i + 1))
# Ceci affichera tous les anniversaires, en commençant par 1
# Attention : range(4) retourne [0, 1, 2, 3] et a donc 4 valeurs.

"""
"range(debut, fin)" retourne un itérable qui va de debut à fin.
Par exemple, ce programme affichera :
  4
  5
  6
  7
"""
for i in range(4, 8):
  print(i)

"""
"range(debut, fin, pas)" retourne un itérable de nombres
de début à fin en incrémentant de pas.
Si le pas n'est pas indiqué, la valeur par défaut est 1.
Affiche:
  4
  6
  8
"""
for i in range(4, 8, 2):
  print(i)

"""

Les boucles "while" bouclent jusqu'à ce que la condition devienne fausse.
Affiche:
  0
  1
  2
  3
"""
x = 0
while x < 4:
  print(x)
  x += 1  # Raccourci pour x = x + 1


####################################################
## 8. Listes
####################################################

# Les listes permettent de stocker des séquences
li = []
# On peut initialiser une liste pré-remplie
other_li = [4, 5, 6]

# On ajoute des objets à la fin d'une liste avec .append
li.append(1)    # li vaut maintenant [1]
li.append(2)    # li vaut maintenant [1, 2]
li.append(4)    # li vaut maintenant [1, 2, 4]
li.append(3)    # li vaut maintenant [1, 2, 4, 3]
# On enlève le dernier élément avec .pop
li.pop()        # => 3 et li vaut maintenant [1, 2, 4]
# Et on le remet
li.append(3)    # li vaut de nouveau [1, 2, 4, 3]

# L'accès à un élément d'une liste commence à 0
li[0]  # => 1
# Accès au dernier élément :
li[-1]  # => 3

# Accéder à un élément en dehors des limites soulève une IndexError
li[4]  # Lève une IndexError

# On peut accéder à une intervalle avec la syntaxe [a:b] ("slice")
li[1:3]  # => [2, 4]
# Pour omettre les deux premiers éléments
li[2:]  # => [4, 3]
# Pour prendre les trois premiers
li[:3]  # => [1, 2, 4]
# Pour sélectionner un élément sur deux
li[::2]   # =>[1, 4]
# Pour avoir une copie de la liste à l'envers
li[::-1]   # => [3, 4, 2, 1]

# Enlever des éléments arbitrairement d'une liste
del li[2]   # li is now [1, 2, 3]

# On peut additionner des listes
# Note: les valeurs de li et other_li ne sont pas modifiées.
li + other_li   # => [1, 2, 3, 4, 5, 6]

# Concaténer des listes avec "extend()"
li.extend(other_li)   # Maintenant li contient [1, 2, 3, 4, 5, 6]

# Vérifier la présence d'un objet dans une liste avec "in"
1 in li   # => True

# Examiner la longueur d'une liste avec "len()"
len(li)   # => 6


####################################################
## 9. Dictionnaires
####################################################

# Un dictionnaire est une structure de données qui associe une clé
# à une valeur.
# La valeur peut être ce que l'on veut : nombres, chaînes de caractères,
# ou même un autre dictionnaire.
# Dans la cas d'un vrai dictionnaire papier, la clé sera le mot cherché,
# et la valeur sera la définition donnée par le dictionnaire.

# On crée un dictionnaire avec {} :
empty_dict = {}

# On peut déclarer un dictionnaire pré-rempli :
filled_dict = {"one": 1, "two": 2, "three": 3}

# Note : les clés des dictionnaires doivent être de types immuables.
# Les types immuables incluent les ints, floats, strings et tuples.
invalid_dict = {[1,2,3]: "123"} # => Lève une TypeError: unhashable type: 'list'
valid_dict = {(1,2,3):[1,2,3]}  # Par contre, les valeurs peuvent être de tout type.

# On accède à une valeur avec []
filled_dict["one"]   # => 1

# L'accès à une clé non-existente lève une KeyError
filled_dict["four"]   # KeyError

# On vérifie la présence d'une clé dans un dictionnaire avec "in"
"one" in filled_dict   # => True
1 in filled_dict   # => False

# Ajouter un couple clé/valeur à un dictionnaire :
filled_dict.update({"four":4}) #=> {"one": 1, "two": 2, "three": 3, "four": 4}
#filled_dict["four"] = 4  # une autre méthode

# Enlever des clés d'un dictionnaire avec del
del filled_dict["one"]  # Enlever la clé "one" de filled_dict.

# On obtient toutes les clés avec "keys()" Il faut l'entourer
# de list() pour avoir une liste. Note: l'ordre des clés n'est pas garanti.
list(filled_dict.keys())   # => ["three", "two", "one"]

# On obtient toutes les valeurs sous forme d'un itérable avec "values()".
# Là aussi, il faut utiliser list() pour avoir une liste.
# Note : l'ordre n'est toujours pas garanti.
list(filled_dict.values())   # => [3, 2, 1]


####################################################
## 10. Fonctions
####################################################

# Une fonction est un bloc de code nommé et réutilisable.

# Les fonctions permettent de décomposer un programme complexe en une série de sous-programmes plus simples.

# La notion de fonction en informatique est comparable à la notion
# de fonction en mathématique.

# Toute fonction a un nom et un prototype, défini par les variables
# qu'elle prend.

# Ex : def ajout_nombres(a, b):
# Ex : def conversion_binaire(nombre):

# Une fonction peut aussi ne prendre aucune variable :
# def quelle_heure_est_il():

# On utilise le mot-clé "def" pour créer des fonctions
def add(x, y):
  print("x vaut {} et y vaut {}".format(x, y))
  return x + y    # On retourne une valeur avec return

# Pour appeler une fonction avec des paramètres, on utilise () :
add(5, 6)   # => affiche "x vaut 5 et y vaut 6" et retourne 11

# Portée des fonctions :
x = 5

def setX(num):
  # La variable locale x n'est pas la même que la variable globale x
  x = num # => 43
  print (x) # => 43

def setGlobalX(num):
  global x
  print (x) # => 5
  x = num # la variable globale x est maintenant 6
  print (x) # => 6

setX(43)
setGlobalX(6)

####################################################
## 11. Modules
####################################################

# On peut importer des modules
import math
print(math.sqrt(16))  # => 4.0

# On peut importer des fonctions spécifiques d'un module
from math import ceil, floor
print(ceil(3.7))  # => 4.0
print(floor(3.7))   # => 3.0

# On peut importer toutes les fonctions d'un module
# Attention: ce n'est pas recommandé.
from math import *

# On peut raccourcir un nom de module
import math as m
math.sqrt(16) == m.sqrt(16)   # => True

# Les modules Python sont juste des fichiers Python.
# Vous pouvez écrire les vôtres et les importer. Le nom du module
# est le nom du fichier.

# On peut voir quels fonctions et objets un module définit avec dir() :
import math
dir(math)
