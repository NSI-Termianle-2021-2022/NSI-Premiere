import sys

message = str(sys.argv[1])

def ligne_1(message):
    retour = ' '
    for i in range(len(message)+2):
        retour += "_"
    return retour

print(ligne_1(message))

def ligne_2(message):
    retour = '< ' + message + ' >'
    return retour

def ligne_3(message):
    retour = ' '
    for i in range(len(message)+2):
        retour += "-"
    return retour

print(ligne_1(message)\n )
print(ligne_2(message))
print(ligne_3(message))
print('        \   ^__^')
print('         \  (oo)\_______')
print("            (__)\       )\/\\")
print("                ||----w |")
print("                ||     ||")