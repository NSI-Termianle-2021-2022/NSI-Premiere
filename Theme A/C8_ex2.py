def C8_ex0(li):
    somme = 0
    for i in range(len(li)):
        somme += li[i]

    return print(somme)

li = [2, 3, 5, 8]
C8_ex0(li)

def C8_ex1(li):
    produit = 1
    for i in range(len(li)):
        produit = produit*li[i]
    print(produit)

C8_ex1(li)

def C8_ex2(li):
    plus_grand_nombre = 0
    for i in range(len(li)):
        if li[i] > plus_grand_nombre:
            plus_grand_nombre = li[i]
    print(plus_grand_nombre)

C8_ex2(li)


def C8_ex3(li):
    plus_petit_nombre = li[1]
    for i in range(len(li)):
        if li[i] < plus_petit_nombre:
            plus_petit_nombre = li[i]
    print(plus_petit_nombre)

C8_ex3(li)

def C8_ex4(li):
    somme = 0
    for i in li:
        if i%2 == 0:
            somme += i
    print(somme)

C8_ex4(li)

def C8_ex5(li):
    nombre = int(input('Quel nombre?'))
    for i in li:
        if i == nombre:
            print('Ce nombre est présent')

C8_ex5(li)