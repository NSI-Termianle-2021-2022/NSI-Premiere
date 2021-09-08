import time
from random import randint

def main():
    values = set()
    for i in range(100000):
        values.add(calcul())
    return average(values)


def new_bd():
    return randint(1, 365)

def calcul():
    anniv = set()
    n_anniv = 1
    while True:
        anniv.add(new_bd())
        if n_anniv != len(anniv):
            return len(anniv)
        n_anniv += 1


def average(l):
    return sum(l) / len(l)

print(main())