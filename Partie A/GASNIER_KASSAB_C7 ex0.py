def fizz_buzz(x):
    a = 0
    for i in range(1,x):
            if i %3 == 0 or i%5 == 0:
                a += i
    return a

print(fizz_buzz(1000))