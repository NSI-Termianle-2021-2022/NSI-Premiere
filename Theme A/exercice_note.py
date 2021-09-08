a = int(input('Quelle est ta note ? '))
b = a%2

if b >0:
    print('impaire')
else:
    print('paire')

if a < 5:
    print('nul')
elif a < 10:
    print('pas terrible...')
elif a < 15:
    print('moyen')
elif a < 20:
    print('Bien')
else:
    print('impossible')