q1 = int(input('Quel est ton age? '))

if q1 < 10:
    print('Tu est un enfant')
elif q1 < 18:
    print('tu ne peux pas voter')
elif q1 < 25:
    print('Tu est jeune')
elif q1 < 50:
    print('Tu est dans la vie active')
elif q1 < 65:
    print('Tu déclines')
elif q1 < 80:
    print('On atteint la fin de l"espérence de vie')
elif q1 < 125:
    print('Bientot la fin')
else:
    print('Encore en vie?')



q2 = input('Dans quelle ville est-tu né?')

if q2 == 'Paris':
    print('La capitale')
elif q2 == 'Marseille':
    print('Ville poubelle')
elif q2 == 'Lyon':
    print('OK')
elif q2 == 'Bordeaux':
    print('Le pays de la chocolatine')
elif q2 == 'Lille':
    print('Rien de bon')
else:
    print('Trou paumé')

q3 = float(input('Quelle est ta taille?'))

if q3 < 1.6:
    print('nain')
elif q3 < 1.7:
    print('petit non?')
elif q3 < 1.75:
    print('juste en dessous de la moyenne')
elif q3 < 1.8:
    print('dans la moyenne')
elif q3 < 1.90:
    print('dans la moyenne supérieure')
else:
    print('Tu est grand')
