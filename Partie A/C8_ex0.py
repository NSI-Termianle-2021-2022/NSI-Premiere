def fizz_buzz(n):
    for i in range(n):
        if i%7 == i%5 == 0:
            print('{} est multiple de 7 et 5'.format(i))
        elif i%7 == 0:
            print('{} est multiple de 3'.format(i))
        elif i%5 ==0 :
            print('{} est multiple de 5'.format(i))
        else:
            print("{} n'est multiple de rien".format(i))



#fizz_buzz(100)

def fibonacci(n):
    n1 = 1
    n2 = 1
    print(n1)
    print(n2)
    for i in range(n-2):
        n3 = n2 + n1
        n2 = n1
        n1 = n3
        print(n3)

fibonacci(20)

