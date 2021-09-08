total_sum = 0
for i in range(1000):
    if (i % 3 == 0 or i % 5 == 0 or i % 7 == 0):
        total_sum = total_sum + i
print(total_sum)

def est_multiple(n, l):
    for i in l:
        if n % i == 0:
            return True
    return False


def fibonacci(n):
    a = 1
    b = 1
    c = 0
    l = [a, b]
    for i in range(n-2):
        c = a+b
        a = b
        b = c
        l.append(c)
    return l
print(sum(fibonacci(20)))

def f_4m():
    a = 2
    b = 2
    c = 0
    while c < 4000000 and c %2 == 0:
        c = a+b
        a = b
        b = c
    return c

print((f_4m()))