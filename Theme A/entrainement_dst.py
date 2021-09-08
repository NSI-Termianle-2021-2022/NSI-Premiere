from C5_ex1 import*


def fibonacci(n):
    n1 = 1
    n2 = 1
    print(n1)
    print(n2)
    for i in range(n-2):
        n3 = n1 + n2
        print(n3)
        n2 = n1
        n1 = n3

def fizz_buzz(x):
    if x%3 == 0 == x%5:
        print('{} est multiple de 3 et 5'.format(x))
    elif x%3 == 0:
        print('{} est multiple de 3'.format(x))
    elif x%5 == 0:
        print('{} est multiple de 5'.format(x))

my_grade(10, 5, 1)