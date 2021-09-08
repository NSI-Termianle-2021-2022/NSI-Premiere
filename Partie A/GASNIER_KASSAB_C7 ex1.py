def fibonacci(n):
    last1= 1
    last2 =1
    print(1)
    print(1)
    for i in range(n-2):
        fnew = last2 + last1
        last1 = last2
        last2 = fnew
        print(fnew)



def fibonacci_somme(n):
    last1 = 1
    last2 = 1
    print(1)
    print(1)
    somme = 0
    for i in range(n-2):
        fnew = last2 + last1
        last1 = last2
        last2 = fnew
        somme += fnew
        print(fnew)
    return somme

print(fibonacci_somme(20))