li = ['ab', 'a', 'abc', 'abcd', 'azertyuiop']
li1 =[]
li2 = [1,2,3,4,5,6,8,9,20, 3]
li3 = [1,2,3,4,5,6,8,9,20, 3]
li4 = [500]

def plus_que_2(lif):
    b = 0
    for i in lif:
        if len(i) > 2:
            b += 1
    if b > 0:
        return True
    else:
        return False

result1 = plus_que_2(li)
print(result1)

def moins_que_5(lif):
    b = 0
    for i in lif:
        if len(i) < 5:
            b += 1
    if b > 0:
        return True
    else:
        return False

result2 = moins_que_5(li)
print(result2)

def liste_vide(lif):
    if len(lif) == 0:
        return True
    else:
        return False

result3 = liste_vide(li)
print(result3)

def croissant(lif):
    print(sorted(lif))

croissant(li2)

def decroissant(lif):
    lif.sort()
    lif.reverse()
    print(lif)

decroissant(li2)

def commun(lif, lif2):
    for i in lif:
        for j in lif2:
            if i == j:
                return True
            else:
                return False

result = commun(li2, li4)
print(result)

def fibonacci(n):
    n1 = 1
    n2 = 1
    print(n1)
    print(n2)
    for i in range(n-2):
        n3 = n1 + n2
        n2 = n1
        n1 = n3
        print(n3)

fibonacci(20)

def fizz_buzz(x):
    if x%3 == x%5 == 0:
        print('{} est divisible par 3 et 5'.format(x))
    elif x%3 == 0:
        print('{} est divisible par 3'.format(x))
    elif x%5 == 0:
        print('{} est divisible par 5'.format(x))
    else:
        print("n'est dividible ni par 3, ni par 5".format(x))

fizz_buzz(30)